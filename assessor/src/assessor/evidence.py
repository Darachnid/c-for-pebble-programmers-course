"""EVIDENCE.md assembly and section utilities."""
from __future__ import annotations

import re
from pathlib import Path

from assessor.bundle import evidence_path_for
from assessor.course_manifest import Activity
from assessor.paths import assessor_dir
from assessor.rubric import Rubric, load_rubric


def lesson_completion_line(course_root: Path, lesson_readme: str) -> str | None:
    readme = course_root / lesson_readme
    if not readme.is_file():
        return None
    text = readme.read_text(encoding="utf-8")
    match = re.search(
        r"## Completion evidence\s*\n+\s*(.+?)(?=\n## |\Z)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if not match:
        return None
    return " ".join(match.group(1).strip().split())


def split_evidence_sections(text: str, headings: list[str]) -> dict[str, str]:
    bodies: dict[str, str] = {}
    for i, heading in enumerate(headings):
        if heading not in text:
            bodies[heading] = ""
            continue
        start = text.index(heading) + len(heading)
        end = len(text)
        for later in headings[i + 1 :]:
            pos = text.find(later, start)
            if pos != -1:
                end = pos
                break
        bodies[heading] = text[start:end].strip()
    return bodies


def merge_evidence_sections(text: str, headings: list[str], bodies: dict[str, str]) -> str:
    out = text
    for i, heading in enumerate(headings):
        if heading not in out:
            continue
        start = out.index(heading) + len(heading)
        end = len(out)
        for later in headings[i + 1 :]:
            pos = out.find(later, start)
            if pos != -1:
                end = pos
                break
        new_body = bodies.get(heading, "")
        if new_body and not new_body.endswith("\n"):
            new_body += "\n"
        if new_body and not new_body.startswith("\n"):
            new_body = "\n\n" + new_body
        elif not new_body:
            new_body = "\n\n"
        out = out[:start] + new_body + out[end:]
    return out


def ensure_evidence_template(
    course_root: Path, activity_id: str, rubric: Rubric, *, force: bool = False
) -> Path:
    path = evidence_path_for(course_root, activity_id)
    if path.is_file() and not force:
        return path
    tpl_path = assessor_dir(course_root) / rubric.evidence_template
    template = tpl_path.read_text(encoding="utf-8")
    body = template.replace("{{ACTIVITY_ID}}", activity_id).replace(
        "{{ACTIVITY_TITLE}}", rubric.id
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    return path


def auto_section_bodies(
    course_root: Path, activity: Activity, rubric: Rubric
) -> dict[str, str]:
    submit_rel = f"submit/{activity.id}/EVIDENCE.md"
    artifact = f"- {activity.pebble_workdir}\n- {submit_rel}"
    if activity.pebble_notes:
        artifact += f"\n- (also: {activity.pebble_notes})"

    build = (
        f"Working directory: `{activity.pebble_workdir}`\n\n"
        "```sh\n"
        f"cd {activity.pebble_workdir}\n"
        "pebble build\n"
        "pebble install --emulator emery\n"
        "pebble logs --emulator emery   # optional\n"
        "```\n\n"
        "Run the commands above in another terminal, then continue here."
    )
    if activity.pebble_notes:
        build += f"\n\nNote: {activity.pebble_notes}"

    diff = (
        f"Git changes under lesson paths (see rubric) are collected automatically on submit. "
        f"Evidence file: `{submit_rel}`."
    )

    auto: dict[str, str] = {
        "## Artifact paths": artifact,
        "## Build and run": build,
        "## Source diff": diff,
    }
    return auto


def assemble_evidence(
    course_root: Path,
    activity: Activity,
    rubric: Rubric,
    user_values: dict[str, str],
) -> Path:
    """Write EVIDENCE.md from auto sections + user field captures."""
    path = ensure_evidence_template(course_root, activity.id, rubric)
    text = path.read_text(encoding="utf-8")
    bodies = split_evidence_sections(text, rubric.evidence_sections)
    bodies.update(auto_section_bodies(course_root, activity, rubric))
    key_to_section = {f.key: f.section for f in activity.user_fields}
    for key, value in user_values.items():
        section = key_to_section.get(key)
        if section and value.strip():
            bodies[section] = value.strip()
    path.write_text(
        merge_evidence_sections(text, rubric.evidence_sections, bodies), encoding="utf-8"
    )
    return path


def criteria_checklist(rubric: Rubric) -> list[str]:
    lines: list[str] = []
    for c in rubric.criteria:
        line = f"• {c.text}"
        if c.spacy and c.spacy.required_phrases:
            line += f" (concepts: {', '.join(c.spacy.required_phrases)})"
        lines.append(line)
    return lines
