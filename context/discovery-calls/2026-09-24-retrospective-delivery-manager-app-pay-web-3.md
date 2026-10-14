---
id: DC-2026-09-24-retrospective-delivery-manager-app-pay-web-3
type: discovery-call
date: 2026-09-24
pillars: [P3, P6, P10]
focus: [people, ownership, productivity]
links: [CH-04, CH-07, IMP-04]
people: []
---

# 2026-09-24 Capture - Delivery Manager, App / Pay / Web 3 (Retrospective)

## Call Context

- **Date:** Original call date unknown; held a few weeks before this retrospective capture and still to be confirmed
- **Capture date:** 2026-09-24
- **Source / role:** Delivery Manager covering App, Pay, and Web 3; one of two Delivery Managers reporting to the Head of Delivery, who reports to the Engineering Director. Person's name not recorded.
- **Conversation type:** Stakeholder discovery
- **Related team or platform:** App, Pay, Web 3; delivery flow and QA capacity
- **Notes based on:** Retrospective personal recollection, supplemented by analysis of the Delivery Manager's shared `Kanban Stats.xlsx` workbook

## Purpose

- Capture an earlier conversation about the QA gap created by my move from Web 3 into the QA & Test Engineering Manager role, and examine whether work shape and ticket fragmentation are consuming scarce QA capacity through repeated handling rather than coherent validation.

## Key Signals

### What Matters To Them

- Protecting delivery flow across App, Pay, and Web 3 while QA capacity is constrained.
- Making the best use of one QA per squad by reducing avoidable context switching, setup, build/release handling, and repeated validation.
- Understanding flow through evidence rather than treating ticket count or story points as individual or team productivity measures.

### Current Friction Or Risks

- My move from Web 3 into the Engineering Manager role may leave a QA capacity gap in Web 3.
- A QA should not routinely receive a stream such as eight tiny tickets in a day when each requires separate context recovery, setup, build or release handling, and validation. The handling overhead may consume capacity without adding equivalent customer confidence.
- Ticket-level flow can hide the cost of repeated QA touchpoints, particularly where related work could be validated together against a coherent feature or acceptance boundary.
- Indiscriminately increasing batch size would create a different risk: slower feedback, later defect discovery, and greater integration uncertainty. The aim is coherent grouping, not simply larger tickets or delayed testing.

### What Is Working Well

- The workbook provides enough throughput, sizing, status-time, WIP, and scope-change data to establish a directional baseline across Web, App, and Pay.
- All three areas completed 21 tickets in the latest complete four-week window, giving a common starting point for comparing work shape while retaining the caveats around story points and unpointed work.
- Existing engineering and QA operating-model direction already recognises risk-based feature-ready or grouped testing, provided acceptance boundaries, regression protection, and risk ownership remain explicit.

### What They Asked For / Suggested

- Explore shaping related work into fewer meaningful validation units so QA can test coherent outcomes rather than handling every small ticket independently.
- Examine whether coherent grouping could reduce builds, releases, and QA touchpoints while preserving fast feedback where risk requires it.
- Use the shared delivery workbook to understand whether the concern is visible in current flow data.

## Workbook Evidence

The analysis below uses the latest complete window in `Kanban Stats.xlsx`: weeks 34-37, ending 2026-09-13. Week 38 is incomplete and excluded. This is retrospective supporting analysis, not evidence that every metric was discussed during the original call.

### Throughput And Work Shape

| Measure | Web | App | Pay |
|---|---:|---:|---:|
| Completed tickets | 21 | 21 | 21 |
| Tickets per week | 5.3 | 5.3 | 5.3 |
| Delivered points | 74 | 66 | 40 |
| Tickets per 10 delivered points | 2.84 | 3.18 | 5.25 |
| 1-2 point tickets | 6/21 (28.6%) | 3/21 (14.3%) | 14/21 (66.7%) |

- On this directional normalization, Pay generated 85% more ticket handling per unit of delivered scope than Web and 65% more than App.
- This supports investigating fragmentation and handling overhead in Pay. It does not prove that Pay was less productive: story points are a team-local proxy, not effort truth, and unpointed-ticket levels make point-based comparisons directional only.

