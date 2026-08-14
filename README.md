# EDA Project: NASA Meteorite Landings

**New here?** Start with `PROJECT_OVERVIEW.md` for what you're building and
why. This file (`README.md`) is where the step-by-step setup lives — you're
already in the right place.

**Due:** 2 weeks. See `CHECKLIST_TIMELINE.md` for the day-by-day pace and
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
- This project's Python packages, **including Polars — new this module**:
  ```bash
  pip install -r requirements.txt
  ```
- An AI assistant that accepts **image uploads** (the same Claude/ChatGPT-
  style tool you already use — confirm it can take an image before Part 3
  of the notebook, not the night this is due).

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

**First, read `SCENARIOS.md` and pick one of the 4 stakeholders** — your
whole notebook builds toward answering their specific question, not just
profiling the dataset in general. Then open `starter/analysis.ipynb` in VS
Code and work through it top to bottom: real pandas code (Part 1), the
same core analysis redone in Polars plus a real tradeoffs reflection (Part
2), a chart you generate yourself and get an AI's read on (Part 3), your
direct answer to your stakeholder's question (Part 4), and a standard-
deviation/volatility question (Part 5). Most of the code is yours to write
this time — a worked example models each new technique, but you're not
just filling in blanks anymore. When the notebook's done, write
`starter/memo.md`. See `MVP.md` for the full scope and
`CHECKLIST_TIMELINE.md` for the day-by-day pace. Commit incrementally as
you go — a `git commit` after Part 1's pandas work, another after Part 2's
Polars work, not one commit at the very end.
