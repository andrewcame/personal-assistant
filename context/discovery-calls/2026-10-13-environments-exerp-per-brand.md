---
id: DC-2026-10-13-environments-exerp-per-brand
type: discovery-call
date: 2026-10-13
pillars: [P5, P4, P8]
focus: [automation, productivity, ownership]
links: [CH-10, CH-08, IMP-02, IMP-01, INI-01]
people: []
---

# 2026-10-13 - Environments Discussion: One Exerp Test Environment Per Brand

## Call Context

- **Date:** 2026-10-13
- **Source / role:** Engineering environments discussion (attendees to confirm)
- **Conversation type:** Engineering discovery / design discussion
- **Related team or platform:** Pico preview and staging environments, Exerp test, pico.deployment, Payments, Kafka on AKS
- **Notes based on:** Personal notes and two Miro board screenshots of the proposal

## Purpose

- Revisit the environment challenges and agree what to fix. Follow-up to the earlier environment and test-data discussions behind [Challenge 10](../../challenges/10-pico-source-of-truth-and-exerp-dependent-test-strategy.md).

## Key Signals

### Proposed Direction

- **One Exerp environment per "test" brand**, matching the model used with the microsites. Previews would stop pointing at PG DEV TEST and use **PureGym Test**, the same Exerp as staging.
- Exerp test then only needs configuring **once per brand**, and the approach scales as brands are added.
- **Exerp Event Broadcaster** (new service): receives a single Exerp event and fans it out to every subscribed Exerp adapter — staging BE, staging Payments BE, and each preview BE / preview Payments BE.
- **pico.deployment** revisited as the industrial way to stand up a full ecosystem (FE, Supergraph, BE) per ticket. This addresses the FE/BE preview problem. Shown as a Pico Deployments UI backed by a database that feeds the broadcaster, and driving Git repos, App Config, and Key Vault.
- **Payments** is the sticking point: hooking Payments components into this model is not yet solved.

### Statement Of Work (from the board)

1. Make sure the repo can deploy and configure everything (creating branches if needed).
2. Build the broadcaster ("dumb") — staging only.
3. Use step 1 to create a preview.
   - 3a. Add the preview to the broadcaster.
4. Measure the impact on step 3.

Principles noted: **single surface**; **opt-in to events** (open question).

### Known Blockers (from the board)

- Payments access to Pico Kafka requires Payments to be in the same namespace (or possibly just the same cluster) on AKS.
- Payments → Kafka connection generally.
- Align preview databases with staging — on a branch initially for testing, not main.
- CORS configuration for Git / Azure from the deployments UI.

### Target Topology (from the diagram)

- Exerp (PureGym-Test) ↔ IDS (Beta).
- Exerp → Broadcaster → Staging BE, Preview BE (and Payments BEs).
- Staging FE → Staging Supergraph → Staging BE; Preview FE → Preview Supergraph → Preview BE.
- Staging and Preview Payments FE → Payments BE, which talks to Exerp.

## Themes And Interpretation

- **Directly stated:** single Exerp test per brand; broadcaster fan-out; pico.deployment for full-stack previews; Payments integration unresolved; a staged SOW with impact measurement at the end.
- **My interpretation (QA):**
  - This resolves much of the "which Exerp does a preview talk to" drift and the per-environment Exerp configuration effort raised in earlier discovery calls.
  - **Shared Exerp means shared data.** Previews and staging would read and write the same member records. Static shared test data becomes riskier, so dynamic member creation and disposal ([Improvement 02](../../improvements/02-dynamic-member-creation-and-test-data.md), [Initiative 01](../../initiatives/01-portal-dynamic-member-creation.md)) becomes more important, not less.
  - **Fan-out means every environment sees every event.** Tests and adapters need to tolerate events that belong to another preview, which is presumably what "opt-in to events" is about. Worth defining before step 3a.
  - **Step 4 is where QA can lead.** "Measure the impact" needs agreed measures: preview spin-up time, preview test pass rate and flakiness, environment-caused failures, and Exerp configuration effort.
  - Until Payments is connected, Payments journeys keep a gap in preview coverage; this should be explicit in release-readiness conversations.
- **Hypotheses to validate:**
  - A single Exerp test per brand is cheaper and more reliable overall than per-environment Exerp instances, even with broadcaster complexity.
  - Event filtering or opt-in can stop cross-preview interference without each test needing its own Exerp data.

## Mapping

### Strategic Mission(s)

- Technical Mastery & Foundations
- Business Risk & Stakeholder Trust

### Role Pillar(s)

- Test Infrastructure, Environments & Data
- Automation Trust & Reliability
- Business-Critical Journey Protection

### Objective Lens(es)

- Business Operator
- Value Creator

### Related Focus Area(s) (People / Ownership / Automation / Productivity)

- Automation
- Productivity
- Ownership

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Offer QA input on step 4 measures** — Owner: AC — Destination: Challenge 10 — Notes: propose the impact measures before the first preview is built so there is a baseline.
- **Raise shared-data and event-isolation risks** — Owner: AC — Destination: Challenge 10 / Improvement 02 — Notes: test data uniqueness and event opt-in.

## Possible Outputs

- Candidate decision: one Exerp test environment per brand (once confirmed).
- Candidate goal input: environment reliability measures feeding the QA flow metrics ([Improvement 04](../../improvements/04-jira-qa-flow-metrics-baseline.md)).
- Candidate achievement evidence: QA-defined impact measures adopted for the environment change.

## Open Questions

- Who attended, and who owns the broadcaster and pico.deployment work?
- Is "one Exerp per test brand" a decision or still a direction?
- How will Payments join Kafka — same namespace, same cluster, or another route?
- What does "opt-in 2 events" mean in practice: preview subscribes to a subset, or tests filter?
- What happens to PG DEV TEST once previews move off it?
