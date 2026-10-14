---
name: gap-analysis
description: "Show where evidence is thin against the role: which pillars and JD responsibilities have no achievements, which have work in flight, and which are deliberately parked. Use when: gap analysis, where are my gaps, what am I missing for my review, coverage of my JD, am I balanced across pillars, what should I focus on for evidence."
---

# Gap Analysis

Read-only. Turns `scripts/check.py coverage` into a judgement about where the role's evidence is thin, and whether that's a problem or a deliberate choice.

## Inputs

1. `python scripts/check.py coverage` — achievements, live records, and discovery calls per pillar; achievements per JD item. If you cannot run commands, ask the user to run it, or count tags directly from `achievements/<year>.md` and front-matter.
2. `context/role-brief.md` and `context/my-role/horizons.md` — what the plan says matters now
3. `context/_taxonomy.md` — ID meanings
4. `achievements/<year>.md` — to check that tags are supported by the entry text

## Method

Classify every pillar and JD item into one of four states:

| State | Meaning | Typical response |
|---|---|---|
| **Evidenced** | Has achievements | Note the strongest one |
| **In flight** | No achievements yet, but live records or Now/Next items | Name what will produce evidence and roughly when |
| **Parked** | No evidence, and Later/none on the horizon, consistent with leadership direction | State it's a deliberate trade-off (e.g. behind microsite sunset) so it reads as a choice in a review |
| **Blind spot** | No evidence, no live work, not deliberately parked | Flag clearly — these are the real gaps |

Then:

1. Check balance across objective lenses (PD / VC / BO) and the time split in the role brief — e.g. heavy technical evidence but little people evidence.
2. Spot-check a few tags: if an achievement's text doesn't support a tag, say so (the fix is to correct the tag, not stretch the evidence).
3. Suggest at most three actions: evidence that probably exists but hasn't been logged (ask the user), a small piece of work that would close a blind spot, or a line to add to the horizons file to make a parked item explicit.

## Output

- A compact table: ID · label · state · one-line note
- **Blind spots** (if any) — the headline
- **Balance** — lenses and time split, two or three lines
- **Tag corrections** — if any
- **Suggested actions** — max three

## Rules

- Read-only. Don't edit files; hand off to Capture or the horizons file.
- Don't invent achievements to fill gaps. Missing evidence is information.
- Provisional goals (G1–G3) are optional in this analysis until they're agreed.
