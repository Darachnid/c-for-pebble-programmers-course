# Project 3.1 — Bouncing ball: variables and expressions

**Emery-only runnable starter (Pebble SDK 4.33.1, C).** This is a modernized, course-authored equivalent of the activity in Mike Jipping's *Learning C with Pebble*; it is not a byte-for-byte copy of the historic sample.

## API scaffolding: provided, not assessed here

The project uses Pebble SDK facilities you will study in later API labs. **You are not expected to write those facilities from scratch in this C-language lesson.**

- **Already provided:** AppTimer drives motion; Window and Layer lifecycle call a graphics drawing callback and queue redraws.
- **Your C-language edit surface:** s_x, s_y, x_velocity, y_velocity, ball_radius, advance(), and the TODO button handlers. Change variables/expressions; do not rewrite window or timer setup.
- **Observable check:** Show two distinct trajectories and a boundary bounce; explain which C value/expression changed.

For a short call-flow diagram and explanations of the supplied SDK functions, read the [Pebble scaffold guide](../../../../curriculum/c-programming/sdk-scaffolding.md). This is a language exercise first; changing unrelated Window, Layer, timer or subscription code is unnecessary.

## What to do

Change ball radius, initial position, velocity and direction by editing variable declarations and expressions. Observe visible motion and boundary behavior.

The **TODO** comments identify places to work; they are not completed answers. The starter is intended to compile and run before modification. Build and test only for `emery` (Pebble Time 2), which has a 200 × 228 rectangular display.

```sh
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

**Evidence:** source diff, observed result (emulator or watch), an explanation of the C feature practiced, and tests at one normal and one boundary input. Avoid AI during the exercise.

**Source credit:** exercise concept adapted from *Learning C with Pebble* Chapter 3. This starter C program is newly written for this repository.
