# 31C — Integrate font browsing with persistent selection

**Skill:** Development Tools and Workflow · **Estimate:** 150m · **Difficulty:** High · **Priority:** Medium · **Prerequisites:** 25C, 24H, 14B, 7B

## Competency checkpoint

**Primary:** Development Tools and Workflow · **Supporting:** Debugging and Testing. Preserve a known-good baseline, make verifiable commits, and explain how logs/Git make the change reproducible. Independently explain both competencies and self-score them at 0–3 using the [common rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). The original exercise and its completion evidence remain unchanged.


**Companion reading:** [31C in the tools workflow guide](../../curriculum/tools-workflow/README.md). Integrate checkpoints incrementally and test persistence after reopening. Complete the assignment using its provided local Emery project.

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
cd lessons/31C/fonts
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
