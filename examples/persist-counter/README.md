# Persist counter — clean storage example

Emery-only C watchapp. Up increments a count; Down resets it; its value survives app restarts.

Used in 5C to identify `persist_exists()`, `persist_read_int()`, and `persist_write_int()`. In 7C, transfer this *pattern*, not the complete app, into your font selector. Verify persistence with exit/reopen tests.

Build: `pebble build` • Run: `pebble install --emulator emery` • Logs: `pebble logs --emulator emery`

Upstream reading: [Pebble persistence guide](https://developer.repebble.com/guides/events-and-services/persistent-storage/).
