# Project Overview: Exploratory Data Analysis

## The objective

Pick one of 4 business domains (see **Choose your domain** below), each with a real
stakeholder and a real or realistic dataset, and answer their question
with exploratory data analysis in a Jupyter notebook:

- **Inspect and clean** messy data: duplicates, missing values, text that
  should be numbers, and placeholder values.
- **Add a feature:** create a new column that helps answer the question.
- **Profile** the key variables with statistics and charts, and find a
  non-obvious pattern across groups.
- **Test an AI** in two directions: judge its read of your chart, and
  judge a chart it suggests.
- **Communicate:** a data-quality memo for your stakeholder and a README an
  employer can read.

## Why it matters

Most of an analyst's time goes into understanding and cleaning data
before any answer is trustworthy. This project is your first full pass:
inspect, clean, explore, and explain, with every decision justified. You
also practice choosing the right statistic for skewed data, which is one
of the most common analyst mistakes. Modules 3 and 4 build on this with
SQL and with pandas connected to a database.

## Choose your domain

Pick **one** of the four domains below. Each has its own stakeholder,
business problem, and data file. Everyone uses the same notebook,
`starter/analysis.ipynb`, and the same requirements. Once you choose,
delete the other three data files.

`data/SOURCE.md` lists every column and every known data problem for
each file. Read your file's section before you open the notebook.

### What every domain asks of you

- **Clean it:** find the data problems listed in `data/SOURCE.md` (and any
  you spot yourself), then decide how to handle each one and say why.
- **Add a feature:** create at least one new column that helps answer
  your stakeholder's question. Each domain below suggests one.
- **Answer the question** with the statistic that fits the data's shape.

### Option 1: Finance & Insurance

**Stakeholder:** an analyst at FEMA's National Flood Insurance Program.

> "Most of our 2015 South Carolina claims came from the October flood. I
> need to know what a typical claim actually paid, which causes of damage
> led to the most severe claims, and whether the number we'd use to plan
> next year's reserves is distorted by a few catastrophic claims."

**Data:** `data/finance_insurance.csv`, 5,710 claims from 2015.

**Suggested feature:** `total_paid`, the building payment plus the
contents payment for each claim.

**QAR note:** cause of damage and property type are FEMA codes (such as
`2` or `4`), not labels. Treat them as categories, and turn "what does
each code mean?" into one of your checkable questions.

### Option 2: Healthcare Operations

**Stakeholder:** a hospital-quality policy analyst reviewing public CMS
data.

> "Emergency departments report very different wait times for
> psychiatric patients before they leave. I need to know what 'typical'
> looks like, which states and hospitals are outliers, and whether this
> data is clean enough to put in a public report."

**Data:** `data/healthcare_operations.csv`, one row per hospital.

**Suggested feature:** `over_4_hours`, a True/False column for hospitals
whose median wait is over 240 minutes.

### Option 3: Public Sector

**Stakeholder:** a program manager at San Francisco's Department of
Building Inspection.

> "People ask how long a building permit takes to get issued and how much
> the work costs. I want a real answer, not an anecdote, and I want to
> know which permit types are slow and whether a few huge projects are
> skewing the story."

**Data:** `data/public_sector.csv`, permits filed in 2023.

**Suggested feature:** `days_to_issue`, the number of days from
`filed_date` to `issued_date`. This one takes a step you haven't done in
class: subtracting two date columns. See the hint in Part 2 of the
notebook.

**QAR note:** `estimated_cost` is the applicant's estimate of the work,
not the permit fee or the final cost. Say so when you report it.

### Option 4: Professional Services

**Stakeholder:** a managing partner at a consulting firm.

> "I want to understand how billed hours break down across our service
> lines and partners before we plan next quarter. I'm worried our
> timesheet data has gaps and errors that could throw off the numbers."

**Data:** `data/professional_services.csv`, 2,200 engagements. This file
is synthetic (made for this project), because real billed-hours data
isn't public.

**Suggested feature:** `is_ongoing`, a True/False column for engagements
with no `end_date` yet.

**QAR note:** the data has no column for individual staff, only partners.
If you talk about staffing, state what you're assuming.

### Before you write code: Question, Assumption, Risk

Your stakeholder won't tell you everything. Before you code, write at
least two QAR notes in `starter/REFLECTION.md`:

- **Question:** what does your code need to decide that the stakeholder
  didn't say? For example, what counts as "severe" or "slow"?
- **Assumption:** what will you assume for now?
- **Risk:** what goes wrong if you're wrong, and how would you check?

## Deliverables at a glance

- A **public GitHub repo** created with "Use this template" (not Fork).
- `starter/analysis.ipynb` complete, running top to bottom with
  **Restart and Run All**.
- `starter/memo.md`: your answer for the stakeholder and 2 checkable
  questions about the data.
- `starter/REFLECTION.md`: your QAR assumptions and one real AI prompt,
  checked.
- Charts saved in `images/`, at least one embedded in your README.
- Your own `README.md` replacing this template's.
- At least 4 commits with descriptive messages.
- The notebook made employer-facing: every instruction block and `TODO`
  deleted.
- School-facing files deleted and `starter/` renamed to `project/`.
- `project/presentation.pdf`: a 3-5 minute share-out deck built from
  your README, memo and reflection. Make it in any slide tool (Google
  Slides, PowerPoint, Canva, Keynote) and export it as a PDF.
- **Day 5 share-out:** present your deck to a small group, then take
  questions.

## Skills you'll practice

- **Statistics and distributions:** mean, median, spread, skew, and
  outliers, and choosing the statistic that fits.
- **Data cleaning:** reusable cleaning functions and justified
  missing-value decisions.
- **Feature creation:** adding a column that answers a business question.
- **Data mining and visualization:** group comparisons and charts that
  fit the question.
- **Critical thinking and AI evaluation:** checkable questions about the
  data, and judging an AI's chart claims against your own numbers.
- **Stakeholder communication:** a memo and README for readers who won't
  open your notebook.
- **Presentations:** a 3-5 minute talk from your deck on Day 5 that leads
  with your answer and handles a stakeholder's question.

## Above & Beyond (optional)

The Above & Beyond section in `CHECKLIST_RUBRIC.md` has 5
stretch items with starter links. None are required.

## Timeline

5 days: 4 build days and a share-out day. See `CHECKLIST_RUBRIC.md`.

## Where to start

Go to `README.md`. It walks you through setup.
