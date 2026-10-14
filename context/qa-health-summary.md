# QA Health Summary

This is the aggregated view of QA/Test Engineering health during the initial listening and baseline phase of the 30-day plan.

It is built from individual team conversations, Lead QA profiles, and relevant external discovery notes. It is a synthesis, not a transcript or a replacement for the underlying context.

## Purpose

- Understand the overall health, sentiment, capability, and direction of the QA function.
- Identify themes that are repeated across people or platforms.
- Separate systemic issues from platform-specific problems.
- Establish an evidence-based baseline before setting formal goals or making major changes.
- Provide a bridge from listening into priorities, challenges, decisions, and future objectives.

## Status

| Field                  | Detail                                                              |
|------------------------|---------------------------------------------------------------------|
| Baseline period        | September 2026                                                      |
| Last updated           | 2026-09-18                                                          |
| Conversations completed| 8                                                                   |
| Conversations planned  | QA leads, wider QA team, relevant engineering and stakeholder calls |
| Confidence in findings | Early / Emerging / Established                                      |

## Executive Summary

Early conversations indicate a generally capable and engaged QA function, with the clearest shared risks around environments, test data, staging breadth, and cross-platform ownership. KB's Website conversation adds evidence that isolated component testing can miss customer-impacting failures and that the Pico model requires stronger end-to-end thinking than the older siloed microsite approach.

### Overall Health

- Early signal: MP is positive about PureGym, the Payments domain, and the role. Payments team has seen recent changes and departures.
- Early signal: TMW said she feels more valued and the team culture has improved. TMW raised tech debt and context switching.
- Early signal: KB is positive about cross-stack testing and AI-assisted investigation, but environment and test-data friction makes reliable end-to-end testing difficult in Website.
- Early signal: JS enjoys web, coding, and user-experience work. JS raised communication and progression clarity.
- Early signal: DA's stated priority: clarity on Staff QA progression.
- Early signal: JFG has strong backend expertise and wants Senior QA progression. Progression evidence being agreed.
- Early signal: LM is highly valued and enjoys the work, but the contractor engagement may end around October or November. E2E knowledge transfer, staging visibility, test-data reliability, and the future shape of E2E capacity are now continuity concerns.

### Strongest Signals

- MP values customer-focused functional testing, edge-case thinking, AI-assisted automation, and a collaborative relationship with developers.
- Payments has strong domain knowledge, but some of it is concentrated in MP and other key individuals.
- TMW is energised by non-ticket work, automation improvements, system understanding, and quality work that has clear value beyond BAU execution.
- KB demonstrates useful cross-stack capability across front end, back end, Exerp Adapter, GraphQL, Kafka, and AI-assisted testing tools.

### Biggest Risks

- Further changes or departures in Payments could affect team support and resilience.
- Pico domain knowledge, test environments, legacy Microsite debt, and limited Payments stakeholder interaction are current friction points.
- Sustainable capacity is the key risk in Apps: tech debt, context switching, Exerp constraints, and single-QA coverage.
- Website quality confidence may be constrained by thin staging coverage, difficult environment and test-data connections, and reliance on isolated component testing or limited E2E capacity.
- Website delivery is also experiencing uncertainty around product-team support, technical-lead responsibilities, and the balance between component delivery and explicit end-to-end ownership.
- Website leadership has a clear progression and accountability tension: DA wants Staff QA progression; Staff evidence plan being defined.
- Cross-platform E2E capacity has a succession risk because LM's contract may end before a replacement or redistribution model is agreed.
- Web 3 capability needs a more precise framing: the mission is focused on the Portal, so DA's development need is primarily Portal and member-journey familiarity. Payments and Mobile may provide useful adjacent learning because some of their features overlap with Portal journeys; this needs validation through cross-platform deep dives.

### Most Likely Easy Wins

- Complete the planned Payments functional and technical domain review.
- Help MP build confidence in the newer Pico ecosystem and connect Payments quality concerns more directly to stakeholders.
- Give TMW more defined space for automation and non-BAU improvement work, and review whether a second QA in Apps would reduce context switching.
- Validate a development/staging ecosystem and preview model that enables safer cross-service testing without destabilising shared staging.

## Team Sentiment And Experience

### Motivation And Enjoyment

- MP is positive about the role and domain.
- TMW raised tech debt and context switching.
- JS raised communication and progression clarity.
- Interested in Staff QA progression (DA).
- Interested in Senior QA progression (JFG).
- **Evidence:** MP, TMW, JS, DA, JFG profiles. **Confidence:** Early.

### Role Clarity

- Not yet captured. **Confidence:** Early / Emerging / Established.

### Ways Of Working

