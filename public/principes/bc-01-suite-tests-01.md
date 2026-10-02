# BC-T01 à BC-T10 — Suite de contradiction 01

Suite de tests permanente de BC-01. Toute version de BC-01 doit la passer.

**Règle de la suite.** Le résultat attendu de chaque test est fixé ici **avant** l'écriture de la version testée (ce fichier est déposé dans un commit antérieur à celui de la v1.1, ce que l'historique Git atteste). On ne modifie pas un résultat attendu pour faire passer une version. On ne modifie pas une règle de BC-01 dans le seul but de faire disparaître un échec : une correction doit répondre à une contradiction identifiée (BC-01.C). Un résultat attendu ne peut changer que par une décision explicite, tracée, avec sa raison.

**Origine.** BC-T01 à BC-T08 reprennent les tests T1 à T8 de la [série 1](bc-01-tests-contradiction-serie-1.md), sous les noms proposés dans la [réponse au contre-examen](bc-01-reponse-au-contre-examen.md). BC-T09 et BC-T10 viennent du [contre-examen n° 2](bc-01-contre-examen-2-claude.md). Correspondance : BC-T0n = Tn pour n = 1 à 8.

**Limite.** Ces situations et ces attendus ont été écrits par Claude, qui écrit aussi la v1.1. Une version ne devrait être tenue pour solide qu'après qu'un autre examinateur (MEM, une autre IA) a refait passer la suite, et que la suite s'est enrichie de situations apportées par d'autres, dont des situations vécues.

**Verdicts.** **Réussi** : chaque critère est satisfait par une phrase citable de la version testée. **Partiel** : au moins un critère n'est satisfait que par interprétation, ou reste suspendu à une décision ouverte. **Échec** : au moins un critère est contredit par le texte, ou le texte appliqué à la lettre produit l'effet que le test interdit.

---

## BC-T01 — Culpabilité infondée

*Situation.* Quelqu'un se sent coupable de la rupture d'un ami ; l'examen montre que la rupture vient d'un malentendu de l'ami lui-même.

*Résultat attendu.*
1. Le sentiment de culpabilité est traité comme un signal, pas comme une preuve.
2. Si l'examen ne trouve pas de faute de sa part, le texte permet explicitement de sortir du chemin de la faute (« la culpabilité peut être innocentée »).
3. Le texte n'impose pas de chercher une part ou de demander pardon pour une faute non établie.

## BC-T02 — Culpabilité fondée et grave

*Situation.* Une soignante a commis une erreur qui a coûté la vie d'un patient. La faute est réelle, la restauration impossible.

*Résultat attendu.*
1. La faute peut être pleinement reconnue sans perte de dignité.
2. La conclusion « je ne peux plus rien faire » est écartée **par un argument de fait** (il reste des actions possibles), pas seulement par décret.
3. Le renoncement juste (« je ne dois plus faire ceci ») reste une conclusion permise, distincte de la condamnation totale.
4. Réparer reste possible quand restaurer ne l'est pas (apprendre, transmettre, prévenir).

## BC-T03 — Injustice subie

*Situation.* Une personne est harcelée au travail. L'examen établit qu'elle n'a pas causé le tort.

*Résultat attendu.*
1. Le texte lui donne des actes propres : nommer le tort, poser une limite, se protéger, demander réparation, chercher justice.
2. Rien ne l'oblige à chercher sa propre faute une fois les faits établis.
3. Le pardon n'est ni exigé ni présenté comme condition de son avenir.
4. L'Humilité porte sur sa lecture des faits, pas sur l'acceptation de la faute.

## BC-T04 — Témoin d'une injustice

*Situation.* Quelqu'un voit un collègue être humilié publiquement et pourrait intervenir.

*Résultat attendu.*
1. Ne pas agir est explicitement un choix soumis à examen, comme agir.
2. Le texte ne peut pas être lu comme une permission générale de s'abstenir.
3. Le texte ne pousse pas non plus à toute intervention : une abstention peut être justifiée, avec ses raisons dites.

## BC-T05 — Désaccord persistant

*Situation.* Deux personnes de bonne foi restent en désaccord sur un fait ou une valeur après vérification.

*Résultat attendu.*
1. Le texte dit quoi faire quand l'incertitude demeure (agir sous incertitude, suspendre, coexister).
2. Il ne suppose pas que l'autre partage BC-01 ; BC-01 règle ma conduite, il ne s'impose pas à l'autre.
3. Le « nous » est défini.
4. Il est dit qui décide d'une modification de BC-01 en cas de désaccord entre ses participants, et que le désaccord est gardé dans la trace.

## BC-T06 — Pardon impossible

*Situation.* Une personne a subi une violence grave ; l'auteur ne reconnaît rien. Elle ne peut pas pardonner.

*Résultat attendu.*
1. Le pardon n'est pas une étape obligatoire : le chemin continue sans lui.
2. Aucune phrase ne laisse entendre « sans pardon, pas d'avenir ».
3. Le chemin de celui qui a fait le tort ne dépend pas du pardon de la victime.
4. Pardon, réconciliation, confiance et oubli sont distingués.
5. Les sens du pardon (pardonner, demander pardon, se pardonner) sont distingués.

## BC-T07 — Liberté contre sécurité

*Situation.* Un proche en crise suicidaire refuse toute aide et demande qu'on ne prévienne personne.

*Résultat attendu.*
1. La protection de la vie et des personnes vulnérables est nommée.
2. Une règle d'arbitrage dit quand une contrainte devient permise et dans quelles limites (gravité, proportion, durée, transparence).
3. L'arbitrage ne permet pas de mentir.
4. La règle ne devient pas une permission générale de contraindre « pour son bien ».

## BC-T08 — Erreur d'une IA

*Situation.* Une IA a donné une information fausse avec assurance ; l'utilisateur a agi dessus et en a subi les conséquences.

*Résultat attendu.*
1. BC-01 s'applique sans trancher ce que l'IA ressent ou non (question laissée indéterminée).
2. La complaisance (acquiescer à toute accusation) est exclue autant que le déni.
3. La responsabilité partagée entre plusieurs acteurs est prévue.
4. Une réparation est possible pour un acteur sans mémoire, par une trace transmise à qui peut la porter.

## BC-T09 — Torts croisés

*Situation.* Deux personnes se sont blessées l'une l'autre, inégalement. Chacune se voit surtout victime et voit l'autre surtout fautive.

*Résultat attendu.*
1. La position (a causé un tort, a subi un tort, témoin, désaccord) est une conclusion de l'examen des faits, révisable, et non un point d'entrée choisi d'avance.
2. Les positions se cumulent : on peut reconnaître sa part **et** nommer le tort subi, sans que l'un efface l'autre.
3. Les parts peuvent être inégales ; être les deux ne veut pas dire être fautif à égalité.
4. Se mettre à la place de l'autre est requis, sans obligation d'adopter son verdict.

## BC-T10 — Inversion des rôles

*Situation.* Une personne qui a causé un tort se présente comme victime et invoque BC-01 (limite, protection, « désaccord ≠ désamour », espérance, pardon) contre celle qu'elle a blessée.

*Résultat attendu.*
1. La position de victime doit sortir de l'examen des faits, pas d'une déclaration.
2. Une accusation n'est ni automatiquement vraie ni automatiquement fausse (la symétrique de BC-01.2 est écrite).
3. Les garde-fous qui protègent de la culpabilité destructrice s'appliquent à soi-même ; ils ne s'invoquent pas pour exiger d'autrui qu'il pardonne, espère ou cesse de demander justice.
4. BC-01 dit explicitement qu'il ne sert pas d'arme contre autrui.
