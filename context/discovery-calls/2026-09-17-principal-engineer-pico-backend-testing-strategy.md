---
id: DC-2026-09-17-principal-engineer-pico-backend-testing-strategy
type: discovery-call
date: 2026-09-17
pillars: [P4, P5, P7, P8]
focus: [ownership, automation]
links: [CH-08]
people: [JFG]
---

# 2026-09-17 - Principal Engineer SRE / Pico (Backend Testing Strategy Follow-Up)

## Call Context

- **Date:** 2026-09-17
- **Source / role:** Principal Engineer, Pico / Exerp / Support / SRE
- **Conversation type:** Engineering discovery (extension of existing thread)
- **Related team or platform:** Pico backend (Account, Basket, Exerp Adapter), Exerp, Kafka, staging
- **Notes based on:** Short follow-up conversation, supported by earlier codebase review and call prep
- **Parallel conversations planned:** BE Tech Lead, Basket and BE Tech Lead, Account — calls next week to confirm ownership, implementation practicality, and alignment.

## Purpose

- Strategise how Pico approaches backend testing given that alignment between Exerp and Pico is increasingly critical to app/portal correctness — not a peripheral concern.
- Challenge the long-standing assumption that "Pico is the source of truth, we don't care about Exerp" and agree whether/how that needs to change.
- Land on a concrete test-tier model with the Principal Engineer, using the Account suite as the proven starting pattern.

## Why Now

A code review surfaced three incidents where Pico's *internal* view of correctness diverged from what Exerp *actually did* with the data Pico sent it:

- `PREJ-1448` — orgCode revert
- Partial-postcode client error
- Fixed-term date: fix → revert → re-fix

These aren't isolated bugs — they're a pattern: Pico assumed a response shape or behaviour from Exerp that didn't hold in practice. The "Pico is the source of truth" framing is an **assumption, not a verified fact**, and these incidents are the evidence.

## Key Signals

### What Matters To Them

- The philosophy that Pico only needs to care about Pico is dated and no longer reflects the expected quality bar. Alignment between Pico and external systems, particularly Exerp, matters for shared app and portal journeys.
- More real-environment integration coverage is valuable, following the pattern JFG has established: tests run against deployed preview environments rather than only containerised dependencies.
- The value is not simply more tests. The tests must be stable enough to trust, target meaningful risks, and catch failures that matter to the business.
- This pattern can extend beyond Account to Basket, Exerp Adapter, and other services where cross-service or external-system behaviour creates material risk.

### Current Friction Or Risks

- Current service-local tests can pass while Pico's assumptions about Exerp behaviour or responses are wrong.
- Preview-environment journeys risk becoming brittle if they depend on unstable data, timing, or internal implementation details rather than observable business outcomes.
- Ownership is unclear: the journeys protect shared web and app concerns, so placing the repository solely under either the web or app release-lead remit could dilute accountability.

### What Is Working Well

- JFG's deployed-preview integration approach provides a practical, proven starting point rather than a new test model to invent from scratch.
- The Principal Engineer agreed with both the problem framing and the value of extending coverage across services.

### What They Asked For

- Build on the deployed-preview integration-test approach, prioritising stable, valuable coverage over volume.
- Confirm the practical scope and ownership model with the Basket and Account BE Tech Leads before setting the direction.

## Themes And Interpretation

- Directly stated: Pico-only correctness is no longer an adequate design philosophy where app and portal journeys depend on Exerp alignment.
- Directly stated: Deployed-preview integration tests have value and can be applied more broadly than Account.
- Directly stated: Test brittleness and relevance are the constraints to manage as coverage expands.
- My interpretation: A shared repository or shared-quality ownership model is the likely fit because the risks and releases cross web and app boundaries; it should be confirmed with the two BE Tech Leads and the relevant release leads before becoming a decision.
- Hypotheses to validate: A small set of cross-service, deployed-preview journeys will detect meaningful Pico/Exerp divergence earlier without creating an unreliable suite.
- Hypotheses to validate: Shared release-lead accountability will prevent the repository becoming an unowned cross-cutting asset.

## Test Strategy Discussed

### Test tier model

1. **Silo test** (current unit/Testcontainers layer) — "does my service do what I coded it to do, against my own mocked/ephemeral view of the world." Keep this; fast, should stay the largest layer.
2. **Journey test against a real deployed instance, observable business outcomes only** (GraphQL response → real Kafka event → real Neon state) — this is what Account's suite already does well, but scoped only to Pico's own services.
3. **Missing tier** — same journeys, but the assertion boundary extends *through* the real external system (real Exerp proxy/sandbox, real Braze) and back: not just "did we write the row" but "did Exerp actually reflect the change, and did we correctly react to what it sent back, including its error shapes." This is the tier that would have caught the postcode and orgCode-type bugs before shipping.

### Silent failure principle

Current suites mostly assert happy-path state (`WaitForX`) — failures only surface via timeout. Propose adding first-class assertions on **failure/DLQ paths** (dead-letter topics, Exerp error-response shapes), not just happy path — this directly targets "things fail silently until someone reads the logs."

### Extending the Account pattern

**Today's pattern (single-service scope):** real GraphQL call → real Neon DB assertion → wait-for-Kafka-consumption. Upstream inputs (e.g. Basket's order data) are synthetically fabricated rather than produced by calling that service for real — proves "Account behaves correctly given real infra and a given input," but nothing about whether the input was realistic.

