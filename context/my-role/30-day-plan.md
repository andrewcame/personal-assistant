# 30-Day Plan: Listen, Understand, Establish Baselines

> **Archived onboarding record.** The live plan is now [horizons.md](horizons.md) (Now / Next / Later). Keep this file as review evidence; don't add new progress here.

## Strategic Framework

Before any of the three phases, four focus areas were established as the lens for the entire transformation. These apply across all 90 days.

| Focus Area      | What It Means                                             |
|-----------------|-----------------------------------------------------------|
| **People**      | Team engagement, knowledge sharing, technical leadership  |
| **Ownership**   | Shift left, dev and QA alignment, cross-team quality      |
| **Automation**  | Reliability, confidence, coverage                         |
| **Productivity**| Better visibility, better tooling, reduce repetition      |

The intent: improve engagement, strengthen quality ownership, rebuild trust in automation, and remove unnecessary friction — so teams can deliver with confidence.

---

## Phase Intent

Do not change anything yet. The first 30 days are about listening, understanding where the pain points are, and creating enough visibility to make informed decisions rather than assumptions. A lot of great work is already underway in delivery and engineering — any action taken must be in step with that, not pulling against it. The team has information available but is not yet turning it into useful knowledge. So: listen, understand, and baseline.

## Build Relationships

- Start with QA leads, team leads, delivery leads, and engineering leads — prioritise those not yet interacted with to get an unfiltered perspective
- Look for common themes across conversations; repeated frustrations help set priority
- Hold a reset call with the full QA team to establish the new dynamic, provide stability, and understand where people are on process
- Structure every conversation around four questions: What motivates you? What do you enjoy? What frustrates you? Where do you want to go?
- Use either an engagement survey or 1:1s — the format matters less than the coverage; speak to the entire team
- Understand current AI adoption and where the team is already seeing value
- Engage business stakeholders (Finance, Commercial, market teams) to understand what confidence means to them — payment reliability, conversion-critical journeys, and market launches are different conversations but both matter
- Make it clear what stakeholders can expect from the role; trust works both ways
- Avoid turning these into status updates — use them to understand risk appetite, expectations, and where confidence is lacking
- Ask for help identifying who to talk to and which meetings to join

## Access Quality Health

- Build an automation health baseline: understand what automation exists, what it covers, how reliable it is, and whether people trust the results; deep-dive with each lead and drive ownership from them
- Track execution runs per repo over time — surface whether this information is easy to access across web, app, and payments
- Include international market coverage in the baseline — which markets are actually covered by automation and which rely on manual effort or are untested?
- Assess environment health: how often are previews or builds causing delays? What is available on each environment? Health checks are a meaningful output here
- Assess test data: understand how data is created, refreshed, and maintained today, and whether it is helping or slowing down delivery; map what is needed versus what exists as a starting point for a later strategy
- Understand where each QA lead sits on the growth framework — what development goals exist, what progress has been made, and whether any promotion cases are in flight; this is the baseline for owning their progression

## Evaluate Delivery

- Review the flow of work through QA: are we holding things up, catching things, or are we optimal?
- Assess how Kanban has landed with QAs — is work more steady than under Scrum? Are queues reducing? Do QAs always have something to work on? How often is Dev Test being used and is it effective?
- Understand where time is actually being spent: testing and analysis, or waiting on environments, data, clarification, or builds? Delays are often where the biggest opportunities are
- Identify the time sinks and bottlenecks — use data and conversations together before drawing conclusions

## Outputs

- Clear view of team sentiment, capability, and direction
- Automation, environment, and test data baseline — including international market coverage gaps
- Understanding of how Kanban is working from a QA perspective
- List of key risks and bottlenecks
- Prioritised set of opportunities and quick wins
- Established relationships across engineering, delivery, and key business stakeholders
- Growth framework snapshot for each QA lead

## Day 30 Review — 2026-09-30

This review records progress against the original listening and baseline intent. It distinguishes completed work from baselines that are still growing and work deliberately deferred to the wider operating-model reset.

### Done

