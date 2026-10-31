# Evidence — 1A

## Artifact paths

- lessons/1A/storage/
- submit/1A/EVIDENCE.md

## Build and run

Built the persist-counter example under `lessons/1A/storage` with `pebble build` and ran it on the Emery emulator.

## Behavior observed

The storage example increments a counter with Up/Down and survives reload via persist APIs. I brainstormed variations anchored on that behavior.

## Boundary case tested

Boundary: what happens if persist key space collides with another app — I would need to pick a unique key; feasibility is high because the starter already demonstrates the API.

## Explain in your own words

After browsing the fonts and clock projects, I focused on storage for these five ideas:

1. **Idea:** Track water intake with persist — **change:** replace counter label — **API:** `persist_exists`, `persist_read`.
2. **Idea:** Reset counter on long-press — **change:** new button handler — **API:** `window_long_click_subscribe`.
3. **Idea:** Mirror count on the time-only clock face — **change:** second screen — **API:** `text_layer_set_text` (would merge lessons later).
4. **Idea:** Log max value seen today — **change:** compare on each tick — **API:** `time_local`, `persist_write`.
5. **Idea:** Export count via AppMessage to phone — **change:** companion channel — **API:** `app_message_outbox_send` (uncertain, defer).

**Top pick to investigate:** Idea 1 because it reuses the starter with minimal new API surface.

## Source diff

None under lessons/1A for this activity.
