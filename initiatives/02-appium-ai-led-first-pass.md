---
id: INI-02
type: initiative
status: in-progress
horizon: now
updated: 2026-10-15
pillars: [P4, P9]
focus: [automation]
goals: []
links: [CH-01, CH-09, INI-01]
people: [GH, KB]
---

**Initiative Name:** Expanding Automated Coverage Of High-Value, High-Risk Mobile App Journeys

**Exec Sponsor:**

**Business Lead:**

**Stakeholders:**

**Value:** Moves the Mobile App from testing a small percentage of live functionality to automated coverage of the areas members actually use most, using an AI-led approach so QA can flesh out the Appium repo without waiting for dedicated developer capacity.

**Problem Statement**

We have a live app in production, but only a small percentage of its functionality is currently covered by automated tests. An Appium framework has already been built, but it has only been rolled out to a small number of tests. Progress has been constrained by issues within the app (e.g. defects, the PKCE implementation, view-hierarchy issues, automation ids etc), as well as competing team priorities.

This leaves us heavily reliant on manual regression, which does not provide a scalable or repeatable way to keep pace with delivery. The risk created by this lack of automated coverage has recently been exposed by several member-facing production issues and needs to be addressed.

The introduction of AI-first engineering practices gives us an opportunity to accelerate this work. Rather than raising granular tickets for every piece of coverage, agents can work using the flows already created (adding more as needed). Issues can be addressed as they arise, while anything the agents cannot resolve being flagged for resolution.

Not addressing this test coverage gap keeps the app under-tested relative to its real-world usage and risk, and keeps the Appium rollout stalled at its current small footprint.

**User Story**

- As a QA engineer building out Mobile App automation
- I want an AI-led process that generates and extends Appium coverage for our highest-usage, highest-risk areas
- So that the app gains reliable automated coverage that passes consistently in the pipeline

**Objective**

Run a first pass of AI-led Appium test creation to extend coverage beyond its current small footprint, prioritising the areas members use most and the areas that carry the most risk.

This will be QA-led, with developer support brought in as needed to unblock app-side issues.

We'll use Firebase data to identify the areas of the app most commonly used by members, then combine this evidence with a risk assessment to prioritise the first journeys to automate. We will also give agents context of the previous Xamarin UI tests to understand historical coverage and patterns, supplemented by current member-journey data.

Success looks like: a larger, more valuable set of Appium tests covering these priority areas and passing reliably in the pipelines.

Some increase in pipeline and overall execution time is an acceptable trade-off for greater coverage and confidence. Tests should still be designed to avoid unnecessary waits or excessively long journeys, while broader performance optimisation can follow as a future improvement.

**Project Scope**

- Use Firebase usage data and a risk-versus-value assessment to prioritise the first journeys and features to automate
- Assess the existing AI flows in the repo, expanding or adjusting them where needed to support effective automation
- Use AI agents to generate tests and extend the COM, POM, and JOM framework elements as needed, ensuring the tests run reliably both locally and in BrowserStack
- Address issues pragmatically as they arise, maintaining momentum and asking for support when needed.
- Get all tests passing reliably in the pipelines as the primary success measure for this first pass
- Review and extend the pipeline definitions where needed to unblock efficient execution, without treating full optimisation as part of this initiative
- Document the coverage remaining after this first pass, prioritise what should come next, and use it to define a separate follow-on initiative

### Portal migration web journeys

Prioritise the Mobile App's web journeys in the first batch of Appium coverage, especially journeys moving from legacy Microsites to the Pico Portal. These journeys exercise important member-state behaviour, including intermittent access, and give the app an early regression signal as the Portal rolls out.

The current delivery proposal is front-end first: temporarily route selected Portal queries through a Business Gateway to legacy backend adapters so the Portal front end and automation can progress before the backend is replaced and its tests are updated. The Mobile App's web journeys can move to the new Portal in parallel with this work.

Treat failures caused by changed Portal identifiers or locators (including the RDS locator) as a migration signal. Update the Appium tests to use the new identifiers and restore passing coverage before expanding the app rollout. This work depends on dynamic member creation being available for the app's tests; the implementation and adoption path from [Initiative 01 — Dynamic Member Creation & Lookup For Portal Automation](01-portal-dynamic-member-creation.md) needs to be confirmed.

**Out of scope**

- Exhaustive coverage of all app functionality — this is a first high-value, high-risk pass, not full regression parity.
- High-volume testing across varied devices, member states, and usage patterns — this can follow in a future initiative.
- Raising and managing every piece of work as a granular ticket — this initiative deliberately uses the AI-led approach

**Open items to flag before this can be finalized**

- Confirm which AI skills/openspec flows already exist and are ready to use for COM/POM/JOM generation, and what gaps still need to be authored first
- Confirm Firebase access/reporting is in place to produce the usage-frequency view needed to prioritise areas
- Agree what "passing reliably in the pipeline" means in practice (e.g. flake tolerance, retry policy) so success is measurable
- Confirm what level of developer support capacity can be relied on to unblock app-side issues during this initiative
- Confirm the app-side path for using dynamic member creation from Initiative 01 in the first web-journey tests

**Supporting Context**
## Progress Update - 2026-10-08

- The Appium initiative is moving forward under the QA & Test Engineering Manager. Appium strategy now led by AC, with space to progress the agreed Appium approach.
- Initial work is focused on making the local developer experience work across macOS and Windows, including Visual Studio and Rider, rather than depending on one developer's setup. This is important for wider QA contribution and future handover to KB.
- AI skills and supporting flows are being made more reusable for other QAs. Once the foundations are ready, the next step is to extend the automated tests; KB is a prospective future owner as he builds app-domain knowledge.
- Review existing repository changes against the originally agreed standards and revert deviations that are no longer needed. This is planned cleanup, not recorded as complete.

## Learning Input - 2026-10-09

- The [Dootrix AI harness call](../context/discovery-calls/2026-10-09-dootrix-ai-harness.md) reinforced the current work on reusable AI skills and cross-platform local setup. AC described already moving repeated emulator/setup work into scripts that skills invoke.
- The useful learning is the combination of reusable engineering standards, project context, activity-based skills, cross-model review and deterministic scripts. QA expertise can shape those activities rather than being expressed only as a generic QA persona or a late review step.
- **Future action:** Implement a similar approach for Appium, as confirmed by AC after the call. For now the focus is understanding Dootrix's practices; no detailed implementation plan or timing is set. The discovery note holds the learning, not an additional task list or a commitment to purchase Dootrix's harness.

**Supporting Context**

- [Challenge 01 — Mobile Automation Strategy (Appium vs Maestro)](../challenges/01-mobile-automation-strategy.md)
- [Challenge 09 — Population-Scale Mobile App Testing And Low-Incidence Defects](../challenges/09-population-scale-mobile-app-testing.md)
- [2026-09-15 Head of Software Engineering (GH) discovery call](../context/discovery-calls/2026-09-15-head-of-software-engineering-gh.md) — Appium AI experiment origin
- [2026-09-16 Technical Lead Mobile / RSR discovery call](../context/discovery-calls/2026-09-16-technical-lead-mobile-rsr.md) — layered testing model, shared ownership, AI experiment evaluation
- [context/my-role/60-day-plan.md](../context/my-role/60-day-plan.md) — agentic AI test creation standards, Appium as first POC

## Progress Update - 2026-10-15

- Appium local-setup documentation updated so the framework runs on both Mac and Windows, and tested (closed in Notion To Do).
