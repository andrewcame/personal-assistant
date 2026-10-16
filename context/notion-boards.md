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

**To-Do Database schema (as at 2026-10-15):** `Name` (title), `Status` (Backlog · To Do · Do Now · Done), `Priority` (High · Medium · Low), `Due date`, `Record` (multi-select of record IDs, e.g. `IMP-08`, `CH-12`), `To-Do Completion` (relation).

- **Titles:** short and plain, no `[CATEGORY]` prefix (retired 2026-10-15). Detail can go in the card body — agents read the body of tracked cards.
- **Record IDs:** go in the `Record` property. Add a new option there when a new record is created; untagged cards are fine for quick tasks.
- **"Open"** means Status is Backlog, To Do, or Do Now.

- **To Do:** quick reminders that open and close within the week are counted as "weekly churn" in the weekly review and otherwise ignored. Cards tagged with a record ID, or open for more than 14 days, are processed: progress or blockers go into the matching record; completed ones may become evidence.
- **Ideas:** capture stays free-form — any bullet, any wording, mid-call. **Sub-bullets drill into their parent**: a top-level bullet plus everything nested under it is one idea group. At triage each unticked group gets a verdict — **Enrich** (covered, but adds detail to an existing record — the default whenever there is anything new), **Covered** (nothing new), **Promote** (new record), **To Do** (becomes a card), or **Park** (not now). After AC approves, the group's top-level line becomes a **ticked checkbox** with a suffix listing every record it fed (`→ IMP-02, INI-01`, `→ To Do`, `→ parked`); sub-bullets stay nested and unchanged. The verdict and what was added are logged in [`state/ideas-log.md`](../state/ideas-log.md). Ticked groups are never re-triaged; AC purges them whenever he likes.
