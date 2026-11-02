from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from assessor.course_manifest import CourseManifest


@dataclass
class Progress:
    completed: list[str] = field(default_factory=list)
    current: str | None = None

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps({"completed": self.completed, "current": self.current}, indent=2)
            + "\n",
            encoding="utf-8",
        )

    @classmethod
    def load(cls, path: Path) -> Progress:
        if not path.is_file():
            return cls()
        data = json.loads(path.read_text(encoding="utf-8"))
        return cls(
            completed=list(data.get("completed", [])),
            current=data.get("current"),
        )


def progress_path(course_root: Path) -> Path:
    return course_root / ".course" / "progress.json"


def deps_satisfied(activity_id: str, manifest: CourseManifest, progress: Progress) -> bool:
    act = manifest.activity(activity_id)
    done = set(progress.completed)
    return all(dep in done for dep in act.depends)


def next_unblocked(manifest: CourseManifest, progress: Progress) -> str | None:
    done = set(progress.completed)
    for aid in manifest.sequence:
        if aid in done:
            continue
        if deps_satisfied(aid, manifest, progress):
            return aid
    return None


def resolve_current(
    manifest: CourseManifest, progress: Progress, explicit: str | None = None
) -> str:
    if explicit:
        aid = explicit.strip().upper()
        if not deps_satisfied(aid, manifest, progress):
            act = manifest.activity(aid)
            missing = [d for d in act.depends if d not in progress.completed]
            raise SystemExit(
                f"Activity {aid} is blocked. Complete first: {', '.join(missing)}"
            )
        return aid
    if progress.current and progress.current not in progress.completed:
        if deps_satisfied(progress.current, manifest, progress):
            return progress.current
    nxt = next_unblocked(manifest, progress)
    if nxt is None:
        raise SystemExit("All Phase I activities in the manifest are complete.")
    return nxt


def mark_complete(manifest: CourseManifest, progress: Progress, activity_id: str) -> None:
    if activity_id not in progress.completed:
        progress.completed.append(activity_id)
    progress.current = next_unblocked(manifest, progress)
