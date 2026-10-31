# Project 6.1 — Clock decomposition: functions, parameters and return values

**Emery/Gabbro runnable starter (Pebble SDK 4.33.1, C).** This is a modernized, course-authored equivalent of the activity in Mike Jipping's *Learning C with Pebble*; it is not a byte-for-byte copy of the historic sample.

## API scaffolding: provided, not assessed here

The project uses Pebble SDK facilities you will study in later API labs. **You are not expected to write those facilities from scratch in this C-language lesson.**

- **Already provided:** The TickTimerService supplies seconds; the drawing callback produces the clock hand and outline.
- **Your C-language edit surface:** is_five_second_mark() and the call site; identify clear function parameters, return values and contracts. Compare against existing logic rather than rebuilding the event loop.
- **Observable check:** Demonstrate the same behavior before/after the refactor at 0, 5, 6 and 59 seconds.

For a short call-flow diagram and explanations of the supplied SDK functions, read the [Pebble scaffold guide](../../../../curriculum/c-programming/sdk-scaffolding.md). This is a language exercise first; changing unrelated Window, Layer, timer or subscription code is unnecessary.

## What to do

Extract repeated conditional clock logic into a helper that accepts a second count and returns whether a five-second mark should be drawn. Preserve the original behavior.

The **TODO** comments identify places to work; they are not completed answers. The starter is intended to compile and run before modification. Build and test only for `emery` (Pebble Time 2), which has a 200 × 228 rectangular display.

```sh
pebble build
pebble install --emulator emery
pebble install --emulator gabbro
pebble logs --emulator emery
```

**Evidence:** source diff, observed result (emulator or watch), an explanation of the C feature practiced, and tests at one normal and one boundary input. Avoid AI during the exercise.

**Source credit:** exercise concept adapted from *Learning C with Pebble* Chapter 6. This starter C program is newly written for this repository.

## Platform evidence (within this exercise)

This exact project builds for Pebble Time 2 (`emery`, 200×228 rectangular) **and** Pebble Round 2 (`gabbro`, 260×260 circular). When working on the already assigned C behavior, check on both emulators; Round 2 can clip graphics or text near its corners. Reuse the existing lesson deliverable and explain any shape-specific adjustments in your normal code/test evidence. The SDK-scaffolding portions remain provided and are **not a separate task**. See [the dual-platform reference](../../../../curriculum/dual-platform/README.md).
