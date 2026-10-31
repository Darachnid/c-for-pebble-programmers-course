# 6B — Diagnose a font-selection boundary bug

**Skill:** Debugging and Testing · **Estimate:** 45m · **Difficulty:** Medium · **Priority:** Medium · **Prerequisites:** 4E, 6A, 3B

**Companion reading:** [6B in the debugging testing guide](../../curriculum/debugging-testing/README.md). Use reproducible button sequences and index logs; the deliberate bug is not identified here. Complete the assignment using its provided local Emery project.

## Exact local example

- [`starter/`](./starter/) — Compiling interactive font-selection C source with deliberate selection logic defect.

Use the APP_LOG index traces to investigate incorrect Up navigation. Compile success is expected. The README intentionally does not reveal which expression is flawed.

## Your task

Use the provided deliberately flawed lessons/6B/starter project. It compiles but navigation behaves incorrectly. Reproduce four successive Up and Down presses, collect the included APP_LOG index traces with pebble logs --emulator emery, locate the wrong transition, apply a minimal fix and verify both boundaries. Compare with the clean example only after debugging.

## Completion evidence

The bug is reproducible, the cause is explained, and tests show that cycling works correctly at both ends of the list.

## Debugging diagnostics

Build normally, press Up and Down repeatedly, and compare the included old/new index APP_LOG messages with the expected cycling behavior. Compiler output alone will not reveal the flaw.

**No hints reveal the exact faulty line or correction.** Preserve a log, your diagnosis, your code diff, and retest evidence.

## Build the starter

From the repository root:

```sh
cd lessons/6B/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
