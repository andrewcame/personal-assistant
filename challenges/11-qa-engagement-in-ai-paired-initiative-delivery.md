---
id: CH-11
type: challenge
status: open
horizon: now
updated: 2026-10-23
pillars: [P3, P6, P9]
focus: [ownership]
jd: [JD-07, JD-13]
goals: []
links: [CH-10]
people: [GL, GH, DJ, JB]
---

# Challenge 11 — QA Engagement In Paired, AI-Assisted Initiative Delivery

---

## Context

Microsite sunset has become the precondition gating almost everything else in engineering. The CTO's consistent answer to resourcing, promotion, and growth conversations is "get off the microsites," which means progression and investment for the team sit behind that migration. At the same time, morale is visibly low — people posted openly in the all-hands chat about feeling demoralised, wanting better pay, and worrying about job security. The loop is self-reinforcing: the things that would lift morale are held behind the migration, and low morale makes the migration harder to deliver.

The leadership response (2026-09-30) is twofold. Technically, Pico gets an adapter to the legacy Business Gateway platform so the front end can move to 100% Pico Portal immediately, with Business Gateway continuing to own the business rules and update Exerp for services not yet migrated. Operationally, delivery moves away from granular, sequentially-tested tickets toward pairs of engineers taking larger initiatives end to end with AI assistance, including AI-drafted tests, with SMEs pulled in at the right moments.

The testing consequence of the technical change is straightforward and already accepted: a front-end-first strategy. QA asserts the Pico Portal journey and the resulting Exerp state, and is largely indifferent to whether the request routed directly through Pico or via the Business Gateway adapter. Backend test depth expands as services migrate off the adapter.

The testing consequence of the operational change is not straightforward, and is the real problem.

## Challenge

How does QA engage meaningfully in a two-engineer, AI-assisted initiative — where code and tests are being generated at pace across a large slice of work — without either becoming the bottleneck that the old sequential model was, or degrading into a rubber stamp on work QA never genuinely understood?

The approach needs to define:

- the points of QA engagement across an initiative, and what QA contributes at each
- what "ready for QA" means when the unit of work is a slice, not a ticket
- how QA reviews AI-drafted tests at a rate that keeps up with generation
- how QA feedback reaches the pair continuously rather than as a late batch of defects
- how we detect and prevent illusory coverage from AI-generated tests
- what evidence leadership needs to trust quality when QA is no longer gating each change

## Questions To Explore

### Engagement Timing And Shape

- At what point in a paired AI-led initiative does QA add most value — shaping, mid-build, at slice handover, or all three at different depths?
- What is the minimum QA presence that still allows risk framing to influence the build, without QA attending everything?
- Does QA sit with the pair as a third voice for parts of the initiative, or engage at defined checkpoints?
- What triggers an unscheduled QA pull-in — a risk threshold, a member-facing journey, a data/Exerp dependency?
- How does SME involvement interact with QA involvement? Are they the same conversation or separate?

### Slices, Readiness, And Handover

- What is the right size of slice to hand to QA so it is complete enough to test properly but small enough to give timely feedback?
- What does a Definition of Ready look like for a slice rather than a ticket?
- What scaffolding must the pair deliver alongside the slice — test data, environment state, feature flags, drafted automation — for QA to be effective immediately?
- How do we avoid the batch-at-the-end failure mode where several slices land on QA simultaneously?

### AI-Drafted Tests And Coverage Confidence

- How does QA review AI-generated tests efficiently — sampling, risk-weighted review, coverage diffing, or review of assertions only?
- What are the signature failure modes of AI-drafted tests here (asserting implementation not behaviour, happy-path bias, over-mocking, tautological assertions), and how do we detect them cheaply?
- Should QA own the test patterns, prompts, and guardrails the pairs use, so quality is shaped upstream rather than reviewed downstream?
- How do we measure whether coverage is real — mutation testing, defect escape rate, production signal — rather than counting tests?
- Where does the front-end-first strategy leave genuine gaps that need explicit, accepted risk rather than silent absence?

### Team, Capability, And Morale

- What capability shift does this require from the QA team — more risk analysis, review, and automation stewardship, less manual execution — and who is ready for it?
- Is this a credible growth narrative for the team given progression is currently gated behind microsite sunset?
- How do QAs stay close enough to the product to test well when they are not building the granular understanding ticket by ticket?
- How does this affect the E2E and platform-specific split across Mobile, Website, and Payments?

