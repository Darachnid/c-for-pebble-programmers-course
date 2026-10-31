# C for Pebble Programmers — Complete Emery Syllabus

**Platform:** Pebble Time 2 (`emery`, rectangular 200 × 228) · **Language:** C · **SDK:** 4.33.1 · **Core skills:** 7 · **Required activities:** 40 · **Estimated focused time:** 48h 35m

## Purpose

Develop independent capability in **UI Design, Idea Generation, Algorithmic Thinking, C Programming, Resource Literacy, Debugging and Testing, and Development Tools and Workflow**. Progress through short, self-directed, example-based activities with explicit Taskwarrior prerequisites. The C programming track has **eight** activities (4A–4H), drawing on *Learning C with Pebble* and current Emery SDK conventions.

## Evidence-based completion

Each task is complete when (a) its stated functionality or written product meets the learning objective, (b) a tangible artifact supports that claim—code, emulator output, API note, pseudocode, sketch, or debugging record—and (c) the student can independently explain the work. Keep a versioned source diff where coding is involved. Attempt normal and boundary cases. Time spent alone is not evidence of mastery.

**Independent-work policy:** No AI-generated code, answers, diagrams, or debugging solutions during activities. Consult the in-repository starter code, SDK documentation, compiler diagnostics, logs and Git. Future grading arrangements are separate from this syllabus.

**Optional self-check (pilot):** After you finish selected activities (**7A**, **4A** in v1), you may run the local [`assessor`](assessor/README.md) tool (`assess submit <ID>`) to compare your Git-backed evidence and `EVIDENCE.md` against course criteria and meets/below exemplars. It uses spaCy, not generative AI, does not help during exercises, and does not mark Taskwarrior tasks complete.

## Guided materials for all seven competencies

Section 4 is not the whole course. The seven skills remain distinct and equally important *as competencies*, even though the eight C coding activities take more time. Each other skill now has a dedicated, progressively structured A–C reading, linked to its existing activities and local examples.

