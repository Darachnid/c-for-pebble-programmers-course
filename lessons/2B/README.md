# 2B — Write a two-example remix brief

**Skill:**  · **Estimate:**  · **Difficulty:**  · **Priority:**  · **Prerequisites:** 

## Exact local examples

- [`clock/`](./clock/) — One-text-layer Emery watchface; time only. It intentionally does not include a date.
- [`storage/`](./storage/) — Independent Emery counter showing the Pebble persist_exists/read/write API.

Two locally stored, self-contained projects to compare; they are not pre-integrated.

## Your task

Select two examples from the included examples/ folder (such as time-only and persist-counter). Describe a possible new application using an element from each. State its purpose, the elements to borrow, the smallest working version and a technical uncertainty. Do not implement yet.

## Completion evidence

A one-page brief explains the purpose, source features, minimal version, and one or more technical questions to investigate.

## Build the starter

From the repository root:

```sh
cd lessons/2B/clock
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

Each included subdirectory is a **separate complete C project**. Run its commands from that subdirectory; it is not an already integrated answer.

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
