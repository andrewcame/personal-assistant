---
id: IMP-06
type: improvement
status: in-progress
horizon: next
updated: 2026-10-23
pillars: [P2]
focus: [automation]
goals: []
links: [CH-07, IMP-04]
people: []
---

# Improvement 06 - QA Knowledge And Coverage Baseline

## Context

- Functional and end-to-end knowledge needs a durable home so that coverage, handoffs, and new-starter onboarding do not depend on individual memory.
- A functional deep dive is being built in Miro. The QA area in Confluence also needs to be tidied and given a clear home for end-to-end results, test scripts, and known caveats.
- Jira placeholders are being established for metrics and automation coverage while a more robust reporting approach is developed. Jira remains the tracking source; Confluence and Miro provide the supporting definitions and functional context.

## Objective

- Establish a usable functional journey map in Miro and a maintainable QA reference in Confluence for end-to-end results, scripts, caveats, and links to Jira-based metrics and coverage tracking.
- Start with explicit known gaps and named locations; do not wait for an exhaustive catalogue before making the reference useful.

## Related

- Goal(s): [2026 goals](../goals/2026.md) - goals are still to be confirmed
- Role pillar(s): [Knowledge Sharing & Quality Practice](../context/role-pillars.md), [Stakeholder Confidence & Visibility](../context/role-pillars.md)
- Related improvement: [Jira QA Flow Metrics Baseline](04-jira-qa-flow-metrics-baseline.md)
- Related challenge: [Challenge 07 - End-to-End Quality Ownership And Continuity](../challenges/07-end-to-end-quality-ownership-and-continuity.md)
- Originating recommendation: Self

## Actions & Progress

### 2026-10-08

- Functional deep-dive work is underway in Miro.
- QA Confluence tidy-up is planned, including a home for end-to-end results, scripts, and known caveats.
- Jira placeholders for metrics and automation coverage are being set up; the detailed QA flow definitions remain tracked in [Improvement 04](04-jira-qa-flow-metrics-baseline.md).

### 2026-10-16 (ideas triage)

_From the Ideas triage on 2026-10-16 ([ideas log](../state/ideas-log.md))._

- **Cross-cutting apps:** some applications don't sit in one team's remit (e.g. IDS/Login, CEP). They need owned tests rather than fringe coverage from other teams' packs, which also reduces impact when changes are made for markets. Review the existing UI tests and consider switching them to Playwright.
- **Braze and CEP:** can these be automated? What is and isn't covered? Do we test emails and messages following member events?
- **Baseline results:** shoot for green — red should be the exception, not "OK".
- **Web checks:** confirm the quality of the Playwright front-end agents file and agentic work; can accessibility be automated (e.g. axe)? It may already be happening.
- **Backend pack gaps:** moved to [IMP-11](11-backend-test-pack-coverage.md).
- **Documentation:** organise QA notes so knowledge doesn't rely on people's memory — start in Confluence; consider AI documentation search; consolidate docs and to-do lists across teams; build Miro documentation through deep dives with the leads (how we test, what, who owns what, value/risk/coverage), using AI to connect the dots.
- **Shared config:** everyone runs packs locally — document what an `app.config` or `.env` should contain, and where configs are stored (is LastPass the place, and what can QAs access?). Review existing Pico backend tools that QA could use.

## Roadmap

| ID | Step | Owner | Depends on | Status |
|----|------|-------|------------|--------|
| IMP-06.1 | Build Miro functional QA board (first functional map) | AC | — | doing |
| IMP-06.2 | Decide home of QA docs and Confluence structure | AC | — | doing |
| IMP-06.3 | Create Confluence automation links page | AC | IMP-06.2 | doing |
| IMP-06.4 | Link references to Jira metrics and coverage items | AC | IMP-06.3, IMP-04.2 | later |
| IMP-06.5 | Draft first-pass coverage register | AC | IMP-06.1, CH-07.2 | later |
| IMP-06.6 | Create Confluence pages for the manual and automation packs and their run status | AC | IMP-06.2 | next |

## Status & Next Action

**Status:** In progress

**Next action:** Complete the first functional map, agree the Confluence structure for end-to-end material, and link each reference to the relevant Jira coverage or metrics item.

## Outcome

- Completed:
- Logged achievement: [to be added when delivered]