### Cycle Time And Independently Normalized Status Time

| Measure | Web | App | Pay |
|---|---:|---:|---:|
| Median cycle time | 5.39 days | 2.18 days | 1.13 days |
| 85th-percentile cycle time | 10.43 days | 6.70 days | 5.41 days |
| Active / waiting time | 86.47 / 79.99 days | 69.85 / 3.12 days | 46.33 / 30.83 days |
| Independently normalized flow efficiency | 51.9% | 95.7% | 60.0% |

- The normalized percentages use a consistent active / (active + waiting) calculation because the workbook's own flow-efficiency formulas differ by sheet. They must not be substituted uncritically for the workbook dashboard or treated as a settled performance measure.
- Pay's shorter cycle time does not mean its work shape carries no capacity cost. Fast movement of many small tickets can coexist with substantial repeated QA handling, queueing, and rework.
- Web recorded 47.12 blocked days. Pay recorded 13.10 days in Ready for Testing and 5.51 days in Failed QA. Directionally, Web's main visible issue is blocking/waiting, while Pay shows fragmentation alongside QA queue and rework signals. This distinction needs investigation rather than a single cross-team conclusion.

### Current Delivery WIP

| Area | Total WIP | Status distribution |
|---|---:|---|
| Web | 10 | 4 Ready to Deploy; 3 In Progress; 2 Pre-Test Review; 1 Ready for Testing |
| App | 4 | 2 In Progress; 2 Pre-Test Review |
| Pay | 7 | 3 In Progress; 2 Ready for Testing; 1 Deploying; 1 Pre-Test Review |

- Current WIP is a snapshot, not a trend. QA-facing work should be tracked with ageing so a low count does not conceal old or repeatedly returning items.

### Scope Proliferation Signals

| Initiative / epic | Original tickets | Current tickets | Change |
|---|---:|---:|---:|
| WEB-78 | 11 | 33 | +200% |
| PAYTEAM-119 | 4 | 9 | +125% |
| WEB-60 | 11 | 19 | +73% |
| APP-45 | 8 | 14 | +75% |
| APP-15 | 6 | 10 | +67% |

- These Summary-sheet changes may indicate scope churn, discovery, or decomposition after work starts. They are investigation prompts, not automatic evidence of poor planning or unnecessary splitting.

### Data Limitations

- Week 38 is incomplete and should not be included in the baseline window.
- `QA Hrs` appears to represent capacity rather than actual QA effort.
- There are no reliable build, deployment, or release event counts.
- There is no Created date from which to calculate true lead time.
- Workbook flow-efficiency formulas are inconsistent between sheets.
- The Web Failed QA formula is incomplete, so its dashboard value should not be used.
- Unpointed-ticket levels make story-point-normalized metrics directional only.

## Focused 30-Day QA Flow Baseline

Use the next 30 days to establish a flow baseline at system and team level, explicitly avoiding individual or team productivity framing:

- weekly throughput
- tickets per 10 delivered points, reported as directional and alongside unpointed-ticket coverage
- proportion of completed tickets sized at 1-2 points
- median and 85th-percentile cycle time
- days in Ready for Testing, Testing, and Failed QA
- blocked days
- current QA-facing WIP and ageing
- QA re-entry / bounce-backs
- original-versus-current epic ticket count

Do not adopt the workbook's existing flow-efficiency or Failed QA dashboard values without correcting and documenting the formulas. Use the baseline to understand work shape, queues, and system friction, not to rank teams or assess personal productivity.

The workbook cannot yet directly test the core hypothesis. Additional instrumentation would be needed for:

- QA touchpoints or status transitions per coherent feature
- tickets per build, deployment, or release
- active test time versus queue time
- escaped defects and rework before and after coherent grouping

## Themes And Interpretation

