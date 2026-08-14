# Choose Your Domain

Pick **one** of the four business domains below. Each gives you a real
stakeholder, a real business problem, and its own data file — but
everyone works from the **same starter notebook** (`starter/analysis.ipynb`)
and the **same bar** (`MVP.md`). The domain changes what you're looking at
and why; it doesn't change what's required of you.

## Option 1: Finance & Insurance

**Stakeholder:** A FEMA National Flood Insurance Program analyst.

> "We need to understand what actually happened in the 2015 South Carolina
> flood season — which counties and property types saw the most severe
> claims, and whether the numbers we'd use to plan next year's reserve fund
> are actually defensible, or quietly distorted by a handful of
> catastrophic claims."

**Business problem:** Characterize claim-payout severity and figure out
which figure — mean or median — leadership should actually trust when
planning reserves.

**Data:** `data/finance_insurance.csv`

## Option 2: Healthcare Operations

**Stakeholder:** A hospital-quality policy analyst reviewing public CMS
data.

> "Emergency departments across the country report wildly different wait
> times for psychiatric patients before they're seen. I need to know what
> 'typical' actually looks like, which hospitals are real outliers worth
> flagging, and whether this data is even clean enough to trust before we
> put a number in a public report."

**Business problem:** Characterize ED wait-time patterns across hospitals/
states, and decide how to handle a metric that isn't cleanly numeric to
start with.

**Data:** `data/healthcare_operations.csv`

## Option 3: Public Sector

**Stakeholder:** A San Francisco Department of Building Inspection program
manager.

> "People constantly ask how long a building permit actually takes and
> what it actually costs. I want a real answer — not an anecdote — and I
> want to know where the process is genuinely slow versus where a handful
> of huge, unusual projects are skewing the story."

**Business problem:** Characterize permit processing time and cost, and
identify what's driving any skew.

**Data:** `data/public_sector.csv`

## Option 4: Professional Services

**Stakeholder:** A managing partner at a consulting firm.

> "I want to understand how billed hours actually break down across our
> service lines and partners before we make staffing decisions next
> quarter — and I'm worried our timesheet data has real gaps and errors
> that could throw off the numbers if nobody catches them first."

**Business problem:** Characterize billed-hours patterns across service
lines, and catch real data-quality problems before they reach a staffing
decision.

**Data:** `data/professional_services.csv` (see `data/SOURCE.md` — this
one is clearly-labeled synthetic data, not real client records)

## What to do with this

Before writing any code: read your stakeholder's actual words again, and
open `data/SOURCE.md` for your chosen file's real column list and known
data-quality wrinkles — nothing is decoded or pre-cleaned for you. See
`MVP.md` for the full bar and `README.md` for where to start.
