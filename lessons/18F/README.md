# 18F — Pointers, Indirection, and Memory Lifetime

**Skill:** C Programming · **Estimate:** 105m · **Difficulty:** High · **Priority:** High · **Prerequisites:** 17E

## Competency checkpoint

**Primary:** C Programming · **Supporting:** Debugging and Testing. Explain the C state or pointer/callback lifetime and test normal, boundary, and cleanup behavior. Retain the original assignment's required output, and self-score **both competencies** at 0–3 using the [common rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This check adds no new independent activity.


**Read:** [18F learning module](../../curriculum/c-programming/18F-pointers-memory.md)

**Use exactly:** [starter/](starter/) — an original Pebble SDK C watchapp targeting only Emery (200 × 228).

## Assignment

Rewrite the coordinate update using an output pointer, add a second pointer-based helper, and document what memory each pointer points to and who owns the TextLayer. Deliberately test NULL using a helper, then restore safe code.

## Evidence-based completion

Use addresses and pointer parameters safely and understand ownership of Pebble UI resources. Submit: working Emery build, source diff, brief explanation of your solution, normal-case and boundary-case tests, and the required diagrams/notes where assigned.

## Running

```sh
cd lessons/18F/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

Do not rely on AI to write the exercise or provide an answer key. The included C starter intentionally provides the existing SDK scaffolding but not your requested extension.
