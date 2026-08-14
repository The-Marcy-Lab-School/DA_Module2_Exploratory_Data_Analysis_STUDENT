# Choose Your Scenario

Pick **one** of the four stakeholders below. Each one asks a real question
about the *same* dataset (`data/meteorite_landings.csv`) — your job is
answering **their specific question**, not just profiling the dataset in
general. Whichever you pick, name it clearly at the top of `starter/memo.md`
so it's obvious which question you're answering.

## Option 1: The Museum Curator

**Stakeholder:** Elena, curator planning a new meteorite exhibit.

> "I want to build a case for which classifications are worth chasing for
> acquisitions — I need to know which meteorite classes tend to produce
> the most exceptional specimens, not just the biggest single rock we
> happen to have on record."

**Question to answer:** Which classification (`recclass`) has produced the
most exceptionally massive specimens, and how does that compare to a
*typical* specimen in that same class?

## Option 2: The Planetary Scientist

**Stakeholder:** Dr. Osei, researching how meteorite discovery has changed
over time.

> "Meteorite science didn't stop in 1950. I want to know whether the
> *pattern* of discovery has actually shifted over the decades — and if it
> has, what that shift might actually mean, not just that a chart goes up."

**Question to answer:** Has the rate and pattern of meteorite discovery
changed by decade, and what might explain any real change you find?

## Option 3: The Program Historian

**Stakeholder:** Marcus, writing about how this dataset itself came to
exist.

> "Half of what's in a dataset like this is really a story about *how* it
> got collected, not just what it describes. I want to understand how
> witnessed falls and later-discovered specimens actually differ — and
> what that difference tells us about the collection process itself."

**Question to answer:** How does mass differ between meteorites that were
witnessed falling (`fall`) vs. found later, and what does that gap suggest
about how this dataset was actually built?

## Option 4: The Geodata Quality Auditor

**Stakeholder:** Priya, deciding whether this dataset's location data is
trustworthy enough to feed into a new mapping tool.

> "Before anyone plots a single point from this data on a real map, I need
> to know how much of the location data can actually be trusted — and what
> a placeholder value looks like versus a real reading, specifically."

**Question to answer:** How much of this dataset's location data
(`reclat`/`reclong`) can actually be trusted, and what patterns suggest a
placeholder rather than a real recorded location?

## What to do with this

Before writing any code: read your stakeholder's actual words again. Your
whole notebook — the variables you profile, the pandas/Polars code you
write, the chart you generate and get an AI's read on — should build toward
**answering their specific question with real evidence**, not just
producing a generic profile of the dataset. See `MVP.md` for the full bar
and `README.md` for where to start.
