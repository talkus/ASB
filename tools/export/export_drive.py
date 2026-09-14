#!/usr/bin/env python3
"""Export Google Drive folders/files into public/exports/drive/.

Auth (one of):
  GOOGLE_SERVICE_ACCOUNT_JSON  — raw JSON or path to service-account file
  GOOGLE_OAUTH_TOKEN_JSON      — authorized-user token JSON (refresh_token)

Optional:
  GOOGLE_DRIVE_FOLDER_IDS      — comma-separated folder IDs to mirror
  GOOGLE_DRIVE_FILE_IDS        — comma-separated file IDs to download
  GOOGLE_DRIVE_QUERY           — Drive search query (default: sharedWithMe or name contains project keywords)

Docs/Sheets/Slides are exported to markdown / csv / pdf when possible.
"""

from __future__ import annotations

import io
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from google.oauth2 import service_account
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaIoBaseDownload
except ImportError:
    print("Install deps: pip install -r tools/export/requirements.txt", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "public" / "exports" / "drive"
STATUS = ROOT / "public" / "exports" / "_status" / "drive.json"
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

EXPORT_MAP = {
    "application/vnd.google-apps.document": (
        "text/markdown",
        ".md",
    ),
    "application/vnd.google-apps.spreadsheet": (
        "text/csv",
        ".csv",
    ),
    "application/vnd.google-apps.presentation": (
        "application/pdf",
        ".pdf",
    ),
    "application/vnd.google-apps.drawing": (
        "image/png",
        ".png",
    ),
}


def slug(text: str, limit: int = 100) -> str:
    s = re.sub(r"[^\w\s\-.àâäéèêëïîôùûüç]", "", text, flags=re.I)
    s = re.sub(r"\s+", "-", s.strip())
    return (s or "file")[:limit]


def load_credentials():
    sa = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "").strip()
    oauth = os.environ.get("GOOGLE_OAUTH_TOKEN_JSON", "").strip()
    if sa:
        info = json.loads(Path(sa).read_text() if sa.startswith("/") or sa.endswith(".json") and Path(sa).exists() else sa)
        # Also try path if JSON parse fails visually — handled above
        if isinstance(info, str):
            info = json.loads(info)
        return service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
    if oauth:
        info = json.loads(Path(oauth).read_text() if Path(oauth).exists() else oauth)
        return Credentials.from_authorized_user_info(info, scopes=SCOPES)
    return None


def list_children(service, folder_id: str):
    cursor = None
    while True:
        resp = (
            service.files()
            .list(
                q=f"'{folder_id}' in parents and trashed=false",
                fields="nextPageToken, files(id, name, mimeType, modifiedTime, size, md5Checksum)",
                pageToken=cursor,
                pageSize=100,
                supportsAllDrives=True,
                includeItemsFromAllDrives=True,
            )
            .execute()
        )
        yield from resp.get("files", [])
        cursor = resp.get("nextPageToken")
        if not cursor:
            break


def search_files(service, query: str):
    cursor = None
    while True:
        resp = (
            service.files()
            .list(
                q=query,
                fields="nextPageToken, files(id, name, mimeType, modifiedTime, size, md5Checksum)",
                pageToken=cursor,
                pageSize=100,
                supportsAllDrives=True,
                includeItemsFromAllDrives=True,
            )
            .execute()
        )
        yield from resp.get("files", [])
        cursor = resp.get("nextPageToken")
        if not cursor:
            break


