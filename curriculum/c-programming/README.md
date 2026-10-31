# Complete C Programming Track — 4A through 4H

This track contains eight progressively dependent C programming activities. The earlier 4A–4D chapters preserve the organization and substantial instructional text of Mike Jipping's *Learning C with Pebble* (Chapters 3–6); their eleven book exercise concepts now have local modern Emery-compatible C projects. The later 4E–4H reading modules are original course notes drawing on additional book chapter themes.

| ID | Topic | Source emphasis | Required local code | Prerequisite |
|---|---|---|---|---|
| [4A — Variables, Data Types, and Operators](4A-variables-data-types-operators.md) | Variables, Data Types, and Operators | Adapted book chapter text | [lessons/4A](../../lessons/4A/) | 7A |
| [4B — Conditional Execution and Decision Making](4B-conditionals-decision-making.md) | Conditional Execution and Decision Making | Adapted book chapter text | [lessons/4B](../../lessons/4B/) | 4A |
| [4C — Loops and Iteration](4C-loops-iteration.md) | Loops and Iteration | Adapted book chapter text | [lessons/4C](../../lessons/4C/) | 4B |
| [4D — Functions and Program Structure](4D-functions-program-structure.md) | Functions and Program Structure | Adapted book chapter text | [lessons/4D](../../lessons/4D/) | 4C |
| [4E — Arrays, Strings, and Bounds](4E-arrays-strings.md) | Arrays, Strings, and Bounds | Original source-informed course notes | [lessons/4E](../../lessons/4E/) | 4D |
| [4F — Pointers, Indirection, and Memory Lifetime](4F-pointers-memory.md) | Pointers, Indirection, and Memory Lifetime | Original source-informed course notes | [lessons/4F](../../lessons/4F/) | 4E |
| [4G — Structures, Enums, and Program State](4G-structs-enums-state.md) | Structures, Enums, and Program State | Original source-informed course notes | [lessons/4G](../../lessons/4G/) | 4F |
| [4H — Event-Driven Integration and Application Lifecycle](4H-events-lifecycle.md) | Event-Driven Integration and Application Lifecycle | Original source-informed course notes | [lessons/4H](../../lessons/4H/) | 4G, 3C |

### Module content and source status

- 4A–4D: substantial source-derived instructional text, with legacy cloud imports removed, the actual exercise starters linked locally, and hardware assumptions corrected where necessary.
- 4E: arrays and strings (book Chapters 7 and 9).
- 4F: pointers and memory (book Chapters 8 and 11).
- 4G: structs, enums, storage and preprocessor (book Chapters 10, 13 and 15).
- 4H: event-driven integration and debugging quality (book Chapters 14, 18 and 21).

### Requirements

All builds use `targetPlatforms: ["emery"]`, SDK 4.33.1, and `pebble install --emulator emery`. Each project folder includes source and build files; the 2016 hosted-IDE imports are not required. No reference answer code is provided.

### Evidence of completion

Meet the acceptance criteria in [the syllabus](../../SYLLABUS.md) and in each [lesson README](../../lessons/README.md), show the resulting code or design evidence, and explain the solution without AI assistance.

## Continue into the C SDK

The [14-lab Pebble API track](../pebble-api/README.md) extends this C track with three recurring Emery projects, introducing missing chapters on graphics, sensors, resources and communication.
