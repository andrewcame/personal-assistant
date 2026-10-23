---
id: CH-04
type: challenge
status: active-monitoring
horizon: later
updated: 2026-10-23
pillars: [P1, P6]
focus: [people]
goals: []
links: []
people: [GL, TMW, DA, KB, JS, JFG, LM]
---

# Challenge 04 — Web QA Capacity, Reporting Lines, And Accountability

---

## Context

There are three QA Leads across the function:

- Mobile App: one QA Lead aligned to one squad
- Payments: one QA Lead aligned to one squad
- Website: one QA Lead supporting three teams, Web 1, Web 2, and Web 3

Before promotion into the QA & Test Engineering Manager role, I was embedded in Web 3 and had not fully recognised that I was also providing a semi-lead layer of support there. Since moving out of Web 3, the function has lost QA capacity in a high-velocity team. Delivery has already flagged a risk that work will back up, particularly with the Exerp release approaching.

In a recent leadership session (2026-09-11), the CTO set an ambitious target to fully migrate off the legacy account/bookings microsites by the end of the year (accelerating the current forecast of end of March 2027). To meet this pace, engineering is proposing creative delivery models: grouping backend changes first and enabling pages once complete, and shifting QA from testing every incremental micro-deploy to testing when full features/batches are ready. This requires strong automated regression and explicit leadership risk acceptance.

