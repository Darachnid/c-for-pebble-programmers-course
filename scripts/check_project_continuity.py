#!/usr/bin/env python3
"""Static guards for *illustrative* cumulative Emery/Gabbro starter checkpoints.

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
clock_c = starter("27C")
check("window_stack_push(s_main,false)" in clock_c and
      "window_stack_push(s_detail,true)" in clock_c,
      "27C must allow opening both windows without already implementing Select")
check("window_single_click_subscribe(" not in clock_c,
      "27C must leave its button implementation to the student")
for lesson in ("37K", "39M"):
    src = starter(lesson)
    check("s_count<99" in src and "if(s_count>0)" in src,
          f"{lesson} lost the previously bounded counter")
    check("BUTTON_ID_UP" in src and "BUTTON_ID_SELECT" in src,
          f"{lesson} lost the three 27C button callbacks")
check("app_timer_register(" not in starter("37K"),
      "37K's AppTimer assignment was accidentally completed in the starter")
check("app_timer_register(" in starter("39M") and
      "app_timer_cancel(" in starter("39M"),
      "39M lost the prior AppTimer lifecycle")
check("persist_write_int(" not in starter("39M"),
      "39M's persistence assignment must remain the student's work")

# Field Instrument — retain rate-limited accel and explicit compass status.
for lesson in ("34H", "35I", "36J"):
    src = starter(lesson)
    check("s_last_accel_draw" in src and
          re.search(r"if\s*\(\s*now\s*!=\s*s_last_accel_draw\s*\)", src) is not None,
          f"{lesson} lost 30G accelerometer display throttling")
    check("accel_data_service_unsubscribe();" in src,
          f"{lesson} lost accelerometer cleanup")
check("compass_service_subscribe(" not in starter("34H"),
      "34H's compass assignment must remain open")
for lesson in ("35I", "36J"):
    src = starter(lesson)
    for status in ("CompassStatusUnavailable","CompassStatusDataInvalid",
                   "CompassStatusCalibrating","CompassStatusCalibrated"):
        check(status in src, f"{lesson} fails to preserve {status}")
    check("#ifdef PBL_COMPASS" in src and "compass_service_unsubscribe();" in src,
          f"{lesson} lost guarded compass service lifecycle")
check("light_enable_interaction(" not in starter("35I"),
      "35I's backlight task must remain open")
check("light_enable_interaction(" in starter("36J"),
      "36J lost prior backlight behavior")
check("vibes_short_pulse(" not in starter("36J") and
      "vibes_enqueue_custom_pattern(" not in starter("36J"),
      "36J's vibration task must remain open")

# Pocket Field Guide — selection must drive display; later layers accumulate.
for lesson in ("29E","33F","38L","40N"):
    src = starter(lesson)
    check("s_selected=i->row;" in src and "layer_mark_dirty(s_canvas)" in src,
          f"{lesson} lost selection-driven canvas redraw")
    check("18+(s_selected%3)*4" in src,
          f"{lesson} lost the changing primitive from 28D")
check("gpath_create(" not in starter("29E"),
      "29E's graphics-path assignment must remain open")
for lesson in ("33F", "38L", "40N"):
    check("gpath_move_to(" in starter(lesson),
          f"{lesson} lost 29E graphics-path movement")
check("gbitmap_create_blank(" not in starter("33F"),
      "33F's bitmap assignment must remain open")
for lesson in ("38L", "40N"):
    check("gbitmap_create_blank(" in starter(lesson) and
          "paint_bitmap();" in starter(lesson),
          f"{lesson} lost 33F bitmap pattern")
check("resource_get_handle(" not in starter("38L"),
      "38L's resource-loading task must remain open")
check("resource_get_handle(" in starter("40N"),
      "40N lost the earlier bundled-resource pattern")
check("app_message_open(" not in starter("40N"),
      "40N's phone protocol must remain the student's task")

# Early C course: each exercise distinguishes SDK scaffolding and C edits.
for prefix, count in (("3A",2),("8B",2),("9C",3),("10D",4)):
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
