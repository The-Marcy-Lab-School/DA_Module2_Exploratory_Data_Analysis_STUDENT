"""
Above & Beyond: a more advanced pandas chain -- code given, you don't need
to write this yourself.

This notebook already had you write real pandas code. This is a taste of
a more advanced technique -- binning a continuous variable into named
tiers and cross-tabulating it against a category in one chain -- that
goes beyond what MVP asks for. Real full fluency with chains like this
keeps deepening in Module 4.

Run it (python3 above_and_beyond/pandas_preview.py, from the repo root)
and read through it -- then add a short section to memo.md comparing what
this cross-tab tells you to what you found by hand.
"""
import pandas as pd

df = pd.read_csv("data/finance_insurance.csv")

# Bin claim severity into named tiers, then cross-tabulate against
# occupancy type in one chain -- .assign() + pd.cut() + a multi-level
# groupby().size().unstack() instead of building each piece separately.
result = (
    df.dropna(subset=["amountPaidOnBuildingClaim"])
    .assign(
        severity_tier=lambda d: pd.cut(
            d["amountPaidOnBuildingClaim"],
            bins=[-1, 5000, 25000, 1_000_000_000],
            labels=["low", "medium", "high"],
        )
    )
    .groupby(["occupancyType", "severity_tier"], observed=True)
    .size()
    .unstack(fill_value=0)
)

print("Claim counts by occupancy type and severity tier:\n")
print(result)
