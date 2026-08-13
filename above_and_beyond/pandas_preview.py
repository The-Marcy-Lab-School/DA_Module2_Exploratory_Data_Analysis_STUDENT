"""
Above & Beyond: Preview of Module 4 -- code given, you don't need to write
this yourself.

Everything in analysis.ipynb used one given helper function and a few given
groupby().describe() calls. This is a small, real taste of what full
pandas fluency looks like once you're writing this kind of chain yourself
(Module 4, Python for Data Analysis) -- filtering, grouping, and
aggregating in one line instead of eyeballing separate tables.

Run it (python3 above_and_beyond/pandas_preview.py, from the repo root) and
read through it -- then add a short section to memo.md comparing what this
one chain tells you to what you found by hand in Part 3 of the notebook.
"""
import pandas as pd

df = pd.read_csv("data/meteorite_landings.csv")

# A real pandas chain: for meteorites found (not witnessed falling) since
# 1970, with a recorded mass, what's the median mass per classification --
# but only for classifications with at least 50 such records, so a single
# huge/tiny meteorite in a rare class doesn't distort the comparison?
result = (
    df[(df["fall"] == "Found") & (df["year"] >= 1970)]
    .dropna(subset=["mass (g)"])
    .groupby("recclass")
    .filter(lambda g: len(g) >= 50)
    .groupby("recclass")["mass (g)"]
    .median()
    .sort_values(ascending=False)
)

print(f"{len(result)} classifications with 50+ found-since-1970 records:\n")
print(result.head(10))
