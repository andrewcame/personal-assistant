---
id: DC-2026-09-16-it-pricing-manager-cr
type: discovery-call
date: 2026-09-16
pillars: [P2, P5, P7, P8, P10]
focus: [people, ownership, automation, productivity]
links: [CH-08]
people: [CR]
---

# 2026-09-16 - IT Pricing Manager - CR

## Call Context

- **Date:** 2026-09-16
- **Source / role:** CR, IT Pricing Manager
- **Conversation type:** Engineering discovery / stakeholder discovery
- **Related team or platform:** Exerp configuration, COP (Commercial Offering Platform), Exerp Extractor/Publisher, Pico, staging, preview, promotions, pricing, subscriptions
- **Notes based on:** Personal notes / discovery conversation

## Purpose

- Understand how pricing and commercial configuration reaches Pico, how the environments are used by Configuration, and where QA can better test the member-facing experience, promotions, pricing, and data reconciliation.

## Key Signals

### What Matters To Them

- Testing should reflect how members use the system, not just whether an individual technical change works in isolation.
- Staging should be a realistic shared environment where Configuration can test promotions and campaigns alongside development and QA.
- Changes need to be communicated clearly to the people whose time and configuration work they depend on.
- QA needs access to the relevant configuration platforms and enough context to understand how pricing and promotions are set up.

### Current Friction Or Risks

- Pricing and commercial data reaches Pico through multiple routes: COP handles commercial offerings such as promotions, while prices and products come through Exerp via the Exerp Extractor and Publisher.
- The Exerp Extractor is a significant reliability risk. It is expected to work automatically, but it does not always extract all data accurately; CR regularly has to correct production and reconcile it back to Exerp.
- The extraction/publishing path is difficult to validate today because it is a long, scheduled chain: a full Exerp extract takes about an hour, publishing into Pico databases follows, and a front-end site rebuild is then needed before the latest prices/products are visible. End to end, this can take around 90 minutes.
- Extract or publish failures can enter a dead-letter queue, leaving Pico out of sync with Exerp without an immediately obvious product failure.
- The current development Exerp environments (PG Dev and Pico 2), which feed the preview ecosystem, are primarily treated as development/QA environments. Configuration does not test promotions there.
- Staging is the only environment shared by Configuration and development where promotions and campaigns are tested, which gives staging more realism and purpose than preview but also increases the importance of keeping it healthy and aligned.
- Changes can go live without the people who need to configure or support them being told. CR cited a student-related fix that required her time and resource even though she was not directly informed beforehand.
- CR is not deeply technical and cannot be expected to follow every cross-team engineering conversation, so the communication mechanism needs to be clear and deliberate.

### What Is Working Well

- Staging is currently the most realistic shared environment because Configuration tests campaigns and promotions there.
- CR is willing to demonstrate how to set up promotions and campaigns, which are among the harder commercial scenarios to configure.
- Configuration can help clarify what should exist in an environment and how pricing/promotion behaviour should be validated.
- The broad direction to improve staging health and understand environment configuration has support from the Configuration side.

### What They Asked For / Suggested

- Think more deliberately about the member/user experience when designing test scenarios and reviewing staging issues.
- Improve communication of changes that require Configuration involvement, especially changes that affect promotions, pricing, subscriptions, or campaign setup.
- Provide clarity on what configuration exists in each environment; CR is happy to help where needed.
- Arrange time for a practical walkthrough of promotion and campaign setup.
- Ensure QA gets access to COP in both staging and production so it can understand and maintain commercial configuration safely.

## Architecture And Data Flow

- Commercial offerings and promotions are managed through COP.
- Prices and products are extracted from Exerp by the Exerp Extractor.
- The extracted data is published into Pico databases by the Exerp Publisher.
- The front-end then needs a new site build to consume the latest prices and products.
- The full scheduled flow can take approximately 90 minutes and can fail at extraction or publication, including through dead-letter handling.

## Themes And Interpretation

