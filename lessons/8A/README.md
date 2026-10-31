# 8A — Windows and layers

**Project:** Clock Workshop · **Estimate:** 60m · **Prerequisites:** 7A, 3A · **Platform:** Emery only, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 7A → 8A → 8C. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`window_create, WindowHandlers, Layer` — [Official C API reference](https://developer.repebble.com/docs/c/User_Interface/Window/).

## Activity

Extend the time-only watchapp with a second Window and root/child layers; trace create/load/unload/destroy.

## Evidence-based completion

Both screens can be displayed; illustrate layer hierarchy and clean teardown. Provide: original code diff, emulator build/run screenshot or log, independent API explanation, a normal test, a boundary/failure test, and a note about subscription/unsubscription or allocation/destruction as appropriate. **No AI-written solutions.**

## Run

```sh
cd lessons/8A/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
