# Source-continuity matrix: cumulative Emery projects

The three project families consist of **separately buildable examples**, not a shared source tree. Each later starter illustrates previously learned behavior, without finishing the *current* activity. The student should use their own earlier solution; these snapshots are references, not shortcuts. The notes below are based on **source inspection**, not an SDK build or physical hardware test.

## A — Clock Workshop

| Starter | Implemented before this activity | Student's new task | Evidence in next starter |
|---|---|---|---|
| [8A](../../lessons/8A/starter/) | Time-only example | Build two viewable windows | [8C](../../lessons/8C/starter/) launches showing details; Back returns to clock |
| [8C](../../lessons/8C/starter/) | Two windows, startup preview, Back | Select reopens details; bounded Up/Down | [8K](../../lessons/8K/starter/) has three click handlers and bounds 0–99 |
| [8K](../../lessons/8K/starter/) | Buttons, bounds and minute ticks | Safe AppTimer with cancellation | [8M](../../lessons/8M/starter/) schedules and cancels a timer |
| [8M](../../lessons/8M/starter/) | Counter + AppTimer callback count | Save and restore validated settings | No pre-completed next stage; submit your own proof |

The startup preview in 8C does not demonstrate Select-button navigation (still assigned to 8C). The 8M display counts *timer callbacks*, not necessarily precise elapsed wall time; see [#23](https://github.com/Darachnid/c-for-pebble-programmers-course/issues/23).

## B — Field Instrument

| Starter | Implemented before this activity | Student's new task | Evidence in next starter |
|---|---|---|---|
| [8G](../../lessons/8G/starter/) | Field display shell | Subscribe to XYZ and limit redraws | [8H](../../lessons/8H/starter/) uses latest sample with one accel redraw per clock second |
| [8H](../../lessons/8H/starter/) | Rate-limited accelerometer | Compass status and calibration | [8I](../../lessons/8I/starter/) distinguishes Unavailable, DataInvalid, Calibrating and Calibrated |
| [8I](../../lessons/8I/starter/) | XYZ + compass states | Backlight control and ambient-lux research | [8J](../../lessons/8J/starter/) has Up-triggered backlight |
| [8J](../../lessons/8J/starter/) | XYZ, compass and backlight | Opt-in vibration / off mode | No pre-completed next stage |

Rate limiting applies to **accelerometer-driven** draws only; a compass status event can redraw independently. `CompassStatusDataInvalid` means unusable calibration data; `CompassStatusCalibrating` provides usable but refining data. Hardware presence is guarded by `PBL_COMPASS` and requires a physical-watch check. 8I and 8J have *independent Taskwarrior prerequisites*: their sample checkpoint history is not an extra compulsory prerequisite.

## C — Pocket Field Guide

| Starter | Implemented before this activity | Student's new task | Evidence in next starter |
|---|---|---|---|
| [8B](../../lessons/8B/starter/) | Basic menu shell | Six scrolling/selection entries | [8D](../../lessons/8D/starter/) displays selected species |
| [8D](../../lessons/8D/starter/) | Menu/selection | Selection-dependent primitive drawing | [8E](../../lessons/8E/starter/) changes circle radius on selection |
| [8E](../../lessons/8E/starter/) | Selection-reactive drawing | GPath and movement | [8F](../../lessons/8F/starter/) moves a GPath on selection |
| [8F](../../lessons/8F/starter/) | Menu + primitives + path | Writable bitmap | [8L](../../lessons/8L/starter/) changes a bitmap on selection |
| [8L](../../lessons/8L/starter/) | Menu, graphics, bitmap, bundled file | Bounded resource loading | [8N](../../lessons/8N/starter/) reads a resource |
| [8N](../../lessons/8N/starter/) | Resource pattern and JS skeleton | Two-way AppMessage and offline fallback | Learner's own final artifact |

The previously reported counter bound and drawing regressions were repaired in an earlier commit and were preserved here. **Do not use** 8C/debug, 8I/debug or 8L/debug as checkpoints; their faults are intentionally planted.

## How to verify

For each stage, compare the preceding lesson's **completion criteria** with its next-stage starter. Verify normal operation, one edge case and SDK resource cleanup. C source inspection is **not** a substitute for `pebble build`, a real Emery install or actual sensor/phone validation. Report failures with the activity ID and relevant source commit.
