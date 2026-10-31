# UI Design — read alongside 5A, 13B and 25C

**Goal:** turn an idea into legible, coherent interactions on **Pebble Time 2 / Emery's rectangular 200 × 228 display**. Design involves choices about attention, feedback and input, not only fonts and colors. Use the source under each linked lesson, not an unrelated platform's screenshots.

## 5A · One purposeful visual change

[Local lesson and clock starter](../../lessons/5A/)

**Read first.** A watchface is read in a glance: a person should find the primary datum immediately. Four design variables compete for attention: hierarchy (which datum first?), position, typographic weight/size, and contrast. The display is small, but do not assume every available pixel should be filled. The value of negative space is that it separates related information. Contrast is a functional requirement, especially outdoors.

**Observe:** in the time-only starter, identify (a) the only datum and (b) what makes it most noticeable. Predict how changing **just one** parameter—alignment, typeface, foreground/background color or position—will change readability. Do not modify several at once: doing so prevents you from isolating cause and effect.

**Practice:** make a quick before-and-after sketch with dimensions or approximate positions; implement the single change; compare the two emulator views at the same time value. Check that digits do not clip at a wide time such as 11:59. If you changed color, note whether the displayed time still has strong contrast.

**Evidence:** emulator screenshots, exactly one intentional property change in the diff, and two sentences explaining the design tradeoff. *Checkpoint:* can a reader identify the change without reading your code?

## 13B · Add a second datum without losing hierarchy

[Local lesson and time-only starter](../../lessons/13B/)

**Read first.** Adding a date creates a hierarchy problem: two layers can compete, overlap or become too small. Decide whether the date is secondary metadata or equal priority. Draw bounding rectangles before writing coordinates. A `TextLayer` has a frame, an alignment, a font and text storage; its visible result depends on all of them. Creation, attachment, updates and destruction are **lifecycle concerns** as well as layout concerns.

**Observe:** read the existing time layer's positioning and update path. Decide where date belongs and how much space it needs, then sketch two alternatives (e.g., stacked and separated). Choose one based on readability, not novelty.

**Practice:** add the date layer yourself using the lesson's source. Test a short and long date display, and observe behavior when the minute changes. A date format that looks fine on one day may clip on another; note this as a boundary condition. Do not paste a finished two-layer watchface as your answer.

**Evidence:** labeled layout showing both layer frames, build/run evidence, a test for text clipping and an explanation of which function owns each layer.

## 25C · Multi-mode design for physical buttons

[Local lesson and licensed Simplicity layout](../../lessons/25C/)

**Read first.** A multi-mode app needs **consistent affordances**: users should be able to predict what Up, Down, Select and Back do in each mode. Emery's round counterpart and touch-style patterns are not equivalent. Design explicitly for buttons and the 200 × 228 rectangle. Separate navigation (changing screens) from manipulation (changing a value inside a screen), and define what Back does from every state.

**Observe:** annotate one screen in the locally bundled layout: headline region, body region, status region and input behavior. Compare its hierarchy with your original concept from 22C and state diagram from 23C.

**Practice:** draw each state on identical-sized frames. Put the name of the state above each frame and button actions below. Add a transition arrow only when the destination is defined. Test these thought experiments: What happens at the first/last item? After reopening? With no saved data? If an action is unavailable? A mode should never leave the user with no discoverable way back.

**Evidence:** connected screen sketches, button-action legend, and a usability walkthrough for a typical task and an error/empty state.

### Design critique checklist

- Is the most important information visually dominant?
- Is text readable without clipping and with sufficient contrast?
- Are button meanings discoverable and consistent?
- Do sketches match the actual Emery shape and the source's layer capabilities?
- Can you explain **why** a design changed rather than merely stating what changed?

**Further reading:** [Pebble C SDK documentation](https://developer.repebble.com/docs/c/) for `TextLayer`, `Window`, `Layer` and button click configuration. The [course-wide index](../README.md) connects design to algorithms and implementation.
