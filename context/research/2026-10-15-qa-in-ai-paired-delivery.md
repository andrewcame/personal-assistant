---
type: research
date: 2026-10-15
links: [CH-11]
---

# Research Brief — QA Engagement In Paired, AI-Assisted Delivery

Discovery input for [CH-11](../../challenges/11-qa-engagement-in-ai-paired-initiative-delivery.md) (roadmap step CH-11.7). It only uses sources not already captured in [industry-signals.md](../industry-signals.md). Morris (on the loop), Böckeler (*To vibe or not to vibe*, *TDD inside the agent loop*), TW Radar Vol 34, DORA 2025 and Modern Testing are already captured there, so this brief refers to them without repeating them.

## Question

- **Research question:** When pairs of engineers deliver large initiatives with coding agents and AI-written tests, where does QA expertise add the most value? And what evidence shows whether AI-written tests and code can be trusted without a per-ticket QA stage?
- **Current position being tested:** A three-touchpoint model (shape at the start, risk-based review mid-way, landing and integration at the end). Review depth is scaled by probability × impact × detectability. Mutation testing checks AI-written tests.

## Sources

### 1. Böckeler — *Harness engineering for coding agent users*

- **Source and date:** Birgitta Böckeler, martinfowler.com, 2 April 2026. It replaces her memo of 17 February 2026.
- **Link:** <https://martinfowler.com/articles/harness-engineering.html>
- **Why it is credible:** Named Thoughtworks Distinguished Engineer. It builds on practice across Thoughtworks teams and cites the OpenAI and Stripe harness write-ups.
- **Relevant finding:** It splits controls into *guides* (feedforward: AGENTS.md, skills, specs) and *sensors* (feedback: tests, linters, review agents). Each can be computational (deterministic) or inferential (judged by an LLM). Checks should be "as far left … as possible", with costly sensors such as mutation testing run after integration. The **behaviour harness** is "the elephant in the room". Most teams rely on a green AI-generated suite plus coverage and manual testing, and she says this "puts a lot of faith into the AI-generated tests, that's not good enough yet." The human's role is to *steer*: when an issue happens more than once, improve a guide or sensor. A good harness "direct[s]" human input "to where our input is most important" rather than removing it. Legacy codebases are harder to harness than greenfield ones.
- **Limits or caveats:** This is a mental model, not measured results. It is mostly about developers, and testers are not named as a role.

### 2. Böckeler — *Maintainability sensors for coding agents*

- **Source and date:** Birgitta Böckeler, martinfowler.com, 27 May 2026.
- **Link:** <https://martinfowler.com/articles/sensors-for-coding-agents.html>
- **Why it is credible:** Hands-on experiment by the same author, with the method and tools (Stryker) published.
- **Relevant finding:** She let the agent write the whole test suite. One file showed 100% statement coverage but had no unit tests, and 13 mutants survived. A broad acceptance test ran the code without checking it. AI-generated acceptance tests "increase coverage, but are often not very assertion-heavy, giving us a false sense of security". She says human review of every test is "unrealistic", and that mutation testing is "crucial" once most testing is left to AI. Whether tests check the *right* behaviour is "a whole other conversation".
- **Limits or caveats:** One application, one author. Mutation testing was run by hand because it uses a lot of compute.

### 3. Vaccari — *Acceptance Tests for AI-assisted development*

- **Source and date:** Matteo Vaccari (Thoughtworks; thanked in both Böckeler pieces for his views on the behaviour harness), personal blog, 29 September 2025, updated 6 March 2026.
- **Link:** <https://matteo.vaccari.name/posts/acceptance-tests-for-ai-assisted-development/>
- **Why it is credible:** Named practitioner with concrete brownfield examples.
- **Relevant finding:** Acceptance tests "look like the most important guardrail for working with AI". They work best when written in the business's language, built from a team-supplied example, and run below the UI through ports and adapters so they are fast and reliable. He lets AI draft them but reviews them himself, which is easy if they read like the user story.
- **Limits or caveats:** Practitioner opinion. It depends on architecture (ports and adapters) that legacy estates may not have.

### 4. Konstantinou, Degiovanni, Papadakis — *Can we find bugs using LLM-generated oracles?*

- **Source and date:** arXiv 2410.21136, first posted 28 October 2024, v2 posted 5 October 2026. The earlier title was *Do LLMs generate test oracles that capture the actual or the expected program behaviour?*
- **Link:** <https://arxiv.org/abs/2410.21136>
- **Why it is credible:** Controlled academic experiment across 24 Java repositories, by authors established in mutation testing research.
- **Relevant finding:** LLM test generation "mainly capture[s] the actual program behavior, making bug detection difficult". AI-written assertions tend to lock in what the code does, bugs included. LLMs are better at *generating* oracles than at *classifying* whether an oracle is correct.
- **Limits or caveats:** Unit-level Java only. Models have changed since the study ran. I read the abstract only.

### 5. Foster et al. (Meta) — *Mutation-Guided LLM-based Test Generation at Meta*

