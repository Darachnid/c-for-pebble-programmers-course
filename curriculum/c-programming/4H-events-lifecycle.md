# 4H — Event-Driven Integration and Application Lifecycle

> **Scope and provenance:** Original course learning notes, organized around themes from Mike Jipping's *Learning C with Pebble*, Chapters 14 (Sensors and Events), 18 (User Interface Development), 21 (Writing High-Quality, Debuggable Code). These are **not verbatim extracts** from the book. Source-derived material from Chapters 3–6 remains in modules 4A–4D.
>
> **Target:** Pebble Time 2 (Emery), SDK 4.33.1, C. Required local starter: [lessons/4H/starter/](../../lessons/4H/starter/).
>
> **Objective:** Integrate button and time callbacks with persistent state and correct object lifetimes.

## Integrating event-driven systems

Chapters 14 and 18 of the book cover Pebble services, user interface and callbacks; Chapter 21 covers maintainability and debugging. Pebble applications are event-driven. Their `main()` calls initialization, then `app_event_loop()`, then cleanup. Callbacks run in response to events: button clicks, ticks, sensor updates or phone messages. Do not implement continuous updates with a busy `while(1)` loop.

## Typical lifecycle

```c
static void init(void) {
  // Create Window, configure click handlers, push Window.
  // Subscribe to TickTimerService only if needed.
}
static void deinit(void) {
  // Unsubscribe from services, then destroy owned resources.
}
int main(void) {
  init();
  app_event_loop();
  deinit();
}
```

Watchfaces display time and respond to services; interactive watchapps can use Up/Down buttons for custom interaction. An Emery build must declare `targetPlatforms: ["emery"]`. In a watchapp, use `window_set_click_config_provider()` to register callbacks, and `text_layer_set_text()` to display app-owned text.

A TickTimerService callback supplies a `struct tm *`. A button handler supplies a `ClickRecognizerRef`. The signatures matter because the SDK, not your application, invokes them. Unused parameters can be explicitly marked with `(void)parameter` to avoid warnings.

## Persistence, cleanup and observability

`persist_exists()`, `persist_read_int()`, and `persist_write_int()` allow simple state to survive app restarts. Select an unused application-local key and validate restored values. Use `APP_LOG()` for diagnostic information; it is not user-visible text. Inspect logs with `pebble logs --emulator emery`. Retain a working baseline in Git and change one subsystem at a time.

The simplest successful integration test checks startup without saved data, button interaction, changes at a minute boundary, a close/reopen cycle, and correct cleanup. The intended outcome is independent C development rather than copying a completed program.

## Practice checkpoints

Extend the starter with a second mode. Draw a state diagram. Implement a mode-dependent button action, demonstrate at least one timer or service callback, and show that stored data survives a restart. Identify every callback registration, the state it changes, and the display update it triggers.


## Assigned project

[Open the complete Emery project for 4H](../../lessons/4H/). Create an additional user-visible mode that changes how buttons behave, add state validation on load, and demonstrate that the display updates via events rather than a busy loop. Verify restart persistence and explain every create/destroy and subscribe/unsubscribe pair.

**Success evidence:** The modified project builds, its specified behavior is demonstrated, the learner explains the C constructs used, and edge cases are tested.

## Further reading

- Mike Jipping, *Learning C with Pebble*, Chapters 14 (Sensors and Events), 18 (User Interface Development), 21 (Writing High-Quality, Debuggable Code) (2016).
- [Pebble C SDK API documentation](https://developer.repebble.com/docs/c/)
- [Complete local example projects](../../lessons/README.md)
