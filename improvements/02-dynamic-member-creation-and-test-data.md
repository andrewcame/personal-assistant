---
id: IMP-02
type: improvement
status: in-progress
horizon: now
updated: 2026-10-16
pillars: [P5]
focus: [automation]
jd: [JD-06]
goals: []
links: [INI-01, CH-10]
people: []
---

# Improvement 02 — Dynamic Member Creation And Automated Test Data Architecture

## Context

- E2E and front-end test automation across Pico and Exerp suffer from static, brittle, or drifting test data (members in incorrect membership states, PIN conflicts, Exerp state desync).
- Sourcing and dynamically creating test members in required states is critical for trusted, repeatable automation runs and continuous CI/CD gating.
- Originating discussion: In-office leadership session (2026-09-11) and Technical Lead Payments discovery call (2026-09-11).
- Discovery evidence: [Software Engineering Manager - Pico architecture (2026-09-14)](../context/discovery-calls/2026-09-14-sem-pico-architecture.md).

## Objective

- Submit and agree an architectural proposal for dynamic test member creation and state provisioning via the Tech Challenges Board; implement reliable tooling/APIs for QA test packs.

## Related

- Goal(s): [goals/2026.md](../goals/2026.md)
- Role pillar(s): [5. Test Infrastructure, Environments & Data](../context/role-pillars.md), [4. Automation Trust & Reliability](../context/role-pillars.md), [8. Business-Critical Journey Protection](../context/role-pillars.md)
- Originating recommendation: Self / Leadership in-office discussion

## Actions & Progress

### 2026-09-11

- Identified need for dynamic member creation and formal architectural backing.
- Agreed to route the requirement through the Tech Challenges Board to establish tech direction with engineering architects before implementation.

### 2026-09-14

- **Observed in Pico architecture discovery:** Internal member lookup and sourcing members in known states are viable scope using the currently available member and subscription data.
- **Observed limitation:** Creating a fresh member that is fully usable for real login remains blocked by the payments/Exerp integration gap. The current Supergraph cannot access payments/Exerp data, so a newly created member would be in debt.
- **Requirement clarified:** Test scenarios that consume or alter member state need disposable state. Cancellation is one example: the test must be able to use a member whose state can safely be changed without contaminating other tests or environments.
- **Requirement clarified:** Pico and Exerp state must remain consistent for any sourced or provisioned member; state drift is not an acceptable success condition.
- **Not decided:** A new Supergraph or direct Exerp API integration are possible future technical approaches, but neither is an agreed architecture.

### 2026-10-13

- Environments discussion leaning towards one Exerp test environment per brand, shared by previews and staging ([notes](../context/discovery-calls/2026-10-13-environments-exerp-per-brand.md)).
- **Implication:** previews and staging would share member records in PureGym Test. Disposable, dynamically created or reserved members become a prerequisite for reliable preview automation, which strengthens the case for this improvement and Initiative 01.
- Payments is still not connected in the proposal, so the fully usable fresh-member limitation recorded on 2026-09-14 remains.

### 2026-10-15

- INI-01 start sequenced after DA's current work; kick-off/refinement with the Lead QAs to agree the approach first.

### 2026-10-16 (ideas triage)

_From the Ideas triage on 2026-10-16 ([ideas log](../state/ideas-log.md))._

- **Payload (CMS) data in dev and staging:** who owns it? With no Product function, are we testing with real data or placeholders? Likely placeholders — the strategy should make sure we always test realistically.
- **Exerp data refresh approach (for IMP-02.7):** seed data weekly, search for data at run time by criteria, or create data in each test run? Move away from hardcoded data.
- **Test data generation:** this was done in CAPI before — can it run on a regular basis again?

## Proposed Direction

_Proposal for engineering discussion, not an architectural decision._

- Define a skeleton initiative around internal-only member lookup and state sourcing first, including the required member states, disposal/reset expectations, and Pico/Exerp consistency checks.
- Separate requirements for fresh, fully usable member creation from this initial scope and retain the payments/Exerp dependency explicitly.
- Take the requirements to the Backend Chapter to shape and test the technical direction before submitting or committing to an implementation approach.

## Roadmap

| ID | Step | Owner | Depends on | Status |
|----|------|-------|------------|--------|
| IMP-02.1 | Agree Tech Challenges Board route for member creation | AC | — | done |
| IMP-02.2 | Clarify scope and limits in Pico architecture discovery | AC | — | done |
| IMP-02.3 | Scope Portal Web MVP as Initiative 01 | AC | IMP-02.2 | done |
| IMP-02.4 | Draft lookup, state-sourcing and disposable-state requirements | DA | IMP-02.2 | next |
| IMP-02.5 | Shape requirements with the Backend Chapter | AC | IMP-02.4 | later |
| IMP-02.6 | Propose architecture through the Tech Challenges Board | AC | IMP-02.5, CH-10.7 | later |
| IMP-02.7 | Agree cross-team test data strategy beyond Portal MVP | AC | IMP-02.6 | later |

## Status & Next Action

**Status:** In progress — formal delivery has graduated to [Initiative 01 — Portal Dynamic Member Creation](../initiatives/01-portal-dynamic-member-creation.md) (Draft). This file keeps the wider test-data architecture direction; the initiative holds the scoped Web MVP.

**Next action:** Draft requirements for internal member lookup/state sourcing and disposable-state scenarios, including Pico/Exerp consistency criteria; use Backend Chapter discussion to inform the skeleton initiative before proposing an architecture through the Tech Challenges Board.

## Outcome

- Completed: 
- Logged achievement: 
