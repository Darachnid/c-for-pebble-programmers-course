# Project 5.1 — Decimal-to-binary converter: counted loops

**Emery-only runnable starter (Pebble SDK 4.33.1, C).** This is a modernized, course-authored equivalent of the activity in Mike Jipping's *Learning C with Pebble*; it is not a byte-for-byte copy of the historic sample.

## API scaffolding: provided, not assessed here

The project uses Pebble SDK facilities you will study in later API labs. **You are not expected to write those facilities from scratch in this C-language lesson.**

- **Already provided:** Up/Down click handlers change a decimal number; graphics_draw_text shows two strings.
- **Your C-language edit surface:** Convert s_number to s_binary using a bounded loop; create/identify a shared conversion helper instead of altering Window or click registration.
- **Observable check:** Prove all eight bits at 0, 1, 127, 128 and 255 and preserve the terminator.

For a short call-flow diagram and explanations of the supplied SDK functions, read the [Pebble scaffold guide](../../../../curriculum/c-programming/sdk-scaffolding.md). This is a language exercise first; changing unrelated Window, Layer, timer or subscription code is unnecessary.

## What to do

Replace the zero-filled binary text with a for-loop that converts an integer 0-255 to eight binary digits; test 0, 1, 127, 128, and 255.

The **TODO** comments identify places to work; they are not completed answers. The starter is intended to compile and run before modification. Build and test only for `emery` (Pebble Time 2), which has a 200 × 228 rectangular display.

```sh
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Evidence:** source diff, observed result (emulator or watch), an explanation of the C feature practiced, and tests at one normal and one boundary input. Avoid AI during the exercise.

**Source credit:** exercise concept adapted from *Learning C with Pebble* Chapter 5. This starter C program is newly written for this repository.
