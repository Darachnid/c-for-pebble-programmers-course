# Pebble SDK capability track (8A–8N)

14 additional labs, 1040 minutes (17h 20m), with **three cumulative Emery-only watchapps**. These complement the original 26 tasks and precede the 9A capstone.

| Lab | Subject | Project | Duration | Dependencies |
|---|---|---|---:|---|
| [8A](../../lessons/8A/) | Windows and layers | A | 60m | 7A, 3A |
| [8B](../../lessons/8B/) | Menus and scrolling | C | 75m | 8A, 4E |
| [8C](../../lessons/8C/) | Button interactions | A | 60m | 8A, 4H |
| [8D](../../lessons/8D/) | Custom drawing | C | 75m | 8B, 4D |
| [8E](../../lessons/8E/) | Graphics paths | C | 75m | 8D, 4F |
| [8F](../../lessons/8F/) | Bitmap manipulation | C | 90m | 8E, 4F |
| [8G](../../lessons/8G/) | Accelerometer | B | 90m | 8C, 4H |
| [8H](../../lessons/8H/) | Magnetometer / compass | B | 90m | 8G |
| [8I](../../lessons/8I/) | Ambient-light limits and backlight | B | 45m | 8H, 5C |
| [8J](../../lessons/8J/) | Vibration | B | 45m | 8I, 8C |
| [8K](../../lessons/8K/) | App timers | A | 75m | 8C, 4H |
| [8L](../../lessons/8L/) | Resource files | C | 65m | 8F, 5C |
| [8M](../../lessons/8M/) | Persistent storage | A | 75m | 8K, 7C |
| [8N](../../lessons/8N/) | Phone communication | C | 120m | 8L, 4H, 7B |

## Revisited programs

**A — Clock Workshop:** 7A time-only clock → 8A windows/layers → 8C buttons → 8K timers → 8M persistence.

**B — Field Instrument:** 8G accelerometer → 8H magnetic heading/compass → 8I backlight → 8J opt-in vibration.

**C — Pocket Field Guide:** 8B menus → 8D primitive drawing → 8E graphics paths → 8F mutable bitmap → 8L bundled data → 8N PebbleKit JS phone messaging.

All starter directories are independent local builds. A later stage is an *example checkpoint* for previous skills, not the solution to the current assignment. Use [the source-continuity matrix](checkpoint-continuity.md) to distinguish inherited code, current TODOs and optional cross-strand examples. Retain Git diffs, a normal and an edge test, API notes and evidence of cleanup.

**Caveats:** Watchfaces cannot receive click events; all 8X code is watchapp code. Compass requires `PBL_COMPASS` and calibration; the Light API does not expose ambient lux. No actual Emery device, phone link or SDK compilation was available in this editing session. The source is authored for SDK 4.33.1 but needs compilation/field verification.

[Chapter-to-capability matrix](capability-matrix.md) · [Official C SDK reference](https://developer.repebble.com/docs/c/)

## Optional fault-finding checkpoints (not extra required tasks)

- [8C button/navigation debugging](../../lessons/8C/debug/) — observable input bug
- [8I Light API debugging](../../lessons/8I/debug/) — compiler/linker diagnostic
- [8L raw-resource debugging](../../lessons/8L/debug/) — valid build, incorrect resource content

All three are separate **intentionally faulty** Emery projects. No answers are included. They should only be attempted after the corresponding capability lab.

## Competency integration

Each API exercise has a **primary and supporting core competency** and belongs to the [41-activity integrated sequence](../course-design/integrated-sequence.md), not an isolated last phase. Revised prerequisites: **8B = 4E + 4H; 8G = 4H + 5C; 8I = 8G + 5C; 8J = 8G + 4H; 8M = 8K + 4H**. The other project strands are not prerequisites unless essential. Review the [assessment rubric](../course-design/learning-outcomes-and-assessment.md) after each activity.
