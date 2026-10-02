# Rapport de delta et de non-régression — Lot C

**Module :** Manager ses collaborateurs en tant qu'élu — IFAP × Congrès de la Nouvelle-Calédonie
**Candidate :** UX18I-C (lot C, grammaire pédagogique commune), construite sur UX18I-D (lots A et D)
**Date :** 1er octobre 2026
**Référentiel :** Cahier des charges d'évolution v1.0 — §4, §5, §8.2, §8.4 et annexe A

## 1. Traçabilité

| Élément | Empreinte SHA-256 |
|---|---|
| Base gelée UX18I — archive | 638a7386ecda11815770c80a4addb7fd1be273a65570dbc42d46485a99ab329f |
| Candidate précédente UX18I-D — index.html | b3c3cf94addba9edd7cd0e67ebde472be216f8f69b6982f8cff5278c3b5abe04 |
| Candidate UX18I-C — index.html | 6c04ccfb0989d708ec2f80743b5c2f2ad1aaa7f6651a3d0eda4a92ae55b6dbb1 |
| Candidate UX18I-C — archive | f41b685ecc1340959a1c5a84535a6088011a595d4ade880101dc3cc9ef490583 |

**Fichier modifié :** index.html uniquement. Images et PDF identiques à la base.

**Code ajouté :** une feuille `<style id="ux18i-lot-c">` et un script `<script id="ux18i-lot-c-js">`. Ils sont autonomes, n'écrivent aucune donnée et ne touchent pas au routeur, au sommaire, à la reprise ni à la couche SCORM.

## 2. Exigences traitées

