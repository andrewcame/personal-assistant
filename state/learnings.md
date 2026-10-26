# Learnings

_Corrections AC has accepted, so they don't have to be repeated. Every agent reads this at the start of a session and follows it. Keep entries to one line each._

## How It Works

1. **Propose** — when AC corrects routing, wording, format, a fact about how things work here, or a preference, the agent proposes one line: `YYYY-MM-DD · scope · rule · why`.
2. **Accept** — add it only if AC says yes. Don't propose learnings for one-off content edits.
3. **Supersede** — if a new learning contradicts an old one, strike the old one through (`~~…~~`) and note the replacement; don't silently delete.
4. **Consolidate** — at each [horizon review](../.github/skills/horizon-review/SKILL.md), move learnings that have held for a month into the agent, skill, template, or `AGENTS.md` they belong to, then remove them here. Aim to keep this file under ~25 lines of rules.

Scopes: `all` · `capture` · `people` · `reviews` · `planning` · `format` · `git`.

## Active Learnings

- 2026-10-14 · git · Never commit without AC's explicit OK; show the changes first. · AC reviews everything before it lands.
- 2026-10-14 · git · Commit straight to `main`; AC pushes to GitHub himself. · Single-owner repo; sandbox can't reach GitHub.
- 2026-10-14 · format · Keep markdown tables column-aligned and preserve CRLF line endings. · AC reads the files directly in VS Code.
- 2026-10-14 · format · Helper scripts are standard-library Python, not PowerShell. · They must run from Cowork as well as locally.
- 2026-10-14 · people · "Jamie" in older notes and review examples is JFG; "Josh" is JBe, not JB (JB is the Dootrix contractor). · Alias clashes.
- 2026-10-14 · reviews · Write matrix positions as "WHAT x / HOW y" — never "3-2". · The two People PDFs use opposite orders.
- 2026-10-14 · reviews · Calibration ratings and sensitive fields are drafted in chat only, never saved. · Subject access request exposure.
- 2026-10-14 · planning · 2026 goals are provisional; tag evidence to pillars and JD items regardless. · Proper goals start in 2027.
- 2026-10-23 · planning · The Exerp Assistant is a test tool, not a backend service; don't list it as a backend coverage gap or treat its card as a backend duplicate. · AC correction.
- 2026-10-26 · all · Cite a source for every ID in a brief (card or roadmap row). Apply Done-card changes to the repo directly and list them afterwards. · Briefs presented IDs that were not Notion cards as cards, and AC needs to see where each one comes from.
- 2026-10-26 · notion · Only the `Admin` Record value means BAU. A card with no Record, or only Admin, is unmapped and ties to no CII. Cards owned by others are titled "Monitor X", not "Do X". · AC's rules for Notion-to-repo mapping.
- 2026-10-26 · notion · To Do cards are for challenges (CH-) and improvements (IMP-) only, never initiatives (INI-); an initiative's tasks go against its parent improvement. · An initiative is tracked in Jira and the repo, so a card duplicates it.
- 2026-10-26 · notion · The To Do board has Backlog, To Do and Done. Now steps go in To Do; Next and Later steps go in Backlog. · AC's board structure.
- 2026-10-26 · notion · Don't create cards for Next or Later steps that have none; AC adds his own. Existing cards are triaged, not expanded. · Future work isn't detailed yet, and extra cards bloat the board.
- 2026-10-23 · all · When mentioning a CH-, IMP- or INI- record, or a roadmap step such as INI-01.3, always give its title too, not just the ID. · AC can't always remember what each one is and finds cross-referencing hard.

## Retired

_Learnings consolidated into agent/skill files or superseded. Keep the line and say where it went._

-
