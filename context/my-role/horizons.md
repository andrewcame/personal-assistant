# Horizons — Now / Next / Later

_Replaces the time-boxed 30/60/90 day plan as the live plan from 2026-10-14. The original [30](30-day-plan.md), [60](60-day-plan.md) and [90](90-day-plan.md) day plans are kept as the onboarding record and as evidence for reviews; this file is what agents should treat as the current plan._

## Driving Theme

_Set 2026-09-30 from the leadership call on microsite sunset ([Leadership Direction](../leadership-direction.md)). If a new leadership signal could change this, Capture flags it as a possible theme change and AC decides; on change, update this section, `context/role-brief.md`, and add a Recent Decision in `state/now.md`._

**Leave it in a good place (provisional, from 2026-11-10).** The 2027 direction preview ([Leadership Direction, 2026-11-10](../leadership-direction.md)) moves all web and app technology to a third party and pivots the team to building agentic workflows for other areas of the business. Until it is confirmed (expected around the end of 2026), every live record is triaged as **finish**, **leave in a good place** (a clean, documented checkpoint) or **park**, and agentic-workflow capability is brought forward. The open questions are tracked in [CH-13](../../challenges/13-2027-business-direction-transition.md).

_Previous theme (2026-09-30 to 2026-11-10):_ **Get off the microsites.** Leadership has made microsite sunset the precondition for most investment, progression, and growth work ([Leadership Direction, 2026-09-30](../leadership-direction.md)). QA's job in this period is to make the Pico-fronted migration safe and fast, while keeping the people and capability work alive so it is ready on the other side.

_From 2026-11-16 (AC):_ the only live work is Pico in-flight tracking, 2027 readiness and training (IMP-19 QA in agentic business workflows), objectives for AC and the team (IMP-08), and AC's own agentic flow (IMP-05). Everything else is Legacy, with five carry-forward candidates in Later. The work may carry into early February 2027.

The four focus areas from the original plan still apply as the lens across every horizon:

| Focus Area       | What It Means                                            |
|------------------|----------------------------------------------------------|
| **People**       | Team engagement, knowledge sharing, technical leadership |
| **Ownership**    | Shift left, dev and QA alignment, cross-team quality     |
| **Automation**   | Reliability, confidence, coverage                        |
| **Productivity** | Better visibility, better tooling, reduce repetition     |

## How To Use This File

- Each item is an **outcome**, not a date. Move items between horizons as priorities change; mark them **Done** with a link to the achievement rather than deleting them.
- **Now** — actively being worked; should be small enough to name in a weekly update (limit 8, which `check.py` warns on).
- **Next** — agreed as worthwhile, starts when a Now item frees up capacity.
- **Later** — direction of travel; revisit quarterly.
- **Legacy** — kept but not planned (from 2026-11-16): no cards or roadmap duty; revive deliberately.
- Every item is carried by a challenge or improvement, which holds the detail. This file holds the plan, not the working notes.
- A plan item or job-spec gap with no record is a **source**: open an improvement or challenge for it (assumed required until you close it as already done). `check.py validate` errors on any row with no record.

## Now (short term)

_From 2026-11-16 Now is only: Pico in-flight work (tracking), 2027 readiness and training, objectives for AC and the team, and AC's own agentic flow (Next)._

| Outcome                                                                                                       | Focus      | Carried by                                                                             | Status                                                                                                   |
|---------------------------------------------------------------------------------------------------------------|------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Dynamic member creation available for Portal automation (Web MVP)                                             | Automation | [Improvement 02](../../improvements/02-dynamic-member-creation-and-test-data.md)       | In progress — tracking DA's Portal member creation initiative to the end; wider test-data work is Legacy |
| 2026 objectives recorded for AC and the team; calibration and EOY reviews delivered                           | People     | [Improvement 08](../../improvements/08-2026-objectives-calibration-and-eoy-reviews.md) | In progress — calibration session Wed 2026-11-18; update my own objectives ahead of EOY                  |
| 2027 direction transition: live work triaged; what of our ecosystem remains and team remit confirmed          | Ownership  | [Challenge 13](../../challenges/13-2027-business-direction-transition.md)              | Open — plan confirmed 2026-11-13; handover timeline next (CH-13.3)                                       |
| QA works with agentic business workflows (Foundry or similar): what is involved, how to test, automated tests | Automation | [Improvement 19](../../improvements/19-qa-in-agentic-business-workflows.md)            | In progress — first task: AC upskilling on Foundry                                                       |

