# 5A — Change one visual property of a time-only watchface

**Skill:** UI Design · **Estimate:** 30m · **Difficulty:** Low · **Priority:** High · **Prerequisites:** 3A, 4A, 2A

## Competency checkpoint

**Primary:** UI Design · **Supporting:** Resource Literacy. Before editing, predict how the design supports glanceability and button/navigation clarity; then verify on the Emery 200×228 and Gabbro 260×260 canvases. After the activity, provide evidence for the stated completion criterion, explain the supporting competency in your own words, and self-score **both** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This checkpoint clarifies how the existing assignment is assessed; it does not add a new exercise.


**Companion reading:** [5A in the ui design guide](../../curriculum/ui-design/README.md). Before editing, predict how one visual property affects glance readability. Use the local starter below; the reading is preparation, not a replacement project.

## Exact local example

- [`starter/`](./starter/) — One-text-layer Emery watchface; time only. It intentionally does not include a date.

Change exactly one visual property. The source contains no date TextLayer; that feature belongs to lesson 13B.

## Your task

Start from the time-only checkpoint of the C watchface tutorial: the code after 'Displaying the Time' and before 'Adding the Date'. Choose exactly one visual property to change: font, position, alignment, text color, or background color. Make the change, build, and inspect it in the emulator. Keep the time working and do not add the date or other functionality.

## Completion evidence

The app builds and runs, the time still updates, and one intentional visual change is visible. The watchface still has no date layer.

## Build the starter

From the repository root:

```sh
cd lessons/5A/starter
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
