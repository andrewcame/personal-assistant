# Industry Signals

A standing watch on external industry thinking — research, standards, practice frameworks, and credible practitioner writing — used to pressure-test where QA and Test Engineering is heading here.

This exists because strong opinions formed over years in the industry are an asset right up until the ground moves. The purpose of this file is to keep a wider eye open, notice when external thinking **supports**, **challenges**, or **refutes** the current position, and re-evaluate deliberately rather than drifting or digging in.

Internal signals from director level and above belong in [leadership-direction.md](leadership-direction.md), not here. This file is for *external* thinking and what it means for our plans — including my own reaction to it, where that reaction is worth keeping.

## How To Add An Entry

- **Date** — when it was captured
- **Source** — what it is, who produced it, and when it was published
- **Signal** — what it actually says, close to the original
- **Stance** — Supports / Challenges / Refutes / Unsettled, relative to our current position
- **My take** — personal reaction, where there is one worth keeping; optional
- **So what** — what changes, what we should watch, or why we're consciously not acting
- **Follow-ups** — only where they are not already tracked as an improvement, challenge, or goal

Mark stance honestly. An entry that only ever says "supports" is confirmation bias with citations.

## Standing Re-evaluation Questions

Revisit these roughly quarterly, or whenever a significant signal lands:

- Is the current QA position still the best answer, or just the most familiar one?
- What would have to be true for the opposite approach to be right?
- Which of my strongly held views are based on evidence that has since moved?
- Where is external thinking ahead of us, and is that a gap worth closing or noise worth ignoring?
- Where are we ahead of external thinking, and can we evidence that rather than assume it?
- Does this change what the QA role *is*, or only how it operates?

---

## Active Themes

Each theme carries the current position, how confident I am in it, and when it was last reviewed.

- **QA engagement in AI-assisted delivery** — QA moves "on the loop": shape the harness, don't inspect output. Confidence: medium, untested here. Reviewed 2026-09-30.
- **Coverage confidence from AI-drafted tests** — coverage percentage is not evidence; mutation testing is the honest signal. Confidence: medium-high, well supported externally. Reviewed 2026-09-30.
- **Front-end-first testing during migration** — correct for this period; backend depth follows migration. Confidence: high. Reviewed 2026-09-30.
- **Future of the dedicated QA specialist** — unresolved; industry direction points to distributed quality capability. Confidence: low. Reviewed 2026-09-30.
- **Environments and test data as foundation** — a precondition, not a parallel nice-to-have. Confidence: high, reinforced by DORA. Reviewed 2026-09-30.
- **Junior QA talent pipeline under AI** — the apprenticeship tasks that taught coverage thinking are being absorbed by AI; no replacement learning vehicle defined. Confidence: medium-high on the risk, low on the answer. Reviewed 2026-09-30.
- **Accessibility standard baseline** — role docs and the JD reference WCAG 2.1 AA; the current W3C recommendation is 2.2 and EU market obligations have tightened. Confidence: low, needs checking. Reviewed 2026-09-30.

---

## Entries

### 2026-09-30 — Accessibility baseline may have drifted behind the standard

