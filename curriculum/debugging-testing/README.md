# Debugging and Testing — read alongside 6A, 21B and 32C

**Goal:** work from observable evidence to a small, justified correction. These lessons contain **intentional defects**. The reading teaches the investigation method without naming the erroneous line, expression or key.

## The repeatable fault-investigation protocol

1. **Reproduce and record:** specify initial conditions, exact actions, expected behavior, actual behavior.
2. **Classify:** compiler error, runtime logic fault or lifecycle/persistence fault? Gather the right evidence—compiler output, `APP_LOG`, or repeated launches.
3. **Form one hypothesis:** state what would be observed if that cause were true.
4. **Change minimally:** alter one causal element; avoid unrelated refactoring or adopting a completed answer.
5. **Verify and regress:** repeat the failing scenario and nearby boundary cases; retain the before/after diff.

## 6A · Syntax and compiler feedback

[Deliberately broken local compiler lesson](../../lessons/6A/)

**Read first.** An error location identifies where the compiler became confused; the underlying mistake can be on that line or a preceding line. Distinguish errors from warnings and prioritize the **first meaningful diagnostic**: later errors may be consequences. A successful build only proves the source compiled, not that the requested behavior works.

**Practice:** run `pebble build` inside the lesson starter and save the first diagnostic. Categorize the message (syntax, type, name or other) before making any edit. Explain how the smallest correction addresses the compiler's complaint. Rebuild; only then install on Emery and observe the watchface.

**Evidence:** failing compiler excerpt, diagnosis, minimal diff and a working emulator run.

## 21B · Logic, invariants and boundaries

[Deliberately faulty font-navigation lesson](../../lessons/21B/)

**Read first.** A program may compile and still violate its specification. Define an **invariant** before searching for a line to change: every selected index must represent a valid item. Probe both directions and both ends of a finite list. Compare observed index logs against a transition table rather than relying on a vague impression that "Up feels wrong."

**Practice:** record initial index and each input from a reproducible sequence of Up/Down presses; inspect `APP_LOG` values. Make a prediction about what transition should occur at each boundary. Isolate the minimal behavior causing the mismatch and verify after correcting it.

**Evidence:** before/after input table, log excerpts, explanation and regression test. This guide does not disclose the deliberate fault.

## 32C · Persistence, restarts and temporal behavior

[Deliberately faulty save/restore lesson](../../lessons/32C/)

**Read first.** Restart bugs require examining **time and lifetime**. In-memory state disappears when the app exits; persistent state should survive it. A test that never closes the app cannot establish successful persistence. Distinguish first install (no stored key), saving a non-default value, restarting, and reading an invalid/outdated value. A correct log can still describe the wrong variable unless you trace the data path.

**Practice:** write a test matrix: fresh start; change selection; close/reopen once; close/reopen twice. Record expected vs actual selection and relevant startup/save messages. Investigate the supplied fault without inspecting a solved integrated implementation; make one minimal change and run the full matrix again.

**Evidence:** reproducible bug report, log trail, fix diff and regression matrix.

### Debugging report template

`Environment: SDK 4.33.1 / emery | Expected | Observed | Steps | Evidence | Hypothesis | Minimal change | Tests after fix | Remaining uncertainty`

Never include answers/spoilers for these lessons in a general curriculum pull request. Link back to [course overview](../README.md) and [lesson index](../../lessons/README.md).
