---
id: DC-2026-10-09-dootrix-ai-harness
type: discovery-call
date: 2026-10-09
pillars: [P2, P3, P4, P5, P9]
focus: [people, ownership, automation, productivity]
links: [CH-11, INI-02]
people: [GH, DG, DW, JT, JB]
---

# 2026-10-09 - Dootrix AI Harness And Engineering Practices

## Call Context

- **Date:** 2026-10-09
- **Source / role:** JB, Dootrix architect (role described by AC); GH, Head of Software Engineering; DG, Principal Engineer; AC, QA & Test Engineering Manager.  DW and JT attended as software engineering managers.
- **Conversation type:** Engineering discovery / supplier knowledge sharing
- **Related team or platform:** PureGym engineering, Pico, shared AI skills, AI-assisted test engineering and Appium
- **Notes based on:** Full Teams transcript supplied by AC as a DOCX. Transcript spelling normalised where clear; likely speech-recognition errors and uncertain model names are treated cautiously. Embedded profile-image URLs and authentication tokens excluded.

## Purpose

- Capture how Dootrix works with AI: what it has built, how skills, agents and models fit together, and how QA expertise contributes to the approach.
- Draw out transferable engineering practices and their relevance to the QA & Test Engineering Manager role. This is a learning record, not a follow-up task list.
- AC described the call as very useful. The account below is based on the supplied extract, not the complete session. Dootrix's experience is a practitioner reference, not evidence that every technique is an established industry standard.

## How Dootrix's Harness Works

### Codified Engineering Practice With A Context Layer

- JB described taking 16 years of Dootrix engineering experience, including C# best practice, and codifying it into a base harness. The aim is to retain engineering quality while changing how software is produced.
- Each client harness starts from that base, then adds client-specific architecture, decisions, documentation, skills and delivery context. PureGym material stays out of the reusable Dootrix base.
- Context includes meeting notes, commitments and contractual scope, not just source code. Agents can challenge an attractive new feature if it falls outside the agreed work.
- **Transferable principle:** separate reusable engineering standards from project-specific knowledge. The harness makes the expected way of working available to the agent instead of relying on the engineer to explain it every session.

### Harness And Workspace Structure

- Dootrix's client harness is a wrapper around project repositories, not necessarily a monolithic checkout. A repository list records which repositories are in scope; engineers clone those into a local workspace, where the checkouts are ignored by the harness repository.
- Agents are told not to clone additional repositories without asking the engineer. This gives the engineer control over the code brought into the workspace and avoids the agent expanding scope by itself.
- A deterministic initialization script sets up the workspace. A separate onboarding skill can inspect the approved repositories and build a picture of the estate and its coding practices; that documentation is then maintained as the project context evolves.
- JB said repository-local skills, which some tools initially failed to recognise, were now being picked up in nested repositories. This allows a shared harness skill and a project-specific skill to coexist at the appropriate level.
- Dootrix also generates project summaries and documentation for non-engineering stakeholders. JB described a MkDocs site published as an Azure Static Website, protected by Active Directory and project RBAC. Useful context is made consumable outside the coding session, not only to agents.
- In the demonstrated client harness, useful changes could be committed directly to main, without a PR process. That is Dootrix's stated workflow, not a general recommendation; a PureGym implementation should follow our own access, review and audit requirements.
- **Transferable principle:** keep repository scope explicit, initialization deterministic, and context useful to both engineers and stakeholders. Let the harness reference project code without automatically taking control of it.

### Skills Encode Activities, Not Job Titles

- Dootrix has base skills and client-specific skills. PR feedback and corrections from client conversations become reusable guidance, reducing the need to repeat the same criticism on later work.
- JB explicitly favours activities such as **adversarial test review** over personas such as "act as a QA engineer". A skill describes the work to do, rather than relying on a role label to imply the right behaviour.
- Named PureGym skills were **back end critic, capability readiness, copy audit, front end critic and local stack verification**. JB described these as relatively light, client-specific guidance accumulated during the engagement, including tying implementations back to architecture/design context.
- The extract does not explain each named skill's internals. Their names should not be treated as proof of particular checks or coverage.
- Skills can travel with scripts. They are not necessarily just prose instructions; they can direct an agent to an existing executable operation.
- JB described opt-in and default-installed distribution in Claude, with skills also configured for OpenAI. Shared skills can therefore be available beyond an individual repository, depending on the platform's distribution mechanism.
- His example was a Dootrix brand skill installed by default: it would be available at runtime while an engineer worked in a project harness, without depending solely on pulling it into each repository. This distinguishes centrally distributed capability from repository-local context.
- Dootrix also maintains a separate skills repository/marketplace. JB said it is especially useful outside engineering: commercial, accounting and finance teams use shared skills, while most engineers spend their working day in a project harness. He gave company voice and branding for marketing material or PDFs as examples of capabilities useful outside a code repository.
- JB described common skills in a cross-tool `.agents` location, alongside tool-specific Claude and Codex configuration. The intent is to share core capability across model environments while isolating provider-specific instructions where needed.
- **Transferable principle:** make a useful engineering activity explicit and reusable, with a clear purpose and expected output. The durable asset is the method, not the persona.

