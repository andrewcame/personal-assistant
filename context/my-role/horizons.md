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
- **Now** — actively being worked; should be small enough to name in a weekly update (aim for ≤ 5).
- **Next** — agreed as worthwhile, starts when a Now item frees up capacity.
- **Later** — direction of travel; revisit quarterly.
- Link each item to the challenge, improvement, or initiative that carries the detail. This file holds the plan, not the working notes.

## Now (short term)

| Outcome | Focus | Carried by | Status |
|---|---|---|---|
| Dynamic member creation available for Portal automation (Web MVP) | Automation | [Initiative 01](../../initiatives/01-portal-dynamic-member-creation.md), [Improvement 02](../../improvements/02-dynamic-member-creation-and-test-data.md) | Draft — AC helping DA refine for kick-off; needs sponsor |
| Staging monitoring and alerting has a clear owner and daily routine | Productivity | [Improvement 01](../../improvements/01-staging-monitoring-and-alerting-ownership.md) | In progress — walkthrough done; AC running checks; explore Claude for manual SRE |
| QA engagement model agreed for paired, AI-assisted initiative delivery | Ownership | [Challenge 11](../../challenges/11-qa-engagement-in-ai-paired-initiative-delivery.md) | Open |
| 2026 objectives recorded for AC and the team; calibration and EOY reviews delivered | People | [Improvement 08](../../improvements/08-2026-objectives-calibration-and-eoy-reviews.md) | In progress — calls being booked; calibration 2026-11-11 |
| BrowserStack renewed at lower cost; device strategy for mobile automation reviewed | Productivity | [Improvement 10](../../improvements/10-browserstack-renewal-and-device-strategy.md) | In progress — account-manager call booked; renewal November |
| Assistant harness improved and used weekly (quick wins) | Productivity | [Improvement 05](../../improvements/05-assistant-skill-backlog.md) | In progress — evals baseline and first cross-review next |

## Next (mid term)

_Mostly the original 60-day "stabilise and reduce friction" intent, re-sequenced behind microsite work._

| Outcome | Focus | Carried by | Status |
|---|---|---|---|
| First-pass coverage register (journey, market, repo, owner, cadence, gap) | Automation | [Improvement 06](../../improvements/06-qa-knowledge-and-coverage-baseline.md) | In progress |
| QA flow metrics baseline in Jira (one-team proof of concept) | Productivity | [Improvement 04](../../improvements/04-jira-qa-flow-metrics-baseline.md) | In progress |
| Domain ownership model for automation code; flaky-pack response agreed | Ownership | — | Not started |
| Test data strategy agreed across teams (beyond the Portal MVP) | Automation | [Improvement 02](../../improvements/02-dynamic-member-creation-and-test-data.md), [Challenge 10](../../challenges/10-pico-source-of-truth-and-exerp-dependent-test-strategy.md) | Not started |
| Defined, risk-based process for Exerp release and upgrade testing | Ownership | [Challenge 12](../../challenges/12-exerp-release-testing-process.md), [Improvement 09](../../improvements/09-exerp-release-testing-process.md) | Not started — discuss with leads |
| AI-led Appium first pass expands coverage of high-value mobile journeys | Automation | [Initiative 02](../../initiatives/02-appium-ai-led-first-pass.md) | On hold — re-scope after app simplification plan (kick-off w/c 2026-10-19) |
| E2E knowledge transfer and continuity (AI-assisted) | People | [Challenge 07](../../challenges/07-end-to-end-quality-ownership-and-continuity.md) | Open — LM extended into 2027 |
| CI/CD quality gate model defined | Automation | — | Not started |

## Later (long term)

_Mostly the original 90-day "build capability and momentum" intent._

| Outcome | Focus | Carried by | Status |
|---|---|---|---|
| QA Chapter reset as an open Testing Chapter with a purpose in the Pico model and a champion | People | — | Deferred (behind chapter reset) |
| NFR partnership with Head of SE and Principal SE; NFR coverage visible | Ownership | [Improvement 03](../../improvements/03-front-end-load-and-performance-testing.md) | Not started |
| Web and App ownership model holds; Join / Portal split decided in 2027 planning | People | [Challenge 04](../../challenges/04-web-qa-capacity-and-accountability.md) | Active monitoring — TMW + DA on Web; KB App lead |
| Payments QA cross-training and cover | People | [Improvement 07](../../improvements/07-payments-qa-cross-training-and-cover.md) | Not started — JFG backfill plan with TMW; behind sunset work |
| Population-scale mobile testing approach for low-incidence defects | Automation | [Challenge 09](../../challenges/09-population-scale-mobile-app-testing.md) | Open |
| Stakeholder coverage cadence with Finance and commercial teams | Ownership | [Challenge 02](../../challenges/02-direct-business-stakeholder-connection.md) | Open |

## Carried Over From The 30-Day Close-Out

The day-30 close-out actions are absorbed above (coverage register, environment/test-data baseline, QA flow baseline, direct-report deep dives, E2E knowledge transfer, Chapter purpose). Tick them off in [30-day-plan.md](30-day-plan.md) only if you want the onboarding record completed; this file is where progress is tracked.

## Done Or Closed

| Outcome | Carried by | Result |
|---|---|---|
| Mobile automation platform decided (Appium) | [Challenge 01](../../challenges/01-mobile-automation-strategy.md) | Resolved 2026-10-15 |
| Growth headroom and talent pipeline | [Challenge 05](../../challenges/05-qa-growth-headroom-and-talent-pipeline.md) | Resolved for now 2026-10-15 — revisit in 2027 planning |
| Working within in-house architecture decisions | [Challenge 03](../../challenges/03-in-house-architecture-decisions.md) | Closed as accepted 2026-10-15 |
