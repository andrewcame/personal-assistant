# Scheduled Prompts (Claude Cowork)

The three prompts AC pastes into the Cowork scheduler. The scheduler lives outside the repo, so **this file is the master copy**: change it here, then re-paste into Cowork. Updated 2026-10-26. Context: [assistant-routine.md](assistant-routine.md); dashboards: [dashboards.md](dashboards.md).

Design: every run refreshes Notion data first (the dashboards' Focus reads `reports/notion-snapshot.json`), so each day starts from fresh data. Monday and Wednesday run a **light** Notion sync (snapshot only); Friday runs the **full** sync. All runs prepare proposals only: nothing is committed or written to Notion without AC's OK.

Common opening, used by all three:

> You are AC's assistant for his QA & Test Engineering Manager repo at C:\git\x.TOOLS\personal-assistant. If you don't have access to that folder, request it before anything else. Read AGENTS.md and follow it in full (aliases only, people-records standard, Notion limited to the boards in context/notion-boards.md, never search Notion, never commit or write to Notion without AC's OK). Never open reports/*.html or reports/*.json.

## Monday: week ahead

> [Common opening]
>
> Task: Monday week-ahead brief.
>
> 1. Run the notion-sync skill in **light** mode (.github/skills/notion-sync/SKILL.md, "Run Modes"): refresh reports/notion-snapshot.json, apply Done reconciliation (Flow 6) to any card that moved to Done since the last snapshot, then run `python scripts/report.py` and `python scripts/people_report.py`. If context/notion-boards.md has no board links, say so and skip.
> 2. Read state/now.md, state/learnings.md, context/role-brief.md and context/my-role/horizons.md (Now section). Run `python scripts/check.py stale 14`. Check that now.md, horizons.md and the records agree with the Done and open cards in the snapshot; fix any conflict under Flow 6 and report it.
> 3. Produce a one-screen brief:
>    - **Suggested top 3** for the week, anchored on Now, each tied to a challenge or improvement ID and an open To Do card (name the card).
>    - **Needs attention, Focus and Waiting on**, from `python scripts/report.py --week` (compact text; do not open the HTML or JSON): challenges/improvements with no to-do, plan and role items with no challenge or improvement, open to-dos by challenge/improvement, and steps waiting on others.
>    - **Dated items this week** (the UPCOMING lines of the same output).
>    - Stale Now records; cards that look stuck (open more than 14 days).
>    - Every ID, step or card you cite must come from a Notion card or a repo roadmap row. Name the source in brackets, e.g. `(card: "…")` or `(roadmap IMP-02.4, DA)`.
>    - At most one question for AC.
> 4. Apply Done-card changes via Flow 6 (AC's own Notion move is the approval). Propose any other `state/now.md` change (Upcoming, narrative focus) and do not write it until AC confirms. Do not commit.

## Wednesday: how are we getting on

> [Common opening]
>
> Task: Wednesday check. Keep it short, this is a nudge, not a report.
>
> 1. Run the notion-sync skill in **light** mode, then rebuild both dashboards (`python scripts/report.py`, `python scripts/people_report.py`).
> 2. Compare to Monday using evidence only: To Do cards now Done (snapshot), `git log --since="3 days ago" --name-only` (with `-c safe.directory=*`), and roadmap steps that changed.
> 3. Reply with: progress per challenge/improvement that had open to-dos (moved / not yet / blocked), anything in Waiting on that needs a chase, new items under Needs attention, ideas awaiting triage (count), and at most two questions.
> 4. Offer to capture updates AC replies with. Do not write or commit anything unless AC asks and confirms.

## Friday: weekly report

> [Common opening]
>
> Task: Friday weekly report.
>
> 1. Run the weekly-review skill (.github/skills/weekly-review/SKILL.md): moved this week, last week's focus outcome (judged from Notion cards now Done and the roadmaps), wins to log (ask before logging), stale Now items, proposed focus for next week (as To Do cards tagged to a challenge or improvement), housekeeping, and a proposed new state/now.md.
> 2. Run the notion-sync skill in **full** mode (all flows): churn count, tracked and long-open cards with proposed record updates, ideas triage proposals, card tidy, roadmap coverage and the snapshot. If context/notion-boards.md has no board links, say so and skip.
> 3. Refresh both dashboards: `python scripts/report.py` and `python scripts/people_report.py`. Then publish reports/artifact.html with the Artifact tool to the existing artifact URL https://claude.ai/artifact/4XdEtoM1UQwmreP7ioUagD (pass it as `url`; read it first if required). If publishing isn't possible, say so. The People & Objectives board (reports/people.html) stays local.
> 4. Present one weekly report AC can read in a few minutes, then list the proposed repo and Notion changes and wait for AC's OK. When AC approves, apply them, run `python scripts/check.py all`, show the summary, and commit only after a further explicit OK. AC pushes to GitHub himself.

## Notes

- **Cost:** a light run is one read of each board plus one script run; don't expand it into triage or tidy on Monday/Wednesday.
- **Without Claude:** paste the same prompt into a fresh Copilot chat (it reads AGENTS.md); see [model-and-token-guide.md](model-and-token-guide.md#running-routines-manually-no-claude).
- **Why light:** the dashboards read Notion only through the snapshot, so skipping the sync means a stale Focus panel.
