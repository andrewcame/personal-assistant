# AGENTS.md — Shared Instructions

Read by every assistant that works in this repo (GitHub Copilot, Claude, or any other agent). Tool-specific agents in `.github/agents/` and skills in `.github/skills/` add detail; **this file wins if they conflict.**

## What This Repo Is

A personal documentation assistant for AC, QA & Test Engineering Manager at PureGym: role context, plan, challenges, improvements, achievements, team evidence, and review preparation. Not a task tracker (tasks live in Notion), not a meeting-notes archive, not a complex multi-agent system.

## The Flow

AC needs a way to track the **big** items he must deliver in his role; when one is done, record it as an **achievement** (his own EOY, and goals where appropriate) or as **evidence** for a team member (their EOY and calibration, which AC supports; they own their own evidence).

```
SOURCES  ->  CHALLENGE or IMPROVEMENT  ->  tasks (Notion)  ->  done  ->  achievement / evidence / goal
```

1. **Sources** — anything that says "this matters": calls with the team or SMEs, things management said, industry signals, the job spec, the 30/60/90-day plan, things AC said he'd do, Notion ideas. They live in `context/` as they are raised (discovery calls, leadership direction, industry signals, job spec, plan). A plan item or job-spec gap with no record is a source too: open an improvement or challenge for it and assume it is required until AC closes it as "already doing that".
2. **Improvement (IMP)** — I've identified something I want to change or improve. **Challenge (CH)** — this is an issue and I'm going to fix or resolve it. Each carries a `## Roadmap` of tasks.
3. **Tasks** — AC's are Notion To Do cards, tagged with the record ID; someone else's are roadmap steps AC monitors. Notion and the roadmaps stay aligned in both directions: the agent creates the record, proposes its roadmap and creates the first card (To Do for Now, Backlog for Next); when a card is Done it creates the next one; a card AC adds that is tagged to a record is added to the roadmap as the next-up step. Ad hoc small tasks are **not tracked in this repo**.
4. **Jira** — if an improvement or challenge needs code or other changes, delivery is a Jira initiative. It is tracked **only in Jira** (and by Notion tasks for AC to monitor): add the Jira keys as an optional `jira:` label on the record. There is no initiative record.
5. **Done** — when a challenge or improvement closes, Capture asks where the result goes and sets `outcome:` on the record: `achievement` (AC's log, `achievements/`), `evidence` (a team member's Year-End Evidence in `team/<alias>.md`), `both`, or `none`. That feeds EOY and calibration.
6. **Goals** — goals are not created at close-out. When AC asks for goals (his own, or a team member's), Goal Builder picks the meatiest challenges and improvements — or better, the pillars they link to — and builds the goals on them, then tags the chosen records with the goal ID.
7. **Objectives periods** — each review period's objectives work is its own improvement (2026: IMP-08 Objectives & reviews); a new one opens for 2027 and keeps the link to the team profiles.

## Start Every Session Here

1. [`state/now.md`](state/now.md) — working memory: Upcoming (dated items) and recent decisions. The dashboards' Focus comes from Notion To Do cards, not from this file.
2. [`context/role-brief.md`](context/role-brief.md) — stable grounding: role, pillars, decision lens, driving theme. The live plan is [`horizons.md`](context/my-role/horizons.md).
3. [`state/learnings.md`](state/learnings.md) — accepted corrections from earlier sessions. Follow them.
4. [`ways-of-working/assistant-routine.md`](ways-of-working/assistant-routine.md) — the working agreement: how AC uses Notion, chats and the weekly/monthly routines.

Open full source files only when these don't answer the question. Prefer folder `README.md` indexes over reading every file.

## Repo Map

| Path | Holds |
|---|---|
| `achievements/<year>.md` | **AC's** evidence log for his own EOY and goals; each entry has a `**Tags:**` line of taxonomy IDs |
| `challenges/`, `improvements/` | Numbered records with YAML front-matter (`CH-`, `IMP-`): the big items AC delivers |
| `context/jira-initiatives/` | Source briefs for Jira initiatives (history, not tracked); delivery shows as a `jira:` label on the parent record |
| `context/my-role/horizons.md` | The live plan: Now / Next / Later under the microsite-sunset theme |
| `context/_taxonomy.md` | Every valid ID (JD-, P, M, lenses, values, goals, statuses) |
| `context/people.md` | Alias → role lookup. No real names anywhere |
| `context/discovery-calls/` | Interpreted call notes with front-matter |
| `context/performance-process/` | HR's performance process (source decks plus summaries): cycle, objectives, matrix, calibration, objective lenses, review style examples. Start at its `README.md` |
| `context/leadership-direction.md` | Director-level-and-above themes, newest first |
| `context/archive/` | Quarterly roll-ups of long context files; don't load unless asked about history |
| `team/` | Per-person development profiles under the writing standard; **Year-End Evidence** (WHAT/HOW) for team EOY and calibration |
| `templates/` | Formats for every record type |
| `scripts/check.py` | Validate, regenerate indexes, coverage, stale report |
| `scripts/report.py`, `scripts/people_report.py` | Build the two dashboards (Quality Leadership Board; People & Objectives Board) into git-ignored `reports/`. How they work and what feeds them: [`ways-of-working/dashboards.md`](ways-of-working/dashboards.md). Run them; never open the output |
| `evals/` | Behaviour checks for agents and skills |
| `ways-of-working/assistant-routine.md` | The weekly rhythm: what runs when, and how AC uses the harness. Scheduler prompts (master copy): [`scheduled-prompts.md`](ways-of-working/scheduled-prompts.md) |
| `state/cross-review/` | Findings from cross-model reviews, with AC's responses |

## Non-Negotiable Rules

1. **Aliases only.** Convert any real name using `context/people.md`; propose an alias for anyone new (check for clashes) and add them there first.
2. **Talk freely, record neutrally.** AC may speak bluntly; engage honestly. Anything written to a file about an individual follows the [people-records writing standard](team/README.md#writing-standard), and you end with a **"Not recorded:"** line listing what you stripped.
3. **Never store** ratings, calibration positions, flight risk, succession views, pay, health, or formal-process (PDP/PIP) details. Those go into official People systems only.
4. **IDs come from the taxonomy.** Never invent one; add it to `context/_taxonomy.md` first.
5. **Front-matter stays true.** When you touch a record, update `status`, `updated`, `horizon`, `links`, `people`. Don't hand-edit index tables between `<!-- index:start -->` / `<!-- index:end -->`.
6. **Facts over inference.** Don't invent achievements, impact, dates, owners, or reactions. Ask for the minimum missing detail.
7. **Commits need AC's explicit OK; Notion card changes don't.** Summarise repo changes and run checks, then pause before committing (small, focused commits on `main`; AC pushes). Notion cards (create, retag, move column, move to Done) are applied directly under the notion-sync flows and **listed afterwards for AC's awareness**; deletes and archiving still need an OK. Repo updates that follow a card AC moved to Done (notion-sync Flow 6) are applied directly and listed.
8. **Preserve formatting.** Keep CRLF line endings and aligned markdown tables as found.
9. **Notion: two boards only.** Read and write only the boards listed in [`context/notion-boards.md`](context/notion-boards.md). Never search the workspace or open other pages — it also holds AC's personal life admin. List every Notion write to AC afterwards.
10. **Every live challenge or improvement has tasks and a roadmap.** Tasks are a Notion To Do card tagged with the record ID for AC, or a roadmap step owned by someone else (monitored). In Now/Next each keeps a `## Roadmap` table (format in `context/_taxonomy.md`) with at least one `doing`/`next` step, each first-up step has a card, and each step names its card in the roadmap's `Card` column so the dashboard can show what is on Notion. Notion and the roadmaps must always align: every tagged open card is a roadmap step (notion-sync adopts any that aren't). Every row in `horizons.md` is carried by a record. The Now limit is 8.
11. **Closing records.** A closed challenge or improvement gets `outcome:` (`achievement`, `evidence`, `both`, `none`) and a link to where it landed; Capture does this. `check.py` warns when it is missing.

## Routing (summary)

Capture is the router — full rules in [`.github/agents/capture.agent.md`](.github/agents/capture.agent.md). In short: wins → `achievements/`; team member outcomes → `team/<alias>.md` Year-End Evidence; open problems → `challenges/`; self-directed work → `improvements/`; Jira delivery → `jira:` label on the parent; conversations → `context/discovery-calls/`; director-level direction → `context/leadership-direction.md`; external reading → `context/industry-signals.md`; person development → `team/<alias>.md`; decisions → `state/now.md`; plan changes → `context/my-role/horizons.md`.

## Agents And Skills

| Name | Use for | File |
|---|---|---|
| Capture | Filing anything | `.github/agents/capture.agent.md` |
| Priority Advisor | "What do I do now?" — one priority | `.github/agents/priority-advisor.agent.md` |
| Idea Validator | Is this worth doing, and when? | `.github/agents/idea-validator.agent.md` |
| Goal Builder | Role or team member goals | `.github/agents/goal-builder.agent.md` |
| Review Writer | Map evidence and draft reviews | `.github/agents/review-writer.agent.md` |
| weekly-review | Friday review; refresh `state/now.md` | `.github/skills/weekly-review/SKILL.md` |
| gap-analysis | Evidence gaps by pillar / JD | `.github/skills/gap-analysis/SKILL.md` |
| horizon-review | Monthly re-plan; consolidate learnings | `.github/skills/horizon-review/SKILL.md` |
| calibration-prep | WHAT/HOW drafts — chat only | `.github/skills/calibration-prep/SKILL.md` |
| industry-research | Source-backed research brief | `.github/skills/industry-research/SKILL.md` |
| action-extraction | Forgotten actions → Notion list | `.github/skills/action-extraction/SKILL.md` |
| notion-sync | Ideas triage, actions out, to-dos back in | `.github/skills/notion-sync/SKILL.md` |
| check-card-status | Every task per challenge and improvement, flagged and cleaned up | `.github/skills/check-card-status/SKILL.md` |
| cross-review | Second-opinion sense check by a different model family | `.github/skills/cross-review/SKILL.md` |

If your tool doesn't load these automatically, read the file and follow it.

## Model And Token Discipline

Applies to every task, whatever the prompt says. Full guide: [`ways-of-working/model-and-token-guide.md`](ways-of-working/model-and-token-guide.md).

- **Right-size the model.** Mechanical filing → Haiku-class; capture, weekly review, Notion sync, research → Sonnet-class; calibration, reviews, goals, horizon review → Opus-class; cross-review → a different model family. You can't switch models yourself: if the task is clearly mismatched to the current one, say so in one line and carry on unless AC switches.
- **Read the minimum.** Start from the four start-here files; use folder `README.md` indexes, `grep` and `view_range`; never open `reports/*.html`, `reports/*.json` or `context/archive/` unless asked. To answer a dashboard question, read [`ways-of-working/dashboards.md`](ways-of-working/dashboards.md), not the output.
- **No sub-agents** for work you can finish in a few direct reads.
- **One task per chat.** If a chat has drifted onto a new, unrelated task, suggest a fresh one.
- **Batch** related captures into one pass and one checks run.

## Checks

After any write, run `python scripts/check.py all` (or ask AC to) and fix errors before proposing a commit.

## Learning Loop

When AC corrects you — routing, wording, format, a fact, a preference — propose a one-line learning in the format used in [`state/learnings.md`](state/learnings.md). Add it only if AC accepts. Don't propose learnings for one-off content changes.
