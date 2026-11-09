"""Génère les 6 fiches outils MGT au gabarit sobre (validé par Marc le 10/11/2026).
Contenu repris mot pour mot des fiches précédentes ; seule la mise en forme change.
Usage : python3 generer_fiches.py DOSSIER_SORTIE   (produit des .html ; pdf.js les imprime)
"""
import sys, os, html as H

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
e = H.escape

CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fiche.css'), encoding='utf8').read()

AIDE_FEUILLE = "Choisissez une situation réelle. Renseignez les éléments utiles avant d’agir, puis fixez votre prochain point de suivi."
AIDE_REPERE = "Repérez la situation qui vous correspond et utilisez ce cadre comme pense-bête pour choisir votre prochain geste."
AIDE_QUESTIONS = "Utilisez ces questions pour préparer une décision, un échange ou un point de suivi."
PIED = "Manager ses collaborateurs en tant qu’élu · fiche personnelle mobilisable dans le mandat"

FICHES = [
 dict(n='01', fichier='MGT_FICHE_01_Place_manager', seq='Séquence 1 · Prendre sa place et ajuster son autorité',
  titre='Prendre ma place de manager élu', sous='Rôle, responsabilités et autorité ajustée',
  pourquoi="Le mandat politique donne une légitimité pour décider, mais il n’autorise ni à déléguer sa parole ni à tout contrôler. Quand les rôles restent implicites, le collaborateur peut agir au-delà de son périmètre, attendre des validations inutiles ou parler au nom de l’élu sans cadre clair.",
  rep_titre='La réponse managériale : quatre repères pour agir',
  rep_intro="Prendre sa place consiste à assumer ce qui relève du mandat, à clarifier ce qui peut être confié et à ajuster son autorité à la situation. Le cap appartient à l’élu ; la préparation, l’expertise et la mise en œuvre peuvent être organisées avec le collaborateur.",
  reperes=[('Assumer le mandat','Décider, arbitrer et porter personnellement sa parole politique.'),
           ('Clarifier les rôles','Nommer ce qui relève de l’élu, du collaborateur et du partage.'),
           ('Ajuster l’autorité','Combiner un cap clair, une marge d’action et un suivi adapté.'),
           ('Sécuriser la parole','Préciser qui prépare, qui conseille, qui s’exprime et au nom de qui.')],
  emporter="Une autorité ajustée n’est ni un contrôle permanent ni un laisser-faire. Elle rend explicites la décision, la responsabilité et la marge d’action.",
  q_aide=AIDE_QUESTIONS,
  questions=[('Rôle','Qu’est-ce qui relève exclusivement de mon mandat ?'),('Délégation','Que puis-je confier sans abandonner ma responsabilité ?'),
             ('Autorité','De quel niveau de cadre cette situation a-t-elle besoin ?'),('Parole','Qui peut préparer, conseiller ou communiquer - et au nom de qui ?')],
  champs=['Situation ou dossier à clarifier','Collaborateur concerné','Échéance','Responsabilité que je conserve','Marge d’action que je confie','Date du prochain point'],
  tab_titre='Le repère opérationnel', tab_aide=AIDE_REPERE,
  tab=[('Élu','Décider, arbitrer, voter et assumer la parole politique.'),('Collaborateur','Préparer, analyser, proposer et mettre en œuvre dans le cadre fixé.'),
       ('Partagé','Échanger, coordonner, suivre et ajuster.'),('À clarifier','Tout ce qui reste ambigu, sensible ou négociable.')],
  engagement='Dans les sept prochains jours, je clarifierai :'),
 dict(n='02', fichier='MGT_FICHE_02_Construire_equipe_pilote', seq='Séquence 2 · Construire et intégrer la bonne équipe',
  titre='Construire une équipe sur laquelle m’appuyer', sous='Comprendre, choisir, intégrer et suivre',
  pourquoi="Un collaborateur choisi uniquement parce qu’il est disponible ou proche de vous peut ne pas répondre aux besoins du mandat. À l’inverse, un profil pertinent, mais mal intégré, risque de rester dépendant, de mal hiérarchiser les priorités ou de quitter l’équipe faute de repères.",
  rep_titre='La réponse managériale : construire l’équipe en quatre décisions',
  rep_intro="La qualité de l’équipe se construit dans le temps. Le besoin du mandat précède le choix d’une personne ; le choix est ensuite confirmé par une intégration organisée et un suivi qui élargit progressivement l’autonomie.",
  reperes=[('Définir le besoin','Partir des missions et des résultats attendus. Nommer les compétences indispensables et la complémentarité recherchée.'),
           ('Choisir','Tenir ensemble trois critères : loyauté au projet, compétence réellement utile et complémentarité avec l’équipe.'),
           ('Intégrer','Rendre explicites le rôle, les priorités, les résultats, les codes, les interlocuteurs, la marge de décision et le suivi.'),
           ('Suivre et ajuster','Faire des points courts, lever les obstacles et élargir l’autonomie à mesure que les repères sont compris et mobilisés.')],
  emporter="La confiance compte, mais elle ne remplace ni les compétences ni la complémentarité. Une bonne intégration transforme progressivement une personne recrutée en collaborateur fiable et autonome.",
  q_aide="Utilisez ces quatre questions avant un recrutement, une réorganisation du cabinet ou l’arrivée d’un nouveau collaborateur.",
  questions=[('Besoin','Quel résultat concret manque aujourd’hui au mandat ?'),('Choix','Quelles preuves avons-nous de la compétence, de la loyauté et de la complémentarité ?'),
             ('Intégration','Quels repères doivent être compris dès la première semaine ?'),('Suivi','Quand vérifierons-nous les obstacles, les résultats et la progression de l’autonomie ?')],
  champs=['Besoin ou résultat à sécuriser','Collaborateur ou profil concerné','Échéance visée','Premier geste concret à réaliser','Résultat observable attendu','Date du prochain point'],
  tab_titre='Le suivi des trente premiers jours', tab_aide="Repérez où vous en êtes et vérifiez que l’étape suivante est explicitement prévue.",
  tab=[('Avant l’arrivée','Préparer le cadre, les accès, les dossiers et les interlocuteurs.'),('1re semaine','Clarifier le rôle, les priorités, les résultats et la marge de décision.'),
       ('Jours 8 à 30','Observer la prise en main, lever les obstacles et faire progresser l’autonomie.'),('Bilan à 30 jours','Nommer les acquis, les ajustements et la prochaine étape.')],
  engagement='Dans les sept prochains jours, je vais :'),
 dict(n='03', fichier='MGT_FICHE_03_Attente_claire', seq='Séquence 3 · Clarifier les attentes',
  titre='Faire comprendre ce que j’attends', sous='Transformer une intention en demande actionnable',
  pourquoi="Une consigne qui paraît évidente à l’élu peut rester ambiguë pour le collaborateur. Le flou provoque des reprises, des retards, de la frustration et parfois un contrôle excessif qui aurait pu être évité par quelques repères explicites.",
  rep_titre='La réponse managériale : quatre repères pour agir',
  rep_intro="Une attente claire indique où aller, pourquoi le résultat est utile, ce qui est prioritaire et dans quel délai agir. Elle précise aussi la marge d’initiative et organise une vérification de compréhension sans dicter inutilement toute la méthode.",
  reperes=[('Donner le cap','Nommer le résultat concret et son destinataire ou son usage.'),('Situer la priorité','Préciser ce qui compte maintenant et l’échéance réelle.'),
           ('Ouvrir une marge','Indiquer ce qui peut être décidé, proposé ou doit être validé.'),('Vérifier et suivre','Faire reformuler l’essentiel et convenir du prochain point.')],
  emporter="Clarifier ne signifie pas tout prescrire : le manager sécurise le résultat, les limites et le suivi, puis laisse une place adaptée à la manière d’agir.",
  q_aide=AIDE_QUESTIONS,
  questions=[('Résultat','Qu’est-ce qui doit être produit ou obtenu concrètement ?'),('Utilité','À quoi servira ce travail et pour qui ?'),
             ('Cadre','Quelle priorité, quelle échéance et quelles limites ?'),('Compréhension','Comment vérifier que le message reçu correspond au message voulu ?')],
  champs=['Demande ou résultat attendu','Collaborateur concerné','Échéance','Marge d’initiative accordée','Point à faire valider','Date et objet du suivi'],
  tab_titre='Le repère opérationnel', tab_aide=AIDE_REPERE,
  tab=[('Résultat','Ce qui doit être obtenu.'),('Usage','À quoi et à qui cela servira.'),('Cadre','Priorité, échéance et ressources.'),('Suivi','Marge d’action, reformulation et point convenu.')],
  engagement='Pour ma prochaine demande, je préciserai :'),
 dict(n='04', fichier='MGT_FICHE_04_Autonomie_engagement', seq='Séquence 4 · Faire grandir l’autonomie',
  titre='Faire grandir l’autonomie', sous='Déléguer, suivre et reconnaître',
  pourquoi="Tout contrôler rend le collaborateur dépendant et transforme l’élu en point de passage obligé. À l’inverse, déléguer sans cadre peut exposer le mandat à des erreurs ou à des décisions non sécurisées. L’autonomie se construit par paliers, pas en une seule fois.",
  rep_titre='La réponse managériale : quatre repères pour agir',
  rep_intro="Déléguer consiste à confier un résultat et une marge d’action tout en restant disponible pour un suivi convenu. L’autonomie progresse lorsque les responsabilités sont explicites, que le droit à l’erreur est proportionné au risque et que le retour reconnaît précisément la contribution.",
  reperes=[('Confier un résultat','Décrire l’effet ou la production attendue, pas seulement une tâche.'),('Fixer les limites','Nommer les points non négociables et les décisions à faire valider.'),
           ('Ajuster le suivi','Prévoir des points utiles sans reprendre systématiquement la main.'),('Reconnaître','Nommer la contribution, son effet et la prochaine progression possible.')],
  emporter="L’autonomie est une capacité accompagnée : elle augmente lorsque le cadre est clair, l’expérience progresse et le suivi devient plus léger.",
  q_aide=AIDE_QUESTIONS,
  questions=[('Résultat','Quel résultat puis-je réellement confier ?'),('Risque','Qu’est-ce qui doit rester non négociable ou validé ?'),
             ('Marge','Quelles décisions le collaborateur peut-il prendre seul ?'),('Progression','Quel retour l’aidera à franchir le palier suivant ?')],
  champs=['Résultat que je souhaite déléguer','Collaborateur concerné','Échéance','Décisions laissées au collaborateur','Points non négociables','Date et forme du suivi'],
  tab_titre='Le repère opérationnel', tab_aide=AIDE_REPERE,
  tab=[('Observer','Comprendre la situation et apprendre.'),('Proposer','Analyser et formuler une recommandation.'),
       ('Décider avec validation','Choisir puis faire sécuriser la décision.'),('Agir et rendre compte','Décider dans le cadre convenu et informer.')],
  engagement='Le prochain palier d’autonomie que je vais ouvrir est :'),
 dict(n='05', fichier='MGT_FICHE_05_Reguler_tensions', seq='Séquence 5 · Réguler tôt',
  titre='Réguler les tensions avant l’escalade', sous='Observer, dialoguer et convenir d’une suite',
  pourquoi="Un retard répété, un silence inhabituel ou une réaction vive ne disent pas, à eux seuls, ce qui se passe. Attendre trop longtemps laisse la tension s’installer ; intervenir sur la base d’une interprétation ou d’une étiquette risque au contraire de fermer le dialogue.",
  rep_titre='La réponse managériale : quatre repères pour agir',
  rep_intro="Réguler consiste à intervenir tôt, en s’appuyant sur des faits observables. L’élu ouvre un échange, écoute le point de vue du collaborateur, distingue la difficulté de la personne puis convient d’une suite concrète et vérifiable.",
  reperes=[('Observer les faits','Décrire ce qui est vu ou entendu sans attribuer d’intention.'),('Ouvrir le dialogue','Nommer la situation et inviter l’autre à donner son point de vue.'),
           ('Comprendre','Écouter les besoins, les contraintes et ce qui a déjà été tenté.'),('Convenir d’une suite','Définir l’action, la responsabilité, l’échéance et le prochain point.')],
  emporter="Intervenir tôt ne signifie pas conclure vite. Un échange utile part des faits, recherche la compréhension et se termine par une suite observable.",
  q_aide=AIDE_QUESTIONS,
  questions=[('Faits','Qu’ai-je précisément observé, sans interprétation ?'),('Intention','Quel résultat est-ce que je recherche en ouvrant l’échange ?'),
             ('Écoute','Qu’ai-je besoin de comprendre avant de conclure ?'),('Suite','Quelle action concrète et quel point de suivi pouvons-nous convenir ?')],
  champs=['Fait ou difficulté à traiter','Collaborateur concerné','Date de l’échange','Formulation d’ouverture','Suite concrète convenue','Date du prochain point'],
  tab_titre='Le repère opérationnel', tab_aide=AIDE_REPERE,
  tab=[('Signaux faibles','Observer et ouvrir un espace de parole.'),('Désaccord','Clarifier les faits et les besoins.'),
       ('Crispation','Ralentir, reformuler et recentrer.'),('Conflit ouvert','Sécuriser le cadre et organiser une médiation si nécessaire.')],
  engagement='La situation sur laquelle je vais ouvrir un échange est :'),
]

