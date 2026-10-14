---
id: DC-2026-09-25-technical-lead-pico-backend-legacy-architecture
type: discovery-call
date: 2026-09-25
pillars: [P4, P5, P7, P8]
focus: [ownership, automation, productivity]
links: [CH-08, IMP-02]
people: []
---

# 2026-09-25 - Technical Lead, Pico Backend / Legacy Portal Architecture

## Call Context

- **Date:** 2026-09-25
- **Source / role:** Technical Lead; backend specialist, involved in Pico's original implementation and historic portal/microsite work
- **Conversation type:** Engineering discovery
- **Related team or platform:** Pico backend, Exerp integration, legacy portal, test environments, automated integration testing
- **Notes based on:** Personal notes and post-call reflection
- **Relationship context:** Long-standing working relationship; we worked in the same team when we first joined. This supported a candid, constructive discussion with genuine challenge from both sides.

## Purpose

- Understand the original Pico architecture intent and how it should inform the current backend and integration-testing strategy.
- Test the balance between mocked dependencies and real Exerp-backed integration coverage.
- Explore constraints and longer-term direction for test data and non-production Exerp environments.

## Key Signals

### What Matters To Them

- Automation coverage is broadly reasonable; the focus should be on the quality and boundaries of coverage rather than adding tests indiscriminately.
- Static test data is a recurring risk. Tests should dynamically find or create the data they need at execution time rather than depend on fixed shared records.
- The original Pico direction was for Pico to remain the source of truth and to limit direct dependency on Exerp. Where appropriate, tests should mock Exerp, IDS, and comparable external services.
- Event-driven signals and SRE observability are important sources of evidence for production problems and system health.

### Current Friction Or Risks

- The platform now contains competing architectural models. Some flows can operate with Pico as the source of truth, while others depend materially on Exerp's response or confirmation.
- The cancellation flow is an example where the application waits for Exerp to confirm the cancellation. Treating Exerp as wholly mockable would not represent the behaviour users currently receive.
- This mixed model increases operational and test complexity because the intended Pico-first design and the implemented Exerp dependencies are not consistently aligned.
- Static data makes tests vulnerable to state drift, collisions, and unclear preconditions.
- Providing dedicated development or test Exerp instances for every brand is costly, especially as the estate grows to ten or twenty brands.
- Tests should not fail simply because Exerp is unavailable or unhealthy, but the team currently has real dependency and environment-health risks that cannot be ignored.

### What Is Working Well

- There was agreement that the existing real-environment integration tests have value when they observe how Pico responds to Exerp-originated events.
- Valuable observable events include order updates returned after Exerp processing, plus the `person created` and extended-attribute-change messages handled through the Exerp adapter during person creation.
- The discussion reached a shared position that tests need a deliberate balance between mocked dependency coverage and a smaller set of real integration journeys.
- The call was candid and constructive despite different starting positions on the architecture and test boundaries.

### What They Asked For

- Prefer dynamic test-data discovery or creation over reliance on static shared data.
- Keep Pico aligned to its original source-of-truth intent wherever the current architecture genuinely supports that model.
- Use mocks deliberately for external dependencies where the behaviour under test is Pico's own logic, rather than automatically expanding real-system dependency coverage.
- Use observability and SRE signals as part of detecting and understanding production failure modes.

## Themes And Interpretation

- Directly stated: Pico's original design should remain influential; it should not unnecessarily become dependent on Exerp for correctness.
- Directly stated: Static test data has historically caused problems and should be replaced by dynamic data handling.
- Directly stated: Maintaining a full Exerp estate for every brand and environment is expensive; more mocked alternatives may be appropriate over the longer term.
- Directly stated: Monitoring and SRE signals are useful for identifying real production issues.
- My interpretation: The practical test strategy must reflect the platform as it exists. Unit and service-level tests should mock dependencies where that isolates Pico behaviour, while selected end-to-end journeys should use real Exerp to verify Pico's handling of the events and responses it depends on.
- My interpretation: Real Exerp-backed tests should assert Pico's receipt and handling of responses, not attempt to validate Exerp itself. This preserves the value of integration evidence without making Exerp's internal implementation the assertion boundary.
- My interpretation: UK is the flagship platform and needs a viable end-to-end route through preview, staging, and production. A longer-term, brand-scalable model may use more Exerp mocking or shared alternatives where dedicated environments are not justified.
- My interpretation: SRE signals complement proactive QA and automation; they cannot replace pre-release testing because production detection accepts customer and operational exposure.
- Hypotheses to validate: Dynamically created or discovered test data will materially reduce preview and staging test flakiness compared with the current static-data approach.
- Hypotheses to validate: A tiered model can keep most checks mocked and fast while retaining a small, stable real-Exerp suite for flows such as cancellation and person creation.
- Hypotheses to validate: Three end-to-end UK environments (preview, staging, production) are sufficient for current delivery needs, with broader multi-brand Exerp environment options treated as a longer-term architecture and cost decision.

