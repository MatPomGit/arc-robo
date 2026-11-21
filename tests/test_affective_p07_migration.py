"""Check exact provenance and safety boundary for migrated AFFECT-P07 planning only."""
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
class AffectiveP07MigrationTest(unittest.TestCase):
    def test_migrated_plan_and_source_manifest(self):
        d=ROOT/"manuscripts/MSC-AFFECT-P07"
        p=json.loads((d/"migration.json").read_text(encoding="utf-8"))
        plan=(d/"plan.md").read_text(encoding="utf-8")
        manifest=json.loads((ROOT/"manuscripts/source_manifest.json").read_text(encoding="utf-8"))
        source=next(p for p in manifest["papers"] if p["id"]=="MSC-AFFECT-P07")
        self.assertEqual(p["source_blob_sha"],"92d7c570f926f4160ca7093c2b4b3acf6756aec2")
        self.assertEqual(p["source_commit_sha"],"0ff5f1531f03270c4f9fdcc7f3af6d2e9aca85dd")
        self.assertEqual(source["migrated_research_plan_path"],"manuscripts/MSC-AFFECT-P07/plan.md")
        self.assertEqual(source["source_blob_sha"],p["source_blob_sha"])
        self.assertNotIn("../../docs/",plan)
        self.assertIn("0ff5f1531f03270c4f9fdcc7f3af6d2e9aca85dd",plan)
        self.assertEqual(source["status"],"PLANNED")
        self.assertEqual(p["migration_phase"],"copy_verified_integrated")
        self.assertEqual(source["migration_phase"],p["migration_phase"])
        self.assertFalse(p["physical_robot_execution_authorized"])
        self.assertEqual(p["source_license_spdx"],"Apache-2.0")
        self.assertIn("Apache License",(d/"ORIGINAL_LICENSE").read_text(encoding="utf-8"))
        self.assertIn("[plan badawczy](plan.md)",(d/"README.md").read_text(encoding="utf-8"))
if __name__=="__main__":
    unittest.main()
