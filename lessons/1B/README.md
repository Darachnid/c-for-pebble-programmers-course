# 1B — Add and style a date TextLayer

**Skill:**  · **Estimate:**  · **Difficulty:**  · **Priority:**  · **Prerequisites:** 

## Exact local example

- [`starter/`](./starter/) — One-text-layer Emery watchface; time only. It intentionally does not include a date.

Add the date TextLayer yourself; the date is deliberately omitted from the starting source.

## Your task

From YOUR time-only emery code, follow the Adding the Date section of the current C tutorial to create, style, position, update, and unload a second TextLayer. Arrange time and date for the Emery 200x228 screen. Build and install on emery. Do not switch to a completed repository.

## Completion evidence

The watchface displays both time and date, both update correctly, and you can explain how the date layer is created, styled, attached, updated, and destroyed.

## Build the starter

From the repository root:

```sh
cd lessons/1B/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
