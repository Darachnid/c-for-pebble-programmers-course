# 5B — Trace an existing feature through source code

**Skill:** Resource Literacy · **Estimate:** 45m · **Difficulty:** Medium · **Priority:** Medium · **Prerequisites:** 3A, 4D, 5A

**Companion reading:** [5B in the resource literacy guide](../../curriculum/resource-literacy/README.md). Trace the event handler through state change to visible result. Use this lesson's local starter; the reading is preparation, not a completed answer.

## Exact local example

- [`starter/`](./starter/) — Independent Emery font-selection watchapp with Up/Down click handlers and APP_LOG diagnostics.

Use the local example as a reference. Make your own decisions and retain the evidence requested by this lesson.

## Your task

Open the Font Browser example. Find where button input is registered or handled, identify the state that changes, and follow the code until the display is updated. Use the README and SDK docs to look up unfamiliar APIs. Write down the file/function names and draw the input -> state change -> display update path.

## Completion evidence

Your notes identify the input handling, changed state, display update, and the relevant source locations and documentation.

## Build the starter

From the repository root:

```sh
cd lessons/5B/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
