# Monitoring Scenario and Threshold Review — complete dashboard template

Version 1.2.0. Use the complete HTML below to create a single downloadable `.html` file in the current session. It includes all style and interaction code. No hosted assets, fonts, CDN, installation, repository access, API key or local server is needed. Where a file tool is unavailable, return the complete HTML as copy-ready text and explicitly state that no file was created.

## Design and behavior contract

| Element | Light | Dark |
| --- | --- | --- |
| Page | `#E4E7E7` muted gray | `#263746` softened navy |
| Panels | `#F1F2EF` stone | `#304655` slate navy |
| Text | `#243641` | `#EFF1EF` |
| Secondary text | `#4E606A` | `#C0CDD3` |
| Suite accent | `#4c5180` | `#c7cdf2` |
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
<title>Monitoring Scenario and Threshold Review</title>
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
  "slug": "monitoring-tuning",
  "title": "Monitoring Scenario and Threshold Review",
  "summary": "Evaluate complete monitoring candidates through protected partitions, labels, routing, workload, below-threshold review and human change gates.",
  "audience": "Monitoring analysts, independent challenge reviewers and accountable human decision makers",
  "decision": "Which frozen candidate merits further validation, and which data, routing or governance gaps block a human change decision?",
  "palette": "indigo",
  "as_of": "2026-10-09",
  "scope": "Complete fictional inputs printed in file 10 only. Public authorities provide context, not evidence about the fictional subjects or an institution-specific mandate.",
  "report_sections": [
    "Candidate recommendation and restrictions",
    "Evaluation scope and partition controls",
    "Coverage workload and routing findings",
    "Complete candidate and population registers",
    "Below-threshold review and decision gates",
    "Evidence provenance uncertainty and blind spots",
    "Validation and change proposals",
    "Limitations quality review and human disposition"
  ],
  "domain_tables": [
    {
      "name": "Population",
      "columns": [
        "unit_id",
        "group_id",
        "partition",
        "segment",
        "score",
        "label",
        "label_basis",
        "eligible",
        "suppressed",
        "review_hours",
        "evidence_ids"
      ],
      "column_contracts": {
        "unit_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "One scored customer-window; never a transaction count."
        },
        "group_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Frozen merge/dependence group containing two units in one partition."
        },
        "partition": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Prospectively assigned evaluation partition.",
          "enum": [
            "TRAIN",
            "VALIDATION",
            "HOLDOUT"
          ]
        },
        "segment": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Frozen customer segment.",
          "enum": [
            "RETAIL",
            "SMALL_BUSINESS",
            "CORRESPONDENT"
          ]
        },
        "score": {
          "type": "number",
          "nullable": false,
          "unit": "score",
          "description": "Supplied deterministic score on a 0 to 100 scale."
        },
        "label": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Available fictional review outcome as of cutoff.",
          "enum": [
            "POSITIVE",
            "NEGATIVE",
            "UNKNOWN",
            "CENSORED"
          ]
        },
        "label_basis": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Provenance or reason the label is not mature."
        },
        "eligible": {
          "type": "boolean",
          "nullable": false,
          "unit": "flag",
          "description": "Whether the supplied unit meets the frozen population predicate."
        },
        "suppressed": {
          "type": "boolean",
          "nullable": false,
          "unit": "flag",
          "description": "Whether group G17 is removed by the illustrative suppression list."
        },
        "review_hours": {
          "type": "number",
          "nullable": false,
          "unit": "hours",
          "description": "Fixed lead-case workload assumption by segment, before merge additions."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Supporting synthetic source IDs."
        }
      },
      "primary_key": [
        "unit_id"
      ],
      "rows": [
        [
          "U01",
          "G01",
          "TRAIN",
          "RETAIL",
          82,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          1,
          "SYN-001"
        ],
        [
          "U02",
          "G01",
          "TRAIN",
          "RETAIL",
          67,
          "NEGATIVE",
          "Fictional closed review",
          true,
          false,
          1,
          "SYN-001"
        ],
        [
          "U03",
          "G02",
          "TRAIN",
          "RETAIL",
          56,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          1,
          "SYN-001"
        ],
        [
          "U04",
          "G02",
          "TRAIN",
          "RETAIL",
          32,
          "NEGATIVE",
          "Fictional closed review",
          true,
          false,
          1,
          "SYN-001"
        ],
        [
          "U05",
          "G03",
          "TRAIN",
          "SMALL_BUSINESS",
          88,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          1.5,
          "SYN-001"
        ],
        [
          "U06",
          "G03",
          "TRAIN",
          "SMALL_BUSINESS",
          72,
          "NEGATIVE",
          "Fictional closed review",
          true,
          false,
          1.5,
          "SYN-001"
        ],
        [
          "U07",
          "G04",
          "TRAIN",
          "SMALL_BUSINESS",
          58,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          1.5,
          "SYN-001"
        ],
        [
          "U08",
          "G04",
          "TRAIN",
          "SMALL_BUSINESS",
          44,
          "UNKNOWN",
          "Review evidence unavailable",
          true,
          false,
          1.5,
          "SYN-001"
        ],
        [
          "U09",
          "G05",
          "TRAIN",
          "CORRESPONDENT",
          93,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          2,
          "SYN-001"
        ],
        [
          "U10",
          "G05",
          "TRAIN",
          "CORRESPONDENT",
          77,
          "NEGATIVE",
          "Fictional closed review",
          true,
          false,
          2,
          "SYN-001"
        ],
        [
          "U11",
          "G06",
          "TRAIN",
          "CORRESPONDENT",
          63,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          2,
          "SYN-001"
        ],
        [
          "U12",
          "G06",
          "TRAIN",
          "CORRESPONDENT",
          39,
          "CENSORED",
          "Outcome window not mature",
          true,
          false,
          2,
          "SYN-001"
        ],
        [
          "U13",
          "G07",
          "VALIDATION",
          "RETAIL",
          79,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          1,
          "SYN-001"
        ],
        [
          "U14",
          "G07",
          "VALIDATION",
          "RETAIL",
          64,
          "NEGATIVE",
          "Fictional closed review",
          true,
          false,
          1,
          "SYN-001"
        ],
        [
          "U15",
          "G08",
          "VALIDATION",
          "RETAIL",
          54,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          1,
          "SYN-001"
        ],
        [
          "U16",
          "G08",
          "VALIDATION",
          "RETAIL",
          28,
          "NEGATIVE",
          "Fictional closed review",
          true,
          false,
          1,
          "SYN-001"
        ],
        [
          "U17",
          "G09",
          "VALIDATION",
          "SMALL_BUSINESS",
          86,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          1.5,
          "SYN-001"
        ],
        [
          "U18",
          "G09",
          "VALIDATION",
          "SMALL_BUSINESS",
          69,
          "NEGATIVE",
          "Fictional closed review",
          true,
          false,
          1.5,
          "SYN-001"
        ],
        [
          "U19",
          "G10",
          "VALIDATION",
          "SMALL_BUSINESS",
          57,
          "UNKNOWN",
          "Review evidence unavailable",
          true,
          false,
          1.5,
          "SYN-001"
        ],
        [
          "U20",
          "G10",
          "VALIDATION",
          "SMALL_BUSINESS",
          42,
          "NEGATIVE",
          "Fictional closed review",
          true,
          false,
          1.5,
          "SYN-001"
        ],
        [
          "U21",
          "G11",
          "VALIDATION",
          "CORRESPONDENT",
          91,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          2,
          "SYN-001"
        ],
        [
          "U22",
          "G11",
          "VALIDATION",
          "CORRESPONDENT",
          74,
          "NEGATIVE",
          "Fictional closed review",
          true,
          false,
          2,
          "SYN-001"
        ],
        [
          "U23",
          "G12",
          "VALIDATION",
          "CORRESPONDENT",
          61,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          2,
          "SYN-001"
        ],
        [
          "U24",
          "G12",
          "VALIDATION",
          "CORRESPONDENT",
          36,
          "CENSORED",
          "Outcome window not mature",
          true,
          false,
          2,
          "SYN-001"
        ],
        [
          "U25",
          "G13",
          "HOLDOUT",
          "RETAIL",
          81,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          1,
          "SYN-001"
        ],
        [
          "U26",
          "G13",
          "HOLDOUT",
          "RETAIL",
          66,
          "NEGATIVE",
          "Fictional closed review",
          true,
          false,
          1,
          "SYN-001"
        ],
        [
          "U27",
          "G14",
          "HOLDOUT",
          "RETAIL",
          53,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          1,
          "SYN-001"
        ],
        [
          "U28",
          "G14",
          "HOLDOUT",
          "RETAIL",
          31,
          "UNKNOWN",
          "Review evidence unavailable",
          true,
          false,
          1,
          "SYN-001"
        ],
        [
          "U29",
          "G15",
          "HOLDOUT",
          "SMALL_BUSINESS",
          84,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          1.5,
          "SYN-001"
        ],
        [
          "U30",
          "G15",
          "HOLDOUT",
          "SMALL_BUSINESS",
          71,
          "NEGATIVE",
          "Fictional closed review",
          true,
          false,
          1.5,
          "SYN-001"
        ],
        [
          "U31",
          "G16",
          "HOLDOUT",
          "SMALL_BUSINESS",
          59,
          "POSITIVE",
          "Fictional closed review",
          true,
          false,
          1.5,
          "SYN-001"
        ],
        [
          "U32",
          "G16",
          "HOLDOUT",
          "SMALL_BUSINESS",
          41,
          "NEGATIVE",
          "Fictional closed review",
          true,
          false,
          1.5,
          "SYN-001"
        ],
        [
          "U33",
          "G17",
          "HOLDOUT",
          "CORRESPONDENT",
          94,
          "POSITIVE",
          "Fictional closed review",
          true,
          true,
          2,
          "SYN-001"
        ],
        [
          "U34",
          "G17",
          "HOLDOUT",
          "CORRESPONDENT",
          76,
          "NEGATIVE",
          "Fictional closed review",
          true,
          true,
          2,
          "SYN-001"
        ],
        [
          "U35",
          "G18",
          "HOLDOUT",
          "CORRESPONDENT",
          62,
          "UNKNOWN",
          "Review evidence unavailable",
          true,
          false,
          2,
          "SYN-001"
        ],
        [
          "U36",
          "G18",
          "HOLDOUT",
          "CORRESPONDENT",
          37,
          "CENSORED",
          "Outcome window not mature",
          true,
          false,
          2,
          "SYN-001"
        ]
      ],
      "formats": {
        "review_hours": "0.00"
      },
      "grain": "One eligible scored customer-window unit, identified by unit_id, before candidate selection or routing."
    },
    {
      "name": "Candidates",
      "columns": [
        "candidate_id",
        "retail_threshold",
        "business_threshold",
        "correspondent_threshold",
        "comparator",
        "freeze_state",
        "evidence_ids"
      ],
      "column_contracts": {
        "candidate_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Frozen candidate key."
        },
        "retail_threshold": {
          "type": "number",
          "nullable": false,
          "unit": "score",
          "description": "Inclusive RETAIL score cutoff."
        },
        "business_threshold": {
          "type": "number",
          "nullable": false,
          "unit": "score",
          "description": "Inclusive SMALL_BUSINESS score cutoff."
        },
        "correspondent_threshold": {
          "type": "number",
          "nullable": false,
          "unit": "score",
          "description": "Inclusive CORRESPONDENT score cutoff."
        },
        "comparator": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact comparison operator.",
          "enum": [
            "GREATER_OR_EQUAL"
          ]
        },
        "freeze_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "All candidates declared before examining protected results.",
          "enum": [
            "ILLUSTRATIVE_PREFROZEN"
          ]
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Parameter evidence ID."
        }
      },
      "primary_key": [
        "candidate_id"
      ],
      "rows": [
        [
          "BASE60",
          60,
          60,
          60,
          "GREATER_OR_EQUAL",
          "ILLUSTRATIVE_PREFROZEN",
          "SYN-002"
        ],
        [
          "HIGH75",
          75,
          75,
          75,
          "GREATER_OR_EQUAL",
          "ILLUSTRATIVE_PREFROZEN",
          "SYN-002"
        ],
        [
          "LOW50",
          50,
          50,
          50,
          "GREATER_OR_EQUAL",
          "ILLUSTRATIVE_PREFROZEN",
          "SYN-002"
        ],
        [
          "SEGMENTED",
          55,
          60,
          65,
          "GREATER_OR_EQUAL",
          "ILLUSTRATIVE_PREFROZEN",
          "SYN-002"
        ]
      ],
      "grain": "One frozen candidate configuration, identified by candidate_id, containing all three segment thresholds."
    },
    {
      "name": "CandidateMetrics",
      "columns": [
        "candidate_id",
        "partition",
        "population_n",
        "known_n",
        "tp",
        "fp",
        "fn",
        "tn",
        "unknown_n",
        "raw_hits",
        "retained_hits",
        "queued_cases",
        "workload_hours",
        "precision",
        "recall",
        "retained_positive_hits"
      ],
      "column_contracts": {
        "candidate_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Candidate key."
        },
        "partition": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Evaluation partition or ALL descriptive reconciliation.",
          "enum": [
            "TRAIN",
            "VALIDATION",
            "HOLDOUT",
            "ALL"
          ]
        },
        "population_n": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "All eligible supplied units in this partition."
        },
        "known_n": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "POSITIVE plus NEGATIVE units only."
        },
        "tp": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Known positive unit meeting the raw predicate before routing."
        },
        "fp": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Known negative unit meeting the raw predicate."
        },
        "fn": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Known positive unit below the raw predicate."
        },
        "tn": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Known negative unit below the raw predicate."
        },
        "unknown_n": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "UNKNOWN plus CENSORED units outside the confusion matrix."
        },
        "raw_hits": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "All units meeting the predicate, including unavailable labels."
        },
        "retained_hits": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Raw hits remaining after suppression, before group merge."
        },
        "queued_cases": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Distinct retained group IDs; not a unit count."
        },
        "workload_hours": {
          "type": "number",
          "nullable": false,
          "unit": "hours",
          "description": "Lead hours plus 0.25 hours for every additional retained unit in a group."
        },
        "precision": {
          "type": "number",
          "nullable": true,
          "unit": "ratio",
          "description": "TP divided by TP plus FP on available labels."
        },
        "recall": {
          "type": "number",
          "nullable": true,
          "unit": "ratio",
          "description": "TP divided by TP plus FN on available labels."
        },
        "retained_positive_hits": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Known positive units reaching a queued case; this does not credit unhit siblings."
        }
      },
      "primary_key": [
        "candidate_id",
        "partition"
      ],
      "rows": [
        [
          "BASE60",
          "TRAIN",
          12,
          10,
          4,
          3,
          2,
          1,
          2,
          7,
          7,
          4,
          7.25,
          0.5714285714285714,
          0.6666666666666666,
          4
        ],
        [
          "BASE60",
          "VALIDATION",
          12,
          10,
          4,
          3,
          1,
          2,
          2,
          7,
          7,
          4,
          7.25,
          0.5714285714285714,
          0.8,
          4
        ],
        [
          "BASE60",
          "HOLDOUT",
          12,
          9,
          3,
          3,
          2,
          1,
          3,
          7,
          5,
          3,
          5.0,
          0.5,
          0.6,
          2
        ],
        [
          "BASE60",
          "ALL",
          36,
          29,
          11,
          9,
          5,
          4,
          7,
          21,
          19,
          11,
          19.5,
          0.55,
          0.6875,
          10
        ],
        [
          "HIGH75",
          "TRAIN",
          12,
          10,
          3,
          1,
          3,
          3,
          2,
          4,
          4,
          3,
          4.75,
          0.75,
          0.5,
          3
        ],
        [
          "HIGH75",
          "VALIDATION",
          12,
          10,
          3,
          0,
          2,
          5,
          2,
          3,
          3,
          3,
          4.5,
          1.0,
          0.6,
          3
        ],
        [
          "HIGH75",
          "HOLDOUT",
          12,
          9,
          3,
          1,
          2,
          3,
          3,
          4,
          2,
          2,
          2.5,
          0.75,
          0.6,
          2
        ],
        [
          "HIGH75",
          "ALL",
          36,
          29,
          9,
          2,
          7,
          11,
          7,
          11,
          9,
          8,
          11.75,
          0.8181818181818182,
          0.5625,
          8
        ],
        [
          "LOW50",
          "TRAIN",
          12,
          10,
          6,
          3,
          0,
          1,
          2,
          9,
          9,
          6,
          9.75,
          0.6666666666666666,
          1.0,
          6
        ],
        [
          "LOW50",
          "VALIDATION",
          12,
          10,
          5,
          3,
          0,
          2,
          2,
          9,
          9,
          6,
          9.75,
          0.625,
          1.0,
          5
        ],
        [
          "LOW50",
          "HOLDOUT",
          12,
          9,
          5,
          3,
          0,
          1,
          3,
          9,
          7,
          5,
          7.5,
          0.625,
          1.0,
          4
        ],
        [
          "LOW50",
          "ALL",
          36,
          29,
          16,
          9,
          0,
          4,
          7,
          27,
          25,
          17,
          27.0,
          0.64,
          1.0,
          15
        ],
        [
          "SEGMENTED",
          "TRAIN",
          12,
          10,
          4,
          3,
          2,
          1,
          2,
          7,
          7,
          4,
          6.25,
          0.5714285714285714,
          0.6666666666666666,
          4
        ],
        [
          "SEGMENTED",
          "VALIDATION",
          12,
          10,
          3,
          3,
          2,
          2,
          2,
          6,
          6,
          3,
          5.25,
          0.5,
          0.6,
          3
        ],
        [
          "SEGMENTED",
          "HOLDOUT",
          12,
          9,
          3,
          3,
          2,
          1,
          3,
          6,
          4,
          2,
          3.0,
          0.5,
          0.6,
          2
        ],
        [
          "SEGMENTED",
          "ALL",
          36,
          29,
          10,
          9,
          6,
          4,
          7,
          19,
          17,
          9,
          14.5,
          0.5263157894736842,
          0.625,
          9
        ]
      ],
      "formats": {
        "workload_hours": "0.00",
        "precision": "0.0%",
        "recall": "0.0%"
      },
      "foreign_keys": [
        {
          "columns": [
            "candidate_id"
          ],
          "table": "Candidates",
          "references": [
            "candidate_id"
          ]
        }
      ],
      "grain": "One candidate_id and partition combination, including a separately labeled ALL reconciliation across the three partitions."
    },
    {
      "name": "AlertRouting",
      "columns": [
        "hit_id",
        "candidate_id",
        "unit_id",
        "group_id",
        "route_state",
        "case_id",
        "lead_unit_id",
        "routing_basis",
        "evidence_ids"
      ],
      "column_contracts": {
        "hit_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique candidate-unit raw hit key."
        },
        "candidate_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Candidate responsible for this raw hit."
        },
        "unit_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Exact scored unit; lookup label separately."
        },
        "group_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Frozen group used for merging only within a partition."
        },
        "route_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Mutually exclusive hit routing outcome.",
          "enum": [
            "SUPPRESSED",
            "QUEUED_LEAD",
            "MERGED_CHILD"
          ]
        },
        "case_id": {
          "type": "text",
          "nullable": true,
          "unit": "identifier",
          "description": "Candidate-group queued case key; null for suppressed hits."
        },
        "lead_unit_id": {
          "type": "text",
          "nullable": true,
          "unit": "identifier",
          "description": "Smallest hit unit ID in the retained group; null when suppressed."
        },
        "routing_basis": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Evidence or missing authorization underlying the route."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Sources for routing inputs and predicate lineage."
        }
      },
      "primary_key": [
        "hit_id"
      ],
      "rows": [
        [
          "BASE60-U01",
          "BASE60",
          "U01",
          "G01",
          "QUEUED_LEAD",
          "BASE60-G01",
          "U01",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U02",
          "BASE60",
          "U02",
          "G01",
          "MERGED_CHILD",
          "BASE60-G01",
          "U01",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U05",
          "BASE60",
          "U05",
          "G03",
          "QUEUED_LEAD",
          "BASE60-G03",
          "U05",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U06",
          "BASE60",
          "U06",
          "G03",
          "MERGED_CHILD",
          "BASE60-G03",
          "U05",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U09",
          "BASE60",
          "U09",
          "G05",
          "QUEUED_LEAD",
          "BASE60-G05",
          "U09",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U10",
          "BASE60",
          "U10",
          "G05",
          "MERGED_CHILD",
          "BASE60-G05",
          "U09",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U11",
          "BASE60",
          "U11",
          "G06",
          "QUEUED_LEAD",
          "BASE60-G06",
          "U11",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U13",
          "BASE60",
          "U13",
          "G07",
          "QUEUED_LEAD",
          "BASE60-G07",
          "U13",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U14",
          "BASE60",
          "U14",
          "G07",
          "MERGED_CHILD",
          "BASE60-G07",
          "U13",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U17",
          "BASE60",
          "U17",
          "G09",
          "QUEUED_LEAD",
          "BASE60-G09",
          "U17",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U18",
          "BASE60",
          "U18",
          "G09",
          "MERGED_CHILD",
          "BASE60-G09",
          "U17",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U21",
          "BASE60",
          "U21",
          "G11",
          "QUEUED_LEAD",
          "BASE60-G11",
          "U21",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U22",
          "BASE60",
          "U22",
          "G11",
          "MERGED_CHILD",
          "BASE60-G11",
          "U21",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U23",
          "BASE60",
          "U23",
          "G12",
          "QUEUED_LEAD",
          "BASE60-G12",
          "U23",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U25",
          "BASE60",
          "U25",
          "G13",
          "QUEUED_LEAD",
          "BASE60-G13",
          "U25",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U26",
          "BASE60",
          "U26",
          "G13",
          "MERGED_CHILD",
          "BASE60-G13",
          "U25",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U29",
          "BASE60",
          "U29",
          "G15",
          "QUEUED_LEAD",
          "BASE60-G15",
          "U29",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U30",
          "BASE60",
          "U30",
          "G15",
          "MERGED_CHILD",
          "BASE60-G15",
          "U29",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U33",
          "BASE60",
          "U33",
          "G17",
          "SUPPRESSED",
          null,
          null,
          "Unexpired authorization absent",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U34",
          "BASE60",
          "U34",
          "G17",
          "SUPPRESSED",
          null,
          null,
          "Unexpired authorization absent",
          "SYN-001;SYN-003"
        ],
        [
          "BASE60-U35",
          "BASE60",
          "U35",
          "G18",
          "QUEUED_LEAD",
          "BASE60-G18",
          "U35",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "HIGH75-U01",
          "HIGH75",
          "U01",
          "G01",
          "QUEUED_LEAD",
          "HIGH75-G01",
          "U01",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "HIGH75-U05",
          "HIGH75",
          "U05",
          "G03",
          "QUEUED_LEAD",
          "HIGH75-G03",
          "U05",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "HIGH75-U09",
          "HIGH75",
          "U09",
          "G05",
          "QUEUED_LEAD",
          "HIGH75-G05",
          "U09",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "HIGH75-U10",
          "HIGH75",
          "U10",
          "G05",
          "MERGED_CHILD",
          "HIGH75-G05",
          "U09",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "HIGH75-U13",
          "HIGH75",
          "U13",
          "G07",
          "QUEUED_LEAD",
          "HIGH75-G07",
          "U13",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "HIGH75-U17",
          "HIGH75",
          "U17",
          "G09",
          "QUEUED_LEAD",
          "HIGH75-G09",
          "U17",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "HIGH75-U21",
          "HIGH75",
          "U21",
          "G11",
          "QUEUED_LEAD",
          "HIGH75-G11",
          "U21",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "HIGH75-U25",
          "HIGH75",
          "U25",
          "G13",
          "QUEUED_LEAD",
          "HIGH75-G13",
          "U25",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "HIGH75-U29",
          "HIGH75",
          "U29",
          "G15",
          "QUEUED_LEAD",
          "HIGH75-G15",
          "U29",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "HIGH75-U33",
          "HIGH75",
          "U33",
          "G17",
          "SUPPRESSED",
          null,
          null,
          "Unexpired authorization absent",
          "SYN-001;SYN-003"
        ],
        [
          "HIGH75-U34",
          "HIGH75",
          "U34",
          "G17",
          "SUPPRESSED",
          null,
          null,
          "Unexpired authorization absent",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U01",
          "LOW50",
          "U01",
          "G01",
          "QUEUED_LEAD",
          "LOW50-G01",
          "U01",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U02",
          "LOW50",
          "U02",
          "G01",
          "MERGED_CHILD",
          "LOW50-G01",
          "U01",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U03",
          "LOW50",
          "U03",
          "G02",
          "QUEUED_LEAD",
          "LOW50-G02",
          "U03",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U05",
          "LOW50",
          "U05",
          "G03",
          "QUEUED_LEAD",
          "LOW50-G03",
          "U05",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U06",
          "LOW50",
          "U06",
          "G03",
          "MERGED_CHILD",
          "LOW50-G03",
          "U05",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U07",
          "LOW50",
          "U07",
          "G04",
          "QUEUED_LEAD",
          "LOW50-G04",
          "U07",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U09",
          "LOW50",
          "U09",
          "G05",
          "QUEUED_LEAD",
          "LOW50-G05",
          "U09",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U10",
          "LOW50",
          "U10",
          "G05",
          "MERGED_CHILD",
          "LOW50-G05",
          "U09",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U11",
          "LOW50",
          "U11",
          "G06",
          "QUEUED_LEAD",
          "LOW50-G06",
          "U11",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U13",
          "LOW50",
          "U13",
          "G07",
          "QUEUED_LEAD",
          "LOW50-G07",
          "U13",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U14",
          "LOW50",
          "U14",
          "G07",
          "MERGED_CHILD",
          "LOW50-G07",
          "U13",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U15",
          "LOW50",
          "U15",
          "G08",
          "QUEUED_LEAD",
          "LOW50-G08",
          "U15",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U17",
          "LOW50",
          "U17",
          "G09",
          "QUEUED_LEAD",
          "LOW50-G09",
          "U17",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U18",
          "LOW50",
          "U18",
          "G09",
          "MERGED_CHILD",
          "LOW50-G09",
          "U17",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U19",
          "LOW50",
          "U19",
          "G10",
          "QUEUED_LEAD",
          "LOW50-G10",
          "U19",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U21",
          "LOW50",
          "U21",
          "G11",
          "QUEUED_LEAD",
          "LOW50-G11",
          "U21",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U22",
          "LOW50",
          "U22",
          "G11",
          "MERGED_CHILD",
          "LOW50-G11",
          "U21",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U23",
          "LOW50",
          "U23",
          "G12",
          "QUEUED_LEAD",
          "LOW50-G12",
          "U23",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U25",
          "LOW50",
          "U25",
          "G13",
          "QUEUED_LEAD",
          "LOW50-G13",
          "U25",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U26",
          "LOW50",
          "U26",
          "G13",
          "MERGED_CHILD",
          "LOW50-G13",
          "U25",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U27",
          "LOW50",
          "U27",
          "G14",
          "QUEUED_LEAD",
          "LOW50-G14",
          "U27",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U29",
          "LOW50",
          "U29",
          "G15",
          "QUEUED_LEAD",
          "LOW50-G15",
          "U29",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U30",
          "LOW50",
          "U30",
          "G15",
          "MERGED_CHILD",
          "LOW50-G15",
          "U29",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U31",
          "LOW50",
          "U31",
          "G16",
          "QUEUED_LEAD",
          "LOW50-G16",
          "U31",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U33",
          "LOW50",
          "U33",
          "G17",
          "SUPPRESSED",
          null,
          null,
          "Unexpired authorization absent",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U34",
          "LOW50",
          "U34",
          "G17",
          "SUPPRESSED",
          null,
          null,
          "Unexpired authorization absent",
          "SYN-001;SYN-003"
        ],
        [
          "LOW50-U35",
          "LOW50",
          "U35",
          "G18",
          "QUEUED_LEAD",
          "LOW50-G18",
          "U35",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U01",
          "SEGMENTED",
          "U01",
          "G01",
          "QUEUED_LEAD",
          "SEGMENTED-G01",
          "U01",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U02",
          "SEGMENTED",
          "U02",
          "G01",
          "MERGED_CHILD",
          "SEGMENTED-G01",
          "U01",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U03",
          "SEGMENTED",
          "U03",
          "G02",
          "QUEUED_LEAD",
          "SEGMENTED-G02",
          "U03",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U05",
          "SEGMENTED",
          "U05",
          "G03",
          "QUEUED_LEAD",
          "SEGMENTED-G03",
          "U05",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U06",
          "SEGMENTED",
          "U06",
          "G03",
          "MERGED_CHILD",
          "SEGMENTED-G03",
          "U05",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U09",
          "SEGMENTED",
          "U09",
          "G05",
          "QUEUED_LEAD",
          "SEGMENTED-G05",
          "U09",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U10",
          "SEGMENTED",
          "U10",
          "G05",
          "MERGED_CHILD",
          "SEGMENTED-G05",
          "U09",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U13",
          "SEGMENTED",
          "U13",
          "G07",
          "QUEUED_LEAD",
          "SEGMENTED-G07",
          "U13",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U14",
          "SEGMENTED",
          "U14",
          "G07",
          "MERGED_CHILD",
          "SEGMENTED-G07",
          "U13",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U17",
          "SEGMENTED",
          "U17",
          "G09",
          "QUEUED_LEAD",
          "SEGMENTED-G09",
          "U17",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U18",
          "SEGMENTED",
          "U18",
          "G09",
          "MERGED_CHILD",
          "SEGMENTED-G09",
          "U17",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U21",
          "SEGMENTED",
          "U21",
          "G11",
          "QUEUED_LEAD",
          "SEGMENTED-G11",
          "U21",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U22",
          "SEGMENTED",
          "U22",
          "G11",
          "MERGED_CHILD",
          "SEGMENTED-G11",
          "U21",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U25",
          "SEGMENTED",
          "U25",
          "G13",
          "QUEUED_LEAD",
          "SEGMENTED-G13",
          "U25",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U26",
          "SEGMENTED",
          "U26",
          "G13",
          "MERGED_CHILD",
          "SEGMENTED-G13",
          "U25",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U29",
          "SEGMENTED",
          "U29",
          "G15",
          "QUEUED_LEAD",
          "SEGMENTED-G15",
          "U29",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U30",
          "SEGMENTED",
          "U30",
          "G15",
          "MERGED_CHILD",
          "SEGMENTED-G15",
          "U29",
          "Same frozen group and partition",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U33",
          "SEGMENTED",
          "U33",
          "G17",
          "SUPPRESSED",
          null,
          null,
          "Unexpired authorization absent",
          "SYN-001;SYN-003"
        ],
        [
          "SEGMENTED-U34",
          "SEGMENTED",
          "U34",
          "G17",
          "SUPPRESSED",
          null,
          null,
          "Unexpired authorization absent",
          "SYN-001;SYN-003"
        ]
      ],
      "foreign_keys": [
        {
          "columns": [
            "candidate_id"
          ],
          "table": "Candidates",
          "references": [
            "candidate_id"
          ]
        },
        {
          "columns": [
            "unit_id"
          ],
          "table": "Population",
          "references": [
            "unit_id"
          ]
        },
        {
          "columns": [
            "lead_unit_id"
          ],
          "table": "Population",
          "references": [
            "unit_id"
          ]
        }
      ],
      "grain": "One raw candidate-unit hit, identified by hit_id, with its suppression or merged-case route."
    },
    {
      "name": "BelowThreshold",
      "columns": [
        "draw_id",
        "unit_id",
        "partition",
        "frame_n",
        "rank",
        "selected",
        "review_label",
        "design",
        "evidence_ids"
      ],
      "column_contracts": {
        "draw_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique frame-row identifier."
        },
        "unit_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "BASE60 nonhit unit."
        },
        "partition": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Frozen stratum; five nonhits per partition.",
          "enum": [
            "TRAIN",
            "VALIDATION",
            "HOLDOUT"
          ]
        },
        "frame_n": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Complete number of eligible nonhits in this stratum."
        },
        "rank": {
          "type": "integer",
          "nullable": false,
          "unit": "rank",
          "description": "Supplied distinct rank within the stratum."
        },
        "selected": {
          "type": "boolean",
          "nullable": false,
          "unit": "flag",
          "description": "True for ranks one and two."
        },
        "review_label": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Observed selected-row outcome or NOT_REVIEWED for unselected records.",
          "enum": [
            "POSITIVE",
            "NEGATIVE",
            "UNKNOWN",
            "CENSORED",
            "NOT_REVIEWED"
          ]
        },
        "design": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Fixture rank list is illustrative; it makes no random-sampling claim.",
          "enum": [
            "ILLUSTRATIVE_RANK"
          ]
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Complete supplied frame and draw record."
        }
      },
      "primary_key": [
        "draw_id"
      ],
      "rows": [
        [
          "BTL-U03",
          "U03",
          "TRAIN",
          5,
          1,
          true,
          "POSITIVE",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ],
        [
          "BTL-U04",
          "U04",
          "TRAIN",
          5,
          3,
          false,
          "NOT_REVIEWED",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ],
        [
          "BTL-U07",
          "U07",
          "TRAIN",
          5,
          2,
          true,
          "POSITIVE",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ],
        [
          "BTL-U08",
          "U08",
          "TRAIN",
          5,
          4,
          false,
          "NOT_REVIEWED",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ],
        [
          "BTL-U12",
          "U12",
          "TRAIN",
          5,
          5,
          false,
          "NOT_REVIEWED",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ],
        [
          "BTL-U15",
          "U15",
          "VALIDATION",
          5,
          1,
          true,
          "POSITIVE",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ],
        [
          "BTL-U16",
          "U16",
          "VALIDATION",
          5,
          3,
          false,
          "NOT_REVIEWED",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ],
        [
          "BTL-U19",
          "U19",
          "VALIDATION",
          5,
          4,
          false,
          "NOT_REVIEWED",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ],
        [
          "BTL-U20",
          "U20",
          "VALIDATION",
          5,
          2,
          true,
          "NEGATIVE",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ],
        [
          "BTL-U24",
          "U24",
          "VALIDATION",
          5,
          5,
          false,
          "NOT_REVIEWED",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ],
        [
          "BTL-U27",
          "U27",
          "HOLDOUT",
          5,
          3,
          false,
          "NOT_REVIEWED",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ],
        [
          "BTL-U28",
          "U28",
          "HOLDOUT",
          5,
          1,
          true,
          "UNKNOWN",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ],
        [
          "BTL-U31",
          "U31",
          "HOLDOUT",
          5,
          4,
          false,
          "NOT_REVIEWED",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ],
        [
          "BTL-U32",
          "U32",
          "HOLDOUT",
          5,
          5,
          false,
          "NOT_REVIEWED",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ],
        [
          "BTL-U36",
          "U36",
          "HOLDOUT",
          5,
          2,
          true,
          "CENSORED",
          "ILLUSTRATIVE_RANK",
          "SYN-004"
        ]
      ],
      "foreign_keys": [
        {
          "columns": [
            "unit_id"
          ],
          "table": "Population",
          "references": [
            "unit_id"
          ]
        }
      ],
      "grain": "One unit in the complete BASE60 nonhit frame within its frozen partition, whether selected for review or not."
    },
    {
      "name": "CandidateDecisions",
      "columns": [
        "candidate_id",
        "decision_state",
        "coverage_gate",
        "capacity_gate",
        "routing_gate",
        "next_evidence",
        "human_disposition",
        "evidence_ids"
      ],
      "column_contracts": {
        "candidate_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Candidate key."
        },
        "decision_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Current proposed analytical recommendation.",
          "enum": [
            "BASELINE_ONLY",
            "DO_NOT_SUPPORT",
            "FURTHER_VALIDATION_ONLY"
          ]
        },
        "coverage_gate": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Explicit known-positive and unknown-label assessment."
        },
        "capacity_gate": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Illustrative hours gate; never the only selection criterion."
        },
        "routing_gate": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Status of suppression verification."
        },
        "next_evidence": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Concrete prerequisite for further consideration."
        },
        "human_disposition": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Operational approval is absent.",
          "enum": [
            "NOT_RECORDED"
          ]
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Sources underlying the recommendation."
        }
      },
      "primary_key": [
        "candidate_id"
      ],
      "rows": [
        [
          "BASE60",
          "BASELINE_ONLY",
          "Raw known recall 11/16; retained positive hits 10",
          "ALL workload 19.5 hours; illustrative combined capacity 15 hours; no staffing-only selection",
          "G17 authorization unverified",
          "Resolve suppression and missing labels before change assessment",
          "NOT_RECORDED",
          "SYN-001;SYN-003"
        ],
        [
          "HIGH75",
          "DO_NOT_SUPPORT",
          "Raw known recall 9/16; retained positive hits 8",
          "ALL workload 11.75 hours; illustrative combined capacity 15 hours; no staffing-only selection",
          "G17 authorization unverified",
          "Challenge losses U11 and U23 against gains; no automatic acceptance",
          "NOT_RECORDED",
          "SYN-001;SYN-002;SYN-003"
        ],
        [
          "LOW50",
          "FURTHER_VALIDATION_ONLY",
          "Raw known recall 16/16; retained positive hits 15",
          "ALL workload 27 hours; illustrative combined capacity 15 hours; no staffing-only selection",
          "G17 authorization unverified",
          "Representative labels, routing repair, capacity and protected retest",
          "NOT_RECORDED",
          "SYN-001;SYN-002;SYN-003"
        ],
        [
          "SEGMENTED",
          "DO_NOT_SUPPORT",
          "Raw known recall 10/16; retained positive hits 9",
          "ALL workload 14.5 hours; illustrative combined capacity 15 hours; no staffing-only selection",
          "G17 authorization unverified",
          "Resolve correspondent sensitivity and RETAIL boundary changes",
          "NOT_RECORDED",
          "SYN-001;SYN-002;SYN-003"
        ]
      ],
      "foreign_keys": [
        {
          "columns": [
            "candidate_id"
          ],
          "table": "Candidates",
          "references": [
            "candidate_id"
          ]
        }
      ],
      "grain": "One proposed analytical disposition for one candidate_id at the case cutoff; this is not a human deployment approval."
    },
    {
      "name": "EvidenceProvenance",
      "columns": [
        "source_id",
        "source_kind",
        "as_of",
        "availability",
        "unit_count",
        "grain",
        "limitation",
        "evidence_ids"
      ],
      "column_contracts": {
        "source_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable source ID resolving to the Evidence register."
        },
        "source_kind": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Nature of supplied material.",
          "enum": [
            "SYNTHETIC_INPUT",
            "SYNTHETIC_CALCULATION",
            "SYNTHETIC_DECISION"
          ]
        },
        "as_of": {
          "type": "text",
          "nullable": false,
          "unit": "date",
          "description": "Evidence cutoff expressed as ISO date, not a receipt timestamp."
        },
        "availability": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Supplied scope status.",
          "enum": [
            "COMPLETE_FIXTURE",
            "PARTIAL_FIXTURE"
          ]
        },
        "unit_count": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Count at the explicitly named grain."
        },
        "grain": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "The counting unit for this row."
        },
        "limitation": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "What this source cannot establish."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "The same source ID, checked against the Evidence register."
        }
      },
      "primary_key": [
        "source_id"
      ],
      "rows": [
        [
          "SYN-001",
          "SYNTHETIC_INPUT",
          "2026-10-09",
          "COMPLETE_FIXTURE",
          36,
          "scored customer-window units",
          "Labels are fictional and dependent within merge groups.",
          "SYN-001"
        ],
        [
          "SYN-002",
          "SYNTHETIC_INPUT",
          "2026-10-09",
          "COMPLETE_FIXTURE",
          4,
          "candidate configurations",
          "Parameter values are illustrative, not approved live settings.",
          "SYN-002"
        ],
        [
          "SYN-003",
          "SYNTHETIC_INPUT",
          "2026-10-09",
          "PARTIAL_FIXTURE",
          1,
          "suppressed group",
          "Suppression exists in the fixture but authorization and expiry evidence are absent.",
          "SYN-003"
        ],
        [
          "SYN-004",
          "SYNTHETIC_INPUT",
          "2026-10-09",
          "COMPLETE_FIXTURE",
          15,
          "BASE60 below-threshold frame units",
          "Six assigned ranks are selected; design does not establish probability sampling.",
          "SYN-004"
        ]
      ],
      "grain": "One synthetic source_id with its own declared counting unit and availability limit."
    },
    {
      "name": "ProcessQA",
      "columns": [
        "check_id",
        "check_scope",
        "expected",
        "actual",
        "status",
        "reviewer",
        "evidence_ids"
      ],
      "column_contracts": {
        "check_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable QA check identifier."
        },
        "check_scope": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact records or decision being checked."
        },
        "expected": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Reference result calculated before inspecting presentation."
        },
        "actual": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Observed synthetic result; no operational execution is implied."
        },
        "status": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Comparison state.",
          "enum": [
            "PASS",
            "FAIL",
            "REVIEW_REQUIRED",
            "NOT_TESTED"
          ]
        },
        "reviewer": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Fictional review role or NOT_RECORDED; never an actual approval."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Semicolon-delimited source IDs resolving to Evidence."
        }
      },
      "primary_key": [
        "check_id"
      ],
      "rows": [
        [
          "MT-Q01",
          "Population conservation",
          "36 = 29 known + 4 UNKNOWN + 3 CENSORED",
          "36 = 29 + 4 + 3",
          "PASS",
          "Fictional checker",
          "SYN-001"
        ],
        [
          "MT-Q02",
          "Partition segregation",
          "12 units per partition; no group crosses partitions",
          "TRAIN12 VALIDATION12 HOLDOUT12; groups disjoint",
          "PASS",
          "Fictional checker",
          "SYN-001"
        ],
        [
          "MT-Q03",
          "Candidate matrices",
          "Each TP+FP+FN+TN equals known_n",
          "All sixteen matrices reconcile",
          "PASS",
          "Fictional checker",
          "SYN-001;SYN-002"
        ],
        [
          "MT-Q04",
          "Suppression authority",
          "Current authorization plus expiry and coverage evidence",
          "No authorization supplied for G17",
          "FAIL",
          "Fictional checker",
          "SYN-003"
        ],
        [
          "MT-Q05",
          "Below-threshold frame",
          "15 frame units; 6 selected; 9 not reviewed",
          "15 = 6 + 9; selected outcomes P3 N1 U1 C1",
          "PASS",
          "Fictional checker",
          "SYN-004"
        ],
        [
          "MT-Q06",
          "Holdout authorization",
          "Protected review record and separate human decision",
          "Only an illustrative prefreeze is supplied",
          "REVIEW_REQUIRED",
          "NOT_RECORDED",
          "SYN-002"
        ]
      ],
      "grain": "One explicitly scoped fixture quality check, identified by check_id, with expected and actual results."
    }
  ],
  "findings": [
    {
      "id": "MT-F01",
      "title": "Suppression removes a known positive from every candidate",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001",
        "SYN-003"
      ],
      "detail": "G17 contains HOLDOUT U33 POSITIVE and U34 NEGATIVE. U33 is a raw hit under all four candidates, but the suppressed group reaches no queued case. The supplied record contains no valid suppression authorization.",
      "recommendation": "Keep routing assurance blocked; obtain scope, reason, expiry, approver and covered-activity evidence, then replay all candidates."
    },
    {
      "id": "MT-F02",
      "title": "Lowest threshold increases raw known coverage and workload",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001",
        "SYN-002",
        "SYN-003"
      ],
      "detail": "LOW50 has 16/16 known positive raw hits and 27 workload hours against an illustrative 15-hour combined capacity. Retained known positive hits are 15/16 after suppression.",
      "recommendation": "Further validate labels and segment behavior, repair routing and assess staffing; do not deploy from the synthetic result."
    },
    {
      "id": "MT-F03",
      "title": "Unknown and censored labels limit population performance claims",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001",
        "SYN-004"
      ],
      "detail": "Twenty-nine of thirty-six units have known labels. Four UNKNOWN and three CENSORED units remain outside confusion matrices, including both hit and nonhit records.",
      "recommendation": "Preserve unavailable labels, obtain independent review and assess outcome maturity before any population recall inference."
    },
    {
      "id": "MT-F04",
      "title": "Segmented cutoffs lose correspondent known positives",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001",
        "SYN-002"
      ],
      "detail": "SEGMENTED moves the correspondent cutoff to 65. TRAIN U11 score 63 and VALIDATION U23 score 61 are known positives caught by BASE60 and missed by SEGMENTED. RETAIL U03 score 56 is gained, so the combined result hides opposite segment effects.",
      "recommendation": "Retain incremental unit IDs and require explicit segment challenge; aggregate workload cannot resolve the coverage tradeoff."
    }
  ],
  "evidence": [
    {
      "id": "SYN-001",
      "title": "Fictional 36-unit population, label and dependence register",
      "locator": "10-worked-example.md, raw population and unit-by-unit trace",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-002",
      "title": "Four predeclared fictional score candidates",
      "locator": "10-worked-example.md, frozen candidate input table",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-003",
      "title": "Fictional G17 suppression and group-routing policy",
      "locator": "10-worked-example.md, routing input and complete hit ledger",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-004",
      "title": "Fictional complete below-threshold frame and assigned ranks",
      "locator": "10-worked-example.md, complete fifteen-row frame",
      "claim_class": "Observed"
    },
    {
      "id": "REF-001",
      "title": "FFIEC suspicious activity monitoring examination procedures",
      "locator": "https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04_ep",
      "claim_class": "Reported"
    },
    {
      "id": "REF-002",
      "title": "Federal Reserve SR 26-2, April 17, 2026",
      "locator": "https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm",
      "claim_class": "Reported"
    },
    {
      "id": "REF-003",
      "title": "Federal Reserve, Supervisory Guidance on Model Risk Management",
      "locator": "https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm",
      "claim_class": "Reported"
    },
    {
      "id": "REF-004",
      "title": "FinCEN and federal banking agencies, SAR FAQs, October 9, 2025",
      "locator": "https://www.fincen.gov/system/files/2025-10/SAR-FAQs-October-2025.pdf",
      "claim_class": "Reported"
    },
    {
      "id": "REF-005",
      "title": "FATF, Guidance for a Risk-Based Approach: The Banking Sector",
      "locator": "https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Risk-Based-Approach-Banking-Sector.pdf.coredownload.pdf",
      "claim_class": "Reported"
    },
    {
      "id": "REF-006",
      "title": "NIST, Confidence intervals for proportions",
      "locator": "https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm",
      "claim_class": "Reported"
    },
    {
      "id": "REF-007",
      "title": "GAO, Standards for Internal Control in the Federal Government, 2025 revision",
      "locator": "https://www.gao.gov/assets/890/882014.pdf",
      "claim_class": "Reported"
    }
  ],
  "metrics": [
    {
      "label": "Scored units",
      "value": 36,
      "method": "Complete frozen unit register; one customer-window per row.",
      "format": "#,##0"
    },
    {
      "label": "Known labels",
      "value": 29,
      "method": "16 POSITIVE plus 13 NEGATIVE; excludes 4 UNKNOWN and 3 CENSORED.",
      "format": "#,##0"
    },
    {
      "label": "LOW50 raw known recall",
      "value": 1.0,
      "format": "0.0%",
      "method": "16 raw positive hits / 16 known positive units; not population recall."
    },
    {
      "label": "LOW50 workload hours",
      "value": 27.0,
      "format": "0.00",
      "method": "Retained group lead hours plus 0.25 per additional hit after suppression."
    }
  ],
  "limitations": [
    "Every record is fictional; results test this supplied procedure and do not establish operational effectiveness.",
    "Illustrative cutoffs, partitions, labels, capacities and severity choices are authored examples, not regulatory thresholds.",
    "Human scope approval, deployment authority, case disposition and reporting decisions are not supplied.",
    "Missing, censored and unresolved evidence remains visible; no favorable default is permitted."
  ],
  "conclusion": "LOW50 is a further-validation candidate only. Its known-label raw coverage improves, but G17 suppression removes a known positive, missing outcomes prevent population effectiveness claims, and illustrative workload exceeds capacity. No candidate is authorized for deployment.",
  "report_narrative": [
    [
      "LOW50 is a further-validation candidate only. Its known-label raw coverage improves, but G17 suppression removes a known positive, missing outcomes prevent population effectiveness claims, and illustrative workload exceeds capacity. No candidate is authorized for deployment."
    ],
    [
      "The 36 fictional units form three disjoint partitions of twelve. Three segments each contain four units per partition. Group pairs never cross partitions. Scores and four candidates are predeclared; the ALL row is descriptive reconciliation rather than an independent evaluation set."
    ],
    [
      "Raw predicate results, suppression, merged case counts and workload are separate stages. Group G17 suppresses HOLDOUT U33 and U34. A case merge does not automatically credit unhit siblings as detected. The raw and retained positive-unit numerators remain separate."
    ],
    [
      "ALL BASE60 TP11 FP9 FN5 TN4; HIGH75 TP9 FP2 FN7 TN11; LOW50 TP16 FP9 FN0 TN4; SEGMENTED TP10 FP9 FN6 TN4. Each matrix has 29 known labels, with seven other units retained outside the matrix."
    ],
    [
      "The complete BASE60 below-threshold frame has fifteen units. Six assigned-rank selections contain three POSITIVE, one NEGATIVE, one UNKNOWN and one CENSORED outcome. Nine frame units remain unreviewed by this draw. The illustrative ranks do not support a random-sample confidence interval."
    ],
    [
      "The source ledger preserves 36 units, four candidates, one suppression group with incomplete authority, and fifteen below-threshold frame records. Public guidance provides governance context. It does not establish a legal cutoff, a live model classification or approval to suppress activity."
    ],
    [
      "Proposed work is to establish suppression authority or revise routing, label unavailable outcomes without leakage, validate incremental segment losses, and test capacity on protected data. The human deployment disposition remains NOT_RECORDED."
    ],
    [
      "Reperform all candidate matrices and the conservation equations. Validate exact threshold boundaries, merge groups, null rates and missing labels. Passing the fictional checks establishes consistency of this example only; it cannot validate live detection effectiveness."
    ]
  ],
  "methods": [
    "Freeze the scope, source versions, population grain, evidence cutoff and decision question before calculating.",
    "Reconcile every received, eligible, excluded, duplicate and unresolved record against independent controls.",
    "Apply the exact predicates, joins, state transitions and denominators in files 03 through 05.",
    "Challenge missing data, counterexamples, boundary conditions and alternative explanations using file 09.",
    "Reproduce file 10 before replacing fictional data; preserve approval gaps and incomplete coverage."
  ],
  "actions": [
    {
      "id": "MO-A01",
      "finding_id": "MT-F01",
      "proposal": "Keep routing assurance blocked; obtain scope, reason, expiry, approver and covered-activity evidence, then replay all candidates.",
      "owner": "Proposed accountable role; assignment not recorded",
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "MO-A02",
      "finding_id": "MT-F02",
      "proposal": "Further validate labels and segment behavior, repair routing and assess staffing; do not deploy from the synthetic result.",
      "owner": "Proposed accountable role; assignment not recorded",
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "MO-A03",
      "finding_id": "MT-F03",
      "proposal": "Preserve unavailable labels, obtain independent review and assess outcome maturity before any population recall inference.",
      "owner": "Proposed accountable role; assignment not recorded",
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "MO-A04",
      "finding_id": "MT-F04",
      "proposal": "Retain incremental unit IDs and require explicit segment challenge; aggregate workload cannot resolve the coverage tradeoff.",
      "owner": "Proposed accountable role; assignment not recorded",
      "due_date": null,
      "status": "Proposed"
    }
  ],
  "qa": [
    {
      "id": "QA-01",
      "check": "Exact fictional reconciliation",
      "result": "REVIEW REQUIRED",
      "evidence": "Reperform all ProcessQA rows and file 10 checkpoints in this session."
    },
    {
      "id": "QA-02",
      "check": "Evidence and counterevidence",
      "result": "REVIEW REQUIRED",
      "evidence": "Review every field, rule and exception in files 02 through 05."
    },
    {
      "id": "QA-03",
      "check": "Authorized human disposition",
      "result": "NOT RECORDED",
      "evidence": "No operational approval or filing decision is represented by these fictional records."
    }
  ],
  "suite_id": "monitoring-tuning",
  "version": "1.2.0",
  "notice": "Synthetic worked example. Fictional records. Not a completed operational review."
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
