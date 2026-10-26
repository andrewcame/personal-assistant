# Taxonomy — Stable IDs

The single source of IDs used in front-matter, achievement tag lines, and cross-references. Scripts in [`scripts/`](../scripts) validate against this file, so **add an ID here before using it anywhere else**. Never reuse or renumber an ID; retire it instead.

Full descriptions live in the linked source files; this file holds only the ID and a short label.

## Job Description Responsibilities (`JD-`)

Source: [job-specification.md](my-role/job-specification.md)

| ID    | Area                  | Responsibility (short)                                            |
|-------|-----------------------|-------------------------------------------------------------------|
| JD-01 | People Leadership     | Line manage Lead QAs (1:1s, performance, development, pastoral)    |
| JD-02 | People Leadership     | Support leads in developing their practitioners                    |
| JD-03 | People Leadership     | Growth framework, progression, promotion cases                     |
| JD-04 | People Leadership     | Hiring, onboarding, QA talent pipeline                             |
| JD-05 | Technical Ownership   | Full-stack test automation frameworks                              |
| JD-06 | Technical Ownership   | Test infrastructure: accounts, seed data, environment parity       |
| JD-07 | Technical Ownership   | AI-driven testing adoption                                         |
| JD-08 | Technical Ownership   | Quality in CI/CD: runs, coverage signals, quality gates            |
| JD-09 | Standards & Strategy  | Quality standards and test strategy                                |
| JD-10 | Standards & Strategy  | Lead the QA Chapter / community of practice                        |
| JD-11 | Standards & Strategy  | NFR partnership: uptime, API performance, accessibility, DORA      |
| JD-12 | Delivery Partnership  | Support squads; surface risk early; data-grounded release readiness|
| JD-13 | Delivery Partnership  | Shift QA left into a shared discipline                             |
| JD-14 | Delivery Partnership  | Agentic AI test boilerplate from requirements                      |
| JD-15 | Stakeholders          | Agree coverage expectations with Finance, payments, commercial     |
| JD-16 | Stakeholders          | Business-language quality visibility before releases/launches      |
| JD-17 | Stakeholders          | Trusted relationships with non-engineering stakeholders            |

## Strategic Missions (`M`) and Role Pillars (`P`)

Source: [role-pillars.md](role-pillars.md)

| ID  | Label                                        | Mission |
|-----|----------------------------------------------|---------|
| M1  | People & Practice                            | —       |
| M2  | Technical Mastery & Foundations              | —       |
| M3  | Delivery Flow & Resilience                   | —       |
| M4  | Business Risk & Stakeholder Trust            | —       |
| P1  | People Capability, Progression & Succession  | M1      |
| P2  | Knowledge Sharing & Quality Practice         | M1      |
| P3  | Quality Ownership & Culture                  | M1      |
| P4  | Automation Trust & Reliability               | M2      |
| P5  | Test Infrastructure, Environments & Data     | M2      |
| P6  | Delivery Confidence & Flow                   | M3      |
| P7  | Non-Functional Quality & Resilience          | M3      |
| P8  | Business-Critical Journey Protection         | M4      |
| P9  | AI-Enabled Testing & Innovation              | M2      |
| P10 | Stakeholder Confidence & Visibility          | M4      |

## Focus Areas

Source: [horizons.md](my-role/horizons.md)

`people`, `ownership`, `automation`, `productivity`

The focus area is the **category** shown on every dashboard card. It is stored in the `focus:` front-matter of each challenge, improvement and initiative (and in the Focus column of the horizons tables).

## Hierarchy: Challenge Or Improvement, Then Tasks, Then (Maybe) An Initiative

1. AC identifies a **challenge** or **improvement** (original plan, reviews, discussions) and tracks it through **tasks** (Notion To Do cards, and roadmap steps owned by others). Progress is recorded on the challenge or improvement.
2. If delivery needs code changes or work by the team, an **initiative** is created: the higher-level work item tracked in Jira. It always comes from a challenge or improvement, which stays the record of progress. Not every challenge or improvement needs one.
3. On the dashboard the initiative is shown on its parent's card; it is never a card or a This week line of its own. Notion cards and roadmap steps on an initiative count towards its parent.

