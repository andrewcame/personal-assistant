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

The focus area is the **category** shown on every dashboard card. It is stored in the `focus:` front-matter of each challenge and improvement (and in the Focus column of the horizons tables).

## Hierarchy: Sources, Then A Challenge Or Improvement, Then Tasks

1. A **source** (a call, something management said, an industry signal, the job spec, the 30/60/90-day plan, something AC said he'd do, a Notion idea) leads to a **challenge** (an issue to fix) or an **improvement** (something to change). A plan item or job-spec gap with no record is a source: open a record for it, assumed required until AC closes it as already done.
2. Each is tracked through **tasks**: Notion To Do cards for AC, roadmap steps owned by others (monitored). Progress is recorded on the challenge or improvement. Ad hoc small tasks are not tracked here.
3. If delivery needs code or other changes, it is a **Jira initiative**, tracked only in Jira. It shows on the record as the optional `jira:` label; there is no initiative record. (INI-01 and INI-02 were folded into IMP-02 and CH-09 on 2026-11-04; their source briefs are in [jira-initiatives](jira-initiatives).)
4. When the record closes, `outcome:` says where the result landed: `achievement` (AC's log), `evidence` (a team member's Year-End Evidence), `both`, or `none`.

| Field | On | Meaning |
|---|---|---|
| `tag: Short label` | Challenge, improvement (required while live) | 1–3 word label. Notion `Record` values are `<ID> <tag>` (e.g. `IMP-02 Member data`); agents and the dashboard read the ID from the start of the value. Unique across records. |
| `jira: [KEY, …]` | Challenge, improvement (optional) | Jira epic or ticket keys delivering it (e.g. `[APP-352, APP-353]`). Shown on the card. |
| `jd: [JD-NN]` | Challenge, improvement (optional) | The job-spec responsibilities this delivers. `check.py coverage` lists responsibilities no open record carries. |
| `outcome: achievement \| evidence \| both \| none` | Closed challenge or improvement | Where the result landed; set by Capture on closing. `check.py` warns if missing. |

## Plan Items And Job-Spec Gaps

Every row in the Now / Next / Later tables of [horizons.md](my-role/horizons.md) is carried by a challenge or improvement (`check.py` errors otherwise). A job-spec (`JD-`) responsibility that no open record carries shows in `python scripts/check.py coverage`; the monthly horizon review turns each into an improvement or challenge.

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

Derived from the file number in each folder — no separate registration needed. Retired IDs are never reused: **CH-06** (retired 2026-10-14; person-specific content moved to the team profile); **INI-01** and **INI-02** (retired 2026-11-04; initiatives are now a `jira:` label on the parent: INI-01 became IMP-02, INI-02 became CH-09, and older notes that mention them stay valid).

| Prefix | Folder                                   | Example  |
|--------|------------------------------------------|----------|
| CH-    | [challenges](../challenges)              | CH-07    |
| IMP-   | [improvements](../improvements)          | IMP-02   |
| DC-    | [discovery-calls](discovery-calls)       | DC-2026-09-16-cr (date + slug) |

## Roadmap Steps (CII)

Every challenge and improvement (a **CII**) carries a `## Roadmap` table: the ordered steps to completion. Step IDs extend the record ID (`IMP-02.1`, `IMP-02.2`); never renumber, append instead.

| Column | Meaning |
|---|---|
| ID | `<record ID>.<n>` |
| Step | Short outcome, verb-first |
| Owner | Alias (`AC`, `DA`, …) |
| Depends on | Step IDs (any record) or `—` |
| Status | `done` · `doing` · `next` · `later` · `blocked` · `dropped` (no longer needed; keep the row for history) |
| Ticket | Optional. Jira key once the step is raised (e.g. `PICO-123`); shown on the dashboard as the card's next ticket. `—` if none yet |
| Card | Optional. The exact title of the Notion To Do card for the step; the Tasks section of the dashboard matches it against the Notion snapshot to show whether the step is on Notion. `—` if none yet. Several steps may name the same card. An open card tagged to the record that no step names is added to the roadmap by notion-sync as a new step |

- **First up** = steps with status `doing` or `next`. Every CII in the Now or Next horizon (unless `on-hold`) must have at least one, and each first-up step should have an open Notion card tagged with the record ID (named in `Card`; "Monitor …" for a step owned by someone else). The agent creates the first card, then the next when it is Done; later steps need no card yet.
- Cross-record dependencies (e.g. `IMP-02.8` depends on `CH-10.3`) are kept in the roadmap tables. The first `doing` (else `next`) step is the card's **next ticket** on the Plan.

## Status Values

| Record      | Allowed status                                              |
|-------------|-------------------------------------------------------------|
| Challenge   | `open`, `active-monitoring`, `resolved`, `closed`           |
| Improvement | `not-started`, `in-progress`, `on-hold`, `blocked`, `done`  |
