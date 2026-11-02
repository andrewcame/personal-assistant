---
type: research
date: 2026-11-02
links: []
---

# Research Brief — Microsoft Foundry And QA For Agentic Workflows

Prompted by the 2027 direction signal in [leadership-direction.md](../leadership-direction.md) (2026-11-02): the tech leadership team is mapping Foundry-delivered agentic workflows and automation across PureGym. It only uses sources not already in [industry-signals.md](../industry-signals.md); the harness-engineering, mutation-testing and "on the loop" material there still applies to agents that write code, and is not repeated.

## Question

- **Research question:** What is Microsoft Foundry, and what does industry practice say about assuring agentic workflows (agents that take actions for business teams) so that QA can propose a proportionate approach?
- **Current position being tested:** None formal. The working assumption from the role brief is "pace with proportionate quality" and "AI with accountability". The aim is to check whether those hold for agents that act on business systems, not only for AI-written code.

## Sources

### 1. Microsoft Learn — *What is Microsoft Foundry?*

- **Source and date:** Microsoft Learn, page dated 2026-08-13, updated 2026-09-24.
- **Link:** <https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry>
- **Why it is credible:** Primary vendor documentation, kept on a 90-day update cycle.
- **Relevant finding:** Foundry (formerly Azure AI Foundry) puts agents, models and tools under one Azure resource with shared RBAC, networking and policy, plus built-in tracing, monitoring and evaluations. It offers three build routes: **prompt agents** (declarative: instructions, a model and tools; Foundry runs them, no code), **voice-based prompt agents**, and **hosted agents** (your own code and framework, such as Microsoft Agent Framework, LangGraph or Semantic Kernel, as a container with a managed endpoint). The catalogue lists 10,000+ models (Microsoft, OpenAI, Anthropic, Meta and others). Tools and retrieval are shared through a **Toolbox**. Governance covers Entra identity, content filters, network isolation and Azure Policy. Some capabilities are marked preview.
- **Limits or caveats:** Vendor description of its own product. Preview features may change.

### 2. Microsoft Learn — *What is Foundry Agent Service?*

- **Source and date:** Microsoft Learn, page dated 2026-10-26.
- **Link:** <https://learn.microsoft.com/en-us/azure/foundry/agents/overview>
- **Why it is credible:** Primary vendor documentation, updated this week.
- **Relevant finding:** Agent Service is the managed runtime: it hosts and scales agents, manages conversations and tool calls, and handles lifecycle. **Toolboxes** curate web search, file search, code interpreter, MCP servers and custom functions once, then share them across agents through one managed MCP endpoint with central authentication, governance and versioning. Models can be swapped without changing agent code. An **agent optimizer** (preview) proposes better instructions, tool descriptions and model choices. Agents are versioned, get stable endpoints, and can be published to Teams, Microsoft Copilot and the Entra Agent Registry. Prompt agents can be defined through SDK or REST to fit CI/CD.
- **Limits or caveats:** Optimizer and Copilot harness are preview. Model swap without code change is convenient, but it also means behaviour can change with no code diff, which is a regression risk (see synthesis).

### 3. Microsoft Learn — *Observability in generative AI* and *Agent evaluators*

