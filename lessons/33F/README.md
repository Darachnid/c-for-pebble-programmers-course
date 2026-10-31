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
pebble install --emulator gabbro
pebble logs --emulator emery
pebble logs --emulator gabbro
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 2A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.

## Dual-platform verification — Time 2 and Round 2

**Same activity, two displays:** [Pebble Time 2 / Emery](../../curriculum/dual-platform/README.md) uses a 200×228 rectangle; Pebble Round 2 / Gabbro uses a 260×260 circle. The existing learning outcome and competency rubric are unchanged. Any code you build should target both `emery` and `gabbro`, and you should check on both emulators for clipped text, invisible controls, and round-edge collisions. For non-coding work, account for both display geometries in your existing explanation/design—**this is not an additional assignment**.

Follow the [two-platform command and testing reference](../../curriculum/dual-platform/README.md). Compare actual results; a manifest listing two platforms is not evidence of successful compilation or physical sensor behavior. Round 2 touch is optional on watchapps; preserve button navigation and graceful touch-disabled behavior.
