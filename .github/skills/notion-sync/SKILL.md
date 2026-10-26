---
name: notion-sync
description: "Two-way bridge between the repo and AC's Notion To Do and Ideas boards: triage new ideas, push approved actions to To Do, pull long-running or record-tagged to-dos back into records, and tidy To Do cards against the repo (move finished cards to Done, add Record tags). Use when: notion sync, triage my ideas, push actions to notion, what's on my to do, check my notion, process my to-dos, tidy my cards."
---

# Notion Sync

Read [`context/notion-boards.md`](../../../context/notion-boards.md) first. It lists the only two boards you may touch and the rules. **If the board links there are still "to add", stop and ask AC for them. Never search Notion to find them.**

## Run Modes

- **Full run (Friday, or when asked):** all five flows below.
- **Light run (Monday and Wednesday scheduled jobs, or "light notion sync"):** read the To Do board and the Ideas page once, then do **Flow 4 only**: write `reports/notion-snapshot.json` (this is what keeps the dashboards' Focus fresh), then rebuild both dashboards. Report only: how many cards are open, any AC-owned next step with no card (propose it, don't create it), any card that looks done, and the count of untriaged ideas. Do **not** triage ideas or tidy cards (Flows 1, 3 and 5) in a light run; leave that for Friday. Same approval rules: no Notion writes, no commits.

## Flow 1 — Ideas Triage

### Reading the page

- The Ideas page is free-form. **Indentation carries meaning:** a top-level bullet is a topic; its sub-bullets (and their sub-bullets) drill into that topic — detail, options, questions, examples, or reasons. Treat a top-level bullet **and all its descendants as one idea group**, never as separate new ideas. Read the children in the context of their parent (e.g. "Use AI" under "How do we accelerate delivery of Appium" means *use AI to accelerate Appium*).
- A group can still touch more than one record — e.g. a "Web" topic whose children cover member creation, cross-country Portal tests, and accessibility. Map each child to the record it informs, but present them together under the parent.
- **Skip ticked checkboxes** — those groups have been processed. A group counts as processed when its top-level line is ticked.

### Triage: enrich, don't just match

"We already have a record for this" is a starting point, not a verdict. For every idea group:

1. Find the related records (`context/role-brief.md`, `context/my-role/horizons.md`, open CIIs, roadmaps, Notion To Do).
2. **Extract what the idea adds** that the record doesn't already say: a new question to explore, an option or approach, a risk, a scope detail, a dependency, a metric, a stakeholder, an example, or a concrete next step. Compare against the record's text and roadmap so you only propose what is genuinely new.
3. Propose one verdict per group (children may carry their own where they map elsewhere):
   - **Enrich → <record ID>** — the idea is covered, *and* here is what to add: list each addition and where it goes (Questions To Explore, a roadmap step, Initial Position, a dated update, or a To Do card). Use this whenever there is anything worth adding.
   - **Covered → <record ID>** — already fully captured; nothing new. Say briefly why, so AC can disagree.
   - **Promote → new challenge/improvement** — one-line objective and pillar.
   - **To Do** — proposed card title and Record tag.
   - **Park** — not now; say what would make it relevant.
4. Keep AC's intent and wording where it carries meaning; tidy only for clarity. Real names become aliases in anything written to the repo.

### After AC confirms

- For **Enrich**: apply the additions to the records (dated, with `updated:` bumped), add or adjust roadmap steps, and propose any resulting To Do cards (Flow 2).
- For **Promote**: hand to Capture to open the record. For **To Do**: create the card (Flow 2).
- Turn the **top-level line** of each processed group into a ticked checkbox with a suffix listing every record it fed, e.g. `→ IMP-02, INI-01` · `→ To Do` · `→ parked` · `→ covered (CH-10)`. Leave the sub-bullets nested underneath, unchanged. Change nothing else on the page.
- Append one row per group to `state/ideas-log.md`, including a short note of what was added to each record.

## Flow 2 — Actions Out

