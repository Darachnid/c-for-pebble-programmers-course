from __future__ import annotations

from pathlib import Path


def find_course_root(start: Path | None = None) -> Path:
    """Walk up from *start* until SYLLABUS.md and assessor/rubrics exist."""
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "SYLLABUS.md").is_file() and (
            candidate / "assessor" / "rubrics"
        ).is_dir():
            return candidate
    raise SystemExit(
        "Not inside a course clone: need SYLLABUS.md and assessor/rubrics/ "
        f"(started from {current})."
    )


def assessor_dir(course_root: Path) -> Path:
    return course_root / "assessor"


def rubric_path(course_root: Path, activity_id: str) -> Path:
    path = assessor_dir(course_root) / "rubrics" / f"{activity_id}.yaml"
    if not path.is_file():
        supported = sorted(p.stem for p in (assessor_dir(course_root) / "rubrics").glob("*.yaml"))
        raise SystemExit(
            f"No rubric for {activity_id!r}. Pilot activities: {', '.join(supported) or '(none)'}"
        )
    return path