- **Date** — 2026-09-30 (raised during repo review)
- **Source** — W3C [WCAG 2.2](https://www.w3.org/TR/WCAG22/), a W3C Recommendation since October 2023, superseding 2.1. Separately, the EU [European Accessibility Act](https://ec.europa.eu/social/main.jsp?catId=1202) (Directive 2019/882) has applied to in-scope consumer digital services since 28 June 2025.
- **Signal** — WCAG 2.2 adds success criteria around focus appearance, dragging movements, target size, consistent help, and reducing cognitive load in authentication. The EAA places legal obligations on consumer-facing digital services in EU markets rather than leaving accessibility as a voluntary standard.
- **Stance** — **Challenges**, pending verification. Our [job specification](my-role/job-specification.md), [role pillars](role-pillars.md), and both the [Lead](team-roles/lead-qa-engineer.md) and [Staff](team-roles/staff-qa-engineer.md) QA role definitions all reference **WCAG 2.1 AA**. That may be a deliberate, agreed baseline, or it may be drift.
- **So what** — Worth a direct check rather than an assumption, especially given the expansion-into-new-markets direction from the C-suite: which markets we operate in, what the legal obligation actually is in each, and whether 2.1 AA is a conscious decision or an inherited number. If it is drift, it is a cheap, credible thing for QA to surface. Confidence in my own reading here is low until checked with the Head of Software Engineering.

### 2026-07-08 — AI is sorting the workforce, not just speeding it up

- **Date** — Captured 2026-07-08, re-read 2026-09-30
- **Source** — 2026 workforce/AI report, "Where do we go from here?" (source loosely identified in the original capture — worth pinning down before citing externally)
- **Signal** — The 2026 workforce is more burned out and less optimistic than a year before, splitting along an AI fault line into those thriving, those struggling, and a large ambivalent middle caught between. Tech workers are largely afraid of being squeezed by rising productivity expectations, privately convinced the field is no longer worth recommending to newcomers, while individually still finding real power and even joy in the tools.
- **Signal (for individuals)** — Find two or three tasks where AI measurably changes your output and go deep rather than broad. Watch for the silent squeeze: absorbing a higher bar for the same pay until you burn out. Manager quality is the single biggest lever on job enjoyment, around a 65% improvement. Smaller companies and more autonomy correlate with higher wellbeing year on year. For early-career people the rungs are disappearing, so team choice matters.
- **Signal (for leaders)** — Invest in managers; only 25% are rated highly effective and nothing else moves burnout or retention as much. Be visible about what you do with productivity gains rather than silently raising the bar. Be deliberate about early-career development when AI is doing the entry-level learning tasks. Design and research roles show the worst sentiment and highest AI anxiety — treat that as a retention signal. Treat AI adoption as a sorting risk: the same tool lifts one group and destabilises another.
- **Stance** — **Challenges**, and has become more relevant since capture.
- **My take** — The company suffers from a lot of noise: people constantly sharing "hey I did this with AI" or "what about this agent", very pie in the sky. That is the destabilised, ambivalent middle in action. The answer isn't to do more, it's to do fewer things well. The approach that feels right is to pick a small number of high-value AI experiments, find internal champions who can help prove them out, then measure the outcome. That is how you move from noise to signal, and it's the kind of deliberate approach that distinguishes a lead from a follower. The junior pipeline risk is particularly relevant for a QA and Test Engineering team: if AI is generating test cases, the apprenticeship tasks that taught juniors *how to think about coverage* are disappearing. That is next year's senior talent pipeline being quietly starved.
- **So what** — Two things have moved since July. First, the morale picture it describes is now visible here directly, in the all-hands chat comments about pay and job security ([leadership direction, 2026-09-30](leadership-direction.md)). Second, the "silent squeeze" warning lands squarely on the new paired AI delivery model: if the team delivers faster and nothing visible changes for them, that is the failure mode. Being explicit about where the gains go is a leadership action, not a comms nicety. The junior pipeline point connects to [Challenge 11](../challenges/11-qa-engagement-in-ai-paired-initiative-delivery.md) — if AI drafts the tests, the apprenticeship task that taught QAs coverage thinking disappears and nothing has replaced it.
- **Follow-ups** — Pick two or three AI leverage points for the team (candidates: test case generation, coverage gap analysis, defect triage summarisation) and run them as small experiments with clear success measures before rolling out broadly. Find champions rather than broadcasters — one or two people genuinely energised by the tools — and pair experiments with them instead of team-wide pushes. Define the junior development path explicitly rather than leaving it undefined. Use 1:1s to read who is amplified and who is struggling, without announcements. Be visible about where productivity gains go. Check own burnout: new manager role plus AI transition is elevated load, worth revisiting at the midyear checkpoint.

### 2026-09-30 — Humans "on the loop" rather than "in the loop"

- **Date** — 2026-09-30
- **Source** — Kief Morris, [Humans and Agents in Software Engineering Loops](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html), Thoughtworks / martinfowler.com, March 2026
- **Signal** — Three postures are possible: *outside the loop* (vibe coding), *in the loop* (inspecting each artefact), and *on the loop* (shaping the harness — specs, quality checks, workflow guidance — that produces the artefacts). Insisting on close involvement makes the human a bottleneck, because agents generate faster than humans can inspect. The fix is framed explicitly as classic shift-left thinking applied to agents: the same move that replaced "developers code, QA finds the bugs."
- **Stance** — **Supports**, and sharpens. It reframes the QA question from *when do we engage* to *what layer do we operate at*.
- **So what** — Adopted as the framing principle in the [QA operating model](../ways-of-working/qa-team-operating-model.md#qa-engagement-in-paired-ai-assisted-initiative-delivery). Watch whether "on the loop" holds for member-critical journeys, or whether some journeys genuinely still need a human in the loop.

### 2026-09-30 — Risk-based review effort: probability × impact × detectability

- **Date** — 2026-09-30
- **Source** — Birgitta Böckeler, [To vibe or not to vibe](https://martinfowler.com/articles/exploring-gen-ai/to-vibe-or-not-vibe.html), Thoughtworks / martinfowler.com, September 2025
- **Signal** — How much to review AI output depends on three dimensions: **probability** it gets things wrong (model, tool, stack familiarity, context quality, codebase cleanliness), **impact** if it's wrong and unnoticed (business criticality, blast radius — "would you ship this if you were on call tonight?"), and **detectability** (tests, typing, monitoring, personal familiarity). These combine into a sliding scale of review effort rather than a binary.
- **Stance** — **Supports**. Gives a defensible, teachable structure to something QA has always done by instinct.
- **So what** — Adopted as the QA triage model. Most transferable idea found so far — it can be taught to the whole team, not just QA, which matters given the direction of travel.

### 2026-09-30 — Mutation testing as the honest coverage signal

- **Date** — 2026-09-30
- **Source** — Thoughtworks Technology Radar Vol 34, April 2026 — **Mutation testing** (Trial)
- **Signal** — Moved to Trial specifically because of AI-assisted development. High coverage percentages can mask "logically hollow tests" and "perpetually green" tests that pass regardless of logic changes due to missing assertions or decoupled mocks. Mutation testing shifts the question from how much code is executed to how much is actually verified. Tools: Stryker, Pitest, cargo-mutants.
- **Stance** — **Supports**. Names a risk we had identified and supplies a concrete mitigation.
- **So what** — Trial on one core domain area before the AI-paired delivery model scales, so we have a real baseline rather than an opinion.

### 2026-09-30 — Quality gates belong inside the agent loop

- **Date** — 2026-09-30
- **Source** — Thoughtworks Technology Radar Vol 34, April 2026 — **Feedback sensors for coding agents** (Trial) and **Curated shared instructions for software teams** (Adopt)
- **Signal** — Wire deterministic gates (linters, structural tests, suites) into agentic workflows so failures trigger self-correction *during* the session, before commit — explicitly framed as reducing load on human reviewers. Separately, relying on individuals to write their own prompts is called an anti-pattern; shared instruction files should be treated as a collaborative engineering asset and distributed through service templates.
- **Stance** — **Supports**. This is the concrete shape of "QA owns the guardrails upstream."
- **So what** — Argues for QA authoring test patterns and instruction files that ship by default with every service, rather than reviewing output after the fact. Practical, low-cost, and a credible growth area for the QA team.

### 2026-09-30 — AI amplifies existing organisational strengths and weaknesses

- **Date** — 2026-09-30
- **Source** — [DORA 2025 State of AI-assisted Software Development](https://dora.dev/research/2025/dora-report/), Google Cloud, plus the companion [DORA AI Capabilities Model](https://dora.dev/ai/capabilities-model/report/)
- **Signal** — AI's primary role is as an *amplifier*: it magnifies whatever the organisation already is. The greatest returns come not from the tools but from a strategic focus on the underlying organisational system.
- **Stance** — **Challenges**. It undercuts any assumption that pairing plus AI will itself deliver acceleration.
- **So what** — If test data, environments, and feedback loops are weak, the new delivery model magnifies that weakness. This turns the environments and test-data work from a parallel strategic initiative into a **precondition** — useful and evidenced leverage when sequencing work with GL. Links to [Challenge 10](../challenges/10-pico-source-of-truth-and-exerp-dependent-test-strategy.md) and [Improvement 02](../improvements/02-dynamic-member-creation-and-test-data.md).

### 2026-09-30 — Rework rate as the early warning of unchecked AI delivery

- **Date** — 2026-09-30
- **Source** — Thoughtworks Technology Radar Vol 34, April 2026 — **DORA metrics** (Adopt), **Coding throughput as a measure of productivity** (Caution), **Measuring collaboration quality with coding agents** (Assess)
- **Signal** — DORA now includes a fifth metric, **rework rate** — how much of the pipeline is consumed by unplanned rework on work previously considered complete. Degradation in it is named as the early warning sign of blind spots and unchecked AI-assisted development. Measuring productivity by lines generated or PR count is placed at Caution: it floods review, extends cycle time, and shapes bad behaviour. Better leading indicators include first-pass acceptance rate, iteration cycles per task, post-merge rework, and review burden — tracked at team, not individual, level.
- **Stance** — **Supports**, and gives QA a stronger evidence story than test counts.
- **So what** — This is what goes to leadership instead of coverage percentages. It also gives an honest answer to "has acceleration cost us quality?" that isn't defensive.

### 2026-09-30 — Codebase cognitive debt

- **Date** — 2026-09-30
- **Source** — Thoughtworks Technology Radar Vol 34, April 2026 — **Codebase cognitive debt** (Caution), citing Margaret-Anne Storey
- **Signal** — The growing gap between a system's implementation and the team's shared understanding of how and why it works. As AI raises change velocity, teams lose track of design intent and hidden coupling. Weaker understanding then reduces the ability to steer AI effectively, creating a reinforcing loop. Left unmanaged, small changes trigger unexpected failures and fixes introduce regressions.
- **Stance** — **Challenges**, by reframing. My concern about QA losing sight of the product is a specific instance of a whole-team problem.
- **So what** — This is not solved by QA testing harder. It needs team-level countermeasures — feedback sensors, tracking team cognitive load, architectural fitness functions. Worth raising as an engineering concern rather than a QA one, which is a better positioning for the role anyway.

### 2026-09-30 — Modern Testing: the uncomfortable end state

- **Date** — 2026-09-30
- **Source** — [Modern Testing Principles](https://www.moderntesting.org/) (Alan Page & Brent Jensen), including the MT 2.0 revision
- **Signal** — Mission: "accelerate the achievement of shippable quality." Priorities include improving the business, using Lean Thinking and Theory of Constraints to identify and remove bottlenecks *from the system*, and being "a force for continuous improvement... rather than using safety nets to catch our failures." Principle 7: expand testing ability and knowhow across the team, "understanding that this may reduce (or eliminate) the need for dedicated specialists."
- **Stance** — **Challenges** — arguably **refutes** the assumption that the answer is a redesigned QA gate.
- **So what** — The logical end of the direction leadership is pushing is fewer dedicated QA gates, not a better one. Two honest responses: lead that conversation rather than let it arrive as a surprise, and position the team's value in the capabilities that don't distribute easily — risk framing, harness ownership, member-experience judgment, and evidence for decisions. Directly relevant to the progression and morale problem, since it changes what "growth" looks like for the team.

### 2026-09-30 — AI-written tests: value not yet settled

- **Date** — 2026-09-30
- **Source** — Birgitta Böckeler, [TDD inside the agent loop — theater or actual value?](https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html), August 2026
- **Signal** — An informal evaluation of whether prompting a coding agent to follow TDD inside its own loop actually improves resulting code and test quality versus no TDD instruction at all.
- **Stance** — **Unsettled**.
- **So what** — That the question is being asked seriously is itself the caution: do not assume AI-drafted tests are a free good. Pair with mutation testing to get local evidence rather than importing a conclusion.

### 2026-09-30 — Supporting techniques worth tracking

- **Date** — 2026-09-30
- **Source** — Thoughtworks Technology Radar Vol 34, April 2026
- **Signal** — **Browser-based component testing** (Trial) reverses earlier Radar advice: real-browser component tests via Playwright are now viable and often preferable to emulated environments such as jsdom, with acceptable performance and reduced flakiness. **Temporal fakes** (Assess) describes stateful simulators of external dependencies that model temporal evolution rather than static request/response pairs — with the caution that fakes drifting from real behaviour create false confidence in pipelines. **Coding assistants do not replace pair programming** remains the position on pairing.
- **Stance** — **Supports**.
- **So what** — Browser-based component testing makes the front-end-first strategy cheaper to execute below full E2E. Temporal fakes are directly relevant to Business Gateway and Exerp — with the fidelity caution applying squarely to us. The pairing point supports the two-engineer-plus-AI shape leadership proposed rather than solo-engineer-plus-agent.
