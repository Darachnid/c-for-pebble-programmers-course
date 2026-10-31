# How to contribute — even if you have never used Git

Contributions are welcome: typographical fixes, accessibility improvements, confusing instructions, missing explanations, and tested Emery examples. You **do not** need to know how to program to propose a documentation fix.

## Vocabulary in plain English

- **Repository (repo)** = a project folder with a recorded history, hosted on GitHub.
- **Fork** = your personal copy on GitHub, separate from the original.
- **Clone** = download a working copy from GitHub to your computer.
- **Branch** = a separate line of work, so `main` stays safe until a change is reviewed.
- **Commit** = save a named snapshot in Git.
- **Push** = upload your local commits to GitHub.
- **Pull request (PR)** = ask maintainers to review your branch and merge it into the original.

## Option A — easiest: make a documentation change entirely on GitHub

1. Sign in to [GitHub](https://github.com), open [this repository](https://github.com/Darachnid/c-for-pebble-programmers-course), and skim the [syllabus](SYLLABUS.md) and [lesson directory](lessons/README.md).
2. Check [Issues](https://github.com/Darachnid/c-for-pebble-programmers-course/issues) and [Pull requests](https://github.com/Darachnid/c-for-pebble-programmers-course/pulls) for a duplicate. For substantial changes, open an Issue explaining your proposal first. A small typo does not need an Issue.
3. Click **Fork → Create fork** on the original repository. You now have a personal GitHub copy.
4. In **your fork**, navigate to the Markdown file you want to change and click the pencil icon (**Edit this file**). Make one focused correction. Use **Preview** to check Markdown links, tables and formatting.
5. Click **Commit changes**. Write a concrete summary like `Clarify date-layer acceptance test in 13B`. When offered, choose **Create a new branch for this commit**; name it something like `docs/clarify-1b`.
6. In your fork, click **Contribute → Open pull request** (or **Compare & pull request**). If no prompt is shown, visit the original repo's **Pull requests → New pull request → compare across forks**. Confirm **base** = `Darachnid/c-for-pebble-programmers-course` / `main` and **compare/head** = your fork / your change branch.
7. Enter what changed and how you checked it, then click **Create pull request**. The change is *proposed*, not yet merged. Watch for review comments. Additional edits committed to the **same branch** update the PR automatically.

## Option B — code or multiple files with Git in a terminal

Install [Git](https://git-scm.com/downloads), a text editor and (for C changes) the [Pebble SDK](https://developer.repebble.com/). Fork the repository in your browser first. Replace `YOUR-USERNAME` with your own GitHub username.

```sh
# Set the author shown on commits (once per computer):
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Download your fork; then enter that folder:
git clone https://github.com/YOUR-USERNAME/c-for-pebble-programmers-course.git
cd c-for-pebble-programmers-course

# Keep a reference to the original repository:
git remote add upstream https://github.com/Darachnid/c-for-pebble-programmers-course.git

# Start a new branch from the original's current main:
git fetch upstream
git switch -c docs/clarify-1b upstream/main
```

Edit only your chosen file(s). For a C example, work inside that lesson's **complete local project**, never an external example. Build and test with the Emery emulator:

```sh
cd lessons/13B/starter
pebble build
pebble install --emulator emery
pebble logs --emulator emery
cd ../../..
```

Review and publish your work:

```sh
git status                         # Show changed files and current branch.
git diff                           # Read the exact changes.
git add lessons/13B/README.md       # Example: stage only this intended file.
git commit -m "Clarify the 13B date-layer test"
git push -u origin docs/clarify-1b # Upload to your fork, NOT original main.
```

Then open a PR as in Option A. `git commit` does **not** send anything to GitHub; `git push` does. For a new independent change, create another branch from fresh `upstream/main`. If GitHub asks you to authenticate, follow its current browser or token sign-in prompts; do not put a password into the repository.

## Course-specific submission checklist

- Identify the affected lesson ID(s). Preserve the 40-activity syllabus, actual prerequisites, and correct local example paths; include source/build files for any new example.
- Keep runtime examples **Emery-only**: `targetPlatforms: ["emery"]` and SDK 4.33.1. Report build, install, runtime and boundary-case results; if you did not run them, say **not tested**.
- Do **not** spoil the intentionally flawed debugging exercises 6A, 21B, 32C, 27C/debug, 35I/debug or 38L/debug by publishing fixes as starter code. The no-AI-solutions policy applies to doing coursework; contribution authors remain responsible for testing and fact-checking their changes.
- Avoid checking in generated `build/` folders, passwords, private files, Taskwarrior data, or unrelated edits. `git add .` can collect more than you intend; inspect `git status` first. Do not use `git reset --hard` or force-push when uncertain.
- Respect copyright: preserve MIT notices in bundled Pebble samples; identify the provenance and license of new text/code/artwork; do not add copied textbook material without permission.
- A useful PR explains **what problem, what changed, how tested, and what remains unverified**. Screenshots or short logs can help. Never claim compilation has passed without running the SDK.

Questions are welcome as GitHub [Issues](https://github.com/Darachnid/c-for-pebble-programmers-course/issues). The purpose of review is to improve the material, not to test your Git vocabulary.
