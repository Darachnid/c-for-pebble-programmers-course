# 27C optional debugging challenge — button

**This is a deliberately defective, standalone Emery project.** Only attempt it after finishing [lesson 27C](../README.md). No answer or location of the defect is supplied. Do not use its source as the next checkpoint for the main project.

## Symptom

The app builds, but the expected details navigation input does not behave correctly.

## Investigation

Compare button callbacks, app state, and the on-watch response. Include a button-event trace. Preserve the initial result, isolate one hypothesis, make a minimal change and rerun the original failure case plus one regression test.

## Evidence of completion

Keep a build log or reproducer, expected-versus-actual table, suspected failure mechanism, a minimal Git diff, and a post-fix result. Your explanation must distinguish the observed symptom from the root cause.

```sh
cd lessons/27C/debug
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

The original SDK 4.33.1 Emery starter remains in [starter](../starter/). An intentionally broken compiler or integration example is **not** a verified build.
