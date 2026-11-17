# Rubric: Exploratory Data Analysis

**Point scale:** Below Expectations = 1, Approaching = 2, Meets = 4,
Exceeds = 5 (extra credit; most Exceeds levels require Above & Beyond
work). 9 skills × 4 points = **36 points at Meets**.

Your instructor grades `analysis.ipynb`, `memo.md`, `REFLECTION.md`, your
rewritten `README.md`, and your commit history together. Exceeds levels
point to the Above & Beyond section at the bottom of
`CHECKLIST_TIMELINE.md`. The Day 5 share-out is practice and isn't graded.

You're graded on your reasoning: why a method, statistic, or chart fits
the question, not just whether the code runs.

Delete this file before your final push. It stays in the LMS.

---

## Technical Skills

### `statistical-analysis`

*Computing descriptive statistics and explaining what they mean for a
real metric.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus answers a second domain's business problem with the same reasoning (Above & Beyond). |
| **Meets** | 4 | Summary statistics are reported correctly throughout, with no mix-up between mean and median. Part 7 explains the standard deviation relative to the mean and what it means for the stakeholder's planning, using the Fellow's own numbers. |
| **Approaching** | 2 | Numbers are correct, but the explanation is a textbook definition not tied to the Fellow's own metric. |
| **Below Expectations** | 1 | Numbers are wrong or missing, or there's no interpretation. |

### `data-distributions-shape`

*Reading a distribution's shape and telling a real outlier from a value
that only looks extreme.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus profiles a useful 4th variable (Above & Beyond). |
| **Meets** | 4 | Part 3 profiles 3 numeric variables relevant to the stakeholder's problem. Each has summary statistics, a chart, and a shape and outlier call that matches what the chart and numbers show. The mean-or-median choice for each matches its shape. |
| **Approaching** | 2 | A shape call doesn't match its chart or numbers for one variable, or the mean is used on a clearly skewed variable without comment. |
| **Below Expectations** | 1 | A distribution is called "symmetric" or "normal" with no evidence, or fewer than 3 variables are profiled. |

### `data-mining`

*Finding a non-obvious pattern in unfamiliar data, with the statistic
that fits.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus a second non-obvious pattern from a different slice of the data (Above & Beyond). |
| **Meets** | 4 | Part 4 has a `groupby` table that compares each group's value of the key statistic with the overall value and says whether any group differs. The finding is non-obvious, uses the statistic that fits the skew, and rests on groups large enough to trust. |
| **Approaching** | 2 | The finding is trivial, the group-vs-overall comparison is asserted without per-group numbers, or a tiny group drives the finding without comment. |
| **Below Expectations** | 1 | No finding of the Fellow's own, or no group-vs-overall comparison. |

### `data-cleaning-imputation`

*Finding problems in raw data, fixing them on purpose with reusable
code, and adding a feature that helps answer the question.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus the cleaning function takes a column as a parameter and is reused on several columns, or the Fellow tests how much a cleaning decision changes the answer (for example, the median with and without filled-in values). |
| **Meets** | 4 | All 4: (1) duplicate rows are counted, and the decision to drop or keep them is justified; (2) a `def` cleaning function fixes a real problem and is called at least twice; (3) at least one missing-value column gets a drop, fill, or flag decision justified by what the column means; (4) at least one new column is created, checked, and used in the analysis. Placeholder or impossible values (such as a $1 cost or negative hours) are handled before any statistics, where the file has them. |
| **Approaching** | 2 | The function is called only once, a missing-value decision is stated but not justified, duplicates are dropped or kept without checking, or the new column is created but never checked or used. |
| **Below Expectations** | 1 | Fixes are copy-pasted inline with no function, missing values are silently dropped everywhere, or no new column is created. |

### `data-visualization`

*Choosing a chart that fits the question, labeling it, and putting the
real chart in front of the reader. Introductory bar.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus one chart is revised after a first draft, with a sentence on what the first version hid. Or every README chart has a title that states its takeaway. |
| **Meets** | 4 | Every required chart has a title and labeled axes with units. Parts 3 and 4 use at least 2 chart types, and the Part 4 chart choice is justified in a sentence. The Part 5 chart is saved as an image. The README embeds at least one real chart image from `images/`. |
| **Approaching** | 2 | Charts render, but axes are unlabeled, every chart is the same type, or the Part 4 choice isn't justified. |
| **Below Expectations** | 1 | Required charts are missing, or the README describes a chart in words instead of embedding it. |

---

## Professional Skills

### `critical-thinking`

*Asking specific, checkable questions about data before trusting a
conclusion drawn from it.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus the Fellow tries to answer one memo question for real and writes up whether it changed their confidence (Above & Beyond). |
| **Meets** | 4 | `memo.md` asks at least 2 specific questions a data steward could answer with a concrete fact, and connects at least one to whether the stakeholder should trust the answer. `REFLECTION.md` states at least 2 assumptions with Question, Assumption, Risk. |
| **Approaching** | 2 | Questions are generic enough to fit almost any dataset, or the trust paragraph or the assumptions are missing. |
| **Below Expectations** | 1 | Fewer than 2 real questions, or `memo.md` is missing or copied. |

### `stakeholder-communication`

*Presenting a finished analysis so someone who never opens the notebook
can understand it.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus the README and memo read as useful to a real stakeholder: specific numbers, a clear recommendation, no unexplained jargon. |
| **Meets** | 4 | `README.md` is fully rewritten with every required section, including an embedded chart. `memo.md` leads with a plain-language answer. School-facing files are deleted and `starter/` is renamed to `analysis/`. |
| **Approaching** | 2 | The README is missing a required section, or the memo buries the answer. |
| **Below Expectations** | 1 | The README is still the template's setup instructions, or most sections are missing. |

---

## AI Skills

### `ai-as-critic`

*Part 5: using AI to read your own chart, then judging whether its read
holds up.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus a follow-up prompt that pushes the AI on a claim it got wrong or left vague, with the second answer judged the same way. |
| **Meets** | 4 | A chart the Fellow made is saved and uploaded. The AI's response is pasted word for word. Each claim in it (shape, center, outliers, pattern) is judged right, wrong, or uncheckable, quoting the Fellow's own number that settles it. |
| **Approaching** | 2 | The judgment is generic ("mostly right") or by eye only, or the response is paraphrased. |
| **Below Expectations** | 1 | Part 5 is missing, the AI's read is accepted as-is, or no real image was uploaded. |

### `ai-evaluation`

*Part 5b: judging a chart the AI proposes, for fit and for accuracy.*

| Level | Points | Criteria |
|---|---|---|
| **Exceeds** | 5 | Meets, plus the Fellow names what the stakeholder would wrongly conclude from the AI's chart, or builds the better chart and shows the difference. |
| **Meets** | 4 | The AI's suggestion is pasted and judged on two counts: is it the right chart type for the question and the variable's shape, and do its values and labels match the Fellow's own numbers? |
| **Approaching** | 2 | Only one count is judged, or the verdict is based on looks ("it's clean"). |
| **Below Expectations** | 1 | Part 5b is missing, or the AI's chart is adopted without evaluation. |

## Reflection AI line (formative)

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

## Common mistakes that cost points

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
