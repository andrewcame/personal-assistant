---
id: DC-2026-11-04-platform-technical-lead
type: discovery-call
date: 2026-11-04
pillars: [P4, P5, P6, P7, P9, P10]
focus: [automation, productivity, ownership]
links: [IMP-04, IMP-11, IMP-14, IMP-10, IMP-03, IMP-05, CH-10]
people: [AE]
---

# 2026-11-04 - Platform Technical Lead (staging value, reporting, backend tests)

## Call Context

- **Date:** 2026-11-04 (Wednesday)
- **Source / role:** Platform Technical Lead (AE), PDEX
- **Conversation type:** Engineering discovery
- **Related team or platform:** Platform / PDEX, Report Portal, staging and prod, backend test coverage, BrowserStack, Cloudflare AI
- **Notes based on:** Dictation (AC)

## Purpose

- Follow-up to the 2026-09-01 conversation with the Platform Staff Engineer ([2026-09-01 Staff Engineer DevEx](2026-09-01-staff-engineer-devex.md)), giving two members of the Platform team on record.
- Continue the in-person conversation held when the awards were written, about what QA could do through PDEX to support QA work.

## Key Signals

### What Matters To Them

- Staging should carry real value as a proving ground. Testing in prod is good practice and robust mechanisms matter, but the business does not want things going wrong in prod, so staging has to catch issues.
- Helping where Platform can unblock QA: technical help on staging backend tests, and open to solving problems as QA meets them.

### Current Friction Or Risks

- Device testing (BrowserStack) is painful for external web views: they sit behind a login that needs Cloudflare access, which is not installed on the BrowserStack devices.
- Backend test coverage in staging is thin, so staging finds less than it could.
- Any hold or gate in the delivery path has to be balanced against what the business and developers need; delivery should not slow down.

### What Is Working Well

- AC has been granted access to a new, empty Report Portal instance rather than migrating the old one (see below).
- The existing front-end test repo already has Report Portal wired in, so there is a working example.
- Platform is open to whitelisting and to helping with staging limitations on request.
- Cloudflare AI is available to AC at no extra tooling cost (paid for with credits).

### What They Asked For / Offered

- **Report Portal:** a fresh portal, AC the only user so far, with no data. AC builds from scratch: add the plugin to the chosen test codebase, add credentials (API key and URL), then populate it, build dashboards and reports.
- **Staging value:** agreed with AC that staging should have more value. AE can support a **soak period**: after a developer merges, the change deploys to staging, is held there for a set time (for example an hour) while a large set of tests runs and monitoring watches it, then it is promoted to prod. Mechanisms exist to hold a change from going further.
- **Backend tests:** AE will help from a technical point of view. If backend tests do not work in staging because of a limitation, AE is always open to talk about sorting it.
- **BrowserStack:** AE offered to whitelist. If QA supplies the IP addresses, Platform can whitelist them so external web views are reachable without installing the Cloudflare client.
- **Cloudflare AI:** gave AC access to Cloudflare's AI service (free agent tooling that AC can build and share applications in). It has built-in controls so requests are not over-used, which keeps credit use down. AE has strong views on AI in general.

## Themes And Interpretation

- Directly stated: Staging should matter more; the business does not want issues in prod; staging tests must catch them.
- Directly stated: Priority for AC is decent backend test coverage, which makes staging more valuable and helps catch problems before they fail in prod.
- Directly stated: Layering is the answer: prod testing matters, staging testing matters, and tests are tagged so some run in staging, some in prod. Overnight and always-on test runs, and load testing, are the direction.
- Directly stated: Report Portal decision point is whether to extend the existing front-end repo or start somewhere fresh (Appium, or another repo nobody else touches). A separate repo is attractive because it is useful without affecting anyone.
- My interpretation: A staging soak is the first concrete model for "staging as a gate", to be balanced against delivery speed and what developers need. It belongs with the CI/CD quality gate model rather than as a separate decision.
- My interpretation: Platform is now an open route for environment and tooling blockers, which supports the staging and backend work.
- Hypotheses to validate: A soak window long enough to be useful but short enough to leave delivery speed untouched exists; the backend packs can run in staging reliably once the coverage is there.
- Hypotheses to validate: Whitelisting is enough to unblock external web views on BrowserStack.

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
- AI-Enabled Testing & Innovation
- Stakeholder Confidence & Visibility

### Objective Lens(es)

- Value Creator
- Business Operator

### Related Focus Area(s) (People / Ownership / Automation / Productivity)

- Automation
- Productivity
- Ownership

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Wire the new Report Portal into a test codebase and build dashboards** — Owner: AC — Destination: IMP-04 QA metrics (IMP-04.11, IMP-04.12) — Notes: Decide between the existing front-end repo and a fresh Appium or untouched repo; needs time.
- **Staging soak before prod** — Owner: AC with AE — Destination: IMP-14 CI/CD gate (IMP-14.2) — Notes: Balance against delivery speed and developer needs.
- **Backend tests in staging** — Owner: AC, TMW, JFG with AE support — Destination: IMP-11 Backend tests — Notes: Coverage first; AE helps with staging limitations.
- **Whitelist BrowserStack IPs for external web views** — Owner: AC to get the IPs, AE to whitelist — Destination: IMP-10 BrowserStack (IMP-10.8) — Notes: Removes the Cloudflare login blocker on devices.
- **Trial Cloudflare AI** — Owner: AC — Destination: IMP-05 Assistant (IMP-05.10) — Notes: Possible input for the AI chapter; AC will experiment and share with others.

## Possible Outputs

- Candidate decision: Staging soak (hold after merge, then promote) as part of the quality gate model.
- Candidate decision: Where Report Portal is wired first.
- Candidate achievement evidence: Relationship-building across the Platform team (Staff Engineer and Technical Lead) opening routes to unblock QA work.
