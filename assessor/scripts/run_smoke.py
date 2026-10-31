#!/usr/bin/env python3
"""CLI smoke checks: exemplar meets vs below produce expected assessment signals."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

from assessor.paths import assessor_dir, find_course_root

ACTIVITIES = ("2A", "3A")


def _assess(*args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["assess", *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )


def _latest_report(course_root: Path, activity_id: str) -> dict:
    reports_dir = course_root / ".assessor" / "reports"
    candidates = sorted(reports_dir.glob(f"{activity_id}-*.json"))
    if not candidates:
        raise AssertionError(f"No report written under {reports_dir} for {activity_id}")
    return json.loads(candidates[-1].read_text(encoding="utf-8"))


def _criterion_statuses(report: dict) -> dict[str, str]:
    return {c["id"]: c["status"] for c in report["criteria"]}


def _copy_evidence(course_root: Path, activity_id: str, tier: str, name: str) -> None:
    src = (
        assessor_dir(course_root)
        / "examples"
        / activity_id
        / tier
        / name
        / "EVIDENCE.md"
    )
    dest = course_root / "submit" / activity_id / "EVIDENCE.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def _run_submit(course_root: Path, activity_id: str) -> dict:
    proc = _assess("submit", activity_id, "--json", cwd=course_root)
    if proc.returncode not in (0, 1):
        raise AssertionError(
            f"assess submit {activity_id} exited {proc.returncode}\n"
            f"stdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
        )
    report = _latest_report(course_root, activity_id)
    return report


def _check_examples(course_root: Path) -> None:
    for activity_id in ACTIVITIES:
        proc = _assess("examples", activity_id, cwd=course_root)
        if proc.returncode != 0:
            raise AssertionError(f"assess examples {activity_id} failed:\n{proc.stderr}")


def _check_7a_meets(course_root: Path) -> None:
    _copy_evidence(course_root, "2A", "meets", "01-minimal-pass")
    report = _run_submit(course_root, "2A")
    statuses = _criterion_statuses(report)
    if statuses.get("build_and_run") != "pass":
        raise AssertionError(f"2A meets: expected build_and_run pass, got {statuses}")
    spacy = report.get("spacy_checks") or []
    if spacy and not any(s.get("margin", 0) > 0 for s in spacy):
        raise AssertionError("2A meets: expected positive spaCy margin vs exemplars")


def _check_7a_below(course_root: Path) -> None:
    _copy_evidence(course_root, "2A", "below", "01-vague-no-artifacts")
    report = _run_submit(course_root, "2A")
    if report["overall"] == "pass":
        raise AssertionError("2A below vague: expected overall not pass")
    statuses = _criterion_statuses(report)
    if statuses.get("build_and_run") == "pass":
        raise AssertionError("2A below vague: build_and_run should not pass")


def _check_4a_meets(course_root: Path) -> None:
    _copy_evidence(course_root, "3A", "meets", "01-both-projects")
    report = _run_submit(course_root, "3A")
    statuses = _criterion_statuses(report)
    if statuses.get("both_projects") != "pass":
        raise AssertionError(f"3A meets: both_projects should pass, got {statuses}")


def _check_4a_below(course_root: Path) -> None:
    _copy_evidence(course_root, "3A", "below", "01-one-project-only")
    report = _run_submit(course_root, "3A")
    statuses = _criterion_statuses(report)
    if statuses.get("both_projects") == "pass":
        raise AssertionError("3A below one-project: both_projects should not pass")


def main() -> int:
    course_root = find_course_root()
    print(f"Smoke CLI: course root {course_root}")
    _check_examples(course_root)
    print("  assess examples 2A, 3A — ok")
    _check_7a_meets(course_root)
    print("  2A meets exemplar — ok")
    _check_7a_below(course_root)
    print("  2A below exemplar — ok")
    _check_4a_meets(course_root)
    print("  3A meets exemplar — ok")
    _check_4a_below(course_root)
    print("  3A below exemplar — ok")
    print("Smoke CLI: all checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
