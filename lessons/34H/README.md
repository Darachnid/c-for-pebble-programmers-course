# 34H — Magnetometer / compass

**Primary competency:** Resource Literacy · **Supporting competency:** C Programming · **Estimate:** 90m · **Prerequisites:** 30G · **Platform:** Emery, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 30G → 34H → 35I. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## Implemented vs. assigned

**Inherited 30G checkpoint:** Latest XYZ samples are retained but accelerometer-driven display refresh occurs at most **once per clock second**. Unsubscription is implemented. **Your work:** implement CompassService and distinguish unavailable, calibrating and valid states. Preserve the throttle.

## SDK APIs

`PBL_COMPASS, CompassService` — [Official C API reference](https://developer.repebble.com/docs/c/Foundation/Event_Service/CompassService/).

## Activity

Add magnetic heading with CompassService; show unavailable/calibrating/valid states and guard unavailable hardware.

## Evidence-based completion

Heading/calibration on supported hardware, otherwise a guarded unavailable report. Score **both primary and supporting competencies at 2 or 3** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). Keep an independent API explanation, original Git diff, running evidence, normal and failure/boundary tests, and a brief reflection. Do not treat emulator-only logs as hardware verification.

## Run

```sh
cd lessons/34H/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 2A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.

**Limit:** Magnetometer data is mediated through CompassService, with calibration and a PBL_COMPASS compile-time guard.
