# 19G — Structures, Enums, and Program State


> **Dual-platform note (course, not a textbook quotation):** The same C concepts and local exercises apply to Pebble Time 2 (`emery`, 200×228 rectangle) and Pebble Round 2 (`gabbro`, 260×260 circle). Source displays near the circular edge may need repositioning, but those geometry changes are SDK scaffolding—not additional C-language exercises. Build/check on both targets and consult the [platform guide](../dual-platform/README.md).

> **Scope and provenance:** Original course learning notes, organized around themes from Mike Jipping's *Learning C with Pebble*, Chapters 10 (Structured Data Types), 13 (Storage Classes and Qualifiers), 15 (Using the C Preprocessor). These are **not verbatim extracts** from the book. Source-derived material from Chapters 3–6 remains in modules 3A–10D.
>
> **Target:** Pebble Time 2 (Emery), SDK 4.33.1, C. Required local starter: [lessons/19G/starter/](../../lessons/19G/starter/).
>
> **Objective:** Represent related variables with a struct and named program modes with an enum.

## Structured data and named states

Chapter 10 introduces `struct`, `union`, `typedef`, and enumerations. Chapters 13 and 15 cover scope, qualifiers, and preprocessor choices. A `struct` groups related values; an `enum` supplies meaningful names for distinct modes.

```c
typedef enum { MODE_CLOCK, MODE_EDIT, MODE_HELP } Mode;
typedef struct {
  Mode mode;
  int counter;
  bool enabled;
} AppState;

static AppState s_state = { MODE_CLOCK, 0, true };
```

This is easier to extend and explain than scattering global integers with undocumented numbers. Use `switch` to handle valid modes and include an appropriate default case. Not every number is a state: distinguish program mode, input event, and data value.

A `const` object cannot be modified through that identifier. `static` has different effects depending on scope: a function-local static value persists between calls; a file-scope static declaration limits linkage to that source file. The preprocessor `#define` replaces tokens before C compilation, but typed constants and enum names often communicate intent more clearly.

## State machine design

Make a transition table with columns: current state, event, next state, visible response. For each event, decide which transitions should happen and which should be ignored. Check boundary and fallback states. For Emery, connect `BUTTON_ID_UP`, `BUTTON_ID_DOWN`, and `BUTTON_ID_SELECT` events to deliberate state transitions in a watchapp.

## Practice checkpoints

Add a new named mode, update the `switch`, and verify every allowed transition. Show that data remains unchanged in modes where input should be ignored. Explain which declarations should be `static` and why.


## Assigned project

[Open the complete Emery project for 19G](../../lessons/19G/). Add a PAUSED enum value and a timer count field to AppState; modify button handling so it changes score only in EDIT mode. Draw a transition table and test each mode (including the default/fallback case).

**Success evidence:** The modified project builds, its specified behavior is demonstrated, the learner explains the C constructs used, and edge cases are tested.

## Further reading

- Mike Jipping, *Learning C with Pebble*, Chapters 10 (Structured Data Types), 13 (Storage Classes and Qualifiers), 15 (Using the C Preprocessor) (2016).
- [Pebble C SDK API documentation](https://developer.repebble.com/docs/c/)
- [Complete local example projects](../../lessons/README.md)
