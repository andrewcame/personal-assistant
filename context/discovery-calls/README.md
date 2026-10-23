# Discovery Calls

This folder captures structured notes from external role discovery conversations: engineering leadership conversations, platform/SRE context, and stakeholder discovery.

These are not transcripts. They are interpreted notes used to identify themes, risks, opportunities, and follow-ups for the QA & Test Engineering Manager role.

## Use This For

- First 30-day discovery conversations
- Staff Engineer, Principal Engineer, Delivery, Product, Finance, Commercial, or stakeholder calls
- Repeated friction points, system risks, and strategic opportunities
- Inputs that may later become goals, challenges, decisions, or achievements

## Do Not Use This For

- Routine 1:1 notes or private pastoral detail
- Delivery task tracking
- Full meeting transcripts
- Action lists that belong in Notion, Jira, or Teams

## Suggested File Naming

Use date-first filenames with a short source/topic:

- `2026-09-01-staff-engineer-devex.md`
- `2026-09-01-principal-engineer-sre-pico.md`
- `2026-09-02-qa-health-check-tmw.md`

## Capture Format

Use [the discovery call template](../../templates/discovery-call.md).

For QA lead and wider team health checks, use the [QA Health Summary](../qa-health-summary.md) and the individual profiles in `team/` instead.

## Captured Calls

- **2026-09-01** — Staff Engineer DevEx — [2026-09-01-staff-engineer-devex.md](2026-09-01-staff-engineer-devex.md) — Automation reporting, staging alerts, backend preview reliability, backend test coverage.
- **2026-09-01** — Principal Engineer SRE / Pico — [2026-09-01-principal-engineer-sre-pico.md](2026-09-01-principal-engineer-sre-pico.md) — Staging gold standard, Exerp/Pico data drift, member test data, Mosaic, load testing.
- **2026-09-11** — Technical Lead Engineer Payments — [2026-09-11-technical-lead-payments.md](2026-09-11-technical-lead-payments.md) — E2E test repo vs monolithic repos, 70% FE pass rate risk, preview/staging pollution, Exerp config, test tooling.
- **2026-09-14** — Technical Lead Engineer CMS (Payload) — [2026-09-14-technical-lead-cms-payload.md](2026-09-14-technical-lead-cms-payload.md) — Static build/content lag, content key test failures, CMS environment topology, content ownership gap, Payload version regression.
- **2026-09-14** — Head of Delivery (DJ) — [2026-09-14-head-of-delivery-dj.md](2026-09-14-head-of-delivery-dj.md) — Initiative lifecycle, QA not a bottleneck, earlier QA involvement in scoping, CR process proportionality, member creation initiative, delivery metrics, Cross Teams staging reporting.
- **2026-09-14** — Software Engineering Manager (Pico architecture) — [2026-09-14-sem-pico-architecture.md](2026-09-14-sem-pico-architecture.md) — Staging monitoring via reused Grafana dashboards + DLQ process, member creation Supergraph/payments limitation, Backend Chapter, phased MVP approach.
- **2026-09-15** — Head of Software Engineering (GH) — [2026-09-15-head-of-software-engineering-gh.md](2026-09-15-head-of-software-engineering-gh.md) — New weekly Friday cadence, QA resourcing model, staging + app alerting ownership, Appium AI experiment, AI-usage-as-skills model.
- **2026-09-16** — IT Pricing Manager (CR) — [2026-09-16-it-pricing-manager-cr.md](2026-09-16-it-pricing-manager-cr.md) — Member-centred pricing/configuration testing, COP and Exerp data flows, staging configuration, Extractor reliability, change communication.
- **2026-09-16** — Technical Lead Engineer Mobile / RSR Lead — [2026-09-16-technical-lead-mobile-rsr.md](2026-09-16-technical-lead-mobile-rsr.md) — Mobile delivery speed, Appium strategy, layered mocked testing, Apps QA capacity, shared automation ownership, QA/SRE chapter value.
- **2026-09-17** — Principal Engineer SRE / Pico (follow-up) — [2026-09-17-principal-engineer-pico-backend-testing-strategy.md](2026-09-17-principal-engineer-pico-backend-testing-strategy.md) — Pico/Exerp alignment, deployed-preview integration coverage, test stability, and shared web/app ownership.
- **2026-09-18** — Technical Lead, Joint Funnel / Corporate Membership Types — [2026-09-18-technical-lead-joint-funnel.md](2026-09-18-technical-lead-joint-funnel.md) — DevQA capacity and culture, actionable test notes, quality-at-speed trade-offs, preview environments, and DJ's existing feature map.
- **2026-09-23** — Head of Configuration — [2026-09-23-head-of-configuration-exerp-release-testing.md](2026-09-23-head-of-configuration-exerp-release-testing.md) — Exerp release visibility, upgrade testing, ticket ownership, environment rationalisation, and app-testing support.
- **2026-09-23** — Technical Lead, Backend / Portal — [2026-09-23-technical-lead-backend-portal-wundergraph.md](2026-09-23-technical-lead-backend-portal-wundergraph.md) — Wundergraph-to-Kafka coverage, integrated preview environments, Supergraph test data, and complete member creation.
- **2026-09-24 capture (original call date to confirm)** — Delivery Manager, App / Pay / Web 3 (retrospective) — [2026-09-24-retrospective-delivery-manager-app-pay-web-3.md](2026-09-24-retrospective-delivery-manager-app-pay-web-3.md) — Web 3 QA gap, ticket fragmentation, coherent validation units, workbook evidence, and a 30-day QA flow baseline.
- **2026-09-25** — Technical Lead, Pico Backend / Legacy Portal Architecture — [2026-09-25-technical-lead-pico-backend-legacy-architecture.md](2026-09-25-technical-lead-pico-backend-legacy-architecture.md) — Pico/Exerp integration boundaries, legacy portal architecture, test environments, automated integration testing.
- **2026-10-21** — Annual conference team conversations — [2026-10-21-annual-conference-team-conversations.md](2026-10-21-annual-conference-team-conversations.md) — Speed vs quality and AI over-use as common themes; test-in-prod/SRE with mocking vs real Exerp integration debate.
- **2026-10-13** — Environments discussion — [2026-10-13-environments-exerp-per-brand.md](2026-10-13-environments-exerp-per-brand.md) — One Exerp test environment per brand, Exerp event broadcaster, pico.deployment full-stack previews, Payments/Kafka blocker.
- **2026-10-09** — Dootrix AI Harness (supplier knowledge sharing) — [2026-10-09-dootrix-ai-harness.md](2026-10-09-dootrix-ai-harness.md) — Harness structure, activity-based skills, scripts alongside skills, cross-model review, self-learning loop, QA architect role.

## How To Use These Notes

When reviewing discovery notes, look for:

- repeated pain points across different sources
- confidence gaps in automation, environments, data, or release readiness
- risks tied to business-critical journeys
- opportunities that map to the strategic missions and role pillars
- follow-ups that should become challenges, decisions, or goals

Keep interpretation separate from what was directly said. When in doubt, mark something as a hypothesis to validate.
