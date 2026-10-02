# Rapport de delta et de non-régression — Lot A

**Module :** Manager ses collaborateurs en tant qu'élu — IFAP × Congrès de la Nouvelle-Calédonie
**Candidate :** UX18I-A (lot A — nettoyage des fuites de production et sources)
**Date :** 1er octobre 2026
**Référentiel :** Cahier des charges d'évolution v1.0, annexe A

## 1. Traçabilité des versions

| Élément | Empreinte SHA-256 |
|---|---|
| Base gelée — archive UX18I_ACCESSIBILITE_OK.zip | 638a7386ecda11815770c80a4addb7fd1be273a65570dbc42d46485a99ab329f |
| Base gelée — index.html | 839a7c658788e43e376815dd78eccb748b67415e552a7a622f75ecc14ab06b5e |
| Candidate — index.html | a789d4bcca78816668b8087a69061e806c21d4863225632cd521a9b74200a124 |
| Candidate — archive UX18I-A_LOT-A.zip | 58a5ea9afa0aedb8994f9ffc0e705b22f6c14b31cdae8549015024b20e73a976 |

Fichiers modifiés : **index.html uniquement**. Les 23 images et les 6 PDF sont identiques à la base, empreinte par empreinte. Les 13 images embarquées dans index.html sont identiques octet par octet.

## 2. Deltas appliqués (21 modifications)

| # | ID | Écran | Avant | Après | Statut corpus |
|---|---|---|---|---|---|
| 1 | MGT-12 | mod-s1-01e | « Ce module vous appartient plus que les précédents : il repose sur des questions à vous poser sincèrement, propres à votre situation. » | « Ce module repose sur des questions à vous poser sincèrement. » | Modifié / arbitré (formulation cible CDC) |
| 2 | MGT-47 | mod-s3-00 | « Repère du corpus : MODULE 4 COMMUNIQUER COMME MANAGER » | Supprimé. MNL-0443 reporté en attribut invisible sur le titre. | Modifié / arbitré (jargon interne) |
| 3 | MGT-53 | mod-s4-00 | « Repères du corpus : MODULE 3 — DONNER DU CAP… » | Supprimé. MNL-0323–0324 reporté sur le titre. | Modifié / arbitré |
| 4 | MGT-53 | mod-s5-00 | « Repères du corpus : MODULE 5 — GÉRER LES TENSIONS… » | Supprimé. MNL-0608–0609 reporté sur le titre. | Modifié / arbitré |
| 5 | MGT-43 | mod-e04 | Surtitre « Avant de commencer · E04 » | « Avant de commencer » | Modifié / arbitré |
| 6 | MGT-43 | g-post | Surtitre « Positionnement · S6-01 » | « Positionnement · Ma photographie aujourd'hui » (libellé déjà présent à l'accueil) | Modifié / arbitré |
| 7 | MGT-10 | g-pre | Bloc visible « Référence scientifique · Pourquoi poser un point de départ » | Accordéon « Source » fermé ; texte intégral conservé | Transformation de forme |
| 8 | MGT-10 | mod-s1-01d | Libellé « Référence scientifique » | « Source » ; MNL-0817/0818 rattachés | Transformation de forme |
| 9 | MGT-42 | mod-s2-04a | « Références scientifiques et professionnelles » (Belbin, Bauer) | Accordéon « Source » | Transformation de forme |
| 10 | MGT-43 | mod-s3-04c | « Référence scientifique · L'impact des mots — Le corpus de Marie-Noëlle rappelle le biais de négativité… » | Accordéon « Source » ; « Le corpus de Marie-Noëlle rappelle » retiré, contenu scientifique intact | Transformation de forme + modifié / arbitré |
| 11 | MGT-53 | mod-s3-04c | « la recherche mobilisée dans le corpus invite à observer » | « la recherche invite à observer » | Modifié / arbitré |
| 12 | MGT-10 | mod-s4-05c | « Références scientifiques et professionnelles » (Oncken & Wass, Deci & Ryan, Hattie & Timperley, Mueller & Dweck) | Accordéon « Source » | Transformation de forme |
| 13 | MGT-10 | mod-s5-05c | « Références scientifiques et professionnelles · Intervenir avant l'escalade » (Deutsch, Glasl) | Accordéon « Source » | Transformation de forme |
| 14 | MGT-10 | g-fin | Libellé « Référence scientifique » (Gollwitzer, déjà dans un accordéon) | « Source » | Transformation de forme |
| 15 à 19 | MGT-11 | mod-s1-06, s2-06, s3-05, s4-06, s5-06 | Références répétées en fin de séquence | Supprimées. Chaque référence reste présente une fois, dans l'apport de sa séquence. | Déplacé (occurrence unique conservée) |

Le composant « Source » utilisé est le composant `details.mgt-source` déjà présent dans UX18I (s1-01d). Aucune CSS n'a été ajoutée.

## 3. Contrôles de non-régression

| Dimension | Contrôle | Résultat |
|---|---|---|
| Contenu | Identifiants MNL distincts présents dans le code | 72 avant / 72 après — aucune perte de traçabilité |
| Contenu | Références bibliographiques | Toutes présentes au moins une fois, sans exception |
| Contenu | Recherche sur le texte rendu : « corpus », « MODULE », « MNL- », « E04 », « S6-01 », « Référence(s) scientifique(s) », « Référence(s) associée(s) », « appartient plus » | 0 occurrence |
| Fonctionnel | Chargement et affichage des 68 écrans via le routeur, sur 3 viewports | 68/68 affichés |
| Fonctionnel | Ouverture d'une « Source » au clavier (Entrée) | Conforme |
| Technique | Erreurs JavaScript (console et exceptions) | 0 avant / 0 après |
| Visuel | Débordement horizontal (desktop 1440, iPad paysage 1180, iPad portrait 820) | Aucun |
| Visuel | Écrans dont la hauteur a changé | 13, tous ciblés par une exigence du lot. Aucun écran non ciblé n'est modifié. |
| Périmètre | Différences non rattachées à un ID MGT | Aucune. Seule addition hors ID : un commentaire HTML d'en-tête de version (MGT-56, non rendu). |

La recette headless ne remplace pas le test sur un iPad réel (MGT-54), qui reste à conduire par l'IFAP.

## 4. Points reportés ou ouverts

**MGT-04.** Non traité dans ce lot.
- Les 5 rappels « Ces trois réponses sont conservées… » disparaîtront avec les instantanés (lot C).
- Les mentions « déclaratif » de g-pre et g-post sont des mentions de conformité (règles R15/R27 inscrites dans le code) : elles sont conservées. Arbitrage à confirmer.

**Fuite restante.** « Profil A/B/C » (JS de la S2) sera traité au lot B, avec MGT-32.

**Surtitres hétérogènes.** « Pause de consolidation », « Comparaison réflexive », etc. seront traités au lot C (MGT-14).

**Mise en page des Sources.** Le texte ouvert d'une Source est étroit sur iPad portrait. Ce point relève de la largeur de colonne, traitée au lot D (MGT-15).