### Evidence And Leadership Trust

- What does QA report when it is no longer the gate on each change — confidence by journey, risk accepted, escaped defects?
- How do we show that acceleration has not come at the cost of member experience?
- What would make leadership comfortable enough with this model to extend it beyond the migration period?

## External Reference Points (2025–2026)

Full entries, stances, and sources are held in [context/industry-signals.md](../context/industry-signals.md) — the standing watch on external thinking. Summary as it applies to this challenge:

**Supports the direction**

- Humans should be **on the loop** (shaping the harness), not **in** it — inspecting output makes you the bottleneck. Morris, *Humans and Agents in Software Engineering Loops*, Mar 2026.
- Review effort should scale by **probability × impact × detectability**, not uniformly. Böckeler, *To vibe or not to vibe*, Sep 2025.
- **Mutation testing** catches "perpetually green" AI-drafted tests that coverage percentages hide. TW Radar Vol 34, Trial.
- Deterministic gates wired **into the agent session**, plus shared instruction files treated as a team asset. TW Radar Vol 34, Trial and Adopt.
- Browser-based component testing is now viable; temporal fakes are a recognised approach for external dependencies. TW Radar Vol 34, Trial and Assess.
- **Rework rate** is the early warning of unchecked AI delivery; throughput metrics are a trap. This changes what we report. DORA 2025 and TW Radar Vol 34.
- Coding assistants do not replace pair programming — supports the two-engineer shape. Thoughtworks, Exploring Gen AI.

**Challenges the direction**

- AI is an **amplifier** of existing organisational strengths and weaknesses, which makes environments and test data a precondition rather than a parallel initiative. DORA 2025.
- **Codebase cognitive debt** is a whole-team problem, not a QA one — reframes where the fix belongs. TW Radar Vol 34, Caution.
- Modern Testing principle 7: distributed quality capability "may reduce or eliminate the need for dedicated specialists." Arguably refutes the assumption that the answer is a redesigned QA gate. Page & Jensen.

**Unsettled**

- Whether AI-drafted tests genuinely improve quality is still being evaluated. Böckeler, *TDD inside the agent loop*, Aug 2026.

### Practices worth lifting directly

- **Probability × impact × detectability review scale** — QA triage model for how deeply to review each slice.
- **Mutation testing on core domain logic** — prove AI-drafted tests actually assert something.
- **Feedback sensors wired into the agent session** — move QA's gates upstream, pre-commit.
- **Curated shared instructions in service templates** — QA-owned test patterns distributed by default.
- **Rework rate and change failure rate** — leadership evidence that pace hasn't cost quality.
- **First-pass acceptance, iteration cycles, review burden** — team-level signal on how well the pairs and AI are collaborating.
- **Browser-based component testing** — cheaper front-end confidence below full E2E.

## Initial Position

### Practitioner Input - 2026-10-09

The [Dootrix AI harness call](../context/discovery-calls/2026-10-09-dootrix-ai-harness.md) supplied concrete practices to evaluate against this challenge: activity-based adversarial test review, switching model family between implementation and review, capturing repeated corrections as reusable guidance, and using deterministic scripts for repeatable checks. These are Dootrix's reported practices, not evidence that PureGym's coverage or readiness problem is solved.

The relevant learning is how QA expertise becomes a reusable engineering activity: JB cited Dootrix's QA architect creating an adversarial test-review skill rather than a QA persona. This supports the position that QA can shape how work is produced and reviewed, not just inspect it afterwards. Cross-model review adds another perspective, not proof of correctness; repeatable checks belong in scripts, and corrections can inform shared guidance without becoming authority to override an approved decision. The call is a learning reference for this challenge, not a new set of follow-up assignments.

Front-end-first testing during the migration is the right call and is already agreed — assert the Pico Portal journey and the Exerp outcome, expand backend coverage as services come off the adapter.

On engagement, my starting position is three touchpoints rather than continuous embedding: risk framing at kickoff, a lightweight mid-build review of the drafted tests, and full exploratory/hardening work at slice handover. The external material sharpens this into a clearer principle: **QA moves "on the loop" rather than "in the loop"** — our job becomes shaping the harness (test patterns, shared instructions, deterministic gates, risk framing) rather than inspecting output at generation speed. That is a fight QA does not win downstream.

How deeply we review any given slice should follow the probability × impact × detectability scale rather than a uniform standard, and coverage claims from AI-drafted tests should be proven with mutation testing on core domain logic rather than accepted on percentage.

