# Data Sources

Pick **one** of the four files below, matching the domain you chose in
`DOMAIN_SCENARIOS.md`. Three are real, government-published data, trimmed
to a focused set of columns (not modified otherwise — real messiness
left in). One (`professional_services.csv`) is clearly-labeled synthetic
data, generated for this project because real billable-hours data is
proprietary business information that isn't published anywhere.

## `finance_insurance.csv` — FEMA NFIP flood insurance claims (South Carolina, 2015)

**5,710 rows.** Real claims data from FEMA's National Flood Insurance
Program. **License:** U.S. Government Work — public domain (17 U.S.C.
§105), per FEMA's own OpenFEMA data dictionary.

| Column | Notes |
|---|---|
| `dateOfLoss` | date of the flood event |
| `occupancyType` | FEMA-defined numeric code (not decoded here — see "known wrinkles") |
| `countyCode` | numeric county code |
| `causeOfDamage` | categorical, 158 rows blank |
| `amountPaidOnBuildingClaim` | dollars paid on the building claim; **1,464 rows missing** |
| `amountPaidOnContentsClaim` | dollars paid on contents; **1,464 rows missing** |
| `buildingDamageAmount` | assessed damage; **876 rows missing** |
| `netBuildingPaymentAmount` | net payment amount |

**Known wrinkle:** `occupancyType` is a real FEMA numeric code (1, 2, 3,
6, 11, ...) — this file doesn't decode it into readable labels. Whether
that's worth tracking down, and where, is a real question, not solved
for you here.

## `healthcare_operations.csv` — CMS emergency-department wait times

**4,658 rows**, one per U.S. hospital, filtered from CMS's public
"Timely and Effective Care" dataset to measure `OP_18c` (median minutes
psychiatric patients spent in the ED before leaving). **License:** public
domain — CMS's own data dictionary states "public reporting data are in
the public domain and permission is not required to reuse them."

| Column | Notes |
|---|---|
| `Facility Name` | hospital name |
| `State` | 2-letter state code |
| `County/Parish` | county |
| `ed_wait_minutes` | **not a clean numeric column** — most rows are real numbers, but some contain the literal text `"Not Available"` (CMS's own suppression flag for small sample sizes) |
| `Sample` | how CMS describes the sample size for that row (also text, not always numeric) |
| `Footnote` | CMS footnote code explaining suppression, where present; blank otherwise |

**Known wrinkle:** `ed_wait_minutes` needs real cleaning before it's
usable as a number — see above.

## `public_sector.csv` — San Francisco building permits (filed 2023)

**24,913 rows.** Real permit data from DataSF. **License:** Open Data
Commons Public Domain Dedication and License (PDDL), per DataSF's own
dataset metadata.

| Column | Notes |
|---|---|
| `permit_type_definition` | category of permit (e.g. "otc alterations permit") |
| `filed_date` | when the permit application was filed |
| `issued_date` | when issued; **2,012 rows missing** (still pending, or never issued) |
| `completed_date` | when work finished; **7,266 rows missing** |
| `estimated_cost` | dollars; **158 rows missing** |
| `existing_units` | **4,887 rows missing** |
| `proposed_units` | **4,662 rows missing** |

**Known wrinkle:** processing time isn't a column — it's something you'd
compute from two date columns yourself, and only for rows where both
dates actually exist.

## `professional_services.csv` — Consulting engagement hours (synthetic)

**2,200 rows.** **Clearly synthetic** — generated for this project, not
real client data (which no firm publishes). Built to have the same kind
of real-feeling messiness as the three real files above: right-skewed
`billed_hours` with rare, genuinely huge outlier engagements, ~4% missing
`billed_hours` (unlogged time), a handful of negative `billed_hours`
values (data-entry errors, planted on purpose), and blank `end_date` for
projects still ongoing as of the file's cutoff.

| Column | Notes |
|---|---|
| `project_id` | unique id |
| `service_type` | Audit / Tax Advisory / Litigation Support / Strategy Consulting |
| `client_industry` | client's industry |
| `partner_assigned` | partner overseeing the engagement |
| `start_date` / `end_date` | `end_date` blank for still-ongoing projects |
| `billed_hours` | see wrinkles above |
