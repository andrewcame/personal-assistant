---
id: DC-2026-09-15-head-of-software-engineering-gh
type: discovery-call
date: 2026-09-15
pillars: [P1, P4, P5, P9]
focus: [people, ownership, automation]
links: [CH-01, IMP-01]
people: [GL, GH, DJ, DA]
---

# 2026-09-15 - Head of Software Engineering - GH

## Call Context

- **Date:** 2026-09-15
- **Source / role:** GH, Head of Software Engineering (peer to me and DJ, both reporting to GL, Software Engineering Director)
- **Conversation type:** Stakeholder discovery
- **Related team or platform:** QA resourcing/reporting lines, environments, staging/app alerting, QA strategy, AI usage, Apps team Appium progress, growth framework/chapter
- **Notes based on:** Personal notes / discovery conversation

## Purpose

- Initial discovery conversation with the Head of Software Engineering to align on QA resourcing, environment ownership, QA testing strategy, and shared interest in AI-assisted testing, and to establish an ongoing working cadence between us.

## Outcome: New Weekly Cadence

- Agreed to meet weekly on Fridays going forward.
- Initially a 1-hour meeting, moving to 30 minutes once settled.
- A working agenda will be maintained in advance via Microsoft Teams Loop, rather than a static pre-meeting document.
- Cadences updated to reflect this — see [cadences.md](../../ways-of-working/cadences.md).

## Key Signals

### What Matters To Them

- Getting QA resourcing and reporting lines right — specifically where QA sit relative to the app/web teams.
- Making faster progress on Apps team test automation (Appium), including being open to using AI to help unblock it.
- A reusable, repo-based approach to capturing AI usage patterns so individual tester AI workflows become shared team capability.

### Current Friction Or Risks

- Apps team is not progressing well with Appium automation; this has been a recurring drag, hence the appetite to try an AI-assisted experiment.
- Web 3 QA involvement was discussed; expectations are being agreed with DA in his 1:1.
- No current candidate identified to run the QA Chapter — people are stretched and reasonably happy where they are, so this is being deliberately parked rather than forced.
- Environments remain a known, unresolved challenge needing deeper attention (consistent with prior discovery calls).

### What Is Working Well

- Alignment on QA strategy: focusing ticket-level testing at the initiative level, with a dedicated end-to-end test pass at the close of each initiative — consistent with the direction agreed in the DJ (Head of Delivery) conversation.
- Shared enthusiasm for AI-assisted testing, with a concrete near-term experiment agreed (see below) rather than just talk.
- General team health/sentiment was covered but surfaced nothing new beyond what's already been captured elsewhere.

### What They Asked For / Suggested

- Resourcing: leaning toward embedding a QA directly into the Apps team, with DA supporting the web teams as needed in his Lead capacity rather than a dedicated Web 3 QA being added immediately.
- Environments: flagged as needing a proper look, without a concrete plan yet.
- Improvement idea: set up end-to-end Exerp with IDs on previews, to reduce bleed into staging and improve the engineering experience — a candidate improvement to progress.
- Staging ownership: I proposed taking short-term ownership of staging monitoring in QA, and suggested expanding this to also cover app alerting (the beta app alerting environment), since it's part of the same ecosystem and isn't currently being watched by anyone. GH is also trying to identify the right signals to alert on for the app side.
- AI usage model (suggested in the call): capture any AI-assisted activity a tester does to make their job easier — requirements analysis, defect triage, ticket notes, etc. — as a reusable "skill" in the repo, so what one person builds becomes usable by the wider team.
- Appium AI experiment: for the next few weeks, extend the normally 30-minute weekly engineering meeting to a full hour, with the second half-hour dedicated to trying to get AI to generate Appium tests live on the call. GH asked me to send instructions in advance covering local Appium setup, connecting to a real device, and access to existing skills/READMEs, ahead of a live demo.
- Parked for the future (not urgent now): growth framework, engagement, resourcing, promotions, and QA Chapter — deliberately deferred rather than forced, given current capacity. Also flagged an internal touring/rotation idea for the team as a longer-term consideration.

## Themes And Interpretation

