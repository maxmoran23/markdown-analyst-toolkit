# Monitoring System Independent Challenge and Validation — complete dashboard template

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
<title>Monitoring System Independent Challenge and Validation</title>
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
  "slug": "monitoring-validation",
  "title": "Monitoring System Independent Challenge and Validation",
  "summary": "Challenge monitoring purpose, data, implementation, outcomes, limitations and governance with complete evidence and explicit release gates.",
  "audience": "Monitoring analysts, independent challenge reviewers and accountable human decision makers",
  "decision": "What can an objective reviewer conclude about the supplied monitoring component, and which defects or evidence gaps restrict its use?",
  "palette": "indigo",
  "as_of": "2026-10-09",
  "scope": "Complete fictional inputs printed in file 10 only. Public authorities provide context, not evidence about the fictional subjects or an institution-specific mandate.",
  "report_sections": [
    "Validation opinion and use restrictions",
    "System scope classification and review design",
    "Material validation findings",
    "Component tests and outcome registers",
    "Issue resolution and release gates",
    "Evidence provenance and competing interpretations",
    "Required remediation and further challenge",
    "Limitations quality review and human disposition"
  ],
  "domain_tables": [
    {
      "name": "ComponentInventory",
      "columns": [
        "component_id",
        "name",
        "classification",
        "input_grain",
        "output",
        "theory_basis",
        "limitation",
        "evidence_ids"
      ],
      "column_contracts": {
        "component_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable analytical component identifier."
        },
        "name": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Component purpose and representation."
        },
        "classification": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Toolkit analytical classification; institutional determination absent.",
          "enum": [
            "DETERMINISTIC_RULE",
            "DETERMINISTIC_TRANSFORM",
            "HUMAN_PROCESS"
          ]
        },
        "input_grain": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact unit consumed by the component."
        },
        "output": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Declared output and permitted values."
        },
        "theory_basis": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Whether quantitative theory underpins an estimate or only fixed logic."
        },
        "limitation": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Scope not established by this component."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Supporting source IDs."
        }
      },
      "primary_key": [
        "component_id"
      ],
      "rows": [
        [
          "CMP-01",
          "Feature construction",
          "DETERMINISTIC_TRANSFORM",
          "Transactions grouped into fixed customer-window",
          "amount_usd;eligible_count;originators",
          "Arithmetic aggregation; raw transaction replay not supplied",
          "Feature values are supplied rather than independently validated",
          "SYN-101"
        ],
        [
          "CMP-02",
          "Reference scenario R1",
          "DETERMINISTIC_RULE",
          "One customer-window",
          "TRUE;FALSE;UNKNOWN",
          "Fixed inclusive predicates with no fitted statistical component",
          "Multi-originator concept misses single-originator activity",
          "SYN-102"
        ],
        [
          "CMP-03",
          "Implementation I1",
          "DETERMINISTIC_RULE",
          "One customer-window",
          "TRUE;FALSE",
          "Strict amount comparison and missing-to-zero default",
          "Implementation differs from R1 at boundary and nulls",
          "SYN-102"
        ],
        [
          "CMP-04",
          "Challenger C1",
          "DETERMINISTIC_RULE",
          "One customer-window",
          "TRUE;FALSE;UNKNOWN",
          "Fixed broader rule removes originator count condition",
          "Diagnostic sensitivity comparison; not a deployment candidate",
          "SYN-102"
        ],
        [
          "CMP-05",
          "Human change disposition",
          "HUMAN_PROCESS",
          "Validation report and unresolved issues",
          "Approve;restrict;reject;request evidence",
          "Not a quantitative model; authority depends on supplied governance",
          "No actual decision or reviewer credentials supplied",
          "SYN-103"
        ]
      ],
      "grain": "One reviewed analytical or governance component, identified by component_id, at the stated system boundary."
    },
    {
      "name": "ChallengeTests",
      "columns": [
        "test_id",
        "domain",
        "test_name",
        "procedure",
        "expected",
        "actual",
        "result",
        "evidence_ids"
      ],
      "column_contracts": {
        "test_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique validation test key."
        },
        "domain": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Validation dimension.",
          "enum": [
            "CONCEPT",
            "DATA",
            "IMPLEMENTATION",
            "OUTCOMES",
            "GOVERNANCE",
            "MONITORING"
          ]
        },
        "test_name": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Distinct question challenged."
        },
        "procedure": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Specific reproducible review action."
        },
        "expected": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Predeclared criterion or expected calculation."
        },
        "actual": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Fictional observation and record IDs."
        },
        "result": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "PASS meets test criterion; FAIL contradicts it; BLOCKED lacks needed evidence.",
          "enum": [
            "PASS",
            "FAIL",
            "BLOCKED"
          ]
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Sources supporting the stated result."
        }
      },
      "primary_key": [
        "test_id"
      ],
      "rows": [
        [
          "C01",
          "CONCEPT",
          "Objective alignment",
          "Compare the stated purpose with the exact predicate",
          "Identify repeated multi-originator credits in one fixed window",
          "Objective and inclusive amount predicate supplied",
          "PASS",
          "SYN-102"
        ],
        [
          "C02",
          "CONCEPT",
          "Alternative mechanisms",
          "Challenge the two-originator assumption",
          "Document single-originator limitations",
          "V05 V11 V17 V23 are known positives outside that concept",
          "FAIL",
          "SYN-101;SYN-102"
        ],
        [
          "C03",
          "CONCEPT",
          "Rule/model classification",
          "Inspect mathematical design and stated use",
          "Record deterministic rule classification without exempting controls",
          "No fitted parameter or probabilistic estimate; deterministic fixture",
          "PASS",
          "SYN-102"
        ],
        [
          "C04",
          "CONCEPT",
          "Segment transfer",
          "Challenge purpose and coverage separately by segment",
          "Evidence of each segment rationale required",
          "Equal mechanics supplied; no real segment rationale",
          "BLOCKED",
          "SYN-102"
        ],
        [
          "D01",
          "DATA",
          "Population counts",
          "Reconcile independent input manifest",
          "24 complete unit identifiers across four segments",
          "24 IDs; six per segment",
          "PASS",
          "SYN-101"
        ],
        [
          "D02",
          "DATA",
          "Amount completeness",
          "Count absent amount inputs without substituting zero",
          "24 amounts required for full calculability",
          "Four missing amounts: V06 V12 V18 V24",
          "FAIL",
          "SYN-101"
        ],
        [
          "D03",
          "DATA",
          "Transaction lineage",
          "Request source transaction-to-feature replay",
          "Trace every amount count and originator value",
          "Fixture supplies feature-level records only",
          "BLOCKED",
          "SYN-101"
        ],
        [
          "D04",
          "DATA",
          "Outcome provenance",
          "Review label derivation and maturity",
          "Independent mature labels supporting generalization",
          "Twenty synthetic labels and four unknowns only",
          "BLOCKED",
          "SYN-101"
        ],
        [
          "I01",
          "IMPLEMENTATION",
          "Amount boundary",
          "Compare 9999 10000 and 12000 against inclusive specification",
          "10000 qualifies when other conditions hold",
          "Implemented strict greater-than loses four boundary positives",
          "FAIL",
          "SYN-101;SYN-102"
        ],
        [
          "I02",
          "IMPLEMENTATION",
          "Count boundary",
          "Reperform the minimum of three eligible events",
          "Count two is below threshold; count three can qualify",
          "V04 V10 V16 V22 rejected consistently",
          "PASS",
          "SYN-101;SYN-102"
        ],
        [
          "I03",
          "IMPLEMENTATION",
          "Originator boundary",
          "Reperform the minimum of two originators",
          "One originator excluded under the frozen concept",
          "V05 V11 V17 V23 excluded consistently",
          "PASS",
          "SYN-101;SYN-102"
        ],
        [
          "I04",
          "IMPLEMENTATION",
          "Missing value behavior",
          "Compare reference unknown with engine default",
          "Missing amount produces unassessable state",
          "Four missing amounts converted to false",
          "FAIL",
          "SYN-101;SYN-102"
        ],
        [
          "O01",
          "OUTCOMES",
          "Reference matrix",
          "Count known labels with the reference predicate",
          "TP8 FP0 FN4 TN8 on twenty known labels",
          "TP8 FP0 FN4 TN8",
          "PASS",
          "SYN-101;SYN-102"
        ],
        [
          "O02",
          "OUTCOMES",
          "Implemented matrix",
          "Count known labels with implemented predicate",
          "TP4 FP0 FN8 TN8 on twenty known labels",
          "TP4 FP0 FN8 TN8",
          "PASS",
          "SYN-101;SYN-102"
        ],
        [
          "O03",
          "OUTCOMES",
          "Challenger behavior",
          "Remove originator restriction with all other conditions held",
          "Expose sensitivity to the excluded mechanism",
          "TP12 FP0 FN0 TN8 on the synthetic known subset",
          "PASS",
          "SYN-101;SYN-102"
        ],
        [
          "O04",
          "OUTCOMES",
          "Generalization",
          "Check independent outcome design and test selection",
          "Representative operational evidence required",
          "Constructed examples cannot support effectiveness inference",
          "BLOCKED",
          "SYN-101"
        ],
        [
          "G01",
          "GOVERNANCE",
          "Version lineage",
          "Compare supplied specification and implementation descriptions",
          "Both versions distinguish inclusive and strict comparison",
          "Spec R1 versus implementation I1 recorded",
          "PASS",
          "SYN-102"
        ],
        [
          "G02",
          "GOVERNANCE",
          "Change authorization",
          "Inspect human change decision and permitted scope",
          "Accountable approver and authorization evidence",
          "No operational authorization supplied",
          "BLOCKED",
          "SYN-103"
        ],
        [
          "G03",
          "GOVERNANCE",
          "Validator objectivity",
          "Review involvement expertise conflict and escalation",
          "Named review role with evidence of sufficient objectivity",
          "Fictional role only; no actual reviewer credentials",
          "BLOCKED",
          "SYN-103"
        ],
        [
          "G04",
          "GOVERNANCE",
          "Issue ownership",
          "Trace defects to proposed actions and evidence requirements",
          "Each material defect has a human decision route",
          "Four proposed issue records populated",
          "PASS",
          "SYN-103"
        ],
        [
          "M01",
          "MONITORING",
          "Missingness indicator",
          "Calculate missing amount count and denominator",
          "4/24 = 16.7% absent",
          "4/24 = 16.7%",
          "PASS",
          "SYN-101"
        ],
        [
          "M02",
          "MONITORING",
          "Boundary mismatch indicator",
          "Identify present-input implementation differences",
          "4/20 = 20.0% among present amounts",
          "V02 V08 V14 V20; 4/20",
          "PASS",
          "SYN-101;SYN-102"
        ],
        [
          "M03",
          "MONITORING",
          "Drift baseline",
          "Inspect the reference period and comparison frame",
          "Comparable independent periods required",
          "Single constructed feature set only",
          "BLOCKED",
          "SYN-101"
        ],
        [
          "M04",
          "MONITORING",
          "Remediation retest",
          "Require corrected replay plus unchanged-case checks",
          "New implementation and all twenty-four outcomes",
          "No corrected implementation supplied",
          "BLOCKED",
          "SYN-103"
        ]
      ],
      "grain": "One predeclared validation test, identified by test_id, within one validation domain."
    },
    {
      "name": "OutcomeUnits",
      "columns": [
        "unit_id",
        "segment",
        "amount_usd",
        "eligible_count",
        "originators",
        "label",
        "reference_hit",
        "implemented_hit",
        "challenger_hit",
        "mismatch",
        "evidence_ids"
      ],
      "column_contracts": {
        "unit_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "One feature-level customer-window test unit."
        },
        "segment": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Fictional segment label.",
          "enum": [
            "RETAIL",
            "BUSINESS",
            "CORRESPONDENT",
            "DIGITAL_SERVICE"
          ]
        },
        "amount_usd": {
          "type": "number",
          "nullable": true,
          "unit": "USD",
          "description": "Eligible credits in USD for the supplied fixed window; null means absent."
        },
        "eligible_count": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Number of eligible posted credits in that window."
        },
        "originators": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Distinct originator identities under the frozen supplied definition."
        },
        "label": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Synthetic outcome; UNKNOWN stays outside matrices.",
          "enum": [
            "POSITIVE",
            "NEGATIVE",
            "UNKNOWN"
          ]
        },
        "reference_hit": {
          "type": "boolean",
          "nullable": true,
          "unit": "flag",
          "description": "Inclusive amount and count rule; null when amount absent."
        },
        "implemented_hit": {
          "type": "boolean",
          "nullable": false,
          "unit": "flag",
          "description": "Observed I1 result with strict amount test and missing-to-false defect."
        },
        "challenger_hit": {
          "type": "boolean",
          "nullable": true,
          "unit": "flag",
          "description": "Diagnostic rule without originator restriction; null when amount absent."
        },
        "mismatch": {
          "type": "boolean",
          "nullable": false,
          "unit": "flag",
          "description": "True when reference and implemented values differ, including null versus false."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Raw features and independent rule definitions."
        }
      },
      "primary_key": [
        "unit_id"
      ],
      "rows": [
        [
          "V01",
          "RETAIL",
          9999,
          3,
          2,
          "NEGATIVE",
          false,
          false,
          false,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V02",
          "RETAIL",
          10000,
          3,
          2,
          "POSITIVE",
          true,
          false,
          true,
          true,
          "SYN-101;SYN-102"
        ],
        [
          "V03",
          "RETAIL",
          12000,
          4,
          3,
          "POSITIVE",
          true,
          true,
          true,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V04",
          "RETAIL",
          14000,
          2,
          2,
          "NEGATIVE",
          false,
          false,
          false,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V05",
          "RETAIL",
          18000,
          5,
          1,
          "POSITIVE",
          false,
          false,
          true,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V06",
          "RETAIL",
          null,
          4,
          3,
          "UNKNOWN",
          null,
          false,
          null,
          true,
          "SYN-101;SYN-102"
        ],
        [
          "V07",
          "BUSINESS",
          9999,
          3,
          2,
          "NEGATIVE",
          false,
          false,
          false,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V08",
          "BUSINESS",
          10000,
          3,
          2,
          "POSITIVE",
          true,
          false,
          true,
          true,
          "SYN-101;SYN-102"
        ],
        [
          "V09",
          "BUSINESS",
          12000,
          4,
          3,
          "POSITIVE",
          true,
          true,
          true,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V10",
          "BUSINESS",
          14000,
          2,
          2,
          "NEGATIVE",
          false,
          false,
          false,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V11",
          "BUSINESS",
          18000,
          5,
          1,
          "POSITIVE",
          false,
          false,
          true,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V12",
          "BUSINESS",
          null,
          4,
          3,
          "UNKNOWN",
          null,
          false,
          null,
          true,
          "SYN-101;SYN-102"
        ],
        [
          "V13",
          "CORRESPONDENT",
          9999,
          3,
          2,
          "NEGATIVE",
          false,
          false,
          false,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V14",
          "CORRESPONDENT",
          10000,
          3,
          2,
          "POSITIVE",
          true,
          false,
          true,
          true,
          "SYN-101;SYN-102"
        ],
        [
          "V15",
          "CORRESPONDENT",
          12000,
          4,
          3,
          "POSITIVE",
          true,
          true,
          true,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V16",
          "CORRESPONDENT",
          14000,
          2,
          2,
          "NEGATIVE",
          false,
          false,
          false,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V17",
          "CORRESPONDENT",
          18000,
          5,
          1,
          "POSITIVE",
          false,
          false,
          true,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V18",
          "CORRESPONDENT",
          null,
          4,
          3,
          "UNKNOWN",
          null,
          false,
          null,
          true,
          "SYN-101;SYN-102"
        ],
        [
          "V19",
          "DIGITAL_SERVICE",
          9999,
          3,
          2,
          "NEGATIVE",
          false,
          false,
          false,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V20",
          "DIGITAL_SERVICE",
          10000,
          3,
          2,
          "POSITIVE",
          true,
          false,
          true,
          true,
          "SYN-101;SYN-102"
        ],
        [
          "V21",
          "DIGITAL_SERVICE",
          12000,
          4,
          3,
          "POSITIVE",
          true,
          true,
          true,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V22",
          "DIGITAL_SERVICE",
          14000,
          2,
          2,
          "NEGATIVE",
          false,
          false,
          false,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V23",
          "DIGITAL_SERVICE",
          18000,
          5,
          1,
          "POSITIVE",
          false,
          false,
          true,
          false,
          "SYN-101;SYN-102"
        ],
        [
          "V24",
          "DIGITAL_SERVICE",
          null,
          4,
          3,
          "UNKNOWN",
          null,
          false,
          null,
          true,
          "SYN-101;SYN-102"
        ]
      ],
      "formats": {
        "amount_usd": "$#,##0.00"
      },
      "grain": "One feature-level customer-window test unit, identified by unit_id, evaluated by the reference, implementation and challenger."
    },
    {
      "name": "OutcomeMetrics",
      "columns": [
        "variant",
        "population_n",
        "known_n",
        "unknown_n",
        "tp",
        "fp",
        "fn",
        "tn",
        "all_hits",
        "unassessable_n",
        "precision",
        "recall",
        "evidence_ids"
      ],
      "column_contracts": {
        "variant": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Frozen comparison variant.",
          "enum": [
            "REFERENCE",
            "IMPLEMENTED",
            "CHALLENGER"
          ]
        },
        "population_n": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "All supplied units."
        },
        "known_n": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Available positive or negative labels."
        },
        "unknown_n": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Missing outcome labels excluded from confusion matrix."
        },
        "tp": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Known positive and variant true."
        },
        "fp": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Known negative and variant true."
        },
        "fn": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Known positive and variant false."
        },
        "tn": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Known negative and variant false."
        },
        "all_hits": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "True outputs across all twenty-four units."
        },
        "unassessable_n": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Null outputs due to missing input; separate from unknown labels."
        },
        "precision": {
          "type": "number",
          "nullable": true,
          "unit": "ratio",
          "description": "TP / (TP+FP) on known labels."
        },
        "recall": {
          "type": "number",
          "nullable": true,
          "unit": "ratio",
          "description": "TP / (TP+FN) on known labels."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Feature and predicate sources."
        }
      },
      "primary_key": [
        "variant"
      ],
      "rows": [
        [
          "REFERENCE",
          24,
          20,
          4,
          8,
          0,
          4,
          8,
          8,
          4,
          1.0,
          0.6666666666666666,
          "SYN-101;SYN-102"
        ],
        [
          "IMPLEMENTED",
          24,
          20,
          4,
          4,
          0,
          8,
          8,
          4,
          0,
          1.0,
          0.3333333333333333,
          "SYN-101;SYN-102"
        ],
        [
          "CHALLENGER",
          24,
          20,
          4,
          12,
          0,
          0,
          8,
          12,
          4,
          1.0,
          1.0,
          "SYN-101;SYN-102"
        ]
      ],
      "formats": {
        "precision": "0.0%",
        "recall": "0.0%"
      },
      "grain": "One comparison variant summarized across the same complete 24-unit fixture and 20-unit known-label subset."
    },
    {
      "name": "IssueRegister",
      "columns": [
        "issue_id",
        "linked_tests",
        "severity",
        "affected_ids",
        "issue",
        "closure_evidence",
        "state",
        "evidence_ids"
      ],
      "column_contracts": {
        "issue_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique issue key."
        },
        "linked_tests": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Semicolon-delimited ChallengeTests identifiers."
        },
        "severity": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Illustrative prioritization independent of certainty.",
          "enum": [
            "HIGH",
            "MEDIUM",
            "LOW"
          ]
        },
        "affected_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact affected units or component IDs."
        },
        "issue": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Observed deficiency or limitation."
        },
        "closure_evidence": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Minimum evidence needed to test a proposed correction."
        },
        "state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "No issue is operationally closed in this fixture.",
          "enum": [
            "OPEN",
            "BLOCKED"
          ]
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Underlying case evidence."
        }
      },
      "primary_key": [
        "issue_id"
      ],
      "rows": [
        [
          "MV-I01",
          "I01;M02",
          "HIGH",
          "V02;V08;V14;V20",
          "Strict amount comparison loses inclusive-boundary hits",
          "Corrected version replay of all 24 units plus boundary neighbors",
          "OPEN",
          "SYN-101;SYN-102"
        ],
        [
          "MV-I02",
          "D02;I04",
          "HIGH",
          "V06;V12;V18;V24",
          "Absent amounts silently become negative outputs",
          "Explicit unknown route, data recovery and no zero substitution",
          "OPEN",
          "SYN-101;SYN-102"
        ],
        [
          "MV-I03",
          "C02;D03;D04;O04",
          "HIGH",
          "CMP-01;CMP-02",
          "Coverage concept and evidence cannot support generalization",
          "Transaction lineage, independent representative outcomes and concept challenge",
          "BLOCKED",
          "SYN-101;SYN-102"
        ],
        [
          "MV-I04",
          "G02;G03;M03;M04",
          "MEDIUM",
          "CMP-05",
          "Authorization objectivity and corrected retest not evidenced",
          "Actual reviewer qualifications, conflict assessment, approvals and corrected retest",
          "BLOCKED",
          "SYN-103"
        ]
      ],
      "grain": "One distinct validation issue, identified by issue_id, with linked tests, affected records and closure evidence."
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
          "SYN-101",
          "SYNTHETIC_INPUT",
          "2026-10-09",
          "COMPLETE_FIXTURE",
          24,
          "supplied feature-level units",
          "Feature-level completeness does not establish transaction lineage.",
          "SYN-101"
        ],
        [
          "SYN-102",
          "SYNTHETIC_INPUT",
          "2026-10-09",
          "COMPLETE_FIXTURE",
          3,
          "predicate definitions",
          "R1 I1 and C1 are fictional rules, not live deployed components.",
          "SYN-102"
        ],
        [
          "SYN-103",
          "SYNTHETIC_DECISION",
          "2026-10-09",
          "PARTIAL_FIXTURE",
          4,
          "proposed issue records",
          "Actual change approval and reviewer credentials are absent.",
          "SYN-103"
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
          "MV-Q01",
          "Feature manifest",
          "24 unique units and four segments of 6",
          "24 unique;6 per segment",
          "PASS",
          "Fictional checker",
          "SYN-101"
        ],
        [
          "MV-Q02",
          "Present and absent amounts",
          "24=20 present+4 absent",
          "20 present and 4 null",
          "PASS",
          "Fictional checker",
          "SYN-101"
        ],
        [
          "MV-Q03",
          "Reference result",
          "8 true;12 false;4 unknown",
          "8 true;12 false;4 unknown",
          "PASS",
          "Fictional checker",
          "SYN-101;SYN-102"
        ],
        [
          "MV-Q04",
          "Implemented result",
          "Specification-equivalent tri-state result",
          "4 true;20 false;0 unknown",
          "FAIL",
          "Fictional checker",
          "SYN-101;SYN-102"
        ],
        [
          "MV-Q05",
          "Mismatches",
          "Four boundary and four null-state differences",
          "8 mismatches; mutually exclusive classes",
          "PASS",
          "Fictional checker",
          "SYN-101;SYN-102"
        ],
        [
          "MV-Q06",
          "Generalization gate",
          "Independent operational data required",
          "Synthetic designed examples only",
          "REVIEW_REQUIRED",
          "NOT_RECORDED",
          "SYN-101"
        ],
        [
          "MV-Q07",
          "Human decision",
          "Actual authorized decision required",
          "NOT_RECORDED",
          "NOT_TESTED",
          "NOT_RECORDED",
          "SYN-103"
        ]
      ],
      "grain": "One explicitly scoped fixture quality check, identified by check_id, with expected and actual results."
    },
    {
      "name": "ReleaseGates",
      "columns": [
        "gate_id",
        "requirement",
        "current_evidence",
        "gate_state",
        "dependency",
        "permitted_claim",
        "evidence_ids"
      ],
      "column_contracts": {
        "gate_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique human review gate."
        },
        "requirement": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Evidence needed before supporting the stated use."
        },
        "current_evidence": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "What is actually supplied."
        },
        "gate_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "No failed or blocked gate can be treated as satisfied.",
          "enum": [
            "SATISFIED_FIXTURE_ONLY",
            "FAILED",
            "BLOCKED"
          ]
        },
        "dependency": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Preceding issue or evidence requirement."
        },
        "permitted_claim": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Narrow statement that can currently be made."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Evidence for the gate."
        }
      },
      "primary_key": [
        "gate_id"
      ],
      "rows": [
        [
          "MV-G01",
          "Reference predicate reproducible",
          "R1 independent replay agrees on 24 units",
          "SATISFIED_FIXTURE_ONLY",
          "SYN-101;SYN-102",
          "Fixture arithmetic is reproducible",
          "SYN-101;SYN-102"
        ],
        [
          "MV-G02",
          "Implementation equivalence",
          "Eight mismatches including four known-positive boundary losses",
          "FAILED",
          "MV-I01;MV-I02",
          "Implementation is not equivalent to the supplied specification",
          "SYN-101;SYN-102"
        ],
        [
          "MV-G03",
          "Complete input lineage",
          "Raw transaction detail is outside the supplied fixture",
          "BLOCKED",
          "MV-I03",
          "Feature-level calculations only",
          "SYN-101"
        ],
        [
          "MV-G04",
          "Representative outcomes",
          "Twenty constructed known labels and four unknowns",
          "BLOCKED",
          "MV-I03",
          "Synthetic comparisons only; no live effectiveness estimate",
          "SYN-101"
        ],
        [
          "MV-G05",
          "Qualified objective review",
          "Fictional review role; no actual conflict or qualification record",
          "BLOCKED",
          "MV-I04",
          "Method supports challenge; institutional independence unverified",
          "SYN-103"
        ],
        [
          "MV-G06",
          "Authorized release disposition",
          "No human approval or corrected replay supplied",
          "BLOCKED",
          "MV-I01;MV-I02;MV-I03;MV-I04",
          "Do not support release on this evidence",
          "SYN-103"
        ]
      ],
      "grain": "One specific release-evidence gate, identified by gate_id, for the stated component and intended use."
    }
  ],
  "findings": [
    {
      "id": "MV-F01",
      "title": "Implementation loses inclusive-boundary known positives",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-101",
        "SYN-102"
      ],
      "detail": "V02 V08 V14 V20 each have amount 10000, count 3 and originators 2. R1 is true, while I1 uses greater-than and returns false. Four known positives are lost.",
      "recommendation": "Correct the predicate in a separately versioned proposal and replay all 24 units, equality boundaries and unchanged cases."
    },
    {
      "id": "MV-F02",
      "title": "Missing amount values silently become negative outcomes",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-101",
        "SYN-102"
      ],
      "detail": "V06 V12 V18 V24 lack amount inputs. R1 and C1 return unknown; I1 returns false. These four records cannot support no-hit assurance.",
      "recommendation": "Preserve unknown outputs, recover missing amounts where possible and define a human exception route with measurable aging."
    },
    {
      "id": "MV-F03",
      "title": "Constructed labels and narrow concept do not establish effectiveness",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-101",
        "SYN-102"
      ],
      "detail": "R1 misses four known positives having one originator, and the broader challenger catches them. Raw transaction lineage and independent representative outcomes are not supplied.",
      "recommendation": "Evaluate the concept and alternative mechanisms, obtain independent data and preserve this challenger as diagnostic evidence only."
    },
    {
      "id": "MV-F04",
      "title": "Governance and corrected replay remain unrecorded",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-103"
      ],
      "detail": "The example supplies proposed issues and fictional roles, but no real reviewer qualifications, objectivity assessment, approval or corrected implementation replay.",
      "recommendation": "Obtain actual accountable review evidence and keep release disposition unresolved until material gates are addressed."
    }
  ],
  "evidence": [
    {
      "id": "SYN-101",
      "title": "Twenty-four fictional unit features and independent outcomes",
      "locator": "10-worked-example.md, complete raw feature ledger",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-102",
      "title": "Reference R1, implemented I1 and challenger C1 definitions",
      "locator": "10-worked-example.md, independent predicate specification",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-103",
      "title": "Fictional challenge records and unresolved governance evidence",
      "locator": "10-worked-example.md, issue and gate registers",
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
      "label": "Validation tests",
      "value": 24,
      "method": "Four predeclared tests in each of six domains.",
      "format": "#,##0"
    },
    {
      "label": "Implementation differences",
      "value": 8,
      "method": "Four inclusive-boundary differences plus four null-versus-false differences.",
      "format": "#,##0"
    },
    {
      "label": "Reference known-label recall",
      "value": 0.6666666666666666,
      "format": "0.0%",
      "method": "8 true positives / 12 known positive feature units."
    },
    {
      "label": "Implemented known-label recall",
      "value": 0.3333333333333333,
      "format": "0.0%",
      "method": "4 true positives / 12 known positive feature units."
    }
  ],
  "limitations": [
    "Every record is fictional; results test this supplied procedure and do not establish operational effectiveness.",
    "Illustrative cutoffs, partitions, labels, capacities and severity choices are authored examples, not regulatory thresholds.",
    "Human scope approval, deployment authority, case disposition and reporting decisions are not supplied.",
    "Missing, censored and unresolved evidence remains visible; no favorable default is permitted."
  ],
  "conclusion": "Do not support release of I1 on the supplied evidence. The implementation differs from the reference at inclusive boundaries and missing values; broader effectiveness, transaction lineage, objective review and actual authorization remain unresolved.",
  "report_narrative": [
    [
      "Do not support release of I1 on the supplied evidence. The implementation differs from the reference at inclusive boundaries and missing values; broader effectiveness, transaction lineage, objective review and actual authorization remain unresolved."
    ],
    [
      "The supplied subject is deterministic monitoring logic over 24 feature-level customer-window units. R1 tests amount\u003e=10000, count\u003e=3 and originators\u003e=2; absent amount returns unknown. I1 uses amount\u003e10000 and returns false for absent amount. No universal institutional model classification is implied."
    ],
    [
      "Four known positive boundary units are lost. Four missing amounts are silently changed to false. A separate conceptual limitation excludes four single-originator positives. These mechanisms require distinct findings rather than one combined percentage."
    ],
    [
      "R1 gives TP8 FP0 FN4 TN8; I1 gives TP4 FP0 FN8 TN8; C1 gives TP12 FP0 FN0 TN8. All matrices use twenty known labels. Four UNKNOWN labels stay outside; only R1 and C1 retain unknown input states."
    ],
    [
      "The 24 tests distinguish arithmetic passes from failed concepts or implementation and blocked evidence requests. Four issues remain OPEN or BLOCKED. A passed matrix calculation means the arithmetic is right; it does not mean the underlying system meets its intended use."
    ],
    [
      "SYN-101 contains features, not source transactions. SYN-102 supplies three independent predicate descriptions. SYN-103 records fictional governance gaps. Current public model guidance must be assessed for scope and applicability; this deterministic example is not automatically a model under that definition."
    ],
    [
      "Proposed corrections need versioned implementation evidence, unchanged-case regression tests, feature lineage, independent outcome review and a real human disposition. The challenger is a diagnostic stress of one assumption, not an approved replacement."
    ],
    [
      "Reproduce eight mismatches, split four boundary losses from four missing-state differences, and verify each matrix. No probability interval or deployment approval follows from designed fictional examples. Keep the report in a restricted draft state until the stated evidence gates are resolved."
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
      "finding_id": "MV-F01",
      "proposal": "Correct the predicate in a separately versioned proposal and replay all 24 units, equality boundaries and unchanged cases.",
      "owner": "Proposed accountable role; assignment not recorded",
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "MO-A02",
      "finding_id": "MV-F02",
      "proposal": "Preserve unknown outputs, recover missing amounts where possible and define a human exception route with measurable aging.",
      "owner": "Proposed accountable role; assignment not recorded",
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "MO-A03",
      "finding_id": "MV-F03",
      "proposal": "Evaluate the concept and alternative mechanisms, obtain independent data and preserve this challenger as diagnostic evidence only.",
      "owner": "Proposed accountable role; assignment not recorded",
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "MO-A04",
      "finding_id": "MV-F04",
      "proposal": "Obtain actual accountable review evidence and keep release disposition unresolved until material gates are addressed.",
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
  "suite_id": "monitoring-validation",
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
