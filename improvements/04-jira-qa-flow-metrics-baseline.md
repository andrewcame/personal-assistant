---
id: IMP-04
type: improvement
status: in-progress
horizon: next
updated: 2026-10-23
pillars: [P6]
focus: [productivity]
jd: [JD-09]
goals: []
links: [IMP-06]
people: []
---

# Improvement 04 — Jira QA Flow Metrics Baseline

## Context

- The 30-day plan requires a baseline of how work flows through QA, where time is spent, and whether queues, environments, data, clarification, or builds are creating avoidable delay.
- Delivery already uses Jira as the source of truth for cycle time, throughput, WIP, ageing work, and blocked items. Analysis of the Delivery Manager's `Kanban Stats.xlsx` confirmed that several useful flow signals are already available, but also exposed inconsistent formulas and manual handling.
- The spreadsheet was useful discovery evidence, not a proposed reporting system. The preferred direction is to source the QA flow baseline directly from Jira and avoid creating a parallel manually maintained dataset.
- The Head of Engineering intends to introduce engineering metrics later. This improvement should establish QA-relevant flow evidence without pre-empting that work or presenting workflow measures as DORA metrics.
- Originating evidence: [Delivery Manager retrospective discovery](../context/discovery-calls/2026-09-24-retrospective-delivery-manager-app-pay-web-3.md) and [Head of Delivery discovery](../context/discovery-calls/2026-09-14-head-of-delivery-dj.md).

## Objective

- Establish a repeatable, Jira-first QA flow baseline for Web, App, and Pay that supports 30-day discovery and improvement decisions without ranking teams or individuals.
- Provide a small shared view of five QA-specific measures, with documented definitions, filters, ownership, caveats, and refresh cadence.
- Use an AI-enabled spreadsheet only if Jira cannot calculate a required distribution or transition measure. Any spreadsheet should refresh from Jira exports or API data rather than become a second source of truth.

## Related

- Goal(s): [2026 goals](../goals/2026.md) — goals are still to be confirmed
- Role pillar(s): [Delivery Confidence & Flow](../context/role-pillars.md), [Stakeholder Confidence & Visibility](../context/role-pillars.md)
- Plan: [30-day plan](../context/my-role/30-day-plan.md) — Evaluate Delivery and establish baselines
- Role expectation: [Job specification](../context/my-role/job-specification.md) — reporting, engineering hygiene, delivery partnership, and release readiness grounded in real data
- Operating model: [Software delivery lifecycle](../ways-of-working/software-delivery-lifecycle.md) — existing Jira flow measures and sources of truth
- Originating recommendation: Self, informed by Delivery discovery and workbook analysis

## Measurement Principles

- Measure the delivery system and its constraints, not individual productivity or QA utilisation.
- Keep definitions consistent across teams, but interpret results in the context of each application and workflow.
- Prefer trends, distributions, and ageing over isolated averages or league tables.
- Pair speed measures with failure, rework, and risk signals so faster movement is not mistaken for better quality.
- Use the smallest useful baseline first. Do not duplicate the Head of Engineering's planned DORA work.
- Record data quality and workflow-adoption gaps alongside every result.

## Starting Measures And Jira Route

### 1. QA Queue And Pickup Time

- **Definition:** Median and 85th percentile elapsed from entering Ready for Testing until QA pulls the item into Testing. Report repeated entries separately so returns do not hide behind one total.
- **Jira route:** Time in Status report or status-transition history.
- **Readiness:** Available after checking the report capabilities.
- **QA relevance:** Shows whether work is waiting for QA capacity or an agreed batching point before testing starts.

### 2. Elapsed Time In QA

- **Definition:** Median and 85th percentile elapsed from first entering Ready for Testing until leaving the QA-facing workflow, including repeated Testing and Failed QA loops. Report queue time and active Testing time alongside the total where the status history allows it.
- **Jira route:** Time in Status or status-transition history, with agreed start and end statuses mapped consistently across teams.
- **Readiness:** Available after checking status-history and report capabilities.
- **QA relevance:** Shows how long work remains within the QA part of the workflow and whether that time is changing.
- **Guardrail:** This is not a measure of tester effort or performance. Environment availability, test data, builds, clarification, dependencies, batching, and engineering rework can all increase elapsed time in QA; review it with the QA-stage delay breakdown before drawing conclusions.

### 3. QA-Facing WIP And Ageing