## Mapping

### Strategic Mission(s)

- Technical Mastery & Foundations
- Delivery Flow & Resilience
- Business Risk & Stakeholder Trust

### Role Pillar(s)

- Automation Trust & Reliability
- Test Infrastructure, Environments & Data
- Business-Critical Journey Protection
- Non-Functional Quality & Resilience

### Objective Lens(es)

- Business Operator
- Value Creator

### Related 30/60/90 Focus Area(s)

- Automation
- Ownership
- Productivity

## Related Context

- Builds on [2026-09-17 Principal Engineer SRE / Pico backend testing strategy](2026-09-17-principal-engineer-pico-backend-testing-strategy.md), which identified the value of deployed-preview journeys extending through real Exerp responses.
- Related to [Improvement 02 - Dynamic Member Creation And Test Data](../../improvements/02-dynamic-member-creation-and-test-data.md), particularly the need to remove static-data dependency from automated journeys.
- Related to [Challenge 08 - Exerp Extractor Reconciliation And Data Integrity](../../challenges/08-exerp-extractor-reconciliation-and-data-integrity.md), but with a different focus: this discussion concerns transactional behaviour, event handling, and test-environment strategy rather than extractor reconciliation.

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Define the test-tier decision rules** — Owner: AC / Backend Technical Leads — Destination: Decision — Notes: Document when a dependency is mocked, when a real integration path is required, and what the assertion boundary is for each tier.
- **Prioritise dynamic test data** — Owner: AC / Automation owners — Destination: Improvement 02 — Notes: Identify the existing static records that cause instability and replace them with safely created or discovered data.
- **Confirm UK end-to-end environment expectation** — Owner: AC / Platform and delivery leads — Destination: Notion / Alignment — Notes: Establish whether preview and staging can reliably support the real journeys needed before evaluating wider multi-brand provision.
- **Separate current needs from longer-term environment strategy** — Owner: AC / Architecture stakeholders — Destination: Challenge / Decision — Notes: Current delivery needs real end-to-end UK coverage; scalable mock or shared-Exerp approaches need a separate cost and architecture decision.
- **Define health gating for real-dependency tests** — Owner: AC / SRE / Automation owners — Destination: Notion / Alignment — Notes: Distinguish genuine product failures from known environment or Exerp availability issues without suppressing dependency-health evidence.

## Possible Outputs

- Candidate challenge: The current platform has a mixed Pico-first and Exerp-dependent architecture, but the test strategy does not yet make the dependency boundary explicit by journey.
- Candidate decision: Adopt a tiered test policy: mocked tests for Pico-local behaviour, real Exerp-backed tests for journeys that depend on Exerp confirmation or event responses, and Pico-owned assertion boundaries for those real journeys.
- Candidate decision: Treat dynamic test-data capability as a prerequisite for expanding reliable preview and staging automation.
- Candidate goal input: Establish stable, data-independent end-to-end coverage for the UK platform across the necessary non-production environments.
- Candidate achievement evidence: Reached a shared, nuanced position with a key Pico architect on balancing original design intent with the dependencies the platform has today.

## Open Questions

- Which current business journeys materially wait for, or change outcome based on, an Exerp response, confirmation, or event?
- For each real-Exerp journey, what Pico-owned state or event is the correct stable assertion boundary?
- Which static data dependencies are the principal causes of test instability today, and can each be dynamically created, reserved, or discovered safely?
- What health signals can identify an Exerp or environment issue before a test run is classified as a product failure?
- Does the UK platform currently have reliable preview and staging routes capable of supporting the required end-to-end journeys?
- What is the costed, scalable alternative for brands that do not justify dedicated Exerp non-production instances?
