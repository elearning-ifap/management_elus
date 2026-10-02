# Prompts images — Module « Manager ses collaborateurs en tant qu'élu »

À utiliser dans Gemini, avec l'image de référence jointe à chaque prompt. Les références sont dans **References_images_prompts.zip** :
- `REF_` : portraits canoniques et image de style à garder ;
- `ACTUEL_` : visuels à remplacer.

## Méthode

1. **Pour les portraits, joindre toujours le portrait canonique du personnage** et demander de garder le même visage. Sans référence, le générateur invente un nouveau visage, ce que la bible des personnages interdit (CDC §6 et §10).
2. Générer 3 ou 4 variantes, puis retenir celle dont le visage, la coiffure et la tenue sont identiques à la référence.
3. Formats à respecter :
   - portraits : carré 1:1 (les originaux font 1254 × 1254 px) ;
   - bandeaux : très larges (les actuels font 1600 × 396 px, environ 4:1). Générer en 21:9, puis recadrer à 1600 × 396.
4. Me transmettre les images retenues. Je les intègre en remplaçant les fichiers actuels, avec traçabilité.

## Bloc de style commun

À coller en début de chaque prompt :

> Illustration 3D stylisée, style film d'animation (rendu doux, type Pixar), proportions réalistes légèrement stylisées, grands yeux expressifs, peau et textiles finement texturés, éclairage studio doux et chaleureux. Palette sobre : bleu nuit, gris bleuté, beige, avec de rares touches d'or et de turquoise. Aucun texte, aucun logo, aucun drapeau, aucune inscription lisible. Pas de photoréalisme, pas d'ambiance sombre ni dramatique.

---

## Point 2 — Portraits visés par les retours de Marie-Noëlle

### 2a. Thomas, pastille de la séquence 1

Il remplace `Thomas examine un dossier urgent.jpg`, perçu comme un « homme triste » (MGT-06). Joindre `REF_portrait_canonique_thomas.png`.

> [Bloc de style commun]
> Portrait en buste de l'homme de l'image de référence : garder exactement le même visage, la même coiffure (cheveux bruns légèrement bouclés), la même barbe courte et la même tenue (chemise bleu nuit ouverte sur un tee-shirt beige). Il tient deux dossiers contre lui d'une main, l'autre main légèrement ouverte, dans une attitude posée et disponible. Expression calme, attentive et assurée, léger sourire : un chargé de mission expérimenté qui maîtrise ses dossiers et attend un cap clair. Regard vers l'objectif. Fond uni dégradé gris-bleu très clair (#E8EEF4), sans décor. Cadrage du haut des cuisses au-dessus de la tête, personnage centré. Format carré 1:1.

**Nom de fichier attendu :** `thomas-pose-dossiers.jpg`

### 2b. Maëva, pastille de la séquence 2

Il remplace `maeva-carnet-attentive.jpg`, dont les yeux écarquillés donnent un air inquiet (MGT-30). Joindre `REF_portrait_canonique_maeva.png`.

