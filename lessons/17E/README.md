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
pebble install --emulator gabbro
pebble logs --emulator emery
pebble logs --emulator gabbro
```

Do not rely on AI to write the exercise or provide an answer key. The included C starter intentionally provides the existing SDK scaffolding but not your requested extension.

## Dual-platform verification — Time 2 and Round 2

**Same activity, two displays:** [Pebble Time 2 / Emery](../../curriculum/dual-platform/README.md) uses a 200×228 rectangle; Pebble Round 2 / Gabbro uses a 260×260 circle. The existing learning outcome and competency rubric are unchanged. Any code you build should target both `emery` and `gabbro`, and you should check on both emulators for clipped text, invisible controls, and round-edge collisions. For non-coding work, account for both display geometries in your existing explanation/design—**this is not an additional assignment**.

Follow the [two-platform command and testing reference](../../curriculum/dual-platform/README.md). Compare actual results; a manifest listing two platforms is not evidence of successful compilation or physical sensor behavior. Round 2 touch is optional on watchapps; preserve button navigation and graceful touch-disabled behavior.