| ID | Traitement |
|---|---|
| MGT-57, 13, 14 | Composant unique des 6 repères, identique dans les 5 séquences (59 écrans). Étape en cours sur fond bleu nuit, étapes passées cochées, étapes à venir neutres. Aucun score, pourcentage ni « X/6 ». Deux lignes de 3 sur iPad portrait. Accessible au lecteur d'écran (« repère en cours », « repère déjà parcouru »). Le menu global UX18I est inchangé. |
| MGT-14, 52 | 60 surtitres harmonisés en « Séquence N · intitulé de la séquence ». Les étiquettes concurrentes (« Pause de consolidation », « Comparaison réflexive », « Apport structuré », « Fiche de référence »…) disparaissent des surtitres. Les encadrés « Pause de consolidation » qui font partie des apports restent. |
| MGT-25, 45, 49, 50 + H-04 | Les 5 instantanés « Avant de commencer » (3 questions + annonce qu'elles seraient reposées) sont supprimés. La première réaction devient le seul « Je me positionne ». |
| MGT-22, 23, 24, 28, 45 + H-05 | Les 5 clôtures suivent le modèle commun : **La situation** (texte repris mot pour mot de l'écran de situation) → **Votre première réaction** → **« Avec le recul, que feriez-vous aujourd'hui ? »** → **Les repères à emporter** → **fiche PDF facultative**. La relecture des instantanés et les 5 petits bilans sont supprimés. |
| MGT-26 | Repères à emporter conservés ; « Les essentiels à retenir » de S1 conservés. |
| MGT-20, 21 | L'écran mod-s1-04b (« Petit bilan prémonitoire », score —/10, curseur « prochain réglage ») est retiré du flux. Il est hors parcours, hors sommaire et hors progression, mais son code reste dans le fichier, masqué, pour réversibilité. |
| MGT-09, 52 + H-02, H-03 | Écrans remis dans l'ordre situation → position → compréhension → essai → ajustement → recul (§3). |
| H-08 | Les clés de stockage des instantanés et bilans ne sont plus écrites. Aucune fonction ne les relisait (vérifié). Aucun nouveau stockage n'est créé. |

## 3. Nouvel ordre des écrans

| Séquence | Situation | Je me positionne | Je comprends | J'essaie | J'ajuste | Je prends du recul |
|---|---|---|---|---|---|---|
| S1 | 00, 01 | 01b, 01c | 01d, 01e, 02, **04** | **03**, 04a | 05 + défis 1-2 | 06 |
| S2 | 00, 01 | 01b, 02 | **04a** | **03**, 03b, 04 | 05 + défis 3-4 | 06 |
| S3 | 00 | 01 | **04, 04b, 04c** | **02** | 03, 06 + défi 5 | **05** |
| S4 | 00 | 01 | **04, 05b, 05c** | **02**, 05 | 03, 07 + défis 6-7 | **06** |
| S5 | 00 | 01 | **05b, 05c** | **04, 05, 02** | 03, 07 + défi 8 | **06** |

En gras : écrans déplacés.

**Recâblage des boutons de sortie d'apport.** Ils pointent maintenant vers l'écran suivant du nouvel ordre (s2-04a → s2-03, s3-04c → s3-02, s4-05c → s4-02, s5-05c → s5-04). Le bouton de s1-02 pointe vers s1-04 ; son libellé « J'applique ces repères → » devient « Je continue → » (convention R105).

**Suites de défis.** En S3, S4 et S5, la relecture clôt désormais la séquence. La suite après résultat change donc : défi 5 → s3-05, défi 7 → s4-06, défi 8 → s5-06. La relecture de S5 mène ensuite au tableau de bord.

## 4. Contrôles de non-régression

| Contrôle | Résultat |
|---|---|
| Erreurs JavaScript (3 viewports, 67 écrans) | 0 |
| Parcours complet au bouton « Suivant » | 67 écrans sur 67, dans le nouvel ordre, sans blocage |
| Retour arrière | Conforme |
| Boutons data-go et liens des défis (repère, quiz, suite) | Toutes les cibles existent |
| Débordement horizontal | Aucun |
| Texte tronqué | Aucun, hors libellés réservés au lecteur d'écran (volontairement masqués) |
| Texte rendu : « instantané », « seront reposées », « Petit bilan », « prochain réglage », « Votre point de départ » | 0 occurrence |
| « /10 » restant | 1 : curseur initial de s1-01c, conservé à la demande du CDC (« garder le curseur initial ») |
| Reprise de session | Comportement identique avant et après en prévisualisation locale. **À tester dans Moodle** : la reprise dépend de l'API SCORM, absente en local. |
| Complétion | L'écran retiré mod-s1-04b n'est plus requis pour la complétion. Aucun autre changement du mécanisme. |

**Correctif du lot D.** La mise en cartes des « repères à emporter » (MGT-15) s'appliquait aussi à la liste imbriquée des « Essentiels à retenir » de S1. Le sélecteur a été restreint aux listes de premier niveau.

## 5. Contenu retiré — traçabilité corpus (§9)

- 16 blocs sont retirés, soit **1 285 mots**. Tous ont le statut **« Modifié / arbitré »** : leur retrait est demandé explicitement par MGT-20, 21, 25, 28, 45 et 49.
- Aucun apport expert n'est touché : seuls des dispositifs de questionnement sont supprimés.
- 12 identifiants MNL ne figurent plus dans le module actif (MNL-0117/0122, 0183/0187, 0239/0244, 0359/0364, 0487/0491, 0673/0678). Les identifiants de mod-s1-04b (MNL-0866–0874) restent dans le code masqué.
- Le texte intégral de chaque bloc est archivé en annexe, pour la matrice de couverture (MGT-55).

## 6. Points à arbitrer

1. **Production utile en S5.** Le CDC demande pour S5 une « relecture simplifiée » : une question, les repères, la fiche. L'exercice « On vérifie dans la vraie vie » (première étape concrète et grille d'auto-évaluation, MNL-0735–0742) est pourtant du contenu corpus. Je l'ai conservé comme en S4, après la question de recul. Deux options : le garder, ou le retirer avec traçabilité.
2. **Chapeaux des clôtures S3, S4 et S5.** « Retrouvez ce que vous aviez écrit, puis évaluez-le avant de le reformuler » reste compatible avec le modèle mais pourrait être harmonisé. Il n'y a pas d'ID : je ne l'ai pas modifié.
3. **Pastille du personnage.** Elle est toujours présente sur tous les écrans ; elle relève du lot B (MGT-08).
4. **Espacements du §7.** Le composant et la clôture respectent 20–28 px entre blocs. Le reste des écrans n'est pas repris faute d'ID dédié.

## Annexe — Blocs retirés (texte intégral)

**mod-s1-01b — Instantané 3 questions** (exigence MGT-25 ; MNL : MNL-0117–MNL-0122)

> Avant de commencer : votre instantané Un temps court d'auto-positionnement — les mêmes 3 questions seront reposées en fin de module. 1. Sur quels sujets sentez-vous que votre rôle est déjà clair aujourd'hui ? 2. Où sentez-vous parfois une confusion — avec votre collaborateur, votre groupe politique, ou l'administration ? 3. Qu'aimeriez-vous clarifier en sortant de ce module ? Ces trois réponses sont conservées et réaffichées en fin de séquence pour comparer votre point de départ à votre réflexion d'aujourd'hui.

**mod-s2-01b — Instantané 3 questions** (exigence MGT-45 ; MNL : MNL-0239–MNL-0244)

> Avant de commencer : votre instantané Un temps court d'auto-positionnement — les mêmes 3 questions seront reposées en fin de module. 1. Qu'est-ce qui, dans votre équipe actuelle, fonctionne déjà bien en matière de complémentarité ? 2. Où sentez-vous un angle mort — une compétence ou un profil qui manque à votre équipe ? 3. Qu'aimeriez-vous clarifier en sortant de ce module ? Ces trois réponses sont conservées et réaffichées en fin de séquence pour comparer votre point de départ à votre réflexion d'aujourd'hui.

**mod-s3-01 — Instantané 3 questions** (exigence MGT-49/50 ; MNL : MNL-0487–MNL-0491)

> Avant de commencer : votre instantané Prêts pour un temps court d'auto-positionnement ? — les mêmes 3 questions seront reposées en fin de module, pour comparer votre pensée « avant » et votre pensée « après ». 1. Dans vos échanges avec votre équipe, de quoi êtes-vous le plus fier(e) aujourd'hui ? 2. Où sentez-vous que ça coince, parfois ? 3. Qu'aimeriez-vous pouvoir faire différemment ? Ces trois réponses sont conservées et réaffichées en fin de séquence pour comparer votre point de départ à votre réflexion d'aujourd'hui.

**mod-s4-01 — Instantané 3 questions** (exigence MGT-28 (H-04) ; MNL : MNL-0359–MNL-0364)

> Avant de commencer : votre instantané Un temps court d'auto-positionnement — les mêmes 3 questions seront reposées en fin de module. 1. Sur quels types de dossiers déléguez-vous déjà facilement, aujourd'hui ? 2. Où sentez-vous que vous reprenez la main plus souvent que nécessaire ? 3. Qu'aimeriez-vous ajuster en sortant de ce module ? Ces trois réponses sont conservées et réaffichées en fin de séquence pour comparer votre point de départ à votre réflexion d'aujourd'hui.

**mod-s5-01 — Instantané 3 questions** (exigence MGT-28 (H-04) ; MNL : MNL-0673–MNL-0678)

> Avant de commencer : votre instantané Un temps court d'auto-positionnement — les mêmes 3 questions seront reposées en fin de module. 1. Face à une tension naissante dans votre équipe, qu'est-ce qui vous réussit déjà aujourd'hui ? 2. Où sentez-vous que vous intervenez trop tard, ou pas assez tôt ? 3. Qu'aimeriez-vous ajuster en sortant de ce module ? Ces trois réponses sont conservées et réaffichées en fin de séquence pour comparer votre point de départ à votre réflexion d'aujourd'hui.

**mod-s1-06 — Relecture des 3 réponses de l’instantané** (exigence MGT-25 ; MNL : MNL-0117–MNL-0122)

> Votre point de départ Relisez ce que vous aviez écrit avant les apports de la séquence. 1. Sur quels sujets sentez-vous que votre rôle est déjà clair aujourd'hui ? (Vous n'aviez pas encore répondu à cette question.) 2. Où sentez-vous parfois une confusion — avec votre collaborateur, votre groupe politique, ou l'administration ? (Vous n'aviez pas encore répondu à cette question.) 3. Qu'aimeriez-vous clarifier en sortant de ce module ? (Vous n'aviez pas encore répondu à cette question.)

