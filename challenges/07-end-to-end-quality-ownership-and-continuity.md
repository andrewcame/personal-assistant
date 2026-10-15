---
id: CH-07
type: challenge
status: open
horizon: next
updated: 2026-10-15
pillars: [P2, P3, P8]
focus: [people]
goals: []
links: []
people: [LM]
---

# Challenge 07 — End-to-End Quality Ownership And Continuity

---

## Context

The current delivery model creates initiative-level E2E work after component tickets have been completed. Individual QAs test their tickets as they are delivered, then a later E2E ticket is created when the wider initiative is ready. LM currently picks up these tickets as the cross-platform E2E contractor.

This model is being used for complex Portal and migration journeys such as:

- cancellation and other membership-change workflows
- student join journeys
- city pages and related member journeys
- regrading and changing member or subscription types
- freezes, adding multiple gyms, and other member benefits
- migration of Microsite journeys into the Portal

These journeys are more complex than a single join funnel. They require coordinated data to be correct in Pico and Exerp, may change Exerp descriptions or member types, and often need broad manual scenario coverage across the full customer journey. Much of the value comes from exploratory and manual testing that is difficult to reproduce fully through automation.

LM provides valuable specialist capability here, but the contractor engagement may end around October or November depending on budget. There is currently no confirmed permanent replacement. The risk is therefore not only losing a person; it is losing a point of ownership for initiative-level E2E testing, cross-platform domain knowledge, and the final confidence check across complex journeys.

The function has two possible future models:

1. Retain or replace a dedicated E2E specialist who owns cross-platform initiative validation.
2. Move E2E responsibility into the QAs and teams that build each initiative, with clear expectations, shared knowledge, and an agreed point in refinement or initiative review for coherent journey testing.

The second model may be more sustainable and closer to ownership, but it changes expectations for teams that currently test their own tickets and rely on LM for the final E2E stage. It will require explicit capacity, test-data support, environment reliability, journey documentation, and leadership oversight. The Lead QA specification makes platform Leads accountable for quality continuity from initiative acceptance through delivery and close; the Staff QA specification adds a potential multiplier role through shared infrastructure, reusable automation, mentoring, and cross-team standards. Any future model should therefore make clear whether E2E is a platform Lead responsibility, a Staff-level cross-platform capability, or a deliberately shared engineering responsibility.

## Challenge

As LM's contractor engagement approaches a possible end, how do I preserve confidence in complex cross-platform initiatives while deciding whether to:

- retain a dedicated E2E testing role
- replace LM with a permanent employee or another specialist
- distribute initiative-level E2E ownership across the delivery QAs
- use a hybrid model with specialist coaching, risk-based oversight, and team-owned execution

The model must protect complicated Portal and Pico/Exerp journeys without allowing E2E testing to become a late-stage quality gate that nobody has capacity or context to own.

## Questions To Explore

### Value And Scope

- What unique value is LM providing beyond the component testing already performed by the delivery QAs?
- Which journeys genuinely require cross-platform manual testing because automation cannot provide equivalent confidence today?
- How much of LM's work is exploratory discovery, how much is repeatable regression, and how much is coordination or test-data setup?
- Which initiatives should receive an E2E ticket, and what risk criteria should trigger one?

### Ownership And Timing

- Should E2E planning happen in refinement and initiative reviews rather than only when a final ticket is created?
- Who owns the end-to-end test approach, data preparation, execution, defect triage, and release recommendation?
- Can the QAs closest to the initiative take responsibility for the final journey checks, with LM or another specialist coaching them during transition?
- How do we prevent a distributed model from becoming "everyone owns it, so nobody owns it"?
- Which parts of initiative-level E2E belong to the platform Lead's quality continuity responsibility, and which require Staff-level cross-platform influence or shared capability?

### Capability And Continuity

- What domain, journey, data, and environment knowledge must be captured from LM before the engagement ends?
- Which QAs need to be paired into the current E2E work so knowledge is distributed rather than documented only after the fact?
- What manual testing skills, automation skills, and cross-platform context would a permanent E2E role need?
- If the specialist role is not retained, what capacity must be added to existing QA plans to make team ownership realistic?
- Could a Staff QA scope be justified by building the reusable data, environment, automation, and journey-testing capability that lets platform QAs own E2E more effectively?

### Environments And Data

- Which E2E failures are product defects, environment failures, test-data problems, or unclear journey expectations?
- What data must exist across Pico and Exerp for the priority Portal journeys to be tested reliably?
- How should staging health and source-data reliability be monitored and reported as part of E2E readiness?
- Would grouped initiative testing reduce duplicated setup and provide better journey confidence than testing every ticket independently?

### Defect Yield And Earlier Detection
- How many defects is LM finding through initiative-level E2E testing, and how severe or customer-impacting are they?
- Which of those defects should reasonably have been found during refinement, component testing, integration testing, or earlier environment validation?
- What patterns do the defects reveal about coverage gaps, unclear ownership, test data, staging, or the timing of E2E testing?
- Does the value of the role come mainly from finding defects, exposing missing scenarios, validating complex data journeys, or preventing release risk?
- Can defect yield and escape analysis show whether a dedicated E2E role is justified, or where the delivery teams need to improve their own earlier testing?
- The CH market go-live post-mortem found that basic issues were reaching the end-to-end stage. How much of this is a coverage gap versus a habit gap where QAs do not verify Exerp or database state?

