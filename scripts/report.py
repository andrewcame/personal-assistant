#!/usr/bin/env python3
"""Build the QA leadership dashboard from the repo. Standard library only.

Usage (from the repo root):
    python scripts/report.py            # writes reports/dashboard.html (open locally), reports/artifact.html (publish), reports/data.json
    python scripts/report.py --json     # print the data only

The HTML template lives in scripts/report_template.html; this script injects the data.
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

def now_state() -> dict:
    text = check.read(ROOT / "state" / "now.md")
    m = re.search(r"\*\*Updated:\*\*\s*(\S+)", text)
    return {
        "updated": m.group(1) if m else None,
        "focus": bullets(section(text, "This Week's Focus")),
        "threads": bullets(section(text, "Open Threads")),
        "decisions": bullets(section(text, "Recent Decisions")),
        "waiting": bullets(section(text, "Waiting On")),
        "upcoming": bullets(section(text, "Upcoming")),
    }


def records() -> tuple[list[dict], list[dict]]:
    recs, calls = [], []
    for r in check.load_records():
        fm = r["fm"]
        if r["kind"] == "discovery-call":
            calls.append({"id": fm.get("id"), "date": fm.get("date"), "title": re.sub(r"^\d{4}-\d{2}-\d{2}\s*-\s*", "", r["title"]),
                          "pillars": fm.get("pillars", []), "file": check.rel(r["path"])})
            continue
        na = re.search(r"\*\*Next action[^*]*\*\*:?\s*(.*)", r["text"])
        nxt = strip_md(na.group(1)) if na and na.group(1).strip() else ""
        if not nxt and na:
            after = r["text"][na.end():]
            first = bullets(after.split("\n\n**")[0])
            nxt = first[0] if first else ""
        recs.append({
            "id": fm.get("id"), "kind": r["kind"], "title": r["title"], "status": fm.get("status"),
            "horizon": fm.get("horizon"), "updated": fm.get("updated"), "age": age(fm.get("updated")),
            "pillars": fm.get("pillars", []), "links": fm.get("links", []), "next": nxt[:260],
            "closed": fm.get("status") in check.CLOSED, "file": check.rel(r["path"]),
        })
    return recs, calls


def horizons(rec_by_file: dict) -> dict:
    text = check.read(ROOT / "context" / "my-role" / "horizons.md")
    theme = re.search(r"\*\*Get off the microsites\.\*\*(.*?)\n", text)
    out = {"theme": strip_md("Get off the microsites." + (theme.group(1) if theme else "")), "rows": []}
    for hz in ["Now", "Next", "Later"]:
        block = section(text, hz)
        for line in block.splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) != 4 or cells[0] in ("Outcome", "") or set(cells[0]) <= set("-"):
                continue
            files = re.findall(r"\]\(\.\./\.\./([^)]+)\)", cells[2])
            ids = [rec_by_file[f]["id"] for f in files if f in rec_by_file]
            ages = [rec_by_file[f]["age"] for f in files if f in rec_by_file and rec_by_file[f]["age"] is not None]
            out["rows"].append({"horizon": hz.lower(), "outcome": strip_md(cells[0]), "focus": cells[1].lower(),
                                "carried": ids, "status": strip_md(cells[3]), "freshest": min(ages) if ages else None})
    return out


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
        goal = re.search(r"Current development goals?:[ \t]*(.*)", text, re.I)
        out.append({"alias": alias, "role": role.group(1).strip() if role else "",
                    "reviewed": rev.group(1) if rev else None, "reviewedAge": age(rev.group(1) if rev else None),
                    "what": what, "how": how, "hasGoal": bool(goal and goal.group(1).strip())})
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
            "live": sum(1 for r in recs if p in r["pillars"] and not r["closed"]),
            "calls": sum(1 for c in calls if p in c["pillars"]),
        })
    jd = [{"id": j, "label": l, "achievements": sum(1 for a in achs if j in a["tags"])} for j, l in jds.items()]
    return {"missions": missions, "pillars": pillars, "jd": jd}


def build() -> dict:
    recs, calls = records()
    by_file = {r["file"]: r for r in recs}
    achs = achievements()
    data = {
        "generated": TODAY.isoformat(),
        "staleDays": STALE_DAYS,
        "now": now_state(),
        "horizons": horizons(by_file),
        "records": recs,
        "calls": sorted(calls, key=lambda c: c["date"] or "", reverse=True),
        "achievements": achs,
        "leadership": leadership(),
        "industry": industry(),
        "team": team(),
        "coverage": coverage(recs, calls, achs),
    }
    return data


def main(argv: list[str]) -> int:
    data = build()
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
    standalone = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"></head><body>\n' + html + "\n</body></html>\n"
    (out_dir / "dashboard.html").write_text(standalone, encoding="utf-8")
    print(f"report: reports/dashboard.html ({len(data['records'])} records, {len(data['achievements'])} achievements)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
