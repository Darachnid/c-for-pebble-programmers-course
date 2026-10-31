# Evidence — 5A

## Artifact paths

- lessons/5A/starter/src/c/main.c

## Build and run

I ran pebble build and pebble install --emulator emery successfully.

## Behavior observed

The time updates each minute. I also added a date TextLayer for the date because it looked empty. The visual change includes a second line for the date.

## Boundary case tested

Boundary: midnight rollover — I checked both layers.

## Explain in your own words

I changed font and added a date layer for better UI.

## Source diff

Added second text_layer_create for the date.
