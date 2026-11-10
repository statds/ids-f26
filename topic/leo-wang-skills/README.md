# Agent Skills for Data Science

Leo Wang — November 16, 2026 topic presentation.

The main deck explains reusable agent instructions through code learning,
email-based planning, and an AI news brief. Supporting skills are examples
for explicit use, not automatically installed services.

## Files

- `index.qmd`: main presentation (19 slides).
- `backup.qmd`: Environment Doctor and Project Handoff examples (5 slides).
- `examples/`: skill instructions, references, and supporting files.
- `fixtures/`: synthetic emails, planning inputs, and a small handoff case.
- `scripts/`: executable calculations and diagnostic examples.

## Render

Use the shared course Python 3.12 environment and its Jupyter dependencies.
From the course repository root, render each deck separately:

```sh
quarto render topic/leo-wang-skills/index.qmd --profile presentations
```

```sh
quarto render topic/leo-wang-skills/backup.qmd --profile presentations
```

The equivalent `make render-one FILE=...` commands use the same profile.
Open `_book/topic/leo-wang-skills/index.html`. The profile copies linked
example and fixture resources. Generated HTML and caches stay uncommitted.

## Inputs and validation

The inbox contains seven simulated messages. E7 uses real CSAS 2027 event
information linked in the slides; it is not a received organizer email.
The planning reference time is Nov 16, 2026, at 9 a.m. in New York.
CSAS preparation windows and progress scenarios are suggested teaching cases.
The December 1 abstract deadline comes from the event website.

The Python examples check arithmetic, an empty selection, phase dates,
calendar capacity, isolated environments, and changed handoff source files.
Earlier explicit Learning Coach and mail/planning skill tests informed the
examples. Revised progress scenarios are designed acceptance cases; no new
independent agent test or deployed daily check-in service is claimed.
The news example describes a Hacker News workflow; no live news feed,
mailbox connection, or daily delivery is configured by rendering this deck.

## AI assistance

OpenAI Codex helped draft the slides and example skills, write supporting
code, and check results. Leo reviewed and revised the presentation.
