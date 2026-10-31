# Algorithmic Thinking — read alongside 11A, 15B and 23C

**Goal:** be able to predict and specify behavior *before* writing code. Pebble is event-driven: startup, ticks, button presses and shutdown occur at different times, and callbacks are invoked by the framework rather than simply read in source-file order.

## 11A · Trace execution, not just function definitions

[Local time-only watchface](../../lessons/11A/)

**Read first.** A **call graph** shows which functions can call others; an **execution trace** shows which functions actually run in a particular scenario. These are different. A callback registration is not a call to the callback. The framework can invoke a handler after registration. In a watchface, distinguish startup initial rendering, a later minute tick, and teardown. An important test is whether a diagram falsely implies that `app_event_loop()` calls every handler directly.

**Practice:** trace two concrete scenarios: app launches, and one minute passes while it remains open. Label every arrow "direct call", "registration", or "framework callback". Then trace shutdown and identify what state or resources cease to exist. Compare the diagram against the actual names in your local starter; do not invent callbacks.

**Evidence:** a correctly labeled graph/trace and an explanation of how a scheduled minute update differs from the initial update.

## 15B · Specify bounded iteration and wraparound

[Local font browser](../../lessons/15B/)

**Read first.** A discrete selector has a state variable such as an index and a legal set of values. For a list of length `N`, valid indices are `0` through `N - 1` only when `N > 0`. Your design must decide whether movement **wraps** or **stops** at either end. Off-by-one errors come from mixing the item count with the last valid index. A correct algorithm also states what happens when there is one item, or no selectable item.

**Practice:** write language-independent pseudocode for Up and Down, then manually trace this input sequence: Up, Up, Down, Down from the first index. Repeat from the last index and for a one-item list. Specify exactly when the display refresh occurs. Do not edit the local C app during this design-only lesson.

**Evidence:** pseudocode, a compact table of inputs and indices, and a flowchart with all boundary decisions.

## 23C · Model modes as a state machine

[Local font browser + your 22C concept](../../lessons/23C/)

**Read first.** A finite-state model names (a) states, (b) events, (c) transition rules and (d) resulting output/actions. A screen is not automatically identical to a state: one screen can represent several modes with different button meanings. A transition table is more testable than a casual drawing because every state/event pair can be examined. Include invalid input and default state explicitly.

**Practice:** define three or fewer essential modes from your 22C concept. Draw directed transitions; then construct a table with columns Current state, Input, Guard/condition, Next state, Display or side effect. Simulate a normal path, an unexpected Back press, and reopening with missing state. State which transitions should be refused, ignored or redirected.

**Evidence:** state graph, complete table for the events you support, and manual traces for at least two edge cases.

### Reasoning tools to reuse

- **Precondition:** what must be true before a function or transition?
- **Invariant:** what must remain true (e.g., index in range)?
- **Postcondition:** what must be true afterward?
- **Boundary case:** what happens at zero, one, last or missing?
- **Event provenance:** what caused this callback and when?

Use these when designing arrays (17E), enum states (19G), event handling (24H), and regression tests (21B/32C). [Course index](../README.md).

## Pebble Round 2 alongside Time 2

Carry the **same competency** across a 200×228 rectangular Emery display and a 260×260 circular Gabbro display. Use existing examples and exercises, not extra assignments. When assessing UI/ideation/algorithms, consider the different readable region; when researching APIs or debugging, compare official feature support and each platform's emulator output. A two-target build is not a physical sensor test. See [the shared platform guide](../dual-platform/README.md).
