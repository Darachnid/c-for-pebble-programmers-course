# 8D — Custom drawing

**Primary competency:** Idea Generation · **Supporting competency:** UI Design · **Estimate:** 75m · **Prerequisites:** 8B, 4D · **Platform:** Emery, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 8B → 8D → 8E. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`layer_set_update_proc, graphics_draw_circle` — [Official C API reference](https://developer.repebble.com/docs/c/Graphics/Drawing_Primitives/).

## Activity

Compare two original field-symbol designs and justify one for legibility at Emery size. Implement it with primitive drawing and a menu-triggered redraw.

## Evidence-based completion

Two original visual alternatives are compared; a chosen symbol redraws on selection and its layout is readable. Score **both primary and supporting competencies at 2 or 3** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). Keep an independent API explanation, original Git diff, running evidence, normal and failure/boundary tests, and a brief reflection. Do not treat emulator-only logs as hardware verification.

## Run

```sh
cd lessons/8D/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
