---
id: DC-2026-10-21-annual-conference-team-conversations
type: discovery-call
date: 2026-10-21
pillars: [P6, P9, P5]
focus: [automation, productivity, ownership]
links: [CH-10, CH-11]
people: [GL, LMo]
---

# 2026-10-21 - Annual Conference: Team Conversations

## Call Context

- **Date:** 2026-10-21
- **Source / role:** Informal conversations with colleagues at the annual conference and awards ceremony, including LMo (Technical Lead, Pico architect) and GL
- **Conversation type:** Other (informal team sounding)
- **Related team or platform:** Engineering-wide; Exerp-dependent testing (CH-10)
- **Notes based on:** Personal notes

## Purpose

- Sense what matters to colleagues and the mood of the wider team. The business direction from the same event is in [leadership-direction](../leadership-direction.md).

## Key Signals

### What Matters To Them

- Speed versus quality, and how AI is being used, came up in most conversations.

### Current Friction Or Risks

- **Over-use of AI** and **speed versus quality** were the common complaints across most people AC spoke to.
- **Where to test, in prod or in staging:** LMo's view is that a lot of testing is based in production using SRE (monitoring and observability), and that distributed systems are more often than not tested that way with mocking. AC's view is that there should be good coverage in staging and real integration, and AC is not willing to accept "no real QA with Exerp" until later because that still feels risky.

### What Is Working Well

- The disagreement is open and not a blocker: both approaches can coexist. GL agreed with both views.

### What They Asked For

- None recorded.

## Themes And Interpretation

- Directly stated: LMo favours mocking plus production-based testing through SRE; AC favours real integration; GL agreed with both; speed versus quality and AI over-use were widely mentioned.
- My interpretation: The two positions map onto the tiered model already proposed in CH-10 (Pico-first mocks by default, a small number of deliberate real-Exerp journeys). The open question is how much real-Exerp coverage is needed now rather than later.
- Hypotheses to validate: Wider industry practice for distributed systems may lean towards production observability plus contract tests or mocks. Check before treating "mocking is the norm" as settled either way.

## Mapping

### Strategic Mission(s)

- Technical Mastery & Foundations
- Delivery Flow & Resilience

### Role Pillar(s)

- P6 Delivery Confidence & Flow
- P9 AI-Enabled Testing & Innovation
- P5 Test Infrastructure, Environments & Data

### Objective Lens(es)

- Value Creator
- Business Operator

### Related Focus Area(s) (People / Ownership / Automation / Productivity)

- Automation
- Productivity
- Ownership

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Industry research on testing in production and SRE versus mocking versus real integration for distributed systems** — Owner: AC — Destination: Challenge (CH-10.9) — Notes: Run through the industry-research skill; log the result in industry signals.
- **Square the speed-versus-quality and AI over-use theme into the QA approach** — Owner: AC — Destination: Decision — Notes: Recurring theme; the business leaders are speed- and AI-led (see the 2026-10-21 leadership entry). Related to CH-11.

## Possible Outputs

- Candidate challenge: none new; extends CH-10 and CH-11
- Candidate decision: how much real-Exerp coverage is needed before the later multi-tenant decision (CH-10.7)
- Candidate goal input: none
- Candidate achievement evidence: none

## Open Questions

- What does credible external practice say about production testing and SRE versus mocking versus real integration for distributed systems?
- What is the minimum real-Exerp coverage that makes "later" acceptable?
