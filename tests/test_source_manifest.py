"""Validate version-pinned sources independently from approval registries."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = ROOT / "manuscripts"

class SourceManifestContract(unittest.TestCase):
    def test_31_unique_sources_and_local_paths(self):
        records = json.loads((BASE / "source_manifest.json").read_text(encoding="utf-8"))["papers"]
        self.assertEqual(len(records), 31)
        self.assertEqual(len({p["id"] for p in records}), 31)
        self.assertEqual({p["id"] for p in records},{p.name for p in BASE.iterdir() if p.is_dir() and p.name.startswith("MSC-")})
        roles = {}
        for p in records:
            with self.subTest(id=p["id"]):
                self.assertRegex(p["source_commit_sha"],r"^[0-9a-f]{40}$")
                url = "https://github.com/{}/blob/{}/{}".format(p["source_repository"],p["source_commit_sha"],p["source_path"])
                self.assertEqual(p["source_reference_url"],url)
                self.assertIn(url,(BASE/p["id"]/"README.md").read_text(encoding="utf-8"))
                roles[p["source_role"]] = roles.get(p["source_role"],0)+1
                if p["local_plan_path"]:
                    self.assertEqual(p["local_plan_path"],"manuscripts/"+p["id"]+"/main.tex")
                    self.assertTrue((ROOT/p["local_plan_path"]).is_file())
                else:
                    self.assertFalse((BASE/p["id"]/"main.tex").exists())
        self.assertEqual(roles,{"research_protocol_or_proposal":14,"existing_manuscript_tex":9,"tex_placeholder":8})
    def test_all_msc_have_grounded_research_areas(self):
        manifest = json.loads((BASE / "source_manifest.json").read_text(encoding="utf-8"))
        lines = json.loads((ROOT / "areas/index.json").read_text(encoding="utf-8"))
        allowed = {line["id"] for line in lines["lines"]}
        records = manifest["papers"]
        self.assertEqual(len(records), 31)
        self.assertEqual({p["area"] for p in records}, allowed)
        counts = {area: sum(p["area"] == area for p in records) for area in allowed}
        self.assertEqual(counts, {
            "teleoperation": 1,
            "hri-safety": 10,
            "perception": 8,
            "inspection": 9,
            "navigation": 3,
        })
        # Research classification is not proof of canonical manuscript ownership.
        self.assertTrue(all("canonical_owner" not in p for p in records))

    def test_unapproved_states_preserved(self):
        records=json.loads((BASE/"source_manifest.json").read_text(encoding="utf-8"))["papers"]
        self.assertTrue(all(p["status"] not in ("PUBLISHED","ACCEPTED","SUBMITTED") for p in records))
        self.assertNotIn("blob/main/",(BASE/"README.md").read_text(encoding="utf-8"))
if __name__ == "__main__":
    unittest.main()
