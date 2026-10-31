# 8F — Bitmap manipulation

**Project:** Pocket Field Guide · **Estimate:** 90m · **Prerequisites:** 8E, 4F · **Platform:** Emery only, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 8E → 8F → 8L. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`GBitmap, gbitmap_get_data, gbitmap_get_bytes_per_row` — [Official C API reference](https://developer.repebble.com/docs/c/User_Interface/Layers/BitmapLayer/).

## Activity

Create a 24x24 bitmap in memory, safely alter two-color pixels by row stride, and show it in a BitmapLayer.

## Evidence-based completion

Pixels visibly change with no out-of-bounds writes; bitmap and layer are freed. Provide: original code diff, emulator build/run screenshot or log, independent API explanation, a normal test, a boundary/failure test, and a note about subscription/unsubscription or allocation/destruction as appropriate. **No AI-written solutions.**

## Run

```sh
cd lessons/8F/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
