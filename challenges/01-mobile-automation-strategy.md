---
id: CH-01
type: challenge
status: open
horizon: now
updated: 2026-10-15
pillars: [P4, P9]
focus: [automation]
goals: []
links: [CH-09, INI-02]
people: [GH, TMW, RW]
---

# Challenge 01 — Mobile Automation Strategy (Appium vs Maestro)

---

## Context

The organisation has an established Appium automation framework for the mobile application (.NET MAUI, iOS and Android). It was built collaboratively between myself (then QA Lead) and a Lead Developer (RW) using engineering principles including Component Object Model (COM), Page Object Model (POM), and Journey Object Model (JOM). The framework was intentionally designed as a shared engineering asset — not QA-owned — and was a long-standing goal for the apps team well before I joined.

The current QA Lead inherited the framework and has a web automation background; they reported friction with MAUI overlays and element hierarchy (view hierarchy issues and intercepted interactions, which are gradually improving).

More recently, Maestro-based automation work has started as a possible alternative to Appium, outside an agreed evaluation.

**Key personal context:**
- I co-built the Appium framework — I have skin in the game and need to be deliberate about neutrality
- The Appium investment aligns with the 60-day plan goal to "establish and settle" automation rather than restart it
- Maestro work started outside an agreed evaluation. Agree how framework changes are proposed and reviewed.

---

## Challenge

As the incoming QA & Test Engineering Manager, how do I:

- Evaluate this fairly without defaulting to defending my own prior work
- Determine whether this is a genuine technical opportunity, a support or skills need, an ownership-model question, or a combination
- Protect the organisation from unnecessary framework churn
- Agree a shared-ownership working agreement.

---

## Questions to Explore

### Business Value
- What problem are we actually trying to solve — speed, maintainability, reliability, onboarding, or something else?
- Which approach best supports the organisation over the next 3–5 years?
- Is a complementary model (Appium for complex journeys, Maestro for smoke/release validation) worth considering?

### Technical
- Where does Appium currently succeed and where does it struggle?
- Which limitations belong to the framework versus the MAUI application itself?
- What does Maestro provide that Appium cannot at the current coverage level?
- What flexibility or investment would be lost by moving away from Appium?
- What is the realistic migration cost in effort, CI/CD integration, and training?

### Capability & Support
- Has the QA Lead had structured support to develop native mobile automation skills?
- What support would help?
- Would pairing with RW or a structured development plan address the issues without a framework change?

### Ownership & Ways of Working
- Agree a shared-ownership working agreement.
- How do I reinforce that automation frameworks are shared engineering assets, not QA property?

### Evidence
- What does a fair, evidence-based comparison look like?
- Which journey to use — ideally the most problematic one, not an easy one
- What success criteria need to be defined *before* the comparison runs, not after

---

## Initial Position

Avoid becoming an advocate for either framework. The decision I co-built Appium does not make it correct. Reported friction with Appium does not by itself make Maestro the answer.

The goal is a mobile automation capability that is:
- trusted, maintainable, and scalable
- easy to contribute to across QA and engineering
- aligned with the wider engineering strategy
- owned by the organisation, not by an individual or discipline

If Maestro work continues outside agreed scope, agree that framework changes go through refinement and review, regardless of the technical outcome.

The 60-day plan commits to establishing and settling automation — not restarting it. Any evaluation needs to be time-boxed, structured, and decided with input from engineering, not by QA alone.

---

## Status & Next Action

**Status:** Open — direction set (Appium remains the default; see 2026-09-16 update and Current Direction below). Delivery now runs through [Initiative 02 — Appium AI-led first pass](../initiatives/02-appium-ai-led-first-pass.md).

**Next action:** Work through the Updated Next Actions in the 2026-09-16 update below; track delivery in Initiative 02 and keep this file for the strategic question (layering, capacity, device farm).

_Original next action (pre-start, superseded 2026-09-16):_ In the first 30 days, have a 1:1 with the QA Lead focused on pain points — not tools. Do not raise Maestro vs Appium directly until the picture is clearer.

**Watch for:**
- Whether the QA Lead raises the topic themselves, and the technical reasons given

