# EDA Project: Choose Your Domain

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
- `pandas`, `matplotlib`, and whichever visualization library you decide
  to use (seaborn and/or plotly are both reasonable choices, or stick
  with matplotlib/pandas' own `.plot()`) — `pip install` each as you need
  it. **`requirements.txt` is yours to write, not given** — see that
  file's own instructions; fill in the real packages/versions you end up
  using before your final commit, not before you've started.
- An AI assistant that accepts **image uploads** (the same Claude/ChatGPT-
  style tool you already use — confirm it can take an image before Part 5
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

## Choose your domain

Read `SCENARIOS.md` and pick **one** of 4 business domains (finance &
insurance, healthcare operations, public sector, or professional
services) — each has a real stakeholder, a real business problem, and its
own data file (three are real government data; one is clearly-labeled
synthetic — see `data/SOURCE.md`). Everyone works from the same starter
notebook and the same bar (`MVP.md`); the domain changes what you're
looking at, not what's required.

## What to do

Open `starter/analysis.ipynb` in VS Code and work through it top to
bottom. **Almost no code is given** — this notebook gives you structure
and asks questions; deciding which pandas method, which chart type, and
which visualization tool (matplotlib, seaborn, plotly, or pandas' own
`.plot()`) actually fits each question is part of the assignment. Real
data cleaning and a real imputation decision are required, and at least
one repeated operation needs to become a real function, not copy-pasted
code. When the notebook's done, write `starter/memo.md`. See `MVP.md` for
the full scope and `CHECKLIST_TIMELINE.md` for the day-by-day pace. Commit
incrementally as you go — a `git commit` after Part 2's cleaning is done,
another after Part 4's charts, not one commit at the very end.
