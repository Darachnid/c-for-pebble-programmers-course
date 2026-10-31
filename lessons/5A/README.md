# 5A — Find and document a Pebble API function

**Skill:** Resource Literacy · **Estimate:** 20m · **Difficulty:** Low · **Priority:** High · **Prerequisites:** 4A

## Competency checkpoint

**Primary:** Resource Literacy · **Supporting:** C Programming. Find and interpret relevant authoritative SDK documentation, then justify what the API can and cannot guarantee. Retain the original assignment's required output, and self-score **both competencies** at 0–3 using the [common rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This check adds no new independent activity.


**Companion reading:** [5A in the resource literacy guide](../../curriculum/resource-literacy/README.md). Record the API function contract and local usage in your own words. Use this lesson's local starter; the reading is preparation, not a completed answer.

## Exact local example

- [`starter/`](./starter/) — One-text-layer Emery watchface; time only. It intentionally does not include a date.

Use the local example as a reference. Make your own decisions and retain the evidence requested by this lesson.

## Your task

Find the SDK documentation for text_layer_set_font() or another function used by your watchface. Record what it does, its full function signature, the type and purpose of each argument, its return type, and one example of where it is used. Write the explanation in your own words.

## Completion evidence

A concise API note contains purpose, signature, argument meanings, return type, and a usage example.

## Build the starter

From the repository root:

```sh
cd lessons/5A/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

## Source and permissions

The complete required starter C source and build files are in this folder. Official Pebble SDK source copies are included only when their license authorizes redistribution, with the MIT license preserved. Other starter code is independently written for this course. Use **Emery only** and follow the no-AI coursework rule.
