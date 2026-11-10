---
id: IMP-11
tag: Backend tests
type: improvement
status: on-hold
horizon: later
updated: 2026-11-10
pillars: [P4, P8]
focus: [automation]
jd: [JD-05]
goals: []
links: [IMP-06, CH-10, IMP-14, CH-13]
people: [TMW, JFG, AE]
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

### 2026-11-04

- Notion card "List backend pack coverage gaps, starting with the Exerp Assistant" found Done in the 2026-11-04 sync (Flow 6). Roadmap IMP-11.1 marked done. Next: agree priority gaps and owners (IMP-11.4), once the backend coverage initiative with TMW and JFG is set up (IMP-11.6).

### 2026-11-05

- Follow-up answers from TMW/JFG confirm that the regression work to date was a review identifying general gaps in Exerp Adapter and Basket tests; no merged or delivered changes were confirmed. The Basket pilot remains in progress, with no specific scenario additions or detailed findings confirmed yet.
- This work overlaps IMP-11.1, which maps missing coverage across Pico backend services, and CH-10, which determines the appropriate balance of Exerp-dependent and internal testing. IMP-11 tracks the coverage gaps; CH-10 defines the test strategy.
- AC plans to set up the backend test coverage initiative and assign it to TMW and JFG so JFG can add the relevant ticket. IMP-11 remains in progress with TMW and JFG as the people involved.

### 2026-11-04 (Platform Technical Lead discovery)

Source: [2026-11-04 Platform Technical Lead](../context/discovery-calls/2026-11-04-platform-technical-lead-staging-reporting.md).

- **Why this is the priority:** AC told AE that decent backend test coverage is the first step, because it means more gets found in staging and staging becomes a more valuable proving ground; things should fail there rather than in prod. AE agreed staging should carry more value.
- **Platform support:** AE will help from a technical point of view, and is open to talking if the backend tests hit a limitation in staging. Use this as the route for staging blockers on the initiative with TMW and JFG (IMP-11.6).
- **Builds on:** layered testing (some checks in staging, some in prod, tagged on the tests) with overnight, always-on runs; see CH-10 Pico source of truth. A staging soak before prod depends on this coverage (IMP-14.2, CI/CD gate).

### 2026-11-10 (2027 direction preview)

Source: [Leadership Direction, 2026-11-10](../context/leadership-direction.md); tracked in [CH-13](../challenges/13-2027-business-direction-transition.md).

- With web and app technology expected to move to a third party, AC decided **not to start** the backend coverage initiative. The gaps are known (IMP-11.1); creating the initiative now is unlikely to be worth it. Moved to Later and on hold; it may be parked (closed with `outcome: none`) once the handover scope is known.
- IMP-11.6 and IMP-11.7 moved to later; their Notion cards moved to Backlog.
- TMW's 2026 objective TMW-O6 (scope a Pico backend coverage initiative by end of December) depends on this work; AC to revisit it.

## Roadmap

| ID       | Step                                                                                                                          | Owner | Depends on         | Status | Card                                                         |
|----------|-------------------------------------------------------------------------------------------------------------------------------|-------|--------------------|--------|--------------------------------------------------------------|
| IMP-11.1 | List backend pack coverage gaps across the priority backend services                                                          | AC    | —                  | done   | —                                                            |
| IMP-11.2 | Check what the Backend and AI chapters are doing on backend tests                                                             | AC    | —                  | later  | —                                                            |
| IMP-11.3 | Fix Kafka Web Sender and decide whether to expand its use                                                                     | AC    | IMP-11.1           | later  | —                                                            |
| IMP-11.4 | Agree priority gaps and owners; add the tests                                                                                 | AC    | IMP-11.1, IMP-11.2 | later  | —                                                            |
| IMP-11.5 | Flesh out a flagged integration tier: select real-Exerp tests, flag them in the packs, decide blocking vs overnight-and-alert | AC    | CH-10.5            | later  | —                                                            |
| IMP-11.6 | Set up the backend test coverage initiative with TMW and JFG (TMW-O6 scoped proposal due end of December)                     | AC    | —                  | later  | Set up the backend test coverage initiative with TMW and JFG |
| IMP-11.7 | Investigate Exerp Assistant not showing all products                                                                          | AC    | —                  | later  | Investigate Exerp Assistant not showing all products         |

## Status & Next Action

**Status:** On hold — not started; moved to Later on 2026-11-10 because of the 2027 direction preview (CH-13). The coverage review has identified general gaps in Exerp Adapter and Basket tests.

**Next action:** None until CH-13 shows whether backend testing stays with us; then restart or park.

## Outcome

- Completed:
- Logged achievement:
