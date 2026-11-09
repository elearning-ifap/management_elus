"""Lot AQ — corrections de l'audit global du 09/11, validées par Marc le 10/11.
Idempotent (marqueur ux18i-lot-aq). Usage : python3 tools/patch_lot_aq.py src/index.html
"""
import re, sys
path = sys.argv[1]
h = open(path, encoding='utf8').read()
if 'ux18i-lot-aq' in h:
    print('Lot AQ déjà appliqué'); sys.exit(0)

def rep(old, new, n=1):
    global h
    c = h.count(old)
    assert c == n, f'{c} occurrence(s) au lieu de {n} : {old[:70]}'
    h = h.replace(old, new)

# 1. S3 3/10 « Se faire vraiment entendre » : intertitres remis en place, titre en double retiré
rep('<h4>Les quatre réflexes en détail</h4><ul>', '<ul>')
rep('<h3>Cinq réflexes qui font la différence</h3>\n', '')
rep('</ul><ol>\n<li><strong>Dire ce qu\'on veut', '</ul>\n<h3>Cinq réflexes qui font la différence</h3><ol>\n<li><strong>Dire ce qu\'on veut')
rep('</a></div></div><h3>Se faire vraiment entendre</h3><div class="mgt-fusion" data-fusion-de="mod-s3-03">',
    '</a></div></div><div class="mgt-fusion" data-fusion-de="mod-s3-03">')

# 2. Défi 8, question 3 : plus de « Niveau 1 » ni de « grille à 3 niveaux »
rep('"question": "Une réponse de \\"Niveau 1\\" dans la grille à 3 niveaux de cette séquence signifie que :"',
    '"question": "Une réponse qui « calme dans l’instant » signifie que :"')
rep('"texte_feedback": "Niveau 1 — ça calme dans l\'instant : la tension redescend momentanément, mais la cause reste entière."',
    '"texte_feedback": "Ça calme dans l’instant : la tension redescend momentanément, mais la cause reste entière."')

# 3. S4 6/11, situation 1 : niveaux d'autonomie nommés, sans numéro
rep('Niveau 4 — Autonome, pour', 'Autonome, pour')
rep('Niveau 3 — Informé, comme', 'Informé, comme')
rep('Niveau 1 ou 2 — Cadré ou Proposé, le temps', 'Cadré ou Proposé, le temps', 3)

# 4. Défis 3 et 4, question 1 : reste de libellé « Situation 3 — »
rep('"question": "Situation 3 — Vous constatez', '"question": "Vous constatez')

# 5. Simulateur S5 : expression plus introduite en amont
rep('permet de rester du même côté de la table.", "accroche"', 'permet d’aborder le problème ensemble, sans se poser en juge.", "accroche"')

# 8. S3 : quatre points d'une attente claire (alignés sur la fiche 03)
rep('data-titre="S3 · Les six points d\'une attente claire"', 'data-titre="S3 · Les quatre points d’une attente claire"')
rep('<h1>Les six points d\'une attente claire</h1>', '<h1>Les quatre points d’une attente claire</h1>')
a = h.find("cartesRevelation('mgt-s3-04-zone',[")
b = h.find("],{panelId:'mod-s3-04'});", a)
assert a > 0 and b > a
cartes = '''cartesRevelation('mgt-s3-04-zone',[
 {titre:'Donner le cap',texte:"Le résultat et son usage : « Une recommandation chiffrée sur deux pages », pas « quelque chose d'utile », pour appuyer un vote en commission plénière — le ton et le niveau de détail en découlent."},
 {titre:'Situer la priorité',texte:"Ce qui compte maintenant et l'échéance réelle : « C'est la priorité de la semaine, pour mardi 17h » plutôt que « quand vous aurez le temps » ou « rapidement »."},
 {titre:"Ouvrir une marge",texte:"Le plan et les exemples restent au choix du collaborateur ; vous validez la recommandation finale."},
 {titre:'Vérifier et suivre',texte:"Faire reformuler l'essentiel, puis un point convenu à l'avance, par exemple lundi en fin de journée."}
'''
h = h[:a] + cartes + h[b:]
rep("Ce sont les six points d'une attente claire, en germe.", "Ce sont les quatre points d’une attente claire, en germe.")
rep('les quatre repères d’une attente claire, et les formulations', 'les quatre points d’une attente claire, et les formulations')

# 9. Menu « Parcours » : titres alignés sur les titres des écrans (hors ouvertures, résultats de défi et écrans généraux)
def norm(t): return re.sub(r'\s+', ' ', t.replace("'", '’')).strip()
ids = re.findall(r'<section class="panel[^"]*"[^>]*\bid="(mod-s\d-[^"]+)"', h)
for pid in ids:
    if pid.endswith('-00'): continue
    a = h.find(f'id="{pid}"'); a = h.rfind('<section', 0, a); z = h.find('<section class="panel', a + 10)
    tag = h[a:h.find('>', a)]
    dt = re.search(r'data-titre="(S\d) · ([^"]*)"', tag)
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', h[a:z], re.S)
    if not dt or not h1: continue
    t1 = norm(re.sub('<[^>]+>', '', h1.group(1)))
    if norm(dt.group(2)) == t1: continue
    old = dt.group(0)
    assert h.count(old) == 1, old
    h = h.replace(old, f'data-titre="{dt.group(1)} · {t1}"')
    print('menu :', pid, '|', dt.group(2), '→', t1)

# 10. Ouverture S3 à S5 : l'étape « Je rencontre une situation » reçoit le titre de la situation
rep("if(!pars[k])pars[k]=titre(p)});\n   ol.innerHTML=ETAPES.map(",
    "if(!pars[k])pars[k]=titre(p)});\n   if(!pars[0]&&pars[1]){pars[0]=pars[1];pars[1]='Ma première réaction'}\n   ol.innerHTML=ETAPES.map(")

# 11. S1 « À retenir » : accordéon « Pour aller plus loin » supprimé
a = h.find('id="mod-s1-fin"'); z = h.find('<section class="panel', a + 10)
d = h.find('<details class="mgt-m-plus">', a); assert a < d < z
i, prof = d, 0
for m in re.finditer(r'<(/?)details\b', h[d:]):
    prof += -1 if m.group(1) else 1
    if prof == 0:
        e = d + m.start() + len('</details>'); break
h = h[:d] + h[e:]

h = h.replace('</head>', '<meta name="ux18i-lot" content="ux18i-lot-aq">\n</head>', 1)
open(path, 'w', encoding='utf8').write(h)
print('Lot AQ appliqué')

# 8 bis. Quatre cartes : grille 2 × 2 (au lieu de 3 + 1)
h = open(path, encoding='utf8').read()
if 'ux18i-lot-aq-css' not in h:
    css = ('<style id="ux18i-lot-aq-css">#mgt-s3-04-zone{flex-wrap:wrap}#mgt-s3-04-zone>.mgt-card{flex:1 1 calc(50% - 8px)!important;max-width:calc(50% - 8px)!important}@media (max-width:640px){#mgt-s3-04-zone>.mgt-card{flex-basis:100%!important;max-width:100%!important}}</style>\n')
    h = h.replace('</head>', css + '</head>', 1)
    open(path, 'w', encoding='utf8').write(h)
    print('Grille 2 × 2 ajoutée')
