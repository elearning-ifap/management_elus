"""Lot AM — retours Marie-Noëlle du 03/11 et réunion du 09/11.
Idempotent : sort sans rien faire si le marqueur ux18i-lot-am est déjà présent.
Usage : python3 patch_am.py chemin/index.html
"""
import re, sys
from bs4 import BeautifulSoup

path = sys.argv[1]
h = open(path, encoding='utf8').read()
if 'ux18i-lot-am' in h:
    print('Lot AM déjà appliqué'); sys.exit(0)

def bloc_details(html, panel_id):
    """Renvoie (début, fin) du <details class="mgt-m-plus"> unique de l'écran."""
    a = html.find(f'id="{panel_id}"'); assert a > 0, panel_id
    fin_panel = html.find('</section>\n', a)
    # le panel peut contenir des <section> internes : on cherche la fin réelle via le prochain panel
    nxt = html.find('<section class="panel', a + 10)
    zone_fin = nxt if nxt > 0 else len(html)
    d = html.find('<details class="mgt-m-plus">', a)
    assert a < d < zone_fin, f'details absent : {panel_id}'
    assert html.find('<details class="mgt-m-plus">', d + 10) > zone_fin or html.find('<details class="mgt-m-plus">', d + 10) < 0, f'plusieurs details : {panel_id}'
    # fin du details en comptant l'imbrication
    i, prof = d, 0
    for m in re.finditer(r'<(/?)details\b', html[d:]):
        prof += -1 if m.group(1) else 1
        if prof == 0:
            e = d + m.start() + len('</details>')
            return d, e
    raise RuntimeError(panel_id)

# 1. Suppression des 7 accordéons « Pour aller plus loin » validés (MN 03/11)
for pid in ['mod-s2-04a', 'mod-s2-04a2', 'mod-s4-04', 'mod-s4-05c', 'mod-s4-fin', 'mod-s5-05c', 'mod-s5-fin']:
    d, e = bloc_details(h, pid)
    h = h[:d] + h[e:]

# 2. S3 10/10 : accordéon supprimé, son introduction remonte devant les 4 réflexes
d, e = bloc_details(h, 'mod-s3-fin')
corps = h[d:e]
paras = re.findall(r'<p class="mgt-recap-intro">.*?</p>', corps)
assert len(paras) == 2
h = h[:d] + h[e:]
a = h.find('id="mod-s3-fin"')
ul = h.find('<ul>', a)
assert ul > 0 and ul < h.find('<section class="panel', a + 10)
h = h[:ul] + ''.join(paras) + h[ul:]

# 3. S5 7/11 : la grille ne sert plus d'accordéon, les cas sortent dans le composant
d, e = bloc_details(h, 'mod-s5-02b')
corps = h[d:e]
cas = re.findall(r'<div class="mgt-cas-mnl".*?<div id="mgt-s5-cas-e\d"></div></div>', corps)
assert len(cas) == 4
consigne = ('<div class="g-consigne mgt-sit-consigne" data-source-mnl="MNL-0706 MNL-0707 MNL-0708 MNL-0709 MNL-0710 MNL-0711">'
            '<p>À partir d’ici, vous évaluez une réponse déjà donnée : choisissez ce qu’elle produit.</p></div>')
nouveaux = []
for k, c in enumerate(cas, 1):
    c = c.replace(f'<h2>Étude de cas {k}</h2>', '<h2>Évaluer une réponse</h2>' + (consigne if k == 1 else ''))
    c = c.replace('<strong>À quel niveau se situe cette réponse ?</strong>', '<strong>Que produit cette réponse ?</strong>')
    nouveaux.append(c)
h = h[:d] + ''.join(nouveaux) + h[e:]

# Situation 2 : l'expression « même côté de la table » n'est plus introduite avant (S5 4/11 supprimé)
old_t = '<h2>À vous de jouer — rester du même côté de la table</h2>'
old_q = '<strong>Quelle relance reste du bon côté de la table ?</strong>'
assert h.count(old_t) == 1 and h.count(old_q) == 1
h = h.replace(old_t, '<h2>À vous de jouer — recréer le dialogue</h2>')
h = h.replace(old_q, '<strong>Quelle relance aide à recréer le dialogue ?</strong>')