### Agents Apply The Context And Skills

- In JB's examples, agents build features, consult architectural and commercial context, challenge scope drift, carry out reviews and update learnings. Skills supply reusable procedures and project-specific expectations for those activities.
- The workflow includes a skill requiring a different model family to perform adversarial review after implementation. Review is part of the described development workflow, not just an optional new prompt at the end.
- DG separately described chaining agents with responsibility for different stages, with an agent loading a skill when it reaches an activity such as writing or reviewing a data file. This was DG's approach; the extract does not establish that Dootrix uses the same agent topology.
- JB described a primary orchestrator delegating bounded tasks such as repository exploration and summaries to worker agents, then reviewing their results. The more capable model plans and critiques; less expensive models do discrete work. DG described a similar planner/implementer/reviewer chain in his own experiments.
- Model allocation is tuned by task and output quality, not by choosing the cheapest model everywhere. JB said Dootrix experimented down to Sonnet but not Haiku: if a low-cost worker returns a poor summary, the orchestrator redoes the work and token savings disappear. He described this as iterative, tedious tuning.
- The tool layout also separates cross-model skills from provider-specific agent instructions. This is one way Dootrix handles portability while tailoring orchestration and cost to the tools each model supports.
- **Useful distinction:** the harness is the working environment and context; an agent carries out work using a model and tools; a skill supplies a reusable method; a script executes a repeatable operation.
- The transcript does not expose Dootrix's complete agent definitions, orchestration or technical enforcement. Avoid inferring a particular multi-agent architecture from the examples.

### Different Models For Implementation And Review

- Dootrix gives engineers access to both OpenAI and Anthropic. If one family performs the implementation, the other performs the adversarial review, and vice versa.
- JB's comparison was that Anthropic models were particularly creative and strong at design, while Codex models were stronger at sustained, detailed code analysis but weaker at design. This explains why Dootrix values both rather than selecting one model for every activity. These are his observations, not universal model rankings; uncertain model names in the transcript have been omitted.
- Supporting both ecosystems creates extra configuration and maintenance work. Dootrix accepts that complexity because it sees value in the different perspectives.
- JB acknowledged that Copilot also offers access to different models, but said Dootrix moved away after finding its coding wrapper unsatisfactory at the time and disliking the move to credits. This is their tooling experience, not a current comparative assessment. The useful distinction is that access to a model and the harness around that model are separate parts of the engineering experience.
- **Transferable principle:** model choice can be specific to the activity. A reviewer should challenge the implementation, not simply continue the author's line of reasoning.
- A second model is another source of scrutiny, not independent proof of correctness. Models can share blind spots; test execution and engineering judgement still matter.

### Cost And Provider Resilience

- Dootrix tracks the token usage that sits behind its subscription seats and estimates what that usage would cost at API rates. JB said this is intended to help them price work if seat allowances change or providers move customers toward usage-based charging.
- JB described having engineers use both Claude and OpenAI, and discussed the maintenance overhead alongside the benefits. He also raised provider price and allowance changes as a business risk; his specific market claims and predictions were not verified in the call.
- The conversation included open and locally run models as possible lower-cost options. JB noted that client acceptance of inference on some providers' infrastructure can be a constraint; DG's Qwen use was personal experimentation, not a company-approved deployment.
- **Transferable principle:** measure usage and test assumptions about cost, quality, privacy and hosting before a provider or model choice becomes embedded in delivery.

## The Most Interesting Capabilities

### A Self-Learning Feedback Loop

- JB described a loop that reads local conversation records, identifies recurring rejected solutions and engineer corrections, and updates learnings or documentation once a pattern has occurred enough times.
- The agent announces the learning during the session, and the engineer can reject it as invalid. This reduces reliance on someone remembering to update instructions manually.
- Examples included repeated C# style corrections and agents resisting an agreed move from a bookings microservice to gym because their recorded scope was stale.
- **Why it is interesting:** the human effort already spent correcting the agent becomes reusable knowledge. The harness can improve from real engineering interactions rather than only from scheduled documentation work.
- **Best-practice interpretation:** corrections are evidence for a learning, not authority to change a decision. Traceability, review and the ability to supersede stale rules matter, especially for architecture or scope. The extract does not establish Dootrix's wider audit and approval controls.

