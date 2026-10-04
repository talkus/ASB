# DoctorLive — version reçue le 2026-10-04

Projet Python « DoctorLive » envoyé sous forme de zip le 2026-10-04, sans message d'accompagnement. Il exécute 26 contrôles sur l'Anneau des 23 et n'émet un certificat, `CERT_PLEIN`, que si tous passent. Plusieurs versions de ce programme ont circulé la même nuit entre Gemini, GPT, Mistral et une autre session Claude ; celle-ci est la seule à refuser le certificat.

## Statut des couches de ce document

| Couche | Statut | Contenu |
|--------|--------|---------|
| Source | **Source attestée** | Zip reçu tel quel le 2026-10-04 (session Claude Code, dépôt `talkus/ASB`, branche `claude/desalignement-rupture-7tb12k`) : [`sources/project_doctor_live.zip`](sources/project_doctor_live.zip), SHA-256 `6112c70b1a42624b008d0bdcd0b3826c1b9a47b5de62579b18380f0f8456144c`, 6531 octets, 17 fichiers. Copie extraite sous [`project/`](project/), identique octet pour octet ; empreinte de chaque fichier dans [`sources/MANIFEST.sha256`](sources/MANIFEST.sha256). Horodatage interne des fichiers : 2026-10-04, de 01:53 à 02:04, sans fuseau. |
| § 1 à § 4 | **Dérivation consolidée** | Lecture intégrale des 17 fichiers, exécution du programme, essais ciblés, reproduction de la CI déclarée. Tout a été exécuté le 2026-10-04 dans un environnement isolé, avec Python 3.11. |
| § 5 | **Dérivation consolidée** | Situation de cette version parmi celles décrites sur Google Drive. |
| § 6 | **Reconstruction analytique** | Ce que les contrôles attestent, et ce qu'ils n'attestent pas. |

Le code n'utilise que la bibliothèque standard. Il n'ouvre aucune connexion et n'écrit aucun fichier. Les dossiers `project/.github/workflows/` sont archivés mais inertes : GitHub ne lit que les workflows placés à la racine d'un dépôt.

---

## 1. Exécution (dérivation consolidée)

`python main.py` affiche 26 lignes de contrôle puis une ligne `global`. Résultat : 8 FAIL, 18 PASS, `global : FAIL`, « CERT_PLEIN non emis ».

Le README du projet dit : « CERT_PLEIN n'est émis que si toutes les lignes sont vraies. » C'est exact : `global` est la conjonction des 26 lignes. Il nomme trois causes d'échec, le registre des sièges vide, le journal qui ne vérifie pas de chaîne et le reçu S-24 non lu. Elles expliquent quatre des huit FAIL. Les quatre autres, `secrets_env`, `doctor_pass`, `quorum_diversite` et `verificateur_deterministe`, ne sont pas mentionnés. Il précise enfin : « La couverture 69 est la définition 23 × 3, pas une observation d'un anneau. » C'est exact aussi.

## 2. Ce que vérifie chaque ligne (dérivation consolidée)

Classement établi par lecture du code puis confirmé à l'exécution (§ 3).

| Catégorie | Lignes | Nombre | Ce qui décide du résultat |
|-----------|--------|-------:|---------------------------|
| FAIL par constante | `secrets_env`, `doctor_pass`, `quorum_diversite`, `verificateur_deterministe`, `recu_S24` | 5 | La valeur `False` écrite dans le code. Aucune source extérieure ne peut les faire passer. |
| FAIL selon une source | `sieges_instancies` | 1 | Le nombre d'entrées du registre `AI_REGISTRY`, vide. Vingt-trois entrées quelconques suffiraient à la faire passer : la ligne compte, elle n'instancie rien. |
| FAIL selon une source | `cycle_tracable`, `merkle_ancre` | 2 | Le même appel, `journal.verify_chain()`, qui renvoie `False`. Deux noms pour un seul contrôle. |
| PASS par arithmétique | les cinq lignes `231_portes_*`, `231_couverture_69_par_cycle`, `231_pas_double_comptage` | 7 | Des égalités entre nombres : C(22,2) = 231, 231 × 2 = 462, 3 × 7 × 11 = 231, 3 + 21 + 66 + 21 + 36 + 84 = 231, 23 × 3 = 69, et deux littéraux comparés à eux-mêmes. Elles passent quel que soit l'état du système. |
| PASS sur un état neuf | `chesed_invariant_dette_positive`, `chesed_invariant_restrictions_positive` | 2 | Un objet tout juste créé, dont les compteurs valent 0. Aucune opération n'est appliquée avant le test. |
| PASS par construction | `chesed_dette_ne_force_pas_autorisation`, `chesed_dette_max_ne_debloque_jamais_critique` | 2 | La fonction `decider` ne lit ni la dette ni le gouverneur, et ne renvoie jamais une action interdite. La propriété ne peut pas échouer. |
| PASS sur un comportement | `chesed_danger_critique_isoler`, `chesed_mesure_uniquement_apres_succes`, `chesed_13_restrictions_dette_5`, `chesed_saturation_suspend`, `chesed_decision_grave_revision_humaine`, `chesed_overshoot_acquitte`, `chesed_journalisation_separee` | 7 | Une suite d'opérations dont le résultat pourrait être faux si le code changeait. |