- **Source and date:** arXiv 2501.12862, 22 January 2025, submitted to the FSE 2025 Industry Track.
- **Link:** <https://arxiv.org/abs/2501.12862>
- **Why it is credible:** Industrial deployment across 10,795 Kotlin classes on 7 platforms. Co-authored by Mark Harman.
- **Relevant finding:** Meta reversed the usual flow. It generated *targeted faults for a specific concern* (privacy), then had an LLM write tests that kill them. Engineers accepted 73% of the 571 tests and judged 36% relevant to privacy.
- **Limits or caveats:** Meta-scale tooling, and only one concern (privacy) was shown. Acceptance by engineers is not the same as defects prevented.

### 6. Liu et al. — *Debt Behind the AI Boom*

- **Source and date:** arXiv 2603.28592, 30 March 2026, v2 26 April 2026 (David Lo's group).
- **Link:** <https://arxiv.org/abs/2603.28592>
- **Why it is credible:** Large empirical study of about 302.6k verified AI-authored commits across 6,299 GitHub repositories and five assistants.
- **Relevant finding:** More than 15% of commits from every assistant introduced at least one static-analysis issue. 89.3% of issues were code smells. 22.7% of issues introduced by AI were still present in the latest revision. The authors call for "stronger quality assurance in AI-assisted development".
- **Limits or caveats:** Only static analysis, so it does not measure defects that reach production. The repositories are open source. Figures changed between v1 and v2, and these are the v2 figures.

### 7. CodeRabbit — *State of AI vs Human Code Generation Report*

- **Source and date:** David Loker, CodeRabbit, 17 December 2025.
- **Link:** <https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report>
- **Why it is credible:** Moderately credible. It states its methodology and limits openly, but it is **vendor research** from a company that sells AI review tools. Treat it as a pointer, not proof.
- **Relevant finding:** 470 open-source PRs. AI-co-authored PRs averaged 10.83 issues against 6.45 for human-only PRs (about 1.7×). Logic and correctness issues were about 75% higher, and error-handling gaps nearly 2×. It cites a Cortex 2026 benchmark showing PRs per author up 20% and incidents per PR up 23.5% (I did not verify that benchmark).
- **Limits or caveats:** Authorship was inferred from signals, and the authors admit "human" PRs may include AI work. Small sample. Commercial interest.

### 8. Stack Overflow — *2025 Developer Survey, AI section*

- **Source and date:** Stack Overflow, 2025 survey (more than 49,000 respondents).
- **Link:** <https://survey.stackoverflow.co/2025/ai>
- **Why it is credible:** Large, long-running, published survey.
- **Relevant finding:** 46% of developers distrust the accuracy of AI output and 33% trust it. Only about 3% "highly trust" it. 66% cite "almost right, but not quite" as their top frustration, and 45% say debugging AI code takes more time. Experienced developers are the most cautious.
- **Limits or caveats:** Self-reported perception, not measured quality. Fielded in mid-2025, before the latest agents.

## Synthesis

- **Points of agreement:**
  - Generation is faster than human inspection, so value moves to designing the *guides and sensors*: specs, acceptance examples, gates and review skills. Sources 1, 2 and 3 say this, consistent with Morris (already captured).
  - Coverage is not evidence. Mutation testing is the practical check on how effective AI tests are (sources 2 and 5, plus Radar Vol 34).
  - AI code shows more issues of the kind QA cares about: logic, error paths and lasting debt (sources 6 and 7). Developers do not fully trust it either (source 8).
- **Points of disagreement or uncertainty:**
  - Whether AI should draft acceptance tests. Vaccari says yes, with human review. Farley, as Vaccari reports him, says humans should write them.
  - No source has a good answer for the **behaviour harness**, which is checking the system does the *right* thing. Böckeler says so directly.
  - The defect-rate data is either vendor research or limited to static analysis. None of it measures production defect escape for paired AI teams.
- **What the evidence supports:**
  - QA engaging *upstream* at shaping, by owning acceptance examples and risk framing.
  - Mutation testing as a targeted check on AI tests.
  - Focusing human review on behaviour and correctness, because computational sensors already handle structure well.
- **What it challenges or refutes:**
  - Treating the mid-build touchpoint as a *read-through of AI tests* is weak. Reading every test is unsustainable (source 2), and AI is poor at judging oracles (source 4). The mid-build touchpoint should be **sensor-led** (mutation hot spots, missing acceptance examples), not a read-through.
  - Mutation testing alone is not enough. It proves tests detect *change*, not that they assert *intended* behaviour (sources 2 and 4).

## Implication Here

- **Likely relevance to this role:** High. It points CH-11 at "QA owns the behaviour harness": acceptance examples, risk framing, mutation and coverage-quality sensors, plus exploratory testing where sensors are blind.
- **Member, business, delivery, people or repeatability implication:**
  - Member: Pico Portal → Exerp state journeys are exactly the behaviour-harness gap, and the place where tests that simply mirror current behaviour hurt most.
  - Delivery: Böckeler notes legacy estates are hardest to harness. That fits the Business Gateway adapter period and strengthens the case to treat environments and test data as a precondition.
  - People: this gives the team a credible capability shift into test design, risk analysis and harness stewardship, rather than a smaller version of manual testing.
- **What should change or be watched:** Reshape touchpoint two from "review the drafted tests" to "review what the sensors and acceptance examples show". Watch for production escapes on paired initiatives, because no external source answers that for us.

## Options For QA Engagement

| Model | How it works | Pros here | Cons here |
|---|---|---|---|
| **A. Three touchpoints, sensor-led** | QA shapes at kickoff (risk map, acceptance examples). Mid-way, QA reviews mutation and coverage-quality output and gaps in the acceptance examples. At landing, QA does exploratory and integration testing against Pico → Exerp. Depth is set by P × I × D. | Fits a small QA team. Clear entry points. Builds on the agreed front-end-first strategy. | Still risks batching at landing. Needs mutation tooling and fast environments to exist. |
| **B. QA as harness owner** | QA writes and maintains the guides and sensors: acceptance-test templates, a /how-to-test skill, an adversarial test-review skill (as in the Dootrix pattern), and mutation gates in CI. QA joins initiatives only when risk triggers fire. | Scales across many pairs. Strongest growth story. Matches the "on the loop" principle. | Large up-front investment while the microsite-sunset pressure is on. Weakest at the behaviour harness, where no gate yet replaces judgement. QA can lose touch with the product. |
| **C. Rotating embedded quality partner** | One QA joins the pair as a third member for the whole initiative, rotated across initiatives, and does exploratory testing continuously. | Best product knowledge and continuous feedback. No late batch of defects. | Doesn't scale with a small team when several initiatives run at once. Can bring back the old bottleneck. |

A hybrid is likely: B as the long-term direction, A as the default for each initiative, and C only for initiatives that score high on impact and low on detectability (payments, Exerp state).

## Questions To Take Into Discovery

1. When the pair hands over a slice, what evidence would you accept that the AI-written tests check *intended* behaviour, not current behaviour?
2. Which parts of a typical initiative do you review line by line, and which do you trust to the suite? Why?
3. Have you seen an AI-written test pass while the feature was wrong? What gave it away?
4. Would acceptance examples from QA at kickoff, as a template the agent works from, help or slow you down?
5. Which checks already run inside the agent session or pre-commit, and which only in CI?
6. Where in Pico, Business Gateway and Exerp do you feel least able to tell whether something broke?
7. What would make a mid-build QA touchpoint useful rather than an interruption?
8. How do you size a slice today, and what would "complete enough to test" mean to you?
9. Could we run mutation testing on one core domain area within the current pipeline time budget?
10. Leads: if QA stopped gating changes, what evidence would you need each month to stay confident?

## Candidate Industry Signals

### 2026-10-15 — The behaviour harness is the unsolved part of agent delivery

- **Date** — 2026-10-15
- **Source** — Birgitta Böckeler, [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html), martinfowler.com, 2 April 2026
- **Signal** — Coding-agent harnesses combine feedforward guides and feedback sensors. These can regulate maintainability and architecture well, but checking functional behaviour is "the elephant in the room". Relying on green AI-generated suites, coverage and manual testing is "not good enough yet". The human steers the harness and focuses their input where it matters most.
- **Stance** — Supports (QA "on the loop"), and narrows it: the unsolved behaviour harness is exactly where QA judgement lives.
- **My take** —
- **So what** — Frame QA's role in CH-11 as owning the behaviour harness: acceptance examples, risk framing, exploratory testing.
- **Follow-ups** — Covered by CH-11.

### 2026-10-15 — AI-generated tests mirror current behaviour and hide weak assertions

- **Date** — 2026-10-15
- **Source** — Konstantinou, Degiovanni & Papadakis, [Can we find bugs using LLM-generated oracles?](https://arxiv.org/abs/2410.21136), arXiv, v2 October 2026; Böckeler, [Maintainability sensors for coding agents](https://martinfowler.com/articles/sensors-for-coding-agents.html), May 2026
- **Signal** — LLM-generated oracles mainly capture actual behaviour rather than expected behaviour. In practice, AI-written acceptance tests raise coverage with few assertions: a file at 100% statement coverage had no unit tests and 13 surviving mutants.
- **Stance** — Supports mutation testing. Challenges reviewing AI tests by reading them.
- **My take** —
- **So what** — Mutation testing checks how effective tests are, not whether they are correct. Intended behaviour still needs human-owned acceptance examples.
- **Follow-ups** — CH-11.4 (mutation trial).

### 2026-10-15 — AI-authored code carries more logic and lasting quality issues

- **Date** — 2026-10-15
- **Source** — Liu et al., [Debt Behind the AI Boom](https://arxiv.org/abs/2603.28592), arXiv, March/April 2026; CodeRabbit, [State of AI vs Human Code Generation](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report), December 2025 (vendor)
- **Signal** — More than 15% of AI-authored commits introduce issues and 22.7% of those persist. AI-co-authored PRs show about 1.7× more issues, with logic and error-path gaps highest.
- **Stance** — Unsettled. The direction is consistent, but the evidence is static analysis or vendor-sourced, not production escapes.
- **My take** —
- **So what** — Track escaped defects and rework on paired initiatives ourselves rather than relying on external rates.
- **Follow-ups** — Covered by CH-11.
