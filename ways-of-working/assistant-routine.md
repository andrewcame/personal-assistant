# Assistant Routine

How AC works with this harness day to day. Agreed 2026-10-15; adjust as it beds in.

## Working Agreement (AC, 2026-10-15)

1. **Ideas** — AC adds them to the Notion Ideas page as they come, free-form. The agent checks and triages them (Friday), ticking each once processed.
2. **To-dos** — AC adds them to the Notion To Do board as they come. The agent checks them and pulls long-running or record-tagged cards into the matching CII.
3. **Developments** — AC messages new calls, ideas, decisions and challenges in a new chat in this project. The agent files them into the repo (neutral record, "Not recorded" line) and keeps CIIs, horizons and `state/now.md` current.
4. **Suggestions** — the agent proposes improvements monthly (industry scan + horizon review), and flags anything urgent in the weekly report.
5. **Two-way monitoring** — the agent keeps CII roadmaps and Notion in step: every first-up step owned by AC has a card; completed cards move roadmap steps on; new records get a `Record` tag option.
6. **Approval** — nothing is committed, and nothing is written to Notion, without AC's OK (cards AC has explicitly approved in the conversation count). AC pushes to GitHub.

## What Lives Where

| Tool | Job |
|---|---|
| **This repo** | Memory: context, records (challenges, improvements, initiatives), evidence, objectives, team development |
| **Notion — To Do** | AC's task list. Quick reminders come and go; long-running or record-tagged cards flow back into the repo |
| **Notion — Ideas** | Loose thoughts. Triaged weekly: park, link to a record, or promote |
| **Claude (Cowork)** | The interface: capture, bounce ideas, research, sense-check, run the routines, commit after AC's OK |
| **Copilot (VS Code)** | Same instructions via `AGENTS.md`; used for cross-model review and quick edits, and as the backup when Claude credits run out ([model and token guide](model-and-token-guide.md)) |
| **Quality Leadership Board** | The dashboard AC reads instead of the markdown files; refreshed every Friday |

## Any Time

- **Capture:** paste rough notes, screenshots, Miro links, or just talk. Speak plainly; records are written neutrally and anything stripped is listed under "Not recorded".
- **Bounce an idea:** "sense-check this" (Idea Validator) or "challenge me on this" (adversarial pushback).
- **Go out to industry:** "research …" (industry-research skill) — produces a brief and a candidate signal for AC to add a take to.
- Every change is shown before it's committed. AC pushes to GitHub.

## Weekly Rhythm (scheduled in Cowork)

| When | Routine | What AC gets |
|---|---|---|
| ~~Monday 08:30~~ (paused 2026-10-16 to save usage) | Week ahead | Focus from `state/now.md`, open To Do cards tagged to records, what's due or stale, suggested top 3 |
| ~~Wednesday 12:30~~ (paused 2026-10-16 to save usage) | How are we getting on | Short mid-week check: progress on the top 3, anything blocked, new ideas waiting for triage |
| **Friday 15:00** | Weekly report | Weekly review (moved, stale, wins to log, next week), Notion sync (churn count, tracked to-dos, ideas triage), refreshed dashboard |

## Monthly And Seasonal

| When | Routine |
|---|---|
| 1st of the month | Industry scan on current Now themes; horizon review (re-plan, consolidate learnings) |
| Quarterly | Run all evals; roll up long context files into `context/archive/`; cross-review of the quarter's changes |
| 2026-11-02 | Calibration prep for the 11 November session (tracked in [IMP-08](../improvements/08-2026-objectives-calibration-and-eoy-reviews.md)) |

Scheduled runs prepare drafts and proposals only. Nothing is committed or written to Notion until AC confirms. Scheduled tasks run while the Claude app is open; a missed run happens on next launch.

## Cross-Model Review

Every few weeks, or before something important leaves the repo (a review, a proposal), AC opens VS Code, picks a GPT model in Copilot, and says "run cross-review". It writes up to eight findings to `state/cross-review/`; AC adds a response to each; the next Claude session applies the agreed ones. See the [cross-review skill](../.github/skills/cross-review/SKILL.md).

## Getting Better Over Time

- Corrections become one-line learnings in `state/learnings.md` (after AC accepts), folded into the agents at each horizon review.
- Evals in `evals/` are re-run after changing instructions or models.
