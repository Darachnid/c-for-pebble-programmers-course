# 4E — Arrays, Strings, and Bounds

**Skill:** C Programming · **Estimate:** 90m · **Difficulty:** Medium · **Priority:** High · **Prerequisites:** 4D

**Read:** [4E learning module](../../curriculum/c-programming/4E-arrays-strings.md)

**Use exactly:** [starter/](starter/) — an original Pebble SDK C watchapp targeting only Emery (200 × 228).

## Assignment

Expand the list to six messages; write a function returning the index of a requested item; ensure boundaries wrap; use snprintf to construct a safe label. Test the first/last index and an overlong string.

## Evidence-based completion

Use arrays and bounded C strings to represent multiple values without overrunning buffers. Submit: working Emery build, source diff, brief explanation of your solution, normal-case and boundary-case tests, and the required diagrams/notes where assigned.

## Running

```sh
cd lessons/4E/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
```

Do not rely on AI to write the exercise or provide an answer key. The included C starter intentionally provides the existing SDK scaffolding but not your requested extension.
