# 8C — Button interactions

**Primary competency:** Algorithmic Thinking · **Supporting competency:** C Programming · **Estimate:** 60m · **Prerequisites:** 8A, 4H · **Platform:** Emery, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 8A → 8C → 8K. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## Implemented vs. assigned

**Inherited 8A checkpoint:** The starter opens the *detail window first*. **Back** reveals the main clock, proving both windows are viewable without implementing this lesson's Select button. **Your work:** wire Select to reopen details and implement Up/Down with counter bounds 0–99. The preview is not a shortcut for your button solution.

## SDK APIs

`window_single_click_subscribe, BUTTON_ID_SELECT` — [Official C API reference](https://developer.repebble.com/docs/c/User_Interface/Clicks/).

## Activity

Add Select to open Clock Workshop details and Up/Down to adjust a bounded counter; Back returns via window stack.

## Evidence-based completion

Three buttons and Back behave correctly, including minimum/maximum boundary cases. Score **both primary and supporting competencies at 2 or 3** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). Keep an independent API explanation, original Git diff, running evidence, normal and failure/boundary tests, and a brief reflection. Do not treat emulator-only logs as hardware verification.

## Run

```sh
cd lessons/8C/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.

## Optional debugging checkpoint

After finishing this lesson, open [debug/](debug/) for an **intentionally defective complete Emery project**. Reproduce its symptom, record diagnostics, repair the minimum cause, and add a regression test. The defect is not revealed here; do not treat the debug version as the next lesson starter.
