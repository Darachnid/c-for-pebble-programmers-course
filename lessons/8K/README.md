# 8K — App timers

**Primary competency:** Debugging and Testing · **Supporting competency:** Algorithmic Thinking · **Estimate:** 75m · **Prerequisites:** 8C, 4H · **Platform:** Emery, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 8C → 8K → 8M. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`app_timer_register, app_timer_cancel` — [Official C API reference](https://developer.repebble.com/docs/c/Foundation/Timer/).

## Activity

Investigate re-entrancy and timer-lifetime risks while adding a one-second elapsed counter beside minute tick updates.

## Evidence-based completion

One active AppTimer, correct output, canceled teardown, and a rapid-navigation or restart regression test. Score **both primary and supporting competencies at 2 or 3** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). Keep an independent API explanation, original Git diff, running evidence, normal and failure/boundary tests, and a brief reflection. Do not treat emulator-only logs as hardware verification.

## Run

```sh
cd lessons/8K/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