**mod-s1-06 — Petit bilan en 3 questions** (exigence MGT-25 ; MNL : MNL-0183–MNL-0187)

> Petit bilan en 3 questions Posez vos trois repères avant de quitter la séquence. 1. Qu'est-ce qui, avec ce module, vous semble déjà clair dans votre positionnement ? 2. Quelle situation — presse, commission, groupe politique, administration — identifiez-vous encore comme un point de vigilance ? 3. Dans un futur proche, quel est le premier geste concret que vous mettrez en place, et quel sera le bénéfice immédiat ?

**mod-s2-06 — Relecture des 3 réponses de l’instantané** (exigence MGT-28 ; MNL : MNL-0239–MNL-0244)

> Votre point de départ Relisez ce que vous aviez écrit avant les apports de la séquence. 1. Qu'est-ce qui, dans votre équipe actuelle, fonctionne déjà bien en matière de complémentarité ? (Vous n'aviez pas encore répondu à cette question.) 2. Où sentez-vous un angle mort — une compétence ou un profil qui manque à votre équipe ? (Vous n'aviez pas encore répondu à cette question.) 3. Qu'aimeriez-vous clarifier en sortant de ce module ? (Vous n'aviez pas encore répondu à cette question.)

**mod-s2-06 — Petit bilan en 3 questions** (exigence MGT-28 ; MNL : non balisé)

> Petit bilan en 3 questions Posez vos trois repères avant de quitter la séquence. 1. Qu'est-ce qui, avec ce module, vous semble déjà clair dans votre façon de recruter et d'intégrer ? 2. Quel angle mort de votre équipe actuelle allez-vous garder en tête pour un prochain recrutement ? 3. Quel est le premier geste concret que vous allez mettre en place, et pour quand ?

**mod-s3-05 — Relecture des 3 réponses de l’instantané** (exigence MGT-28 ; MNL : MNL-0487–MNL-0491)

> Votre point de départ Relisez ce que vous aviez écrit avant les apports de la séquence. 1. Dans vos échanges avec votre équipe, de quoi êtes-vous le plus fier(e) aujourd'hui ? (Vous n'aviez pas encore répondu à cette question.) 2. Où sentez-vous que ça coince, parfois ? (Vous n'aviez pas encore répondu à cette question.) 3. Qu'aimeriez-vous pouvoir faire différemment ? (Vous n'aviez pas encore répondu à cette question.)

**mod-s3-05 — Petit bilan en 3 questions** (exigence MGT-28 ; MNL : non balisé)

> Petit bilan en 3 questions Posez vos trois repères avant de quitter la séquence. 1. Dans vos échanges avec votre équipe, de quoi êtes-vous le plus fier(e) aujourd'hui ? Une réussite récente, une qualité relationnelle que vous mobilisez bien, un effet positif que vous avez observé. 2. Où sentez-vous que ça coince, parfois ? Un repère du parcours qui aurait changé une situation récente. 3. Qu'aimeriez-vous pouvoir faire différemment ? Un engagement formulable en une phrase.

**mod-s4-06 — Relecture des 3 réponses de l’instantané** (exigence MGT-28 ; MNL : MNL-0359–MNL-0364)

> Votre point de départ Relisez ce que vous aviez écrit avant les apports de la séquence. 1. Sur quels types de dossiers déléguez-vous déjà facilement, aujourd'hui ? (Vous n'aviez pas encore répondu à cette question.) 2. Où sentez-vous que vous reprenez la main plus souvent que nécessaire ? (Vous n'aviez pas encore répondu à cette question.) 3. Qu'aimeriez-vous ajuster en sortant de ce module ? (Vous n'aviez pas encore répondu à cette question.)

**mod-s4-06 — Petit bilan en 3 questions** (exigence MGT-28 ; MNL : non balisé)

> Petit bilan en 3 questions Posez vos trois repères avant de quitter la séquence. 1. Qu'est-ce qui, avec ce module, vous semble déjà clair dans votre façon de déléguer ? 2. Sur quel dossier ou quel collaborateur identifiez-vous encore un réflexe de reprise de contrôle ? 3. Quel est le premier geste concret que vous mettez en place, et pour quand ?

**mod-s5-06 — Relecture des 3 réponses de l’instantané** (exigence MGT-28 ; MNL : MNL-0673–MNL-0678)

> Votre point de départ Relisez ce que vous aviez écrit avant les apports de la séquence. 1. Face à une tension naissante dans votre équipe, qu'est-ce qui vous réussit déjà aujourd'hui ? (Vous n'aviez pas encore répondu à cette question.) 2. Où sentez-vous que vous intervenez trop tard, ou pas assez tôt ? (Vous n'aviez pas encore répondu à cette question.) 3. Qu'aimeriez-vous ajuster en sortant de ce module ? (Vous n'aviez pas encore répondu à cette question.)

**mod-s5-06 — Petit bilan en 3 questions** (exigence MGT-28 ; MNL : non balisé)

> Petit bilan en 3 questions Posez vos trois repères avant de quitter la séquence. 1. Qu'est-ce qui, avec ce module, vous semble déjà clair dans votre façon de repérer les tensions ? 2. Quel signal — raidissement, ton, retrait — reconnaissez-vous comme votre point de vigilance personnel ? 3. Quel est le premier geste concret qu’il vous semble prêt à mettre en application et quand ?

**mod-s1-04b — Écran « Petit bilan prémonitoire » (score /10, curseur « prochain réglage », 3 questions)** (exigence MGT-20/21 ; MNL : MNL-0866–MNL-0874)

> Thomas Séquence 1 · Comparaison réflexive Petit bilan prémonitoire : où en serez-vous demain ? Avec ce que vous savez maintenant, repositionnez-vous sur la même échelle. Il ne s'agit pas d'avoir « bougé » à tout prix, mais d'avoir une conscience plus claire de là où vous êtes. Votre point de départ : —/10 À vous de jouer Placez le repère là où vous souhaitez tester votre posture dans une prochaine situation réelle. Votre prochain réglage — /10 1 · Je tranche presque toujours moi-même, vite 10 · Je laisse presque toujours l’initiative aux autres ↔ Souris ou tactile : faites glisser le repère · clavier : utilisez les flèches ← →. 1. Ce qui est plus clair Qu'est-ce qui, avec ce module, vous semble plus clair sur votre propre curseur ? 2. Ce que je vais tester Dans quelle situation précise allez-vous tester un ajustement ? 3. Mon premier geste concret Quel est le premier geste concret que vo
