# 17E — Arrays, Strings, and Bounds

**Skill:** C Programming · **Estimate:** 90m · **Difficulty:** Medium · **Priority:** High · **Prerequisites:** 10D

## Competency checkpoint

**Primary:** C Programming · **Supporting:** Debugging and Testing. Explain which C data/functions produce the behavior, identify ownership or bounds as relevant, and verify a failing/edge case. Demonstrate the stated lesson outcome and explain your supporting skill; self-score **both** at 0–3 with the [common mastery rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This is the assessment lens for the existing lesson, not another exercise.


**Read:** [17E learning module](../../curriculum/c-programming/17E-arrays-strings.md)

**Use exactly:** [starter/](starter/) — an original Pebble SDK C watchapp targeting only Emery (200 × 228).

## Assignment

Expand the list to six messages; write a function returning the index of a requested item; ensure boundaries wrap; use snprintf to construct a safe label. Test the first/last index and an overlong string.

## Evidence-based completion

Use arrays and bounded C strings to represent multiple values without overrunning buffers. Submit: working Emery build, source diff, brief explanation of your solution, normal-case and boundary-case tests, and the required diagrams/notes where assigned.

## Running

```sh
cd lessons/17E/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

Do not rely on AI to write the exercise or provide an answer key. The included C starter intentionally provides the existing SDK scaffolding but not your requested extension.
