# Dashboards: How They Work And How To Work With Them

Two generated pages. Both are built from the repo by standard-library Python, are git-ignored (`reports/`), and are **never opened or read by an agent** (100 KB+; run the script, don't read the output). Updated 2026-11-04.

| Board | Run | Output | Answers |
|---|---|---|---|
| **Quality Leadership Board** | `python scripts/report.py` | `reports/dashboard.html` (open locally), `reports/artifact.html` (publish), `reports/data.json` | What am I doing, what is my focus, what needs attention, what are the tasks and are they on Notion, what is the plan, what are the signals |
| **People & Objectives Board** | `python scripts/people_report.py` | `reports/people.html`, `reports/people-data.json` | Team readiness, my evidence, framework (pillar and JD) coverage |

Rebuild both after any change to records, `horizons.md`, `now.md` or the Notion snapshot (the Friday routine does this). Code: `scripts/report.py` and `scripts/people_report.py` (data), `scripts/report_template.html` and `scripts/people_template.html` (page). The people board reuses the main board's stylesheet. Only edit the scripts when the layout or logic must change.

## The Model In One Page

1. **Source** → **challenge (CH) or improvement (IMP)**, tracked through **tasks**. Progress is recorded on it. Sources are calls, management direction, industry signals, the job spec, the 30/60/90-day plan and ideas; plan items and job-spec gaps with no record become a record (assumed required until closed).
2. **Tasks** are Notion To Do cards (tagged with the record ID in `Record`, named in the roadmap's `Card` column) for AC, and `## Roadmap` steps owned by someone else (monitored with a "Monitor …" card).
3. **Jira initiative**: tracked only in Jira. It shows on the record as the optional `jira:` label (epic/ticket keys). There is no initiative record.
4. **Done**: `outcome:` says where the result landed: AC's achievements, a team member's Year-End Evidence, both, or neither.

## Quality Leadership Board: Where Every Number Comes From

| Section | Shows | Source of truth |
|---|---|---|
| **This week · Focus** | Open To Do cards, grouped by CH/IMP (cards still tagged with a retired INI- ID roll up into the parent) | `reports/notion-snapshot.json` (Notion sync) |
| **This week · Needs attention** | Roadmap and Notion out of step: Now/Next CH/IMP with no open card (whoever owns the next step); open tagged cards no step names; Done cards whose step isn't done | roadmaps, snapshot |
| **This week · Coming up** | Dated items not covered above | `state/now.md` → Upcoming |
| **Three tiles** | Counts of the three panels above (this section only) | derived |
| **Plan** | One card per open CH/IMP in Now / Next / Later (lane = `horizon:`): category, Jira keys, status, to-dos, next ticket | record front-matter and roadmaps; Notion snapshot |
| **Tasks** | Every open roadmap step per CH/IMP with owner, status and where it is on Notion: To Do, Backlog, Needs card (a doing/next step with no card on the board), blank (later or blocked: no card expected yet), plus Untracked (an open tagged card no step names) and Card done (card Done, step not). Untracked and Card done also show under Needs attention and are fixed by notion-sync. Text view: `python scripts/report.py --tasks` | roadmaps (`Card` column), Notion snapshot |
| **Signals** | Leadership direction, industry signals, recent conversations | `context/leadership-direction.md`, `industry-signals.md`, `discovery-calls/` |

People & Objectives Board: Team readiness from `team/<alias>.md` (counts only, never ratings); Evidence from `achievements/<year>.md`; Framework coverage from achievement tags, `jd:`/`pillars:` front-matter and discovery calls.

## Fields The Dashboards Read

| Field | Where | Rule |
|---|---|---|
| `focus:` | CH/IMP front-matter | The card **category**: people, ownership, automation, productivity |
| `horizon:` | CH/IMP front-matter | now / next / later; must match the `horizons.md` row (check.py warns) |
| `jira: [KEY, …]` | CH/IMP (optional) | Jira epic/ticket keys delivering it; shown on the card |
| `jd: [JD-NN]` | CH/IMP (optional) | Which job-spec responsibilities it delivers; `check.py coverage` lists those no open record carries |
| `outcome:` | Closed CH/IMP | achievement / evidence / both / none; check.py warns if missing |
| Roadmap `Owner` | `## Roadmap` | Shown on the card's next ticket. Every first-up step needs a card whoever owns it ("Monitor …" for someone else's) |
| Roadmap `Ticket` (optional) | `## Roadmap` | Jira key shown on the card next to the next step |
| Roadmap `Card` (optional) | `## Roadmap` | Exact Notion card title for the step; the Tasks section matches it against the snapshot |
| Card `url` (optional) | `notion-snapshot.json` | Makes each Focus to-do and task a link |

Definitions: `context/_taxonomy.md` (hierarchy, fields, roadmap format). Validation: `python scripts/check.py all`.

## How To Do Common Jobs (Cheapest Way)

| You want to… | Do this | Model tier |
|---|---|---|
| Add a task for a CH/IMP | A Notion To Do card with `Record` = the ID, then name its exact title in the step's `Card` column. If it is for someone else, add a roadmap step with their alias as Owner and a "Monitor …" card | Haiku-class |
| Cover a plan item or job-spec gap | Open a CH/IMP for it (assumed required until you close it), add its `horizons.md` row, give it a roadmap | Sonnet |
| Show Jira delivery | Add the epic/ticket keys to `jira:` on the CH/IMP; note status in its progress log | Haiku-class |
| Change a target horizon | Edit `horizon:` on the record **and** its row in `horizons.md`; run check.py | Haiku-class |
| Update the Upcoming panel | Edit the Upcoming bullets in `now.md` (`IMP-08 Short label — the point`, or `General — …`) | Haiku-class |
| Refresh everything | `python scripts/check.py all`, then both report scripts. Notion data is only as fresh as the last sync: the Monday/Wednesday (light) and Friday (full) scheduled runs do it, or ask for "the notion-sync skill, light" ([scheduled-prompts.md](scheduled-prompts.md)) | any |
| See This week or the tasks as text (for an agent) | `python scripts/report.py --week` or `--tasks` (compact; no need to open the HTML/JSON) | any |
| Change what a section shows | Edit `scripts/report.py` (data) or the template (layout), rebuild, check the page once | Sonnet |

## Keeping Credit Use Low

- Run the scripts; never open `reports/*` (see [model and token guide](model-and-token-guide.md)). For This week as text use `python scripts/report.py --week`; for tasks, `--tasks`.
- To work on the dashboard code, open only the function you need (`grep` for `def this_week`, `def task_list`), not the whole template.
- A data question ("why is X in Needs attention?") is answered from this page's source table, not by reading the page.
- Don't re-derive tags: `jd:` and `focus:` are already on the records; `check.py coverage` gives the JD/pillar gaps without a model.
- Keep `state/now.md` to one screen (Upcoming and Recent Decisions only).

## Known Limits

- No Waiting on panel or logic (removed 2026-10-27): there is no reliable signal yet for what is waiting on others. Steps owned by someone else show in Tasks with their owner.
- Focus and Tasks are as fresh as the last Notion sync (`notion-snapshot.json`). Without the Notion MCP, paste the open To Do cards into a chat and ask for the snapshot to be written.
- The `jd:` tags were assigned by inference from record titles on 2026-10-26; correct them in the record if a coverage gap looks wrong.
