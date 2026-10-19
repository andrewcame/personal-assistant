---
id: IMP-11
type: improvement
status: not-started
horizon: next
updated: 2026-10-16
pillars: [P4, P8]
focus: [automation]
goals: []
links: [IMP-06]
people: []
---

# Improvement 11 — Backend Test Pack Coverage

## Context

- The existing backend test pack misses many areas, because the QA who wrote it focused only on certain tickets and services.
- The Exerp Assistant is a big gap (from the Notion To Do card "Add new initiatives (future)").
- Kafka Web Sender needs fixing, with a question of whether to expand its use.
- Opened 2026-10-16 from the Ideas triage ([ideas log](../state/ideas-log.md)); AC agreed a new improvement.

## Objective

- The backend test pack covers the priority backend services, starting with the Exerp Assistant, with known gaps listed and owned.

## Related

- Role pillar(s): [4. Automation Trust & Reliability](../context/role-pillars.md), [8. Business-Critical Journey Protection](../context/role-pillars.md)
- Originating recommendation: self (Ideas page)
- Related: [IMP-06 — QA Knowledge And Coverage Baseline](06-qa-knowledge-and-coverage-baseline.md)

## Actions & Progress

### 2026-10-16

- Opened. Starting point: list the current pack's coverage against backend services, starting with the Exerp Assistant.
- Check what the Backend and AI chapters are already doing before adding tests.

## Roadmap

| ID | Step | Owner | Depends on | Status |
|----|------|-------|------------|--------|
| IMP-11.1 | List backend pack coverage gaps, starting with the Exerp Assistant | AC | — | next |
| IMP-11.2 | Check what the Backend and AI chapters are doing on backend tests | AC | — | later |
| IMP-11.3 | Fix Kafka Web Sender and decide whether to expand its use | AC | IMP-11.1 | later |
| IMP-11.4 | Agree priority gaps and owners; add the tests | AC | IMP-11.1, IMP-11.2 | later |

## Status & Next Action

**Status:** Not started

**Next action:** List the backend pack's coverage gaps, starting with the Exerp Assistant.

## Outcome

- Completed:
- Logged achievement:
