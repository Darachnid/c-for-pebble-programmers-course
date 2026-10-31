# Resource Literacy — read alongside 4A, 14B and 20C

**Goal:** find trustworthy technical information, determine what it actually promises, and connect it to code under test. Being able to locate an example is not the same as understanding an API contract or its limits.

## 4A · Read an API contract

[Local time-only watchface](../../lessons/4A/)

**Read first.** Official API documentation is a specification, not simply a snippet to paste. For each function identify: return type, argument types and ownership, required setup, invalid input, relevant side effects and matching cleanup. A `void` return means there is no return value; it does **not** mean the function can never fail. Distinguish a documented guarantee from an inference based on one example.

**Practice:** find `text_layer_set_font()` in the [Pebble C SDK](https://developer.repebble.com/docs/c/) and locate one call in your local starter. Write a six-line API card: purpose, signature, parameters, return, lifecycle/dependency, example call location. In your own words explain how a `TextLayer` is created before you configure it.

**Evidence:** the card with exact source file/function and a direct documentation URL; label any uncertainty explicitly.

## 14B · Follow behavior across functions

[Local font browser](../../lessons/14B/)

**Read first.** You rarely understand an application from a single line. Start with an observable event (Up/Down press), find its handler and follow control flow through state mutation to the screen update. Ask what owns the data and which function refreshes the visible result. Ignore irrelevant functions until the path is clear. This is code reading with a falsifiable claim: "pressing Up changes X, which triggers Y."

**Practice:** produce a path with at least four points: event registration/handler → old state → state update → applied font/display change. Record exact file and function locations; compare SDK documentation for unfamiliar calls. Build and run to confirm the trace matches observation.

**Evidence:** annotated source trace, one predicted behavior, the actual result and any discrepancy.

## 20C · Research an unfamiliar capability responsibly

[Local persistent counter](../../lessons/20C/)

**Read first.** A feasible implementation plan must identify *constraints*, not just function names. Persistence raises questions about key identifiers, data types, startup defaults, failure cases and state validity across versions. Resource ownership and limited storage may also matter. The same research discipline later applies to phone messaging, resources and sensors, but a capability's mention does not mean it is already implemented in this repo.

**Practice:** trace `persist_exists`, `persist_read_int` and `persist_write_int` in the local counter. Check current SDK docs for their contracts, then propose a stepwise plan for saving the font selector's chosen index. Specify a default when nothing is saved and a fallback if a stored index exceeds the font list. Keep this a plan, not a copy-pasted completed solution.

**Evidence:** short technical note containing primary references, implementation steps, risks, test cases and an explicit "not verified" list.

### Source evaluation checklist

Prefer current official SDK docs for API guarantees; consult bundled examples for usage; use compiler logs and emulator runs for actual behavior. Write down SDK version (4.33.1), target (`emery`) and when a source applies to a different device or older SDK. If sources disagree, record the discrepancy instead of silently choosing one. [Course index](../README.md).

## Pebble Round 2 alongside Time 2

Carry the **same competency** across a 200×228 rectangular Emery display and a 260×260 circular Gabbro display. Use existing examples and exercises, not extra assignments. When assessing UI/ideation/algorithms, consider the different readable region; when researching APIs or debugging, compare official feature support and each platform's emulator output. A two-target build is not a physical sensor test. See [the shared platform guide](../dual-platform/README.md).
