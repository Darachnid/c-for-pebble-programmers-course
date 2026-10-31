# 8I optional debugging challenge — api

**This is a deliberately defective, standalone Emery project.** Only attempt it after finishing [lesson 8I](../README.md). No answer or location of the defect is supplied. Do not use its source as the next checkpoint for the main project.

## Symptom

The backlight checkpoint does not produce a valid SDK build.

## Investigation

Capture the first relevant compiler or linker diagnostic, find its SDK API reference, and correct the smallest error. Preserve the initial result, isolate one hypothesis, make a minimal change and rerun the original failure case plus one regression test.

## Evidence of completion

Keep a build log or reproducer, expected-versus-actual table, suspected failure mechanism, a minimal Git diff, and a post-fix result. Your explanation must distinguish the observed symptom from the root cause.

```sh
cd lessons/8I/debug
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

The original SDK 4.33.1 Emery starter remains in [starter](../starter/). An intentionally broken compiler or integration example is **not** a verified build.