- **Definition:** Current items in Pre-Test Review, Ready for Testing, Testing, or Failed QA; age since entering the QA-facing workflow and the current status.
- **Jira route:** Saved filter and dashboard; card ageing for live use; status history or API data for reproducible ageing.
- **Readiness:** Available now, with the ageing definition still to confirm.
- **QA relevance:** Shows current QA demand, stale work, and whether WIP is exceeding available test capacity.

### 4. QA-Stage Delay By Cause

- **Definition:** Count and elapsed time for QA-facing items delayed by QA capacity, environments, test data, builds, clarification, dependencies, or another recorded cause.
- **Jira route:** QA-facing status filter combined with Blocked status or flag, Time in Status or changelog data, and a consistently populated delay-reason field or label.
- **Readiness:** Requires consistent blocker use and an agreed delay-cause classification.
- **QA relevance:** Separates time spent testing from delays around testing and shows whether QA itself or a dependency is slowing delivery.

### 5. Failed-QA Return Rate

- **Definition:** Distinct items entering Failed QA divided by distinct items entering Testing during the same cohort and reporting window.
- **Jira route:** Jira changelog, Atlassian Analytics, marketplace Time in Status report, or API extraction. Basic JQL alone is unlikely to provide a reliable transition count.
- **Readiness:** Requires an extraction check.
- **QA relevance:** Indicates how often testing identifies work that needs further engineering change and supports analysis of requirements, developer verification, and defect causes.
- **Guardrail:** Do not treat a high or low rate as QA performance. Segment by failure cause and risk; a falling rate is only positive if escaped defects and release outcomes do not worsen.

## Delivery Measures Excluded From The QA Baseline

- **Weekly throughput:** A Delivery capacity and forecasting measure. It does not show QA effectiveness or whether QA caused delay.
- **End-to-end workflow cycle time:** A Delivery system measure already owned through the wider operating model. QA should use the QA-stage measures above to explain its contribution when total cycle time changes.
- **Ticket-shape distribution:** Useful context for investigating fragmented demand and repeated QA handling, but story points and ticket size are not quality measures.
- **Epic scope growth:** A product and delivery predictability measure. It may explain late quality risk, but it does not measure QA or QE performance.

These measures can be referenced as context during an investigation, but should not appear on the QA baseline dashboard or be reported as QA-owned metrics.

### Cohort And Segmentation Rules

- Use completed calendar weeks and exclude the current incomplete week.
- Start with a rolling four-week view for the 30-day baseline; retain weekly data so trends are not hidden.
- Report Web, App, and Pay separately before drawing any cross-team conclusion.
- Split planned delivery work from bugs, support, operational, and initiative/epic work where Jira issue types allow it.
- Exclude cancelled or duplicate work and document how reopened items are treated.
- Show sample size and missing-field coverage beside status-based measures.

## Jira Discovery Checklist

1. Confirm Jira deployment type, reporting features, marketplace apps, and access to issue changelogs or Atlassian Analytics.
2. Confirm project keys, board filters, QA-facing statuses, issue types, and team-identifying fields for Web, App, and Pay.
3. Map the actual workflow statuses to active, waiting, QA-facing, blocked, and done categories; identify team-specific differences.
4. Validate whether Time in Status reports expose median, 85th percentile, repeated status entries, and exportable underlying data.
5. Check whether `Failed QA`, `Blocked`, and `Dev Testing` are used consistently enough to support trend reporting.
6. Create saved filters and a draft dashboard for measures available natively.
7. Test one status-history extraction for Ready for Testing time and Failed-QA transitions against a small hand-checked sample.

## Fallback: AI-Enabled Analysis Workbook

- Use only where Jira's native reports cannot calculate percentiles, repeated transitions, or cohort-level ratios.
- Pull a reproducible export containing issue key, project or team, issue type, status, transition-from, transition-to, transition timestamp, resolution timestamp, blocker or delay cause, and current status.
- Use Power Query or an equivalent structured import so refreshes do not rely on copy/paste.
- Keep metric definitions and transformations visible and versioned. AI may help generate formulas, summarize patterns, and investigate anomalies, but must not silently alter definitions or source data.
- Reconcile a sample of results back to Jira before using the workbook in leadership reporting.
- Do not extend the Delivery Manager's workbook as the long-term source unless direct Jira reporting proves impractical.

## Relationship To DORA And Wider Quality Metrics

