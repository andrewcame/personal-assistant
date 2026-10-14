---
id: DC-2026-09-01-staff-engineer-devex
type: discovery-call
date: 2026-09-01
pillars: [P4, P5, P6, P7, P10]
focus: [ownership, automation, productivity]
links: []
people: []
---

# 2026-09-01 - Staff Engineer DevEx

## Call Context

- **Date:** 2026-09-01
- **Source / role:** Staff Engineer, Platform / DevEx
- **Conversation type:** Engineering discovery
- **Related team or platform:** Platform, DevEx, backend previews, staging, automation reporting
- **Notes based on:** Personal notes / Dictation

## Purpose

- Understand platform and DevEx friction affecting QA confidence, environment health, automation reporting, deployment reliability, and backend test coverage.

## Key Signals

### What Matters To Them

- A unified automation reporting view across environments.
- A dashboard approach similar to Grafana for test and environment health.
- Better staging health checks, reporting, and alerting, closer to the alerting cadence already used in production.
- Stronger visibility of alerts, dead-letter queues, and other red flags before issues reach production.
- More reliable backend preview deploys and a deployment model with less coordination risk.
- Improved backend test coverage beyond a narrow initial backlog.

### Current Friction Or Risks

- Automation reporting is fragmented. ReportPortal is already set up, but the current status and suitability need to be reviewed.
- Staging does not appear to have the same operational alerting discipline as production.
- A recent production issue appeared in staging first but was not flagged.
- Backend preview deploys are flaky, operationally complex, and prone to error.
- Current backend deployment appears to require broad system coordination, with services/adapters deploying in stages and race-condition risk from different deployment orders.
- There are very few backend tests, and current ownership is concentrated with one QA on one backlog.
- Other teams are not consistently adding backend tests.
- Lack of reliable test reporting makes it hard to understand whether failures are caused by product issues, test issues, or environment/deployment issues.

### What Is Working Well

- ReportPortal may already provide a foundation for automation reporting.
- There is existing production alerting practice that could be mirrored or adapted for staging.
- There is enough shared concern around previews, deployments, and alerting to justify focused discovery.

### What They Asked For

- Keep load testing running continuously once it is added.
- Consider staging as the long-term place for load testing if the environment and data can be stabilised, rather than requiring a dedicated environment.
- Use performance testing reactively when things go wrong, supported by production alerts.
- Improve visibility and coordination around Pico backend deployments.
- Investigate whether future preview deployments could deploy only the updated adapter/service and leave the rest of the system as-is.

## Themes And Interpretation

- Directly stated: Environments, monitoring, deployment reliability, and backend test coverage are current areas of concern.
- Directly stated: QA should be closer to staging health, alerts, DLQs, and SRE visibility; QA will own staging alert attention for now.
- Directly stated: Joining the SRE chapter is a useful short-term step.
- My interpretation: Environment health and deployment reliability are becoming prerequisites for trusted automation, not separate platform concerns.
- My interpretation: A unified test dashboard would only be useful if it combines test outcomes with environment/deployment context, otherwise it risks showing symptoms without causes.
- My interpretation: Backend coverage is both a technical gap and an ownership gap; it needs a model that makes contributions normal across teams rather than dependent on one QA/backlog.
- Hypotheses to validate: ReportPortal can become the first iteration of a unified automation and environment-health dashboard.
- Hypotheses to validate: Staging can support continuous load testing if test data and environment stability improve.
- Hypotheses to validate: A generic preview cluster or partial-service deployment model could reduce preview duplication and coordination overhead.

## Mapping

### Strategic Mission(s)

- Technical Mastery & Foundations
- Delivery Flow & Resilience
- Business Risk & Stakeholder Trust

### Role Pillar(s)

- Automation Trust & Reliability
- Test Infrastructure, Environments & Data
- Delivery Confidence & Flow
- Non-Functional Quality & Resilience
- Stakeholder Confidence & Visibility

### Objective Lens(es)

- Value Creator
- Business Operator

### Related 30/60/90 Focus Area(s)

- Automation
- Productivity
- Ownership

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Review current ReportPortal setup and status** — Owner: AC — Destination: Notion / Discovery follow-up — Notes: Check whether it can support unified test reporting by environment.
- **Set up or extend staging alerts** — Owner: Staff Engineer, DevEx — Destination: Notion / Platform follow-up — Notes: Aim to surface alerts, DLQs, and staging red flags before production.
- **Join SRE chapter** — Owner: AC — Destination: Notion / Relationship-building — Notes: Use this to build visibility into support, alerting, and operational signals.
- **Monitor backend preview reliability** — Owner: AC / Platform — Destination: Challenge — Notes: Capture frequency, causes, and delivery impact before recommending changes.
- **Explore backend test ownership model** — Owner: AC / QA Leads — Destination: Challenge / Goal input — Notes: Validate how backend tests should be owned across teams rather than one backlog.

## Possible Outputs

- Candidate challenge: Backend preview deployments are flaky, complex, and risky enough to affect QA confidence and delivery flow.
- Candidate challenge: Staging health signals are not visible or acted on early enough, allowing staging issues to become production issues.
- Candidate challenge: Backend test coverage and ownership are too narrow to support confident recommendations or broad quality ownership.
- Candidate decision: Whether ReportPortal becomes the first unified automation reporting dashboard.
- Candidate decision: Whether QA temporarily owns staging alert review while the alerting cadence is established.
- Candidate goal input: Establish trusted automation and environment-health visibility across key platforms.
- Candidate goal input: Improve backend quality ownership and coverage beyond the initial backlog.
- Candidate initiative input: Unified automation and environment-health dashboard.
- Candidate achievement evidence: Relationship-building with Platform / DevEx and SRE to identify concrete quality foundations and operational risks.

## Open Questions

- What is the current status, adoption, and data coverage of ReportPortal?
- Which automation suites currently publish results anywhere central?
- Which staging alerts, DLQs, and health checks already exist but are not being watched?
- What production alerting cadence should staging mirror, and where should QA sit in that flow?
- How often do backend preview deployments fail or delay testing?
- Which parts of Pico backend deployment require manual coordination today?
- Is partial adapter/service deployment technically viable, and what risks would it introduce?
- What backend tests exist today, who owns them, and which teams should contribute next?
