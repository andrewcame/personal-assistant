---
id: DC-2026-09-14-technical-lead-cms-payload
type: discovery-call
date: 2026-09-14
pillars: [P2, P5, P8, P9]
focus: [people, ownership, automation]
links: [CH-03, IMP-01]
people: [GL, JS, GD]
---

# 2026-09-14 - Technical Lead Engineer CMS (Payload) - GD

## Call Context

- **Date:** 2026-09-14
- **Source / role:** Technical Lead Engineer, CMS (Payload specialist)
- **Conversation type:** Engineering discovery
- **Related team or platform:** Payload CMS, Payload Adapter, Kafka event store, Cloudflare, website/app/portal, environments (preview/staging/prod)
- **Notes based on:** Questions sent ahead of call + written responses (GD) + follow-up dictation

## Purpose

- Understand how Payload CMS works, how it integrates with the rest of the platform (event-driven architecture via Kafka), where the testing blindspots and risks are (localization/multitenancy, regression, environment parity), and how content/version changes are managed operationally.

## Key Signals

### What Matters To Them

- Localization and multitenancy correctness: whether new features/fields introduced in Payload are relevant and correctly localized/scoped per tenant.
- Not blindly copying data between environments (e.g. prod to test) without a considered process — has seen this done via AI tooling (Claude) by another engineer and is wary of the risk.
- Wants environment alignment between preview/staging/prod to extend to the underlying Payload environments (dev Payload, test/staging Payload, prod Payload) rather than just the app layer.
- Wants JS's (tester) deep Payload knowledge shared more widely rather than concentrated in one person.

### Current Friction Or Risks

- **Static site build dependency:** The website is statically built, so a content change made in Payload is not visible until a rebuild runs — a structural limitation, not a bug, but a source of confusion/failed expectations.
- **Content key vs content value confusion causing test failures:** GL raised a challenge where content changes triggered test failures; investigation suggests failures were caused by incorrect content *keys*, not the content itself — a distinction that isn't obvious to engineers/stakeholders and can look like a flaky or unfair test failure.
- **Environment topology gap:** Only three real environments exist end-to-end — dev, staging (test), and production — and Payload itself is hosted by a third party with no on-demand environments. There isn't a clean 1:1 mapping today between Pico's preview/staging/prod and Payload's own dev/test/prod instances.
- **No content ownership model post-"products":** Now that "products" (as a concept/team) have gone, there's a gap in who owns keeping content aligned across environments. Two options floated: developers update preview while doing the work, and business owners update staging — but the likely reality is developers end up doing both, which isn't sustainable or correctly owned.
- **Payload version upgrades require full manual regression:** When the underlying Payload software version increments, a full manual regression pack is currently required. No automation exists for this today. JS holds most of the detailed knowledge and notes on this.
- **No direct automation of the CMS in isolation:** Payload only has real test value when exercised through the systems that consume it (website, app, portal) — there's no meaningful way to automate/test it standalone.
- **Knowledge concentration:** JS knows the Payload/CMS domain well but this knowledge is not well distributed across the team.

### What Is Working Well

- **Front-end schema validation against live CMS:** The front-end pack downloads the Payload CMS schema and validates fields against it dynamically, rather than hardcoding field/label names — so the UI always pulls the "real" field (e.g. member label) rather than a hardcoded guess. This meaningfully reduces one class of drift risk.
- **Event-driven decoupling via Payload Adapter:** Payload is decoupled from Kafka via a dedicated Payload Adapter service that subscribes to Kafka and forwards events to Payload through a webhook (`{PAYLOAD_BASE_URL}/api/webhook`), rather than Payload consuming Kafka directly. This is deliberate given Payload's early/immature integration maturity.
- **Clear ownership boundary with the third-party vendor:** Payload is hosted and developed by a third-party vendor; the team is a large/influential customer able to help shape the roadmap, but doesn't own the infrastructure itself.
- **Documented adapter contribution workflow:** Payload Adapter has a documented setup (bootstrap repo, PAT-based NuGet auth, PR-based preview environment spin-up, image tag promotion via `payload-adapter.yaml`, ArgoCD monitoring) and dedicated environments per stage (`payload-adapter.preview/staging/prod.*`).

### What They Asked For / Suggested

- Better shared understanding across the team (not just JS) of how Payload versioning/regression and CMS integration work.
- A more deliberate approach to environment/content alignment between staging and prod — ideally without resorting to blind prod-to-test data copying.
- Someone to think through and propose a clearer content ownership model now that "products" no longer own this.
- Interested in whether AI could help with the Payload version-upgrade regression pack, even though no automation currently exists for it.
- Wants QA more actively involved in First Responders — the rotating pair who monitor live services/app, identify issues, and raise/triage bugs across teams. I agree with this ask.

