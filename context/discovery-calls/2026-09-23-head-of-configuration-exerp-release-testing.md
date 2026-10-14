---
id: DC-2026-09-23-head-of-configuration-exerp-release-testing
type: discovery-call
date: 2026-09-23
pillars: [P4, P5, P8]
focus: [ownership, automation, productivity]
links: []
people: []
---

# 2026-09-23 - Head of Configuration / Exerp Release Testing

## Call Context

- **Date:** 2026-09-23
- **Source / role:** Head of Configuration
- **Conversation type:** Stakeholder discovery
- **Related team or platform:** Exerp configuration, release testing, shared test environments, Pico
- **Notes based on:** Short discovery conversation and follow-up summary

## Purpose

- Understand how Exerp release and upgrade testing currently works, where it is reactive, and how QA can make the process more predictable.
- Identify opportunities to improve release visibility, test ownership, environment stability, and app-testing support.

## Key Signals

### What Matters To Them

- Earlier visibility of upcoming Exerp versions and upgrades would make release testing easier to plan.
- Change notes are important input for understanding what needs to be tested and where Pico may be affected.
- A clearer, more industrialised testing process would help as the organisation moves away from microsites and further into Pico.
- The configuration team needs a practical route into app testing when configuration changes or gaps affect app journeys.

### Current Friction Or Risks

- The initial release-testing process has been reactive because version information and change notes were not reaching QA early enough.
- Existing tickets are a mixed record of activity and do not consistently represent the work that is actually being done.
- Exerp has a large number of environments, creating uncertainty about which are still needed and increasing maintenance overhead.
- The shared test PG test environment needs review and cleanup so that it remains reliable for everyone who depends on it.
- There is a gap in understanding and ownership around app testing for configuration-related changes.

### What Is Working Well

- The conversation was positive and produced clear alignment on the practical changes needed.
- The Head of Configuration is willing to provide earlier version visibility and access to change notes.
- There is openness to QA helping with app testing where configuration work creates a need or exposes a gap.

### What They Asked For

- Provide earlier notice of versions and upgrades that are coming.
- Share relevant Exerp change notes so release testing can be planned against actual changes.
- Help review the current release-testing epic and activities, then align tickets and ownership with the work that needs to happen.
- Support the review of unused Exerp environments and the cleanup of the shared test PG test environment.
- Act as a point of contact for app-testing support when configuration work needs it.

## Themes And Interpretation

- Directly stated: Earlier release information and change notes would improve planning.
- Directly stated: Existing tickets do not accurately reflect the testing work and need to be reviewed and reassigned.
- Directly stated: Exerp environment usage should be reviewed, with unused environments decommissioned and active environments refreshed through copy-backs where needed.
- Directly stated: There is uncertainty about app-testing involvement and a willingness to close that gap collaboratively.
- My interpretation: Exerp release testing needs to move from a reactive activity to a visible, risk-led process with clear inputs, ownership, and traceability.
- My interpretation: Environment rationalisation is a prerequisite for trustworthy release testing; instability and unnecessary variation will otherwise continue to obscure results.
- Hypotheses to validate: A simple release-readiness flow built around version notice, change-note review, an agreed test scope, and correctly assigned tickets will reduce late surprises and duplicated effort.

## Mapping

### Strategic Mission(s)

- Technical Mastery & Foundations
- Delivery Flow & Resilience
- Business Risk & Stakeholder Trust

### Role Pillar(s)

- Test Infrastructure, Environments & Data
- Automation Trust & Reliability
- Business-Critical Journey Protection
- Quality Strategy & Risk-Based Coverage

### Objective Lens(es)

- Business Operator
- Value Creator

### Related 30/60/90 Focus Area(s)

- Ownership
- Automation
- Productivity

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Establish a regular Exerp version and change-note handoff** — Owner: Head of Configuration / AC — Destination: Notion / Cadence — Notes: Agree how much notice is practical and where the information will be visible to QA.
- **Review the Exerp release-testing epic and current tickets** — Owner: AC / Head of Configuration — Destination: Notion / Alignment — Notes: Separate the real testing activities, clarify expected outputs, and reassign work to the people who should perform it.
- **Review Exerp environments and shared test PG** — Owner: AC / Configuration — Destination: Challenge / Decision — Notes: Identify environments to retain, refresh through copy-back, or decommission; include the shared environment used by the wider team.
- **Define the app-testing support route** — Owner: AC / Head of Configuration — Destination: Notion / Alignment — Notes: Make it easy for configuration to request help when a change needs app coverage or an app-testing gap is identified.

## Possible Outputs

- Candidate challenge: Exerp environment sprawl and shared test-environment instability reduce confidence in release testing.
- Candidate decision: Adopt a clearer Exerp release-testing flow with early version notice, change-note review, agreed scope, and explicit ownership.
- Candidate goal input: Industrialise configuration and Exerp upgrade testing so that tickets, coverage, and ownership reflect the actual risk and work.
- Candidate achievement evidence: Established a constructive working relationship with Configuration and agreed the inputs needed to make release testing more proactive.

## Open Questions

- What lead time can Configuration realistically provide for versions and upgrades?
- Where should Exerp change notes and release-testing scope be recorded so that they remain visible and usable?
- Which Exerp environments are still actively needed, and what is the safe process for copy-back or decommissioning?
- What app-testing coverage is currently expected for configuration changes, and where are the highest-risk gaps?
