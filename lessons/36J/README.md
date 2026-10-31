# 36J — Vibration

**Primary competency:** Debugging and Testing · **Supporting competency:** UI Design · **Estimate:** 45m · **Prerequisites:** 30G, 24H · **Platform:** Emery, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 35I → 36J → independent capstone. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## Implemented vs. assigned

**Inherited checkpoint:** XYZ throttling, explicit compass statuses and Up-requested backlight are implemented. **Your work:** opt-in vibration with an off mode and negative tests. This starter contains prior 34H/35I work for project continuity even though those lessons are not formal Taskwarrior prerequisites.

## SDK APIs

`vibes_short_pulse, VibePattern` — [Official C API reference](https://developer.repebble.com/docs/c/User_Interface/Vibes/).

## Activity

Hypothesize and test false or repeated vibration triggers, then add opt-in feedback for a deliberate user action and an off mode.

## Evidence-based completion

A written negative test demonstrates no unintended continuous vibration; deliberate and off states both work. Score **both primary and supporting competencies at 2 or 3** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). Keep an independent API explanation, original Git diff, running evidence, normal and failure/boundary tests, and a brief reflection. Do not treat emulator-only logs as hardware verification.

## Run

```sh
cd lessons/36J/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 2A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
