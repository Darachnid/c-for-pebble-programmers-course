# 7C — Integrate font browsing with persistent selection

**Skill:**  · **Estimate:**  · **Difficulty:**  · **Priority:**  · **Prerequisites:** 

## Exact local examples

- [`fonts/`](./fonts/) — Independent Emery font-selection watchapp with Up/Down click handlers and APP_LOG diagnostics.
- [`storage/`](./storage/) — Independent Emery counter showing the Pebble persist_exists/read/write API.

Two independent C projects are present. Implement the storage pattern in the font app yourself; no combined solution is provided.

## Your task

Start with the local clean font-selector project and the local persist-counter reference. Add persistent selection to your own font app, saving its font index and restoring it on startup, with a safe default for missing/out-of-range values. Build and test on Emery; do not simply copy the integrated debugging sample.

## Completion evidence

The combined app builds, font navigation works, the selected font survives a restart, invalid or absent stored values are handled safely, and Git records the work.

## Build the starter

From the repository root:

```sh
cd lessons/7C/fonts
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

Each included subdirectory is a **separate complete C project**. Run its commands from that subdirectory; it is not an already integrated answer.

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
