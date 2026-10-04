# ASB — Archive publique des travaux

Dépôt public de sauvegarde et de rapatriement des travaux produits avec des agents IA pour Mik Mireault (`talkus`).

## Contenu

| Chemin | Origine | Description |
|--------|---------|-------------|
| [`public/harmonie-libre/`](public/harmonie-libre/) | [talkus/harmonie-libre](https://github.com/talkus/harmonie-libre) @ `fc7bac82` (2026-09-14) | Snapshot intégral : manifeste, Anneau des 23, Forteresse, registre de continuité, overview projets |
| [`public/exports/`](public/exports/) | Notion + Google Drive | Pipeline d'export (en attente des secrets) — inventaire 20 cibles |
| [`public/principes/`](public/principes/) | Sessions Claude Code, 2026-09-25 et 2026-09-29 | Négatif du Principe d'Alignement Universel en deux versions reçues (« Désalignement et Rupture », puis « Désalignement Universel » étendu à tout le principe) — textes reçus + SHA-256, diff, endroit reconstruit, concordances ; modèle « Deux schémas, une seule mécanique » (connexion et rupture) avec lettre de Copilot ; charte « Créer du lien, cultiver l'ouverture » comparée au modèle |
| [`public/cadre-c/`](public/cadre-c/) | Session Claude Code, 2026-09-25 | Cycle Snapshots 1 à 8 du cadre C : transcription reçue, puis textes intégraux des Snapshots 3 à 8 et lecture du Snapshot 2 — copies + SHA-256, lacunes de chaque copie, vérification des artefacts annoncés (2 attestés sur Drive, 1 non retrouvé), cohérence interne recalculée |
| [`public/doctor-live/`](public/doctor-live/) | Session Claude Code, 2026-10-04 | Programme DoctorLive reçu en zip — zip + SHA-256, copie extraite avec manifeste, exécution (certificat non émis), classement des 26 contrôles, CI reproduite, situation parmi les versions décrites sur Drive |

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

1. `NOTION_TOKEN` — puis partager les pages avec l'intégration Notion
2. `GOOGLE_SERVICE_ACCOUNT_JSON` (recommandé) **ou** `GOOGLE_OAUTH_TOKEN_JSON` — puis partager les dossiers Drive avec le compte de service
3. Relancer : `./tools/export/run_export.sh`

## Provenance

Voir [`PROVENANCE.md`](PROVENANCE.md).

## Licence / contribution

Le contenu sous `public/harmonie-libre/` suit les règles du dépôt source ([CODE-DE-CONDUITE](public/harmonie-libre/CODE-DE-CONDUITE.md), [CONTRIBUTION](public/harmonie-libre/CONTRIBUTION.md)).
