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

Each theme carries the current position, how confident I am in it, the stance mix of the entries behind it, and when it was last reviewed. Reviewed 2026-10-14 unless noted.

- **QA engagement in AI-assisted delivery** — QA moves "on the loop": shape the harness and gates, don't inspect each output; scale review effort by probability × impact × detectability. Confidence: medium, untested here. Stance mix: 3 Supports (on the loop; risk-based review; gates inside the agent loop). Entries: 2026-09-30.
- **Coverage confidence from AI-drafted tests** — coverage percentage is not evidence; mutation testing is the honest signal, and the value of AI-written tests is not settled. Red/green TDD is the cheap instruction that makes agents test properly, but suite size is a live disagreement: one practitioner now tolerates very verbose suites because agents maintain them. Confidence: medium-high, well supported externally. Stance mix: 1 Supports (mutation testing), 1 Unsettled (TDD in the agent loop), 1 Supports and 1 Challenges (2026-11-02). Entries: 2026-09-30, 2026-11-02.
- **Measuring quality under acceleration** — rework rate and team-level leading indicators, not test counts or throughput, answer "has acceleration cost us quality?". Confidence: medium-high. Stance mix: 1 Supports. Entries: 2026-09-30.
- **Front-end-first testing during migration** — correct for this period; backend depth follows migration; browser-based component tests make it cheaper, temporal fakes need a fidelity check. Confidence: high. Stance mix: 1 Supports (supporting techniques). Entries: 2026-09-30.
- **Environments and test data as foundation** — a precondition, not a parallel nice-to-have, because AI amplifies existing weaknesses. Confidence: high, reinforced by DORA. Stance mix: 1 Challenges (to the assumption that pairing plus AI alone accelerates). Entries: 2026-09-30.
- **Shared understanding of the system** — codebase cognitive debt is a whole-team problem needing team-level countermeasures, not harder QA testing. Confidence: medium. Stance mix: 1 Challenges. Entries: 2026-09-30.
- **Future of the dedicated QA specialist** — unresolved; Modern Testing points to distributed quality capability and fewer dedicated gates, while 2026 evidence says the verify-and-be-accountable layer stays human and the exposed work is execution-only testing. Confidence: low. Stance mix: 1 Challenges (arguably refutes), 1 Supports (qualified), 1 Unsettled. Entries: 2026-09-30, 2026-11-02.
- **Junior QA talent pipeline and morale under AI** — the apprenticeship tasks that taught coverage thinking are being absorbed by AI; no replacement learning vehicle defined; be visible about where productivity gains go. New and contested: one 2026 account says new starters onboard faster with AI and the mid-career group is the one at risk, which cuts against the apprenticeship worry. Confidence: medium-high on the risk, low on the answer. Stance mix: 1 Challenges, 1 Unsettled. Entries: 2026-07-08, re-read 2026-09-30 ([archived](archive/industry-signals-2026-q3.md)), 2026-11-02.
- **Accessibility standard baseline** — role docs and the JD reference WCAG 2.1 AA; the current W3C recommendation is 2.2 and EU market obligations have tightened. Confidence: low, needs checking. Stance mix: 1 Challenges, pending verification. Entries: 2026-09-30.
- **Production testing, mocking and real integration** — mocks by default, verified against the real dependency; testing in production complements rather than replaces pre-production testing and needs canary, rollback and observability first; keep real-dependency tests few and flagged. A 2026 practitioner account adds that coding agents can generate full simulators of third-party services from public API docs, which makes the mock tier cheap but not self-verifying. Confidence: medium (older, owner-team sources; nothing on third-party platforms or payments). Stance mix: 1 Supports (with a caution on breadth), 1 Supports (cheap simulators, one company). Entries: 2026-10-23, 2026-11-02.
- **Verification as the bottleneck under AI acceleration** — as code generation gets cheap, the constraint moves to deciding what to build and verifying and being accountable for it, which is where QA sits. Evidence: 8x more code but only about 30% more releases across 100,000 GitHub developers. Unproven locally. Confidence: medium-high on the direction, low on what it does to dedicated QA roles. Stance mix: 2 Supports, 1 Unsettled (dark-factory simulated QA). Entries: 2026-11-02.
- **Safe use of AI tools in our own work** — an agent that holds private data, reads untrusted content and can send data out is exploitable, and filters that block 97% of attacks are a failing grade; limit the blast radius instead. Confidence: medium (one practitioner, well argued, widely echoed). Stance mix: 1 Challenges (to how freely we extend our own AI tooling). Entries: 2026-11-02.
- **AI-assisted work and cognitive load** — supervising several agents is mentally exhausting, and management expectations decide whether that becomes burnout. Confidence: low-medium (practitioner testimony, not research). Stance mix: 1 Unsettled. Entries: 2026-11-02.
- **Assuring agentic workflows (Microsoft Foundry)** — agents are assured with real-task evals, layered graders, repeated trials and a regression suite run on every model or prompt change, tiered by autonomy and impact. Confidence: low (vendor and practitioner sources; nothing PureGym-specific yet). Stance mix: 1 Unsettled. Possible challenge if concerns firm up. Entries: 2026-11-02.

