# Customer Risk Review — complete dashboard template

Version 1.1.0. Use the complete HTML below to create a single downloadable `.html` file in the current session. It includes all style and interaction code. No hosted assets, fonts, CDN, installation, repository access, API key or local server is needed. Where a file tool is unavailable, return the complete HTML as copy-ready text and explicitly state that no file was created.

## Design and behavior contract

| Element | Light | Dark |
| --- | --- | --- |
| Page | `#E4E7E7` muted gray | `#263746` softened navy |
| Panels | `#F1F2EF` stone | `#304655` slate navy |
| Text | `#243641` | `#EFF1EF` |
| Secondary text | `#4E606A` | `#C0CDD3` |
| Suite accent | `#735327` | `#e9d3aa` |
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
<title>Customer Risk Review</title>
<style>
:root{--bg:#e4e7e7;--panel:#f1f2ef;--ink:#243641;--muted:#4e606a;--line:#9baab0;--accent:#735327;--soft:#d4dee2;--high:#8a3439;--medium:#735119;--low:#315f54;--focus:#005f9c;--radius:8px}
:root[data-theme=dark]{--bg:#263746;--panel:#304655;--ink:#eff1ef;--muted:#c0cdd3;--line:#6b8291;--accent:#e9d3aa;--soft:#3c5667;--high:#ffb8b8;--medium:#f0d393;--low:#b1dcc9;--focus:#9bd3fa}
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
  "slug": "customer-risk-review",
  "title": "Customer Risk Review",
  "summary": "Review a customer profile with transparent factor weighting, evidence gaps, material exceptions, and human rating decisions.",
  "audience": "Analysts preparing generic customer risk review drafts",
  "decision": "What review priority and additional evidence are supported, and which rating decisions remain for an authorized human?",
  "palette": "umber",
  "report_sections": [
    "Customer review conclusion",
    "Population scope and scoring method",
    "Material profile findings",
    "Customer factor assessment",
    "Evidence completeness and review priorities",
    "Evidence provenance and alternatives",
    "Proposed review actions",
    "Limitations quality review and human disposition"
  ],
  "domain_tables": [
    {
      "name": "CustomerFactors",
      "columns": [
        "factor_id",
        "customer_id",
        "dimension",
        "weight",
        "factor_value",
        "contribution",
        "evidence_ids",
        "notes"
      ],
      "rows": [
        [
          "C01-1",
          "C01",
          "business",
          0.3,
          1,
          10.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C01-2",
          "C01",
          "product",
          0.25,
          1,
          8.333333333333332,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C01-3",
          "C01",
          "geography",
          0.2,
          0,
          0.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C01-4",
          "C01",
          "channel",
          0.15,
          1,
          5.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C01-5",
          "C01",
          "ownership",
          0.1,
          0,
          0.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C02-1",
          "C02",
          "business",
          0.3,
          2,
          20.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C02-2",
          "C02",
          "product",
          0.25,
          2,
          16.666666666666664,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C02-3",
          "C02",
          "geography",
          0.2,
          1,
          6.666666666666667,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C02-4",
          "C02",
          "channel",
          0.15,
          2,
          10.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C02-5",
          "C02",
          "ownership",
          0.1,
          1,
          3.3333333333333335,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C03-1",
          "C03",
          "business",
          0.3,
          3,
          30.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C03-2",
          "C03",
          "product",
          0.25,
          2,
          16.666666666666664,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C03-3",
          "C03",
          "geography",
          0.2,
          2,
          13.333333333333334,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C03-4",
          "C03",
          "channel",
          0.15,
          1,
          5.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C03-5",
          "C03",
          "ownership",
          0.1,
          3,
          10.000000000000002,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C04-1",
          "C04",
          "business",
          0.3,
          1,
          10.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C04-2",
          "C04",
          "product",
          0.25,
          1,
          8.333333333333332,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C04-3",
          "C04",
          "geography",
          0.2,
          null,
          null,
          "SYN-001",
          "NOT SUPPLIED"
        ],
        [
          "C04-4",
          "C04",
          "channel",
          0.15,
          1,
          5.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C04-5",
          "C04",
          "ownership",
          0.1,
          1,
          3.3333333333333335,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C05-1",
          "C05",
          "business",
          0.3,
          1,
          10.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C05-2",
          "C05",
          "product",
          0.25,
          0,
          0.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C05-3",
          "C05",
          "geography",
          0.2,
          0,
          0.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C05-4",
          "C05",
          "channel",
          0.15,
          0,
          0.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C05-5",
          "C05",
          "ownership",
          0.1,
          0,
          0.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C06-1",
          "C06",
          "business",
          0.3,
          2,
          20.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C06-2",
          "C06",
          "product",
          0.25,
          1,
          8.333333333333332,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C06-3",
          "C06",
          "geography",
          0.2,
          2,
          13.333333333333334,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C06-4",
          "C06",
          "channel",
          0.15,
          2,
          10.0,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ],
        [
          "C06-5",
          "C06",
          "ownership",
          0.1,
          1,
          3.3333333333333335,
          "SYN-001",
          "Fictional rubric assignment; not calibrated"
        ]
      ],
      "formats": {
        "weight": "0.0%",
        "factor_value": "0.0",
        "contribution": "0.0"
      }
    },
    {
      "name": "ReviewOutcomes",
      "columns": [
        "customer_id",
        "illustrative_score",
        "illustrative_band",
        "complete_items",
        "required_items",
        "completeness",
        "material_gap",
        "review_priority",
        "evidence_ids",
        "rationale"
      ],
      "rows": [
        [
          "C01",
          23.333333333333332,
          "LOW",
          4,
          4,
          1.0,
          "NONE",
          "STANDARD",
          "SYN-001",
          "All four evidence items supplied"
        ],
        [
          "C02",
          56.666666666666664,
          "MODERATE",
          4,
          4,
          1.0,
          "NONE",
          "HEIGHTENED",
          "SYN-001",
          "Complexity warrants contextual review"
        ],
        [
          "C03",
          75.0,
          "HIGH",
          3,
          4,
          0.75,
          "Ownership rights unresolved",
          "SPECIALIST",
          "SYN-001",
          "High illustrative band and material ownership gap"
        ],
        [
          "C04",
          null,
          "INCOMPLETE",
          2,
          4,
          0.5,
          "Geography input, ownership evidence and funds explanation missing",
          "INCOMPLETE",
          "SYN-001",
          "No complete score; prioritize missing information"
        ],
        [
          "C05",
          10.0,
          "LOW",
          3,
          4,
          0.75,
          "Third-party source of funds unsupported",
          "TARGETED",
          "SYN-001",
          "Low illustrative score cannot close a material funds gap"
        ],
        [
          "C06",
          54.99999999999999,
          "MODERATE",
          4,
          4,
          1.0,
          "Control operating exceptions in separate sample",
          "HEIGHTENED",
          "SYN-001;SYN-002",
          "No arithmetic control discount; examine exception relevance"
        ]
      ],
      "formats": {
        "illustrative_score": "0.0",
        "completeness": "0.0%"
      }
    }
  ],
  "findings": [
    {
      "id": "CR-F01",
      "title": "One incomplete score remains outside band counts",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001"
      ],
      "detail": "C04 lacks its geography factor. The possible score spans 26.7 to 46.7 and crosses LOW/MODERATE boundaries.",
      "recommendation": "Obtain the missing factor evidence; preserve an incomplete result."
    },
    {
      "id": "CR-F02",
      "title": "Low illustrative score does not settle funds provenance",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001"
      ],
      "detail": "C05 scores 10.0 but lacks support for a planned third-party source of funds.",
      "recommendation": "Request a targeted funds explanation and preserve the unresolved disposition."
    },
    {
      "id": "CR-F03",
      "title": "Control claims cannot be converted to a score discount",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001",
        "SYN-002"
      ],
      "detail": "C06 has two exceptions among eight fictional control checks; the sample has no demonstrated population representativeness.",
      "recommendation": "Investigate the exceptions and their coverage before relying on the control."
    }
  ],
  "evidence": [
    {
      "id": "SYN-001",
      "title": "Fictional six-customer profiles and factor rubric",
      "locator": "10-worked-example.md, complete customer population",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-002",
      "title": "Fictional eight-check control sample for C06",
      "locator": "10-worked-example.md, complete control sample",
      "claim_class": "Observed"
    },
    {
      "id": "REF-CDD",
      "title": "FFIEC Customer Due Diligence overview",
      "locator": "https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/02",
      "claim_class": "Observed"
    },
    {
      "id": "REF-RISK",
      "title": "FFIEC BSA/AML Risk Assessment overview",
      "locator": "https://bsaaml.ffiec.gov/manual/BSAAMLRiskAssessment/01",
      "claim_class": "Observed"
    }
  ],
  "metrics": [
    {
      "label": "Computable illustrative scores",
      "value": "5 of 6 (83.3%)",
      "method": "Customers with all five factor values / six supplied customers; C04 remains incomplete.",
      "format": "#,##0"
    },
    {
      "label": "Evidence completeness",
      "value": "20 of 24 (83.3%)",
      "method": "Sum of supplied decision-evidence items / four expected items per customer \u00d7 six customers.",
      "format": "#,##0"
    },
    {
      "label": "C06 sample exceptions",
      "value": "2 of 8 (25.0%)",
      "method": "Exception checks K03 and K07 / all eight supplied checks; descriptive sample rate only.",
      "format": "#,##0"
    }
  ],
  "limitations": [
    "Scores and bands are illustrative ordering conventions, not calibrated AML probabilities.",
    "An incomplete score and a material evidence gap cannot be treated as approval.",
    "The C06 sample does not establish live control effectiveness or population exception rates.",
    "No customer rating, onboarding, restriction, exit, or filing decision is authorized."
  ],
  "conclusion": "Five of six fictional profiles have computable illustrative scores; C04 remains incomplete. C05 requires targeted funds review despite its low score, and C06 control exceptions require investigation without a numeric discount.",
  "report_narrative": [
    [
      "Five of six fictional profiles have computable illustrative scores; C04 remains incomplete. C05 requires targeted funds review despite its low score, and C06 control exceptions require investigation without a numeric discount."
    ],
    [
      "The six customer profiles use five fixed factors weighted 30%, 25%, 20%, 15%, and 10%. Values range from zero to three; contributions equal value \u00d7 weight / 3 \u00d7 100. Evidence completeness uses a separate four-item checklist per customer."
    ],
    [
      "C04 has no geography value and cannot receive a complete band. C05 has an unsupported planned third-party receipt that the score does not resolve. C06 has two control exceptions among eight checks, with no demonstrated representativeness."
    ],
    [
      "Complete scores are C01 23.3, C02 56.7, C03 75.0, C05 10.0, and C06 55.0. C04 has an illustrative possible range from 26.7 to 46.7; no midpoint or reweighted score is assigned."
    ],
    [
      "Twenty of twenty-four expected evidence items are supplied. C03 remains subject to ownership review, C04 is incomplete, C05 receives targeted funds review, and C06 remains subject to control exception review. The low-band count is two among five complete scores, not two approved customers.",
      "SYN-002 preserves all eight targeted C06 checks: K01 NO EXCEPTION (review field present); K02 NO EXCEPTION (review field present); K03 EXCEPTION (review timestamp absent); K04 NO EXCEPTION (review field present); K05 NO EXCEPTION (review field present); K06 NO EXCEPTION (review field present); K07 EXCEPTION (escalation rationale absent); K08 NO EXCEPTION (review field present). Thus 2/8 = 25.0% have recorded exceptions. Selection is targeted; the larger operating population is unknown."
    ],
    [
      "SYN-001 supplies all profiles, rubric assignments, and evidence checklist statuses. SYN-002 supplies the complete eight-check sample. FFIEC references provide public U.S. bank context; they do not prescribe these weights, bands, or customer dispositions."
    ],
    [
      "Propose evidence requests for C03 ownership, C04 geography, ownership and funds explanation, and C05 funds provenance. Examine C06 exceptions and control scope. Retain all numeric and narrative differences for the human rating reviewer."
    ],
    [
      "QA must reproduce the five scores, the C04 range, the twenty-of-twenty-four evidence count, and two-of-eight exceptions. These are fictional consistency tests; independent review and actual customer decisions remain unrecorded."
    ]
  ],
  "as_of": "2026-09-30",
  "scope": "Six fictional customer relationships at Sep 30, 2026, with five factor assignments and four evidence expectations each; a separate eight-check C06 sample is descriptive only.",
  "suite_id": "customer-risk-review",
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
      "finding_id": "CR-F01",
      "proposal": "Obtain the missing factor evidence; preserve an incomplete result.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-002",
      "finding_id": "CR-F02",
      "proposal": "Request a targeted funds explanation and preserve the unresolved disposition.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-003",
      "finding_id": "CR-F03",
      "proposal": "Investigate the exceptions and their coverage before relying on the control.",
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