---

## 2026-10-15 Update

- Owner: AC.
- In discovery, pending decisions on simplifying the app. A kick-off on this is booked for the week of 2026-10-19.
- The Appium strategy questions below stay open until the simplification direction is known.

## 2026-09-16 Evidence Update — Mobile Technical Lead / RSR Lead

The mobile discussion widened this challenge beyond Appium versus Maestro. The immediate risk is a combination of slow Mobile App delivery, limited automation, insufficient Apps QA capacity, and unclear test-layer ownership.

- Mobile delivery is described as very slow because of the codebase, legacy processes, long build/deploy cycles, and migration from Exerp-direct endpoints to Pico-backed endpoints. The migration is exposing issues and recent P1s.
- TMW is currently the only Apps QA and cannot realistically cover manual regression, historical automation gaps, and new-feature automation at the same time.
- The preferred target flow is to test a feature, add automation that protects it, and rely on that automation at release rather than repeat the full manual exercise.
- A layered model should be evaluated: unit/spec tests, a developer-contributed mocked integration layer using mapped endpoints, and thinner Appium coverage on real devices and real integrations.
- Appium changes should enter normal refinement and developer review like other code changes. This reinforces that the framework is a shared engineering asset rather than an individual QA-owned system.
- The AI-assisted Appium experiment with GH is useful evidence, but should be judged on maintainability, coverage, and fit with the existing architecture rather than novelty alone.
- QA/SRE chapter participation currently appears low-value. Staging monitoring is a practical first route into stronger operational involvement before redesigning chapter expectations.
- Additional Apps QA support should be assessed as strategic capacity, not only extra manual execution. The intended benefit is to free TMW to act more fully as a Lead QA: shape the App testing strategy, reproduce realistic member behaviour, understand how defects escape to production, and build the automation capability she has said she wants to develop.
- BrowserStack/device-farm reliability is part of the automation confidence problem. Remote devices can contribute to failures, so the team should compare BrowserStack with other managed providers and a controlled local device estate before assuming the current farm is the right long-term option.
- The current direction is to continue with Appium as the default platform. Maestro should not become the de facto platform unless a strong, evidence-based reason emerges; the cost and duplication of adopting another platform need to be justified.
- Offer TMW ownership of test design within Appium, the intermediate testing layer, and realistic member-behaviour scenarios, while retaining shared engineering standards and developer contribution.

### Updated Questions To Explore

- Which Mobile App feature and endpoint set is the best first proof of concept for mocked intermediate testing?
- Which tests belong in unit/spec, mocked integration, and Appium real-device layers?
- What capacity would allow TMW to build automation and strategy without leaving manual coverage exposed?
- Can the AI experiment generate tests that fit the existing Appium architecture and pass normal developer review?
- What outcomes and contributions should QA/SRE chapters be expected to produce?
- What strategic outcomes should become visible if TMW is freed from a meaningful share of manual execution?
- How often are BrowserStack/device failures contributing to automation noise, and what would a controlled local device estate need to cover?

### Updated Next Actions

1. Add the layered testing model to the Appium/automation evaluation.
2. Select a representative feature for a mocked integration testing proof of concept.
3. Continue the AI-assisted Appium test-generation experiment and assess the output against the existing architecture.
4. Build an evidence-based case for additional Apps QA capacity.
5. Define meaningful QA/SRE chapter outcomes with GH.
6. Build a resourcing case around strategic Lead QA capacity, not only manual test throughput.
7. Baseline BrowserStack/device-farm failure causes and compare managed and local-device options.

### Current Direction

- Continue with Appium as the default mobile automation platform.
- Do not adopt Maestro as the de facto platform without a compelling, evidence-based case.
- Offer clear ownership through supported Appium contribution, strategic test design, and a layered testing model.

## Related

- [Challenge 09 — Population-Scale Mobile App Testing And Low-Incidence Defects](09-population-scale-mobile-app-testing.md) — extends the strategic concern beyond automation mechanics into execution volume, representative usage patterns, data and state variation, and detection of defects affecting a small proportion of members.