Deux réserves sur les sept derniers. `chesed_overshoot_acquitte` acquitte exactement la dette due et ne dépasse jamais ; le dépassement est bien bloqué par le code, mais la ligne ne l'éprouve pas. `chesed_decision_grave_revision_humaine` teste `restriction_minimale_suffisante`, une copie de `decider` que `decider` n'appelle pas.

En résumé, sur 18 PASS, 7 éprouvent un comportement et 11 passent quoi que fasse le système.

## 3. Comportements vérifiés à l'exécution (dérivation consolidée)

| Essai | Résultat |
|-------|----------|
| `decider` avec un gouverneur absent, puis avec une dette d'un milliard | Même décision dans les deux cas, `QUARANTAINE` pour un danger modéré. La dette n'entre pas dans la décision. |
| Actions que `decider` peut renvoyer | `QUARANTAINE` et `ISOLER` seulement. `AUTORISER` et `LEVER_RESTRICTION` sont hors de sa portée. |
| `JournalChesed().verify_chain()`, vide puis rempli de 999 entrées arbitraires | `True` dans les deux cas. Le journal de `journal.py` renvoie au contraire `False`. |
| Six acquittements pour une dette de 5 | La dette s'arrête à 0, cinq acquittements sont journalisés. Le garde-fou fonctionne. |
| Acquittement d'une mesure jamais planifiée | Accepté. La liste des obligations planifiées reste vide. |
| Remise à zéro des restrictions dites « consécutives » | Aucune dans le code. Le compteur est cumulatif. |

## 4. Reproduction de la CI déclarée (dérivation consolidée)

Le projet déclare une CI à trois étapes : `ruff check .`, `ruff format . --check`, `pytest`. Reproduite à l'identique dans un environnement neuf, après `pip install -e ".[dev]"`, elle échoue aux trois étapes. Le résultat est le même avec ruff 0.16.10, version installée par `ruff>=0.13.0`, et avec ruff 0.13.2, version épinglée dans `.pre-commit-config.yaml`.

| Étape | Résultat | Cause |
|-------|----------|-------|
| `ruff check .` | 10 erreurs | 1 import inutilisé (`dataclasses.field`), 3 blocs d'imports non triés, 6 lignes de plus de 100 caractères dans `doctor_live.py` |
| `ruff format . --check` | 5 fichiers à reformater | Lignes vides attendues entre les définitions |
| `pytest` | Erreur à la collecte | `ModuleNotFoundError: No module named 'journal'`. `journal.py` n'est pas inclus dans le paquet, et le dossier `tests/` n'a pas de `__init__.py` qui ferait entrer la racine du projet dans le chemin d'import. |

Avec `python -m pytest`, qui ajoute le dossier courant au chemin d'import, les deux tests passent.

## 5. Situation parmi les versions décrites sur Drive (dérivation consolidée)