def download_file(service, file_meta: dict, dest: Path) -> dict:
    dest.parent.mkdir(parents=True, exist_ok=True)
    mime = file_meta["mimeType"]
    name = file_meta["name"]
    file_id = file_meta["id"]

    if mime in EXPORT_MAP:
        export_mime, ext = EXPORT_MAP[mime]
        out_path = dest / f"{slug(name)}{ext}"
        data = service.files().export_media(fileId=file_id, mimeType=export_mime).execute()
        out_path.write_bytes(data)
        method = "export"
    elif mime == "application/vnd.google-apps.folder":
        return {"id": file_id, "name": name, "type": "folder", "skipped": True}
    else:
        # keep original extension if present
        suffix = Path(name).suffix or ""
        out_path = dest / f"{slug(Path(name).stem)}{suffix}"
        request = service.files().get_media(fileId=file_id)
        buf = io.BytesIO()
        downloader = MediaIoBaseDownload(buf, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()
        out_path.write_bytes(buf.getvalue())
        method = "download"

    return {
        "id": file_id,
        "name": name,
        "mimeType": mime,
        "modifiedTime": file_meta.get("modifiedTime"),
        "md5Checksum": file_meta.get("md5Checksum"),
        "path": str(out_path.relative_to(ROOT)),
        "bytes": out_path.stat().st_size,
        "method": method,
    }


def mirror_folder(service, folder_id: str, dest: Path, results: list, errors: list, depth: int = 0):
    if depth > 12:
        errors.append({"folder_id": folder_id, "error": "max depth exceeded"})
        return
    for item in list_children(service, folder_id):
        if item["mimeType"] == "application/vnd.google-apps.folder":
            sub = dest / slug(item["name"])
            sub.mkdir(parents=True, exist_ok=True)
            mirror_folder(service, item["id"], sub, results, errors, depth + 1)
        else:
            try:
                results.append(download_file(service, item, dest))
                print(f"OK: {item['name']}")
            except Exception as exc:  # noqa: BLE001
                errors.append({"id": item["id"], "name": item.get("name"), "error": str(exc)})
                print(f"FAIL {item.get('name')}: {exc}", file=sys.stderr)


def main() -> int:
    creds = load_credentials()
    if not creds:
        print(
            "GOOGLE_SERVICE_ACCOUNT_JSON ou GOOGLE_OAUTH_TOKEN_JSON manquant.",
            file=sys.stderr,
        )
        STATUS.parent.mkdir(parents=True, exist_ok=True)
        STATUS.write_text(
            json.dumps(
                {
                    "ok": False,
                    "error": "Google credentials missing",
                    "at": datetime.now(timezone.utc).isoformat(),
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return 1

    service = build("drive", "v3", credentials=creds, cache_discovery=False)
    OUT.mkdir(parents=True, exist_ok=True)
    results: list[dict] = []
    errors: list[dict] = []

    folder_ids = [x.strip() for x in os.environ.get("GOOGLE_DRIVE_FOLDER_IDS", "").split(",") if x.strip()]
    file_ids = [x.strip() for x in os.environ.get("GOOGLE_DRIVE_FILE_IDS", "").split(",") if x.strip()]
    query = os.environ.get("GOOGLE_DRIVE_QUERY", "").strip()

    if not folder_ids and not file_ids and not query:
        # Heuristic: files shared with the service account / user matching known project names
        query = (
            "trashed=false and ("
            "name contains 'WayMaker' or "
            "name contains 'Anneau' or "
            "name contains 'AEGIS' or "
            "name contains 'Mammouth' or "
            "name contains 'thermodynamique' or "
            "name contains 'Théorie' or "
            "name contains 'CAPA' or "
            "name contains 'biblique' or "
            "sharedWithMe"
            ")"
        )

    for fid in folder_ids:
        dest = OUT / "folders" / fid
        dest.mkdir(parents=True, exist_ok=True)
        try:
            meta = service.files().get(fileId=fid, fields="id,name").execute()
            folder_dest = OUT / "folders" / slug(meta["name"])
            folder_dest.mkdir(parents=True, exist_ok=True)
            mirror_folder(service, fid, folder_dest, results, errors)
        except Exception as exc:  # noqa: BLE001
            errors.append({"folder_id": fid, "error": str(exc)})

    for file_id in file_ids:
        try:
            meta = (
                service.files()
                .get(fileId=file_id, fields="id, name, mimeType, modifiedTime, size, md5Checksum")
                .execute()
            )
            results.append(download_file(service, meta, OUT / "files"))
        except Exception as exc:  # noqa: BLE001
            errors.append({"file_id": file_id, "error": str(exc)})

    if query:
        for item in search_files(service, query):
            if item["mimeType"] == "application/vnd.google-apps.folder":
                folder_dest = OUT / "search" / slug(item["name"])
                folder_dest.mkdir(parents=True, exist_ok=True)
                mirror_folder(service, item["id"], folder_dest, results, errors)
            else:
                try:
                    results.append(download_file(service, item, OUT / "search"))
                    print(f"OK: {item['name']}")
                except Exception as exc:  # noqa: BLE001
                    errors.append({"id": item["id"], "name": item.get("name"), "error": str(exc)})

    report = {
        "ok": bool(results) and not errors,
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "files": results,
        "errors": errors,
        "count": len(results),
    }
    STATUS.parent.mkdir(parents=True, exist_ok=True)
    STATUS.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUT / "INDEX.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Drive: {len(results)} files, {len(errors)} errors")
    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main())
