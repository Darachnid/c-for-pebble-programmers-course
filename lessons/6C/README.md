# 6C — Diagnose a persistent-state integration bug

**Skill:** Debugging and Testing · **Estimate:** 90m · **Difficulty:** High · **Priority:** Low · **Prerequisites:** 4H, 6B, 7C

## Exact local example

- [`starter/`](./starter/) — Compiling font selection/persistence C source with deliberate restart-state defect.

Test a non-default font across restart; compare selection versus startup logs. Diagnose stored and restored state. No solution provided.

## Your task

Use the deliberately flawed lessons/6C/starter project. Select a nondefault font, exit, reopen; document the discrepancy. Inspect the provided startup and selection logs; trace storage write/read behavior; fix the single persistence defect and test fresh install plus repeated restarts. Do not consult a clean integrated implementation before diagnosing.

## Completion evidence

A reproducible bug report records expected and actual behavior, the cause is explained, and the fix passes fresh-start, selection, and restart tests.

## Debugging diagnostics

Build normally, select a nondefault font, close the app and reopen. Compare APP_LOG startup and navigation traces, and test the storage lifecycle. Investigate the single persistence defect.

**No hints reveal the exact faulty line or correction.** Preserve a log, your diagnosis, your code diff, and retest evidence.

## Build the starter

From the repository root:

```sh
cd lessons/6C/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