Two things temper this. First, DORA's amplifier finding says the new model will magnify our existing weaknesses in environments and test data — so those foundations become a precondition, which is useful ammunition when sequencing work with GL. Second, Modern Testing principle 7 points at a future with fewer dedicated specialists; I would rather lead that conversation than have it arrive as a surprise for the team.

The unresolved part is slice sizing and the batching risk. That is where this most likely breaks first.

## 2026-10-16 Update — Ideas Triage

_From the Ideas triage on 2026-10-16 ([ideas log](../state/ideas-log.md))._

- **Right tests, not more tests:** add the correct automated tests rather than one for every case, with a periodic scope review to check we're testing the right thing.
- **Test the initiative, not the ticket:** a QA strategy for how to test work that focuses on the initiative; shift left, build skills, and use AI during development.
- **Dev testing:** are devs deploying previews and checking their code? Dev-QA (no QA on some tickets) is already happening under Kanban — measure its success. Ask devs what would speed up QA and what they can show us, then document it.
- **QA adds diagnosis:** if devs help us, we help devs by debugging more (with AI) rather than returning a ticket with "this failed".
- **Role shift:** the ability to write tests is no longer the differentiator — the value is analysis, asking questions and risk assessment. Work out how QA time splits between repetitive work (basic tests, manual testing) and high-judgement work (refinement, exploratory, edge cases, risk) to size the AI opportunity.
- **Empowerment:** can QA block releases? Visibility, and an opinion that matters (feeds the CI/CD quality gate item in Next).
- **AI options to explore:** suggest test scenarios and regression scope from a well-formed Jira ticket, again once the PR is known, possibly raising a PR of test changes to review (dev-friendly, so devs can spot a misunderstood implementation); expand a thin dev-written ticket once the implementation is known; "auto" manual regression.

## Roadmap

| ID | Step | Owner | Depends on | Status |
|----|------|-------|------------|--------|
| CH-11.1 | Raise QA engagement model at leadership call | AC | — | done |
| CH-11.2 | Take three-touchpoint model to the QA lead sync | AC | CH-11.7 | later |
| CH-11.3 | Argue environments and test data as precondition with GL | AC | CH-11.7 | later |
| CH-11.4 | Trial mutation testing on one core domain area | AC | — | later |
| CH-11.5 | Test slice sizing on the first AI-paired initiative | AC | CH-11.2, INI-02.4 | later |
| CH-11.6 | Agree QA engagement model for AI-paired delivery | AC | CH-11.4, CH-11.5 | later |
| CH-11.7 | Own discovery: read research brief, then talk to engineers and leads | AC | — | doing |
| CH-11.8 | Agree interim model: QA does one e2e ticket once coding is done, with input throughout (tentative) | AC | — | done |
| CH-11.9 | Automate the e2e ticket using dynamic Portal member creation | AC | CH-11.8 | later |

## Status & Next Action

- _2026-10-23:_ tentatively agreed that QA does one e2e ticket once coding is done, with input throughout while the team manages delivery. This should carry the sunset mission; the longer-term QA model still needs thinking (CH-11.6). Dynamic Portal member creation (INI-01) will make automating that ticket possible.
- _2026-10-15:_ research brief started: [QA in AI-paired delivery](../context/research/2026-10-15-qa-in-ai-paired-delivery.md).

_2026-10-15:_ AC wants to do his own discovery and research on QA in AI-paired delivery before taking a model to the lead sync (CH-11.7).

**Status:** Open — raised 2026-09-30 at the leadership call with GL, DJ, and GH. External reference points added 2026-09-30.
- **Next action:** Bring the three-touchpoint model and the probability/impact/detectability review scale to the QA lead sync for reaction, and test the slice-sizing question against the first initiative run this way.
- **Next action:** Trial mutation testing on one core domain area to get a real signal on AI-drafted test quality before the model scales.
- **Next action:** Use the DORA amplifier finding to argue environments and test data as a precondition for the new delivery model in the next 1:1 with GL.
- **Related:** [Leadership direction 2026-09-30](../context/leadership-direction.md) · [QA operating model](../ways-of-working/qa-team-operating-model.md#qa-engagement-in-paired-ai-assisted-initiative-delivery) · [Challenge 10 — Pico source of truth](10-pico-source-of-truth-and-exerp-dependent-test-strategy.md)
