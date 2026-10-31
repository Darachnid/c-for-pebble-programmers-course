# Evidence — 2A

## Artifact paths

- lessons/2A/starter/src/c/main.c
- lessons/2A/starter/package.json

## Build and run

From `lessons/2A/starter` I ran `pebble build` (success) and `pebble install --emulator emery`.
I saved key lines in submit/2A/build.log.

## Behavior observed

The Emery emulator shows the current time centered on screen. It updates when the minute rolls over.
I confirmed only one TextLayer is created in main.c for the clock string. There is no date TextLayer.

## Boundary case tested

Normal: launch at :30 and read the time. Boundary: waited past a minute boundary to confirm the display updates without restarting the app.

## Explain in your own words

I followed the SDK 4 watchface tutorial through the time-only checkpoint: one window, one TextLayer, tick handler updating the buffer with `%H:%M`.

## Source diff

Changes are committed under lessons/2A/starter; assessor collects git diff on submit.
