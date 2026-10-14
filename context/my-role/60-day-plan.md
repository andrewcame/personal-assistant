# 60-Day Plan: Stabilise and Reduce Friction

> **Archived onboarding record.** The live plan is now [horizons.md](horizons.md) (Now / Next / Later). Keep this file as review evidence; don't add new progress here.

## Phase Intent

By day 30 there should be a clear understanding of the team's challenges, the biggest delivery bottlenecks, and where the organisation lacks confidence. This phase addresses the most impactful findings and reduces friction for QA and engineering in the most targeted way possible. Not everything will be solved — the goal is to move on the highest-value problems first.

## Automation

- Establish visibility of what is actually being protected: not just web and app journeys, but member communications, market-specific behaviours, and business-critical flows — including which international markets have meaningful coverage and which do not
- Aim for a centralised place that lists what runs, how often, and latest results — full wider visibility may not be achievable by day 60 but centralisation is the target
- Establish a clear ownership model by domain: each lead becomes responsible for the automation code in their area; agree how shared areas (e.g. IDS) are co-owned so that shared responsibility does not become no responsibility
- Identify flaky test packs and agree a response: easy fixes go straight to the backlog; anything harder gets assessed for value before committing resource; engineering support can be requested where needed
- Agree and set standards for agentic AI test creation across the team; Appium is the candidate for a first POC
- Define the CI/CD quality gate model: what automated signals are visible to engineers throughout the pipeline, not just at the end? Agree the standard and identify the gaps between current state and target

## Environments and Data

- Use the environment health findings from the first 30 days to drive meaningful resolution conversations — is the impact large enough to justify investment? Aim high (scaled prod-like environments) but review based on need, value, and cost; reporting on environment health is a key output
- Agree a test data strategy: real live data with Exerp copy-back protection, or team-owned seeded data? Aim for alignment across teams rather than platform-by-platform divergence
- Explore the use of AI in either approach — agent-driven data discovery or automated reseeding on copy-back cycles

## NFRs and Quality Standards

- Partner with the Head of Software Engineering and Principal Software Engineer to understand the current state of NFR coverage: uptime, API performance, accessibility (WCAG 2.1 AA), and the quality signals feeding into DORA metrics
- Identify which NFR areas have clear ownership and measurement and which are opaque or unmeasured
- Agree a baseline and a direction of travel — this does not need to be solved by day 60 but the partnership and shared understanding should be established

## Stakeholder Continuity

- The Finance and payment partner relationships introduced in the first 30 days should move beyond introductions by this point — agree a regular cadence for coverage updates ahead of significant releases or payment system changes
- Ensure commercial and market teams have a clear point of contact and understand what quality visibility they can expect before market launches
- Feed findings back to engineering and business stakeholders to confirm priorities and ensure focus is on areas that genuinely affect delivery confidence

## Lead Alignment

- Build a common priority list from the first 30-day findings; work from a shared backlog of activity and support each other where capacity allows
- Identify champions within the team who are enthusiastic about AI and emerging tooling so that innovation comes from the team rather than being imposed on it
- Drive consistency between platforms in the standards held, even where platform challenges differ between Web, Mobile, and Payments
- Align on consistent leadership: how things are built and how teams are managed; the team should have a consistent experience regardless of who they report to — same goals, expectations, coaching approach, and technical direction
- Feed findings back to engineering and business stakeholders to confirm priorities and ensure focus is on areas that genuinely affect delivery confidence

## Outputs

- Shared goals across the QA leads
- Improved ownership of technical domains
- Reduced siloed behaviour
- CI/CD quality gate model defined
- NFR partnership established with Head of SE and Principal SE
- Stakeholder coverage cadence agreed with Finance and commercial teams
