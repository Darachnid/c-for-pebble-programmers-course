# Emery lesson directory — 41 activities

Every activity has a numbered folder and an exact local starting project. All seven competencies now have [companion readings](../curriculum/README.md), alongside the [14-lab API track](../curriculum/pebble-api/README.md). All C programming exercises, including the old Chapter 3–6 examples, are now self-contained under the eight numbered C modules (3A, 8B, 9C, 10D, 17E, 18F, 19G, 24H).

| ID | Activity | Time | Depends on | Reading or exact starter |
|---|---|---:|---|---|
| [1A](1A/) | Explore Pebble examples | 20m | None | [Lesson folder](1A/) |
| [2A](2A/) | Build and run a time-only C watchface | 30m | None | [Lesson folder](2A/) |
| [3A](3A/) | Variables, Data Types, and Operators | 120m | 2A | [C module](../curriculum/c-programming/3A-variables-data-types-operators.md) |
| [4A](4A/) | Find and document a Pebble API function | 20m | 3A | [Lesson folder](4A/) |
| [5A](5A/) | Change one visual property of a time-only watchface | 30m | 3A, 4A, 2A | [Lesson folder](5A/) |
| [6A](6A/) | Diagnose a simple compiler error | 20m | 3A, 2A | [Lesson folder](6A/) |
| [7B](7B/) | Create a Git-based modification workflow | 45m | 2A, 5A, 6A | [Lesson folder](7B/) |
| [8B](8B/) | Conditional Execution and Decision Making | 120m | 3A | [C module](../curriculum/c-programming/8B-conditionals-decision-making.md) |
| [9C](9C/) | Loops and Iteration | 135m | 8B | [C module](../curriculum/c-programming/9C-loops-iteration.md) |
| [10D](10D/) | Functions and Program Structure | 150m | 9C | [C module](../curriculum/c-programming/10D-functions-program-structure.md) |
| [11A](11A/) | Trace the watchface lifecycle | 30m | 10D, 2A | [Lesson folder](11A/) |
| [12A](12A/) | Windows and layers | 60m | 2A, 11A | [Lesson folder](12A/) |
| [13B](13B/) | Add and style a date TextLayer | 45m | 5A, 10D, 4A | [Lesson folder](13B/) |
| [14B](14B/) | Trace an existing feature through source code | 45m | 11A, 10D, 4A | [Lesson folder](14B/) |
| [15B](15B/) | Design a font-cycling algorithm | 30m | 11A, 14B | [Lesson folder](15B/) |
| [16B](16B/) | Write a two-example remix brief | 30m | 1A, 14B | [Lesson folder](16B/) |
| [17E](17E/) | Arrays, Strings, and Bounds | 90m | 10D | [C module](../curriculum/c-programming/17E-arrays-strings.md) |
| [18F](18F/) | Pointers, Indirection, and Memory Lifetime | 105m | 17E | [C module](../curriculum/c-programming/18F-pointers-memory.md) |
| [19G](19G/) | Structures, Enums, and Program State | 105m | 18F | [C module](../curriculum/c-programming/19G-structs-enums-state.md) |
| [20C](20C/) | Research an unfamiliar Pebble capability | 60m | 17E, 14B | [Lesson folder](20C/) |
| [21B](21B/) | Diagnose a font-selection boundary bug | 45m | 17E, 6A, 15B | [Lesson folder](21B/) |
| [22C](22C/) | Develop an original Pebble app concept | 60m | 16B, 20C | [Lesson folder](22C/) |
| [23C](23C/) | Design a state machine for an app | 60m | 22C, 15B, 19G | [Lesson folder](23C/) |
| [24H](24H/) | Event-Driven Integration and Application Lifecycle | 150m | 19G, 23C | [C module](../curriculum/c-programming/24H-events-lifecycle.md) |
| [25C](25C/) | Design a multi-mode Pebble interface | 90m | 13B, 22C, 23C, 24H | [Lesson folder](25C/) |
| [26B](26B/) | Menus and scrolling | 75m | 17E, 24H | [Lesson folder](26B/) |
| [27C](27C/) | Button interactions | 60m | 12A, 24H | [Lesson folder](27C/) |
| [28D](28D/) | Custom drawing | 75m | 26B, 10D | [Lesson folder](28D/) |
| [29E](29E/) | Graphics paths | 75m | 28D, 18F | [Lesson folder](29E/) |
| [30G](30G/) | Accelerometer | 90m | 24H, 20C | [Lesson folder](30G/) |
| [31C](31C/) | Integrate font browsing with persistent selection | 150m | 25C, 24H, 14B, 7B | [Lesson folder](31C/) |
| [32C](32C/) | Diagnose a persistent-state integration bug | 90m | 24H, 21B, 31C | [Lesson folder](32C/) |
| [33F](33F/) | Bitmap manipulation | 90m | 29E, 18F | [Lesson folder](33F/) |
| [34H](34H/) | Magnetometer / compass | 90m | 30G | [Lesson folder](34H/) |
| [35I](35I/) | Ambient-light limits and backlight | 45m | 30G, 20C | [Lesson folder](35I/) |
| [36J](36J/) | Vibration | 45m | 30G, 24H | [Lesson folder](36J/) |
| [37K](37K/) | App timers | 75m | 27C, 24H | [Lesson folder](37K/) |
| [38L](38L/) | Resource files | 65m | 33F, 20C | [Lesson folder](38L/) |
| [39M](39M/) | Persistent storage | 75m | 37K, 24H | [Lesson folder](39M/) |
| [40N](40N/) | Phone communication | 120m | 38L, 24H, 7B | [Lesson folder](40N/) |
| [41A](41A/) | Build and demonstrate an original Emery app | 240m | 22C, 25C, 32C, 36J, 39M, 40N | [Lesson folder](41A/) |

## Three cumulative Emery watchapps

**Clock Workshop:** 2A → 12A → 27C → 37K → 39M. **Field Instrument:** 30G → 34H → 35I → 36J. **Pocket Field Guide:** 26B → 28D → 29E → 33F → 38L → 40N.

Optional debugging checkpoints: [27C](27C/debug/), [35I](35I/debug/), [38L](38L/debug/). The final independent app is [41A](41A/).

See the [integrated five-phase sequence](../curriculum/course-design/integrated-sequence.md), [competency rubric](../curriculum/course-design/learning-outcomes-and-assessment.md) and [legacy ID map](../taskwarrior/legacy-id-map.json).
