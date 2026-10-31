# Emery lesson directory — 40 activities

Every activity has a numbered folder and an exact local starting project. All C programming exercises, including the old Chapter 3–6 examples, are now self-contained under **lessons/4A through lessons/4H**.

| ID | Activity | Time | Depends on | Source |
|---|---|---:|---|---|
| [2A](2A/) | Explore Pebble examples | 20m | None | [Local lesson](2A/) |
| [7A](7A/) | Build and run a time-only C watchface | 30m | None | [Local lesson](7A/) |
| [4A](4A/) | Variables, Data Types, and Operators | 120m | 7A | [Reading](../curriculum/c-programming/4A-variables-data-types-operators.md) |
| [5A](5A/) | Find and document a Pebble API function | 20m | 4A | [Local lesson](5A/) |
| [1A](1A/) | Change one visual property of a time-only watchface | 30m | 4A, 5A, 7A | [Local lesson](1A/) |
| [6A](6A/) | Diagnose a simple compiler error | 20m | 4A, 7A | [Local lesson](6A/) |
| [7B](7B/) | Create a Git-based modification workflow | 45m | 7A, 1A, 6A | [Local lesson](7B/) |
| [4B](4B/) | Conditional Execution and Decision Making | 120m | 4A | [Reading](../curriculum/c-programming/4B-conditionals-decision-making.md) |
| [4C](4C/) | Loops and Iteration | 135m | 4B | [Reading](../curriculum/c-programming/4C-loops-iteration.md) |
| [4D](4D/) | Functions and Program Structure | 150m | 4C | [Reading](../curriculum/c-programming/4D-functions-program-structure.md) |
| [3A](3A/) | Trace the watchface lifecycle | 30m | 4D, 7A | [Local lesson](3A/) |
| [1B](1B/) | Add and style a date TextLayer | 45m | 1A, 4D, 5A | [Local lesson](1B/) |
| [5B](5B/) | Trace an existing feature through source code | 45m | 3A, 4D, 5A | [Local lesson](5B/) |
| [3B](3B/) | Design a font-cycling algorithm | 30m | 3A, 5B | [Local lesson](3B/) |
| [2B](2B/) | Write a two-example remix brief | 30m | 2A, 5B | [Local lesson](2B/) |
| [4E](4E/) | Arrays, Strings, and Bounds | 90m | 4D | [Reading](../curriculum/c-programming/4E-arrays-strings.md) |
| [4F](4F/) | Pointers, Indirection, and Memory Lifetime | 105m | 4E | [Reading](../curriculum/c-programming/4F-pointers-memory.md) |
| [4G](4G/) | Structures, Enums, and Program State | 105m | 4F | [Reading](../curriculum/c-programming/4G-structs-enums-state.md) |
| [5C](5C/) | Research an unfamiliar Pebble capability | 60m | 4E, 5B | [Local lesson](5C/) |
| [6B](6B/) | Diagnose a font-selection boundary bug | 45m | 4E, 6A, 3B | [Local lesson](6B/) |
| [2C](2C/) | Develop an original Pebble app concept | 60m | 2B, 5C | [Local lesson](2C/) |
| [3C](3C/) | Design a state machine for an app | 60m | 2C, 3B, 4G | [Local lesson](3C/) |
| [4H](4H/) | Event-Driven Integration and Application Lifecycle | 150m | 4G, 3C | [Reading](../curriculum/c-programming/4H-events-lifecycle.md) |
| [1C](1C/) | Design a multi-mode Pebble interface | 90m | 1B, 2C, 3C, 4H | [Local lesson](1C/) |
| [7C](7C/) | Integrate font browsing with persistent selection | 150m | 1C, 4H, 5B, 7B | [Local lesson](7C/) |
| [6C](6C/) | Diagnose a persistent-state integration bug | 90m | 4H, 6B, 7C | [Local lesson](6C/) |

The default course uses Emery only. 6A is intentionally compiler-broken, while 6B and 6C contain deliberate runtime faults. No answers are supplied. Use `pebble build` followed by `pebble install --emulator emery` from each project directory.

## Added API labs (8A–8N)

| Lesson | Topic | Time | Prerequisites |
|---|---|---:|---|
| [8A](8A/) | Windows and layers | 60m | 7A, 3A |
| [8B](8B/) | Menus and scrolling | 75m | 8A, 4E |
| [8C](8C/) | Button interactions | 60m | 8A, 4H |
| [8D](8D/) | Custom drawing | 75m | 8B, 4D |
| [8E](8E/) | Graphics paths | 75m | 8D, 4F |
| [8F](8F/) | Bitmap manipulation | 90m | 8E, 4F |
| [8G](8G/) | Accelerometer | 90m | 8C, 4H |
| [8H](8H/) | Magnetometer / compass | 90m | 8G |
| [8I](8I/) | Ambient-light limits and backlight | 45m | 8H, 5C |
| [8J](8J/) | Vibration | 45m | 8I, 8C |
| [8K](8K/) | App timers | 75m | 8C, 4H |
| [8L](8L/) | Resource files | 65m | 8F, 5C |
| [8M](8M/) | Persistent storage | 75m | 8K, 7C |
| [8N](8N/) | Phone communication | 120m | 8L, 4H, 7B |

All 14 source checkpoints are local, self-contained Emery watchapps. Their progression is explained in [the Pebble API track](../curriculum/pebble-api/README.md).
