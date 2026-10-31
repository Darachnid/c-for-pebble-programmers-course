# 24H — Event-Driven Integration and Application Lifecycle

**Skill:** C Programming · **Estimate:** 150m · **Difficulty:** High · **Priority:** Medium · **Prerequisites:** 19G

## Competency checkpoint

**Primary:** C Programming · **Supporting:** Development Tools and Workflow. Explain the C state or pointer/callback lifetime and test normal, boundary, and cleanup behavior. Retain the original assignment's required output, and self-score **both competencies** at 0–3 using the [common rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md). This check adds no new independent activity.


**Read:** [24H learning module](../../curriculum/c-programming/24H-events-lifecycle.md)

**Use exactly:** [starter/](starter/) — an original Pebble SDK C watchapp targeting only Emery (200 × 228).

## Assignment

Create an additional user-visible mode that changes how buttons behave, add state validation on load, and demonstrate that the display updates via events rather than a busy loop. Verify restart persistence and explain every create/destroy and subscribe/unsubscribe pair.

## Evidence-based completion

Integrate button and time callbacks with persistent state and correct object lifetimes. Submit: working Emery build, source diff, brief explanation of your solution, normal-case and boundary-case tests, and the required diagrams/notes where assigned.

## Running

```sh
cd lessons/24H/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

Do not rely on AI to write the exercise or provide an answer key. The included C starter intentionally provides the existing SDK scaffolding but not your requested extension.
