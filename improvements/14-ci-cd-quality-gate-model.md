---
id: IMP-14
tag: CI/CD gate
type: improvement
status: not-started
horizon: later
updated: 2026-11-09
pillars: [P4, P6]
focus: [automation]
jd: [JD-08]
goals: []
links: [CH-10, IMP-11]
people: [AE]
---

# Improvement 14 — CI/CD Quality Gate Model

## Context

- Source: [60-day plan](../context/my-role/60-day-plan.md) and job-spec responsibility JD-08 (quality in CI/CD: runs, coverage signals, quality gates). Opened 2026-11-04 from the plan-only row in [horizons.md](../context/my-role/horizons.md). Assumed required until closed.
- Question to answer: what automated signals are visible to engineers throughout the pipeline, not just at the end?

## Objective

- The CI/CD quality gate model defined: the agreed standard, and the gaps between current state and target.

## Related

- Role pillar(s): [P4 Automation Trust & Reliability](../context/role-pillars.md), [P6 Delivery Confidence & Flow](../context/role-pillars.md)
- Originating recommendation: 60-day plan

## Actions & Progress

### 2026-11-04

- Opened from the plan-only row in horizons.md.

### 2026-11-04 (Platform Technical Lead discovery)

Source: [2026-11-04 Platform Technical Lead](../context/discovery-calls/2026-11-04-platform-technical-lead-staging-reporting.md).

- AE and AC agreed staging should carry more value as a gate: the business does not want issues in prod, so staging has to catch them.
- AE's idea: a staging soak. After a developer merges, the change deploys to staging and is held there for a set time (for example an hour) while a large set of tests runs and monitoring watches; then it is promoted to prod. Mechanisms to hold a change from going further already exist.
- Constraint: balance against what the business and developers need; do not slow delivery. Backend coverage in staging (IMP-11 Backend tests) is the first priority, because it makes the soak worth having.
- Added IMP-14.2 to design the soak with AE once there is test coverage to run in it.

## Roadmap

| ID | Step | Owner | Depends on | Status | Card |
|----|------|-------|------------|--------|------|
| IMP-14.1 | Define the quality gate standard and list gaps against current state | AC | — | later | — |
| IMP-14.2 | Design a staging soak (hold after merge while tests and monitoring run, then promote) with AE, balanced against delivery speed | AC | IMP-11.4 | later | — |

## Status & Next Action

**Status:** Not started — Later.

**Next action:** Revisit when capacity frees up (IMP-14.1).

## Outcome

- Completed:
- Result: [achievement, team evidence, both or none — set `outcome:` in the front-matter when closed]
