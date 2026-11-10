---
name: project-handoff
description: >-
  Create or refresh an evidence-based handoff for resuming a project in a
  later session or with a collaborator. Use when the user asks to preserve
  project state, prepare a handoff, or recover the next steps from project
  files and available history.
---

# Project handoff

Produce a concise, portable account of the project's state and a practical
starting point for its next session. This is a snapshot, not persistent model
memory or a guarantee that the next agent will read it automatically.

## Identify the project

Use the root and scope specified by the user. If several repositories could
match, resolve the target before inspecting unrelated projects. Distinguish
course submissions from related research repositories. Respect the user's
chosen destination and audience for the handoff.

## Inspect evidence

Start with project instructions, its README, any existing handoff, and the
files relevant to the current task. When available, read Git status, current
branch, recent commits, and the relevant diff. Avoid dumping full histories
or entire datasets. Git is optional; absence of Git does not prevent a useful
handoff. If access fails, state which evidence could not be checked.

Use conversation and user statements as attributed context, not proof that
files were changed, checks passed, or remote submissions succeeded. A stale
README may conflict with newer files; state the conflict and evidence dates.
Local tracking refs alone do not establish current remote synchronization.

Distinguish:

- planned work;
- implemented work visible in files;
- executed work supported by a run or log;
- verified results supported by a specific check;
- submitted or published work confirmed at the relevant destination.

A clean Git tree proves none of the last three by itself. An old generated
report may not match the current source. Mention these issues when relevant.

## Prepare a useful restart

Use [the template](assets/handoff-template.md), omitting irrelevant sections.
Keep the main handoff brief; link to detailed notes instead of copying them.
Record the purpose, important decisions and their reasons, supporting files,
unresolved questions, and the first concrete action for the next session.
Include only commands grounded in inspected configuration or known runs.
Label untested commands as proposed and identify their working directory.

For coursework, identify the current assignment/rubric source when available.
Do not infer next year's deadlines or AI rules from a past semester. Record
open scientific decisions without choosing an answer just to complete a note.

Prefer project-relative file paths inside the handoff. Describe local data
requirements without copying private data, credentials, or personal chats.
If sharing scope is unclear, prepare a local draft; creating a handoff does
not authorize a commit, upload, message, or invitation.

## Save and check

If the user requests a saved handoff, use their destination or a plainly
named file such as HANDOFF.md under the confirmed project root. Read an
existing file before editing it; preserve still-relevant decisions and flag
superseded statements. Do not change project code or configuration merely
to write the handoff.

Check referenced paths, status labels, and the proposed restart action.
State what was inspected and what remains unverified. Tell the user to give
the next collaborator or chat the handoff file and access to its referenced
materials; the note alone cannot recreate missing files or dependencies.
