# Leadership Direction

This file captures themes, missions, and priorities from leadership at director level or above, including GL, equivalent leaders, and their managers. Sources can include 1:1s, leadership calls, organisational updates, and other material authored or presented by someone in that group.

It is **not** a task list. Tasks live in Notion. This is for themes and signals that should influence how the role is focused and how ideas are validated.

The idea-validator agent should load this file alongside the job spec and the [horizons plan](my-role/horizons.md) when sense-checking ideas.

## How To Add An Entry

- **Date** — when you heard it
- **Source** — who said or published it and in what context (for example, a 1:1, leadership call, or podcast)
- **Theme** — the mission or direction in their words or close to it
- **Implication** — what this means for current focus, if clear
- **My read** — personal reaction, where there is one worth keeping; optional

Add new entries at the top of **Entries** (newest first). If a new entry changes earlier direction, add `**Supersedes:** <date/heading>` to it and `_Superseded by <date>_` under the older heading, rather than deleting it.

### Leadership Scope

Include material from anyone at director level or above. This includes GL, leaders at an equivalent level, and the director's manager or more senior leaders. It is not limited to the director himself. Log the durable theme and its implication rather than a transcript or routine meeting notes. Material from below this level belongs in the more relevant team, discovery, ways-of-working, or notes file unless it directly records a signal from someone in scope.

## Decision Lens

Use these questions when shaping or assessing work, especially decisions involving QA, technology, AI, or ways of working:

- **Member value** — What member outcome does this improve or protect? Can the connection be made explicit?
- **Business enablement** — Does this help PureGym grow, improve, simplify, or expand into new markets without creating avoidable operating complexity?
- **Quality at speed** — What is the smallest proportionate quality approach that gives confidence without slowing a valuable decision unnecessarily?
- **Repeatability** — Does this create a reliable capability, pattern, or evidence base that can work across markets, products, or future acquisitions?
- **Ownership** — Who can make the decision, and are we giving the people closest to the work enough responsibility and context to act?
- **AI with accountability** — Could AI remove toil or improve thinking here? If so, how will people verify the output and remain accountable for risk, quality, and member experience?
- **People and purpose** — Does this preserve focus, learning, connection, and meaningful responsibility as the way of working changes?

The leadership signal behind these tests is that QA should help PureGym move quickly without making member experience, expansion, or operational reliability fragile. Quality is therefore part of making growth repeatable, not friction added after the fact.

---

## Entries

### 2026-09-30 — Leadership call: sunsetting microsites as the gateway to everything else

