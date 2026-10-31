# Local examples for all 21 Emery lessons

Every activity is now a **self-contained `lessons/<ID>/` directory**. For example, `lessons/7A/starter/` contains a full Pebble project with `package.json`, `wscript`, and `src/c/main.c`.

| Lesson | Activity | Complete included projects | Est. |
|---|---|---|---|
| [2A](2A/) | Explore Pebble examples | `clock`, `fonts`, `storage` |  |
| [7A](7A/) | Build and run a time-only C watchface | `starter` |  |
| [4A](4A/) | Annotate the time-only watchface code | `starter` |  |
| [5A](5A/) | Find and document a Pebble API function | `starter` |  |
| [3A](3A/) | Trace the watchface lifecycle | `starter` |  |
| [1A](1A/) | Change one visual property of a time-only watchface | `starter` |  |
| [6A](6A/) | Diagnose a simple compiler error | `starter` |  |
| [7B](7B/) | Create a Git-based modification workflow | `starter` |  |
| [5B](5B/) | Trace an existing feature through source code | `starter` |  |
| [1B](1B/) | Add and style a date TextLayer | `starter` |  |
| [3B](3B/) | Design a font-cycling algorithm | `starter` |  |
| [2B](2B/) | Write a two-example remix brief | `clock`, `storage` |  |
| [4B](4B/) | Modify the Font Browser | `starter` |  |
| [6B](6B/) | Diagnose a font-selection boundary bug | `starter` |  |
| [5C](5C/) | Research an unfamiliar Pebble capability | `starter` |  |
| [2C](2C/) | Develop an original Pebble app concept | `layout`, `fonts`, `storage` |  |
| [3C](3C/) | Design a state machine for an app | `starter` |  |
| [1C](1C/) | Design a multi-mode Pebble interface | `starter` |  |
| [4C](4C/) | Refactor font selection into a reusable component | `starter` |  |
| [7C](7C/) | Integrate font browsing with persistent selection | `fonts`, `storage` |  |
| [6C](6C/) | Diagnose a persistent-state integration bug | `starter` |  |

## Source provenance and compatibility

- Official SDK MIT sources are copied locally with their licenses: the Pebble watchface tutorial source (under time-only lesson `sdk-original/`), the exact **Simplicity** watchface source (lesson 1C and part of 2C), and the App Glance storage example (lesson 5C reference).
- Licensed SDK sources that include already-completed features are kept as **reference material**. The separate Emery-only `starter/` projects are intentionally minimal, so the exercise doesn't solve itself.
- The older official Font Browser and Persist Counter repositories do not provide a redistribution license. This course uses independently authored, self-contained Emery implementations of those APIs instead of copying unlicensed C code.
- Every executable starter restricts the SDK to `emery`. There is no dependence on downloading source examples from outside this repository. The emulator is `emery`.

## Build

```sh
cd lessons/7A/starter
pebble build
pebble install --emulator emery
```

The `6A` starter intentionally contains a compiler error. `6B` and `6C` contain intentional behavior bugs and include diagnostic logs but no answer key.
