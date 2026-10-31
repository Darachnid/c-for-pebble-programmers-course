# 8D — Custom drawing

**Project:** Pocket Field Guide · **Estimate:** 75m · **Prerequisites:** 8B, 4D · **Platform:** Emery only, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 8B → 8D → 8E. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`layer_set_update_proc, graphics_draw_circle` — [Official C API reference](https://developer.repebble.com/docs/c/Graphics/Drawing_Primitives/).

## Activity

Use a custom Field Guide Layer to draw a symbol using primitives; change its output on a menu selection and mark dirty.

## Evidence-based completion

A visible non-clipped drawing changes on demand and you can explain the drawing callback. Provide: original code diff, emulator build/run screenshot or log, independent API explanation, a normal test, a boundary/failure test, and a note about subscription/unsubscription or allocation/destruction as appropriate. **No AI-written solutions.**

## Run

```sh
cd lessons/8D/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
