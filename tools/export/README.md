# Export Notion + Google Drive → ASB

Pipeline pour rapatrier les brouillons Notion et les archives Drive dans `public/exports/`.

## Prérequis (secrets Cloud Agent)

À ajouter dans l’environnement Cursor Cloud Agent pour ce dépôt :

| Secret | Rôle |
|--------|------|
| `NOTION_TOKEN` | Jeton d’intégration Notion (partager chaque page/base avec l’intégration) |
| `GOOGLE_SERVICE_ACCOUNT_JSON` **ou** `GOOGLE_OAUTH_TOKEN_JSON` | Accès Drive en lecture |
| `GOOGLE_DRIVE_FOLDER_IDS` (optionnel) | IDs de dossiers à mirroir |
| `NOTION_ROOT_PAGE_ID` (optionnel) | Hub Notion à exporter en priorité |
| `NOTION_DATABASE_IDS` (optionnel) | Bases (WayMaker tableaux, etc.) |

### Notion
1. Créer une intégration sur https://www.notion.so/my-integrations  
2. Copier le secret → `NOTION_TOKEN`  
3. Sur chaque page à exporter : `⋯` → *Connections* → ajouter l’intégration  

### Google Drive
**Option A — compte de service (recommandé)**  
1. Créer un service account GCP + clé JSON  
2. Partager les dossiers/fichiers Drive avec l’email du service account (lecteur)  
3. Coller le JSON complet dans `GOOGLE_SERVICE_ACCOUNT_JSON`  

**Option B — OAuth utilisateur**  
Fournir un JSON authorized-user avec `refresh_token` dans `GOOGLE_OAUTH_TOKEN_JSON`.

## Lancer

```bash
chmod +x tools/export/run_export.sh
./tools/export/run_export.sh
```

Sorties :
- `public/exports/notion/` — pages Markdown + meta JSON, bases CSV/JSON  
- `public/exports/drive/` — fichiers / exports Docs→md, Sheets→csv  
- `public/exports/manifest/EXPORT_MANIFEST.md` — suivi vs inventaire cible  
- `public/exports/_status/` — rapports machine-readable  

## Inventaire cible

Voir [`public/exports/manifest/TARGETS.json`](../public/exports/manifest/TARGETS.json) (12 pages Notion + sources Drive listées dans `PROJETS_OVERVIEW.md`).
