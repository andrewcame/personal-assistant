# Reviews

This folder is for review-specific working notes and writeups.

Use it to keep the path from raw achievements to review-ready text simple:

- midyear checkpoint drafts
- end-of-year review summaries combining goals, achievements, and values

Suggested pattern:

1. Keep goals in `goals/`.
2. Log achievements in `achievements/`.
3. Map each achievement back to a goal, supported objective lens, then to a core value or review theme.
4. Draft the final review writeup here when needed.

Use the [Review Writer agent](../.github/agents/review-writer.agent.md) to map evidence to goals, lenses, and values, and to turn it into the actual review text.

## Team Reviews And Calibration

For the QA team's end-of-year cycle (calibration session 2026-11-11; reviews completed by 31 December):

1. Through the year, add dated evidence to each person's **Year-End Evidence** section in `team/<alias>.md`.
2. Before calibration, run the **calibration-prep** skill: it drafts each person's Top 3 WHAT, Top 3 HOW, development areas, and a suggested matrix position — **in chat only**.
3. Type ratings, flight risk, succession, and PDP/PIP fields straight into the People team's template. They are never stored in this repo ([why](../team/README.md#writing-standard)).
4. After calibration, use the Review Writer agent with the agreed outcome to draft each review conversation, spending as much time on development as on looking back.

Process and matrix reference: [context/performance-calibration.md](../context/performance-calibration.md).

