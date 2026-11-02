"""Deprecated: use `scripts/course` (assessor.course_flow). Kept for assess wizard alias."""
from __future__ import annotations

import sys
from pathlib import Path

from assessor.bundle import build_bundle, evidence_path_for, render_bundle_preview
from assessor.evidence import (
    criteria_checklist,
    ensure_evidence_template,
    lesson_completion_line,
    merge_evidence_sections,
    split_evidence_sections,
)
from assessor.paths import assessor_dir, rubric_path
from assessor.report import assess_rubric, format_report_text, save_report
from assessor.rubric import load_rubric

SECTION_HINTS: dict[str, str] = {
    "## Artifact paths": "List repo-relative paths you used or changed.",
    "## Build and run": "pebble build; pebble install --emulator emery.",
    "## Behavior observed": "What you saw in the emulator or logs.",
    "## Boundary case tested": "One normal and one boundary case.",
    "## Explain in your own words": "Your main written evidence.",
    "## Source diff": "Where git changes live; assessor collects diff on submit.",
}


def run_wizard(
    course_root: Path,
    activity_id: str,
    *,
    baseline: str | None = None,
    force_init: bool = False,
    skip_submit: bool = False,
) -> int:
    print(
        "Note: `assess wizard` is deprecated. Use ./scripts/course from the repo root.\n",
        file=sys.stderr,
    )
    rubric = load_rubric(rubric_path(course_root, activity_id))
    evidence_path = ensure_evidence_template(
        course_root, activity_id, rubric, force=force_init
    )
    completion = lesson_completion_line(course_root, rubric.lesson_readme)
    print(f"\n  Evidence wizard — activity {activity_id}")
    print(f"  File: {evidence_path.relative_to(course_root)}\n")
    if completion:
        print(f"Lesson completion: {completion}\n")
    for line in criteria_checklist(rubric):
        print(f"  {line}")
    print("\nUse ./scripts/course for the streamlined flow.\n")
    return 0 if skip_submit else 1
