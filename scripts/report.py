#!/usr/bin/env python3
"""Build the QA leadership dashboard from the repo. Standard library only.

Usage (from the repo root):
    python scripts/report.py            # writes reports/dashboard.html (open locally), reports/artifact.html (publish), reports/data.json
    python scripts/report.py --json     # print the data only
    python scripts/report.py --week     # print only the This week panels as compact text (for agents)

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

REF_RE = re.compile(r"^((?:CH|IMP|INI)-\d\d)(?:\.\d+)?\b[^—]*—\s*(.+)$")


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
    """Only Upcoming is read from now.md; Focus and Waiting On on the dashboard come from To Do cards and roadmaps."""
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
            "origin": fm.get("origin", []), "initiativeNeed": fm.get("initiative", "tbc"), "jd": fm.get("jd", []),
            "nextStep": nxt, "closed": fm.get("status") in check.CLOSED, "file": check.rel(r["path"]),
            "roadmap": roadmap,
        })
    # a challenge/improvement is delivered by every initiative that names it as an origin
    by_id = {r["id"]: r for r in recs}
    for r in recs:
        r["initiatives"] = [{"id": i["id"], "title": i["title"], "status": i["status"]} for i in recs
                            if i["kind"] == "initiative" and r["id"] in i["origin"] and not i["closed"]]
    return recs, calls


def parent_of(rec_id: str, by_id: dict) -> str:
    """Initiatives roll up into the challenge or improvement they deliver."""
    r = by_id.get(rec_id)
    if r and r["kind"] == "initiative" and r["origin"]:
        return r["origin"][0]
    return rec_id


def plan_only() -> list[dict]:
    """Plan rows (horizons.md) that no challenge or improvement carries yet."""
    out = []
    for row in check.plan_rows():
        if re.search(r"\]\(\.\./\.\./", row["carried"]):
            continue
        src = strip_md(row["source"]).strip("—- ") or "plan"
        out.append({"horizon": row["horizon"], "outcome": strip_md(row["outcome"]), "focus": row["focus"].lower(),
                    "status": strip_md(row["status"]), "source": src, "jd": re.findall(r"JD-\d+", src)})
    return out


def role_items(recs: list[dict], orphans: list[dict]) -> list[dict]:
    """Job-spec responsibilities that no open challenge/improvement and no plan item covers."""
    tax = check.read(ROOT / "context" / "_taxonomy.md")
    jd = re.findall(r"^\|\s*(JD-\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", tax, re.M)
    covered = {j for r in recs if not r["closed"] and r["kind"] != "initiative" for j in r["jd"]}
    covered |= {j for o in orphans for j in o["jd"]}
    return [{"id": i, "area": area, "label": label} for i, area, label in jd if i not in covered]


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
        out.append({"alias": alias, "role": role.group(1).strip() if role else "",
                    "reviewed": rev.group(1) if rev else None, "reviewedAge": age(rev.group(1) if rev else None),
                    "what": what, "how": how, "objectives": len(objs),
                    "selfEvidence": self_n, "managerEvidence": mgr_n})
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
            "open": sum(1 for r in recs if p in r["pillars"] and not r["closed"] and r["kind"] != "initiative"),
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


def this_week(recs: list[dict], orphans: list[dict], roles: list[dict], snap: dict | None) -> dict:
    """To-do-led view. Each open challenge/improvement (initiatives roll up into theirs) is asked: does it have a task?
    A To Do card on AC -> Focus. A first-up roadmap step owned by someone else -> Waiting on.
    Neither (or an AC step with no card) -> Needs attention. Plan and role items with no record also go to Needs attention."""
    by_id = {r["id"]: r for r in recs}
    ciis = [r for r in recs if r["kind"] != "initiative" and not r["closed"]]
    cards_by: dict[str, list[dict]] = {}
    for card in (snap or {}).get("cards", []):
        if card.get("status") == "Done":
            continue
        for rid in card.get("records", []):
            p = parent_of(rid, by_id)
            if p in by_id and by_id[p]["kind"] != "initiative" and card not in cards_by.setdefault(p, []):
                cards_by[p].append(card)
    rank = {"Do Now": 0, "To Do": 1}
    horizon_order = {"now": 0, "next": 1, "later": 2}
    focus, waiting, no_todo = [], [], []
    for c in sorted(ciis, key=lambda r: (horizon_order.get(r["horizon"], 3), r["id"])):
        # Tasks and waiting-on are tracked on challenges and improvements only; initiative steps roll up into their CII.
        first_up = [s for s in c["roadmap"] if s["status"] in check.FIRST_UP]
        mine = [s for s in first_up if s["owner"] == "AC"]
        theirs = [s for s in first_up if s["owner"] != "AC"]
        cards = cards_by.get(c["id"], [])
        c["todoOpen"] = len(cards)
        c["waitingOn"] = sorted({s["owner"] for s in theirs})
        if not c["nextStep"] and first_up:
            c["nextStep"] = next((s for s in first_up if s["status"] == "doing"), first_up[0])
        tasks = sorted((x for x in cards if x.get("status") in rank), key=lambda x: rank[x["status"]])
        # Plan status follows the Notion card: To Do = In progress, Backlog = Open, no card = Not started.
        c["taskState"] = "In progress" if tasks else ("Open" if cards else "Not started")
        if tasks:
            focus.append({"ref": c["id"], "tasks": [{"title": t["title"], "status": t["status"], "due": t.get("due"),
                                                      "url": t.get("url")} for t in tasks]})
        if theirs:
            waiting.append({"ref": c["id"], "tasks": [{"title": s["step"], "owner": s["owner"], "step": s["id"]} for s in theirs]})
        # Now work needs a To Do card; Next work needs a Backlog card.
        needed = tasks if c["horizon"] == "now" else cards
        if snap is None or c["horizon"] not in ("now", "next") or c["status"] == "on-hold" or needed:
            continue
        card_word = "To Do" if c["horizon"] == "now" else "Backlog card"
        if mine:
            no_todo.append({"id": c["id"], "title": c["title"], "issue": f"Needs a {card_word}: {mine[0]['step']} ({mine[0]['id']})"})
        elif not theirs:
            no_todo.append({"id": c["id"], "title": c["title"], "issue": f"No {card_word} and no next step on the roadmap"})
    no_cii = [{"kind": "plan", "title": o["outcome"], "detail": f"{o['horizon'].capitalize()} · {o['source']}"} for o in orphans]
    no_cii += [{"kind": "role", "title": r["label"], "detail": f"{r['id']} · {r['area']}"} for r in roles]
    return {"focus": focus, "waiting": waiting, "noTodo": no_todo, "noCii": no_cii}


def build() -> dict:
    recs, calls = records()
    snap = notion_snapshot()
    orphans = plan_only()
    roles = role_items(recs, orphans)
    week = this_week(recs, orphans, roles, snap)
    by_id = {r["id"]: r for r in recs}
    now = now_state()
    for e in now["upcoming"]:
        if e["ref"]:
            e["ref"] = parent_of(e["ref"], by_id)
    data = {
        "generated": TODAY.isoformat(),
        "staleDays": STALE_DAYS,
        "now": now,
        "horizons": horizons(),
        "records": recs,
        "planOnly": orphans,
        "calls": sorted(calls, key=lambda c: c["date"] or "", reverse=True),
        "leadership": leadership(),
        "industry": industry(),
        "notion": snap,
        "week": week,
        "roles": roles,
    }
    return data


def main(argv: list[str]) -> int:
    data = build()
    if "--week" in argv:
        # compact text for agents: avoids opening the large generated files
        w = data["week"]
        for f in w["focus"]:
            print(f"FOCUS {f['ref']}: " + "; ".join(f"[{t['status']}] {t['title']}" for t in f["tasks"]))
        for f in w["waiting"]:
            print(f"WAITING {f['ref']}: " + "; ".join(f"{t['owner']}: {t['title']} ({t['step']})" for t in f["tasks"]))
        for n in w["noTodo"]:
            print(f"NO-TODO {n['id']} {n['title']}: {n['issue']}")
        for n in w["noCii"]:
            print(f"NO-CII [{n['kind']}] {n['title']} ({n['detail']})")
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
