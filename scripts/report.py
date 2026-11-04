#!/usr/bin/env python3
"""Build the QA leadership dashboard from the repo. Standard library only.

Usage (from the repo root):
    python scripts/report.py            # writes reports/dashboard.html (open locally), reports/artifact.html (publish), reports/data.json
    python scripts/report.py --json     # print the data only
    python scripts/report.py --week     # print only the This week panels as compact text (for agents)
    python scripts/report.py --tasks    # print every open task per challenge/improvement and its Notion state (for agents)

The HTML template lives in scripts/report_template.html; this script injects the data.
Team readiness, evidence and framework coverage are on the separate People & Objectives board (scripts/people_report.py), which reuses the parsers below.
People data is limited to aliases, profile dates, and evidence counts — never ratings.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check  # noqa: E402  (reuse parsers)

ROOT = check.ROOT
TODAY = dt.date.today()
STALE_DAYS = 21
PERMANENT_TEAM = ["TMW", "DA", "MP", "KB", "JS", "JFG"]


def strip_md(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\*\*|__|`", "", text)
    return text.strip()


def age(date_str: str | None) -> int | None:
    try:
        return (TODAY - dt.date.fromisoformat(date_str)).days
    except (TypeError, ValueError):
        return None


def section(text: str, heading: str, level: int = 2) -> str:
    m = re.search(rf"^{'#' * level} {re.escape(heading)}[^\n]*\n(.*?)(?=^#{{1,{level}}} |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def bullets(block: str) -> list[str]:
    return [strip_md(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", l)) for l in block.splitlines()
            if re.match(r"^\s*(?:[-*]|\d+\.)\s+\S", l)]


# ---------------------------------------------------------------- sources

REF_RE = re.compile(r"^((?:CH|IMP)-\d\d)(?:\.\d+)?\b[^—]*—\s*(.+)$")
# Notion cards tagged before initiatives were folded into their parent record
LEGACY_TAGS = {"INI-01": "IMP-02", "INI-02": "CH-09"}


def entries(block: str) -> list[dict]:
    """now.md bullets shaped 'IMP-08 Short label — one point'; anything else is filed under General."""
    out = []
    for b in bullets(block):
        m = REF_RE.match(b)
        if m:
            out.append({"ref": m.group(1), "text": m.group(2).strip()})
        else:
            out.append({"ref": None, "text": re.sub(r"^General\s*—\s*", "", b)})
    return out


def now_state() -> dict:
    """Only Upcoming is read from now.md; Focus on the dashboard comes from To Do cards."""
    text = check.read(ROOT / "state" / "now.md")
    m = re.search(r"\*\*Updated:\*\*\s*(\S+)", text)
    return {"updated": m.group(1) if m else None, "upcoming": entries(section(text, "Upcoming"))}


def records() -> tuple[list[dict], list[dict]]:
    recs, calls = [], []
    for r in check.load_records():
        fm = r["fm"]
        if r["kind"] == "discovery-call":
            calls.append({"id": fm.get("id"), "date": fm.get("date"), "title": re.sub(r"^\d{4}-\d{2}-\d{2}\s*-\s*", "", r["title"]),
                          "pillars": fm.get("pillars", []), "file": check.rel(r["path"])})
            continue
        roadmap = r.get("roadmap") or []
        nxt = next((st for st in roadmap if st["status"] == "doing"), None) or next((st for st in roadmap if st["status"] == "next"), None)
        recs.append({
            "id": fm.get("id"), "kind": r["kind"], "title": r["title"], "status": fm.get("status"),
            "horizon": fm.get("horizon"), "updated": fm.get("updated"), "age": age(fm.get("updated")),
            "pillars": fm.get("pillars", []), "focus": fm.get("focus", []), "links": fm.get("links", []),
            "jira": fm.get("jira", []), "jd": fm.get("jd", []), "outcome": fm.get("outcome"),
            "nextStep": nxt, "closed": fm.get("status") in check.CLOSED, "file": check.rel(r["path"]),
            "roadmap": roadmap,
        })
    return recs, calls


def record_id(value: str) -> str:
    """Notion Record values are '<ID> <tag>'; match on the ID."""
    rid = value.split(" ", 1)[0]
    return LEGACY_TAGS.get(rid, rid)


def horizons() -> dict:
    text = check.read(ROOT / "context" / "my-role" / "horizons.md")
    theme = re.search(r"\*\*Get off the microsites\.\*\*(.*?)\n", text)
    meta = re.search(r"_Set (\d{4}-\d{2}-\d{2}) from ([^(]+?)\s*\(", text)
    return {"theme": strip_md("Get off the microsites." + (theme.group(1) if theme else "")),
            "themeSet": meta.group(1) if meta else None, "themeSource": meta.group(2).strip() if meta else None}


def achievements() -> list[dict]:
    out = []
    for a in check.load_achievements():
        text = check.read(a["path"])
        start = text.find(f"### {a['date']} - {a['title']}")
        block = text[start: text.find("\n### ", start + 5) if text.find("\n### ", start + 5) != -1 else len(text)]
        summ = bullets(section(block, "Review-Ready Summary", 4))
        first = bullets(block.split("####")[0])
        out.append({"date": a["date"], "title": a["title"], "tags": a["tags"] or [],
                    "summary": (summ or first or [""])[0]})
    return sorted(out, key=lambda x: x["date"], reverse=True)


def leadership() -> list[dict]:
    text = check.read(ROOT / "context" / "leadership-direction.md")
    out = []
    for m in re.finditer(r"^### (\d{4}-\d{2}-\d{2}) — (.+)$", text, re.M):
        body = text[m.end(): text.find("\n### ", m.end()) if text.find("\n### ", m.end()) != -1 else len(text)]
        imp = re.search(r"\*\*Implication[^*]*\*\*\s*—\s*(.+)", body)
        out.append({"date": m.group(1), "title": m.group(2).strip(),
                    "implication": strip_md(imp.group(1))[:240] if imp else ""})
    return out


def industry() -> list[dict]:
    text = check.read(ROOT / "context" / "industry-signals.md")
    out = []
    for m in re.finditer(r"^### (\d{4}-\d{2}-\d{2}) — (.+)$", text, re.M):
        body = text[m.end(): text.find("\n### ", m.end()) if text.find("\n### ", m.end()) != -1 else len(text)]
        st = re.search(r"\*\*Stance\*\*\s*—\s*\**(\w+)", body)
        out.append({"date": m.group(1), "title": m.group(2).strip(), "stance": (st.group(1).capitalize() if st else "Unsettled")})
    return out


def team() -> list[dict]:
    out = []
    for alias in PERMANENT_TEAM:
        p = ROOT / "team" / f"{alias.lower()}.md"
        if not p.exists():
            continue
        text = check.read(p)
        rev = re.search(r"last reviewed[^|\n]*\|\s*(\d{4}-\d{2}-\d{2})", text, re.I)
        role = re.search(r"Current role and level\s*\|\s*([^|]+)\|", text)
        ye = section(text, "Year-End Evidence", 2)
        what = len([b for b in bullets(section(ye + "\n", "WHAT", 3)) if not b.startswith("YYYY")])
        how = len([b for b in bullets(section(ye + "\n", "HOW", 3)) if not b.startswith("YYYY")])
        objs = re.findall(rf"^\|\s*({alias}-O\d+)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|", text, re.M)
        objs = [{"id": o[0], "objective": o[1], "agreed": o[2], "status": o[3]} for o in objs if o[1]]
        ev = bullets(section(ye + "\n", "WHAT", 3)) + bullets(section(ye + "\n", "HOW", 3))
        ev = [e for e in ev if not e.startswith("YYYY")]
        self_n = sum(1 for e in ev if re.search(r"—\s*self\s*—", e))
        mgr_n = sum(1 for e in ev if re.search(r"—\s*manager\s*—", e))
        line_mgr_n = sum(1 for e in ev if re.search(r"—\s*line-manager\s*—", e))
        out.append({"alias": alias, "role": role.group(1).strip() if role else "",
                    "reviewed": rev.group(1) if rev else None, "reviewedAge": age(rev.group(1) if rev else None),
                    "what": what, "how": how, "objectives": len(objs),
                    "selfEvidence": self_n, "managerEvidence": mgr_n, "lineManagerEvidence": line_mgr_n})
    return out


def coverage(recs, calls, achs) -> dict:
    labels, jds = check.pillar_labels(), check.jd_labels()
    tax = check.read(ROOT / "context" / "_taxonomy.md")
    mission_of = dict(re.findall(r"^\|\s*(P\d+)\s*\|[^|]+\|\s*(M\d)\s*\|", tax, re.M))
    missions = dict(re.findall(r"^\|\s*(M\d)\s*\|\s*([^|]+?)\s*\|", tax, re.M))
    pillars = []
    for p, label in labels.items():
        pillars.append({
            "id": p, "label": label, "mission": mission_of.get(p),
            "achievements": sum(1 for a in achs if p in a["tags"]),
            "open": sum(1 for r in recs if p in r["pillars"] and not r["closed"]),
            "calls": sum(1 for c in calls if p in c["pillars"]),
        })
    jd = [{"id": j, "label": l, "achievements": sum(1 for a in achs if j in a["tags"])} for j, l in jds.items()]
    return {"missions": missions, "pillars": pillars, "jd": jd}


def notion_snapshot() -> dict | None:
    p = ROOT / "reports" / "notion-snapshot.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return None


def norm(title: str) -> str:
    return re.sub(r"\s+", " ", title or "").strip().lower()


def card_map(snap: dict | None) -> dict[str, list[dict]]:
    """Notion cards by the challenge/improvement their Record tag names (Done cards included)."""
    out: dict[str, list[dict]] = {}
    for card in (snap or {}).get("cards", []):
        for value in card.get("records", []):
            lst = out.setdefault(record_id(value), [])
            if card not in lst:
                lst.append(card)
    return out


def task_list(c: dict, cards: list[dict], snap: dict | None) -> list[dict]:
    """Every open roadmap step plus any other open Notion card tagged to the record, with where it stands in Notion.
    Notion state: the card's column (To Do / Backlog), 'Needs card' for a doing/next step with no card (or whose named
    card is not on the board), '' for later or blocked steps (no card expected yet), 'Card done' if the named card is
    Done but the step is not, 'Untracked' for an open card no step names (notion-sync adds it to the roadmap)."""
    by_title = {norm(x["title"]): x for x in cards}
    used, rows = set(), []
    for s in c["roadmap"]:
        if s["status"] in ("done", "dropped"):
            continue
        card = by_title.get(norm(s["card"])) if s["card"] else None
        if card:
            used.add(norm(card["title"]))
        if snap is None:
            state = "Unknown"
        elif card:
            state = "Card done" if card.get("status") == "Done" else (card.get("status") or "Unknown")
        else:
            state = "Needs card" if s["status"] in check.FIRST_UP else ""
        rows.append({"id": s["id"], "task": s["step"], "owner": s["owner"], "status": s["status"], "ticket": s["ticket"],
                     "notion": state, "card": card["title"] if card else s["card"], "url": (card or {}).get("url")})
    for card in cards:
        if card.get("status") != "Done" and norm(card["title"]) not in used:
            rows.append({"id": "", "task": card["title"], "owner": "AC", "status": "untracked card", "ticket": "",
                         "notion": "Untracked", "card": card["title"], "url": card.get("url")})
    return rows


def this_week(recs: list[dict], snap: dict | None) -> dict:
    """To-do-led view. Each open challenge/improvement is asked: does it have a task?
    A To Do card on AC -> Focus. No card for the work -> Needs attention. Also builds each record's task list."""
    ciis = [r for r in recs if not r["closed"]]
    all_cards = card_map(snap)
    horizon_order = {"now": 0, "next": 1, "later": 2}
    focus, no_todo = [], []
    for c in sorted(ciis, key=lambda r: (horizon_order.get(r["horizon"], 3), r["id"])):
        first_up = [s for s in c["roadmap"] if s["status"] in check.FIRST_UP]
        every = all_cards.get(c["id"], [])
        cards = [x for x in every if x.get("status") != "Done"]
        c["todoOpen"] = len(cards)
        c["tasks"] = task_list(c, every, snap)
        for t in c["tasks"]:
            if t["notion"] == "Untracked":
                no_todo.append({"id": c["id"], "title": c["title"], "issue": f"Card not on the roadmap: {t['task']}"})
            elif t["notion"] == "Card done":
                no_todo.append({"id": c["id"], "title": c["title"], "issue": f"Card is Done but step {t['id']} is not: {t['task']}"})
        if not c["nextStep"] and first_up:
            c["nextStep"] = next((s for s in first_up if s["status"] == "doing"), first_up[0])
        tasks = [x for x in cards if x.get("status") in ("To Do", "Do Now")]
        # Plan status follows the Notion card: To Do = In progress, Backlog = Open, no card = Not started.
        c["taskState"] = "In progress" if tasks else ("Open" if cards else "Not started")
        if tasks:
            focus.append({"ref": c["id"], "tasks": [{"title": t["title"], "status": t["status"], "due": t.get("due"),
                                                      "url": t.get("url")} for t in tasks]})
        # Now work needs a To Do card; Next work needs a Backlog card.
        needed = tasks if c["horizon"] == "now" else cards
        if snap is None or c["horizon"] not in ("now", "next") or c["status"] == "on-hold" or needed:
            continue
        card_word = "To Do" if c["horizon"] == "now" else "Backlog card"
        if first_up:
            s = first_up[0]
            no_todo.append({"id": c["id"], "title": c["title"], "issue": f"Needs a {card_word}: {s['step']} ({s['id']}, {s['owner']})"})
        else:
            no_todo.append({"id": c["id"], "title": c["title"], "issue": f"No {card_word} and no next step on the roadmap"})
    return {"focus": focus, "noTodo": no_todo}


