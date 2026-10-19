---
id: IMP-01
type: improvement
status: in-progress
horizon: now
updated: 2026-10-16
pillars: [P5]
focus: [productivity]
goals: []
links: []
people: [JT]
---

# Improvement 01 — Staging Monitoring And Alerting Ownership

## Context

- Staging environment instability and silent deployment failures are a recurring bottleneck for E2E testing and release confidence.
- Platform and DevEx engineers are currently stretched and carrying the operational burden of monitoring staging.
- As the QA & Test Engineering Manager, having direct visibility and first-responder responsibility over staging health protects QA's core dependency while relieving pressure on platform peers.
- Originating discussion: In-office leadership session (2026-09-11).
- Discovery evidence: [Software Engineering Manager - Pico architecture (2026-09-14)](../context/discovery-calls/2026-09-14-sem-pico-architecture.md).

## Objective

- Onboard to staging monitoring, dashboards, and alerting systems; establish QA-led first-responder triage for staging alerts to detect and resolve test environment issues before they block delivery or reach production.

## Related

- Goal(s): [goals/2026.md](../goals/2026.md)
- Role pillar(s): [5. Test Infrastructure, Environments & Data](../context/role-pillars.md), [4. Automation Trust & Reliability](../context/role-pillars.md)
- Originating recommendation: Self / Leadership in-office discussion

## Actions & Progress

### 2026-09-11

- Offered in leadership session to take on staging alerting and first-responder triage to alleviate pressure on DevEx.
- Set up knowledge transfer / walkthrough call with DevEx/Platform to review staging monitoring tooling and alert rules.

### 2026-09-14

- **Observed in Pico architecture discovery:** Existing Grafana Pico Backend dashboards can be reused for staging by selecting the staging environment; new dashboards are not required to begin first-response monitoring.
- **Observed guidance:** First-response checks should include the existing Golden Signals, error, and database-performance dashboards, with the environment filter confirmed before interpreting the result.
- **Observed guidance:** Dead-letter queue (DLQ) investigation should capture the error and relevant context before any recovery action, then be logged and escalated to the appropriate SME for resolution advice.
- **Observed safe recovery sequence:** Where recovery is agreed after investigation, recreate the Kafka DLQ topic because clearing messages was unreliable, then restart the affected consumer pod so it recreates its subscription. This is not a routine "clear the queue" action: preserve evidence and seek awareness/escalation before doing it.

### 2026-10-15

- DevEx/Platform walkthrough completed (by 2026-10-15); nothing materially new beyond the 2026-09-14 guidance.
- AC is currently doing staging first-response checks manually.
- Idea: use Claude to assist or automate the manual SRE checks (dashboard review, DLQ inspection, log entry). Candidate next step, not yet scoped.

### 2026-10-15 (direction)

- The mission is unchanged; the method changes. The morning first-response checks could be run by Claude, while AC (and the team) still own fixing what is found. Tracked as roadmap steps IMP-01.6–7 rather than a separate improvement.

### 2026-10-16

- AC confirmed a separate agreement of the daily routine with DevEx/Platform isn't needed: AC is running the checks manually, and the next step is to automate them with AI and work through the issues found so far (IMP-01.4 dropped).
- Staging DLQ issues found so far (IMP-01.5, from the Notion card):
  - `account.basket.dlq.raw`, `account.membership.dlq.raw` and `account.payment.dlq.raw` are receiving some "production"-tagged messages — use AI to work out why.
  - `brazeadapter.account.dlq.raw` has many errors about config missing in Braze — identify and get fixed.
  - `exerpadapter.extracts.internal.dlq.raw` — check why and when it runs, what it does, and whether it can be disabled in staging if unused; compare with prod.
  - `exerpadapter.product.dlq.raw` — work with JT to learn how to clear and re-run it.

## Proposed Daily First-Response Routine

_Proposal based on the 2026-09-14 discovery guidance; validate ownership, escalation contacts, and permissions with DevEx/Platform before adopting it._

1. Open the existing Grafana Pico Backend dashboards, select the staging environment, and review Golden Signals, errors, and database performance.
2. Inspect the staging DLQ when dashboard signals or test failures indicate a possible asynchronous-processing issue; capture the error and relevant context before changing queue or consumer state.
3. Record findings in the agreed local log, including the environment, time, observed signal, error evidence, impact, and escalation/outcome.
4. Escalate actionable findings to the appropriate SME. If DLQ recovery is agreed, recreate the Kafka DLQ topic and then restart the affected consumer pod; verify that the consumer recreates its subscription.

## Roadmap

| ID | Step | Owner | Depends on | Status |
|----|------|-------|------------|--------|
| IMP-01.1 | Offer to own staging first-response triage | AC | — | done |
| IMP-01.2 | Complete DevEx/Platform monitoring walkthrough | AC | — | done |
| IMP-01.3 | Run staging first-response checks manually | AC | IMP-01.2 | doing |
| IMP-01.4 | Confirm daily first-response routine with DevEx/Platform | AC | IMP-01.2 | dropped |
| IMP-01.5 | Look into staging DLQ issues | AC | — | next |
| IMP-01.6 | Scope Claude running the morning staging checks (what it reads, what stays human) | AC | IMP-01.3 | next |
| IMP-01.7 | Pilot Claude-run morning checks; AC triages and fixes findings | AC | IMP-01.6 | later |

## Status & Next Action

**Status:** In progress

**Next action:** Work through the four DLQ issues found so far, and scope how Claude could take on the repetitive manual SRE checks (what it can read, what stays human, how findings are logged).

_Superseded 2026-10-16:_ confirm the daily routine with DevEx/Platform first (not needed).

_Superseded 2026-10-15:_ complete the DevEx/Platform walkthrough (done).

## Outcome

- Completed: 
- Logged achievement: 
