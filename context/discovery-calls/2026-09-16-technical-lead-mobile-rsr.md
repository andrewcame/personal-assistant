---
id: DC-2026-09-16-technical-lead-mobile-rsr
type: discovery-call
date: 2026-09-16
pillars: [P1, P3, P4, P5, P6, P7]
focus: [people, ownership, automation, productivity]
links: [CH-01, IMP-01]
people: [GH, TMW]
---

# 2026-09-16 - Technical Lead Engineer Mobile / RSR Lead

## Call Context

- **Date:** 2026-09-16
- **Source / role:** Technical Lead Engineer, Mobile App; also RSR lead; previously worked in Payments
- **Conversation type:** Engineering discovery
- **Related team or platform:** Mobile App, Appium, .NET MAUI, mocked/spec testing, legacy endpoint migration, Pico, Exerp, SRE, QA chapter
- **Notes based on:** Personal notes / discovery conversation

## Purpose

- Understand the Mobile App team's delivery and quality constraints through someone with Payments testing experience, explore the Appium strategy and possible intermediate testing layers, and understand how QA could engage more meaningfully with SRE.

## Key Signals

### What Matters To Them

- Improving the pace of Mobile App delivery, which is currently described as "glacial" because of the codebase, legacy processes, long build/deploy cycles, and endpoint migration.
- Replacing repeated manual verification with fast, trusted feedback that lets engineers make changes and verify assumptions safely.
- Preserving the strong testing discipline from Payments while adapting it to the realities of Mobile App delivery.
- Freeing TMW from constant manual execution so she can operate more fully as a Lead QA: shaping the App testing strategy, understanding how issues reach production, and designing tests that reproduce realistic member behaviour.
- Treating Appium changes as shared engineering work: refined with developers, reviewed normally, and contributed to as code rather than controlled by one person.
- Creating a meaningful role for QA and SRE chapters, with practical value rather than silent status meetings.

### Current Friction Or Risks

- Mobile App currently lacks a sufficiently effective automation framework and relies heavily on manual testing. This makes even small changes slow to verify and limits the team's ability to respond quickly.
- TMW is the only App QA and has insufficient capacity to manually test existing coverage gaps while also creating new automation for new features.
- The app is being migrated away from legacy endpoints that call Exerp directly toward Pico-backed endpoints; the migration is uncovering a high volume of issues and recent P1s, creating significant executive noise and delivery pressure.
- Payments has a mature, robust testing method because of its business-critical edge cases, but that discipline has not transferred cleanly into the App team. Payments' UI may look simple while the underlying business logic is complex.
- TL view: Appium friction includes framework familiarity; pairing proposed.
- QA/SRE chapter value is unclear; define expected outcomes.
- BrowserStack/device-farm reliability is an additional risk: the remote devices themselves can contribute to automation failures, making it difficult to distinguish product, framework, and device-estate problems.

### What Is Working Well

- The Mobile App team wants to do a good job despite the legacy burden and delivery friction.
- There is a credible target flow for testing: test the feature, add automation that protects it, then rely on that automation at release rather than repeating the full manual exercise every time.
- The App team has an opportunity to introduce an intermediate testing layer between unit/spec tests and Appium on real devices, using mocked integration points and endpoint mappings to provide faster feature/UI feedback.
- Developers could contribute to this intermediate layer, making it a shared engineering capability rather than a QA-only suite.
- Starting with QA-owned staging monitoring may be a practical first route into stronger SRE engagement before broader chapter participation is redesigned.

### What They Asked For / Suggested

- Explore a testing layer between unit/spec tests and Appium: test the app in isolation through mocked scenarios and mapped endpoints, then keep real-device/real-integration Appium coverage thinner and risk-focused.
- Treat Appium test changes like any other code: bring them into normal refinement, discuss them with developers, and incorporate feedback through the standard approach.
- Consider additional Apps QA support. The likely short-term value is to give TMW capacity to step back from constant manual execution and focus on automation, strategy, and higher-value quality engineering.
- Treat the resourcing case as a quality-strategy investment, not only extra execution capacity: free TMW to work on realistic behaviour, production escape prevention, and the Lead QA responsibilities she is motivated by.
- Support TMW's desire to build and shape automation, but address that need through a supported Appium ownership model and better test-layer opportunities rather than adopting a second platform by default.
- Continue the Appium AI experiment with GH, but judge it against whether it can generate maintainable, useful tests within the existing engineering approach.
- Agreed that Maestro should not become the de facto mobile automation platform. Unless a strong, evidence-based reason emerges, the team should continue with Appium because adopting Maestro would bring cost and platform-duplication overhead.
- Review whether BrowserStack is the right device-farm partner. Longer term, compare it with a controlled local device setup connected in an office or other managed location; this was exploratory and not an immediate change.
- Make SRE/QA chapter participation meaningful, and use staging monitoring as the practical first step toward stronger operational involvement.

