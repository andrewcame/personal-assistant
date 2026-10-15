---
name: notion-sync
description: "Two-way bridge between the repo and AC's Notion To Do and Ideas boards: triage new ideas, push approved actions to To Do, and pull long-running or record-tagged to-dos back into records. Use when: notion sync, triage my ideas, push actions to notion, what's on my to do, check my notion, process my to-dos."
---

# Notion Sync

Read [`context/notion-boards.md`](../../../context/notion-boards.md) first. It lists the only two boards you may touch and the rules. **If the board links there are still "to add", stop and ask AC for them. Never search Notion to find them.**

## Flow 1 — Ideas Triage

1. Fetch the Ideas page (a free-form page of bullets, not a database). Treat each top-level bullet or block as one idea; skip any already marked with a verdict.
2. For each, sense-check against `context/role-brief.md`, `context/my-role/horizons.md`, and open records (the Idea Validator method): where does it fit, does it duplicate something, is now the time?
3. Propose one verdict per idea: **Park**, **Link → <record ID>**, or **Promote → new improvement/challenge** (with a one-line objective and pillar).
4. After AC confirms: write the verdict and record ID back to each card; for Link, add a dated line to the record; for Promote, hand to Capture to open the record.

## Flow 2 — Actions Out

1. Gather candidate actions: from the action-extraction skill, a record's next action, or what AC asks for.
2. Propose cards as `<verb-first action>` with the record ID in the `Record`/`Multi-select` property (or `[<ID>]` at the end of the title until that is set up), keeping AC's category-prefix style, with a due date only if AC gave one.
3. Create them in To Do only after AC approves the list.

## Flow 3 — To Do Back In

1. Fetch To Do cards that are open, or were completed in the last 7 days.
2. Split them:
   - **Weekly churn:** untagged cards opened and closed within the week. Report a count and a one-line flavour only.
   - **Tracked:** cards tagged with a record ID, or open for more than 14 days.
3. For tracked cards, propose: progress or blocker lines for the matching record; a possible achievement if a meaningful outcome completed (ask before logging); a nudge if a card has been open for a long time with no movement.
4. Apply repo changes only after AC confirms; they follow the normal show-then-commit rule.

## Output

- **Ideas:** table of idea → proposed verdict → reason.
- **Actions out:** list of proposed cards.
- **To Do back in:** churn count; tracked cards with proposed record updates; long-open cards.
- **Not recorded:** anything stripped under the people-records standard.

## Rules

- Only the two boards in `context/notion-boards.md`. No search, no browsing, no other pages.
- Show every Notion write before making it.
- Aliases only in anything written to Notion or the repo.
