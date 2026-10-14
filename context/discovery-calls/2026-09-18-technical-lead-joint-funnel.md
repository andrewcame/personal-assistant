---
id: DC-2026-09-18-technical-lead-joint-funnel
type: discovery-call
date: 2026-09-18
pillars: [P2, P3, P5, P8]
focus: [people, ownership, productivity]
links: []
people: [DJ, LM]
---

# 2026-09-18 - Technical Lead, Joint Funnel / Corporate Membership Types

## Call Context

- **Date:** 2026-09-18
- **Source / role:** Technical Lead, joint funnel; expert in corporate membership types
- **Conversation type:** Engineering discovery
- **Related team or platform:** Joint funnel, corporate membership journeys, preview environments
- **Notes based on:** Personal notes

## Purpose

- Understand how the joint funnel team views shared QA ownership, test information, delivery slicing, and the balance between speed and risk.

## Key Signals

### What Matters To Them

- DevQA, with developers taking on QA activities, is broadly positive and effective when it works. It increases capacity, but adoption is uneven: not every developer wants to test, potentially because of remote working patterns or a preference for development work. This is both a capacity-planning and cultural issue.
- QA notes should include concrete, actionable test steps, so anyone picking up the ticket can understand exactly how to test it.
- Broad involvement in QA, including developers, is valuable when there are good test notes and a good preview environment.

### Current Friction Or Risks

- High-level or abstract QA notes are not useful enough to support consistent testing or shared ownership.
- Uneven willingness to adopt DevQA limits the capacity benefit and may reflect a wider cultural preference for separating development from testing.
- Larger work chunks can introduce more issues, while smaller tickets can deliver value quickly with less risk. The useful balance is not settled and should not be reduced to a rule about ticket size.

### What Is Working Well

- DevQA can be effective and is viewed positively where developers engage with it.
- The lead sees value in testing the right things and involving the people closest to the work, rather than treating QA as a stage owned only by testers.
- DJ has already created a feature map. It is considered worthwhile and may be a useful starting point for the planned session with LM next week, avoiding duplicated work.

### What They Asked For

- Improve ticket test notes so they provide concrete, repeatable instructions and expected outcomes.
- Keep QA focused on value and risk: the exact size of the delivery chunk matters less than identifying where QA adds value and testing the right things.

## Themes And Interpretation

- Directly stated: Delivery should speed up the delivery of value to members, be more experimental with AI and pairing, and produce valuable chunks of code without becoming overly process-driven.
- Directly stated: Smaller chunks can reduce risk and deliver quickly; larger chunks can also be valuable but often introduce issues.
- My interpretation: The emerging direction is quality at speed through proportionate testing and broader ownership, not a final decision to standardise on smaller tickets.
- My interpretation: Good test notes and a reliable preview environment are prerequisites for making shared QA ownership practical.
- Hypotheses to validate: Uneven DevQA adoption is driven by both capacity and culture, and may need different responses for motivation, context, and working patterns.

## Mapping

### Strategic Mission(s)

- People & Practice
- Delivery Flow & Resilience
- Business Risk & Stakeholder Trust

### Role Pillar(s)

- Quality Ownership & Culture
- Knowledge Sharing & Quality Practice
- Test Infrastructure, Environments & Data
- Business-Critical Journey Protection

### Objective Lens(es)

- People Developer
- Value Creator
- Business Operator

### Related 30/60/90 Focus Area(s)

- People
- Ownership
- Productivity

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Use DJ's existing feature map as the starting point for the LM session** — Owner: AC — Destination: Notion / Alignment — Notes: Confirm whether it covers the required joint-funnel and corporate-membership perspective before creating anything new.
- **Clarify the phrase "get as many people as possible to do QA, devs included. Make sure we've got good test notes in a good preview environment."** — Owner: AC — Destination: Notion / Alignment — Notes: Recover the original context and intended implication; this is a follow-up question, not a recorded fact.

## Possible Outputs

- Candidate challenge: Make shared QA ownership practical by improving test-note quality and preview-environment reliability while understanding the cultural barriers to DevQA adoption.
- Candidate decision: None yet; the call supports a balanced quality-at-speed direction but not a final ticket-slicing or ownership model.
- Candidate goal input: Establish a standard for actionable ticket test notes and identify where QA adds the most value across joint-funnel work.
- Candidate achievement evidence: None yet.

## Open Questions

- What specifically explains the uneven adoption of DevQA, and which parts are capacity, preference, remote-working pattern, or team culture?
- What is the minimum content a ticket's QA notes must include so another person can test it without additional interpretation?
- Which parts of DJ's feature map are most useful for the planned LM session?
- What preview-environment capabilities are required for developers and testers to share QA responsibility confidently?