---
id: IMP-05
tag: Assistant
type: improvement
status: in-progress
horizon: next
updated: 2026-11-10
pillars: [P9]
focus: [productivity]
jd: [JD-07]
goals: []
links: [CH-13, IMP-16]
people: []
---

# Improvement 05 — Assistant skill backlog

## Context

The repository currently uses five role-based agents. A small number of reusable procedures may be better expressed as workspace skills so they can be applied consistently across agents and requests.

## Objective

Identify and add only the skills that remove repeated procedural guidance without turning the repository into a complex multi-agent system.

## Related

- Goal(s):
- Role pillar(s):
- Originating recommendation: self

## Actions & Progress

### 2026-09-30

- Added `.github/skills/industry-research/SKILL.md` for source-backed external research and industry-signal drafting.
- Added `.github/skills/action-extraction/SKILL.md` for read-only extraction of forgotten actions into a Notion-ready handoff list.
- Potential follow-up skills:
  - Repository health and context consistency audit
  - Shared signal-to-record routing guidance for Capture and related agents
  - Evidence extraction and normalisation before review drafting
  - Challenge and improvement lifecycle validation

### 2026-10-14

- Harness restructure, informed by the [Dootrix AI harness call](../context/discovery-calls/2026-10-09-dootrix-ai-harness.md) (activities not personas; scripts alongside skills; retrieve rather than load everything).
- Backlog candidates delivered as a script rather than skills: repository health audit and lifecycle validation are now `scripts/check.py` (validate, index, coverage, stale).
- Added a taxonomy of stable IDs, front-matter on records, achievement tag lines, a people alias lookup, `state/now.md` working memory, and a condensed `context/role-brief.md`.
- Added three activity skills: `weekly-review`, `gap-analysis`, `horizon-review`.
- Remaining candidates: shared routing guidance (partly covered by Capture's routing table), evidence extraction before review drafting (partly covered by tags + gap-analysis).

### 2026-10-14 (phase 4)

- Added root `AGENTS.md` (shared instructions for Copilot and Claude) and `CLAUDE.md` importing it.
- Added a learning loop: `state/learnings.md` (propose → accept → consolidate at horizon review), seeded with today's corrections.
- Added `evals/` with ten behaviour cases (privacy, routing, reasoning, learning loop) and a results log.

### 2026-10-16 (ideas triage)

_From the Ideas triage on 2026-10-16 ([ideas log](../state/ideas-log.md))._

- **QA harness ahead of GL's:** following the Dootrix harness discussion, GL plans a PureGym harness next year. QA could get ahead by defining a QA harness for all automation rules and standards (new step IMP-05.8).
- **Skills from each QA's best practice:** create a skill for the "best thing" each QA does; the harness might be the place for this.
- **Rovo vs Claude + MCP:** explore whether Atlassian Rovo or Claude with an MCP connection is better for Jira and Confluence (new step IMP-05.9).

### 2026-11-04 (Platform Technical Lead discovery)

Source: [2026-11-04 Platform Technical Lead](../context/discovery-calls/2026-11-04-platform-technical-lead-staging-reporting.md).

- AE gave AC access to Cloudflare's AI service: free agent tooling, paid for in credits rather than GitHub Copilot or Claude usage, with built-in controls so requests are not over-used. AC can experiment by building applications there and sharing them. Possible tool to bring to the AI chapter; AE has strong views on AI in general. Added IMP-05.10 (later).

### 2026-11-10 (2027 direction preview)

Source: [Leadership Direction, 2026-11-10](../context/leadership-direction.md); tracked in [CH-13](../challenges/13-2027-business-direction-transition.md).

- The team is expected to pivot to building agentic workflows for other areas of the business in 2027. This assistant is a working example of an agentic workflow, so IMP-05 moved from Later to Next to build capability and evidence ahead of the pivot. IMP-05.10 (Cloudflare AI trial) moved to next, with a Backlog card.

## Roadmap

| ID        | Step                                                                   | Owner | Depends on | Status | Card                                                |
|-----------|------------------------------------------------------------------------|-------|------------|--------|-----------------------------------------------------|
| IMP-05.1  | Add industry-research and action-extraction skills                     | AC    | —          | done   | —                                                   |
| IMP-05.2  | Add taxonomy, front-matter and check.py scripts                        | AC    | —          | done   | —                                                   |
| IMP-05.3  | Add AGENTS.md, learning loop and evals                                 | AC    | IMP-05.2   | done   | —                                                   |
| IMP-05.4  | Build dashboard and Notion bridge                                      | AC    | IMP-05.2   | done   | —                                                   |
| IMP-05.5  | Run evals baseline in Copilot and Claude                               | AC    | IMP-05.3   | next   | Run assistant evals baseline and first cross-review |
| IMP-05.6  | Run the first cross-review                                             | AC    | IMP-05.3   | next   | Run assistant evals baseline and first cross-review |
| IMP-05.7  | Trial weekly-review and gap-analysis; keep, adjust or drop             | AC    | —          | later  | —                                                   |
| IMP-05.8  | Scope a QA automation-standards harness ahead of GL's 2027 harness     | AC    | —          | later  | —                                                   |
| IMP-05.9  | Compare Rovo with Claude + MCP for Jira and Confluence                 | AC    | —          | later  | —                                                   |
| IMP-05.10 | Trial Cloudflare AI on a small agentic tool; share with the AI chapter | AC    | —          | next   | Trial Cloudflare AI on a small agentic tool         |

## Status & Next Action

**Status:** In progress

**Next action:** Run the evals baseline and first cross-review (IMP-05.5, IMP-05.6), and trial Cloudflare AI on a small agentic tool (IMP-05.10) to build capability ahead of the 2027 pivot.

## Outcome

- Completed:
- Logged achievement:
