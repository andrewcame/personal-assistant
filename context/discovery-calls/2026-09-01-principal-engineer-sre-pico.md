---
id: DC-2026-09-01-principal-engineer-sre-pico
type: discovery-call
date: 2026-09-01
pillars: [P2, P3, P4, P5, P6, P7, P8, P10]
focus: [people, ownership, automation, productivity]
links: []
people: [MJ, CR]
---

# 2026-09-01 - Principal Engineer SRE / Pico

## Call Context

- **Date:** 2026-09-01
- **Source / role:** Principal Engineer, Pico / Exerp / Support / SRE
- **Conversation type:** Engineering discovery
- **Related team or platform:** Pico, Exerp, staging, backend previews, test data, SRE, architecture
- **Notes based on:** Personal notes / Dictation

## Purpose

- Understand the architectural and operational constraints around staging, Pico, Exerp, test data, backend previews, and the QA role in shaping better technical outcomes.

## Key Signals

### What Matters To Them

- Staging should become a gold-standard environment and an early warning system for issues before they reach production.
- Staging alerting and reporting should be treated as a priority, aligning with the Staff Engineer DevEx conversation.
- Data and configuration alignment between environments is central to reliable testing.
- Clean, locked-down staging is a prerequisite for meaningful load testing.
- QA should be able to ask better codebase and testing questions through tools such as Mosaic.
- QA tooling should fit the Pico way of doing things, rather than creating isolated tools that only one engineer or team owns.

### Current Friction Or Risks

- Staging has legacy data issues; a data load was underway to resolve some of these.
- Backend previews remain difficult to test, even with existing supporting tooling.
- Backend preview improvements are lower priority than establishing staging as the de facto environment for testing front-end changes.
- Events generated in Exerp to Pico can drift from production behaviour.
- PG Test, which is hooked to staging, should not be used for preview event testing.
- Config drift between production and staging is a risk; rules between the two environments need to be aligned.
- Pico database drift is mainly caused by defects and data misalignment.
- There is a lack of backend tests, consistent with the Staff Engineer DevEx call.
- Brand and environment linkage may become more complex in a multi-brand world; desired UK environment mappings may not remain sustainable from a cost/value perspective.

### What Is Working Well

- There is strong agreement that staging needs to be raised to a production-like standard.
- The Principal Engineer is already engaged in data correction work to improve staging quality.
- The Tech Challenges board includes relevant thinking around reconciliation services to check data integrity and health.
- Existing UK environment linkage can potentially be exploited short-term because the UK remains the biggest market.
- Mosaic may provide a foundation for agentic codebase/documentation support that QA can adapt.

### What They Asked For

- Treat staging as the priority de facto environment for testing front-end changes against.
- Encourage engineers to use PG Dev for preview work rather than PG Test when testing Exerp/event behaviour.
- Speak to Configuration, specifically MJ and CR, about locking down Exerp Test and aligning environment configuration.
- Use technical support to shape robust tooling solutions rather than QA building and owning isolated tools alone.
- Help move engineering behaviour from individual engineer-owned tools toward the Pico way of doing things.

## Themes And Interpretation

- Directly stated: Staging needs to be a gold standard and an early warning system.
- Directly stated: Alerting and reporting for staging should be a priority.
- Directly stated: Load testing on staging depends on having a clean, locked-down environment.
- Directly stated: Finding suitable members for tests is as important as creating members.
- Directly stated: A private supergraph would be needed to support richer member finding, and this requires technical input.
- Directly stated: Backend preview testing is difficult, but staging quality is the higher near-term priority.
- My interpretation: This call reinforces that environment health is not just an automation concern; it is the foundation for QA credibility and release confidence.
- My interpretation: Test data should be treated as a product capability, covering member creation, member discovery, state modelling, and reconciliation.
- My interpretation: The private supergraph dependency is likely a technical challenge or architectural decision rather than a small QA tooling task.
- My interpretation: The role should set direction and identify needs, then partner with architecture/platform to avoid creating unsupported local solutions.
- Hypotheses to validate: Locking down who can create Exerp events in PG Test will reduce staging drift.
- Hypotheses to validate: Reconciliation services could provide useful staging data-health signals and possibly broader production/support value.
- Hypotheses to validate: Mosaic can be adapted into a useful QA knowledge tool for questions such as "how do I test x?"

