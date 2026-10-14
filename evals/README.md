# Evals

Small, repeatable checks that the agents and skills still behave as intended. Agent behaviour drifts when instructions are edited or models change, so re-run the relevant cases after either.

## When To Run

- After editing an agent, skill, `AGENTS.md`, or the people-records standard — run the cases for that agent (privacy cases E01–E04 after **any** change).
- After switching model or tool (e.g. a Copilot model change, or moving work between Copilot and Claude).
- Quarterly, alongside the horizon review — run them all.

## How To Run

1. Pick cases from [cases.md](cases.md).
2. Paste the prompt into the named agent or skill. **Decline any save or commit** — the details are fictional.
3. Score each: **Pass**, **Partial** (minor miss), or **Fail** (any fail signal present).
4. Log the result below. For a Fail, fix the agent or skill instruction (or add a learning), then re-run that case.

**Cross-model check (optional):** run the privacy cases in both Copilot and Claude. A second model is another source of scrutiny, not proof — but differences show where the instructions are ambiguous.

`python scripts/check.py validate` is the deterministic counterpart: it checks IDs, front-matter, tags, aliases, and links on every run.

## Results Log

| Date | Tool / model | Cases | Pass | Partial | Fail | Notes / fixes |
|------|--------------|-------|------|---------|------|---------------|
|      |              |       |      |         |      |               |
