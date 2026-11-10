---
id: IMP-18
tag: In-app Join test
type: improvement
status: not-started
horizon: later
updated: 2026-11-10
pillars: [P4, P8]
focus: [automation]
jd: [JD-05]
goals: []
links: [IMP-02, IMP-10, IMP-14, CH-10]
people: []
---

# Improvement 18 — Join Journey Test Through Facebook And Instagram In-App Browsers

## Context

- Paid social (Facebook and Instagram adverts and promotions) sends members to Pico Join inside the app's own in-app browser, not Safari or Chrome. Our front-end tests only run the Join journey in a normal browser, so we do not know a member can actually join the way a promotion sends them.
- Prompted by a recent `/cart.js` error that members saw only in these in-app browsers. The aim is not to catch that one bug; it is to make the Join journey run as simulated Facebook and Instagram traffic and confirm a member can join.
- Source: AC idea, 2026-11-10 (with a worked Playwright suggestion). Judged a new improvement rather than an enrichment: IMP-11 (backend test pack), IMP-03 (front-end load and performance) and IMP-10 (mobile app device strategy) each cover a different part of the pack.

## Objective

- The Join journey runs in the front-end pack as simulated Facebook and Instagram in-app traffic (campaign landing, in-app user agent, mobile viewport) with a normal mobile browser as control, and confirms a member can join end to end.

## Related

- Role pillar(s): [P4 Automation Trust & Reliability](../context/role-pillars.md), [P8 Business-Critical Journey Protection](../context/role-pillars.md)
- Originating recommendation: self (AC idea)
- Related: [IMP-02 — Dynamic Member Creation And Automated Test Data Architecture](02-dynamic-member-creation-and-test-data.md) (a Join run creates a real member), [CH-10 — Pico Source-Of-Truth And Exerp-Dependent Test Strategy](../challenges/10-pico-source-of-truth-and-exerp-dependent-test-strategy.md) (Join can break reliance on Exerp, but has failed before), [IMP-10 — BrowserStack Renewal And Mobile Device Strategy](10-browserstack-renewal-and-device-strategy.md) (real-device option), [IMP-14 — CI/CD Quality Gate Model](14-ci-cd-quality-gate-model.md) (where it runs)
- Jira: an initiative is expected when this is promoted; add the keys as `jira:` then.

## Actions & Progress

### 2026-11-10

- Opened from AC's idea. Decision: new improvement, Later (Now is near its limit and delivery will need a Jira initiative).
- Fidelity limit to carry into the design: a custom user agent on a normal browser engine (the suggested approach is Playwright with an iPhone profile plus the Facebook `FBAN/FBIOS` or Instagram user-agent suffix) does not reproduce the real in-app WebView (cookie and storage rules, native bridge). A pass is regression evidence, not proof. A periodic check on a real device inside the real app remains the source of truth.
- Test from the final landing URL with campaign parameters, not the ad click (Facebook's link redirect is out of scope). Run on staging only, because Join creates real member sessions.
- Capture current user-agent strings from real devices before writing the tests; version numbers change.
- AC set the first steps: scope the initiative, and source repeatable test data in staging. Roadmap reordered (IMP-18.1 scope and raise in Jira; IMP-18.2 repeatable staging data); user-agent capture and the test build follow. Still Later, so no Notion cards until promoted to Next.

## Roadmap

| ID       | Step                                                                                                                  | Owner | Depends on         | Status | Card |
|----------|-----------------------------------------------------------------------------------------------------------------------|-------|--------------------|--------|------|
| IMP-18.1 | Scope the initiative and raise it in Jira                                                                              | AC    | —                  | later  | —    |
| IMP-18.2 | Source repeatable test data in staging for the joiners a run creates, including Exerp clean-up                         | AC    | —                  | later  | —    |
| IMP-18.3 | Capture current Facebook and Instagram in-app user agents from real devices and agree the campaign landing URLs        | AC    | IMP-18.1           | later  | —    |
| IMP-18.4 | Add Facebook, Instagram and control browser projects to the front-end pack and run the Join journey to a joined member | AC    | IMP-18.2, IMP-18.3 | later  | —    |
| IMP-18.5 | Decide where it runs (each deploy or overnight) and how a failure alerts                                               | AC    | IMP-18.4           | later  | —    |
| IMP-18.6 | Agree a periodic real-device check inside the real apps                                                                | AC    | IMP-10.4           | later  | —    |

## Status & Next Action

**Status:** Not started — Later.

**Next action:** None until promoted. First steps when promoted: scope the initiative (IMP-18.1) and source repeatable staging test data (IMP-18.2), which can run in parallel.

## Outcome

- Completed: YYYY-MM-DD
- Result: [achievement link in achievements/ · team evidence link in team/<alias>.md · or "none"] — Capture asks and sets `outcome:` above