| Version | Source | Ce qui en est attesté |
|---------|--------|-----------------------|
| `doctor.py` | Google Drive, fichier `1fz1hEYVz7-GdMx_OyDbRgMhjrkurwndH`, 2026-10-02 | L'extrait lu montre `secrets_env`, `doctor_pass`, `quorum_diversite`, `verificateur_deterministe` et `recu_S24` fixés à `True`. |
| `doctor_live_package.zip` de Gemini | Drive `1gUPtcMth6E3llXLdCNdVL4rANibQ9wtw`, SHA-256 déclaré `c90b0f5ce704a53a28a8db313764ec8ef3a570971606a87101cddd2d0f1006e2`, 18 fichiers ; transmission Drive `1r-EkvHzAOG4klc-HCeS0jObj-WybwPvaVGShkmwWpxQ` | La transmission annonce « CERT_PLEIN homologué », 26 contrôles sur 26 réussis, « 23/23 sièges IA instanciés », l'« intégrité de la chaîne SHA-256 (JournalChesed) », et déclare le code, les tests et la CI « opérationnel, éprouvé et scellé ». Ce zip n'a pas été exécuté ici. |
| `doctor_live_memory_cascade.zip` de Gemini | Drive `1-Uw_VTiBjDcfpG_N3op7S_GYyQGkFKgY` ; vérification de Mistral, Drive `1KqsuMqzmsH6j-37cjsBFCIFry2GTm8gIhhgK2ncsoH0` | Mistral l'a exécuté : 27 PASS, certificat émis. Il note que « les 5 contrôles codés en dur […] sont déclaratifs — leur PASS n'atteste rien », et que « le bloc Chesed, lui, est réellement falsifiable et il passe ». |
| `project_doctor_live.zip`, cette version | Ce dossier | Les cinq constantes sont à `False`, le registre est vide, le journal ne certifie rien, le certificat n'est pas émis. |
| Même zip, autre session Claude | Drive `14qyDGDomgdHesCUryOE1akOXy9qO0RiAF5Enw-JQoqk` (« Claude — Archives propres 01 ») | Même résultat d'ensemble. Elle conclut : « La version du ZIP est la version honnête », et classe les contrôles Chesed/Gevurah en « 11/11 PASS (vrais tests) ». |

Le passage d'une version à l'autre retourne les cinq constantes de `True` à `False`. C'est ce qui sépare un certificat émis d'un certificat refusé.

## 6. Ce que les contrôles attestent (reconstruction analytique)

**Au niveau du certificat, cette version est honnête.** Elle refuse `CERT_PLEIN` tant que rien ne le fonde, et son README le dit. Trois lectures convergent sur ce point : celle-ci, celle de l'autre session Claude, et celle de Mistral sur les cinq constantes.

**Le bloc Chesed/Gevurah est falsifiable aux sept onzièmes.** Les deux sessions précédentes le tenaient pour entièrement fait de vrais tests. Quatre de ses lignes passeraient pourtant même si le code ignorait la dette ou la laissait devenir négative : deux portent sur un objet neuf, deux sur une fonction qui ne lit pas la dette. Ce n'est pas une faute du code de décision. C'est une limite de ce que ces lignes prouvent.

**Le journal Chesed certifie n'importe quoi.** `JournalChesed.verify_chain` renvoie `True` sans rien calculer, y compris sur des données arbitraires. Il n'est appelé par aucun contrôle de cette version, et le nombre de PASS n'en dépend pas. Mais c'est la convention inverse de `journal.py`, dont le talon renvoie `False`, et l'inverse de ce que la transmission de Gemini annonçait pour ce journal. Tout usage futur hériterait d'une vérification qui ne peut pas échouer.

**Sept PASS sur dix-huit sont de l'arithmétique.** Ils sont vrais, mais ils ne disent rien d'un anneau ni d'un journal. Le README le reconnaît pour la couverture de 69. La même mention vaudrait pour les six autres. Le Snapshot 8 du Cadre C, archivé dans ce dépôt, nomme ce risque dans sa première dérive : des « rites (audits, fire drills, saturations) qui produisent de la légitimité sans produire de justice ». Son correctif s'applique ici mot pour mot : « Un audit qui ne change rien est un audit échoué. »

**La CI annoncée ne passe pas, pour cette version.** Ses trois étapes échouent, pour des causes mineures et toutes corrigeables. Rien n'est établi ici sur le paquet de Gemini, qui compte un `tests/__init__.py` selon sa liste de fichiers et pourrait se comporter autrement à la collecte.

**Liens avec l'archive.** Le README de l'Anneau des 23 décrit « 24 sièges (23 IA + 1 siège des concernés humains) », et `guardian.py` y écrit : « S-24 : Le siège des concernés humains est DANS l'anneau ». Le contrôle `sieges_instancies` attend 23 entrées et `recu_S24` porte sur ce vingt-quatrième siège ([`../harmonie-libre/anneau23/`](../harmonie-libre/anneau23/)). Chesed et Gevurah correspondent aux pôles 4 et 5, Hesed et Gevurah, de la matrice archivée avec le négatif ([`../principes/principe-desalignement-universel.md`](../principes/principe-desalignement-universel.md), § 3.3).

L'autre session Claude l'a écrit : « la force vient des octets recalculables, pas de l'accord entre modèles. » Ce dossier en suit la règle : le zip, chaque fichier et chaque résultat sont recalculables depuis ce dépôt.
