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

## Cadre C, troisième réception (2026-09-25)

Un troisième message, reçu le même jour dans la même session, a apporté les textes intégraux des Snapshots 8, 7, 6, 5, 4 et 3, dans cet ordre, puis la lecture critique du Snapshot 2. Ils comblent la lacune consignée ci-dessus. Déposés sous `public/cadre-c/sources/snapshots/`, un fichier par texte, scindés aux titres « Snapshot N — » et à la phrase « Je lis ce texte comme le Snapshot 2 du banc d'essai ».

| Fichier | SHA-256 | Octets |
|---------|---------|--------|
| `snapshot-8.source.txt` | `6eb7a65d5cf57672ea74c17b48d7280a0fce823c0281cca0fb6b2c973ffbf2e5` | 16073 |
| `snapshot-7.source.txt` | `bead721ba243b8fdd9be1cdaa639924910cff377873991849a8f69e95c9d2f53` | 18683 |
| `snapshot-6.source.txt` | `c94a378484060bf94d550f2db5d293537aeccd1cfbf4476642612572a4318a9e` | 14678 |
| `snapshot-5.source.txt` | `03079fe6e60351a9e00f612f37e0ac4798eab0b8258ae358945647c7389d5f27` | 13307 |
| `snapshot-4.source.txt` | `b0ff4e6c04cb33e66349b994b7e99afd781a1920f2c83f43ac79576892a0ea85` | 10872 |
| `snapshot-3.source.txt` | `a006b0eb41eab85d4f07c30a0a069b52c849b2b508af038a0b0333c346896ee3` | 9319 |
| `snapshot-2-lecture.source.txt` | `bd057c5314a71fb5d73f7547c8e7b0c8df94d72e36ee876551c28cb5b9cbec0c` | 3512 |

Notes de fidélité et de cohérence, détaillées dans `public/cadre-c/cycle-snapshots-1-8.md` § 6 : tableaux aplatis au collage, aucune équation perdue ; le Snapshot 6 déclare ses données illustratives, ce qui requalifie le dossier ASU / ADU-3 de Drive en cas construit ; une incohérence interne consignée (180 000 décisions sur 18 mois contre 15 000 par mois) ; les chiffres du Snapshot 7 recalculent juste ; les règles 6.3 et 7.6 n'ont pas d'article dédié dans la Charte Générale.

## Cadre C, vérification complémentaire (2026-09-25, suite)

Recherche de meilleures copies des Snapshots 1 et 2 dans Drive et Notion : aucune. Relecture intégrale du dossier ASU / ADU-3 : aucun rappel du caractère illustratif déclaré par le Snapshot 6. Relecture intégrale de l'INDEX MAÎTRE du Cadre C (Drive `1jQC74FDtswy4asANHzKmJvYZ4mhqWSsMjCuSlqHjTto`) : neuf actifs sur dix attestés sur Drive, le dixième (outil logiciel) introuvable, dix liens d'accès pointant vers l'index lui-même, et redéfinition de R ≺ E et de L⃗ incompatible avec la Charte Générale ; même glissement du sens des lettres S, O, R, E dans la note technique. Relecture intégrale du Dictionnaire encyclopédique des termes du Cadre C (Drive `1x2dGajqjOZwRciVPr6vmdSzDcCuW_X9LmD-_LW157qE`, cinquante entrées dites opposables) : quinze notions centrales redéfinies à l'écart des sources, dont le pardon défini comme effacement rétroactif des registres, le vecteur L comme maximisation d'utilité, O comme objet ou algorithme, ρ en sens inversé et la saturation comme renvoi à un niveau supérieur. Consigné dans `public/cadre-c/cycle-snapshots-1-8.md` § 7 comme dérive lexicale ; les définitions de la Charte Générale, des Snapshots et des préférences déclarées font foi dans cette archive. Aucun document Drive modifié.
