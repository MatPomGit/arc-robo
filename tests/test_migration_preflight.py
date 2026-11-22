"""Regression tests for read-only ARC Robo v2 migration preflight."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from migration_preflight import audit


class MigrationPreflightTests(unittest.TestCase):
    def test_existing_inventory_is_valid_but_not_migrated(self):
        result = audit(ROOT)
        self.assertEqual(result["inventory_status"], "PASS", result["findings"])
        self.assertEqual(result["migration_status"], "BLOCKED")
        self.assertFalse(result["migration_ready"])
        self.assertEqual(result["record_count"], 31)
        self.assertEqual(result["local_plan_count"], 31)
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


if __name__ == "__main__":
    unittest.main()
