# 5C — Research an unfamiliar Pebble capability

**Skill:**  · **Estimate:**  · **Difficulty:**  · **Priority:**  · **Prerequisites:** 

## Exact local example

- [`starter/`](./starter/) — Independent Emery counter showing the Pebble persist_exists/read/write API.

A second SDK source snapshot (App Glance) demonstrates persisted launch counts; the executable starter is the smaller counter.

## Your task

Study the local Emery persist-counter app. Identify how it checks for saved data, reads it at startup, and writes changes. Research the SDK's persistence functions using official documentation, and write an implementation plan to reuse the pattern in another app; no copy-and-paste integration yet.

## Completion evidence

A technical note names the capability, links the documentation and example, lists relevant APIs and constraints, and proposes implementation steps.

## Build the starter

From the repository root:

```sh
cd lessons/5C/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
