"""Check v3 records without modifying source provenance."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def main():
    program = Draft202012Validator(load("schemas/program.v3.schema.json"))
    program.validate(load("program.json"))
    validator = Draft202012Validator(load("schemas/paper.v3.schema.json"))
    manifest = load("manuscripts/source_manifest.json")
    expected = {p["id"] for p in manifest["papers"] + manifest["local_only_plans"]}
    paths = sorted(ROOT.glob("manuscripts/MSC-*/paper.json"))
    assert {p.parent.name for p in paths} == expected
    for path in paths:
        record = load(path.relative_to(ROOT))
        validator.validate(record)
        assert record["id"] == path.parent.name
        assert record["manuscript"]["path"] == f"manuscripts/{record['id']}/main.tex"
        for relative in [record["manuscript"]["path"], record["study_plan"]] + [d["contract_path"] for d in record["dependencies"]["tools"]]:
            assert (ROOT / relative).is_file()
        assert record["public_listing"] is False
    print(f"PASS: {len(paths)} v3 records")

if __name__ == "__main__":
    main()