## Next (mid term)

| Outcome                                                                               | Focus        | Carried by                                                         | Status                                                                                      |
|---------------------------------------------------------------------------------------|--------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Assistant harness improved; agentic-workflow capability built ahead of the 2027 pivot | Productivity | [Improvement 05](../../improvements/05-assistant-skill-backlog.md) | In progress — widened to AC's own agentic flow; evals baseline and Cloudflare AI trial next |

## Later (long term)

_Carry-forward candidates for the new role: bigger test improvements AC may bring forward once the 2027 remit is known._

| Outcome                                                                | Focus        | Carried by                                                                            | Status                                                                                       |
|------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| QA flow metrics baseline in Jira (one-team proof of concept)           | Productivity | [Improvement 04](../../improvements/04-jira-qa-flow-metrics-baseline.md)              | Carry-forward candidate for the new role (AC, 2026-11-16); no cards until the remit is known |
| QA engagement model agreed for paired, AI-assisted initiative delivery | Ownership    | [Challenge 11](../../challenges/11-qa-engagement-in-ai-paired-initiative-delivery.md) | Carry-forward candidate for the new role (AC, 2026-11-16); no cards until the remit is known |
| CI/CD quality gate model defined                                       | Automation   | [Improvement 14](../../improvements/14-ci-cd-quality-gate-model.md)                   | Carry-forward candidate for the new role (AC, 2026-11-16); no cards until the remit is known |
| Agentic AI test boilerplate generated from requirements                | Automation   | [Improvement 16](../../improvements/16-agentic-ai-test-boilerplate.md)                | Carry-forward candidate for the new role (AC, 2026-11-16); no cards until the remit is known |
| Business-language quality visibility before releases and launches      | Ownership    | [Improvement 17](../../improvements/17-business-language-quality-visibility.md)       | Carry-forward candidate for the new role (AC, 2026-11-16); no cards until the remit is known |

## Legacy

_Added 2026-11-16 at AC's review of every record. Kept for reference, not planned: no cards, no roadmap duty, left out of the stale report. Each record has a Legacy Value note. Revive by giving it a real status and horizon again. The work may carry into early February 2027, which is the main reason to revive._

