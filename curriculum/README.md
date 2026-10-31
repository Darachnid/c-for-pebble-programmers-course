# Course-wide learning materials (Emery only)

This is a **seven-competency course**, not just a C-language textbook. Read the short preparation section of the relevant competency guide before each lesson, then use the *exact local starter* in that lesson folder. The eight [C modules](c-programming/README.md) provide the language depth; the other six guides develop the design, research, reasoning, debugging and workflow skills that turn C code into a usable watch app.

| Competency | Guide | Lessons | Primary evidence |
|---|---|---|---|
| UI Design | [Screens, hierarchy and navigation](ui-design/README.md) | [1A](../lessons/1A/), [1B](../lessons/1B/), [1C](../lessons/1C/) | Before/after screenshot, layout decisions, annotated screens |
| Idea Generation | [Observe, remix and specify](idea-generation/README.md) | [2A](../lessons/2A/), [2B](../lessons/2B/), [2C](../lessons/2C/) | Idea inventory, remix brief, smallest viable concept |
| Algorithmic Thinking | [Traces and state machines](algorithmic-thinking/README.md) | [3A](../lessons/3A/), [3B](../lessons/3B/), [3C](../lessons/3C/) | Execution trace, pseudocode, transition table |
| C Programming | [Eight C readings](c-programming/README.md) | [4A–4H](../SYLLABUS.md#c-programming-progression) | Builds, diffs, boundary tests, explanation |
| Resource Literacy | [Finding and assessing technical evidence](resource-literacy/README.md) | [5A](../lessons/5A/), [5B](../lessons/5B/), [5C](../lessons/5C/) | API note, source trace, justified implementation plan |
| Debugging and Testing | [Reproduce, isolate and verify](debugging-testing/README.md) | [6A](../lessons/6A/), [6B](../lessons/6B/), [6C](../lessons/6C/) | Symptom, evidence, minimal fix, regression test |
| Development Tools and Workflow | [Build, branch and integrate](tools-workflow/README.md) | [7A](../lessons/7A/), [7B](../lessons/7B/), [7C](../lessons/7C/) | Emery run, meaningful Git history, integration checklist |

## Three recurring example families

Rather than starting over for each skill, revisit three small, locally included systems:

1. **Clock / time-only watchface.** Start at [7A](../lessons/7A/); adjust its visual hierarchy in 1A, extend with a date in 1B, trace lifecycle in 3A, document its APIs in 5A, diagnose a syntax fault in 6A, and practice Git in 7B.
2. **Font browser.** Discover it in 2A; trace button-to-display behavior in 5B; design wrapping in 3B; reason about arrays and state in 4E/4G; diagnose selection in 6B; sketch its modes in 1C.
3. **Persistent counter / saved selection.** Compare with clock for 2B; research the persist API in 5C; model transitions in 3C/4H; combine it with font browsing in 7C; investigate restart behavior in 6C.

The three families are **related examples, not guaranteed step-by-step snapshots of one unified codebase**. Each lesson's folder is authoritative; build each subproject separately unless the lesson explicitly asks you to integrate it.

## Repeatable learning loop

1. **Predict:** write one hypothesis about behavior, design or API use before opening the complete source.
2. **Inspect and act:** read the competency guide; inspect the local example; make a small change or produce the required reasoning artifact.
3. **Verify:** run on `emery` when coding, including a normal and boundary case; for design/research, validate against requirements and primary documentation.
4. **Explain and record:** save the artifact, a short explanation, and a source diff or citation trail. Completion requires evidence, not just elapsed time.

The [syllabus](../SYLLABUS.md) defines timing, prerequisites and acceptance criteria. [Lesson folders](../lessons/README.md) contain the actual source. The [PDF snapshot](../SYLLABUS.pdf) may lag behind the canonical Markdown syllabus until regenerated.
