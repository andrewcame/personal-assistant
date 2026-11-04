# Scheduled Prompts (Claude Cowork)

The three prompts AC pastes into the Cowork scheduler. The scheduler lives outside the repo, so **this file is the master copy**: change it here, then re-paste into Cowork. Updated 2026-11-04. Context: [assistant-routine.md](assistant-routine.md); dashboards: [dashboards.md](dashboards.md).

Design: every run refreshes Notion data first (the dashboards' Focus reads `reports/notion-snapshot.json`), so each day starts from fresh data. Monday and Wednesday run a **light** Notion sync (snapshot plus Done reconciliation, Flow 6); Friday runs the **full** sync. A card AC has moved to Done in Notion is applied to the repo directly (Flow 6), and Notion card writes (create, retag, column fixes) are applied and listed afterwards; everything else is a proposal: nothing is committed without AC's OK, and deleting, archiving or moving a card to Done in Notion needs it too.

## Suggested Models (credit use)

Set per scheduled task in Cowork. Tiers follow the [model and token guide](model-and-token-guide.md); check current multipliers in the picker.

| Job | Suggested model | Reasoning effort | Why |
|---|---|---|---|
| Monday | **Sonnet-class** | default | Grounded top 3 tied to real cards, plus Flow 6 repo edits |
| Wednesday | **Haiku-class** | low | A nudge built from evidence: sync, `git log`, compare against the snapshot. Biggest saving |
| Friday | **Sonnet-class** | default | Ideas triage and enrichment, weekly review, card tidy, all under the people-records standard |

Use Opus-class only for calibration prep and the monthly horizon review, not these runs. If a Haiku Wednesday invents an ID or card, move it to Sonnet; the "name the source" rule in the prompt is the guard.

Common opening, used by all three:

> You are AC's assistant for his QA & Test Engineering Manager repo at C:\git\x.TOOLS\personal-assistant. If you don't have access to that folder, request it before anything else. Read AGENTS.md and follow it in full (aliases only, people-records standard, Notion limited to the boards in context/notion-boards.md, never search Notion, never commit without AC's OK; Notion card writes are applied and listed afterwards). Never open reports/*.html or reports/*.json.

## Monday: week ahead

> [Common opening]
>
> Task: Monday week-ahead brief.
>
> 1. Run the notion-sync skill in **light** mode (.github/skills/notion-sync/SKILL.md, "Run Modes"): refresh reports/notion-snapshot.json, apply Done reconciliation (Flow 6) to any card that moved to Done since the last snapshot, then run `python scripts/report.py` and `python scripts/people_report.py`. If context/notion-boards.md has no board links, say so and skip.
> 2. Read state/now.md, state/learnings.md and context/my-role/horizons.md (Now section). Run `python scripts/check.py stale 14`. Check that now.md, horizons.md and the records agree with the Done and open cards in the snapshot; fix any conflict under Flow 6 and report it.
> 3. Produce a one-screen brief:
>    - **Suggested top 3** for the week, anchored on Now, each tied to a challenge or improvement ID and an open To Do card (name the card).
>    - **Needs attention and Focus**, from `python scripts/report.py --week` (compact text; do not open the HTML or JSON): challenges/improvements with no to-do, and open to-dos by challenge/improvement. For steps owned by others and which tasks are not yet on Notion, use `python scripts/report.py --tasks`.
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
> 1. Run the notion-sync skill in **light** mode (.github/skills/notion-sync/SKILL.md, "Run Modes"): refresh reports/notion-snapshot.json, apply Done reconciliation (Flow 6) to any card that moved to Done since the last snapshot, then rebuild both dashboards (`python scripts/report.py`, `python scripts/people_report.py`). If context/notion-boards.md has no board links, say so and skip.
> 2. Compare to Monday using evidence only: To Do cards now Done (snapshot), `git log --since="3 days ago" --name-only` (with `-c safe.directory=*`), and roadmap steps that changed. Use `python scripts/report.py --week` for the current Focus and Needs attention and `--tasks` for steps owned by others (do not open the HTML or JSON).
> 3. Reply with: progress per challenge/improvement that had open to-dos (moved / not yet / blocked), steps owned by others that need a chase, new items under Needs attention, ideas awaiting triage (count), and at most two questions. Every ID, step or card you cite must come from a Notion card or a repo roadmap row; name the source in brackets, e.g. `(card: "…")` or `(roadmap IMP-02.4, DA)`.
> 4. Apply Done-card changes via Flow 6 (AC's own Notion move is the approval). Offer to capture any other updates AC replies with. Do not write anything else or commit unless AC asks and confirms.

## Friday: weekly report

> [Common opening]
>
> Task: Friday weekly report.
>
> 1. Run the weekly-review skill (.github/skills/weekly-review/SKILL.md): moved this week, last week's focus outcome (judged from Notion cards now Done and the roadmaps), wins to log (ask before logging), stale Now items, proposed focus for next week (as To Do cards tagged to a challenge or improvement), housekeeping, and a proposed new state/now.md.
> 2. Run the notion-sync skill in **full** mode (all six flows, including Done reconciliation, Flow 6): churn count, tracked and long-open cards with proposed record updates, ideas triage proposals, card tidy, roadmap coverage and the snapshot. If context/notion-boards.md has no board links, say so and skip.
> 3. Refresh both dashboards: `python scripts/report.py` and `python scripts/people_report.py`. Then publish reports/artifact.html with the Artifact tool to the existing artifact URL https://claude.ai/artifact/4XdEtoM1UQwmreP7ioUagD (pass it as `url`; read it first if required). If publishing isn't possible, say so. The People & Objectives board (reports/people.html) stays local.
> 4. Present one weekly report AC can read in a few minutes. List the Notion card writes already applied, then the proposed repo changes (and any deletes, archiving or moves to Done in Notion) and wait for AC's OK. When AC approves, apply them, run `python scripts/check.py all`, show the summary, and commit only after a further explicit OK. AC pushes to GitHub himself.

## Notes

- **Cost:** a light run is one read of each board plus one script run; don't expand it into triage or tidy on Monday/Wednesday.
- **Without Claude:** paste the same prompt into a fresh Copilot chat (it reads AGENTS.md); see [model-and-token-guide.md](model-and-token-guide.md#running-routines-manually-no-claude).
- **Why light:** the dashboards read Notion only through the snapshot, so skipping the sync means a stale Focus panel.
