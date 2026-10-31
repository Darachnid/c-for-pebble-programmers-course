# C for Pebble Programmers — Emery and Gabbro course syllabus

**Version:** revised 41-activity self-directed syllabus · **Targets:** Pebble Time 2 (Emery, 200 × 228 rectangle) **and** Pebble Round 2 (Gabbro, 260 × 260 circle) · **Language:** C · **SDK:** 4.33.1 · **Focused study estimate:** **52h 35m** · **Schedule:** self-paced with prerequisite gates.

## Course purpose

Learn to design, implement, understand, test and independently extend Pebble apps. This is **not merely a catalog of SDK functions**: the technical capabilities support seven essential competencies, revisited throughout the course. You progress from a time-only watchface to three evolving dual-platform watchapps and finally to an independently conceived and built app. No university enrollment, attendance, grade, or fixed deadline is implied.

## Seven learning outcomes

By the end of the course, demonstrate all seven abilities independently:

| Core competency | Measurable outcome |
|---|---|
| **UI Design** | Create legible rectangular Emery and circular Gabbro layouts, navigate between screens, and communicate states and actions clearly. |
| **Idea Generation** | Develop alternatives, evaluate constraints, and justify an original app concept or representation. |
| **Algorithmic Thinking** | Trace execution, specify state/loop logic, and validate state transitions and boundary conditions. |
| **C Programming** | Write and explain C data/control flow, pointers, callback functions, object ownership, and resource safety. |
| **Resource Literacy** | Interpret SDK signatures and limits, locate sources, and make evidence-based API choices. |
| **Debugging and Testing** | Reproduce issues, form hypotheses, make minimal fixes, and verify regression and negative tests. |
| **Development Tools and Workflow** | Build, test, log, use Git, manage integration artifacts, and reproduce results independently. |

Each of the 40 preparatory activities has a primary and supporting competency; the capstone is evaluated against **all seven**. Primary task distribution: 10 C programming; 5 each in the other six competencies. Hours may vary by task; equal task counts do not imply equal time.

[Complete outcomes, evidence and capstone rubric](curriculum/course-design/learning-outcomes-and-assessment.md) · [All 41 activities mapped to competencies](curriculum/course-design/integrated-sequence.md)

## What you need

