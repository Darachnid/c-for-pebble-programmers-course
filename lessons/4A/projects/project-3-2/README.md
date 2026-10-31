# Project 3.2 — Orbiting letter: numeric types, expressions, and integer trigonometry

**Emery-only runnable starter (Pebble SDK 4.33.1, C).** This is a modernized, course-authored equivalent of the activity in Mike Jipping's *Learning C with Pebble*; it is not a byte-for-byte copy of the historic sample.

## API scaffolding: provided, not assessed here

The project uses Pebble SDK facilities you will study in later API labs. **You are not expected to write those facilities from scratch in this C-language lesson.**

- **Already provided:** Timer advances degrees, custom Layer renders the letter; sin_lookup/cos_lookup convert an angle to screen coordinates.
- **Your C-language edit surface:** s_degrees, s_radius, s_speed and the TODO click handlers. Treat trig lookup functions as supplied math tools; focus on casts, modulo, scaling and operators.
- **Observable check:** Demonstrate changed speed/direction/radius and explain bounds on s_degrees (0–359).

For a short call-flow diagram and explanations of the supplied SDK functions, read the [Pebble scaffold guide](../../../../curriculum/c-programming/sdk-scaffolding.md). This is a language exercise first; changing unrelated Window, Layer, timer or subscription code is unnecessary.

## What to do

Alter the angle increment and orbit radius; explain modulo, cast, and arithmetic order. Compare integer lookup coordinates and floating point conceptual alternatives.

The **TODO** comments identify places to work; they are not completed answers. The starter is intended to compile and run before modification. Build and test only for `emery` (Pebble Time 2), which has a 200 × 228 rectangular display.

```sh
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Evidence:** source diff, observed result (emulator or watch), an explanation of the C feature practiced, and tests at one normal and one boundary input. Avoid AI during the exercise.

**Source credit:** exercise concept adapted from *Learning C with Pebble* Chapter 3. This starter C program is newly written for this repository.
