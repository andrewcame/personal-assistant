---
id: CH-12
type: challenge
status: open
horizon: next
updated: 2026-10-15
pillars: [P5, P8, P6]
focus: [ownership, productivity]
jd: [JD-12]
goals: []
links: [IMP-09, CH-08, CH-10]
people: [MJ]
---

# Challenge 12 — No Reliable Process For Exerp Release And Upgrade Testing

## Context

- Exerp release and upgrade testing has been reactive: version information and change notes have not reached QA early enough to plan ([2026-09-23 Head of Configuration call](../context/discovery-calls/2026-09-23-head-of-configuration-exerp-release-testing.md)).
- Existing tickets are a mixed record and don't reflect the testing work actually done.
- There are many Exerp environments, some possibly unused, and the shared test environment needs review and clean-up.
- Ownership of app testing for configuration-related changes is unclear.
- The direction towards one Exerp test environment per brand ([2026-10-13 environments discussion](../context/discovery-calls/2026-10-13-environments-exerp-per-brand.md)) changes where upgrades would be validated first.

## Challenge

How do we move Exerp release testing from a reactive activity to a predictable, risk-led process with clear inputs, scope, ownership, and traceability — as Pico takes over from the microsites?

## Questions To Explore

- What notice and change-note detail do we need, and from whom, for each Exerp version or upgrade?
- Which Pico and app journeys are most exposed to Exerp changes, and what is the minimum regression scope per release?
- Who owns release-testing tickets, and how should they be structured so they reflect the actual work?
- Which environments are needed for release validation once the one-Exerp-per-brand model lands?
- What is the route for app testing when configuration changes affect app journeys?

## Initial Position

The Head of Configuration is willing to provide earlier version visibility and change notes. A simple flow — version notice → change-note review → agreed risk-based scope → correctly assigned tickets → sign-off — is the likely shape, worked out with the Lead QAs rather than imposed. The process itself is tracked as [IMP-09](../improvements/09-exerp-release-testing-process.md).

## Roadmap

| ID | Step | Owner | Depends on | Status |
|----|------|-------|------------|--------|
| CH-12.1 | Discuss Exerp release testing with the Lead QAs | AC | — | next |
| CH-12.2 | Pilot the agreed process on the next Exerp release | AC | IMP-09.4 | later |
| CH-12.3 | Confirm challenge resolved after pilot review | AC | CH-12.2 | later |

## Status & Next Action

**Status:** Open — raised 2026-10-15 from the Notion to-do "discuss Exerp release testing with the leads".

**Next action:** Book time with the Lead QAs to discuss Exerp release testing and agree who drafts the process (IMP-09).
