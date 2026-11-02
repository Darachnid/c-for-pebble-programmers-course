"""Terminal-first course driver — Phase I activities via one flow."""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from assessor.bundle import build_bundle, render_bundle_preview
from assessor.course_manifest import load_manifest, validate_manifest
from assessor.evidence import (
    assemble_evidence,
    criteria_checklist,
    lesson_completion_line,
)
from assessor.paths import assessor_dir, find_course_root, rubric_path
from assessor.progress import (
    Progress,
    mark_complete,
    next_unblocked,
    progress_path,
)
from assessor.report import assess_rubric, format_report_text, save_report
from assessor.rubric import load_rubric
from assessor.tmux_layout import (
    SESSION,
    launch_session,
    layout_commands,
    refresh_activity_panes,
    session_exists,
    tmux_available,
    wizard_shell_command,
)


def _read_multiline_prompt(label: str, prompt: str) -> str:
    print(f"\n--- {label} ---")
    print(prompt)
    print("(Paste your text; finish with an empty line.)\n")
    lines: list[str] = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "" and lines:
            break
        lines.append(line)
    return "\n".join(lines).strip()


def _capture_user_fields(activity, existing: dict[str, str] | None = None) -> dict[str, str]:
    existing = existing or {}
    values: dict[str, str] = {}
    for field in activity.user_fields:
        prior = existing.get(field.key, "")
        if prior.strip():
            print(f"\n--- {field.key} (already captured; Enter to keep, or type new text) ---")
            first = input().strip()
            if first == "":
                values[field.key] = prior
                continue
            values[field.key] = _read_multiline_prompt(field.key, field.prompt)
            if not values[field.key]:
                values[field.key] = first
            continue
        values[field.key] = _read_multiline_prompt(field.key, field.prompt)
    return values


def _print_pebble_hints(course_root: Path, activity) -> None:
    wd = course_root / activity.pebble_workdir
    print("\nPebble commands (run in another terminal):\n")
    print(f"  cd {course_root / activity.pebble_workdir}")
    print("  pebble build")
    print("  pebble install --emulator emery")
    if activity.pebble_notes:
        print(f"\n  {activity.pebble_notes}")
    if not (wd / "package.json").is_file():
        print(f"\n  Warning: no package.json in {activity.pebble_workdir}", file=sys.stderr)
    input("\nPress Enter when you have run the lesson work (or read-only for 1A)...")


def _run_assessment(
    course_root: Path, activity_id: str, rubric, *, baseline: str | None
) -> tuple[int, object]:
    bundle = build_bundle(
        course_root,
        activity_id,
        rubric.paths,
        rubric.evidence_sections,
        baseline=baseline,
    )
    report = assess_rubric(rubric, bundle, assessor_dir(course_root))
    report_path = save_report(course_root, report)
    print(format_report_text(report))
    print(f"Report saved: {report_path.relative_to(course_root)}")
    code = 1 if report.overall == "fail" else 0
    return code, report


def print_progress(course_root: Path) -> None:
    manifest = load_manifest(assessor_dir(course_root))
    progress = Progress.load(progress_path(course_root))
    nxt = next_unblocked(manifest, progress)
    print("Phase I progress\n")
    for aid in manifest.sequence:
        act = manifest.activity(aid)
        if aid in progress.completed:
            mark = "done"
        elif aid == nxt:
            mark = "next"
        elif all(d in progress.completed for d in act.depends):
            mark = "ready"
        else:
            mark = "blocked"
        print(f"  {aid}  {mark:8}  {act.title}")
    print()


def _wait_for_pebble(course_root: Path, activity, *, inside_tmux: bool) -> None:
    if inside_tmux:
        print("\nLesson: top-left pane. Pebble shell: top-right pane.")
        print("Ctrl-b, then an arrow key, moves between panes. Ctrl-b d detaches.")
        print("Run the build in the shell pane, then come back here.")
        input("Press Enter to record your evidence...")
        return
    _print_pebble_hints(course_root, activity)