- TMW values kanban, less sprint pressure, and more time to understand the bigger picture; she still wants stronger communication and shared ownership across teams.
- JS's team is experimenting with component delivery and later end-to-end sweeper tickets, but technical-lead ownership is still settling.
- **Evidence:** TMW, JS profiles. **Confidence:** Early.

### Developer Relationships

- TMW feels more valued with developers than before, but some relationships remain uneven and team communication remains a challenge.
- JS said decision routes have been unclear since the product changes.
- **Evidence:** TMW, JS profiles. **Confidence:** Early.

### Workload And Effectiveness

- Workload has eased, partly because fewer developers are creating demand.
- TMW still experiences high context switching and limited capacity due to app-wide responsibilities.
- KB experiences environment and test-data friction that makes backend and end-to-end testing slower.
- JFG finds Exerp/BGW release work time-consuming and is developing into front-end work.
- **Evidence:** MP, TMW, KB, JFG profiles. **Confidence:** Early.

### Development And Progression

- TMW said she wants quality improvement work and broader exposure; she moved to Web Team Two on 2026-10-08.
- JS feels ready to progress and wants a supportive Lead QA route rather than QA management.
- DA is focused on Staff QA progression and needs clearer evidence expectations.
- JFG wants Senior QA progression and needs evidence beyond technical capability.
- **Evidence:** TMW, JS, DA, JFG profiles. **Confidence:** Early.

### Manager Support Needed

- TMW wants clearer team communication, more collaborative ways of working, and sustained support to improve Appium and reduce technical debt pressure.
- JS needs clearer communication routes, progression support, and a review of QA code-owner expectations.
- DA needs context-rich communication, Staff progression clarity, and alignment on Web 3 ownership and test-data strategy.
- JFG needs coordinated support across the reporting crossover, front-end development, and Exerp documentation.
- **Evidence:** TMW, JS, DA, JFG profiles. **Confidence:** Early.

## Common Themes

### What Is Working Well

-

### Friction And Frustrations

- Current Payments-specific friction includes Pico domain knowledge, test environments, and legacy Microsite technical debt.
- Website-specific friction includes connecting previews and staging across services, thin staging coverage, and difficulty testing backend changes through meaningful end-to-end journeys.
- Ticket QA notes are sometimes too abstract to support shared ownership; they need concrete steps and expected outcomes so anyone picking up the work can test it. DevQA adoption is also uneven, making shared QA a capacity and culture question rather than a simple resourcing solution. **Evidence:** 2026-09-18 Joint Funnel technical lead discovery. **Confidence:** Early.

### Desires And Direction

- MP prefers specialist functional testing, customer-focused challenge, front-end work, and practical AI-assisted automation; direct reports are not currently desired.

### Capability And Succession

- Payments quality knowledge is concentrated in a small number of people. MP is currently the sole QA in the domain, making resilience and future support worth monitoring even though another QA is not an immediate requirement.
- Website cross-stack and E2E knowledge also needs resilience planning: the function should not assume that a dedicated E2E tester will always be available, and specialist knowledge around CEP and GCM 2 may need refreshing.
- Structural career headroom bottlenecks exist across the department: Lead QAs (Level 7) face a steep leap to Staff (Level 8) with limited clear scope; Senior II (Level 6) lacks an open Lead vacancy; and the department lacks Junior/Graduate (Levels 1–2) roles to seed a continuous talent pipeline.
- Stagnation among longstanding engineers is creating pent-up demand for promotion, requiring transparent competency-based expectation setting and alternative growth pathways.
- JS's conversation adds a concrete example: a capable practitioner feels ready to progress but does not want line management, reinforcing the need for a supportive technical Lead QA route.
- DA's conversation adds the corresponding Level 7 to Level 8 pressure: a Lead wants Staff progression and believes he is close, but the evidence must include visible domain leadership and cross-functional impact.
- JFG's conversation adds a practitioner-level progression signal: strong technical ability is present; agreed evidence includes communication, meeting contribution, and ownership beyond a backend specialism.

### Knowledge Sharing And Documentation

- The planned Payments domain review should document functional journeys, business-critical coverage, technical flows, repositories, and existing automation.
- Portal knowledge should be developed as a cross-platform capability, using relevant overlap with Payments and Mobile to support DA's Web 3 onboarding and strengthen end-to-end member-journey understanding.
- Web teams need clearer ownership for component-to-E2E validation, technical-lead responsibilities, and decisions following the product-team changes.
- Test-data strategy needs an explicit engineering decision: whether to create and retain data by default or create it on demand, with the trade-off between repeatability, maintenance, and speed made visible.
- Exerp release and BGW update knowledge should be documented so the process does not depend on JFG or TMW learning it informally.
- LM's E2E domain knowledge and journey detail should be documented before the contractor engagement ends, with a clear decision on replacement, redistribution, or role continuation.
- Member communications (emails, SMS, PIN delivery, direct debit confirmations, GCM messaging) are not routinely verified end to end; the domain review should establish what is sent at each stage and what is covered.
- Staging promotions are maintained informally on an out-of-date Confluence page while automation depends on hard-coded promotions; ownership, accuracy, and protection from overwrites need to be agreed.
- Ticket-level test notes should be written as usable testing guidance, with concrete steps and expected outcomes rather than only high-level intent. **Evidence:** 2026-09-18 Joint Funnel technical lead discovery. **Confidence:** Early.

