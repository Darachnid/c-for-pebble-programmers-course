# 8N — Phone communication

**Project:** Pocket Field Guide · **Estimate:** 120m · **Prerequisites:** 8L, 4H, 7B · **Platform:** Emery only, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 8L → 8N → independent capstone. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`AppMessage, DictionaryIterator, PebbleKit JS` — [Official C API reference](https://developer.repebble.com/docs/c/Foundation/AppMessage/).

## Activity

Implement watch-to-phone request and phone-to-watch reply starting from src/js/app.js and the messageKeys manifest; keep offline fallback.

## Evidence-based completion

Two-way log with success, failure and invalid payload behavior; no required continuous connection. Provide: original code diff, emulator build/run screenshot or log, independent API explanation, a normal test, a boundary/failure test, and a note about subscription/unsubscription or allocation/destruction as appropriate. **No AI-written solutions.**

## Run

```sh
cd lessons/8N/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
