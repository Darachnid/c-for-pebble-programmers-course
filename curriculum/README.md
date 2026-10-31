# Course-wide learning materials (Emery only)

This is a **seven-competency course**, not just a C-language textbook. Read the short preparation section of the relevant competency guide before each lesson, then use the *exact local starter* in that lesson folder. The eight [C modules](c-programming/README.md) provide the language depth; the other six guides develop the design, research, reasoning, debugging and workflow skills that turn C code into a usable watch app.

| Competency | Guide | Lessons | Primary evidence |
|---|---|---|---|
| UI Design | [Screens, hierarchy and navigation](ui-design/README.md) | [5A](../lessons/5A/), [13B](../lessons/13B/), [25C](../lessons/25C/) | Before/after screenshot, layout decisions, annotated screens |
| Idea Generation | [Observe, remix and specify](idea-generation/README.md) | [1A](../lessons/1A/), [16B](../lessons/16B/), [22C](../lessons/22C/) | Idea inventory, remix brief, smallest viable concept |
| Algorithmic Thinking | [Traces and state machines](algorithmic-thinking/README.md) | [11A](../lessons/11A/), [15B](../lessons/15B/), [23C](../lessons/23C/) | Execution trace, pseudocode, transition table |
| C Programming | [Eight C readings](c-programming/README.md) | [3A–24H](../SYLLABUS.md#c-programming-progression) | Builds, diffs, boundary tests, explanation |
| Resource Literacy | [Finding and assessing technical evidence](resource-literacy/README.md) | [4A](../lessons/4A/), [14B](../lessons/14B/), [20C](../lessons/20C/) | API note, source trace, justified implementation plan |
| Debugging and Testing | [Reproduce, isolate and verify](debugging-testing/README.md) | [6A](../lessons/6A/), [21B](../lessons/21B/), [32C](../lessons/32C/) | Symptom, evidence, minimal fix, regression test |
| Development Tools and Workflow | [Build, branch and integrate](tools-workflow/README.md) | [2A](../lessons/2A/), [7B](../lessons/7B/), [31C](../lessons/31C/) | Emery run, meaningful Git history, integration checklist |
| **Pebble API capability labs** | [Three cumulative Emery projects](pebble-api/README.md) | [12A–40N](../lessons/README.md) | Windows, drawing, sensors, resources, persistence and phone integration |

## Three recurring example families

Rather than starting over for each skill, revisit three small, locally included systems:

1. **Clock / time-only watchface.** Start at [2A](../lessons/2A/); adjust its visual hierarchy in 5A, extend with a date in 13B, trace lifecycle in 11A, document its APIs in 4A, diagnose a syntax fault in 6A, and practice Git in 7B.
2. **Font browser.** Discover it in 1A; trace button-to-display behavior in 14B; design wrapping in 15B; reason about arrays and state in 17E/19G; diagnose selection in 21B; sketch its modes in 25C.
3. **Persistent counter / saved selection.** Compare with clock for 16B; research the persist API in 20C; model transitions in 23C/24H; combine it with font browsing in 31C; investigate restart behavior in 32C.

The three families are **related examples, not guaranteed step-by-step snapshots of one unified codebase**. Each lesson's folder is authoritative; build each subproject separately unless the lesson explicitly asks you to integrate it.

## Repeatable learning loop

1. **Predict:** write one hypothesis about behavior, design or API use before opening the complete source.
2. **Inspect and act:** read the competency guide; inspect the local example; make a small change or produce the required reasoning artifact.
3. **Verify:** run on `emery` when coding, including a normal and boundary case; for design/research, validate against requirements and primary documentation.
4. **Explain and record:** save the artifact, a short explanation, and a source diff or citation trail. Completion requires evidence, not just elapsed time.

**Additional cumulative track:** Clock Workshop (12A/27C/37K/39M), Field Instrument (30G–36J), and Pocket Field Guide (26B/28D–33F/38L/40N) extend these foundational methods to platform capabilities. All 14 checkpoints retain independent local starters. They are part of the 40-activity syllabus, not extra optional material.

The [syllabus](../SYLLABUS.md) defines timing, prerequisites and acceptance criteria. [Lesson folders](../lessons/README.md) contain the actual source. The [PDF snapshot](../SYLLABUS.pdf) may lag behind the canonical Markdown syllabus until regenerated.

## Two supported watch platforms

All 41 activities now apply to both Pebble Time 2 (`emery`) and Pebble Round 2 (`gabbro`). The seven core competencies and course structure are unchanged. Read the [Emery/Gabbro compatibility and testing guide](dual-platform/README.md) for circular-safe layouts, optional touch and dual-emulator evidence.