| Field | On | Meaning |
|---|---|---|
| `origin: [CH-NN / IMP-NN]` | Initiative (required) | The challenge or improvement this initiative delivers. `check.py` errors if it is missing. The dashboard derives the initiative shown on the parent from this. |
| `initiative: tbc \| needed \| not-needed` | Challenge, improvement (optional, default `tbc`) | Whether delivery needs an initiative. |
| `jd: [JD-NN]` | Challenge, improvement (optional) | The job-spec responsibilities this delivers. Used to find role expectations nothing tracks. |

## Plan Items And Role Items Without A Record

- **Plan item** — a row in the Now / Next / Later tables of [horizons.md](my-role/horizons.md) with no record in **Carried by**: something AC said he would do. Its **Source** column says where it came from (30/60/90-day plan, with a `JD-` ID if it is also a job-spec responsibility). Shown as an amber card.
- **Role item** — a `JD-` responsibility that no open challenge or improvement (`jd:`) and no plan item (JD ID in Source) covers: something the role expects that nothing tracks. Shown as a purple card with category **Role**.

Both appear under Needs attention on the dashboard until a challenge or improvement is created for them.

## Horizons

`now`, `next`, `later`

## Objective Lenses

Source: [objective-lenses.md](objective-lenses.md)

| ID | Lens               |
|----|--------------------|
| PD | People Developer   |
| VC | Value Creator      |
| BO | Business Operator  |

## Core Values

Source: [goals/2026.md](../goals/2026.md#core-values)

| ID       | Value                     |
|----------|---------------------------|
| V-DETAIL | Focus on the Detail       |
| V-WIN    | Play to Win               |
| V-SHOULDER | Stand Shoulder to Shoulder |
| V-DIFF   | Make a Difference         |

## Goals (`G`)

Source: [goals/2026.md](../goals/2026.md) — 2026 goals are provisional.

| ID | Goal |
|----|------|
| G1 | tbc  |
| G2 | tbc  |
| G3 | tbc  |

## Record IDs

Derived from the file number in each folder — no separate registration needed. Retired IDs are never reused: **CH-06** (retired 2026-10-14; person-specific content moved to the team profile).

| Prefix | Folder                                   | Example  |
|--------|------------------------------------------|----------|
| CH-    | [challenges](../challenges)              | CH-07    |
| IMP-   | [improvements](../improvements)          | IMP-02   |
| INI-   | [initiatives](../initiatives)            | INI-01   |
| DC-    | [discovery-calls](discovery-calls)       | DC-2026-09-16-cr (date + slug) |

## Roadmap Steps (CII)

Every challenge and improvement (a **CII**) carries a `## Roadmap` table: the ordered steps to completion. Step IDs extend the record ID (`IMP-02.1`, `IMP-02.2`); never renumber, append instead. **Initiatives have no roadmap.** Their status note says what happens next, and any dependency on initiative work points at the parent challenge or improvement step.

| Column | Meaning |
|---|---|
| ID | `<record ID>.<n>` |
| Step | Short outcome, verb-first |
| Owner | Alias (`AC`, `DA`, …) |
| Depends on | Step IDs (any record) or `—` |
| Status | `done` · `doing` · `next` · `later` · `blocked` · `dropped` (no longer needed; keep the row for history) |
| Ticket | Optional. Jira key once the step is raised (e.g. `PICO-123`); shown on the dashboard as the card's next ticket. `—` if none yet |

- **First up** = steps with status `doing` or `next`. Every CII in the Now or Next horizon (unless `on-hold`) must have at least one, and each first-up step owned by AC should have an open Notion To Do card tagged with the record ID. A first-up step owned by someone else is tracked as "waiting on" rather than a card.
- Cross-record dependencies (e.g. `INI-01.2` depends on `CH-10.3`) are kept in the roadmap tables; the dashboard no longer draws them. The first `doing` (else `next`) step is the card's **next ticket** on the Plan.

## Status Values

| Record      | Allowed status                                              |
|-------------|-------------------------------------------------------------|
| Challenge   | `open`, `active-monitoring`, `resolved`, `closed`           |
| Improvement | `not-started`, `in-progress`, `on-hold`, `blocked`, `done` |
| Initiative  | `draft`, `submitted`, `in-progress`, `on-hold`, `done`, `rejected` |
