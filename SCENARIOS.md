# Choose Your Domain

Pick **one** of the four domains below. Each has its own stakeholder,
business problem, and data file. Everyone uses the same notebook,
`starter/analysis.ipynb`, and the same requirements. Once you choose,
delete the other three data files.

`data/SOURCE.md` lists every column and every known data problem for
each file. Read your file's section before you open the notebook.

## What every domain asks of you

- **Clean it:** find the data problems listed in `data/SOURCE.md` (and any
  you spot yourself), then decide how to handle each one and say why.
- **Add a feature:** create at least one new column that helps answer
  your stakeholder's question. Each domain below suggests one.
- **Answer the question** with the statistic that fits the data's shape.

## Option 1: Finance & Insurance

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

## Option 2: Healthcare Operations

**Stakeholder:** a hospital-quality policy analyst reviewing public CMS
data.

> "Emergency departments report very different wait times for
> psychiatric patients before they leave. I need to know what 'typical'
> looks like, which states and hospitals are outliers, and whether this
> data is clean enough to put in a public report."

**Data:** `data/healthcare_operations.csv`, one row per hospital.

**Suggested feature:** `over_4_hours`, a True/False column for hospitals
whose median wait is over 240 minutes.

## Option 3: Public Sector

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

## Option 4: Professional Services

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

## Before you write code: Question, Assumption, Risk

Your stakeholder won't tell you everything. Before you code, write at
least two QAR notes in `starter/REFLECTION.md`:

- **Question:** what does your code need to decide that the stakeholder
  didn't say? For example, what counts as "severe" or "slow"?
- **Assumption:** what will you assume for now?
- **Risk:** what goes wrong if you're wrong, and how would you check?
