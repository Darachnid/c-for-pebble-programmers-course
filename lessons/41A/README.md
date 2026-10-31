# 41A — Independently build, test, and present an original Emery app

**Primary assessment:** Integrated demonstration of all **seven core competencies** · **Estimate:** 240m (4h focused) · **Prerequisites:** 22C, 25C, 32C, 36J, 39M, 40N · **Platform:** Emery/Gabbro, SDK 4.33.1

## Starting point

[starter/](starter/) is an intentionally minimal standalone C watchapp with a single Window; it builds the application shell but implements none of your proposed features. Use your **own** idea/specification from 22C and your **own** UI sketches from 25C. Reference completed Clock Workshop, Field Instrument, and Pocket Field Guide checkpoints only as examples. Do not copy an entire finished app.

## Assignment

Build an original working Pebble application: establish a useful purpose and audience, compare two alternatives, select a limited feature set, implement at least two SDK capabilities from different project strands (or justify equivalent integration), write usable UI states, independently debug/test, and record a reproducible development history. Include normal, edge/failure and restart/disconnection tests as relevant. Prove the app is an **application** and not just a concept statement or visual mockup.

## Evidence and mastery

Deliver a Git-tracked application, a brief README with setup and trade-offs, source/SDK references, a 1-page engineering retrospective, a screen recording or hardware demo, and a seven-competency self-assessment. Use [the capstone rubric](../../curriculum/course-design/learning-outcomes-and-assessment.md): each competency must score **2/3 or better** with specific evidence. Keep distinct statuses for emulator-validated versus physical sensor/phone-validated claims. Grade the work yourself first and describe the weakest competence candidly.

## Build

```sh
cd lessons/41A/starter
pebble build
pebble install --emulator emery
pebble install --emulator gabbro
pebble logs --emulator emery
pebble logs --emulator gabbro
```

**Independent-work rule:** Do not use AI to write, debug, interpret the solution or self-assessment. SDK docs, your own previous work, API notes, compiler output, and project logs are allowed.

## Dual-platform verification — Time 2 and Round 2

**Same activity, two displays:** [Pebble Time 2 / Emery](../../curriculum/dual-platform/README.md) uses a 200×228 rectangle; Pebble Round 2 / Gabbro uses a 260×260 circle. The existing learning outcome and competency rubric are unchanged. Any code you build should target both `emery` and `gabbro`, and you should check on both emulators for clipped text, invisible controls, and round-edge collisions. For non-coding work, account for both display geometries in your existing explanation/design—**this is not an additional assignment**.

Follow the [two-platform command and testing reference](../../curriculum/dual-platform/README.md). Compare actual results; a manifest listing two platforms is not evidence of successful compilation or physical sensor behavior. Round 2 touch is optional on watchapps; preserve button navigation and graceful touch-disabled behavior.
