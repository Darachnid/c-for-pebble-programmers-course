# 8B — Menus and scrolling

**Project:** Pocket Field Guide · **Estimate:** 75m · **Prerequisites:** 8A, 4E · **Platform:** Emery only, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 7A → 8B → 8D. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`MenuLayer, MenuLayerCallbacks` — [Official C API reference](https://developer.repebble.com/docs/c/User_Interface/Layers/MenuLayer/).

## Activity

Build a six-entry scrolling Field Guide menu; implement draw_row and select_click; test the first, middle, and last rows.

## Evidence-based completion

Six entries scroll smoothly and selecting a row changes the visible species. Provide: original code diff, emulator build/run screenshot or log, independent API explanation, a normal test, a boundary/failure test, and a note about subscription/unsubscription or allocation/destruction as appropriate. **No AI-written solutions.**

## Run

```sh
cd lessons/8B/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
