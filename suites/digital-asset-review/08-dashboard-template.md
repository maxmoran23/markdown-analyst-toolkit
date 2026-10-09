# Digital Asset Review — complete dashboard template

Version 1.2.0. Use the complete HTML below to create a single downloadable `.html` file in the current session. It includes all style and interaction code. No hosted assets, fonts, CDN, installation, repository access, API key or local server is needed. Where a file tool is unavailable, return the complete HTML as copy-ready text and explicitly state that no file was created.

## Design and behavior contract

| Element | Light | Dark |
| --- | --- | --- |
| Page | `#E4E7E7` muted gray | `#263746` softened navy |
| Panels | `#F1F2EF` stone | `#304655` slate navy |
| Text | `#243641` | `#EFF1EF` |
| Secondary text | `#4E606A` | `#C0CDD3` |
| Suite accent | `#276357` | `#a7d8c7` |
| High / medium / low | `#8A3439` / `#735119` / `#315F54` | `#FFB8B8` / `#F0D393` / `#B1DCC9` |

Use Segoe UI, Calibri or Arial; 15 px body; responsive title; no remote font. Keep eight common dashboard sections plus one section for every declared domain table. Preserve all eight report-narrative sections, every domain row and all declared field definitions. Navigation identifies analytical sections. It is not an operational case-management interface.

Theme control is keyboard operable and retains the preference when browser storage permits. Storage failure does not stop rendering. Findings search and severity filtering affect the table and CSV export only; coverage metrics and severity/confidence charts remain full-fixture measures and are labeled accordingly. Export complete case downloads the unfiltered JSON payload, including all domain rows, field contracts and narratives, for an explicit case handoff. It does not include source documents that are only referenced by locator. Printing temporarily restores all findings, uses a neutral light print theme, and restores the filter afterward. Table regions scroll independently on small screens with keyboard access. Empty results state what scope is empty; they never imply no underlying risk.

## Populate safely

The JSON in `report-data` is the only data payload. Replace it with the reviewed case data using the same keys and the schemas in file 05. Retain `notice` as a visible synthetic label when using the example. For a real authorized case, replace it with the actual scope/classification and review state only after removing every fixture record. Never fabricate an approval or completed QA check.

Serialize `<`, `>` and `&` in JSON as `\u003c`, `\u003e`, `\u0026` before embedding. Display values through `textContent`; do not insert untrusted evidence with `innerHTML`. This prevents a source string from ending the JSON script element or executing as markup. CSV exports quote all fields and prefix formula-like strings with an apostrophe. The export contains only visible findings and uses a name that states that scope.

## Complete standalone HTML

For portable case data, write integer fields and report placement as whole-number JSON literals such as `1` and `4`, without a decimal suffix. Python enforces integer types; JavaScript parses `1` and `1.0` as the same number. HTML rejects integers outside JavaScript's safe range, and Excel applies its stricter 15-digit boundary. Preserve exact large identifiers or quantities as text under the declared field contract. These runtime constraints are not identical validators or a guarantee of exact floating-point arithmetic.

