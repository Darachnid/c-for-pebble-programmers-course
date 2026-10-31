# Evidence — 4A

## Artifact paths

- lessons/4A/starter/src/c/main.c
- submit/4A/api-note.md

## Build and run

From `lessons/4A/starter` I ran `pebble build` and `pebble install --emulator emery` to confirm the starter still runs before documenting the font API.

## Behavior observed

The starter watchface calls `text_layer_set_font` with `fonts_get_system_font(FONT_KEY_GOTHIC_28_BOLD)` when creating the time layer.

## Boundary case tested

Boundary: I checked what happens if `NULL` is passed as the font — SDK docs say behavior is undefined; I did not rely on that in production code.

## Explain in your own words

**Function:** `text_layer_set_font`

**Purpose:** Assigns the `GFont` used to render a TextLayer’s string on screen.

**Signature:** `void text_layer_set_font(TextLayer *text_layer, GFont font);`

**Arguments:** `text_layer` is the layer to modify; `font` is a handle from `fonts_get_system_font` or a custom font resource.

**Return type:** `void` — no status code; invalid layer pointers are not safe to pass.

**Usage example:** In `main.c` after `text_layer_create`, the starter calls `text_layer_set_font(s_time_layer, fonts_get_system_font(FONT_KEY_GOTHIC_28_BOLD));` so the clock uses bold Gothic 28.

I paraphrased the Pebble SDK documentation; I did not paste the whole reference page.

## Source diff

No code change required for 4A; commits may only touch submit/4A notes.
