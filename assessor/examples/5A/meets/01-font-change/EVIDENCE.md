# Evidence — 5A

## Artifact paths

- lessons/5A/starter/src/c/main.c

## Build and run

From `lessons/5A/starter` I ran `pebble build` (success) and `pebble install --emulator emery`.

## Behavior observed

I changed exactly one visual property: the time TextLayer now uses `FONT_KEY_GOTHIC_24_BOLD` instead of 28 bold. The time still updates each minute on the Emery emulator. There is still only one TextLayer and no date layer.

## Boundary case tested

Normal: read time at arm’s length. Boundary: waited past a minute tick to confirm the font change did not break the tick handler.

## Explain in your own words

I predicted a smaller bold font would improve glance readability on the 200x228 canvas without moving the layer. The visual change is intentional and single-purpose; I did not add alignment or color tweaks in the same commit.

## Source diff

Committed under lessons/5A/starter; `text_layer_set_font` line edited only.