### Scripts Alongside Skills

- JB stressed the difference between inference and deterministic execution. Repeatedly generating and discarding the same script wastes tokens and introduces unnecessary variation.
- DG described roughly 80 Makefile targets in his own project, with skills pointing to retained commands for repeatable work.
- AC recognised the same pattern in his emulator/setup work: write the script once, then have the skill invoke it each time.
- **Transferable principle:** use AI where judgement, interpretation or synthesis is needed; use tested scripts where the operation is repeatable. An AI-led workflow need not use inference for every step.

### Context Retrieval Rather Than Loading Everything

- Dootrix currently ingests client documents as markdown in RBAC-controlled repositories. JB acknowledged that this is token-intensive and reflects its commercial and access-control constraints.
- For an internal business setup, he recommended considering document embeddings and a vector store so agents can retrieve relevant context more efficiently.
- **Transferable principle:** context should be relevant, current and accessible to the right people. More documentation in the prompt is not automatically better.
- Retrieval introduces its own permissions, freshness and hosting considerations. JB's recommendation is a design option, not a universal requirement or a PureGym decision.

### Build By Learning, Not By Speculating

- JB said Dootrix spent too long designing a perfect harness around hypothetical edge cases before proving it in use. His advice was to form an opinionated starting point, roll it out with engineers, then fix the friction and agent failures people actually encounter.
- GH described his original intent as trialling the approach with one team and expanding based on learning, but said the idea was mistaken for a golden bullet and excitement outpaced the intended experiment.
- **Transferable principle:** start with a bounded, real workflow and learn from use. Neither a large up-front architecture exercise nor an organisation-wide rollout proves value.

## How QA Fits Into The Approach

- AC initially joked that it sounded as though Dootrix had "no QA"; JB immediately clarified that Dootrix has QA architects. JB said the business no longer has manual testers or automation engineers in the former team model: engineers now test and deliver work through to production readiness, working with agents throughout the feature loop.
- JB described the prior hand-off pattern, where an engineer built a feature, passed it to QA, then had to pick it up again, as a slow human interface. Dootrix's aim is for engineers to own the end-to-end feature outcome rather than queue behind a separate testing stage.
- This does not mean QA expertise has disappeared. Dootrix has two QA architects and expects to need more as its Software Factory offering scales. They own the conceptual testing approach and QA guardrails, including skills and expectations for test automation; JB said they update this guidance weekly.
- In some client engagements, QA architects periodically inspect test plans and the client testing approach, and act as the QA interface to the client alongside principal engineers. JB described them as senior, visible counterparts, rather than QA working in the background. He also stressed that the PureGym engagement is different because PureGym already has a QA function.
- JB said QA architects bring the specialist interest and expertise that engineering leaders may not have, including UI automation and test guardrails. AC framed the value as shaping test breadth, scenarios and front-end/back-end strategy upstream, rather than simply taking AI-generated code later and writing tests against it.
- The Dootrix model is a particular operating choice, not a recommendation to remove a QA team. Its transferable lesson is to move QA expertise into engineering standards, skills, risk framing and periodic review, while keeping people accountable for the integrated result.
- JB used a pilot analogy: engineers help shape the work at "takeoff," agents do more of the implementation during the middle, and engineers re-engage at "landing" to bring the work safely to production. AC noted that integration across environments and third-party systems makes that landing especially important. Treat the analogy as JB's aspiration, not a description of fully autonomous delivery.
- The transcript does not provide comparative quality or productivity results for the change in QA staffing. It describes Dootrix's model and rationale, not evidence that the model is suitable for every team or product.

## Selected Extracts

- **JB, 7:35-7:58:** "we try to skillify all of that" - referring to critical feedback being retained as reusable guidance.
- **JB, 51:11:** "it's a job function rather than, or like an activity rather than a persona."
- **JB, 29:14:** engineers take a feature "all the way to being production ready" with agents.
- **JB, 30:53:** QA architects inspect the test approach and act as the client's QA interface on some engagements.
- **JB, 44:20-44:40:** "just roll it out" and fix the issues encountered, rather than trying to design a perfect harness in advance.
- **DG, 1:01:55:** "if a thing is going to be repeated, it goes in the make file and the skill points at the make file."

## What This Means For My Role