- These five measures are QA flow and quality diagnostics, not DORA metrics.
- Do not infer deployment frequency from ticket deployment statuses, change lead time from workflow cycle time, or change failure from Failed QA.
- Leave the future DORA implementation aligned to the Head of Engineering's wider metrics work, using source-control, CI/CD deployment, and incident data.
- Later QA quality signals may include escaped defects, critical-journey coverage, automation reliability, environment health, and release outcomes. They should be added from their authoritative systems rather than forced into Jira.

## Actions & Progress

### 2026-09-24

- Reviewed `Kanban Stats.xlsx` as discovery evidence and identified useful existing flow data alongside formula and data-quality limitations.
- Confirmed Jira-first as the preferred direction; the shared workbook will not be reworked into the primary QA metrics system.
- Reduced the initial eight-measure set to five QA-specific measures, including elapsed time in QA with attribution guardrails; retained general delivery measures only as investigative context.
- Recorded DORA as a separate, later engineering-owned measurement stream.

### 2026-10-08

- Jira will remain the initial home for QA flow measures and automation-coverage tracking. Lightweight placeholders are being set up first, with definitions and a more robust reporting approach to follow as the baseline is established.
- Coordinate the metrics home with the QA Confluence tidy-up and functional coverage reference tracked in [Improvement 06 - QA Knowledge And Coverage Baseline](06-qa-knowledge-and-coverage-baseline.md).

### 2026-10-16 (ideas triage)

_From the Ideas triage on 2026-10-16 ([ideas log](../state/ideas-log.md))._

- **Report Portal vs Claude reports:** set up Report Portal access with PDEX to check it gives what's needed, and compare it with Claude-built reports. For now, build up the Claude reports and expand later (new step IMP-04.8).
- **Ready-for-Test dwell time by team:** average Ready for Test tickets and how long they stay there. Is the distribution disproportionate to the nature of the work (e.g. more front end means more QA)? Metrics should show whether team ratios (devs vs QA in a team) are appropriate. Data point: Web 1, 3 September — 3 tickets.
- **Metrics home (IMP-04.7):** option of a combined engineering/QA dashboard rather than separate ones; GL hosts internal tools on Cloudflare Workers. Keep discussing with GL.
- **Further measures to consider:** success of dev-QA tickets vs normal QA; right-first-time / rework. Which metrics drive decisions, and what should we surface first?
- **Parked:** a record of ticket changes over time (useful, but possibly not one of the measures needed).

### 2026-10-23 (ideas triage)

_From the Ideas triage on 2026-10-23 ([ideas log](../state/ideas-log.md))._

- **AI coverage check on Jira tickets:** an AI tool that reads Jira tickets and comments for search terms, to answer "did we test x?". It is resource heavy, so filter by people first. Enriched as a later step once the JQL queries exist (new step IMP-04.10).

## Roadmap

| ID | Step | Owner | Depends on | Status |
|----|------|-------|------------|--------|
| IMP-04.1 | Agree five QA flow measures, Jira-first | AC | — | done |
| IMP-04.2 | Set up Jira placeholders for metrics and coverage | AC | IMP-04.1 | doing |
| IMP-04.3 | Write first JQL queries | AC | IMP-04.2 | doing |
| IMP-04.4 | Complete Jira discovery checklist with Delivery or Jira admin | AC | — | later |
| IMP-04.5 | Vibe-code Jira metric tool for gaps | AC | IMP-04.3 | later |
| IMP-04.6 | Produce one-team proof-of-concept baseline | AC | IMP-04.3, IMP-04.4 | later |
| IMP-04.7 | Agree metrics home alongside the Confluence tidy-up | AC | IMP-06.2 | later |
| IMP-04.8 | Set up Report Portal access with PDEX; compare with Claude reports | AC | — | next |
| IMP-04.9 | Build a separate Jira dashboard from the JQL queries | AC | IMP-04.3 | later |
| IMP-04.10 | Test an AI coverage check over Jira tickets and comments ("did we test x?"), filtered by people | AC | IMP-04.3 | later |

## Status & Next Action

**Status:** In progress

**Next action:** Meet the relevant Delivery Manager or Jira administrator to complete the Jira discovery checklist, then produce a one-team proof of concept using native Jira reports first. Use a refreshable analysis workbook only for measures Jira cannot calculate accurately.

## Outcome

- Completed:
- Logged achievement: