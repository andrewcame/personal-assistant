---
id: CH-13
tag: 2027 transition
type: challenge
status: open
horizon: now
updated: 2026-11-10
pillars: [P1, P6]
focus: [people, ownership]
jd: []
jira: []
outcome:
goals: []
links: [IMP-02, IMP-05, IMP-10, IMP-11, CH-09]
people: []
---

# Challenge 13 — 2027 Business Direction Transition

## Context

- On 2026-11-10 AC saw a preview of the 2027 business direction ([Leadership Direction, 2026-11-10](../context/leadership-direction.md)): web and app technology moves to a third party; the QA team pivots to building agentic workflows for other areas of the business; for the rest of 2026 the aim is to "get done what we can" and leave things in a good place.
- It is a preview, not an announcement. AC's understanding (2026-11-10) is that, whatever the outcome, the team will not manage any of the systems. The open question is therefore **what of our ecosystem remains**: which test packs, pipelines, environments, tools and documentation the third party keeps, and which are retired. AC expects it to be confirmed around the end of 2026.
- It changes the driving theme ([horizons.md](../context/my-role/horizons.md)) and most of the improvement plan.

## The Challenge

- How do we keep delivering useful work for the rest of 2026, and leave things in a good place for whoever owns them next, while the scope of the handover and the team's future remit are unknown?

## Questions To Explore

- What of our ecosystem remains: which test packs, pipelines, environments, tools (e.g. BrowserStack, Report Portal) and documentation the third party keeps, and which are retired?
- When does the handover start, and who leads it on each side?
- What is the QA team's remit in 2027, and what is AC's role?
- What does "a good place" mean for each live record: finished, documented and handed over, or parked?
- Which current skills and tools (this assistant, Foundry, Cloudflare AI) carry over into building agentic workflows?

## Initial Position

- Don't rip up the plan until the direction is confirmed. Triage every live challenge and improvement into **finish** (worth doing whatever happens), **leave in a good place** (stop at a clean, documented checkpoint) or **park** (Later, or close with `outcome: none`).
- Bring the agentic-workflow work forward (IMP-05 Assistant) so capability and evidence are ready for 2027.
- Log outcomes and evidence carefully as records close or reach a checkpoint; EOY reviews are due by 2027-01-15.
- Decisions taken on 2026-11-10: IMP-10 BrowserStack explores a monthly rolling plan; IMP-11 Backend tests is not started and moves to Later; IMP-02 Member data sees the Portal member creation initiative out; CH-09 Mobile coverage has not really started and moves to Later.

## Roadmap

| ID      | Step                                                                                      | Owner | Depends on                | Status | Ticket | Card                                                       |
|---------|-------------------------------------------------------------------------------------------|-------|---------------------------|--------|--------|------------------------------------------------------------|
| CH-13.1 | Triage live challenges and improvements: finish, leave in a good place, or park           | AC    | —                         | done   | —      | Triage challenges and improvements for the 2027 transition |
| CH-13.2 | Find out what of our ecosystem remains (test packs, pipelines, environments, tools, docs) | AC    | —                         | next   | —      | Find out what of our ecosystem remains                     |
| CH-13.3 | Confirm the handover timeline and who leads it on each side                               | AC    | CH-13.2                   | later  | —      | —                                                          |
| CH-13.4 | Confirm the QA team's 2027 remit and AC's role                                            | AC    | —                         | later  | —      | —                                                          |
| CH-13.5 | Re-plan the horizons and driving theme for 2027 once the direction is confirmed           | AC    | CH-13.2, CH-13.3, CH-13.4 | later  | —      | —                                                          |

## Status & Next Action

**Status:** Open — direction previewed 2026-11-10 and live records triaged; not yet confirmed (expected around the end of 2026).

**Next action:** Find out what of our ecosystem remains (CH-13.2).

## Outcome

_Fill when resolved or closed: where the result landed (achievement or team evidence) and set `outcome:` above (achievement | evidence | both | none)._

## 2026-11-10 Update — triage agreed

AC approved the triage of the remaining records:

| Verdict                 | Records                                                                                                                                                                                                                                          |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Finish                  | IMP-08 Objectives & reviews; CH-07 E2E continuity (refocused on handover documentation, moved to Now); IMP-02 Member data (Portal member creation initiative only)                                                                                |
| Leave in a good place   | IMP-01 Staging SRE (routine and alert runbook); IMP-04 QA metrics (JQL baseline documented, Report Portal not wired); IMP-06 Coverage baseline (handover inventory); IMP-10 BrowserStack (monthly rolling plan)                                    |
| Park (Later)            | IMP-11 Backend tests; CH-09 Mobile coverage; IMP-12 Domain ownership; CH-10 Pico source of truth; CH-12 Exerp release risk; IMP-09 Exerp release process; IMP-07 Payments cover; IMP-03, IMP-13, IMP-14, IMP-15, IMP-17, IMP-18, CH-02, CH-05, CH-08, CH-11 |
| Bring forward           | IMP-05 Assistant (Next); IMP-16 AI test boilerplate flagged as a 2027 pivot candidate                                                                                                                                                             |

- Parked records close with `outcome: none` once CH-13.2 confirms what of our ecosystem remains.

## 2026-11-10 Update — reframed

- AC: whatever the direction, the team will not manage any of the systems, so the question is not "what do we look after" but "what of our ecosystem remains". CH-13.2 and the parked records reworded to match; nothing is expected to restart.
- The Report Portal card stays in Backlog (not archived) in case it is useful in the new set-up. IMP-18 In-app Join test may no longer be relevant; it stays parked in Later.

## 2026-11-10 Update — opened

- Opened from the 2027 direction preview. First four decisions applied (see Initial Position); the remaining records are proposed for triage in chat.
