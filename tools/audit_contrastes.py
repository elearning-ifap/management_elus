"""Audit des contrastes (WCAG AA) sur tous les écrans, accordéons ouverts. Aucune ligne affichée = conforme.
Usage : python tools/audit_contrastes.py [chemin/vers/index.html]
"""
import asyncio,os,sys,json
from playwright.async_api import async_playwright
JS=r"""(pid)=>{
function parse(c){const m=c.match(/rgba?\(([^)]+)\)/);if(!m)return null;const v=m[1].split(',').map(x=>parseFloat(x));return {r:v[0],g:v[1],b:v[2],a:v.length>3?v[3]:1}}
function lum(c){const f=x=>{x/=255;return x<=0.03928?x/12.92:Math.pow((x+0.055)/1.055,2.4)};return 0.2126*f(c.r)+0.7152*f(c.g)+0.0722*f(c.b)}
function bg(el){let layers=[];while(el){const cs=getComputedStyle(el);if(cs.backgroundImage&&cs.backgroundImage!=='none'&&!cs.backgroundImage.includes('url'))return {grad:true};const c=parse(cs.backgroundColor);if(c&&c.a>0){layers.push(c);if(c.a>=0.99)break}el=el.parentElement}
 let out={r:255,g:255,b:255};for(let i=layers.length-1;i>=0;i--){const c=layers[i];out={r:c.r*c.a+out.r*(1-c.a),g:c.g*c.a+out.g*(1-c.a),b:c.b*c.a+out.b*(1-c.a)}}return out}
const res=[];const p=document.getElementById(pid);const w=document.createTreeWalker(p,NodeFilter.SHOW_TEXT);const seen=new Set();
while(w.nextNode()){const n=w.currentNode;if(n.textContent.trim().length<2)continue;const e=n.parentElement;if(seen.has(e))continue;seen.add(e);
 const r=e.getBoundingClientRect();if(!r.width||!r.height)continue;const cs=getComputedStyle(e);if(cs.visibility==='hidden'||parseFloat(cs.opacity)<0.1)continue;
 if(e.closest('.mgt-6r-sr'))continue;
 const fg=parse(cs.color);const b=bg(e);if(!fg||b.grad)continue;
 const L1=lum(fg),L2=lum(b);const ratio=(Math.max(L1,L2)+0.05)/(Math.min(L1,L2)+0.05);
 const fs=parseFloat(cs.fontSize),bold=parseInt(cs.fontWeight)>=700;const large=fs>=24||(fs>=18.66&&bold);
 if(ratio<(large?3:4.5))res.push([ratio.toFixed(2),fs,cs.color,`rgb(${Math.round(b.r)},${Math.round(b.g)},${Math.round(b.b)})`,e.tagName+'.'+String(e.className).slice(0,40),n.textContent.trim().slice(0,40)])}
return res}"""
async def m(path):
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1440,'height':900})
    await pg.goto('file://'+path); await pg.wait_for_timeout(1000); allr={}
    await pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)")
    for pid in await pg.eval_on_selector_all('section.panel','e=>e.map(x=>x.id)'):
      await pg.evaluate(f"GABARIT.aller('{pid}')"); await pg.wait_for_timeout(60)
      await pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)")
      for r in await pg.evaluate(JS,pid):
        k=(r[4],r[2],r[3]); allr.setdefault(k,[r[0],r[1],r[5],set()]); allr[k][3].add(pid)
    await b.close()
  for k,v in sorted(allr.items(),key=lambda x:float(x[1][0])): print(v[0],v[1],k[0],k[1],'sur',k[2],'|',v[2],'|',len(v[3]),sorted(v[3])[:3])
import pathlib
asyncio.run(m(str(pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'src/index.html').resolve())))
