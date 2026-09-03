# Checklist & Timeline — 4 Days + Share-Out

This project runs as **one sprint**, 4 build days plus a share-out day.
Every item below is also the actual submission checklist — work through
it in order, top to bottom.

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
  legitimate work that doesn't fit in 4 days without cutting something
  that matters more. A backlog isn't "things you failed to finish" — it's
  how a team protects a real deadline by explicitly deciding what's *not*
  in scope, on purpose, instead of letting "just one more thing" quietly
  blow up the schedule. With only 4 days here, leaning on the backlog for
  anything past MVP matters even more than it did in Module 1.
- **A sprint ends with a real stopping point**, not a status update. Once
  `MVP.md` is done and pushed, the sprint is over — picking up a backlog
  item afterward, if you have real time, is a bonus, not part of this
  sprint.

## Day 1 — Setup, pick your domain, inspect, clean, profile

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
- [ ] Part 1: shape, dtypes, and missing-value counts genuinely inspected
  — you choose the methods.
- [ ] Commit your work — a real, descriptive message you write yourself.
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
Day 1 — `git log --oneline` should already tell a real story.

## Day 2 — Part 4: relationships and segments

- [ ] A relationship or segment explored with a chart type that actually
  fits (bar/boxplot-by-category, line graph for a trend, scatterplot for
  two numeric variables) — and the choice justified in a sentence.
  > ⚠️ Common mistake: using a histogram or bar chart out of habit when
  > the actual question is about a trend over time or a relationship
  > between two variables.
- [ ] **At least 2 distinct chart types used across Part 3 + Part 4
  combined** — not the same chart type for every variable/relationship
  regardless of what it's actually showing.
  > ⚠️ Common mistake: defaulting to a histogram (or whichever chart type
  > you're most comfortable with) for everything, instead of letting the
  > question decide the chart.
- [ ] A groupby table of your key statistic (mean or median, whichever
  fits) by group, with each group's number **explicitly compared against
  the overall aggregate value of that same statistic** — does every group
  point the same direction as the aggregate, or does at least one group's
  own trend actually diverge from it?
  > ⚠️ Common mistake: reporting only the aggregate number, or only the
  > single most extreme group, without checking whether the *other*
  > groups actually agree with the aggregate too.
- [ ] One non-obvious finding stated, backed by the statistic (mean or
  median) that fits your variable's actual skew.
  > ⚠️ Common mistake: using the mean by default on a visibly skewed
  > variable without acknowledging the mismatch.
  > ⚠️ Common mistake: treating a pattern found in a very small slice of
  > the data as a reliable finding — check how many rows are behind it.
- [ ] Commit your work.

## Day 3 — Part 5, 6 & 7: two AI critiques, answer the problem, explain the spread

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

## Day 4 — The findings report, data-quality memo, final review

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
- [ ] **Replace `README.md`'s content with your own real project README**
  — write it for someone who's never seen this assignment, replacing the
  setup instructions entirely:
  - **Scenario** — your domain/stakeholder and their business problem, in
    your own words.
  - **Data Overview** — what the dataset is, its source, roughly how big
    it is.
  - **Statistical Summary** — your key variables' real numbers (mean/
    median/spread), correctly labeled.
  - **Visualizations** — real, embedded chart images (saved as files,
    referenced with markdown) — not descriptions.
  - **Takeaways** — your answer to the business problem and what you'd
    flag before anyone trusts it.
  > ⚠️ Common mistake: describing a chart in words instead of actually
  > saving it and embedding the real image — a reader should be able to
  > see what you saw, not just read your summary of it.
- [ ] Clean sweep: notebook runs top-to-bottom without errors, no leftover
  debugging cells or dead code.
- [ ] Full self-check against `MVP.md`.
- [ ] **Delete `PROJECT_OVERVIEW.md`, `SCENARIOS.md`, and this file
  (`CHECKLIST_TIMELINE.md`)** — now that their content is captured in your
  real README, they're just "here's what you were asked to build" clutter
  that shouldn't sit in a real portfolio repo.
- [ ] Final commit(s) pushed — `git log --oneline` should show 4+ commits
  total, each with a real message you wrote yourself. Repo confirmed
  public.

**Exit criterion:** everything in `MVP.md` is done and pushed. That's the
whole sprint. `ABOVE_AND_BEYOND.md` — your backlog — is exactly that:
optional, for real time left over, not a requirement of these 4 days.

## Day 5 — Share-out

Your instructor schedules this once every submission is in — usually a
few days after Day 4, not necessarily the next calendar day. Real
session, not optional: your instructor anonymizes every submitted
`memo.md`, groups students in threes, and each group reviews its
assigned memos as if they were the actual stakeholder — rating each one
for clarity, actionability, and whether it addressed the real business
problem — then shares the patterns it noticed across memos and reflects
on what it would change in its own writing. No prep needed beyond
having a real, finished `memo.md` already pushed — see your instructor
for the exact date.

## Above & Beyond (Your Backlog)

Only the additional items — everything above still applies and isn't
repeated here. All four are detailed in `ABOVE_AND_BEYOND.md`. Picking one
up *after* Day 4, if you have real time, is a bonus sprint — not part of
this one.

**This section's own given code (`above_and_beyond/`) isn't in your repo
by default** — it lives on this template's `project-scope` branch, same
as `MVP.md`/`ABOVE_AND_BEYOND.md`. Ask your instructor for that branch's
link if you want to pick any of this up.

- [ ] Find a **second** non-obvious pattern, from a different slice of the
  data than the one your business problem already led you to.
- [ ] Answer a **second** domain's business problem, briefly, using its
  own data file.
- [ ] Pick one memo question and actually try to answer it for real (a
  real search, not a guess) — write up what you found and whether it
  changed your confidence in your answer.
- [ ] Run the given-code `above_and_beyond/pandas_preview.py` and compare
  what it tells you to your own findings.
