# Pebble SDK scaffolding for C Programming 4A–4D

This is a **short primer**, not an extra activity or a prerequisite to all 8X API labs. It explains framework operations already present in the **local** C exercises, so the learner can concentrate on variables, decisions, loops and functions instead of having to understand graphics and timers immediately.

## The basic call flow

```text
main() → init() → window_stack_push() → window_load()
                   │                          │
                   │                          └→ attach drawing Layer
                   ↓
             app_event_loop()
                   ├→ button callback (Up/Down/Select)
                   ├→ minute/second TickTimerService callback
                   └→ AppTimer callback
                         ↓ (if state changes)
                   layer_mark_dirty()
                         ↓ (framework invokes update handler)
                   canvas_update(layer, context)
                   ↓
              app closes → deinit() → destroy owned resources
```

The framework calls handlers **later** in response to events. Registering a callback does not mean that your C code calls it directly.

## What to treat as given

- **Window / Layer / WindowHandlers:** The app creates and arranges display objects. C language exercises do not ask you to write these from scratch. Dedicated windows/layers study is [8A](../../lessons/8A/).
- **Graphics callback / GContext:** The SDK passes a drawing context. Expressions inside the drawing callback can use it without requiring general drawing mastery. Dedicated custom drawing comes in [8D](../../lessons/8D/).
- **AppTimer / TickTimerService:** A timer schedules callbacks or watch time changes. You can modify the values those handlers use without changing registration/cancellation code. Dedicated AppTimer study is [8K](../../lessons/8K/).
- **Click handlers:** Up/Down callbacks are ordinary C functions with SDK-prescribed signatures. In 4A, you change variable/condition expressions *inside* them. Full button interaction comes in [8C](../../lessons/8C/).
- **sin_lookup / cos_lookup:** Pebble supplies integer trigonometry for screen coordinates. In 3.2, focus on numeric types, angle increments, modulo and arithmetic; do not implement sine/cosine or a floating-point math library.
- **Strings and TextLayers:** The SDK can show text but the C rules for buffers and lifetimes still matter. These are studied explicitly in 4E and later API examples.

## The 11 C exercises: given API versus the actual C task

| Local project | Supplied framework / scaffolding | C-language work to perform |
|---|---|---|
| [Project 3.1](../../lessons/4A/projects/project-3-1/) | AppTimer drives motion; Window and Layer lifecycle call a graphics drawing callback and queue redraws. | s_x, s_y, x_velocity, y_velocity, ball_radius, advance(), and the TODO button handlers. Change variables/expressions; do not rewrite window or timer setup. |
| [Project 3.2](../../lessons/4A/projects/project-3-2/) | Timer advances degrees, custom Layer renders the letter; sin_lookup/cos_lookup convert an angle to screen coordinates. | s_degrees, s_radius, s_speed and the TODO click handlers. Treat trig lookup functions as supplied math tools; focus on casts, modulo, scaling and operators. |
| [Project 4.1](../../lessons/4B/projects/project-4-1/) | TickTimerService supplies seconds; a drawing callback renders the hand and a text label. | mark_the_second() and its conditional/switch logic; treat hand geometry and tick registration as provided. |
| [Project 4.2](../../lessons/4B/projects/project-4-2/) | TickTimerService populates a display buffer and a Layer renders clock text. | The conditional logic inside tick_handler(), including visual state and optionally boundary-only vibration. Do not redesign the timer service. |
| [Project 5.1](../../lessons/4C/projects/project-5-1/) | Up/Down click handlers change a decimal number; graphics_draw_text shows two strings. | Convert s_number to s_binary using a bounded loop; create/identify a shared conversion helper instead of altering Window or click registration. |
| [Project 5.2](../../lessons/4C/projects/project-5-2/) | A custom Layer draws a fixed 10×12 array of colored cells; Up and Down call replace_colors(). | The nested iteration and conditional inside replace_colors(); don't rewrite the rendering callback. |
| [Project 5.3](../../lessons/4C/projects/project-5-3/) | The Layer update callback gives a GContext and bounds; graphics_draw_text already renders one example label. | fill_screen() loops and screen coordinate arithmetic; leave window initialization and drawing callback registration unchanged. |
| [Project 6.1](../../lessons/4D/projects/project-6-1/) | The TickTimerService supplies seconds; the drawing callback produces the clock hand and outline. | is_five_second_mark() and the call site; identify clear function parameters, return values and contracts. Compare against existing logic rather than rebuilding the event loop. |
| [Project 6.2](../../lessons/4D/projects/project-6-2/) | A Layer draws a 3×5 digit pattern using small filled rectangles; Window and update callback are supplied. | Extract the repeated/dense drawing logic into functions accepting the pattern, position and dimensions. No need to redesign the SDK drawing API. |
| [Project 6.3](../../lessons/4D/projects/project-6-3/) | Window and Layer are created; a GRect is drawn and passed to fill_the_rectangle(). | Implement fill_the_rectangle() using the supplied ctx and box arguments; focus on signatures and parameter use. |
| [Project 6.4](../../lessons/4D/projects/project-6-4/) | A drawing callback and GContext are already prepared; draw_circles() draws concentric circles with a for loop. | Replace only draw_circles()'s loop with a recursive call and explicit base condition; keep Window and Layer plumbing untouched. |

## An independent-work protocol

1. **Predict:** Identify one variable/expression/branch/loop/helper you plan to change, and predict the effect.
2. **Modify:** Edit the C code identified in the project README; avoid rewriting unrelated SDK setup.
3. **Verify:** Run `pebble build` and `pebble install --emulator emery`; test one normal and one edge case.
4. **Explain:** Show the source diff and explain the **C concept**, not just what the screen looks like.

There is **no extra Taskwarrior requirement** to master the later API labs before 4A. This explicit distinction keeps the C course beginner-accessible, while subsequent 8A/8C/8D/8K lessons teach how the previously provided framework itself works.

The reference projects are Emery-targeted but have not all been independently build-tested using SDK 4.33.1; report SDK compatibility failures rather than treating them as part of a C variable exercise.
