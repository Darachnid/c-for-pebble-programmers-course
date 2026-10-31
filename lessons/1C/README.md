# 1C — Design a multi-mode Pebble interface

**Skill:** UI Design · **Estimate:** 90m · **Difficulty:** High · **Priority:** Medium · **Prerequisites:** 1B, 2C, 3C, 4H

## Exact local example

- [`starter/`](./starter/) — Exact C source from official MIT-licensed Pebble Simplicity example, adapted Emery-only manifest.

Pebble Simplicity C code is copied unchanged from the MIT-licensed upstream; the package.json is adapted for Emery.

## Your task

Using your concept from 2C and the state diagram from 3C, draw each interface mode for the Emery 200x228 rectangular screen. Use layouts from the included simple examples as starting references, but develop your own visual hierarchy and navigation.

## Completion evidence

A set of labeled sketches covers every main state, navigation between states, button outcomes, and screen-size considerations.

## Build the starter

From the repository root:

```sh
cd lessons/1C/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
