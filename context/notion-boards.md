# Notion Boards

The **only** Notion content any agent may read or write. The connection reaches AC's whole personal workspace, which also holds unrelated life admin, so these limits are strict.

## Allowed Boards

| Board | Purpose | Link / ID |
|---|---|---|
| To Do | AC's task list. Agents read open and recently closed cards; create cards only after AC approves. | Page: https://app.notion.com/p/To-Do-3f9ea035c7f1809482f2f2bab36e7a88 · Data source: `collection://1fbea035-c7f1-8354-a218-0711ea45ecb7` (✅ To-Do Database) |
| Ideas | Loose ideas not yet tied to a record. Agents triage and write a verdict back after AC approves. | Page: https://app.notion.com/p/Ideas-376ea035c7f180fd9248fcc4486f66d3 (free-form page, not a database) |

Both sit under AC's **Work** page in Notion. The "To-Do Completion" database on the To Do page is a completion tracker; read it only if AC asks.

## Rules

1. **Fetch these boards by link or ID only.** Never use Notion search, never list or browse other pages, never follow links from a card to other pages.
2. **Show before writing.** Every create or update in Notion is shown to AC first, the same as a commit.
3. **Tag with record IDs.** A card created from the repo carries its record ID (see Conventions below). An idea promoted to a record gets the new ID written back next to it.
4. **Nothing sensitive goes to Notion** — the people-records standard applies to card text too.
5. **Tasks are tracked in Notion, not in the repo.** The repo records outcomes and progress against records, not the task list.

## Conventions

**To-Do Database schema (as at 2026-10-15):** `Name` (title, AC prefixes a category like `[AI]`, `[DOCS]`, `[METRICS/DOCS]`), `Status` (Backlog · To Do · Do Now · Done), `Priority` (High · Medium · Low), `Due date`, `Multi-select` (unused — proposed for record IDs), `To-Do Completion` (relation).

- **Record IDs:** because titles already carry AC's category prefix, record IDs go in the `Multi-select` property (proposed rename: `Record`), e.g. `IMP-08`. Until that is agreed, put the ID in brackets at the end of the title: `Book objectives call with MP [IMP-08]`.
- **"Open"** means Status is Backlog, To Do, or Do Now.

- **To Do:** quick reminders that open and close within the week are counted as "weekly churn" in the weekly review and otherwise ignored. Cards tagged with a record ID, or open for more than 14 days, are processed: progress or blockers go into the matching record; completed ones may become evidence.
- **Ideas:** each new idea gets one verdict — **Park** (keep in Notion), **Link** (add as context to an existing record), or **Promote** (open a new improvement or challenge). The verdict and any record ID are written back to the card.
