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
function parseCsv(text){
 const rows=[];let row=[],field='',quoted=false;const input=text.replace(/^\uFEFF/,'');
 for(let i=0;i<input.length;i++){const c=input[i];
  if(c==='"'){if(quoted&&input[i+1]==='"'){field+='"';i++;}else quoted=!quoted;}
  else if(c===','&&!quoted){row.push(field);field='';}
  else if((c==='\r'||c==='\n')&&!quoted){if(c==='\r'&&input[i+1]==='\n')i++;row.push(field);rows.push(row);row=[];field='';}
  else field+=c;
 }
 assert.equal(quoted,false);if(field.length||row.length){row.push(field);rows.push(row);}return rows;
}
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
  assert.equal(await page.evaluate(()=>formatted(1.2345,'0.0000')),'1.2345');
  assert.equal(await page.evaluate(()=>formatted(1.2,'0.0000')),'1.2000');
  assert.equal(await page.locator('main section').count(),8+data.domain_tables.length);
  assert.equal(await page.locator('#finding-table tbody tr').count(),data.findings.length);
  for(const [i,t] of data.domain_tables.entries()){
   const host='#domain-'+i+'-table';
   assert.equal(await page.locator(host+' tbody tr').count(),t.rows.length);
   assert.deepEqual(await page.locator(host+' th').allTextContents(),t.columns);
   const expected=await page.evaluate(({rows,columns,formats})=>rows.map(row=>row.map((value,j)=>formatted(value,(formats||{})[columns[j]]))),t);
   const rendered=await page.locator(host+' tbody tr').evaluateAll(rows=>rows.map(row=>[...row.cells].map(cell=>cell.textContent)));
   assert.deepEqual(rendered,expected,slug+' / '+t.name+' values');
   assert.equal(await page.locator('nav a[href="#domain-'+i+'"]').count(),1);
   if(t.column_contracts){assert.equal(await page.locator('#domain-'+i+' dl dt').count(),t.columns.length);}
  }
  for(const [i,paragraphs] of data.report_narrative.entries()){
   assert.deepEqual(await page.locator('[data-narrative-section="'+i+'"] p').allTextContents(),paragraphs);
  }
  const [caseDownload]=await Promise.all([page.waitForEvent('download'),page.locator('#case-export').click()]);
  const casePath=path.join(build,slug+'-complete-case.json');await caseDownload.saveAs(casePath);
  assert.deepEqual(JSON.parse(fs.readFileSync(casePath,'utf8')),data);
  const high=data.findings.filter(f=>f.severity==='HIGH').length;
  await page.locator('#severity').selectOption('HIGH');
  assert.equal(await page.locator('#finding-table tbody tr').count(),high);
  const [download]=await Promise.all([page.waitForEvent('download'),page.locator('#export').click()]);
  const csvPath=path.join(build,slug+'-filtered.csv');await download.saveAs(csvPath);
  const csv=fs.readFileSync(csvPath,'utf8');const csvRows=parseCsv(csv);
  assert.deepEqual(csvRows[0],['id','title','severity','confidence','claim_class','evidence_ids','detail','recommendation']);
  assert.deepEqual(csvRows.slice(1).map(r=>r[0]),data.findings.filter(f=>f.severity==='HIGH').map(f=>f.id));
  assert(csvRows.slice(1).every(r=>r[2]==='HIGH'));
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
  results.push({suite:slug,sections:8+data.domain_tables.length,domain_tables:data.domain_tables.length,domain_rows:data.domain_tables.reduce((n,t)=>n+t.rows.length,0),complete_case_export:true,findings:data.findings.length,minimum_text_contrast:Number(Math.min(...ratios).toFixed(2)),desktop_and_mobile:true,filter_export_print:true,external_requests:0,page_errors:0});
 }
 const deep=results.find(result=>result.domain_tables>2);
 let domainContractsTested=false;
 if(deep){
 await page.goto('file://'+path.join(build,deep.suite+'.html'));
 const boundaryChecks=await page.evaluate(()=>{
  const original=JSON.parse(document.getElementById('report-data').textContent);
  const mutate=fn=>{const changed=structuredClone(original);fn(changed);return caseErrors(changed);};
  const typed=original.domain_tables.findIndex(t=>t.column_contracts&&t.rows.length);
  const table=original.domain_tables[typed];
  const enumField=original.domain_tables.flatMap((t,i)=>Object.entries(t.column_contracts||{}).filter(([name,s])=>s.enum&&t.rows.length).map(([name])=>[i,name]))[0];
  const checks={
   wrongType:mutate(d=>{const t=d.domain_tables[typed];const c=t.columns[0];t.rows[0][0]=t.column_contracts[c].type==='text'?42:'invalid';}),
   duplicateKey:mutate(d=>d.domain_tables[typed].rows.push(structuredClone(d.domain_tables[typed].rows[0]))),
   invalidEnum:mutate(d=>{const [i,name]=enumField;d.domain_tables[i].rows[0][d.domain_tables[i].columns.indexOf(name)]='UNDECLARED_STATE';}),
   invalidFindingEvidence:mutate(d=>d.findings[0].evidence_ids=['UNRESOLVED_KEY']),
   invalidMetricFormat:mutate(d=>{d.metrics[0].value=9;d.metrics[0].format={};}),
   excessivePrecision:mutate(d=>{const t=d.domain_tables[typed];t.formats={[t.columns[0]]:'0.'+'0'.repeat(101)};})
  };
  return checks;
 });
 for(const [name,problems] of Object.entries(boundaryChecks))assert(problems.length,name+' was not rejected');
 const deepOriginal=fs.readFileSync(path.join(build,deep.suite+'.html'),'utf8');
 for(const failure of ['duplicate-key','metric-format','format-precision']){
 const blockedData=JSON.parse(deepOriginal.match(/<script id="report-data" type="application\/json">([\s\S]*?)<\/script>/)[1]);
 if(failure==='duplicate-key')blockedData.domain_tables[0].rows.push(structuredClone(blockedData.domain_tables[0].rows[0]));
 else if(failure==='metric-format'){blockedData.metrics[0].value=9;blockedData.metrics[0].format={};}
 else{const t=blockedData.domain_tables[0];t.formats={[t.columns[0]]:'0.'+'0'.repeat(101)};}
 const blockedJson=JSON.stringify(blockedData).replaceAll('<','\\u003c').replaceAll('>','\\u003e').replaceAll('&','\\u0026');
 const blocked=deepOriginal.replace(/(<script id="report-data" type="application\/json">)[\s\S]*?(<\/script>)/,(_,a,b)=>a+blockedJson+b);
 const blockedPath=path.join(build,'invalid-'+failure+'.html');fs.writeFileSync(blockedPath,blocked);await page.goto('file://'+blockedPath);
 assert((await page.locator('#notice').textContent()).startsWith('Case data rejected:'));
 assert.equal(await page.locator('main section').count(),0);assert(await page.locator('#case-export').isDisabled());assert.deepEqual(errors,[]);domainContractsTested=true;
 }
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
 const result={browser:await browser.version(),suites:results,negative_controls:{script_injection_literal:true,csv_formula_escaped:true,domain_type_key_enum_rejections:domainContractsTested,invalid_case_blocks_exports:domainContractsTested},limits:['Browser verification uses fictional data, not an enterprise tenant.','No native Office rendering is established by browser checks.']};
 fs.writeFileSync(path.join(build,'results.json'),JSON.stringify(result,null,2)+'\n');
 console.log(JSON.stringify({browser:result.browser,suites:results.length,negative_controls:result.negative_controls}));
 await browser.close();
}
main().catch(e=>{console.error(e);process.exit(1);});
