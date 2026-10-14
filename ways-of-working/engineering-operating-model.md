# Engineering Operating Model

This page captures how the wider engineering function works and where the QA & Test Engineering Manager role fits.

## Purpose

- Build a clear view of engineering rhythms, decision forums, and information flow.
- Identify where QA needs to contribute, listen, escalate, or provide quality signals.
- Avoid joining every forum by default; understand the purpose and expected contribution.

## Current Understanding

The organisation is adapting to a structure with closer, more direct business involvement and more architecture ownership within engineering. The Principal Engineer is the architectural point of accountability, with Operations and Security providing specialist support. The Tech Lead Chapter is the route for technical challenges that would previously have gone to the architecture council.

## Engineering Rhythm

### Planning And Prioritisation

- **How it works today:** Closer direct involvement from business stakeholders is expected as the new structure settles. High-urgency goal set to migrate off account/bookings microsites by year-end (ahead of March forecast).
- **My role:** Help connect business-critical journeys, batch release plans, and quality risk to prioritisation.
- **Open question:** Who owns prioritisation, discovery, and acceptance criteria without a Product team?

### Delivery Flow

- **How it works today:** Creative delivery models being adopted: grouping backend changes first, then enabling front-end pages. QA moving to feature-complete / batch testing to reduce deploy thrash.
- **My role:** Define acceptance criteria for grouped changes; ensure risk of batching is clearly understood and accepted by leadership.
- **Open question:** What automated regression gating is required before batch merges?

### Release Readiness

- **How it works today:** Shifting from micro-testing every deploy to testing when full features or component groups are assembled, supported by automated regression.
- **My role:** Provide transparent risk assessments and verify regression safety nets.
- **Open question:** How do we balance rapid delivery with production stability on critical journeys?

### Incident / Support Rhythm

- Not yet captured.

### SRE / Operational Health

- **How it works today:** Operations and Security support engineering; QA & Test Engineering Manager actively onboarding to staging monitoring and alert triage as first responder.
- **My role:** Act as first responder on staging alerts to relieve DevEx pressure and protect test environment integrity.
- **Open question:** What runbooks are needed for common staging failure modes?

### Architecture / Technical Challenges

- **How it works today:** Engineering owns more design decisions; the Principal Engineer provides architectural direction and the Tech Lead Chapter replaces the architecture council for shared challenges. Requests like Dynamic Member Creation routed to the Tech Challenges Board.
- **My role:** Surface testability, observability, resilience, accessibility, test data requirements, and release-risk consequences early.
- **Open question:** What requires a written decision record or escalation?

### Engineering Leadership Alignment

- **How it works today:** Escalate unresolved architectural, product, or design blockers to the named engineering leaders and director.
- **My role:** Make quality risks, batch testing trade-offs, and unresolved stakeholder ambiguity visible.

## Calls And Forums

_Link to entries in [cadences.md](cadences.md) once populated._

-

## Inputs QA Should Bring

- Automation health and trust signals.
- Environment and test data health signals.
- Known release risks and confidence gaps.
- Business-critical journey coverage.
- NFR, performance, accessibility, and resilience concerns.
- Team capacity or ownership constraints where relevant.

## Outputs To Capture

- Decisions affecting QA approach, release risk, or quality ownership.
- Repeated process friction that may become a challenge.
- New expectations for QA reporting, involvement, or escalation.
- Follow-ups that belong in Notion, Jira, Teams, challenges, decisions, or goals.

## Current Hypotheses

- Staging health and alerting may become a central engineering confidence signal.
- QA needs closer visibility into SRE/support signals to identify issues before they reach production.
- Backend preview reliability and backend test ownership are likely cross-team problems, not isolated QA problems.
- Direct business stakeholder involvement can improve clarity and reduce rework if decision ownership remains explicit.
- In-house architecture can preserve delivery pace if shared constraints, decision records, and escalation routes are lightweight and visible.
