---
name: weekly-review
description: "Run the end-of-week review: what moved, what went stale, which wins still need logging, and what the focus should be next week; then refresh state/now.md. Use when: weekly review, Friday review, what happened this week, review my week, update now.md, plan next week."
---

# Weekly Review

A short, repeatable end-of-week pass that keeps `state/now.md` honest and catches evidence before it's forgotten. Aim for something that takes the user five minutes to read and confirm.

## Inputs

1. `state/now.md` — last week's focus, threads, decisions, waiting-on
2. `context/role-brief.md` — grounding (open full sources only if needed)
3. `python scripts/check.py stale 7` and `python scripts/check.py validate` — if you cannot run commands, ask the user to run them and paste the output, or read front-matter `updated:` dates directly
4. What changed this week: `git log --since="7 days ago" --name-only` if available; otherwise records whose `updated:` falls in the last 7 days
5. `context/my-role/horizons.md` — the Now list

## Method

1. **Moved** — list records updated this week and what changed, in one line each.
2. **Last week's focus** — for each item in "This Week's Focus", say done / progressed / not touched, with evidence. Don't infer progress that isn't recorded; ask.
3. **Wins to log** — spot outcomes that look like achievements but have no entry in `achievements/<year>.md`. Ask the user to confirm each one before handing it to Capture. Never write an achievement from inference alone.
4. **Stale Now items** — any Now record not updated in 7+ days: ask whether it is genuinely active. If not, propose moving it to Next.
5. **Next week** — propose up to three focus items, anchored on the Now horizon. If leadership direction or a stuck challenge argues for something else, say why.
6. **Housekeeping** — list any `validate` errors, and anything flagged by `stale` that isn't in Now (one line each, no essay).

## Output

- **Moved this week** · **Last week's focus: outcome** · **Wins to log (confirm?)** · **Stale Now items** · **Proposed focus for next week** · **Housekeeping**
- Then a proposed new `state/now.md`, shown in full.

## Writing Rules

- Only write `state/now.md` after the user confirms. Set **Updated:** to today.
- Keep `state/now.md` to one screen: drop resolved threads, move decisions older than ~4 weeks out (they live in their records), and keep "Recent Decisions" to the last five.
- Achievements, challenge updates, and status changes go through Capture (or the Capture rules) — not this skill.
- Aliases only. The user may speak candidly about people; use it as context, but anything written to `state/now.md` or handed to Capture follows the [people-records standard](../../../team/README.md#writing-standard) — say what was left out.
