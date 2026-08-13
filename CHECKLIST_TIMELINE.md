# Checklist & Timeline — 1 Week

Same sprint rhythm as Module 1: a fixed block of time, a clear goal
(`MVP.md`), and a real stopping point — not an open-ended "whenever it's
done." Every item below is also the actual submission checklist — work
through it in order, top to bottom.

## Day 1 — Setup, and profile the first two variables

- [ ] Repo created from the template via **"Use this template"** (not
  Fork), cloned locally — see `README.md`.
- [ ] `requirements.txt` installed; `.gitignore`/`LICENSE`/git history
  confirmed already present; `LICENSE`'s `[YOUR NAME]` placeholder replaced
  with your actual name, committed.
- [ ] `data/SOURCE.md` read before opening the notebook — know what this
  dataset is and what's already known to be messy about it.
- [ ] `starter/analysis.ipynb` opened in VS Code; the setup cell and the
  `mass (g)` worked example run, and its given interpretation actually
  read (it's the model for what you write yourself next).
- [ ] `year` profiled: run `profile_variable(df, "year")`, then write the
  shape/outlier description yourself.
  > ⚠️ Common mistake: describing a distribution as symmetric or normal
  > without looking at the histogram — glance at the shape first, then
  > check whether the five-number summary agrees.

## Day 2 — The third variable, and the AI-mistake exercise

- [ ] `reclat` profiled the same way. Pay attention to anything stacking up
  right at 0 before you write your answer.
  > ⚠️ Common mistake: labeling every extreme value an "outlier" without
  > asking whether it's a real value or something else entirely (like a
  > missing-value placeholder).
- [ ] Part 2 done: read the given AI interpretation of `mass (g)`, and
  write a specific, correct explanation of what it gets wrong — cite your
  own five-number summary/histogram from Part 1, don't just assert it's
  wrong.
- [ ] Commit: `git commit -m "profile all 3 variables, catch the AI's mistake"`.

## Day 3 — Mine for a pattern, then explain why spread matters

- [ ] Part 3's three given grouped views run and actually looked at side
  by side — `fall`, `recclass`, and decade.
- [ ] **One non-obvious pattern or segment** identified and written up,
  with the mean-or-median choice justified by that variable's actual skew
  (not a reflexive mean).
  > ⚠️ Common mistake: using the mean by default on a visibly skewed
  > variable without acknowledging the mismatch.
  > ⚠️ Common mistake: treating a pattern found in a very small slice of
  > the data as a reliable finding — check how many rows are actually
  > behind it.
- [ ] Part 4's standard-deviation question answered in your own words,
  tied to the real number from `mass (g)`'s five-number summary.
- [ ] Commit: `git commit -m "mine for a pattern, explain std/volatility"`.

## Day 4 — The data-quality memo

- [ ] `starter/memo.md` written: **at least 2 specific, checkable
  questions** about this dataset's origin, completeness, or bias.
  > ⚠️ Common mistake: writing a question too generic to actually be
  > checkable, like "is this data accurate?" — a real data steward should
  > be able to answer your question with a specific fact.
- [ ] The "why this matters" paragraph connects at least one of those
  questions back to whether you'd trust your Part 3 pattern.
- [ ] Clean sweep: notebook runs top-to-bottom without errors, no leftover
  debugging cells or dead code.
- [ ] Commit: `git commit -m "add data-quality memo"`.

**Exit criterion:** everything in `MVP.md` is done and pushed. That's the
whole submission. `ABOVE_AND_BEYOND.md` is exactly that — optional, for
real time left over, not a requirement of this week.

## Above & Beyond

Only the additional items — everything above still applies and isn't
repeated here. All four are detailed in `ABOVE_AND_BEYOND.md`.

- [ ] Find a **second** non-obvious pattern, from a different slice than
  the one you already wrote up.
- [ ] Profile `reclong` yourself — the fourth numeric variable, not
  required for MVP.
- [ ] Quantify your Part 3 finding both ways — compute it with the mean
  *and* the median, and show how different the conclusion would look using
  the "wrong" one.
- [ ] Pick one question from your memo and actually try to answer it for
  real (a real search, not a guess) — write up what you found and whether
  it changed your confidence in your Part 3 pattern.