| Outcome                                                                                                                   | Focus        | Carried by                                                                                                                                                                      | Status                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Staging monitoring and alerting has a clear owner and daily routine                                                       | Productivity | [Improvement 01](../../improvements/01-staging-monitoring-and-alerting-ownership.md)                                                                                            | Legacy (2026-11-16) — revive if the work carries into Feb 2027 or the new remit needs it |
| E2E knowledge captured as handover documentation (AI-assisted)                                                            | People       | [Challenge 07](../../challenges/07-end-to-end-quality-ownership-and-continuity.md)                                                                                              | Legacy (2026-11-16) — revive if the work carries into Feb 2027 or the new remit needs it |
| QA Chapter reset as an open Testing Chapter with a purpose in the Pico model and a champion                               | People       | [Improvement 13](../../improvements/13-qa-chapter-reset.md)                                                                                                                     | Legacy (2026-11-16) — takes shape once next year's team is known                         |
| NFR partnership with Head of SE and Principal SE; NFR coverage visible                                                    | Ownership    | [Improvement 03](../../improvements/03-front-end-load-and-performance-testing.md)                                                                                               | Legacy (2026-11-16) — revive if the work carries into Feb 2027 or the new remit needs it |
| Stakeholder coverage cadence with Finance and commercial teams                                                            | Ownership    | [Challenge 02](../../challenges/02-direct-business-stakeholder-connection.md)                                                                                                   | Legacy (2026-11-16) — revive if the work carries into Feb 2027 or the new remit needs it |
| Growth headroom and talent pipeline (Staff QA route for the Web leads, wider pipeline)                                    | People       | [Challenge 05](../../challenges/05-qa-growth-headroom-and-talent-pipeline.md)                                                                                                   | Legacy (2026-11-16) — revive if the work carries into Feb 2027 or the new remit needs it |
| Hiring, onboarding and QA talent pipeline view                                                                            | People       | [Improvement 15](../../improvements/15-hiring-onboarding-and-qa-talent-pipeline.md)                                                                                             | Legacy (2026-11-16) — takes shape once next year's team is known                         |
| First-pass coverage register (journey, market, repo, owner, cadence, gap)                                                 | Automation   | [Improvement 06](../../improvements/06-qa-knowledge-and-coverage-baseline.md)                                                                                                   | Legacy (2026-11-16) — revive if the work carries into Feb 2027 or the new remit needs it |
| Join journey tested as simulated Facebook and Instagram in-app browser traffic                                            | Automation   | [Improvement 18](../../improvements/18-in-app-browser-join-journey-test.md)                                                                                                     | Legacy (2026-11-16) — revive if the work carries into Feb 2027 or the new remit needs it |
| Backend test pack covers priority services                                                                                | Automation   | [Improvement 11](../../improvements/11-backend-test-pack-coverage.md)                                                                                                           | Legacy (2026-11-16) — revive if the work carries into Feb 2027 or the new remit needs it |
| Mobile App has appropriate, reliable test coverage (Phase 1: stabilise existing tests; Phase 2: population-scale testing) | Automation   | [Challenge 09](../../challenges/09-population-scale-mobile-app-testing.md)                                                                                                      | Legacy (2026-11-16) — revive if the work carries into Feb 2027 or the new remit needs it |
| Domain ownership model for automation code; flaky-pack response agreed                                                    | Ownership    | [Improvement 12](../../improvements/12-domain-ownership-model-for-automation-code.md)                                                                                           | Legacy (2026-11-16) — revive if the work carries into Feb 2027 or the new remit needs it |
| Test data strategy agreed across teams (beyond the Portal MVP)                                                            | Automation   | [Improvement 02](../../improvements/02-dynamic-member-creation-and-test-data.md), [Challenge 10](../../challenges/10-pico-source-of-truth-and-exerp-dependent-test-strategy.md) | Legacy (2026-11-16) — revive if the work carries into Feb 2027 or the new remit needs it |
| Defined, risk-based process for Exerp release and upgrade testing                                                         | Ownership    | [Challenge 12](../../challenges/12-exerp-release-testing-process.md), [Improvement 09](../../improvements/09-exerp-release-testing-process.md)                                  | Legacy (2026-11-16) — revive if the work carries into Feb 2027 or the new remit needs it |
| Payments QA cross-training and cover                                                                                      | People       | [Improvement 07](../../improvements/07-payments-qa-cross-training-and-cover.md)                                                                                                 | Legacy (2026-11-16) — revive if the work carries into Feb 2027 or the new remit needs it |

## Carried Over From The 30-Day Close-Out

The day-30 close-out actions are absorbed above (coverage register, environment/test-data baseline, QA flow baseline, direct-report deep dives, E2E knowledge transfer, Chapter purpose). Tick them off in [30-day-plan.md](30-day-plan.md) only if you want the onboarding record completed; this file is where progress is tracked.

## Done Or Closed

| Outcome | Carried by | Result |
|---|---|---|
| Mobile automation platform decided (Appium) | [Challenge 01](../../challenges/01-mobile-automation-strategy.md) | Resolved 2026-10-15 — achievement logged |
| Working within in-house architecture decisions | [Challenge 03](../../challenges/03-in-house-architecture-decisions.md) | Closed as accepted 2026-10-15 — no outcome to log |
| Web QA capacity and accountability | [Challenge 04](../../challenges/04-web-qa-capacity-and-accountability.md) | Closed 2026-10-27 — TMW on Web, DA owning Portal member creation; monitoring is BAU — achievement and team evidence logged |
| BrowserStack renewal: about $3k saving negotiated; licence runs one more year, not renewed after | [Improvement 10](../../improvements/10-browserstack-renewal-and-device-strategy.md) | Done 2026-11-16 — achievement logged |
