#!/usr/bin/env python3
"""Static structure and dependency checks for the Emery C course."""
from __future__ import annotations
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
src = (ROOT / "taskwarrior/import_course.py").read_text(encoding="utf8")
tree = ast.parse(src)
config = {}
for stmt in tree.body:
    if isinstance(stmt, ast.Assign):
        for name in stmt.targets:
            if isinstance(name, ast.Name) and name.id in {"COURSE_V2", "COURSE_SEQUENCE"}:
                config[name.id] = ast.literal_eval(stmt.value)
tasks, order = config["COURSE_V2"], config["COURSE_SEQUENCE"]
assert len(tasks) == len(order) == len(set(order)) == 26
assert set(tasks) == set(order)
seen = set()
minutes = 0
syllabus = (ROOT / "SYLLABUS.md").read_text(encoding="utf8")
for key in order:
    task = tasks[key]
    assert task["key"] == key
    assert task["description"].split(" ")[0] == key
    assert task["instructions"] and task["done"], key
    assert set(task["depends"]).issubset(seen), key
    seen.add(key)
    assert (ROOT / "lessons" / key / "README.md").is_file(), key
    assert syllabus.count(f"#### {key} — ") == 1, key
    minutes += int(task["estimated"].removesuffix("m"))

projects = 0
for manifest in (ROOT / "lessons").glob("*/*/package.json"):
    cfg = json.loads(manifest.read_text(encoding="utf8"))
    assert cfg["pebble"]["targetPlatforms"] == ["emery"], manifest
    assert cfg["pebble"]["sdkVersion"] == "3", manifest
    assert (manifest.parent / "wscript").is_file(), manifest
    assert list((manifest.parent / "src").rglob("*.c")), manifest
    projects += 1

books = {
    "4A": ("3-1","3-2"),
    "4B": ("4-1","4-2"),
    "4C": ("5-1","5-2","5-3"),
    "4D": ("6-1","6-2","6-3","6-4")
}
for skill, project_ids in books.items():
    chapter = next((ROOT / "curriculum/c-programming").glob(skill + "-*.md"))
    chapter_text = chapter.read_text(encoding="utf8")
    assert "must be added to this repository" not in chapter_text
    for p in project_ids:
        d = ROOT / "lessons" / skill / "projects" / ("project-" + p)
        for path in ("README.md","package.json","wscript","src/c/main.c"):
            assert (d / path).is_file(), d / path
        assert "project-" + p in chapter_text, p
for letter in "ABCDEFGH":
    key = "4" + letter
    assert list((ROOT / "curriculum/c-programming").glob(key + "-*.md")), key
    assert (ROOT / "lessons" / key / "README.md").is_file()
assert (ROOT / "SYLLABUS.pdf").is_file()
print(f"PASS: {len(tasks)} activities, {projects} Emery projects, {minutes//60}h {minutes%60:02d}m")
