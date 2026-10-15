# AGENTS.md — Shared Instructions

Read by every assistant that works in this repo (GitHub Copilot, Claude, or any other agent). Tool-specific agents in `.github/agents/` and skills in `.github/skills/` add detail; **this file wins if they conflict.**

## What This Repo Is

A personal documentation assistant for AC, QA & Test Engineering Manager at PureGym: role context, plan, challenges, improvements, initiatives, achievements, team development, and review preparation. Not a task tracker (tasks live in Notion), not a meeting-notes archive, not a complex multi-agent system.

## Start Every Session Here

1. [`state/now.md`](state/now.md) — this week's focus, open threads, recent decisions, waiting on.
2. [`context/role-brief.md`](context/role-brief.md) — condensed role, plan, pillars, decision lens.
3. [`state/learnings.md`](state/learnings.md) — accepted corrections from earlier sessions. Follow them.

Open full source files only when these don't answer the question. Prefer folder `README.md` indexes over reading every file.

## Repo Map

| Path | Holds |
|---|---|
| `achievements/<year>.md` | Evidence log; each entry has a `**Tags:**` line of taxonomy IDs |
| `challenges/`, `improvements/`, `initiatives/` | Numbered records with YAML front-matter (`CH-`, `IMP-`, `INI-`) |
| `context/my-role/horizons.md` | The live plan: Now / Next / Later under the microsite-sunset theme |
| `context/_taxonomy.md` | Every valid ID (JD-, P, M, lenses, values, goals, statuses) |
| `context/people.md` | Alias → role lookup. No real names anywhere |
| `context/discovery-calls/` | Interpreted call notes with front-matter |
| `context/leadership-direction.md` | Director-level-and-above themes, newest first |
| `context/archive/` | Quarterly roll-ups of long context files; don't load unless asked about history |
| `team/` | Per-person development profiles under the writing standard |
| `templates/` | Formats for every record type |
| `scripts/check.py` | Validate, regenerate indexes, coverage, stale report |
| `evals/` | Behaviour checks for agents and skills |
| `ways-of-working/assistant-routine.md` | The weekly rhythm: what runs when, and how AC uses the harness |
| `state/cross-review/` | Findings from cross-model reviews, with AC's responses |

## Non-Negotiable Rules

1. **Aliases only.** Convert any real name using `context/people.md`; propose an alias for anyone new (check for clashes) and add them there first.
2. **Talk freely, record neutrally.** AC may speak bluntly; engage honestly. Anything written to a file about an individual follows the [people-records writing standard](team/README.md#writing-standard), and you end with a **"Not recorded:"** line listing what you stripped.
3. **Never store** ratings, calibration positions, flight risk, succession views, pay, health, or formal-process (PDP/PIP) details. Those go into official People systems only.
4. **IDs come from the taxonomy.** Never invent one; add it to `context/_taxonomy.md` first.
5. **Front-matter stays true.** When you touch a record, update `status`, `updated`, `horizon`, `links`, `people`. Don't hand-edit index tables between `<!-- index:start -->` / `<!-- index:end -->`.
6. **Facts over inference.** Don't invent achievements, impact, dates, owners, or reactions. Ask for the minimum missing detail.
7. **Show before saving; never commit without AC's explicit OK.** Summarise changes, run checks, then pause. Small, focused commit messages on `main`.
8. **Preserve formatting.** Keep CRLF line endings and aligned markdown tables as found.
9. **Notion: two boards only.** Read and write only the boards listed in [`context/notion-boards.md`](context/notion-boards.md). Never search the workspace or open other pages — it also holds AC's personal life admin. Show every Notion write first.
10. **Every live CII has a roadmap.** Challenges, improvements and initiatives in Now/Next keep a `## Roadmap` table (format in `context/_taxonomy.md`) with at least one `doing`/`next` step; AC-owned first-up steps have a tagged Notion To Do card.

## Routing (summary)

Capture is the router — full rules in [`.github/agents/capture.agent.md`](.github/agents/capture.agent.md). In short: wins → `achievements/`; open problems → `challenges/`; self-directed work → `improvements/`; sponsored proposals → `initiatives/`; conversations → `context/discovery-calls/`; director-level direction → `context/leadership-direction.md`; external reading → `context/industry-signals.md`; person development → `team/<alias>.md`; decisions/threads → `state/now.md`; plan changes → `context/my-role/horizons.md`.

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
| cross-review | Second-opinion sense check by a different model family | `.github/skills/cross-review/SKILL.md` |

If your tool doesn't load these automatically, read the file and follow it.

## Checks

After any write, run `python scripts/check.py all` (or ask AC to) and fix errors before proposing a commit.

## Learning Loop

When AC corrects you — routing, wording, format, a fact, a preference — propose a one-line learning in the format used in [`state/learnings.md`](state/learnings.md). Add it only if AC accepts. Don't propose learnings for one-off content changes.
