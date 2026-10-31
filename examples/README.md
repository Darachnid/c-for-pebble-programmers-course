# Local Emery-only C examples

These **original course-owned** starter projects target **only** `emery` (Pebble Time 2, 200 × 228 pixels). They are intentionally small and have no third-party source-code dependencies.

| Folder | Working? | Use |
|---|---|---|
| [time-only](time-only/) | Yes | 2A, 3A, 4A, 11A, 5A, 13B, 7B — *one TextLayer, no date* |
| [font-selector](font-selector/) | Yes | 14B, 15B, 8B, 9C and 31C — Up/Down font selection |
| [persist-counter](persist-counter/) | Yes | 20C and 31C — persistent integer state |
| [debug-6a](debug-6a/) | **No, deliberate compiler error** | Low — use compiler diagnostics |
| [debug-21b](debug-21b/) | Builds, misbehaves | Medium — use runtime APP_LOG index traces |
| [debug-32c](debug-32c/) | Builds, fails after restart | High — trace saved versus restored state |

## Use

From the directory of an individual example:

```sh
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

For debugging 6A, the first build should **fail**. This is expected. Do not use a debugger or AI to get a solution; read the compiler error.

**Watchapp versus watchface:** The time-only example is a watchface; the font selector and counter are watchapps because they use Up/Down button input.

## Pedagogical rule

Study an example, then work on your **own copy**. During debugging exercises, don't compare against the clean starter until you've documented your hypothesis and attempted a fix. No solutions are included.

## Upstream reading (not required source code)

The minimal projects here are **not** copies of third-party code. For optional, independent reading, see the [Pebble C watchface tutorial](https://developer.repebble.com/tutorials/watchface-tutorial/part1/), [Pebble Font Browser](https://github.com/pebble-examples/app-font-browser), and [Pebble storage guide](https://developer.repebble.com/guides/events-and-services/persistent-storage/).

