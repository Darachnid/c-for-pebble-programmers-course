# 21B — Diagnose a font-selection boundary bug

**Skill:** Debugging and Testing · **Estimate:** 45m · **Difficulty:** Medium · **Priority:** Medium · **Prerequisites:** 17E, 6A, 15B

## Competency checkpoint

**Primary:** Debugging and Testing · **Supporting:** C Programming. Reproduce the symptom, form a root-cause hypothesis, make a minimal change and run a new regression case. Independently explain both competencies and self-score them at 0–3 using the [common rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). The original exercise and its completion evidence remain unchanged.


**Companion reading:** [21B in the debugging testing guide](../../curriculum/debugging-testing/README.md). Use reproducible button sequences and index logs; the deliberate bug is not identified here. Complete the assignment using its provided local Emery project.

## Exact local example

- [`starter/`](./starter/) — Compiling interactive font-selection C source with deliberate selection logic defect.

Use the APP_LOG index traces to investigate incorrect Up navigation. Compile success is expected. The README intentionally does not reveal which expression is flawed.

## Your task

Use the provided deliberately flawed lessons/21B/starter project. It compiles but navigation behaves incorrectly. Reproduce four successive Up and Down presses, collect the included APP_LOG index traces with pebble logs --emulator emery, locate the wrong transition, apply a minimal fix and verify both boundaries. Compare with the clean example only after debugging.

## Completion evidence

The bug is reproducible, the cause is explained, and tests show that cycling works correctly at both ends of the list.

## Debugging diagnostics

Build normally, press Up and Down repeatedly, and compare the included old/new index APP_LOG messages with the expected cycling behavior. Compiler output alone will not reveal the flaw.

**No hints reveal the exact faulty line or correction.** Preserve a log, your diagnosis, your code diff, and retest evidence.

## Build the starter

From the repository root:

```sh
cd lessons/21B/starter
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
