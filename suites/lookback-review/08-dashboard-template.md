# Historical Monitoring Lookback and Remediation Review — complete dashboard template

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
<title>Historical Monitoring Lookback and Remediation Review</title>
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
  "slug": "lookback-review",
  "title": "Historical Monitoring Lookback and Remediation Review",
  "summary": "Define and reconcile a historical monitoring review from defect scope through retrieval, deduplication, re-review, expansion and evidence-preserving completion gates.",
  "audience": "Monitoring analysts, independent challenge reviewers and accountable human decision makers",
  "decision": "Which historical units remain exposed or unresolved, and what evidence is necessary before a human can accept the lookback scope and completion?",
  "palette": "indigo",
  "as_of": "2026-10-09",
  "scope": "Complete fictional inputs printed in file 10 only. Public authorities provide context, not evidence about the fictional subjects or an institution-specific mandate.",
  "report_sections": [
    "Lookback status and completion restrictions",
    "Historical scope defect chronology and population",
    "Retrieval review and coverage findings",
    "Complete historical population and intake registers",
    "Review actions expansion and stopping gates",
    "Evidence preservation and unresolved periods",
    "Proposed remediation and case-review handoffs",
    "Limitations quality review and human disposition"
  ],
  "domain_tables": [
    {
      "name": "PeriodReconciliation",
      "columns": [
        "period",
        "expected_units",
        "retrieved_rows",
        "duplicate_rows",
        "retrieved_units",
        "missing_units",
        "known_amount_usd",
        "coverage_state",
        "evidence_ids"
      ],
      "column_contracts": {
        "period": {
          "type": "text",
          "nullable": false,
          "unit": "month",
          "description": "Calendar month in the frozen January through June scope."
        },
        "expected_units": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Independent control-manifest canonical count."
        },
        "retrieved_rows": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Received rows in this period before duplicate removal."
        },
        "duplicate_rows": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Additional representations of an already received canonical unit."
        },
        "retrieved_units": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Distinct in-scope canonical units with some retrieved material."
        },
        "missing_units": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Control units absent from retrieval."
        },
        "known_amount_usd": {
          "type": "number",
          "nullable": false,
          "unit": "USD",
          "description": "Sum of available canonical amounts only; excludes missing amount."
        },
        "coverage_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Whether counts fully reconcile; says nothing about review completeness.",
          "enum": [
            "RECONCILED",
            "PARTIAL"
          ]
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Independent control and retrieval sources."
        }
      },
      "primary_key": [
        "period"
      ],
      "rows": [
        [
          "2026-01",
          5,
          6,
          1,
          5,
          0,
          17500,
          "RECONCILED",
          "SYN-201;SYN-202"
        ],
        [
          "2026-02",
          5,
          5,
          0,
          5,
          0,
          42500,
          "RECONCILED",
          "SYN-201;SYN-202"
        ],
        [
          "2026-03",
          5,
          6,
          1,
          5,
          0,
          67500,
          "RECONCILED",
          "SYN-201;SYN-202"
        ],
        [
          "2026-04",
          5,
          5,
          0,
          5,
          0,
          92500,
          "RECONCILED",
          "SYN-201;SYN-202"
        ],
        [
          "2026-05",
          5,
          6,
          1,
          5,
          0,
          117500,
          "RECONCILED",
          "SYN-201;SYN-202"
        ],
        [
          "2026-06",
          5,
          4,
          0,
          4,
          1,
          112000,
          "PARTIAL",
          "SYN-201;SYN-202"
        ]
      ],
      "formats": {
        "known_amount_usd": "$#,##0.00"
      },
      "grain": "One historical calendar month in the frozen January\u2013June scope, reconciling expected canonical units to received representations."
    },
    {
      "name": "CanonicalUnits",
      "columns": [
        "unit_id",
        "period",
        "source_id",
        "amount_usd",
        "original_state",
        "defect_affected",
        "review_state",
        "new_information",
        "priority",
        "evidence_ids"
      ],
      "column_contracts": {
        "unit_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "One expected historical review unit from the independent manifest."
        },
        "period": {
          "type": "text",
          "nullable": false,
          "unit": "month",
          "description": "Manifest month, not the latest retrieval date."
        },
        "source_id": {
          "type": "text",
          "nullable": true,
          "unit": "identifier",
          "description": "Canonical retrieval row; null for not-retrieved unit L30."
        },
        "amount_usd": {
          "type": "number",
          "nullable": true,
          "unit": "USD",
          "description": "Supplied unit activity amount; absent for L30. Not a loss amount."
        },
        "original_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Historical status preserved unchanged.",
          "enum": [
            "CLOSED",
            "ESCALATED",
            "NOT_GENERATED",
            "UNKNOWN"
          ]
        },
        "defect_affected": {
          "type": "boolean",
          "nullable": true,
          "unit": "flag",
          "description": "Known impact flag; null when the missing record prevents assessment."
        },
        "review_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Current lookback review state, separate from historical state.",
          "enum": [
            "REVIEW_COMPLETE_NO_NEW",
            "REFERRED_FOR_CASE_REVIEW",
            "REREVIEW_REQUIRED",
            "PENDING_REVIEW",
            "UNABLE_TO_ASSESS",
            "NOT_RETRIEVED"
          ]
        },
        "new_information": {
          "type": "boolean",
          "nullable": true,
          "unit": "flag",
          "description": "Comparison outcome; null when review or evidence is incomplete."
        },
        "priority": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Illustrative attention priority; not a legal deadline.",
          "enum": [
            "HIGH",
            "MEDIUM"
          ]
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Exact control and retrieved evidence sources."
        }
      },
      "primary_key": [
        "unit_id"
      ],
      "rows": [
        [
          "L01",
          "2026-01",
          "RAW-01",
          1500,
          "CLOSED",
          true,
          "REVIEW_COMPLETE_NO_NEW",
          false,
          "MEDIUM",
          "SYN-201;SYN-202;SYN-205"
        ],
        [
          "L02",
          "2026-01",
          "RAW-02",
          2500,
          "ESCALATED",
          true,
          "REVIEW_COMPLETE_NO_NEW",
          false,
          "MEDIUM",
          "SYN-201;SYN-202;SYN-205"
        ],
        [
          "L03",
          "2026-01",
          "RAW-03",
          3500,
          "NOT_GENERATED",
          false,
          "REVIEW_COMPLETE_NO_NEW",
          false,
          "MEDIUM",
          "SYN-201;SYN-202;SYN-205"
        ],
        [
          "L04",
          "2026-01",
          "RAW-04",
          4500,
          "CLOSED",
          true,
          "REVIEW_COMPLETE_NO_NEW",
          false,
          "MEDIUM",
          "SYN-201;SYN-202;SYN-205"
        ],
        [
          "L05",
          "2026-01",
          "RAW-05",
          5500,
          "ESCALATED",
          true,
          "REVIEW_COMPLETE_NO_NEW",
          false,
          "MEDIUM",
          "SYN-201;SYN-202;SYN-205"
        ],
        [
          "L06",
          "2026-02",
          "RAW-06",
          6500,
          "NOT_GENERATED",
          false,
          "REVIEW_COMPLETE_NO_NEW",
          false,
          "MEDIUM",
          "SYN-201;SYN-202;SYN-205"
        ],
        [
          "L07",
          "2026-02",
          "RAW-07",
          7500,
          "CLOSED",
          true,
          "REFERRED_FOR_CASE_REVIEW",
          true,
          "HIGH",
          "SYN-201;SYN-202;SYN-205"
        ],
        [
          "L08",
          "2026-02",
          "RAW-08",
          8500,
          "ESCALATED",
          true,
          "REFERRED_FOR_CASE_REVIEW",
          true,
          "HIGH",
          "SYN-201;SYN-202;SYN-205"
        ],
        [
          "L09",
          "2026-02",
          "RAW-09",
          9500,
          "NOT_GENERATED",
          false,
          "REFERRED_FOR_CASE_REVIEW",
          true,
          "HIGH",
          "SYN-201;SYN-202;SYN-205"
        ],
        [
          "L10",
          "2026-02",
          "RAW-10",
          10500,
          "CLOSED",
          true,
          "REFERRED_FOR_CASE_REVIEW",
          true,
          "HIGH",
          "SYN-201;SYN-202;SYN-205"
        ],
        [
          "L11",
          "2026-03",
          "RAW-11",
          11500,
          "ESCALATED",
          true,
          "REFERRED_FOR_CASE_REVIEW",
          true,
          "HIGH",
          "SYN-201;SYN-202;SYN-205"
        ],
        [
          "L12",
          "2026-03",
          "RAW-12",
          12500,
          "NOT_GENERATED",
          false,
          "REFERRED_FOR_CASE_REVIEW",
          true,
          "HIGH",
          "SYN-201;SYN-202;SYN-205"
        ],
        [
          "L13",
          "2026-03",
          "RAW-13",
          13500,
          "CLOSED",
          true,
          "REREVIEW_REQUIRED",
          null,
          "HIGH",
          "SYN-201;SYN-202"
        ],
        [
          "L14",
          "2026-03",
          "RAW-14",
          14500,
          "ESCALATED",
          true,
          "REREVIEW_REQUIRED",
          null,
          "HIGH",
          "SYN-201;SYN-202"
        ],
        [
          "L15",
          "2026-03",
          "RAW-15",
          15500,
          "NOT_GENERATED",
          false,
          "REREVIEW_REQUIRED",
          null,
          "HIGH",
          "SYN-201;SYN-202"
        ],
        [
          "L16",
          "2026-04",
          "RAW-16",
          16500,
          "CLOSED",
          true,
          "REREVIEW_REQUIRED",
          null,
          "HIGH",
          "SYN-201;SYN-202"
        ],
        [
          "L17",
          "2026-04",
          "RAW-17",
          17500,
          "ESCALATED",
          true,
          "REREVIEW_REQUIRED",
          null,
          "HIGH",
          "SYN-201;SYN-202"
        ],
        [
          "L18",
          "2026-04",
          "RAW-18",
          18500,
          "NOT_GENERATED",
          false,
          "REREVIEW_REQUIRED",
          null,
          "HIGH",
          "SYN-201;SYN-202"
        ],
        [
          "L19",
          "2026-04",
          "RAW-19",
          19500,
          "CLOSED",
          true,
          "PENDING_REVIEW",
          null,
          "MEDIUM",
          "SYN-201;SYN-202"
        ],
        [
          "L20",
          "2026-04",
          "RAW-20",
          20500,
          "ESCALATED",
          true,
          "PENDING_REVIEW",
          null,
          "MEDIUM",
          "SYN-201;SYN-202"
        ],
        [
          "L21",
          "2026-05",
          "RAW-21",
          21500,
          "NOT_GENERATED",
          false,
          "PENDING_REVIEW",
          null,
          "MEDIUM",
          "SYN-201;SYN-202"
        ],
        [
          "L22",
          "2026-05",
          "RAW-22",
          22500,
          "CLOSED",
          true,
          "PENDING_REVIEW",
          null,
          "MEDIUM",
          "SYN-201;SYN-202"
        ],
        [
          "L23",
          "2026-05",
          "RAW-23",
          23500,
          "ESCALATED",
          true,
          "PENDING_REVIEW",
          null,
          "MEDIUM",
          "SYN-201;SYN-202"
        ],
        [
          "L24",
          "2026-05",
          "RAW-24",
          24500,
          "NOT_GENERATED",
          false,
          "PENDING_REVIEW",
          null,
          "MEDIUM",
          "SYN-201;SYN-202"
        ],
        [
          "L25",
          "2026-05",
          "RAW-25",
          25500,
          "CLOSED",
          true,
          "UNABLE_TO_ASSESS",
          null,
          "HIGH",
          "SYN-201;SYN-202"
        ],
        [
          "L26",
          "2026-06",
          "RAW-26",
          26500,
          "ESCALATED",
          true,
          "UNABLE_TO_ASSESS",
          null,
          "HIGH",
          "SYN-201;SYN-202"
        ],
        [
          "L27",
          "2026-06",
          "RAW-27",
          27500,
          "NOT_GENERATED",
          false,
          "UNABLE_TO_ASSESS",
          null,
          "HIGH",
          "SYN-201;SYN-202"
        ],
        [
          "L28",
          "2026-06",
          "RAW-28",
          28500,
          "CLOSED",
          true,
          "UNABLE_TO_ASSESS",
          null,
          "HIGH",
          "SYN-201;SYN-202"
        ],
        [
          "L29",
          "2026-06",
          "RAW-29",
          29500,
          "ESCALATED",
          true,
          "UNABLE_TO_ASSESS",
          null,
          "HIGH",
          "SYN-201;SYN-202"
        ],
        [
          "L30",
          "2026-06",
          null,
          null,
          "UNKNOWN",
          null,
          "NOT_RETRIEVED",
          null,
          "HIGH",
          "SYN-201"
        ]
      ],
      "formats": {
        "amount_usd": "$#,##0.00"
      },
      "foreign_keys": [
        {
          "columns": [
            "period"
          ],
          "table": "PeriodReconciliation",
          "references": [
            "period"
          ]
        }
      ],
      "grain": "One independently expected historical review unit, identified by unit_id, including an unretrieved placeholder when source evidence is absent."
    },
    {
      "name": "RetrievalLedger",
      "columns": [
        "raw_id",
        "unit_id",
        "source_period",
        "classification",
        "canonical_id",
        "raw_amount_usd",
        "evidence_ids"
      ],
      "column_contracts": {
        "raw_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique received representation identifier."
        },
        "unit_id": {
          "type": "text",
          "nullable": true,
          "unit": "identifier",
          "description": "Matched in-scope canonical unit; null for out-of-scope July records."
        },
        "source_period": {
          "type": "text",
          "nullable": false,
          "unit": "month",
          "description": "Historical month associated with the received record."
        },
        "classification": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exactly one intake accounting bucket.",
          "enum": [
            "CANONICAL",
            "DUPLICATE",
            "OUT_OF_SCOPE"
          ]
        },
        "canonical_id": {
          "type": "text",
          "nullable": true,
          "unit": "identifier",
          "description": "Retained canonical unit for matching rows; null when out of scope."
        },
        "raw_amount_usd": {
          "type": "number",
          "nullable": false,
          "unit": "USD",
          "description": "Amount on this raw representation before deduplication; do not aggregate as canonical activity."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Retrieval input source."
        }
      },
      "primary_key": [
        "raw_id"
      ],
      "rows": [
        [
          "RAW-01",
          "L01",
          "2026-01",
          "CANONICAL",
          "L01",
          1500,
          "SYN-202"
        ],
        [
          "RAW-02",
          "L02",
          "2026-01",
          "CANONICAL",
          "L02",
          2500,
          "SYN-202"
        ],
        [
          "RAW-03",
          "L03",
          "2026-01",
          "CANONICAL",
          "L03",
          3500,
          "SYN-202"
        ],
        [
          "RAW-04",
          "L04",
          "2026-01",
          "CANONICAL",
          "L04",
          4500,
          "SYN-202"
        ],
        [
          "RAW-05",
          "L05",
          "2026-01",
          "CANONICAL",
          "L05",
          5500,
          "SYN-202"
        ],
        [
          "RAW-06",
          "L06",
          "2026-02",
          "CANONICAL",
          "L06",
          6500,
          "SYN-202"
        ],
        [
          "RAW-07",
          "L07",
          "2026-02",
          "CANONICAL",
          "L07",
          7500,
          "SYN-202"
        ],
        [
          "RAW-08",
          "L08",
          "2026-02",
          "CANONICAL",
          "L08",
          8500,
          "SYN-202"
        ],
        [
          "RAW-09",
          "L09",
          "2026-02",
          "CANONICAL",
          "L09",
          9500,
          "SYN-202"
        ],
        [
          "RAW-10",
          "L10",
          "2026-02",
          "CANONICAL",
          "L10",
          10500,
          "SYN-202"
        ],
        [
          "RAW-11",
          "L11",
          "2026-03",
          "CANONICAL",
          "L11",
          11500,
          "SYN-202"
        ],
        [
          "RAW-12",
          "L12",
          "2026-03",
          "CANONICAL",
          "L12",
          12500,
          "SYN-202"
        ],
        [
          "RAW-13",
          "L13",
          "2026-03",
          "CANONICAL",
          "L13",
          13500,
          "SYN-202"
        ],
        [
          "RAW-14",
          "L14",
          "2026-03",
          "CANONICAL",
          "L14",
          14500,
          "SYN-202"
        ],
        [
          "RAW-15",
          "L15",
          "2026-03",
          "CANONICAL",
          "L15",
          15500,
          "SYN-202"
        ],
        [
          "RAW-16",
          "L16",
          "2026-04",
          "CANONICAL",
          "L16",
          16500,
          "SYN-202"
        ],
        [
          "RAW-17",
          "L17",
          "2026-04",
          "CANONICAL",
          "L17",
          17500,
          "SYN-202"
        ],
        [
          "RAW-18",
          "L18",
          "2026-04",
          "CANONICAL",
          "L18",
          18500,
          "SYN-202"
        ],
        [
          "RAW-19",
          "L19",
          "2026-04",
          "CANONICAL",
          "L19",
          19500,
          "SYN-202"
        ],
        [
          "RAW-20",
          "L20",
          "2026-04",
          "CANONICAL",
          "L20",
          20500,
          "SYN-202"
        ],
        [
          "RAW-21",
          "L21",
          "2026-05",
          "CANONICAL",
          "L21",
          21500,
          "SYN-202"
        ],
        [
          "RAW-22",
          "L22",
          "2026-05",
          "CANONICAL",
          "L22",
          22500,
          "SYN-202"
        ],
        [
          "RAW-23",
          "L23",
          "2026-05",
          "CANONICAL",
          "L23",
          23500,
          "SYN-202"
        ],
        [
          "RAW-24",
          "L24",
          "2026-05",
          "CANONICAL",
          "L24",
          24500,
          "SYN-202"
        ],
        [
          "RAW-25",
          "L25",
          "2026-05",
          "CANONICAL",
          "L25",
          25500,
          "SYN-202"
        ],
        [
          "RAW-26",
          "L26",
          "2026-06",
          "CANONICAL",
          "L26",
          26500,
          "SYN-202"
        ],
        [
          "RAW-27",
          "L27",
          "2026-06",
          "CANONICAL",
          "L27",
          27500,
          "SYN-202"
        ],
        [
          "RAW-28",
          "L28",
          "2026-06",
          "CANONICAL",
          "L28",
          28500,
          "SYN-202"
        ],
        [
          "RAW-29",
          "L29",
          "2026-06",
          "CANONICAL",
          "L29",
          29500,
          "SYN-202"
        ],
        [
          "RAW-D1",
          "L02",
          "2026-01",
          "DUPLICATE",
          "L02",
          2500,
          "SYN-202"
        ],
        [
          "RAW-D2",
          "L12",
          "2026-03",
          "DUPLICATE",
          "L12",
          12500,
          "SYN-202"
        ],
        [
          "RAW-D3",
          "L22",
          "2026-05",
          "DUPLICATE",
          "L22",
          22500,
          "SYN-202"
        ],
        [
          "RAW-X31",
          null,
          "2026-07",
          "OUT_OF_SCOPE",
          null,
          31500,
          "SYN-202"
        ],
        [
          "RAW-X32",
          null,
          "2026-07",
          "OUT_OF_SCOPE",
          null,
          32500,
          "SYN-202"
        ]
      ],
      "formats": {
        "raw_amount_usd": "$#,##0.00"
      },
      "foreign_keys": [
        {
          "columns": [
            "unit_id"
          ],
          "table": "CanonicalUnits",
          "references": [
            "unit_id"
          ]
        },
        {
          "columns": [
            "canonical_id"
          ],
          "table": "CanonicalUnits",
          "references": [
            "unit_id"
          ]
        }
      ],
      "grain": "One received source representation, identified by raw_id, before canonical deduplication or scope exclusion."
    },
    {
      "name": "ReviewActions",
      "columns": [
        "action_id",
        "unit_id",
        "review_state",
        "action_state",
        "observed_basis",
        "required_next_step",
        "comparison_id",
        "human_disposition",
        "evidence_ids"
      ],
      "column_contracts": {
        "action_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique historical-unit action identifier."
        },
        "unit_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Canonical unit requiring or receiving review."
        },
        "review_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "State replicated from CanonicalUnits to permit reconciliation.",
          "enum": [
            "REVIEW_COMPLETE_NO_NEW",
            "REFERRED_FOR_CASE_REVIEW",
            "REREVIEW_REQUIRED",
            "PENDING_REVIEW",
            "UNABLE_TO_ASSESS",
            "NOT_RETRIEVED"
          ]
        },
        "action_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Operational work position; a handoff is not closed.",
          "enum": [
            "DESK_REVIEW_COMPLETE",
            "HANDOFF_OPEN",
            "REVIEW_OPEN",
            "EVIDENCE_BLOCKED",
            "RETRIEVAL_BLOCKED"
          ]
        },
        "observed_basis": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Fictional basis supporting this work state."
        },
        "required_next_step": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Specific evidence-preserving work proposal."
        },
        "comparison_id": {
          "type": "text",
          "nullable": true,
          "unit": "identifier",
          "description": "Populated comparison packet ID for the twelve desk-complete units; null where no completed packet exists."
        },
        "human_disposition": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Actual institutional acceptance is absent.",
          "enum": [
            "NOT_RECORDED"
          ]
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Review-state source."
        }
      },
      "primary_key": [
        "action_id"
      ],
      "rows": [
        [
          "LA-L01",
          "L01",
          "REVIEW_COMPLETE_NO_NEW",
          "DESK_REVIEW_COMPLETE",
          "Fictional re-review found no new information within supplied scope",
          "Preserve comparison and independent QA; no filing judgment inferred",
          "COMP-L01",
          "NOT_RECORDED",
          "SYN-203;SYN-205"
        ],
        [
          "LA-L02",
          "L02",
          "REVIEW_COMPLETE_NO_NEW",
          "DESK_REVIEW_COMPLETE",
          "Fictional re-review found no new information within supplied scope",
          "Preserve comparison and independent QA; no filing judgment inferred",
          "COMP-L02",
          "NOT_RECORDED",
          "SYN-203;SYN-205"
        ],
        [
          "LA-L03",
          "L03",
          "REVIEW_COMPLETE_NO_NEW",
          "DESK_REVIEW_COMPLETE",
          "Fictional re-review found no new information within supplied scope",
          "Preserve comparison and independent QA; no filing judgment inferred",
          "COMP-L03",
          "NOT_RECORDED",
          "SYN-203;SYN-205"
        ],
        [
          "LA-L04",
          "L04",
          "REVIEW_COMPLETE_NO_NEW",
          "DESK_REVIEW_COMPLETE",
          "Fictional re-review found no new information within supplied scope",
          "Preserve comparison and independent QA; no filing judgment inferred",
          "COMP-L04",
          "NOT_RECORDED",
          "SYN-203;SYN-205"
        ],
        [
          "LA-L05",
          "L05",
          "REVIEW_COMPLETE_NO_NEW",
          "DESK_REVIEW_COMPLETE",
          "Fictional re-review found no new information within supplied scope",
          "Preserve comparison and independent QA; no filing judgment inferred",
          "COMP-L05",
          "NOT_RECORDED",
          "SYN-203;SYN-205"
        ],
        [
          "LA-L06",
          "L06",
          "REVIEW_COMPLETE_NO_NEW",
          "DESK_REVIEW_COMPLETE",
          "Fictional re-review found no new information within supplied scope",
          "Preserve comparison and independent QA; no filing judgment inferred",
          "COMP-L06",
          "NOT_RECORDED",
          "SYN-203;SYN-205"
        ],
        [
          "LA-L07",
          "L07",
          "REFERRED_FOR_CASE_REVIEW",
          "HANDOFF_OPEN",
          "New information exists in comparison packet",
          "Obtain authorized case review acknowledgment and decision evidence",
          "COMP-L07",
          "NOT_RECORDED",
          "SYN-203;SYN-205"
        ],
        [
          "LA-L08",
          "L08",
          "REFERRED_FOR_CASE_REVIEW",
          "HANDOFF_OPEN",
          "New information exists in comparison packet",
          "Obtain authorized case review acknowledgment and decision evidence",
          "COMP-L08",
          "NOT_RECORDED",
          "SYN-203;SYN-205"
        ],
        [
          "LA-L09",
          "L09",
          "REFERRED_FOR_CASE_REVIEW",
          "HANDOFF_OPEN",
          "New information exists in comparison packet",
          "Obtain authorized case review acknowledgment and decision evidence",
          "COMP-L09",
          "NOT_RECORDED",
          "SYN-203;SYN-205"
        ],
        [
          "LA-L10",
          "L10",
          "REFERRED_FOR_CASE_REVIEW",
          "HANDOFF_OPEN",
          "New information exists in comparison packet",
          "Obtain authorized case review acknowledgment and decision evidence",
          "COMP-L10",
          "NOT_RECORDED",
          "SYN-203;SYN-205"
        ],
        [
          "LA-L11",
          "L11",
          "REFERRED_FOR_CASE_REVIEW",
          "HANDOFF_OPEN",
          "New information exists in comparison packet",
          "Obtain authorized case review acknowledgment and decision evidence",
          "COMP-L11",
          "NOT_RECORDED",
          "SYN-203;SYN-205"
        ],
        [
          "LA-L12",
          "L12",
          "REFERRED_FOR_CASE_REVIEW",
          "HANDOFF_OPEN",
          "New information exists in comparison packet",
          "Obtain authorized case review acknowledgment and decision evidence",
          "COMP-L12",
          "NOT_RECORDED",
          "SYN-203;SYN-205"
        ],
        [
          "LA-L13",
          "L13",
          "REREVIEW_REQUIRED",
          "REVIEW_OPEN",
          "Prior reasoning does not address changed defect context",
          "Reperform analysis against recovered evidence and preserve original rationale",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L14",
          "L14",
          "REREVIEW_REQUIRED",
          "REVIEW_OPEN",
          "Prior reasoning does not address changed defect context",
          "Reperform analysis against recovered evidence and preserve original rationale",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L15",
          "L15",
          "REREVIEW_REQUIRED",
          "REVIEW_OPEN",
          "Prior reasoning does not address changed defect context",
          "Reperform analysis against recovered evidence and preserve original rationale",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L16",
          "L16",
          "REREVIEW_REQUIRED",
          "REVIEW_OPEN",
          "Prior reasoning does not address changed defect context",
          "Reperform analysis against recovered evidence and preserve original rationale",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L17",
          "L17",
          "REREVIEW_REQUIRED",
          "REVIEW_OPEN",
          "Prior reasoning does not address changed defect context",
          "Reperform analysis against recovered evidence and preserve original rationale",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L18",
          "L18",
          "REREVIEW_REQUIRED",
          "REVIEW_OPEN",
          "Prior reasoning does not address changed defect context",
          "Reperform analysis against recovered evidence and preserve original rationale",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L19",
          "L19",
          "PENDING_REVIEW",
          "REVIEW_OPEN",
          "No completed desk review record supplied",
          "Assign reviewer and preserve priority; completion cannot be inferred",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L20",
          "L20",
          "PENDING_REVIEW",
          "REVIEW_OPEN",
          "No completed desk review record supplied",
          "Assign reviewer and preserve priority; completion cannot be inferred",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L21",
          "L21",
          "PENDING_REVIEW",
          "REVIEW_OPEN",
          "No completed desk review record supplied",
          "Assign reviewer and preserve priority; completion cannot be inferred",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L22",
          "L22",
          "PENDING_REVIEW",
          "REVIEW_OPEN",
          "No completed desk review record supplied",
          "Assign reviewer and preserve priority; completion cannot be inferred",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L23",
          "L23",
          "PENDING_REVIEW",
          "REVIEW_OPEN",
          "No completed desk review record supplied",
          "Assign reviewer and preserve priority; completion cannot be inferred",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L24",
          "L24",
          "PENDING_REVIEW",
          "REVIEW_OPEN",
          "No completed desk review record supplied",
          "Assign reviewer and preserve priority; completion cannot be inferred",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L25",
          "L25",
          "UNABLE_TO_ASSESS",
          "EVIDENCE_BLOCKED",
          "Retrieved summary lacks essential supporting evidence",
          "Recover missing support or record qualified scope limitation",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L26",
          "L26",
          "UNABLE_TO_ASSESS",
          "EVIDENCE_BLOCKED",
          "Retrieved summary lacks essential supporting evidence",
          "Recover missing support or record qualified scope limitation",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L27",
          "L27",
          "UNABLE_TO_ASSESS",
          "EVIDENCE_BLOCKED",
          "Retrieved summary lacks essential supporting evidence",
          "Recover missing support or record qualified scope limitation",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L28",
          "L28",
          "UNABLE_TO_ASSESS",
          "EVIDENCE_BLOCKED",
          "Retrieved summary lacks essential supporting evidence",
          "Recover missing support or record qualified scope limitation",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L29",
          "L29",
          "UNABLE_TO_ASSESS",
          "EVIDENCE_BLOCKED",
          "Retrieved summary lacks essential supporting evidence",
          "Recover missing support or record qualified scope limitation",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ],
        [
          "LA-L30",
          "L30",
          "NOT_RETRIEVED",
          "RETRIEVAL_BLOCKED",
          "Control manifest names a unit absent from retrieval",
          "Recover archive record or retain unreconciled coverage gap",
          null,
          "NOT_RECORDED",
          "SYN-203"
        ]
      ],
      "foreign_keys": [
        {
          "columns": [
            "unit_id"
          ],
          "table": "CanonicalUnits",
          "references": [
            "unit_id"
          ]
        },
        {
          "columns": [
            "comparison_id"
          ],
          "table": "ComparisonPackets",
          "references": [
            "comparison_id"
          ]
        }
      ],
      "grain": "One current lookback work action for one canonical unit, identified by action_id, with a separate comparison and human-disposition state."
    },
    {
      "name": "ExpansionDecisions",
      "columns": [
        "expansion_id",
        "trigger",
        "proposed_scope",
        "inclusion_rule",
        "stopping_condition",
        "decision_state",
        "evidence_ids"
      ],
      "column_contracts": {
        "expansion_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable scope-change or stopping decision key."
        },
        "trigger": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Specific new evidence or observed condition."
        },
        "proposed_scope": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Bounded additional review population or work."
        },
        "inclusion_rule": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact predicate for the proposed change."
        },
        "stopping_condition": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Evidence needed to stop the associated work."
        },
        "decision_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Proposals do not invent actual human acceptance.",
          "enum": [
            "PROPOSED",
            "BLOCKED"
          ]
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Supporting scope or defect evidence."
        }
      },
      "primary_key": [
        "expansion_id"
      ],
      "rows": [
        [
          "EX-01",
          "Initial January through March review cannot exclude later mapping impact",
          "Extend analytical fixture through June 30",
          "Manifest period 2026-04 through 2026-06",
          "Reconcile all fifteen added canonical units and impact evidence",
          "PROPOSED",
          "SYN-201;SYN-204"
        ],
        [
          "EX-02",
          "L30 missing despite independent June control count",
          "Recover June archive and linkage records",
          "Canonical unit L30 plus source representations matching its key",
          "L30 recovered or documented unreconciled coverage limitation remains",
          "BLOCKED",
          "SYN-201;SYN-202"
        ],
        [
          "EX-03",
          "Six comparison packets identify new information",
          "Route L07 through L12 to authorized case review",
          "new_information=true",
          "Acknowledged referral and later authorized decision evidence",
          "PROPOSED",
          "SYN-203"
        ],
        [
          "EX-04",
          "Six prior reviews do not address revised defect context",
          "Re-review L13 through L18",
          "review_state=REREVIEW_REQUIRED",
          "Complete fresh comparison preserving historical record",
          "PROPOSED",
          "SYN-203"
        ],
        [
          "EX-05",
          "Five retrieved summaries lack essential support",
          "Recover support for L25 through L29",
          "review_state=UNABLE_TO_ASSESS",
          "Support recovered and reviewed or qualified scope limit retained",
          "BLOCKED",
          "SYN-203"
        ],
        [
          "EX-06",
          "July rows are outside current analytical boundary",
          "Assess whether defect evidence crosses June 30 before adding July",
          "Mapping continuity evidence beyond 2026-06-30",
          "Documented boundary evidence; no silent inclusion or dismissal",
          "PROPOSED",
          "SYN-202;SYN-204"
        ]
      ],
      "grain": "One bounded scope-change, recovery or review proposal, identified by expansion_id, with its trigger and stopping condition."
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
          "SYN-201",
          "SYNTHETIC_INPUT",
          "2026-10-09",
          "COMPLETE_FIXTURE",
          30,
          "expected canonical historical units",
          "Manifest counts do not supply absent record content.",
          "SYN-201"
        ],
        [
          "SYN-202",
          "SYNTHETIC_INPUT",
          "2026-10-09",
          "PARTIAL_FIXTURE",
          34,
          "received representations including duplicates and exclusions",
          "One expected canonical unit is missing; retrieved summaries may lack support.",
          "SYN-202"
        ],
        [
          "SYN-203",
          "SYNTHETIC_DECISION",
          "2026-10-09",
          "PARTIAL_FIXTURE",
          30,
          "review-state assignments",
          "Twelve desk comparisons complete; six have no open unit action; actual institutional disposition not supplied.",
          "SYN-203"
        ],
        [
          "SYN-204",
          "SYNTHETIC_INPUT",
          "2026-10-09",
          "PARTIAL_FIXTURE",
          7,
          "dated mapping-version records",
          "July continuity and actual production correction remain unverified.",
          "SYN-204"
        ],
        [
          "SYN-205",
          "SYNTHETIC_INPUT",
          "2026-10-09",
          "COMPLETE_FIXTURE",
          12,
          "historical/current comparison packets",
          "Completed desk comparison is separate from actual case disposition.",
          "SYN-205"
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
          "LB-Q01",
          "Raw intake accounting",
          "34=29 canonical+3 duplicate+2 out-of-scope",
          "34=29+3+2",
          "PASS",
          "Fictional checker",
          "SYN-202"
        ],
        [
          "LB-Q02",
          "Expected scope accounting",
          "30=29 retrieved+1 missing",
          "30=29+1;L30 absent",
          "PASS",
          "Fictional checker",
          "SYN-201;SYN-202"
        ],
        [
          "LB-Q03",
          "Full retrieval coverage",
          "All 30 expected units retrieved",
          "29/30 retrieved; June 4/5",
          "FAIL",
          "Fictional checker",
          "SYN-201;SYN-202"
        ],
        [
          "LB-Q04",
          "Canonical amount conservation",
          "Known amounts 449500; missing unit excluded explicitly",
          "449500 known; L30 amount null",
          "PASS",
          "Fictional checker",
          "SYN-201;SYN-202"
        ],
        [
          "LB-Q05",
          "Desk review completion",
          "6 no-new plus 6 referred =12 examined",
          "12/30 examined;6 handoffs still open",
          "PASS",
          "Fictional checker",
          "SYN-203"
        ],
        [
          "LB-Q06",
          "Whole-lookback completion",
          "No material unresolved review retrieval or handoff",
          "24 units retain open dependency;6 desk-complete only",
          "FAIL",
          "Fictional checker",
          "SYN-203"
        ],
        [
          "LB-Q07",
          "No missing-to-negative conversion",
          "L30 remains not retrieved and impact unknown",
          "L30 source amount impact and new_information remain null",
          "PASS",
          "Fictional checker",
          "SYN-201"
        ],
        [
          "LB-Q08",
          "Filing or closure decision",
          "Separate authorized human process required",
          "NOT_RECORDED",
          "NOT_TESTED",
          "NOT_RECORDED",
          "SYN-203"
        ]
      ],
      "grain": "One explicitly scoped fixture quality check, identified by check_id, with expected and actual results."
    },
    {
      "name": "CompletionGates",
      "columns": [
        "gate_id",
        "gate",
        "numerator",
        "denominator",
        "state",
        "residual",
        "permitted_statement",
        "evidence_ids"
      ],
      "column_contracts": {
        "gate_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique stopping or completion gate."
        },
        "gate": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Evidence required for the stated completion claim."
        },
        "numerator": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Satisfied units at the stated denominator grain."
        },
        "denominator": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Complete in-scope population for this gate."
        },
        "state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "SATISFIED_FIXTURE_ONLY does not mean operational signoff.",
          "enum": [
            "SATISFIED_FIXTURE_ONLY",
            "FAILED",
            "BLOCKED"
          ]
        },
        "residual": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Specific unresolved gap."
        },
        "permitted_statement": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Narrow completion statement supported by the record."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Evidence supporting the gate."
        }
      },
      "primary_key": [
        "gate_id"
      ],
      "rows": [
        [
          "LB-G01",
          "Raw rows assigned an intake bucket",
          34,
          34,
          "SATISFIED_FIXTURE_ONLY",
          "None within supplied intake",
          "All received rows classified; expected population still missing one",
          "SYN-202"
        ],
        [
          "LB-G02",
          "Expected canonical units retrieved",
          29,
          30,
          "FAILED",
          "L30 not retrieved",
          "Retrieval coverage 29/30; no complete-coverage claim",
          "SYN-201;SYN-202"
        ],
        [
          "LB-G03",
          "Desk comparison completed",
          12,
          30,
          "FAILED",
          "18 not desk-complete",
          "12 comparisons completed, including 6 unresolved referrals",
          "SYN-203"
        ],
        [
          "LB-G04",
          "Desk review with no open unit action",
          6,
          30,
          "FAILED",
          "24 units retain review evidence retrieval or handoff dependency",
          "6 units have completed no-new-information comparisons",
          "SYN-203"
        ],
        [
          "LB-G05",
          "Referred units acknowledged and disposed",
          0,
          6,
          "BLOCKED",
          "No actual receiving-case decision evidence",
          "Six handoffs remain open",
          "SYN-203"
        ],
        [
          "LB-G06",
          "Authorized whole-review acceptance",
          0,
          1,
          "BLOCKED",
          "Actual approval and accepted limitations absent",
          "Lookback remains incomplete",
          "SYN-203;SYN-204"
        ]
      ],
      "grain": "One distinct completion claim, identified by gate_id, with its own expressly stated numerator and denominator grain."
    },
    {
      "name": "ComparisonPackets",
      "columns": [
        "comparison_id",
        "unit_id",
        "historical_cutoff",
        "historical_source",
        "historical_fact_ids",
        "historical_facts",
        "historical_rationale",
        "recovered_date",
        "recovered_source",
        "current_fact_ids",
        "current_observation",
        "source_path",
        "material_delta",
        "expected_route",
        "evidence_ids"
      ],
      "column_contracts": {
        "comparison_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique populated historical/current packet ID."
        },
        "unit_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Canonical unit whose desk comparison is documented."
        },
        "historical_cutoff": {
          "type": "text",
          "nullable": false,
          "unit": "date",
          "description": "Date through which the fictional historical packet was available."
        },
        "historical_source": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Printed historical source packet locator."
        },
        "historical_fact_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Semicolon-delimited material facts available historically."
        },
        "historical_facts": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Concrete facts actually present in the original packet."
        },
        "historical_rationale": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Original reasoning preserved without retrospective rewriting."
        },
        "recovered_date": {
          "type": "text",
          "nullable": false,
          "unit": "date",
          "description": "Date newly retrieved source material became available."
        },
        "recovered_source": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Printed recovered source packet locator."
        },
        "current_fact_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Complete current material fact set; additions drive the new-information test."
        },
        "current_observation": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Concrete current facts and whether they differ from the historical basis."
        },
        "source_path": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Supplied source feed path, not inferred from historical disposition.",
          "enum": [
            "PATH_A",
            "PATH_B",
            "PATH_C"
          ]
        },
        "material_delta": {
          "type": "boolean",
          "nullable": false,
          "unit": "flag",
          "description": "True exactly when the current material fact set adds a fact outside the historical set."
        },
        "expected_route": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Completed comparison result; referral disposition remains open.",
          "enum": [
            "REVIEW_COMPLETE_NO_NEW",
            "REFERRED_FOR_CASE_REVIEW"
          ]
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Source for the complete packet and fact dictionary."
        }
      },
      "primary_key": [
        "comparison_id"
      ],
      "rows": [
        [
          "COMP-L01",
          "L01",
          "2026-01-31",
          "HIST-L01",
          "L01-F1;L01-F2",
          "Payroll credits from two identified employers matched the supplied pay records.",
          "The historical review already inspected both payer identities and pay records.",
          "2026-10-02",
          "REC-L01",
          "L01-F1;L01-F2",
          "Both payer identities, amounts and pay-record matches are unchanged; corrected monitoring count adds no unseen fact.",
          "PATH_A",
          false,
          "REVIEW_COMPLETE_NO_NEW",
          "SYN-205"
        ],
        [
          "COMP-L02",
          "L02",
          "2026-01-31",
          "HIST-L02",
          "L02-F1;L02-F2",
          "Four originators and the complete activity were already included in the earlier escalation packet.",
          "Historical escalation expressly covered all four identified originators.",
          "2026-10-02",
          "REC-L02",
          "L02-F1;L02-F2",
          "Recovered source messages match the four identities and activity already escalated; no additional party or transaction is found.",
          "PATH_B",
          false,
          "REVIEW_COMPLETE_NO_NEW",
          "SYN-205"
        ],
        [
          "COMP-L03",
          "L03",
          "2026-01-31",
          "HIST-L03",
          "L03-F1;L03-F2",
          "One documented transfer from the same beneficial owner matched the account ownership evidence.",
          "The correctly mapped control path produced no scenario hit and the underlying ownership fact was documented.",
          "2026-10-02",
          "REC-L03",
          "L03-F1;L03-F2",
          "The source-path replay and ownership documentation are unchanged.",
          "PATH_C",
          false,
          "REVIEW_COMPLETE_NO_NEW",
          "SYN-205"
        ],
        [
          "COMP-L04",
          "L04",
          "2026-01-31",
          "HIST-L04",
          "L04-F1;L04-F2",
          "Three commercial payers matched the supplied invoices and recorded business counterparties.",
          "Historical closure relied on inspected invoice and counterparty matches, not the defective aggregate alone.",
          "2026-10-02",
          "REC-L04",
          "L04-F1;L04-F2",
          "Recovered messages preserve the same three payers and invoice references with no contradiction.",
          "PATH_A",
          false,
          "REVIEW_COMPLETE_NO_NEW",
          "SYN-205"
        ],
        [
          "COMP-L05",
          "L05",
          "2026-01-31",
          "HIST-L05",
          "L05-F1;L05-F2",
          "Five originators and their activity were fully described in the earlier escalation.",
          "The historical packet included the source messages and all five counterparties.",
          "2026-10-02",
          "REC-L05",
          "L05-F1;L05-F2",
          "The replay identifies the same five parties already in that packet; no new transaction or identity is added.",
          "PATH_B",
          false,
          "REVIEW_COMPLETE_NO_NEW",
          "SYN-205"
        ],
        [
          "COMP-L06",
          "L06",
          "2026-02-28",
          "HIST-L06",
          "L06-F1;L06-F2",
          "A single internal operating transfer matched the supplied account mapping.",
          "The control path mapped the actual originator and the activity remained outside the scenario concept.",
          "2026-10-02",
          "REC-L06",
          "L06-F1;L06-F2",
          "The original source and current replay agree on the same internal account and purpose.",
          "PATH_C",
          false,
          "REVIEW_COMPLETE_NO_NEW",
          "SYN-205"
        ],
        [
          "COMP-L07",
          "L07",
          "2026-02-28",
          "HIST-L07",
          "L07-F1;L07-F2",
          "The historical summary described all credits as transfers from the same customer-controlled account.",
          "Closure relied on the one-originator summary and did not include underlying payment messages.",
          "2026-10-02",
          "REC-L07",
          "L07-F1;L07-F2;L07-F3",
          "Recovered messages identify four third-party originator IDs; three are absent from the historical packet and their purpose is unsupported.",
          "PATH_A",
          true,
          "REFERRED_FOR_CASE_REVIEW",
          "SYN-205"
        ],
        [
          "COMP-L08",
          "L08",
          "2026-02-28",
          "HIST-L08",
          "L08-F1;L08-F2",
          "The prior escalation packet identified two originators and stated that it covered the complete relationship.",
          "The earlier referral scope was limited to those two identities and their supplied activity.",
          "2026-10-02",
          "REC-L08",
          "L08-F1;L08-F2;L08-F3",
          "Recovered messages identify seven originators; five additional identities were outside the earlier scope.",
          "PATH_B",
          true,
          "REFERRED_FOR_CASE_REVIEW",
          "SYN-205"
        ],
        [
          "COMP-L09",
          "L09",
          "2026-02-28",
          "HIST-L09",
          "L09-F1;L09-F2",
          "The control-path unit showed one payer and a supplier-payment explanation.",
          "No scenario hit was generated; the supplied original packet contained the stated supplier rationale.",
          "2026-10-02",
          "REC-L09",
          "L09-F1;L09-F2;L09-F3",
          "A newly recovered contract names a different economic supplier than the payment message, creating an identity-purpose inconsistency unrelated to the mapping defect.",
          "PATH_C",
          true,
          "REFERRED_FOR_CASE_REVIEW",
          "SYN-205"
        ],
        [
          "COMP-L10",
          "L10",
          "2026-02-28",
          "HIST-L10",
          "L10-F1;L10-F2",
          "The historical review treated the credits as customer self-funding based on the summary identity.",
          "Closure relied on apparent common ownership without the underlying message identities.",
          "2026-10-02",
          "REC-L10",
          "L10-F1;L10-F2;L10-F3",
          "Five distinct third-party originators appear in recovered messages and the claimed ownership link is not supported.",
          "PATH_A",
          true,
          "REFERRED_FOR_CASE_REVIEW",
          "SYN-205"
        ],
        [
          "COMP-L11",
          "L11",
          "2026-03-31",
          "HIST-L11",
          "L11-F1;L11-F2",
          "The prior escalation described three counterparties and excluded no known message records.",
          "Its stated scope and rationale addressed those three named parties only.",
          "2026-10-02",
          "REC-L11",
          "L11-F1;L11-F2;L11-F3",
          "The corrected message grouping identifies three additional counterparties, including activity outside the original referral narrative.",
          "PATH_B",
          true,
          "REFERRED_FOR_CASE_REVIEW",
          "SYN-205"
        ],
        [
          "COMP-L12",
          "L12",
          "2026-03-31",
          "HIST-L12",
          "L12-F1;L12-F2",
          "The control-path unit had one identified payer and an equipment-sale explanation.",
          "The original source did not contradict the stated sale purpose and the monitoring predicate did not hit.",
          "2026-10-02",
          "REC-L12",
          "L12-F1;L12-F2;L12-F3",
          "A newly recovered invoice describes consulting services instead of equipment, creating a material purpose contradiction independent of mapping.",
          "PATH_C",
          true,
          "REFERRED_FOR_CASE_REVIEW",
          "SYN-205"
        ]
      ],
      "foreign_keys": [
        {
          "columns": [
            "unit_id"
          ],
          "table": "CanonicalUnits",
          "references": [
            "unit_id"
          ]
        }
      ],
      "grain": "One completed fictional historical-versus-current desk-comparison packet for one canonical unit, identified by comparison_id."
    },
    {
      "name": "DefectChronology",
      "columns": [
        "chronology_id",
        "event_date",
        "source_locator",
        "mapping_version",
        "record_kind",
        "observed_fact",
        "boundary_limit",
        "evidence_ids"
      ],
      "column_contracts": {
        "chronology_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique chronology event ID."
        },
        "event_date": {
          "type": "text",
          "nullable": false,
          "unit": "date",
          "description": "Date of the supplied event or missing historical checkpoint."
        },
        "source_locator": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Exact fictional record locator printed in this table."
        },
        "mapping_version": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Known mapping version or explicit UNKNOWN."
        },
        "record_kind": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Nature of the timing evidence.",
          "enum": [
            "CHANGE_RECORD",
            "RUNTIME_SNAPSHOT",
            "UNAVAILABLE",
            "DEFECT_REPRODUCTION",
            "PROPOSED_CORRECTION"
          ]
        },
        "observed_fact": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Concrete fact supplied by the record."
        },
        "boundary_limit": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "What the record cannot establish about scope or completion."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Chronology source ID."
        }
      },
      "primary_key": [
        "chronology_id"
      ],
      "rows": [
        [
          "DC-01",
          "2025-12-29",
          "CR-MAP-04",
          "MAP-1",
          "CHANGE_RECORD",
          "Deployment plan enables PATH_A and PATH_B identity mapping on January01; PATH_C retains correct source-originator mapping.",
          "Plan is not proof of runtime before January01.",
          "SYN-204"
        ],
        [
          "DC-02",
          "2026-01-01",
          "CFG-JAN-01",
          "MAP-1",
          "RUNTIME_SNAPSHOT",
          "PATH_A and PATH_B use customer_id instead of payment_originator_id in the monitoring originator key; PATH_C uses payment_originator_id.",
          "The established mechanism can collapse distinct originators on affected paths.",
          "SYN-204"
        ],
        [
          "DC-03",
          "2026-03-31",
          "CFG-MAR-31",
          "MAP-1",
          "RUNTIME_SNAPSHOT",
          "The same two affected mappings remain active in the archived configuration.",
          "Supports the initial January\u2013March discovery scope, not a March end to exposure.",
          "SYN-204"
        ],
        [
          "DC-04",
          "2026-06-30",
          "CFG-JUN-30",
          "MAP-1",
          "RUNTIME_SNAPSHOT",
          "The affected PATH_A and PATH_B configuration is still present in the June archive.",
          "Supports analytical extension through June; missing L30 still lacks its own source path.",
          "SYN-204"
        ],
        [
          "DC-05",
          "2026-07-01",
          "CFG-JUL-MISSING",
          "UNKNOWN",
          "UNAVAILABLE",
          "No July runtime configuration or mapping continuity evidence is supplied.",
          "July exposure remains unresolved; received July records alone cannot settle the boundary.",
          "SYN-204"
        ],
        [
          "DC-06",
          "2026-09-28",
          "REPRO-0928",
          "MAP-1",
          "DEFECT_REPRODUCTION",
          "A separate reproduction confirms distinct payment-originator IDs collapse to the customer key on PATH_A and PATH_B.",
          "Discovery date is not the exposure start date.",
          "SYN-204"
        ],
        [
          "DC-07",
          "2026-10-01",
          "SANDBOX-MAP-2",
          "MAP-2",
          "PROPOSED_CORRECTION",
          "Sandbox proposal maps PATH_A and PATH_B to payment_originator_id and preserves PATH_C.",
          "No production deployment or acceptance is evidenced.",
          "SYN-204"
        ]
      ],
      "grain": "One dated mapping-version evidence event or explicitly unavailable historical checkpoint, identified by chronology_id."
    }
  ],
  "findings": [
    {
      "id": "LB-F01",
      "title": "Expected historical unit remains absent from retrieval",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-201",
        "SYN-202"
      ],
      "detail": "The independent manifest names 30 units. Twenty-nine distinct in-scope units are retrieved; L30 is absent. June coverage is 4/5 even though raw intake rows all have classification buckets.",
      "recommendation": "Recover L30 and its source lineage or retain the explicit unreconciled population limitation; do not close the lookback as complete."
    },
    {
      "id": "LB-F02",
      "title": "Most units retain a review or evidence dependency",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-201",
        "SYN-203",
        "SYN-205"
      ],
      "detail": "Only six no-new-information desk reviews have no open unit action. Six referrals, six re-reviews, six pending reviews, five unassessable summaries and one missing unit account for 24 unresolved unit dependencies.",
      "recommendation": "Assign and complete each distinct evidence, retrieval, re-review and referral route; report progress with all 30 expected units as denominator."
    },
    {
      "id": "LB-F03",
      "title": "Three duplicate rows and two July exclusions can distort activity totals",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-202"
      ],
      "detail": "Raw intake has 34 representations:29 canonical, three duplicates of L02 L12 L22, and two July records. Known canonical activity is 449500 USD; duplicate and excluded amounts must not inflate it.",
      "recommendation": "Preserve alias links and excluded rows, verify canonical selection and investigate the July scope boundary separately."
    },
    {
      "id": "LB-F04",
      "title": "Historical desk review does not decide filing or case closure",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-203",
        "SYN-204",
        "SYN-205"
      ],
      "detail": "Six new-information referrals remain unacknowledged in the fictional record. No actual authorized filing, nonfiling, account action or whole-review disposition is supplied.",
      "recommendation": "Carry open handoffs until the responsible human process returns evidence; preserve this lookback as an analytical review with explicit limits."
    }
  ],
  "evidence": [
    {
      "id": "SYN-201",
      "title": "Independent fictional historical control manifest",
      "locator": "10-worked-example.md, thirty-unit manifest and six-period control totals",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-202",
      "title": "Fictional archive retrieval with duplicates exclusions and missing unit",
      "locator": "10-worked-example.md, complete thirty-four-row retrieval ledger",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-203",
      "title": "Fictional comparison outcomes and incomplete review states",
      "locator": "10-worked-example.md, complete unit and review-action registers",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-204",
      "title": "Dated fictional mapping-version chronology and source-path impact register",
      "locator": "10-worked-example.md, DefectChronology and SourcePathInputs",
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
    },
    {
      "id": "SYN-205",
      "title": "Complete fictional historical/current comparison packets and material fact dictionary",
      "locator": "10-worked-example.md, ComparisonPackets and exact historical/current source facts",
      "claim_class": "Observed"
    }
  ],
  "metrics": [
    {
      "label": "Expected historical units",
      "value": 30,
      "method": "Independent six-period manifest with five canonical units per month.",
      "format": "#,##0"
    },
    {
      "label": "Retrieved canonical units",
      "value": 29,
      "method": "34 received rows minus 3 duplicates minus 2 out-of-scope rows.",
      "format": "#,##0"
    },
    {
      "label": "Desk comparisons completed",
      "value": 12,
      "method": "6 no-new-information comparisons plus 6 referrals; referral work remains open.",
      "format": "#,##0"
    },
    {
      "label": "Known canonical activity USD",
      "value": 449500,
      "format": "$#,##0.00",
      "method": "Sum of L01 through L29 once; L30 amount is unknown."
    }
  ],
  "limitations": [
    "Every record is fictional; results test this supplied procedure and do not establish operational effectiveness.",
    "Illustrative cutoffs, partitions, labels, capacities and severity choices are authored examples, not regulatory thresholds.",
    "Human scope approval, deployment authority, case disposition and reporting decisions are not supplied.",
    "Missing, censored and unresolved evidence remains visible; no favorable default is permitted."
  ],
  "conclusion": "The lookback is incomplete. Twenty-nine of 30 expected historical units are retrieved, twelve desk comparisons are complete, and only six units have no open desk-review action. Six referrals and eighteen other evidence or review dependencies remain unresolved; no filing or whole-review approval is implied.",
  "report_narrative": [
    [
      "The lookback is incomplete. Twenty-nine of 30 expected historical units are retrieved, twelve desk comparisons are complete, and only six units have no open desk-review action. Six referrals and eighteen other evidence or review dependencies remain unresolved; no filing or whole-review approval is implied."
    ],
    [
      "The independent manifest defines January through June2026 and five units per month. Dated MAP-1 snapshots on January01, March31 and June30 show PATH_A and PATH_B using customer_id instead of payment_originator_id; PATH_C remains correctly mapped. July configuration evidence is unavailable. Analytical expansion through June follows that chronology; actual institutional scope acceptance is not supplied."
    ],
    [
      "Raw intake reconciles 34 representations to 29 canonical units,3 duplicates and 2 July exclusions. That arithmetic does not cure missing L30. June is 4/5 retrieved. Known canonical activity totals 449500 USD and excludes L30, whose amount is unknown."
    ],
    [
      "CanonicalUnits preserves all 30 expected records, including the missing placeholder. RetrievalLedger preserves every received representation and alias link. Historical statuses remain separate from current review states, so re-review never rewrites the original decision history."
    ],
    [
      "Twelve complete historical/current packets support the desk-comparison count. COMP-L01 through COMP-L06 retain the same material fact sets and identify no newly material information; COMP-L07 through COMP-L12 add concrete identity, scope or purpose facts and require referral. Six other units need re-review, six await review, five lack essential support and one is not retrieved. All six referrals have completed comparison packets but no actual receiving disposition."
    ],
    [
      "ComparisonPackets prints original facts, rationale, cutoff, recovered evidence, material fact sets and expected routes. DefectChronology supplies dated version evidence and the unresolved July boundary. SourcePathInputs identifies each retrieved unit\u2019s feed path; L30 remains unknown. These sources support the fictional analytical result but not an actual institutional decision."
    ],
    [
      "Proposed work is to recover L30, obtain support for L25 through L29, finish L13 through L24 reviews, and obtain responsible case-review responses for L07 through L12. Filing, account action and whole-review acceptance remain separate human decisions."
    ],
    [
      "Do not report a 100% completion rate from received-row classification or twelve completed desk comparisons. Reperform the thirty-unit state reconciliation, amount conservation, duplicate links and completion gates. The fictional checks establish evidence accounting only, not a completed operational remediation."
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
      "id": "LO-A01",
      "finding_id": "LB-F01",
      "proposal": "Recover L30 and its source lineage or retain the explicit unreconciled population limitation; do not close the lookback as complete.",
      "owner": "Proposed accountable role; assignment not recorded",
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "LO-A02",
      "finding_id": "LB-F02",
      "proposal": "Assign and complete each distinct evidence, retrieval, re-review and referral route; report progress with all 30 expected units as denominator.",
      "owner": "Proposed accountable role; assignment not recorded",
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "LO-A03",
      "finding_id": "LB-F03",
      "proposal": "Preserve alias links and excluded rows, verify canonical selection and investigate the July scope boundary separately.",
      "owner": "Proposed accountable role; assignment not recorded",
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "LO-A04",
      "finding_id": "LB-F04",
      "proposal": "Carry open handoffs until the responsible human process returns evidence; preserve this lookback as an analytical review with explicit limits.",
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
  "suite_id": "lookback-review",
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
