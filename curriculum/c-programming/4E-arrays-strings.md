# 4E — Arrays, Strings, and Bounds

> **Scope and provenance:** Original course learning notes, organized around themes from Mike Jipping's *Learning C with Pebble*, Chapters 7 (Arrays) and 9 (Strings). These are **not verbatim extracts** from the book. Source-derived material from Chapters 3–6 remains in modules 4A–4D.
>
> **Target:** Pebble Time 2 (Emery), SDK 4.33.1, C. Required local starter: [lessons/4E/starter/](../../lessons/4E/starter/).
>
> **Objective:** Use arrays and bounded C strings to represent multiple values without overrunning buffers.

## Values, collections and bounds

Chapters 7 and 9 of *Learning C with Pebble* introduce arrays and C strings. An array is a fixed-size sequence of elements of a single type. Use a loop to process a collection, not a cascade of repeated `if` statements. An index starts at zero. For an array of `N` items, valid indices are 0 through `N-1`; accessing `N` is **out of bounds** and invokes undefined behavior.

```c
int readings[4] = {12, 15, 9, 20};
for (size_t i = 0; i < 4; ++i) {
  APP_LOG(APP_LOG_LEVEL_DEBUG, "reading %u is %d", (unsigned)i, readings[i]);
}
```

A C string is a sequence of `char` values terminated with the zero byte `'\0'`. Its buffer must hold that terminator *in addition to* visible characters. String literals can be used through `const char *` when you are not modifying them. Use `snprintf(buffer, sizeof(buffer), ...)` to format text with a size limit.

## Arrays on a Pebble

An array of label strings is particularly practical for a button-controlled app: the current index selects a display name. A small lookup table also replaces long, brittle chains of conditions. Arrays do **not** carry their own length into a function accepting a pointer: pass the length explicitly. Never use `sizeof(pointer)` to infer an array's element count.

Important: `text_layer_set_text(layer, buffer)` uses the text stored at the provided address; the buffer must remain valid as long as the layer uses it. A `static char[]` or other app-owned storage is appropriate for dynamic text. A local stack buffer that goes out of scope is not.

## Practice checkpoints

Explain why `char label[4] = "ABC"` fits but `char label[3] = "ABC"` does not provide space for the terminator. Given a selector of four items, write the correct wraparound expression for moving forward and backward. Test both edges and demonstrate no out-of-range access. Keep the code clear and bounded.


## Assigned project

[Open the complete Emery project for 4E](../../lessons/4E/). Expand the list to six messages; write a function returning the index of a requested item; ensure boundaries wrap; use snprintf to construct a safe label. Test the first/last index and an overlong string.

**Success evidence:** The modified project builds, its specified behavior is demonstrated, the learner explains the C constructs used, and edge cases are tested.

## Further reading

- Mike Jipping, *Learning C with Pebble*, Chapters 7 (Arrays) and 9 (Strings) (2016).
- [Pebble C SDK API documentation](https://developer.repebble.com/docs/c/)
- [Complete local example projects](../../lessons/README.md)
