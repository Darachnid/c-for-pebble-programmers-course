# 4F — Pointers, Indirection, and Memory Lifetime

> **Scope and provenance:** Original course learning notes, organized around themes from Mike Jipping's *Learning C with Pebble*, Chapters 8 (Pointers and Memory Allocation) and 11 (How C Programs Execute). These are **not verbatim extracts** from the book. Source-derived material from Chapters 3–6 remains in modules 4A–4D.
>
> **Target:** Pebble Time 2 (Emery), SDK 4.33.1, C. Required local starter: [lessons/4F/starter/](../../lessons/4F/starter/).
>
> **Objective:** Use addresses and pointer parameters safely and understand ownership of Pebble UI resources.

## Indirection, addresses, and lifetime

Chapter 8 introduces pointers and Chapter 11 describes how a compiled C program executes. A pointer stores an address. The unary `&` operator takes an object's address and `*` dereferences a pointer to access the pointed-to object. Passing a pointer to a helper allows the helper to update a caller-owned value.

```c
static void step(int *position, int delta) {
  if (position != NULL) {
    *position += delta;
  }
}
int x = 10;
step(&x, 2);  // x becomes 12
```

Pointers are not automatically safe. Never dereference `NULL`, a pointer to released memory, or a pointer outside an allocated array. Pointer arithmetic moves in units of the pointed-to type. Although array expressions often decay to pointers, arrays and pointers are not identical objects and have different `sizeof` behavior.

## Memory ownership on Pebble

For every call that creates a Pebble UI object, identify the matching destroy call. `Window *` from `window_create()` must be destroyed with `window_destroy()`; a `TextLayer *` created with `text_layer_create()` requires `text_layer_destroy()`. Destroy child layers during window unload; destroy the window at shutdown. Prefer static application state for small embedded apps when ownership is straightforward, but do not assume static storage makes a pointer safe.

Local variables usually live for the duration of their scope; static objects live for the duration of the app. If you allocate with `malloc()`, pair it with `free()` and handle allocation failure. You do not need dynamic allocation for every small collection.

## Practice checkpoints

Trace which values change after calling a pointer-based function. Explain why returning a pointer to a local stack buffer is unsafe. Inspect your starter's create/destroy pairs and show how the buffer used by its TextLayer stays alive. Make a pointer helper robust to invalid input.


## Assigned project

[Open the complete Emery project for 4F](../../lessons/4F/). Rewrite the coordinate update using an output pointer, add a second pointer-based helper, and document what memory each pointer points to and who owns the TextLayer. Deliberately test NULL using a helper, then restore safe code.

**Success evidence:** The modified project builds, its specified behavior is demonstrated, the learner explains the C constructs used, and edge cases are tested.

## Further reading

- Mike Jipping, *Learning C with Pebble*, Chapters 8 (Pointers and Memory Allocation) and 11 (How C Programs Execute) (2016).
- [Pebble C SDK API documentation](https://developer.repebble.com/docs/c/)
- [Complete local example projects](../../lessons/README.md)
