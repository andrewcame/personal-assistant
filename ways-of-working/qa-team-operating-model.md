# QA/Test Engineering Operating Model

This page captures how the QA/Test Engineering team communicates, aligns, learns, and improves.

## Purpose

- Define a clear operating rhythm for the QA function.
- Keep team communication intentional rather than meeting-heavy.
- Support consistency across Mobile App, Website, Payments, and cross-platform E2E work.
- Make sure the team has useful forums for health checks, technical deep dives, chapter practice, and lead alignment.

## Current Understanding

_To populate after QA health checks and team deep dives._

For the initial Lead QA conversations, use [the QA lead call agendas](qa-lead-call-agendas.md). Capture individual durable context in [team profiles](../team/README.md) and aggregate findings in the [QA Health Summary](../context/qa-health-summary.md). These are listening conversations focused on people, team health, friction, direction, and support rather than formal goal setting or technical deep dives.

## Core Operating Principles

- Use team forums to create clarity, not to repeat status.
- Keep tactical delivery actions in the owning systems.
- Make quality risks visible early.
- Keep a wider eye on external industry thinking and re-evaluate the QA position against it deliberately — see [industry signals](../context/industry-signals.md). Experience is an asset; treating it as settled is not.
- Share knowledge across domains so each platform is not isolated.
- Use evidence where possible: automation runs, environment health, data issues, defect trends, and release outcomes.
- Keep the QA leads aligned on standards, coaching approach, and technical direction.
- Build direct relationships with business stakeholders around critical journeys and quality confidence, while keeping Product ownership gaps visible rather than silently absorbing them into QA.
- Contribute early to engineering design discussions when decisions affect testability, observability, resilience, accessibility, security, or member impact.
- **Evolving Testing Models for Pace:** Move pragmatically between continuous incremental testing and "feature-ready / batch testing" where high-velocity migration demands it (e.g., grouping backend changes first, testing when constituent parts are assembled), backed by explicit leadership risk acceptance and deterministic automated regression.

## QA Engagement In Paired, AI-Assisted Initiative Delivery

_Added 2026-09-30 following the leadership call on microsite sunset (see [leadership direction](../context/leadership-direction.md)). Practices below are grounded in [industry signals](../context/industry-signals.md) and should be re-evaluated as that watch list moves._

Delivery is moving away from granular, sequential tickets — where each small change was individually built, tested, QA'd and deployed — toward pairs of engineers taking larger initiatives end to end with AI assistance, including AI-drafted tests, with SMEs pulled in at the right points. The work arrives at QA more complete and with test scaffolding already in place; QA's job becomes verifying, tweaking, and expanding rather than starting from zero.

### What This Changes For QA

- QA is no longer the gate at the end of every small change. Sequencing QA per-ticket is what slowed the old model down.
- The unit of QA engagement becomes the **initiative or a meaningful slice of it**, not the individual ticket.
- Much of the first-pass automation is authored by the pair (with AI), so QA's value shifts toward risk framing up front and critical review of coverage afterwards.
- Front-end-first strategy applies during migration: assert the Pico Portal journey and the resulting Exerp state; treat the Business Gateway adapter as an implementation detail.

### Working Model (Current Position)

QA's centre of gravity moves **"on the loop" rather than "in the loop"** — shaping the harness that produces the work (test patterns, shared instructions, deterministic gates, risk framing) rather than inspecting output at generation speed. Inspecting every artefact makes QA the bottleneck, because agents generate faster than people can review.

- **Shaping / kickoff** — QA joins the pair's kickoff to frame risk, member impact, and what "done and safe" looks like. Output: agreed risk areas and the checks that must exist.
- **Mid-build checkpoint** — lightweight review of the AI-drafted tests as they appear: are they asserting the right things, at the right level? Output: early correction before coverage hardens in the wrong shape.
- **Slice handover** — QA takes a working, scaffolded slice for exploratory testing, edge cases, and hardening of the drafted automation. Output: verified slice and strengthened automation.
- **Close** — confirm the regression suite reflects the new behaviour and feed gaps back into the pair's AI prompting patterns. Output: durable coverage and a better next initiative.

### How Much To Review: Risk-Based, Not Uniform

