# MP

## Snapshot

| Field                  | Detail                        |
|------------------------|-------------------------------|
| Current team/platform  | Payments                      |
| Current role and level | Lead QA (Level 7)             |
| Reports to             | QA & Test Engineering Manager |
| Direct report to me    | Yes                           |
| Last promoted          | Unknown                       |
| Profile last reviewed  | 2026-10-19                    |

## Experience And Specialism

### Current Focus

- Lead QA owning quality and testing across payment subsystems, payment partners, and financial integrations.
- Currently the only QA in the Payments team; workload has eased somewhat as the number of developers has reduced.

### Team History

- Payments domain.

### Strengths And Specialist Knowledge

- Payments processing, integration testing, domain specialist for financial transactions and checkout flows.
- Strong functional testing mindset: challenges assumptions, explores edge cases, and adopts the customer's perspective.
- Comfortable contributing to test automation with AI and suggesting changes without being precious about ownership.

## Current Working Context

- Positive about working at PureGym.
- Enjoys the Payments team and domain.
- Prefers front-end work to back-end work, while continuing to contribute to tests and technical discussions.
- Has limited interaction with Payments stakeholders. Requirements reach MP via the Product Owner, and MP often supplies acceptance criteria.
- Helps bridge the gap between high-level payment needs and low-level technical implementation by asking how a change should be tested.

## Capability And Development

- Interested in the move toward agentic AI and uses AI to write tests and suggest changes.
- Has a current blind spot in the newer Pico ecosystem, particularly the `pico.frontend` package; this is a potential development and support area.
- Does not currently want direct reports. Would accept support if another QA joined Payments in future.
- Relevant objective lens(es): Business Operator / Value Creator / People Developer

## Direction And Sentiment

_Last discussed: 2026-09-03_

- What they enjoy:
- What motivates them:
- What frustrates them:
- Where they want to go:
- Support they want:

## Development

- Current development goals:
- Relevant objective lens(es): People Developer / Value Creator / Business Operator
- Progress and evidence:
- Next development conversation:

## Observations And Feedback

### 2026-08-26 - Profile Initialization

- Type: Direct evidence
- Source: QA Department Roster
- Observation: Established initial profile as Lead QA for Payments domain (Level 7).
- Impact or relevance: Core leadership direct report.
- Follow-up or evidence needed: Conduct initial 1:1 discovery conversation.

### 2026-09-03 - Initial Lead Conversation

- Type: Direct conversation notes
- Source: Initial Payments Lead conversation
- Observation: MP said they are positive about the role, team, domain, and working at PureGym. Morale is currently low within the Payments team, with recent company changes and departures affecting the team, including a key Payments technical lead.
- Impact or relevance: Check in on support needs as the Payments team changes.
- Observation: MP finds the role most rewarding when challenging assumptions, acting as the customer, and identifying edge cases. MP is comfortable using AI to create tests and allowing developers to contribute to automation.
- Impact or relevance: Strong fit with functional quality thinking, AI-enabled testing, and shared quality ownership.
- Observation: Main pain points are the Pico domain, test environments, and legacy Microsite technical debt. MP identified a blind spot in the newer Pico ecosystem, particularly `pico.frontend`.
- Impact or relevance: Targeted domain support and the planned Payments deep dive could improve confidence and reduce isolation.
- Observation: MP is currently the only QA in Payments and does not want direct reports at present. Workload has eased and another QA is not an immediate concern.
- Impact or relevance: Review capacity and resilience over time without assuming an immediate headcount solution.
- Observation: MP has limited interaction with Payments stakeholders and often fills the gap between straightforward business payment needs and highly technical implementation.
- Impact or relevance: There may be a stakeholder visibility and requirements-shaping gap around Payments quality.
- Follow-up or evidence needed: Complete the Payments functional and technical domain review; explore Pico, Exerp events, payment agreements, reconciliation, sandbox coverage, and existing automation.

### 2026-09-07 - Leadership 1:1 context

- Type: Manager observation shared in leadership 1:1
- Source: GL 1:1 with QA & Test Engineering Manager
- Observation: GL described MP as performing strongly in Payments and contributing beyond the immediate group by getting involved in wider Payments work.
- Impact or relevance: This is useful evidence of cross-team ownership and growing business/domain impact; look for concrete examples that can support future progression and review conversations.

## 2026 Objectives

_As held in the performance system, recorded 2026-10-19. The WHAT rating is judged against these. Stable IDs: `MP-O<n>`. Comments below are MP's, as logged in the system (dates not captured)._

