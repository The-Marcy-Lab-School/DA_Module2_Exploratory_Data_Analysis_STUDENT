# Checklist & Rubric: 5-Day Sprint

This file has four parts:

1. **MVP checklist:** the minimum to pass.
2. **Above & Beyond:** optional stretch work.
3. **Day-by-day plan:** what to do each day of the sprint.
4. **Rubric:** how your project is graded.

## MVP checklist

The minimum for a complete, passing project. It's the same list as the
MVP checklist in the LMS.

- [ ] **Domain chosen** from `PROJECT_OVERVIEW.md`, other 3 data files deleted.
- [ ] **Assumptions:** at least 2 QAR notes in `REFLECTION.md`.
- [ ] **Part 1:** shape, data types, missing values, and duplicate rows
  checked.
- [ ] **Part 2:** a justified decision on duplicate rows; a `def`
  cleaning function called at least twice; a justified drop, fill, or
  flag decision for missing values; placeholder or impossible values
  handled.
- [ ] **Part 2b:** at least one new column, checked and used.
- [ ] **Part 3:** 3 numeric variables profiled, each with summary
  statistics, a labeled chart, and a shape and outlier call.
- [ ] **Part 4:** a `groupby` table comparing each group with the
  overall number, a chart that fits, and a non-obvious finding.
- [ ] **At least 2 chart types** across Parts 3 and 4, each with a title
  and labeled axes.
- [ ] **Part 5:** a saved chart, an AI's read of it pasted word for word,
  and each claim judged against your numbers.
- [ ] **Part 5b:** an AI-suggested chart judged on type and accuracy.
- [ ] **Parts 6 and 7:** the stakeholder answered with the statistic that
  fits, and the standard deviation explained.
- [ ] **`memo.md`:** a plain-language answer, 2 checkable questions, and
  the link to trust.
- [ ] **`REFLECTION.md`:** QAR assumptions and one real AI prompt,
  checked.
- [ ] **Notebook runs** with Restart and Run All.
- [ ] **Notebook is employer-facing:** every instruction block, `TODO`,
  and the "Questions" section deleted, with your own explanation in every
  section.
- [ ] **Your own `README.md`** with every section listed at the top of
  the template README (including Statistical summary, Recommendations, and How AI was used),
  and at least one chart embedded from `images/`.
- [ ] **Clean submission:** `CHECKLIST_RUBRIC.md` and
  `PROJECT_OVERVIEW.md` deleted, and `starter/` renamed to `project/`.
- [ ] **Public GitHub repo** with at least 4 commits, each with a
  descriptive message that says what changed.
- [ ] **Day 5 share-out:** a pair repo review and a 90-second BLUF
  answer. Not graded.

## Above & Beyond (optional)

These use tools the MVP doesn't need. Research them yourself, starting
from the links. A complete MVP without any of these is still a full,
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

## Day-by-day plan

**4 build days, then a share-out day.** Work through the items in order.

Start each build day with a 2-minute check-in. Answer three questions:
What did I finish last build day? What will I finish today? Is anything
blocking me?

### Day 1: Set up, choose, and inspect

- [ ] Create your repo with **"Use this template"** (not Fork), clone it,
  and follow every setup step in `README.md`, including the virtual
  environment and kernel.
- [ ] Replace `[YOUR NAME]` in `LICENSE` and commit.
- [ ] Confirm you have an AI assistant that accepts image uploads. You'll
  need it on Day 3.
- [ ] Read all 4 domains in `PROJECT_OVERVIEW.md`. Pick one and delete the other
  3 data files.
- [ ] Read your file's section in `data/SOURCE.md`.
- [ ] Write at least 2 QAR assumptions in `starter/REFLECTION.md`.
- [ ] Fill in "Stakeholder and business problem" in the notebook.
- [ ] **Part 1:** inspect shape, data types, missing values, and duplicate
  rows. Write down what you found.
  - Common mistake: guessing a column's type from its name instead of
    checking.
