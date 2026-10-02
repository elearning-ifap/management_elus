# Rapport de delta et de non-régression — Lot D

**Module :** Manager ses collaborateurs en tant qu'élu — IFAP × Congrès de la Nouvelle-Calédonie
**Candidate :** UX18I-D (lot D, premiumisation CSS sans refonte), construite sur UX18I-A (lot A)
**Date :** 1er octobre 2026
**Référentiel :** Cahier des charges d'évolution v1.0, §7 et annexe A

## 1. Traçabilité des versions

| Élément | Empreinte SHA-256 |
|---|---|
| Base gelée UX18I — archive | 638a7386ecda11815770c80a4addb7fd1be273a65570dbc42d46485a99ab329f |
| Candidate précédente UX18I-A — index.html | a789d4bcca78816668b8087a69061e806c21d4863225632cd521a9b74200a124 |
| Candidate UX18I-D — index.html | b3c3cf94addba9edd7cd0e67ebde472be216f8f69b6982f8cff5278c3b5abe04 |
| Candidate UX18I-D — archive | 0c428abf65b3bc8d2d25972450118fd2b4dbc01891f6b7a5e60798c3c4362704 |

**Fichier modifié :** index.html uniquement. Les 23 images et les 6 PDF sont identiques à la base gelée.

## 2. Méthode

Toute la premiumisation passe par **une seule couche CSS ajoutée**, `<style id="ux18i-lot-d">`. Elle est placée après la dernière feuille de style existante. Aucune règle des couches antérieures (noyau, UX14, UX15, UX18H) n'est modifiée. Chaque bloc de la couche porte son identifiant d'exigence en commentaire.

Pour revenir en arrière sur la partie visuelle, il suffit de supprimer cette balise. Deux retouches HTML complètent le lot (MGT-18, MGT-46).

## 3. Deltas appliqués

| ID | Zone | Avant | Après |
|---|---|---|---|
| H-01 (§7) | Police | Pile « Lato, Segoe UI, Arial » : rendu Segoe UI sous Windows, contraire au CDC | Arial, Helvetica, sans-serif |
| H-01 (§7) | Corps de texte | 16 px (token) ; textes de cartes à 13–14 px ; descriptions des personnages à l'accueil à 11,5 px | Corps à 17 px pour apports, consignes, options, listes, cartes de réflexion et tableaux. Textes secondaires : 16 px (cartes modèle, jetons de tri, cartes « six repères », fiches) et 15 px (Source, aides de saisie, citations). Personnages à l'accueil : 14 px, contrainte de colonne. |
| H-01 (§7) | Chapeau (.chapo) | 16 px gris | 18 px, couleur encre |
| H-01 (§7) | Largeur de lecture | 64 ch (environ 600 px) | 78 ch (environ 740 px, cible CDC 700–760 px) |
| MGT-01 | Accueil — « Votre parcours en un clin d'œil » | Titre 20 px ; étapes 12,5 px grises | Titre 26 px ; étapes 15,5 px couleur encre ; numéros agrandis. Page non recomposée. |
| MGT-02 | Accueil — 8 défis | Distinction par un filet de couleur fin | Pictogramme décoratif propre à chaque défi, teinté à la couleur de sa séquence (réglage, liste, cible, arrivée, message, transmission, étoile, bouclier). Libellés, ordre et états vert/jaune inchangés (MGT-03 préservé). |
| MGT-15 | Fins de séquence — « Les repères à emporter » | Liste à puces étirée sur 1 000 px | Cartes en grille (3 colonnes sur desktop, 1 colonne sur iPad portrait), 17 px |
| MGT-18 | mod-s1-02 | Pastille « 4 » + « Quatre rôles distincts… » | Pastille « 1 », alignée sur S2 à S5 où la pastille porte le numéro de séquence. Libellé : « 4 rôles distincts coexistent autour de vous. » |
| MGT-46 | S2 (mod-s2-01, 01b, 02, 06) | Surtitre « Séquence 2 » seul | « Séquence 2 · Construire et intégrer la bonne équipe » (titre de l'ouverture mod-s2-00) |
| §11 | Ajouts du lot | — | `prefers-reduced-motion` respecté |

## 4. Contrôles de non-régression

| Dimension | Contrôle | Résultat |
|---|---|---|
| Technique | Erreurs JavaScript sur 3 viewports | 0 |
| Fonctionnel | 68 écrans affichés via le routeur | 68/68 |
| Visuel | Débordement horizontal (1440, 1180, 820 px) | Aucun |
| Visuel | Texte tronqué dans un conteneur à hauteur fixe | 0 avant / 0 après |
| Visuel | Allongement des écrans (effet de la typographie) | Médiane +1,6 % desktop, +2,3 % iPad portrait ; maximum +17 % ; aucun écran au-delà de +25 % |
| Visuel | Textes de plus de 40 caractères sous 15 px | Restent : surtitres et badges, qui sont des étiquettes, et les cartes personnages de l'accueil (14 px) |
| Contenu | Texte pédagogique modifié | Aucun, hors MGT-18 (« Quatre » → « 4 ») et MGT-46 (surtitres S2) |
| Périmètre | Lignes de diff hors couche CSS | 5 lignes HTML, toutes rattachées à MGT-18 ou MGT-46 |

Les captures avant/après (desktop et iPad portrait) sont fournies dans *Preuves_captures_LOT-D.zip* : défis, clin d'œil, repères à emporter, pastille S1 et un écran d'apport S2.

## 5. Points d'attention

- **Changement de police sous Windows.** Le module s'affichait en Segoe UI sur les postes Windows ; il passe en Arial. C'est conforme au CDC (« Arial conservée »), mais c'est visible pour qui connaît la version actuelle.
- **Cartes personnages de l'accueil.** La colonne est trop étroite pour porter 17 px sans recomposer le bloc. Le texte est passé de 11,5 à 14 px. Aller plus loin demande de recomposer ce bloc, ce que le CDC interdit sans décision.
- **Espacements du §7.** Les valeurs cibles (48–64 px entre zones, 24–32 px de padding de carte) ne sont pas appliquées globalement : elles ne sont rattachées à aucun ID du registre. Je propose de les traiter au lot C, écran par écran, avec la nouvelle grammaire.
- **MGT-46 limité à S2**, comme le demande le registre. L'harmonisation des surtitres des autres séquences relève de MGT-14 et MGT-57 (lot C).
- **Validation sur iPad réel** : reste à faire par l'IFAP (MGT-54).
