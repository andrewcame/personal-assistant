---
id: DC-2026-09-23-technical-lead-backend-portal-wundergraph
type: discovery-call
date: 2026-09-23
pillars: [P4, P5, P8]
focus: [ownership, automation, productivity]
links: []
people: [DA]
---

# 2026-09-23 - Technical Lead, Backend / Portal / Wundergraph Testing

## Call Context

- **Date:** 2026-09-23
- **Source / role:** Technical Lead, Backend and Portal
- **Conversation type:** Engineering discovery
- **Related team or platform:** Wundergraph / Supergraph, backend services, Portal, Kafka, preview environments, member creation
- **Notes based on:** Short discovery conversation and follow-up summary

## Purpose

- Understand the gap in backend and portal testing around events triggered through Wundergraph rather than injected directly onto Kafka.
- Explore how more complete preview environments and Supergraph capabilities could improve test data creation and end-to-end confidence.

## Key Signals

### What Matters To Them

- Backend testing is a known gap and is expected to be picked up by DA, but the missing Wundergraph coverage is a distinct and important risk.
- Tests need to exercise the same entry points used by clients: a Wundergraph call should trigger the downstream Kafka messages, rather than tests only placing messages directly onto Kafka.
- An integrated preview backend, frontend, and CMS would create more freedom to test complete journeys and could make tools such as Tilt more useful.
- Supergraph queries and mutations could remove the need for Nuggets, bespoke packages, and other test-data helpers if the required capabilities are exposed directly.
- A Supergraph-based member-creation flow could become complete once payment-agreement creation is available in Pico.

### Current Friction Or Risks

- Current message tests often put events directly onto Kafka and observe the result, but do not prove that Wundergraph calls produce the correct downstream Kafka messages.
- A recent URL-discovery issue was caused by deployment ordering and would likely have been visible earlier with coverage through the Wundergraph entry point.
- Preview backend, frontend, and CMS environments are not currently integrated into a single dependable end-to-end setup.
- Member creation automation cannot currently complete the payment side of the flow, so it cannot reliably create a fully paid member.
- Test data creation depends on Nuggets and packages because the Supergraph queries needed to find and create suitable members are not yet exposed.

### What Is Working Well

- The conversation was brief but productive, with agreement that Wundergraph-triggered tests would close a meaningful gap.
- There is broad interest in an integrated preview environment; the value is being recognised by multiple people and teams.
- Payment-agreement work is expected to move into Pico soon, which could unlock the final part of the member-creation flow.
- The preferred direction is to expose the required capabilities in Supergraph so each test package can create its own data when needed, rather than centralising all data creation in Exerp.

### What They Asked For

- Add tests that call Wundergraph and verify the resulting downstream Kafka messages and behaviour.
- Continue the conversation around an integrated preview environment spanning backend, frontend, and CMS.
- Explore Supergraph queries that can find suitable members, including education members, members in debt, or staff members, depending on the test need.
- Revisit full member creation once payment-agreement creation is available in Pico.

## Themes And Interpretation

- Directly stated: Direct Kafka injection does not cover the Wundergraph path that creates the Kafka messages used by the real system.
- Directly stated: Wundergraph-triggered tests could have caught the URL-discovery issue caused by deployment ordering.
- Directly stated: A unified preview environment across backend, frontend, and CMS would have significant value.
- Directly stated: Supergraph is preferred as the long-term test-data interface, reducing reliance on Nuggets and bespoke packages.
- Directly stated: Payment-agreement creation in Pico is the remaining capability needed to complete the member-creation flow.
- My interpretation: The missing Wundergraph tier is an entry-point coverage gap, not simply a lack of more Kafka tests; it tests whether the public orchestration layer emits the correct events.
- My interpretation: Integrated preview environments and Supergraph-based data creation are connected enabling capabilities for reliable end-to-end automation.
- Hypotheses to validate: A small set of high-value Wundergraph-to-Kafka tests would catch deployment-order and orchestration regressions that direct Kafka tests cannot see.
- Hypotheses to validate: Once payment agreements are supported, Supergraph can provide enough capability for test packages to create complete, disposable member scenarios without Nuggets.

## Mapping

### Strategic Mission(s)

- Technical Mastery & Foundations
- Delivery Flow & Resilience
- Business Risk & Stakeholder Trust

### Role Pillar(s)

- Automation Trust & Reliability
- Test Infrastructure, Environments & Data
- Business-Critical Journey Protection
- Quality Strategy & Risk-Based Coverage

### Objective Lens(es)

- Value Creator
- Business Operator

### Related 30/60/90 Focus Area(s)

- Automation
- Ownership
- Productivity

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Identify the first Wundergraph-to-Kafka journeys to automate** — Owner: AC / DA / Backend — Destination: Challenge / Notion — Notes: Prioritise flows where direct Kafka tests currently provide false confidence, including deployment-order-sensitive behaviour.
- **Confirm the Wundergraph schema and available operations** — Owner: AC / Backend — Destination: Notion / Alignment — Notes: Establish which mutations and queries can be used as stable test entry points and which downstream messages they should produce.
- **Define the integrated preview environment opportunity** — Owner: Backend / Portal / CMS / QA — Destination: Challenge / Decision — Notes: Capture the required backend, frontend, CMS, and deployment pieces, including whether Tilt can support the intended workflow.
- **Explore Supergraph test-data queries** — Owner: AC / Backend — Destination: Notion / Alignment — Notes: Identify the filters needed to find member types such as education members, members in debt, and staff members.
- **Track payment-agreement support in Pico** — Owner: Backend / AC — Destination: Notion / Alignment — Notes: Reassess full member creation when member, subscription, and payment-agreement creation can all be completed through Supergraph.

## Possible Outputs

- Candidate challenge: Direct Kafka message tests leave an untested Wundergraph orchestration path that can fail in production-like flows.
- Candidate decision: Establish Wundergraph-to-Kafka coverage as a distinct backend test tier alongside direct message tests.
- Candidate goal input: Build a reliable Supergraph-based member-creation capability covering member, subscription, and payment agreement creation.
- Candidate goal input: Help shape an integrated preview environment spanning backend, frontend, and CMS.
- Candidate achievement evidence: Identified a specific backend testing gap and aligned with engineering on a practical path to close it.

## Open Questions

- Which Wundergraph mutations are the highest-value first candidates, and what Kafka events should each produce?
- Can the staging Wundergraph endpoint support stable automated tests, or is a dedicated preview route required?
- What caused the URL-discovery deployment-order issue, and what observable assertion would have caught it?
- Which team owns the integrated preview-environment initiative, and what is the current proposed scope?
- When will payment-agreement creation be available in Pico, and what remaining dependencies would block complete member creation?
- Should Supergraph expose generic member search, purpose-built test-data queries, or both?