## Quality Health Baseline

### Automation Trust And Reliability

- **Current signal:** AI-assisted local tooling is useful, but the value and ownership of wider E2E coverage need validating. The front-end pack has become the de facto end-to-end safety net, catching issues originating in Exerp, databases, and COP promotions that cannot be traced to the triggering code change.
- **Impact:** Local tools can help investigate tickets; dedicated E2E capability should have succession cover. Unexplained failures are often genuine system signals rather than test noise.
- **Evidence:** KB, LM profiles. **Next validation:** Identify reusable tools and critical E2E journeys; decide whether to formalise and expand the front-end pack's end-to-end role.

### Test Coverage And Ownership

- **Current signal:** Isolated testing can miss customer-impacting failures; Pico delivery needs stronger journey-level ownership. Not all QAs verify Exerp or database state when testing, and member communications (email, SMS, PIN, direct debit, GCM) are largely unverified.
- **Impact:** Student journey testing exposed products disappearing from the website. The CH market go-live post-mortem found basic issues surfacing only at the end-to-end stage.
- **Evidence:** KB, LM profiles. **Next validation:** Compare with other Website and engineering evidence; establish Exerp/database verification as normal QA practice.

### Environments And Previews

- **Current signal:** Backend preview to staging front-end connections are complex and can affect other teams.
- **Impact:** Makes backend and cross-service end-to-end testing difficult.
- **Evidence:** KB profile. **Next validation:** Validate a separated dev/staging ecosystem and preview model.

### Test Data

- **Current signal:** Connecting the right data across environments is a recurring hindrance, and source-data reliability is tightly coupled to environment stability for E2E testing.
- **Impact:** Slows investigation, reduces confidence in realistic journeys, and makes cross-platform test results harder to trust.
- **Evidence:** KB, LM profiles. **Next validation:** Agree a data strategy for priority journeys.

### Staging Health And Alerting

- **Current signal:** Staging appears thin for the variety and integration paths in Pico; concerns recur across E2E work and need a visible cross-team quality signal. Unreliability makes it hard to tell a genuine defect from an environment problem.
- **Impact:** Broadening coverage was necessary to find issues in the student journey. Poor visibility also makes it harder to distinguish environment failure from product failure and make release decisions. Bolt-on and joining-fee issues have appeared in both staging and live.
- **Evidence:** KB, LM profiles. **Next validation:** Define monitoring, reporting, and ownership for staging health.

### Delivery Flow And Handoffs

- **Current signal:** The older siloed microsite model conflicts with Pico's end-to-end expectations.
- **Impact:** Cross-team handoffs can leave risks undiscovered between component checks.
- **Evidence:** KB profile. **Next validation:** Define ownership for cross-service quality risks.

### NFR, Performance, And Resilience

- Not yet captured.

### Business-Critical Journeys

- Not yet captured.

## Platform Differences

### Mobile App

- Team culture has improved (TMW, 2026-09-04).
- The most tangible risk in Apps is sustainability: a high-tech-debt environment, context switching, Exerp bottlenecks, and single-QA coverage leave less time for customer-perspective testing.
- A second QA in Apps would support delivery capacity and reduce context switching.

### Website

- Website spans Web 1, Web 2, and Web 3, but QA capacity and reporting lines are not aligned cleanly with that platform structure. The reduction in Web 3 QA capacity is creating a delivery and Exerp release risk that needs both an immediate cover plan and a structural ownership review.
- DA's reported difficulty managing three Web teams reinforces the need for active QA boards, visible prioritisation, and explicit Web 3 ownership.
- JFG's crossover reporting arrangement reinforces the need to separate people management from domain support: TMW owns the line relationship while DA supports Website and front-end capability.
- JS's team is considering faster component delivery with explicit end-to-end sweeper tickets; validate who owns the sweeper and whether it is sufficient for member journeys.
- KB's conversation adds a Website-wide quality signal: preview, test-data, and staging constraints make it difficult to test backend changes end to end. The student journey exposed the risk of thin staging variety and isolated component testing, while Pico's one-repo model creates an expectation of joining up the customer journey.
- Follow-up practitioner conversation reinforces that the gap is not just tooling: KB is using AI and lightweight test tooling effectively, but the underlying environment model and the split between siloed microsite testing and end-to-end Pico thinking still shape whether QA can find the important issues early.

