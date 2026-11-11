---
name: deadline-planner
description: >-
  Turn sourced tasks and deadlines into a plan for today and the coming week,
  accounting for preparation time, dependencies, and available work sessions.
---

# Deadline Planner

Accept tasks from an inbox brief, documents, a task list, or the user's own
instructions. Preserve source links and unresolved facts. Establish a
reference time and timezone. Use supplied calendar availability; do not
assume an empty calendar when none has been provided.

Resolve updates before sorting. An authoritative extension supersedes the
old deadline. Mark completed and canceled work separately. An optional event
is not a required task unless the user plans to attend or register.

Distinguish three kinds of information:

- A deadline stated by the source, including its exact timezone/precision.
- A user-provided estimate of work, such as three study sessions.
- A suggested start time calculated or estimated by the planner.

Keep these labels visible. Do not turn a work estimate into a quoted course
requirement. If duration, timezone, or date is unclear, identify what needs
confirmation and offer only a conditional plan.

For a multi-session task, work backward through available sessions from its
deadline, allowing the user's requested buffer. Define whether the buffer
means calendar days or working days. Honor per-day capacity and dependencies.
If there are too few sessions, show the shortfall rather than silently
overbooking. Dates needed for preparation may fall before the report's week.

## Check progress before each daily plan

For multi-day work, read the latest user-confirmed progress before generating
the next morning's plan. Ask briefly: “Did you finish yesterday's step? If
not, what remains and how much time do you need?” Use done / partial / not
started / blocked / unknown, with confirmation time and source. If a fresh
update already exists, use it instead of asking again. Elapsed time, unread
messages, or silence do not establish completion.

Keep task and phase IDs, actual completion dates, dependencies, remaining
work estimates, availability, and the original hard deadline in a user-provided
or authorized local task record. Preserve a change log. If no persistent store
is available, return an updated record for the next run; do not claim memory.
The reference example is in references/progress-example.md.

When completion is confirmed early, advance the next unfinished phase to the
next available work session. If delayed, recalculate remaining internal dates
from the remaining estimate and capacity, respecting dependencies and buffers.
Do not blindly shift every phase by the same number of days. Report which
phase changed, why, and the new suggested dates. Never move an external hard
deadline unless an authoritative update changes it. If work no longer fits,
show the shortfall and ask the user to choose scope, capacity, or an extension
request; do not silently assume more hours or grant an extension.

If no confirmation arrives by the report time, mark yesterday's status unknown
and provide a conditional plan. Do not default to completed or overdue. A host
can collect an early check-in before the daily report if configured; this skill
does not itself schedule or send questions. Calendar writes remain separate
from updating the proposed plan and require the user's request.

Summarize what is due today, what is due soon, what needs starting now, and
what requires clarification. State the next concrete step and why it belongs
there. Rank by the user's goals and consequences as well as date; avoid
inventing a universal numerical importance score.

Include a small "later" section for large tasks beyond the next seven days
when their start window is already approaching. Do not equate the next seven
days with a calendar week without labeling the window.

The output is a proposed plan. Creating reminders, updating a task service,
or editing a calendar requires the user's request. A skill does not schedule
itself to run every day; use a separately configured scheduler if requested.
