#!/usr/bin/env python3
"""Validate all 41 sequential lesson IDs, core competencies and local artifacts."""
from __future__ import annotations
import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
src = (ROOT / "taskwarrior/import_course.py").read_text(encoding="utf-8")
tree = ast.parse(src)
values = {}
for stmt in tree.body:
    if isinstance(stmt, ast.Assign):
        for target in stmt.targets:
            if isinstance(target, ast.Name) and target.id in {"COURSE_V2", "COURSE_SEQUENCE"}:
                values[target.id] = ast.literal_eval(stmt.value)
baseline = values["COURSE_V2"]
sequence = values["COURSE_SEQUENCE"]
assert len(baseline) == len(sequence) == 26
assert set(baseline) == set(sequence)

extension = json.loads((ROOT / "taskwarrior/extension_api_labs.json").read_text(encoding="utf-8"))
all_tasks = list(baseline.values()) + extension
ids = [t["key"] for t in all_tasks]
assert len(ids) == len(set(ids)) == 41, ids
assert sorted(int(re.match(r"^\d+", i).group()) for i in ids) == list(range(1, 42))
by_id = {t["key"]: t for t in all_tasks}
for id_, t in by_id.items():
    assert re.fullmatch(r"\d+[A-Z]", id_), id_
    assert t["description"].split(" ", 1)[0] == id_, id_
    assert t["done"] and t["instructions"], id_
    assert (ROOT / "lessons" / id_ / "README.md").is_file(), id_
    for dep in t["depends"]:
        assert dep in by_id and int(re.match(r"^\d+", dep).group()) < int(re.match(r"^\d+", id_).group()), (id_, dep)

syllabus = (ROOT / "SYLLABUS.md").read_text(encoding="utf-8")
for id_ in by_id:
    assert syllabus.count(f"[{id_} — ") == 1, id_

mapping = json.loads((ROOT / "taskwarrior/legacy-id-map.json").read_text(encoding="utf-8"))["old_to_new"]
assert len(mapping) == 41 and len(set(mapping.values())) == 41
for old, new in mapping.items():
    assert old[-1] == new[-1], (old, new)

modules = ["3A", "8B", "9C", "10D", "17E", "18F", "19G", "24H"]
for lesson in modules:
    assert list((ROOT / "curriculum/c-programming").glob(lesson + "-*.md")), lesson
for lesson, chapters in {"3A": ["3-1", "3-2"], "8B": ["4-1", "4-2"],
                         "9C": ["5-1", "5-2", "5-3"], "10D": ["6-1", "6-2", "6-3", "6-4"]}.items():
    for chapter in chapters:
        assert (ROOT / "lessons" / lesson / "projects" / ("project-" + chapter) / "src/c/main.c").is_file()

projects = 0
for manifest in (ROOT / "lessons").glob("*/*/package.json"):
    cfg = json.loads(manifest.read_text(encoding="utf-8"))
    assert cfg["pebble"]["targetPlatforms"] == ["emery"], manifest
    assert (manifest.parent / "wscript").is_file(), manifest
    assert list((manifest.parent / "src").rglob("*.c")), manifest
    projects += 1

assert (ROOT / "assessor/rubrics/2A.yaml").is_file()
assert (ROOT / "assessor/rubrics/3A.yaml").is_file()
assert (ROOT / "SYLLABUS.pdf").is_file()
print(f"PASS: {len(ids)} sequential lessons, {projects} Emery example projects")
