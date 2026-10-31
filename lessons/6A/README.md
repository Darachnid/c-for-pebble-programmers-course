# 6A — Diagnose a simple compiler error

**Skill:** Debugging and Testing · **Estimate:** 20m · **Difficulty:** Low · **Priority:** High · **Prerequisites:** 3A, 2A

## Competency checkpoint

**Primary:** Debugging and Testing · **Supporting:** Development Tools and Workflow. Separate symptom from cause, record a reproducible hypothesis and a minimal correction, and run a regression test. Retain the original assignment's required output, and self-score **both competencies** at 0–3 using the [common rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This check adds no new independent activity.


**Companion reading:** [6A in the debugging testing guide](../../curriculum/debugging-testing/README.md). Capture the first compiler diagnostic before touching source; no error solution is given here. Complete the assignment using its provided local Emery project.

## Exact local example

- [`starter/`](./starter/) — Deliberately malformed time-only C source. Initial compilation is supposed to fail.

Compile, capture the first compiler diagnostic, identify a syntax error, make the smallest correction and rebuild. No answer key.

## Your task

Start from the deliberately flawed lessons/6A/starter project. Run pebble build; capture the first compiler diagnostic; identify and correct the single syntax fault; rebuild and run on Emery and Gabbro. The original clean time-only example is for comparison AFTER the diagnosis.

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
pebble install --emulator gabbro
pebble logs --emulator emery
pebble logs --emulator gabbro
```

**Expected:** The first build fails until you find the deliberate error. Do not install it before correcting the error.

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery and Gabbro** and follow the no-AI coursework rule.

## Dual-platform verification — Time 2 and Round 2

**Same activity, two displays:** [Pebble Time 2 / Emery](../../curriculum/dual-platform/README.md) uses a 200×228 rectangle; Pebble Round 2 / Gabbro uses a 260×260 circle. The existing learning outcome and competency rubric are unchanged. Any code you build should target both `emery` and `gabbro`, and you should check on both emulators for clipped text, invisible controls, and round-edge collisions. For non-coding work, account for both display geometries in your existing explanation/design—**this is not an additional assignment**.

Follow the [two-platform command and testing reference](../../curriculum/dual-platform/README.md). Compare actual results; a manifest listing two platforms is not evidence of successful compilation or physical sensor behavior. Round 2 touch is optional on watchapps; preserve button navigation and graceful touch-disabled behavior.
