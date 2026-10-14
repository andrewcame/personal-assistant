# LM

## Snapshot

| Field                  | Detail                        |
|------------------------|-------------------------------|
| Current team/platform  | All Platforms (End-to-End)    |
| Current role and level | E2E Contractor (N/A)          |
| Reports to             | QA & Test Engineering Manager |
| Direct report to me    | Yes                           |
| Last promoted          | N/A                           |
| Profile last reviewed  | 2026-09-17                    |

## Experience And Specialism

### Current Focus

- End-to-end integration and system-wide testing across all platforms and user journeys.

### Team History

- Cross-platform e2e contractor engagement.

### Strengths And Specialist Knowledge

- End-to-end user journey validation, cross-platform integration testing, contract testing.

## Engagement Context & Feedback

### Contract / Role Focus

- Focus on critical e2e paths spanning Web, Mobile App, and Payments.
- Formal performance reviews do not apply, but key observations regarding deliverables, contract extensions, and technical contributions are tracked here.
- Daily catch-ups are primarily functional and delivery-focused rather than formal pastoral or engagement conversations.
- The current engagement may end around October or November, so continuity and knowledge transfer need to be planned before the end date is confirmed.

## Observations And Feedback

### 2026-08-26 - Profile Initialization

- Type: Direct evidence
- Source: QA Department Roster
- Observation: Established contractor profile for cross-platform E2E testing. Reports directly to QA & Test Engineering Manager.
- Impact or relevance: Core contributor for cross-system integration confidence.
- Follow-up or evidence needed: Review ongoing e2e coverage priorities and contract scope.

### 2026-09-14 - E2E Contractor Conversation

_Updated 2026-09-17 following a fuller, more detailed follow-up conversation._

- Type: Direct conversation notes
- Source: E2E catch-up and detailed follow-up discussion
- Observation: LM is highly valued and enjoys working at PureGym, but the contractor arrangement means the engagement will eventually end, potentially around October or November. She agrees in principle that her domain knowledge and documentation should be strengthened before she leaves or the work is handed over.
- Impact or relevance: E2E capability and domain knowledge carry a clear continuity risk. The team needs to extract essential detail from the engagement and decide whether the role should be replaced, retained, or redistributed within available budget.
- Observation: LM supports grouping related tickets where possible rather than testing every ticket in isolation. Refinement and initiative reviews should help identify the best point to test a feature or journey as a coherent unit.
- Impact or relevance: Grouped testing may improve end-to-end efficiency and reduce duplicated setup, provided the model retains clear risk ownership and does not defer important feedback too late.
- Observation: Staging remains a significant concern. The issue has been raised repeatedly, and work is underway with others to improve monitoring and cross-team reporting so that staging health becomes a visible quality signal.
- Impact or relevance: Staging stability is a shared delivery dependency, not only an E2E testing inconvenience. A visible signal could support better release decisions and prioritisation.
- Observation: Test data and the reliability of source data are closely tied to environment stability. LM's concerns reinforce the need for a coherent data strategy for reliable end-to-end testing.
- Impact or relevance: Environment and data reliability should be treated together when designing cross-platform test coverage and quality reporting.
- Observation: LM enjoys manual testing and is interested in developing more automation capability, although the available opportunity within PureGym is uncertain.
- Impact or relevance: Any future E2E role design should make the balance between exploratory/manual journey testing, automation, and cross-platform investigation explicit rather than assuming the same contractor model can simply be repeated.
- Observation: Staging unreliability makes it hard to tell whether a failure is a genuine product defect or an environment problem. Bolt-on and joining-fee issues are examples where the same symptoms have also been seen in live, making it difficult to connect the dots.
- Impact or relevance: Without alerting and regular monitoring, time is lost re-investigating ambiguous failures and real defects risk being dismissed as environment noise. Reinforces the need to take staging alerting and monitoring seriously.
- Observation: The front-end automation pack catches far more than front-end code changes. Because staging is a connected end-to-end ecosystem, the tests regularly surface issues originating in Exerp, databases, or COP promotions that cannot be traced back to the triggering code change.
- Impact or relevance: The front-end pack has effectively become the de facto end-to-end safety net. That role should be made deliberate: expand coverage to cover genuine end-to-end paths, and treat unexplained failures as system signals rather than test noise.
- Observation: In the CH market go-live post-mortem, LM found that a number of basic issues were missed by QA testing and surfaced only at the end-to-end stage. A contributing factor is that not all QAs check Exerp or the databases when testing.
- Impact or relevance: This is a ways-of-working gap, not only a coverage gap. QAs need to test the whole journey and underlying system state rather than only the code change in front of them. CH join is live, with remaining features being moved off the microsites onto Pico.
- Observation: Member communications are largely untested end to end. Emails and SMS such as direct debit confirmations, PIN delivery, and GCM communications are not routinely verified.
- Impact or relevance: A real member-facing gap. Temporary/disposable email tooling could make inbound messages verifiable, and the domain review should establish what is sent at each journey stage and what is actually covered.
- Observation: Promotions on staging are poorly managed. A Confluence page is maintained informally but is out of date, while automation tests depend on hard-coded promotions.
- Impact or relevance: Creates silent fragility in the automation pack. Needs a deep-dive review to confirm which promotions are still valid, whether coverage should be expanded, and how they are maintained and protected from being overwritten.
- Observation: Missing or incomplete requirements remain a recurring problem, now more acute without a product team.
- Impact or relevance: QA needs to actively question and clarify in refinement and initiative discussions rather than assuming requirements are complete.
- Follow-up or evidence needed: Capture LM's essential domain and journey knowledge; map the continuity risk and replacement options; agree how grouped testing should work in refinement and initiative reviews; define the staging/data signals needed by QA and Delivery; and run the Miro-based end-to-end domain review.

## Open Follow-Ups

_Keep operational actions in Notion; link or summarize only the context needed here._

- Create a focused E2E knowledge-transfer and documentation plan with LM.
- Assess whether an E2E tester role should continue and whether budget exists for it.
- Define staging and test-data health signals with the relevant engineering teams.
- Run the Miro-based end-to-end domain review: map what happens functionally at each stage of the system, identify coverage gaps, then map back to domains (potentially with AI assistance).
- Deep-dive the staging promotions setup: validate the existing Confluence list, review hard-coded promotions used by automation, and agree ownership and protection from overwrites.
- Establish expectations that QAs verify Exerp and database state, not only the front-end code change.
- Explore temporary/disposable email tooling to bring member emails and SMS into end-to-end coverage.
