# Jurisdiction Risk and Exposure Review — complete dashboard template

Version 1.1.0. Use the complete HTML below to create a single downloadable `.html` file in the current session. It includes all style and interaction code. No hosted assets, fonts, CDN, installation, repository access, API key or local server is needed. Where a file tool is unavailable, return the complete HTML as copy-ready text and explicitly state that no file was created.

## Design and behavior contract

| Element | Light | Dark |
| --- | --- | --- |
| Page | `#E4E7E7` muted gray | `#263746` softened navy |
| Panels | `#F1F2EF` stone | `#304655` slate navy |
| Text | `#243641` | `#EFF1EF` |
| Secondary text | `#4E606A` | `#C0CDD3` |
| Suite accent | `#276357` | `#a7d8c7` |
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
<title>Jurisdiction Risk and Exposure Review</title>
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
  "slug": "jurisdiction-risk",
  "title": "Jurisdiction Risk and Exposure Review",
  "summary": "Map jurisdiction-related exposure while separating strategic AML deficiencies, sanctions scope, governance context, and evidence gaps.",
  "audience": "Analysts preparing generic geographic exposure and jurisdiction review drafts",
  "decision": "Which geographic exposures and legal-scope questions need additional review, without turning a country label into a customer decision?",
  "palette": "teal",
  "report_sections": [
    "Jurisdiction exposure conclusion",
    "Scope dates and allocation method",
    "Material geographic findings",
    "Jurisdiction context assessment",
    "Exposure allocation and overlap",
    "Source applicability and uncertainty",
    "Proposed specialist and evidence actions",
    "Limitations quality review and human disposition"
  ],
  "domain_tables": [
    {
      "name": "JurisdictionFactors",
      "columns": [
        "jurisdiction_id",
        "aml_category",
        "sanctions_scope",
        "corruption_context",
        "source_date",
        "as_of_date",
        "evidence_ids",
        "limitation"
      ],
      "rows": [
        [
          "J-A",
          "NONE_IN_FIXTURE",
          "NO_PROGRAM_QUESTION_IN_FIXTURE",
          "Lower fictional concern",
          "2026-09-15",
          "2026-09-30",
          "SYN-001",
          "Invented jurisdiction; no real-world status asserted"
        ],
        [
          "J-B",
          "INCREASED_MONITORING_FIXTURE",
          "NO_PROGRAM_QUESTION_IN_FIXTURE",
          "Moderate fictional concern",
          "2026-09-15",
          "2026-09-30",
          "SYN-001",
          "Strategic-deficiency context is separate from sanctions"
        ],
        [
          "J-C",
          "CALL_FOR_ACTION_FIXTURE",
          "NO_PROGRAM_QUESTION_IN_FIXTURE",
          "Higher fictional concern",
          "2026-09-15",
          "2026-09-30",
          "SYN-001",
          "Illustrative category requires contextual review, not automatic exclusion"
        ],
        [
          "J-D",
          "NONE_IN_FIXTURE",
          "SCOPE_REVIEW_REQUIRED",
          "Moderate fictional concern",
          "2026-09-15",
          "2026-09-30",
          "SYN-001",
          "Fictional sector-related restriction question; applicability unresolved"
        ]
      ]
    },
    {
      "name": "ExposureMapping",
      "columns": [
        "exposure_id",
        "subject_id",
        "destination_id",
        "intermediary_id",
        "amount",
        "currency",
        "exposure_role",
        "include_in_total",
        "evidence_ids",
        "notes"
      ],
      "rows": [
        [
          "T01",
          "C01",
          "J-A",
          "J-A",
          100000,
          "USD",
          "BENEFICIARY_JURISDICTION",
          true,
          "SYN-002",
          "Single transfer; intermediary not a second payment"
        ],
        [
          "T02",
          "C01",
          "J-B",
          "J-A",
          200000,
          "USD",
          "BENEFICIARY_JURISDICTION",
          true,
          "SYN-002",
          "Single transfer; intermediary not a second payment"
        ],
        [
          "T03",
          "C02",
          "J-C",
          "J-D",
          150000,
          "USD",
          "BENEFICIARY_JURISDICTION",
          true,
          "SYN-002",
          "Single transfer; intermediary not a second payment"
        ],
        [
          "T04",
          "C02",
          "J-B",
          "J-A",
          50000,
          "USD",
          "BENEFICIARY_JURISDICTION",
          true,
          "SYN-002",
          "Single transfer; intermediary not a second payment"
        ],
        [
          "T05",
          "C03",
          null,
          "J-A",
          100000,
          "USD",
          "BENEFICIARY_JURISDICTION",
          true,
          "SYN-002",
          "Destination not supplied; retained in total"
        ],
        [
          "T06",
          "C03",
          "J-D",
          "J-A",
          250000,
          "USD",
          "BENEFICIARY_JURISDICTION",
          true,
          "SYN-002",
          "Single transfer; intermediary not a second payment"
        ],
        [
          "T07",
          "C04",
          "J-A",
          "J-A",
          50000,
          "USD",
          "BENEFICIARY_JURISDICTION",
          true,
          "SYN-002",
          "Single transfer; intermediary not a second payment"
        ],
        [
          "T08",
          "C04",
          "J-C",
          "J-A",
          100000,
          "USD",
          "BENEFICIARY_JURISDICTION",
          true,
          "SYN-002",
          "Single transfer; intermediary not a second payment"
        ]
      ],
      "formats": {
        "amount": "#,##0.00"
      }
    }
  ],
  "findings": [
    {
      "id": "JR-F01",
      "title": "Unknown destination remains a material exposure gap",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-002"
      ],
      "detail": "$100,000.00 of the $1,000,000.00 fictional transfer population has no beneficiary jurisdiction.",
      "recommendation": "Resolve T05 destination without excluding it from the total."
    },
    {
      "id": "JR-F02",
      "title": "Destination and any-nexus exposure use different inclusion rules",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001",
        "SYN-002"
      ],
      "detail": "J-D receives $250,000.00 as destination, while its destination-or-intermediary union is $400,000.00.",
      "recommendation": "Preserve role-specific and union calculations; deduplicate T03 and T06."
    },
    {
      "id": "JR-F03",
      "title": "Fictional sanctions scope question is unresolved",
      "severity": "HIGH",
      "confidence": "MODERATE",
      "claim_class": "Inferred",
      "evidence_ids": [
        "SYN-001",
        "SYN-002"
      ],
      "detail": "J-D has a fictional sector-related restriction question; neither country presence nor absence from an AML category resolves transaction applicability.",
      "recommendation": "Obtain the relevant authoritative rule and transaction facts for specialist review."
    }
  ],
  "evidence": [
    {
      "id": "SYN-001",
      "title": "Fictional four-jurisdiction context snapshots",
      "locator": "10-worked-example.md, full context population",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-002",
      "title": "Fictional eight-transfer exposure ledger",
      "locator": "10-worked-example.md, full transfer population",
      "claim_class": "Observed"
    },
    {
      "id": "REF-FATF",
      "title": "FATF monitored-jurisdiction category descriptions",
      "locator": "https://www.fatf-gafi.org/en/countries/black-and-grey-lists.html",
      "claim_class": "Observed"
    },
    {
      "id": "REF-OFAC",
      "title": "OFAC sanctions programs and country information",
      "locator": "https://ofac.treasury.gov/sanctions-programs-and-country-information",
      "claim_class": "Observed"
    },
    {
      "id": "REF-WGI",
      "title": "World Bank Worldwide Governance Indicators and usage advisory",
      "locator": "https://www.worldbank.org/en/publication/worldwide-governance-indicators",
      "claim_class": "Observed"
    }
  ],
  "metrics": [
    {
      "label": "Total supplied transfers",
      "value": "$1,000,000.00",
      "method": "Sum of eight unique USD transfers T01\u2013T08; no FX required.",
      "format": "#,##0"
    },
    {
      "label": "Destination mapped",
      "value": "$900,000.00 (90.0%)",
      "method": "Transfers with a supplied destination / all $1,000,000.00; unknown T05 remains in denominator.",
      "format": "#,##0"
    },
    {
      "label": "J-D any-nexus union",
      "value": "$400,000.00 (40.0%)",
      "method": "Unique IDs T03 and T06 with J-D as destination or intermediary / total $1,000,000.00.",
      "format": "#,##0"
    }
  ],
  "limitations": [
    "All jurisdiction identifiers, category assignments, and transfer records are fictional.",
    "No current live country list or actual sanctions determination is supplied.",
    "Country context, nationality, and payment routing do not establish individual wrongdoing.",
    "Destination and intermediary exposures overlap; role totals are not additive.",
    "The unknown destination could change category allocations and remains in the denominator."
  ],
  "conclusion": "The fictional transfer population totals $1,000,000.00, with $100,000.00 of destination exposure unresolved. J-D accounts for 25.0% by destination and 40.0% by unique destination-or-intermediary nexus; its separate sanctions-scope question requires specialist review.",
  "report_narrative": [
    [
      "The fictional transfer population totals $1,000,000.00, with $100,000.00 of destination exposure unresolved. J-D accounts for 25.0% by destination and 40.0% by unique destination-or-intermediary nexus; its separate sanctions-scope question requires specialist review."
    ],
    [
      "The cutoff is Sep 30, 2026. Eight unique transfers in USD form the monetary denominator. Beneficiary jurisdiction is the primary allocation role; intermediary jurisdiction is a separate overlapping role. No actual-country statuses or present-day legal conclusions are imported."
    ],
    [
      "T05 is unmapped by destination and remains $100,000.00 of the total. J-B and J-C each receive $250,000.00 under different fictional AML-context categories. J-D raises a separate sector-related scope question that neither AML category resolves."
    ],
    [
      "The four snapshots keep AML strategic-deficiency context, sanctions-scope status, and corruption-related context in separate fields. J-A has no fixture category, J-B has an increased-monitoring fixture label, J-C a call-for-action fixture label, and J-D a distinct unresolved scope question."
    ],
    [
      "Destination allocation is J-A $150,000.00, J-B $250,000.00, J-C $250,000.00, J-D $250,000.00, and unknown $100,000.00. J-D appears on T03 as intermediary and T06 as destination, producing a deduplicated union of $400,000.00.",
      "Under the separate missing-destination scenario, allocating all of T05's $100,000.00 to J-D raises J-D destination exposure from $250,000.00/$1,000,000.00 = 25.0% to $350,000.00/$1,000,000.00 = 35.0%. Allocating none to J-D preserves 25.0%. The 25.0%\u201335.0% range is deterministic sensitivity, with no assigned probabilities; the observed baseline remains unchanged (SYN-002)."
    ],
    [
      "SYN-001 defines invented context and SYN-002 defines all transfers. FATF category descriptions, OFAC program scope, and the World Bank usage advisory were reviewed for methodological distinctions. They do not establish any fictional jurisdiction status or replace a current rule applicability review."
    ],
    [
      "Resolve T05 destination and review T03/T06 transaction roles, sector facts, parties, dates, and applicable authority. Preserve both destination and any-nexus views. Propose targeted diligence and specialist assessment without an automatic customer outcome."
    ],
    [
      "QA must reconcile eight IDs, the $1,000,000.00 total, the $900,000.00 mapped amount, and the $400,000.00 J-D union. Dynamic country statements, legal applicability, and human disposition remain outside this fictional result."
    ]
  ],
  "as_of": "2026-09-30",
  "scope": "Eight fictional USD transfers at the Sep 30, 2026 review cutoff; four invented jurisdiction snapshots dated Sep 15, 2026. Beneficiary jurisdiction is the primary additive role.",
  "suite_id": "jurisdiction-risk",
  "version": "1.1.0",
  "notice": "Synthetic worked example. Fictional records. Not a completed operational review.",
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
      "finding_id": "JR-F01",
      "proposal": "Resolve T05 destination without excluding it from the total.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-002",
      "finding_id": "JR-F02",
      "proposal": "Preserve role-specific and union calculations; deduplicate T03 and T06.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-003",
      "finding_id": "JR-F03",
      "proposal": "Obtain the relevant authoritative rule and transaction facts for specialist review.",
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
function formatted(value,format){if(typeof value!=='number'||!format)return show(value);if(format==='0.0%')return(value*100).toFixed(1)+'%';if(format==='0.0"%"')return value.toFixed(1)+'%';const decimals=format.match(/\.([0#]+)/);const places=decimals?decimals[1].length:0;return(format.includes('$')?'$':'')+value.toLocaleString('en-US',{minimumFractionDigits:places,maximumFractionDigits:places});}
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
