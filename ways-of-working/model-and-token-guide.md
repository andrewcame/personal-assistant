# Model And Token Guide

Reminder for AC on getting the most from the agents without overspending Copilot premium requests (or Claude credits). Added 2026-10-23. The short rules in [AGENTS.md](../AGENTS.md#model-and-token-discipline) apply to every agent whatever the prompt says; this page is the fuller version.

Copilot bills each prompt at the chosen model's multiplier, so the savings come from **fewer, well-scoped prompts on the cheapest model that can do the job**. Check the multipliers in the model picker; they change.

## Which Model For Which Task

The agent cannot switch its own model. AC picks it before sending the prompt.

| Task | Agent / skill | Tier |
|---|---|---|
| Quick filing: one to-do, a roadmap step, a `now.md` line, a status change; running `check.py`; Notion churn count | Capture (small inputs) | **Haiku-class** |
| Filing calls, achievements and CII updates; weekly review; Notion sync and ideas triage; action extraction; industry research; gap analysis; Idea Validator; Priority Advisor | Capture, weekly-review, notion-sync, action-extraction, industry-research, gap-analysis | **Sonnet-class (default)** |
| Calibration prep; review writing; goal building; monthly horizon review; anything about an individual's development | calibration-prep, Review Writer, Goal Builder, horizon-review | **Opus-class, sparingly** |
| Second-opinion sense check | cross-review | **A different family** (e.g. GPT), so the review is independent |

Rules of thumb:

- Start on Sonnet-class. Move down for mechanical work, up only when the output matters or the first pass missed.
- Sensitive people work (calibration, reviews, development goals) is worth the higher tier; the writing standard is easy to breach on a weaker model.
- After switching models or tools, re-run the relevant [evals](../evals/README.md). Privacy cases E01–E04 are the minimum.
- `python scripts/check.py all` is the safety net for any model: run it after every write.

## Cutting Token Spend

1. **One task per chat.** Start fresh for each job. Long chats re-send their whole history every turn.
2. **Start from the standard four files only:** `state/now.md`, `context/role-brief.md`, `state/learnings.md`, `ways-of-working/assistant-routine.md`. Open others only when those don't answer the question; prefer folder `README.md` indexes.
3. **Name the file or record in the prompt** (e.g. "file this call, then update CH-12") so the agent doesn't explore.
4. **Never open generated output.** `reports/*.html` and `reports/data.json` are 100 KB+ and git-ignored. Run `report.py`; don't read it.
5. **Read ranges, not whole files.** Use `grep` and `view_range` for anything over ~20 KB (`cadences.md`, `engineering-behaviors.md`, `software-delivery-lifecycle.md`, long call notes).
6. **Batch captures.** Paste several notes into one chat rather than one chat each.
7. **No sub-agents for small jobs.** Direct reads are cheaper than spinning up a delegate.
8. **Heavy routines early in the month.** Horizon review plus the industry scan on the 1st is the most expensive run; give it the stronger model and a fresh chat.
9. **Don't load archives.** `context/archive/` is for history questions only.
10. **Lower reasoning effort for filing.** Mechanical capture doesn't need extended thinking.

## Running Routines Manually (No Claude)

Scheduled runs are just skills, so ask for them by name in a fresh chat: "run the weekly-review skill" (Fridays), "run horizon-review" (1st of the month), "run calibration-prep" (2 Nov). Nothing runs on a schedule in VS Code, so set a calendar reminder.

- **Checks:** `python scripts/check.py all` and `python scripts/report.py` need Python 3 (standard library only).
- **Notion:** needs the Notion MCP connected in VS Code. Without it, paste the Ideas page and open To Do cards into the chat and write the verdicts back by hand.
- **Approval rules are unchanged:** nothing is committed or written to Notion without AC's OK.
