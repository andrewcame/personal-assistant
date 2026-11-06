---
name: notion-sync
description: "Two-way bridge between the repo and AC's Notion To Do and Ideas boards: triage new ideas, push approved actions to To Do, pull long-running or record-tagged to-dos back into records, and tidy To Do cards against the repo (move finished cards to Done, add Record tags). Use when: notion sync, triage my ideas, push actions to notion, what's on my to do, check my notion, process my to-dos, tidy my cards."
---

# Notion Sync

Read [`context/notion-boards.md`](../../../context/notion-boards.md) first. It lists the only two boards you may touch and the rules. **If the board links there are still "to add", stop and ask AC for them. Never search Notion to find them.**

## Run Modes

- **Full run (Friday, or when asked):** all six flows below.
- **Light run (Monday and Wednesday scheduled jobs, or "light notion sync"):** read the To Do board and the Ideas page once, then do **Flow 4 and Flow 6**: reconcile Notion with the roadmaps (adopt untracked tagged cards into roadmaps, create any missing first-up card), write `reports/notion-snapshot.json` (this is what keeps the dashboards' Focus fresh), apply Done reconciliation (Flow 6) to any card that has moved to Done, then rebuild both dashboards. Report only: how many cards are open, the roadmap changes and cards created (listed for AC's awareness), and the count of untriaged ideas. Do **not** triage ideas or tidy cards (Flows 1, 3 and 5) in a light run; leave that for Friday. No commits.

## Flow 1 — Ideas Triage

### Reading the page

- The Ideas page is free-form. **Indentation carries meaning:** a top-level bullet is a topic; its sub-bullets (and their sub-bullets) drill into that topic — detail, options, questions, examples, or reasons. Treat a top-level bullet **and all its descendants as one idea group**, never as separate new ideas. Read the children in the context of their parent (e.g. "Use AI" under "How do we accelerate delivery of Appium" means *use AI to accelerate Appium*).
- A group can still touch more than one record — e.g. a "Web" topic whose children cover member creation, cross-country Portal tests, and accessibility. Map each child to the record it informs, but present them together under the parent.
- **Skip ticked checkboxes** — those groups have been processed. A group counts as processed when its top-level line is ticked.

### Triage: enrich, don't just match

"We already have a record for this" is a starting point, not a verdict. For every idea group:

1. Find the related records (`context/my-role/horizons.md`, open CIIs, roadmaps, Notion To Do).
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
- Turn the **top-level line** of each processed group into a ticked checkbox with a suffix listing every record it fed, e.g. `→ IMP-02, CH-10` · `→ To Do` · `→ parked` · `→ covered (CH-10)`. Leave the sub-bullets nested underneath, unchanged. Change nothing else on the page.
- Append one row per group to `state/ideas-log.md`, including a short note of what was added to each record.

## Flow 2 — Actions Out

1. Gather candidate actions: from the action-extraction skill, a record's next action, or what AC asks for.
2. Propose cards with a short, plain, verb-first title (no bracket prefix) and the record in the `Record` property as `<ID> <tag>` (e.g. `IMP-02 Member data`; the tag is the record's `tag:` front-matter; add the option if it's a new record), with a due date only if AC gave one. Cards are only for challenges and improvements; Jira delivery is tracked in Jira and its tasks go against the parent record.
3. Create them directly, then list what was created for AC's awareness. **The card flow is a two-way street.** The agent creates the first card for a record's first-up step (a **Now** record's card goes in `To Do`; a **Next** record's in `Backlog`); when that card is Done, it creates the card for the next step (Flow 6). Records in **Later** get their first card when AC moves them to **Next** (and it moves from `Backlog` to `To Do` when they reach Now). AC can also add cards himself at any time (Flow 4 adopts them into the roadmap). After creating a card, put its exact title in the roadmap step's `Card` column.
4. **Always set `To-Do Completion` on every card you create:** `["https://app.notion.com/45cea035c7f183fc9462817b8425947b"]` (the same value cards created in the Notion UI get). Every view on the board filters on this relation, so a card without it is invisible to AC, and the Backlog column disappears if its only cards lack it. Set `Status` explicitly too. Don't read or edit the To-Do Completion database itself.
5. After creating cards, confirm none are missing the relation: query the data source for rows where `To-Do Completion` is null (expect none).

## Flow 3 — To Do Back In

