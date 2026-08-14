# Checklist & Timeline — 2 Weeks

Same sprint rhythm as Module 1: a fixed block of time, a clear goal
(`MVP.md`), and a real stopping point. Every item below is also the actual
submission checklist — work through it in order, top to bottom.

## Day 1 — Setup, pick your stakeholder

- [ ] Repo created from the template via **"Use this template"** (not
  Fork), cloned locally — see `README.md`.
- [ ] `requirements.txt` installed **(this now includes Polars — new this
  module)**; `.gitignore`/`LICENSE`/git history confirmed already present;
  `LICENSE`'s `[YOUR NAME]` placeholder replaced with your actual name,
  committed.
- [ ] An AI assistant that accepts image uploads confirmed working —
  you'll need it in Week 2, don't discover it's missing then.
- [ ] `data/SOURCE.md` read before opening the notebook — know what this
  dataset is and what's already known to be messy about it.
- [ ] All 4 scenarios in `SCENARIOS.md` read; one picked. Restate your
  stakeholder's actual question in your own words before moving on.
- [ ] Skim `MVP.md` (your goal) and `ABOVE_AND_BEYOND.md` so you know the
  line between them before you start.

## Day 2-3 — Part 1: pandas exploration

- [ ] `starter/analysis.ipynb` opened; the setup cell and the `mass (g)`
  worked example run, and its given interpretation actually read (it's the
  model for what you write yourself next).
- [ ] Real pandas code written to explore the variable(s) your
  stakeholder's question actually needs — at least one grouped summary,
  at least one sort or filter. Expect more than one attempt before you
  find something worth reporting.
  > ⚠️ Common mistake: describing a distribution as symmetric or normal
  > without looking at the histogram — glance at the shape first, then
  > check whether the five-number summary agrees.
- [ ] What you found written up in your own words, tied to real numbers.
- [ ] Commit: `git commit -m "pandas exploration for [stakeholder]'s question"`.

## Day 4-5 — Part 2: the same analysis in Polars, and the real tradeoffs

- [ ] The Polars worked example run and read.
- [ ] Your Part 1 core analysis redone in Polars — same question, new
  syntax.
- [ ] The timing-comparison cell run **twice in a row**, not just once —
  watch what happens to Polars' number the second time.
  > ⚠️ Common mistake: reporting a single timing run as "the" answer —
  > run it more than once before drawing a conclusion, same discipline as
  > not trusting a single data point anywhere else in this project.
- [ ] All 4 tradeoffs-reflection questions answered for real, tied to your
  own numbers and your own syntax friction — not a generic "Polars is
  faster" restatement from outside reading.
- [ ] Commit: `git commit -m "redo analysis in Polars, tradeoffs reflection"`.

**Exit criterion:** at least 2 real commits pushed to GitHub by end of
Week 1 — `git log --oneline` should already tell a real story.

## Day 6 — Part 3: generate a chart, get an AI's read on it

- [ ] A real chart generated from your own exploration and saved as an
  actual image file (`my_chart.png` or similar) — confirmed it exists,
  not just that the cell ran.
- [ ] That image actually uploaded to an AI assistant, and its real,
  verbatim response pasted into the notebook.
  > ⚠️ Common mistake: paraphrasing or summarizing the AI's response
  > instead of pasting what it actually said — the critique needs the real
  > text to be checkable.
- [ ] A real critique written: does the AI's read match your own
  five-number summary? Where does it agree or fall short?

## Day 7 — Part 4 & 5: answer the question, explain the spread

- [ ] Part 4: a direct answer to your stakeholder's question, backed by
  the correct statistic (mean or median) for your variable's actual skew.
- [ ] Part 5: the standard-deviation/volatility question answered in your
  own words, tied to the real number from `mass (g)`'s five-number
  summary.
- [ ] Commit: `git commit -m "AI-vision exercise, answer stakeholder question"`.

## Day 8 — The findings report & data-quality memo

- [ ] `starter/memo.md` written: your stakeholder named, your answer to
  their question restated for a non-technical reader, **at least 2
  specific, checkable questions** about this dataset's origin,
  completeness, or bias.
  > ⚠️ Common mistake: writing a question too generic to actually be
  > checkable, like "is this data accurate?" — a real data steward should
  > be able to answer your question with a specific fact.
- [ ] The "why this matters" paragraph connects at least one of those
  questions back to whether your stakeholder should trust your answer.
- [ ] Clean sweep: notebook runs top-to-bottom without errors, no leftover
  debugging cells or dead code.

## Day 9 — Final review

- [ ] Full self-check against `MVP.md`, top to bottom.
- [ ] Final commit(s) pushed — `git log --oneline` should show 4+ commits
  total, each with a real message.
- [ ] Repo confirmed public.

**Exit criterion:** everything in `MVP.md` is done and pushed. That's the
whole submission. `ABOVE_AND_BEYOND.md` is exactly that — optional, for
real time left over, not a requirement of these 2 weeks.

## Above & Beyond

Only the additional items — everything above still applies and isn't
repeated here. All five are detailed in `ABOVE_AND_BEYOND.md`.

- [ ] Find a **second** non-obvious pattern, from a different slice of the
  data than the one your stakeholder's question already led you to.
- [ ] Scale the dataset up (concatenate it with itself many times over)
  and re-run the timing comparison — does the winner change at real scale?
- [ ] Answer a **second** stakeholder's question from `SCENARIOS.md`,
  briefly, using what you already built.
- [ ] Pick one memo question and actually try to answer it for real (a
  real search, not a guess) — write up what you found and whether it
  changed your confidence in your answer.
- [ ] Run the given-code `above_and_beyond/pandas_preview.py` and compare
  what it tells you to your own findings.
