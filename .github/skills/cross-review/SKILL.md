---
name: cross-review
description: "Light second-opinion sense check of recent repo changes or a named draft, run by a DIFFERENT model family from the one that wrote it (e.g. GPT in Copilot reviewing Claude's work). Produces a short findings file for AC to comment on; makes no edits. Use when: cross-review, second opinion, sense check this, run cross-review, GPT review."
---

# Cross-Review

A short, adversarial-but-proportionate second opinion. The point is a fresh pair of eyes from a different model family, not a rewrite. Inspired by the Dootrix practice of reviewing with a different model from the one that implemented.

## Who Runs It

- **Reviewer:** a model from a different family to the author. Default: AC runs this in GitHub Copilot with a GPT model over work Claude did in Cowork (or the reverse).
- **Author:** reconciles afterwards, in the next session, using AC's comments.

## Scope

Pick one, in this order:

1. A file or draft AC names ("cross-review IMP-08", "cross-review this review draft").
2. Otherwise, everything changed since the last cross-review: find the date of the newest file in `state/cross-review/`, then `git log --since=<date> --name-only` (or files whose front-matter `updated:` is after that date).
3. If there is no previous cross-review, the last 7 days.

Skip generated files (`reports/`, index tables between `<!-- index:start -->` markers) and `context/archive/`.

## What To Check

Read `AGENTS.md`, `state/learnings.md`, and `context/role-brief.md` first. Then check the scoped files for:

1. **Accuracy** — claims, dates, owners, and numbers that aren't supported by the record's own sources or linked notes.
2. **People standard** — anything about an individual that fails the [writing standard](../../../team/README.md#writing-standard): motive, retention, pay, health, hearsay, ratings, or a real name.
3. **Consistency** — front-matter vs body (status, horizon, links); a record vs its row in `context/my-role/horizons.md`; `state/now.md` vs the records it cites.
4. **Reasoning** — a conclusion stronger than the evidence; an obvious alternative or risk not considered; an industry signal in `context/industry-signals.md` that challenges the position but isn't acknowledged.
5. **Evidence quality** — achievements or review text that overclaim, lack an impact, or tag pillars/JD items the text doesn't support.

## Output

Write **one file**: `state/cross-review/YYYY-MM-DD.md`, and nothing else.

```markdown
# Cross-review YYYY-MM-DD

- Reviewer: <tool / model>
- Scope: <what was reviewed>

| # | File | Check | Severity | Finding | Suggestion | AC response |
|---|------|-------|----------|---------|------------|-------------|
| 1 | path:line | Accuracy | Fix / Consider / Note | one or two sentences | optional wording | |

## Overall

Two or three sentences: is the work sound, and is there one thing that matters most?
```

## Rules

- **Maximum 8 findings.** Prioritise; drop trivia (typos only if they change meaning).
- **No edits** to any other file. No commits.
- Be specific and cite the line or text. Don't restate the file.
- "Nothing material found" is a valid result — say so in Overall.
- Aliases only; never quote candid language about a person.

## After The Review (author's side)

1. AC fills in **AC response** (agree / disagree / park, plus any comment).
2. In the next session, the author applies the agreed items, notes any that became learnings in `state/learnings.md`, and adds one line to the bottom of the cross-review file: "Reconciled YYYY-MM-DD: N applied, N declined."
3. Repeated findings of the same kind are a signal to update the relevant agent, skill, or learning.

## Later: Automation

A script could run this automatically by calling a second model through an API (for example GitHub Models with a personal access token) from AC's machine or a GitHub Action. It needs a token with model access and confirmation that sending repo content to that API is acceptable. Tracked in [IMP-05](../../../improvements/05-assistant-skill-backlog.md); not built yet.
