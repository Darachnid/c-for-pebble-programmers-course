from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from assessor.bundle import build_bundle, evidence_path_for, render_bundle_preview
from assessor.paths import assessor_dir, find_course_root, rubric_path
from assessor.report import assess_rubric, format_report_text, save_report
from assessor.rubric import load_rubric

PILOT_IDS = ("1A", "2A", "3A", "4A", "5A")


def _activity_id(raw: str) -> str:
    aid = raw.strip().upper()
    if aid not in PILOT_IDS:
        print(
            f"Note: {aid} is not in the v1 pilot ({', '.join(PILOT_IDS)}); rubric may be missing.",
            file=sys.stderr,
        )
    return aid


def cmd_init(args: argparse.Namespace) -> int:
    course_root = find_course_root()
    activity_id = _activity_id(args.activity_id)
    rubric = load_rubric(rubric_path(course_root, activity_id))
    assess_root = assessor_dir(course_root)
    tpl_path = assess_root / rubric.evidence_template
    if not tpl_path.is_file():
        raise SystemExit(f"Missing evidence template: {tpl_path}")

    template = tpl_path.read_text(encoding="utf-8")
    body = template.replace("{{ACTIVITY_ID}}", activity_id).replace(
        "{{ACTIVITY_TITLE}}", rubric.id
    )
    out = evidence_path_for(course_root, activity_id)
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.is_file() and not args.force:
        print(f"Already exists: {out.relative_to(course_root)} (use --force to overwrite)")
    else:
        out.write_text(body, encoding="utf-8")
        print(f"Wrote {out.relative_to(course_root)}")

    print("\nGit will watch these paths on submit:")
    for p in rubric.paths:
        print(f"  {p}")
    print(f"\nNext: complete the activity, fill EVIDENCE.md, then: assess submit {activity_id}")
    return 0


def cmd_diff(args: argparse.Namespace) -> int:
    course_root = find_course_root()
    activity_id = _activity_id(args.activity_id)
    rubric = load_rubric(rubric_path(course_root, activity_id))
    bundle = build_bundle(
        course_root,
        activity_id,
        rubric.paths,
        rubric.evidence_sections,
        baseline=args.baseline,
    )
    print(render_bundle_preview(bundle))
    return 0


def cmd_submit(args: argparse.Namespace) -> int:
    course_root = find_course_root()
    activity_id = _activity_id(args.activity_id)
    rubric = load_rubric(rubric_path(course_root, activity_id))
    bundle = build_bundle(
        course_root,
        activity_id,
        rubric.paths,
        rubric.evidence_sections,
        baseline=args.baseline,
    )
    report = assess_rubric(rubric, bundle, assessor_dir(course_root))
    report_path = save_report(course_root, report)

    if args.json:
        payload = {
            "activity_id": report.activity_id,
            "overall": report.overall,
            "criteria": [
                {
                    "id": c.id,
                    "status": c.status,
                    "text": c.text,
                    "messages": c.messages,
                }
                for c in report.criteria
            ],
            "report_path": str(report_path.relative_to(course_root)),
        }
        print(json.dumps(payload, indent=2))
    else:
        print(format_report_text(report))
        print(f"Report saved: {report_path.relative_to(course_root)}")

    return 1 if report.overall == "fail" else 0


def cmd_examples(args: argparse.Namespace) -> int:
    course_root = find_course_root()
    activity_id = _activity_id(args.activity_id)
    rubric = load_rubric(rubric_path(course_root, activity_id))
    assess_root = assessor_dir(course_root)
    meets = assess_root / rubric.exemplar_meets if rubric.exemplar_meets else None
    below = assess_root / rubric.exemplar_below if rubric.exemplar_below else None

    print(f"Exemplars for {activity_id} (evidence shape — not solutions to copy):\n")
    for label, base in ("MEETS (at/above threshold)", meets), ("BELOW (common gaps)", below):
        print(f"  {label}:")
        if not base or not base.is_dir():
            print("    (none)")
            continue
        for child in sorted(base.iterdir()):
            if not child.is_dir():
                continue
            notes = child / "NOTES.md"
            note_line = ""
            if notes.is_file():
                first = notes.read_text(encoding="utf-8").strip().splitlines()
                if first:
                    note_line = f" — {first[0]}"
            print(f"    {child.name}{note_line}")
        print("")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="assess",
        description="Post-submit evidence assessor (pilot: 2A, 3A). Run only after finishing an activity.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="Create submit/<ID>/EVIDENCE.md from template")
    p_init.add_argument("activity_id", help="Activity id, e.g. 2A or 3A")
    p_init.add_argument("--force", action="store_true", help="Overwrite existing EVIDENCE.md")
    p_init.set_defaults(func=cmd_init)

    for name, help_text in (
        ("diff", "Preview git bundle without scoring"),
        ("submit", "Run deterministic + spaCy assessment"),
    ):
        p = sub.add_parser(name, help=help_text)
        p.add_argument("activity_id")
        p.add_argument(
            "--baseline",
            default=None,
            help="Git ref for diff baseline (default: working tree vs HEAD / unstaged)",
        )
        if name == "submit":
            p.add_argument("--json", action="store_true", help="Print JSON summary to stdout")
        p.set_defaults(func=cmd_diff if name == "diff" else cmd_submit)

    p_ex = sub.add_parser("examples", help="List meets vs below exemplar folders")
    p_ex.add_argument("activity_id")
    p_ex.set_defaults(func=cmd_examples)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