def entete(f, droite):
    return f'<div class="entete"><span><b>IFAP</b> · Parcours des élus · Fiche outil {f["n"]}</span><span>{e(droite)}</span></div>'

def pied(p):
    return f'<div class="pied"><span>{PIED}</span><span>{p} / 2</span></div>'

def doc(titre, corps):
    return f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{e(titre)}</title><style>{CSS}</style></head><body>{corps}</body></html>'

def fiche_standard(f):
    reps = ''.join(f'<div class="repere"><span class="num">{i}</span><div><h3>{e(t)}</h3><p>{e(d)}</p></div></div>' for i, (t, d) in enumerate(f['reperes'], 1))
    qs = ''.join(f'<li><span class="num">{i}</span><strong>{e(t)}</strong><span>{e(d)}</span></li>' for i, (t, d) in enumerate(f['questions'], 1))
    c = f['champs']
    champs = (f'<div class="champ large"><span>{e(c[0])}</span></div><div class="champ"><span>{e(c[1])}</span></div><div class="champ"><span>{e(c[2])}</span></div>'
              f'<div class="champ large"><span>{e(c[3])}</span></div><div class="champ"><span>{e(c[4])}</span></div><div class="champ"><span>{e(c[5])}</span></div>')
    th = ''.join(f'<th>{e(t)}</th>' for t, _ in f['tab']); td = ''.join(f'<td>{e(d)}</td>' for _, d in f['tab'])
    p1 = f'''<div class="page">{entete(f, f['seq'])}
 <h1>{e(f['titre'])}</h1><p class="sous-titre">{e(f['sous'])}</p><div class="accent"></div>
 <section><p class="label">Pourquoi est-ce important ?</p><p class="intro">{e(f['pourquoi'])}</p></section>
 <section><h2>{e(f['rep_titre'])}</h2><p class="intro">{e(f['rep_intro'])}</p><div class="reperes">{reps}</div></section>
 <div class="emporter"><p class="label">Le repère à emporter</p><p>{e(f['emporter'])}</p></div>{pied(1)}</div>'''
    p2 = f'''<div class="page">{entete(f, 'De la synthèse à l’action dans votre mandat')}
 <section class="premiere"><h2>Comment agir dans votre mandat ?</h2><p class="aide">{e(f['q_aide'])}</p><ol class="questions">{qs}</ol></section>
 <section><h2>Ma feuille de route opérationnelle</h2><p class="aide sans-marge">{e(AIDE_FEUILLE)}</p><div class="champs">{champs}</div></section>
 <section><h2>{e(f['tab_titre'])}</h2><p class="aide">{e(f['tab_aide'])}</p><table class="reperes-tab"><thead><tr>{th}</tr></thead><tbody><tr>{td}</tr></tbody></table></section>
 <div class="engagement"><p class="label">Mon engagement</p><p>{e(f['engagement'])}</p><div class="ligne"></div><div class="ligne"></div></div>{pied(2)}</div>'''
    return doc(f['titre'] + ' — fiche outil', p1 + p2)

