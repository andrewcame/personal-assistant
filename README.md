# personal-assistant

This repository is a lightweight documentation assistant for my work as a QA & Test Engineering Manager.

It helps with:

- Capturing useful industry signals, leadership signals, and QA/discovery calls as they happen
- Logging and tracking open management challenges over time
- Logging achievements and tying them back to goals and objectives
- Building goals for my own role and for each direct report
- Writing midyear and end-of-year reviews based on goals and achievements
- Managing team development, progression, and review context
- Reducing the mental load of higher-level planning

It holds the context needed for planning, reflection, and review writing: role expectations, goals, achievements, challenges, team context, operating models, discovery notes, and writing examples.

It is **not** a day-to-day activity tracker — that lives in Notion.

It is not meant to become:

- a full email archive
- a general-purpose second brain
- a complex multi-agent system

## How This Repo Is Organized

- [achievements](achievements) - Yearly evidence logs, linked to goals where appropriate.
- `addons` - Reserved for supporting tools (currently empty; `.gitignore` already covers a future frontend there).
- `.github/agents` - Small, role-based chat agents for the most common tasks.
- `.github/skills` - Reusable research and action-extraction workflows.
- [challenges](challenges) - Numbered records of open management problems, with context, questions, position, and next action.
- [AGENTS.md](AGENTS.md) - Shared instructions for every assistant (Copilot reads it directly; [CLAUDE.md](CLAUDE.md) imports it). Start-here files, repo map, non-negotiable rules, agent and skill list.
- [state](state) - [now.md](state/now.md): short working memory (upcoming dated items, narrative focus and waiting-on notes, open threads, recent decisions). [learnings.md](state/learnings.md): corrections AC has accepted, consolidated into agents at each horizon review. Every agent reads both first.
- [evals](evals) - Behaviour checks for agents and skills; re-run after changing instructions or models.
- [scripts](scripts) - Repo health checks (`python scripts/check.py all`): validates front-matter, IDs, tags and links; regenerates folder indexes; reports evidence coverage by pillar/JD and stale records. Also builds the two dashboards in git-ignored `reports/`: `python scripts/report.py` (Quality Leadership Board: this week, plan, signals) and `python scripts/people_report.py` (People & Objectives Board: team readiness, evidence, framework coverage). How they work: [dashboards.md](ways-of-working/dashboards.md). Standard-library Python only.
- [initiatives](initiatives) - The Jira-level work item for a challenge or improvement that needs code changes or team work. Each names the challenge or improvement it delivers (`origin:`) and shows on that record's dashboard card.
- [context](context) - [Taxonomy](context/_taxonomy.md) (stable IDs for JD items, pillars, lenses, values, goals, records), [People lookup](context/people.md) (alias → role; no real names anywhere in the repo), personal role context, team role expectations, discovery calls, QA health, industry signals, objective lenses, role pillars, and QA banding.
- [goals](goals) - Annual priorities, active goals, milestones, and review anchors.
- [improvements](improvements) - Numbered records of in-flight improvement initiatives, tracked until folded into an achievement.
- [reviews](reviews) - Midyear checkpoints and end-of-year review material.
- [team](team) - Alias-based profiles for development, progression, review context, and team planning.
- [templates](templates) - Reusable formats for logs, profiles, calls, and reviews.
- [ways-of-working](ways-of-working) - Engineering and QA operating models, recurring cadences, and call agendas.

## Current Scope

- Current role: QA & Test Engineering Manager
- Mission model: focus on the big items, not the small things
- Ongoing capture: leadership signals, QA/discovery calls, cadence updates, and industry signals, filed as they come in rather than batched
- Challenge tracking: open management problems logged and updated over time until resolved
- Improvement tracking: initiatives worth pursuing logged in `improvements/` while in flight, then folded into an achievement once delivered
- Achievement logging: keep one yearly file in `achievements/` as the evidence trail
- Team development: progression, review context, observations, and goals kept per person in `team/`
- Review cycle: retain the engineer checkpoint as archive material, then use the manager track for objectives and review preparation

## How The Assistant Works

