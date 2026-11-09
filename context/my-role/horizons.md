# Horizons — Now / Next / Later

_Replaces the time-boxed 30/60/90 day plan as the live plan from 2026-10-14. The original [30](30-day-plan.md), [60](60-day-plan.md) and [90](90-day-plan.md) day plans are kept as the onboarding record and as evidence for reviews; this file is what agents should treat as the current plan._

## Driving Theme

_Set 2026-09-30 from the leadership call on microsite sunset ([Leadership Direction](../leadership-direction.md)). If a new leadership signal could change this, Capture flags it as a possible theme change and AC decides; on change, update this section, `context/role-brief.md`, and add a Recent Decision in `state/now.md`._

**Get off the microsites.** Leadership has made microsite sunset the precondition for most investment, progression, and growth work ([Leadership Direction, 2026-09-30](../leadership-direction.md)). QA's job in this period is to make the Pico-fronted migration safe and fast, while keeping the people and capability work alive so it is ready on the other side.

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
- Every item is carried by a challenge or improvement, which holds the detail. This file holds the plan, not the working notes.
- A plan item or job-spec gap with no record is a **source**: open an improvement or challenge for it (assumed required until you close it as already done). `check.py validate` errors on any row with no record.

## Now (short term)

| Outcome                                                                                                                   | Focus        | Carried by                                                                             | Status                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------|--------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dynamic member creation available for Portal automation (Web MVP)                                                         | Automation   | [Improvement 02](../../improvements/02-dynamic-member-creation-and-test-data.md)       | In progress — AC sponsoring; tickets approved 2026-10-23, kick-off done 2026-10-26; DA scoping the plan                                                    |
| Staging monitoring and alerting has a clear owner and daily routine                                                       | Productivity | [Improvement 01](../../improvements/01-staging-monitoring-and-alerting-ownership.md)   | In progress — AC running checks manually; next: DLQ issues and AI-run checks                                                                               |
| 2026 objectives recorded for AC and the team; calibration and EOY reviews delivered                                       | People       | [Improvement 08](../../improvements/08-2026-objectives-calibration-and-eoy-reviews.md) | In progress — objectives calls held; calibration prep 2026-11-09, calibration 2026-11-11                                                                   |
| BrowserStack renewed at lower cost; device strategy for mobile automation reviewed                                        | Productivity | [Improvement 10](../../improvements/10-browserstack-renewal-and-device-strategy.md)    | In progress — call held 2026-10-19; plan list awaited from BrowserStack; renewal 2026-11-22 (confirmed)                                                    |
| QA flow metrics baseline in Jira (one-team proof of concept)                                                              | Productivity | [Improvement 04](../../improvements/04-jira-qa-flow-metrics-baseline.md)               | In progress                                                                                                                                                |
| Backend test pack covers priority services (Exerp Assistant first)                                                        | Automation   | [Improvement 11](../../improvements/11-backend-test-pack-coverage.md)                  | In progress — gap review done; set up initiative with TMW and JFG by 2026-11-13                                                                            |
| Mobile App has appropriate, reliable test coverage (Phase 1: stabilise existing tests; Phase 2: population-scale testing) | Automation   | [Challenge 09](../../challenges/09-population-scale-mobile-app-testing.md)             | Open — rescoped 2026-10-27; epics APP-352 (stabilise) and APP-353 (pipelines) raised; app simplification tickets received; next: kick off epic 1 (APP-352) |

## Next (mid term)

_Mostly the original 60-day "stabilise and reduce friction" intent, re-sequenced behind microsite work._

| Outcome | Focus | Carried by | Status |
|---|---|---|---|
| Domain ownership model for automation code; flaky-pack response agreed | Ownership | [Improvement 12](../../improvements/12-domain-ownership-model-for-automation-code.md) | Not started |
| Test data strategy agreed across teams (beyond the Portal MVP) | Automation | [Improvement 02](../../improvements/02-dynamic-member-creation-and-test-data.md), [Challenge 10](../../challenges/10-pico-source-of-truth-and-exerp-dependent-test-strategy.md) | Not started |
| Defined, risk-based process for Exerp release and upgrade testing | Ownership | [Challenge 12](../../challenges/12-exerp-release-testing-process.md), [Improvement 09](../../improvements/09-exerp-release-testing-process.md) | Not started — discuss with leads |
| E2E knowledge transfer and continuity (AI-assisted) | People | [Challenge 07](../../challenges/07-end-to-end-quality-ownership-and-continuity.md) | Open — LM extended into 2027 |
| Payments QA cross-training and cover | People | [Improvement 07](../../improvements/07-payments-qa-cross-training-and-cover.md) | Not started — JFG backfill plan with TMW |