- Directly stated: QA strategy should centre on initiative-level testing with an end-to-end pass at initiative close — this is now consistent across both the DJ and GH conversations, reinforcing it as the agreed direction rather than a one-off suggestion.
- Directly stated: GH is supportive of expanding my staging ownership proposal to also include app alerting, since no one currently owns that signal either.
- Directly stated: the Apps team's Appium progress is a real concern for GH, enough to dedicate a live, hands-on AI experiment slot to it.
- My interpretation: the resourcing lean (embedded Apps QA, DA supporting web teams from his Lead capacity) is a reasonable starting position, but should be treated as a working hypothesis until tested against actual web/app workload data.
- My interpretation: the AI-skill-capture idea is a strong, low-cost knowledge-sharing mechanism — it converts individual AI usage into a discoverable, reusable team asset rather than one-off tricks.
- My interpretation: parking the QA Chapter and growth framework work isn't neglect — it's a deliberate sequencing choice given current team capacity, and should be revisited once nearer-term items (resourcing, environments, Appium) are less pressing.
- Hypotheses to validate: whether the Appium AI experiment can meaningfully unblock the Apps team's automation progress, or whether the underlying issue is more structural (per [Challenge 01 — Mobile Automation Strategy](../../challenges/01-mobile-automation-strategy.md)).

## Mapping

### Strategic Mission(s)

- Technical Mastery & Foundations
- People & Practice
- Delivery Flow & Resilience

### Role Pillar(s)

- Test Infrastructure, Environments & Data
- AI-Enabled Testing & Innovation
- Automation Trust & Reliability
- People Capability, Progression & Succession

### Objective Lens(es)

- Business Operator
- Value Creator
- People Developer

### Related 30/60/90 Focus Area(s)

- Ownership
- Automation
- People

## Follow-Ups

_Keep operational actions in Notion, Jira, or Teams. Record only strategic follow-up context here._

- **Set up weekly Friday sync with GH, with a Teams Loop working agenda** — Owner: AC — Destination: Cadences — Notes: Added to [cadences.md](../../ways-of-working/cadences.md); starts at 1 hour, moving to 30 minutes.
- **Progress the embedded Apps QA / DA-supports-web-teams resourcing model** — Owner: AC — Destination: Notion / Ways of Working — Notes: Treat as a working hypothesis; validate against actual workload before treating as settled.
- **Expand staging ownership proposal to include app/beta alerting** — Owner: AC — Destination: Notion / Improvement [01-staging-monitoring-and-alerting-ownership.md](../../improvements/01-staging-monitoring-and-alerting-ownership.md) — Notes: No one currently owns app alerting signals; GH is also looking at what the right signals should be.
- **Scope end-to-end Exerp with IDs on previews** — Owner: AC / Platform — Destination: Notion / Improvement — Notes: Aim to reduce preview bleed into staging and improve engineering experience.
- **Send GH/team instructions for local Appium setup ahead of the AI test-generation demo** — Owner: AC — Destination: Notion / Ways of Working — Notes: Cover local setup, real device connection, and access to existing skills/READMEs.
- **Run the Appium AI test-generation experiment in the extended weekly engineering meeting** — Owner: AC / Apps team — Destination: Challenge [01-mobile-automation-strategy.md](../../challenges/01-mobile-automation-strategy.md) — Notes: Meeting extended to 1 hour for a few weeks; second half-hour dedicated to a live AI-assisted Appium demo.
- **Capture reusable AI usage patterns as repo-based skills** — Owner: AC — Destination: Notion / Improvement — Notes: Any AI-assisted tester activity (requirements analysis, defect triage, ticket notes) becomes a documented, reusable skill.
- **Revisit growth framework, engagement, promotions, QA Chapter, and internal touring** — Owner: AC — Destination: Notion / Goals — Notes: Deliberately parked; no current candidate to run the QA Chapter, and capacity is stretched.

## Possible Outputs

- Candidate ways-of-working update: New weekly GH sync added to [cadences.md](../../ways-of-working/cadences.md).
- Candidate improvement: Expanded staging + app alerting ownership under QA.
- Candidate improvement: End-to-end Exerp with IDs on previews.
- Candidate improvement: AI-usage-as-reusable-skills capture model.
- Candidate challenge update: [01-mobile-automation-strategy.md](../../challenges/01-mobile-automation-strategy.md) — AI-assisted experiment as a new data point on the Appium approach.
- Candidate goal input: QA resourcing model (embedded Apps QA, DA supporting web teams).

## Open Questions

- What does "internal touring" mean in practice, and is it worth scoping now or fully parking until capacity frees up?
- What are the right alerting signals for the beta app environment, and who else needs to be involved in defining them?
- Will the embedded Apps QA / DA-supports-web-teams model hold up once tested against real workload data across the web teams?
- Is the Apps team's Appium friction better addressed by the AI experiment, or does it point to the deeper Maestro-vs-Appium tension already logged in Challenge 01?
