# C for Pebble Programmers — Emery course syllabus

**Version:** revised 41-activity self-directed syllabus · **Target:** Pebble Time 2 (Emery, 200 × 228) · **Language:** C · **SDK:** 4.33.1 · **Focused study estimate:** **52h 35m** · **Schedule:** self-paced with prerequisite gates.

## Course purpose

Learn to design, implement, understand, test and independently extend Pebble apps. This is **not merely a catalog of SDK functions**: the technical capabilities support seven essential competencies, revisited throughout the course. You progress from a time-only watchface to three evolving watchapps and finally to an independently conceived and built app. No university enrollment, attendance, grade, or fixed deadline is implied.

## Seven learning outcomes

By the end of the course, demonstrate all seven abilities independently:

| Core competency | Measurable outcome |
|---|---|
| **UI Design** | Create legible Emery layouts, navigate between screens, and communicate states and actions clearly. |
| **Idea Generation** | Develop alternatives, evaluate constraints, and justify an original app concept or representation. |
| **Algorithmic Thinking** | Trace execution, specify state/loop logic, and validate state transitions and boundary conditions. |
| **C Programming** | Write and explain C data/control flow, pointers, callback functions, object ownership, and resource safety. |
| **Resource Literacy** | Interpret SDK signatures and limits, locate sources, and make evidence-based API choices. |
| **Debugging and Testing** | Reproduce issues, form hypotheses, make minimal fixes, and verify regression and negative tests. |
| **Development Tools and Workflow** | Build, test, log, use Git, manage integration artifacts, and reproduce results independently. |

Each of the 40 preparatory activities has a primary and supporting competency; the capstone is evaluated against **all seven**. Primary task distribution: 10 C programming; 5 each in the other six competencies. Hours may vary by task; equal task counts do not imply equal time.

[Complete outcomes, evidence and capstone rubric](curriculum/course-design/learning-outcomes-and-assessment.md) · [All 41 activities mapped to competencies](curriculum/course-design/integrated-sequence.md)

## What you need

