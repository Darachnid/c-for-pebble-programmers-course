# 3A — Trace the watchface lifecycle

**Skill:** Algorithmic Thinking · **Estimate:** 30m · **Difficulty:** Low · **Priority:** High · **Prerequisites:** 4D, 7A

**Companion reading:** [3A in the algorithmic thinking guide](../../curriculum/algorithmic-thinking/README.md). Distinguish direct calls from framework-triggered callbacks. Use this lesson's local starter; the reading is preparation, not a completed answer.

## Exact local example

- [`starter/`](./starter/) — One-text-layer Emery watchface; time only. It intentionally does not include a date.

Use the local example as a reference. Make your own decisions and retain the evidence requested by this lesson.

## Your task

Draw the execution flow for the time-only watchface. Include main(), init(), window_stack_push(), main_window_load(), update_time(), tick_handler(), app_event_loop(), main_window_unload(), and deinit() where applicable. Show which functions call other functions and which are callbacks. Show the separate path for a minute tick after startup.

## Completion evidence

A flow diagram shows startup, initial display, minute updates, and cleanup, with direct calls distinguished from callbacks.

## Build the starter

From the repository root:

```sh
cd lessons/3A/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
