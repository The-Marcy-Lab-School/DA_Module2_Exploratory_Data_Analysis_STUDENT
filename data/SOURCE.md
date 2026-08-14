# Data Source

**Dataset:** NASA Meteorite Landings
**File:** `meteorite_landings.csv` (45,716 rows, 10 columns)
**Downloaded from:** https://data.nasa.gov/docs/legacy/meteorite_landings/Meteorite_Landings.csv

## License

Published by NASA (a U.S. federal agency; publisher bureau code `026:00`,
`accessLevel: public`). The dataset's own listing doesn't attach a specific
license, but NASA's official content policy resolves that: *"NASA content —
images, audio, video, related media and files... generally are not subject
to copyright in the United States... United States government works... are
not protected by copyright in the U.S. (17 U.S.C. §105) and may be used
without obtaining permission from NASA."* This is public-domain factual/
tabular data — safe to redistribute in this repo.

## Columns

| Column | Type | Notes |
|---|---|---|
| `name` | text | meteorite name |
| `id` | integer | record id |
| `nametype` | category | `Valid` or `Relict` (heavily lopsided — not useful for grouping) |
| `recclass` | category, 466 unique values | meteorite classification (e.g. `L6`, `H5`) |
| `mass (g)` | number | mass in grams; 131 rows missing |
| `fall` | category, 2 values | `Fell` (witnessed fall, 1,107 rows) or `Found` (discovered later, 44,609 rows) |
| `year` | number | year of fall/find; 291 rows missing |
| `reclat` | number | latitude; 7,315 rows missing |
| `reclong` | number | longitude; 7,315 rows missing |
| `GeoLocation` | text | `(lat, long)` as a single string — redundant with `reclat`/`reclong` |

## Known data-quality wrinkles (real, not staged)

These are genuinely present in the raw file — nothing here was added or
modified for this project:

- **7,315 rows have no `reclat`/`reclong` at all** (blank in the raw file).
- **Separately, 6,214 rows have `reclat`/`reclong` set to exactly
  `0.000000, 0.000000`** — a real location on Earth (off the coast of west
  Africa) that is wildly over-represented in this data, a classic sign of a
  missing-value placeholder rather than 6,214 genuine meteorite landings at
  the same spot.
- **131 rows are missing `mass (g)`; 291 rows are missing `year`.**
- **One row (`Northwest Africa 7701`) lists `year` as 2101** — a date in
  the future relative to when this dataset was compiled, almost certainly
  a data-entry error rather than a real historical find.
- **One row's `reclong` (354.47) falls outside the valid -180/180 range**
  for an Earth longitude — not a data error, worth investigating why.

This file is used unmodified — figuring out which of the above (if any)
actually matters for a specific analysis is part of the project.