## Testing Model Discussed

- **Unit/spec tests:** Fast developer-level feedback for isolated logic.
- **Intermediate mocked integration layer:** App-level feature and UI confidence through mapped endpoints and controlled scenarios, without requiring every check to run against live systems.
- **Appium on real devices:** Thinner, higher-value coverage against real devices and real integration points, focused on journeys and risks that cannot be represented adequately in mocked tests.

This layered model could improve build and release speed while preserving confidence: fast feedback earlier, targeted real-device coverage later, and less dependence on repeating broad manual testing.

## Themes And Interpretation

- Directly stated: Mobile App delivery is currently very slow because of codebase, legacy process, build/deploy, and migration constraints.
- Directly stated: the lack of effective automation leaves TMW with too much manual testing and no realistic capacity to close historical gaps while covering new features.
- Directly stated: the App team's preferred future is feature testing plus automation added at the same time, with release confidence coming from the automation rather than a full repeat manual pass.
- Directly stated: an intermediate mocked testing layer could sit between unit/spec testing and Appium on real devices, with developer contribution.
- Directly stated: Appium changes should go through normal refinement and developer discussion like other code changes.
- Directly stated: unless a compelling reason emerges, Appium remains the agreed default strategy; Maestro is not being adopted as the de facto platform because of the cost and duplication involved.
- Directly stated: QA and SRE chapter participation is currently not delivering enough visible value; staging monitoring may be a better practical entry point.
- My interpretation: the mobile automation problem is broader than Appium versus Maestro. It includes missing test-layer architecture, insufficient App QA capacity, slow feedback loops, legacy migration risk, and shared ownership.
- My interpretation: a second Apps QA is not only a capacity request. It could create the space for TMW to move from manual execution toward automation leadership and more analytical quality work, which matches her stated interests.
- My interpretation: the strongest resourcing argument is not simply faster ticket throughput. Additional Apps support would create protected capacity for TMW to act as a Lead QA: developing the test strategy, modelling realistic member behaviour, and understanding why defects escape to production.
- Next step: offer TMW ownership of test design within Appium, the intermediate testing layer, and realistic member-behaviour scenarios, while retaining shared engineering standards.
- My interpretation: the intermediate testing layer may be the highest-leverage technical idea from this conversation because it could reduce Appium's burden without discarding real-device coverage.
- My interpretation: device-farm reliability deserves to be treated as part of automation trust. A local device estate could improve control, but it would introduce maintenance, connectivity, security, device lifecycle, and geographic coverage responsibilities that need comparing with BrowserStack or another provider.
- My interpretation: the Appium AI experiment should be evaluated as part of the wider strategy, not as proof that AI can replace framework design or developer collaboration.
- Hypotheses to validate: endpoint-mapped mocked scenarios can provide useful App feature/UI confidence without reproducing the full live integration stack.
- Hypotheses to validate: a layered testing model would reduce build/release time and manual regression effort without increasing escaped mobile defects.
- Hypotheses to validate: reducing TMW's manual execution load would allow measurable improvement in strategic App testing, production-escape analysis, and automation ownership.
- Hypotheses to validate: BrowserStack is contributing materially to failure noise, and a different managed or local device strategy would improve signal quality enough to justify the additional ownership.

## Mapping

### Strategic Mission(s)

- Technical Mastery & Foundations
- Delivery Flow & Resilience
- People & Practice
- Business Risk & Stakeholder Trust

### Role Pillar(s)

- Automation Trust & Reliability
- Test Infrastructure, Environments & Data
- Delivery Confidence & Flow
- Quality Ownership & Culture
- People Capability, Progression & Succession
- Non-Functional Quality & Resilience

