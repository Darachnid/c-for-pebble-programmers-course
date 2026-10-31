# 8C — Button interactions

**Project:** Clock Workshop · **Estimate:** 60m · **Prerequisites:** 8A, 4H · **Platform:** Emery only, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 8A → 8C → 8K. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`window_single_click_subscribe, BUTTON_ID_SELECT` — [Official C API reference](https://developer.repebble.com/docs/c/User_Interface/Clicks/).

## Activity

Add Select to open Clock Workshop details and Up/Down to adjust a bounded counter; Back returns via window stack.

## Evidence-based completion

Three buttons and Back behave correctly, including minimum/maximum boundary cases. Provide: original code diff, emulator build/run screenshot or log, independent API explanation, a normal test, a boundary/failure test, and a note about subscription/unsubscription or allocation/destruction as appropriate. **No AI-written solutions.**

## Run

```sh
cd lessons/8C/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
