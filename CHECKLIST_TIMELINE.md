# Checklist & Timeline: 5-Day Sprint

**4 build days, then a share-out day.** Work through the items in order.
Each one is also part of the submission checklist.

Start each build day with a 2-minute check-in. Answer three questions:
What did I finish yesterday? What am I doing today? Is anything blocking
me?

## Day 1: Set up, choose, and inspect

- [ ] Create your repo with **"Use this template"** (not Fork), clone it,
  and follow every setup step in `README.md`, including the virtual
  environment and kernel.
- [ ] Replace `[YOUR NAME]` in `LICENSE` and commit.
- [ ] Confirm you have an AI assistant that accepts image uploads. You'll
  need it on Day 3.
- [ ] Read all 4 domains in `SCENARIOS.md`. Pick one and delete the other
  3 data files.
- [ ] Read your file's section in `data/SOURCE.md`.
- [ ] Write at least 2 QAR assumptions in `starter/REFLECTION.md`.
- [ ] Fill in "Your scenario" in the notebook.
- [ ] **Part 1:** inspect shape, data types, missing values, and duplicate
  rows. Write down what you found.
  - Common mistake: guessing a column's type from its name instead of
    checking.
- [ ] Commit: `git commit -m "inspect [domain] data"`.

## Day 2: Clean, add a feature, profile

- [ ] **Part 2:** decide on duplicates, write a cleaning function and call
  it at least twice, make a justified drop, fill, or flag decision, and
  handle any placeholder values.
  - Common mistake: copy-pasting the same fix instead of writing a
    function.
  - Common mistake: dropping matching rows without checking whether
    they're separate records.
- [ ] **Part 2b:** add at least one new column and check it.
- [ ] **Part 3:** profile 3 numeric variables, each with summary
  statistics, a labeled chart, and a shape and outlier call.
  - Common mistake: calling a distribution "normal" without looking at
    the chart.
- [ ] Commit after cleaning and again after profiling.

## Day 3: Segments and AI critiques

- [ ] **Part 4:** a `groupby` table comparing each group with the overall
  number, a chart that fits, and a non-obvious finding.
  - Common mistake: reporting only the overall number, or a pattern from
    a tiny group.
- [ ] **Part 5:** save a chart to `images/`, get an AI's read of it, paste
  it word for word, and judge each claim against your numbers.
- [ ] **Part 5b:** ask an AI to suggest a chart and judge its type and
  accuracy. If it gives you code, recall the AI audit checklist
  from class: rows before and after, one number checked by hand, data
  types, what got dropped or filled, and whether the statistic fits the
  shape. If the code merges or filters, also predict the row count first,
  count any blanks a merge adds, and test an edge case.
- [ ] Commit and push. You should have at least 4 commits on GitHub by
  the end of Day 3.

## Day 4: Answer, write up, clean up

- [ ] **Part 6:** answer your stakeholder, backed by the statistic that
  fits.
- [ ] **Part 7:** explain the standard deviation of your key variable.
- [ ] Write `starter/memo.md` and finish `starter/REFLECTION.md`, including
  "One real AI prompt, checked."
- [ ] Delete the "Questions my analysis can answer" section from the
  notebook.
- [ ] Run **Restart and Run All** and confirm every cell runs with no
  errors.
- [ ] Replace `README.md` with your own, using the sections listed at its
  top. Embed at least one chart from `images/` with
  `![caption](images/chart_name.png)`.
  - Common mistake: describing a chart in words instead of embedding it.
- [ ] Delete `CHECKLIST_TIMELINE.md` (this file), `RUBRIC.md`,
  `SCENARIOS.md`, and `PROJECT_OVERVIEW.md`. They're school-facing and stay
  in the LMS.
- [ ] Rename the folder: `git mv starter analysis`. Run the notebook once
  more from `analysis/` to confirm it still works.
- [ ] Final push. Open your repo in a private browser window to confirm
  it's public and the chart shows in the README.

## Day 5: Share-out

No slides. You'll do two things in class, in TIP style:

- **Pair repo review:** you and a partner review each other's repo against
  a checklist your instructor hands out, then trade one strength and one
  fix.
- **Beat the Buzzer:** answer "What did you find?" in 90 seconds using
  BLUF (Bottom Line Up Front): your answer and its number first, then the
  evidence, then one caveat. Your instructor stops you at 110 seconds.
  Classmates score you, and you try again.

To prepare:

- [ ] Your README's takeaways are your talking points. Say your answer
  out loud once, with a timer.
- [ ] After the share-out, push any fixes your partner found.

## Above & Beyond (optional)

Most of these go past what was taught in class. Research them yourself,
starting from the links. A complete MVP without any of these is still a full,
passing submission.

**Use AI to learn, not to do it for you.** Ask it to explain a concept,
show a small example on different data, or review code you wrote. Don't
paste in the task and copy the answer. Note what you looked up in
`REFLECTION.md`.

- [ ] **Profile a 4th variable** that adds something the first 3 don't.
- [ ] **Find a second non-obvious pattern** using a different grouping
  column or variable. Start here: [pandas: group by](https://pandas.pydata.org/docs/user_guide/groupby.html).
- [ ] **Answer a second domain's question** in a few sentences in
  `memo.md`. Download that domain's file from `data/` in the original
  template repo.
- [ ] **Check one of your memo questions for real.** Look it up in the
  data publisher's own documentation and write up whether it changed your
  confidence. Start here: [OpenFEMA](https://www.fema.gov/about/openfema/data-sets),
  [CMS Provider Data](https://data.cms.gov/provider-data/), or
  [DataSF](https://data.sfgov.org/).
- [ ] **Split a numeric variable into tiers and count each group in
  each tier.** The `project-scope` branch of the original template has a
  given script, `above_and_beyond/pandas_preview.py`. Copy it into your
  repo's top folder, set the two column names at the top, run it, and
  compare its table to your findings in `memo.md`. It combines `pd.qcut`
  and `.unstack()`, which you may recall from class, in a new way. Start here:
  [pandas: `pd.qcut`](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html).
