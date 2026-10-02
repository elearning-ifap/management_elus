"""Parcourt tout le module au bouton « Suivant » et signale les erreurs JavaScript.
Usage : python tools/recette_parcours.py [chemin/vers/index.html]
"""
import asyncio,os
from playwright.async_api import async_playwright
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1180,'height':820},has_touch=True)
    errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    import sys,pathlib
    await pg.goto(pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'src/index.html').resolve().as_uri()); await pg.wait_for_timeout(700)
    seq=[]
    for i in range(80):
      cur=await pg.evaluate("document.querySelector('.panel.actif').id"); seq.append(cur)
      dis=await pg.evaluate("document.getElementById('g-btn-suiv').disabled")
      if dis: break
      await pg.evaluate("document.getElementById('g-btn-suiv').click()"); await pg.wait_for_timeout(120)
    print(len(seq),'écrans parcourus au bouton Suivant ; erreurs',errs); print(' > '.join(seq[3:20]))
    await b.close()
asyncio.run(m())
