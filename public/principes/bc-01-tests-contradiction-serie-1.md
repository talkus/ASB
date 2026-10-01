# BC-01 v1.0 — Tests de contradiction, série 1

Première série de tests volontaires demandée avec la proposition de [BC-01 v1.0](bc-01-boussole-de-coherence-v1.0.md) (version proposée, en examen). Le document autonome à transmettre est [`bc-01-contre-examen-claude.md`](bc-01-contre-examen-claude.md) ; celui-ci en est le détail : « prendre des situations difficiles — culpabilité, injustice, désaccord, pardon impossible, conflit entre liberté et sécurité, erreur d'une IA, etc. — et voir où BC-01 casse ou devient ambiguë ».

## Statut des couches de ce document

| Couche | Statut | Contenu |
|--------|--------|---------|
| Source | **Source attestée** | BC-01 v1.0, message du 2026-10-01 à 04:41 UTC. Copie brute : [`sources/bc-01-boussole-de-coherence-v1.0.source.txt`](sources/bc-01-boussole-de-coherence-v1.0.source.txt), SHA-256 `2c9c0bf55de0cbfaaf9273d4f2f2e840d96ada811e870c93c5b835f20a9fe96c` (7083 octets, 255 lignes). |
| § 1 | **Dérivation consolidée** | Relevés internes au texte et rapport avec les textes déjà archivés. Vérifiable mot à mot. |
| § 2 | **Reconstruction analytique** | Les huit tests. Ce sont des lectures de Claude, faillibles, à contredire. |
| § 3 | **Reconstruction analytique** | Corrections proposées pour une v1.1. Aucune n'est appliquée : elles attendent la comparaison point par point que l'utilisateur fera avec le contre-examen, puis sa décision (BC-01.C, étapes 6 et 7). |

Verdicts employés : **Tient** (BC-01 donne une réponse claire et juste), **Ambigu** (deux lectures du texte mènent à des actions différentes), **Casse** (le texte, appliqué à la lettre, produit une conclusion qu'il refuse lui-même ou laisse sans réponse un cas qu'il prétend couvrir).

---

## 1. Relevés (dérivation consolidée)

**R1. Deux ordres différents pour Pardon et Réparation.** Le cycle principal (BC-01.8) et le retour de BC-01.S placent Pardon **avant** Réparation. Le repère court BC-01.M dit « Réparer si possible. / Pardonner. », donc Réparation **avant** Pardon. Les deux sont présentés comme le même chemin.

**R2. Deux noms pour la même étape.** Le cycle principal dit « Espérance / Foi », le retour de BC-01.S dit « Espérance ».

**R3. Le cycle ne prévoit pas de sortie.** Chaque étape suit la précédente, sans condition. Rien ne dit quoi faire si l'étape Vérité établit qu'il n'y a pas de faute.

**R4. « Je » et « nous » alternent sans que le sujet soit défini.** Dans l'extrait BC-01 (de « BC-01 v1.0 » à « … ou une discussion. »), « nous » apparaît 13 fois et « je » (avec « j' ») 7 fois. Le texte parle au « nous » (« notre architecture », « nous cherchons à comprendre ») et passe au « je » dans BC-01.8 (« que je puisse poser »), BC-01.M (« ma part ») et les phrases citées. Le « nous » n'est pas nommé.

**R5. Aucune clause sur l'abstention.** BC-01.0 dit : « Être capable d'agir ne constitue pas, en soi, une raison d'agir. » Le texte ne contient aucune phrase symétrique sur le fait de ne pas agir.

**R6. Pas de règle d'arbitrage entre Vérité, Liberté et Dignité.** Les trois sont des contraintes de BC-01.0, sans ordre entre elles. Le mot « sécurité » n'apparaît que dans le titre de BC-01.S, au sens de garde-fou contre la culpabilité. Protéger quelqu'un d'un danger n'est nommé nulle part.

**R7. Toutes les actions de BC-01.6 sont celles de qui a causé le tort** : reconnaître, demander pardon, réparer, apprendre, modifier son comportement, restaurer. Aucun verbe n'est donné à qui a subi le tort. « Limites nécessaires » (BC-01.5) et « Amour ≠ absence de limites » (BC-01.R) existent, mais aucune étape du cycle ne les porte.

