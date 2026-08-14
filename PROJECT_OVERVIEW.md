# Project Overview: EDA Profile — NASA Meteorite Landings

## What you're building

A written exploratory-data-analysis (EDA) profile of a real dataset you
haven't worked with before: 45,716 real NASA-recorded meteorite landings.
You'll pick a stakeholder and their real question (`SCENARIOS.md`), then
write real **pandas** code to explore it, redo that same core analysis in
**Polars** (a second, newer dataframe library) and reflect on the real
tradeoffs between them, generate your own chart and get an AI's read on
the actual image, and answer your stakeholder's question with the right
statistic for your data's actual skew. You'll close with a written report
raising real, checkable data-quality concerns — the kind of thing an
analyst should ask *before* anyone trusts a conclusion built on this data.

## Why this matters

Module 1 was about writing correct code. This project is about two more
things at once: writing real code to actually explore data (not just
running code someone else wrote), and deciding whether to trust what that
exploration — or an AI describing it — actually tells you. Dataframe
fluency across more than one library, reading a distribution's shape
correctly, and questioning an AI's read on your own work all come back
constantly for the rest of the program: **pandas gets a full, dedicated
module next in Module 4**, and this is your first real exposure to it, not
your last. **Statistical reasoning becomes a practical, recurring concern
starting in Module 6** (dashboards) and again in **Module 11** (inferential
statistics) and **Module 12** (predictive analytics/ML) — and not trusting
a fluent-sounding AI description at face value is exactly what **Module
13** (agentic AI tooling) and **Module 14** (responsible AI) formally
assess later.

## Skills you'll practice

- **Statistical Analysis** — computing and correctly interpreting mean,
  median, and standard deviation, including what a large spread implies.
- **Data Distributions & Shape** — reading a five-number summary and a
  histogram together to correctly call a distribution symmetric or skewed,
  and to spot a real outlier (or something that only looks like one).
- **Data Mining** — finding a genuinely non-obvious pattern or segment in
  a dataset you've never seen before, without being handed the answer.
- **Critical Thinking** — asking specific, checkable questions about where
  data came from and what might be wrong with it, before trusting a
  conclusion drawn from it — including an AI's own conclusion about a
  chart you made.
- **Dataframe Manipulation (pandas & Polars)** — real, hands-on authorship
  in two dataframe libraries, and reasoning about when each one actually
  wins. Not yet an official curriculum skill line — see
  `../../CURRICULUM_CHANGES.md` if you're curious — but a real, graded part
  of this project.

## Deliverables at a glance

- `starter/analysis.ipynb` — pandas exploration, the Polars comparison +
  tradeoffs reflection, the AI-vision exercise, and your answer to your
  stakeholder's question.
- `starter/memo.md` — your written findings report for your stakeholder,
  plus the required data-quality questions.

See `SCENARIOS.md` to pick your stakeholder first, `CHECKLIST_TIMELINE.md`
for the day-by-day pace and the full submission checklist, and
`README.md` for how to get set up.
