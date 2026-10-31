# 22C — Develop an original Pebble app concept

**Skill:** Idea Generation · **Estimate:** 60m · **Difficulty:** High · **Priority:** Medium · **Prerequisites:** 16B, 20C

## Competency checkpoint

**Primary:** Idea Generation · **Supporting:** Resource Literacy. Before choosing an idea, explicitly compare alternatives against feasibility, user benefit and technical uncertainty. After the activity, provide evidence for the stated completion criterion, explain the supporting competency in your own words, and self-score **both** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This checkpoint clarifies how the existing assignment is assessed; it does not add a new exercise.


**Companion reading:** [22C in the idea generation guide](../../curriculum/idea-generation/README.md). Compare feasibility and uncertainty before choosing the smallest app. Use the local starter below; the reading is preparation, not a replacement project.

## Exact local examples

- [`layout/`](./layout/) — Exact C source from official MIT-licensed Pebble Simplicity example, adapted Emery-only manifest.
- [`fonts/`](./fonts/) — Independent Emery font-selection watchapp with Up/Down click handlers and APP_LOG diagnostics.
- [`storage/`](./storage/) — Independent Emery counter showing the Pebble persist_exists/read/write API.

Three locally stored, self-contained projects to compare. Choose a concept before implementing.

## Your task

Use the included examples/ collection as inspiration. Propose three original Pebble Time 2 applications based on your interests. Compare feasibility and learning value; write a minimal specification for one without committing to build it.

## Completion evidence

Three ideas are compared and one has a concise specification for purpose, interaction, minimum version, and technical uncertainty.

## Build the starter

From the repository root:

```sh
cd lessons/22C/layout
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

Each included subdirectory is a **separate complete C project**. Run its commands from that subdirectory; it is not an already integrated answer.

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