### Objective Lens(es)

- Business Operator
- Value Creator
- People Developer

### Related 30/60/90 Focus Area(s)

- Automation
- Ownership
- Productivity
- People

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Add the layered Mobile App testing model to the Appium strategy evaluation** — Owner: AC / Mobile Engineering — Destination: Challenge [01-mobile-automation-strategy.md](../../challenges/01-mobile-automation-strategy.md) — Notes: Evaluate unit/spec, mocked intermediate integration, and real-device Appium coverage as complementary layers.
- **Test whether mocked endpoint scenarios can support a first intermediate layer** — Owner: AC / Mobile Engineering — Destination: Notion / Improvement — Notes: Start with a representative feature and measure feedback speed, maintainability, and confidence.
- **Continue the AI-assisted Appium test-generation experiment** — Owner: AC / GH / Apps team — Destination: Challenge [01-mobile-automation-strategy.md](../../challenges/01-mobile-automation-strategy.md) — Notes: Assess generated tests for maintainability, useful coverage, and fit with normal refinement/review.
- **Help TMW succeed with the Appium strategy** — Owner: AC / Mobile Engineering — Destination: Challenge [01-mobile-automation-strategy.md](../../challenges/01-mobile-automation-strategy.md) — Notes: Create meaningful ownership through strategic test design, realistic member-behaviour scenarios, and the intermediate testing layer rather than switching platforms by default.
- **Build the evidence for additional Apps QA support** — Owner: AC — Destination: Notion / Resourcing — Notes: Quantify manual regression demand, automation backlog, P1/migration pressure, and the capacity needed to give TMW strategic headroom.
- **Define the strategic capacity case for additional Apps QA support** — Owner: AC — Destination: Notion / Resourcing — Notes: Show how support would free TMW for Lead QA work: realistic member-behaviour testing, production-escape analysis, and App testing strategy.
- **Assess BrowserStack/device-farm reliability and alternatives** — Owner: AC / Mobile Engineering — Destination: Challenge [01-mobile-automation-strategy.md](../../challenges/01-mobile-automation-strategy.md) — Notes: Compare BrowserStack with another managed provider and a controlled local device estate; include device reliability, maintenance, security, connectivity, and coverage.
- **Raise the value and participation of QA/SRE chapters with GH** — Owner: AC / GH — Destination: Ways of Working — Notes: Define expected outcomes and contribution rather than adding more silent status meetings.
- **Use staging monitoring as the first practical SRE engagement route** — Owner: AC — Destination: Improvement [01-staging-monitoring-and-alerting-ownership.md](../../improvements/01-staging-monitoring-and-alerting-ownership.md) — Notes: Build operational understanding before expanding chapter involvement.

## Possible Outputs

- Candidate challenge update: [01-mobile-automation-strategy.md](../../challenges/01-mobile-automation-strategy.md) — expand from framework choice to layered testing architecture, capacity, and shared ownership.
- Candidate decision: Continue with Appium as the default platform; do not make Maestro the de facto platform unless a compelling evidence-based case emerges.
- Candidate improvement: Proof of concept for an intermediate mocked integration testing layer in Mobile App.
- Candidate goal input: Mobile automation capability and delivery feedback speed.
- Candidate resourcing evidence: Case for additional Apps QA capacity.
- Candidate improvement: BrowserStack/device-farm evaluation, including the option of a controlled local device estate.
- Candidate ways-of-working update: Meaningful QA/SRE chapter outcomes and contribution expectations.

## Open Questions

- Which Mobile App feature and endpoint set would make the best first proof of concept for mocked intermediate testing?
- Which tests belong in unit/spec, mocked integration, and Appium real-device layers?
- What does the current Appium suite already cover, and what historical gap creates the most delivery risk?
- Can the AI experiment generate tests that fit the existing Appium architecture and pass normal developer review?
- What capacity would allow TMW to build automation and strategy without leaving manual coverage exposed?
- What strategic outcomes should become visible if TMW is freed from a meaningful share of manual execution?
- How often are BrowserStack/device failures contributing to automation noise, and which device/OS coverage would a local estate need to provide?
- What should QA and SRE chapter members be expected to contribute or leave each session with?
