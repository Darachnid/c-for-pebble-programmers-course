# 8L optional debugging challenge — resource

**This is a deliberately defective, standalone Emery project.** Only attempt it after finishing [lesson 8L](../README.md). No answer or location of the defect is supplied. Do not use its source as the next checkpoint for the main project.

## Symptom

The app appears to run but the bundled field note does not match the source text.

## Investigation

Use a byte-by-byte comparison, the resource-size API, and a trace showing expected versus observed content. Preserve the initial result, isolate one hypothesis, make a minimal change and rerun the original failure case plus one regression test.

## Evidence of completion

Keep a build log or reproducer, expected-versus-actual table, suspected failure mechanism, a minimal Git diff, and a post-fix result. Your explanation must distinguish the observed symptom from the root cause.

```sh
cd lessons/8L/debug
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

The original SDK 4.33.1 Emery starter remains in [starter](../starter/). An intentionally broken compiler or integration example is **not** a verified build.
