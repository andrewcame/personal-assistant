---
id: INI-01
type: initiative
status: draft
horizon: now
updated: 2026-09-25
pillars: [P4, P5]
focus: [automation]
goals: []
links: [CH-09, CH-10, IMP-02]
people: [MP, RT]
---

**Initiative Name:** Dynamic Member Creation & Lookup For Portal Automation

**Exec Sponsor:**

**Business Lead:**

**Stakeholders:**

**Value:** Unblocks reliable Portal automation for any test that changes member state (cancel, regrade, etc.)

**Problem Statement**

We cannot reliably automate Portal journeys that change a member's state — cancellation, regrade, and similar — until we have members whose state can safely be updated without affecting other tests.

This leaves us dependent on manual testing to confirm state-changing behavior like cancellation, which doesn't scale and can't give us the same repeatable, regression-safe confidence automation would.

There is also no unified approach to member creation between App and Web automation; each risks solving this independently, duplicating effort and producing inconsistent patterns. The current legacy `Test Data` package is not appropriate and we should look for a simpler Pico approach.

Web automation has already established a precedent for sourcing test data via WunderGraph (the Pico GraphQL entry point), so this initiative extends that existing pattern rather than introducing a new one.

Not addressing this keeps Portal automation gated behind static members which cannot be altered (limiting the scope of portal testing).

**User Story**

- As a QA engineer
- I want to create a fresh, disposable member on demand through Pico,
- So that my test has an isolated member to act on and doesn't collide with, or depend on, any other test's data.

**Objective**

For the first phase, we are proposing we update the `pico.frontend` tests to create a usable test member on demand via Pico (WunderGraph), using the following high level flow:

1. Create a lead via an account mutation
2. Sell the lead a subscription via the basket/order mutation
3. Create a payment agreement to ensure the member is not in debt (this may require kafka `order-defined` and `payment-attempted` events)

Creating members this way through Pico's real join entry points also has a secondary benefit: it simulates real traffic through the services involved (rather than bypassing them via direct Exerp creation), so the creation flow itself exercises the system in a way that's closer to a real join.

We can extend this pattern to **find members in certain states** (for example debt members) at a later date when we need this.

Success looks like: any Portal test can request a newly created member, with clear error handling if creation fails (see Out of Scope) and a documented, reusable pattern that App automation can adopt for its own rollout later.

Making this change within the Pico front-end repo first lets us establish the pattern quickly, directly addresses the immediate lack of Portal automation coverage, and reduces risk by avoiding a dependency where a change in one system could break another. A shared, cross-repo pattern can be looked at later if needed, once this approach has proven out — it is not a prerequisite for this initiative.

**Project Scope**

- Confirm the exact Wundergraph mutations available today for: creating a lead (account mutation), and selling a subscription (basket/order mutation)
- Confirm with payments that the ability to create payment agreements has been established in Pico and is passed to Exerp. Identify the shape and nature of these events.
- Expand the existing Playwright helpers to implement the query/request logic - no shared cross-repo library/service is introduced at this stage
- Define error handling for the case where member creation fails — treat this as equivalent to failing a Pico "Join," since if this step doesn't work the test can't proceed either way; no complex fallback is planned
- Migrate existing Portal tests that mutate member state off the two static shared members onto on-demand created member.
- Document the pattern (mutations used, sequence, error handling) so it can be reused for the future mobile rollout

**Out of scope**

- Mobile/App automation rollout of this pattern — a distinct future initiative once the pattern is proven on Web
- "Find members" capability (sourcing existing members in specific states, e.g. in debt) — a future improvement once creation is stable
- Any new front-end/UI for member creation — this is a backend/API-level test-automation capability only
- Full member creation coverage of every edge-case membership state - this initiative covers standard creation only; edge-case state rules are a future consideration
- A shared, cross-repo member-creation library/service — each repo (Web now, App later) owns its own implementation for now; consolidating into a shared layer can be raised as a later improvement if duplication becomes a problem

**Open items to flag before this can be finalized**

- Confirm the Exerp Adapter does in fact create a Payment Agreement off `order-defined` + `payment-attempted` events for a basket created this way — currently based on RT's and MP's understanding, not yet proven end-to-end
- Confirm which Wundergraph environment (staging vs preview) Portal automation should target, and that the required mutations are exposed there
- Agree whether member-creation failures should hard-fail the test immediately or produce a distinguishable "setup failure" vs "test failure" result

**Supporting Context**

- [Improvement 02 — Dynamic Member Creation And Automated Test Data Architecture](../improvements/02-dynamic-member-creation-and-test-data.md)
- [Challenge 10 — Pico Source-Of-Truth And Exerp-Dependent Test Strategy](../challenges/10-pico-source-of-truth-and-exerp-dependent-test-strategy.md)
- [Challenge 09 — Population-Scale Mobile App Testing And Low-Incidence Defects](../challenges/09-population-scale-mobile-app-testing.md)
- [2026-09-14 SEM Pico Architecture discovery call](../context/discovery-calls/2026-09-14-sem-pico-architecture.md)
- [2026-09-23 Technical Lead, Backend/Portal/Wundergraph discovery call](../context/discovery-calls/2026-09-23-technical-lead-backend-portal-wundergraph.md)
- [2026-09-25 Technical Lead, Pico Backend Legacy Architecture discovery call](../context/discovery-calls/2026-09-25-technical-lead-pico-backend-legacy-architecture.md)
