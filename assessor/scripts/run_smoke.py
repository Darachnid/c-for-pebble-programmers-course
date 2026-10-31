#!/usr/bin/env python3
"""CLI smoke checks: exemplar meets vs below produce expected assessment signals."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

from assessor.paths import assessor_dir, find_course_root

ACTIVITIES = ("1A", "2A", "3A", "4A", "5A")

MEETS_CHECKS: dict[str, tuple[str, str, str]] = {
    "1A": ("1A", "meets", "01-five-ideas-clock"),
    "2A": ("2A", "meets", "01-minimal-pass"),
    "3A": ("3A", "meets", "01-both-projects"),
    "4A": ("4A", "meets", "01-text-layer-set-font"),
    "5A": ("5A", "meets", "01-font-change"),
}

BELOW_CHECKS: dict[str, tuple[str, str, str]] = {
    "1A": ("1A", "below", "01-two-vague-ideas"),
    "2A": ("2A", "below", "01-vague-no-artifacts"),
    "3A": ("3A", "below", "01-one-project-only"),
    "4A": ("4A", "below", "01-vague-no-signature"),
    "5A": ("5A", "below", "01-vague-no-visual"),
}


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


def _positive_spacy_margin(report: dict) -> bool:
    spacy = report.get("spacy_checks") or []
    return bool(spacy and any(s.get("margin", 0) > 0 for s in spacy))


def _check_meets(course_root: Path, activity_id: str) -> None:
    aid, tier, name = MEETS_CHECKS[activity_id]
    _copy_evidence(course_root, aid, tier, name)
    report = _run_submit(course_root, activity_id)
    statuses = _criterion_statuses(report)
    if activity_id == "1A":
        if report["overall"] != "pass":
            raise AssertionError(f"{activity_id} meets {name}: expected overall pass, got {report['overall']}")
    elif activity_id == "2A":
        if statuses.get("build_and_run") != "pass":
            raise AssertionError(f"{activity_id} meets: build_and_run should pass, got {statuses}")
        if not _positive_spacy_margin(report):
            raise AssertionError(f"{activity_id} meets: expected positive spaCy margin vs exemplars")
    elif activity_id == "3A":
        if statuses.get("both_projects") != "pass":
            raise AssertionError(f"{activity_id} meets: both_projects should pass, got {statuses}")
    elif activity_id == "4A":
        if statuses.get("api_note_complete") != "pass":
            raise AssertionError(f"{activity_id} meets: api_note_complete should pass, got {statuses}")
    elif activity_id == "5A":
        if statuses.get("build_and_run") != "pass" or statuses.get("one_visual_change") != "pass":
            raise AssertionError(f"{activity_id} meets: build/visual criteria should pass, got {statuses}")
        if not _positive_spacy_margin(report):
            raise AssertionError(f"{activity_id} meets: expected positive spaCy margin vs exemplars")
    else:
        if report["overall"] != "pass":
            raise AssertionError(f"{activity_id} meets {name}: expected overall pass, got {report['overall']}")


def _check_below(course_root: Path, activity_id: str) -> None:
    aid, tier, name = BELOW_CHECKS[activity_id]
    _copy_evidence(course_root, aid, tier, name)
    report = _run_submit(course_root, activity_id)
    statuses = _criterion_statuses(report)
    if activity_id == "1A":
        if statuses.get("five_ideas_with_api") == "pass":
            raise AssertionError(f"{activity_id} below {name}: five_ideas_with_api should not pass")
    elif activity_id == "2A":
        if report["overall"] == "pass":
            raise AssertionError(f"{activity_id} below {name}: expected overall not pass")
        if statuses.get("build_and_run") == "pass":
            raise AssertionError(f"{activity_id} below vague: build_and_run should not pass")
    elif activity_id == "3A":
        if statuses.get("both_projects") == "pass":
            raise AssertionError(f"{activity_id} below one-project: both_projects should not pass")
    elif activity_id == "4A":
        if statuses.get("api_note_complete") == "pass":
            raise AssertionError(f"{activity_id} below {name}: api_note_complete should not pass")
    elif activity_id == "5A":
        if statuses.get("one_visual_change") == "pass":
            raise AssertionError(f"{activity_id} below {name}: one_visual_change should not pass")
    elif report["overall"] == "pass":
        raise AssertionError(f"{activity_id} below {name}: expected overall not pass")


def main() -> int:
    course_root = find_course_root()
    print(f"Smoke CLI: course root {course_root}")
    _check_examples(course_root)
    print(f"  assess examples {', '.join(ACTIVITIES)} — ok")
    for activity_id in ACTIVITIES:
        _check_meets(course_root, activity_id)
        print(f"  {activity_id} meets exemplar — ok")
    for activity_id in ACTIVITIES:
        _check_below(course_root, activity_id)
        print(f"  {activity_id} below exemplar — ok")
    print("Smoke CLI: all checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
