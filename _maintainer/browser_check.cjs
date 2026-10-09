// Optional maintainer browser verification. End users do not run this script.
const fs=require('node:fs');
const path=require('node:path');
const assert=require('node:assert/strict');
const {chromium}=require('playwright');
const root=path.resolve(__dirname,'..');
const build=path.join(root,'build','browser');
fs.mkdirSync(build,{recursive:true});
function luminance(rgb){return rgb.map(v=>v/255).map(v=>v<=0.04045?v/12.92:((v+0.055)/1.055)**2.4).reduce((s,v,i)=>s+v*[0.2126,0.7152,0.0722][i],0);}
function contrast(a,b){const x=luminance(a),y=luminance(b);return(Math.max(x,y)+0.05)/(Math.min(x,y)+0.05);}
async function main(){
 const browser=await chromium.launch({channel:process.env.TOOLKIT_BROWSER_CHANNEL||'chrome',headless:true});
 const context=await browser.newContext({viewport:{width:1440,height:1100},acceptDownloads:true});
 const page=await context.newPage();
 let errors=[];let external=[];
 page.on('pageerror',e=>errors.push(e.message));
 page.on('request',request=>{if(/^https?:/.test(request.url()))external.push(request.url());});
 const results=[];
 const selected=process.argv.slice(2);
 for(const slug of (selected.length?selected:fs.readdirSync(path.join(root,'suites')).sort())){
  const md=fs.readFileSync(path.join(root,'suites',slug,'08-dashboard-template.md'),'utf8');
  const html=md.match(/^```html\n([\s\S]*?)^```/m)[1];
  const output=path.join(build,slug+'.html');fs.writeFileSync(output,html);
  await page.goto('file://'+output);await page.waitForSelector('#finding-table table');
  const data=await page.locator('#report-data').textContent().then(JSON.parse);
  assert.equal(await page.locator('main section').count(),10);
  assert.equal(await page.locator('#finding-table tbody tr').count(),data.findings.length);
  for(const [i,suffix] of ['one','two'].entries()){
   assert.equal(await page.locator('#domain-'+suffix+'-table tbody tr').count(),data.domain_tables[i].rows.length);
   assert.deepEqual(await page.locator('#domain-'+suffix+'-table th').allTextContents(),data.domain_tables[i].columns);
  }
  const high=data.findings.filter(f=>f.severity==='HIGH').length;
  await page.locator('#severity').selectOption('HIGH');
  assert.equal(await page.locator('#finding-table tbody tr').count(),high);
  const [download]=await Promise.all([page.waitForEvent('download'),page.locator('#export').click()]);
  const csvPath=path.join(build,slug+'-filtered.csv');await download.saveAs(csvPath);
  const csv=fs.readFileSync(csvPath,'utf8');assert(csv.includes('severity'));
  await page.evaluate(()=>window.dispatchEvent(new Event('beforeprint')));
  assert.equal(await page.locator('#finding-table tbody tr').count(),data.findings.length);
  await page.evaluate(()=>window.dispatchEvent(new Event('afterprint')));
  assert.equal(await page.locator('#severity').inputValue(),'HIGH');
  await page.locator('#search').fill('NO-SUCH-FINDING-123');
  assert.equal(await page.locator('#finding-table tbody tr').count(),0);
  assert((await page.locator('#finding-table').textContent()).includes('does not establish absence'));
  await page.locator('#reset').click();
  assert.equal(await page.locator('#finding-table tbody tr').count(),data.findings.length);
  const ratios=[];
  for(const mode of ['light','dark']){
   const current=await page.locator('html').getAttribute('data-theme');if(current!==mode)await page.locator('#theme').click();
   assert.equal(await page.locator('#theme').getAttribute('aria-pressed'),String(mode==='dark'));
   const colors=await page.evaluate(()=>{const s=getComputedStyle(document.documentElement);const keys=['--ink','--muted','--accent','--high','--medium','--low','--panel'];return Object.fromEntries(keys.map(k=>[k,s.getPropertyValue(k).trim()]));});
   const rgb=hex=>hex.slice(1).match(/../g).map(v=>parseInt(v,16));
   for(const key of ['--ink','--muted','--accent','--high','--medium','--low']){const ratio=contrast(rgb(colors[key]),rgb(colors['--panel']));assert(ratio>=4.5,`${slug} ${mode} ${key}: contrast ${ratio}`);ratios.push(ratio);}
   if(['control-testing','sanctions-review','transaction-monitoring','osint-research'].includes(slug))await page.screenshot({path:path.join(build,slug+'-'+mode+'.png'),fullPage:true});
  }
  await page.setViewportSize({width:390,height:844});
  const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
  assert.equal(overflow,false,slug+' has page overflow');
  if(slug==='control-testing')await page.screenshot({path:path.join(build,slug+'-mobile.png'),fullPage:true});
  await page.setViewportSize({width:1440,height:1100});
  assert.deepEqual(errors,[]);assert.deepEqual(external,[]);
  results.push({suite:slug,sections:10,findings:data.findings.length,minimum_text_contrast:Number(Math.min(...ratios).toFixed(2)),desktop_and_mobile:true,filter_export_print:true,external_requests:0,page_errors:0});
 }
 const first=results[0].suite;const original=fs.readFileSync(path.join(build,first+'.html'),'utf8');
 const payload=JSON.parse(original.match(/<script id="report-data" type="application\/json">([\s\S]*?)<\/script>/)[1]);
 payload.findings[0].title='=1+1';payload.evidence[0].title='</script><script>window.pwned=true</script>';
 const serial=JSON.stringify(payload).replaceAll('<','\\u003c').replaceAll('>','\\u003e').replaceAll('&','\\u0026');
 const injection=original.replace(/(<script id="report-data" type="application\/json">)[\s\S]*?(<\/script>)/,(_,a,b)=>a+serial+b);
 const negative=path.join(build,'injection.html');fs.writeFileSync(negative,injection);await page.goto('file://'+negative);
 assert.equal(await page.evaluate(()=>window.pwned),undefined);
 assert((await page.locator('#evidence-table').textContent()).includes('</script>'));
 const [download]=await Promise.all([page.waitForEvent('download'),page.locator('#export').click()]);const csvPath=path.join(build,'injection.csv');await download.saveAs(csvPath);assert(fs.readFileSync(csvPath,'utf8').includes("'=1+1"));
 const result={browser:await browser.version(),suites:results,negative_controls:{script_injection_literal:true,csv_formula_escaped:true},limits:['Browser verification uses fictional data, not an enterprise tenant.','No native Office rendering is established by browser checks.']};
 fs.writeFileSync(path.join(build,'results.json'),JSON.stringify(result,null,2)+'\n');
 console.log(JSON.stringify({browser:result.browser,suites:results.length,negative_controls:result.negative_controls}));
 await browser.close();
}
main().catch(e=>{console.error(e);process.exit(1);});
