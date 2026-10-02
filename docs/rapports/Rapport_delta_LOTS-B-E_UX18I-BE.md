# Rapport de delta et de non-régression — Lots B et E

**Module :** Manager ses collaborateurs en tant qu'élu — IFAP × Congrès de la Nouvelle-Calédonie
**Candidate :** UX18I-BE (lots B, personnages, et E, interactions), construite sur UX18I-C (lots A, D et C)
**Date :** 1er octobre 2026
**Référentiel :** Cahier des charges d'évolution v1.0 — §6 (bible personnages), annexe A

## 1. Traçabilité

| Élément | Empreinte SHA-256 |
|---|---|
| Base gelée UX18I — archive | 638a7386ecda11815770c80a4addb7fd1be273a65570dbc42d46485a99ab329f |
| Candidate précédente UX18I-C — index.html | 6c04ccfb0989d708ec2f80743b5c2f2ad1aaa7f6651a3d0eda4a92ae55b6dbb1 |
| Candidate UX18I-BE — index.html | bfc7fa8772b4833ae61b02e9806c6f2f66ce4805ff05f913f15aa28e1a3ff29e |
| Candidate UX18I-BE — archive | fbd01d83452a8785f860740906f69755fbfcbb54fb52056744499ce354c689ca |

**Fichier modifié :** index.html uniquement. Les images et PDF de l'archive sont identiques. Une image de l'archive, jusque-là inutilisée, est désormais appelée : `reunion-collaborative-dossier.jpg`.

**Code ajouté :** une feuille `ux18i-lot-be`, un script `ux18i-lot-be-js` et trois retouches de la bibliothèque `mgt` :
- point d'accroche `onChoix` dans `cartesProfils` ;
- bloc d'écarts dans la branche `visualSummary` de `triCartes`, actif seulement si une grille est fournie ;
- boussole réversible.

Le noyau GABARIT n'est pas modifié.

## 2. Arbitrages appliqués par défaut

Ces trois points avaient été soumis à arbitrage. Je les ai appliqués selon mes propositions ; chacun est réversible en une modification.

| Point | Choix appliqué | Pour revenir en arrière |
|---|---|---|
| **MGT-37 — persistance du profil choisi** | Le choix est enregistré dans le magasin de réponses existant (`MGT_REPONSES`, clé `s2-profil`). Ce magasin est déjà sauvegardé par `ecrirePersistanceMgt`. Aucun nouveau mécanisme, aucune donnée transmise à la plateforme. | Retirer la clé : la personnalisation ne vaut alors que pour la session. |
| **MGT-19 — grille attendue du tri S1** | La grille est déduite **mot pour mot des feedbacks existants** de chaque carte : priorité politique → élu ; première analyse → collaborateur ; message final → élu ; signaler une difficulté → ensemble ; rythme de suivi → ensemble. | Supprimer la ligne `solution` : retour à la synthèse seule. |
| **MGT-38 — variantes Léon / Thomas** | Pas de nouvelle rédaction. Le texte commun est conservé ; seuls changent le prénom, le portrait et 7 accords grammaticaux (« seule » → « seul », « ce qu'elle porte » → « ce qu'il porte », « isolée » → « isolé »…). | — |

## 3. Deltas — Lot B (personnages)