- Directly stated: QA should think more like a member and test the experience, not only the technical implementation.
- Directly stated: the Exerp Extractor does not always produce a reliable or complete result and can require production reconciliation back to Exerp.
- Directly stated: staging is the only environment where Configuration and development/QA currently test together, including promotions and campaigns.
- Directly stated: preview Exerp environments are simpler from a testing perspective because Configuration does not currently test promotions there; whatever is configured in development Exerp needs to support ticket testing in preview.
- Directly stated: changes are sometimes released without the Configuration Manager knowing, even when the change consumes Configuration time and resource.
- My interpretation: the Extractor is not just an integration implementation detail; it is a business-critical data integrity boundary between Exerp and Pico and deserves its own test and reconciliation strategy.
- My interpretation: the promotion/campaign walkthrough is a practical way to improve QA's domain understanding and make staging scenarios more representative.
- My interpretation: staging's shared use is valuable because it increases realism, but it also creates a stronger need for clear ownership, monitoring, configuration visibility, and communication.
- My interpretation: change communication should be treated as part of delivery readiness where a release depends on Configuration action, rather than relying on Configuration to discover changes after release.
- Hypotheses to validate: a reconciliation check comparing extracted/published Exerp data with the corresponding Pico data could detect drift before it reaches production.
- Hypotheses to validate: a small catalogue of representative promotion, pricing, and subscription scenarios would provide more useful confidence than relying on generic ticket-level checks.

## Mapping

### Strategic Mission(s)

- Technical Mastery & Foundations
- Business Risk & Stakeholder Trust
- Delivery Flow & Resilience
- People & Practice

### Role Pillar(s)

- Test Infrastructure, Environments & Data
- Business-Critical Journey Protection
- Non-Functional Quality & Resilience
- Knowledge Sharing & Quality Practice
- Stakeholder Confidence & Visibility

### Objective Lens(es)

- Business Operator
- Value Creator
- People Developer

### Related 30/60/90 Focus Area(s)

- Ownership
- Automation
- Productivity
- People

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Arrange a promotion and campaign configuration walkthrough with CR** — Owner: AC / CR — Destination: Notion / Knowledge sharing — Notes: Use the session to identify realistic QA scenarios and the setup/configuration required in each environment.
- **Obtain COP access in staging and production** — Owner: AC / Configuration — Destination: Notion / Access follow-up — Notes: Required to understand, validate, and maintain commercial configuration safely.
- **Define the Exerp Extractor reconciliation challenge** — Owner: AC / Engineering / Configuration — Destination: Challenge [08-exerp-extractor-reconciliation-and-data-integrity.md](../../challenges/08-exerp-extractor-reconciliation-and-data-integrity.md) — Notes: Capture extraction, publication, front-end rebuild, dead-letter, and Exerp-versus-Pico reconciliation risks.
- **Improve communication for changes requiring Configuration support** — Owner: AC / Engineering leadership — Destination: Ways of Working — Notes: Identify a lightweight mechanism to notify CR/Configuration before changes consume their time or resource.
- **Clarify environment configuration ownership and contents** — Owner: AC / Configuration / Platform — Destination: Notion / Environment strategy — Notes: Document what is configured in PG Dev, Pico 2, preview, staging, and production, and who can change it.

## Possible Outputs

- Candidate challenge: [08-exerp-extractor-reconciliation-and-data-integrity.md](../../challenges/08-exerp-extractor-reconciliation-and-data-integrity.md).
- Candidate improvement: Representative promotion and campaign scenario pack for staging.
- Candidate improvement: Configuration-aware release/change communication.
- Candidate goal input: Member-centred testing across pricing, promotions, subscriptions, and commercial journeys.
- Candidate knowledge-sharing input: COP and Exerp pricing configuration walkthrough for QA.

## Open Questions

- What fields and business rules should be compared between Exerp and Pico to detect meaningful drift?
- Can extraction and publication be made repeatable and observable in non-production environments?
- What should happen when the Extractor partially succeeds or sends work to a dead-letter queue?
- Which promotion, pricing, and subscription scenarios are the minimum representative set for staging?
- Who owns notifying Configuration when a change requires their setup, validation, or production support?
- What access model allows QA to inspect COP in staging and production without creating unsafe production changes?
