# Project 6.2 — Bit-pattern digit: function decomposition

**Emery/Gabbro runnable starter (Pebble SDK 4.33.1, C).** This is a modernized, course-authored equivalent of the activity in Mike Jipping's *Learning C with Pebble*; it is not a byte-for-byte copy of the historic sample.

## API scaffolding: provided, not assessed here

The project uses Pebble SDK facilities you will study in later API labs. **You are not expected to write those facilities from scratch in this C-language lesson.**

- **Already provided:** A Layer draws a 3×5 digit pattern using small filled rectangles; Window and update callback are supplied.
- **Your C-language edit surface:** Extract the repeated/dense drawing logic into functions accepting the pattern, position and dimensions. No need to redesign the SDK drawing API.
- **Observable check:** The digit remains legible after refactor; varied dimensions still produce correct cells.

For a short call-flow diagram and explanations of the supplied SDK functions, read the [Pebble scaffold guide](../../../../curriculum/c-programming/sdk-scaffolding.md). This is a language exercise first; changing unrelated Window, Layer, timer or subscription code is unnecessary.

## What to do

Refactor the provided drawing logic into reusable functions accepting the pattern, row, column, and size. Do not merely duplicate draw calls.

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
