---
id: DC-2026-09-14-head-of-delivery-dj
type: discovery-call
date: 2026-09-14
pillars: [P3, P6, P10]
focus: [people, ownership, productivity]
links: [IMP-01, IMP-02]
people: [GL, GH, DJ, LM, CR]
---

# 2026-09-14 - Head of Delivery - DJ

## Call Context

- **Date:** 2026-09-14
- **Source / role:** DJ, Head of Delivery (peer to me and GH — Head of Software Engineering — both reporting to GL, Software Engineering Director)
- **Conversation type:** Stakeholder discovery
- **Related team or platform:** Initiative lifecycle / delivery process, CR process, QA involvement in initiative scoping
- **Notes based on:** Personal notes / discovery conversation

## Purpose

- Initial discovery conversation with the Head of Delivery to understand delivery's perspective on QA, check whether QA is perceived as a bottleneck, and understand how the initiative lifecycle (Kanban-based) works end-to-end so QA can plug into it at the right stage.

## Key Signals

### What Matters To Them

- Keeping work well-scoped: initiatives are capped at 4-6 weeks (hard target, not a guideline); anything bigger must be sliced.
- Clean flow through the initiative lifecycle with WIP limits enforced, particularly 1-2 initiatives per team in development.
- Weekly reporting up to senior/chief executive stakeholders on initiative progress.
- Getting QA involved at the right point in initiative scoping, not just at the end.

### Current Friction Or Risks

- No standing regular 1:1 cadence needed between DJ and me — we're both already present in enough shared forums (e.g. weekly initiative review) covering the same ground, so a dedicated recurring call would be redundant. Agreed to keep this as a one-off discovery call and meet only when a specific challenge or experiment needs discussing.
- No Product Owner currently in place for initiatives — role called out as missing from the standard three-lead group (Delivery Manager, Product Owner, SEM/Principal Engineer).
- GL currently does much of the up-front requirements-gathering work with the business at Intake, which may not be sustainable/scalable as a single point of ownership.
- QA is not currently looped in until later in the lifecycle; both agreed QA should be brought in earlier, around First Refinement / team-level discovery rather than only at development or hypercare.

### What Is Working Well

- Direct, positive feedback: DJ does not see QA as holding up delivery; the team is delivering well against initiatives as a whole.
- The move from Scrum to Kanban-style initiative flow (max 4-6 week initiatives) is seen as working well.
- LM's (end-to-end tester) role validating that an initiative has fully met its acceptance criteria / definition of done at the end of an initiative is seen as valuable and correctly placed.
- CR (change request) process is proportionate: not applied to every day-to-day change, only to larger features — agreed and aligned between us; Head of Service Delivery is keen on CRs generally but both DJ and I agreed the lighter-touch approach for routine changes is right.
- Initiatives can be raised for QA-driven work, not just product/business-driven work.

### What They Asked For / Suggested

- Suggested exploring retros specifically on completed initiatives as a possibly useful addition.
- Agreed I should raise the member creation tool/process need as a formal initiative, likely engaging the Principal Engineer as the technical lead, then get it properly triaged and documented through Intake so it can be put in front of the group.
- Agreed QA should be pulled into the initiative process earlier — at the point work starts moving from senior leadership scoping into team-level discovery/refinement — rather than only engaging once development starts.

## Metrics Discussed

DJ has Delivery Managers below him, one embedded per scrum/squad. The metrics below are what DJ tracks at his (Head of Delivery) level; each Delivery Manager tracks more granular, squad-level metrics underneath this.

| Metric            | Source Of Truth                                       |
|-------------------|-------------------------------------------------------|
| Cycle Time        | Time in Status report                                 |
| Throughput        | Jira transition to Done                               |
| WIP               | Live on the board                                     |
| Flow Efficiency   | Time in Status report                                 |
| Ageing Work Items | Dots on card in Kanban / cross-team escalation report |

- **Cycle Time:** time from work starting to work done; lower and more consistent is better. If trending wrong, look for blockers, large items, or stages where work pools up.
- **Throughput:** items completed per period (bi-weekly); reveals sustainable delivery capacity and underpins forecasting. If trending wrong, investigate whether items are getting bigger or WIP is too high.
- **WIP:** items actively in progress at any point; high WIP means slow flow, context switching, and hidden risk. If trending wrong, enforce WIP limits — stop starting, start finishing.
- **Flow Efficiency:** % of cycle time actively worked on vs waiting; most teams are under 20% efficient, so raising this is where the big gains are. If trending wrong, find and eliminate waiting states — approvals, handoffs, dependencies.
- **Ageing Work Items:** items in progress longer than expected based on historical cycle time; surfaces stuck work before it becomes a crisis. If trending wrong, investigate and unblock immediately — age should be visible on the board. Cross-team stale items (3+ days in progress) are reported daily.

