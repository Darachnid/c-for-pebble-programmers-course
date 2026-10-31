# 33F — Bitmap manipulation

**Primary competency:** C Programming · **Supporting competency:** Debugging and Testing · **Estimate:** 90m · **Prerequisites:** 29E, 18F · **Platform:** Emery, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 29E → 33F → 38L. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`GBitmap, gbitmap_get_data, gbitmap_get_bytes_per_row` — [Official C API reference](https://developer.repebble.com/docs/c/User_Interface/Layers/BitmapLayer/).

## Activity

Create a 24x24 bitmap in memory, safely alter two-color pixels by row stride, and show it in a BitmapLayer.

## Evidence-based completion

Pixels visibly change with no out-of-bounds writes; bitmap and layer are freed. Score **both primary and supporting competencies at 2 or 3** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). Keep an independent API explanation, original Git diff, running evidence, normal and failure/boundary tests, and a brief reflection. Do not treat emulator-only logs as hardware verification.

## Run

```sh
cd lessons/33F/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 2A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
