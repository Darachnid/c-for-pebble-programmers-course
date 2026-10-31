# 3B — Design a font-cycling algorithm

**Skill:** Algorithmic Thinking · **Estimate:** 30m · **Difficulty:** Medium · **Priority:** Medium · **Prerequisites:** 3A, 5B

**Companion reading:** [3B in the algorithmic thinking guide](../../curriculum/algorithmic-thinking/README.md). Define wrapping rules and trace both ends of the selector. Use this lesson's local starter; the reading is preparation, not a completed answer.

## Exact local example

- [`starter/`](./starter/) — Independent Emery font-selection watchapp with Up/Down click handlers and APP_LOG diagnostics.

Use the local example as a reference. Make your own decisions and retain the evidence requested by this lesson.

## Your task

Before editing code, write pseudocode for cycling through a list of fonts in both directions. Define how the selected font is represented, what Up and Down do, whether the list wraps at either end, and how the screen is refreshed. Work through the first item, last item, and a one-item list. Keep this as an algorithm-design exercise; do not implement it yet.

## Completion evidence

Pseudocode and a small flowchart cover both directions, normal selection, and boundary cases.

## Build the starter

From the repository root:

```sh
cd lessons/3B/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
