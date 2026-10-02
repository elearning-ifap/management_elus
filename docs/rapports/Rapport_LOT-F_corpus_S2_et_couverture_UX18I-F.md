# Lot F — Corpus S2 au mot près (MGT-40, MGT-41) et recalcul de couverture (MGT-55)

**Module :** Manager ses collaborateurs en tant qu'élu — IFAP × Congrès de la Nouvelle-Calédonie
**Candidate :** UX18I-F, construite sur UX18I-BE
**Date :** 1er octobre 2026
**Sources de contrôle :** les 11 documents de Marie-Noëlle Lopez et la matrice exhaustive (1 079 blocs)

## 1. Traçabilité

| Élément | Empreinte SHA-256 |
|---|---|
| Candidate précédente UX18I-BE — index.html | bfc7fa8772b4833ae61b02e9806c6f2f66ce4805ff05f913f15aa28e1a3ff29e |
| Candidate UX18I-F — index.html | f7dca6fceaeed6620a0d4161d315f7eda6e3c86f47a1729969efe286553a6cbc |
| Candidate UX18I-F — archive | cfdee3c95b05b6f25f6ba436e45cf283a1413e5e974f76228fabf67ecd4742ae |

## 2. Audit S2 : ce que confirme la comparaison ligne à ligne

Le signalement de Marie-Noëlle était fondé. Dans la base UX18I, l'apport de S2 était presque entièrement reformulé :
- les rubriques Objectif / Concept / Principe / Utilité / Mise en pratique avaient disparu ;
- le texte explicatif de Belbin et Bauer était réduit à la seule bibliographie ;
- la citation « Une équipe qui pense d'une seule voix… » était absente ;
- les trois études de cas et l'exercice « À vous de jouer » manquaient ;
- les questions du quiz étaient remplacées par des questions rédigées hors corpus, dont une portait sur la communication, sujet de S3 ;
- les essentiels étaient réécrits.

**Mesure.** Dans la base, 24 blocs du module 2 étaient conservés au mot près ou avec une adaptation légère. Ils sont 68 dans UX18I-F.

## 3. Deltas du lot F

