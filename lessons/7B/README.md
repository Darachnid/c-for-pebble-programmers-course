# 7B — Create a Git-based modification workflow

**Skill:** Development Tools and Workflow · **Estimate:** 45m · **Difficulty:** Medium · **Priority:** High · **Prerequisites:** 7A, 1A, 6A

**Companion reading:** [7B in the tools workflow guide](../../curriculum/tools-workflow/README.md). Keep baseline and edited commits distinct and inspect the diff. Complete the assignment using its provided local Emery project.

## Exact local example

- [`starter/`](./starter/) — One-text-layer Emery watchface; time only. It intentionally does not include a date.

Use the local example as a reference. Make your own decisions and retain the evidence requested by this lesson.

## Your task

Create your own working copy of the example; do not edit the reference repository in place. Initialize or use a Git repository, commit the known-good starting point, make one small visual modification, build and test it, then commit the working change with a meaningful message. Confirm you can inspect the diff and return to the earlier version.

## Completion evidence

The repository has a baseline commit and a modification commit, the app builds, and you have inspected the diff or demonstrated how to restore the baseline.

## Build the starter

From the repository root:

```sh
cd lessons/7B/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
