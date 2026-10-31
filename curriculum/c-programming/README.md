# Complete C Programming Track — 3A through 24H

This track contains eight progressively dependent C programming activities. The earlier 3A–10D chapters preserve the organization and substantial instructional text of Mike Jipping's *Learning C with Pebble* (Chapters 3–6); their eleven book exercise concepts now have local modern Emery-compatible C projects. The later 17E–24H reading modules are original course notes drawing on additional book chapter themes.

| ID | Topic | Source emphasis | Required local code | Prerequisite |
|---|---|---|---|---|
| [3A — Variables, Data Types, and Operators](3A-variables-data-types-operators.md) | Variables, Data Types, and Operators | Adapted book chapter text | [lessons/3A](../../lessons/3A/) | 2A |
| [8B — Conditional Execution and Decision Making](8B-conditionals-decision-making.md) | Conditional Execution and Decision Making | Adapted book chapter text | [lessons/8B](../../lessons/8B/) | 3A |
| [9C — Loops and Iteration](9C-loops-iteration.md) | Loops and Iteration | Adapted book chapter text | [lessons/9C](../../lessons/9C/) | 8B |
| [10D — Functions and Program Structure](10D-functions-program-structure.md) | Functions and Program Structure | Adapted book chapter text | [lessons/10D](../../lessons/10D/) | 9C |
| [17E — Arrays, Strings, and Bounds](17E-arrays-strings.md) | Arrays, Strings, and Bounds | Original source-informed course notes | [lessons/17E](../../lessons/17E/) | 10D |
| [18F — Pointers, Indirection, and Memory Lifetime](18F-pointers-memory.md) | Pointers, Indirection, and Memory Lifetime | Original source-informed course notes | [lessons/18F](../../lessons/18F/) | 17E |
| [19G — Structures, Enums, and Program State](19G-structs-enums-state.md) | Structures, Enums, and Program State | Original source-informed course notes | [lessons/19G](../../lessons/19G/) | 18F |
| [24H — Event-Driven Integration and Application Lifecycle](24H-events-lifecycle.md) | Event-Driven Integration and Application Lifecycle | Original source-informed course notes | [lessons/24H](../../lessons/24H/) | 19G, 23C |

### Module content and source status

- 3A–10D: substantial source-derived instructional text, with legacy cloud imports removed, the actual exercise starters linked locally, and hardware assumptions corrected where necessary.
- 17E: arrays and strings (book Chapters 7 and 9).
- 18F: pointers and memory (book Chapters 8 and 11).
- 19G: structs, enums, storage and preprocessor (book Chapters 10, 13 and 15).
- 24H: event-driven integration and debugging quality (book Chapters 14, 18 and 21).

### Requirements

All builds use `targetPlatforms: ["emery"]`, SDK 4.33.1, and `pebble install --emulator emery`. Each project folder includes source and build files; the 2016 hosted-IDE imports are not required. No reference answer code is provided.

### Evidence of completion

Meet the acceptance criteria in [the syllabus](../../SYLLABUS.md) and in each [lesson README](../../lessons/README.md), show the resulting code or design evidence, and explain the solution without AI assistance.


## Why these C lessons come before the Pebble API labs

Projects 3.1–6.4 include existing Window, Layer, drawing, tick and timer callbacks. Students **do not** need independent mastery of those APIs to complete the early C exercises. The [framework-scaffolding guide](sdk-scaffolding.md) explains their flow and identifies exactly which C expressions, branches, loops and helpers the learner should modify. Each of the eleven project READMEs separates the *given API* from the *required C change*.

This is deliberately a **just-in-time reading**, not a new assessed activity or a dependency on 12A–37K. Formal teaching of those SDK APIs occurs in their named capability lessons.

## Continue into the C SDK

The [14-lab Pebble API track](../pebble-api/README.md) extends this C track with three recurring Emery projects, introducing missing chapters on graphics, sensors, resources and communication.
