# 25C — Design a multi-mode Pebble interface

**Skill:** UI Design · **Estimate:** 90m · **Difficulty:** High · **Priority:** Medium · **Prerequisites:** 13B, 22C, 23C, 24H

## Competency checkpoint

**Primary:** UI Design · **Supporting:** Idea Generation. Before editing, predict how the design supports glanceability and button/navigation clarity; then verify on the 200x228 canvas. After the activity, provide evidence for the stated completion criterion, explain the supporting competency in your own words, and self-score **both** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This checkpoint clarifies how the existing assignment is assessed; it does not add a new exercise.


**Companion reading:** [25C in the ui design guide](../../curriculum/ui-design/README.md). Give every screen a visible hierarchy and every button a defined action. Use the local starter below; the reading is preparation, not a replacement project.

## Exact local example

- [`starter/`](./starter/) — Exact C source from official MIT-licensed Pebble Simplicity example, adapted Emery-only manifest.

Pebble Simplicity C code is copied unchanged from the MIT-licensed upstream; the package.json is adapted for Emery.

## Your task

Using your concept from 22C and the state diagram from 23C, draw each interface mode for the Emery 200x228 rectangular screen. Use layouts from the included simple examples as starting references, but develop your own visual hierarchy and navigation.

## Completion evidence

A set of labeled sketches covers every main state, navigation between states, button outcomes, and screen-size considerations.

## Build the starter

From the repository root:

```sh
cd lessons/25C/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