- Completed conversations with the full QA team and held a wider team reset. The current meeting cadence is in place.
- Established working relationships across engineering and Configuration, with initial business engagement. Broader visibility and stakeholder relationships remain ongoing work.
- Identified the initial strategic priorities: dynamic member creation and Appium automation, both aligned to the mission to sunset Microsites. The corresponding initiatives are ready for refinement.
- Established a personal staging-health tracking mechanism to monitor issues and support mitigation.
- Identified the E2E tester's knowledge as a capability to transfer gradually into QA rather than leave concentrated in one role.

### In Progress

- Coverage and automation baseline: repository locations and run cadence are known. Functional mapping is underway; AI-assisted repo analysis and consolidation will connect journeys to tests over time. Use Confluence as an interim reference if ReportPortal is not ready to provide the needed view.
- Environment baseline and response: current restrictions and recurring issues are understood and being tracked. Fixing recurring causes and industrialising monitoring remain follow-on work.
- Direct-report development: complete deep dives on each direct report's objectives, growth, and plan, then identify the shared team priorities.
- E2E knowledge transfer: extract journey and system knowledge, pair QA colleagues into the work, and progressively distribute responsibilities.
- Wider business visibility: continue building relationships over time beyond the initial internal engineering and Configuration connections.

### Intentionally Deferred

- Do not restart a formal monthly QA call while the existing QA group chat is meeting the need to communicate issues as they arise; revisit only if it stops working.
- Restart the QA Chapter as part of the wider chapter reset, after defining QA's purpose in the Pico model and identifying a champion.
- Keep environment improvements visible and discuss them as needed, but prioritize the current Microsite-sunset initiatives first. Staging monitoring and better control provide interim visibility and mitigation, not a resolution of the underlying constraints.
- Record other valid improvements as coming soon rather than promoting them to active initiatives when they do not align with current strategic priorities.

### Close-Out Actions

- [ ] Create a first-pass coverage register: functional journey, market, automation repo, owner, run cadence, results location, and known gap. Mark unknowns explicitly; do not wait for exhaustive coverage. The priority Portal/Pico/Exerp journey catalogue overlaps with [Challenge 07 — End-to-End Quality Ownership And Continuity](../../challenges/07-end-to-end-quality-ownership-and-continuity.md); the broader cross-repo and international coverage inventory is not yet owned by an improvement.
- [ ] Use AI to inventory tests in the known repositories, then validate the results against the functional map and link the two in Miro or the chosen reference space. Align the Miro journey mapping and knowledge capture with [Challenge 07](../../challenges/07-end-to-end-quality-ownership-and-continuity.md); repository-wide automation inventory remains a separate baseline activity.
- [ ] Record a concise initial environment and test-data baseline: available environments, key restrictions, recurring delays or failures, and how test data is created and maintained. Connect environment monitoring to [Improvement 01 — Staging Monitoring And Alerting Ownership](../../improvements/01-staging-monitoring-and-alerting-ownership.md) and test-data needs to [Improvement 02 — Dynamic Member Creation And Automated Test Data Architecture](../../improvements/02-dynamic-member-creation-and-test-data.md); the concrete Web MVP is [Initiative 01 — Dynamic Member Creation & Lookup For Portal Automation](../../initiatives/01-portal-dynamic-member-creation.md). These address parts of the baseline, not the full environment or test-data strategy.
- [ ] Resolve the QA-flow baseline through [Improvement 04 — Jira QA Flow Metrics Baseline](../../improvements/04-jira-qa-flow-metrics-baseline.md), including how Kanban is working, where work queues or waits, how Dev Test is used, and the main sources of delay. Use available Jira evidence where practical.
- [ ] Hold a growth and objectives deep dive with each direct report and record agreed next steps; then filter common needs into team priorities.
- [ ] Agree a practical E2E knowledge-transfer sequence with the E2E tester, including topics, paired QA owners, and knowledge that must be documented, through [Challenge 07 — End-to-End Quality Ownership And Continuity](../../challenges/07-end-to-end-quality-ownership-and-continuity.md).
- [ ] For the QA Chapter reset, draft the purpose and expected outcomes for QA in the Pico model, then identify a suitable champion before restarting the forum.

The day-30 baseline is a usable first view, not a complete catalogue or a commitment to solve every identified issue. Continue expanding coverage and reporting through the 60-day stabilisation phase.
