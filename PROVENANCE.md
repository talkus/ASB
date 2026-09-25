# Provenance du rapatriement

## Snapshot `public/harmonie-libre/`

| Champ | Valeur |
|-------|--------|
| Dépôt source | https://github.com/talkus/harmonie-libre |
| Branche | `main` |
| Commit | `fc7bac82d310569ff0cd0035c007ce207c0bf6c5` |
| Date du commit | 2026-09-14T00:20:43+00:00 |
| Message | fix: sync FK causale — e2e_bootstrap + apply_transition + migration 012 |
| Fichiers | 86 |
| Date de copie dans ASB | 2026-09-14 |

## Méthode

Clone shallow du dépôt public `talkus/harmonie-libre`, copie des fichiers hors `.git` vers `public/harmonie-libre/`. Aucune modification du contenu source lors de la copie.

## Autres dépôts `talkus` (non dupliqués)

Les forks suivants existent déjà en public sur GitHub et ne sont pas recopiés ici :

- `opencode` ← anomalyco/opencode
- `ECC` ← affaan-m/ECC
- `academic-research-skills` ← Imbad0202/academic-research-skills
- `scientific-agent-skills` ← K-Dense-AI/scientific-agent-skills
- `minimind` ← jingyaogong/minimind
- `openclaude` ← Gitlawb/openclaude
- `awesome-design-md` ← VoltAgent/awesome-design-md
- `Tutorial` — quasi vide (heartbeat probe)

Seul le travail original (`harmonie-libre`) est archivé dans ce dépôt.

## Export Notion / Drive (2026-09-14)

Pipeline ajouté sous `tools/export/`. Exécution sans secrets → statut `blocked_auth` pour les 20 cibles (voir `public/exports/manifest/EXPORT_MANIFEST.md`).

Secrets requis pour un export réel : `NOTION_TOKEN`, `GOOGLE_SERVICE_ACCOUNT_JSON` ou `GOOGLE_OAUTH_TOKEN_JSON`.

## Principes (2026-09-25)

| Champ | Valeur |
|-------|--------|
| Fichier | `public/principes/principe-desalignement-rupture.md` |
| Source brute | `public/principes/sources/principe-desalignement-rupture.source.txt` |
| SHA-256 (source brute) | `b9c2bceb74648eee01177d0b5718329788834123f1313beb93483d081705aaff` |
| Origine | Texte fourni par l'utilisateur en session Claude Code (branche `claude/desalignement-rupture-7tb12k`), présenté comme « inversion sémantique terme à terme » du principe d'alignement |
| Date de réception | 2026-09-25 |

Le texte positif d'origine n'a pas été retrouvé verbatim (dépôt, Notion, Google Drive consultés le 2026-09-25). L'endroit inclus dans la fiche est une **reconstruction analytique**, signalée comme telle ; les concordances renvoient aux sources apparentées attestées (Charte du Principe d'Alignement Universel et version pédagogique sur Drive, CONDITIONS_ALIGNEMENT sur Drive, Forteresse dans ce dépôt).

## Principes, seconde réception, et Cadre C (2026-09-25)

Un second message, reçu le même jour dans la même session, contenait deux textes distincts. Il a été scindé à la phrase « La branche locale étant close et son rôle diagnostique consigné, nous ré-ancrons immédiatement le travail sur la trajectoire active ».

| Champ | Valeur |
|-------|--------|
| Fichier | `public/principes/principe-desalignement-universel.md` |
| Source brute | `public/principes/sources/principe-desalignement-universel.source.txt` |
| SHA-256 (source brute) | `c7c13870ac13f1906c017914af439bc20a6147741ac6aa926801a237ea4ff934` |
| Origine | Seconde version du négatif, titrée « Principe de Désalignement Universel », étendue aux régulateurs, au mantra, à l'arbre des dix pôles, aux axes et à la discipline mémorielle ; quatre envois successifs conservés avec leurs phrases d'introduction |
| Date de réception | 2026-09-25 |

| Champ | Valeur |
|-------|--------|
| Fichier | `public/cadre-c/cycle-snapshots-1-8.md` |
| Source brute | `public/cadre-c/sources/cycle-snapshots-1-8.transcript.txt` |
| SHA-256 (source brute) | `2f75eb817ee21e103ad801524e399b2e34cfdc26a1239a789fd3a92eb27ecd89` |
| Origine | Transcription d'un dialogue de recherche sur le cadre C (Snapshots 1 à 8), rôles non étiquetés, équations perdues au collage, textes des Snapshots 3 à 8 absents |
| Date de réception | 2026-09-25 |

Les empreintes attestent les copies déposées dans ce dépôt, telles que reçues dans la session. Elles ne disent rien de l'original chez l'expéditeur.

Vérification des artefacts que la transcription déclare produits (Drive, Notion et ce dépôt consultés le 2026-09-25) : la Charte Générale et Manuel de Gouvernance du Cadre C (Drive `1BSDnIHkohDOauQ1QoNcdV7CD3t77EbuqWzHJjRKddtI`, relue, 29 articles) et le Dossier d'Ingénierie Institutionnelle ASU / ADU-3 (Drive `1I5enlC6scgxUwI7kOPrUxiJJ0IencQDgLKZuiAHZvtI`) existent ; le paquet Python `c_runtime` et ses 18 tests n'ont été retrouvés nulle part. Les documents Drive ne sont pas recopiés ici.
