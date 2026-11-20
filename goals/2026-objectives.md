# 2026 Objectives

Objectives for the 2026 cycle, as entered in the People system. Part 1 is the Senior QA Engineer objectives, now closed. Part 2 is the QA & Test Engineering Manager objectives. Wording is as entered; names are aliases ([people](../context/people.md)).

Related: [2026 goals](2026.md) · [midyear checkpoint (archived)](../reviews/2026-midyear-checkpoint.md) · [IMP-08 Objectives & reviews](../improvements/08-2026-objectives-calibration-and-eoy-reviews.md)

## Part 1: Senior QA Engineer objectives (closed)

### Objective 1: Load Testing K6

**Status:** Closed (complete) · **Objective lens:** not tagged (set before lenses were in use)

**Title:** Load Testing K6 - Upskill on K6 load testing and review testing of areas for the MX Web team

**Description:**

K6 Load Testing

- Up-skill in K6 Load Testing
- Review Load Tests for PICO

**Comment 1 (midyear):**

I have performed a deep dive on this part of the repo and have a full understanding of how it works. I will do official handovers with DW and AA, who worked on this, so that this becomes a QA led activity. Any gaps can be addressed as future tickets

**Comment 2 (closing statement):**

Worked on tickets relating to new load testing when this was a planned priority for the MXBE team. Confirmed that the tests worked, ran them across staging, approved the amendments as this was a dev led activity. We agreed to move on from this and focus on functional gaps in testing, so marking this objective as complete.

**Evidence links:** [IMP-03 Load testing](../improvements/03-front-end-load-and-performance-testing.md) (legacy; related load testing follow-on, not this K6 work itself). The work was done earlier in the year, so the comments above are the record for the EOY. No achievement logged; the work predates the repo.
### Objective 2: Accessibility testing on the Web Portal

**Status:** Closed (complete) · **Objective lens:** not tagged (set before lenses were in use)

**Title:** Accessibility testing on the Web Portal

**Description:**

Accessibility testing on the Front End for the web portal.

This can include:

- Screen readers
- Contrast checking
- Basic usability testing
- Tabbing order
- Keyboard navigation etc
- POUR (Perceivable, Operable, Understandable and Robust)

**Comment 1 (midyear):**

I have started work on this alongside other sprint work. The plan is to build a tracking sheet of all pages tested and areas of concern. To support myself, I am also using AI to suggest automated ways of doing some of this to support the eyes on checks required on the site.

**Comment 2 (closing statement):**

Marking as done. Completed accessibility reviews as part of the early/initial web portal tickets (ie dashboard/profile and early cancel pages). These were raised to the developer and fixed accordingly. Following the pivot towards sunsetting the microsites, the focus moved away from accessibility and general UX and to deliver 100% of UK portal functionality before the end of the year. As such, accessibility checks were descoped to "should" priority to be reviewed post go live. With the portal likely to move onto Exerp white label, this post go live becomes irrelevant (unless that position changes).

**Evidence links:** none in the repo; the closing comment above is the record (the work predates the repo).
### Objective 3: Use ByteSmith/Agentic AI in Playwright test suite

**Status:** Closed (complete) · **Objective lens:** not tagged (set before lenses were in use)

**Title:** Use ByteSmith/Agentic AI in Playwright test suite

**Description:**

Use ByteSmith/Agentic AI in Playwright test suite

Use AI to flesh out test suite, analyse tests etc on a regular basis

**Comment 1 (midyear):**

I am using an agentic first approach to playwright test addition. Using copilot CLI, and the agentic guardrails implemented by DA, I utilize the agents to build the tests and connect to the members area for XML review using the playwright MCP server. Whenever adding code, I always get AI to check the existing code base to ensure standards are maintained and drive consistency.

Any changes to the agents file required based on the nuance of the members area, I also consider.

We are restricted at the moment on how fast we can move on this by the speed of the portal development. I have begun discussions with GH and DG around member creation as this will become a blocker soon. We have a plan for how we will do this and I will track this work in an AI chapter ticket

**Comment 2 (closing statement):**

All agents files added, pending dynamic member creation to be able to roll this out further for the portal.

**Evidence links:** [IMP-02 Member data](../improvements/02-dynamic-member-creation-and-test-data.md) (the dynamic member creation blocker named in the closing comment); [IMP-16 AI test boilerplate](../improvements/16-agentic-ai-test-boilerplate.md) (later; the agentic approach carried forward).

## Part 2: QA & Test Engineering Manager objectives (open)

_Covers the four months in the Manager role. Three objectives. Descriptions kept light (one intent line, a few bullets); detail goes in the comments and the EOY review._

### Objective 1: Establish and transition into the QA & Test Engineering Manager role

**Status:** Open · **Objective lens(es):** People Developer, Business Operator

**Title:** Establish and transition into the QA & Test Engineering Manager role

