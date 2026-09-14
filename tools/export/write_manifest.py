#!/usr/bin/env python3
"""Build public/exports/manifest from status files + target inventory."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPORTS = ROOT / "public" / "exports"
MANIFEST = EXPORTS / "manifest" / "EXPORT_MANIFEST.json"
TARGETS = EXPORTS / "manifest" / "TARGETS.json"  # inventaire cible


def load(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    targets = load(TARGETS) or {"items": []}
    notion = load(EXPORTS / "_status" / "notion.json")
    drive = load(EXPORTS / "_status" / "drive.json")

    notion_titles = {p.get("title", "").lower() for p in (notion or {}).get("pages", [])}
    drive_names = {f.get("name", "").lower() for f in (drive or {}).get("files", [])}

    items = []
    for item in targets.get("items", []):
        status = "pending"
        matched = None
        needle = (item.get("match") or item.get("title") or "").lower()
        source = item.get("source")
        if source == "notion" and notion and notion.get("ok") is not False:
            for t in notion_titles:
                if needle and needle in t:
                    status = "exported"
                    matched = t
                    break
            if status == "pending" and notion.get("error"):
                status = "blocked_auth"
        elif source == "drive" and drive and drive.get("ok") is not False:
            for n in drive_names:
                if needle and needle in n:
                    status = "exported"
                    matched = n
                    break
            if status == "pending" and drive.get("error"):
                status = "blocked_auth"
        elif source in {"notion", "drive"}:
            if (source == "notion" and notion and notion.get("error")) or (
                source == "drive" and drive and drive.get("error")
            ):
                status = "blocked_auth"
        items.append({**item, "status": status, "matched": matched})

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "notion": notion,
        "drive": drive,
        "items": items,
        "summary": {
            "total": len(items),
            "exported": sum(1 for i in items if i["status"] == "exported"),
            "blocked_auth": sum(1 for i in items if i["status"] == "blocked_auth"),
            "pending": sum(1 for i in items if i["status"] == "pending"),
        },
    }
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    md = ["# Manifeste d'export", "", f"Généré : `{report['generated_at']}`", ""]
    s = report["summary"]
    md.append(
        f"**{s['exported']}** exportés · **{s['blocked_auth']}** bloqués (auth) · **{s['pending']}** en attente / **{s['total']}**"
    )
    md.append("")
    md.append("| Titre | Source | Statut |")
    md.append("|-------|--------|--------|")
    for i in items:
        md.append(f"| {i.get('title','')} | {i.get('source','')} | `{i['status']}` |")
    md.append("")
    (EXPORTS / "manifest" / "EXPORT_MANIFEST.md").write_text("\n".join(md), encoding="utf-8")
    print(f"Manifest: {s}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
