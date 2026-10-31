# Two-target development — Pebble Time 2 + Pebble Round 2

This is a **cross-cutting guide**, not an extra lesson or new prerequisite. All 41 activities retain their ID, order, duration and primary/supporting competencies. Adapt the same original C source and examples to **two** SDK platforms.

| Device | Platform | Display | Shape | Notes |
|---|---|---|---|---|
| Pebble Time 2 | `emery` | 200 × 228 | Rectangular, color | Touch-capable watchapps; buttons continue to work |
| Pebble Round 2 | `gabbro` | 260 × 260 | Circular, color | Round clipping, circular safe layout and touch settings |

**Sources:** [SDK platform list](https://developer.repebble.com/pebbleos/docs/sdk/), [hardware](https://developer.repebble.com/guides/tools-and-resources/hardware-information/), [shape/platform macros](https://developer.repebble.com/guides/best-practices/building-for-every-pebble/), [Round App UI](https://developer.repebble.com/round/), [Touch](https://developer.repebble.com/guides/events-and-services/touch/), [Gabbro framebuffer details](https://developer.repebble.com/guides/graphics-and-animations/framebuffer-graphics/).

## Build once per project, exercise both emulators

Each local `package.json` declares:

```json
"targetPlatforms": ["emery", "gabbro"]
```

From the **individual project folder**, for example `lessons/12A/starter`:

```sh
pebble sdk list
pebble build
pebble install --emulator emery
pebble logs --emulator emery
pebble install --emulator gabbro
pebble logs --emulator gabbro
```

The exact `pebble` commands require SDK 4.33.1 configured on your machine and compatible emulator runtimes. Use `bash scripts/test_dual_platform.sh lessons/12A/starter` from the repository root for a one-project build and install smoke test if both emulators are configured. That script will **not** claim to test physical accelerometer, compass, radio, touch hardware or battery behavior.

A passing manifest audit does **not** prove a successful compiler build, on-screen layout or hardware response. Save **separate build/installation evidence for each platform** and write down remaining problems.

## Rectangular versus circular UI

The 260×260 circle is **not** a full 260×260 content rectangle. Text and selectable rows near its corners can disappear. The recurring starter apps now include **their own local** `src/c/course_display.h`: `course_content_rect()` uses a conservative centered square on a round watch and small rectangular margins on Emery. The students can read the helper early, without being asked to invent round geometry before their C and layout lessons.

For your own edits, use `layer_get_bounds()` and `PBL_ROUND`/`PBL_IF_ROUND_ELSE()` rather than assuming a fixed width/height. Center text and short labels. Use a round-safe menu inset and verify the first/last items scroll into view. Recalculate graphics-path centers, draw bounds, bitmap positions and physical hit regions for each platform. For **framebuffer** manipulation, the firmware reports a circular 8-bit framebuffer on Gabbro; use its row metadata and valid pixel spans rather than assuming Emery's rectangular framebuffer layout. See the dedicated SDK documentation above.

The helper intentionally sacrifices some of the available circle area for reliable course examples. A later individual app may use a more ambitious polar layout—but only after demonstrating clipping-safe hit targets and text.

## Buttons, touch and feature differences

The existing exercises use **Up, Down, Select, Back**. Preserve those controls on **both** watches. Both have touch-capable watchapps, but touch may be disabled in settings. `PBL_TOUCH` indicates compile-time support; `touch_service_is_enabled()` determines whether touch is available at runtime. Add touch **only if already relevant to the current exercise**, and retain an equivalent button path. Never add required touch input to a watchface: watchfaces cannot receive button or touch events.

Both support accelerometer and a compass (guard SDK features such as `PBL_COMPASS` and handle calibration/unavailable states). **Do not infer every sensor API from the physical sensor list**: the C Light API does not expose ambient lux. Speaker and heart-rate availability differ between these watches; any future app using them should be gated on `PBL_SPEAKER` or `PBL_HEALTH`, not assume both support them. Physical sensors, vibration, phone communication and touch-disabled behavior require real-device or connected-phone testing before claiming those capabilities verified.

## Same evidence-based completion policy

- **C coding task:** collect a source diff, SDK explanation, and **Emery + Gabbro** build/run/screenshots (when the required environment is available), with one normal and boundary/failure case on each. Verify no text/menu/control is clipped on Round 2.
- **Design, idea, algorithm or source-analysis task:** compare the rectangular and circular design constraints within the task's **existing** deliverable. Do not invent an extra exercise.
- **Hardware-dependent task:** separate `build verified`, `emulator observed`, `device verified`, and `pending hardware test`. A missing physical watch is a blocker to hardware verification—not evidence of success.
- **Optional deliberate debugging challenges:** preserve the intentional flaws. Do not repair the learner's bug while adding platform support.
- **Capstone 41A:** one original C app with both `emery` and `gabbro` binaries and documented UI/interaction behavior; the same seven-competency scoring rubric still applies.

## Where to look next

[Complete 41-lesson index](../../lessons/README.md) · [Three cumulative project checkpoints](../pebble-api/checkpoint-continuity.md) · [Seven competencies and assessment](../course-design/learning-outcomes-and-assessment.md) · [Two-target static audit](../../scripts/check_dual_platform.py).
