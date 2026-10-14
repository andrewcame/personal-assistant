---
name: horizon-review
description: "Monthly review of the Now / Next / Later plan: check each outcome against its records, propose moves between horizons, close finished items into achievements, and refresh the role brief. Use when: horizon review, review my plan, monthly review, what's in now, re-plan, move things between now and next, close out the plan."
---

# Horizon Review

Keeps `context/my-role/horizons.md` an accurate plan rather than a wish list. Run roughly monthly, or when priorities shift (e.g. a new leadership direction entry).

## Inputs

1. `context/my-role/horizons.md`
2. Front-matter of every record linked in the "Carried by" column (status, updated, horizon)
3. `python scripts/check.py stale` and `python scripts/check.py coverage` (or read front-matter directly if you cannot run commands)
4. `context/leadership-direction.md` — entries since the last review only
5. `state/now.md` and `context/role-brief.md`

## Method

1. **Reconcile** — for each outcome, compare the horizon file's status with the linked records' front-matter. Flag mismatches (e.g. horizon says In progress, record says not-started, or record `horizon:` disagrees with where the row sits).
2. **Done** — outcomes whose records are done: propose marking them Done and confirm there is an achievement entry; if not, ask the user for the outcome and hand it to Capture.
3. **Now** — keep it to five or fewer. For each Now item, ask "was this actively worked in the last two weeks?" Propose demoting anything that wasn't.
4. **Promote** — propose what moves from Next to Now to fill freed capacity, using the Decision Lens and the driving theme.
5. **New direction** — check new leadership direction entries: does anything add, remove, or re-order outcomes? Does the driving theme still hold?
6. **Orphans** — open records not linked from any horizon row: propose linking them, or confirm they're intentionally off-plan.
7. **Gaps** — note any blind spots from the coverage output that the plan doesn't address.
8. **Consolidate learnings** — for each line in `state/learnings.md` older than a month, propose moving it into the agent, skill, template, or `AGENTS.md` it belongs to, then retiring it from the learnings file. Flag any learning that has been contradicted in practice.

## Output

- **Mismatches** · **Done (and achievement check)** · **Proposed moves** (from → to, with reason) · **New direction impact** · **Orphans** · **Gaps**
- Then the proposed edits to `horizons.md`, `role-brief.md` (Now line), and record front-matter `horizon:` values.

## Rules

- Propose, then write only after the user confirms.
- Move rows rather than deleting them; Done rows stay with a link to the achievement.
- When a row moves, update the linked records' `horizon:` front-matter so `check.py index` stays consistent, and run `python scripts/check.py all` afterwards if you can.
- Bump **Last refreshed** in `role-brief.md` when its Now line changes.