Pebble SDK 4.33.1, the **Emery and Gabbro emulators**, C build tools, Git, editor, and local source files. Use the actual Time 2 or Round 2 corresponding to each hardware claim where sensor calibration, vibration, backlight or physical device behavior must be confirmed; phone communications also need a connected compatible Pebble mobile environment. Do not present an emulator result as physical hardware verification. [Official C reference](https://developer.repebble.com/docs/c/).

**Start here:** [Dual-platform field guide](curriculum/dual-platform/README.md) · [Lesson index](lessons/README.md) · [C readings 3A–24H](curriculum/c-programming/README.md) · [Pebble API track](curriculum/pebble-api/README.md) · [Taskwarrior instructions](taskwarrior/README.md).

## Two-platform requirements (no new lessons)

| | Time 2 | Round 2 |
|---|---|---|
| SDK target | `emery` | `gabbro` |
| Display | 200×228 rectangle | 260×260 circle |
| Display/layout test | Text alignment and edge margins | Inset menu/text controls, no clipping at circular edges |
| Input | Four buttons; optional touch in watchapps | Four buttons; optional touch in watchapps |

**One C codebase, two built targets.** Every local project manifest contains `targetPlatforms: ["emery", "gabbro"]`. For each C exercise, build once and install/check separately with `pebble install --emulator emery` and `pebble install --emulator gabbro`; retain both platform results and avoid claiming physical-device validation from a simulator. For design/readings, account for the two shapes **within the existing exercise**, not as a new assignment. The SDK supports `PBL_ROUND`, dimension-aware layer bounds, and `PBL_TOUCH`, but touch must remain optional when disabled. The conservative safe-area helper included in recurring projects prevents Gabbro corner clipping. This maintains **41 activities, seven competencies and 52h 35m** of scheduled focused study. [Full platform guide](curriculum/dual-platform/README.md).

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

**Optional self-check (pilot):** After you finish Phase I activities (**1A** through **5A**), you may run the local [`assessor`](assessor/README.md) tool (`assess submit <ID>`) to compare your Git-backed evidence and `EVIDENCE.md` against course criteria and meets/below exemplars. It uses spaCy, not generative AI, does not help during exercises, and does not mark Taskwarrior tasks complete.

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
| [1A — Explore Pebble examples](lessons/1A/) | 20m | Idea Generation | Resource Literacy | None |
| [2A — Build and run a time-only C watchface](lessons/2A/) | 30m | Development Tools and Workflow | C Programming | None |
| [3A — Variables, Data Types, and Operators](lessons/3A/) | 120m | C Programming | Debugging and Testing | 2A |
| [4A — Find and document a Pebble API function](lessons/4A/) | 20m | Resource Literacy | C Programming | 3A |
| [5A — Change one visual property of a time-only watchface](lessons/5A/) | 30m | UI Design | Resource Literacy | 3A, 4A, 2A |
| [6A — Diagnose a simple compiler error](lessons/6A/) | 20m | Debugging and Testing | Development Tools and Workflow | 3A, 2A |
| [7B — Create a Git-based modification workflow](lessons/7B/) | 45m | Development Tools and Workflow | Debugging and Testing | 2A, 5A, 6A |

### Phase II — Control flow, code reading and first window

**Readiness checkpoint:** Explain control flow, trace callbacks, design an initial UI and articulate a bounded algorithm.

| ID / Activity | Time | Primary competency | Supporting competency | Prerequisites |
|---|---:|---|---|---|
| [8B — Conditional Execution and Decision Making](lessons/8B/) | 120m | C Programming | Algorithmic Thinking | 3A |
| [9C — Loops and Iteration](lessons/9C/) | 135m | C Programming | Algorithmic Thinking | 8B |
| [10D — Functions and Program Structure](lessons/10D/) | 150m | C Programming | Algorithmic Thinking | 9C |
| [11A — Trace the watchface lifecycle](lessons/11A/) | 30m | Algorithmic Thinking | C Programming | 10D, 2A |
| [12A — Windows and layers](lessons/12A/) | 60m | UI Design | Development Tools and Workflow | 2A, 11A |
| [13B — Add and style a date TextLayer](lessons/13B/) | 45m | UI Design | C Programming | 5A, 10D, 4A |
| [14B — Trace an existing feature through source code](lessons/14B/) | 45m | Resource Literacy | Algorithmic Thinking | 11A, 10D, 4A |
| [15B — Design a font-cycling algorithm](lessons/15B/) | 30m | Algorithmic Thinking | UI Design | 11A, 14B |
| [16B — Write a two-example remix brief](lessons/16B/) | 30m | Idea Generation | UI Design | 1A, 14B |

### Phase III — Memory, design, events and interactive foundations

**Readiness checkpoint:** Demonstrate C memory/state, original concept and interactive app behavior with tests.

| ID / Activity | Time | Primary competency | Supporting competency | Prerequisites |
|---|---:|---|---|---|
| [17E — Arrays, Strings, and Bounds](lessons/17E/) | 90m | C Programming | Debugging and Testing | 10D |
| [18F — Pointers, Indirection, and Memory Lifetime](lessons/18F/) | 105m | C Programming | Debugging and Testing | 17E |
| [19G — Structures, Enums, and Program State](lessons/19G/) | 105m | C Programming | Algorithmic Thinking | 18F |
| [20C — Research an unfamiliar Pebble capability](lessons/20C/) | 60m | Resource Literacy | C Programming | 17E, 14B |
| [21B — Diagnose a font-selection boundary bug](lessons/21B/) | 45m | Debugging and Testing | C Programming | 17E, 6A, 15B |
| [22C — Develop an original Pebble app concept](lessons/22C/) | 60m | Idea Generation | Resource Literacy | 16B, 20C |
| [23C — Design a state machine for an app](lessons/23C/) | 60m | Algorithmic Thinking | UI Design | 22C, 15B, 19G |
| [24H — Event-Driven Integration and Application Lifecycle](lessons/24H/) | 150m | C Programming | Development Tools and Workflow | 19G, 23C |
| [25C — Design a multi-mode Pebble interface](lessons/25C/) | 90m | UI Design | Idea Generation | 13B, 22C, 23C, 24H |
| [26B — Menus and scrolling](lessons/26B/) | 75m | UI Design | Algorithmic Thinking | 17E, 24H |
| [27C — Button interactions](lessons/27C/) | 60m | Algorithmic Thinking | C Programming | 12A, 24H |
| [28D — Custom drawing](lessons/28D/) | 75m | Idea Generation | UI Design | 26B, 10D |
| [29E — Graphics paths](lessons/29E/) | 75m | Algorithmic Thinking | UI Design | 28D, 18F |
| [30G — Accelerometer](lessons/30G/) | 90m | C Programming | Resource Literacy | 24H, 20C |

### Phase IV — Graphics, hardware, validation and integration

**Readiness checkpoint:** Verify the three recurring projects, record limitations and diagnose integration faults.

| ID / Activity | Time | Primary competency | Supporting competency | Prerequisites |
|---|---:|---|---|---|
| [31C — Integrate font browsing with persistent selection](lessons/31C/) | 150m | Development Tools and Workflow | Debugging and Testing | 25C, 24H, 14B, 7B |
| [32C — Diagnose a persistent-state integration bug](lessons/32C/) | 90m | Debugging and Testing | Development Tools and Workflow | 24H, 21B, 31C |
| [33F — Bitmap manipulation](lessons/33F/) | 90m | C Programming | Debugging and Testing | 29E, 18F |
| [34H — Magnetometer / compass](lessons/34H/) | 90m | Resource Literacy | C Programming | 30G |
| [35I — Ambient-light limits and backlight](lessons/35I/) | 45m | Resource Literacy | UI Design | 30G, 20C |
| [36J — Vibration](lessons/36J/) | 45m | Debugging and Testing | UI Design | 30G, 24H |
| [37K — App timers](lessons/37K/) | 75m | Debugging and Testing | Algorithmic Thinking | 27C, 24H |
| [38L — Resource files](lessons/38L/) | 65m | Idea Generation | Resource Literacy | 33F, 20C |
| [39M — Persistent storage](lessons/39M/) | 75m | Development Tools and Workflow | Debugging and Testing | 37K, 24H |
| [40N — Phone communication](lessons/40N/) | 120m | Development Tools and Workflow | C Programming | 38L, 24H, 7B |

### Phase V — Independent application capstone

**Readiness checkpoint:** Build and defend an original working app using all seven competencies.

| ID / Activity | Time | Primary competency | Supporting competency | Prerequisites |
|---|---:|---|---|---|
| [41A — Build and demonstrate an original Emery app](lessons/41A/) | 240m | Integrated capstone (all seven competencies) | All seven competencies | 22C, 25C, 32C, 36J, 39M, 40N |


## Three evolving project strands

| Project | Continuously revised lesson checkpoints | Learning trajectory |
|---|---|---|
| **Clock Workshop** | 2A → 12A → 27C → 37K → 39M | Time-only watchface reference → two-window watchapp → button behavior → AppTimer → persisted setting and recovery |
| **Field Instrument** | 30G → 34H → 35I → 36J | Accelerometer → magnetic heading and calibration → light API limitations → intentional vibration and negative tests |
| **Pocket Field Guide** | 26B → 28D → 29E → 33F → 38L → 40N | Menu/scrolling → custom drawing → GPath → writable bitmap → raw resource → phone messaging |

Each new lesson starts from a *completed prior-stage reference checkpoint*, not a solution to its current exercise. Changes completed in a previous lesson should remain present in later examples. The 2A time-only watchface remains a watchface; the new interactive projects are watchapps. **No dependency is imposed between unrelated project strands unless shared prerequisites truly require it.** See the [API coverage matrix](curriculum/pebble-api/capability-matrix.md).

## Reading and exercises

**C/SDK prerequisite policy:** [The 3A–10D framework-scaffolding guide](curriculum/c-programming/sdk-scaffolding.md) explains graphics/timer callbacks already given to novices. These are not hidden prerequisites or additional tasks; 12A/27C/28D/37K assess those APIs later. **Project continuity:** [A/B/C checkpoint matrix](curriculum/pebble-api/checkpoint-continuity.md) identifies behavior each next-stage starter must preserve.

**3A–10D:** Read the local chapters adapting *Learning C with Pebble* (Jipping, 2016), including the 11 distinct local Chapter 3–6 starter projects. **17E–24H:** Read the original C-focused course notes on arrays, pointers, structs and event-driven lifecycles. **12A–40N:** Consult each lesson's specific C API reference before editing its checkpoint. Keep coding exercises distinct from the written ideation, UI, tracing, resource-research and debugging exercises; none of these are optional simply because they produce no executable code.

**Optional debugging challenges:** 27C/debug (button navigation), 35I/debug (bad Light API call), 38L/debug (resource extraction); the original compulsory 6A/21B/32C remain. Optional challenges do not increase the required activity count or estimated total.

## Independent demonstration — 41A

The capstone implements the original concept developed in 22C and UI groundwork in 25C. You must deliver **a working, original app targeting both Emery and Gabbro**, integrating at least two cross-strand capabilities (or an equivalent justified integration), and defend implementation decisions with source references, normal/failure tests, Git history and a demo. Score each of the seven competencies 0–3; **every competency must reach 2+**. [Detailed capstone directions](lessons/41A/).

## Course management and validation status

Use `python3 taskwarrior/import_course.py` to synchronize activities, prerequisites and learning objectives, preserving existing completed tasks and personal annotations. To inspect: `task project:pebble.course list`, `task project:pebble.course unblocked`, and `task <ID> info`. Always work in a personal branch/copy, with a known-good baseline.

**Source/status transparency:** All local lesson/project paths and Emery target manifests should be checked, but C code and phone integrations have **not been fully compiled or physically validated in this editing environment**. Do not treat a passing manifest audit as a passing SDK build. Maintain separate statuses: source supplied, build passed, emulator passed, real-device passed. Hardware-only validation can remain pending while continuing other independently unlocked tasks.

## References

Jipping, M. (2016). *Learning C with Pebble*. GitBook. [Local C course reading index](curriculum/c-programming/README.md).

Pebble Developers. (n.d.). *C SDK documentation*. https://developer.repebble.com/docs/c/
