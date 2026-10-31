# Font selector — clean interactive watchapp

Emery-only C **watchapp** (not a watchface), with four Pebble system fonts, Up/Down navigation, and index diagnostics. Used for 5B, 3B, 4B, 4C, and concept exercises.

Run `pebble build && pebble install --emulator emery`; inspect `pebble logs --emulator emery` while pressing buttons.

- 5B: trace the click handler to `s_index` to `apply_font()`.
- 3B: write your own selection pseudocode before implementing a change.
- 4B: extend behavior (for example, displaying the index or adding a preview line).
- 4C: refactor part of the font selection into a reusable function; do not just paste code from another app.
- 7C: **copy only the storage pattern** from [persist-counter](../persist-counter/README.md) into your own font app.

Upstream inspiration: [Pebble Font Browser](https://github.com/pebble-examples/app-font-browser). The course starter is original and targets Emery directly.
