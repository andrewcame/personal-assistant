# Dashboards: How They Work And How To Work With Them

Two generated pages. Both are built from the repo by standard-library Python, are git-ignored (`reports/`), and are **never opened or read by an agent** (100 KB+; run the script, don't read the output). Updated 2026-10-26.

| Board | Run | Output | Answers |
|---|---|---|---|
| **Quality Leadership Board** | `python scripts/report.py` | `reports/dashboard.html` (open locally), `reports/artifact.html` (publish), `reports/data.json` | What am I doing, what is my focus, what needs attention, what is the plan, what are the signals |
| **People & Objectives Board** | `python scripts/people_report.py` | `reports/people.html`, `reports/people-data.json` | Team readiness, my evidence, framework (pillar and JD) coverage |

Rebuild both after any change to records, `horizons.md`, `now.md` or the Notion snapshot (the Friday routine does this). Code: `scripts/report.py` and `scripts/people_report.py` (data), `scripts/report_template.html` and `scripts/people_template.html` (page). The people board reuses the main board's stylesheet. Only edit the scripts when the layout or logic must change.

## The Model In One Page

1. **Challenge (CH) or improvement (IMP)** is how a problem or idea is tracked, through **tasks**. Progress is recorded on it. Initiatives are never tracked on their own.
2. **Tasks** are Notion To Do cards (tagged with the record ID in `Record`) for AC, and `## Roadmap` steps owned by someone else.
3. **Initiative (INI)** exists only if delivery needs code changes or team work (a Jira item). It must name the CH/IMP it delivers (`origin:`). It shows on its parent's card; cards and steps on an initiative count towards the parent.
4. **Plan item** is something AC said he would do (30/60/90-day plan) that has no CH/IMP. **Role item** is a job-spec responsibility (`JD-`) that no open CH/IMP and no plan item covers. Both show as amber cards in the plan and under Needs attention until a CH/IMP is created.

## Quality Leadership Board: Where Every Number Comes From

| Section | Shows | Source of truth |
|---|---|---|
| **This week · Focus** | Open To Do / Do Now cards, grouped by CH/IMP (initiative tags roll up) | `reports/notion-snapshot.json` (Friday Notion sync) |
| **This week · Waiting on** | First-up roadmap steps (`doing`/`next`) owned by someone other than AC | `## Roadmap` tables, Owner column |
| **This week · Needs attention** | (a) Now/Next CH/IMP with no open card and either an AC-owned next step or no next step; (b) plan items and role items with no CH/IMP | roadmaps, snapshot, `horizons.md`, `jd:` tags |
| **This week · Coming up** | Dated items not covered above | `state/now.md` → Upcoming |
| **Four tiles** | Counts of the four panels above (this section only) | derived |
| **Plan** | One card per open CH/IMP in Now / Next / Later (lane = `horizon:`): category, initiative, status, to-dos, next ticket. Amber dashed cards: plan and role items | record front-matter and roadmaps; `horizons.md` Source column; `_taxonomy.md` JD list |
| **Signals** | Leadership direction, industry signals, recent conversations | `context/leadership-direction.md`, `industry-signals.md`, `discovery-calls/` |

People & Objectives Board: Team readiness from `team/<alias>.md` (counts only, never ratings); Evidence from `achievements/<year>.md`; Framework coverage from achievement tags, `jd:`/`pillars:` front-matter and discovery calls.

## Fields The Dashboards Read

| Field | Where | Rule |
|---|---|---|
| `focus:` | CH/IMP/INI front-matter | The card **category**: people, ownership, automation, productivity |
| `horizon:` | CH/IMP front-matter | now / next / later; must match the `horizons.md` row (check.py warns) |
| `origin: [CH-/IMP-]` | INI (required) | The CH/IMP it delivers; check.py errors if missing |
| `initiative: tbc\|needed\|not-needed` | CH/IMP (optional, default tbc) | Shown on the card |
| `jd: [JD-NN]` | CH/IMP (optional) | Which job-spec responsibilities it delivers; untracked JDs become role items |
| Roadmap `Owner` | `## Roadmap` | `AC` = a To Do card is expected; anyone else = Waiting on |
| Roadmap `Ticket` (optional 6th column) | `## Roadmap` | Jira key shown on the card next to the next step |
| `Source` column | `horizons.md` tables | `—` when a record carries the row; else where it came from (e.g. `60-day plan; JD-08`) |
| Card `url` (optional) | `notion-snapshot.json` | Makes each Focus to-do a link |

Definitions: `context/_taxonomy.md` (hierarchy, fields, roadmap format). Validation: `python scripts/check.py all`.

## How To Do Common Jobs (Cheapest Way)

| You want to… | Do this | Model tier |
|---|---|---|
| Add a task for a CH/IMP | A Notion To Do card with `Record` = the ID. If it is for someone else, add a roadmap step with their alias as Owner | Haiku-class |
| Mark a gap closed on Needs attention | Give the CII a card or roadmap step; for a plan/role item, open a CH/IMP, then add it to `Carried by` in `horizons.md` (and `jd:` on the record) | Sonnet |
| Raise an initiative | Create `initiatives/NN-….md` from the template with `origin: [IMP-NN]`; set `initiative: needed` on the parent if undecided | Sonnet |
| Change a target horizon | Edit `horizon:` on the record **and** its row in `horizons.md`; run check.py | Haiku-class |
| Update the Upcoming panel | Edit the Upcoming bullets in `now.md` (`IMP-08 Short label — the point`, or `General — …`) | Haiku-class |
| Refresh everything | `python scripts/check.py all`, then both report scripts. Notion data is only as fresh as the last sync: the Monday/Wednesday (light) and Friday (full) scheduled runs do it, or ask for "the notion-sync skill, light" ([scheduled-prompts.md](scheduled-prompts.md)) | any |
| See This week as text (for an agent) | `python scripts/report.py --week` (compact; no need to open the HTML/JSON) | any |
| Change what a section shows | Edit `scripts/report.py` (data) or the template (layout), rebuild, check the page once | Sonnet |

## Keeping Credit Use Low

- Run the scripts; never open `reports/*` (see [model and token guide](model-and-token-guide.md)). For This week as text use `python scripts/report.py --week`.
- To work on the dashboard code, open only the function you need (`grep` for `def this_week`, `def role_items`, `def plan_only`), not the whole template.
- A data question ("why is X in Needs attention?") is answered from this page's source table, not by reading the page.
- Don't re-derive tags: `jd:` and `focus:` are already on the records; `check.py coverage` gives the JD/pillar gaps without a model.
- Keep `state/now.md` to one screen. Its Focus and Waiting On sections are narrative notes only; the dashboards read Upcoming.

## Known Limits

- Waiting on only covers roadmap steps owned by an alias (external parties such as a vendor need an owner alias or a tagged Notion card).
- Focus is as fresh as the last Notion sync (`notion-snapshot.json`). Without the Notion MCP, paste the open To Do cards into a chat and ask for the snapshot to be written.
- The `jd:` tags were assigned by inference from record titles on 2026-10-26; correct them in the record if a role item looks wrong.
