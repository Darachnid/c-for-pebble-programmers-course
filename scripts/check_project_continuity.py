#!/usr/bin/env python3
"""Static guards for *illustrative* cumulative Emery starter checkpoints.

This checks that later starters preserve required source-level patterns and
that today's assigned API work is still left to the learner. It does NOT
compile the Pebble SDK, simulate hardware or establish runtime correctness.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "lessons"

def starter(key: str) -> str:
    path = LESSONS / key / "starter" / "src" / "c" / "main.c"
    assert path.is_file(), f"Missing starter source: {path}"
    return path.read_text(encoding="utf-8")

def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

# Clock Workshop — inherited two-window access, bounded interaction, safe timer.
clock_c = starter("8C")
check("window_stack_push(s_main,false)" in clock_c and
      "window_stack_push(s_detail,true)" in clock_c,
      "8C must allow opening both windows without already implementing Select")
check("window_single_click_subscribe(" not in clock_c,
      "8C must leave its button implementation to the student")
for lesson in ("8K", "8M"):
    src = starter(lesson)
    check("s_count<99" in src and "if(s_count>0)" in src,
          f"{lesson} lost the previously bounded counter")
    check("BUTTON_ID_UP" in src and "BUTTON_ID_SELECT" in src,
          f"{lesson} lost the three 8C button callbacks")
check("app_timer_register(" not in starter("8K"),
      "8K's AppTimer assignment was accidentally completed in the starter")
check("app_timer_register(" in starter("8M") and
      "app_timer_cancel(" in starter("8M"),
      "8M lost the prior AppTimer lifecycle")
check("persist_write_int(" not in starter("8M"),
      "8M's persistence assignment must remain the student's work")

# Field Instrument — retain rate-limited accel and explicit compass status.
for lesson in ("8H", "8I", "8J"):
    src = starter(lesson)
    check("s_last_accel_draw" in src and
          re.search(r"if\s*\(\s*now\s*!=\s*s_last_accel_draw\s*\)", src) is not None,
          f"{lesson} lost 8G accelerometer display throttling")
    check("accel_data_service_unsubscribe();" in src,
          f"{lesson} lost accelerometer cleanup")
check("compass_service_subscribe(" not in starter("8H"),
      "8H's compass assignment must remain open")
for lesson in ("8I", "8J"):
    src = starter(lesson)
    for status in ("CompassStatusUnavailable","CompassStatusDataInvalid",
                   "CompassStatusCalibrating","CompassStatusCalibrated"):
        check(status in src, f"{lesson} fails to preserve {status}")
    check("#ifdef PBL_COMPASS" in src and "compass_service_unsubscribe();" in src,
          f"{lesson} lost guarded compass service lifecycle")
check("light_enable_interaction(" not in starter("8I"),
      "8I's backlight task must remain open")
check("light_enable_interaction(" in starter("8J"),
      "8J lost prior backlight behavior")
check("vibes_short_pulse(" not in starter("8J") and
      "vibes_enqueue_custom_pattern(" not in starter("8J"),
      "8J's vibration task must remain open")

# Pocket Field Guide — selection must drive display; later layers accumulate.
for lesson in ("8E","8F","8L","8N"):
    src = starter(lesson)
    check("s_selected=i->row;" in src and "layer_mark_dirty(s_canvas)" in src,
          f"{lesson} lost selection-driven canvas redraw")
    check("18+(s_selected%3)*4" in src,
          f"{lesson} lost the changing primitive from 8D")
check("gpath_create(" not in starter("8E"),
      "8E's graphics-path assignment must remain open")
for lesson in ("8F", "8L", "8N"):
    check("gpath_move_to(" in starter(lesson),
          f"{lesson} lost 8E graphics-path movement")
check("gbitmap_create_blank(" not in starter("8F"),
      "8F's bitmap assignment must remain open")
for lesson in ("8L", "8N"):
    check("gbitmap_create_blank(" in starter(lesson) and
          "paint_bitmap();" in starter(lesson),
          f"{lesson} lost 8F bitmap pattern")
check("resource_get_handle(" not in starter("8L"),
      "8L's resource-loading task must remain open")
check("resource_get_handle(" in starter("8N"),
      "8N lost the earlier bundled-resource pattern")
check("app_message_open(" not in starter("8N"),
      "8N's phone protocol must remain the student's task")

# Early C course: each exercise distinguishes SDK scaffolding and C edits.
for prefix, count in (("4A",2),("4B",2),("4C",3),("4D",4)):
    folders = sorted((LESSONS/prefix/"projects").glob("project-*"))
    check(len(folders) == count, f"{prefix} has {len(folders)} projects, expected {count}")
    for project in folders:
        readme = (project/"README.md").read_text(encoding="utf-8")
        check("## API scaffolding: provided, not assessed here" in readme,
              f"{project} lacks C/API scope distinction")
        check("sdk-scaffolding.md" in readme,
              f"{project} does not link just-in-time primer")
for path in ("curriculum/c-programming/sdk-scaffolding.md",
             "curriculum/pebble-api/checkpoint-continuity.md"):
    check((ROOT/path).is_file(), f"Missing course-continuity documentation: {path}")

print("PASS: three cumulative example strands and eleven C scaffolding guides")