Pebble SDK 4.33.1, the **Emery emulator**, C build tools, Git, editor, and local source files. Use an actual Pebble Time 2 where sensor calibration, vibration, backlight or physical device behavior must be confirmed; phone communications also need a connected compatible Pebble mobile environment. Do not present an emulator result as physical hardware verification. [Official C reference](https://developer.repebble.com/docs/c/).

**Start here:** [Lesson index](lessons/README.md) · [C readings 4A–4H](curriculum/c-programming/README.md) · [Pebble API track](curriculum/pebble-api/README.md) · [Taskwarrior instructions](taskwarrior/README.md).

## Learning method and assessment

For every lesson: **(1) Read and plan:** study the linked local reading/SDK signatures and express the intended change in your own words. **(2) Implement and test:** work from the local starter, commit your change, build/run, and test a normal plus a boundary/failure case. **(3) Reflect and transfer:** explain state and resource ownership, record a problem or trade-off, and name one additional use. Existing activities already specify their deliverables; these steps organize rather than replace them.

Score the activity's **primary and supporting competency** at 0–3 using the common rubric. Both must reach **2 or 3**, *and* the stated acceptance criteria must pass, before marking the activity complete. Do not conflate unverified hardware behavior with an implemented fallback.

| Level | Standard |
|---|---|
| **0 — Not demonstrated** | No functional evidence or intelligible explanation |
| **1 — Developing** | Partially demonstrated, with critical understanding/test gaps |
| **2 — Competent** | Correct or appropriately scoped result, independent explanation, normal and boundary tests, and saved evidence |
| **3 — Transferable** | Competent plus independent generalization to a new context with justified trade-offs |

**Independent-work policy:** Do not use AI-generated source, solutions, code explanations, diagrams or debugging fixes to complete exercises. Consult included starters, official SDK documentation, logs, compiler diagnostics and your own notes. Versioned evidence is required. [Detailed scoring and readiness gates](curriculum/course-design/learning-outcomes-and-assessment.md).

**Optional self-check (pilot):** After you finish selected activities (**7A**, **4A** in v1), you may run the local [`assessor`](assessor/README.md) tool (`assess submit <ID>`) to compare your Git-backed evidence and `EVIDENCE.md` against course criteria and meets/below exemplars. It uses spaCy, not generative AI, does not help during exercises, and does not mark Taskwarrior tasks complete.

## Recommended integrated course progression

The sequence **interleaves** C learning with UI work, ideation, algorithm design, research, debugging and tools. The API material no longer sits as a detached final block. Preserve all original IDs, and use the “Depends on” column and Taskwarrior to work out of order safely.

| Phase | Focus | Activities | Estimated study |
|---|---|---:|---:|
| **I** | Orientation and fundamentals | 7 | 4h 45m |
| **II** | Control flow, code reading and first window | 9 | 10h 45m |
| **III** | Memory, design, events and interactive foundations | 14 | 19h 00m |
| **IV** | Graphics, hardware, validation and integration | 10 | 14h 05m |
| **V** | Independent application capstone | 1 | 4h 00m |

### Phase I — Orientation and fundamentals

**Readiness checkpoint:** Working time-only watchface, baseline Git workflow and independent diagnostic explanation.

| ID / Activity | Time | Primary competency | Supporting competency | Prerequisites |
|---|---:|---|---|---|
| [2A — Explore Pebble examples](lessons/2A/) | 20m | Idea Generation | Resource Literacy | None |
| [7A — Build and run a time-only C watchface](lessons/7A/) | 30m | Development Tools and Workflow | C Programming | None |
| [4A — Variables, Data Types, and Operators](lessons/4A/) | 120m | C Programming | Debugging and Testing | 7A |
| [5A — Find and document a Pebble API function](lessons/5A/) | 20m | Resource Literacy | C Programming | 4A |
| [1A — Change one visual property of a time-only watchface](lessons/1A/) | 30m | UI Design | Resource Literacy | 4A, 5A, 7A |
| [6A — Diagnose a simple compiler error](lessons/6A/) | 20m | Debugging and Testing | Development Tools and Workflow | 4A, 7A |
| [7B — Create a Git-based modification workflow](lessons/7B/) | 45m | Development Tools and Workflow | Debugging and Testing | 7A, 1A, 6A |

### Phase II — Control flow, code reading and first window

**Readiness checkpoint:** Explain control flow, trace callbacks, design an initial UI and articulate a bounded algorithm.

| ID / Activity | Time | Primary competency | Supporting competency | Prerequisites |
|---|---:|---|---|---|
| [4B — Conditional Execution and Decision Making](lessons/4B/) | 120m | C Programming | Algorithmic Thinking | 4A |
| [4C — Loops and Iteration](lessons/4C/) | 135m | C Programming | Algorithmic Thinking | 4B |
| [4D — Functions and Program Structure](lessons/4D/) | 150m | C Programming | Algorithmic Thinking | 4C |
| [3A — Trace the watchface lifecycle](lessons/3A/) | 30m | Algorithmic Thinking | C Programming | 4D, 7A |
| [8A — Windows and layers](lessons/8A/) | 60m | UI Design | Development Tools and Workflow | 7A, 3A |
| [1B — Add and style a date TextLayer](lessons/1B/) | 45m | UI Design | C Programming | 1A, 4D, 5A |
| [5B — Trace an existing feature through source code](lessons/5B/) | 45m | Resource Literacy | Algorithmic Thinking | 3A, 4D, 5A |
| [3B — Design a font-cycling algorithm](lessons/3B/) | 30m | Algorithmic Thinking | UI Design | 3A, 5B |
| [2B — Write a two-example remix brief](lessons/2B/) | 30m | Idea Generation | UI Design | 2A, 5B |

### Phase III — Memory, design, events and interactive foundations

**Readiness checkpoint:** Demonstrate C memory/state, original concept and interactive app behavior with tests.

| ID / Activity | Time | Primary competency | Supporting competency | Prerequisites |
|---|---:|---|---|---|
| [4E — Arrays, Strings, and Bounds](lessons/4E/) | 90m | C Programming | Debugging and Testing | 4D |
| [4F — Pointers, Indirection, and Memory Lifetime](lessons/4F/) | 105m | C Programming | Debugging and Testing | 4E |
| [4G — Structures, Enums, and Program State](lessons/4G/) | 105m | C Programming | Algorithmic Thinking | 4F |
| [5C — Research an unfamiliar Pebble capability](lessons/5C/) | 60m | Resource Literacy | C Programming | 4E, 5B |
| [6B — Diagnose a font-selection boundary bug](lessons/6B/) | 45m | Debugging and Testing | C Programming | 4E, 6A, 3B |
| [2C — Develop an original Pebble app concept](lessons/2C/) | 60m | Idea Generation | Resource Literacy | 2B, 5C |
| [3C — Design a state machine for an app](lessons/3C/) | 60m | Algorithmic Thinking | UI Design | 2C, 3B, 4G |
| [4H — Event-Driven Integration and Application Lifecycle](lessons/4H/) | 150m | C Programming | Development Tools and Workflow | 4G, 3C |
| [1C — Design a multi-mode Pebble interface](lessons/1C/) | 90m | UI Design | Idea Generation | 1B, 2C, 3C, 4H |
| [8B — Menus and scrolling](lessons/8B/) | 75m | UI Design | Algorithmic Thinking | 4E, 4H |
| [8C — Button interactions](lessons/8C/) | 60m | Algorithmic Thinking | C Programming | 8A, 4H |
| [8D — Custom drawing](lessons/8D/) | 75m | Idea Generation | UI Design | 8B, 4D |
| [8E — Graphics paths](lessons/8E/) | 75m | Algorithmic Thinking | UI Design | 8D, 4F |
| [8G — Accelerometer](lessons/8G/) | 90m | C Programming | Resource Literacy | 4H, 5C |

### Phase IV — Graphics, hardware, validation and integration

**Readiness checkpoint:** Verify the three recurring projects, record limitations and diagnose integration faults.

| ID / Activity | Time | Primary competency | Supporting competency | Prerequisites |
|---|---:|---|---|---|
| [7C — Integrate font browsing with persistent selection](lessons/7C/) | 150m | Development Tools and Workflow | Debugging and Testing | 1C, 4H, 5B, 7B |
| [6C — Diagnose a persistent-state integration bug](lessons/6C/) | 90m | Debugging and Testing | Development Tools and Workflow | 4H, 6B, 7C |
| [8F — Bitmap manipulation](lessons/8F/) | 90m | C Programming | Debugging and Testing | 8E, 4F |
| [8H — Magnetometer / compass](lessons/8H/) | 90m | Resource Literacy | C Programming | 8G |
| [8I — Ambient-light limits and backlight](lessons/8I/) | 45m | Resource Literacy | UI Design | 8G, 5C |
| [8J — Vibration](lessons/8J/) | 45m | Debugging and Testing | UI Design | 8G, 4H |
| [8K — App timers](lessons/8K/) | 75m | Debugging and Testing | Algorithmic Thinking | 8C, 4H |
| [8L — Resource files](lessons/8L/) | 65m | Idea Generation | Resource Literacy | 8F, 5C |
| [8M — Persistent storage](lessons/8M/) | 75m | Development Tools and Workflow | Debugging and Testing | 8K, 4H |
| [8N — Phone communication](lessons/8N/) | 120m | Development Tools and Workflow | C Programming | 8L, 4H, 7B |

### Phase V — Independent application capstone

**Readiness checkpoint:** Build and defend an original working app using all seven competencies.

| ID / Activity | Time | Primary competency | Supporting competency | Prerequisites |
|---|---:|---|---|---|
| [9A — Build and demonstrate an original Emery app](lessons/9A/) | 240m | Integrated capstone (all seven competencies) | All seven competencies | 2C, 1C, 6C, 8J, 8M, 8N |


## Three evolving project strands

| Project | Continuously revised lesson checkpoints | Learning trajectory |
|---|---|---|
| **Clock Workshop** | 7A → 8A → 8C → 8K → 8M | Time-only watchface reference → two-window watchapp → button behavior → AppTimer → persisted setting and recovery |
| **Field Instrument** | 8G → 8H → 8I → 8J | Accelerometer → magnetic heading and calibration → light API limitations → intentional vibration and negative tests |
| **Pocket Field Guide** | 8B → 8D → 8E → 8F → 8L → 8N | Menu/scrolling → custom drawing → GPath → writable bitmap → raw resource → phone messaging |

Each new lesson starts from a *completed prior-stage reference checkpoint*, not a solution to its current exercise. Changes completed in a previous lesson should remain present in later examples. The 7A time-only watchface remains a watchface; the new interactive projects are watchapps. **No dependency is imposed between unrelated project strands unless shared prerequisites truly require it.** See the [API coverage matrix](curriculum/pebble-api/capability-matrix.md).

## Reading and exercises

**C/SDK prerequisite policy:** [The 4A–4D framework-scaffolding guide](curriculum/c-programming/sdk-scaffolding.md) explains graphics/timer callbacks already given to novices. These are not hidden prerequisites or additional tasks; 8A/8C/8D/8K assess those APIs later. **Project continuity:** [A/B/C checkpoint matrix](curriculum/pebble-api/checkpoint-continuity.md) identifies behavior each next-stage starter must preserve.

**4A–4D:** Read the local chapters adapting *Learning C with Pebble* (Jipping, 2016), including the 11 distinct local Chapter 3–6 starter projects. **4E–4H:** Read the original C-focused course notes on arrays, pointers, structs and event-driven lifecycles. **8A–8N:** Consult each lesson's specific C API reference before editing its checkpoint. Keep coding exercises distinct from the written ideation, UI, tracing, resource-research and debugging exercises; none of these are optional simply because they produce no executable code.

**Optional debugging challenges:** 8C/debug (button navigation), 8I/debug (bad Light API call), 8L/debug (resource extraction); the original compulsory 6A/6B/6C remain. Optional challenges do not increase the required activity count or estimated total.

## Independent demonstration — 9A

The capstone implements the original concept developed in 2C and UI groundwork in 1C. You must deliver **a working, original Emery app**, integrating at least two cross-strand capabilities (or an equivalent justified integration), and defend implementation decisions with source references, normal/failure tests, Git history and a demo. Score each of the seven competencies 0–3; **every competency must reach 2+**. [Detailed capstone directions](lessons/9A/).

## Course management and validation status

Use `python3 taskwarrior/import_course.py` to synchronize activities, prerequisites and learning objectives, preserving existing completed tasks and personal annotations. To inspect: `task project:pebble.course list`, `task project:pebble.course unblocked`, and `task <ID> info`. Always work in a personal branch/copy, with a known-good baseline.

**Source/status transparency:** All local lesson/project paths and Emery target manifests should be checked, but C code and phone integrations have **not been fully compiled or physically validated in this editing environment**. Do not treat a passing manifest audit as a passing SDK build. Maintain separate statuses: source supplied, build passed, emulator passed, real-device passed. Hardware-only validation can remain pending while continuing other independently unlocked tasks.

## References

Jipping, M. (2016). *Learning C with Pebble*. GitBook. [Local C course reading index](curriculum/c-programming/README.md).

Pebble Developers. (n.d.). *C SDK documentation*. https://developer.repebble.com/docs/c/