- **Date** — 2026-09-30
- **Source** — Leadership call with GL (Group Software Engineering Director), DJ (Head of Delivery), GH (Head of Software Engineering); reflecting the CTO's standing position
- **Theme** — the CTO's consistent response to any conversation about resourcing, promotions, growth work, or new investment is "we need to get off the microsites." Sunsetting the legacy microsites has become the single precondition gating almost everything else, and in practice acts as a blinker on other activity.
- **Theme** — Morale is a live counter-pressure. After a recent all-hands, people openly posted in chat about feeling demoralised, wanting better pay, and worrying about job security. This creates a difficult loop: the things that would improve morale (progression, investment, growth work) are held behind microsite sunset, while low morale makes the migration harder to deliver at pace.
- **Theme** — The emerging technical approach is a Pico-fronted adapter to the legacy stack. Pico becomes the front-end experience for everything, with an adapter that calls the old Business Gateway platform for services not yet fully migrated. Business Gateway continues to own those business rules and updates Exerp, which in turn flows back into Pico. This lets the front end move to 100% Portal/Pico far faster than a full backend migration would allow.
- **Theme** — Delivery style is being deliberately changed to accelerate: fewer granular tickets, less sequential "tiny change → test → QA → deploy" work, and instead pairs of engineers taking on larger initiatives using AI (including AI-written tests), pulling SMEs in at the right moments, and handing QA something more complete and better scaffolded to test.
- **Implication (QA)** — A front-end-first test strategy is acceptable and sensible for this period. The routing underneath (direct Pico vs Business Gateway adapter) is largely irrelevant to the member-facing assertion; what matters is that the Pico Portal journey works and that Exerp ends up correctly updated. Backend test depth expands naturally as services migrate off the adapter — sequence backend coverage behind migration progress rather than trying to cover the adapter path.
- **Implication (delivery)** — The QA engagement model has to change with the delivery model. With two engineers driving a larger AI-assisted initiative, the open question is *when* QA engages and *how*, rather than QA sitting at the end of each granular ticket. Captured as [Challenge 11](../challenges/11-qa-engagement-in-ai-paired-initiative-delivery.md) and reflected in the [QA operating model](../ways-of-working/qa-team-operating-model.md#qa-engagement-in-paired-ai-assisted-initiative-delivery).
- **Implication (people)** — Treat microsite sunset as the unlock narrative, not just a migration. Being explicit with the team that progression and investment sit on the other side of it — and showing visible progress against it — is currently the most direct lever on morale available to me.

### 2026-09-17 — Follow-up touch-base with GL

- **Date** — 2026-09-17
- **Source** — 1:1 with GL (Group Software Engineering Director)
- **Theme** — GL offered support on the Web 3 visibility expectation. He also recognised that embedding new cultural ways of working across the wider team takes time, and that extending current interim support may be needed to protect that.
- **Theme** — Once through the immediate firefighting, the expectation is to shift focus onto strategic foundations — starting with staging environments and test data. Allocate pieces of the environment/test-data work to DA (GL sponsoring).
- **Implication** — Balance short-term firefighting with a deliberate move toward sponsored strategic work once capacity allows; the environments/test-data initiative is a genuine strategic need and also supports DA's agreed development goals.
- **Implication** — I am meeting the engineering lead shortly to work through delivery strategies for the interim period; feed the outcome back into Challenge 04's short-term plan.

### 2026-09-15 — Weekly Senior Leadership Call

- **Date** — 2026-09-15
- **Source** — Weekly Engineering Senior Leadership Meeting: me, GL (Software Engineering Director), GH (GH, Head of Software Engineering), DJ (Head of Delivery)
- **Theme** — Getting better at spotting signals when things are going wrong is a shared priority. A recent front-end usage-creep issue was caught by members reporting it rather than by monitoring, which is the wrong way round. Front-end load/performance testing is now recognised as a real gap alongside the backend load testing already being considered.
- **Theme** — GL suggested a nightly performance run, potentially on staging, as a pragmatic alternative to a dedicated load test environment — ramping the Exerp test instance overnight to meet demand and reviewing results each morning alongside existing staging/app alerting. This could also justify retiring the unused Southampton satellite Exerp test instance once staging is validated as the de facto UK load test environment.
- **Theme** — GH wants the agenda for this months monthly engineering all-hands to revisit ways of working across teams, prompted by a conflict/issue-resolution challenge in one web team this week.
- **Implication** — Treat front-end load/performance testing and the nightly staging performance run as a concrete improvement to scope, sequenced UK-first before considering brand/multi-market variants or retiring Southampton capacity.
- **Implication** — Prepare content for the all-hands (progress, direction of travel) and support the ways-of-working reset prompted by this week's team conflict.

### 2026-09-11 — In-office leadership sessions: pace, risk acceptance, resourcing, and infrastructure

- **Date** — 2026-09-11
- **Source** — In-office leadership trip and strategy discussions (Engineering Leadership, me, Principal Software Engineer)
- **Theme** — the CTO has set an explicit expectation to be completely off the account and bookings microsites by the end of the year, against team forecasts pointing to end of March 2027. Engineering is adopting creative delivery approaches to close that gap, starting with grouping backend changes first and enabling front-end pages once foundational pieces are in place.
- **Theme** — A proposal for QA to evolve from "test everything all the time on every micro-deploy" to "test when a feature is ready to go live or when all constituent parts are assembled." This requires explicit leadership acceptance of intermediate delivery risk, counterbalanced by deterministic automated regression, and reduces test duplication and deployment churn.
- **Theme** — Resourcing: placement options for the returning contractor: Web or Apps. Placing them in Apps would accelerate Appium automation and add App QA capacity.
- **Theme** — Infrastructure ownership: an offer for QA to take on staging alerting and first-responder triage, relieving stretched DevEx and Platform engineers and giving QA operational grip on its core testing environment. Separately, dynamic member creation and test-data tooling to be routed through the Tech Challenges Board for architectural backing rather than built as an isolated workaround.
- **Implication** — This is the origin point of the delivery-model change that the [2026-09-30 leadership call](#2026-09-30--leadership-call-sunsetting-microsites-as-the-gateway-to-everything-else) later extended into paired, AI-assisted initiative delivery. The batch/feature-ready testing model only works if the regression safety net is genuinely deterministic, and the risk of finding integration defects later must be formally owned at leadership level rather than absorbed quietly by QA.
- **Implication** — Owning staging alerting turns QA from passive complainant into active custodian of its own biggest bottleneck. Tracked as [Improvement 01](../improvements/01-staging-monitoring-and-alerting-ownership.md); test data as [Improvement 02](../improvements/02-dynamic-member-creation-and-test-data.md); the resourcing and Website QA capacity question as [Challenge 04](../challenges/04-web-qa-capacity-and-accountability.md).

### 2026-09-07 — First 1:1 with GL

- **Date** — 2026-09-07
- **Source** — 1:1 with GL (Group Software Engineering Director)
- **Theme** — The immediate expectation is focused, proportionate progress rather than trying to solve every quality problem at once. GL encouraged taking care of personal wellbeing, starting with tactical improvements that can make an immediate difference, and developing the larger strategic foundations in parallel, including environments. He is available between the planned fortnightly 1:1s when support is needed, particularly around the first significant strategic change.
- **Theme** — Quality should be experienced more like a member experiences it, especially on mobile. The direction is to identify fewer, more valuable tests rather than accumulate broad coverage without clear value. Business-critical journeys should be made visible and used to communicate business readiness, with tests mapped to the risks and outcomes that matter.
- **Theme** — Leadership visibility should be purposeful and useful rather than reporting for its own sake. GL wants visible ownership of a communication stream that establishes credibility; a future quality report for senior leaders could be valuable if it explains quality, risk, and readiness in a way that supports decisions.
- **Theme** — Automation is worthwhile where it adds business value, but it is expensive to create and maintain. The right balance is to understand the value and risk of each functional area first, then use that to decide where automated tests provide meaningful confidence.
- **Theme** — The Web 3 mission is focused on the Portal. The immediate capability question for DA is therefore becoming familiar with the Portal and its member journeys, rather than treating Web 3 as an abstract or broad technology area. There may be useful overlap with Payments and Mobile because MP and TMW work on features that connect to or intersect with Portal journeys.
- **Implication** — Work should be framed at two levels: small tactical changes that improve information flow, member realism, and immediate confidence, alongside a focused strategy for environments, critical journeys, automation value, and business readiness. Use the first visible wins to build trust and create a credible basis for wider change.
- **Implication** — A fortnightly leadership conversation is the default rhythm, with direct contact when a decision or strategic change needs support. The role should make progress visible through useful evidence and communication, while keeping the emphasis on outcomes, member value, and decisions rather than activity metrics.
- **Implication** — Support DA with a practical Portal familiarisation path and use shared Portal-related journeys to create learning and collaboration across Website, Payments, and Mobile. Validate the overlap through the planned deep dives rather than assuming that platform adjacency automatically provides the required knowledge.

### 2026-09-03 — Organisational reshuffle: closer to the business and more in-house technical ownership

- **Date** — 2026-09-03
- **Source** — Engineering director update following the organisational reshuffle
- **Theme** — The new structure brings engineering closer to the business and to decision makers who can maximise the impact of the team's work. The organisation should operate as a more autonomous function, drawing on its own expertise, collaborating directly, and making sensible decisions at pace. The broad architecture is in place, with Operations and Security supporting the function; specific architectural, product, or design blockers should be escalated to the named engineering leaders and director. Issues previously taken to the architecture council should now go to the Tech Lead Chapter.
- **Implication** — Build direct, purposeful relationships with business stakeholders rather than relying on a Product intermediary by default, while keeping ownership of priorities and decisions explicit. Support engineering-led design decisions with lightweight records, shared technical context, and early consideration of quality, operability, security, and testability. Use the Tech Lead Chapter for shared technical challenges without recreating a slow approval forum.

---

### 2026-08-11 — London Tech Leaders: The CTO Lens Podcast

- **Date** — 2026-08-11
- **Source** — London Tech Leaders — The CTO Lens Podcast, guest GL (Group Software Engineering Director, PureGym)
- **Theme** — PureGym’s technology is not a shiny innovation platform; it is the low-cost membership engine that makes the business work: digital join flow, member portal, access, retention, pricing discipline, and an operating model built for scale. GL framed engineering as a business enabler: teams need to stay tightly aligned to value, cost, and growth, not just build for the sake of building. He also described AI as an unavoidable shift in how engineering work is done — not a replacement for what matters, but an amplifier of the need for clear business alignment, critical review, and human connection. He emphasised that the craft of engineering is changing: more of the work is becoming orchestration, review, and judgment, while AI handles more of the drafting and repetitive production tasks.
- **Implication** — For this role, the key implication is that senior engineering and QA leadership must keep the team anchored to business value, quality, and operating reality rather than being seduced by broad AI hype or overbuilding. The right response is selective adoption: measure AI use, provide tooling, train people, and make it part of progression without losing standards and human judgment. The most important leadership signal is to protect purpose, manager quality, and team connection as AI compresses more of the production work, because the enduring differentiator becomes clear thinking, strong judgment, and being close to the business outcome.
- **My read** — This was the clearest articulation so far of the shift happening in senior engineering leadership: less about a heroic engineering culture, more about a business-aware operating model. GL’s framing resonated because it turns technology into a means for the business to scale sensibly rather than an end in itself. The most useful part was his point that AI is not just changing how code is written, it is changing how engineers work day to day — managing multiple AI outputs, triaging generated work, reviewing more code, and paying attention to context, quality, and business outcomes. The craft is not disappearing; it is evolving into something more managerial and more judgment-heavy. The “be honest, label the changes, protect time” point was equally relevant: for a team leader the biggest risk isn’t that AI replaces people, it’s that people become overrun by noise, context switching, and the feeling that they are constantly managing work rather than doing real thinking. Practical follow-ups: anchor the team to business value rather than output; treat AI adoption as a management and quality issue rather than a tooling one, with expectations, measured usage, and protected review standards; actively design for calm, focused work and clear priorities; keep purpose visible; and differentiate hype from real leverage by proving a small number of targeted experiments before expanding. Worth revisiting as a reference point for leading through transformation without losing team quality or culture.

---

### 2026-08-11 — Additional leaders’ themes from the same podcast

- **Date** — 2026-08-11
- **Source** — London Tech Leaders — The CTO Lens Podcast, GL
- **Theme** — As companies scale, culture must be actively redesigned rather than inherited. GL described the need to keep the best of the past while leaving behind overbuilt structures, excessive process, and low-value complexity. He also highlighted a real shift in team expectations: engineers are increasingly managing a “mini virtual team” of AI agents, reviewing outputs, coordinating workflows, and staying in constant context-switching mode. In that environment, the people skill becomes critical because the business still needs trust, clear communication, and the ability to turn technical work into measurable value.
- **Implication** — This matters for direction-setting in a leadership role: keep the team lean, outcome-focused, and business-connected; avoid treating AI as an excuse for more noise or faster output without clarity; and invest in manager quality, team health, and intentional learning. The risk is not only productivity loss but a drift into “everyone is managing everything,” which can strip away flow and craft. The antidote is disciplined focus, transparent prioritisation, and a deliberate effort to retain purpose and connection as the work becomes more AI-mediated.

---

### 2026-07-29 — C-suite leadership call after organisational restructure

- **Date** — 2026-07-29
- **Source** — C-suite leadership call led by the COO, the CTO, and the CEO, following the removal of several leadership layers and a move to a simpler senior structure. The CTO is the manager of my manager.
- **Theme** — The business is organised around three strategic priorities: grow, improve, and simplify. The stated North Star is to be the best gym and fitness business in the world, with high standards, high support, low ego, and people flying in formation behind clear decisions. Technology is an enabler, not the objective: members care about joining easily, paying easily, and having a consistently good end-to-end experience. Growth through new markets and acquisitions requires repeatable, integrated infrastructure that can be deployed quickly and operated efficiently. Simplification means removing unnecessary complexity, bringing leaders closer to the business and members, making decisions faster, and giving more responsibility to people lower in the organisation.
- **Theme** — the CTO strongly positioned AI as a major opportunity for PureGym. He wants people to get involved quickly, experiment with the available tools, share learning, and use AI to simplify routine work, increase the speed and quality of decisions, and create more time for ideation and improvement. He connected this directly to the importance of an integrated data spine: AI will only be as effective as the quality, accessibility, and connectedness of the underlying business data and systems.
- **Implication** — QA must always be rooted in member value. Quality is not a property of a technical project in isolation; it is confidence that the member can join, pay, access the service, and move through the wider experience simply and reliably. When shaping quality work, make the member outcome and business value explicit, then use that to decide what to test, automate, measure, or simplify.
- **Implication** — Expansion readiness is a quality concern. As PureGym enters markets and integrates acquisitions, QA should help identify the repeatable capabilities, data dependencies, operational risks, and end-to-end journeys needed to launch and scale without adding unnecessary complexity. The goal is not maximal process or coverage everywhere; it is reliable, adaptable foundations that support rapid growth.
- **Implication** — The new structure creates permission and expectation for faster, more direct decision making and broader ownership. Take problems to the right people early, make pragmatic decisions within the available context, and step beyond narrowly defined role boundaries when the outcome needs it. This creates opportunity for people who can combine hands-on involvement with good judgment and visible delivery.
- **Implication** — AI adoption should be treated as part of how the function improves, not as a separate innovation programme. Use it where it removes toil, improves analysis, strengthens test thinking, or accelerates feedback, while preserving human accountability for risk, quality, and the member experience. The CTO’s enthusiasm makes this an important leadership signal, but adoption still needs to be tied to measurable outcomes rather than tool activity.

---
