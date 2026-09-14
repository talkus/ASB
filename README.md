# ASB — Archive publique des travaux

Dépôt public de sauvegarde et de rapatriement des travaux produits avec des agents IA pour Mik Mireault (`talkus`).

## Contenu

| Chemin | Origine | Description |
|--------|---------|-------------|
| [`public/harmonie-libre/`](public/harmonie-libre/) | [talkus/harmonie-libre](https://github.com/talkus/harmonie-libre) @ `fc7bac82` (2026-09-14) | Snapshot intégral : manifeste, Anneau des 23, Forteresse, registre de continuité, overview projets |
| [`public/exports/`](public/exports/) | Notion + Google Drive | Pipeline d’export (en attente des secrets) — inventaire 20 cibles |

## Modules inclus (harmonie-libre)

- **Manifeste & site** — `harmonie-libre-v0.1.md`, `index.html`, discussions, versions
- **Anneau des 23** — analyseur, VRF, registre, invariants, certificats
- **Forteresse** — PWA / manifeste offline
- **Registre de continuité** — DuckDB, attestations Ed25519, graphe causal, gouvernance, tests
- **PROJETS_OVERVIEW.md** — inventaire des projets (théorie, thermodynamique, corpus biblique, WayMaker)

## Export Notion / Drive

Scripts : [`tools/export/`](tools/export/) — guide : [`tools/export/README.md`](tools/export/README.md)

Suivi : [`public/exports/manifest/EXPORT_MANIFEST.md`](public/exports/manifest/EXPORT_MANIFEST.md)

**Statut actuel : 0/20 exportés — secrets manquants.**

Pour débloquer, ajouter dans les secrets Cloud Agent de ce dépôt :

1. `NOTION_TOKEN` — puis partager les pages avec l’intégration Notion  
2. `GOOGLE_SERVICE_ACCOUNT_JSON` (recommandé) **ou** `GOOGLE_OAUTH_TOKEN_JSON` — puis partager les dossiers Drive avec le compte de service  
3. Relancer : `./tools/export/run_export.sh`

## Provenance

Voir [`PROVENANCE.md`](PROVENANCE.md).

## Licence / contribution

Le contenu sous `public/harmonie-libre/` suit les règles du dépôt source ([CODE-DE-CONDUITE](public/harmonie-libre/CODE-DE-CONDUITE.md), [CONTRIBUTION](public/harmonie-libre/CONTRIBUTION.md)).
