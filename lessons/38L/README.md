# 38L — Resource files

**Primary competency:** Idea Generation · **Supporting competency:** Resource Literacy · **Estimate:** 65m · **Prerequisites:** 33F, 20C · **Platform:** Emery, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 33F → 38L → 40N. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`resource_get_handle, resource_size, resource_load` — [Official C API reference](https://developer.repebble.com/docs/c/Foundation/Resources/).

## Activity

Design an original field-note data format and explain which information belongs in bundled read-only resources, then implement bounded loading.

## Evidence-based completion

A justified original content format is loaded, with empty/truncated file handling and clear resource-versus-persistence explanation. Score **both primary and supporting competencies at 2 or 3** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). Keep an independent API explanation, original Git diff, running evidence, normal and failure/boundary tests, and a brief reflection. Do not treat emulator-only logs as hardware verification.

## Run

```sh
cd lessons/38L/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 2A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.

## Optional debugging checkpoint

After finishing this lesson, open [debug/](debug/) for an **intentionally defective complete Emery project**. Reproduce its symptom, record diagnostics, repair the minimum cause, and add a regression test. The defect is not revealed here; do not treat the debug version as the next lesson starter.
