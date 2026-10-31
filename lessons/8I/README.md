# 8I — Ambient-light limits and backlight

**Project:** Field Instrument · **Estimate:** 45m · **Prerequisites:** 8H, 5C · **Platform:** Emery only, SDK 4.33.1

## Exact local example

The [starter/](starter/) folder contains a full `package.json`, `wscript`, `src/c/main.c` and any extra resources needed. It is a **prior-stage checkpoint**, not the solution to the current exercise. Start here instead of cloning an external repository.

**Project history:** 8H → 8I → 8J. Commit your own solution in a separate Git working branch/copy. Later reference checkpoints illustrate completed earlier features; do not simply copy them backwards.

## SDK APIs

`light_enable_interaction, light_is_on` — [Official C API reference](https://developer.repebble.com/docs/c/User_Interface/Light/).

## Activity

Add user-triggered backlight interaction. Explicitly distinguish the public backlight API from unavailable raw lux readings.

## Evidence-based completion

Backlight interaction works and API note explains the ambient-light measurement limitation. Provide: original code diff, emulator build/run screenshot or log, independent API explanation, a normal test, a boundary/failure test, and a note about subscription/unsubscription or allocation/destruction as appropriate. **No AI-written solutions.**

## Run

```sh
cd lessons/8I/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Compatibility:** These are watchapps, since watchfaces cannot receive button events. The watchface in lesson 7A remains unchanged. Sensor fidelity and phone-to-watch connection may require a real device; emulator launch alone does not prove physical sensor or phone communication functionality.

**Limit:** The documented C Light API controls the backlight; it does not return ambient lux.

## Optional debugging checkpoint

After finishing this lesson, open [debug/](debug/) for an **intentionally defective complete Emery project**. Reproduce its symptom, record diagnostics, repair the minimum cause, and add a regression test. The defect is not revealed here; do not treat the debug version as the next lesson starter.
