# 6A — Diagnose a simple compiler error

**Skill:** Debugging and Testing · **Estimate:** 20m · **Difficulty:** Low · **Priority:** High · **Prerequisites:** 4A, 7A

## Competency checkpoint

**Primary:** Debugging and Testing · **Supporting:** Development Tools and Workflow. Separate symptom from cause, record a reproducible hypothesis and a minimal correction, and run a regression test. Retain the original assignment's required output, and self-score **both competencies** at 0–3 using the [common rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This check adds no new independent activity.


**Companion reading:** [6A in the debugging testing guide](../../curriculum/debugging-testing/README.md). Capture the first compiler diagnostic before touching source; no error solution is given here. Complete the assignment using its provided local Emery project.

## Exact local example

- [`starter/`](./starter/) — Deliberately malformed time-only C source. Initial compilation is supposed to fail.

Compile, capture the first compiler diagnostic, identify a syntax error, make the smallest correction and rebuild. No answer key.

## Your task

Start from the deliberately flawed lessons/6A/starter project. Run pebble build; capture the first compiler diagnostic; identify and correct the single syntax fault; rebuild and run on emery. The original clean time-only example is for comparison AFTER the diagnosis.

## Completion evidence

You can show the original error, identify its cause, fix it, and produce a successful build.

## Debugging diagnostics

Start with the compiler's file/line diagnostic; fix only the syntax issue and rebuild.

**No hints reveal the exact faulty line or correction.** Preserve a log, your diagnosis, your code diff, and retest evidence.

## Build the starter

From the repository root:

```sh
cd lessons/6A/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Expected:** The first build fails until you find the deliberate error. Do not install it before correcting the error.

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