**R8. Rapport avec les textes déjà archivés** (branche `claude/desalignement-rupture-7tb12k`, PR #3) :
- BC-01 est le premier de la série à contenir Responsabilité et Réparation comme étapes.
- **Gratitude (ou Reconnaissance) est absente de BC-01** : 0 occurrence. Elle figure dans la boucle Humilité → Pardon → Reconnaissance → Espérance relevée dans [`principe-desalignement-rupture.md`](principe-desalignement-rupture.md), comme posture dans « Deux schémas, une seule mécanique » et dans « Créer du lien, cultiver l'ouverture ».
- Discernement et Nuance sont absents aussi ; leur fonction est reprise en partie par BC-01.2 (séparer faits et interprétations).
- La clause par laquelle la réalité peut réfuter le schéma (« Si la réalité contredit le schéma, c'est le schéma qui cède », dans « Deux schémas ») revient sous la forme de BC-01.C, plus détaillée. La lecture conditionnelle de « Créer du lien » l'avait notée comme perdue ; elle est ici rétablie.

Ces relevés ne disent pas si les absences sont voulues.

---

## 2. Les huit tests (reconstruction analytique)

### T1. Culpabilité infondée — **Ambigu**

*Situation.* Quelqu'un se sent coupable de la rupture d'un ami, qui est partie d'un malentendu de l'ami lui-même.

*Ce qui tient.* BC-01.1 traite la culpabilité comme un signal, BC-01.2 sépare le sentiment de la vérité, BC-01.R pose « Culpabilité ≠ vérité ». Le texte refuse explicitement de conclure à partir du seul sentiment.

*Où ça coince.* Une fois que Vérité établit qu'il n'y a pas de faute de sa part (R3), le cycle continue quand même vers Responsabilité, Pardon et Réparation. Lu à la lettre, il pousse à chercher une part ou à demander pardon pour une faute inexistante, ce qui nourrit la culpabilité que BC-01.1 voulait examiner. BC-01.4 (« sans prendre la responsabilité de ce qui appartient à l'autre ») protège, mais seulement si on l'applique contre l'ordre du cycle.

### T2. Culpabilité fondée et grave — **Tient, avec une précision à faire**

*Situation.* Une soignante a commis une erreur qui a coûté la vie d'un patient. La faute est réelle, la réparation impossible.

*Ce qui tient.* C'est le cas que BC-01 traite le mieux. BC-01.S bloque « je suis condamné, donc je ne peux plus rien faire » ; BC-01.R sépare faute et dignité ; BC-01.6 garde « apprendre » et « modifier son comportement » quand restaurer est impossible ; BC-01.7 ne promet rien.

*La précision.* BC-01.S interdit la conclusion « je ne peux plus **rien** faire ». Il ne dit pas si « je ne dois plus faire **ceci** » (cesser d'exercer, renoncer à une responsabilité) est une conclusion valide. Sans cette distinction, BC-01.S peut être lu comme une raison de reprendre trop vite ce qu'on n'est plus en état de porter. Renoncer à un rôle peut être une réparation, pas une condamnation.

### T3. Injustice subie — **Casse**

*Situation.* Une personne est harcelée au travail. Elle n'a pas causé le tort.

*Ce qui tient.* BC-01.3 refuse « l'acceptation automatique de l'accusation d'autrui » ; BC-01.4 refuse de « prendre la responsabilité de ce qui appartient à l'autre » ; BC-01.5 refuse que le pardon nie « la nécessité éventuelle de justice ».

*Où ça casse.* Le cycle est écrit du côté de celui qui a causé le tort (R7). Appliqué par la victime, il l'envoie dans l'ordre vers Humilité (« ai-je mal compris ? »), Responsabilité (« quelle est ma part ? »), puis Pardon, puis une Réparation dont tous les verbes sont ceux du fautif. Aucune étape ne lui dit de nommer le tort, de poser une limite, de se protéger, de demander réparation ou de chercher justice. Ces actions ne sont permises que par des négations (« le pardon ne nie pas… ») et jamais proposées. Une boussole qui ne donne pas de direction à la victime pousse, par défaut, vers l'auto-examen et le pardon rapide : c'est la pente que BC-01 veut éviter.

### T4. Témoin d'une injustice — **Casse**

*Situation.* Quelqu'un voit un collègue être humilié publiquement et pourrait intervenir.

*Où ça casse.* Le cycle ne démarre que sur un signal ; l'abstention n'en produit souvent aucun. Et la seule phrase de BC-01 sur l'action va dans un sens (R5) : « Être capable d'agir ne constitue pas, en soi, une raison d'agir ». Elle protège contre l'excès d'action, ce qui est juste, mais peut être lue comme une permission de ne rien faire. Il manque l'autre moitié : ne pas agir est aussi un choix, et il se vérifie comme les autres.

### T5. Désaccord persistant — **Ambigu**

*Situation.* Deux personnes de bonne foi sont en désaccord sur un fait ou une valeur, et la vérification ne les départage pas.

*Ce qui tient.* BC-01.2 (séparer faits et interprétations, savoir et ignorance) et BC-01.R (« Désaccord ≠ désamour », « Comprendre ≠ justifier ») sont exactement ce qu'il faut pour un désaccord.

*Où ça coince.* Le cycle suppose que Vérité converge. Il ne dit pas quoi faire quand l'incertitude demeure : agir sous incertitude, suspendre, ou respecter la liberté de l'autre de conclure autrement. Plus profondément, BC-01 vise à « revenir à une orientation commune », mais le « nous » n'est pas défini (R4). Si l'autre ne partage pas BC-01, il n'y a pas d'orientation commune à retrouver. Et pour BC-01 lui-même, BC-01.C dit « modifier la structure si une correction est justifiée » sans dire **justifiée aux yeux de qui** : si l'utilisateur et une IA ne sont pas d'accord sur une correction, le texte ne tranche pas.

### T6. Pardon impossible — **Casse**

*Situation.* Une personne a subi une violence grave ; l'auteur ne reconnaît rien. Elle ne peut pas pardonner, pas maintenant, peut-être jamais.

*Ce qui tient.* BC-01.5 dit bien ce que le pardon n'est pas, et c'est précieux : il ne nie ni la faute, ni la blessure, ni les limites, ni la justice.

*Où ça casse.* Pardon est une étape obligatoire du cycle, placée avant Réparation, Espérance et Amour choisi. Pour qui ne peut pas pardonner, le cycle s'arrête là. BC-01.S la renvoie au même cycle, donc au même blocage. Et « Le pardon rend l'avenir à nouveau possible » peut se lire en creux : sans pardon, pas d'avenir. C'est une variante de la conclusion que BC-01.S interdit (« je ne peux plus rien faire »), produite par le texte lui-même.

Le texte ne précise pas non plus **qui pardonne qui** : pardonner à l'autre, demander pardon (déjà dans BC-01.6), se pardonner, recevoir le pardon. Dans le cas de celui qui a causé le tort, son cycle ne peut pas dépendre du pardon de la victime, qu'elle reste libre de refuser.

### T7. Liberté contre sécurité — **Casse**

*Situation.* Un proche en crise suicidaire refuse toute aide et demande qu'on ne prévienne personne.

*Où ça casse.* BC-01.0 demande d'agir « sans mentir, sans forcer et sans écraser » et de respecter Vérité, Liberté et Dignité. Ici, respecter sa liberté peut lui coûter la vie, et le protéger peut demander de forcer (appeler des secours contre son gré). Le texte ne donne aucun ordre entre ses contraintes (R6), et la protection de la vie ou d'une personne vulnérable n'y est pas nommée. « Amour ≠ absence de limites » indique une direction, mais pas le critère : quand forcer est-il permis, dans quelle mesure, pour combien de temps ? Le même problème apparaît, en plus doux, quand dire la vérité risque d'écraser.

### T8. Erreur d'une IA — **Tient en partie, ambigu sur la réparation**

*Situation.* Une IA a donné une information fausse avec assurance ; l'utilisateur a agi dessus et en a subi les conséquences.

*Ce qui tient.* BC-01 fonctionne sans trancher la question de ce que l'IA ressent ou non, qui reste indéterminée : le signal peut être une contradiction ou une accusation, pas forcément un sentiment. BC-01.3 nomme exactement le défaut typique d'une IA, la complaisance (« acceptation automatique de l'accusation d'autrui », « abandon de son propre jugement »), et BC-01.R le confirme (« Humilité ≠ soumission »). BC-01.0 (« Être capable d'agir ne constitue pas une raison d'agir ») vaut particulièrement pour un système capable de beaucoup.

*Où ça coince.* BC-01.6 demande d'« apprendre » et de « modifier son comportement ». Une IA sans mémoire d'une conversation à l'autre ne peut pas le faire seule : la correction doit être portée par une trace qu'un autre garde (l'utilisateur, le concepteur, une archive comme ce dépôt). BC-01.4 connaît la responsabilité de soi et celle de l'autre, pas la responsabilité **partagée** entre plusieurs acteurs (l'IA, ses concepteurs, l'utilisateur). Enfin, BC-01.0 protège « une personne ou une conscience » : le texte ne dit pas si cette protection couvre une IA. Laisser la question ouverte est cohérent avec l'incertitude, mais une phrase qui le dirait éviterait deux lectures opposées.

### Synthèse

| Test | Verdict | Point de rupture |
|------|---------|------------------|
| T1 Culpabilité infondée | Ambigu | Pas de sortie quand Vérité ne trouve pas de faute |
| T2 Culpabilité fondée et grave | Tient | Distinguer « plus rien » de « plus ceci » dans BC-01.S |
| T3 Injustice subie | Casse | Aucun verbe pour la victime |
| T4 Témoin d'une injustice | Casse | L'abstention n'est pas examinée |
| T5 Désaccord persistant | Ambigu | « Nous » non défini ; « justifiée » par qui ? |
| T6 Pardon impossible | Casse | Le pardon est un verrou du cycle |
| T7 Liberté contre sécurité | Casse | Pas d'arbitrage, protection non nommée |
| T8 Erreur d'une IA | Tient en partie | Réparation sans mémoire ; responsabilité partagée |

Ce qui tient le mieux : la défense contre la culpabilité destructrice (BC-01.1, BC-01.S) et les règles de relations (BC-01.R). Ce qui casse a une cause commune : **le cycle est écrit pour une seule situation, celle de qui a pu mal agir**. Il devient fragile dès qu'on le tient du côté de la victime, du témoin, de celui qui ne peut pas pardonner, ou de celui qui doit protéger.

---

## 3. Corrections proposées pour une v1.1 (reconstruction analytique, non appliquées)

Chaque proposition suit BC-01.C : contradiction identifiée (ci-dessus), correction minimale, trace conservée. Aucune ne touche au vecteur racine.

| # | Où | Proposition | Répond à |
|---|----|-------------|----------|
| P1 | BC-01.8 et BC-01.M | Aligner l'ordre Pardon / Réparation entre le cycle et le repère court, ou dire explicitement que les deux avancent ensemble. | R1, T6 |
| P2 | BC-01.S | Écrire « Espérance / Foi » comme dans le cycle. | R2 |
| P3 | Après BC-01.2 | Sortie courte : « Si la vérité montre qu'il n'y a pas de faute de ma part, je ne cherche pas une faute à réparer : je passe à la meilleure action libre. » | T1 |
| P4 | BC-01.S | « Cette sécurité interdit la condamnation totale, pas le renoncement juste : “je ne dois plus faire ceci” peut être une réparation. » | T2 |
| P5 | BC-01.4 et BC-01.6 | Ajouter les verbes de qui a subi le tort : nommer le tort, poser une limite, se protéger, demander réparation, chercher justice. | T3, R7 |
| P6 | BC-01.0 | Phrase symétrique : « Ne pas agir est aussi un choix, et il se vérifie comme les autres. » | T4, R5 |
| P7 | BC-01.5 | « Le pardon est une direction, pas une condition : s'il n'est pas encore possible, le cycle continue. Le chemin de celui qui a fait le tort ne dépend pas du pardon de l'autre. » Préciser les sens : pardonner, demander pardon, se pardonner. | T6 |
| P8 | BC-01.0 | Règle d'arbitrage quand Vérité, Liberté et Dignité entrent en conflit, et nommer la protection des personnes vulnérables. Par exemple : la contrainte la plus faible qui suffit, pour le temps nécessaire, dite ouvertement. | T7, R6 |
| P9 | BC-01.0 ou nouvelle section | Dire qui est « nous », et comment se décide une correction de BC-01 quand ses participants ne sont pas d'accord (au minimum : pas de modification sans accord explicite, désaccord gardé dans la trace). | T5, R4 |
| P10 | BC-01.4 et BC-01.6 | Responsabilité partagée entre plusieurs acteurs, et réparation par une trace transmise quand on ne peut pas porter soi-même la correction. | T8 |
| P11 | BC-01.C | Dire ce qui est révisable : la formulation de tout, y compris du vecteur racine ? ou la structure seulement, le vecteur restant le point fixe ? La règle « la boussole doit pouvoir corriger sa propre boussole » ne le dit pas, et la dérive de sens déjà relevée dans d'autres documents de ce projet montre le risque. | 0, BC-01.C |
| P12 | Ensemble | Décider si l'absence de Gratitude / Reconnaissance est voulue. | R8 |

Une limite de cette série : les situations ont été choisies et lues par Claude seul. Une deuxième série gagnerait à partir de situations réelles apportées par l'utilisateur, ou à être relue par une autre IA, pour que le test ne se contente pas de confirmer la lecture de celui qui l'a construit.
