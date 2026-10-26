#!/usr/bin/env python3
"""Repo health checks for the personal-assistant repo. Standard library only.

Usage (from the repo root):
    python scripts/check.py all          # validate + index + coverage + stale
    python scripts/check.py validate     # front-matter, IDs, tags, links  (exit 1 on errors)
    python scripts/check.py index        # regenerate README index tables
    python scripts/check.py coverage     # evidence per pillar and JD item
    python scripts/check.py stale [days] # open records not updated recently (default 21)

Reads IDs from context/_taxonomy.md and aliases from context/people.md, so add new
IDs or people there first.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TODAY = dt.date.today()

RECORD_DIRS = {
    "challenge": ("challenges", "CH"),
    "improvement": ("improvements", "IMP"),
    "initiative": ("initiatives", "INI"),
}
STATUSES = {
    "challenge": ["open", "active-monitoring", "resolved", "closed"],
    "improvement": ["not-started", "in-progress", "on-hold", "blocked", "done"],
    "initiative": ["draft", "submitted", "in-progress", "on-hold", "done", "rejected"],
}
CLOSED = {"resolved", "closed", "done", "rejected"}
HORIZONS = ["now", "next", "later", "none"]
FOCUS = ["people", "ownership", "automation", "productivity"]
INDEX_START, INDEX_END = "<!-- index:start -->", "<!-- index:end -->"
STEP_STATUSES = ["done", "doing", "next", "later", "blocked", "dropped"]
FIRST_UP = {"doing", "next"}
INITIATIVE_NEEDS = ["tbc", "needed", "not-needed"]


# ---------------------------------------------------------------- io helpers

def read(path: Path) -> str:
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n")


def write_preserving_eol(path: Path, text: str) -> None:
    raw = path.read_bytes().decode("utf-8") if path.exists() else ""
    eol = "\r\n" if "\r\n" in raw else "\n"
    path.write_bytes(text.replace("\n", eol).encode("utf-8"))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


# ---------------------------------------------------------------- taxonomy

def load_taxonomy() -> dict[str, set[str]]:
    text = read(ROOT / "context" / "_taxonomy.md")
    ids = set(re.findall(r"^\|\s*((?:JD-\d+|M\d+|P\d+|G\d+|PD|VC|BO|V-[A-Z]+))\s*\|", text, re.M))
    people = set(re.findall(r"^\|\s*([A-Z][A-Za-z]{1,3})\s*\|", read(ROOT / "context" / "people.md"), re.M))
    people.discard("Alias")
    return {
        "pillars": {i for i in ids if re.fullmatch(r"P\d+", i)},
        "jd": {i for i in ids if i.startswith("JD-")},
        "goals": {i for i in ids if re.fullmatch(r"G\d+", i)},
        "lenses": {"PD", "VC", "BO"},
        "values": {i for i in ids if i.startswith("V-")},
        "people": people,
    }


def pillar_labels() -> dict[str, str]:
    text = read(ROOT / "context" / "_taxonomy.md")
    return dict(re.findall(r"^\|\s*(P\d+)\s*\|\s*([^|]+?)\s*\|", text, re.M))


def jd_labels() -> dict[str, str]:
    text = read(ROOT / "context" / "_taxonomy.md")
    return {k: v for k, _, v in re.findall(r"^\|\s*(JD-\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", text, re.M)}


# ---------------------------------------------------------------- records

def parse_front_matter(text: str) -> dict | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    data = {}
    for line in text[4:end].splitlines():
        line = line.split("#", 1)[0].rstrip()
        if not line.strip() or ":" not in line:
            continue
        key, val = line.split(":", 1)
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            data[key.strip()] = [v.strip() for v in val[1:-1].split(",") if v.strip()]
        else:
            data[key.strip()] = val
    return data


def title_of(text: str, kind: str) -> str:
    if kind == "initiative":
        m = re.search(r"\*\*Initiative Name:\*\*\s*(.+)", text)
        if m:
            return m.group(1).strip()
    m = re.search(r"^# (.+)$", text, re.M)
    if not m:
        return "(untitled)"
    t = m.group(1).strip()
    return re.sub(r"^(Challenge|Improvement|Initiative)\s+\d+\s*[—–-]\s*", "", t)


def parse_roadmap(text: str) -> list[dict] | None:
    """Return roadmap steps from a '## Roadmap' table, or None if the section is missing."""
    m = re.search(r"^## Roadmap[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return None
    steps = []
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or not re.fullmatch(r"(CH|IMP|INI)-\d\d\.\d+", cells[0]):
            continue
        deps = [d.strip() for d in re.split(r"[,;]", cells[3]) if d.strip() and d.strip() not in ("—", "-")]
        ticket = cells[5] if len(cells) > 5 and cells[5] not in ("", "—", "-") else ""
        steps.append({"id": cells[0], "step": cells[1], "owner": cells[2], "deps": deps, "status": cells[4].lower(),
                      "ticket": ticket})
    return steps


def load_records() -> list[dict]:
    records = []
    for kind, (folder, prefix) in RECORD_DIRS.items():
        for path in sorted((ROOT / folder).glob("[0-9][0-9]-*.md")):
            text = read(path)
            fm = parse_front_matter(text) or {}
            records.append({"kind": kind, "path": path, "fm": fm, "text": text,
                            "num": path.name[:2], "prefix": prefix, "title": title_of(text, kind),
                            "roadmap": parse_roadmap(text)})
    for path in sorted((ROOT / "context" / "discovery-calls").glob("20*.md")):
        text = read(path)
        records.append({"kind": "discovery-call", "path": path, "fm": parse_front_matter(text) or {},
                        "text": text, "num": None, "prefix": "DC", "title": title_of(text, "discovery-call")})
    return records


def plan_rows() -> list[dict]:
    """Rows of the Now / Next / Later tables in horizons.md (Outcome | Focus | Carried by | Status | Source)."""
    text = read(ROOT / "context" / "my-role" / "horizons.md")
    rows = []
    for hz in ("Now", "Next", "Later"):
        m = re.search(rf"^## {hz}[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        for line in (m.group(1) if m else "").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 4 or cells[0] in ("Outcome", "") or set(cells[0]) <= set("-"):
                continue
            rows.append({"horizon": hz.lower(), "outcome": cells[0], "focus": cells[1], "carried": cells[2],
                         "status": cells[3], "source": cells[4] if len(cells) > 4 else ""})
    return rows


def load_achievements() -> list[dict]:
    out = []
    for path in sorted((ROOT / "achievements").glob("20*.md")):
        text = read(path)
        for m in re.finditer(r"^### (\d{4}-\d{2}-\d{2}) - (.+)$", text, re.M):
            block = text[m.end(): text.find("\n### ", m.end()) if text.find("\n### ", m.end()) != -1 else len(text)]
            t = re.search(r"\*\*Tags:\*\*\s*(.+)", block)
            tags = [x.strip() for x in t.group(1).split(",")] if t else None
            out.append({"path": path, "date": m.group(1), "title": m.group(2).strip(), "tags": tags})
    return out


# ---------------------------------------------------------------- validate

def validate() -> int:
    tax = load_taxonomy()
    records = load_records()
    known_ids = {r["fm"].get("id") for r in records if r["fm"].get("id")}
    errors, warnings = [], []

    def err(path, msg): errors.append(f"{rel(path)}: {msg}")
    def warn(path, msg): warnings.append(f"{rel(path)}: {msg}")

    for r in records:
        fm, path, kind = r["fm"], r["path"], r["kind"]
        if not fm:
            err(path, "missing front-matter")
            continue
        if kind != "discovery-call":
            expected = f"{r['prefix']}-{r['num']}"
            if fm.get("id") != expected:
                err(path, f"id '{fm.get('id')}' should be '{expected}'")
            if fm.get("status") not in STATUSES[kind]:
                err(path, f"status '{fm.get('status')}' not in {STATUSES[kind]}")
            if fm.get("horizon") not in HORIZONS:
                err(path, f"horizon '{fm.get('horizon')}' not in {HORIZONS}")
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fm.get("updated", "")):
                err(path, "updated must be YYYY-MM-DD")
            for g in fm.get("goals", []):
                if g not in tax["goals"]:
                    err(path, f"unknown goal '{g}'")
            if not fm.get("pillars") and kind != "improvement":
                warn(path, "no pillars tagged")
        for p in fm.get("pillars", []):
            if p not in tax["pillars"]:
                err(path, f"unknown pillar '{p}'")
        for f in fm.get("focus", []):
            if f not in FOCUS:
                err(path, f"unknown focus '{f}'")
        for j in fm.get("jd", []):
            if j not in tax["jd"]:
                err(path, f"unknown job-spec id '{j}'")
        for link in fm.get("links", []):
            if link not in known_ids:
                err(path, f"link '{link}' does not match any record id")
        for a in fm.get("people", []):
            if a not in tax["people"]:
                err(path, f"alias '{a}' not in context/people.md")
        if kind == "initiative":
            origin = fm.get("origin", [])
            if not origin:
                err(path, "initiative needs 'origin: [CH-NN or IMP-NN]' — the challenge or improvement it delivers")
            for o in origin:
                if o not in known_ids or o.startswith(("INI-", "DC-")):
                    err(path, f"origin '{o}' must be a challenge or improvement id")
        elif kind in ("challenge", "improvement") and fm.get("initiative", "tbc") not in INITIATIVE_NEEDS:
            err(path, f"initiative '{fm.get('initiative')}' not in {INITIATIVE_NEEDS}")

    # roadmaps
    all_steps = {st["id"] for r in records for st in (r.get("roadmap") or [])}
    for r in records:
        if r["kind"] == "discovery-call" or not r["fm"]:
            continue
        rid, fm, rm = r["fm"].get("id"), r["fm"], r.get("roadmap")
        live = fm.get("status") not in CLOSED
        if rm is None:
            if live and fm.get("horizon") in ("now", "next") and r["kind"] != "initiative":
                warn(r["path"], "no ## Roadmap section (required for Now/Next records)")
            continue
        for st in rm:
            if not st["id"].startswith(f"{rid}."):
                err(r["path"], f"roadmap step {st['id']} should start with {rid}.")
            if st["status"] not in STEP_STATUSES:
                err(r["path"], f"roadmap step {st['id']} status '{st['status']}' not in {STEP_STATUSES}")
            if st["owner"] and st["owner"] not in tax["people"]:
                err(r["path"], f"roadmap step {st['id']} owner '{st['owner']}' not in context/people.md")
            for d in st["deps"]:
                if d not in all_steps and d not in known_ids:
                    err(r["path"], f"roadmap step {st['id']} depends on unknown '{d}'")
        if live and fm.get("status") != "on-hold" and fm.get("horizon") in ("now", "next") and not any(st["status"] in FIRST_UP for st in rm):
            warn(r["path"], "Now/Next record has no 'doing' or 'next' roadmap step")

    valid_tags = tax["pillars"] | tax["jd"] | tax["goals"] | tax["lenses"] | tax["values"] | known_ids

    # the plan tables and record front-matter must agree on horizon; CII-less rows must say where they came from
    by_file = {r["path"].name: r for r in records if r["kind"] != "discovery-call"}
    listed: dict[str, set] = {}
    for row in plan_rows():
        files = re.findall(r"\]\(\.\./\.\./[^)]*?/([^/)]+\.md)\)", row["carried"])
        if not files and row["source"] in ("", "—", "-"):
            warn(ROOT / "context" / "my-role" / "horizons.md", f"'{row['outcome'][:50]}' has no CII and no Source")
        for f in files:
            listed.setdefault(f, set()).add(row["horizon"])
        for j in re.findall(r"JD-\d+", row["source"]):
            if j not in tax["jd"]:
                err(ROOT / "context" / "my-role" / "horizons.md", f"Source cites unknown job-spec id '{j}'")
    for f, horizons_listed in listed.items():
        rec = by_file.get(f)
        if rec and rec["fm"].get("horizon") not in horizons_listed:
            warn(rec["path"], f"horizon '{rec['fm'].get('horizon')}' but horizons.md lists it under {', '.join(sorted(horizons_listed))}")
    for a in load_achievements():
        if a["tags"] is None:
            warn(a["path"], f"achievement '{a['date']} - {a['title']}' has no Tags line")
            continue
        for t in a["tags"]:
            if t not in valid_tags:
                err(a["path"], f"achievement '{a['date']}' has unknown tag '{t}'")

    # markdown links
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or "templates" in path.parts:
            continue
        for target in re.findall(r"\]\(([^)\s]+)\)", read(path)):
            if target.startswith(("http", "mailto:", "#")):
                continue
            t = urllib.parse.unquote(target.split("#")[0])
            if t and not (path.parent / t).resolve().exists():
                err(path, f"broken link -> {target}")

    # discovery-call README lists every call
    dc_readme = read(ROOT / "context" / "discovery-calls" / "README.md")
    for r in records:
        if r["kind"] == "discovery-call" and r["path"].name not in dc_readme:
            warn(r["path"], "not listed in context/discovery-calls/README.md")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"validate: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


# ---------------------------------------------------------------- index

def aligned_table(header: list[str], rows: list[list[str]]) -> str:
    widths = [max(len(header[i]), *(len(r[i]) for r in rows)) if rows else len(header[i]) for i in range(len(header))]
    line = lambda cells: "| " + " | ".join(c.ljust(widths[i]) for i, c in enumerate(cells)) + " |"
    sep = "|" + "|".join("-" * (w + 2) for w in widths) + "|"
    return "\n".join([line(header), sep, *(line(r) for r in rows)])


def nice(status: str) -> str:
    return status.replace("-", " ").capitalize() if status else "?"


def index() -> int:
    records = load_records()
    for kind, (folder, _) in RECORD_DIRS.items():
        readme = ROOT / folder / "README.md"
        text = read(readme)
        rows = []
        for r in (x for x in records if x["kind"] == kind):
            fm = r["fm"]
            rows.append([f"[{r['num']}]({r['path'].name})", r["title"], nice(fm.get("status", "")),
                         fm.get("horizon", ""), ", ".join(fm.get("pillars", [])), fm.get("updated", "")])
        table = aligned_table(["#", "Title", "Status", "Horizon", "Pillars", "Updated"], rows)
        block = f"{INDEX_START}\n_Generated by `python scripts/check.py index` from each file's front-matter — edit the files, not this table._\n\n{table}\n{INDEX_END}"
        if INDEX_START in text:
            text = re.sub(re.escape(INDEX_START) + r".*?" + re.escape(INDEX_END), lambda _: block, text, flags=re.S)
        else:
            # replace the last markdown table in the file, or append
            m = list(re.finditer(r"(?:^\|.*\|\n?)+", text, re.M))
            if m:
                last = m[-1]
                text = text[: last.start()] + block + "\n" + text[last.end():]
            else:
                text = text.rstrip("\n") + "\n\n## Index\n\n" + block + "\n"
        write_preserving_eol(readme, text)
        print(f"index: {rel(readme)} ({len(rows)} rows)")
    return 0


# ---------------------------------------------------------------- coverage

def coverage() -> int:
    records = load_records()
    ach = load_achievements()
    labels, jds = pillar_labels(), jd_labels()
    print("\n## Evidence by pillar\n")
    rows = []
    for p, label in labels.items():
        a = sum(1 for x in ach if x["tags"] and p in x["tags"])
        live = sum(1 for r in records if r["kind"] in RECORD_DIRS and p in r["fm"].get("pillars", [])
                   and r["fm"].get("status") not in CLOSED)
        dc = sum(1 for r in records if r["kind"] == "discovery-call" and p in r["fm"].get("pillars", []))
        flag = "no achievements yet" if a == 0 else ""
        rows.append([p, label, str(a), str(live), str(dc), flag])
    print(aligned_table(["Pillar", "Label", "Achievements", "Live records", "Discovery calls", "Gap"], rows))
    print("\n## Evidence by JD responsibility\n")
    rows = []
    for j, label in jds.items():
        a = sum(1 for x in ach if x["tags"] and j in x["tags"])
        rows.append([j, label, str(a), "no evidence yet" if a == 0 else ""])
    print(aligned_table(["JD", "Responsibility", "Achievements", "Gap"], rows))
    return 0


# ---------------------------------------------------------------- stale

def stale(days: int = 21) -> int:
    cutoff = TODAY - dt.timedelta(days=days)
    print(f"\n## Open records not updated since {cutoff} ({days} days)\n")
    rows = []
    for r in load_records():
        if r["kind"] not in RECORD_DIRS:
            continue
        fm = r["fm"]
        if fm.get("status") in CLOSED:
            continue
        try:
            upd = dt.date.fromisoformat(fm.get("updated", ""))
        except ValueError:
            continue
        if upd < cutoff:
            rows.append([fm.get("id", "?"), r["title"][:60], nice(fm.get("status", "")), fm.get("horizon", ""),
                         str(upd), f"{(TODAY - upd).days}d"])
    rows.sort(key=lambda x: x[4])
    print(aligned_table(["ID", "Title", "Status", "Horizon", "Updated", "Age"], rows) if rows else "None.")

    print(f"\n## Team profiles not reviewed in {days * 2} days\n")
    prow = []
    for path in sorted((ROOT / "team").glob("*.md")):
        m = re.search(r"last reviewed[^|\n]*\|\s*(\d{4}-\d{2}-\d{2})", read(path), re.I)
        if m:
            d = dt.date.fromisoformat(m.group(1))
            if d < TODAY - dt.timedelta(days=days * 2):
                prow.append([path.stem.upper(), str(d), f"{(TODAY - d).days}d"])
    print(aligned_table(["Alias", "Last reviewed", "Age"], prow) if prow else "None.")

    qa = ROOT / "context" / "qa-health-summary.md"
    m = re.search(r"Last updated[^0-9]*(\d{4}-\d{2}-\d{2})", read(qa), re.I)
    if m and dt.date.fromisoformat(m.group(1)) < cutoff:
        print(f"\nqa-health-summary.md last updated {m.group(1)} — consider a refresh.")
    return 0


# ---------------------------------------------------------------- main

def main(argv: list[str]) -> int:
    cmd = argv[1] if len(argv) > 1 else "all"
    if cmd == "validate":
        return validate()
    if cmd == "index":
        return index()
    if cmd == "coverage":
        return coverage()
    if cmd == "stale":
        return stale(int(argv[2]) if len(argv) > 2 else 21)
    if cmd == "all":
        index()
        rc = validate()
        coverage()
        stale()
        return rc
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
