# Hacker News retrieval notes

Current classroom entry: https://news.ycombinator.com/best?h=24
Checked November 9, 2026. The page labels itself most-upvoted stories of the
last 24 hours. It includes all topics. Filter for AI, read linked sources,
and record the actual retrieval time, story IDs, points and comment counts.
Describe the HN pages and original sources actually checked.

Official API: https://github.com/HackerNews/API
Use item timestamps, score and descendants (comment count) when available.
Best-story ID lists are bounded snapshots, not a historical completeness
promise. Missing, deleted or inaccessible items remain retrieval gaps.

Optional search: https://hn.algolia.com/api
Source: https://github.com/algolia/hn-search
The source indexes created_at_i, points and num_comments. Consult current
API documentation and verify response fields before using numericFilters.
If available, use a fixed run timestamp and both lower and upper submission
time bounds; request stories and follow all returned pages within limits.
Record caps, failures and indexing limitations. A points>50 filter is an
optional selection threshold, not proof of complete coverage; do not default
to it. Old submissions receiving new comments are a separate query problem.
The API documentation page required JavaScript in the web reader; no Algolia
retrieval or live briefing was executed for these slides.

For five important AI stories, consider the substantive change, affected
users, relevance and community attention together. Votes and comments help
explain why an event deserves attention; inspect discussion for context.
Check original event dates, group duplicates and explain each inclusion.
Record metrics at retrieval time. Avoid rigid sorting by comments alone.

HN background: https://news.ycombinator.com/newsfaq.html
Use the community's link sharing, voting and discussion to introduce why it
is a useful discovery source. Professional expertise is not verified for
every contributor; describe technical discussion without assigning credentials.
