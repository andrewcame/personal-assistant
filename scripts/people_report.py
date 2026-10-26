#!/usr/bin/env python3
"""Build the People & Objectives board (team readiness, evidence, framework coverage). Standard library only.

Usage (from the repo root):
    python scripts/people_report.py          # writes reports/people.html and reports/people-data.json
    python scripts/people_report.py --json   # print the data only

Shares its parsers with scripts/report.py and its styles with scripts/report_template.html.
People data is limited to aliases, profile dates, and evidence counts — never ratings.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import report  # noqa: E402

ROOT = report.ROOT


def build() -> dict:
    recs, calls = report.records()
    achs = report.achievements()
    return {
        "generated": report.TODAY.isoformat(),
        "staleDays": report.STALE_DAYS,
        "achievements": achs,
        "team": report.team(),
        "coverage": report.coverage(recs, calls, achs),
    }


def main(argv: list[str]) -> int:
    data = build()
    if "--json" in argv:
        print(json.dumps(data, indent=1))
        return 0
    out_dir = ROOT / "reports"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "people-data.json").write_text(json.dumps(data, indent=1), encoding="utf-8")
    scripts = Path(__file__).parent
    main_template = (scripts / "report_template.html").read_text(encoding="utf-8")
    # reuse the fonts and stylesheet from the main board (everything up to </style>)
    head = main_template[: main_template.index("</style>") + len("</style>")]
    head = head.replace("<title>Quality Leadership Board</title>", "<title>People &amp; Objectives Board</title>")
    page = (scripts / "people_template.html").read_text(encoding="utf-8")
    page = page.replace("<!--__HEAD__-->", head).replace("/*__DATA__*/null", json.dumps(data).replace("</", "<\\/"))
    standalone = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"></head><body>\n' + page + '\n</body></html>\n'
    (out_dir / "people.html").write_text(standalone, encoding="utf-8")
    print(f"people report: reports/people.html ({len(data['team'])} team, {len(data['achievements'])} achievements)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
