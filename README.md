# Manager ses collaborateurs en tant qu'élu

Module e-learning de la plateforme **LIANE** (IFAP Nouvelle-Calédonie), conçu pour les élus du Congrès de la Nouvelle-Calédonie (mandature 2026-2031). Contenu expert : Marie-Noëlle Lopez.

- **Format :** une page HTML autonome (`src/index.html`), destinée à être empaquetée en SCORM 1.2 pour Moodle (eformation.ifap.nc).
- **Version courante :** `UX18I-U` (tag `ux18i-U`). La base de départ est `UX18I_ACCESSIBILITE_OK` (tag `ux18i-base`).
- **Contenu :** 59 écrans, 5 séquences, 8 défis (« carnet de mandat »), 3 simulateurs, positionnements d'entrée et de sortie, plan d'action. Durée affichée : environ 2 h 50.

## Arborescence

```
src/                    le module (index.html, img/, pdf/)
docs/rapports/          rapports de modifications des lots A à G
docs/pilotage/          pré-audit du CDC, registre MGT, matrice de couverture du corpus
docs/prompts-images/    prompts de génération des visuels (bandeaux, cartes)
docs/references-images/ portraits de référence des personnages (cohérence visuelle)
tools/                  scripts de recette automatisée (Playwright)
CHANGELOG.md            historique des lots
```

## Consulter le module

Ouvrir `src/index.html` dans un navigateur récent. Aucun serveur n'est nécessaire.

## Recette automatisée

```bash
pip install playwright && playwright install chromium
python tools/recette_parcours.py src/index.html      # parcours complet au bouton « Suivant », erreurs JS
python tools/recette_completion.py src/index.html    # complétion SCORM avec un faux LMS
python tools/audit_contrastes.py src/index.html      # contrastes WCAG AA (aucune sortie = conforme)
```

Résultats attendus sur `ux18i-U` : 59 écrans parcourus sans erreur ; « completed » à 100 % pour un apprenant qui fait tout ; aucun contraste sous le seuil.

## Règles de travail

1. **Un lot = un commit + un tag** (`ux18i-<lot>`). On repart toujours de la version précédente, sans refonte globale.
2. **Chaque modification se rattache à une exigence** (identifiant MGT du cahier des charges ou constat de recette). Une modification sans rattachement est rejetée.
3. **Le corpus de l'experte est la source.** Il est intégré au mot près ; toute adaptation est tracée dans la matrice de couverture (`docs/pilotage/`).
4. **Après chaque lot :** recette automatisée, captures avant / après sur ordinateur et iPad portrait, mise à jour du CHANGELOG.

## Reste à faire avant la mise en production

- Relecture par Marie-Noëlle Lopez des contenus rédigés : simulateurs, phrases « En bref », accroches des défis, question du défi 7.
- Recette sur un vrai iPad et test dans Moodle : reprise, complétion, reprise sur un autre appareil, impression du carnet.
- Fiches PDF (`src/pdf/`) à mettre à jour avec les nouveaux titres de séquence.
- Illustrations dédiées des 8 cartes du carnet (prompts dans `docs/prompts-images/`).
- Package SCORM (manifeste, retrait des images inutilisées).