def _run_until_pass(
    course_root: Path,
    activity_id: str,
    *,
    baseline: str | None,
    inside_tmux: bool,
) -> None:
    manifest = load_manifest(assessor_dir(course_root))
    activity = manifest.activity(activity_id)
    if not activity.assessor_rubric:
        raise SystemExit(f"{activity_id} has no assessor rubric in this manifest.")
    rubric = load_rubric(rubric_path(course_root, activity_id))
    completion = lesson_completion_line(course_root, activity.lesson_readme)
    print(f"\n=== {activity_id} — {activity.title} ===\n")
    if completion:
        print(f"Completion: {completion}\n")
    print("Assessor checklist:")
    for line in criteria_checklist(rubric):
        print(f"  {line}")
    _wait_for_pebble(course_root, activity, inside_tmux=inside_tmux)
    user_values = _capture_user_fields(activity)
    assemble_evidence(course_root, activity, rubric, user_values)
    progress = Progress.load(progress_path(course_root))
    progress.current = activity_id
    progress.save(progress_path(course_root))
    while True:
        print("\n--- Git capture preview ---")
        bundle = build_bundle(
            course_root,
            activity_id,
            rubric.paths,
            rubric.evidence_sections,
            baseline=baseline,
        )
        print(render_bundle_preview(bundle))
        code, _report = _run_assessment(course_root, activity_id, rubric, baseline=baseline)
        if code == 0:
            print(f"\n{activity_id} passed.")
            return
        print("\nSome criteria failed. Re-enter the fields below (auto sections unchanged).")
        user_values = _capture_user_fields(activity, user_values)
        assemble_evidence(course_root, activity, rubric, user_values)


def run_course_loop(
    course_root: Path,
    *,
    baseline: str | None = None,
    inside_tmux: bool = False,
) -> int:
    """Walk every remaining Phase I activity in this process."""
    manifest = load_manifest(assessor_dir(course_root))
    validate_manifest(course_root, manifest)
    first = True
    try:
        while True:
            progress = Progress.load(progress_path(course_root))
            activity_id = next_unblocked(manifest, progress)
            print_progress(course_root)
            if activity_id is None:
                print("Phase I is complete. This session can stay open.")
                input("Press Enter to leave the wizard...")
                return 0
            activity = manifest.activity(activity_id)
            if inside_tmux and not first:
                refresh_activity_panes(
                    activity_id=activity_id,
                    title=activity.title,
                    lesson_readme=course_root / activity.lesson_readme,
                    pebble_workdir=course_root / activity.pebble_workdir,
                    pebble_notes=activity.pebble_notes,
                )
            first = False
            _run_until_pass(
                course_root,
                activity_id,
                baseline=baseline,
                inside_tmux=inside_tmux,
            )
            progress = Progress.load(progress_path(course_root))
            mark_complete(manifest, progress, activity_id)
            progress.save(progress_path(course_root))
    except KeyboardInterrupt:
        print("\nCourse flow cancelled.", file=sys.stderr)
        return 130


def open_tmux(course_root: Path) -> int:
    if not tmux_available():
        raise SystemExit("tmux is required. Install it with: pacman -S tmux")
    inside = bool(os.environ.get("TMUX"))
    if session_exists():
        print(f"Reusing tmux session {SESSION}.")
        cmd = ["tmux", "switch-client" if inside else "attach-session", "-t", SESSION]
        os.execvp(cmd[0], cmd)
    manifest = load_manifest(assessor_dir(course_root))
    validate_manifest(course_root, manifest)
    progress = Progress.load(progress_path(course_root))
    activity_id = next_unblocked(manifest, progress) or manifest.sequence[-1]
    activity = manifest.activity(activity_id)
    commands = layout_commands(
        course_root=course_root,
        activity_id=activity_id,
        title=activity.title,
        lesson_readme=course_root / activity.lesson_readme,
        pebble_workdir=course_root / activity.pebble_workdir,
        wizard_cmd=wizard_shell_command(course_root),
        pebble_notes=activity.pebble_notes,
        inside_tmux=inside,
    )
    launch_session(commands)
    return 0


def _course_root_from_env() -> Path:
    root_env = os.environ.get("PEBBLE_COURSE_ROOT")
    if root_env:
        course_root = Path(root_env).resolve()
        if not (course_root / "SYLLABUS.md").is_file():
            raise SystemExit(f"PEBBLE_COURSE_ROOT invalid: {course_root}")
        return course_root
    return find_course_root()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="course",
        description="Open the Phase I course in tmux. This is the only learner command.",
    )
    parser.add_argument("--inside-tmux", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--no-tmux", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--baseline", default=None, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    course_root = _course_root_from_env()
    if args.inside_tmux or args.no_tmux:
        return run_course_loop(
            course_root,
            baseline=args.baseline,
            inside_tmux=args.inside_tmux,
        )
    return open_tmux(course_root)


if __name__ == "__main__":
    raise SystemExit(main())