def build() -> dict:
    recs, calls = records()
    snap = notion_snapshot()
    week = this_week(recs, snap)
    now = now_state()
    data = {
        "generated": TODAY.isoformat(),
        "staleDays": STALE_DAYS,
        "now": now,
        "horizons": horizons(),
        "records": recs,
        "calls": sorted(calls, key=lambda c: c["date"] or "", reverse=True),
        "leadership": leadership(),
        "industry": industry(),
        "notion": snap,
        "week": week,
    }
    return data


def main(argv: list[str]) -> int:
    data = build()
    if "--tasks" in argv:
        # every open task per challenge/improvement, and whether it is on Notion
        for r in data["records"]:
            if r["closed"] or r["horizon"] not in ("now", "next", "later"):
                continue
            print(f"{r['id']} [{r['horizon']}] {r['title']}")
            for t in r["tasks"]:
                who = f" ({t['owner']})" if t["owner"] else ""
                print(f"  {t['id'] or 'card'} {t['status']}{who}: {t['task']} -> Notion: {t['notion'] or '-'}")
        return 0
    if "--week" in argv:
        # compact text for agents: avoids opening the large generated files
        w = data["week"]
        for f in w["focus"]:
            print(f"FOCUS {f['ref']}: " + "; ".join(f"[{t['status']}] {t['title']}" for t in f["tasks"]))
        for n in w["noTodo"]:
            print(f"NO-TODO {n['id']} {n['title']}: {n['issue']}")
        for e in data["now"]["upcoming"]:
            print(f"UPCOMING {e['ref'] or 'General'}: {e['text']}")
        return 0
    if "--json" in argv:
        print(json.dumps(data, indent=1))
        return 0
    out_dir = ROOT / "reports"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "data.json").write_text(json.dumps(data, indent=1), encoding="utf-8")
    template = (Path(__file__).parent / "report_template.html").read_text(encoding="utf-8")
    html = template.replace("/*__DATA__*/null", json.dumps(data).replace("</", "<\\/"))
    # artifact.html is the bare page for publishing (the host adds the document skeleton);
    # dashboard.html is a standalone copy for opening locally in a browser.
    (out_dir / "artifact.html").write_text(html, encoding="utf-8")
    standalone = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"></head><body>\n' + html + '\n</body></html>\n'
    (out_dir / "dashboard.html").write_text(standalone, encoding="utf-8")
    print(f"report: reports/dashboard.html ({len(data['records'])} records)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
