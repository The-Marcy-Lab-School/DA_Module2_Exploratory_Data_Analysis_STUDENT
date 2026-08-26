# Checklist & Timeline — 5 Days

This project runs as **one sprint**, 5 days long. Every item below is
also the actual submission checklist — work through it in order, top to
bottom.

## What's a sprint, and why does this project run as one?

A sprint is a short, fixed block of time where a team commits to a
specific, achievable set of work, builds it, then **stops** — a real
deadline, not an open-ended "whenever it's done." You had one rep of this
in Module 1; here it is again, since sprint planning isn't a habit yet
after just one round:

- **The goal is fixed up front.** `MVP.md` *is* this sprint's plan — the
  bar doesn't move once you start.
- **Daily check-in.** At the start of each work session, ask yourself:
  what did I finish last time, what am I doing today, is anything
  blocking me? A real team does this out loud in ~10 minutes; here, it's
  worth 2 minutes of honest self-check.
- **The backlog is real work, deliberately not in this sprint.**
  `ABOVE_AND_BEYOND.md` **is** this sprint's backlog — genuinely good,
  legitimate work that doesn't fit in 5 days without cutting something
  that matters more. A backlog isn't "things you failed to finish" — it's
  how a team protects a real deadline by explicitly deciding what's *not*
  in scope, on purpose, instead of letting "just one more thing" quietly
  blow up the schedule. With only 5 days here, leaning on the backlog for
  anything past MVP matters even more than it did in Module 1.
- **A sprint ends with a real stopping point**, not a status update. Once
  `MVP.md` is done and pushed, the sprint is over — picking up a backlog
  item afterward, if you have real time, is a bonus, not part of this
  sprint.

## Day 1 — Setup, pick your domain, start inspecting

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
- [ ] Skim `MVP.md` (your sprint goal) and `ABOVE_AND_BEYOND.md` (your
  backlog) so you know the line between them before you start.
- [ ] Part 1 started: shape, dtypes, and missing-value counts genuinely
  inspected — you choose the methods.
- [ ] Commit your work — a real, descriptive message you write yourself.

## Day 2 — Part 2 & 3: clean it, then profile it

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
- [ ] Part 3: at least 3 numeric variables profiled — each with a
  five-number-summary-style computation and at least one chart
  (histogram, boxplot, or another type that fits).
  > ⚠️ Common mistake: describing a distribution as symmetric or normal
  > without looking at the chart — look at the shape first, then check
  > whether the summary numbers agree.
- [ ] Commit your work.

**Exit criterion:** at least 2 real commits pushed to GitHub by the end of
Day 2 — `git log --oneline` should already tell a real story.

## Day 3 — Part 4: relationships and segments

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
- [ ] Commit your work.

## Day 4 — Part 5, 6 & 7: two AI critiques, answer the problem, explain the spread

- [ ] A real chart generated from your own exploration and saved as an
  actual image file — confirmed it exists, not just that the cell ran.
- [ ] That image actually uploaded to an AI assistant, and its real,
  verbatim response pasted into the notebook, plus a real critique: does
  the AI's read match your own numbers?
  > ⚠️ Common mistake: paraphrasing or summarizing the AI's response
  > instead of pasting what it actually said — the critique needs the
  > real text to be checkable.
- [ ] **Part 5b:** the AI asked to generate/suggest its own visualization
  for one of your variables or relationships — what it actually produced
  pasted or described, and a real critique of whether it's the right
  chart type and whether it's accurate.
  > ⚠️ Common mistake: accepting an AI-suggested chart because it looks
  > polished, without checking whether it's actually the right chart type
  > for what you asked it to show.
- [ ] Part 6: a direct answer to your stakeholder's business problem,
  backed by the correct statistic, mentioning how your cleaning/
  imputation decisions affect your confidence in it.
- [ ] Part 7: the standard-deviation/volatility question answered in your
  own words, tied to your own computed number.
- [ ] Commit your work.

## Day 5 — The findings report, data-quality memo, final review

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
- [ ] **Delete `PROJECT_OVERVIEW.md` and `SCENARIOS.md`** — they explain
  the assignment, not your project; a real portfolio repo shouldn't have
  "here's what you were asked to build" sitting in it.
- [ ] `README.md` rewritten — replace the setup instructions entirely with
  your own project README: scenario, data overview, statistical summary,
  visualizations (real chart images, saved as files and embedded with
  markdown — not just described), and takeaways.
  > ⚠️ Common mistake: describing a chart in words instead of actually
  > saving it and embedding the real image — a reader should be able to
  > see what you saw, not just read your summary of it.
- [ ] Clean sweep: notebook runs top-to-bottom without errors, no leftover
  debugging cells or dead code.
- [ ] Full self-check against `MVP.md`.
- [ ] Final commit(s) pushed — `git log --oneline` should show 4+ commits
  total, each with a real message you wrote yourself. Repo confirmed
  public.

**Exit criterion:** everything in `MVP.md` is done and pushed. That's the
whole sprint. `ABOVE_AND_BEYOND.md` — your backlog — is exactly that:
optional, for real time left over, not a requirement of these 5 days.

## After Day 5: peer memo review

Once everyone's submitted, there's a separate session where your
`memo.md` gets shared **anonymously** with a small group of peers — they
review it as if they were your actual stakeholder and give real
feedback, and you'll do the same for a few of theirs (possibly spanning
different domains than yours). No prep needed beyond having a real,
finished `memo.md` — just know it's coming, and that a memo other people
can't actually act on is exactly the kind of thing this session surfaces
fast.

## Above & Beyond (Your Backlog)

Only the additional items — everything above still applies and isn't
repeated here. All four are detailed in `ABOVE_AND_BEYOND.md`. Picking one
up *after* Day 5, if you have real time, is a bonus sprint — not part of
this one.

- [ ] Find a **second** non-obvious pattern, from a different slice of the
  data than the one your business problem already led you to.
- [ ] Answer a **second** domain's business problem, briefly, using its
  own data file.
- [ ] Pick one memo question and actually try to answer it for real (a
  real search, not a guess) — write up what you found and whether it
  changed your confidence in your answer.
- [ ] Run the given-code `above_and_beyond/pandas_preview.py` and compare
  what it tells you to your own findings.
