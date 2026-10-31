# 14B — Trace an existing feature through source code

**Skill:** Resource Literacy · **Estimate:** 45m · **Difficulty:** Medium · **Priority:** Medium · **Prerequisites:** 11A, 10D, 4A

## Competency checkpoint

**Primary:** Resource Literacy · **Supporting:** Algorithmic Thinking. Find and interpret relevant authoritative SDK documentation, then justify what the API can and cannot guarantee. Retain the original assignment's required output, and self-score **both competencies** at 0–3 using the [common rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This check adds no new independent activity.


**Companion reading:** [14B in the resource literacy guide](../../curriculum/resource-literacy/README.md). Trace the event handler through state change to visible result. Use this lesson's local starter; the reading is preparation, not a completed answer.

## Exact local example

- [`starter/`](./starter/) — Independent Emery font-selection watchapp with Up/Down click handlers and APP_LOG diagnostics.

Use the local example as a reference. Make your own decisions and retain the evidence requested by this lesson.

## Your task

Open the Font Browser example. Find where button input is registered or handled, identify the state that changes, and follow the code until the display is updated. Use the README and SDK docs to look up unfamiliar APIs. Write down the file/function names and draw the input -> state change -> display update path.

## Completion evidence

Your notes identify the input handling, changed state, display update, and the relevant source locations and documentation.

## Build the starter

From the repository root:

```sh
cd lessons/14B/starter
pebble build
pebble install --emulator emery
pebble install --emulator gabbro
pebble logs --emulator emery
pebble logs --emulator gabbro
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery and Gabbro** and follow the no-AI coursework rule.

## Dual-platform verification — Time 2 and Round 2

**Same activity, two displays:** [Pebble Time 2 / Emery](../../curriculum/dual-platform/README.md) uses a 200×228 rectangle; Pebble Round 2 / Gabbro uses a 260×260 circle. The existing learning outcome and competency rubric are unchanged. Any code you build should target both `emery` and `gabbro`, and you should check on both emulators for clipped text, invisible controls, and round-edge collisions. For non-coding work, account for both display geometries in your existing explanation/design—**this is not an additional assignment**.

Follow the [two-platform command and testing reference](../../curriculum/dual-platform/README.md). Compare actual results; a manifest listing two platforms is not evidence of successful compilation or physical sensor behavior. Round 2 touch is optional on watchapps; preserve button navigation and graceful touch-disabled behavior.
