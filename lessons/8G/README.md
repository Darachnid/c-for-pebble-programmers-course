# 8G — Accelerometer

**Project:** Field Instrument · **Estimate:** 90m · **Prerequisites:** 8C, 4H · **Platform:** Emery only, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 7A → 8G → 8H. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`accel_data_service_subscribe, AccelData` — [Official C API reference](https://developer.repebble.com/docs/c/Foundation/Event_Service/AccelerometerService/).

## Activity

Subscribe to batched XYZ motion samples, rate-limit display and unsubscribe during shutdown.

## Evidence-based completion

Hardware data or a documented emulator limitation with sample logs, rate, and cleanup. Provide: original code diff, emulator build/run screenshot or log, independent API explanation, a normal test, a boundary/failure test, and a note about subscription/unsubscription or allocation/destruction as appropriate. **No AI-written solutions.**

## Run

```sh
cd lessons/8G/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
