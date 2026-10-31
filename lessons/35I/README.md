# 35I — Ambient-light limits and backlight

**Primary competency:** Resource Literacy · **Supporting competency:** UI Design · **Estimate:** 45m · **Prerequisites:** 30G, 20C · **Platform:** Emery, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 34H → 35I → 36J. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## Implemented vs. assigned

**Inherited 30G/34H checkpoint:** XYZ refresh is throttled. Compass status distinguishes unavailable, calibrating with invalid data, calibrating with usable data, and calibrated/valid under `PBL_COMPASS`. **Your work:** research the Light API and add a deliberate backlight action; no backlight handler is in this starter.

## SDK APIs

`light_enable_interaction, light_is_on` — [Official C API reference](https://developer.repebble.com/docs/c/User_Interface/Light/).

## Activity

Add user-triggered backlight interaction. Explicitly distinguish the public backlight API from unavailable raw lux readings.

## Evidence-based completion

Backlight interaction works and API note explains the ambient-light measurement limitation. Score **both primary and supporting competencies at 2 or 3** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). Keep an independent API explanation, original Git diff, running evidence, normal and failure/boundary tests, and a brief reflection. Do not treat emulator-only logs as hardware verification.

## Run

```sh
cd lessons/35I/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 2A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.

**Limit:** The documented C Light API controls the backlight; it does not return ambient lux.

## Optional debugging checkpoint

After finishing this lesson, open [debug/](debug/) for an **intentionally defective complete Emery project**. Reproduce its symptom, record diagnostics, repair the minimum cause, and add a regression test. The defect is not revealed here; do not treat the debug version as the next lesson starter.
