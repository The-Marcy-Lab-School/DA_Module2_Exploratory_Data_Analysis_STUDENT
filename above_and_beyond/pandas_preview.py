"""
Above & Beyond: split a numeric column into three equal-sized tiers and
count how many rows from each category land in each tier.

Given code: you don't need to write this yourself. Copy this file into
your repo's top folder, set COLUMN and GROUP below to columns from your
own data file, then run:

    python3 pandas_preview.py

Compare the table to your Part 4 findings in memo.md. Look up pd.qcut and
.unstack() in the pandas docs to learn what each step does.
"""
import glob

import pandas as pd

COLUMN = None  # TODO: a numeric column, e.g. "billed_hours"
GROUP = None   # TODO: a category column, e.g. "service_type"

if COLUMN is None or GROUP is None:
    raise SystemExit("Set COLUMN and GROUP at the top of this file first.")

df = pd.read_csv(glob.glob("data/*.csv")[0])
values = pd.to_numeric(df[COLUMN], errors="coerce")

# Split into three tiers with about the same number of rows in each.
df["tier"] = pd.qcut(values, q=3, duplicates="drop")

# Rows per category in each tier, one column per tier.
table = df.groupby([GROUP, "tier"], observed=True).size().unstack(fill_value=0)

print("Rows per", GROUP, "in each", COLUMN, "tier:\n")
print(table)
