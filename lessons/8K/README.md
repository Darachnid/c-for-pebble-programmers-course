# 8K — App timers

**Project:** Clock Workshop · **Estimate:** 75m · **Prerequisites:** 8C, 4H · **Platform:** Emery only, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 8C → 8K → 8M. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`app_timer_register, app_timer_cancel` — [Official C API reference](https://developer.repebble.com/docs/c/Foundation/Timer/).

## Activity

Add a one-second elapsed counter to Clock Workshop while retaining minute tick for clock time. Reschedule/cancel safely.

## Evidence-based completion

One running timer, correct elapsed output, and no callback after cleanup. Provide: original code diff, emulator build/run screenshot or log, independent API explanation, a normal test, a boundary/failure test, and a note about subscription/unsubscription or allocation/destruction as appropriate. **No AI-written solutions.**

## Run

```sh
cd lessons/8K/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
