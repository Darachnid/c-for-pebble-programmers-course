# 8J — Vibration

**Project:** Field Instrument · **Estimate:** 45m · **Prerequisites:** 8I, 8C · **Platform:** Emery only, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 8I → 8J → independent capstone. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`vibes_short_pulse, VibePattern` — [Official C API reference](https://developer.repebble.com/docs/c/User_Interface/Vibes/).

## Activity

Add optional vibration to a deliberate user action; never vibrate on startup or continuously for sensor data.

## Evidence-based completion

Explicit trigger and off mode are demonstrated; no repeated unintended feedback. Provide: original code diff, emulator build/run screenshot or log, independent API explanation, a normal test, a boundary/failure test, and a note about subscription/unsubscription or allocation/destruction as appropriate. **No AI-written solutions.**

## Run

```sh
cd lessons/8J/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
