# 4B — Modify the Font Browser

**Skill:**  · **Estimate:**  · **Difficulty:**  · **Priority:**  · **Prerequisites:** 

## Exact local example

- [`starter/`](./starter/) — Independent Emery font-selection watchapp with Up/Down click handlers and APP_LOG diagnostics.

Use the local example as a reference. Make your own decisions and retain the evidence requested by this lesson.

## Your task

Start from the working local Emery font-selector watchapp. Trace its input handler, index state, and apply_font function; add one extension you design yourself (e.g., index indicator or extra preview), committing and testing after each change. This is a watchapp, so Up/Down are available.

## Completion evidence

Your modified app builds and runs, the original font browsing still works, and your added feature is visible and tested.

## Build the starter

From the repository root:

```sh
cd lessons/4B/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