# Réponses explicites : « Niveau n » remplacé par ce que la réponse produit (grille MNL-0708 à 0711)
NIV = {
    '1': ("Ça calme dans l’instant", "la tension redescend momentanément, mais la cause reste entière — le signal reviendra."),
    '2': ("Ça règle le point précis", "le sujet de friction identifié est traité, la tension retombe durablement sur ce point."),
    '3': ("Ça restaure la coopération", "au-delà du point précis, la capacité des deux personnes à travailler ensemble est reconstruite."),
}
for k in range(1, 5):
    a = h.find(f"choixUnique('mgt-s5-cas-e{k}'"); e = h.find('\n', a)
    seg = h[a:e]
    for n, (lib, desc) in NIV.items():
        seg = seg.replace(f'"texte": "Niveau {n}"', f'"texte": "{lib}"')
        seg = seg.replace(f'"Le repère retenu : « Niveau {n} »."', f'"Le repère retenu : « {lib} » : {desc}"')
    assert 'Niveau' not in seg, k
    h = h[:a] + seg + h[e:]

# 4. Navigation option A : un seul bouton d'avancée sur les 5 écrans « Que feriez-vous ? »
css = '''<style id="ux18i-lot-am-css">
/* Lot AM — un seul bouton d'avancée : le bouton « Suivant » du bas parcourt les situations. */
.mgt-sit .mgt-sit-suiv{display:none!important}
.mgt-sit-nav{justify-content:flex-start}
.mgt-sit-nav:has(.mgt-sit-prec:disabled){display:none}
.mgt-sit-consigne{margin:0 0 14px}
</style>
'''
js = '''<script id="ux18i-lot-am-js">
/* Lot AM — option A validée par Marc et Marie-Noëlle (09/11) : sur les écrans « Que feriez-vous ? »,
   le bouton « Suivant » du bas avance de situation en situation (« Situation suivante (n/N) → »),
   puis redevient « Suivant → » sur la dernière situation et passe à l'écran suivant. */
(function(){
 var LIB='Suivant →';
 function panelActif(){return document.querySelector('.panel.actif')}
 function etat(){var p=panelActif();if(!p)return null;var box=p.querySelector('.mgt-sit');if(!box)return null;
  var sv=box.querySelector('.mgt-sit-suiv'),m=(box.querySelector('.mgt-sit-compteur')||{}).textContent;
  m=m&&m.match(/Situation (\\d+) sur (\\d+)/);if(!sv||!m)return null;
  return {sv:sv,n:+m[1],N:+m[2],reste:!sv.hidden&&+m[1]<+m[2]}}
 function maj(){var b=document.getElementById('g-btn-suiv');if(!b)return;var e=etat();
  if(e&&e.reste){var t='Situation suivante ('+(e.n+1)+'/'+e.N+') →';if(b.textContent!==t)b.textContent=t;b.setAttribute('aria-label','Situation suivante, '+(e.n+1)+' sur '+e.N);b.classList.add('mgt-sit-avance')}
  else{if(b.textContent!==LIB)b.textContent=LIB;b.removeAttribute('aria-label');b.classList.remove('mgt-sit-avance')}}
 document.addEventListener('click',function(ev){
  if(!ev.target.closest||!ev.target.closest('#g-btn-suiv'))return;
  var e=etat();if(!e||!e.reste)return;
  ev.preventDefault();ev.stopImmediatePropagation();e.sv.click();maj()},true);
 function init(){setTimeout(function(){
  var obs=new MutationObserver(maj);
  document.querySelectorAll('.panel').forEach(function(p){obs.observe(p,{attributes:true,attributeFilter:['class']})});
  document.querySelectorAll('.mgt-sit-compteur').forEach(function(c){obs.observe(c,{childList:true,characterData:true,subtree:true})});
  maj()},200)}
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
'''
assert h.rstrip().endswith('</html>') and h.find('</head>') < h.find('<body')
h = h.replace('</head>', css + '</head>', 1)
k = h.rfind('</body>')
h = h[:k] + js + h[k:]

open(path, 'w', encoding='utf8').write(h)
print('Lot AM appliqué')
