---
name: notion-sync
description: "Two-way bridge between the repo and AC's Notion To Do and Ideas boards: triage new ideas, push approved actions to To Do, and pull long-running or record-tagged to-dos back into records. Use when: notion sync, triage my ideas, push actions to notion, what's on my to do, check my notion, process my to-dos."
---

# Notion Sync

Read [`context/notion-boards.md`](../../../context/notion-boards.md) first. It lists the only two boards you may touch and the rules. **If the board links there are still "to add", stop and ask AC for them. Never search Notion to find them.**

## Flow 1 — Ideas Triage

1. Fetch the Ideas page (free-form bullets, not a database). Treat each line or short bullet group as one idea. **Skip ticked checkboxes** — they have been processed.
2. For each, sense-check against `context/role-brief.md`, `context/my-role/horizons.md`, and open records (the Idea Validator method): where does it fit, does it duplicate something, is now the time?
3. Propose one verdict per idea: **Park**, **Link → <record ID>**, **Promote → new improvement/challenge** (one-line objective and pillar), or **To Do** (proposed card title and Record tag).
4. After AC confirms: turn each processed line into a ticked checkbox with a suffix (`→ IMP-04`, `→ To Do`, `→ parked`) — change nothing else on the page; append one row per idea to `state/ideas-log.md`; for Link, add a dated line to the record; for Promote, hand to Capture; for To Do, create the card (Flow 2).

## Flow 2 — Actions Out

1. Gather candidate actions: from the action-extraction skill, a record's next action, or what AC asks for.
2. Propose cards with a short, plain, verb-first title (no bracket prefix) and the record ID in the `Record` property (add the option if it's a new record), with a due date only if AC gave one.
3. Create them in To Do only after AC approves the list.

## Flow 3 — To Do Back In

1. Query the To-Do data source for cards that are open (Backlog, To Do, Do Now) or were completed in the last 7 days. For tracked cards (below), also fetch the card body — AC may keep detail there rather than in the title.
2. Split them:
   - **Weekly churn:** untagged cards opened and closed within the week. Report a count and a one-line flavour only.
   - **Tracked:** cards tagged with a record ID, or open for more than 14 days.
3. For tracked cards, propose: progress or blocker lines for the matching record; a possible achievement if a meaningful outcome completed (ask before logging); a nudge if a card has been open for a long time with no movement.
4. Apply repo changes only after AC confirms; they follow the normal show-then-commit rule.

## Flow 4 — Roadmap Coverage And Snapshot

1. For every CII in the Now or Next horizon, find its first-up roadmap steps (`doing`/`next`). Each AC-owned first-up step should have an open To Do card tagged with the record ID. Propose cards for any that are missing (Flow 2); steps owned by others are reported as "waiting on", not carded.
2. Write `reports/notion-snapshot.json` for the dashboard (no approval needed — it's a generated, git-ignored file):
   `{"generated": "YYYY-MM-DD", "cards": [{"title", "status", "records": [...], "created", "due"}], "ideas": {"untriaged": n, "processedTicked": n, "lastTriage": "YYYY-MM-DD" | null}}`
   Include open cards and cards completed in the last 7 days. Convert any real names in titles to aliases. Count Ideas lines that are not ticked as `untriaged`.

## Output

- **Ideas:** table of idea → proposed verdict → reason.
- **Actions out:** list of proposed cards.
- **To Do back in:** churn count; tracked cards with proposed record updates; long-open cards.
- **Not recorded:** anything stripped under the people-records standard.

## Rules

- Only the two boards in `context/notion-boards.md`. No search, no browsing, no other pages.
- Show every Notion write before making it.
- Aliases only in anything written to Notion or the repo.
