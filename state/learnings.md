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
- ~~2026-10-26 · notion · To Do cards are for challenges (CH-) and improvements (IMP-) only, never initiatives (INI-); an initiative's tasks go against its parent improvement.~~ Retired 2026-11-04: initiatives are no longer records; cards stay CH-/IMP- only (now in `context/notion-boards.md`).
- 2026-10-26 · notion · The To Do board has Backlog, To Do and Done. Now steps go in To Do; Next and Later steps go in Backlog. · AC's board structure.
- ~~2026-10-26 · notion · Don't create cards for Next or Later steps that have none; AC adds his own.~~ Superseded 2026-11-04 by the two-way card flow below.
- 2026-11-04 · notion · Cards for a Later record are created when AC moves it to Next, not before; the agent creates the first card then. · AC confirmed.
- 2026-11-04 · notion · Two-way card flow: the agent creates the record, proposes its roadmap, creates the first card (To Do for Now, Backlog for Next; Later records on promotion), then the next card when one is Done. A card AC adds tagged to a record is added to the roadmap as the next-up step. Notion and roadmaps must always align. · AC's rule.
- 2026-11-04 · planning · Goals are created when AC asks Goal Builder for them, from the meatiest challenges and improvements or, better, the pillars they link to; not at close-out of a record. · AC's flow.
- ~~2026-10-26 · planning · Initiatives have no roadmap; step dependencies point at the parent record's steps.~~ Retired 2026-11-04: no initiative records.
- 2026-10-26 · notion · Every Now and Next to-do on a record exists as a Notion card, and card titles carry no internal step IDs (e.g. IMP-02.4). The step-to-card mapping is the roadmap's `Card` column (exact card title). · AC needs every task visible in Notion, and internal IDs are not for Notion.
- 2026-10-23 · all · When mentioning a CH- or IMP- record, or a roadmap step such as IMP-02.3, always give its title too, not just the ID. · AC can't always remember what each one is and finds cross-referencing hard.
- 2026-10-27 · all · "C&I" / "C&Is" in AC's messages means challenges and improvements (CH- and IMP- records), i.e. the same as CII. · AC's shorthand.
- ~~2026-10-27 · planning · An initiative is listed in its parent C&I's horizons row, never its own row, and doesn't count toward the Now limit.~~ Retired 2026-11-04: no initiative records. The Now limit is now 8.
- 2026-11-02 · all · When talking to AC, give the C&I's Notion tag (e.g. "IMP-02 Member data") with the ID, not just the ID or title. · AC doesn't recall them by ID.
- 2026-11-02 · planning · Notion is the master for the next in-progress task. If an open card is tagged to a record but no roadmap step names it, add the step (next-up) to the roadmap; if a first-up step has no card, create it. · The repo roadmap is a plan; Notion shows what is actually being worked.
- 2026-11-02 · notion · "To Do" means in progress (there is no separate in-progress column). A Now C&I can have several To Do cards because AC adds them as he thinks of them, so more than one card is not a duplicate. · AC's board structure.
- 2026-11-03 · people · People-system objectives are light (title, one intent line, 2–4 bullets); detail belongs in the EOY review. · AC correction after objectives were over-written.
- ~~2026-11-03 · people · For calibration of non-direct reports (e.g. JFG), second-hand evidence reviewed by their line manager may be recorded...~~ Moved 2026-11-04 into the writing standard in `team/README.md`.
- 2026-11-04 · all · Achievements (`achievements/`) are AC's own, for his EOY and goals; evidence (`team/<alias>.md` Year-End Evidence) is for the team's EOY and calibration. A closing challenge or improvement records which via `outcome:`. · AC's definition.
- 2026-11-04 · planning · Plan items and job-spec gaps with no record are assumed required: open an improvement or challenge for each; AC closes any already done. Jira delivery is a `jira:` label, not a record. · AC's simplified flow.
- 2026-11-04 · notion · Card writes (create, retag, column, rename) are applied and listed afterwards; deleting, archiving and moving to Done still need AC's OK. Commits still need AC's OK. · AC relaxed the show-before-write rule for cards.

## Retired

_Learnings consolidated into agent/skill files or superseded. Keep the line and say where it went._

-