- Cycle time / time-in-status is total elapsed time, including if a ticket bounces between In Progress and QA and back again — it isn't reset each time it re-enters a stage.
- DJ confirmed again here (separately from the earlier general feedback) that QA is not seen as taking too long to test things, based on this data.
- I suggested an additional metric that isn't currently tracked at DJ's level: how many times an item gets sent back to development as "failed QA". DJ agreed this could be useful, but it's more likely tracked (if at all) by individual leads/squads rather than at his level, and might need to be hand-cranked out of Jira rather than being a ready-made report.
- We also discussed the ratio of tickets tested as "dev QA" (developer self-verification) versus tickets going through "real" QA — DJ agreed this could be a useful metric for me to report on.

### Shift-Left / QA Capacity Discussion

- Recurring problem raised: individual QAs embedded in teams often have an empty "ready to test" column with nothing queued, but as soon as a ticket lands there it's hard for a QA to justify not pulling it in immediately — there's no accepted definition of "QA is deliberately waiting/batching" versus "QA is idle".
- I think this needs to be a cultural shift over time: if QA is faster and more consistently in progress, it's an easier case to make for batching/grouping tickets together and testing them once at a natural checkpoint, rather than testing every ticket as it lands.
- This reinforces the existing view (see LM's end-to-end role) that quality should be checked incrementally along the way, but weighed against risk and batching efficiency — not tested ticket-by-ticket by default.
- DJ agreed with this direction, which is what prompted the "dev QA vs real QA" ratio idea above — it would give visibility into how much is genuinely QA-tested versus developer-self-verified.
- Agreed the bigger levers for QA value are: getting involved in initiative planning/scenario design earlier, grouping ticket testing rather than one-by-one, and maximising QA time through better environments and test data — i.e. shifting QA toward more analytical/planning work and away from being purely a per-ticket testing gate.
- DJ's view on how he can help: keeping initiatives properly scoped (not overblown) so the volume of tickets QA has to get through per initiative stays manageable.

## Cross Teams / Staging Reporting Discussion

- Raised that while having a dedicated QA line in Cross Teams is good, it's sometimes hard to give a clean update there because I'm commenting across many other points as we go through actions and issues — there's almost always a QA angle to other people's items too, not just the QA line itself.
- Agreed there's still value in keeping a distinct QA line for anything that falls genuinely outside other remits; talked through what I typically cover in that slot — QA capacity, workload, and what the team is balancing.
- Agreed Cross Teams should start specifically covering staging: how it's going and its monitoring points, including a dedicated point for any staging warning signals. I can own reporting this end-to-end, which ties directly into the staging monitoring/first-responder work already underway.
- Noted the end-to-end tester (LM) currently comments on this in Cross Teams; when she leaves, this may instead be covered per-initiative as each initiative completes its end-to-end pass, rather than as a standing Cross Teams comment.
- Flagged this as a process point rather than something to resolve in this call: initiative sign-up should always include an end-to-end test as a requirement, and this should feed into succession planning for the end-to-end tester role rather than being solved here.

## Themes And Interpretation

- Directly stated: QA is not perceived as a delivery bottleneck; the working relationship and current output are viewed positively.
- Directly stated: the initiative lifecycle runs through Intake → In Discovery → Ready for Development → In Development → Hypercare & Measurement → Closed, governed by a three-lead group (Delivery Manager, Product Owner, SEM/Principal Engineer) and a weekly initiative review meeting (Tuesdays).
- Directly stated: In Development is hard-capped at 6 weeks; anything needing more must be raised as a new initiative rather than extending the current one.
- My interpretation: this was a useful one-off calibration call rather than the start of an ongoing cadence — the real signal is that DJ and I already have enough shared surface area (initiative review, ways of working) that a dedicated recurring sync would be low value; better to convene only around specific challenges or trials.
- My interpretation: the missing Product Owner role and GL's concentration of Intake-stage business requirements gathering is a wider organisational gap, not something QA can resolve, but worth keeping visible since it affects how well-formed initiatives are by the time they reach a team.
- My interpretation: getting QA involved earlier (around First Refinement / team discovery) is a concrete, actionable change I can drive — it doesn't require DJ's ongoing involvement, just visibility into when initiatives move from senior scoping into team-level detail.
- Hypotheses to validate: raising the member creation tool as a formal initiative via Intake, with the Principal Engineer as technical lead, is the correct route to get development support committed.
- Directly stated: current pacing metrics (cycle time, throughput, WIP, flow efficiency, ageing items) are viewed as adequate at DJ's level and confirm QA isn't a delivery drag.
- My interpretation: a "failed QA" bounce-back metric and a "dev QA vs real QA" ratio metric are both credible, low-cost additions that would give evidence for the shift-left conversation, but neither exists today at DJ's reporting level — I may need to source or build this myself from Jira rather than expect it handed to me.
- My interpretation: the empty-queue-vs-batching tension is a genuine cultural blocker to shift-left, not a process gap — it needs an explicit, agreed definition of acceptable QA batching behaviour so individual QAs aren't penalised for not instantly pulling tickets.
- Directly stated: Cross Teams will start carrying a specific staging health/monitoring point, including staging warning signals, which I will own reporting on.
- My interpretation: the QA line in Cross Teams is a slightly awkward format for me currently, since QA-relevant commentary spans other people's updates too — worth keeping in mind rather than something that needs fixing immediately.
- My interpretation: the loss of LM's standing Cross Teams end-to-end commentary is really a succession-planning risk, not a Cross Teams process gap — the fix is ensuring end-to-end testing is a hard requirement of initiative sign-up regardless of who covers it.

## Mapping

### Strategic Mission(s)

- Delivery Flow & Resilience
- People & Practice
- Business Risk & Stakeholder Trust

### Role Pillar(s)

- Delivery Confidence & Flow
- Quality Ownership & Culture
- Stakeholder Confidence & Visibility

### Objective Lens(es)

- Business Operator
- Value Creator

### Related 30/60/90 Focus Area(s)

- Ownership
- Productivity

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Raise the member creation tool/process need as a formal initiative via Intake** — Owner: AC — Destination: Notion / Improvement [02-dynamic-member-creation-and-test-data.md](../../improvements/02-dynamic-member-creation-and-test-data.md) — Notes: Document requirements clearly; engage Principal Engineer as likely technical lead; get triaged through the initiative process.
- **Get QA looped into initiatives earlier (around First Refinement / team discovery)** — Owner: AC — Destination: Ways of Working — Notes: Agreed direction with DJ; needs a practical mechanism (e.g. visibility into board moves from Discovery to Ready for Development).
- **Consider whether initiative-level retros are worth trialling** — Owner: AC — Destination: Notion / Ways of Working — Notes: Raised by DJ as a possibly useful addition; not yet committed.
- **Confirm no standing recurring call needed with DJ; convene only for specific challenges/trials** — Owner: AC — Destination: Cadences — Notes: Update [cadences.md](../../ways-of-working/cadences.md) to reflect this decision.
- **Investigate feasibility of a "failed QA" bounce-back metric** — Owner: AC — Destination: Notion / Metrics — Notes: Not currently tracked at DJ's level; likely needs to be sourced from Jira directly.
- **Investigate feasibility of a "dev QA vs real QA" ratio metric** — Owner: AC — Destination: Notion / Metrics — Notes: DJ agreed this would be a useful metric for me to report on.
- **Define what acceptable QA batching/waiting looks like, to support shift-left** — Owner: AC — Destination: Notion / Ways of Working — Notes: Address the cultural tension where an empty queue makes it hard for QA to justify not instantly pulling a ticket.
- **Start reporting staging health/monitoring and warning signals in Cross Teams** — Owner: AC — Destination: Notion / Improvement [01-staging-monitoring-and-alerting-ownership.md](../../improvements/01-staging-monitoring-and-alerting-ownership.md) — Notes: Agreed with DJ as a new standing Cross Teams point; ties into staging first-responder work.
- **Add "initiative sign-up requires an end-to-end test" as a process point** — Owner: AC — Destination: Notion / Ways of Working — Notes: Raised as a succession-planning consideration for the end-to-end tester role rather than a Cross Teams fix.

## Possible Outputs

- Candidate improvement: Formal initiative submission for the member creation tool/process, evidenced in [02-dynamic-member-creation-and-test-data.md](../../improvements/02-dynamic-member-creation-and-test-data.md).
- Candidate ways-of-working update: QA entry point moved earlier in the initiative lifecycle (First Refinement rather than In Development).
- Candidate achievement evidence: Positive stakeholder feedback that QA is not a delivery bottleneck and is delivering well against initiatives.
- Candidate improvement: New QA-relevant delivery metrics ("failed QA" bounce-backs, dev QA vs real QA ratio) to evidence shift-left progress.
- Candidate ways-of-working update: Staging health/monitoring as a standing Cross Teams reporting point, owned by QA.
- Candidate succession-planning input: End-to-end test as a mandatory initiative sign-up requirement, for the end-to-end tester role.

## Open Questions

- What is the practical mechanism for QA to get visibility into initiatives as they move from senior leadership scoping into team-level First Refinement?
- Who fills the Product Owner gap in the three-lead group, and does that affect how well-scoped initiatives are before reaching a team?
- Is GL's concentration of Intake-stage requirements gathering sustainable, and does it create a bottleneck upstream of delivery?
- Can a "failed QA" bounce-back metric and a dev-QA-vs-real-QA ratio be sourced from Jira without significant manual effort?
- What does an agreed, defensible definition of QA batching/waiting look like, so idle-queue time isn't mistaken for QA sitting around?
- Once LM moves on, how will end-to-end initiative sign-off be covered in practice, and is per-initiative coverage a robust enough replacement for standing Cross Teams visibility?
