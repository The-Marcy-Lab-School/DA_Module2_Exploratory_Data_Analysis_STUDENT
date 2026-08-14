# Above & Beyond

Finished the MVP with time to spare? Each of these previews a skill a later
module leans on — pick one or two, don't feel obligated to do all of them.

- **Find a second non-obvious pattern**, from a different slice of the data
  than the one your stakeholder's question already led you to — try a
  different grouping column or a different numeric variable. More reps at
  telling a real pattern from a coincidence is exactly what **Module 6**
  (dashboards), **Module 11** (inferential statistics), and **Module 12**
  (predictive analytics) all assume you already have.

- **Scale the dataset up and re-time it.** Concatenate `meteorite_landings.csv`
  with itself many times over (real code, not a given snippet — try
  `pandas.concat([df] * 40)`) and re-run your Part 2 timing comparison at
  that larger size. Does the winner change? Polars is specifically built
  for larger data and **lazy** query chains (`pl.scan_csv` instead of
  `pl.read_csv`) — try that too if you want the fuller picture. This turns
  the tradeoffs reflection from "explain" into "prove," and pandas/Polars
  fluency at real scale is exactly what **Module 4** assumes you're ready
  to build on.

- **Answer a second stakeholder's question**, briefly, using what you
  already built in Part 1-2 — you likely already have most of the pandas/
  Polars code you need. Write a short answer (a few sentences, not a full
  second report) in `memo.md`.

- **Verify one of your memo.md questions for real.** Pick the most
  checkable one and actually try to answer it — a real search, not a
  guess — then write up what you found and whether it changed your
  confidence in your answer to your stakeholder. This is the same "verify
  before trusting" habit **Module 13** (agentic AI tooling) and **Module
  14** (responsible AI) formally assess later, applied to your own claim
  instead of an AI's.

- **Preview of Module 4 — code given, you don't need to write this
  yourself.** `above_and_beyond/pandas_preview.py` is a real pandas chain
  (filter → group → aggregate in one line) applied to this same dataset —
  a taste of what full pandas fluency looks like once you're writing
  longer chains yourself. Run it, then add a short section to `memo.md`
  comparing what it tells you to your own findings.

None of these change what counts as "done" per `MVP.md` — they're
optional, and a complete MVP without any of these is still a full, passing
submission.