### Payments

- Positive engagement with the Payments domain; recent organisational changes create a resilience risk. MP currently bridges business payment needs and highly technical implementation, with limited direct stakeholder interaction.

### Cross-Platform E2E

- KB described a tension between older siloed microsite testing and Pico's end-to-end expectations. Dedicated E2E capacity currently exists, but succession and distributed ownership should be considered so cross-service confidence does not depend on one person.
- LM's contract end date makes that succession risk immediate: E2E knowledge, documentation, and role ownership need to be secured before October/November if the engagement ends then.
- The CH market go-live post-mortem suggests the gap is partly behavioural: QAs need to verify Exerp and database state as a normal part of testing, not treat end-to-end validation as someone else's stage.

## External Context

Use this section for themes raised by engineering, platform, SRE, product, delivery, or business stakeholders that affect the QA team's health or ability to deliver.

- [Staff Engineer DevEx discovery](discovery-calls/2026-09-01-staff-engineer-devex.md)
- [Principal Engineer SRE / Pico discovery](discovery-calls/2026-09-01-principal-engineer-sre-pico.md)
- [Technical Lead, Joint Funnel / Corporate Membership Types discovery](discovery-calls/2026-09-18-technical-lead-joint-funnel.md)

## Mission And Pillar Mapping

### Strategic Mission(s)

- People & Practice
- Technical Mastery & Foundations
- Delivery Flow & Resilience
- Business Risk & Stakeholder Trust

### Role Pillar(s)

- People Capability, Progression & Succession
- Test Infrastructure, Environments & Data
- Business-Critical Journey Protection
- Knowledge Sharing & Quality Practice
- Quality Ownership & Culture
- AI-Enabled Testing & Innovation

### Objective Lens(es)

- People Developer
- Value Creator
- Business Operator

## Emerging Priorities

These are hypotheses until supported by enough conversations and evidence.

1. Establish a Payments functional and technical domain baseline through the planned deep dive.
2. Understand Payments team resilience to further team changes.
3. Identify the support and knowledge-sharing needed around Pico, environments, and stakeholder confidence.
4. Validate whether a separate development/staging ecosystem and improved preview model would reduce cross-team testing friction.
5. Review App QA capacity, including whether a second QA in Apps would improve sustainability.
6. Define the Portal journeys and shared feature boundaries that can support DA's Web 3 familiarisation, involving MP and TMW where their Payments and Mobile work overlaps.
7. Clarify Web technical-lead responsibilities, communication routes, and QA participation in pull-request review without creating unnecessary QA distraction.
8. Define and review DA's Staff QA evidence plan, including Web 3 ownership, cross-platform contribution, and test-data strategy.
9. Review JFG's Senior QA progression evidence and document the Exerp/BGW release process.
10. Secure LM's E2E knowledge and decide the future replacement or redistribution model before the contractor engagement ends.
11. Decide the future ownership model for initiative-level E2E testing across complex Portal and Pico/Exerp journeys before LM's contract possibly ends in October/November.

## Decisions And Challenges To Consider

- [Challenge 04 — Web QA Capacity, Reporting Lines, And Accountability](../challenges/04-web-qa-capacity-and-accountability.md)
- [Challenge 05 — QA Growth Headroom, Stagnation, And Talent Pipeline](../challenges/05-qa-growth-headroom-and-talent-pipeline.md)
- [Challenge 07 — End-to-End Quality Ownership And Continuity](../challenges/07-end-to-end-quality-ownership-and-continuity.md)
- Candidate decision:
- Candidate goal input:
- Candidate achievement evidence:

## Source Conversations

| Date       | Person / source | Platform or scope   | Profile / note                |
|------------|-----------------|---------------------|-------------------------------|
| 2026-09-03 | MP              | Payments            | [MP profile](../team/mp.md)   |
| 2026-09-04 | TMW             | Mobile App          | [TMW profile](../team/tmw.md) |
| 2026-09-07 | KB              | Website             | [KB profile](../team/kb.md)   |
| 2026-09-08 | KB              | Website             | [KB profile](../team/kb.md)   |
| 2026-09-14 | JS              | Website             | [JS profile](../team/js.md)   |
| 2026-09-14 | DA              | Website             | [DA profile](../team/da.md)   |
| 2026-09-14 | JFG             | Website             | [JFG profile](../team/jfg.md) |
| 2026-09-14 | LM              | All Platforms / E2E | [LM profile](../team/lm.md)   |

## Review Notes

- Revisit after all initial Lead QA conversations.
- Revisit after wider QA health checks and team deep dives.
- Compare findings with the 30-day plan outputs before formalising goals.
- Do not turn an isolated comment into a department-wide conclusion without validation.
