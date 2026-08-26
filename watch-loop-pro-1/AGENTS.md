# AGENTS.md

## What this repo is
Single-script test fixture for agent watch-loop behavior. No build, lint, test, or dependency config; Python stdlib only.

## How it works
- `python long_task.py` prints "Starting long task...", sleeps **120 seconds**, then writes `task-completed.txt` in the repo root. It blocks the whole time — run it in the background if you need to do anything else meanwhile.
- The completion signal file is **`task-completed.txt`** (with "-ed"). Prompts or instructions saying `task-complete.txt` are wrong; trust the filename in `long_task.py`.

## Watch-loop rules
- Poll every 10 seconds for existence of `task-completed.txt`; report completion once, then stop.
- Do not modify `long_task.py` while it is running.

## Gotchas
- `task-completed.txt` is a **generated artifact** left over from prior runs. Before starting a fresh run/watch, delete it, or the watcher will see instant "completion" from the old file.
- Git repo has no commits yet (`master`, everything untracked).
