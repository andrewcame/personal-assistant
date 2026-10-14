---
id: DC-2026-09-14-sem-pico-architecture
type: discovery-call
date: 2026-09-14
pillars: [P4, P5, P6]
focus: [ownership, automation]
links: [IMP-01, IMP-02]
people: [DJ]
---

# 2026-09-14 - Software Engineering Manager - Pico Architecture

## Call Context

- **Date:** 2026-09-14
- **Source / role:** Software Engineering Manager, deep hands-on history with the Pico architecture and design
- **Conversation type:** Engineering discovery
- **Related team or platform:** Staging health monitoring, Pico architecture, Supergraph, member creation tool, payments/Exerp integration
- **Notes based on:** Personal notes / discovery conversation. Full transcript to follow separately; architectural deep-dive detail from that transcript will be routed to the my-order-space repo rather than duplicated here.

## Purpose

- Get practical help setting up staging health monitoring (dashboards, dead letter queue process) as part of taking on a first-responder-style role for staging.
- Explore the Pico architecture's challenges/limitations specifically around the member creation tool problem, and sense-check the technical approach with someone deeply experienced in the ecosystem.

## Key Signals

### What Matters To Them

- Reusing existing product Grafana dashboards rather than building new ones — just point them at the right environment.
- Getting the member creation initiative properly aired with the wider engineering community (Backend Chapter), not just decided in isolation.
- Being realistic about what's achievable technically for member creation given the current state of payments integration — favouring a phased/MVP approach over solving everything at once.

### Current Friction Or Risks

- Member creation via Supergraph works for member and subscription data, but not for payments — the current (non-private) Supergraph can't reach payment/Exerp data, so a member created this way would immediately be "in debt" if they tried to log in for real.
- Internal member lookup and sourcing members in known states are viable scope; fresh, fully usable member creation remains blocked by the payment/Exerp integration gap.
- This creates a view, shared with the Lead QA in Web, that differs somewhat from the Principal Engineer's — worth being aware there isn't full technical alignment yet on the right approach.
- Payments isn't yet in a state within Pico where it can be interacted with cleanly via Supergraph, so a full end-to-end member creation (including payments) isn't currently feasible.

### What Is Working Well

- Existing product Grafana dashboards can be reused for staging monitoring simply by switching the environment filter — no need to build new dashboards from scratch.
- Clear, practical guidance already exists for the dead letter queue process, which is a key part of diagnosing staging issues.
- Strong architectural knowledge available from this person as a go-to source for understanding how Pico actually works underneath.

### What They Asked For / Suggested

- Suggested I set up a daily staging-check routine, first-responder style, and gave a concrete method: use GitHub Desktop/Copilot with context of all the environments, copy error messages found during checks, and use that to interpret where/what the problem was.
- Suggested building a local log/database of what I find during these checks, then reporting up to SMEs who can advise on resolution.
- Gave a safe DLQ recovery sequence: inspect and capture the error first; where recovery is agreed, recreate the Kafka DLQ topic because clearing messages was unreliable; then restart the affected consumer pod so it recreates its subscription. Clearing is not routine and needs awareness/escalation.
- Suggested joining the Backend Chapter as a forum to air ideas on the member creation approach.
- Suggested that for the member creation tool, a new Supergraph (or calling Exerp APIs directly) may be needed to properly expose payments-related data — but this is a technical decision for engineers to propose; my role is to own and clearly write the requirements.
- Suggested targeting an MVP using existing (member + subscription) data first, then extending to payments once Pico's payments integration matures enough to support it via Supergraph.

## Themes And Interpretation

- Directly stated: reusing existing Grafana dashboards (just repointed at the right environment) removes what looked like a blocker to starting staging monitoring quickly.
- Directly stated: the technical approach to member creation isn't yet settled — there's a difference in view between this SEM/Principal Engineer and the Lead QA in Web on how to handle the payments gap.
- Directly stated: full member creation (with working payments) isn't achievable today because payments/Exerp data isn't reachable through the current Supergraph.
- My interpretation: the practical next step for staging monitoring is very close to executable — I have a dashboard source, a DLQ process, and a suggested daily workflow (GitHub Desktop/Copilot-assisted) — this could move from discovery into practice quickly.
- My interpretation: member creation should be framed as a phased initiative from the outset (MVP without payments, later phase with payments) rather than a single all-or-nothing ask — this keeps it achievable and avoids the initiative being "overblown" per the DJ conversation.
- My interpretation: my role in the member creation problem is to own and clearly articulate the requirements/problem statement, not to decide the technical solution (new Supergraph vs direct Exerp API calls) — that's for engineering to propose, with Backend Chapter as a sounding board.
- Hypotheses to validate: whether a new Supergraph exposing payments-relevant data, or direct Exerp API calls, ends up being the preferred technical route once engineering weighs in via Backend Chapter.

## Mapping

### Strategic Mission(s)

- Technical Mastery & Foundations
- Delivery Flow & Resilience

### Role Pillar(s)

- Test Infrastructure, Environments & Data
- Automation Trust & Reliability
- Delivery Confidence & Flow

### Objective Lens(es)

- Business Operator
- Value Creator

### Related 30/60/90 Focus Area(s)

- Automation
- Ownership

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Set up daily staging health-check routine using existing Grafana dashboards + DLQ process** — Owner: AC — Destination: Notion / Improvement [01-staging-monitoring-and-alerting-ownership.md](../../improvements/01-staging-monitoring-and-alerting-ownership.md) — Notes: Repoint existing product dashboards at the right environment; use GitHub Desktop/Copilot-assisted workflow to log and interpret errors found.
- **Join the Backend Chapter to air member creation approach ideas** — Owner: AC — Destination: Ways of Working — Notes: Suggested forum for surfacing the Supergraph-vs-direct-Exerp-API question to engineering.
- **Write clear requirements for member creation as a phased initiative (MVP without payments, later phase with payments)** — Owner: AC — Destination: Notion / Improvement [02-dynamic-member-creation-and-test-data.md](../../improvements/02-dynamic-member-creation-and-test-data.md) — Notes: Aligns with DJ conversation on raising this via Intake; keep scope realistic given payments/Supergraph limitation.
- **Route detailed Pico architecture knowledge from the fuller transcript into the my-order-space repo** — Owner: AC — Destination: my-order-space repo (external to this workspace) — Notes: Architectural deep-dive content doesn't belong in this discovery log; keep this file focused on decisions/signals.

## Possible Outputs

- Candidate improvement update: [01-staging-monitoring-and-alerting-ownership.md](../../improvements/01-staging-monitoring-and-alerting-ownership.md) — concrete daily routine and dashboard reuse now unblocked.
- Candidate improvement update: [02-dynamic-member-creation-and-test-data.md](../../improvements/02-dynamic-member-creation-and-test-data.md) — phased MVP approach (no payments) plus requirement-ownership framing.
- Candidate ways-of-working note: Backend Chapter as a forum for technical debate on QA-driven initiatives.

## Open Questions

- Will engineering land on a new Supergraph or direct Exerp API calls as the preferred way to eventually expose payments data for member creation?
- What is the actual timeline/dependency for payments being in a state within Pico where Supergraph access becomes viable?
- How should the differing views between this SEM/Principal Engineer and the Lead QA in Web on the member creation approach be reconciled — is this something to surface in Backend Chapter or resolve directly first?
