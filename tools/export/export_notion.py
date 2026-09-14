#!/usr/bin/env python3
"""Export Notion pages shared with the integration into public/exports/notion/.

Required secrets:
  NOTION_TOKEN          — integration secret (ntn_… / secret_…)
Optional:
  NOTION_ROOT_PAGE_ID   — limit crawl to one hub page and its children
  NOTION_DATABASE_IDS   — comma-separated database IDs to dump as CSV+JSON
"""

from __future__ import annotations

import csv
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from notion_client import Client
except ImportError:
    print("Install deps: pip install -r tools/export/requirements.txt", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "public" / "exports" / "notion"
STATUS = ROOT / "public" / "exports" / "_status" / "notion.json"


def slug(text: str, limit: int = 80) -> str:
    s = re.sub(r"[^\w\s\-àâäéèêëïîôùûüç]", "", text.lower(), flags=re.I)
    s = re.sub(r"\s+", "-", s.strip())
    return (s or "page")[:limit]


def rich_text(parts: list | None) -> str:
    if not parts:
        return ""
    return "".join(p.get("plain_text", "") for p in parts)


def block_to_md(block: dict) -> str:
    t = block.get("type")
    data = block.get(t, {}) if t else {}
    text = rich_text(data.get("rich_text"))
    if t == "paragraph":
        return text
    if t == "heading_1":
        return f"# {text}"
    if t == "heading_2":
        return f"## {text}"
    if t == "heading_3":
        return f"### {text}"
    if t == "bulleted_list_item":
        return f"- {text}"
    if t == "numbered_list_item":
        return f"1. {text}"
    if t == "to_do":
        mark = "x" if data.get("checked") else " "
        return f"- [{mark}] {text}"
    if t == "quote":
        return f"> {text}"
    if t == "code":
        lang = data.get("language") or ""
        return f"```{lang}\n{text}\n```"
    if t == "divider":
        return "---"
    if t == "callout":
        return f"> {text}"
    if t == "toggle":
        return f"<details><summary>{text}</summary>\n\n</details>"
    if t in {"child_page", "child_database"}:
        title = data.get("title") or text or t
        return f"<!-- child: {title} -->"
    if t == "image":
        url = (data.get("file") or data.get("external") or {}).get("url", "")
        return f"![image]({url})" if url else ""
    if t == "bookmark":
        url = data.get("url", "")
        return f"[bookmark]({url})" if url else ""
    if t == "equation":
        return f"$$\n{data.get('expression', '')}\n$$"
    return f"<!-- unsupported block: {t} -->"


def iter_blocks(notion: Client, block_id: str):
    cursor = None
    while True:
        resp = notion.blocks.children.list(block_id=block_id, start_cursor=cursor)
        for b in resp.get("results", []):
            yield b
            if b.get("has_children") and b.get("type") not in {"child_page", "child_database"}:
                for child in iter_blocks(notion, b["id"]):
                    yield child
        if not resp.get("has_more"):
            break
        cursor = resp.get("next_cursor")


def page_title(page: dict) -> str:
    props = page.get("properties") or {}
    for prop in props.values():
        if prop.get("type") == "title":
            return rich_text(prop.get("title")) or "untitled"
    return "untitled"


def export_page(notion: Client, page_id: str, dest_dir: Path) -> dict:
    page = notion.pages.retrieve(page_id=page_id)
    title = page_title(page)
    lines = [f"# {title}", ""]
    for block in iter_blocks(notion, page_id):
        line = block_to_md(block)
        if line:
            lines.append(line)
            lines.append("")
    dest_dir.mkdir(parents=True, exist_ok=True)
    md_path = dest_dir / f"{slug(title)}.md"
    meta_path = dest_dir / f"{slug(title)}.meta.json"
    md_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    meta = {
        "id": page_id,
        "title": title,
        "url": page.get("url"),
        "last_edited_time": page.get("last_edited_time"),
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "markdown": str(md_path.relative_to(ROOT)),
    }
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return meta


def export_database(notion: Client, database_id: str, dest_dir: Path) -> dict:
    db = notion.databases.retrieve(database_id=database_id)
    title = rich_text(db.get("title")) or "database"
    dest_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    cursor = None
    while True:
        resp = notion.databases.query(database_id=database_id, start_cursor=cursor)
        for page in resp.get("results", []):
            flat = {"id": page["id"], "url": page.get("url")}
            for name, prop in (page.get("properties") or {}).items():
                ptype = prop.get("type")
                val = prop.get(ptype)
                if ptype == "title":
                    flat[name] = rich_text(val)
                elif ptype == "rich_text":
                    flat[name] = rich_text(val)
                elif ptype == "number":
                    flat[name] = val
                elif ptype == "select":
                    flat[name] = (val or {}).get("name")
                elif ptype == "multi_select":
                    flat[name] = ", ".join(x.get("name", "") for x in (val or []))
                elif ptype == "checkbox":
                    flat[name] = bool(val)
                elif ptype == "url":
                    flat[name] = val
                elif ptype == "email":
                    flat[name] = val
                elif ptype == "date":
                    flat[name] = (val or {}).get("start")
                elif ptype == "status":
                    flat[name] = (val or {}).get("name")
                else:
                    flat[name] = json.dumps(val, ensure_ascii=False) if val is not None else None
            rows.append(flat)
        if not resp.get("has_more"):
            break
        cursor = resp.get("next_cursor")

    json_path = dest_dir / f"{slug(title)}.json"
    csv_path = dest_dir / f"{slug(title)}.csv"
    json_path.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if rows:
        keys = sorted({k for r in rows for k in r})
        with csv_path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(rows)
    return {
        "id": database_id,
        "title": title,
        "rows": len(rows),
        "json": str(json_path.relative_to(ROOT)),
        "csv": str(csv_path.relative_to(ROOT)) if rows else None,
    }


def search_all(notion: Client) -> tuple[list[str], list[str]]:
    pages, databases = [], []
    cursor = None
    while True:
        resp = notion.search(start_cursor=cursor)
        for item in resp.get("results", []):
            if item.get("object") == "page":
                pages.append(item["id"])
            elif item.get("object") == "database":
                databases.append(item["id"])
        if not resp.get("has_more"):
            break
        cursor = resp.get("next_cursor")
    return pages, databases


def main() -> int:
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        print("NOTION_TOKEN manquant — export Notion impossible.", file=sys.stderr)
        STATUS.parent.mkdir(parents=True, exist_ok=True)
        STATUS.write_text(
            json.dumps(
                {
                    "ok": False,
                    "error": "NOTION_TOKEN missing",
                    "at": datetime.now(timezone.utc).isoformat(),
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return 1

    notion = Client(auth=token)
    OUT.mkdir(parents=True, exist_ok=True)

    page_ids: list[str] = []
    db_ids: list[str] = []

    root = os.environ.get("NOTION_ROOT_PAGE_ID")
    if root:
        page_ids.append(root)
    env_dbs = os.environ.get("NOTION_DATABASE_IDS", "").strip()
    if env_dbs:
        db_ids.extend(x.strip() for x in env_dbs.split(",") if x.strip())

    if not page_ids and not db_ids:
        found_pages, found_dbs = search_all(notion)
        page_ids.extend(found_pages)
        db_ids.extend(found_dbs)

    exported_pages = []
    exported_dbs = []
    errors = []

    for pid in dict.fromkeys(page_ids):
        try:
            exported_pages.append(export_page(notion, pid, OUT / "pages"))
            print(f"page OK: {exported_pages[-1]['title']}")
        except Exception as exc:  # noqa: BLE001 — surface per-page failures
            errors.append({"page_id": pid, "error": str(exc)})
            print(f"page FAIL {pid}: {exc}", file=sys.stderr)

    for did in dict.fromkeys(db_ids):
        try:
            exported_dbs.append(export_database(notion, did, OUT / "databases"))
            print(f"database OK: {exported_dbs[-1]['title']} ({exported_dbs[-1]['rows']} rows)")
        except Exception as exc:  # noqa: BLE001
            errors.append({"database_id": did, "error": str(exc)})
            print(f"database FAIL {did}: {exc}", file=sys.stderr)

    report = {
        "ok": not errors,
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "pages": exported_pages,
        "databases": exported_dbs,
        "errors": errors,
    }
    STATUS.parent.mkdir(parents=True, exist_ok=True)
    STATUS.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUT / "INDEX.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Notion: {len(exported_pages)} pages, {len(exported_dbs)} databases, {len(errors)} errors")
    return 0 if exported_pages or exported_dbs else 1


if __name__ == "__main__":
    raise SystemExit(main())
