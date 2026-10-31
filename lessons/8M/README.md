# 8M — Persistent storage

**Primary competency:** Development Tools and Workflow · **Supporting competency:** Debugging and Testing · **Estimate:** 75m · **Prerequisites:** 8K, 4H · **Platform:** Emery, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 8K → 8M → independent capstone. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`persist_exists, persist_read_int, persist_write_int` — [Official C API reference](https://developer.repebble.com/docs/c/Foundation/Storage/).

## Activity

Version and test persistent Clock Workshop settings with a documented clean/restart/corruption matrix and milestone commits.

## Evidence-based completion

Absent, valid, invalid, restart and reset scenarios pass; source and logs are versioned without per-second writes. Score **both primary and supporting competencies at 2 or 3** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). Keep an independent API explanation, original Git diff, running evidence, normal and failure/boundary tests, and a brief reflection. Do not treat emulator-only logs as hardware verification.

## Run

```sh
cd lessons/8M/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
