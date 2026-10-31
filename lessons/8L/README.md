# 8L — Resource files

**Project:** Pocket Field Guide · **Estimate:** 65m · **Prerequisites:** 8F, 5C · **Platform:** Emery only, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 8F → 8L → 8N. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`resource_get_handle, resource_size, resource_load` — [Official C API reference](https://developer.repebble.com/docs/c/Foundation/Resources/).

## Activity

Bundle a raw field-note resource and read it with bounded NUL-terminated storage; compare read-only resources and persistent data.

## Evidence-based completion

Raw file is loaded without overflow; truncation and empty cases are considered. Provide: original code diff, emulator build/run screenshot or log, independent API explanation, a normal test, a boundary/failure test, and a note about subscription/unsubscription or allocation/destruction as appropriate. **No AI-written solutions.**

## Run

```sh
cd lessons/8L/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.
