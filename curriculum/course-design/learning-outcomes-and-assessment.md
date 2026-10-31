# Learning outcomes, assessment, and readiness gates

This is a **self-directed Emery-only C programming course**, not a university credit course. It develops seven mutually reinforcing competencies through a cumulative set of C and SDK tasks. The [integrated course map](integrated-sequence.md) and [API project track](../pebble-api/README.md) provide the next steps.

## Seven measurable outcomes

| Competency | Observable outcome | Primary-competency labs |
|---|---|---|
| **UI Design** | Design readable, navigable interfaces for Emery's 200×228 display, justify layout and interaction choices, and implement feedback and accessible states. | 5A, 13B, 25C, 12A, 26B |
| **Idea Generation** | Generate alternatives, identify feasible constraints, remix examples ethically, and make a justified design choice for a real user or use case. | 1A, 16B, 22C, 28D, 38L |
| **Algorithmic Thinking** | Represent transformations, loops, state machines, and event sequences with pseudocode/diagrams and verify boundary cases. | 11A, 15B, 23C, 27C, 29E |
| **C Programming** | Read/write well-scoped C with validated data, memory lifetimes, callbacks, and structured state. | 3A–24H, 33F, 30G |
| **Resource Literacy** | Find authoritative APIs, read signatures/constraints, distinguish supported/unsupported features, and justify technical decisions from sources. | 4A, 14B, 20C, 34H, 35I |
| **Debugging and Testing** | Form a hypothesis, reproduce a failure, inspect logs/bounds, apply a minimal fix, and run regression/failure tests. | 6A, 21B, 32C, 36J, 37K |
| **Development Tools and Workflow** | Use a repeatable build/test/version-control process, manage artifacts and external integrations, and retain evidence of independent progress. | 2A, 7B, 31C, 39M, 40N |

**Primary** describes the lens through which work is assessed, **not** an exclusive category. Every lab must also exercise at least one supporting competency. The 14 API lessons are intentionally distributed **two apiece** across the seven competencies. With the original activities, the 40 non-capstone tasks have 10 C-primary and 5 primary in each other competency. The final capstone assesses all seven equally. This allocation is an instructional balance, not a claim that all tasks require the same amount of time or are equally difficult.

## Four-level mastery rubric

| Level | Evidence | Meaning |
|---|---|---|
| **0 — Not demonstrated** | No working or interpretable evidence; cannot explain. |
| **1 — Developing** | Partial implementation or explanation; important failure/edge case unresolved. |
| **2 — Competent** | Correct behavior or reasoned limitation, clear independent explanation, tested boundary case, and saved evidence. |
| **3 — Transferable** | Meets level 2 and independently applies the concept to a new context with justified trade-offs. |

For each activity score **(a) its primary competency** and **(b) its designated supporting competency**, separately, at 0–3. The activity is ready to mark complete at **2 or 3 in both** and with its documented technical acceptance criteria satisfied. Score 3 is not necessary for progression. A missing hardware capability can satisfy a *research and failure-handling* objective, but **not** a physical sensor measurement or an actual phone-to-watch round trip: distinguish “implementation ready; physical verification pending” from “hardware verified.” Keep tasks open when mandatory hardware-only evidence is unavailable; document blockers so the learning track can continue on a separate strand.

### Required evidence after each coding lab

1. **Read / plan:** State the assigned APIs and expected behavior in your own words; sketch a small flow, state change, or constraint before editing.
2. **Build / test:** Keep your own Git diff and a real build/emulator log (and physical-watch/phone evidence where required). Test one normal and one boundary/failure case.
3. **Reflect / transfer:** Explain which function owns the state and resources, what failed or changed, and one related use of the technique elsewhere. Self-score the two competencies and note any remaining issue.

The three steps are a workflow, not three new assignments. No AI-generated solutions, code explanations, diagrams or debugging fixes while completing course exercises. Students may consult source, official SDK docs, compiler diagnostics, logs, and their own notes.

## Readiness gates

| Gate | Before advancing | Check |
|---|---|---|
| **After Phase I** | Working 2A watchface and Git baseline | Can explain startup, use compiler diagnostics, and restore known-good code |
| **After Phase II** | C control-flow modules and initial UI design | Can trace callbacks and produce an original small algorithm with bounds |
| **After Phase III** | C pointers/state plus core integration | Can explain allocation/callback lifetime, failure cases, and an original app specification |
| **After Phase IV** | Three recurring projects; optional fault labs | Can build/run required features, demonstrate failure recovery, and state hardware validation limitations |
| **Final capstone (41A)** | Independent application grounded in 22C and 25C | Seven outcomes each scored 2+ with artifact and demo; no template-generated solution |

## Independent capstone rubric

Assess each of the seven competencies, 0–3, using evidence below. Pass = **at least 2 on each** (minimum 14/21 without a zero or one). A total score alone is insufficient.

| Competency | Capstone evidence of competency (level 2) |
|---|---|
| UI Design | Legible layout, meaningful button/menu behavior, and visible error/empty states. |
| Idea Generation | Original purpose and documented comparison of at least two feasible concepts before choosing. |
| Algorithmic Thinking | State diagram/pseudocode and at least two validated transition or boundary cases. |
| C Programming | Functional Emery C build, sensible ownership, validated inputs and lifecycle teardown. |
| Resource Literacy | Two authoritative API references with a reasoned implementation choice and documented limitations. |
| Debugging and Testing | Failure hypothesis, reproducible or deliberately injected test, minimal correction, and regression check. |
| Development Tools and Workflow | Versioned commits, reproducible build instructions, app demo and evidence directory. |

The capstone selects **at least two capabilities from different recurring projects** (or provides a justified integrated alternative), and implements them in a new application—rather than copying a fully finished checkpoint. Do not start it until the relevant prerequisite tasks are complete.
