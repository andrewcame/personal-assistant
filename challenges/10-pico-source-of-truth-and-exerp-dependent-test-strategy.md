---
id: CH-10
type: challenge
status: open
horizon: next
updated: 2026-10-14
pillars: [P4, P5]
focus: [automation]
goals: []
links: [CH-08, IMP-02, INI-01]
people: []
---

# Challenge 10 — Pico Source-Of-Truth And Exerp-Dependent Test Strategy

---

## Context

Pico was originally designed around a clear philosophy: Pico should be the source of truth for its domain, external systems should be isolated behind adapters where possible, and Pico's own behaviour should be tested without making Exerp, IDS, or other dependencies prerequisites for most automated checks. This remains a valuable architectural direction. It supports fast, deterministic tests and avoids making the platform's quality signal dependent on an external system's availability or implementation.

The platform as implemented does not follow that model consistently. Some journeys can remain Pico-first, but others materially depend on Exerp confirmation, responses, or events. For example, the cancellation flow waits for Exerp to confirm the cancellation. Person creation and order flows also produce Exerp-originated events that Pico consumes through the Exerp adapter, including `person created`, extended-attribute changes, and order updates.

This creates competing design philosophies in practice. A fully mocked approach can show that Pico behaves correctly against its expected contract, but cannot show that Pico handles the responses and signals the real Exerp dependency actually produces. Conversely, treating Exerp as a universal real-test dependency makes feedback slower and more fragile, introduces environment cost, and risks validating Exerp rather than Pico.

The current multi-tenant estate makes the environment question harder. Dedicated non-production Exerp instances for every brand would be expensive as the estate grows, yet the UK flagship platform needs dependable end-to-end coverage across preview, staging, and production. Static shared test data further amplifies the problem through collisions, drift, and unclear preconditions.

## Challenge

How do we apply Pico's source-of-truth philosophy without ignoring the real Exerp dependencies built into current member and commercial journeys, so that QA has trustworthy evidence of Pico behaviour without creating an unaffordable, brittle, real-Exerp test estate across every tenant?

The approach needs to define:

- which behaviours can and should be tested with mocked Exerp, IDS, and equivalent dependencies
- which journeys require a real Exerp-backed path because Pico waits for or reacts to its confirmation, response, or event
- Pico-owned assertion boundaries for real integration tests, so the suite verifies Pico's handling rather than Exerp's internal implementation
- how automated tests dynamically create, find, reserve, and dispose of data instead of relying on static shared records
- the minimum UK preview and staging environment capability needed now
- a scalable multi-tenant direction for brands where dedicated Exerp environments are not justified
- how observability, dependency-health checks, and SRE signals distinguish product failures from environmental failures without masking either

## Questions To Explore

### Architecture And Dependency Boundaries

- Which current journeys are genuinely Pico-first, and which materially depend on an Exerp response, confirmation, or event before the member outcome is complete?
- What was the intended contract boundary for each dependency, and where has the implemented platform moved beyond it?
- Which dependencies should remain mocked for fast service-level coverage?
- Which dependencies need real-environment evidence because a mock cannot represent the risk seen in production?
- Where an Exerp-backed test is needed, what Pico-owned state, event, or observable outcome is the appropriate assertion boundary?

### Test Strategy And Automation

- What tiered test model gives most checks fast, deterministic feedback while retaining a small, stable set of real integration journeys?
- Which existing backend tests already cover Pico-local behaviour, and where are the gaps in handling real Exerp responses and events?
- Which high-risk journeys should form the first real-Exerp proof of concept, such as cancellation, person creation, or order updates?
- How should failure and dead-letter paths be asserted so a missing or malformed external response does not surface only as a timeout?
- What conditions should cause an Exerp-backed test to be blocked, retried, quarantined, or reported as dependency-health evidence rather than treated as a product regression?

### Data And Environments

- Which static test records currently cause the most drift, collision, or unreliable precondition problems?
- For each priority journey, can data be safely created, discovered, reserved, mutated, and disposed of at runtime?
- What exact preview and staging configuration does the UK platform need for dependable end-to-end testing today?
- Which environment capabilities are a current delivery requirement, and which belong to a longer-term multi-tenant cost and architecture decision?
- Can shared, sandboxed, or mocked Exerp alternatives provide enough evidence for lower-priority brands without claiming coverage they do not provide?

### Ownership, Observability, And Decision-Making

- Who owns the contract and test evidence where a journey crosses Pico services, Exerp Adapter, and Exerp?
- What dependency health signals should QA, SRE, and engineering share before and during a real-integration test run?
- How should real-environment failures feed back into mocks, contracts, monitoring, and service-level tests?
- What decision criteria would justify expanding, maintaining, or reducing real Exerp coverage over time?

## Initial Position

