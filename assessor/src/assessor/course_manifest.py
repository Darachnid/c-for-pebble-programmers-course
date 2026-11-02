from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml
import re


@dataclass
class UserField:
    key: str
    section: str
    prompt: str


@dataclass
class Activity:
    id: str
    title: str
    depends: list[str]
    lesson_readme: str
    pebble_workdir: str
    assessor_rubric: str | None
    user_fields: list[UserField] = field(default_factory=list)
    pebble_notes: str | None = None


@dataclass
class CourseManifest:
    version: int
    sequence: list[str]
    activities: dict[str, Activity]

    def activity(self, activity_id: str) -> Activity:
        if activity_id not in self.activities:
            raise KeyError(f"Unknown activity {activity_id!r}")
        return self.activities[activity_id]


def manifest_path(assessor_root: Path) -> Path:
    return assessor_root / "course" / "manifest.yaml"


def load_manifest(assessor_root: Path) -> CourseManifest:
    path = manifest_path(assessor_root)
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    activities: dict[str, Activity] = {}
    for aid, raw in data.get("activities", {}).items():
        fields = [
            UserField(
                key=f["key"],
                section=f["section"],
                prompt=str(f["prompt"]).strip(),
            )
            for f in raw.get("user_fields", [])
        ]
        activities[aid] = Activity(
            id=aid,
            title=raw["title"],
            depends=list(raw.get("depends", [])),
            lesson_readme=raw["lesson_readme"],
            pebble_workdir=raw["pebble_workdir"],
            assessor_rubric=raw.get("assessor_rubric"),
            user_fields=fields,
            pebble_notes=raw.get("pebble_notes"),
        )
    # Fill the remaining activities from the authoritative, ordered lesson index.
    # Existing Phase I definitions (and their assessor rubrics) are preserved.
    course_root = assessor_root.parent
    index = (course_root / "lessons" / "README.md").read_text(encoding="utf-8")
    for match in re.finditer(r"^\\| \\[(\\d+[A-Z])\\]\\([^)]+\\) \\| ([^|]+) \\|[^|]+\\| ([^|]+) \\|", index, re.MULTILINE):
        aid, title, depends = match.groups()
        if aid in activities:
            continue
        folder = course_root / "lessons" / f"{int(aid[:-1]):02d}{aid[-1]}"
        if not folder.is_dir():
            raise FileNotFoundError(f"Missing lesson directory: {folder}")
        projects = sorted(folder.glob("*/package.json"))
        workdir = projects[0].parent if projects else folder
        activities[aid] = Activity(
            id=aid, title=title.strip(),
            depends=re.findall(r"\\d+[A-Z]", depends),
            lesson_readme=str((folder / "README.md").relative_to(course_root)),
            pebble_workdir=str(workdir.relative_to(course_root)),
            assessor_rubric=None,
            user_fields=[
                UserField("behavior", "## Behavior observed", "Describe what you did and the artifacts produced."),
                UserField("boundary", "## Boundary case tested", "Record normal and edge-case tests, or explain why this activity is non-executable."),
                UserField("explain", "## Explain in your own words", "Explain how each lesson completion criterion was met."),
            ],
        )
    sequence = list(data["sequence"]) + [aid for aid in activities if aid not in data["sequence"]]
    return CourseManifest(
        version=int(data.get("version", 1)),
        sequence=sequence,
        activities=activities,
    )


def validate_manifest(course_root: Path, manifest: CourseManifest) -> None:
    for aid in manifest.sequence:
        if aid not in manifest.activities:
            raise ValueError(f"sequence lists {aid} but activities missing")
    for aid, act in manifest.activities.items():
        readme = course_root / act.lesson_readme
        if not readme.is_file():
            raise FileNotFoundError(f"{aid}: missing {act.lesson_readme}")
        workdir = course_root / act.pebble_workdir
        if not workdir.is_dir():
            raise FileNotFoundError(f"{aid}: missing pebble_workdir {act.pebble_workdir}")
        if act.assessor_rubric:
            rubric = course_root / "assessor" / act.assessor_rubric
            if not rubric.is_file():
                raise FileNotFoundError(f"{aid}: missing rubric {act.assessor_rubric}")