## Later (long term)

_Mostly the original 90-day "build capability and momentum" intent._

| Outcome                                                                                     | Focus        | Carried by                                                                            | Status                                                                                   |
|---------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| QA Chapter reset as an open Testing Chapter with a purpose in the Pico model and a champion | People       | [Improvement 13](../../improvements/13-qa-chapter-reset.md)                           | Deferred (behind chapter reset)                                                          |
| NFR partnership with Head of SE and Principal SE; NFR coverage visible                      | Ownership    | [Improvement 03](../../improvements/03-front-end-load-and-performance-testing.md)     | Not started                                                                              |
| Stakeholder coverage cadence with Finance and commercial teams                              | Ownership    | [Challenge 02](../../challenges/02-direct-business-stakeholder-connection.md)         | Open                                                                                     |
| Growth headroom and talent pipeline (Staff QA route for the Web leads, wider pipeline)      | People       | [Challenge 05](../../challenges/05-qa-growth-headroom-and-talent-pipeline.md)         | Open — KB's move unlocked his growth; other bottlenecks remain; revisit at 2027 planning |
| QA engagement model agreed for paired, AI-assisted initiative delivery                      | Ownership    | [Challenge 11](../../challenges/11-qa-engagement-in-ai-paired-initiative-delivery.md) | Open — interim model tentatively agreed: QA does one e2e ticket once coding is done      |
| Assistant harness improved and used weekly (quick wins)                                     | Productivity | [Improvement 05](../../improvements/05-assistant-skill-backlog.md)                    | In progress — evals baseline and first cross-review next                                 |
| CI/CD quality gate model defined                                                            | Automation   | [Improvement 14](../../improvements/14-ci-cd-quality-gate-model.md)                   | Not started                                                                              |
| Hiring, onboarding and QA talent pipeline view                                              | People       | [Improvement 15](../../improvements/15-hiring-onboarding-and-qa-talent-pipeline.md)   | Not started — 2027 planning                                                              |
| Agentic AI test boilerplate generated from requirements                                     | Automation   | [Improvement 16](../../improvements/16-agentic-ai-test-boilerplate.md)                | Not started                                                                              |
| Business-language quality visibility before releases and launches                           | Ownership    | [Improvement 17](../../improvements/17-business-language-quality-visibility.md)       | Not started                                                                              |
| First-pass coverage register (journey, market, repo, owner, cadence, gap)                   | Automation   | [Improvement 06](../../improvements/06-qa-knowledge-and-coverage-baseline.md)         | In progress — moved to Later 2026-11-06 (less urgent than other Now work)                |

## Carried Over From The 30-Day Close-Out

The day-30 close-out actions are absorbed above (coverage register, environment/test-data baseline, QA flow baseline, direct-report deep dives, E2E knowledge transfer, Chapter purpose). Tick them off in [30-day-plan.md](30-day-plan.md) only if you want the onboarding record completed; this file is where progress is tracked.

## Done Or Closed

| Outcome | Carried by | Result |
|---|---|---|
| Mobile automation platform decided (Appium) | [Challenge 01](../../challenges/01-mobile-automation-strategy.md) | Resolved 2026-10-15 — achievement logged |
| Working within in-house architecture decisions | [Challenge 03](../../challenges/03-in-house-architecture-decisions.md) | Closed as accepted 2026-10-15 — no outcome to log |
| Web QA capacity and accountability | [Challenge 04](../../challenges/04-web-qa-capacity-and-accountability.md) | Closed 2026-10-27 — TMW on Web, DA owning Portal member creation; monitoring is BAU — achievement and team evidence logged |
