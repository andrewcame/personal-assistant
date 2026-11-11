# DA

_Written to the [people-records standard](README.md#writing-standard): dated, observable facts; agreed expectations and support; no interpretation of motives. Ratings, retention, and any formal process live in the official People systems, not here._

## Snapshot

| Field                  | Detail                        |
|------------------------|-------------------------------|
| Current team/platform  | Website                       |
| Current role and level | Lead QA (Level 7)             |
| Reports to             | QA & Test Engineering Manager |
| Direct report to me    | Yes                           |
| Last promoted          | Unknown                       |
| Profile last reviewed  | 2026-11-11                    |

## Experience And Specialism

### Current Focus

- Lead QA owning quality and test automation across Website platforms (Astro-powered web applications, Web Teams 1, 2 and 3).
- Leading the Dynamic Member Creation initiative ([INI-01](../context/jira-initiatives/01-portal-dynamic-member-creation.md)) from 2026-10-08.

### Strengths And Specialist Knowledge

- Web test automation, web performance, and user journeys.
- Subject-matter expert for the front-end test repository; maintains the automation improvement backlog.

### Working Arrangements

- Has an agreed working-pattern arrangement through HR; plan cover and availability around it.

## Direction (in DA's words, 2026-09-14)

- Enjoys: Website quality and technical ownership, with enough autonomy and context to make decisions.
- Wants: progression to Staff QA Engineer; does not want to become a Test Manager.
- Asked for: clear context when work is allocated, clarity on the promotion path, and alignment on Website, Web 3, cross-platform exposure, and test-data strategy.
- Biggest technical concern: test-data strategy (prefers creating and retaining data by default).

## Development

- **Current development goal:** demonstrate Staff-level impact through visible Website ownership (including Web 3), initiative leadership, and enough familiarity with Mobile App and Payments to contribute beyond a single domain.
- **Evidence so far:** Website platform ownership across three Web teams; automation improvement backlog; agreed to lead backend integration testing as an initiative (2026-09-22); leading INI-01 (2026-10-08).
- **Evidence still needed for Staff:** sustained hands-on Website ownership including Web 3; cross-platform contribution; constructive communication when disagreeing; proactive surfacing of risks and blockers; measurable outcomes from automation or test-data work.
- **Support offered:** initiative-shaped work rather than open-ended epics; manager as second reviewer for the automation backlog; coaching on people management (DA line-manages JS); test-data approach to be worked through with the Principal Engineer.
- **Promotion discussion status:** Exploring.

## Agreed Expectations

| Date       | Expectation                                                                                                   | Source                 |
|------------|---------------------------------------------------------------------------------------------------------------|------------------------|
| 2026-09-14 | Become more visible and involved in Web 3; define the evidence needed for Staff                               | 1:1                    |
| 2026-09-22 | First point of contact for Web 2 ticket pickup during cover; attend stand-ups when a ticket is in flight       | 1:1                    |
| 2026-09-22 | Use the manager as a second reviewer for the automation backlog                                                | 1:1                    |
| 2026-09-22 | Take on backend integration testing as an initiative                                                           | 1:1                    |
| 2026-10-08 | Lead the Dynamic Member Creation initiative; provide Web cover when needed with progress visible to Delivery  | 1:1                    |
| 2026-10-08 | When disagreeing or declining a request, do so constructively and propose a workable next step or review point | Feedback given in 1:1  |

The Lead QA specification's flow-discipline clause ("stepping into whatever is needed to keep things moving") applies during agreed cover periods.

## 2026 Objectives

_As held in the performance system, recorded 2026-10-19; comments confirmed with DA and supplied by AC on 2026-11-05. Stable IDs: `DA-O<n>`: O2 is reliability and O3 is AI-generated automation, regardless of the order in the latest update. AC confirmed adding DA-O4 to the performance system on 2026-11-05; final wording below._

| ID      | Objective                                                                           | Agreed                    | Status                           |
|---------|-------------------------------------------------------------------------------------|---------------------------|----------------------------------|
| DA-O1   | Drive high quality delivery of the web experience across key market rollouts        | 2026 (date not recorded)  | Closed as met, 2026-11-05        |
| DA-O2   | Leverage automation to support early defect identification and incident prevention  | 2026 (date not recorded)  | Comment added 2026-11-05         |
| DA-O3   | Adapt/extend ByteSmith so AI can start to generate automation tests                 | 2026 (date not recorded)  | Ongoing; comment 2026-11-05      |
| DA-O4   | Deliver dynamic member creation for reliable Portal automation                      | Added 2026-11-05          | Added; no comment yet            |

### DA-O1 — Web experience delivery across key market rollouts (Jan–Jun 2026)

- Provide QA ownership of the web front-end member experience, including leading the DK/CH rollouts and overseeing UK CoP automation testing.
- Ensure effective development, clear objectives and successful outcomes for the team.
- Comment (confirmed with DA; supplied by AC, 2026-11-05): DA led the DK/CH QA activity, ensuring coverage in the front-end test repository and QA for the go-lives. DK was subsequently descoped as the business pivoted towards sunsetting the microsites. The team had clear objectives to track the work. Objective closed as met.

### DA-O2 — Automation for early defect identification and incident prevention (Mar–Jul 2026)

- Using the AI / ByteSmith approach and next-generation automation techniques, take end-to-end ownership of testing to actively improve Pico system reliability.
- Develop and implement a QA strategy to improve the current approach, for example increasing sharding to 100% for smoke tests in production deploy pipelines, including maturing features such as CoP/rejoiners, and ensuring the large daily automation pack reliably catches problems.
- Communicate confidently and professionally with key cross-functional stakeholders to build trust that testing identifies issues early.
- Comment (confirmed with DA; supplied by AC, 2026-11-05): the pico.frontend pack has:
  - agentic AI skills and agent files to guide setup and standards
  - an appropriate split of staging and production tests, scheduled as needed
  - additional segmentation and pricing edge-case coverage in response to production issues
  - Exerp checks as part of the Join flow
- Evidence gap: these updates do not confirm the 100% smoke-test sharding target or quantify the daily pack's reliability.

### DA-O3 — ByteSmith AI-generated automation (Jan–Nov 2026)

- AI upskilling in Copilot CLI and MCP.
- Baselining so AI improvements can be measured.
- Work with the AI Chapter (especially GH) to broaden Playwright coverage via the QA Chapter.
- Coach, mentor and manage others in the QA team to succeed in this space.
- Target: a minimum 10% increase in AI-generated Playwright coverage for the large pack and smoke test packs by Q4 2026.
- Comment (confirmed with DA; supplied by AC, 2026-11-05): this remains ongoing as the AI landscape changes. Creating, adapting and updating skills and agent files addresses problems encountered; documenting new AI features supports team use and onboarding. DA also onboarded another team member to the pico.frontend pack, including its AI skills and conventions.
- Evidence gap: the baseline and measured change against the 10% AI-generated coverage target have not been supplied.

### DA-O4 — Deliver dynamic member creation for reliable Portal automation

Lead the dynamic member creation initiative so Portal automation can run consistently and support the microsite sunset mission.

- Deliver the agreed Portal member creation scope.
- Enable reliable, consistent creation of Portal members, with clear error handling when member setup fails.
- Document the approach in the repo with appropriate AI skills and agent updates.
- Support the QA team in using it on new tests as required.
- Context: AC confirmed adding this wording to the performance system on 2026-11-05. No timeframe or core-versus-stretch measures supplied. Related: [IMP-02 Member data — Dynamic Member Creation And Automated Test Data Architecture](../improvements/02-dynamic-member-creation-and-test-data.md), pillars P5 and P4. Objective lens: Value Creator / Business Operator.
- Comment: none yet; delivery is still in progress.

## Observations

### 2026-09-03 - Web 3 capacity discussion

- Type: Direct evidence (Teams thread)
- Observation: Asked DA and TMW for short-term mitigation ideas for reduced Web 3 QA capacity. DA advised resetting team velocity and business expectations. His message also included language describing colleagues that was not respectful.
- Follow-up: Expectation on respectful, solution-focused communication covered in later feedback.

### 2026-09-14 - Initial 1:1

- Type: Direct conversation
- Observation: Discussed direction (above), the challenge of managing quality across three Web teams (active QA boards, joining tickets when needed, automation improvement epic), and openness to Mobile App and Payments exposure if it supports Staff scope.
- Follow-up: Staff evidence plan; Web 3 visibility; test-data approach with the Principal Engineer.

### 2026-09-17 - Bookings Portal PR review request

- Type: Direct evidence (Teams thread)
- Observation: Asked DA to review test-code changes in a large external PR by mid the following week. DA correctly identified failed preview deployments and merge conflicts, and declined to review until a successful build existed; the wording was dismissive.
- Follow-up: Discussed 2026-09-22; DA said he could have handled it better.

### 2026-09-17 - Pico backend coverage question

- Type: Direct evidence (meeting)
- Observation: DA correctly identified that a reported gap was backend rather than front end. Whether existing basket tests covered the risk was not yet established.
- Follow-up: DA to coordinate with JFG to classify existing coverage and agree an owner for any gap.

### 2026-09-18 - Web 2 cover

- Type: Direct evidence
- Observation: During Web 2 holiday cover, DA did not attend the Web 2 stand-up, and a ready ticket was reassigned to LM after DA said he was busy; the capacity clash was not escalated to me.
- Follow-up: Cover expectations agreed 2026-09-22 (see table).

### 2026-09-22 - Ways-of-working 1:1

- Type: Direct conversation
- Observation: Positive conversation covering the automation epic, Web 2 cover, and ways of working. DA said he is adjusting to having a technical line manager; welcomed moving from open-ended epics to defined initiatives; agreed to take on backend integration testing; confirmed Web 2 cover is in hand.
- Manager's own action: provide initiative-level work so ownership can be assessed fairly.

### 2026-10-08 - Objectives and communication

- Type: Direct conversation and manager feedback
- Observation: DA assigned to lead INI-01 with Web cover expectations (see table). Some messages since 2026-09-22 have been abrupt; each instance has been addressed directly at the time, naming the impact and the expected approach.
- Follow-up: Review INI-01 progress, cover, and communication at regular 1:1s.

## Year-End Evidence (2026)

_Feeds calibration prep and the end-of-year review. Add dated, linked evidence through the year. Source: **self** (what they tell AC), **manager** (what AC saw) or **line-manager** (see team/README.md)._

### WHAT — impact against objectives

- 2026-10-27 — DA-O1 — manager — Owns Web QA alongside TMW, broadly DA the front end and TMW the backend side. This resolved the Web QA capacity and accountability challenge (closed 2026-10-27) — [CH-04](../challenges/04-web-qa-capacity-and-accountability.md), [achievement](../achievements/2026.md)
- 2026 (date not recorded) — DA-O2 — self — A new segment-pricing check found that production student join pages were showing staging prices, leaving customers stuck mid-join (WEB-805). DA reproduced it on production and traced it to a cache shared between production and staging; it was fixed the next day.
- 2026 (from 2026-10-08) — DA-O4 — self — Leading Dynamic Member Creation (WEB-856). DA showed a fresh test member can be created through the APIs in about 10-15 seconds, against up to a minute through the UI, which allows Portal journeys such as cancellation to be automated without shared test accounts — [IMP-02](../improvements/02-dynamic-member-creation-and-test-data.md)
- 2026 (date not recorded) — DA-O2 — self — Widened and stabilised the test suite: brought CH coverage in line with GB, added Exerp sale verification, added estate-wide price and joining-fee guards, replaced hard-coded gym data with backend lookups, added feature-file linting, fixed CI runner issues, and set up AI tooling for the team (also relevant to DA-O3).

### HOW — behaviours against the values

- 2026 — V-DETAIL — self — Raises issues with clear evidence, the root cause and a suggested fix so they can be acted on quickly (WEB-805 above).
- 2026 — V-SHOULDER — self — Takes review feedback on board and changes approach where it makes sense, for example adding duplicate-payment safeguards after a code review; pushes back with evidence where it does not.
- 2026 — V-DIFF — self — Looks for gaps proactively (flaky test tracking, accessibility, visual regression) and adopts new tools early that help the team.

### Improvement and development areas (from DA, 2026-11-09)

- Follow through on tech debt: prioritise and deliver the most valuable items from the improvement backlog DA has raised.
- Align earlier: agree the approach with the relevant teams before building, to reduce rework.
- Work in smaller increments: story-sized PRs from the start so reviews are quicker and easier.

### Manager's view of development areas

_AC, 2026-11-11. Manager's perspective for calibration prep and the EOY review, read alongside the evidence and the Observations above._

- **Strengths observed:** a very capable, detail-oriented engineer with strong technical understanding. Makes good progress when scope and direction are clear (consistent with the move to initiative-shaped work agreed 2026-09-22 and with INI-01).
- **Line management:** new to line management, with one report (JS). His approach is light-touch so far. AC has little direct view of it yet; this is an area to develop.
- **Development areas (as could be said to DA):**
  - Look beyond test execution to the bigger picture: how the work, and the way you communicate about it, lands with the teams and stakeholders around you. This builds on the communication expectation agreed on 2026-10-08.
  - Be present and contribute on calls, including stand-ups during cover, as agreed on 2026-09-22.
  - Develop your line-management practice with JS: regular, structured support for her progression case.
  - Where scope is not set for you, propose it yourself so the direction is clear. This is part of the evidence needed for Staff.

## Open Follow-Ups

_Operational actions live in Notion._

- 2026-11-09: DA's top 3 WHAT, top 3 HOW and improvement areas received and recorded above. Verify the WEB-805 and WEB-856 details (dates, timings) in Jira before they are used in calibration or the review.
- Agree the Staff QA Engineer evidence plan and review it through QA Lead Sync.
- Review INI-01 progress and Web cover against the agreed expectations.
- Align test-data strategy with the Principal Engineer.
- If concerns persist despite support, follow the company performance process with the People Business Partner (records held there, not here).
