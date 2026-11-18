# Data Sources

Four files, one per domain in `PROJECT_OVERVIEW.md`. Three are real
government data, trimmed to the columns below but otherwise left as
published, problems included. One, `professional_services.csv`, is
synthetic, because real billed-hours data isn't public.

## How the four differ

| Domain | File | Rows | Main data problem | New column you'll add |
|---|---|---|---|---|
| Finance | `finance_insurance.csv` | 5,710 | Missing payments that really mean $0, coded categories, rows that look duplicated | `total_paid` |
| Healthcare | `healthcare_operations.csv` | 4,658 | The wait-time column is text, with "Not Available" in 35% of rows | `over_4_hours` |
| Public sector | `public_sector.csv` | 24,913 | Exact duplicate rows, a $1 placeholder cost, extreme projects | `days_to_issue` |
| Professional services | `professional_services.csv` | 2,200 | Missing and negative hours, a few huge engagements | `is_ongoing` |

Every file has missing values and at least one skewed numeric column, so
every domain needs a cleaning decision and a mean-or-median decision.

## Finance: FEMA flood insurance claims (South Carolina, 2015)

Real claims from FEMA's National Flood Insurance Program. Public domain
(U.S. Government Work). 94% of claims are from October 2015, the month of
the South Carolina flood.

| Column | What it holds |
|---|---|
| `dateOfLoss` | Date of the flood event, stored as text |
| `occupancyType` | FEMA property-type code, such as 1 or 11 (12 codes, not decoded) |
| `countyCode` | County FIPS code (37 counties), stored as a decimal number |
| `causeOfDamage` | FEMA cause code: `0`, `1`, `2`, `3`, `4`, `9`, or `A` |
| `amountPaidOnBuildingClaim` | Dollars paid for the building |
| `amountPaidOnContentsClaim` | Dollars paid for belongings |
| `buildingDamageAmount` | Assessed building damage in dollars |
| `netBuildingPaymentAmount` | Net building payment |

**Known problems:**
- 1,464 rows have no building **and** no contents payment. In every one
  of them `netBuildingPaymentAmount` is 0, which suggests "no payment",
  not "unknown".
- 876 rows are missing `buildingDamageAmount`, 158 are missing
  `causeOfDamage`, and 6 are missing `countyCode`.
- `causeOfDamage` has 5 rows coded `A`, which isn't a standard code.
- 422 rows are exact copies of another row. Almost all are no-payment
  claims. The file has no claim ID, so two separate claims can look
  identical. Decide whether these are real duplicates before you drop
  anything.
- 1 negative contents payment.
- Codes aren't labels. Treat them as categories.

## Healthcare: CMS emergency-department wait times

One row per hospital, from CMS's public "Timely and Effective Care" data,
measure OP_18c: the median minutes psychiatric patients spent in the
emergency department before leaving. Public domain.

| Column | What it holds |
|---|---|
| `Facility Name` | Hospital name |
| `State` | 2-letter code: 50 states plus DC, PR, GU, VI, AS, MP |
| `County/Parish` | County |
| `ed_wait_minutes` | Median wait in minutes, **stored as text** |
| `Sample` | Number of patients behind the measure, also text |
| `Footnote` | CMS code explaining why a value is missing, where present |

**Known problems:**
- `ed_wait_minutes` is text. 1,635 rows (35%) say `Not Available`, CMS's
  flag for too few patients to report. Convert the column to numbers
  before any math.
- Some states and territories have very few hospitals with data (Guam
  has 1, Puerto Rico and Delaware have 4). Don't rank them alongside
  large states without saying so.
- The longest wait is 6,870 minutes, nearly 5 days.
- 1 exact duplicate row. After you drop it, 15 more hospitals still
  share a name and state with another row.

## Public sector: San Francisco building permits (filed 2023)

Permits from DataSF. Open Data Commons Public Domain Dedication and
License (PDDL).

| Column | What it holds |
|---|---|
| `permit_type_definition` | Permit type (8 types; 92% are "otc alterations permit") |
| `filed_date` | When the application was filed, as text with a time |
| `issued_date` | When the permit was issued; 2,012 blank (not issued yet) |
| `completed_date` | When the work finished; 7,266 blank |
| `estimated_cost` | The applicant's estimated cost of the work; 158 blank |
| `existing_units` | Housing units before; 4,887 blank |
| `proposed_units` | Housing units after; 4,662 blank |

**Known problems:**
- 1,895 rows are exact copies of another row, down to the second on
  every timestamp.
- 3,003 permits list `estimated_cost` as exactly $1, a placeholder rather
  than a real estimate. 46 permits are $10 million or more; the largest
  is $400 million.
- Processing time isn't a column. You'll compute it from `filed_date`
  and `issued_date`.
- 7 permits show an issue date before the filed date.
- Over half of issued permits were issued the same day they were filed.

## Professional services: consulting engagements (synthetic)

Made for this project, with the kinds of problems real timesheet data
has.

| Column | What it holds |
|---|---|
| `project_id` | Unique ID |
| `service_type` | Audit, Tax Advisory, Litigation Support, or Strategy Consulting |
| `client_industry` | Client's industry |
| `partner_assigned` | One of 6 partners |
| `start_date` / `end_date` | Engagement dates; `end_date` blank for ongoing work |
| `billed_hours` | Total hours billed |

**Known problems:**
- 88 rows (4%) are missing `billed_hours`.
- 6 rows have negative hours, which are data-entry errors.
- 14 engagements have no `end_date` because they're still ongoing.
- `billed_hours` is right-skewed: the median is about 120 hours, and the
  largest engagement is over 5,000.