Pico-first isolation should remain the default for unit, component, and most service-level journey tests. A mock is appropriate where the purpose is to prove Pico's own logic against a defined contract, and it should not be displaced merely because a real dependency exists.

However, the current platform should not be tested as if all journeys are isolated. Where a member outcome depends on Pico receiving or handling an Exerp response, confirmation, or event, a small number of deliberate real-Exerp integration journeys are needed. These tests should assert Pico-owned outcomes: for example, that Pico consumes the event, persists or exposes the expected state, and handles failure paths. They should not query or certify Exerp's internal state unless a separate business reconciliation requirement calls for it.

The immediate opportunity is the planned backend-testing initiative. It should first map dependency boundaries for a limited number of high-risk journeys, establish a tiered test policy, replace the static-data dependencies preventing reliable automation, and prove the model in the UK environments. This is a practical quality intervention, not a decision to recreate a dedicated Exerp estate for every brand.

Over time, the multi-tenant environment model needs an explicit architecture and cost decision. The right answer may combine dedicated real paths for the flagship platform with controlled mocks, sandbox alternatives, or shared services for other brands. Until that decision is made, tests should be clear about what each tier proves and what it cannot prove.

## Status & Next Action

**Status:** Open — captured on 2026-09-25. Pico's original isolation philosophy remains valuable, but the implemented platform has real Exerp-dependent journeys without an agreed test-boundary policy or scalable multi-tenant environment direction.

**Next action:**

1. Use the backend-testing initiative to map a small set of high-risk journeys by dependency type: Pico-local, contract-mocked, and real Exerp-backed.
2. Agree the test-tier decision rules and Pico-owned assertion boundary with the backend technical leads and Exerp Adapter owners.
3. Select one real-Exerp proof-of-concept journey and one dynamic-data scenario for UK preview or staging.
4. Define dependency-health evidence and failure classification for that proof of concept.
5. Record the broader multi-tenant Exerp environment options, costs, and evidence trade-offs as a separate architecture decision once the UK proof establishes the minimum viable model.

**Watch for:**

- The Pico-first philosophy being used to dismiss evidence from journeys that are currently Exerp-dependent.
- Real Exerp tests expanding indiscriminately until they are slow, unstable, costly, and difficult to diagnose.
- Tests asserting Exerp internals rather than Pico's handling of Exerp responses and events.
- Static test data continuing to create false failures or conceal state-dependent defects.
- Environment failures being silently suppressed as test noise, or being misclassified as product failures.
- A UK-focused environment solution being assumed to scale automatically across every brand.

## 2026-10-13 Update — Environments Discussion

Source: [2026-10-13 environments discussion](../context/discovery-calls/2026-10-13-environments-exerp-per-brand.md).

- **Direction (not yet confirmed as a decision):** one Exerp test environment per test brand, as with the microsites. Previews move off PG DEV TEST onto PureGym Test, shared with staging. Exerp is configured once per brand.
- An **Exerp Event Broadcaster** would fan each Exerp event out to the staging and preview adapters; **pico.deployment** would stand up full FE/Supergraph/BE previews per ticket. Payments integration (Kafka access on AKS) is the open blocker.
- **Effect on this challenge:** this gives the multi-tenant environment question a working answer — a shared real Exerp per brand rather than per environment — which is the "separate architecture decision" next action 5 anticipated. It also raises two new QA risks: shared data between previews and staging, and events reaching environments they don't belong to.
- **Effect on the test-tier model:** unchanged. Pico-first mocks remain the default; real-Exerp journeys now have a consistent target (PureGym Test) in both preview and staging.

**Next action (added 2026-10-13):** offer QA-defined impact measures for SOW step 4 (preview spin-up time, preview test pass rate and flakiness, environment-caused failures, Exerp configuration effort) and raise data isolation and event opt-in as design questions before previews are added to the broadcaster.

## Related

- [2026-09-25 Technical Lead, Pico backend / legacy portal architecture](../context/discovery-calls/2026-09-25-technical-lead-pico-backend-legacy-architecture.md) — source discussion on original Pico intent, static data, test boundaries, and the UK environment need.
- [2026-09-17 Principal Engineer SRE / Pico backend testing strategy](../context/discovery-calls/2026-09-17-principal-engineer-pico-backend-testing-strategy.md) — evidence for using selected real-Exerp journeys with Pico-owned assertion boundaries.
- [Improvement 02 - Dynamic Member Creation And Automated Test Data Architecture](../improvements/02-dynamic-member-creation-and-test-data.md) — current initiative addressing static, drifting, and brittle automation data.
- [Challenge 08 - Exerp Extractor Reconciliation And Data Integrity](08-exerp-extractor-reconciliation-and-data-integrity.md) — distinct commercial-data extraction and reconciliation concern; this challenge addresses transactional dependency boundaries and test strategy.
