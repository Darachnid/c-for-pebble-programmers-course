# Evidence — 4A

## Artifact paths

- lessons/4A/starter/src/c/main.c

## Build and run

`pebble build` and emulator install on Emery succeeded from the starter directory.

## Behavior observed

The window background defaults to black; I documented `window_set_background_color` instead because I might use it in a later UI lesson.

## Boundary case tested

Boundary: setting a color with alpha — I read whether the emulator matches hardware; I only tested solid GColorBlack/GColorWhite swaps.

## Explain in your own words

**API:** `window_set_background_color`

**Purpose:** Sets the background color of a Window’s root layer so content behind TextLayers shows that color.

**Signature:** `void window_set_background_color(Window *window, GColor background_color);`

**Parameters:** `window` must be the active window; `background_color` is a GColor value (e.g. `GColorBlack`).

**Returns:** void — callers must still invalidate or layer stack updates as usual.

**Example:** After `window_create`, `window_set_background_color(window, GColorBlack);` matches the time-only tutorial checkpoint.

Documentation source: Pebble SDK reference for Window layer styling.

## Source diff

Read-only review of starter; evidence in submit/4A.