Review depth follows three dimensions rather than a flat standard (after Böckeler, [To vibe or not to vibe](https://martinfowler.com/articles/exploring-gen-ai/to-vibe-or-not-vibe.html)):

- **Probability** — how likely is the AI to get this wrong? (unfamiliar stack, thin context, messy existing code all raise it)
- **Impact** — what happens if it is wrong and nobody notices? (member-facing join/pay/access journeys sit at the top)
- **Detectability** — will we notice? (existing tests, typing, monitoring, familiarity with the area)

Low probability + low impact + high detectability needs little QA attention. High probability + high impact + low detectability gets full scrutiny. Most work sits between, and the point is to place it deliberately rather than treat everything the same.

### Countermeasures Against Illusory Coverage

- **Mutation testing** on core domain logic to prove AI-drafted tests actually assert behaviour — high coverage can mask "perpetually green" tests with missing assertions or decoupled mocks.
- **QA-owned test patterns and shared instruction files** distributed through service templates, so guardrails are applied by default rather than reviewed after the fact.
- **Deterministic quality gates wired into the agent session** (lint, structural tests, suites) so failures self-correct before commit rather than landing on a reviewer.
- **Fidelity checks on fakes** for Business Gateway and Exerp — a fake that drifts from real behaviour produces confident, wrong results.

### Evidence For Leadership

Report flow and stability, not activity. **Rework rate** (unplanned rework on work previously considered complete) and **change failure rate** are the early warning signs of unchecked AI-assisted delivery. Test counts and coverage percentages are not evidence. Team-level signals on how well the pairs and AI are working together — first-pass acceptance, iteration cycles per task, review burden — sit alongside these.

### Open Questions

These are deliberately unresolved and tracked in [Challenge 11](../challenges/11-qa-engagement-in-ai-paired-initiative-delivery.md):

- When exactly does QA engage in a two-engineer AI-led initiative without becoming a bottleneck or a rubber stamp?
- How does QA keep sight of what's been built when the volume of AI-generated code and tests outpaces review capacity?
- How do we keep QA feedback flowing into the pair continuously rather than arriving as a late batch of defects?
- What does "ready for QA" mean when a slice is larger than a ticket but smaller than an initiative?
- How do we avoid AI-drafted tests creating the illusion of coverage?
- Does the environments and test-data foundation need to land *before* this model scales? (DORA's finding that AI amplifies existing organisational weaknesses suggests yes.)
- Where does this leave dedicated QA specialists long term, given the industry direction is toward quality capability spread across the team?

## QA Rhythm

### QA Lead Alignment
- **Current / planned forum:** QA Lead Sync (fortnightly).
- **Purpose:** Shared priorities, people context, risks, standards.
- **Output:** Actions log reviewed and driven each session; themes into team profiles and QA Health Summary.

### Full QA Team Communication
- **Current / planned forum:** Not yet defined.
- **Purpose:** Team-wide context, engagement, shared direction.
- **Output:** Not yet defined.

### Testing Chapter / Practice
- **Current / planned forum:** Not yet defined.
- **Purpose:** Knowledge sharing and quality practice across engineering.
- **Output:** Not yet defined.

### Technical Deep Dives
- **Current / planned forum:** Not yet defined.
- **Purpose:** Platform-specific learning and problem solving.
- **Output:** Not yet defined.

### Automation Health Review
- **Current / planned forum:** Not yet defined.
- **Purpose:** Trust, coverage, failures, flaky tests, reporting.
- **Output:** Not yet defined.

### Environment And Data Health
- **Current / planned forum:** Not yet defined.
- **Purpose:** Test data, staging, previews, Exerp/Pico drift.
- **Output:** Not yet defined.

### People Development
- **Current / planned forum:** Not yet defined.
- **Purpose:** Growth framework, progression, coaching, support.
- **Output:** Not yet defined.

## Information To Present

- What has changed that affects QA.
- Where confidence is strong or weak.
- What is blocked by environment, data, tooling, or process.
- Which quality risks need engineering or business visibility.
- Which learning, documentation, or chapter topics would help the team.
- Which business stakeholders need direct involvement in shaping or validating critical journeys.
- Which technical decisions need shared discussion in the Tech Lead Chapter rather than local resolution.

## Questions To Keep Asking

- Is this forum creating a decision, shared understanding, or useful visibility?
- Who needs to be in the room, and who only needs the output?
- What should be captured here versus in Notion, Jira, Teams, a challenge, or a decision?
- Are we improving flow and confidence, or just adding communication overhead?
