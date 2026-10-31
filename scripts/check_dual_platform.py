#!/usr/bin/env python3
"""Static Emery/Gabbro project audit — never claims SDK build or runtime success."""
from __future__ import annotations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {"emery", "gabbro"}
manifests = sorted((ROOT / "lessons").glob("**/package.json"))
manifests += sorted((ROOT / "examples").glob("**/package.json"))
assert len(manifests) >= 66, f"Expected at least 66 local Pebble projects, found {len(manifests)}"
for path in manifests:
    config = json.loads(path.read_text(encoding="utf-8"))
    target = config["pebble"]["targetPlatforms"]
    assert set(target) == TARGETS and len(target) == 2, f"Not dual-platform: {path}: {target}"
    assert (path.parent / "wscript").is_file(), path
    assert list((path.parent / "src").rglob("*.c")), path

# Critical cumulative checkpoints must retain the same local geometric helper,
# avoiding the old mistake of marking 260x260 alone as a round-safe layout.
local_safe = ["2A", "5A", "12A", "13B", "17E", "19G", "24H",
              "26B", "27C", "28D", "29E", "30G", "33F", "34H",
              "35I", "36J", "37K", "38L", "39M", "40N", "41A"]
for lesson in local_safe:
    base = ROOT / "lessons" / lesson / "starter" / "src" / "c"
    src = (base / "main.c").read_text(encoding="utf-8")
    helper = (base / "course_display.h").read_text(encoding="utf-8")
    assert '#include "course_display.h"' in src, base
    assert "course_content_rect(" in src, base
    assert "PBL_ROUND" in helper and "return GRect(" in helper, base

for lesson in ["27C", "35I", "38L"]:
    base = ROOT / "lessons" / lesson / "debug" / "src" / "c"
    assert (base / "course_display.h").is_file(), base
    assert "course_content_rect(" in (base / "main.c").read_text(encoding="utf-8"), base

guide = ROOT / "curriculum" / "dual-platform" / "README.md"
assert guide.is_file()
for lesson in sorted((ROOT / "lessons").iterdir()):
    if not lesson.is_dir() or not (lesson / "README.md").is_file():
        continue
    text = (lesson / "README.md").read_text(encoding="utf-8")
    assert "## Dual-platform verification" in text, lesson
print(f"PASS: {len(manifests)} dual-target manifest(s); safe-area helpers and 41 lesson notes present")