- Directly stated: my move from Web 3 into the Engineering Manager role may create a QA gap.
- Directly stated: a stream of many tiny tickets can impose repeated context switching, setup, build/release handling, and validation on a single QA.
- Directly stated: related work should be explored as fewer coherent validation units where that reduces handling without weakening feedback.
- My interpretation: Pay's ticket-shape data is consistent with the fragmentation concern, but the workbook does not measure QA touchpoints, build/release events, or active test effort and therefore cannot establish the capacity cost directly.
- My interpretation: Web and Pay currently show different flow problems. Web's blocking/waiting signal should not be collapsed into the same intervention as Pay's fragmentation and QA queue/rework signals.
- My interpretation: equal ticket throughput across Web, App, and Pay conceals materially different delivered-point and ticket-size profiles; ticket count alone is not an adequate flow or capacity narrative.
- My interpretation: coherent grouping should be defined around testable customer or system outcomes and explicit acceptance boundaries, with early checks retained for high-risk integration points.
- Hypotheses to validate: grouping related work reduces QA touchpoints, build/release handling, and context switching without increasing cycle-time tail, escaped defects, or rework.
- Hypotheses to validate: original-versus-current ticket growth is partly caused by decomposition after work begins and contributes to extra QA handling.
- Hypotheses to validate: QA re-entry and time in Ready for Testing / Testing / Failed QA will identify where fragmentation becomes queueing or rework rather than fast feedback.

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

- Productivity
- Ownership

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Run a focused 30-day QA flow baseline across Web, App, and Pay** — Owner: AC / Delivery — Destination: [30-Day Plan](../my-role/30-day-plan.md) / Notion metrics — Notes: Use system-flow measures, correct inconsistent formulas, and avoid individual/team productivity framing.
- **Define a coherent validation-unit trial** — Owner: AC / Delivery / Engineering leads — Destination: [Engineering Operating Model](../../ways-of-working/engineering-operating-model.md) / [QA Team Operating Model](../../ways-of-working/qa-team-operating-model.md) — Notes: Specify acceptance boundaries, early-risk checks, and measures before trialling grouping; do not default to larger batches.
- **Connect the Web 3 capacity signal to the existing ownership response** — Owner: AC — Destination: Challenge [04-web-qa-capacity-and-accountability.md](../../challenges/04-web-qa-capacity-and-accountability.md) — Notes: Treat work shaping as one lever within the capacity and accountability response, not a substitute for ownership or adequate cover.
- **Use grouped validation evidence in the E2E continuity decision** — Owner: AC — Destination: Challenge [07-end-to-end-quality-ownership-and-continuity.md](../../challenges/07-end-to-end-quality-ownership-and-continuity.md) — Notes: Compare coherent initiative-level validation with late-stage batching and retain explicit ownership.
- **Align the trial with prior Delivery and DevQA findings** — Owner: AC / Delivery — Destination: [Head of Delivery discovery](2026-09-14-head-of-delivery-dj.md) / [Joint Funnel discovery](2026-09-18-technical-lead-joint-funnel.md) — Notes: Reuse the existing direction on deliberate grouping, developer verification, and risk-based QA rather than creating a parallel model.

## Possible Outputs

- Candidate challenge evidence: [Challenge 04](../../challenges/04-web-qa-capacity-and-accountability.md) — additional evidence for the Web 3 QA gap and the need to reshape demand as well as clarify coverage.
- Candidate challenge evidence: [Challenge 07](../../challenges/07-end-to-end-quality-ownership-and-continuity.md) — evidence for defining coherent initiative-level acceptance and E2E ownership.
- Active improvement: [Improvement 04 — Jira QA Flow Metrics Baseline](../../improvements/04-jira-qa-flow-metrics-baseline.md) — establish five QA-specific flow and quality measures directly from Jira, using a refreshable analysis workbook only where native reporting is insufficient.
- Candidate ways-of-working update: a measured coherent-validation trial with explicit acceptance boundaries and safeguards against delayed feedback.

## Open Questions

- What was the exact original call date, and who was the Delivery Manager?
- How many QA touchpoints and status transitions does each coherent feature currently generate?
- How many tickets are handled per build, deployment, and release in each area?
- How much elapsed QA-stage time is active testing versus queueing, setup, environment, data, build, or release waiting?
- Do escaped defects and rework improve or worsen after related work is grouped around coherent acceptance boundaries?
- Which ticket-count increases reflect healthy discovery or decomposition, and which occur late enough to create avoidable handling and integration cost?
- What grouping size preserves early feedback for high-risk changes while reducing repeated low-value QA handling?