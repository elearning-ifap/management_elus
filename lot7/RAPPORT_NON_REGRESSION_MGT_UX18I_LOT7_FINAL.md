# Rapport de non-régression — MGT UX18I lot 7 corrigé

Code du module : commit `4778676a623bae2ce89fdc2a4417f3cddee55b7e` · blob `index.html` `dfea37d25b0946f326a0ac688a162f6300949425`.

## Invariants contrôlés

- 67 panneaux `section.panel` conservés ;
- 5 séquences et 8 défis conservés ;
- six repères pédagogiques communs inchangés dans leur ordre et leur fonction ;
- positionnements d’entrée et de sortie à 6 dimensions conservés ;
- 6 fiches PDF toujours présentes ;
- aucune réapparition de « Profil A/B/C », « Repère du corpus » ou ancien instantané S3 ;
- MGT-29 reste clos par arbitrage.

## Non-régression fonctionnelle ciblée

- MGT-17 : interaction réelle testée ;
- MGT-19 : classement erroné détecté, feedback affiché, repositionnement encore possible ;
- MGT-38 : avec Thomas choisi, Thomas est conservé sur les résultats des défis 3 et 4 ;
- variante du défi 4 : « Thomas arrive… » après sélection de Thomas ;
- 0 erreur JavaScript pendant la recette ciblée.

## Responsive

- iPad portrait : 67/67 écrans, 0 débordement horizontal, 0 cible contrôlée < 44 px ;
- iPad paysage : 67/67 écrans, 0 débordement horizontal, 0 cible contrôlée < 44 px ;
- desktop : 67/67 écrans, 0 débordement horizontal, 0 cible contrôlée < 44 px.