1. Query the To-Do data source for cards that are open (Backlog, To Do) or were completed in the last 7 days. For tracked cards (below), also fetch the card body — AC may keep detail there rather than in the title.
2. Split them:
   - **Weekly churn:** untagged cards opened and closed within the week. Report a count and a one-line flavour only.
   - **Tracked:** cards tagged with a record ID, or in To Do for more than 14 days (Backlog cards are never flagged as long-open).
3. For tracked cards, propose: progress or blocker lines for the matching record; a possible achievement if a meaningful outcome completed (ask before logging); a nudge if a card has been open for a long time with no movement.
4. Apply repo changes only after AC confirms; they follow the normal show-then-commit rule.

## Flow 4 — Roadmap Coverage And Snapshot

1. **Reconcile Notion with the roadmaps, both ways.** Notion and the roadmaps must always align.
   - **Cards to roadmap (adopt).** For every open card whose `Record` value names a challenge or improvement but which no roadmap step names in its `Card` column, add a new roadmap step to that record (next free number, never renumber): Step = the card title reworded as a short verb-first outcome, Owner = AC (or the other person for a "Monitor X" card), Status = `doing` if the card is in `To Do`, `next` if in `Backlog`, `Card` = the exact card title. If it clearly is the same work as an existing step, set that step's `Card` instead of adding one. Apply directly and list afterwards. Do not adopt a card with no `Record` value or only `Admin`.
   - **Roadmap to cards (create).** For every CII in the Now or Next horizon, its first-up step (`doing`/`next`), whoever owns it, must have an open card, named in the step's `Card` column (exact title; the dashboard's Tasks section reads it). Create any missing card (Flow 2) and list it. Later steps need no card.
   - **Done cards.** A card that is Done while its step is not is handled by Flow 6.
   - Mapping rules:
     - A card maps to a CII only through its `Record` value, read by the ID at its start (`IMP-02 Member data` → `IMP-02`). No value, or only `Admin`, means the card is unmapped and does not tie to any CII.
     - `Admin` means BAU. It is the only category. Do not use "BAU" as a separate label.
     - A card for a step owned by someone else is titled "Monitor X", not "Do X".
     - Column rule: "To Do" means in progress. A card for a **Now** step sits in `To Do`; a card for a **Next** or **Later** step sits in `Backlog`. Fix any card in the wrong column (Flow 5, step 6).