### Coverage Gaps Identified

- Member communications are largely untested: emails and SMS such as direct debit confirmations, PIN delivery, and GCM messaging. Would temporary/disposable email tooling make these verifiable?
- The front-end automation pack is already acting as the de facto end-to-end safety net, catching Exerp, database, and COP promotion issues unrelated to the code change. Should this role be made deliberate and the coverage expanded?
- Staging promotions are maintained on an out-of-date Confluence page while automation relies on hard-coded promotions. Who owns them, are they still valid, and how are they protected from being overwritten?
- Missing or incomplete requirements remain common, and more acute without a product team. How do we make questioning in refinement a consistent QA behaviour?

### Resourcing And Decision

- Do we have the budget and business need for a permanent E2E tester?
- What is the cost of losing E2E capability, including escaped defects, delayed releases, and lost domain knowledge?
- Is a full-time specialist, a hybrid technical QA role, or distributed ownership the best fit for the volume and complexity of Portal migration work?
- What decision must be made before October/November to avoid a capability gap?

## Initial Position

LM is providing real value through manual, cross-platform testing of complex journeys that span Portal, Pico, Exerp, data, and member scenarios. The role should not be treated as an optional final check or replaced without understanding what confidence it currently creates.

At the same time, the current model concentrates too much initiative-level E2E knowledge and ownership in one contractor. The preferred direction should be evidence-led: document the critical journeys, pair delivery QAs into the work now, identify the irreducible specialist capability, and compare the cost and risk of a permanent E2E role with a properly resourced distributed model.

E2E responsibility should be considered during refinement and initiative reviews, not introduced only after all component tickets are complete. Grouping related work may improve the point at which testing happens, but it must retain clear ownership, representative data, and enough time to act on findings.

The future decision should be informed by evidence of value. Measure the defects, missing scenarios, and release risks LM is finding, then work backwards to understand why they were not found earlier. This should improve the delivery system regardless of whether the eventual answer is a permanent specialist, a hybrid model, or team-owned E2E testing. It should also test whether the capability itself is a legitimate Staff-level opportunity: not simply owning a queue of late E2E tickets, but building the shared utilities, data patterns, automation, and coaching that raise confidence and make other engineers faster.

## Roadmap

| ID | Step | Owner | Depends on | Status |
|----|------|-------|------------|--------|
| CH-07.1 | Run Miro end-to-end domain review with LM | AC | — | next |
| CH-07.2 | Catalogue priority journeys LM covers, AI-assisted | AC | CH-07.1 | later |
| CH-07.3 | Publish E2E results page in Confluence | AC | IMP-06.2 | next |
| CH-07.4 | Pair delivery QAs into upcoming E2E work | AC | CH-07.2 | later |
| CH-07.5 | Define criteria for a dedicated E2E stage | AC | CH-07.2 | later |
| CH-07.6 | Review sample of LM findings for escape causes | AC | — | later |
| CH-07.7 | Recommend E2E resourcing and ownership model before 2027 | AC | CH-07.4, CH-07.6 | later |

## Status & Next Action

**Status:** Open — LM's contract has been extended into 2027 (confirmed 2026-10-15; end date to record), so the resourcing decision is no longer immediate. Knowledge transfer remains valid and should use AI to capture and structure journey knowledge.

_Superseded 2026-10-15:_ LM's possible departure created an immediate decision point.

**Next action:**

1. Build a catalogue of the priority Portal and Pico/Exerp journeys currently covered by LM.
2. Run the Miro-based end-to-end domain review with LM (meeting booked): map what happens functionally at each stage of the system, identify the gaps, then map back to domains, potentially using AI assistance.
3. Pair the relevant delivery QAs into upcoming E2E work and capture the domain, data, environment, and scenario knowledge required.
4. Define criteria for when an initiative needs a dedicated E2E stage or grouped journey test.
5. Review a representative sample of LM's E2E findings: count defects, classify severity and defect type, record where each issue was first found, and identify why earlier checks did not catch it.
6. Compare three options: retain a specialist, replace with a permanent E2E resource, or distribute ownership through a hybrid/team-owned model.
7. Make a resourcing and ownership recommendation in good time before the extended contract ends (2027).
8. Use AI to support knowledge transfer: e.g. turn LM walkthroughs, Miro journey maps, and E2E test notes into structured journey documentation and test scenarios that delivery QAs can reuse.

**Watch for:**

- E2E tickets being created too late for meaningful findings to affect delivery.
- Teams assuming that component-level testing is sufficient for Portal journeys spanning Pico and Exerp.
- Distributed ownership being agreed without capacity, training, data, or environment support.
- LM's contract ending with undocumented journey and domain knowledge.
- E2E defect counts being collected without asking why the defects escaped earlier stages.
- Staging or source-data failures being misclassified as product defects, or vice versa.
- Automation being treated as a complete substitute for the manual exploratory coverage currently providing value.
