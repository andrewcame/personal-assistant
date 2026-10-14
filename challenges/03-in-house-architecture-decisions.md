---
id: CH-03
type: challenge
status: open
horizon: none
updated: 2026-09-04
pillars: [P3, P7]
focus: [ownership]
goals: []
links: []
people: [GH, DG, AV]
---

# Challenge 03 — Making In-House Architecture Decisions Well

---

## Context

A recent organisational reshuffle also removed the architecture function supporting the engineering organisation. Design decisions are now expected to be made more within engineering. The move to Pico makes this more viable because the organisation has stronger in-house context, and the Principal Engineer is acting as the architectural point of accountability.

The broad elements of the architecture are already in place, with Operations and Security providing specialist support. The direction is to collaborate, make sensible decisions, and continue delivering at pace. Issues that cannot be resolved sensibly should be raised to GH, DG, AV, and the director. Topics that would previously have gone to the architecture council should now be brought to the Tech Lead Chapter.

This creates more autonomy, but also makes decision clarity, technical coherence, and lightweight governance more important. The risk is either recreating a slow approval process or allowing important design choices to remain local, implicit, or inconsistent.

## Challenge

As the QA & Test Engineering Manager, how do I contribute to an in-house architecture model that:

- enables engineers to make timely, well-reasoned design decisions
- keeps decisions coherent across Pico and the wider platform
- gives the Principal Engineer and Tech Lead Chapter the right level of visibility
- brings quality, operability, security, testability, and member impact into design conversations early
- provides a clear escalation path without recreating the former architecture council

## Questions To Explore

### Decision Rights And Governance

- Which decisions belong to a squad, a platform, the Principal Engineer, the Tech Lead Chapter, or senior leadership?
- What is the expected route for a technical challenge that cannot be resolved within the team?
- What kinds of decisions need a lightweight written record, and where should those records live?
- How will the Tech Lead Chapter distinguish a decision that needs group input from one that should simply be shared afterwards?

### Technical Quality

- What architectural principles and constraints are already agreed for Pico?
- How do we assess trade-offs across reliability, security, operability, performance, accessibility, testability, cost, and delivery pace?
- How do we identify when a local solution creates a wider platform or support risk?
- How can QA contribute quality and risk signals without turning design discussions into a late approval gate?

### Capability And Collaboration

- Where do engineers need more context, patterns, or coaching to make design decisions confidently?
- How do we make useful architecture knowledge visible across teams rather than relying on the Principal Engineer as the only source?
- Which Operations, Security, or specialist inputs must be involved early for particular classes of decision?
- How do we review whether the new model is improving pace and decision quality over time?

## Initial Position

The organisation should take advantage of the expertise now within engineering and make decisions close to the work. In-house autonomy does not mean unstructured autonomy: the Principal Engineer should provide architectural direction, the Tech Lead Chapter should replace the architecture council as the place for shared technical challenges, and significant decisions should remain visible and explainable.

QA should be involved where design affects testability, observability, resilience, accessibility, release risk, or critical member journeys. The contribution should be practical and early, helping the team see consequences and trade-offs rather than acting as an approval barrier.

Use the smallest governance mechanism that preserves coherence: clear decision ownership, short written records for consequential choices, and escalation when a team cannot sensibly resolve an issue.

## Status & Next Action

**Status:** Open — new in-house architecture model is settling.

**Next action:** Confirm the decision and escalation path with the Principal Engineer and Tech Lead Chapter. Capture the agreed route, decision-recording expectation, and the quality concerns QA should bring into design discussions.

**Watch for:**

- teams making incompatible decisions because shared constraints are unclear
- the Principal Engineer becoming a bottleneck or a single point of failure
- architecture discussions becoming an approval ceremony
- important quality, operational, security, or testability consequences being considered too late
- technical decisions being made without a visible rationale or owner
