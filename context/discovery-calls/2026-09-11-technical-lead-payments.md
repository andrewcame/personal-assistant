---
id: DC-2026-09-11-technical-lead-payments
type: discovery-call
date: 2026-09-11
pillars: [P3, P4, P5, P6, P8]
focus: [people, ownership, automation, productivity]
links: [CH-03]
people: [DA, MP]
---

# 2026-09-11 - Technical Lead Engineer Payments

## Call Context

- **Date:** 2026-09-11
- **Source / role:** Technical Lead Engineer, Payments
- **Conversation type:** Engineering discovery
- **Related team or platform:** Payments, FE/PE/Payments repos, environments (preview/staging), Exerp
- **Notes based on:** Personal notes / Discovery conversation

## Purpose

- Understand payments team perspective on end-to-end testing, environment parity, preview vs staging pollution, test tooling, and integration with Exerp.

## Key Signals

### What Matters To Them

- High standards of release confidence and stability (comes from the microsite background where 100% pass rate was mandatory for go-live).
- Clear visibility into true quality: a flat 70% pass rate on the FE repo is misleading and unacceptable because the failing 30% could conceal critical journey failures.
- Environment isolation: avoiding preview and staging cross-contamination.
- Reliable Exerp instances configured for both preview/dev and staging.
- High regard for MP (QA Lead Payments) and his attention to detail.

### Current Friction Or Risks

- Adapting from legacy microsites (isolated, high-pass requirements) to the unified Pico architecture (single FE, single PE, single payments repo) without dedicated cross-cutting E2E coverage points.
- Proposal for a dedicated E2E test repo was previously rejected by DA. While failing FE tests due to BE issues is frustrating, it reflects reality in a singular dependent platform.
- **Environment Parity & Pollution:**
  - No parity between preview (dev/QA) and staging (E2E baseline).
  - Staging backend is currently used for front-end previews, risking data and state pollution.
  - Engineers manipulate or point dev work directly to staging to test features, causing long-standing breakage for E2E runs.
  - Exerp has 1 active instance; preview and staging instances exist but are not yet configured/wired.
- Low FE pass rate baseline (~70%) lacks risk nuance: without tying tests to critical user journeys, 70% passing can mask 100% failure on business-critical paths.
- Tech debt scale and QA scope fatigue: TL noted the risk of burnout given the sheer volume of QA debt.

### What Is Working Well

- **Payment Modal Isolation:** Dedicated test pack and sandbox allowing isolated component-level testing on change, complemented by E2E payments tests.
- **Local Ecosystem Tooling (Tilt):** Enables local full-ecosystem development (minus Exerp).
- **Historical Archetypes:** `pico.preview` repo exists as a reference concept for an E2E preview ecosystem.
- **Staging Exerp Member Inspector Tool:** A web page/URL exists to look up member state directly in Exerp, which could be integrated into key FE E2E test verification steps.

### What They Asked For / Suggested

- Re-evaluate the environment model (consider whether returning to full alpha/beta style ecosystems or configuring separate Exerp dev vs staging instances is viable).
- Tie test reporting and gating to critical user journeys rather than raw percentage pass rates.
- Better harness and integrate the niche tools already built (modal sandbox, Exerp lookup tool, Tilt).

## Themes And Interpretation

- Directly stated: The shift to a monolithic/unified repo architecture removed E2E safety nets, leading to tension around test ownership and cross-service failures.
- Directly stated: Staging is polluted by dev previews and uncoordinated testing; Exerp instance separation is available but unconfigured.
- Directly stated: 70% FE pass rate gives false comfort and obscures critical risk.
- My interpretation: We have an abundance of tactical tools (Tilt, modal test packs, Exerp lookup web tools, `pico.preview`), but lack an overarching harness and governance model to connect them to daily QA flow.
- My interpretation: Pass rates must be tiered by criticality (e.g. Tier 1 / Business-Critical Journeys = 100% gate, non-critical = defect triage) rather than treated as a flat aggregate metric.
- My interpretation: Pacing and prioritization are critical — the backlog of QA/environment debt is massive, so picking high-impact battles is essential to avoid burnout and maintain momentum.
- Hypotheses to validate: Exerp preview vs staging instances can be configured to stop dev work from polluting staging.
- Hypotheses to validate: The Exerp member lookup tool can be automated as an assertion step in FE critical journeys to verify backend sync.

## Mapping

### Strategic Mission(s)

- People & Practice
- Technical Mastery & Foundations
- Delivery Flow & Resilience
- Business Risk & Stakeholder Trust

### Role Pillar(s)

- Automation Trust & Reliability
- Test Infrastructure, Environments & Data
- Delivery Confidence & Flow
- Business-Critical Journey Protection
- Quality Ownership & Culture

### Objective Lens(es)

- Value Creator
- Business Operator
- People Developer

### Related 30/60/90 Focus Area(s)

- Ownership
- Automation
- Productivity
- People

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Investigate configuration of Exerp dev/preview vs staging instances** — Owner: AC / Platform — Destination: Notion / Challenge [03-in-house-architecture-decisions.md](../../challenges/03-in-house-architecture-decisions.md) — Notes: Prevent preview tests polluting staging Exerp data.
- **Evaluate Exerp staging lookup web tool for E2E test assertions** — Owner: AC / MP — Destination: Notion / Improvement — Notes: Explore adding member state checks to critical journey tests.
- **Review FE pass rate categorization (critical journeys vs non-critical)** — Owner: AC / DA — Destination: Notion / [08-business-critical-journey-protection](../../context/role-pillars.md) — Notes: Replace flat 70% threshold with journey-based confidence gating.
- **Discuss E2E cross-repo testing approach with DA & MP** — Owner: AC — Destination: Notion / Ways of Working — Notes: Balance isolated repo testing with end-to-end confidence across FE/PE/Payments.

## Possible Outputs

- Candidate challenge update: [challenges/03-in-house-architecture-decisions.md](../../challenges/03-in-house-architecture-decisions.md) or a new environment integrity challenge.
- Candidate improvement: Tiered test reporting & critical journey gating; Exerp test data lookup automation.
- Candidate goal input: Environment parity and staging protection.

## Open Questions

- What is the blocker to configuring the second Exerp instance for preview/dev?
- How can we formalise staging freeze / clean-state rules without blocking dev velocity?
- Can Tilt be extended or documented for QA local exploratory/debugging use?
