# EDA Project: NASA Meteorite Landings

**New here?** Start with `PROJECT_OVERVIEW.md` for what you're building and
why. This file (`README.md`) is where the step-by-step setup lives — you're
already in the right place.

**Due:** 1 week. See `CHECKLIST_TIMELINE.md` for the day-by-day pace and
the full submission checklist.

This repo is a **GitHub template** — a starting point, not something you
edit directly on Marcy's copy of it.

## Getting started

**Step 1 — Get your own copy.** On this repo's GitHub page, click **"Use
this template" → "Create a new repository"** (not **Fork**) — this gives
you a clean copy with no "forked from" badge, the right choice for a
portfolio project. Fork keeps a network link back to this template, meant
for contributing back upstream, not for an independent assignment.

**Step 2 — Install what you need.**
- Python 3, if you don't already have it.
- The [Jupyter extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter), if you don't already have it — this is how you'll open and run `starter/analysis.ipynb`.
- This project's Python packages:
  ```bash
  pip install -r requirements.txt
  ```

**Step 3 — Clone your copy locally** and open it in VS Code:
```bash
git clone <your-new-repo-url>
```

**Step 4 — Confirm your environment is already set up.** This module
doesn't test git/environment setup, so `.gitignore` and `LICENSE` are
already in this repo, with real git history already in place — nothing to
build yourself here. **Do open `LICENSE`, though**, and replace the
`[YOUR NAME]` placeholder with your actual name, then commit that change —
easy to miss precisely because the file already exists and nothing else
prompts you to open it.

## The dataset

`data/meteorite_landings.csv` — 45,716 real NASA-recorded meteorite
landings. Public domain (U.S. government work) — see `data/SOURCE.md` for
the full license note, column descriptions, and known data-quality
wrinkles in the raw file. You haven't seen this dataset before; that's
deliberate.

## What to do

Open `starter/analysis.ipynb` in VS Code and work through it top to
bottom — every code cell either runs as-is or has a small `# TODO` blank;
the markdown cells below each one are where you write the real analysis.
When the notebook's done, write `starter/memo.md`. See `MVP.md` for the
full scope and `CHECKLIST_TIMELINE.md` for the day-by-day pace. Commit
incrementally as you go — a `git commit` after Part 1's profiling is done,
another after Part 3's pattern-mining, not one commit at the very end.