Concurrently, a potential returning QA contractor/resource may become available. A key strategic question is where to place this resource. Placement options: Web (adds capacity to DA's teams) or Apps (adds capacity alongside TMW and could accelerate the Appium automation initiative, with Web ticket testing covered within the Website team). This must be weighed against upcoming platform risks like Portal.

The remaining Web 3 QA reports to the Mobile App Lead. The Website Lead therefore primarily supports Web 1 and Web 2, where their direct reports are, even though they are accountable for Website as a platform. Web 3 and Mobile App also have meaningful overlap: both predominantly cover the web portal and member login areas. This may create an opportunity for the Mobile App Lead to provide more active support to Web 3 while the reporting model is reviewed.

The immediate response from the cross-team conversation was to reset expectations around reduced throughput and rely more heavily on developer involvement. That is necessary context, but it does not fully answer the leadership question: how do we use the available QA capability, reporting lines, technical overlap, and engineering support to reduce risk while being honest about capacity?

JS's initial conversation adds a related operating concern: product-team support has reduced, technical leads have taken on more initiative and team leadership without a fully clear remit, and JS said decision routes have been unclear since the product changes. She also finds QA pull-request code-owner responsibilities distracting and believes one developer reviewer plus one reliable code owner is sufficient. The role of KB in QA PR review should be explored because of his backend and cross-stack experience.

JFG's conversation adds a people-and-domain crossover: he reports to TMW while working in Website, with DA providing front-end and automation support. This is workable if TMW retains clear people-development ownership, DA owns Website domain support, and JFG's backend and Portal knowledge flows back into App context.

LM's E2E conversation adds an immediate continuity concern: the contractor engagement may end around October or November, and her cross-platform journey knowledge is not yet fully documented. Grouping related tickets for coherent E2E testing, clearer staging monitoring, and reliable source data should be built into the future Website and cross-platform operating model.

There is also an ownership question. The Website Lead is accountable for the Website platform, and management expectations outside QA assume they will handle the situation. Expectation for Web 3 involvement agreed with DA on 2026-09-14.

KB's initial Website conversation adds a related quality-system concern: backend preview, staging front-end, and test-data connections can make end-to-end testing difficult, while thin staging coverage and isolated component testing may miss customer-impacting failures. This means the sustainable model needs to address environment and journey coverage as well as people capacity.

## Challenge

As the QA & Test Engineering Manager, how do I protect Web 3 delivery and Exerp release confidence while creating a sustainable model for Website QA that:

- acknowledges the real capacity reduction without accepting avoidable delivery risk
- prevents work from silently queuing behind the remaining Web 3 QA
- clarifies whether the reporting lines are aligned with platform accountability and day-to-day support
- determines whether the Mobile App Lead should provide more active Web 3 support because of the reporting line and overlapping domain
- makes the Website Lead genuinely accountable for understanding and managing Website quality risk across Web 1, Web 2, and Web 3
- uses developer-QA collaboration and changed team velocity as part of the solution, rather than as the whole solution
- creates a model that remains workable after the immediate Exerp pressure has passed

## Questions To Explore

### Capacity And Immediate Risk

- What Web 3 work is genuinely critical before the Exerp release, and what can be deferred, reduced, or covered differently?
- Where exactly is work backing up: refinement, test preparation, execution, defect investigation, or release readiness?
- What is the realistic throughput of one QA in Web 3, and how should the team adjust scope and commitments around it?
- Which checks can developers own or pair on without weakening confidence?
- Can a short, time-boxed cross-cover arrangement reduce the immediate risk without creating a second unmanaged queue elsewhere?
- What evidence should trigger escalation for another QA resource rather than continued expectation-setting?
- Does the current QA pull-request code-owner model improve quality enough to justify its focus cost, and can KB provide more targeted coverage for backend or cross-stack changes?

### Reporting Lines And Coverage

- Is it correct for the Web 3 QA to report to the Mobile App Lead when the role is embedded in Website?
- Should reporting follow people management, platform accountability, day-to-day technical leadership, or a deliberate combination?
- What would be gained and lost by moving the report to the Website Lead?
- If the reporting line stays as it is, what explicit responsibility does the Mobile App Lead have for Web 3 support and development?
- How should the Website Lead remain accountable for Web 3 quality risk even when the QA report is elsewhere?

### App And Web 3 Overlap

- How much do the Web 3 and Mobile App domains genuinely overlap in the web portal and member login journeys?
- Can the Mobile App Lead provide useful cover, pairing, prioritisation, or coaching without becoming overloaded by Mobile App problems?
- Would shared domain knowledge and automation patterns make this a sustainable relationship or only a short-term plaster?
- Which responsibilities must remain with the Website Lead because they concern Website delivery, stakeholder expectations, or platform risk?

### Leadership And Ownership

- What information does the Website Lead need to manage Website quality risk across all three teams?
- What support does DA need for Web 3?
- What does accountable leadership look like in practice: attending the right conversations, understanding risk, setting priorities, coordinating cover, and communicating trade-offs?
- How should technical leads' new responsibility for team and initiative leadership be defined, especially where product support has reduced?
- Review Web 3 ownership at QA Lead Sync.

### Sustainable Operating Model

- Should Website have one shared QA capacity model across Web 1, Web 2, and Web 3 rather than treating each report as a separate team resource?
- How should the three QA Leads coordinate cross-cover, priorities, specialist knowledge, and release risk?
- How should the model provide representative staging and preview paths for cross-service journeys without destabilising shared staging?
- What should be visible to Delivery and the business when QA capacity is constrained?
- How do we ensure the model does not rely on me continuing to act as the unofficial Web 3 lead?

## Initial Position

The capacity reduction is real and should lead to an explicit reset of scope, throughput, and risk. Telling teams that work will slow down is necessary, but it is not a complete management response. Before accepting avoidable delay, map the critical Exerp work, remove lower-value demand, use targeted developer-QA pairing, and test whether short-term cross-cover is possible.

The reporting line should be reviewed against both people leadership and platform accountability. The current arrangement may be defensible if the Mobile App Lead actively supports the Web 3 QA and the Website Lead retains clear platform accountability. It is not defensible if the reporting line simply leaves Web 3 without practical leadership. The overlap between Mobile App and Web 3 is worth exploring, but it should be evidence-led and should not conceal the need for a sustainable Website model.

The Website Lead needs to own the situation in practice, not only on the organisation chart. That means understanding the detail sufficiently to prioritise, coordinate cover, communicate risk, and make the case for resource. Set the expectation, offer support, review progress.

DA's initial conversation confirms that managing three Web teams is difficult and that he currently relies on active QA boards, joining tickets when needed, and a separate automation-improvement epic. He accepted that he needs to become more visible and involved in Web 3. This gives the accountability question a practical baseline: agree what visible Web 3 ownership means and review whether it is happening, rather than treating platform ownership as an abstract expectation.

The operating model should also make it possible to test the journeys it is accountable for. A capacity plan that leaves preview and staging connections unreliable will continue to produce false confidence even if ownership is clarified. The environment proposal should therefore be validated with engineering and treated as a supporting hypothesis, not assumed to be the only solution.

## 2026-10-15 Update

- Ownership model largely settled for now: TMW (Web Team Two) works with DA on Website lead responsibilities; KB has taken on the App lead role as a Senior QA, supported by AC.
- A possible Join / Portal split for Web is held until 2027 planning, when the work is known.
- Status moved to active monitoring; horizon to Later.

## 2026-10-16 Update — Ideas Triage

_From the Ideas triage on 2026-10-16 ([ideas log](../state/ideas-log.md))._

- Each team (Web, Payments, Mobile) has a lead handling issues in their space with AC's support, but the leads still don't talk enough across teams. The QA lead sync is the current bridge; TMW's move into Web should help.
- Question: is the lead sync enough, or does cross-team work (shared apps, Exerp data and config) need named owners?

## Roadmap

| ID | Step | Owner | Depends on | Status |
|----|------|-------|------------|--------|
| CH-04.1 | Agree interim Web 2 cover expectations with DA | AC | — | done |
| CH-04.2 | Reassign platforms: TMW to Web Team Two, KB to App | AC | — | done |
| CH-04.3 | Review DA's Web visibility expectations at next 1:1 | AC | — | later |
| CH-04.4 | Agree ownership and coverage model across Web and App | AC | CH-04.2 | done |
| CH-04.5 | Document JFG crossover support and resilient Exerp release ownership | AC | CH-04.4, IMP-09.4 | later |
| CH-04.6 | Decide whether the reporting line should change | AC | CH-04.4 | later |
| CH-04.7 | Decide Join / Portal split for Web in 2027 planning | AC | CH-04.4 | later |

## Status & Next Action

**Status:** Open — Web 3 capacity and Website QA accountability need a short-term response and structural review. GL has offered his support in a 2026-09-17 touch-base and agreed a two-part plan (see [Leadership Direction, 2026-09-17](../context/leadership-direction.md)).

_2026-10-23:_ moving TMW onto Web has given the area more support. TMW can act as a secondary lead and is closely involved in Web 3, where JFG reports to her.

**Short-term:** DA is covering the current Web 2 gap created by a holiday absence, with defined, visible work for this period rather than open-ended cover. I am meeting the engineering lead shortly to work through delivery strategies for this period, including whether the interim support currently in place should be extended to give more time to embed the wider ways of working. 2026-09-18: a Web 2 ticket was reassigned to LM as an interim fix; cover expectations agreed with DA on 2026-09-22.

**Long-term:** Once firefighting eases, shift focus to the sponsored strategic initiatives — starting with staging environments and test data — with GL as sponsor. Allocate pieces of this work to DA, giving concrete, visible ownership aligned with his Staff-level development goals (see [DA profile](../team/da.md)).

**Next action:** Build a two-part view with the Website Lead, Mobile App Lead, Web 3, and Delivery: first, the critical work and Exerp risk for the next few weeks; second, the proposed ownership and coverage model across Web 1, Web 2, Web 3, and Mobile App. Use this to agree immediate cover, revised expectations, and whether the reporting line should change.

Following DA's initial conversation, include a clear, observable expectation for his Web 3 involvement and review it through the QA Lead Sync. Capture the active-board, ticket-level, and automation-improvement mechanisms that make Website ownership visible.

Also document the support model for JFG's crossover arrangement and make Exerp/BGW release ownership resilient rather than dependent on informal knowledge transfer.

Add a time-bound E2E knowledge-transfer plan and a decision on whether the function needs a replacement E2E role, redistributed ownership, or a different capability model.

**Watch for:**

- Web 3 work queuing while delivery commitments remain unchanged
- developer-QA support being proposed without time, ownership, or a defined scope
- the Mobile App Lead being expected to cover Web 3 without capacity or explicit accountability
- me continuing to absorb Web 3 leadership informally
- a short-term Exerp fix becoming the permanent operating model

## Related

- [DA profile](../team/da.md) — agreed expectations and development goals.
