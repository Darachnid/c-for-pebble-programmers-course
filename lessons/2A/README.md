# 2A — Build and run a time-only C watchface

**Skill:** Development Tools and Workflow · **Estimate:** 30m · **Difficulty:** Low · **Priority:** High · **Prerequisites:** None

## Competency checkpoint

**Primary:** Development Tools and Workflow · **Supporting:** C Programming. Preserve a known-good baseline, make verifiable commits, and explain how logs/Git make the change reproducible. Independently explain both competencies and self-score them at 0–3 using the [common rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). The original exercise and its completion evidence remain unchanged.


**Companion reading:** [2A in the tools workflow guide](../../curriculum/tools-workflow/README.md). Identify the project root and distinguish build, install and observation. Complete the assignment using its provided local Emery project.

## Exact local example

- [`starter/`](./starter/) — One-text-layer Emery watchface; time only. It intentionally does not include a date.

This watchface has only the time; do not add a date yet.

## Your task

Create a new C project with the CURRENT watchface tutorial for SDK 4. Set package.json targetPlatforms to ["emery"]. Follow the tutorial through Displaying the Time and STOP before Adding the Date. Run pebble build then pebble install --emulator emery; confirm time updates and only one TextLayer exists. Identify project structure and build output.

## Completion evidence

The project builds and runs in the emulator, displays the current time, updates by minute, and has no date TextLayer.

## Build the starter

From the repository root:

```sh
cd lessons/2A/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
