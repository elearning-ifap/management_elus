"""Lot AR — interface aérée, option B validée par Marc le 10/11 : menu en panneau.
Ne s'applique qu'aux écrans larges (menu affiché en colonne, > 1100 px) ; iPad et mobile inchangés.
Usage : python3 tools/patch_lot_ar.py src/index.html
"""
import sys
path = sys.argv[1]
h = open(path, encoding='utf8').read()
if 'ux18i-lot-ar-css' in h:
    print('Lot AR déjà appliqué'); sys.exit(0)
css = '''<style id="ux18i-lot-ar-css">
/* Lot AR — menu en panneau, colonne de contenu centrée, plus d'air (écrans larges uniquement) */
@media (min-width:1101px){
 .g-page{padding-top:40px}
 .g-layout{grid-template-columns:240px minmax(0,880px);column-gap:64px;justify-content:center}
 .g-menu{background:#fff;border-radius:16px;box-shadow:0 1px 3px rgba(47,67,84,.08),0 0 0 1px rgba(47,67,84,.04);
   padding:18px 14px 18px 4px;top:96px;max-height:calc(100vh - 200px);max-height:calc(100dvh - 200px)}
 .g-menu-head{margin:0 4px 15px 14px}
 .g-nav-bas-inner{max-width:1184px;width:calc(100% - 56px);padding:9px 0 9px 304px;box-sizing:border-box}
 .mgt-entete{margin-bottom:36px}
 .panel h1{margin-bottom:18px}
}
</style>
'''
k = h.find('</head>'); assert 0 < k < h.find('<body')
h = h[:k] + css + h[k:]
open(path, 'w', encoding='utf8').write(h)
print('Lot AR appliqué')