- [ ] Commit with a descriptive message, such as
  `git commit -m "Inspect flood claims data: dtypes, blanks, duplicates"`.
  Messages like `update` or `final` don't tell an employer anything.

### Day 2: Clean, add a feature, profile

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

### Day 3: Segments and AI critiques

- [ ] **Part 4:** a `groupby` table comparing each group with the overall
  number, a chart that fits, and a non-obvious finding.
  - Common mistake: reporting only the overall number, or a pattern from
    a tiny group.
- [ ] **Part 5:** save a chart to `images/`, get an AI's read of it, paste
  it word for word, and judge each claim against your numbers.
- [ ] **Part 5b:** ask an AI to suggest a chart and judge its type and
  accuracy. If it gives you code, audit it: rows before and after, one number checked by hand, data
  types, what got dropped or filled, and whether the statistic fits the
  shape. If the code merges or filters, also predict the row count first,
  count any blanks a merge adds, and test an edge case.
- [ ] Commit and push. You should have at least 4 commits on GitHub by
  the end of Day 3.

### Day 4: Answer, write up, clean up

- [ ] **Part 6:** answer your stakeholder, backed by the statistic that
  fits.
- [ ] **Part 7:** explain the standard deviation of your key variable.
- [ ] Write `starter/memo.md` and finish `starter/REFLECTION.md`, including
  "One real AI prompt, checked."
- [ ] Make the notebook employer-facing: delete every **Instructions
  (delete before you submit)** block, every `TODO`, and the "Questions my
  analysis can answer" section. Replace them with your own explanations.
  Read it top to bottom as a hiring manager would.
- [ ] Run **Restart and Run All** and confirm every cell runs with no
  errors.
- [ ] Replace `README.md` with your own, using the sections listed at its
  top: title and summary, stakeholder and business problem, data,
  analysis, statistical summary, findings, recommendations, how AI was
  used, and how to run it. Embed at least one chart from `images/` with
  `![caption](images/chart_name.png)`.
  - Common mistake: describing a chart in words instead of embedding it.
- [ ] Delete `CHECKLIST_RUBRIC.md` (this file) and `PROJECT_OVERVIEW.md`.
  They're school-facing and stay in the LMS.
- [ ] Rename the folder: `git mv starter project`. Run the notebook once
  more from `project/` to confirm it still works.
- [ ] Final push. Open your repo in a private browser window to confirm
  it's public and the chart shows in the README.

### Day 5: Share-out

No slides. You'll do two things in class, in TIP style:

- **Pair repo review:** you and a partner review each other's repo against
  a checklist your instructor hands out, then trade one strength and one
  fix.
- **Beat the Buzzer:** answer "What did you find?" in 90 seconds using
  BLUF (Bottom Line Up Front): your answer and its number first, then the
  evidence, then one caveat. Your instructor stops you at 110 seconds.
  Classmates score you, and you try again.

To prepare:

- [ ] Your README's findings and recommendations are your talking points.
  Rehearse your BLUF answer once with a 90-second timer.
- [ ] After the share-out, push any fixes your partner found.

---

## Rubric

**Point scale:** Below Expectations = 1, Approaching = 2, Meets = 4,
Exceeds = 5 (extra credit; most Exceeds levels require Above & Beyond
work). 9 skills × 4 points = **36 points at Meets**.

Your instructor grades `analysis.ipynb`, `memo.md`, `REFLECTION.md`, your
rewritten `README.md`, and your commit history together. Exceeds levels
point to the Above & Beyond section above. The Day 5 share-out is practice and isn't graded.

You're graded on your reasoning: why a method, statistic, or chart fits
the question, not just whether the code runs.

---

### Technical Skills

#### `statistical-analysis`

