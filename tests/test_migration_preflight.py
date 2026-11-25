"""Regression tests for read-only ARC Robo v2 migration preflight."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from migration_preflight import audit, local_plan_inventory


class MigrationPreflightTests(unittest.TestCase):
    def test_existing_inventory_is_valid_but_not_migrated(self):
        result = audit(ROOT)
        self.assertEqual(result["inventory_status"], "PASS", result["findings"])
        self.assertEqual(result["migration_status"], "BLOCKED")
        self.assertFalse(result["migration_ready"])
        self.assertEqual(result["record_count"], 31)
        self.assertEqual(result["local_plan_count"], 32)
        self.assertEqual(result["local_only_plan_count"], 1)
        self.assertEqual(result["pinned_source_count"], 31)
        self.assertEqual(result["external_reference_count"], 0)
        self.assertEqual(sum(result["research_lines"].values()), 31)
        self.assertIn("canonical_owner_for_each_msc", result["unresolved_decisions"])

    def test_missing_source_does_not_pass(self):
        original = json.loads((ROOT / "manuscripts/source_manifest.json").read_text())
        original["papers"][0]["source_commit_sha"] = "unverified"
        with patch("migration_preflight.json.loads", side_effect=[
            original,
            json.loads((ROOT / "areas/index.json").read_text()),
            json.loads((ROOT / "portfolio/papers.json").read_text()),
            json.loads((ROOT / "program.json").read_text()),
        ]):
            result = audit(ROOT)
        self.assertEqual(result["inventory_status"], "FAIL")
        self.assertTrue(any(v.startswith("invalid_source_sha:") for v in result["findings"]))

    def test_unsafe_source_paths_fail_closed(self):
        base = json.loads((ROOT / "manuscripts/source_manifest.json").read_text())
        areas = json.loads((ROOT / "areas/index.json").read_text())
        registry = json.loads((ROOT / "portfolio/papers.json").read_text())
        program = json.loads((ROOT / "program.json").read_text())
        for path in ("../private.md", "/tmp/secrets", r"private\\file.tex",
                     "folder//file.tex", "file\\x00.tex"):
            with self.subTest(path=path):
                source = json.loads(json.dumps(base))
                source["papers"][0]["source_path"] = path
                with patch("migration_preflight.json.loads",
                           side_effect=[source, areas, registry, program]):
                    report = audit(ROOT)
                self.assertEqual(report["inventory_status"], "FAIL")
                self.assertIn("unsafe_source_path:MSC-AFFECT-P07", report["findings"])

    def test_incorrect_source_repository_is_rejected(self):
        source = json.loads((ROOT / "manuscripts/source_manifest.json").read_text())
        source["papers"][0]["source_repository"] = "other.invalid/repository"
        other = [
            json.loads((ROOT / "areas/index.json").read_text()),
            json.loads((ROOT / "portfolio/papers.json").read_text()),
            json.loads((ROOT / "program.json").read_text()),
        ]
        with patch("migration_preflight.json.loads", side_effect=[source, *other]):
            report = audit(ROOT)
        self.assertEqual(report["inventory_status"], "FAIL")
        self.assertIn("invalid_source_repository:MSC-AFFECT-P07", report["findings"])

 
class LocalPlanInventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = {
            "papers": [{"id": "MSC-AAA-P01", "local_plan_path": "manuscripts/MSC-AAA-P01/main.tex",
                        "source_role": "existing_manuscript_tex"},
                       {"id": "MSC-BBB-P02", "local_plan_path": None}],
            "local_only_plans": [{"id": "MSC-CCC-P03", "local_plan_path": "manuscripts/MSC-CCC-P03/main.tex"}],
        }
        for ident in ("MSC-AAA-P01", "MSC-CCC-P03"):
            self.make_plan(ident)

    def make_plan(self, ident):
        path = self.root / "manuscripts" / ident / "main.tex"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("fixture", encoding="utf-8")
        return path

    def test_external_source_with_local_plan_and_local_only_concept(self):
        paths, problems = local_plan_inventory(self.root, self.source)
        self.assertEqual(len(paths), 2)
        self.assertEqual(problems, [])

    def test_missing_plan(self):
        self.make_plan("MSC-AAA-P01").unlink()
        _, problems = local_plan_inventory(self.root, self.source)
        self.assertIn("missing_local_plan:manuscripts/MSC-AAA-P01/main.tex", problems)

    def test_unregistered_plan(self):
        self.make_plan("MSC-NEW-P04")
        _, problems = local_plan_inventory(self.root, self.source)
        self.assertIn("unregistered_local_plan:manuscripts/MSC-NEW-P04/main.tex", problems)

    def test_equal_counts_do_not_hide_wrong_paths(self):
        self.make_plan("MSC-AAA-P01").unlink()
        self.make_plan("MSC-NEW-P04")
        _, problems = local_plan_inventory(self.root, self.source)
        self.assertEqual(len(problems), 2)

    def test_duplicate_id_across_groups(self):
        self.source["local_only_plans"].append(self.source["papers"][0].copy())
        _, problems = local_plan_inventory(self.root, self.source)
        self.assertIn("duplicate_local_plan_id:MSC-AAA-P01", problems)

    def test_unsafe_path(self):
        self.source["local_only_plans"][0]["local_plan_path"] = "../outside.tex"
        _, problems = local_plan_inventory(self.root, self.source)
        self.assertIn("invalid_local_plan_path:MSC-CCC-P03", problems)

    def test_symlink_plan_rejected(self):
        path = self.make_plan("MSC-AAA-P01")
        path.unlink()
        try:
            path.symlink_to(self.make_plan("MSC-CCC-P03"))
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable")
        _, problems = local_plan_inventory(self.root, self.source)
        self.assertIn("invalid_local_plan_file:manuscripts/MSC-AAA-P01/main.tex", problems)

    def test_empty_inventory_rejected(self):
        _, problems = local_plan_inventory(self.root, {"papers": [], "local_only_plans": []})
        self.assertIn("no_registered_local_plans", problems)

    def test_missing_local_only_registry_rejected(self):
        del self.source["local_only_plans"]
        _, problems = local_plan_inventory(self.root, self.source)
        self.assertIn("invalid_local_only_plans", problems)


if __name__ == "__main__":
    unittest.main()
