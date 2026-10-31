# 2A — Explore Pebble examples

**Skill:**  · **Estimate:**  · **Difficulty:**  · **Priority:**  · **Prerequisites:** 

## Exact local examples

- [`clock/`](./clock/) — One-text-layer Emery watchface; time only. It intentionally does not include a date.
- [`fonts/`](./fonts/) — Independent Emery font-selection watchapp with Up/Down click handlers and APP_LOG diagnostics.
- [`storage/`](./storage/) — Independent Emery counter showing the Pebble persist_exists/read/write API.

Three locally stored, self-contained projects to inspect; no external examples are needed.

## Your task

Browse only the included Emery-targeted projects under examples/, initially time-only, font-selector, and persist-counter. Choose one and brainstorm five creative variations; describe what changes and what new API each might require. Do not browse or solve the debugging challenges yet.

## Completion evidence

Five distinct ideas are recorded, each describes a possible change, and one idea is marked as the most interesting to investigate.

## Build the starter

From the repository root:

```sh
cd lessons/2A/clock
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

Each included subdirectory is a **separate complete C project**. Run its commands from that subdirectory; it is not an already integrated answer.

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
