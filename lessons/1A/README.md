# 1A — Explore Pebble examples

**Skill:** Idea Generation · **Estimate:** 20m · **Difficulty:** Low · **Priority:** High · **Prerequisites:** None

## Competency checkpoint

**Primary:** Idea Generation · **Supporting:** Resource Literacy. Before choosing an idea, explicitly compare alternatives against feasibility, user benefit and technical uncertainty. After the activity, provide evidence for the stated completion criterion, explain the supporting competency in your own words, and self-score **both** using the [four-level rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This checkpoint clarifies how the existing assignment is assessed; it does not add a new exercise.


**Companion reading:** [1A in the idea generation guide](../../curriculum/idea-generation/README.md). Observe input, state and output before proposing new features. Use the local starter below; the reading is preparation, not a replacement project.

## Exact local examples

- [`clock/`](./clock/) — One-text-layer Emery watchface; time only. It intentionally does not include a date.
- [`fonts/`](./fonts/) — Independent Emery font-selection watchapp with Up/Down click handlers and APP_LOG diagnostics.
- [`storage/`](./storage/) — Independent Emery counter showing the Pebble persist_exists/read/write API.

Three locally stored, self-contained projects to inspect; no external examples are needed.

## Your task

Browse only the included Emery/Gabbro-targeted projects under examples/, initially time-only, font-selector, and persist-counter. Choose one and brainstorm five creative variations; describe what changes and what new API each might require. Do not browse or solve the debugging challenges yet.

## Completion evidence

Five distinct ideas are recorded, each describes a possible change, and one idea is marked as the most interesting to investigate.

## Build the starter

From the repository root:

```sh
cd lessons/1A/clock
pebble build
pebble install --emulator emery
pebble install --emulator gabbro
pebble logs --emulator emery
pebble logs --emulator gabbro
```

Each included subdirectory is a **separate complete C project**. Run its commands from that subdirectory; it is not an already integrated answer.

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery and Gabbro** and follow the no-AI coursework rule.

## Dual-platform verification — Time 2 and Round 2

**Same activity, two displays:** [Pebble Time 2 / Emery](../../curriculum/dual-platform/README.md) uses a 200×228 rectangle; Pebble Round 2 / Gabbro uses a 260×260 circle. The existing learning outcome and competency rubric are unchanged. Any code you build should target both `emery` and `gabbro`, and you should check on both emulators for clipped text, invisible controls, and round-edge collisions. For non-coding work, account for both display geometries in your existing explanation/design—**this is not an additional assignment**.

Follow the [two-platform command and testing reference](../../curriculum/dual-platform/README.md). Compare actual results; a manifest listing two platforms is not evidence of successful compilation or physical sensor behavior. Round 2 touch is optional on watchapps; preserve button navigation and graceful touch-disabled behavior.