1. Gather candidate actions: from the action-extraction skill, a record's next action, or what AC asks for.
2. Propose cards with a short, plain, verb-first title (no bracket prefix) and the record ID in the `Record` property (add the option if it's a new record), with a due date only if AC gave one.
3. Create them in To Do only after AC approves the list.
4. **Always set `To-Do Completion` on every card you create:** `["https://app.notion.com/45cea035c7f183fc9462817b8425947b"]` (the same value cards created in the Notion UI get). Every view on the board filters on this relation, so a card without it is invisible to AC, and the Backlog column disappears if its only cards lack it. Set `Status` explicitly too. Don't read or edit the To-Do Completion database itself.
5. After creating cards, confirm none are missing the relation: query the data source for rows where `To-Do Completion` is null (expect none).

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
   `{"generated": "YYYY-MM-DD", "cards": [{"title", "status", "records": [...], "created", "due", "url"}], "ideas": {"untriaged": n, "processedTicked": n, "lastTriage": "YYYY-MM-DD" | null}}`
   `url` is the card's Notion page URL (optional; the dashboard links each Focus to-do to it). The dashboard's Focus lists open To Do / Do Now cards by their `records` tags, with initiative tags rolling up into the challenge or improvement they deliver.
   Include open cards and cards completed in the last 7 days. Convert any real names in titles to aliases (snapshot only; leave the Notion titles as they are). Count Ideas lines that are not ticked as `untriaged`.
3. Rebuild the dashboards (`python scripts/report.py`, `python scripts/people_report.py`). Don't open the output; see [dashboards.md](../../../ways-of-working/dashboards.md) for what each panel reads.

## Flow 5 — Card Tidy

Review the open cards (Backlog, To Do, Do Now) against the repo and propose tidy-ups. Run it after Flow 3 and before Flow 4, so the snapshot reflects the tidied board. Reading a card's body and comments is allowed (same card, no links followed); never open other pages.

For each open card, look for:

1. **Done in the repo, still open in Notion** — the matching roadmap step is `done`, or a record, progress log, achievement or `state/now.md` says it is finished. Read the card's body and comments first for anything pertinent (a blocker, a follow-up, a change of plan). If nothing contradicts it, propose **move to Done**; if a comment raises a follow-up, propose that as a new card or roadmap step instead.
2. **Done in Notion, repo not updated** — a Done card whose roadmap step is still `doing`/`next`: propose marking the step `done` (and the next step `doing`/`next` if it is now unblocked).
3. **Missing `Record` tag** — an untagged card that clearly relates to one record (title, body, or a matching roadmap step): propose the tag, and say which step it matches. Add the option first if the record is new. Quick untagged reminders that match nothing stay untagged.
4. **Wrong or stale tag** — a tag whose record is resolved, closed or dropped, or a card whose step was dropped: propose retagging, moving to Done, or deleting. Never delete without explicit approval.
5. **Duplicates and drift** — two cards for the same step, or a card whose title no longer matches the step wording: propose merging or renaming (short, plain, verb-first, no bracket prefix).
6. **Status mismatch** — a Do Now card for a `later` step, or a `doing` step whose card sits in Backlog: propose the status change.

7. **Missing relation** — any card (open or Done) whose `To-Do Completion` is empty: it is hidden from every view. Propose setting it (value in Flow 2, step 4). Check this first on every run.
8. **Fortnightly Done clear-out** — a Done card that has not been edited for 14 days or more. Before proposing it, make sure its outcome is already in the matching record or achievement (Flow 3). Then propose archiving all such cards in one batch (move to Trash, restorable); never archive without AC's approval. Run this on the first sync of each fortnight (record the date of the last clear-out in `state/now.md`, under Open Threads, as "To Do Done clear-out: last YYYY-MM-DD"). Cards that fed an open record's progress line stay until that line is written.

Present one table (Card · Current status/tags · Evidence from the repo · Proposed change). Apply only the changes AC approves, one write at a time, and show each before making it. Repo changes that follow (marking steps done, new steps) go through the normal show-then-commit rule.

## Output

- **Ideas:** one block per idea group (top-level line, with its sub-bullets summarised) → verdict → for Enrich, each proposed addition and the record/section it goes into.
- **Actions out:** list of proposed cards.
- **To Do back in:** churn count; tracked cards with proposed record updates; long-open cards.
- **Card tidy:** the table of proposed moves to Done, new tags, retags, merges, missing relations and the fortnightly Done clear-out, with the repo evidence for each.
- **Not recorded:** anything stripped under the people-records standard.

## Rules

- Only the two boards in `context/notion-boards.md`. No search, no browsing, no other pages.
- Show every Notion write before making it.
- Card status moves and deletions are never made without AC's approval; check the card's body and comments before proposing Done.
- Aliases only in the repo (records, snapshot, `state/`). Notion card titles are AC's own text: don't rewrite real names there; convert them to aliases only when copying into the repo.