## Mapping

### Strategic Mission(s)

- Technical Mastery & Foundations
- Delivery Flow & Resilience
- Business Risk & Stakeholder Trust
- People & Practice

### Role Pillar(s)

- Test Infrastructure, Environments & Data
- Automation Trust & Reliability
- Non-Functional Quality & Resilience
- Delivery Confidence & Flow
- Business-Critical Journey Protection
- Stakeholder Confidence & Visibility
- Knowledge Sharing & Quality Practice
- Quality Ownership & Culture

### Objective Lens(es)

- Business Operator
- Value Creator
- People Developer

### Related 30/60/90 Focus Area(s)

- Automation
- Productivity
- Ownership
- People

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Speak to Configuration about Exerp Test access** — Owner: AC — Destination: Notion / Stakeholder follow-up — Notes: Discuss MJ and CR locking down Exerp Test and directing preview testing to PG Dev.
- **Review Mosaic for QA knowledge use** — Owner: AC / QA Leads — Destination: Discovery follow-up / Goal input — Notes: Assess whether it can support questions like "how do I test x?" using codebase context.
- **Track staging data and config drift themes** — Owner: AC / Principal Eng — Destination: Challenge — Notes: Capture Exerp event drift, config drift, and Pico DB drift as root causes of poor confidence.
- **Explore member creation and member finding need** — Owner: AC / Principal Eng — Destination: Challenge / Tech dependency — Notes: Clarify direct Exerp creation, Exerp client creation, Pico join-flow creation, and search.
- **Understand private supergraph dependency** — Owner: AC / Tech board — Destination: Challenge / Decision input — Notes: Use Tech Challenges board access to understand feasibility, ownership, and sequencing.
- **Assess staging suitability for load testing** — Owner: AC / SRE / QA Leads — Destination: Goal input / Challenge — Notes: Validate clean data, locked-down config, Exerp capacity, and alerting before relying on it.

## Possible Outputs

- Candidate challenge: Staging is not yet production-like enough to act as a trusted early warning system.
- Candidate challenge: Exerp event drift, config drift, and Pico database drift are undermining confidence in staging test results.
- Candidate challenge: Member test data requires both creation and discovery capabilities, including support for richer states such as members in debt.
- Candidate challenge: A private supergraph may be needed before QA can build useful member discovery tooling.
- Candidate challenge: Backend preview testing remains difficult, but should be sequenced behind raising staging quality for front-end testing.
- Candidate decision: Whether PG Test should be locked down for staging and PG Dev used for preview event testing.
- Candidate decision: Whether Mosaic should become a QA-facing knowledge and documentation assistant.
- Candidate goal input: Establish staging as the de facto gold-standard test environment and early warning system.
- Candidate goal input: Build a test data strategy covering member creation, member discovery, state modelling, and environment reconciliation.
- Candidate initiative input: Staging data/config health and reconciliation reporting.
- Candidate achievement evidence: Built alignment with Principal Engineering around staging health, test data foundations, and QA's role in shaping technical direction.

## Open Questions

- What specific staging alerts and reports are needed for the first useful early-warning dashboard?
- Which Exerp event types are drifting most from production behaviour?
- Who currently has access to create or alter data in PG Test, and what should the locked-down model be?
- Which configuration rules differ between production and staging today?
- What are the main causes of Pico database drift, and can they be detected automatically?
- What data states do QA and engineers most commonly need to find, not just create?
- What would a private supergraph expose, who would own it, and what are the security constraints?
- How well does Mosaic answer QA-oriented questions today?
- What would be the minimum staging stability required before continuous load testing is useful?
- How underpowered is PG Test / Exerp compared with production, and can that be used deliberately as a throttle/resilience signal?