1. Use the context files to understand questions and updates.
2. Capture leadership signals, QA/discovery calls, cadence updates, achievements, and reading as they happen, using the **Capture** agent — it routes each note to the right file and format regardless of which chat it came from.
3. Log and update open problems in [challenges](challenges) as they develop.
4. Track improvement initiatives in [improvements](improvements) while they're in flight, folding each into an achievement once delivered, using the **Capture** agent.
5. Build or refine role goals in [goals/2026.md](goals/2026.md) and team member development goals in [team](team), using the **Goal Builder** agent.
6. Map achievements to goals, values, and objective lenses before drafting a review, using the **Review Writer** agent.
7. Keep [team](team) profiles current for development, progression, and review context.
8. When it's unclear what to focus on next, ask the **Priority Advisor** agent — it grounds everything captured so far against the JD, the Now/Next/Later horizons plan, leadership direction, and role pillars to surface one priority.
9. When you need external evidence, use the **Industry Research** skill — it produces a source-backed brief and candidate industry-signal entry without filing it automatically.
10. When you need to recover forgotten commitments, use the **Action Extraction** skill — it scans recorded context and produces a Notion-ready to-do list without editing the repo or syncing tasks.
11. Every Friday, run the **Weekly Review** skill — what moved, what's stale, wins still to log, next week's focus; it refreshes `state/now.md` after you confirm.
12. Before a review or 1:1 with GL, run the **Gap Analysis** skill — which pillars and JD responsibilities have evidence, which are in flight or deliberately parked, and which are blind spots.
13. Roughly monthly, run the **Horizon Review** skill — reconcile Now / Next / Later with the records, close finished items into achievements, and re-plan.
14. Before calibration (2026-11-11) and end-of-year reviews, run the **Calibration Prep** skill — drafts each QA team member's Top 3 WHAT / Top 3 HOW and a suggested matrix position in chat only; ratings and sensitive fields go straight into the People template. Anything about an individual follows the [people-records writing standard](team/README.md#writing-standard).

## What To Ask The Chat Agent For

Use the smallest role that fits the job. These are registered as chat agents under `.github/agents` and selectable from the agent picker.

- Logging or filing anything — an achievement, a challenge, an improvement, a QA call, a leadership signal, a cadence update, or an industry signal: **Capture**
- Building or refining a role goal or a team member's development goal: **Goal Builder**
- Mapping achievements to goals/values and drafting a review in your own voice: **Review Writer**
- Sense-checking an idea against the role, plan, and JD before committing time to it: **Idea Validator**
- "What do I do now?" — grounding everything captured against the JD, plan, leadership direction, and role pillars to surface one priority: **Priority Advisor**

## How To Feed The Assistant

**Ideas and activities you are considering**
Use the Idea Validator agent. Describe what you are thinking — rough is fine. It will tell you where it fits, whether the timing is right, and whether it is worth pursuing or parking. If it is an actionable task, it lives in Notion, not here.

**Everything else worth keeping**
Use the Capture agent for achievements, challenges, QA/discovery calls, leadership signals, cadence updates, and reading. It files each into the right place using the formats already established in this repo.

**Themes and direction from leadership**
If a 1:1, CEO or leadership call, organisational update, or other material from anyone at director level or above surfaces something that should influence how the role is focused, add it to [context/leadership-direction.md](context/leadership-direction.md) (via Capture or directly). This includes GL, equivalent leaders, and his manager or more senior leaders; it is not limited to the director himself. Use the format in that file: date, source, theme, implication. The Idea Validator loads this automatically so it stays current.

**Articles, research, and ideas you found yourself**
There is no separate reading log. External material — articles, podcasts, reports, standards, practice frameworks — goes in [context/industry-signals.md](context/industry-signals.md) with an honest stance: supports, challenges, refutes, or unsettled, plus your own take where it's worth keeping. This is the standing watch that keeps the plan pressure-tested rather than assumed, and it is reviewed roughly quarterly. Leadership-sourced material, including podcasts or writing by someone at director level or above, still goes to `context/leadership-direction.md`. Follow-ups that are real work belong in `improvements/`, `challenges/`, or `goals/2026.md` rather than sitting as open checkboxes.