---

## Entries

### 2026-11-02 — Why AI hasn't replaced software engineers: the decide-execute-deliver sandwich

- **Date** — 2026-11-02
- **Source** — Arvind Narayanan and Sayash Kapoor (Princeton), [Why AI hasn't replaced software engineers, and won't](https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers), *AI as Normal Technology*, 11 June 2026. First of a series. The authors hold a stated thesis (AI as normal technology), so this is argument backed by data, not neutral research. It cites the Willison interview in the next entry, so the two are not independent.
- **Signal** —
  - **AI washing:** the Block (4,000), Snap (1,000) and Intuit (3,000) layoffs were attributed to AI, but reporting pointed to overhiring, investor pressure and management layers; Intuit's CEO said none of it was about AI. An HBR survey found 21% of executives made large cuts in anticipation of AI against 2% from actual implementation. Of 160+ New York WARN filings in the first year of an AI checkbox, none ticked it. A Federal Reserve paper finds US software employment still growing, about 3 percentage points a year slower than without AI, through slower hiring rather than separations.
  - **The sandwich:** work is decide (what to build), execute, and deliver (testing, verification, integration, maintenance), with deep understanding underneath all three. AI has compressed execute and left the ends largely unchanged. Evidence: a study of 100,000 GitHub developers ("Writing Code vs. Shipping Code") found an 8x rise in lines written but only about 30% more releases. Developers have always spent 9% to 61% of their time coding.
  - **Accountability stays human** through norms, liability and regulation, so the engineer's role becomes supervising agents, like a crane operator. Execution-only "programmer" roles have shrunk and paid less for two decades; AI accelerates that.
  - **Vibe coding is not agentic engineering.** In one dataset (SWE-chat, self-selected users) only 44% of agent code survived into commits and vibe-coded commits had nine times the vulnerability rate; the authors say it cannot carry strong conclusions alone. Supervising agents is time-consuming.
  - **Outlook:** demand for software is likely to rise as it gets cheaper, with more engineers rather than fewer, but individual careers may be rocky (the next essay). They bet against democratisation replacing engineers.
  - **Limits the authors state:** the WARN data is New York only, the Fed study excludes self-employment and defines "coder" by skills. Most data is US.
- **Stance** — **Supports**, with qualifications. QA sits in the deliver layer, which the argument says resists automation, and the 8x-versus-30% finding is direct evidence that verification is the constraint. It softens, without refuting, the Modern Testing end state: it says nothing about whether verification stays with dedicated specialists. It also implies that a role defined by executing tests is the exposed part, like the "programmer".
- **My take** — The code-versus-releases finding is an interesting theme to pick up when we look at more DORA measures next year.
- **So what** —
  - Gives a sourced answer to "is QA still needed?": the durable work is risk framing on the decide side and verification and accountability on the deliver side; execution is what compresses. This matches the capability shift already noted in [CH-11](../challenges/11-qa-engagement-in-ai-paired-initiative-delivery.md) (analysis, questions and risk over writing tests).
  - Gives a measure for leadership: releases and rework against output. Lines or tests generated is the metric the study shows to be disconnected from shipping. Consistent with the rework-rate entry below.
  - Usable, carefully, in the job-security conversation: the evidence points to slower hiring and role change rather than mass replacement, but it is aggregate and US-centred, and says nothing about PureGym's decisions. Do not present it to the team as reassurance about local outcomes.