- **Source and date:** Microsoft Learn; observability page read 2026-11-02 (page date not shown in the fetched text); agent evaluators page read the same day (date not captured).
- **Links:** <https://learn.microsoft.com/en-us/azure/foundry/concepts/observability> and <https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators>
- **Why it is credible:** Primary vendor documentation.
- **Relevant finding:** Three capabilities: **evaluation**, **monitoring** and **tracing** (OpenTelemetry-based, Application Insights integration, supports LangChain, LangGraph, OpenAI Agents SDK and Microsoft Agent Framework). Evaluation runs at three lifecycle stages: model selection, **pre-production** (own datasets, custom evaluators, and an **AI red teaming agent** built on Microsoft's PyRIT, "best used with human-in-the-loop"), and **post-production** (sampled continuous evaluation of live traffic, scheduled evaluation on test datasets to catch drift, scheduled red teaming, alerts on quality thresholds). Quality gates can be built into CI/CD. Built-in agent evaluators are split into *system* level (Task Completion, Task Adherence, Intent Resolution, Task Navigation Efficiency, Customer Satisfaction) and *process* level (Tool Call Accuracy, Tool Selection, Tool Input Accuracy, Tool Output Utilization, Tool Call Success). Some are AI-assisted (a judge model scores output); some are deterministic. Several are preview.
- **Limits or caveats:** The built-ins are generic. They do not know PureGym's rules, so domain correctness needs custom evaluators. Judge-model scores are themselves a thing to be calibrated.

### 4. Anthropic — *Demystifying evals for AI agents*

- **Source and date:** Anthropic engineering/research blog (publication date not shown in the fetched text; I did not verify it).
- **Link:** <https://www.anthropic.com/research/demystifying-evals-for-ai-agents>
- **Why it is credible:** Written by the team that builds agent harnesses, citing real deployments (Claude Code, Descript, Bolt). A model vendor, so it has an interest in agents succeeding; its guidance is not Foundry-specific.
- **Relevant finding:**
  - Vocabulary: a *task* is a test case; each attempt is a *trial*; a *grader* scores it; the *transcript* is the full trajectory; the *outcome* is the final state in the environment (a booking exists in the database, not just "your flight is booked" in the chat).
  - Combine three grader types: **code-based**, **model-based** and **human**. Weighted, binary or hybrid scoring per task.
  - Separate **capability evals** (start low, a hill to climb) from **regression evals** (near 100%). High-scoring capability evals "graduate" into the regression suite.
  - Outputs vary between runs, so run multiple trials. **pass@k** (at least one success in k tries) suits tools where one success matters. **pass^k** (all k succeed) suits agents where consistency is essential: 75% per trial gives about 42% over three.
  - Start with **20–50 tasks drawn from real failures** and the manual checks you already run. A good task is one where two domain experts independently reach the same verdict. A 0% pass rate across many trials usually means a broken task, not an incapable agent.
  - Conversational agents need a second LLM to simulate the user. Research-style agents need groundedness, coverage and source-quality checks, with LLM rubrics regularly calibrated against expert humans.
  - Evals let teams adopt new models in days rather than weeks.
- **Limits or caveats:** Vendor practitioner guidance, not measured results. I read most of it but not every section.

### 5. Husain — *Your AI Product Needs Evals*

- **Source and date:** Hamel Husain, personal blog (date not shown in the fetched text; I did not verify it).
- **Link:** <https://hamel.dev/blog/posts/evals/>
- **Why it is credible:** Named practitioner who led the CodeSearchNet team; worked example from a real SaaS assistant.
- **Relevant finding:** Unsuccessful AI products "almost always" fail for the same reason: no robust evaluation system. Three levels: **Level 1 unit-test assertions** (cheap, every change), **Level 2 human and model review of logged traces** (on a cadence), **Level 3 A/B testing** (after significant change). Look at your traces; whack-a-mole prompt fixes are the symptom of having no evals.
- **Limits or caveats:** One case study (a real estate assistant). I read the first part of the post only.

### 6. OWASP — *Top 10 for Agentic Applications 2026*

- **Source and date:** OWASP GenAI Security Project, 2026 edition.
- **Link:** <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/>
- **Why it is credible:** Standards body; peer-reviewed with 100+ contributors.
- **Relevant finding:** A reference list of the most critical security risks for agents that plan, act and decide across workflows. I read only the landing page, not the ten items.
- **Limits or caveats:** The detail is unread; use it as a checklist to open, not as a source of claims yet.

## Synthesis

- **Points of agreement:**
  - An agent is evaluated as a system: the model, the instructions, the tools and the environment together. "Testing the prompt" is not enough (sources 2, 3, 4).
  - You need a dataset of real tasks before you need a framework. Start small (20–50), from what people already check by hand and from real failures (sources 4, 5).
  - Layer the checks: deterministic first, judge-model second, human on a sample (sources 3, 4, 5). Cost and cadence rise with each layer (source 5).
  - Judge the **outcome** in the target system and the **process** (tool choice and inputs), not just the words (sources 3, 4).
  - Production is part of testing: sampled live evaluation, drift runs and alerts (sources 3, 4).
- **Points of disagreement or uncertainty:**
  - How far to trust judge-model scoring. Sources 3 and 4 both use it; source 4 insists on human calibration.
  - Foundry's built-in evaluators are mostly preview, so which are stable enough to gate a release is unsettled.
  - I found no independent evidence in these sources on how well Foundry itself performs. These are all vendor or practitioner descriptions, not comparative results.
- **What the evidence supports:** Evals are the specification and the regression suite for an agent. A small set built from real tasks, run on every change including model swaps, is the single highest-value control. Variation between runs has to be handled by repeated trials.
- **What it challenges:** The idea that agents can be checked by demo or spot-check, or that a platform's built-in scores replace business-specific criteria.

## Implication Here

- **Likely relevance to this role:** If capacity opens up and Engineering builds agents for other teams, QA is the natural owner of *how we know an agent is good enough to release and stay good*. That is the same job as today (risk, confidence, repeatability) applied to a non-deterministic system. It fits the JD's agentic testing and AI-driven testing responsibilities, but note the JD is about using agents to test, whereas this is testing agents. That is a scope extension AC may want to agree with GL. (Inference, not from a source.)
- **Proposed approach (a proportionate starter kit, to validate before use):**
  1. **Tier by autonomy and impact.** Use the existing probability × impact × detectability lens. Read-only and draft-for-human agents get a light route; agents that write to member, payment or financial data get the full one. Humans stay "on the loop" for low tiers and "in the loop" for approval of high-impact actions.
  2. **Business owner defines success.** The department's process owner is the domain expert who writes pass/fail ("two experts reach the same verdict"). QA shapes the tasks and graders; QA does not own the business rules.
  3. **Seed the eval set from the manual process.** 20–50 tasks from what the team does by hand today plus known failures. Keep a reference answer per task.
  4. **Layered graders.** Deterministic checks of the end state in the target system and of tool inputs (Foundry's Tool Input Accuracy and Task Adherence are candidates); judge-model rubrics for tone and completeness; periodic human sampling to calibrate the judge.
  5. **Handle non-determinism.** Run several trials per task and gate on pass^k for anything transactional.
  6. **Capability versus regression suites.** Regression suite runs in CI on every change, **including model, prompt and toolbox changes**, because Foundry allows model swaps with no code change.
  7. **Safety and security.** Scheduled AI red teaming (PyRIT-based agent) and an OWASP agentic checklist for tiers with write access; least-privilege tool access through Toolbox and agent identity.
  8. **Production watch.** Tracing and sampled continuous evaluation with alerts, owned the way staging alerting is owned under IMP-01 Staging monitoring and alerting ownership.
  9. **Environments and test data.** Agents act on real systems, so expect the same test-data and environment problems as CH-10 (Pico source of truth and Exerp-dependent test strategy) and IMP-02 (dynamic member creation and test data). A safe sandbox per agent is a prerequisite for write-action tiers. (Inference from existing records.)
- **Member, business, delivery, people and repeatability implication:** A reusable kit (eval template, risk tiers, release checklist, CI gate) makes each new agent cheaper to assure, which matches the repeatability lens and the "pace with proportionate quality" theme. It also gives the QA team a visible, forward-looking skill area while microsite sunset limits other progression (see Standing Themes).
- **What should change, be watched, or no action:** No action is justified yet. The scope of the agent work, the departments, and who builds it are all unknown. **Watch:** the workshop outcome, which processes are chosen, and whether QA is invited into the first one. **If it goes ahead:** the likely destination is a new improvement (an agent quality kit), not a challenge, and a small pilot on the first agent is the right test. Not created; AC to decide.

## Proposed Industry Signal

Not filed. This is sourced mostly from vendor documentation, and the leadership context is already logged in [leadership-direction.md](../leadership-direction.md). If AC wants a signal, the candidate is:

- **Date** — 2026-11-02
- **Source** — Anthropic, *Demystifying evals for AI agents*; Microsoft Learn, *Observability in generative AI* and *Agent evaluators* (all read 2026-11-02)
- **Signal** — Agents are assured with evals built from real tasks, layered graders (code, model, human), repeated trials (pass^k for consistency) and continuous production evaluation. A regression suite is what lets a team change model or prompt safely.
- **Stance** — Supports (the "proportionate quality" and "AI with accountability" themes)
- **My take** — leave blank
- **So what** — If QA is asked to assure agents for other departments, propose a small eval-first starter kit with risk tiers, not a per-output test stage.
- **Follow-ups** — Possible improvement: agent quality kit, if the Foundry work is confirmed.