2. Before overwriting the snapshot, read the old one: any card that was open there and is now Done is a Done transition, which feeds Flow 6. Then write `reports/notion-snapshot.json` for the dashboard (no approval needed — it's a generated, git-ignored file):
   `{"generated": "YYYY-MM-DD", "cards": [{"title", "status", "records": [...], "created", "due", "url"}], "ideas": {"untriaged": n, "processedTicked": n, "lastTriage": "YYYY-MM-DD" | null}}`
   `url` is the card's Notion page URL (optional; the dashboard links each Focus to-do to it). The dashboard's Focus lists open To Do cards by their `records` tags. Cards still tagged with a retired initiative ID (INI-01, INI-02) roll up into the parent record through a mapping in `scripts/report.py`; retag them to the parent when tidying.
   Include open cards and cards completed in the last 7 days. Convert any real names in titles to aliases (snapshot only; leave the Notion titles as they are). Count Ideas lines that are not ticked as `untriaged`.
3. Rebuild the dashboards (`python scripts/report.py`, `python scripts/people_report.py`). Don't open the output; see [dashboards.md](../../../ways-of-working/dashboards.md) for what each panel reads.

## Flow 5 — Card Tidy

Review the open cards (Backlog, To Do) against the repo and propose tidy-ups. Run it after Flow 3 and before Flow 4, so the snapshot reflects the tidied board. Reading a card's body and comments is allowed (same card, no links followed); never open other pages.

For each open card, look for:

1. **Done in the repo, still open in Notion** — the matching roadmap step is `done`, or a record, progress log, achievement or `state/now.md` says it is finished. Read the card's body and comments first for anything pertinent (a blocker, a follow-up, a change of plan). If nothing contradicts it, propose **move to Done**; if a comment raises a follow-up, propose that as a new card or roadmap step instead.
2. **Done in Notion, repo not updated** — a Done card whose roadmap step is still `doing`/`next`: handled by Flow 6 and applied directly, not proposed.
3. **Missing `Record` tag** — an untagged card that clearly relates to one record (title, body, or a matching roadmap step): propose the tag, and say which step it matches. Add the option first if the record is new. Quick untagged reminders that match nothing stay untagged.
4. **Wrong or stale tag** — a tag whose record is resolved, closed or dropped, or a card whose step was dropped: propose retagging, moving to Done, or deleting. Never delete without explicit approval.
5. **Duplicates and drift** — two cards for the same step, or a card whose title no longer matches the step wording: propose merging or renaming (short, plain, verb-first, no bracket prefix).
6. **Status mismatch** — a card for a Next or Later step sitting in `To Do`, or a card for a Now step sitting in `Backlog`: fix the column. A card still tagged with a retired initiative ID (INI-01, INI-02): retag it to the parent record.

7. **Missing relation** — any card (open or Done) whose `To-Do Completion` is empty: it is hidden from every view. Propose setting it (value in Flow 2, step 4). Check this first on every run.
8. **Fortnightly Done clear-out** — a Done card that has not been edited for 14 days or more. Before proposing it, make sure its outcome is already in the matching record or achievement (Flow 3). Then propose archiving all such cards in one batch (move to Trash, restorable); never archive without AC's approval. Run this on the first sync of each fortnight (record the date of the last clear-out in `state/now.md`, in the Upcoming Done clear-out line, as "last clear-out: YYYY-MM-DD"). Cards that fed an open record's progress line stay until that line is written.

Present one table (Card · Current status/tags · Evidence from the repo · Change). Apply column fixes, retags, renames and relation fixes directly and list them; propose only moves to Done and archiving for AC's approval. Repo changes that follow (marking steps done, new steps) go through the normal show-then-commit rule.

## Flow 6 — Done Reconciliation

When AC moves a card to Done in Notion, the repo must follow it. The move in Notion is AC's own approval, so these repo updates are applied directly (no commit). Creating the next card is a Notion write and is listed afterwards.

1. **Match the card to its record** by title against the roadmap step wording and the record's progress log. If there is no confident match, list the card under "Unmatched Done cards" and ask AC. Never guess a record or step ID.
2. **Mark the step `done`** in the record's roadmap. Then **create the next card**: promote the next step in the roadmap to `next` or `doing` if it is still `later`, create its card (Flow 2: `To Do` for a Now record, `Backlog` for Next) and put the title in its `Card` column. If no steps remain, tell AC and ask the Capture close-out question (achievement, evidence, both or neither) instead of closing the record yourself. Add a dated line to the record's progress log that names the card.
3. **Check for contradictions** in `state/now.md` first (Upcoming, Recent Decisions), then `context/my-role/horizons.md` and the record's own text. Amend or remove any line that still presents the card as open. Set **Updated:** in `now.md` to today.
4. **Bump `updated:`** in every record changed, and correct any horizons row whose status line is now out of date.
5. **Verify**: run `python scripts/check.py validate`, then rebuild the dashboards. List each card, the repo changes made, and any unmatched cards in the output.

## Output

- **Ideas:** one block per idea group (top-level line, with its sub-bullets summarised) → verdict → for Enrich, each proposed addition and the record/section it goes into.
- **Actions out:** list of proposed cards.
- **To Do back in:** churn count; tracked cards with proposed record updates; long-open cards.
- **Done reconciliation:** each card moved to Done, the repo changes made, and unmatched cards.
- **Card tidy:** the table of proposed moves to Done, new tags, retags, merges, missing relations and the fortnightly Done clear-out, with the repo evidence for each.
- **Not recorded:** anything stripped under the people-records standard.

## Rules

- Only the two boards in `context/notion-boards.md`. No search, no browsing, no other pages.
- **Card writes are applied directly and listed afterwards for AC's awareness:** creating cards (Flow 2), setting the `Record` tag or `To-Do Completion` relation, fixing the column, renaming. Deleting or archiving a card, and moving a card to Done, still need AC's approval (a card AC moves to Done himself triggers Flow 6). Check the card's body and comments before proposing Done.
- Ideas page edits (ticking and suffixes after triage) are also applied directly and listed.
- Repo updates that follow a card AC has already moved to Done (Flow 6) are applied directly and listed afterwards. Other repo changes follow the show-then-commit rule in `AGENTS.md`.
- Every record ID, step ID or card title cited in a brief or output must come from a Notion card or a repo roadmap row. Name the source in brackets, e.g. `(card: "…")` or `(roadmap IMP-02.4, DA)`.
- Aliases only in the repo (records, snapshot, `state/`). Notion card titles are AC's own text: don't rewrite real names there; convert them to aliases only when copying into the repo.