| ID | Écran | Avant | Après |
|---|---|---|---|
| MGT-32, 34 | mod-s2-01 | Profil A / B / C | **Léon / Maëva / Thomas**. Descriptions d'origine conservées, complétées par l'identité canonique de la bible (Léon : connaît l'environnement institutionnel ; Maëva : rigoureuse, découvrira le Congrès ; Thomas : maîtrise ses dossiers, réseau de travail). |
| MGT-30 | mod-s2-01 | Portrait de Léon « sous pression » sur la carte de recrutement | Portrait « Léon prépare une commission » (même visage, expression plus ouverte) |
| MGT-31 | mod-s2-00 à 02, 04a | Maëva affichée et nommée avant le choix | Pastille masquée. Visuel d'ouverture remplacé par la scène des trois personnages (actif existant). Texte neutre : « le nouveau collaborateur ». |
| MGT-37, 38 | mod-s2-03 → s2-06, résultats des défis 3 et 4, tableau de bord | Maëva codée en dur | Le personnage choisi est propagé : titre, situation, portrait, six repères, feedbacks du tri, pastille, textes du défi 4. Le choix est conservé au rechargement. Sans choix, aucun personnage n'est imposé. |
| MGT-39 | mod-s2-03, s2-03b | — | Mini-carte du personnage choisi |
| MGT-07 | mod-s1-01b | Pastille seule | Mini-carte canonique de Thomas au moment de la décision |
| MGT-51 | mod-s3-02 | — | Mini-carte de Maëva au démarrage du simulateur 1 |
| MGT-07 (extension) | mod-s4-02, mod-s5-02 | — | Mini-cartes de Thomas et de Léon au démarrage des simulateurs 2 et 3 |
| MGT-08 | S1, S3, S4, S5 | Pastille personnage sur 100 % des écrans | Masquée sur « Je comprends » (apports), sur « Je prends du recul » (la situation y est rappelée) et là où une mini-carte la remplace |
| MGT-16 | mod-s1-02 | « Une situation avec Léon » | Thomas, avec son portrait canonique |
| MGT-34 | mod-s3-00 | « oblige Thomas à deviner » | « oblige Maëva à deviner » |

**Mini-cartes.** Le contenu reprend la bible du CDC §6 : parcours, caractéristiques, « Ce dont il / elle a besoin ».

## 4. Deltas — Lot E (interactions)

| ID | Écran | Avant | Après |
|---|---|---|---|
| MGT-17 | mod-s1-02 | « Voir le repère » (dévoilement passif) | 3 options → feedback immédiat → repère. Options et feedbacks construits à partir du repère et des « limites » déjà présents dans l'écran. Choix modifiable, erreur non punitive. |
| MGT-19 | mod-s1-03 | Synthèse sans repérage d'erreur | Pour chaque carte mal placée : « votre choix → repère proposé » avec l'explication existante, puis possibilité de repositionner et de revalider. La synthèse visuelle « La carte de vos responsabilités » est conservée. La consigne annonce ce fonctionnement. |
| MGT-35 | mod-s2-02 | Réponses verrouillées dès le premier clic | Choix modifiable sans réinitialisation ; état annoncé au lecteur d'écran |
| MGT-36 | mod-s2-02 | « Construisez votre boussole en répondant aux quatre questions. » | « …pour chacune des quatre questions, **choisissez une seule réponse, la principale**. Vous pouvez changer votre choix à tout moment. » |

## 5. Contrôles

| Contrôle | Résultat |
|---|---|
| Erreurs JavaScript (3 viewports, 67 écrans) | 0 |
| Parcours complet au bouton « Suivant », retour arrière | 67/67, conforme |
| Débordement horizontal, texte tronqué | Aucun |
| « Profil A/B/C » dans le code | 0 |
| S2 avec Léon : occurrences résiduelles de « Maëva » dans s2-03 et son feedback | 0 ; accords corrects (« Il arrive », « décider seul », « reste isolé ») |
| S2 avec Thomas : formes féminines résiduelles liées au personnage | 0 (les « il/elle » génériques de s2-04 sont d'origine) |
| S3 après un choix de Léon en S2 | Maëva inchangée (S3 reste canonique) |
| Choix conservé après rechargement | Oui |
| MGT-17 : mauvaise puis bonne réponse | Feedback « À ajuster… » puis « C'est le bon réflexe », repère affiché |
| MGT-19 : tout placé côté élu | 3 écarts listés avec le repère et l'explication |
| MGT-35 : changement de choix | Ancien choix désélectionné, nouveau sélectionné, aucun bouton désactivé |

Les captures sur ordinateur et iPad portrait sont dans *Preuves_captures_LOTS-B-E.zip* : s2-00, profils, s2-03 avec Léon, s3-02, s1-02, s1-03, s2-02.

## 6. Points ouverts

1. **Léon en S2.** Son trait canonique « la pression commence à peser sur sa charge » apparaît dans la mini-carte alors qu'il vient d'arriver. C'est conforme à la bible mais un peu décalé dans ce contexte. À confirmer avec Marie-Noëlle.
2. **Portraits S2 (MGT-30).** Un seul remplacement a été fait (Léon, carte de recrutement). Les autres visuels jugés tristes restent à désigner nommément.
3. **Défi 4 — banque de variantes.** Les textes sont personnalisés à l'affichage. La logique du défi n'est pas modifiée.
4. **MGT-29 (« Mme Christesse »)** : toujours ouvert, non localisé.
5. **Corpus.** MGT-40, 41 et 55 restent bloqués tant que le corpus de Marie-Noëlle ou la matrice n'ont pas été transmis.
