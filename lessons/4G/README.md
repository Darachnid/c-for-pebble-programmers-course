# 4G — Structures, Enums, and Program State

**Skill:** C Programming · **Estimate:** 105m · **Difficulty:** High · **Priority:** Medium · **Prerequisites:** 4F

## Competency checkpoint

**Primary:** C Programming · **Supporting:** Algorithmic Thinking. Explain the C state or pointer/callback lifetime and test normal, boundary, and cleanup behavior. Retain the original assignment's required output, and self-score **both competencies** at 0–3 using the [common rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This check adds no new independent activity.


**Read:** [4G learning module](../../curriculum/c-programming/4G-structs-enums-state.md)

**Use exactly:** [starter/](starter/) — an original Pebble SDK C watchapp targeting only Emery (200 × 228).

## Assignment

Add a PAUSED enum value and a timer count field to AppState; modify button handling so it changes score only in EDIT mode. Draw a transition table and test each mode (including the default/fallback case).

## Evidence-based completion

Represent related variables with a struct and named program modes with an enum. Submit: working Emery build, source diff, brief explanation of your solution, normal-case and boundary-case tests, and the required diagrams/notes where assigned.

## Running

```sh
cd lessons/4G/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

Do not rely on AI to write the exercise or provide an answer key. The included C starter intentionally provides the existing SDK scaffolding but not your requested extension.