# Fiche 06 : référence de formulations (gabarit tableau)
F6 = dict(n='06', fichier='MGT_FICHE_06_Mots_qui_piquent_mots_qui_soutiennent', titre='Les mots qui piquent / les mots qui soutiennent')
BLOCS1 = [
 ('Pour donner une consigne', 'Ça ferme', [('« Débrouillez-vous. »','« Voici ce dont vous avez besoin pour démarrer : … »'),
   ('« Il faut que ça avance. »','« J’ai besoin que ce soit prêt pour [date/heure précise]. »'),
   ('« C’est pas compliqué pourtant. »','« Dites-moi si un point n’est pas clair. »'),
   ('« Vous auriez dû anticiper. »','« La prochaine fois, prévenons-nous plus tôt sur ce type de point. »')]),
 ('Pour faire un retour (feedback)', 'Ça ferme', [('« C’est mal fait. »','« Cette partie est claire ; celle-ci mérite d’être reprise. »'),
   ('« Vous n’y arrivez pas. »','« Voici ce qui manque pour que ce soit complet. »'),
   ('« Ça ne va pas du tout. »','« Voici précisément ce qui doit changer. »'),
   ('« Comme d’habitude… »','(à bannir — ramène toujours au passé plutôt qu’à la situation présente)')]),
]
BLOCS2 = [
 ('Pour reconnaître un travail', 'Ça ferme (ou n’a aucun effet)', [('« C’était pas mal. »','« La logistique était nickel, c’est vous qui avez géré ça. »'),
   ('« Bon travail. » (seul, sans précision)','« Ce point précis a vraiment fait la différence : … »'),
   ('« Vous êtes doué. »','« Vous avez tenu ce délai grâce à votre organisation. »'),
   ('(silence, aucune remarque)','Un mot bref mais spécifique, même en passant.')]),
 ('Pour recadrer', 'Ça ferme', [('« N’importe quoi. »','« Voilà ce qui s’est passé, tel que je le comprends : … »'),
   ('« Vous n’auriez jamais dû. »','« Je me suis senti(e) mis(e) devant le fait accompli. »'),
   ('« Ça ne se reproduira plus, j’espère. »','« J’ai besoin de… la prochaine fois. »'),
   ('(devant témoin)','(en tête-à-tête, dès que possible)')]),
]
SURV = [('« Toujours », « jamais »','Généralise à outrance, invite à se défendre plutôt qu’à s’ajuster','Nommer le fait précis, daté'),
 ('« Il faut que vous… » (répété)','Sonne comme une injonction, ferme le dialogue','« J’ai besoin que… », « Je vous propose de… »'),
 ('« De toute façon… »','Ferme la discussion avant qu’elle ait lieu','Poser une question ouverte'),
 ('« Ce n’est pas compliqué »','Minimise ce que l’autre vit, même sans le vouloir','Décrire l’action attendue, sans commentaire sur sa difficulté'),
 ('« On verra »','Flou, laisse l’autre dans l’incertitude','Donner une échéance, même approximative')]

