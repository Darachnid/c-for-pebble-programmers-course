# Pebble SDK capability track — 14 interleaved lessons

14 additional labs, 1040 minutes (17h 20m), with **three cumulative Emery-only watchapps**. These complement the original 26 tasks and precede the 41A capstone. The numeric prefixes establish the recommended course order, while the suffix letters are legacy identifiers without sequencing constraints.

| Lab | Subject | Project | Duration | Dependencies |
|---|---|---|---:|---|
| [12A](../../lessons/12A/) | Windows and layers | A | 60m | 2A, 11A |
| [26B](../../lessons/26B/) | Menus and scrolling | C | 75m | 17E, 24H |
| [27C](../../lessons/27C/) | Button interactions | A | 60m | 12A, 24H |
| [28D](../../lessons/28D/) | Custom drawing | C | 75m | 26B, 10D |
| [29E](../../lessons/29E/) | Graphics paths | C | 75m | 28D, 18F |
| [30G](../../lessons/30G/) | Accelerometer | B | 90m | 24H, 20C |
| [33F](../../lessons/33F/) | Bitmap manipulation | C | 90m | 29E, 18F |
| [34H](../../lessons/34H/) | Magnetometer / compass | B | 90m | 30G |
| [35I](../../lessons/35I/) | Ambient-light limits and backlight | B | 45m | 30G, 20C |
| [36J](../../lessons/36J/) | Vibration | B | 45m | 30G, 24H |
| [37K](../../lessons/37K/) | App timers | A | 75m | 27C, 24H |
| [38L](../../lessons/38L/) | Resource files | C | 65m | 33F, 20C |
| [39M](../../lessons/39M/) | Persistent storage | A | 75m | 37K, 24H |
| [40N](../../lessons/40N/) | Phone communication | C | 120m | 38L, 24H, 7B |

## Revisited programs

**A — Clock Workshop:** 2A time-only clock → 12A windows/layers → 27C buttons → 37K timers → 39M persistence.

**B — Field Instrument:** 30G accelerometer → 34H magnetic heading/compass → 35I backlight → 36J opt-in vibration.

**C — Pocket Field Guide:** 26B menus → 28D primitive drawing → 29E graphics paths → 33F mutable bitmap → 38L bundled data → 40N PebbleKit JS phone messaging.

All starter directories are independent local builds. A later stage is an *example checkpoint* for previous skills, not the solution to the current assignment. Use [the source-continuity matrix](checkpoint-continuity.md) to distinguish inherited code, current TODOs and optional cross-strand examples. Retain Git diffs, a normal and an edge test, API notes and evidence of cleanup.

**Caveats:** Watchfaces cannot receive click events; all 8X code is watchapp code. Compass requires `PBL_COMPASS` and calibration; the Light API does not expose ambient lux. No actual Emery device, phone link or SDK compilation was available in this editing session. The source is authored for SDK 4.33.1 but needs compilation/field verification.

[Chapter-to-capability matrix](capability-matrix.md) · [Official C SDK reference](https://developer.repebble.com/docs/c/)

## Optional fault-finding checkpoints (not extra required tasks)

- [27C button/navigation debugging](../../lessons/27C/debug/) — observable input bug
- [35I Light API debugging](../../lessons/35I/debug/) — compiler/linker diagnostic
- [38L raw-resource debugging](../../lessons/38L/debug/) — valid build, incorrect resource content

All three are separate **intentionally faulty** Emery projects. No answers are included. They should only be attempted after the corresponding capability lab.

## Competency integration

Each API exercise has a **primary and supporting core competency** and belongs to the [41-activity integrated sequence](../course-design/integrated-sequence.md), not an isolated last phase. Revised prerequisites: **26B = 17E + 24H; 30G = 24H + 20C; 35I = 30G + 20C; 36J = 30G + 24H; 39M = 37K + 24H**. The other project strands are not prerequisites unless essential. Review the [assessment rubric](../course-design/learning-outcomes-and-assessment.md) after each activity.
