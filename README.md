# ids-f26

Student-developed collaborative notes for the Fall 2026 Introduction to Data
Science course.

These notes supplement the instructor-authored `ids-book`. They are a place
for students to share worked examples, alternative explanations,
Python demonstrations, visualizations, debugging notes, applications, and
other insights from the semester. Link to relevant material in `ids-book`
rather than duplicating substantial instructor-authored content.

Private graded assignments and assessment materials belong in the designated
Classroom 50 repositories, not in this repository.

## Contributing

Use a topic branch for each focused contribution. Make small, coherent
commits, push the branch, and open a pull request. Revise the contribution in
response to review before it is merged.

A contribution should generally include:

1. **What:** a concise explanation of the concept.
2. **Example:** preferably an executable Python demonstration.
3. **Interpretation:** an explanation of what the result means.
4. **Takeaway:** one or two central conclusions.
5. **Sources:** citations or links for material used.

Keep examples minimal and reproducible. Use explicit imports, document data
sources and new dependencies, set random seeds when appropriate, and verify
that Quarto files render successfully. Do not commit generated output, cache
files, credentials, sensitive student information, or copied material without
proper attribution.

## Commit Messages

Make each commit a coherent change. Use an imperative, concise subject without
a trailing period, preferably no longer than 72 characters. Commit messages
follow this format:

```text
type: concise imperative summary
```

Use these types:

- `content`: add or revise notes, examples, exercises, or explanations
- `feat`: add a structural or reader-facing capability
- `fix`: correct an error or broken behavior
- `build`: change Quarto, Python, dependency, or build configuration
- `style`: make formatting-only changes
- `refactor`: reorganize source without materially changing content
- `docs`: update repository or contribution documentation
- `chore`: perform repository maintenance

For example:

```text
content: add example of reshaping data
fix: correct axis labels in scatterplot
build: add pandas to the Python environment
docs: clarify pull request workflow
```

Add a commit body when the motivation or a non-obvious decision needs further
explanation. Reference a related issue in the body when applicable.

## Review

Review emphasizes technical correctness, reproducibility, clarity,
attribution, and constructive revision while preserving the contributor's
authorship. Editorial acceptance and course assessment are separate
decisions; a contribution does not have to be merged to receive credit.
