"""Recette de complétion SCORM du module (Playwright, Chromium).

Usage : python tools/recette_completion.py [chemin/vers/index.html]
Prérequis : pip install playwright && playwright install chromium

Deux scénarios, avec un faux LMS SCORM 1.2 injecté dans la page :
1. l'apprenant ne clique que sur « Suivant » : la clôture doit lister les étapes restantes ;
2. l'apprenant fait tout (positionnements, défis) : statut attendu « completed », progression 100 %.
"""
import asyncio,os,json
from playwright.async_api import async_playwright
import sys,pathlib
U=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'src/index.html').resolve().as_uri()
STUB="""window.__S={};window.API={LMSInitialize:()=> 'true',LMSFinish:()=> 'true',LMSGetValue:k=>window.__S[k]||'',LMSSetValue:(k,v)=>{window.__S[k]=String(v);return 'true'},LMSCommit:()=> 'true',LMSGetLastError:()=> '0',LMSGetErrorString:()=> '',LMSGetDiagnostic:()=> ''};"""
async def page(b):
  ctx=await b.new_context(viewport={'width':1440,'height':900}); await ctx.add_init_script(STUB); pg=await ctx.new_page(); errs=[]
  pg.on('pageerror',lambda e:errs.append(str(e))); await pg.goto(U); await pg.wait_for_timeout(1200); return pg,errs
async def pos(pg,pid,btn_ids):
  # répond à toutes les affirmations visibles puis avance, en boucle
  for _ in range(8):
    await pg.evaluate(f"""document.querySelectorAll('#{pid} .mgt-pos-choix, #{pid} .g-echelle').forEach(g=>{{const b=[...g.querySelectorAll('button')].find(x=>x.offsetParent);if(b&&!g.querySelector('.on,[aria-pressed=true]'))b.click()}})""")
    await pg.evaluate(f"document.querySelectorAll('#{pid} input[type=range]').forEach(r=>{{if(r.offsetParent){{r.value=6;r.dispatchEvent(new Event('input',{{bubbles:true}}))}}}})")
    await pg.wait_for_timeout(120)
    clicked=await pg.evaluate(f"""(()=>{{const b=[...document.querySelectorAll('#{pid} [data-mgt-pos-next]')].find(x=>x.offsetParent&&!x.disabled)||[...document.querySelectorAll('#{pid} button')].find(x=>x.offsetParent&&!x.disabled&&/^continuer : relire/i.test(x.innerText));if(b){{b.click();return b.innerText}}return null}})()""")
    await pg.wait_for_timeout(200)
    act=await pg.evaluate("document.querySelector('.panel.actif').id")
    if act!=pid or not clicked: return act
  return await pg.evaluate("document.querySelector('.panel.actif').id")
async def quiz(pg,nav):
  for _ in range(12):
    ok=await pg.evaluate(f"""(()=>{{const z=document.getElementById('{nav}-zone');if(!z)return false;const o=[...z.querySelectorAll('.opt')].find(x=>x.offsetParent&&!x.disabled);if(o)o.click();return !!o}})()"""); await pg.wait_for_timeout(100)
    await pg.evaluate(f"""(()=>{{const b=document.querySelector('#{nav}-zone [data-quiz-suite],#{nav}-zone [data-quiz-fin]');if(b&&b.offsetParent)b.click()}})()"""); await pg.wait_for_timeout(150)
    if not ok: break
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    # 1. Suivant seul
    pg,errs=await page(b)
    for _ in range(70):
      if await pg.evaluate("document.querySelector('.panel.actif').id")=='g-fin': break
      await pg.evaluate("document.getElementById('g-btn-suiv').click()"); await pg.wait_for_timeout(120)
    await pg.wait_for_timeout(300)
    print('[Suivant seul] progression',await pg.evaluate("document.getElementById('g-menu-pct').textContent"),'| reste :',await pg.evaluate("window.mgtResteAFaire()"))
    print('  bloc reste affiché :',await pg.evaluate("(document.querySelector('#g-fin .mgt-reste h2')||{}).textContent"))
    print('  « > » parasites :',await pg.evaluate("[...document.getElementById('g-app').childNodes].filter(n=>n.nodeType===3&&n.textContent.trim()).length"),'| erreurs',errs)
    await pg.screenshot(path='p_fin_reste.png')
    # 2. Apprenant complet
    pg,errs=await page(b)
    for _ in range(90):
      pid=await pg.evaluate("document.querySelector('.panel.actif').id")
      if pid in('g-pre','g-post'):
        nxt=await pos(pg,pid,None)
        if nxt!=pid: continue
      if pid in('mod-s1-05','mod-s2-05','mod-s3-06','mod-s4-07','mod-s5-07'):
        await quiz(pg,pid.replace('mod-',''))
        await pg.wait_for_timeout(200)
        pid2=await pg.evaluate("document.querySelector('.panel.actif').id")
        if pid2!=pid: continue
      if pid=='g-fin' or pid=='g-credits': break
      await pg.evaluate("document.getElementById('g-btn-suiv').click()"); await pg.wait_for_timeout(120)
    st=await pg.evaluate("window.__S['cmi.core.lesson_status']||''")
    print('[Apprenant complet] statut SCORM :',st,'| progression',await pg.evaluate("document.getElementById('g-menu-pct').textContent"),'| reste',await pg.evaluate("window.mgtResteAFaire()"),'| erreurs',errs)
    await b.close()
asyncio.run(m())
