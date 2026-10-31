# Evidence — 1A

## Artifact paths

- lessons/1A/clock/src/c/main.c (read only)
- submit/1A/ideas.md (my brainstorm)

## Build and run

From `lessons/1A/clock` I ran `pebble build` and `pebble install --emulator emery` once to see how the time-only example behaves.

## Behavior observed

The clock example uses one TextLayer centered on the 200x228 canvas. I used that as the base for variations rather than the fonts or storage apps.

## Boundary case tested

Normal: skim all three local examples. Boundary: I compared feasibility when an idea needs a second TextLayer versus only changing fonts or persist keys, and dropped one idea that would break the time-only constraint.

## Explain in your own words

**Idea 1:** Add a subtle background stripe behind the time — change `window_set_background_color` and keep one TextLayer; API: `window_set_background_color`.

**Idea 2:** Cycle fonts on button press like the fonts example — reuse `text_layer_set_font` and click handlers; API: `text_layer_set_font`, `window_single_click_subscribe`.

**Idea 3:** Show a daily step goal pulled from persist storage — read/write counters like storage example; API: `persist_read`, `persist_write`.

**Idea 4:** Flash the time briefly on shake — would need accelerometer service; API: `accel_service_subscribe` (higher technical uncertainty).

**Idea 5:** Dim the time after 22:00 for night glanceability — adjust text color in the tick handler; API: `text_layer_set_text_color`.

**Most interesting to investigate first:** Idea 5, because it keeps the single-layer clock but tests UI readability without new windows.

Supporting competency (Resource Literacy): I noted which APIs are documented in the SDK versus which would need me to read accelerometer samples.

## Source diff

No lesson source edits for 1A; evidence lives in submit/1A/.
