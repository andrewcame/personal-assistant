---
id: IMP-11
tag: Backend tests
type: improvement
status: in-progress
horizon: now
updated: 2026-11-03
pillars: [P4, P8]
focus: [automation]
jd: [JD-05]
goals: []
links: [IMP-06, CH-10]
people: [TMW, JFG]
---

# Improvement 11 — Backend Test Pack Coverage

## Context

- The existing backend test pack misses many areas, because the QA who wrote it focused only on certain tickets and services.
- The Exerp Assistant is a test tool, not a backend service, so it is not a backend coverage gap.
- Kafka Web Sender needs fixing, with a question of whether to expand its use.
- Opened 2026-10-16 from the Ideas triage ([ideas log](../state/ideas-log.md)); AC agreed a new improvement.

## Objective

- The backend test pack covers the priority backend services, with known gaps listed and owned.

## Related

- Role pillar(s): [4. Automation Trust & Reliability](../context/role-pillars.md), [8. Business-Critical Journey Protection](../context/role-pillars.md)
- Originating recommendation: self (Ideas page)
- Related: [IMP-06 — QA Knowledge And Coverage Baseline](06-qa-knowledge-and-coverage-baseline.md)
- Related: [CH-10 — Pico Source-Of-Truth And Exerp-Dependent Test Strategy](../challenges/10-pico-source-of-truth-and-exerp-dependent-test-strategy.md) (test-tier rules for Exerp-dependent tests)

## Actions & Progress

### 2026-11-03

- Learned from the JFG calibration evidence that JFG is already reviewing regression coverage for backend services outside the MXBE/MXWEB/WEB3 account and metadata domains, with Basket as the pilot, using Copilot to find gaps and draft scenarios. What has been delivered is not yet confirmed (open question, Notion card "Close open JFG calibration evidence questions").
- TMW's 2026 objective TMW-O6 (agreed 2026-11-03) is to scope a Pico backend coverage initiative by the end of December. Plan: AC sets up the initiative this week so TMW and JFG can work on it together. Added IMP-11.6.
- Status moved to in-progress; TMW and JFG added to people.

### 2026-10-23

- Added a step to flesh out a flagged integration tier: select real-Exerp integration tests, flag them in the packs, and decide per test whether it blocks releases or runs overnight and alerts. Basis: AC's view that no Exerp tests in the backend is not acceptable, and the [2026-10-23 industry signal](../context/industry-signals.md).
- Correction: the Exerp Assistant is a test tool, not a backend service, so it is no longer the starting point for coverage. The coverage list starts with the priority backend services.
- Principle: write the tests even if they are not enabled by default. The Dootrix Exerp simulator (bookings service) is a precedent for the mock tier; the equivalent real-Exerp checks were manual and are candidates to automate.

### 2026-10-16

- Opened. Starting point: list the current pack's coverage against backend services, starting with the Exerp Assistant.
- Check what the Backend and AI chapters are already doing before adding tests.

## Roadmap

| ID | Step | Owner | Depends on | Status |
|----|------|-------|------------|--------|
| IMP-11.1 | List backend pack coverage gaps across the priority backend services | AC | — | next |
| IMP-11.2 | Check what the Backend and AI chapters are doing on backend tests | AC | — | later |
| IMP-11.3 | Fix Kafka Web Sender and decide whether to expand its use | AC | IMP-11.1 | later |
| IMP-11.4 | Agree priority gaps and owners; add the tests | AC | IMP-11.1, IMP-11.2 | later |
| IMP-11.5 | Flesh out a flagged integration tier: select real-Exerp tests, flag them in the packs, decide blocking vs overnight-and-alert | AC | CH-10.5 | later |
| IMP-11.6 | Set up the backend test coverage initiative with TMW and JFG (TMW-O6 scoped proposal due end of December) | AC | — | next |

## Status & Next Action

**Status:** In progress (JFG is already working on coverage gaps; initiative to be set up with TMW)

**Next action:** Set up the backend test coverage initiative with TMW and JFG this week, then confirm what JFG's coverage work has delivered.

## Outcome

- Completed:
- Logged achievement:
