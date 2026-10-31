# 30G — Accelerometer

**Primary competency:** C Programming · **Supporting competency:** Resource Literacy · **Estimate:** 90m · **Prerequisites:** 24H, 20C · **Platform:** Emery, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 2A → 30G → 34H. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`accel_data_service_subscribe, AccelData` — [Official C API reference](https://developer.repebble.com/docs/c/Foundation/Event_Service/AccelerometerService/).

## Activity

Subscribe to batched XYZ motion samples, rate-limit display and unsubscribe during shutdown.

## Evidence-based completion

Hardware data or a documented emulator limitation with sample logs, rate, and cleanup. Score **both primary and supporting competencies at 2 or 3** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). Keep an independent API explanation, original Git diff, running evidence, normal and failure/boundary tests, and a brief reflection. Do not treat emulator-only logs as hardware verification.

## Run

```sh
cd lessons/30G/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 2A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