**Description:**

Make the move from peer to manager of the QA team.

- Take on line management of the QA team
- Take ownership of the QA approach and direction and show authority in making decisions for the function
- Build and establish a working relationship with GH and DG as a manager, not a peer

**Comments:** to come from AC.

**Linked achievements (agreed with AC 2026-11-17; may be tweaked at EOY prep):**

- Completed initial QA team listening and reset (2026-09-30), [achievements/2026.md](../achievements/2026.md)
- Rebalanced QA Staffing And Platform Assignments (2026-10-08), [achievements/2026.md](../achievements/2026.md)

**Other evidence links (proposed):** [IMP-13 QA chapter reset](../improvements/13-qa-chapter-reset.md); [CH-04 Web QA capacity and accountability](../challenges/04-web-qa-capacity-and-accountability.md).

### Objective 2: Ensure QA supports the business mission to sunset the microsites by year end

**Status:** Open · **Objective lens(es):** Business Operator

**Title:** Ensure QA supports the business mission to sunset the microsites by year end

**Description:**

Ensure QA supports the business mission to sunset the microsites by year end.

- Ensure the right level of QA is delivered for the business journeys moving away from legacy tech: student join, multi-site and ultimate, buddy, bookings and the Portal
- Organise the team and effort so it is efficient and effective and doesn't bottleneck the delivery end date
- Put a plan in place to deliver automation for the critical areas of the cutover

**Comments:** to come from AC.

**Linked achievements (agreed with AC 2026-11-17; may be tweaked at EOY prep):**

- Set initial quality priorities against the Microsite sunset mission (2026-09-30), [achievements/2026.md](../achievements/2026.md)
- Rebalanced QA Staffing And Platform Assignments (2026-10-08), [achievements/2026.md](../achievements/2026.md)
- Built A Tracking Mechanism For The Plan (2026-10-15), [achievements/2026.md](../achievements/2026.md)
- Dug In On Bookings Go-Live Testing (BAU) (2026-11-06), [achievements/2026.md](../achievements/2026.md)

**Other evidence links (proposed):** [IMP-02 Member data](../improvements/02-dynamic-member-creation-and-test-data.md) (Portal member creation that Portal automation depends on); [CH-07 E2E continuity](../challenges/07-end-to-end-quality-ownership-and-continuity.md) (legacy; initiative-level E2E for student join, cancellation, freezes and multi-gym journeys).

**Team delivery to draw on in comments (from AC's calibration notes, aliases only):** DA led front-end QA for the DK and CH rollouts and found the student join pricing issue (WEB-805); MP got CH payments live and protected payments coverage as services moved into Pico; JS was heavily focused on QA for the Pico market launches including CH; KB added automation for the segmented student journey; TMW industrialised the Exerp release process; JFG led the Exerp upgrades and BGW updates needed before microsite testing could start. There is no repo record yet for buddy or multi-site and ultimate delivery, so those need your input.

### Objective 3: Build credibility and trust with key business stakeholders

**Status:** Open · **Objective lens(es):** Business Operator

**Title:** Build credibility and trust with key business stakeholders

**Description:**

Build credibility and trust with the business stakeholders that QA's work supports

- Build working relationships: attend calls and be a point of contact for QA.
- Be proactive: raise risks and changes that affect them early, rather than waiting to be asked

**Comments:** to come from AC.

**Linked achievements (proposed; AC to confirm):**

- Completed initial QA team listening and reset (2026-09-30), [achievements/2026.md](../achievements/2026.md) (also linked to Objective 1; its wording names the early working relationships with Configuration). No other achievements logged yet for the business stakeholder work.

**Stakeholders covered so far (AC, 2026-11-20):** CR (IT Pricing Manager, Configuration) and LK (Finance Manager). CG (Business Development Coordinator) to be added with achievements later. More to come.

**Other evidence links (proposed):** [discovery call with CR, 2026-09-16](../context/discovery-calls/2026-09-16-it-pricing-manager-cr.md) (member-centred pricing and configuration testing, Extractor reliability, communicating changes that need Configuration support, promotions and campaigns walkthrough); [CH-02 Business stakeholders](../challenges/02-direct-business-stakeholder-connection.md) (legacy; mapping stakeholders and decision owners); [CH-08 Exerp Extractor](../challenges/08-exerp-extractor-reconciliation-and-data-integrity.md) (legacy; the reconciliation problem CR raised); [IMP-17 Business visibility](../improvements/17-business-language-quality-visibility.md) (later; quality in business language). Job spec: Business Stakeholder Engagement ([JD-15, JD-17](../context/_taxonomy.md)).

**Note on source:** GL suggested Vivamo as a route to credibility and trust with senior stakeholders. AC has had little involvement with the Vivamo stakeholders, so the objective is deliberately more general. Other names from GL's message are not recorded here.
