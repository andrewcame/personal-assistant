---
name: action-extraction
description: "Extract forgotten actions and commitments from this assistant repo and turn them into a Notion-ready to-do list. Use when: find actions, what needs my attention, forgotten follow-ups, review open actions, extract tasks, prepare my to-do list, or audit commitments."
---

# Action Extraction

Scan the repository for recorded actions and commitments that may need attention. Produce a concise handoff list for Notion. This skill is read-only: it does not edit the repository and does not claim to create or sync Notion tasks.

## Scope

Read the current, relevant records rather than only the most recently changed file:

- `challenges/`
- `improvements/`
- `context/discovery-calls/`
- `context/leadership-direction.md`
- `context/industry-signals.md`
- `ways-of-working/`
- `team/`
- `goals/2026.md`
- recent `achievements/` entries where follow-up is still open

Use templates and surrounding context to understand whether a line is an action, a decision, evidence to gather, or background context.

## What Counts As An Action

Include items that are:

- explicitly assigned to the user
- recorded as a next action, follow-up, open item, or proposed action
- an unresolved decision the user needs to make or convene
- evidence, conversation, review, or escalation needed to move an active challenge or improvement forward
- overdue or stale work that remains open in the record

Exclude:

- completed actions
- actions owned by someone else unless the user needs to chase, support, or decide something
- routine task lists that belong in Notion and are only mentioned as background
- speculative ideas with no commitment or clear next step
- duplicate mentions of the same action

## Extraction Method

1. Scan the scoped folders and files for action language such as `next action`, `follow-up`, `open question`, `open item`, `candidate`, `should`, `need to`, `review`, `check`, `raise`, `agree`, `define`, and `validate`.
2. Read enough surrounding context to identify the actual outcome required.
3. Deduplicate actions across records and keep the clearest source.
4. Infer urgency only from dates, status, explicit sequencing, or leadership direction. Label other urgency as unknown rather than guessing.
5. Separate a single actionable outcome from background context. Split compound actions only when they have different owners or destinations.
6. Preserve uncertainty and flag where the user needs to clarify ownership, scope, or timing.

## Output

Start with a short summary:

- Actions found:
- High-attention items:
- Stale or ambiguous items:
- No-action conclusion, if nothing needs attention:

Then provide a flat, Notion-ready list. For each item include:

- **Action:** begin with a verb and make it specific
- **Why it matters:** one short sentence
- **Source:** link to the repository file
- **Status:** Not started / In progress / Blocked / Waiting / Stale
- **Suggested priority:** High / Medium / Low / Unknown
- **Suggested timing:** only when supported by the record
- **Dependency or owner:** if recorded
- **Notion notes:** concise context needed to act

Order by suggested priority, then by explicit timing, then by staleness. Do not convert every open question into a task: retain it as an open question when it needs discovery before commitment.

## Safety Rules

- Do not invent due dates, owners, priorities, or commitments.
- Mark inferred fields as suggested and explain the evidence briefly.
- Do not edit source records.
- Do not call, imply, or simulate a Notion integration.
- Do not include sensitive personal detail unless it is necessary to understand the action.
