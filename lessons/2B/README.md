# 2B — Write a two-example remix brief

**Skill:** Idea Generation · **Estimate:** 30m · **Difficulty:** Medium · **Priority:** Medium · **Prerequisites:** 2A, 5B

## Competency checkpoint

**Primary:** Idea Generation · **Supporting:** UI Design. Before choosing an idea, explicitly compare alternatives against feasibility, user benefit and technical uncertainty. After the activity, provide evidence for the stated completion criterion, explain the supporting competency in your own words, and self-score **both** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This checkpoint clarifies how the existing assignment is assessed; it does not add a new exercise.


**Companion reading:** [2B in the idea generation guide](../../curriculum/idea-generation/README.md). Identify the interface between clock updates and persisted data. Use the local starter below; the reading is preparation, not a replacement project.

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