*Computing descriptive statistics and explaining what they mean for a
real metric.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus answers a second domain's business problem with the same reasoning (Above & Beyond). |
| **Meets** | 4 | Summary statistics are reported correctly throughout, with no mix-up between mean and median. Part 7 explains the standard deviation relative to the mean and what it means for the stakeholder's planning, using the Fellow's own numbers. |
| **Approaching** | 2 | Numbers are correct, but the explanation is a textbook definition not tied to the Fellow's own metric. |
| **Below Expectations** | 1 | Numbers are wrong or missing, or there's no interpretation. |

#### `data-distributions-shape`

*Reading a distribution's shape and telling a real outlier from a value
that only looks extreme.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus profiles a useful 4th variable (Above & Beyond). |
| **Meets** | 4 | Part 3 profiles 3 numeric variables relevant to the stakeholder's problem. Each has summary statistics, a chart, and a shape and outlier call that matches what the chart and numbers show. The mean-or-median choice for each matches its shape. |
| **Approaching** | 2 | A shape call doesn't match its chart or numbers for one variable, or the mean is used on a clearly skewed variable without comment. |
| **Below Expectations** | 1 | A distribution is called "symmetric" or "normal" with no evidence, or fewer than 3 variables are profiled. |

#### `data-mining`

*Finding a non-obvious pattern in unfamiliar data, with the statistic
that fits.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus a second non-obvious pattern from a different slice of the data (Above & Beyond). |
| **Meets** | 4 | Part 4 has a `groupby` table that compares each group's value of the key statistic with the overall value and says whether any group differs. The finding is non-obvious, uses the statistic that fits the skew, and rests on groups large enough to trust. |
| **Approaching** | 2 | The finding is trivial, the group-vs-overall comparison is asserted without per-group numbers, or a tiny group drives the finding without comment. |
| **Below Expectations** | 1 | No finding of the Fellow's own, or no group-vs-overall comparison. |

#### `data-cleaning-imputation`

*Finding problems in raw data, fixing them on purpose with reusable
code, and adding a feature that helps answer the question.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus the cleaning function takes a column as a parameter and is reused on several columns, or the Fellow tests how much a cleaning decision changes the answer (for example, the median with and without filled-in values). |
| **Meets** | 4 | All 4: (1) duplicate rows are counted, and the decision to drop or keep them is justified; (2) a `def` cleaning function fixes a real problem and is called at least twice; (3) at least one missing-value column gets a drop, fill, or flag decision justified by what the column means; (4) at least one new column is created, checked, and used in the analysis. Placeholder or impossible values (such as a $1 cost or negative hours) are handled before any statistics, where the file has them. |
| **Approaching** | 2 | The function is called only once, a missing-value decision is stated but not justified, duplicates are dropped or kept without checking, or the new column is created but never checked or used. |
| **Below Expectations** | 1 | Fixes are copy-pasted inline with no function, missing values are silently dropped everywhere, or no new column is created. |

#### `data-visualization`

*Choosing a chart that fits the question, labeling it, and putting the
real chart in front of the reader. Introductory bar.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus one chart is revised after a first draft, with a sentence on what the first version hid. Or every README chart has a title that states its takeaway. |
| **Meets** | 4 | Every required chart has a title and labeled axes with units. Parts 3 and 4 use at least 2 chart types, and the Part 4 chart choice is justified in a sentence. The Part 5 chart is saved as an image. The README embeds at least one real chart image from `images/`. |
| **Approaching** | 2 | Charts render, but axes are unlabeled, every chart is the same type, or the Part 4 choice isn't justified. |
| **Below Expectations** | 1 | Required charts are missing, or the README describes a chart in words instead of embedding it. |

---

### Professional Skills

#### `critical-thinking`

*Asking specific, checkable questions about data before trusting a
conclusion drawn from it.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus the Fellow tries to answer one memo question for real and writes up whether it changed their confidence (Above & Beyond). |
| **Meets** | 4 | `memo.md` asks at least 2 specific questions a data steward could answer with a concrete fact, and connects at least one to whether the stakeholder should trust the answer. `REFLECTION.md` states at least 2 assumptions with Question, Assumption, Risk. |
| **Approaching** | 2 | Questions are generic enough to fit almost any dataset, or the trust paragraph or the assumptions are missing. |
| **Below Expectations** | 1 | Fewer than 2 real questions, or `memo.md` is missing or copied. |