> [Bloc de style commun]
> Portrait en buste de la jeune femme de l'image de référence : garder exactement le même visage, les mêmes cheveux noirs bouclés attachés et la même tenue (blazer bleu marine, haut bleu clair). Elle tient un carnet fermé contre elle, avec une attitude ouverte et volontaire : une juriste méthodique qui vient d'arriver dans l'équipe et découvre son nouvel environnement avec curiosité. Expression souriante, regard franc vers l'objectif, sourcils détendus, sans étonnement ni inquiétude. Fond uni dégradé gris-bleu très clair (#E8EEF4), sans décor. Cadrage du haut des cuisses au-dessus de la tête, personnage centré. Format carré 1:1.

**Nom de fichier attendu :** `maeva-accueil-souriante.jpg`

**Alternative sans génération :** utiliser `maeva-checklist-tablette.jpg`, déjà dans l'archive (Maëva souriante, tablette avec check-list). Elle est cohérente avec la check-list « 30 premiers jours » de la séquence.

---

## Point 4 — Bandeaux de décor des écrans de situation

Ce sont des décors sans personnage. Joindre `REF_style_Thomas_plan_action.jpg` comme référence de style, et l'ancien bandeau (`ACTUEL_bandeau_Sx.jpg`) comme référence de composition.

### 4a. Séquence 1 — Le dossier qui n'est pas prêt (écran mod-s1-01)

> [Bloc de style commun]
> Décor sans personnage : le bureau d'un collaborateur d'élu, la veille d'une commission, en fin de journée. Au premier plan, sur un bureau en bois clair, un dossier ouvert et annoté avec quelques post-it, une montre-bracelet posée à côté, une tasse de café à moitié bue et un stylo. Sentiment d'échéance proche mais maîtrisée, sans désordre ni dramatisation. Au fond, légèrement flou, une fenêtre donnant sur des pins colonnaires et un bout de lagon turquoise sous une lumière dorée de fin d'après-midi. Composition panoramique très large, sujet principal centré horizontalement, beaucoup d'air en haut et en bas pour permettre un recadrage. Format 21:9.

**Nom de fichier attendu :** `MGT-BANDEAU-S1-dossier-commission.jpg`

### 4b. Séquence 3 — « Prépare-moi quelque chose rapidement » (écran mod-s3-01)

> [Bloc de style commun]
> Décor sans personnage : une salle de commission vide d'une assemblée délibérante, lumineuse et sobre. Tables disposées en U avec micros sur pied fin, fauteuils bleu nuit alignés, boiseries claires. Au premier plan, un dossier annoté posé sur la table, avec une feuille de notes et un stylo. Grandes baies vitrées laissant voir une végétation tropicale et des pins colonnaires. Ambiance calme, institutionnelle, accueillante. Aucun drapeau, aucun emblème, aucune plaque nominative lisible. Composition panoramique très large, beaucoup d'air en haut et en bas. Format 21:9.

**Nom de fichier attendu :** `MGT-BANDEAU-S3-salle-commission.jpg`

### 4c. Séquence 4 — Le dossier de subvention (écran mod-s4-01)

> [Bloc de style commun]
> Décor sans personnage : vue légèrement plongeante sur une table de travail claire. Un dossier de subvention ouvert et bien organisé, avec intercalaires de couleur, un bloc-notes portant des puces et des flèches dessinées (sans texte lisible), un stylo, deux post-it turquoise et or, et un petit graphique imprimé. Ambiance de dossier sensible en cours de traitement, ordonné et maîtrisé. Lumière naturelle douce venant de la gauche. Composition panoramique très large, éléments répartis sur toute la largeur. Format 21:9.

**Nom de fichier attendu :** `MGT-BANDEAU-S4-dossier-subvention.jpg`

### 4d. Séquence 5 — Le retard qui se répète (écran mod-s5-01)

> [Bloc de style commun]
> Décor sans personnage : un coin de bureau calme préparé pour un entretien individuel. Deux fauteuils confortables gris-bleu placés face à face, légèrement de biais, une petite table basse entre eux avec deux verres d'eau et un carnet fermé. Une plante verte tropicale, une bibliothèque basse en bois clair, une fenêtre aux stores à demi ouverts laissant entrer une lumière douce de matinée. Ambiance apaisée, propice au dialogue, ni froide ni solennelle. Composition panoramique très large, les fauteuils au centre. Format 21:9.

**Nom de fichier attendu :** `MGT-BANDEAU-S5-entretien.jpg`

---

## Contrôle avant transmission

- [ ] Visage, coiffure et tenue strictement identiques au portrait canonique (portraits).
- [ ] Aucun texte lisible, aucun logo, aucun drapeau.
- [ ] Rendu illustré 3D, cohérent avec les autres personnages (pas de photo).
- [ ] Ambiance lumineuse, pas sombre.
- [ ] Bandeaux recadrés en 1600 × 396 px, sujet visible une fois recadrés.
