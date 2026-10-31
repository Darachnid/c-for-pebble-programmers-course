#!/usr/bin/env python3
"""CLI smoke checks: exemplar meets vs below produce expected assessment signals."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

from assessor.paths import assessor_dir, find_course_root

ACTIVITIES = ("7A", "4A")


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


def _det_pass(report: dict, criterion_id: str) -> bool:
    checks = [
        c
        for c in report.get("deterministic_checks", [])
        if c.get("criterion_id") == criterion_id
    ]
    return bool(checks) and all(c.get("status") == "pass" for c in checks)


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
    return _latest_report(course_root, activity_id)


def _check_examples(course_root: Path) -> None:
    for activity_id in ACTIVITIES:
        proc = _assess("examples", activity_id, cwd=course_root)
        if proc.returncode != 0:
            raise AssertionError(f"assess examples {activity_id} failed:\n{proc.stderr}")


def _check_7a_meets(course_root: Path) -> None:
    _copy_evidence(course_root, "7A", "meets", "01-minimal-pass")
    report = _run_submit(course_root, "7A")
    if not _det_pass(report, "build_and_run"):
        raise AssertionError("7A meets: deterministic build_and_run checks should pass")
    if not report.get("llm_checks"):
        raise AssertionError("7A meets: expected LLM checks in report (is Ollama running?)")


def _check_7a_below(course_root: Path) -> None:
    _copy_evidence(course_root, "7A", "below", "01-vague-no-artifacts")
    report = _run_submit(course_root, "7A")
    if _det_pass(report, "build_and_run"):
        raise AssertionError("7A below vague: deterministic build_and_run should not all pass")


def _check_4a_meets(course_root: Path) -> None:
    _copy_evidence(course_root, "4A", "meets", "01-both-projects")
    report = _run_submit(course_root, "4A")
    if not _det_pass(report, "both_projects"):
        raise AssertionError("4A meets: deterministic both_projects checks should pass")


def _check_4a_below(course_root: Path) -> None:
    _copy_evidence(course_root, "4A", "below", "01-one-project-only")
    report = _run_submit(course_root, "4A")
    if _det_pass(report, "both_projects"):
        raise AssertionError("4A below one-project: deterministic both_projects should not all pass")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--skip-submit",
        action="store_true",
        help="Only run assess examples (no Ollama submit checks)",
    )
    args = parser.parse_args()

    course_root = find_course_root()
    print(f"Smoke CLI: course root {course_root}")
    _check_examples(course_root)
    print("  assess examples 7A, 4A — ok")

    if args.skip_submit:
        print("  submit checks skipped (no Ollama)")
        return 0

    _check_7a_meets(course_root)
    print("  7A meets exemplar — ok")
    _check_7a_below(course_root)
    print("  7A below exemplar — ok")
    _check_4a_meets(course_root)
    print("  4A meets exemplar — ok")
    _check_4a_below(course_root)
    print("  4A below exemplar — ok")
    print("Smoke CLI: all checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
