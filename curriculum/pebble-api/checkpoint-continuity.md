# Source-continuity matrix: cumulative Emery projects

The three project families consist of **separately buildable examples**, not a shared source tree. Each later starter illustrates previously learned behavior, without finishing the *current* activity. The student should use their own earlier solution; these snapshots are references, not shortcuts. The notes below are based on **source inspection**, not an SDK build or physical hardware test.

## A — Clock Workshop

| Starter | Implemented before this activity | Student's new task | Evidence in next starter |
|---|---|---|---|
| [12A](../../lessons/12A/starter/) | Time-only example | Build two viewable windows | [27C](../../lessons/27C/starter/) launches showing details; Back returns to clock |
| [27C](../../lessons/27C/starter/) | Two windows, startup preview, Back | Select reopens details; bounded Up/Down | [37K](../../lessons/37K/starter/) has three click handlers and bounds 0–99 |
| [37K](../../lessons/37K/starter/) | Buttons, bounds and minute ticks | Safe AppTimer with cancellation | [39M](../../lessons/39M/starter/) schedules and cancels a timer |
| [39M](../../lessons/39M/starter/) | Counter + AppTimer callback count | Save and restore validated settings | No pre-completed next stage; submit your own proof |

The startup preview in 27C does not demonstrate Select-button navigation (still assigned to 27C). The 39M display counts *timer callbacks*, not necessarily precise elapsed wall time; see [#23](https://github.com/Darachnid/c-for-pebble-programmers-course/issues/23).

## B — Field Instrument

| Starter | Implemented before this activity | Student's new task | Evidence in next starter |
|---|---|---|---|
| [30G](../../lessons/30G/starter/) | Field display shell | Subscribe to XYZ and limit redraws | [34H](../../lessons/34H/starter/) uses latest sample with one accel redraw per clock second |
| [34H](../../lessons/34H/starter/) | Rate-limited accelerometer | Compass status and calibration | [35I](../../lessons/35I/starter/) distinguishes Unavailable, DataInvalid, Calibrating and Calibrated |
| [35I](../../lessons/35I/starter/) | XYZ + compass states | Backlight control and ambient-lux research | [36J](../../lessons/36J/starter/) has Up-triggered backlight |
| [36J](../../lessons/36J/starter/) | XYZ, compass and backlight | Opt-in vibration / off mode | No pre-completed next stage |

Rate limiting applies to **accelerometer-driven** draws only; a compass status event can redraw independently. `CompassStatusDataInvalid` means unusable calibration data; `CompassStatusCalibrating` provides usable but refining data. Hardware presence is guarded by `PBL_COMPASS` and requires a physical-watch check. 35I and 36J have *independent Taskwarrior prerequisites*: their sample checkpoint history is not an extra compulsory prerequisite.

## C — Pocket Field Guide

| Starter | Implemented before this activity | Student's new task | Evidence in next starter |
|---|---|---|---|
| [26B](../../lessons/26B/starter/) | Basic menu shell | Six scrolling/selection entries | [28D](../../lessons/28D/starter/) displays selected species |
| [28D](../../lessons/28D/starter/) | Menu/selection | Selection-dependent primitive drawing | [29E](../../lessons/29E/starter/) changes circle radius on selection |
| [29E](../../lessons/29E/starter/) | Selection-reactive drawing | GPath and movement | [33F](../../lessons/33F/starter/) moves a GPath on selection |
| [33F](../../lessons/33F/starter/) | Menu + primitives + path | Writable bitmap | [38L](../../lessons/38L/starter/) changes a bitmap on selection |
| [38L](../../lessons/38L/starter/) | Menu, graphics, bitmap, bundled file | Bounded resource loading | [40N](../../lessons/40N/starter/) reads a resource |
| [40N](../../lessons/40N/starter/) | Resource pattern and JS skeleton | Two-way AppMessage and offline fallback | Learner's own final artifact |

The previously reported counter bound and drawing regressions were repaired in an earlier commit and were preserved here. **Do not use** 27C/debug, 35I/debug or 38L/debug as checkpoints; their faults are intentionally planted.

## How to verify

For each stage, compare the preceding lesson's **completion criteria** with its next-stage starter. Verify normal operation, one edge case and SDK resource cleanup. C source inspection is **not** a substitute for `pebble build`, a real Emery install or actual sensor/phone validation. Report failures with the activity ID and relevant source commit.