1. **Extend the same single-service pattern to Basket** — high value, lower effort than it sounds: same recipe, pointed at Basket's own mutations (`createShoppingBasket`, `updateShoppingBasket`, `createOrder`). Call real mutation → wait for real Kafka `OrderDefined`/`OrderUpdated` → assert Basket's own Neon state. This is where `MXPO-406`'s fixed-term end-date bug lived, and it currently has **zero automated real-environment coverage** (`APITestAutomation` exists with this scope but isn't wired into CI).
2. **Multi-service E2E (Account → Basket → Exerp → back into Pico)** — distinct, higher-value tier: trigger a real flow via GraphQL, let it propagate across service boundaries, and where Exerp is invoked, wait for Exerp's genuine response to land back in Pico (via whatever consumer/webhook `exerp-adapter` uses) and assert against **Pico's own resulting state** — not Exerp's internals. Different from the currently-disabled `Integration tests.feature` (which reaches directly into Exerp): this validates "did Pico correctly handle what Exerp actually sent back," treating Exerp as a real black-box dependency rather than a trusted assumption or a queried source of truth.
   - Both `PREJ-1448` (orgCode revert) and the partial-postcode fix were bugs in how Pico *handled Exerp's real response shape*, not bugs in what Exerp's database contained — this tier would have caught both without querying Exerp directly.
   - Natural home for the `WEB-402` suspended-status class of bug too, since a flow spanning Account and Exerp Adapter surfaces a disagreement in state rather than each service's isolated tests independently passing against their own assumptions.

## Open Decision: Assertion Boundary

Given the multi-service E2E tier only requires waiting on Exerp's real response *arriving into Pico*, is there separate value in also directly querying/asserting against Exerp's own state (as the disabled `Integration tests.feature` already does) — or does that duplicate/over-couple to Exerp's internals once the E2E flow exists? Treat this as a deliberate decision, not something to leave disabled by default.

## Mapping

### Strategic Mission(s)

- Technical Mastery & Foundations
- Business Risk & Stakeholder Trust
- Delivery Flow & Resilience

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

## Related Context

- Builds on [2026-09-01 Principal Engineer SRE / Pico](2026-09-01-principal-engineer-sre-pico.md) (staging as gold standard, Exerp/Pico data drift).
- Adjacent to [Challenge 08 — Exerp Extractor Reconciliation And Data Integrity](../../challenges/08-exerp-extractor-reconciliation-and-data-integrity.md), but distinct scope: Challenge 08 covers commercial/pricing data extraction and reconciliation; this call covers transactional/member-state behavioural alignment (orgCode, postcode, fixed-term dates) surfaced through real-time Kafka event flows rather than batch extraction.

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Confirm CI status of `APITestAutomation`** — Owner: AC — Destination: Notion / Alignment — Notes: Verify it exists for Basket-scope real-mutation testing but is not wired into CI before proposing it as a near-term gap to close.
- **Decide on `Integration tests.feature`** — Owner: AC / Principal Eng — Destination: Decision — Notes: Re-enable with narrower purpose, or retire in favour of the multi-service E2E tier — don't leave it disabled by default.
- **Confirm with BE Tech Lead, Basket** — Owner: AC — Destination: Notion / Alignment — Notes: Sense-check the "extend Account pattern to Basket" proposal, `APITestAutomation` CI-wiring gap, and whether a shared repo is workable.
- **Confirm with BE Tech Lead, Account** — Owner: AC — Destination: Notion / Alignment — Notes: Sense-check the multi-service E2E tier (Account → Basket → Exerp → Pico), the `exerp-adapter` consumer/webhook assumption, and shared web/app release-lead accountability.
- **Propose an ownership model** — Owner: AC / Web and App Release Leads — Destination: Decision — Notes: Validate whether this becomes one shared repository and a joint release-quality expectation rather than a web-only or app-only concern.

## Possible Outputs

- Candidate challenge: The historical Pico-only correctness philosophy does not protect app and portal journeys where Exerp and Pico must align.
- Candidate decision: Adopt a three-tier test model (silo / single-service journey / multi-service E2E through real Exerp) as the standard for Pico backend services.
- Candidate decision: Whether to wire `APITestAutomation` into CI for Basket as a near-term, low-effort win.
- Candidate decision: Fate of the disabled `Integration tests.feature` (retire vs. re-scope vs. keep as a supplementary direct-Exerp check).
- Candidate goal input: Extend the Account real-environment testing pattern to Basket and to a first multi-service E2E flow (Account → Basket → Exerp → Pico).
- Candidate decision: Establish a shared repository with joint web/app release-lead accountability for the cross-service preview journey suite.

## Open Questions

- What is Exerp's actual error-response shape across the scenarios that caused `PREJ-1448` and the postcode bug — is it documented anywhere, or only known empirically?
- Does `exerp-adapter` have a stable consumer/webhook hook that a test can reliably wait on for "Exerp's response landed back in Pico"?
- Is there a sandbox/proxy version of Exerp stable enough to run this tier in CI, or does it require a shared real environment (staging)?
- How does this tier relate to the Principal Engineer's existing staging-as-gold-standard priority — does it depend on staging health work landing first, or can it proceed in parallel?
- Who owns `exerp-adapter` today, and would they need to be part of designing the assertion points for the multi-service tier?
- Should the test repository be owned jointly by the web and app release leads, and what does shared accountability mean in practice for contribution, triage, and release expectations?
