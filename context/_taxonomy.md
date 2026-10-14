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

## Status Values

| Record      | Allowed status                                              |
|-------------|-------------------------------------------------------------|
| Challenge   | `open`, `active-monitoring`, `resolved`, `closed`           |
| Improvement | `not-started`, `in-progress`, `blocked`, `done`             |
| Initiative  | `draft`, `submitted`, `in-progress`, `done`, `rejected`     |
