# QA Health Summary

Last updated: 2026-10-14

Team-level view of QA/Test Engineering health. Individual detail lives in `team/<alias>.md` (see [team/README.md](../team/README.md)) and in the dashboard's Team section. The September 2026 baseline, which predates the 2026-10-08 reassignment, is kept in [archive/qa-health-summary-2026-09.md](archive/qa-health-summary-2026-09.md).

## Current Team Shape

Changes on 2026-10-08: KB moved to Mobile App as its sole QA, TMW moved to Website (Web Team Two), and IY joined as a floating contractor.

| Platform       | Aliases                                      |
|----------------|----------------------------------------------|
| Website        | DA (Lead), TMW (Lead, Web Team Two), JS, JFG |
| Mobile App     | KB (sole QA)                                 |
| Payments       | MP (sole QA)                                 |
| All (E2E)      | LM (contractor)                              |
| All (Floating) | IY (contractor; reporting line TBC)          |

## Team-Level Themes

These held in the September baseline and still apply after the reassignment.

- **Progression clarity** — evidence expectations and routes between levels (including a technical, non-management Lead route and the Level 7 to 8 step) need making explicit; growth is currently held behind microsite sunset.
- **Automation trust** — the front-end pack acts as the de facto end-to-end safety net; its scope, ownership, and reliability need confirming before more weight is put on it.
- **Environments and test data** — preview-to-staging connections, thin staging variety, and unreliable source data slow end-to-end testing and blur defect vs environment failures.
- **Staging health visibility** — there is no shared, visible signal of staging health, which makes release decisions harder.
- **Capacity and single-QA coverage** — Mobile App and Payments each have one QA; end-to-end knowledge sits with a contractor and needs to be documented and spread.
- **End-to-end ownership** — component testing and the old microsite split leave gaps between services; checking Exerp, database state, and member comms should be normal practice.
- **Communication routes** — decision routes and technical-lead responsibilities in Web teams are still settling; ticket test notes need concrete steps and expected outcomes.
- **Knowledge concentration** — Payments, Exerp/BGW release, and staging promotions knowledge is held informally by a few people.
- **Speed versus quality, and AI use** — the most common complaint in conference conversations (2026-10-21) was the tension between speed and quality and the over-use of AI; the QA approach needs to address it explicitly (see [CH-11](../challenges/11-qa-engagement-in-ai-paired-initiative-delivery.md)).

## Open Team-Level Questions

- How should QA engage in paired, AI-assisted initiative delivery ([Challenge 11](../challenges/11-qa-engagement-in-ai-paired-initiative-delivery.md))?
- How should end-to-end ownership work if the E2E contractor engagement ends ([Challenge 07](../challenges/07-end-to-end-quality-ownership-and-continuity.md))?
- Is Website QA capacity and reporting aligned with Web 1/2/3 after the moves ([Challenge 04](../challenges/04-web-qa-capacity-and-accountability.md))?
- What growth routes exist while progression is held behind microsite sunset ([Challenge 05](../challenges/05-qa-growth-headroom-and-talent-pipeline.md))?
- Where should the floating contractor be placed for the most impact?
- Should test data be created on demand or kept by default for priority journeys?
