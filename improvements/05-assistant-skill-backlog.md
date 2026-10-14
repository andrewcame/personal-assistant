---
id: IMP-05
type: improvement
status: in-progress
horizon: none
updated: 2026-10-14
pillars: []
focus: [productivity]
goals: []
links: []
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

## Status & Next Action

**Status:** In progress

**Next action:** Use the weekly-review skill for two consecutive Fridays and the gap-analysis skill before the next GL 1:1; keep, adjust, or drop each based on real use. Run eval cases E01–E04 once in Copilot and once in Claude to set a baseline.

## Outcome

- Completed:
- Logged achievement:
