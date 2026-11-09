const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage();const dir=process.argv[2];
for(const f of fs.readdirSync(dir).filter(x=>x.endsWith('.html'))){
 await p.goto('file://'+path.resolve(dir,f));await p.waitForTimeout(200);
 // contrôle débordement : chaque .page doit tenir dans sa hauteur
 const over=await p.evaluate(()=>[...document.querySelectorAll('.page')].map(pg=>pg.scrollHeight-pg.clientHeight));
 await p.pdf({path:path.resolve(dir,f.replace('.html','.pdf')),format:'A4',printBackground:true,preferCSSPageSize:true});
 console.log(f,'débordement px par page:',over.join(','));}
await b.close()})();