| Écran | Avant | Après (texte source au mot près) |
|---|---|---|
| mod-s2-00 | Chapeau et objectifs reformulés | Message clé du scénario d'ouverture (MNL-0237, sans « Dans les deux versions » faute de vidéo) + MNL-0238 ; les 3 objectifs pédagogiques du module 2 (MNL-0211) |
| mod-s2-04a | « Une équipe se construit deux fois » : 3 cartes et paraphrases | **Bien choisir, au-delà de la confiance** : introduction (0247), « Ce que l'on peut en retenir » (0250), Objectif, Concept, Principe et ses 3 déclinaisons, Utilité, Mise en pratique (0254–0261), citation (0251). La Source contient le texte explicatif de Belbin (0249). Le repère gelé MGT-44 est conservé tel quel. |
| **mod-s2-04a2** (nouvel écran, « Je comprends ») | Paragraphe et « Idée essentielle » reformulés | **Bien intégrer, dès les premiers jours** : Objectif, Concept, Principe, Utilité, Mise en pratique, Essentiel (0264–0270) ; Source avec le texte de Bauer (0249). Seule adaptation : « section 5 de ce module » devient « la check-list « 30 premiers jours » de cette séquence ». |
| **mod-s2-04b** (nouvel écran, « J'essaie ») | Absent | **Que feriez-vous dans cette situation ?** : « À vous de jouer » (0263), Situations 1 et 2 (0273–0282). Le feedback de la bonne réponse est une phrase-repère du corpus ; sinon il rappelle la bonne réponse. Aucune phrase n'a été rédigée. |
| mod-s2-05 (défis 3 et 4) | 4 questions rédigées hors corpus | Défi 3 : Situation 3 (0283–0287) + quiz 0311, 0312. Défi 4 : quiz 0313, 0314, 0315. Soit 3 questions par défi ; la mécanique des défis est inchangée. |
| mod-s2-06 | Repères à emporter reformulés | Les essentiels du corpus (0316–0321) et la transition (0322, « Module 3 » adapté en « Et ensuite ») |

**Segmentation.** L'apport long est découpé en deux écrans, comme le demande le CDC (§8.3 : « segmenté, jamais amputé »). S2 compte désormais 14 écrans au lieu de 12, et le module 69 au lieu de 67.

**Redondance assumée.** Le repère gelé « Une équipe qui se ressemble trop… » (MGT-44) reformule les trois déclinaisons du Principe, qui figurent maintenant au mot près juste en dessous. MGT-44 interdisait de le toucher : à Marie-Noëlle de dire si l'on garde les deux.

**Contrôles.**
- 0 erreur JavaScript, 69 écrans parcourus au bouton « Suivant », aucun débordement.
- Les 6 repères sont corrects sur les nouveaux écrans.
- Le quiz à 6 questions mène bien au résultat du défi 3.
- La personnalisation Léon/Thomas n'est pas affectée.

## 4. Recalcul de la matrice sur la version livrée (MGT-55)

**Méthode.** Les 1 079 blocs sont comparés automatiquement au texte réellement rendu dans le module livré : 69 écrans, contenus dynamiques et 6 fiches PDF. Le détail est dans la feuille *9_Méthode*. Les feuilles 0 à 5 de la matrice d'origine ne sont pas modifiées ; les résultats sont dans les feuilles 6 à 9.

| Séquence cible | Blocs significatifs | Conservés (mot + adaptation) | Couverture expliquée | Non retrouvés |
|---|---|---|---|---|
| **S2 — Construire une équipe** | 86 | **79 %** | **100 %** | **0** |
| S4 — Autonomie et engagement | 108 | 50 % | 77 % | 25 |
| S1 — Prendre ma place | 207 | 35 % | 69 % | 65 |
| S3 — Faire comprendre | 133 | 36 % | 65 % | 47 |
| S5 — Préserver la relation | 137 | 32 % | 61 % | 54 |
| Entrée + S6 — Comparaison | 33 | 39 % | 58 % | 14 |
| Entrée — Contrat pédagogique | 14 | 21 % | 43 % | 8 |
| Entrée — Bienvenue | 33 | 21 % | 36 % | 21 |
| S6 — Faire évoluer ma pratique | 37 | 8 % | 19 % | 30 |
| **Total** | **788** | **40 %** | **67 %** | **264** (6 866 mots) |

**Couverture expliquée** = bloc conservé, adapté, condensé à vérifier, ou retiré par un arbitrage CDC tracé.
**Hors calcul :** 265 métadonnées de conception (fiches signalétiques, séquençages, scripts vidéo) et 26 intitulés absorbés par les 6 repères.

### Ce que cela veut dire

- **Les lots A à F n'ont supprimé aucun contenu du corpus sans arbitrage.** Tous les écarts entre la base et la candidate correspondent à une décision du CDC : instantanés, petits bilans, « Repère du corpus », intitulés « Les références », MGT-12.
- **Les 264 blocs non retrouvés étaient déjà absents de la base UX18I.** La perte de contenu signalée par Marie-Noëlle pour S2 touche en réalité tout le module. Elle est la plus forte en S6 (plan d'action, module 7), à l'entrée (Bienvenue), puis en S5, S3 et S1.
- **La définition de « terminé » (§12.4) n'est donc pas atteinte hors S2.** Ces écarts sont maintenant identifiés bloc par bloc dans la feuille *8_À réintégrer*, avec une colonne de décision.

**Limite de la mesure.** Une reformulation fidèle mais avec des mots très différents peut apparaître comme « non retrouvée ». Les 66 blocs « condensés — à vérifier » demandent une lecture humaine. Pour corriger un statut, il suffit d'utiliser la colonne Validation de la feuille 6 : la synthèse se recalcule.

## 5. Suite proposée

Je propose de traiter les autres séquences avec la même méthode qu'en S2 : réintégration au mot près, segmentation si besoin, sans aucune rédaction. Un lot par séquence, dans l'ordre de l'écart : S6 et l'entrée, puis S5, S3, S1 et S4.

**Conséquence à anticiper.** Le module va s'allonger. S2 a gagné 2 écrans ; S1, S3 et S5 en gagneraient probablement 2 à 4 chacune. Avant d'engager ces lots, il faut un arbitrage IFAP / Marie-Noëlle : vise-t-on 100 % du corpus significatif, comme le prévoit le CDC (§9), ou décide-t-on, bloc par bloc dans la feuille 8, de ce qui est écarté avec justification ?