| Skill | Preparation reading | Activities | Estimated focused time | Evidence type |
|---|---|---|---:|---|
| UI Design | [Visual hierarchy, TextLayers, navigation](curriculum/ui-design/README.md) | [1A](lessons/1A/), [1B](lessons/1B/), [1C](lessons/1C/) | 2h 45m | Annotated screenshots and mode sketches |
| Idea Generation | [Explore, remix, specify](curriculum/idea-generation/README.md) | [2A](lessons/2A/), [2B](lessons/2B/), [2C](lessons/2C/) | 1h 50m | Idea inventory, remix brief, viable concept |
| Algorithmic Thinking | [Call traces, boundary logic, states](curriculum/algorithmic-thinking/README.md) | [3A](lessons/3A/), [3B](lessons/3B/), [3C](lessons/3C/) | 2h | Trace, pseudocode, transition table |
| C Programming | [Eight C chapters](curriculum/c-programming/README.md) | [4A–4H](#c-programming-progression) | 16h 15m | Build, diff, boundary tests |
| Resource Literacy | [API contracts, source reading, research](curriculum/resource-literacy/README.md) | [5A](lessons/5A/), [5B](lessons/5B/), [5C](lessons/5C/) | 2h 05m | Documented evidence, implementation plan |
| Debugging and Testing | [Reproduction, diagnosis, regression](curriculum/debugging-testing/README.md) | [6A](lessons/6A/), [6B](lessons/6B/), [6C](lessons/6C/) | 2h 35m | Before/after logs, minimal fix, tests |
| Development Tools and Workflow | [Build, Git, integration](curriculum/tools-workflow/README.md) | [7A](lessons/7A/), [7B](lessons/7B/), [7C](lessons/7C/) | 3h 45m | Reproducible build, commits, integration |
| **Cross-cutting Pebble APIs** | [14 cumulative capability labs](curriculum/pebble-api/README.md) | [8A–8N](curriculum/pebble-api/README.md) | 17h 20m | Three revisited Emery project families and API verification |

**Course-wide practice loop:** Predict → examine the **lesson-local** source → make a change or complete the written artifact → verify normal and boundary cases → explain and record evidence. A design sketch is assessed as design evidence, not as a C build; code work must be tested on `emery`.

**Revisited example families:** The **time-only clock** underpins 7A, 1A, 1B, 3A and 5A; the **font browser** underpins 5B, 3B, 6B and the final integration; the **persistent counter** underpins 2B, 5C and 7C/6C. These are related lesson-local versions, not one continuously edited original project. The original 26 foundational activities plus the 14 new Pebble SDK capability labs remain 40 tasks. Their existing prerequisites and time estimates are preserved.

See the [learning-materials index](curriculum/README.md) for the guide-to-lesson map and [contribution instructions](CONTRIBUTING.md) for Git help.

## C programming progression

| Activity | Core C subject | Local reading | Local starting code |
|---|---|---|---|
| **4A** | Variables, Data Types, and Operators | [Markdown reading](curriculum/c-programming/4A-variables-data-types-operators.md) | [Complete Emery lesson](lessons/4A/) |
| **4B** | Conditional Execution and Decision Making | [Markdown reading](curriculum/c-programming/4B-conditionals-decision-making.md) | [Complete Emery lesson](lessons/4B/) |
| **4C** | Loops and Iteration | [Markdown reading](curriculum/c-programming/4C-loops-iteration.md) | [Complete Emery lesson](lessons/4C/) |
| **4D** | Functions and Program Structure | [Markdown reading](curriculum/c-programming/4D-functions-program-structure.md) | [Complete Emery lesson](lessons/4D/) |
| **4E** | Arrays, Strings, and Bounds | [Markdown reading](curriculum/c-programming/4E-arrays-strings.md) | [Complete Emery lesson](lessons/4E/) |
| **4F** | Pointers, Indirection, and Memory Lifetime | [Markdown reading](curriculum/c-programming/4F-pointers-memory.md) | [Complete Emery lesson](lessons/4F/) |
| **4G** | Structures, Enums, and Program State | [Markdown reading](curriculum/c-programming/4G-structs-enums-state.md) | [Complete Emery lesson](lessons/4G/) |
| **4H** | Event-Driven Integration and Application Lifecycle | [Markdown reading](curriculum/c-programming/4H-events-lifecycle.md) | [Complete Emery lesson](lessons/4H/) |

Book-based exercises from Chapters 3–6 now have **11 complete, in-repository project starters** under `lessons/4A/projects` through `lessons/4D/projects`. Activities 4E–4H each supply their own independent C watchapp under `lessons/<ID>/starter`. The original historical chapter text is preserved in the first four readings with necessary Emery updates and links to these local examples.

## Recommended phase order and exact dependencies

### Phase I — Orientation and first C expressions

| Activity | Estimate | Difficulty | Priority | Depends on |
|---|---:|---|---|---|
| [2A Explore Pebble examples](lessons/2A/) | 20m | Low | High | None |
| [7A Build and run a time-only C watchface](lessons/7A/) | 30m | Low | High | None |
| [4A Variables, Data Types, and Operators](lessons/4A/) | 120m | Low | High | 7A |
| [5A Find and document a Pebble API function](lessons/5A/) | 20m | Low | High | 4A |
| [1A Change one visual property of a time-only watchface](lessons/1A/) | 30m | Low | High | 4A, 5A, 7A |
| [6A Diagnose a simple compiler error](lessons/6A/) | 20m | Low | High | 4A, 7A |
| [7B Create a Git-based modification workflow](lessons/7B/) | 45m | Medium | High | 7A, 1A, 6A |

### Phase II — Control flow, functions and interaction

| Activity | Estimate | Difficulty | Priority | Depends on |
|---|---:|---|---|---|
| [4B Conditional Execution and Decision Making](lessons/4B/) | 120m | Medium | High | 4A |
| [4C Loops and Iteration](lessons/4C/) | 135m | Medium | High | 4B |
| [4D Functions and Program Structure](lessons/4D/) | 150m | Medium | High | 4C |
| [3A Trace the watchface lifecycle](lessons/3A/) | 30m | Low | High | 4D, 7A |
| [1B Add and style a date TextLayer](lessons/1B/) | 45m | Medium | Medium | 1A, 4D, 5A |
| [5B Trace an existing feature through source code](lessons/5B/) | 45m | Medium | Medium | 3A, 4D, 5A |
| [3B Design a font-cycling algorithm](lessons/3B/) | 30m | Medium | Medium | 3A, 5B |
| [2B Write a two-example remix brief](lessons/2B/) | 30m | Medium | Medium | 2A, 5B |

### Phase III — Data, memory, state and original design

| Activity | Estimate | Difficulty | Priority | Depends on |
|---|---:|---|---|---|
| [4E Arrays, Strings, and Bounds](lessons/4E/) | 90m | Medium | High | 4D |
| [4F Pointers, Indirection, and Memory Lifetime](lessons/4F/) | 105m | High | High | 4E |
| [4G Structures, Enums, and Program State](lessons/4G/) | 105m | High | Medium | 4F |
| [5C Research an unfamiliar Pebble capability](lessons/5C/) | 60m | High | Medium | 4E, 5B |
| [6B Diagnose a font-selection boundary bug](lessons/6B/) | 45m | Medium | Medium | 4E, 6A, 3B |
| [2C Develop an original Pebble app concept](lessons/2C/) | 60m | High | Medium | 2B, 5C |
| [3C Design a state machine for an app](lessons/3C/) | 60m | High | Medium | 2C, 3B, 4G |
| [4H Event-Driven Integration and Application Lifecycle](lessons/4H/) | 150m | High | Medium | 4G, 3C |
| [1C Design a multi-mode Pebble interface](lessons/1C/) | 90m | High | Medium | 1B, 2C, 3C, 4H |

### Phase IV — Integration and independent verification

| Activity | Estimate | Difficulty | Priority | Depends on |
|---|---:|---|---|---|
| [7C Integrate font browsing with persistent selection](lessons/7C/) | 150m | High | Medium | 1C, 4H, 5B, 7B |
| [6C Diagnose a persistent-state integration bug](lessons/6C/) | 90m | High | Low | 4H, 6B, 7C |


| Lesson | Topic | Duration | Depends on |
|---|---|---:|---|
| [8A](lessons/8A/) | Windows and layers | 60m | 7A, 3A |
| [8B](lessons/8B/) | Menus and scrolling | 75m | 8A, 4E |
| [8C](lessons/8C/) | Button interactions | 60m | 8A, 4H |
| [8D](lessons/8D/) | Custom drawing | 75m | 8B, 4D |
| [8E](lessons/8E/) | Graphics paths | 75m | 8D, 4F |
| [8F](lessons/8F/) | Bitmap manipulation | 90m | 8E, 4F |
| [8G](lessons/8G/) | Accelerometer | 90m | 8C, 4H |
| [8H](lessons/8H/) | Magnetometer / compass | 90m | 8G |
| [8I](lessons/8I/) | Ambient-light limits and backlight | 45m | 8H, 5C |
| [8J](lessons/8J/) | Vibration | 45m | 8I, 8C |
| [8K](lessons/8K/) | App timers | 75m | 8C, 4H |
| [8L](lessons/8L/) | Resource files | 65m | 8F, 5C |
| [8M](lessons/8M/) | Persistent storage | 75m | 8K, 7C |
| [8N](lessons/8N/) | Phone communication | 120m | 8L, 4H, 7B |

#### 8A — Windows and layers

**Skill:** C Programming / SDK Lab · **Time:** 60m · **Prerequisites:** 7A, 3A

**Exact starting project:** [lessons/8A/starter/](lessons/8A/starter/) and [activity instructions](lessons/8A/README.md).

**Do:** Extend the time-only watchapp with a second Window and root/child layers; trace create/load/unload/destroy.

**Complete when:** Both screens can be displayed; illustrate layer hierarchy and clean teardown.

#### 8B — Menus and scrolling

**Skill:** C Programming / SDK Lab · **Time:** 75m · **Prerequisites:** 8A, 4E

**Exact starting project:** [lessons/8B/starter/](lessons/8B/starter/) and [activity instructions](lessons/8B/README.md).

**Do:** Build a six-entry scrolling Field Guide menu; implement draw_row and select_click; test the first, middle, and last rows.

**Complete when:** Six entries scroll smoothly and selecting a row changes the visible species.

#### 8C — Button interactions

**Skill:** C Programming / SDK Lab · **Time:** 60m · **Prerequisites:** 8A, 4H

**Exact starting project:** [lessons/8C/starter/](lessons/8C/starter/) and [activity instructions](lessons/8C/README.md).

**Do:** Add Select to open Clock Workshop details and Up/Down to adjust a bounded counter; Back returns via window stack.

**Complete when:** Three buttons and Back behave correctly, including minimum/maximum boundary cases.

#### 8D — Custom drawing

**Skill:** C Programming / SDK Lab · **Time:** 75m · **Prerequisites:** 8B, 4D

**Exact starting project:** [lessons/8D/starter/](lessons/8D/starter/) and [activity instructions](lessons/8D/README.md).

**Do:** Use a custom Field Guide Layer to draw a symbol using primitives; change its output on a menu selection and mark dirty.

**Complete when:** A visible non-clipped drawing changes on demand and you can explain the drawing callback.

#### 8E — Graphics paths

**Skill:** C Programming / SDK Lab · **Time:** 75m · **Prerequisites:** 8D, 4F

**Exact starting project:** [lessons/8E/starter/](lessons/8E/starter/) and [activity instructions](lessons/8E/README.md).

**Do:** Build a vertex-based species symbol using GPath; move it on selection and destroy it correctly.

**Complete when:** A graphics path appears in two positions and ownership/bounds are demonstrated.

#### 8F — Bitmap manipulation

**Skill:** C Programming / SDK Lab · **Time:** 90m · **Prerequisites:** 8E, 4F

**Exact starting project:** [lessons/8F/starter/](lessons/8F/starter/) and [activity instructions](lessons/8F/README.md).

**Do:** Create a 24x24 bitmap in memory, safely alter two-color pixels by row stride, and show it in a BitmapLayer.

**Complete when:** Pixels visibly change with no out-of-bounds writes; bitmap and layer are freed.

#### 8G — Accelerometer

**Skill:** C Programming / SDK Lab · **Time:** 90m · **Prerequisites:** 8C, 4H

**Exact starting project:** [lessons/8G/starter/](lessons/8G/starter/) and [activity instructions](lessons/8G/README.md).

**Do:** Subscribe to batched XYZ motion samples, rate-limit display and unsubscribe during shutdown.

**Complete when:** Hardware data or a documented emulator limitation with sample logs, rate, and cleanup.

#### 8H — Magnetometer / compass

**Skill:** C Programming / SDK Lab · **Time:** 90m · **Prerequisites:** 8G

**Exact starting project:** [lessons/8H/starter/](lessons/8H/starter/) and [activity instructions](lessons/8H/README.md).

**Do:** Add magnetic heading with CompassService; show unavailable/calibrating/valid states and guard unavailable hardware.

**Complete when:** Heading/calibration on supported hardware, otherwise a guarded unavailable report.

#### 8I — Ambient-light limits and backlight

**Skill:** C Programming / SDK Lab · **Time:** 45m · **Prerequisites:** 8H, 5C

**Exact starting project:** [lessons/8I/starter/](lessons/8I/starter/) and [activity instructions](lessons/8I/README.md).

**Do:** Add user-triggered backlight interaction. Explicitly distinguish the public backlight API from unavailable raw lux readings.

**Complete when:** Backlight interaction works and API note explains the ambient-light measurement limitation.

#### 8J — Vibration

**Skill:** C Programming / SDK Lab · **Time:** 45m · **Prerequisites:** 8I, 8C

**Exact starting project:** [lessons/8J/starter/](lessons/8J/starter/) and [activity instructions](lessons/8J/README.md).

**Do:** Add optional vibration to a deliberate user action; never vibrate on startup or continuously for sensor data.

**Complete when:** Explicit trigger and off mode are demonstrated; no repeated unintended feedback.

#### 8K — App timers

**Skill:** C Programming / SDK Lab · **Time:** 75m · **Prerequisites:** 8C, 4H

**Exact starting project:** [lessons/8K/starter/](lessons/8K/starter/) and [activity instructions](lessons/8K/README.md).

**Do:** Add a one-second elapsed counter to Clock Workshop while retaining minute tick for clock time. Reschedule/cancel safely.

**Complete when:** One running timer, correct elapsed output, and no callback after cleanup.

#### 8L — Resource files

**Skill:** C Programming / SDK Lab · **Time:** 65m · **Prerequisites:** 8F, 5C

**Exact starting project:** [lessons/8L/starter/](lessons/8L/starter/) and [activity instructions](lessons/8L/README.md).

**Do:** Bundle a raw field-note resource and read it with bounded NUL-terminated storage; compare read-only resources and persistent data.

**Complete when:** Raw file is loaded without overflow; truncation and empty cases are considered.

#### 8M — Persistent storage

**Skill:** C Programming / SDK Lab · **Time:** 75m · **Prerequisites:** 8K, 7C

**Exact starting project:** [lessons/8M/starter/](lessons/8M/starter/) and [activity instructions](lessons/8M/README.md).

**Do:** Save Clock Workshop's user-defined setting and restore safely on restart; reset invalid data, do not persist live seconds.

**Complete when:** Persistent, absent and invalid cases all behave as specified.

#### 8N — Phone communication

**Skill:** C Programming / SDK Lab · **Time:** 120m · **Prerequisites:** 8L, 4H, 7B

**Exact starting project:** [lessons/8N/starter/](lessons/8N/starter/) and [activity instructions](lessons/8N/README.md).

**Do:** Implement watch-to-phone request and phone-to-watch reply starting from src/js/app.js and the messageKeys manifest; keep offline fallback.

**Complete when:** Two-way log with success, failure and invalid payload behavior; no required continuous connection.


## Activity types

**Capability Labs:** Isolate one technique (e.g., TextLayers, iteration, button callbacks, arrays, persistence, or state) and test what it enables.

**Remix challenges (optional extension levels):** Modify one feature → customize several → borrow a feature → combine two projects → combine three → create an original application. Remix work supplements rather than replaces the 26 required activities.

## Working with local examples

Each lesson has its own folder and a README with exact instructions. Book projects have separate `package.json`, `wscript`, and `src/c/main.c` files. Use `pebble build`, `pebble install --emulator emery`, and `pebble logs --emulator emery` from the project directory.

**Debugging exercises:** 6A initially fails compilation with a deliberate syntax flaw; 6B compiles but has incorrect font-navigation logic; 6C compiles but restores the wrong stored value. Read diagnostics to identify the problem. Solutions are withheld.

## Taskwarrior tracking

Import or update with [taskwarrior/import_course.py](taskwarrior/import_course.py). The importer matches existing task IDs and preserves completion status and personal annotations while refreshing dependencies, estimates and course-generated directions.

```sh
python3 taskwarrior/import_course.py
task project:pebble.course list
task project:pebble.course unblocked
task <ID> info
```

## Format and permissions

The Markdown syllabus is canonical. [The PDF](SYLLABUS.pdf) covers 40 activities but precedes the new non-C companion-reading links. Review book-derived text in readings 4A–4D for rights/permissions before applying a blanket license; see [README license options](README.md#license-options-not-yet-selected) and [beginner contributing guide](CONTRIBUTING.md).

## References

Jipping, M. (2016). *Learning C with Pebble*. GitBook. Source-derived text is clearly marked in the associated learning modules.

Official C SDK documentation: https://developer.repebble.com/docs/c/

**Compatibility note:** The C samples are authored/port-adapted for Emery, but the Pebble SDK was not available for automated compilation in this environment. Students must validate builds with SDK 4.33.1 and the Emery emulator.

**Edition note:** `SYLLABUS.pdf` has been regenerated to include the 40-activity course.
