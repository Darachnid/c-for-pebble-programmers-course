# 8N — Phone communication

**Primary competency:** Development Tools and Workflow · **Supporting competency:** C Programming · **Estimate:** 120m · **Prerequisites:** 8L, 4H, 7B · **Platform:** Emery, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 8L → 8N → independent capstone. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`AppMessage, DictionaryIterator, PebbleKit JS` — [Official C API reference](https://developer.repebble.com/docs/c/Foundation/AppMessage/).

## Activity

Implement reproducible two-way AppMessage/PebbleKit JS with watch/phone logs, documented message-key contracts and offline fallback.

## Evidence-based completion

A verified two-way round trip, failure handling and reproducible setup/log record. Score **both primary and supporting competencies at 2 or 3** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). Keep an independent API explanation, original Git diff, running evidence, normal and failure/boundary tests, and a brief reflection. Do not treat emulator-only logs as hardware verification.

## Run

```sh
cd lessons/8N/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
