# Ownership Analysis — complete dashboard template

Version 1.0.0. Use the complete HTML below to create a single downloadable `.html` file in the current session. It includes all style and interaction code. No hosted assets, fonts, CDN, installation, repository access, API key or local server is needed. Where a file tool is unavailable, return the complete HTML as copy-ready text and explicitly state that no file was created.

## Design and behavior contract

| Element | Light | Dark |
| --- | --- | --- |
| Page | `#E4E7E7` muted gray | `#263746` softened navy |
| Panels | `#F1F2EF` stone | `#304655` slate navy |
| Text | `#243641` | `#EFF1EF` |
| Secondary text | `#4E606A` | `#C0CDD3` |
| Suite accent | `#4c5180` | `#c7cdf2` |
| High / medium / low | `#8A3439` / `#735119` / `#315F54` | `#FFB8B8` / `#F0D393` / `#B1DCC9` |

Use Segoe UI, Calibri or Arial; 15 px body; responsive title; no remote font. Keep the ten fixed dashboard sections and exact domain tables. Navigation identifies analytical sections. It is not an operational case-management interface.

Theme control is keyboard operable and retains the preference when browser storage permits. Storage failure does not stop rendering. Findings search and severity filtering affect the table and CSV export only; coverage metrics and severity/confidence charts remain full-fixture measures and are labeled accordingly. Printing temporarily restores all findings, uses a neutral light print theme, and restores the filter afterward. Table regions scroll independently on small screens with keyboard access. Empty results state what scope is empty; they never imply no underlying risk.

## Populate safely

The JSON in `report-data` is the only data payload. Replace it with the reviewed case data using the same keys and the schemas in file 05. Retain `notice` as a visible synthetic label when using the example. For a real authorized case, replace it with the actual scope/classification and review state only after removing every fixture record. Never fabricate an approval or completed QA check.

Serialize `<`, `>` and `&` in JSON as `\u003c`, `\u003e`, `\u0026` before embedding. Display values through `textContent`; do not insert untrusted evidence with `innerHTML`. This prevents a source string from ending the JSON script element or executing as markup. CSV exports quote all fields and prefix formula-like strings with an apostrophe. The export contains only visible findings and uses a name that states that scope.

## Complete standalone HTML

