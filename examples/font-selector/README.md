# Font selector — clean interactive watchapp

Emery-only C **watchapp** (not a watchface), with four Pebble system fonts, Up/Down navigation, and index diagnostics. Used for 14B, 15B, 8B, 9C, and concept exercises.

Run `pebble build && pebble install --emulator emery`; inspect `pebble logs --emulator emery` while pressing buttons.

- 14B: trace the click handler to `s_index` to `apply_font()`.
- 15B: write your own selection pseudocode before implementing a change.
- 8B: extend behavior (for example, displaying the index or adding a preview line).
- 9C: refactor part of the font selection into a reusable function; do not just paste code from another app.
- 31C: **copy only the storage pattern** from [persist-counter](../persist-counter/README.md) into your own font app.

Upstream inspiration: [Pebble Font Browser](https://github.com/pebble-examples/app-font-browser). The course starter is original and targets Emery directly.