- **Follow-ups** — Read the next essay in the series (individual software engineers' careers) when published; it bears directly on the junior and mid-level QA question. Code versus releases is a candidate theme for next year's DORA work; not tracked yet (the nearest record is [IMP-04](../improvements/04-jira-qa-flow-metrics-baseline.md), Jira QA flow metrics baseline).

### 2026-11-02 — Simon Willison on the inflection point and dark factories (Lenny's Podcast)

- **Date** — 2026-11-02
- **Source** — Lenny Rachitsky interviewing Simon Willison, Lenny's Podcast, "An AI state of the union: we've passed the inflection point and dark factories are coming" (2026; the date is not shown in the transcript supplied). Willison co-created Django and coined "prompt injection". This is an experienced practitioner's account, not research.
- **Signal** —
  - **Inflection:** models from November 2025 (GPT-5.1, Claude Opus 4.5) crossed a threshold where agent-written code mostly does what it is told. He now types about 5% of his code and expects it to be unremarkable by the end of 2026 for engineers to write almost all code with AI. Using agents well takes "every inch" of his 25 years of experience; it is not easy.
  - **Bottleneck:** writing code is cheap, so the constraint moves everywhere else. Prototypes are nearly free (he builds three versions of a feature), but proving which is right still needs real people; simulating users with AI is "not credible".
  - **Dark factory:** the pattern is "nobody writes code, then nobody reads code". He describes StrongDM (access-management security software) replacing the QA hand-off with a swarm of simulated employees making requests around the clock in simulated Slack, Jira and Okta, at about $10,000 a day in tokens (his recollection, from a demo in October 2025, so secondhand). The simulated services were built by coding agents from public API docs and client libraries, run as small binaries, and avoid rate limits. He cautions that a virtual QA team saying software is good does not make it secure.
  - **Tests:** agents should write the test first and watch it fail (red/green TDD); dropping tests for speed is "a huge mistake", because tests let you move faster. But he now tolerates very verbose suites (100+ tests for a small library) since agents maintain them. Tests and documentation no longer signal quality, since an hour's work can have both; he labels unused software alpha and wants proof of usage rather than proof of work.
  - **People:** experience amplifies; new starters onboard faster (Cloudflare and Shopify intern hiring, via a Thoughtworks session); the mid-career group is the one most at risk. Running four agents in parallel leaves him "wiped out" by 11am; he links the strain to management expectations.
  - **Security:** the lethal trifecta (private data, exposure to malicious instructions, a way to send data out) cannot be fixed by guardrails, and a 97% filter is a failing grade; cut one leg and limit the blast radius. He predicts an AI "Challenger disaster" from normalised unsafe use, while admitting he has made that prediction every six months for three years.
- **Stance** — **Unsettled** overall, split by point. **Supports**: tests as the thing that lets agents move fast; human judgement for proving ideas; verification as the new constraint. **Challenges**: a QA function can be simulated rather than staffed, and a verbose-suite stance that cuts against "right tests, not more tests" (it ignores run time, flakiness and review burden). **Unsettled**: mid-career versus junior risk.
- **My take** — Sees value in both positions (simulated and real). Layer the testing: some real e2e, some mocked, some lower level, at different levels and in different environments, each gated by a different release-blocking capacity. That supports both views. For example, preview uses less Exerp integration, while staging and prod use real Exerp.
- **So what** —
  - **Simulators (CH-10, IMP-11):** strengthens the case for a cheap, agent-built simulator tier, with the Dootrix Exerp simulator as the local precedent. The fidelity caution from the 2026-10-23 entry still applies, since a simulator built from documentation can drift from the real service. Whether our Exerp documentation is enough to generate one is unchecked.
  - **Not evidence for us:** one company, a security-software domain, a very high token spend, a secondhand account and no outcome data. It does not show human QA is dispensable.
  - **Verification harness as QA's work:** simulated users and dependencies plus scenario sets is a concrete form of "on the loop" and a credible growth narrative for the team, if it is tried before it is promised.
  - **Our own tooling:** the lethal-trifecta test applies to any AI tool we run that reads untrusted content and also holds private data or can write out. Worth checking before extending agent-run checks such as those in IMP-01.
  - **Wellbeing:** watch team-level load as AI-assisted work scales; the claim is testimony, not research.
- **Follow-ups** — Not tracked yet; the evidence is carried in the [CH-11](../challenges/11-qa-engagement-in-ai-paired-initiative-delivery.md) and [CH-10](../challenges/10-pico-source-of-truth-and-exerp-dependent-test-strategy.md) updates.

### 2026-11-02 — Microsoft Foundry and assuring agentic workflows

- **Date** — 2026-11-02 (prompted by the 2027 direction signal in [leadership-direction.md](leadership-direction.md); the tech leadership team is mapping Foundry for agentic workflows and automation, and AC expects it to reach QA's queue). Full brief: [research](research/2026-11-02-foundry-agentic-workflows-qa.md).
- **Source** — Microsoft Learn, [What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry) (updated 2026-09-24), [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) (2026-10-26), [Observability](https://learn.microsoft.com/en-us/azure/foundry/concepts/observability) and [Agent evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators) (dates not shown); Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) (date not shown); Hamel Husain, [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) (date not shown); OWASP, [Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) (landing page only read)
- **Signal** — Foundry is Microsoft's managed platform for building and running agents: prompt agents (configuration only), hosted agents (own code), shared governed tools (Toolbox), swappable models, and built-in tracing, evaluation, monitoring and red teaming (PyRIT-based). Practitioners agree that agents are assured through evals built from real tasks (start with 20–50), layered graders (code, model, human), outcome and process checks, repeated trials with pass^k for consistency, a regression suite that also runs on model or prompt change, and sampled production evaluation. Several Foundry evaluators are still preview, and its built-ins are generic, so business correctness needs custom evaluators.
- **Stance** — **Unsettled**. It fits the "pace with proportionate quality" and "AI with accountability" themes, but there is no current QA position on testing agents that act for other departments, and the sources are vendor or practitioner descriptions, not comparative evidence.
- **My take** — This will probably land in QA's queue because it is being discussed now. If concerns about how the agents will be assured firm up, it could become a challenge.
- **So what** — Watch which processes are chosen and whether QA is invited into the first one. If it goes ahead, propose a small eval-first starter kit with risk tiers rather than a per-output test stage. Triggers for opening a challenge: agents with write access to member, payment or financial data and no agreed owner of assurance; no sandbox or test data for them (the CH-10 and IMP-02 problem again); or release pressure with no eval gate. A challenge would need a Notion card and a roadmap, so it is not opened yet.
- **Follow-ups** — None tracked yet. Likely destinations: a new challenge if the concerns above appear, or an improvement (agent quality kit) if QA is asked to build the approach.

### 2026-10-23 — Testing in production vs mocking vs real integration (distributed systems)

- **Date** — 2026-10-23 (prompted by a conference disagreement with LMo; see [discovery note](discovery-calls/2026-10-21-annual-conference-team-conversations.md))
- **Source** — Cindy Sridharan, [Testing in Production, the Safe Way](https://readmedium.com/testing-in-production-the-safe-way-18ca102d0ef1) and [Testing Microservices, the Sane Way](https://readmedium.com/testing-microservices-the-sane-way-9bb31d158c16) (c.2018; mirror copies, dates not shown); Martin Fowler, [Contract Test](https://martinfowler.com/bliki/ContractTest.html) (2018 revision); Spotify Engineering, [Testing of Microservices](https://engineering.atspotify.com/2018/01/testing-of-microservices) (Jan 2018); DORA, [Test automation](https://dora.dev/capabilities/test-automation/) (current, undated); Honeycomb, [Testing in production](https://www.honeycomb.io/blog/testing-in-production) (vendor view; author and date not captured)
- **Signal** — Per source:
  - **Sridharan (Safe Way):** staging is rarely a true replica of production (smaller clusters, different configuration, thinner monitoring, drifting data), and parity takes large effort; some checks, such as soak testing, are best done with real traffic. Staging is often relied on more than needed. Testing in production is "by no means a substitute to pre-production testing nor is it, by any stretch, easy", and needs heavy automation, canary and staged rollouts, observability, and a system designed for it.
  - **Sridharan (Sane Way):** massive integration tests spanning many services are an anti-pattern, and testing every component in unison is an outdated model for microservices.
  - **Fowler (Contract Test):** doubles for external services keep tests fast and reliable, but you must check periodically that they still match the real service, by running contract tests against a test instance of it (daily is often enough, outside the main pipeline). A failure should trigger a task and a conversation with the service owner rather than necessarily breaking the build; consumer-driven contracts reduce surprises.
  - **Spotify:** the traditional pyramid can be harmful for microservices; favour integration tests of the service in isolation with explicit interaction points, a few implementation-detail tests and ideally no "integrated tests" (tests that pass or fail on another system's correctness, such as in a shared test environment), which are fragile.
  - **DORA:** fast, reliable automated suites in the delivery pipeline improve stability and reduce burnout; acceptance tests typically run the service with dependencies replaced by test doubles; testers work alongside developers; suites should give feedback in under ten minutes.
  - **Honeycomb (vendor view):** every deploy is a test in production; most systems are too big or unpredictable to clone; mitigate risk with automated canaries, fast rollback, feature flags and observability; a staging copy does little to prevent deploy-caused failures.
- **Stance** — **Supports**, with a caution on breadth: it backs the tiered model (mocks by default, a small number of real-dependency checks) and challenges any growth of real-Exerp testing into a broad shared-staging suite. Limits: sources are 2014–2018, mostly about services the team owns rather than a third-party platform, and none covers payments or regulated member data.
- **My take** — Being able to deploy "your bit" to production with the relevant mocks and checks is great and should be kept. In the front end we cannot decouple from Exerp, and that will grow as Portal tests need Exerp for auth and include synchronous calls such as cancel. In the Join journey the reliance can be broken, but we have seen where that falls over (members never getting a subscription). The backend is more nuanced: no Exerp tests is not acceptable, because it breaks things. People regularly report "Exerp has done something", and if QA can catch it, it should. Possible split: select integration tests, flagged in the packs, that may not run every time or block releases, but run overnight and flag issues. This needs fleshing out in the backend initiative. Example: when Dootrix built the bookings service they mocked Exerp by creating an Exerp simulator, and LMo noted it was a good test tool. But in testing we had real Exerp, and that was manual, so why not automate something that is manual? Layers of testing, whatever works best; it is better to have tests and not enable them than to not have tests and need them.
- **So what** — Treat the real-Exerp tier as verification of the Exerp assumptions (mocks and contracts) plus a few journeys where the member outcome depends on Exerp, not a general suite. Flag these tests in the packs and decide per tier whether they block releases or run overnight and alert. Before leaning on production testing, check the maturity of canary, rollback and observability. Gives evidence for the conversation with LMo and GL.
- **Follow-ups** — Tracked as [CH-10](../challenges/10-pico-source-of-truth-and-exerp-dependent-test-strategy.md) (CH-10.5 test-tier rules, CH-10.6 real-Exerp proof of concept) and [IMP-11](../improvements/11-backend-test-pack-coverage.md) (IMP-11.5 flagged integration tier).

### 2026-09-30 — Accessibility baseline may have drifted behind the standard

- **Date** — 2026-09-30 (raised during repo review)
- **Source** — W3C [WCAG 2.2](https://www.w3.org/TR/WCAG22/), a W3C Recommendation since October 2023, superseding 2.1. Separately, the EU [European Accessibility Act](https://ec.europa.eu/social/main.jsp?catId=1202) (Directive 2019/882) has applied to in-scope consumer digital services since 28 June 2025.
- **Signal** — WCAG 2.2 adds success criteria around focus appearance, dragging movements, target size, consistent help, and reducing cognitive load in authentication. The EAA places legal obligations on consumer-facing digital services in EU markets rather than leaving accessibility as a voluntary standard.
- **Stance** — **Challenges**, pending verification. Our [job specification](my-role/job-specification.md), [role pillars](role-pillars.md), and both the [Lead](team-roles/lead-qa-engineer.md) and [Staff](team-roles/staff-qa-engineer.md) QA role definitions all reference **WCAG 2.1 AA**. That may be a deliberate, agreed baseline, or it may be drift.
- **So what** — Worth a direct check rather than an assumption, especially given the expansion-into-new-markets direction from the C-suite: which markets we operate in, what the legal obligation actually is in each, and whether 2.1 AA is a conscious decision or an inherited number. If it is drift, it is a cheap, credible thing for QA to surface. Confidence in my own reading here is low until checked with the Head of Software Engineering.

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

Older entries (before 2026-09-01): [archive/industry-signals-2026-q3.md](archive/industry-signals-2026-q3.md).
