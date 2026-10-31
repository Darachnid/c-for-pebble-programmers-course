# 8H — Magnetometer / compass

**Project:** Field Instrument · **Estimate:** 90m · **Prerequisites:** 8G · **Platform:** Emery only, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 8G → 8H → 8I. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`PBL_COMPASS, CompassService` — [Official C API reference](https://developer.repebble.com/docs/c/Foundation/Event_Service/CompassService/).

## Activity

Add magnetic heading with CompassService; show unavailable/calibrating/valid states and guard unavailable hardware.

## Evidence-based completion

Heading/calibration on supported hardware, otherwise a guarded unavailable report. Provide: original code diff, emulator build/run screenshot or log, independent API explanation, a normal test, a boundary/failure test, and a note about subscription/unsubscription or allocation/destruction as appropriate. **No AI-written solutions.**

## Run

```sh
cd lessons/8H/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.

**Limit:** Magnetometer data is mediated through CompassService, with calibration and a PBL_COMPASS compile-time guard.