```html
<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; connect-src 'none'; base-uri 'none'; form-action 'none'">
<title>Ownership Analysis</title>
<style>
:root{--bg:#e4e7e7;--panel:#f1f2ef;--ink:#243641;--muted:#4e606a;--line:#9baab0;--accent:#4c5180;--soft:#d4dee2;--high:#8a3439;--medium:#735119;--low:#315f54;--focus:#005f9c;--radius:8px}
:root[data-theme=dark]{--bg:#263746;--panel:#304655;--ink:#eff1ef;--muted:#c0cdd3;--line:#6b8291;--accent:#c7cdf2;--soft:#3c5667;--high:#ffb8b8;--medium:#f0d393;--low:#b1dcc9;--focus:#9bd3fa}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:16px}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 "Segoe UI",Calibri,Arial,sans-serif}button,input,select{font:inherit;color:inherit}button,select,input{border:1px solid var(--line);border-radius:5px;background:var(--panel);padding:8px 12px}button{cursor:pointer}button:hover{background:var(--soft)}a{color:var(--accent);text-underline-offset:3px}a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,summary:focus-visible,[tabindex]:focus-visible{outline:3px solid var(--focus);outline-offset:3px}.skip{position:absolute;left:12px;top:-60px;background:var(--panel);padding:8px;z-index:10}.skip:focus{top:8px}.shell{max-width:1500px;margin:auto;padding:28px 32px}header{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:start;padding:8px 0 24px;border-bottom:2px solid var(--accent)}h1{font-size:clamp(25px,3.5vw,38px);line-height:1.14;margin:6px 0 12px;max-width:28ch;font-weight:650}h2{font-size:21px;line-height:1.25;margin:0 0 16px}h3{font-size:16px;margin:14px 0 8px}p{max-width:85ch;margin:8px 0 14px}.subtle,.meta{color:var(--muted)}.meta{font-size:13px}.toolbar{display:flex;gap:8px;flex-wrap:wrap;align-items:center}.notice{background:var(--soft);border-left:4px solid var(--accent);padding:12px 16px;margin:24px 0}.layout{display:grid;grid-template-columns:205px minmax(0,1fr);gap:32px}nav{align-self:start;position:sticky;top:20px;padding-top:10px}nav a{display:block;padding:7px 10px;margin:2px 0;text-decoration:none;border-left:2px solid transparent}nav a:hover{background:var(--soft);border-color:var(--accent)}section{background:var(--panel);padding:24px;margin:0 0 22px;border:1px solid var(--line);border-radius:var(--radius);min-width:0}section.hero{background:transparent;border:0;padding:8px 0 16px}.metrics{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin:18px 0}.metric{padding:14px;border-left:3px solid var(--accent);background:var(--soft)}.metric strong{font-size:23px;display:block;overflow-wrap:anywhere;font-variant-numeric:tabular-nums}.metric span{font-size:13px}.metric small{display:block;color:var(--muted);margin-top:6px}.table-wrap{overflow:auto;max-height:560px;border:1px solid var(--line);border-radius:5px}table{border-collapse:collapse;width:100%;font-size:13px}caption{text-align:left;padding:10px;font-weight:600;color:var(--muted)}th,td{text-align:left;vertical-align:top;padding:10px 12px;border-bottom:1px solid var(--line);overflow-wrap:anywhere;min-width:110px;max-width:440px}th{background:var(--soft);position:sticky;top:0;font-weight:600}tr:last-child td{border-bottom:0}tbody tr:nth-child(even){background:color-mix(in srgb,var(--soft) 35%,transparent)}.badge{display:inline-block;padding:2px 6px;border:1px solid currentColor;border-radius:4px;white-space:nowrap;font-weight:600}.high,.critical{color:var(--high)}.medium{color:var(--medium)}.low{color:var(--low)}.charts{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:18px}.bar-row{display:grid;grid-template-columns:112px 1fr 32px;align-items:center;gap:8px;margin:9px 0;font-size:12px}.bar-track{height:12px;background:var(--soft);border:1px solid var(--line)}.bar-fill{height:100%;background:var(--accent)}.empty{padding:18px;color:var(--muted)}.filters{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:15px}.filters label{display:grid;gap:4px;font-size:13px}input{min-width:240px;max-width:100%}details{border-top:1px solid var(--line);padding:12px 0}summary{cursor:pointer;font-weight:600}ol,ul{padding-left:22px}li{margin:7px 0}.decision{border-left:4px solid var(--accent);padding-left:16px}footer{padding:10px 0 30px;color:var(--muted);font-size:12px}#filter-state{min-height:24px}.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}
@media(max-width:900px){.shell{padding:20px 16px}.layout{display:block}nav{position:static;display:flex;flex-wrap:wrap;gap:2px;margin:0 0 20px}nav a{font-size:13px;padding:5px 8px}header{grid-template-columns:1fr}.charts{grid-template-columns:1fr}section{padding:18px}.table-wrap{max-height:440px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@media print{:root,:root[data-theme=dark]{--bg:#fff;--panel:#fff;--ink:#202d35;--muted:#44535c;--line:#a6b0b4;--accent:#31566b;--soft:#e9edf0;--high:#8a3439;--medium:#735119;--low:#315f54}body{font-size:10pt}.shell{padding:0;max-width:none}header{display:block}.layout{display:block}nav,.toolbar,.filters,.skip,#filter-state{display:none!important}section{break-inside:auto;padding:14px 0;border:0;border-bottom:1px solid var(--line);border-radius:0}.metric,.charts,details{break-inside:avoid}h2,h3{break-after:avoid}.table-wrap{overflow:visible;max-height:none;border:0}th{position:static}td,th{font-size:8pt;min-width:0;padding:5px;overflow-wrap:anywhere}thead{display:table-header-group}tr{break-inside:avoid}.notice{margin:12px 0}a{color:inherit;text-decoration:none}@page{size:A4 landscape;margin:14mm}}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to analysis</a>
<div class="shell">
<header><div><p class="meta" id="identity"></p><h1 id="title"></h1><p id="subtitle"></p></div><div class="toolbar"><button id="theme" type="button" aria-pressed="false">Use dark theme</button><button id="export" type="button">Export visible findings</button><button id="print" type="button">Print full report</button></div></header>
<div class="notice" id="notice"></div>
<div class="layout"><nav aria-label="Report sections">
<a href="#decision">Decision brief</a><a href="#coverage">Coverage and measures</a><a href="#findings">Findings</a><a href="#evidence">Evidence index</a><a href="#domain-one" id="nav-one">Analysis register</a><a href="#domain-two" id="nav-two">Supporting register</a><a href="#actions">Proposed actions</a><a href="#review">Review record</a><a href="#method">Method and scope</a><a href="#limitations">Limitations</a>
</nav><main id="main">
<section id="decision" class="hero"><h2>Decision brief</h2><p class="decision" id="decision-text"></p><p class="subtle">Recommendation status: proposed. Human disposition: not recorded.</p></section>
<section id="coverage"><h2>Coverage and measures</h2><div class="metrics" id="metrics"></div><p class="meta">Measures below are from the complete supplied case record. Filtering affects the findings table and its export only.</p><div class="charts"><div><h3>Findings by severity</h3><div id="severity-chart"></div></div><div><h3>Findings by confidence</h3><div id="confidence-chart"></div></div></div></section>
<section id="findings"><h2>Findings</h2><div class="filters"><label>Search findings<input id="search" type="search" placeholder="Search title, evidence, or recommendation"></label><label>Severity<select id="severity"><option value="">All severities</option><option>CRITICAL</option><option>HIGH</option><option>MEDIUM</option><option>LOW</option></select></label><button id="reset" type="button">Reset filters</button></div><p id="filter-state" class="meta" role="status" aria-live="polite"></p><div id="finding-table"></div></section>
<section id="evidence"><h2>Evidence index</h2><p class="meta">Resolve each evidence identifier to its exact locator. The visible data label states whether the records are synthetic.</p><div id="evidence-table"></div></section>
<section id="domain-one"><h2 id="domain-one-title"></h2><div id="domain-one-table"></div></section>
<section id="domain-two"><h2 id="domain-two-title"></h2><div id="domain-two-table"></div></section>
<section id="actions"><h2>Proposed actions</h2><p>These actions are drafts for the designated reviewer. No operational instruction has been executed.</p><div id="action-table"></div></section>
<section id="review"><h2>Review record</h2><div id="review-table"></div></section>
<section id="method"><h2>Method and scope</h2><p id="scope"></p><ol id="methods"></ol><details open><summary>Interpretation rules</summary><p>Severity expresses potential consequence. Confidence expresses evidence strength. Reported claims remain attributed; an indicator is not proof of wrongdoing. Missing inputs retain an explicit unknown state. A fixture check does not validate real-world performance.</p></details></section>
<section id="limitations"><h2>Limitations and unresolved questions</h2><ul id="limits"></ul><p class="meta">Preserve the limitation attached to every metric when adapting this template. Do not replace an unknown denominator with zero.</p></section>
</main></div><footer id="footer"></footer>
</div>
<script id="report-data" type="application/json">{
  "slug": "ownership-analysis",
  "title": "Ownership Analysis",
  "summary": "Trace dated ownership edges, economic paths, unresolved branches, and control rights with separate legal overlays.",
  "audience": "Analysts reviewing layered ownership structures and public ownership disclosures",
  "decision": "Which ultimate economic interests are supported by the dated graph, and what evidence or interpretation remains missing?",
  "palette": "indigo",
  "report_sections": [
    "Ownership decision brief",
    "Scope and graph method",
    "Material findings",
    "Direct ownership assessment",
    "Ultimate interests and unresolved branches",
    "Evidence record",
    "Recommended ownership review actions",
    "Limitations and human review"
  ],
  "domain_tables": [
    {
      "name": "OwnershipEdges",
      "columns": [
        "edge_id",
        "owner_id",
        "owned_entity_id",
        "interest_pct",
        "interest_basis",
        "effective_date",
        "evidence_ids",
        "notes"
      ],
      "formats": {
        "interest_pct": "0.0\"%\""
      },
      "rows": [
        [
          "OW-01",
          "PERSON-A",
          "HOLDCO",
          60,
          "Ordinary economic equity",
          "2026-09-30",
          "SYN-001",
          "Fictional supplied schedule"
        ],
        [
          "OW-02",
          "PERSON-B",
          "HOLDCO",
          40,
          "Ordinary economic equity",
          "2026-09-30",
          "SYN-001",
          "Fictional supplied schedule"
        ],
        [
          "OW-03",
          "HOLDCO",
          "TARGET",
          50,
          "Ordinary economic equity",
          "2026-09-30",
          "SYN-001",
          "Intermediate holding"
        ],
        [
          "OW-04",
          "PERSON-A",
          "TARGET",
          10,
          "Ordinary economic equity",
          "2026-09-30",
          "SYN-001",
          "Separate direct holding"
        ],
        [
          "OW-05",
          "PERSON-C",
          "TARGET",
          25,
          "Ordinary economic equity",
          "2026-09-30",
          "SYN-001",
          "Reported veto right assessed separately"
        ],
        [
          "OW-06",
          "UNKNOWN-POOL",
          "TARGET",
          15,
          "Ordinary economic equity",
          "2026-09-30",
          "SYN-001",
          "Amount known; holders unresolved"
        ]
      ]
    },
    {
      "name": "UltimateInterests",
      "columns": [
        "ultimate_id",
        "target_id",
        "economic_interest_pct",
        "path_ids",
        "resolution_state",
        "control_state",
        "claim_class",
        "evidence_ids",
        "notes"
      ],
      "formats": {
        "economic_interest_pct": "0.0\"%\""
      },
      "rows": [
        [
          "PERSON-A",
          "TARGET",
          40,
          "OW-01\u003eOW-03;OW-04",
          "RESOLVED ON SUPPLIED GRAPH",
          "NOT ASSESSED",
          "Estimated",
          "SYN-001",
          "60 percent \u00d7 50 percent + 10 percent"
        ],
        [
          "PERSON-B",
          "TARGET",
          20,
          "OW-02\u003eOW-03",
          "RESOLVED ON SUPPLIED GRAPH",
          "NOT ASSESSED",
          "Estimated",
          "SYN-001",
          "40 percent \u00d7 50 percent"
        ],
        [
          "PERSON-C",
          "TARGET",
          25,
          "OW-05",
          "RESOLVED ON SUPPLIED GRAPH",
          "REPORTED RIGHTS",
          "Reported",
          "SYN-001",
          "Veto scope and legal effect not established"
        ],
        [
          "UNKNOWN-POOL",
          "TARGET",
          15,
          "OW-06",
          "UNRESOLVED",
          "NOT ASSESSED",
          "Reported",
          "SYN-001",
          "Do not allocate residual to known holders"
        ]
      ]
    }
  ],
  "findings": [
    {
      "id": "F-01",
      "title": "Unidentified holders account for 15.0%",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001"
      ],
      "detail": "UNKNOWN-POOL holds a reported 15.0% direct target interest without identified underlying holders.",
      "recommendation": "Obtain the missing holder schedule and effective-date evidence."
    },
    {
      "id": "F-02",
      "title": "Known terminal economic interests total 85.0%",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Estimated",
      "evidence_ids": [
        "SYN-001"
      ],
      "detail": "Person A 40.0% + Person B 20.0% + Person C 25.0% under proportional acyclic assumptions.",
      "recommendation": "Preserve path arithmetic, reported-source status, and separate legal questions."
    },
    {
      "id": "F-03",
      "title": "Reported veto right lacks supporting instrument",
      "severity": "MEDIUM",
      "confidence": "LOW",
      "claim_class": "Reported",
      "evidence_ids": [
        "SYN-001"
      ],
      "detail": "Person C reportedly has a veto over certain asset sales; scope and governing document are absent.",
      "recommendation": "Obtain rights evidence before drawing a control conclusion."
    }
  ],
  "evidence": [
    {
      "id": "SYN-001",
      "title": "Fictional ownership graph",
      "locator": "10-worked-example.md, OW-01 through OW-06",
      "claim_class": "Observed"
    },
    {
      "id": "REF-CDD",
      "title": "FinCEN CDD overview",
      "locator": "https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule",
      "claim_class": "Observed"
    },
    {
      "id": "REF-CDD-2026",
      "title": "FinCEN FIN-2026-R001",
      "locator": "https://www.fincen.gov/system/files/2026-02/FinCEN-Order-CCDExceptiveRelief.pdf",
      "claim_class": "Observed"
    },
    {
      "id": "REF-OFAC-401",
      "title": "OFAC FAQ 401",
      "locator": "https://ofac.treasury.gov/faqs/401",
      "claim_class": "Observed"
    },
    {
      "id": "REF-OFAC-398",
      "title": "OFAC FAQ 398",
      "locator": "https://ofac.treasury.gov/faqs/398",
      "claim_class": "Observed"
    }
  ],
  "metrics": [
    {
      "label": "Known terminal economic interests",
      "value": "85.0%",
      "method": "40.0% Person A + 20.0% Person B + 25.0% Person C.",
      "format": "#,##0"
    },
    {
      "label": "Unresolved economic interest",
      "value": "15.0%",
      "method": "100.0% less 85.0% known terminal interests.",
      "format": "#,##0"
    },
    {
      "label": "Direct edges",
      "value": "6",
      "method": "Count distinct OW-01 through OW-06; no graph-wide percentage sum.",
      "format": "#,##0"
    }
  ],
  "limitations": [
    "All holdings and rights are fictional reported inputs.",
    "Simple path multiplication requires comparable proportional rights and no cycles or overlap.",
    "Economic interest, control, legal beneficial ownership, and sanctions propagation are distinct questions."
  ],
  "metadata": {
    "conclusion": "The fictional graph supports estimated economic interests of 40.0% for Person A, 20.0% for Person B, and a reported 25.0% for Person C. A further 15.0% remains unresolved, and the reported veto right requires evidence before any control conclusion."
  },
  "report_narrative": [
    [
      "The fictional graph supports estimated economic interests of 40.0% for Person A, 20.0% for Person B, and a reported 25.0% for Person C. A further 15.0% remains unresolved, and the reported veto right requires evidence before any control conclusion."
    ],
    [
      "The review uses six dated direct ownership edges for an acyclic, proportional economic-equity graph. It assesses path arithmetic and unresolved branches separately from control, legal beneficial ownership and sanctions propagation."
    ],
    [
      "F-01: UNKNOWN-POOL holds a reported 15.0% direct target interest without identified underlying holders.",
      "F-02: Person A 40.0% + Person B 20.0% + Person C 25.0% under proportional acyclic assumptions.",
      "F-03: Person C reportedly has a veto over certain asset sales; scope and governing document are absent."
    ],
    [
      "HOLDCO is owned 60.0% by PERSON-A and 40.0% by PERSON-B. TARGET is held 50.0% by HOLDCO, 10.0% directly by PERSON-A, 25.0% by PERSON-C and 15.0% by unidentified holders. Distinct direct and indirect holdings are retained."
    ],
    [
      "PERSON-A has 60.0% \u00d7 50.0% + 10.0% = 40.0%; PERSON-B has 40.0% \u00d7 50.0% = 20.0%; PERSON-C has 25.0%. Resolved terminal interests total 85.0%; the 15.0% residual is not reallocated. The reported veto right lacks its supporting instrument."
    ],
    [
      "SYN-001 supplies the fictional reported schedule and rights assertion. The arithmetic is conditional on comparable proportional rights and no overlapping or circular interests; source verification remains distinct from calculation."
    ],
    [
      "Obtain the missing holder schedule and rights instrument. Reassess effective dates, share classes and path overlap before carrying these economic results into any separate legal test."
    ],
    [
      "All holdings and rights are fictional reported inputs.",
      "Simple path multiplication requires comparable proportional rights and no cycles or overlap.",
      "Economic interest, control, legal beneficial ownership, and sanctions propagation are distinct questions.",
      "QA remains pending and no authorized human disposition is recorded."
    ]
  ],
  "suite_id": "ownership-analysis",
  "version": "1.0.0",
  "as_of": "2026-10-09",
  "notice": "Synthetic worked example. Fictional records. Not a completed operational review.",
  "scope": "Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.",
  "conclusion": "The fictional graph supports estimated economic interests of 40.0% for Person A, 20.0% for Person B, and a reported 25.0% for Person C. A further 15.0% remains unresolved, and the reported veto right requires evidence before any control conclusion.",
  "methods": [
    "Confirm the question, authorized scope, period, population and available capabilities.",
    "Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.",
    "Apply the suite method and decision rules; test competing explanations and missing inputs.",
    "Populate the fixed domain registers without inventing fields, facts or approvals.",
    "Review calculations and citations; record exceptions and seek the named human disposition."
  ],
  "actions": [
    {
      "id": "A-001",
      "finding_id": "F-01",
      "proposal": "Obtain the missing holder schedule and effective-date evidence.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-002",
      "finding_id": "F-02",
      "proposal": "Preserve path arithmetic, reported-source status, and separate legal questions.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-003",
      "finding_id": "F-03",
      "proposal": "Obtain rights evidence before drawing a control conclusion.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    }
  ],
  "qa": [
    {
      "id": "QA-01",
      "check": "Synthetic fixture calculations",
      "result": "REVIEW REQUIRED",
      "evidence": "Reproduce the arithmetic in file 10."
    },
    {
      "id": "QA-02",
      "check": "Evidence support and competing explanations",
      "result": "REVIEW REQUIRED",
      "evidence": "Compare findings to the exact fixture locators and file 04."
    },
    {
      "id": "QA-03",
      "check": "Authorized human disposition",
      "result": "NOT RECORDED",
      "evidence": "No reviewer identity, decision or approval has been supplied."
    }
  ]
}</script>
<script>
'use strict';
const data=JSON.parse(document.getElementById('report-data').textContent);
const byId=id=>document.getElementById(id);
const write=(id,value)=>{byId(id).textContent=value;};
const show=value=>value===null||value===undefined?'Not provided':Array.isArray(value)?value.join('; '):String(value);
function formatted(value,format){if(typeof value!=='number'||!format)return show(value);if(format==='0.0%')return(value*100).toFixed(1)+'%';if(format==='0.0"%"')return value.toFixed(1)+'%';const places=format.includes('.00')?2:format.includes('.0')?1:0;return(format.includes('$')?'$':'')+value.toLocaleString('en-US',{minimumFractionDigits:places,maximumFractionDigits:places});}
function table(target,columns,rows,caption,formats={}){
  const host=byId(target);host.replaceChildren();
  if(!rows.length){const p=document.createElement('p');p.className='empty';p.textContent='No records in this view. This does not establish absence in the underlying population.';host.append(p);return;}
  const wrap=document.createElement('div');wrap.className='table-wrap';wrap.tabIndex=0;wrap.setAttribute('role','region');wrap.setAttribute('aria-label',caption);
  const t=document.createElement('table');const cap=t.createCaption();cap.textContent=caption;
  const h=t.createTHead().insertRow();columns.forEach(c=>{const th=document.createElement('th');th.scope='col';th.textContent=c;h.append(th);});
  const body=t.createTBody();rows.forEach(row=>{const tr=body.insertRow();row.forEach((v,i)=>{const td=tr.insertCell();if(columns[i]==='severity'){const span=document.createElement('span');span.className='badge '+show(v).toLowerCase();span.textContent=show(v);td.append(span);}else{td.textContent=formatted(v,formats[columns[i]]);}});});
  wrap.append(t);host.append(wrap);
}
function chart(target,field,labels){const host=byId(target);const counts=labels.map(label=>data.findings.filter(f=>f[field]===label).length);const max=Math.max(1,...counts);labels.forEach((label,i)=>{const row=document.createElement('div');row.className='bar-row';const name=document.createElement('span');name.textContent=label;const track=document.createElement('div');track.className='bar-track';track.setAttribute('aria-hidden','true');const bar=document.createElement('div');bar.className='bar-fill';bar.style.width=(counts[i]/max*100)+'%';track.append(bar);const value=document.createElement('span');value.textContent=counts[i];row.append(name,track,value);host.append(row);});}
const findingColumns=['id','title','severity','confidence','claim_class','evidence_ids','detail','recommendation'];
let visible=[];
function renderFindings(){const q=byId('search').value.trim().toLowerCase();const level=byId('severity').value;visible=data.findings.filter(f=>(!level||f.severity===level)&&(!q||findingColumns.map(k=>show(f[k])).join(' ').toLowerCase().includes(q)));table('finding-table',findingColumns,visible.map(f=>findingColumns.map(k=>f[k])),'Finding register');write('filter-state',`${visible.length} of ${data.findings.length} findings visible. Coverage measures remain unfiltered.`);}
write('identity',`${data.suite_id} / ${data.version} / As of ${data.as_of}`);write('title',data.title);write('subtitle',data.summary);write('notice',data.notice);write('decision-text',data.conclusion);write('scope',data.decision+' '+data.scope);
data.metrics.forEach(m=>{const box=document.createElement('div');box.className='metric';const label=document.createElement('span');label.textContent=m.label;const value=document.createElement('strong');value.textContent=formatted(m.value,m.format);const method=document.createElement('small');method.textContent=m.method;box.append(label,value,method);byId('metrics').append(box);});
chart('severity-chart','severity',['CRITICAL','HIGH','MEDIUM','LOW']);chart('confidence-chart','confidence',['HIGH','MODERATE','LOW','NOT ASSESSABLE']);
table('evidence-table',['id','title','locator','claim_class'],data.evidence.map(e=>[e.id,e.title,e.locator,e.claim_class]),'Evidence pointers');
['one','two'].forEach((suffix,i)=>{const t=data.domain_tables[i];write('domain-'+suffix+'-title',t.name);write('nav-'+suffix,t.name);table('domain-'+suffix+'-table',t.columns,t.rows,t.name,t.formats||{});const counts=document.createElement('p');counts.className='meta';counts.textContent=`Domain record count: ${t.rows.length}. Missing (null) cells: ${t.rows.flat().filter(v=>v===null).length}. Empty text follows the field-specific contract.`;byId('domain-'+suffix+'-table').append(counts);});
table('action-table',['action_id','finding_id','proposal','owner','due_date','status'],data.actions.map(a=>[a.id,a.finding_id,a.proposal,a.owner,a.due_date,a.status]),'Proposed action register');
table('review-table',['check_id','check','result','evidence'],data.qa.map(q=>[q.id,q.check,q.result,q.evidence]),'Review checks');
data.methods.forEach(m=>{const li=document.createElement('li');li.textContent=m;byId('methods').append(li);});data.limitations.forEach(m=>{const li=document.createElement('li');li.textContent=m;byId('limits').append(li);});
write('footer',`${data.title} | ${data.version} | ${data.notice} | Prepared for human review.`);
function theme(mode){document.documentElement.dataset.theme=mode;byId('theme').setAttribute('aria-pressed',String(mode==='dark'));write('theme',mode==='dark'?'Use light theme':'Use dark theme');}
const storageKey='markdown-toolkit-theme-v1';try{theme(localStorage.getItem(storageKey)==='dark'?'dark':'light');}catch{theme('light');}
byId('theme').addEventListener('click',()=>{const mode=document.documentElement.dataset.theme==='dark'?'light':'dark';theme(mode);try{localStorage.setItem(storageKey,mode);}catch{}});
byId('search').addEventListener('input',renderFindings);byId('severity').addEventListener('change',renderFindings);byId('reset').addEventListener('click',()=>{byId('search').value='';byId('severity').value='';renderFindings();});
function csvCell(value){let text=show(value);if(/^[\s]*[=+\-@\t\r]/.test(text)){text="'"+text;}return '"'+text.replaceAll('"','""')+'"';}
byId('export').addEventListener('click',()=>{const csv=[findingColumns,...visible.map(f=>findingColumns.map(k=>f[k]))].map(row=>row.map(csvCell).join(',')).join('\r\n');const url=URL.createObjectURL(new Blob(['\ufeff'+csv],{type:'text/csv;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download=data.suite_id+'-visible-findings.csv';document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);});
let beforePrint=null;window.addEventListener('beforeprint',()=>{beforePrint={query:byId('search').value,severity:byId('severity').value};byId('search').value='';byId('severity').value='';renderFindings();});window.addEventListener('afterprint',()=>{if(beforePrint){byId('search').value=beforePrint.query;byId('severity').value=beforePrint.severity;renderFindings();beforePrint=null;}});byId('print').addEventListener('click',()=>window.print());renderFindings();
</script>
</body>
</html>

```

## Acceptance and delivery

Open the actual file. Check both themes, desktop and narrow screens, keyboard navigation, visible focus, long evidence strings, missing values, empty filters, reset, CSV scope and print preview. Reconcile every displayed metric and chart to its input rows. Verify no network resources are requested. Rendering success does not establish evidence quality or analytical validity. Record untested browser/platform behavior honestly. If a browser blocks downloads or scripting, use the unchanged source data and fixed report/workbook alternatives; do not invent a functioning control.