def bloc_ff(titre, gauche, lignes):
    rows = ''.join(f'<tr><td class="ferme">{e(a)}</td><td>{e(b)}</td></tr>' for a, b in lignes)
    return f'<section class="ff"><h2>{e(titre)}</h2><table class="ff-tab"><thead><tr><th>{e(gauche)}</th><th>Ça ouvre</th></tr></thead><tbody>{rows}</tbody></table></section>'

def fiche_06():
    f = F6
    p1 = f'''<div class="page">{entete(f, 'Fiche de référence')}
 <h1>{e(f['titre'])}</h1><p class="sous-titre">Fiche de référence · avant un échange sensible</p><div class="accent"></div>
 <section><p class="label">Comment l’utiliser</p><p class="intro">Avant un échange sensible, un coup d’œil suffit : repérer si la formulation prévue appartient à la colonne de gauche, et si oui, piocher l’équivalent à droite.</p></section>
 {''.join(bloc_ff(*b) for b in BLOCS1)}{pied(1).replace(PIED, 'Manager ses collaborateurs en tant qu’élu · fiche mobilisable dans le mandat')}</div>'''
    rows = ''.join(f'<tr><td class="ferme">{e(a)}</td><td class="gris">{e(b)}</td><td>{e(c)}</td></tr>' for a, b, c in SURV)
    p2 = f'''<div class="page">{entete(f, 'Des formulations à garder à portée de main')}
 <div class="premiere"></div>{''.join(bloc_ff(*b) for b in BLOCS2)}
 <section class="ff"><h2>Mots et tournures à surveiller, en général</h2><table class="ff-tab trois"><thead><tr><th>À bannir ou limiter</th><th>Pourquoi</th><th>À privilégier</th></tr></thead><tbody>{rows}</tbody></table></section>
 <div class="pousse"></div>{pied(2).replace(PIED, 'Manager ses collaborateurs en tant qu’élu · fiche mobilisable dans le mandat')}</div>'''
    return doc(f['titre'] + ' — fiche de référence', p1 + p2)

for f in FICHES:
    open(os.path.join(OUT, f['fichier'] + '.html'), 'w', encoding='utf8').write(fiche_standard(f))
open(os.path.join(OUT, F6['fichier'] + '.html'), 'w', encoding='utf8').write(fiche_06())
print('6 fiches HTML générées dans', OUT)
