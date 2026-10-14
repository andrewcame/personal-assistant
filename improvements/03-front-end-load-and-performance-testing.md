---
id: IMP-03
type: improvement
status: not-started
horizon: later
updated: 2026-09-15
pillars: [P7]
focus: [automation]
goals: []
links: []
people: [GL, GH, DJ]
---

# Improvement 03 — Front-End Load And Performance Testing

## Context

- A recent front-end issue saw app usage creep up with no monitoring in place to catch it; members reported the problem before we did.
- Current front-end/browser-based testing loads a single journey and closes the browser, which doesn't resemble sustained usage patterns (e.g. memory growth over time) that a real performance/load scenario would expose.
- Backend load testing is already being considered; front-end load/performance testing had not been, until raised in this session.
- Originating discussion: Weekly Engineering Senior Leadership Meeting (2026-09-15), with GL, GH, and DJ. See [context/leadership-direction.md](../context/leadership-direction.md#2026-09-15--weekly-senior-leadership-call).

## Objective

- Stand up front-end load/performance testing, anchored by a nightly performance run on staging (GL's suggestion) rather than a dedicated load test environment: ramp the Exerp test instance overnight to meet demand, and review results each morning alongside existing staging/app alerting.
- Once staging is validated as the de facto UK load test environment, retire the unused Southampton satellite Exerp test instance as a cost saving. Sequence this after validation, and revisit brand/multi-market considerations later — UK first.

## Related

- Goal(s): [goals/2026.md](../goals/2026.md)
- Role pillar(s): [7. Non-Functional Quality & Resilience](../context/role-pillars.md), [5. Test Infrastructure, Environments & Data](../context/role-pillars.md)
- Originating recommendation: GL (Software Engineering Director), via Weekly Senior Leadership Meeting

## Actions & Progress

### 2026-09-15

- Raised in Senior Leadership Meeting as a new gap distinct from backend load testing; agreed as a candidate improvement to action.

## Status & Next Action

**Status:** Not started

**Next action:** Design the nightly staging performance run (scope, scenarios that would realistically catch usage/memory creep, and how results feed into existing staging/app alerting review).

## Outcome

- Completed: YYYY-MM-DD
- Logged achievement: [link once written via Capture]
