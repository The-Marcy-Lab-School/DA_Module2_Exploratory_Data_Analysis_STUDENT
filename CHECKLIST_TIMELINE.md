# Checklist & Timeline — 2 Weeks

Same sprint rhythm as Module 1: a fixed block of time, a clear goal
(`MVP.md`), and a real stopping point. Every item below is also the actual
submission checklist — work through it in order, top to bottom.

## Day 1 — Setup, pick your domain

- [ ] Repo created from the template via **"Use this template"** (not
  Fork), cloned locally — see `README.md`.
- [ ] Packages installed as you need them (`pandas`, `matplotlib`, your
  chosen viz library); `.gitignore`/`LICENSE`/git history confirmed
  already present; `LICENSE`'s `[YOUR NAME]` placeholder replaced with
  your actual name, committed.
- [ ] An AI assistant that accepts image uploads confirmed working —
  you'll need it in Part 5, don't discover it's missing then.
- [ ] All 4 domains in `SCENARIOS.md` read; one picked. `data/SOURCE.md`'s
  entry for your file read before opening the notebook.
- [ ] The "Your Scenario" section at the top of `starter/analysis.ipynb`
  filled in (the "Data Overview" paragraph can wait until after Part 1).
- [ ] Skim `MVP.md` (your goal) and `ABOVE_AND_BEYOND.md` so you know the
  line between them before you start.

## Day 2-3 — Part 1 & 2: inspect, then clean

- [ ] `starter/analysis.ipynb`'s setup cell filled in with your chosen
  file, and run.
- [ ] Part 1: shape, dtypes, and missing-value counts genuinely
  inspected — you choose the methods.
- [ ] Part 2: **at least one real cleaning function written and used** —
  not inline code copy-pasted for each fix.
  > ⚠️ Common mistake: writing the same cleaning logic 2-3 times inline
  > instead of once as a function — if you're copy-pasting a fix, it
  > should be a function.
- [ ] An imputation decision made and justified in writing for at least
  one column with real missing values.
  > ⚠️ Common mistake: dropping every row with any missing value by
  > default, without asking whether that's actually the right call for
  > *this* column.
- [ ] Commit: `git commit -m "inspect and clean [domain] data"`.

## Day 4-5 — Part 3: profile your key variables

- [ ] At least 3 numeric variables profiled — each with a five-number-
  summary-style computation and at least one chart (histogram, boxplot,
  or another type that fits).
  > ⚠️ Common mistake: describing a distribution as symmetric or normal
  > without looking at the chart — look at the shape first, then check
  > whether the summary numbers agree.
- [ ] Shape and outlier calls written for each of the 3, in your own
  words.
- [ ] Commit: `git commit -m "profile 3 key variables"`.

## Day 6-7 — Part 4: relationships and segments

- [ ] A relationship or segment explored with a chart type that actually
  fits (bar/boxplot-by-category, line graph for a trend, scatterplot for
  two numeric variables) — and the choice justified in a sentence.
  > ⚠️ Common mistake: using a histogram or bar chart out of habit when
  > the actual question is about a trend over time or a relationship
  > between two variables.
- [ ] One non-obvious finding stated, backed by the statistic (mean or
  median) that fits your variable's actual skew.
  > ⚠️ Common mistake: using the mean by default on a visibly skewed
  > variable without acknowledging the mismatch.
  > ⚠️ Common mistake: treating a pattern found in a very small slice of
  > the data as a reliable finding — check how many rows are behind it.
- [ ] Commit: `git commit -m "explore relationships, find a pattern"`.

**Exit criterion:** at least 3 real commits pushed to GitHub by end of
Week 1 — `git log --oneline` should already tell a real story.

## Day 8 — Part 5: two real AI critiques

- [ ] A real chart generated from your own exploration and saved as an
  actual image file — confirmed it exists, not just that the cell ran.
- [ ] That image actually uploaded to an AI assistant, and its real,
  verbatim response pasted into the notebook.
  > ⚠️ Common mistake: paraphrasing or summarizing the AI's response
  > instead of pasting what it actually said — the critique needs the
  > real text to be checkable.
- [ ] A real critique written: does the AI's read match your own numbers?
- [ ] **Part 5b:** the AI asked to generate/suggest its own visualization
  for one of your variables or relationships — what it actually produced
  pasted or described, and a real critique of whether it's the right
  chart type and whether it's accurate.
  > ⚠️ Common mistake: accepting an AI-suggested chart because it looks
  > polished, without checking whether it's actually the right chart type
  > for what you asked it to show.

## Day 9 — Part 6 & 7: answer the business problem, explain the spread

- [ ] Part 6: a direct answer to your stakeholder's business problem,
  backed by the correct statistic, mentioning how your cleaning/
  imputation decisions affect your confidence in it.
- [ ] Part 7: the standard-deviation/volatility question answered in your
  own words, tied to your own computed number.
- [ ] Commit: `git commit -m "AI-vision exercise, answer business problem"`.

## Day 10 — The findings report, data-quality memo, final review

- [ ] `starter/memo.md` written: your domain/stakeholder named, your
  answer restated for a non-technical reader, **at least 2 specific,
  checkable questions** about this dataset's origin, completeness, or
  bias.
  > ⚠️ Common mistake: writing a question too generic to actually be
  > checkable, like "is this data accurate?" — a real data steward should
  > be able to answer your question with a specific fact.
- [ ] The "why this matters" paragraph connects at least one of those
  questions back to whether your stakeholder should trust your answer.
- [ ] Your own `requirements.txt` written — real packages you actually
  used, with real, exact version numbers, replacing the placeholder
  instructions the template shipped with.
- [ ] The "Questions My Analysis Can Answer" section **deleted** from the
  notebook — check it against your own Parts 1-7 first, then remove it.
- [ ] Clean sweep: notebook runs top-to-bottom without errors, no leftover
  debugging cells or dead code.
- [ ] Full self-check against `MVP.md`.
- [ ] Final commit(s) pushed — `git log --oneline` should show 4+ commits
  total, each with a real message. Repo confirmed public.

**Exit criterion:** everything in `MVP.md` is done and pushed. That's the
whole submission. `ABOVE_AND_BEYOND.md` is exactly that — optional, for
real time left over, not a requirement of these 2 weeks.

## Above & Beyond

Only the additional items — everything above still applies and isn't
repeated here. All four are detailed in `ABOVE_AND_BEYOND.md`.

- [ ] Find a **second** non-obvious pattern, from a different slice of the
  data than the one your business problem already led you to.
- [ ] Answer a **second** domain's business problem, briefly, using its
  own data file.
- [ ] Pick one memo question and actually try to answer it for real (a
  real search, not a guess) — write up what you found and whether it
  changed your confidence in your answer.
- [ ] Run the given-code `above_and_beyond/pandas_preview.py` and compare
  what it tells you to your own findings.