#### `stakeholder-communication`

*Presenting a finished analysis so someone who never opens the notebook
can understand it.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus the README and memo read as useful to a real stakeholder: specific numbers, a clear recommendation, no unexplained jargon. |
| **Meets** | 4 | `README.md` is fully rewritten with every required section, including a statistical summary, recommendations, how AI was used, and an embedded chart. `memo.md` leads with a plain-language answer. The notebook is employer-facing: no instruction blocks or `TODO`s are left, and every section has the Fellow's own explanation. School-facing files are deleted, `starter/` is renamed to `project/`, and commit messages describe what changed. |
| **Approaching** | 2 | The README is missing a required section, the memo buries the answer, or instruction blocks and `TODO`s are left in the notebook. |
| **Below Expectations** | 1 | The README is still the template's setup instructions, or most sections are missing. |

---

### AI Skills

#### `ai-as-critic`

*Part 5: using AI to read your own chart, then judging whether its read
holds up.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus a follow-up prompt that pushes the AI on a claim it got wrong or left vague, with the second answer judged the same way. |
| **Meets** | 4 | A chart the Fellow made is saved and uploaded. The AI's response is pasted word for word. Each claim in it (shape, center, outliers, pattern) is judged right, wrong, or uncheckable, quoting the Fellow's own number that settles it. |
| **Approaching** | 2 | The judgment is generic ("mostly right") or by eye only, or the response is paraphrased. |
| **Below Expectations** | 1 | Part 5 is missing, the AI's read is accepted as-is, or no real image was uploaded. |

#### `ai-evaluation`

*Part 5b: judging a chart the AI proposes, for fit and for accuracy.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus the Fellow names what the stakeholder would wrongly conclude from the AI's chart, or builds the better chart and shows the difference. |
| **Meets** | 4 | The AI's suggestion is pasted and judged on two counts: is it the right chart type for the question and the variable's shape, and do its values and labels match the Fellow's own numbers? |
| **Approaching** | 2 | Only one count is judged, or the verdict is based on looks ("it's clean"). |
| **Below Expectations** | 1 | Part 5b is missing, or the AI's chart is adopted without evaluation. |

### Reflection AI line (formative)

*Did you ask the AI well, and check what it gave you?* This covers
`REFLECTION.md`'s "One real AI prompt, checked" section. It's scored and
you get feedback on it, but it doesn't count toward the 36 points. Didn't
use AI? You can still earn Meets: write the prompt you would have used,
label it "not sent," and run the same check on your own work.

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus a second version of the prompt with what changed and why. Or the check caught a real flaw, and the Fellow explains what they fixed. |
| **Meets** | 4 | One real prompt, pasted word for word. At least one technique is named and pointed to in the prompt. The AI's answer is shown, trimmed but not reworded. One concrete check, and what it showed. |
| **Approaching** | 2 | The technique is named but not pointed to, or the check is vague ("it looked right"). |
| **Below Expectations** | 1 | No prompt, or an answer accepted with no check. |

### Common mistakes that cost points

1. Calling a distribution "symmetric" or "normal" without looking at a
   chart.
2. Using the mean on a clearly skewed variable without saying why.
3. Trusting a pattern from a very small group.
4. Data-quality questions too generic to check ("is this data accurate?").
5. Copy-pasting the same fix instead of writing one function.
6. A missing-value decision with no reason.
7. Dropping duplicate rows without checking whether they're real
   duplicates.
8. Computing statistics before handling placeholder values.
9. Describing a chart in your README instead of embedding the image.
10. Reporting only the overall number without checking every group.
11. Using the same chart type for everything instead of the one that fits
    the variable and the question.
