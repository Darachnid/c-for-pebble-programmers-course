# 4C — Refactor font selection into a reusable component

**Skill:**  · **Estimate:**  · **Difficulty:**  · **Priority:**  · **Prerequisites:** 

## Exact local example

- [`starter/`](./starter/) — Independent Emery font-selection watchapp with Up/Down click handlers and APP_LOG diagnostics.

Use the local example as a reference. Make your own decisions and retain the evidence requested by this lesson.

## Your task

Using your emery-compatible Font Browser implementation, refactor selected font state and update logic into reusable functions without duplicating cases. Use current C watchface custom font tutorial Part 2 if you add font resources. Confirm correct loading/unloading. Build, install, and test on emery exclusively.

## Completion evidence

Font selection uses a reusable function and organized data, both navigation directions work, and any allocated font resources are cleaned up correctly.

## Build the starter

From the repository root:

```sh
cd lessons/4C/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
