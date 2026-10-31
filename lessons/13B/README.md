# 13B — Add and style a date TextLayer

**Skill:** UI Design · **Estimate:** 45m · **Difficulty:** Medium · **Priority:** Medium · **Prerequisites:** 5A, 10D, 4A

## Competency checkpoint

**Primary:** UI Design · **Supporting:** C Programming. Before editing, predict how the design supports glanceability and button/navigation clarity; then verify on the 200x228 canvas. After the activity, provide evidence for the stated completion criterion, explain the supporting competency in your own words, and self-score **both** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This checkpoint clarifies how the existing assignment is assessed; it does not add a new exercise.


**Companion reading:** [13B in the ui design guide](../../curriculum/ui-design/README.md). Sketch both text-layer rectangles before choosing their positions. Use the local starter below; the reading is preparation, not a replacement project.

## Exact local example

- [`starter/`](./starter/) — One-text-layer Emery watchface; time only. It intentionally does not include a date.

Add the date TextLayer yourself; the date is deliberately omitted from the starting source.

## Your task

From YOUR time-only emery code, follow the Adding the Date section of the current C tutorial to create, style, position, update, and unload a second TextLayer. Arrange time and date for the Emery 200x228 screen. Build and install on emery. Do not switch to a completed repository.

## Completion evidence

The watchface displays both time and date, both update correctly, and you can explain how the date layer is created, styled, attached, updated, and destroyed.

## Build the starter

From the repository root:

```sh
cd lessons/13B/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
