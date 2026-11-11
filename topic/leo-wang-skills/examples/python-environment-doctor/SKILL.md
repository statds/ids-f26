---
name: python-environment-doctor
description: >-
  Diagnose Python interpreter, package, notebook, and Quarto environment
  mismatches from a student's error and runtime evidence. Use for import or
  environment failures before proposing installation or configuration
  changes.
---

# Python environment doctor

Find the smallest evidence-supported correction. Distinguish diagnosis,
proposed repair, and a verified repair. A working interpreter is not proof
that the entire analysis is correct.

## Establish the failing context

Use the error, command, working directory, and whether the failure occurred
in a terminal, notebook, editor, or Quarto render. Ask for missing information
only when it changes the diagnosis. Avoid collecting broad environment dumps,
credentials, or unrelated configuration.

Inspect the project's documented environment before suggesting a new one.
Do not assume a Python version, shell, or student's personal paths.

## Check identity and availability

Run [inspect_env.py](scripts/inspect_env.py) with the interpreter that failed,
passing the top-level import names relevant to the error. The helper reports
interpreter identity and package discovery without importing those packages.
Discovery alone does not prove an import or native dependency will work.

Compare with the documented intended interpreter when it is available.
For notebooks, inspect the active kernel's sys.executable. For Quarto,
inspect its Python selection and kernel configuration as needed. Selecting
QUARTO_PYTHON alone does not prove a notebook kernel uses that interpreter.

If package state matters, use the selected interpreter's -m pip rather than
assuming a bare pip command targets it. An import failure can also arise from
a local file shadowing a package, missing binary dependencies, or an API
change; do not diagnose a missing package from every ImportError.

## Propose and verify the correction

Prefer selecting an existing intended interpreter when that resolves the
mismatch. If installation is actually needed, follow the current project's
dependency instructions and explain which environment would change.
Do not alter global settings or PowerShell execution policy as a first fix.
An absolute interpreter path can run Python without shell activation.

Use a minimal relevant import or failing command to verify the proposed
repair when running it is within scope. Read project code before executing
an unfamiliar command. Report what succeeded and what remains untested.
Do not claim to have fixed the user's machine from simulated logs alone.

## Explain the result

State the likely cause with evidence, the smallest next action, and how the
student can confirm it. Keep commands separate and adapt quoting to their
shell. If evidence is inconclusive, give a targeted next diagnostic instead
of a list of reinstall commands.

Sources checked October 31, 2026:

- Python venv: https://docs.python.org/3/library/venv.html
- Quarto Python: https://quarto.org/docs/computations/python.html

This is a student-developed tool, not an official course environment policy.
