# Idea Generation — read alongside 1A, 16B and 22C

**Goal:** move from observing other programs to defining a feasible original Pebble application. A strong idea is neither a list of features nor a vague slogan; it is a clear user action, a visible result, and a plausible minimum implementation.

## 1A · Observe and vary

[Local lesson with clock, font browser and storage counter](../../lessons/1A/)

**Read first.** Separate **behavior** (what the program does) from **implementation** (how it does it) and **context** (who uses it and why). When you see a clock, ask what changes on a tick, what changes on a button press, and what exists after the app closes. These questions expose reusable capabilities: scheduled updates, input, display changes and persistence. Combining capabilities too early makes ideas hard to evaluate.

**Practice:** examine each local example as a small system: write one sentence for input, state and output. Generate five variations through distinct prompts: change the data, change the audience, change the interaction, add a constraint, or combine one existing behavior with a different purpose. Do not use five cosmetic variants of the same idea. Mark the one you would investigate first and state what evidence could invalidate it.

**Evidence:** five clearly different ideas, one selection and its technical unknown—not code.

## 16B · Remix two complete examples

[Local clock and counter projects](../../lessons/16B/)

**Read first.** A remix is not the same as copying two programs together. It requires an **interface between capabilities**. A time display is refreshed by a tick; persistent storage represents state across launches. If combined, decide what information is being saved, when it changes, when it is rendered, and when to load/save it. Two individually working projects can have conflicting global variables, lifecycles and event subscriptions.

**Practice:** write a one-page brief with (1) user/problem, (2) source feature A, (3) source feature B, (4) one interaction narrative, (5) smallest testable version, and (6) what is uncertain. Draw a rough flow: event → state change → visible output → persistence, omitting any step that does not apply. Estimate work in terms of unknown APIs and dependencies, not by how attractive the idea sounds.

**Evidence:** a concise remix brief with the files or functions you inspected and a verification plan. No integration code yet.

## 22C · Select a testable original concept

[Local layout, fonts and storage examples](../../lessons/22C/)

**Read first.** Prioritize **value, feasibility, and learning** separately. A feature can be useful but technologically inaccessible; another can be easy but teach nothing. Define the smallest outcome that could still demonstrate the concept on an Emery emulator. Separate necessary features from attractive extensions. A "minimum viable app" in this course is not necessarily publishable; it is a testable slice that exercises the intended interaction.

**Practice:** propose three concepts, each in one paragraph. Score them Low/Medium/High for personal value, technical uncertainty and learning opportunity, with one reason per score. Choose one, write a two-sentence user story, list the minimum buttons, states and display elements, and sketch one successful path plus one empty/error path. Flag features needing phone communication, sensors or resources as research items rather than claiming that a local starter already implements them.

**Evidence:** comparison table, selected concept, acceptance criteria, major technical unknowns and the smallest emulator demonstration you could run.

### Idea-quality review

A proposal is ready to move to 23C/25C when a peer can answer: Who is it for? What starts an action? What state changes? What appears on screen? What is the smallest proof? What might fail? Preserve rejected ideas; they are evidence of selection rather than wasted work.

**Examples stay local:** use [course example families](../README.md), and return to [the syllabus](../../SYLLABUS.md) for prerequisites. No external example is required to complete these lessons.
