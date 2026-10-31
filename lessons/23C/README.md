# 23C — Design a state machine for an app

**Skill:** Algorithmic Thinking · **Estimate:** 60m · **Difficulty:** High · **Priority:** Medium · **Prerequisites:** 22C, 15B, 19G

## Competency checkpoint

**Primary:** Algorithmic Thinking · **Supporting:** UI Design. Predict state or loop behavior and test normal and boundary transitions with your own diagram or trace. Demonstrate the stated lesson outcome and explain your supporting skill; self-score **both** at 0–3 with the [common mastery rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This is the assessment lens for the existing lesson, not another exercise.


**Companion reading:** [23C in the algorithmic thinking guide](../../curriculum/algorithmic-thinking/README.md). Express every supported state/event pair in a transition table. Use this lesson's local starter; the reading is preparation, not a completed answer.

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
cd lessons/23C/starter
pebble build
pebble install --emulator emery
pebble install --emulator gabbro
pebble logs --emulator emery
pebble logs --emulator gabbro
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery and Gabbro** and follow the no-AI coursework rule.

## Dual-platform verification — Time 2 and Round 2

**Same activity, two displays:** [Pebble Time 2 / Emery](../../curriculum/dual-platform/README.md) uses a 200×228 rectangle; Pebble Round 2 / Gabbro uses a 260×260 circle. The existing learning outcome and competency rubric are unchanged. Any code you build should target both `emery` and `gabbro`, and you should check on both emulators for clipped text, invisible controls, and round-edge collisions. For non-coding work, account for both display geometries in your existing explanation/design—**this is not an additional assignment**.

Follow the [two-platform command and testing reference](../../curriculum/dual-platform/README.md). Compare actual results; a manifest listing two platforms is not evidence of successful compilation or physical sensor behavior. Round 2 touch is optional on watchapps; preserve button navigation and graceful touch-disabled behavior.