## Themes And Interpretation

- Directly stated: the website's static build means content changes are not immediately live — this needs to be common knowledge to avoid false "why hasn't my change appeared" reports.
- Directly stated: GL's test failures after a content change were most likely caused by incorrect content keys, not incorrect content — a nuance worth surfacing so it isn't mistaken for automation flakiness.
- Directly stated: Payload is one of three systems (website, app, portal) that will eventually consume the CMS data; the data shape is intentionally engineered by the team, not a raw off-the-shelf capture.
- Directly stated: environment parity is harder here because Payload itself is a third-party hosted product with only dev/test/prod instances, and today there's no clean alignment between those and Pico's own preview/staging/prod.
- My interpretation: this is a strong candidate addition to the existing environment/architecture-ownership challenge — the CMS adds a *fourth* environment axis (its own dev/test/prod) that must be reasoned about alongside preview/staging/prod, distinct from the payments/Exerp environment gaps already logged.
- My interpretation: the "content key vs content value" distinction is a knowledge/documentation gap more than a technical one — a short internal note here could prevent repeat confusion and defensive reactions to test failures.
- My interpretation: the missing content ownership model (post-"products") is a genuine organisational gap, not just a testing concern, and should be raised as a cross-functional follow-up rather than something QA solves alone.
- Hypotheses to validate: AI-assisted regression support for Payload version upgrades could reduce the manual pack effort, but this needs JS's domain input to scope properly.
- Hypotheses to validate: the front-end's dynamic schema-validation approach could be extended or referenced as a pattern for other CMS-adjacent integration risk (e.g. localization checks per tenant).
- My interpretation: QA joining First Responders is a natural extension of the staging monitoring/alerting ownership work already underway — starting QA as "first responders for staging" builds the operational understanding and trust needed before extending into production First Responders.

## Mapping

### Strategic Mission(s)

- Technical Mastery & Foundations
- Business Risk & Stakeholder Trust
- People & Practice

### Role Pillar(s)

- Test Infrastructure, Environments & Data
- Business-Critical Journey Protection
- Knowledge Sharing & Quality Practice
- AI-Enabled Testing & Innovation

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

- **Add Payload's own dev/test/prod environment axis to the environment/architecture ownership challenge** — Owner: AC — Destination: Notion / Challenge [03-in-house-architecture-decisions.md](../../challenges/03-in-house-architecture-decisions.md) — Notes: CMS environments don't currently map cleanly to Pico preview/staging/prod.
- **Document the "content key vs content value" test-failure distinction** — Owner: AC / JS — Destination: Notion / Knowledge share — Notes: Prevent repeat confusion when content-driven test failures occur (per GL's earlier challenge).
- **Propose a content ownership model now that "products" no longer own it** — Owner: AC — Destination: Notion / Ways of Working — Notes: Decide who updates staging vs preview content going forward; avoid default-to-developer ownership.
- **Explore AI-assisted support for Payload version-upgrade regression pack** — Owner: AC / JS — Destination: Notion / Improvement — Notes: No current automation exists; scope with JS's domain knowledge first.
- **Broaden Payload/CMS domain knowledge beyond JS** — Owner: AC / JS — Destination: Notion / Knowledge Sharing & Quality Practice — Notes: Reduce single-point-of-knowledge risk.
- **Trial QA joining First Responders rotation, starting with staging** — Owner: AC — Destination: Notion / Improvement [01-staging-monitoring-and-alerting-ownership.md](../../improvements/01-staging-monitoring-and-alerting-ownership.md) — Notes: Raise access/tooling needs with SRE later this week; use staging first-response as the stepping stone toward prod involvement.

## Possible Outputs

- Candidate challenge update: [challenges/03-in-house-architecture-decisions.md](../../challenges/03-in-house-architecture-decisions.md) — add CMS/Payload environment topology as a further dimension.
- Candidate improvement: AI-assisted Payload version-upgrade regression support.
- Candidate improvement: Knowledge-sharing session/documentation for Payload content keys and version-upgrade regression, led by JS.
- Candidate improvement: QA joining First Responders, starting with staging as a proving ground — ties into [01-staging-monitoring-and-alerting-ownership.md](../../improvements/01-staging-monitoring-and-alerting-ownership.md).
- Candidate goal input: Content ownership model definition across environments.

## Open Questions

- Who should ultimately own content parity between staging and prod now that "products" no longer exists as a function?
- Is there a safer, non-AI-tool-dependent way to selectively align content between environments without a full blind copy?
- What would a minimal automated check look like to catch localization/multitenancy gaps when a new field/feature is introduced in Payload?
- How should regression scope change specifically when a Payload version upgrade happens, versus a standard content/feature change?
