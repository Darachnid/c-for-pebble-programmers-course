# Time-only watchface — clean starter

Emery-only C watchface with exactly **one TextLayer**. This is the baseline for 7A, 4A, 5A, 3A, 1A, 1B, and 7B.

- Build: `pebble build`
- Run: `pebble install --emulator emery`
- For 1A, change **one** visual property. For 1B, create the date layer yourself; the completed date layer is intentionally absent.
- Check that time updates at the minute boundary. No buttons are required in a watchface.

Upstream reading: [official C watchface tutorial](https://developer.repebble.com/tutorials/watchface-tutorial/part1/). This starter is independently authored for the course.
