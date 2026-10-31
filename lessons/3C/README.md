# 3C — Design a state machine for an app

**Skill:** Algorithmic Thinking · **Estimate:** 60m · **Difficulty:** High · **Priority:** Medium · **Prerequisites:** 2C, 3B, 4G

**Companion reading:** [3C in the algorithmic thinking guide](../../curriculum/algorithmic-thinking/README.md). Express every supported state/event pair in a transition table. Use this lesson's local starter; the reading is preparation, not a completed answer.

## Exact local example

- [`starter/`](./starter/) — Independent Emery font-selection watchapp with Up/Down click handlers and APP_LOG diagnostics.

Use the local example as a reference. Make your own decisions and retain the evidence requested by this lesson.

## Your task

Use your original emery app concept or the included local font-selector watchapp as an input-pattern reference. Enumerate states, transitions, button press behavior, screen changes, and edge cases. Create a state diagram and table. Plan for Emery input and display only.

## Completion evidence

A state diagram and transition table describe all main states, triggers, resulting states, and visible responses, including important edge cases.

## Build the starter

From the repository root:

```sh
cd lessons/3C/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
