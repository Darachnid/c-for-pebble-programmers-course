# 4A — Annotate the time-only watchface code

**Skill:**  · **Estimate:**  · **Difficulty:**  · **Priority:**  · **Prerequisites:** 

## Exact local example

- [`starter/`](./starter/) — One-text-layer Emery watchface; time only. It intentionally does not include a date.

Use the local example as a reference. Make your own decisions and retain the evidence requested by this lesson.

## Your task

Use your time-only watchface source. In your own notes, annotate the variable declarations, data types, pointers, function calls, arguments, and callback registrations. For each function, state its responsibility. Mark which calls happen directly and which functions Pebble calls as callbacks. Do not use AI to explain or write the annotations.

## Completion evidence

Your notes explain the key declarations and each function's role, and distinguish direct calls from callbacks.

## Build the starter

From the repository root:

```sh
cd lessons/4A/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
