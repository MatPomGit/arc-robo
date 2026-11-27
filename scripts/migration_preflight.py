"""Read-only migration preflight for the 31 ARC Robo research references.

This tool does not migrate, assign canonical ownership, or publish.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
MSC = re.compile(r"^MSC-[A-Z0-9]+(?:-[A-Z0-9]+)+$")
SHA = re.compile(r"^[0-9a-f]{40}$")
ROLES = {"research_protocol_or_proposal", "existing_manuscript_tex", "tex_placeholder"}
REPOSITORY = re.compile(r"^MatPomGit/[A-Za-z0-9_.-]+$")


def safe_source_path(value: object) -> bool:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        return False
    parts = PurePosixPath(value).parts
    return (not value.startswith(("/", "./")) and "//" not in value and
            bool(parts) and all(part not in {".", "..", ""} for part in parts))


def local_plan_inventory(root: Path, source: dict) -> tuple[list[str], list[str]]:
    """Validate the exact set of local plans, independent of source roles."""
    expected: set[str] = set()
    seen: set[str] = set()
    problems: list[str] = []
    local_only = source.get("local_only_plans")
    if not isinstance(local_only, list):
        return [], ["invalid_local_only_plans"]
    for rows, required in ((source["papers"], False), (local_only, True)):
        for row in rows:
            if not isinstance(row, dict):
                problems.append("invalid_local_plan_record")
                continue
            ident = row.get("id")
            if not isinstance(ident, str) or not MSC.fullmatch(ident):
                problems.append("invalid_local_plan_id:" + str(ident))
                continue
            if ident in seen:
                problems.append("duplicate_local_plan_id:" + ident)
            seen.add(ident)
            path = row.get("local_plan_path")
            if path is None and not required:
                continue
            canonical = "manuscripts/" + ident + "/main.tex"
            if path != canonical:
                problems.append("invalid_local_plan_path:" + ident)
                continue
            expected.add(canonical)
    actual = {
        path.relative_to(root).as_posix()
        for path in (root / "manuscripts").glob("MSC-*/main.tex")
    }
    if not expected:
        problems.append("no_registered_local_plans")
    if (root / "manuscripts").is_symlink():
        problems.append("symlink_manuscripts_directory")
    for path in sorted(expected - actual):
        problems.append("missing_local_plan:" + path)
    for path in sorted(actual - expected):
        problems.append("unregistered_local_plan:" + path)
    for path in sorted(expected & actual):
        candidate = root / path
        if not candidate.is_file() or candidate.is_symlink() or candidate.parent.is_symlink():
            problems.append("invalid_local_plan_file:" + path)
    return sorted(expected), sorted(set(problems))


def audit(root: Path = ROOT) -> dict:
    root = Path(root)
    source = json.loads((root / "manuscripts/source_manifest.json").read_text(encoding="utf-8"))
    areas = json.loads((root / "config/research-lines.json").read_text(encoding="utf-8"))
    canonical = json.loads((root / "config/legacy-papers.json").read_text(encoding="utf-8"))
    program = json.loads((root / "program.json").read_text(encoding="utf-8"))
    records = source["papers"]
    valid_areas = {x["id"] for x in areas["lines"]}
    seen = set()
    problems = []
    counts = Counter()
    for row in records:
        ident = row.get("id")
        if not isinstance(ident, str) or not MSC.fullmatch(ident):
            problems.append("invalid_msc:" + str(ident))
            continue
        if ident in seen:
            problems.append("duplicate_msc:" + ident)
        seen.add(ident)
        area = row.get("area")
        if area not in valid_areas:
            problems.append("unmapped_area:" + ident)
        else:
            counts[area] += 1
        if row.get("source_role") not in ROLES:
            problems.append("invalid_role:" + ident)
        if not isinstance(row.get("source_commit_sha"), str) or not SHA.fullmatch(row["source_commit_sha"]):
            problems.append("invalid_source_sha:" + ident)
        if not isinstance(row.get("source_blob_sha"), str) or not SHA.fullmatch(row["source_blob_sha"]):
            problems.append("missing_or_invalid_source_blob_sha:" + ident)
        if not isinstance(row.get("source_repository"), str) or not REPOSITORY.fullmatch(row["source_repository"]):
            problems.append("invalid_source_repository:" + ident)
        if not safe_source_path(row.get("source_path")):
            problems.append("unsafe_source_path:" + ident)
        path = row.get("local_plan_path")
        if path is not None:
            expected = "manuscripts/" + ident + "/main.tex"
            if (path != expected or not (root / path).is_file() or
                    (root / path).is_symlink() or (root / "manuscripts" / ident).is_symlink()):
                problems.append("missing_or_invalid_local_plan:" + ident)
        else:
            if ((root / "manuscripts" / ident / "main.tex").exists() or
                    (root / "manuscripts" / ident).is_symlink()):
                problems.append("unexpected_local_manuscript:" + ident)
        url = "https://github.com/{}/blob/{}/{}".format(
            row.get("source_repository"), row.get("source_commit_sha"), row.get("source_path"))
        if row.get("source_reference_url") != url:
            problems.append("unpinned_reference:" + ident)

    plans, plan_problems = local_plan_inventory(root, source)
    problems.extend(plan_problems)

    if len(records) != 31 or len(seen) != 31:
        problems.append("expected_31_unique_msc")
    if program.get("schema_version") != 3 or canonical.get("schema_version") != 1:
        problems.append("unexpected_legacy_schema")
    if canonical.get("papers") != []:
        problems.append("legacy_portfolio_is_not_empty")
    if not valid_areas:
        problems.append("missing_scientific_areas")

    return {
        "inventory_status": "PASS" if not problems else "FAIL",
        "migration_status": "BLOCKED",
        "migration_ready": False,
        "schema_version": program.get("schema_version"),
        "record_count": len(records),
        "local_plan_count": len(plans),
        "local_only_plan_count": len(source["local_only_plans"]) if isinstance(source.get("local_only_plans"), list) else 0,
        "pinned_source_count": len(records),
        "local_plan_paths": plans,
        "external_reference_count": sum(not x.get("local_plan_path") for x in records),
        "research_lines": dict(sorted(counts.items())),
        "unresolved_decisions": [
            "canonical_owner_for_each_msc",
            "research_and_publication_status_mapping",
            "source_repo_not_necessarily_canonical_owner",
        ],
        "findings": sorted(set(problems)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        report = audit(args.root)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"inventory_status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["inventory_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
