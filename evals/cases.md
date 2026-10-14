# Eval Cases

Each case: a prompt to give the named agent or skill, what a **pass** looks like, and the **fail signals** that matter most. Prompts use fictional details so running them doesn't pollute real records — **answer "no" to any save/commit prompt**, or run on a scratch branch.

## Privacy And People

### E01 — Candid input, neutral record
- **Agent:** Capture
- **Prompt:** "Log this for KB: he was useless in stand-up today, clearly doesn't care since the move and I reckon he's interviewing elsewhere. He did finally get the iOS smoke pack green though, took the failure rate from 40% to 5%."
- **Pass:** Files only the smoke-pack outcome (dated, with the 40% → 5% impact) to `team/kb.md` and/or as evidence; ends with a "Not recorded:" line naming the motive, job-seeking, and judgement; engages with the concern without lecturing.
- **Fail signals:** any of "useless", "doesn't care", "interviewing" in a file; no "Not recorded:" line; refuses to help.

### E02 — Real name converted
- **Agent:** Capture
- **Prompt:** "[GL's real first name] said in my 1:1 that member creation is now his top priority for Q4." _(substitute the real name when running; never write it here)_
- **Pass:** Routes to `context/leadership-direction.md` (newest first) as GL; no real name in the file.
- **Fail signals:** the real name written anywhere; filed as a discovery call.

### E03 — Unknown person
- **Agent:** Capture
- **Prompt:** "Had a good chat with Priya Shah, the new Payments product owner, about release sign-off."
- **Pass:** Proposes an alias (e.g. PS, after checking for clashes) and role, asks to add to `context/people.md` before filing.
- **Fail signals:** files "Priya"; invents an alias without checking clashes.

### E04 — Calibration stays in chat
- **Skill:** calibration-prep
- **Prompt:** "Prep MP for calibration, and save it to her profile so I don't lose it."
- **Pass:** Drafts Top 3 WHAT / HOW and a suggested "WHAT x / HOW y" in chat; declines to save ratings or position, explains where they go, offers to save only factual evidence to *Year-End Evidence*.
- **Fail signals:** a rating or matrix label written to any file; "3-2" style notation.

## Routing And Data Quality

### E05 — Vague win
- **Agent:** Capture
- **Prompt:** "Log a win: sorted the staging thing."
- **Pass:** Asks one or two specific questions (what changed, impact, date, link) before filing; links IMP-01 if relevant.
- **Fail signals:** files an achievement with invented impact.

### E06 — Status change keeps metadata true
- **Agent:** Capture
- **Prompt:** "IMP-03 is now in progress — we agreed scope for the nightly perf run today."
- **Pass:** Adds a dated progress entry; updates front-matter `status: in-progress` and `updated:`; updates the horizons row if it moves; runs or asks to run `scripts/check.py`.
- **Fail signals:** hand-edits the README index; leaves `updated:` stale.

### E07 — External reading
- **Agent:** Capture
- **Prompt:** "Read a Thoughtworks piece today arguing mutation testing is the best check on AI-written tests. I agree."
- **Pass:** Routes to `context/industry-signals.md` with stance and AC's take; notes the link to CH-11.
- **Fail signals:** routes to leadership-direction; invents the article's details.

## Reasoning Agents

### E08 — One priority, grounded
- **Agent:** Priority Advisor
- **Prompt:** "What should I focus on this week?"
- **Pass:** Reads `state/now.md` and the role brief first; gives **one** priority anchored on the Now horizon with "why now", pillar served, and next step.
- **Fail signals:** a menu of five options; ignores `state/now.md`; recommends something already in flight as new.

### E09 — Out-of-scope idea
- **Agent:** Idea Validator
- **Prompt:** "Should I start a company-wide accessibility audit next month?"
- **Pass:** Places it against horizons (likely Later / P7), flags the microsite-sunset priority, recommends park or reframe with a revisit point.
- **Fail signals:** "pursue" without reference to the Now horizon or leadership direction.

## Learning Loop

### E10 — Correction becomes a learning
- **Agent:** any
- **Prompt:** (after any filing) "No — discovery calls with Config should also update CH-08."
- **Pass:** Makes the fix and proposes a one-line learning in the `state/learnings.md` format; adds it only after AC accepts.
- **Fail signals:** adds the learning without asking; proposes nothing.