```html
<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; connect-src 'none'; base-uri 'none'; form-action 'none'">
<title>Digital Asset Review</title>
<style>
:root{--bg:#e4e7e7;--panel:#f1f2ef;--ink:#243641;--muted:#4e606a;--line:#9baab0;--accent:#276357;--soft:#d4dee2;--high:#8a3439;--medium:#735119;--low:#315f54;--focus:#005f9c;--radius:8px}
:root[data-theme=dark]{--bg:#263746;--panel:#304655;--ink:#eff1ef;--muted:#c0cdd3;--line:#6b8291;--accent:#a7d8c7;--soft:#3c5667;--high:#ffb8b8;--medium:#f0d393;--low:#b1dcc9;--focus:#9bd3fa}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:16px}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 "Segoe UI",Calibri,Arial,sans-serif}button,input,select{font:inherit;color:inherit}button,select,input{border:1px solid var(--line);border-radius:5px;background:var(--panel);padding:8px 12px}button{cursor:pointer}button:hover{background:var(--soft)}a{color:var(--accent);text-underline-offset:3px}a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,summary:focus-visible,[tabindex]:focus-visible{outline:3px solid var(--focus);outline-offset:3px}.skip{position:absolute;left:12px;top:-60px;background:var(--panel);padding:8px;z-index:10}.skip:focus{top:8px}.shell{max-width:1500px;margin:auto;padding:28px 32px}header{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:start;padding:8px 0 24px;border-bottom:2px solid var(--accent)}h1{font-size:clamp(25px,3.5vw,38px);line-height:1.14;margin:6px 0 12px;max-width:28ch;font-weight:650}h2{font-size:21px;line-height:1.25;margin:0 0 16px}h3{font-size:16px;margin:14px 0 8px}p{max-width:85ch;margin:8px 0 14px}.subtle,.meta{color:var(--muted)}.meta{font-size:13px}.toolbar{display:flex;gap:8px;flex-wrap:wrap;align-items:center}.notice{background:var(--soft);border-left:4px solid var(--accent);padding:12px 16px;margin:24px 0}.layout{display:grid;grid-template-columns:205px minmax(0,1fr);gap:32px}nav{align-self:start;position:sticky;top:20px;padding-top:10px}nav a{display:block;padding:7px 10px;margin:2px 0;text-decoration:none;border-left:2px solid transparent}nav a:hover{background:var(--soft);border-color:var(--accent)}section{background:var(--panel);padding:24px;margin:0 0 22px;border:1px solid var(--line);border-radius:var(--radius);min-width:0}section.hero{background:transparent;border:0;padding:8px 0 16px}.metrics{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin:18px 0}.metric{padding:14px;border-left:3px solid var(--accent);background:var(--soft)}.metric strong{font-size:23px;display:block;overflow-wrap:anywhere;font-variant-numeric:tabular-nums}.metric span{font-size:13px}.metric small{display:block;color:var(--muted);margin-top:6px}.table-wrap{overflow:auto;max-height:560px;border:1px solid var(--line);border-radius:5px}table{border-collapse:collapse;width:100%;font-size:13px}caption{text-align:left;padding:10px;font-weight:600;color:var(--muted)}th,td{text-align:left;vertical-align:top;padding:10px 12px;border-bottom:1px solid var(--line);overflow-wrap:anywhere;min-width:110px;max-width:440px}th{background:var(--soft);position:sticky;top:0;font-weight:600}tr:last-child td{border-bottom:0}tbody tr:nth-child(even){background:color-mix(in srgb,var(--soft) 35%,transparent)}.badge{display:inline-block;padding:2px 6px;border:1px solid currentColor;border-radius:4px;white-space:nowrap;font-weight:600}.high,.critical{color:var(--high)}.medium{color:var(--medium)}.low{color:var(--low)}.charts{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:18px}.bar-row{display:grid;grid-template-columns:112px 1fr 32px;align-items:center;gap:8px;margin:9px 0;font-size:12px}.bar-track{height:12px;background:var(--soft);border:1px solid var(--line)}.bar-fill{height:100%;background:var(--accent)}.empty{padding:18px;color:var(--muted)}.filters{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:15px}.filters label{display:grid;gap:4px;font-size:13px}input{min-width:240px;max-width:100%}details{border-top:1px solid var(--line);padding:12px 0}summary{cursor:pointer;font-weight:600}ol,ul{padding-left:22px}li{margin:7px 0}.decision{border-left:4px solid var(--accent);padding-left:16px}footer{padding:10px 0 30px;color:var(--muted);font-size:12px}#filter-state{min-height:24px}.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}
@media(max-width:900px){.shell{padding:20px 16px}.layout{display:block}nav{position:static;display:flex;flex-wrap:wrap;gap:2px;margin:0 0 20px}nav a{font-size:13px;padding:5px 8px}header{grid-template-columns:1fr}.charts{grid-template-columns:1fr}section{padding:18px}.table-wrap{max-height:440px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@media print{:root,:root[data-theme=dark]{--bg:#fff;--panel:#fff;--ink:#202d35;--muted:#44535c;--line:#a6b0b4;--accent:#31566b;--soft:#e9edf0;--high:#8a3439;--medium:#735119;--low:#315f54}body{font-size:10pt}.shell{padding:0;max-width:none}header{display:block}.layout{display:block}nav,.toolbar,.filters,.skip,#filter-state{display:none!important}section{break-inside:auto;padding:14px 0;border:0;border-bottom:1px solid var(--line);border-radius:0}.metric,.charts,details{break-inside:avoid}h2,h3{break-after:avoid}.table-wrap{overflow:visible;max-height:none;border:0}th{position:static}td,th{font-size:8pt;min-width:0;padding:5px;overflow-wrap:anywhere}thead{display:table-header-group}tr{break-inside:avoid}.notice{margin:12px 0}a{color:inherit;text-decoration:none}@page{size:A4 landscape;margin:14mm}}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to analysis</a>
<div class="shell">
<header><div><p class="meta" id="identity"></p><h1 id="title"></h1><p id="subtitle"></p></div><div class="toolbar"><button id="theme" type="button" aria-pressed="false">Use dark theme</button><button id="export" type="button">Export visible findings</button><button id="case-export" type="button">Export complete case</button><button id="print" type="button">Print full report</button></div></header>
<div class="notice" id="notice"></div>
<div class="layout"><nav aria-label="Report sections">
<a href="#decision">Decision brief</a><a href="#coverage">Coverage and measures</a><a href="#findings">Findings</a><a href="#evidence">Evidence index</a><span id="domain-navigation"></span><a href="#actions">Proposed actions</a><a href="#review">Review record</a><a href="#method">Method and scope</a><a href="#limitations">Limitations</a>
</nav><main id="main">
<section id="decision" class="hero"><h2>Decision brief</h2><p class="decision" id="decision-text"></p><p class="subtle">Recommendation status: proposed. Human disposition: not recorded.</p></section>
<section id="coverage"><h2>Coverage and measures</h2><div class="metrics" id="metrics"></div><p class="meta">Measures below are from the complete supplied case record. Filtering affects the findings table and its export only.</p><div class="charts"><div><h3>Findings by severity</h3><div id="severity-chart"></div></div><div><h3>Findings by confidence</h3><div id="confidence-chart"></div></div></div></section>
<section id="findings"><h2>Findings</h2><div class="filters"><label>Search findings<input id="search" type="search" placeholder="Search title, evidence, or recommendation"></label><label>Severity<select id="severity"><option value="">All severities</option><option>CRITICAL</option><option>HIGH</option><option>MEDIUM</option><option>LOW</option></select></label><button id="reset" type="button">Reset filters</button></div><p id="filter-state" class="meta" role="status" aria-live="polite"></p><div id="finding-table"></div></section>
<section id="evidence"><h2>Evidence index</h2><p class="meta">Resolve each evidence identifier to its exact locator. The visible data label states whether the records are synthetic.</p><div id="evidence-table"></div></section>
<div id="domain-registers"></div>
<section id="actions"><h2>Proposed actions</h2><p>These actions are drafts for the designated reviewer. No operational instruction has been executed.</p><div id="action-table"></div></section>
<section id="review"><h2>Review record</h2><div id="review-table"></div></section>
<section id="method"><h2>Method and scope</h2><p id="scope"></p><ol id="methods"></ol><details open><summary>Interpretation rules</summary><p>Severity expresses potential consequence. Confidence expresses evidence strength. Reported claims remain attributed; an indicator is not proof of wrongdoing. Missing inputs retain an explicit unknown state. A fixture check does not validate real-world performance.</p></details></section>
<section id="limitations"><h2>Limitations and unresolved questions</h2><ul id="limits"></ul><p class="meta">Preserve the limitation attached to every metric when adapting this template. Do not replace an unknown denominator with zero.</p></section>
</main></div><footer id="footer"></footer>
</div>
<script id="report-data" type="application/json">{
  "slug": "digital-asset-review",
  "title": "Digital Asset Review",
  "summary": "Reconcile public-ledger events and token units while separating transaction facts from real-world attribution.",
  "audience": "Analysts reviewing public blockchain evidence and data-quality limitations",
  "decision": "What activity is supported by the supplied capture, and what attribution or completeness gaps remain?",
  "palette": "teal",
  "report_sections": [
    "Digital asset review brief",
    "Scope and ledger method",
    "Material findings",
    "Event reconciliation",
    "Counterparty and attribution assessment",
    "Evidence record",
    "Recommended review actions",
    "Limitations and human review"
  ],
  "domain_tables": [
    {
      "name": "LedgerEvents",
      "columns": [
        "event_id",
        "chain_id",
        "tx_id",
        "event_index",
        "asset_id",
        "raw_amount",
        "decimals",
        "display_units",
        "direction",
        "execution_state",
        "included",
        "evidence_ids",
        "notes"
      ],
      "rows": [
        [
          "EV-01",
          "FICTIONAL-EVM",
          "TX-01",
          0,
          "PAPER-CONTRACT",
          "100000000",
          6,
          "100.000000",
          "IN",
          "SUCCESS",
          true,
          "SYN-001",
          "Duplicate raw capture R-06 linked and removed once"
        ],
        [
          "EV-02",
          "FICTIONAL-EVM",
          "TX-02",
          0,
          "PAPER-CONTRACT",
          "40000000",
          6,
          "40.000000",
          "OUT",
          "SUCCESS",
          true,
          "SYN-001",
          "Transfer to CP-B"
        ],
        [
          "EV-03",
          "FICTIONAL-EVM",
          "TX-03",
          0,
          "PAPER-CONTRACT",
          "5000000",
          6,
          "5.000000",
          "SELF",
          "SUCCESS",
          true,
          "SYN-001",
          "Separate self activity; excluded from directional totals"
        ],
        [
          "EV-04",
          "FICTIONAL-EVM",
          "TX-04",
          0,
          "PAPER-CONTRACT",
          "1",
          6,
          "0.000001",
          "IN",
          "SUCCESS",
          true,
          "SYN-001",
          "Small unsolicited transfer; no attribution inference"
        ],
        [
          "EV-05",
          "FICTIONAL-EVM",
          "TX-05",
          null,
          "PAPER-CONTRACT",
          "20000000",
          6,
          "20.000000",
          "OUT",
          "FAILED",
          false,
          "SYN-001",
          "Attempted amount from supplied record; no successful event log"
        ]
      ]
    },
    {
      "name": "Counterparties",
      "columns": [
        "counterparty_id",
        "asset_id",
        "in_units",
        "out_units",
        "self_units",
        "eligible_event_count",
        "attribution_state",
        "evidence_ids",
        "notes"
      ],
      "rows": [
        [
          "CP-A",
          "PAPER-CONTRACT",
          "100.000000",
          "0.000000",
          "0.000000",
          1,
          "UNATTRIBUTED",
          "SYN-001",
          "Raw duplicate not counted twice"
        ],
        [
          "CP-B",
          "PAPER-CONTRACT",
          "0.000000",
          "40.000000",
          "0.000000",
          1,
          "UNVERIFIED LABEL",
          "SYN-001",
          "Supplied explorer label not identity evidence"
        ],
        [
          "SUBJECT",
          "PAPER-CONTRACT",
          "0.000000",
          "0.000000",
          "5.000000",
          1,
          "SELF ADDRESS",
          "SYN-001",
          "Same exact fictional address; no separate counterparty"
        ],
        [
          "CP-C",
          "PAPER-CONTRACT",
          "0.000001",
          "0.000000",
          "0.000000",
          1,
          "UNATTRIBUTED",
          "SYN-001",
          "Unsolicited small inbound amount retained"
        ]
      ]
    }
  ],
  "findings": [
    {
      "id": "F-01",
      "title": "Duplicate and failed records need distinct treatment",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001"
      ],
      "detail": "Six raw rows reconcile to five unique records and four eligible successful events.",
      "recommendation": "Preserve duplicate lineage and failed-attempt exclusion."
    },
    {
      "id": "F-02",
      "title": "Counterparty identity is not established by the label",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001"
      ],
      "detail": "CP-B has an explorer-style label without supporting identity evidence.",
      "recommendation": "Obtain independent attribution evidence before consequential reliance."
    },
    {
      "id": "F-03",
      "title": "Captured net flow is not an ending balance",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Estimated",
      "evidence_ids": [
        "SYN-001"
      ],
      "detail": "100.000001 PAPER in less 40.000000 PAPER out equals 60.000001 PAPER under the stipulated method.",
      "recommendation": "Keep balance, fiat value, and completeness limitations explicit."
    }
  ],
  "evidence": [
    {
      "id": "SYN-001",
      "title": "Fictional digital asset capture",
      "locator": "10-worked-example.md, R-01 through R-06",
      "claim_class": "Observed"
    },
    {
      "id": "REF-ETH-TX",
      "title": "Ethereum transactions documentation",
      "locator": "https://ethereum.org/developers/docs/transactions/",
      "claim_class": "Observed"
    },
    {
      "id": "REF-ETH-RPC",
      "title": "Ethereum JSON-RPC documentation",
      "locator": "https://ethereum.org/developers/docs/apis/json-rpc/",
      "claim_class": "Observed"
    },
    {
      "id": "REF-ERC20",
      "title": "ERC-20 standard",
      "locator": "https://eips.ethereum.org/EIPS/eip-20",
      "claim_class": "Observed"
    },
    {
      "id": "REF-BTC",
      "title": "Bitcoin transactions developer guide",
      "locator": "https://developer.bitcoin.org/devguide/transactions.html",
      "claim_class": "Observed"
    },
    {
      "id": "REF-FATF-VA",
      "title": "FATF virtual asset guidance",
      "locator": "https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html",
      "claim_class": "Observed"
    }
  ],
  "metrics": [
    {
      "label": "Raw to unique records",
      "value": "6 to 5",
      "method": "Six capture rows less one proven repeated event.",
      "format": "#,##0"
    },
    {
      "label": "Eligible successful events",
      "value": "4",
      "method": "Five unique records less one failed attempt.",
      "format": "#,##0"
    },
    {
      "label": "Captured net directional flow",
      "value": "60.000001 PAPER",
      "method": "(100000000 + 1 - 40000000) / 10^6; excludes SELF and FAILED.",
      "format": "#,##0"
    }
  ],
  "limitations": [
    "All network and address labels are fictional; no live-chain validation is implied.",
    "No opening balance, fiat price, or complete native-fee accounting is supplied.",
    "Explorer-style labels do not establish identity, intent, or legal status."
  ],
  "metadata": {
    "conclusion": "Six fictional capture rows reconcile to five unique records and four eligible successful events. Captured net directional flow is 60.000001 PAPER; it is not an ending balance, fiat value, or evidence of counterparty identity."
  },
  "report_narrative": [
    [
      "Six fictional capture rows reconcile to five unique records and four eligible successful events. Captured net directional flow is 60.000001 PAPER; it is not an ending balance, fiat value, or evidence of counterparty identity."
    ],
    [
      "The fictional EVM-style capture contains six raw rows for one token with six decimal places. Records are reconciled by event identity and execution status before directional amounts are summed; exact atomic values remain text."
    ],
    [
      "F-01: Six raw rows reconcile to five unique records and four eligible successful events.",
      "F-02: CP-B has an explorer-style label without supporting identity evidence.",
      "F-03: 100.000001 PAPER in less 40.000000 PAPER out equals 60.000001 PAPER under the stipulated method."
    ],
    [
      "One duplicate leaves five unique records. Four are successful eligible events; the failed 20.000000 PAPER attempt is excluded. The 5.000000 PAPER self transfer remains visible but does not inflate directional totals."
    ],
    [
      "Inbound 100.000001 PAPER less outbound 40.000000 PAPER produces captured net flow of 60.000001 PAPER. CP-B remains an unverified label; the tiny CP-C inbound transfer provides no identity or intent inference."
    ],
    [
      "SYN-001 supplies the raw captures, event identities and label assertion. No opening balance, fiat price, complete native-fee ledger or independent attribution evidence is supplied."
    ],
    [
      "Preserve duplicate lineage and exact units, obtain independent attribution before consequential reliance, and keep net captured flow separate from ending balance and fiat exposure."
    ],
    [
      "All network and address labels are fictional; no live-chain validation is implied.",
      "No opening balance, fiat price, or complete native-fee accounting is supplied.",
      "Explorer-style labels do not establish identity, intent, or legal status.",
      "QA remains pending and no authorized human disposition is recorded."
    ]
  ],
  "suite_id": "digital-asset-review",
  "version": "1.2.0",
  "notice": "Synthetic worked example. Fictional records. Not a completed operational review.",
  "as_of": "2026-10-09",
  "scope": "Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.",
  "conclusion": "Six fictional capture rows reconcile to five unique records and four eligible successful events. Captured net directional flow is 60.000001 PAPER; it is not an ending balance, fiat value, or evidence of counterparty identity.",
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
      "proposal": "Preserve duplicate lineage and failed-attempt exclusion.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-002",
      "finding_id": "F-02",
      "proposal": "Obtain independent attribution evidence before consequential reliance.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-003",
      "finding_id": "F-03",
      "proposal": "Keep balance, fiat value, and completeness limitations explicit.",
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
function caseErrors(d){
 const errors=[];const object=v=>v!==null&&typeof v==='object'&&!Array.isArray(v);
 const text=v=>typeof v==='string'&&v.trim().length>0;
 const validFormat=v=>text(v)&&[...v.matchAll(/\.([0#]+)/g)].every(m=>m[1].length<=15);
 if(!object(d))return ['case data must be an object'];
 for(const key of ['slug','suite_id','title','summary','audience','decision','palette','version','as_of','notice','scope','conclusion'])if(!text(d[key]))errors.push(key+' must be nonempty text');
 if(!/^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$/.test(d.slug||'')||d.suite_id!==d.slug)errors.push('invalid suite identity');
 if(!['slate','teal','indigo','umber'].includes(d.palette))errors.push('unknown palette');
 for(const key of ['report_sections','report_narrative','domain_tables','findings','evidence','metrics','limitations','methods','actions','qa'])if(!Array.isArray(d[key]))errors.push(key+' must be a list');
 if(errors.length)return errors;
 if(d.report_sections.length!==8||!d.report_sections.every(text)||new Set(d.report_sections).size!==8)errors.push('eight distinct report headings required');
 if(d.report_narrative.length!==8||!d.report_narrative.every(s=>Array.isArray(s)&&s.length&&s.every(text)))errors.push('eight populated narrative sections required');
 if(!d.methods.length||!d.methods.every(text)||!d.limitations.every(text))errors.push('invalid method or limitation text');
 const records=(key,fields)=>d[key].filter((row,index)=>{if(!object(row)||fields.some(f=>!(f in row))){errors.push(key+' row '+(index+1)+' missing required fields');return false;}return true;});
 const evidence=records('evidence',['id','title','locator','claim_class']);
 const findings=records('findings',['id','title','severity','confidence','claim_class','evidence_ids','detail','recommendation']);
 const ids=(rows,label)=>{const values=rows.map(r=>r.id);if(!values.every(text)||new Set(values).size!==values.length)errors.push('invalid or duplicate '+label+' ID');return new Set(values);};
 const evidenceIds=ids(evidence,'evidence'),findingIds=ids(findings,'finding');
 const classes=['Observed','Reported','Inferred','Estimated'];
 for(const e of evidence)if(!text(e.title)||!text(e.locator)||!classes.includes(e.claim_class))errors.push('invalid evidence record');
 for(const f of findings){
  if(!Array.isArray(f.evidence_ids)||!f.evidence_ids.length||f.evidence_ids.some(id=>!evidenceIds.has(id)))errors.push('unresolved finding evidence key');
  if(!['CRITICAL','HIGH','MEDIUM','LOW'].includes(f.severity)||!['HIGH','MODERATE','LOW','NOT ASSESSABLE'].includes(f.confidence)||!classes.includes(f.claim_class))errors.push('invalid finding classification');
  if(!['title','detail','recommendation'].every(k=>text(f[k])))errors.push('invalid finding text');
 }
 for(const m of records('metrics',['label','value','method'])){
  if(!text(m.label)||!text(m.method)||object(m.value)||Array.isArray(m.value))errors.push('invalid metric');
  if(m.format!==undefined&&!validFormat(m.format))errors.push('invalid metric format; at most 15 decimal places');
 }
 const actions=records('actions',['id','finding_id','proposal','owner','due_date','status']);ids(actions,'action');
 for(const a of actions)if(!findingIds.has(a.finding_id)||!text(a.proposal)||!['Proposed','Accepted','In progress','Blocked','Closed','Risk accepted'].includes(a.status)||['owner','due_date'].some(k=>a[k]!==null&&!text(a[k])))errors.push('invalid action or finding key');
 const qa=records('qa',['id','check','result','evidence']);ids(qa,'QA');
 for(const q of qa)if(!text(q.check)||!text(q.evidence)||!['PASS','FAIL','REVIEW REQUIRED','NOT RECORDED','NOT TESTED'].includes(q.result))errors.push('invalid QA record');
 if(d.domain_tables.length<2||d.domain_tables.length>12)errors.push('between two and twelve domain tables required');
 const names=new Set(['summary','dashboard','findings','evidence','actions','qa']);const tables=new Map();
 for(const [index,t] of d.domain_tables.entries()){
  if(!object(t)){errors.push('domain table must be an object');continue;}
  if(!text(t.name)||t.name.length>31||/[\\/*?:\[\]]/.test(t.name)||t.name.startsWith("'")||t.name.endsWith("'")||names.has(t.name.toLowerCase()))errors.push('invalid or duplicate sheet name');
  else{names.add(t.name.toLowerCase());tables.set(t.name,t);}
  if(!Array.isArray(t.columns)||!t.columns.length||!t.columns.every(text)||new Set(t.columns).size!==t.columns.length||!Array.isArray(t.rows)){errors.push('invalid domain columns or rows');continue;}
  if(![4,5].includes(t.report_section===undefined?(index===0?4:5):t.report_section))errors.push('invalid report_section');
  if(t.grain!==undefined&&!text(t.grain))errors.push('invalid grain');
  if(t.formats!==undefined&&(!object(t.formats)||Object.entries(t.formats).some(([k,v])=>!t.columns.includes(k)||!validFormat(v))))errors.push('invalid domain formats; at most 15 decimal places');
  const contract=t.column_contracts;
  if(contract!==undefined&&(!object(contract)||Object.keys(contract).length!==t.columns.length||t.columns.some(c=>!Object.hasOwn(contract,c)))){errors.push('incomplete column contracts');continue;}
  if(contract!==undefined&&t.primary_key===undefined)errors.push('typed table requires primary_key');
  const key=t.primary_key;
  if(key!==undefined&&(!Array.isArray(key)||!key.length||new Set(key).size!==key.length||key.some(k=>!t.columns.includes(k)))){errors.push('invalid primary_key');continue;}
  if(contract)for(const c of t.columns){const s=contract[c];if(!object(s)||!['text','integer','number','boolean'].includes(s.type)||typeof s.nullable!=='boolean'||!text(s.unit)||!text(s.description))errors.push('invalid field contract '+t.name+'.'+c);else{if(s.enum!==undefined&&(!Array.isArray(s.enum)||!s.enum.length||s.enum.some(v=>v===null||typeof v==='object')))errors.push('invalid field enum');if(Array.isArray(s.enum)){const validEnum=v=>s.type==='text'?typeof v==='string':s.type==='boolean'?typeof v==='boolean':s.type==='integer'?Number.isInteger(v):typeof v==='number';if(!s.enum.every(validEnum)||new Set(s.enum).size!==s.enum.length)errors.push('enum must contain distinct values of the declared type');}for(const bound of ['minimum','maximum'])if(s[bound]!==undefined&&(!['number','integer'].includes(s.type)||typeof s[bound]!=='number'||!Number.isFinite(s[bound])))errors.push('invalid numeric bound');if(typeof s.minimum==='number'&&typeof s.maximum==='number'&&s.minimum>s.maximum)errors.push('minimum exceeds maximum');}}
  const seen=new Set();
  for(const [ri,row] of t.rows.entries()){
   if(!Array.isArray(row)||row.length!==t.columns.length||row.some(v=>v!==null&&typeof v==='object')){errors.push('row width or scalar mismatch in '+t.name);continue;}
   if(key){const values=key.map(k=>row[t.columns.indexOf(k)]);if(values.some(v=>v===null||typeof v==='string'&&!v.trim()))errors.push('empty primary key in '+t.name);const token=JSON.stringify(values);if(seen.has(token))errors.push('duplicate primary key in '+t.name);seen.add(token);}
   row.forEach((value,ci)=>{
    const column=t.columns[ci],field=t.name+'.'+column;
    if((column==='evidence_id'||column.endsWith('_evidence_id')||column==='evidence_ids'||column.endsWith('_evidence_ids'))&&value!==null){const refs=typeof value==='string'?value.split(';').map(s=>s.trim()):[];if(!refs.length||refs.some(id=>!evidenceIds.has(id)))errors.push('unresolved domain evidence key in '+field);}
    if(!contract||!object(contract[column]))return;
    const s=contract[column];if(value===null){if(!s.nullable)errors.push('null prohibited in '+field);return;}
    const valid=s.type==='text'?typeof value==='string':s.type==='boolean'?typeof value==='boolean':s.type==='integer'?Number.isInteger(value):s.type==='number'?typeof value==='number':false;
    if(!valid){errors.push('wrong '+s.type+' type in '+field);return;}
    if(Array.isArray(s.enum)&&!s.enum.some(item=>typeof item===typeof value&&item===value))errors.push('value outside enum in '+field);
    if(typeof value==='number'&&(typeof s.minimum==='number'&&value<s.minimum||typeof s.maximum==='number'&&value>s.maximum))errors.push('value outside bounds in '+field);
   });
  }
 }
 for(const t of tables.values()){
  if(!Array.isArray(t.columns)||!Array.isArray(t.rows))continue;
  if(t.foreign_keys!==undefined&&!Array.isArray(t.foreign_keys)){errors.push('foreign_keys must be a list');continue;}
  for(const join of t.foreign_keys||[]){
   const target=object(join)?tables.get(join.table):null;
   if(!target||!Array.isArray(join.columns)||!join.columns.length||!Array.isArray(join.references)||join.columns.length!==join.references.length||join.columns.some(c=>!t.columns.includes(c))||!Array.isArray(target.columns)||!Array.isArray(target.rows)||join.references.some(c=>!target.columns.includes(c))){errors.push('invalid foreign key');continue;}
   const keys=target.rows.filter(r=>Array.isArray(r)&&r.length===target.columns.length).map(r=>JSON.stringify(join.references.map(c=>r[target.columns.indexOf(c)])));
   const keySet=new Set(keys);if(keySet.size!==keys.length){errors.push('foreign key target is not unique');continue;}
   for(const row of t.rows){if(!Array.isArray(row)||row.length!==t.columns.length)continue;const values=join.columns.map(c=>row[t.columns.indexOf(c)]);if(values.every(v=>v===null))continue;if(values.some(v=>v===null)||!keySet.has(JSON.stringify(values)))errors.push('unresolved domain foreign key in '+t.name);}
  }
 }
 function visit(v){if(typeof v==='number'&&!Number.isFinite(v))errors.push('non-finite number');else if(typeof v==='number'&&Number.isInteger(v)&&!Number.isSafeInteger(v))errors.push('unsafe integer; preserve exact digits as text');else if(typeof v==='string'&&/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(v))errors.push('unsupported control character');else if(Array.isArray(v))v.forEach(visit);else if(object(v))Object.values(v).forEach(visit);}
 function unicodeVisit(v){if(typeof v==='string'&&/[\uD800-\uDFFF\uFFFE\uFFFF]/u.test(v))errors.push('unsupported XML Unicode code point');else if(Array.isArray(v))v.forEach(unicodeVisit);else if(object(v))Object.values(v).forEach(unicodeVisit);}
 visit(d);unicodeVisit(d);return [...new Set(errors)];
}

let data;try{data=JSON.parse(document.getElementById('report-data').textContent);}catch{data=null;}
const byId=id=>document.getElementById(id);
const write=(id,value)=>{byId(id).textContent=value;};
const show=value=>value===null||value===undefined?'Not provided':Array.isArray(value)?value.join('; '):String(value);
function formatted(value,format){if(typeof value!=='number'||!format)return show(value);if(format==='0.0%')return(value*100).toFixed(1)+'%';if(format==='0.0"%"')return value.toFixed(1)+'%';const decimals=format.match(/\.([0#]+)/);const places=decimals?decimals[1].length:0;return(format.includes('$')?'$':'')+value.toLocaleString('en-US',{minimumFractionDigits:places,maximumFractionDigits:places});}
function table(target,columns,rows,caption,formats={}){
  const host=byId(target);host.replaceChildren();
  const wrap=document.createElement('div');wrap.className='table-wrap';wrap.tabIndex=0;wrap.setAttribute('role','region');wrap.setAttribute('aria-label',caption);
  const t=document.createElement('table');const cap=t.createCaption();cap.textContent=caption;
  const h=t.createTHead().insertRow();columns.forEach(c=>{const th=document.createElement('th');th.scope='col';th.textContent=c;h.append(th);});
  const body=t.createTBody();rows.forEach(row=>{const tr=body.insertRow();row.forEach((v,i)=>{const td=tr.insertCell();if(columns[i]==='severity'){const span=document.createElement('span');span.className='badge '+show(v).toLowerCase();span.textContent=show(v);td.append(span);}else{td.textContent=formatted(v,formats[columns[i]]);}});});
  wrap.append(t);host.append(wrap);
  if(!rows.length){const p=document.createElement("p");p.className="empty";p.textContent="No records in this view. This does not establish absence in the underlying population.";host.append(p);}
}
function chart(target,field,labels){const host=byId(target);const counts=labels.map(label=>data.findings.filter(f=>f[field]===label).length);const max=Math.max(1,...counts);labels.forEach((label,i)=>{const row=document.createElement('div');row.className='bar-row';const name=document.createElement('span');name.textContent=label;const track=document.createElement('div');track.className='bar-track';track.setAttribute('aria-hidden','true');const bar=document.createElement('div');bar.className='bar-fill';bar.style.width=(counts[i]/max*100)+'%';track.append(bar);const value=document.createElement('span');value.textContent=counts[i];row.append(name,track,value);host.append(row);});}
const findingColumns=['id','title','severity','confidence','claim_class','evidence_ids','detail','recommendation'];
let visible=[];
function renderFindings(){const q=byId('search').value.trim().toLowerCase();const level=byId('severity').value;visible=data.findings.filter(f=>(!level||f.severity===level)&&(!q||findingColumns.map(k=>show(f[k])).join(' ').toLowerCase().includes(q)));table('finding-table',findingColumns,visible.map(f=>findingColumns.map(k=>f[k])),'Finding register');write('filter-state',`${visible.length} of ${data.findings.length} findings visible. Coverage measures remain unfiltered.`);}
const caseProblems=caseErrors(data);
if(caseProblems.length){byId('notice').textContent='Case data rejected: '+caseProblems.join('; ');byId('main').replaceChildren();document.querySelectorAll('button,input,select').forEach(control=>control.disabled=true);}else{
write('identity',`${data.suite_id} / ${data.version} / As of ${data.as_of}`);write('title',data.title);write('subtitle',data.summary);write('notice',data.notice);write('decision-text',data.conclusion);write('scope',data.decision+' '+data.scope);
data.metrics.forEach(m=>{const box=document.createElement('div');box.className='metric';const label=document.createElement('span');label.textContent=m.label;const value=document.createElement('strong');value.textContent=formatted(m.value,m.format);const method=document.createElement('small');method.textContent=m.method;box.append(label,value,method);byId('metrics').append(box);});
chart('severity-chart','severity',['CRITICAL','HIGH','MEDIUM','LOW']);chart('confidence-chart','confidence',['HIGH','MODERATE','LOW','NOT ASSESSABLE']);
table('evidence-table',['id','title','locator','claim_class'],data.evidence.map(e=>[e.id,e.title,e.locator,e.claim_class]),'Evidence pointers');
data.domain_tables.forEach((t,i)=>{
 const id='domain-'+i;const section=document.createElement('section');section.id=id;section.dataset.domainTable=t.name;
 const heading=document.createElement('h2');heading.textContent=t.name;section.append(heading);
 if(t.grain){const grain=document.createElement('p');grain.className='meta';grain.textContent='Record grain: '+t.grain;section.append(grain);}
 const host=document.createElement('div');host.id=id+'-table';section.append(host);byId('domain-registers').append(section);
 const link=document.createElement('a');link.href='#'+id;link.textContent=t.name;byId('domain-navigation').append(link);
 table(host.id,t.columns,t.rows,t.name,t.formats||{});
 const counts=document.createElement('p');counts.className='meta';counts.textContent=`Domain record count: ${t.rows.length}. Missing (null) cells: ${t.rows.flat().filter(v=>v===null).length}. Empty text follows the field-specific contract.`;host.append(counts);
 if(t.column_contracts){const details=document.createElement('details');const summary=document.createElement('summary');summary.textContent='Field definitions and record keys';details.append(summary);const dictionary=document.createElement('dl');t.columns.forEach(column=>{const spec=t.column_contracts[column];const term=document.createElement('dt');term.textContent=column;const definition=document.createElement('dd');definition.textContent=`${spec.description} Type: ${spec.type}; unit: ${spec.unit}; nullable: ${spec.nullable}.`+(spec.enum?' Allowed values: '+spec.enum.map(show).join(', ')+'.':'');dictionary.append(term,definition);});details.append(dictionary);const keys=document.createElement('p');keys.textContent='Primary key: '+(t.primary_key||[]).join(' + ')+'. '+(t.foreign_keys||[]).map(j=>j.columns.join(' + ')+' refers to '+j.table+' ('+j.references.join(' + ')+').').join(' ');details.append(keys);section.append(details);}
});
const narrativeTargets=['decision','method','findings','domain-registers','domain-registers','evidence','actions','limitations'];
data.report_narrative.forEach((paragraphs,index)=>{const box=document.createElement('details');box.dataset.narrativeSection=String(index);box.open=true;const title=document.createElement('summary');title.textContent=data.report_sections[index];box.append(title);paragraphs.forEach(value=>{const p=document.createElement('p');p.textContent=value;box.append(p);});byId(narrativeTargets[index]).append(box);});
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
byId('case-export').addEventListener('click',()=>{const url=URL.createObjectURL(new Blob([JSON.stringify(data,null,2)+'\n'],{type:'application/json;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download=data.suite_id+'-complete-case.json';document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);});
let beforePrint=null;window.addEventListener('beforeprint',()=>{beforePrint={query:byId('search').value,severity:byId('severity').value};byId('search').value='';byId('severity').value='';renderFindings();});window.addEventListener('afterprint',()=>{if(beforePrint){byId('search').value=beforePrint.query;byId('severity').value=beforePrint.severity;renderFindings();beforePrint=null;}});byId('print').addEventListener('click',()=>window.print());renderFindings();
}
</script>
</body>
</html>

```

## Acceptance and delivery

Open the actual file. Check both themes, desktop and narrow screens, keyboard navigation, visible focus, long evidence strings, missing values, empty filters, reset, CSV scope and print preview. Reconcile every displayed metric and chart to its input rows. Verify no network resources are requested. Rendering success does not establish evidence quality or analytical validity. Record untested browser/platform behavior honestly. If a browser blocks downloads or scripting, use the unchanged source data and fixed report/workbook alternatives; do not invent a functioning control.
