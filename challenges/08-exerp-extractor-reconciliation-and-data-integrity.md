---
id: CH-08
type: challenge
status: open
horizon: later
updated: 2026-10-15
pillars: [P5, P8]
focus: [automation]
goals: []
links: []
people: []
---

# Challenge 08 — Exerp Extractor Reconciliation And Data Integrity

---

## Context

Pricing, products, subscriptions, and commercial offerings reach Pico through more than one path. COP manages commercial offerings such as promotions, while prices and products are extracted from Exerp and published into Pico databases before the front end consumes them through a new site build.

The Exerp Extractor is expected to work automatically, but the IT Pricing Manager reports that it does not always extract all data accurately. Production corrections and reconciliation back to Exerp are sometimes required. This creates a risk that Pico can present incomplete or incorrect commercial data even when the source configuration in Exerp is correct.

The process is also slow and asynchronous. A full extract takes approximately an hour because it retrieves all products and prices rather than a scoped subset. Publishing follows, and a front-end site rebuild is then required before the latest data is visible. The complete path can take around 90 minutes. Errors can occur during extraction or publication and may enter a dead-letter queue.

Staging is currently the most realistic shared environment because Configuration tests promotions and campaigns there alongside development and QA. That makes staging useful for validation, but also means its health and configuration need to be reliable enough to expose data-integrity failures before production.

## Challenge

How do we create confidence that pricing, product, subscription, and promotion data extracted from Exerp and published into Pico is complete, accurate, observable, and suitable for member-facing journeys before it reaches production?

The approach needs to account for:

- extraction of the full commercial dataset rather than a scoped gym or scenario
- publication into Pico databases
- the front-end rebuild required before changes are visible
- partial failures and dead-letter handling
- reconciliation between Exerp, the published Pico data, and the member-facing result
- realistic promotion and campaign scenarios in staging
- the operational ownership of correcting drift when the automated path fails

## Questions To Explore

### Data Integrity And Reconciliation

- Which Exerp fields and business rules must be compared with the corresponding Pico data?
- Can we identify a meaningful representative subset while the Extractor remains full-dataset only?
- How do we distinguish a genuine source-data change from an extraction or publication defect?
- Can reconciliation be automated after publication and before the front-end build is treated as ready?
- What evidence is needed to show that a promotion, price, product, or subscription is correct from source to member experience?

### Failure Handling And Observability

- Which extraction and publication failures currently enter a dead-letter queue?
- How are partial extracts or partial publications detected?
- Who owns investigation, replay, correction, and sign-off after a failed run?
- What alerts should be visible in staging and production?
- Can the scheduled 90-minute flow expose progress and failure state clearly enough for QA and Configuration to act?

### Environment And Test Strategy

- What should be configured in PG Dev, Pico 2, preview, staging, and production for reliable testing?
- Which promotion and campaign scenarios should be maintained as a minimum representative staging pack?
- Can Configuration show QA how to set up the hardest promotion and campaign cases?
- How do we test the Extractor and Publisher without relying only on production corrections?
- How should staging's shared use by Configuration, development, and QA be protected from accidental drift?

### Member Experience And Release Readiness

- Which member journeys are most sensitive to pricing, promotion, product, or subscription drift?
- How do we test what a member sees after extraction, publication, and front-end rebuild?
- When a release requires Configuration action, what communication and acceptance step is needed before production?
- What is the minimum confidence signal required before a commercial-data change is released?

## Initial Position

The Exerp Extractor should be treated as a business-critical integration and data-integrity boundary, not only as background platform plumbing. A useful first step is to document the source-to-member flow, select representative promotion/pricing/subscription scenarios with Configuration, and define a small set of reconciliation checks between Exerp and Pico.

The full-dataset extraction and 90-minute propagation time may limit fast feedback, so the strategy should combine targeted representative scenarios with post-run reconciliation and clear failure visibility. Staging is the natural proving ground because Configuration already tests campaigns and promotions there, but its shared role makes environment ownership and communication important prerequisites.

## Roadmap

| ID | Step | Owner | Depends on | Status |
|----|------|-------|------------|--------|
| CH-08.1 | Arrange COP and promotion walkthrough with CR | AC | CH-08.6 | later |
| CH-08.2 | Map Extractor to Publisher to Pico to front-end flow | AC | CH-08.1 | later |
| CH-08.3 | Select representative commercial scenarios for staging | AC | CH-08.2 | later |
| CH-08.4 | Define minimum Exerp-versus-Pico reconciliation checks | AC | CH-08.3 | later |
| CH-08.5 | Confirm ownership for failed runs, replay and sign-off | AC | CH-08.2 | later |
| CH-08.6 | Discover Extractor usage and sunset plan; decide if testing is needed | AC | — | later |

## Status & Next Action

**Status:** Open — reliability and reconciliation evidence are not yet defined, and production correction is sometimes needed.

**Next action:**

1. Arrange the COP and promotion/campaign walkthrough with the IT Pricing Manager.
2. Map the Exerp Extractor → Publisher → Pico database → front-end build flow, including dead-letter paths.
3. Select a representative set of commercial scenarios for staging.
4. Identify the minimum Exerp-versus-Pico fields and outcomes to reconcile.
5. Confirm ownership for failed runs, replay, correction, and release sign-off.

**Watch for:**

- Pricing or promotion defects first discovered by members or Configuration after release.
- Extractor failures that are not visible until a later front-end build or member journey.
- Dead-letter items without an owner or replay process.
- Staging scenarios that do not reflect the commercial configuration used in production.
- Production reconciliation becoming the normal way to discover data-integrity problems.