| ID     | Objective                                                               | Agreed                   | Status                             |
|--------|-------------------------------------------------------------------------|--------------------------|------------------------------------|
| MP-O1  | Payments automation merge with Pico codebase (UK only)                  | 2026 (date not recorded) | Changed (scope; 50% reported)      |
| MP-O2  | DK payments: robust, relevant E2E QA test coverage                      | 2026 (date not recorded) | Marked complete (agreed with GL)   |
| MP-O3  | CH payments: robust, relevant E2E QA test coverage                      | 2026 (date not recorded) | Update logged (CH live)            |
| MP-O4  | Adapt and extend ByteSmith guidance so AI can generate Playwright tests | 2026 (date not recorded) | Update logged (rewording proposed) |

### MP-O1 — Payments automation merge with Pico codebase, UK only (Mar–Jun 2026)

- Work with the Pico web team to assess and review existing Pico UK payments automation coverage for the large Pico pack and the smaller smoke packs, so robustness is embedded for all brands.
- Aim to extend coverage to boundary testing and edge cases, for example redirects, integration-point coverage, basket changes after the form has loaded, situational/state testing, unhappy paths and rejoiners.
- Gap analysis in Q1; remediation plan and completion by June 2026.
- Note: Pico playground remains the early warning system.
- MP's update: the scope has changed. Merging the payments codebase into Pico is no longer realistic, so that work is delayed until fully off the microsite, when it can be revisited. The focus has shifted to test coverage, because some payments services have moved from the payments repo to the Pico repo and coverage in that area must not be lost.
- MP's update: progress reported at 50%. A Miro board documents the post-payment processing flow. Next steps are to identify where existing coverage exists and how to add anything missing.

### MP-O2 — DK payments (Jan–Jun 2026)

- Ensure robust, relevant E2E QA test coverage for Denmark payments, including Betalingsservice, pro rata, DDAN checking and payment form accessibility.
- MP's update: good test coverage so far, but nothing end-to-end because development had not got that far. The initiative has been deprioritised, so MP cannot progress the objective. Agreed with GL to mark it complete.

### MP-O3 — CH payments (Jan–Jun 2026)

- Ensure robust, relevant E2E QA test coverage for Swiss payments, including thorough TWINT validation, DDAN checking and payment form accessibility.
- MP's update: CH is live and there is good test coverage.

### MP-O4 — ByteSmith AI-generated Playwright tests (Jul–Dec 2026)

- Begin to adopt the QA Chapter's post-ByteSmith strategy, aiming for AI to start generating Playwright automation scripts.
- Work with GH, DA and TMW to adapt it for payments and Playwright.
- Upskilling (Udemy or the ISTQB AI extension).
- Baseline the test pack so improvements can be measured.
- Mentor others within the QA team.
- Target: a minimum 10% increase in AI-generated automation coverage by Q4 2026.
- MP's update: not sure the objective is realistic, and prefers not to set an arbitrary percentage of AI-created tests. MP would prefer it reworded to focus on how AI can help the QA process (writing code, suggesting coverage, analysis, assisting manual QA), noting this is hard to measure. MP also noted limited time to work on it.
- Suggested by GL: record the wins from using AI and its limitations, then use that evidence to shape a more formal strategy later.

## Progression And Review Evidence

- Evidence supporting current-level performance:
- Evidence of next-level behaviours:
- Gaps or areas needing more evidence:
- Promotion discussion status: Not discussed

## Team Movement Considerations

- Relevant interests or constraints: Prefers specialist contribution and currently does not want direct reports.
- Potential opportunities: Support Pico domain knowledge, involve MP in the Payments domain review, and strengthen stakeholder connection.
- Risks or support needed: Check in on team changes and support needs through 1:1s.

### 2026-09-07 - QA Lead Sync Update

- Type: Direct conversation notes
- Source: First QA Lead Sync (TMW, MP; DA apologies)
- Observation: MP raised concern about a change-deduction-date issue implemented by Web 3, where further issues were subsequently found in Payments.
- Impact or relevance: Highlights a cross-team QA visibility gap — a Web-implemented change surfaced downstream Payments risk that QA did not catch earlier. Agreed that initiative reviews should now include QA to catch this kind of cross-team dependency; findings will be fed back to Delivery, and MP or other leads will be invited as appropriate.
- Follow-up or evidence needed: Confirm the initiative review process change lands in practice; track whether it surfaces similar cross-team risks earlier in future.

### 2026-09-11 - Technical Lead Payments Discovery Context

- Type: Stakeholder / Peer engineering feedback
- Source: Technical Lead Engineer Payments discovery conversation
- Observation: TL holds MP in very high regard, highlighting a longstanding working relationship and praising MP's deep attention to detail.
- Impact or relevance: Strong positive peer leadership feedback demonstrating high engineering trust and respect in the Payments domain. Valuable for review evidence and progression under People & Practice.

## Open Follow-Ups

_Keep operational actions in Notion; link or summarize only the context needed here._

- Complete Payments domain review with MP.
- Consider how another QA would be supported if Payments capacity changes.
- Explore a suitable route for MP to build confidence in the newer Pico ecosystem.