- **Quality practice as a shared engineering asset:** my leverage is not limited to reviewing more output. Test-design standards, risk analysis and review methods can become reusable capabilities available wherever engineering work happens.
- **Quality capability versus a separate QA stage:** Dootrix moves routine test execution into engineer-owned delivery, while its QA architects shape guardrails, automation practice and test strategy. The role shift is toward making quality easier to do well and checking the riskier parts, not removing specialist QA judgement.
- **QA expertise without a generic QA persona:** activity-based guidance makes the contribution concrete. Test review, readiness assessment and evidence interpretation are potential capabilities; "be a senior QA" does not define the work or its result.
- **Learning that survives the individual:** useful corrections from QAs can become shared guidance rather than knowledge that stays in a conversation or one person's setup. This supports wider team contribution and reduces repeated coaching on the same issue.
- **Trust comes from evidence:** model review can add challenge, while deterministic checks and meaningful assertions provide executable feedback. More generated tests or a second model's approval are not sufficient evidence of better coverage.
- **Visible QA leadership:** on some Dootrix engagements the QA architect is a client-facing peer to the principal engineer. This is a useful counterpoint to assuming that embedding quality in delivery makes QA less strategic; it can make QA architecture and stakeholder advice more visible.
- **Model and cost literacy:** orchestration, worker-model selection and token/API cost tracking are part of the engineering operating model. For my role, this links AI adoption to sustainable cost, approved data handling and quality outcomes, not just tool access.
- **Trial design matters:** GH's original one-team trial intent was lost when colleagues treated the harness as a golden bullet. The learning for adoption is to set expectations that a bounded trial is for discovering limitations and improving the process, not validating a predetermined success story.
- **Outcome-focused adoption:** the value is reliable coverage, fewer repeated mistakes and a workflow other engineers can use. Harness complexity or the number of skills is not the outcome.
- **Appium as a future application:** the combination of project context, activity-based skills, reusable setup scripts and review fits the existing Appium initiative. Implementation is a future action; this record keeps the learning separate from a delivery plan.

## Wider Engineering And Commercial Context

- GH's interest was in learning from the harness and becoming more outcome-focused, encouraged by the speed of the class-booking demonstration.
- JB said the full Dootrix harness is not included by default in Software Factory outputs; a snapshot or ongoing licence is a separate option. The five named client skills are intended for the relevant PureGym repositories by engagement close, though their current locations were not all confirmed. These are sharing boundaries, not follow-up assignments for AC.
- Rising token costs, changing allowances and dependence on providers were discussed as business risks. Specific pricing and financing claims, and predictions of future increases, were not independently verified.
- Alternative models and local inference were discussed, including DG's personal use of Qwen. Model origin, inference location, company-data permissions and total operating cost are distinct considerations.
- DG's experience of generated skills using the wrong format illustrates a practical reliability point: tool-native structure and actual invocation matter as much as the quality of the instructions inside the skill.
- JB pointed to an OpenAI white paper on "harness engineering" as a source for Dootrix's context-engineering approach and repository structure. This is a practitioner-recommended reference, not material independently reviewed as part of this capture.

## Mapping

### Strategic Mission(s)

- Technical Mastery & Foundations
- People & Practice
- Delivery Flow & Resilience

### Role Pillar(s)

- AI-Enabled Testing & Innovation
- Automation Trust & Reliability
- Test Infrastructure, Environments & Data
- Knowledge Sharing & Quality Practice
- Quality Ownership & Culture

### Objective Lens(es)

- Value Creator
- Business Operator
- People Developer

### Related 30/60/90 Focus Area(s)

- Automation
- Productivity
- Ownership

## Follow-Ups

- **Future application: implement a similar approach for Appium** - Owner: AC - Destination: [Appium initiative](../../initiatives/02-appium-ai-led-first-pass.md) - Recorded from AC's clarification after the call. No timing or detailed implementation plan is set here; the current focus is understanding the practices.

## Possible Outputs

- Learning reference for [Challenge 11 - QA engagement in AI-assisted delivery](../../challenges/11-qa-engagement-in-ai-paired-initiative-delivery.md): QA methods made reusable within the engineering workflow.
- Design reference for the [Appium AI-led first pass](../../initiatives/02-appium-ai-led-first-pass.md): context, skills, models and scripts working together. This is not yet an implementation specification.

## Open Questions

_Limits of the extract, not a list of tasks to chase._

- The full agent orchestration, skill contents and learning-loop controls are not shown.
- The QA example does not establish the balance between agent review, human review, exploratory testing and release assurance.
- No measured quality, productivity or cost comparison was supplied for the change in operating model; reported benefits and model comparisons remain practitioner experience rather than quantified results.