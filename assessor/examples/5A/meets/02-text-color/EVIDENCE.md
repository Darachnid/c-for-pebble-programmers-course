# Evidence — 5A

## Artifact paths

- lessons/5A/starter/src/c/main.c
- submit/5A/build.log

## Build and run

`pebble build` and `pebble install --emulator emery` from the starter folder; build.log saved under submit/5A/.

## Behavior observed

Single visual change: I set the time text color to GColorMelon with `text_layer_set_text_color`. Clock digits still update when the minute rolls over. One TextLayer only; no date TextLayer was added.

## Boundary case tested

Boundary: checked contrast on the default black window background for glanceability in bright light.

## Explain in your own words

UI design supporting competency: color was the one property I changed; position and font stayed as the tutorial checkpoint. Resource literacy: I confirmed the API in SDK docs before editing.

## Source diff

Git diff shows one new line calling `text_layer_set_text_color` after layer creation.
