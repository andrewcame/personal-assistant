---
name: check-card-status
description: "On-demand audit and clean-up of every task against every challenge and improvement: lists each roadmap step and Notion card by record, flags what is out of step (missing, untracked, wrong column, stale, duplicate, unmapped), and works through the fixes with AC. Use when: check card status, card check, tidy my cards, clean up the board, list every task per challenge and improvement, audit Notion against the roadmaps."
---

# Check Card Status

The full, interactive version of the card tidy. [notion-sync](../notion-sync/SKILL.md) keeps Notion and the roadmaps aligned on a schedule (light on Monday and Wednesday, full on Friday). Use this skill when AC wants to **see everything and clean up in one sitting**.

Rules that apply throughout: only the two boards in `context/notion-boards.md` (fetch by link or ID, never search Notion); aliases only in the repo; commits need AC's OK. Fixes the checks find on their own (create a missing first card, adopt an untracked card, fix a column, add a `Card` title) are applied directly and listed afterwards. Anything that closes, drops, deletes or archives happens only when AC tells you to in the review; his instruction is the approval.

## Inputs

1. The live To Do board, read once (open cards and Done cards). Use the data source in `context/notion-boards.md`.
2. `python scripts/report.py --tasks` after the snapshot is refreshed (every open roadmap step per record, its owner, status and Notion state). Never open `reports/*.html` or `reports/*.json`.
3. Each live record's `horizon:` and status (front-matter) and its roadmap, for the checks below.

## Method

1. **Refresh the snapshot.** Read the board, apply notion-sync Flow 4 (adopt untracked tagged cards into roadmaps, create any missing first-up card) and Flow 6 (a card AC has moved to Done), write `reports/notion-snapshot.json`, and rebuild the dashboards. Convert real names in titles to aliases in the snapshot only.
2. **List everything.** Present one block per live record, ordered Now, Next, Later: `ID tag · title · horizon · status`, then a table of every open task: step ID, step, owner, step status, card title, Notion column. Include open cards that no step names, and cards tagged to closed or retired records.
3. **Flag, using these checks** (a card or step can carry more than one flag):
   - **Needs card** — a Now or Next record's first-up step (`doing`/`next`) with no open card. Later records need none until AC moves them to Next.
   - **Untracked** — an open card tagged to a record that no step names. Fix: adopt it as a step.
   - **Card done, step open** — a Done card whose step is not `done` (Flow 6).
   - **Wrong column** — a card for a Now record's step in `Backlog`, or for a Next or Later record's step in `To Do`. "To Do" means in progress.
   - **Wrong or stale tag** — tagged to a closed, dropped or retired (INI-) record, or a tag that doesn't match the step.
   - **Unmapped** — no `Record` value, or only `Admin`. Fine for BAU; ask whether any belongs to a record.
   - **Stale** — in To Do (not Backlog) more than 14 days with no movement (use `created` from the snapshot).
   - **Duplicate or drift** — two cards for the same step, or a title that no longer matches its step.
   - **Naming** — a card for someone else's step not titled "Monitor …", an internal step ID in a title, a `[CATEGORY]` prefix.
   - **Overloaded** — a record with many To Do cards. Not an error (AC adds cards as he thinks of them); just show the count.
   - **Cap** — more than 8 records in Now (`check.py` warns).
4. **Summarise** at the top: counts per flag, then the table of flagged items only (Record · Card or step · Flag · Proposed fix).
5. **Review with AC, and apply each decision to both sides.** This is an alignment skill: whenever AC makes a call in the review ("close this", "open this", "drop that", "rename it", "move it to Now"), change the **roadmap and Notion together** so they never diverge. AC's instruction in the review is the approval, including for archiving and moving to Done. Group related fixes and ask one question per ambiguous item. Don't archive, delete or close anything AC hasn't told you to.

   | AC says | Roadmap (repo) | Notion |
   |---|---|---|
   | Close this / it's done | Step `done`, dated progress line naming the card | Card moved to `Done`; then create the card for the next step (see below) |
   | Open this / add this | New step (next free number, never renumber), status `next` or `doing` | New card, `To Do` for a Now record, `Backlog` for Next; title in the step's `Card` column |
   | Drop this / not needed | Step `dropped` (keep the row) | Card archived (Trash, restorable) |
   | Adopt this card | New step from the card, `Card` = exact title | Card unchanged (add the `Record` tag if missing) |
   | Rename / reword | Step text and `Card` column updated to match | Card renamed |
   | Retag / move to another record | Step moved: dropped on the old record, new step on the new one | `Record` tag changed |
   | Move to Now / Next | `horizon:` in the record and its `horizons.md` row | Card column fixed (`To Do` for Now, `Backlog` for Next); a Next promotion creates the first card |
   | Merge duplicates | One step kept, the other `dropped` | One card kept, the other archived |
   | Leave it | No change | No change |

   After a **close**, create the next card: promote the next step in the roadmap to `next` or `doing` if it is `later`, create its card, and put the title in `Card`. If no steps remain, ask the Capture close-out question (achievement, evidence, both or neither) instead of closing the record yourself.
6. **Verify the alignment.** Run `python scripts/check.py all` and both report scripts, re-read the changed cards (or the board) so the snapshot matches Notion, then re-run `python scripts/report.py --tasks`. Every open step should show its card, every tagged card a step, and no flags remain; list anything that does and why.

## Output

- **Everything by record** (the list from step 2, compact).
- **Flags** (counts, then the flagged table).
- **Changes applied** (each decision, roadmap side and Notion side, one line each).
- **Waiting on AC** (open questions, and anything flagged that he hasn't decided yet).
- **Not recorded:** anything stripped under the people-records standard.

## Notes

- Suggested model: Sonnet-class.
- Related: notion-sync Flow 5 (the scheduled card tidy) uses the same checks; this skill is the on-demand, whole-board version.
- If the Notion connection needs signing in, say so and stop after producing the repo-side list from `report.py --tasks`; don't guess card state.
