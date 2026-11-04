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

## Ideas Triage

### E11 — Sub-bullets are one idea; covered still enriches
- **Skill:** notion-sync (Flow 1)
- **Prompt:** Triage this fictional Ideas excerpt:
  ```
  - Speed up test data
      - Seed weekly or create per test?
      - Market-specific data — we've drifted from what prod markets look like
          - Lean into each market's nuance in scenario breadth
  - Book coffee with new SEM
  ```
- **Pass:** Two groups, not five. The first is matched to the test-data record (IMP-02 / CH-10) with verdict **Enrich**, proposing concrete additions (e.g. the seed-vs-create question and market-specific scenario breadth as Questions To Explore or a roadmap step). The second is a **To Do** (or Park). Ticking is proposed on the top-level lines only, with suffixes.
- **Fail signals:** each sub-bullet treated as a separate idea; "already covered by IMP-02" with no additions; sub-bullets ticked or rewritten.

## Dashboards And Tracking Model

### E12 — A new task goes to a to-do, not free text
- **Agent:** Capture
- **Prompt:** "I need to chase DA for the member-creation requirements this week" (IMP-02).
- **Pass:** Proposes a roadmap step or step update owned by DA on IMP-02 (it then shows under Tasks with DA as owner), or a Notion To Do card tagged IMP-02 if the chase is AC's own task (created and listed afterwards); does not rely on a `now.md` line for the dashboard.
- **Fail signals:** writes only a `now.md` line; tags the card to a retired INI- ID.

### E13 — Jira delivery is a label, not a record
- **Agent:** Capture
- **Prompt:** "Open an initiative to automate the Exerp release checks."
- **Pass:** Explains there is no initiative record; asks which challenge or improvement it delivers (or proposes CH-12 / IMP-09 for AC to confirm), adds the Jira keys to its `jira:` front-matter and the status to its progress log, and runs `check.py`.
- **Fail signals:** creates a file in `initiatives/`; creates it as a standalone card.

### E14 — Dashboard question answered without opening the output
- **Agent:** any
- **Prompt:** "Is IMP-04's first JQL step on Notion yet?"
- **Pass:** Runs `python scripts/report.py --tasks` (or reads the roadmap's `Card` column against the snapshot) and answers from it.
- **Fail signals:** opens `reports/*.html` or `reports/*.json`.

### E15 — Closing a challenge asks where the result goes
- **Agent:** Capture
- **Prompt:** "CH-12 is resolved; the Exerp release process is agreed."
- **Pass:** Asks whether the result is an achievement for AC, evidence for a team member, both or neither; then sets `outcome:`, fills the Outcome section, drops open steps and updates the `horizons.md` row. Does not ask about goals.
- **Fail signals:** sets the status to resolved with no `outcome:`; writes an achievement without asking; offers to turn the record into a goal.

### E16 — A job-spec gap becomes a record
- **Agent:** horizon-review
- **Prompt:** "Run the horizon review."
- **Pass:** Runs `check.py coverage`, and for each job-spec responsibility with no open record proposes an improvement or challenge (assumed required until AC closes it), with its `horizons.md` row.
- **Fail signals:** leaves the gap as a note; adds a `horizons.md` row with no record.

### E17 — A tagged card AC adds becomes a roadmap step
- **Agent:** notion-sync
- **Prompt:** "Run the light notion sync." (the board has an open card tagged `IMP-04 QA metrics` that no IMP-04 roadmap step names)
- **Pass:** Adds a new IMP-04 roadmap step (next free number) with the card's exact title in `Card` and status `doing` (To Do) or `next` (Backlog), applies it directly and lists it; rebuilds the dashboards.
- **Fail signals:** leaves the card as "untracked"; renumbers steps; adopts a card with no `Record` value.

### E18 — Goals are built from records and pillars
- **Agent:** Goal Builder
- **Prompt:** "Help me draft goals for 2027."
- **Pass:** Groups the challenges and improvements by pillar, picks the pillar(s) with the meatiest records (or one or two substantial records), drafts 1–3 goals naming the pillar and records, and offers to tag the records with the goal ID.
- **Fail signals:** asks only about recently closed records; invents goals with no link to a record or pillar.

### E19 — Card status check lists every task and fixes what's out of step
- **Agent:** check-card-status
- **Prompt:** "Check card status."
- **Pass:** Refreshes the snapshot, lists every open step and card by record (Now, Next, Later), flags Needs card, Untracked, wrong column, stale, unmapped and duplicates, and applies AC's decisions to the roadmap and Notion together ("close this" marks the step done and moves the card to Done, then creates the next card; "drop this" drops the step and archives the card; "open this" adds a step and a card). Applies the check's own fixes (missing first card, adoption, column) directly and lists them. Ends with `report.py --tasks` showing no flags, or says what remains.
- **Fail signals:** opens `reports/*.html` or `reports/*.json`; updates only the roadmap or only Notion; closes, drops, archives or deletes anything AC didn't ask for; creates cards for Later records.
