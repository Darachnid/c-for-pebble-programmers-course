# 32C — Diagnose a persistent-state integration bug

**Skill:** Debugging and Testing · **Estimate:** 90m · **Difficulty:** High · **Priority:** Low · **Prerequisites:** 24H, 21B, 31C

## Competency checkpoint

**Primary:** Debugging and Testing · **Supporting:** Development Tools and Workflow. Reproduce the symptom, form a root-cause hypothesis, make a minimal change and run a new regression case. Independently explain both competencies and self-score them at 0–3 using the [common rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). The original exercise and its completion evidence remain unchanged.


**Companion reading:** [32C in the debugging testing guide](../../curriculum/debugging-testing/README.md). Test fresh start, save and restart separately; no spoiler is provided here. Complete the assignment using its provided local Emery project.

## Exact local example

- [`starter/`](./starter/) — Compiling font selection/persistence C source with deliberate restart-state defect.

Test a non-default font across restart; compare selection versus startup logs. Diagnose stored and restored state. No solution provided.

## Your task

Use the deliberately flawed lessons/32C/starter project. Select a nondefault font, exit, reopen; document the discrepancy. Inspect the provided startup and selection logs; trace storage write/read behavior; fix the single persistence defect and test fresh install plus repeated restarts. Do not consult a clean integrated implementation before diagnosing.

## Completion evidence

A reproducible bug report records expected and actual behavior, the cause is explained, and the fix passes fresh-start, selection, and restart tests.

## Debugging diagnostics

Build normally, select a nondefault font, close the app and reopen. Compare APP_LOG startup and navigation traces, and test the storage lifecycle. Investigate the single persistence defect.

**No hints reveal the exact faulty line or correction.** Preserve a log, your diagnosis, your code diff, and retest evidence.

## Build the starter

From the repository root:

```sh
cd lessons/32C/starter
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
