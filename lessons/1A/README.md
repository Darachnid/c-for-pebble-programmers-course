# 1A — Change one visual property of a time-only watchface

**Skill:** UI Design · **Estimate:** 30m · **Difficulty:** Low · **Priority:** High · **Prerequisites:** 4A, 5A, 7A

## Exact local example

- [`starter/`](./starter/) — One-text-layer Emery watchface; time only. It intentionally does not include a date.

Change exactly one visual property. The source contains no date TextLayer; that feature belongs to lesson 1B.

## Your task

Start from the time-only checkpoint of the C watchface tutorial: the code after 'Displaying the Time' and before 'Adding the Date'. Choose exactly one visual property to change: font, position, alignment, text color, or background color. Make the change, build, and inspect it in the emulator. Keep the time working and do not add the date or other functionality.

## Completion evidence

The app builds and runs, the time still updates, and one intentional visual change is visible. The watchface still has no date layer.

## Build the starter

From the repository root:

```sh
cd lessons/1A/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
