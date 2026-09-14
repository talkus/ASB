#!/usr/bin/env bash
# Lance les exports Notion + Drive si les secrets sont présents.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

python3 -m pip install -q -r tools/export/requirements.txt

code=0
python3 tools/export/export_notion.py || code=$?
python3 tools/export/export_drive.py || code=$?

python3 tools/export/write_manifest.py || true
exit "$code"
