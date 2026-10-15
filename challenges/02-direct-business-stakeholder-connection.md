---
id: CH-02
type: challenge
status: open
horizon: later
updated: 2026-10-15
pillars: [P8, P10]
focus: [ownership]
goals: []
links: []
people: []
---

# Challenge 02 — Rebuilding Direct Business Stakeholder Connection

---

## Context

A recent organisational reshuffle removed the Product team supporting the engineering organisation. This has weakened the established connection between engineering and the business, including the route by which needs, priorities, acceptance criteria, and business context reach squads.

The new structure is intended to put engineering closer to the business and the decision makers who can maximise the impact of the team's work. That creates an opportunity for more direct stakeholder involvement, but it also means the organisation needs clear ownership for discovery, prioritisation, requirements, and feedback rather than allowing those responsibilities to become informal or fragmented.

The absence of Product is already visible in Payments: there is limited interaction with stakeholders, and technical people can end up filtering or interpreting needs without enough connection to the business outcome. Domain reviews and business-critical journey mapping may help establish a shared functional view while the new model settles.

## Challenge

As the QA & Test Engineering Manager, how do I help engineering build a direct, productive relationship with business stakeholders while:

- keeping business priorities and member outcomes visible in technical decisions
- making acceptance criteria and business-critical journeys clear and testable
- avoiding QA becoming a substitute Product function or the sole translator of business needs
- creating a practical feedback loop that works without adding unnecessary process
- ensuring stakeholder involvement improves delivery confidence rather than creating more conflicting inputs

## Questions To Explore

### Stakeholder Connection

- Which business stakeholders own the outcomes for each domain, and how do squads reach them directly?
- Which forums or regular touchpoints are needed for Finance, Commercial, market teams, and other domain stakeholders?
- What does useful quality and release confidence look like to each stakeholder group?
- How do we ensure important stakeholder knowledge is shared rather than held by one person?

### Product And Delivery Ownership

- Who owns discovery, prioritisation, scope, acceptance criteria, and the final business call in the new structure?
- Where should engineering, QA, and stakeholders collaborate directly, and where is a clear accountable owner still needed?
- How do we identify and resolve ambiguity before work reaches implementation?
- What should be escalated when the business need, technical interpretation, or delivery scope is unclear?

### Evidence And Outcomes

- Which member and revenue-critical journeys should anchor the initial stakeholder conversations?
- Can domain reviews provide a useful functional baseline in the absence of Product?
- How will we know that direct involvement is improving outcomes: less rework, clearer acceptance, faster decisions, or stronger release confidence?

## Initial Position

The new structure should be treated as an opportunity to get closer to the business, not as permission for engineering to make assumptions on the business's behalf. Direct stakeholder involvement should become normal for shaping important work and understanding risk.

QA can help expose ambiguity, map user journeys, and translate quality risk into business language, but it should not quietly become the replacement Product function. Engineering, QA, delivery, and stakeholders need an explicit working agreement about who brings context, who makes decisions, and how disagreements are resolved.

Start with the highest-value domains, use real journeys rather than abstract requirements, and keep the feedback loop lightweight enough that it supports pace.

## Roadmap

| ID | Step | Owner | Depends on | Status |
|----|------|-------|------------|--------|
| CH-02.1 | Map stakeholders and decision owners for critical domains | AC | — | later |
| CH-02.2 | Validate business journeys through the domain reviews | AC | CH-02.1 | later |
| CH-02.3 | Agree regular stakeholder touchpoints for shaping work | AC | CH-02.2 | later |
| CH-02.4 | Decide which business relationships QA needs to build | AC | CH-02.1 | later |

## Status & Next Action

**Status:** Open — adapting to the new organisational structure.

**Next action:** Map the key stakeholders and decision owners for Payments and the other critical domains. Use the planned domain reviews to validate business journeys, identify missing context, and agree a small set of regular touchpoints for shaping work and discussing quality confidence.

**Watch for:**

- engineering interpreting stakeholder needs without direct validation
- acceptance criteria becoming increasingly technical while the business outcome is lost
- QA being pulled into Product ownership by default
- decisions or priorities differing between stakeholder conversations
- evidence that direct involvement is reducing rework and improving confidence
