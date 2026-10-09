# Investigation Case Review — complete dashboard template

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
<title>Investigation Case Review</title>
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
  "slug": "investigations",
  "title": "Investigation Case Review",
  "summary": "Reconstruct a full case chronology, reconcile account and entity flows, test competing claims, preserve contradictions and produce a bounded human decision package.",
  "audience": "Investigators, case reviewers and quality-assurance analysts",
  "decision": "Which propositions survive a complete chronology, reconciliation and contrary-evidence review, and what evidence or human decision is still required?",
  "palette": "indigo",
  "as_of": "2026-09-30T17:00:00-04:00",
  "scope": "Fictional Entity-J, accounts A/B, Sep 01\u201330, 2026; 30 received raw representations, 27 posted account entries and 24 canonical transfers, all USD. Sources are printed in file 10.",
  "report_sections": [
    "Decision questions and current assessment",
    "Scope, chronology method, and coverage",
    "Findings and contradictions",
    "Chronology and funds movement",
    "Competing hypothesis tests and decision gates",
    "Evidence inventory and provenance",
    "Proposed investigative actions",
    "Limitations, quality checks, and reviewer decision"
  ],
  "domain_tables": [
    {
      "name": "CaseTimeline",
      "columns": [
        "event_id",
        "event_time",
        "from_node",
        "to_node",
        "amount_usd",
        "currency",
        "linked_return_of",
        "account_a_balance_usd",
        "evidence_ids",
        "claim_class",
        "detail"
      ],
      "column_contracts": {
        "event_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique canonical economic transfer identifier, not source-row number."
        },
        "event_time": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact posted timestamp in ISO-8601 with offset; human narrative uses ET."
        },
        "from_node": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Recorded immediate sender node; ultimate ownership not inferred."
        },
        "to_node": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Recorded immediate receiver node; purpose not inferred."
        },
        "amount_usd": {
          "type": "number",
          "nullable": false,
          "unit": "USD",
          "description": "Positive booked USD amount of one canonical transfer."
        },
        "currency": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Native currency of every monetary record.",
          "enum": [
            "USD"
          ]
        },
        "linked_return_of": {
          "type": "text",
          "nullable": true,
          "unit": "identifier",
          "description": "Parent debit event for explicitly linked return; null otherwise."
        },
        "account_a_balance_usd": {
          "type": "number",
          "nullable": false,
          "unit": "USD",
          "description": "Account A running balance after this event, opening USD5000."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "evidence identifiers",
          "description": "Semicolon-delimited exact identifiers in the common Evidence register; each must resolve."
        },
        "claim_class": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Class of the proposition visible in this event row.",
          "enum": [
            "Observed"
          ]
        },
        "detail": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Bounded event description including unresolved purpose where relevant."
        }
      },
      "rows": [
        [
          "T01",
          "2026-09-02T10:00:00-04:00",
          "P",
          "A",
          12000,
          "USD",
          null,
          17000,
          "S01",
          "Observed",
          "Receipt described by customer as equipment sale"
        ],
        [
          "T02",
          "2026-09-02T11:00:00-04:00",
          "A",
          "Q",
          11000,
          "USD",
          null,
          6000,
          "S01",
          "Observed",
          "Equipment-purpose explanation; invoice names R"
        ],
        [
          "T03",
          "2026-09-04T09:00:00-04:00",
          "Q",
          "A",
          2000,
          "USD",
          "T02",
          8000,
          "S01;S08",
          "Observed",
          "Explicit partial return of T02"
        ],
        [
          "T04",
          "2026-09-05T09:00:00-04:00",
          "P2",
          "A",
          8000,
          "USD",
          null,
          16000,
          "S01",
          "Observed",
          "Second customer receipt"
        ],
        [
          "T05",
          "2026-09-05T12:00:00-04:00",
          "A",
          "R",
          7500,
          "USD",
          null,
          8500,
          "S01",
          "Observed",
          "Invoice INV-B and delivery receipt support purpose"
        ],
        [
          "T06",
          "2026-09-06T09:00:00-04:00",
          "A",
          "B",
          500,
          "USD",
          null,
          8000,
          "S01;S09",
          "Observed",
          "Same-entity account transfer; both books supplied"
        ],
        [
          "T07",
          "2026-09-08T09:00:00-04:00",
          "P3",
          "A",
          6000,
          "USD",
          null,
          14000,
          "S01",
          "Observed",
          "Customer receipt; remitter identity supported"
        ],
        [
          "T08",
          "2026-09-08T09:20:00-04:00",
          "A",
          "U",
          6000,
          "USD",
          null,
          8000,
          "S01",
          "Observed",
          "Purpose explanation absent"
        ],
        [
          "T09",
          "2026-09-10T10:00:00-04:00",
          "P",
          "A",
          3000,
          "USD",
          null,
          11000,
          "S01",
          "Observed",
          "Additional customer receipt"
        ],
        [
          "T10",
          "2026-09-10T14:00:00-04:00",
          "A",
          "Q",
          2500,
          "USD",
          null,
          8500,
          "S01",
          "Observed",
          "Customer says invoice INV-C settlement"
        ],
        [
          "T11",
          "2026-09-10T16:00:00-04:00",
          "A",
          "BANK",
          100,
          "USD",
          null,
          8400,
          "S01",
          "Observed",
          "Posted service fee"
        ],
        [
          "T12",
          "2026-09-12T09:00:00-04:00",
          "P4",
          "A",
          7000,
          "USD",
          null,
          15400,
          "S01",
          "Observed",
          "Customer receipt"
        ],
        [
          "T13",
          "2026-09-12T10:00:00-04:00",
          "A",
          "R",
          6800,
          "USD",
          null,
          8600,
          "S01",
          "Observed",
          "Invoice INV-D full amount supported"
        ],
        [
          "T14",
          "2026-09-13T10:00:00-04:00",
          "R",
          "A",
          400,
          "USD",
          "T13",
          9000,
          "S01;S08",
          "Observed",
          "Explicit partial return of T13"
        ],
        [
          "T15",
          "2026-09-14T09:00:00-04:00",
          "A",
          "B",
          1000,
          "USD",
          null,
          8000,
          "S01;S09",
          "Observed",
          "Same-entity transfer; both books supplied"
        ],
        [
          "T16",
          "2026-09-15T09:00:00-04:00",
          "B",
          "A",
          1000,
          "USD",
          null,
          9000,
          "S01;S09",
          "Observed",
          "Same-entity return transfer; not a supplier refund"
        ],
        [
          "T17",
          "2026-09-17T09:00:00-04:00",
          "P5",
          "A",
          5000,
          "USD",
          null,
          14000,
          "S01",
          "Observed",
          "Customer receipt"
        ],
        [
          "T18",
          "2026-09-17T11:00:00-04:00",
          "A",
          "V",
          4000,
          "USD",
          null,
          10000,
          "S01",
          "Observed",
          "Invoice INV-E and delivery support purpose"
        ],
        [
          "T19",
          "2026-09-18T10:00:00-04:00",
          "A",
          "CASH",
          1000,
          "USD",
          null,
          9000,
          "S01",
          "Observed",
          "Cash withdrawal; ultimate use uncorroborated"
        ],
        [
          "T20",
          "2026-09-21T09:00:00-04:00",
          "P5",
          "A",
          1500,
          "USD",
          null,
          10500,
          "S01",
          "Observed",
          "Customer receipt"
        ],
        [
          "T21",
          "2026-09-21T12:00:00-04:00",
          "A",
          "V",
          1500,
          "USD",
          null,
          9000,
          "S01",
          "Observed",
          "Invoice INV-F and delivery support purpose"
        ],
        [
          "T22",
          "2026-09-23T10:00:00-04:00",
          "U",
          "A",
          1000,
          "USD",
          "T08",
          10000,
          "S01;S08",
          "Observed",
          "Explicit partial return of T08"
        ],
        [
          "T23",
          "2026-09-24T09:00:00-04:00",
          "A",
          "Q",
          700,
          "USD",
          null,
          9300,
          "S01",
          "Observed",
          "Adjustment description; supporting memo absent"
        ],
        [
          "T24",
          "2026-09-25T16:00:00-04:00",
          "A",
          "BANK",
          300,
          "USD",
          null,
          9000,
          "S01",
          "Observed",
          "Posted service fee"
        ]
      ],
      "primary_key": [
        "event_id"
      ],
      "grain": "One canonical transfer touching A; same-entity mirror legs are represented once.",
      "report_section": 4,
      "formats": {
        "amount_usd": "$#,##0.00",
        "account_a_balance_usd": "$#,##0.00"
      }
    },
    {
      "name": "AccountBalances",
      "columns": [
        "account_id",
        "opening_usd",
        "credits_usd",
        "debits_usd",
        "calculated_close_usd",
        "supplied_close_usd",
        "difference_usd",
        "evidence_ids"
      ],
      "column_contracts": {
        "account_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Account identifier in the supplied two-account perimeter."
        },
        "opening_usd": {
          "type": "number",
          "nullable": false,
          "unit": "USD",
          "description": "Supplied opening balance, not inferred from first transaction."
        },
        "credits_usd": {
          "type": "number",
          "nullable": false,
          "unit": "USD",
          "description": "Sum of positive postings to this account, including own-account mirrors."
        },
        "debits_usd": {
          "type": "number",
          "nullable": false,
          "unit": "USD",
          "description": "Sum of outgoing postings from this account, including own-account mirrors."
        },
        "calculated_close_usd": {
          "type": "number",
          "nullable": false,
          "unit": "USD",
          "description": "Opening plus credits minus debits."
        },
        "supplied_close_usd": {
          "type": "number",
          "nullable": false,
          "unit": "USD",
          "description": "Independent supplied close from S03."
        },
        "difference_usd": {
          "type": "number",
          "nullable": false,
          "unit": "USD",
          "description": "Calculated close minus supplied close."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "evidence identifiers",
          "description": "Semicolon-delimited exact identifiers in the common Evidence register; each must resolve."
        }
      },
      "rows": [
        [
          "A",
          5000,
          46900,
          42900,
          9000,
          9000,
          0,
          "S01;S03"
        ],
        [
          "B",
          1000,
          1500,
          1000,
          1500,
          1500,
          0,
          "S02;S03"
        ]
      ],
      "primary_key": [
        "account_id"
      ],
      "grain": "One account-period balance equation.",
      "report_section": 4,
      "formats": {
        "opening_usd": "$#,##0.00",
        "credits_usd": "$#,##0.00",
        "debits_usd": "$#,##0.00",
        "calculated_close_usd": "$#,##0.00",
        "supplied_close_usd": "$#,##0.00",
        "difference_usd": "$#,##0.00"
      }
    },
    {
      "name": "ClaimTests",
      "columns": [
        "claim_id",
        "proposition",
        "supporting_ids",
        "conflicting_ids",
        "assessment",
        "confidence",
        "discriminator",
        "evidence_ids"
      ],
      "column_contracts": {
        "claim_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable falsifiable claim identifier."
        },
        "proposition": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Bounded question that can be supported, contradicted or unresolved."
        },
        "supporting_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon references or explicit NONE_LOCATED; narrative explains meaning."
        },
        "conflicting_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon references or explicit NONE_LOCATED."
        },
        "assessment": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Outcome under the printed evidence.",
          "enum": [
            "SUPPORTED",
            "CONTRADICTED",
            "UNRESOLVED",
            "PATTERN_SUPPORTED"
          ]
        },
        "confidence": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Confidence in this bounded proposition.",
          "enum": [
            "HIGH",
            "MODERATE",
            "LOW",
            "NOT ASSESSABLE"
          ]
        },
        "discriminator": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Evidence capable of changing the assessment."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "evidence identifiers",
          "description": "Semicolon-delimited exact identifiers in the common Evidence register; each must resolve."
        }
      },
      "rows": [
        [
          "CL01",
          "T02 is fully reconciled equipment settlement",
          "S04;S05",
          "S01;S05",
          "UNRESOLVED",
          "LOW",
          "Beneficiary bridge plus USD1000 difference and delivery evidence",
          "S01;S04;S05"
        ],
        [
          "CL02",
          "T03 fully reversed T02",
          "S08",
          "S01;S08",
          "CONTRADICTED",
          "HIGH",
          "No additional source needed for the supplied-period arithmetic",
          "S01;S08"
        ],
        [
          "CL03",
          "Every supplier payment is unexplained",
          "S01",
          "S06",
          "CONTRADICTED",
          "HIGH",
          "Matched B/D/E/F records are material counterevidence",
          "S01;S06"
        ],
        [
          "CL04",
          "T08 purpose is substantiated",
          "NONE_LOCATED",
          "S01",
          "UNRESOLVED",
          "LOW",
          "Contract, invoice and beneficiary-purpose evidence",
          "S01;S10"
        ],
        [
          "CL05",
          "Own-account transfers create external turnover",
          "S01",
          "S02;S09",
          "CONTRADICTED",
          "HIGH",
          "Entity aggregation removes three own transfers",
          "S01;S02;S09"
        ],
        [
          "CL06",
          "Rapid onward timing pattern exists for T01/T02",
          "S01",
          "NONE_LOCATED",
          "PATTERN_SUPPORTED",
          "HIGH",
          "Timing established; source allocation and purpose remain separate",
          "S01;S04;S05"
        ]
      ],
      "primary_key": [
        "claim_id"
      ],
      "grain": "One proposition, including favorable and contrary alternatives.",
      "report_section": 5,
      "formats": {}
    },
    {
      "name": "Contradictions",
      "columns": [
        "contradiction_id",
        "claim_id",
        "left_account",
        "right_account",
        "effect",
        "state",
        "evidence_ids"
      ],
      "column_contracts": {
        "contradiction_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable difference identifier."
        },
        "claim_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Claim being challenged or qualified."
        },
        "left_account": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "One source-supported representation."
        },
        "right_account": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Conflicting or qualifying representation."
        },
        "effect": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact consequence for a live decision."
        },
        "state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Resolution state.",
          "enum": [
            "OPEN",
            "RESOLVED_ARITHMETIC",
            "RESOLVED_SCOPE"
          ]
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "evidence identifiers",
          "description": "Semicolon-delimited exact identifiers in the common Evidence register; each must resolve."
        }
      },
      "rows": [
        [
          "CT01",
          "CL01",
          "T02 paid Q USD11000",
          "INV-A names R USD10000",
          "Amount gap USD1000 and identity bridge remain separate",
          "OPEN",
          "S01;S05"
        ],
        [
          "CT02",
          "CL02",
          "Return described as full reversal",
          "Linked posted return USD2000 against USD11000",
          "Net unreversed T02 is USD9000",
          "RESOLVED_ARITHMETIC",
          "S01;S08"
        ],
        [
          "CT03",
          "CL03",
          "All supplier activity described as unsupported",
          "INV-B/D/E/F support USD19800 gross supplier payments",
          "Do not generalize unresolved subset to all USD40000 gross supplier debits",
          "RESOLVED_SCOPE",
          "S01;S06"
        ],
        [
          "CT04",
          "CL05",
          "Account credits summed as new external funds",
          "A/B internal mirrors total USD2500 canonical own transfer value",
          "Entity external inflow excludes both directions of own transfers",
          "RESOLVED_SCOPE",
          "S01;S02;S09"
        ]
      ],
      "primary_key": [
        "contradiction_id"
      ],
      "grain": "One material contradiction or qualification and its exact decision effect.",
      "report_section": 5,
      "formats": {},
      "foreign_keys": [
        {
          "columns": [
            "claim_id"
          ],
          "table": "ClaimTests",
          "references": [
            "claim_id"
          ]
        }
      ]
    },
    {
      "name": "EvidenceRequests",
      "columns": [
        "request_id",
        "claim_id",
        "request_text",
        "state",
        "decision_effect",
        "evidence_ids"
      ],
      "column_contracts": {
        "request_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable proposed request identifier."
        },
        "claim_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Decision-sensitive claim this request serves."
        },
        "request_text": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Narrow question, records and period; no accusation."
        },
        "state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Fixture request status.",
          "enum": [
            "PROPOSED",
            "INACCESSIBLE",
            "SATISFIED_FOR_SCOPE"
          ]
        },
        "decision_effect": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "What changes if evidence supports or contradicts the claim."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "evidence identifiers",
          "description": "Semicolon-delimited exact identifiers in the common Evidence register; each must resolve."
        }
      },
      "rows": [
        [
          "RQ01",
          "CL01",
          "Provide beneficiary bridge Q/R, explanation of USD1000 difference and delivery evidence for T02.",
          "PROPOSED",
          "Can resolve purpose/amount/beneficiary separately; cannot retroactively invent receipt",
          "S01;S04;S05"
        ],
        [
          "RQ02",
          "CL04",
          "Provide readable Contract-C and supporting T08 purpose documents.",
          "INACCESSIBLE",
          "Readable contract may support represented terms; payment purpose still needs linkage",
          "S01;S10"
        ],
        [
          "RQ03",
          "CL03",
          "Retain INV-B/D/E/F and delivery matches in favorable evidence set.",
          "SATISFIED_FOR_SCOPE",
          "Prevents claim that every supplier payment lacks support",
          "S06"
        ],
        [
          "RQ04",
          "CL05",
          "Retain supplied A/B ownership extract and mirrored postings.",
          "SATISFIED_FOR_SCOPE",
          "Supports perimeter netting only for A/B",
          "S02;S09"
        ],
        [
          "RQ05",
          "CL06",
          "Obtain allocation evidence only if attribution of T01 funds to T02 is decision-material.",
          "PROPOSED",
          "Could narrow source attribution; chronological proximity alone cannot do so",
          "S01"
        ]
      ],
      "primary_key": [
        "request_id"
      ],
      "grain": "One decision-sensitive request or satisfied request outcome.",
      "report_section": 5,
      "formats": {},
      "foreign_keys": [
        {
          "columns": [
            "claim_id"
          ],
          "table": "ClaimTests",
          "references": [
            "claim_id"
          ]
        }
      ]
    },
    {
      "name": "EvidenceProvenance",
      "columns": [
        "source_id",
        "source_title",
        "locator",
        "availability",
        "origin_type",
        "claim_class",
        "limitation"
      ],
      "column_contracts": {
        "source_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Exact identifier in common Evidence register."
        },
        "source_title": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Fictional source name."
        },
        "locator": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact raw-data locator in file 10."
        },
        "availability": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Availability distinct from reliability.",
          "enum": [
            "AVAILABLE",
            "INACCESSIBLE"
          ]
        },
        "origin_type": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Origin family relevant to independence."
        },
        "claim_class": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Class applicable to source description.",
          "enum": [
            "Observed",
            "Reported"
          ]
        },
        "limitation": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Specific proposition this source cannot establish."
        }
      },
      "rows": [
        [
          "S01",
          "Account A posted ledger",
          "Raw postings T01\u2013T24",
          "AVAILABLE",
          "SYSTEM_EXPORT",
          "Observed",
          "Complete stated account-period posting set; does not establish purpose"
        ],
        [
          "S02",
          "Account B posted ledger",
          "Mirror legs T06, T15, T16",
          "AVAILABLE",
          "SYSTEM_EXPORT",
          "Observed",
          "Ownership extract identifies A and B as same entity; mirror legs do not create new economic transfers"
        ],
        [
          "S03",
          "Opening and closing balances",
          "A 5000\u21929000; B 1000\u21921500",
          "AVAILABLE",
          "BALANCE_RECORD",
          "Observed",
          "Balances cover stated September perimeter only"
        ],
        [
          "S04",
          "Customer explanation",
          "Statement X01",
          "AVAILABLE",
          "CUSTOMER_STATEMENT",
          "Reported",
          "T02 said to pay equipment supplier Q; T10 said to settle INV-C; T19 said to cover expenses"
        ],
        [
          "S05",
          "Invoice INV-A",
          "Face 10000 USD; supplier R",
          "AVAILABLE",
          "CUSTOMER_DOCUMENT",
          "Observed",
          "Document text observed; actual delivery and beneficiary bridge absent"
        ],
        [
          "S06",
          "Supported invoices and receipts",
          "INV-B 7500; INV-D 6800; INV-E 4000; INV-F 1500",
          "AVAILABLE",
          "CUSTOMER_DOCUMENT",
          "Observed",
          "Matched amounts and counterparties; supplied delivery records corroborate within fixture"
        ],
        [
          "S07",
          "Invoice INV-C",
          "Face 2500 USD; supplier Q",
          "AVAILABLE",
          "CUSTOMER_DOCUMENT",
          "Observed",
          "Amount and name match T10; no delivery record supplied"
        ],
        [
          "S08",
          "Return references",
          "T03\u2192T02; T14\u2192T13; T22\u2192T08",
          "AVAILABLE",
          "SYSTEM_EXPORT",
          "Observed",
          "Explicit linkage; amounts are partial, not full reversals"
        ],
        [
          "S09",
          "Account ownership extract",
          "A and B belong to fictional Entity-J",
          "AVAILABLE",
          "ACCOUNT_RECORD",
          "Observed",
          "No ownership linkage supplied for Q, R, U or V"
        ],
        [
          "S10",
          "Contract file",
          "Contract-C encrypted attachment",
          "INACCESSIBLE",
          "CUSTOMER_DOCUMENT",
          "Reported",
          "Filename supplied; text not accessible and cannot corroborate terms"
        ],
        [
          "S11",
          "Receipt manifest",
          "30 raw rows: 27 posted representations; 1 duplicate; 1 instruction; 1 pending",
          "AVAILABLE",
          "INTAKE_MANIFEST",
          "Observed",
          "Includes one T01 duplicate, unexecuted T02 instruction and pending USD2000 debit; exact exclusions in file 10"
        ],
        [
          "S12",
          "Illustrative review charter",
          "Fixture policy CP-INV-1",
          "AVAILABLE",
          "ILLUSTRATIVE_POLICY",
          "Observed",
          "Requires amount/beneficiary/purpose checks for this exercise; no legal filing conclusion authorized"
        ]
      ],
      "primary_key": [
        "source_id"
      ],
      "grain": "One source origin or explicitly unavailable supplied item.",
      "report_section": 5,
      "formats": {}
    },
    {
      "name": "DecisionRecord",
      "columns": [
        "decision_id",
        "gate",
        "status",
        "basis",
        "evidence_ids"
      ],
      "column_contracts": {
        "decision_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable analytical gate identifier."
        },
        "gate": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Decision being recorded."
        },
        "status": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Analytical state distinct from human disposition.",
          "enum": [
            "COMPLETE",
            "HOLD_EVIDENCE",
            "NOT_RECORDED"
          ]
        },
        "basis": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Case-specific reason."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "evidence identifiers",
          "description": "Semicolon-delimited exact identifiers in the common Evidence register; each must resolve."
        }
      },
      "rows": [
        [
          "D01",
          "Population and balance gate",
          "COMPLETE",
          "30 received rows reduce to 24 canonical transfers and 27 posted account representations; both balances tie.",
          "S01;S02;S03;S11"
        ],
        [
          "D02",
          "T02 purpose and beneficiary gate",
          "HOLD_EVIDENCE",
          "USD1000 invoice difference and Q/R bridge remain unresolved.",
          "S01;S04;S05"
        ],
        [
          "D03",
          "T08 purpose gate",
          "HOLD_EVIDENCE",
          "Readable contract and purpose corroboration absent; partial return does not resolve purpose.",
          "S01;S08;S10"
        ],
        [
          "D04",
          "Human case disposition",
          "NOT_RECORDED",
          "No actual authorized reviewer decision supplied.",
          "S12"
        ]
      ],
      "primary_key": [
        "decision_id"
      ],
      "grain": "One distinct gate; completion is not equivalent to case closure.",
      "report_section": 5,
      "formats": {}
    },
    {
      "name": "ProcessQA",
      "columns": [
        "check_id",
        "check",
        "expected",
        "actual",
        "result",
        "evidence_ids"
      ],
      "column_contracts": {
        "check_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable reperformable check."
        },
        "check": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Specific invariant or calculation."
        },
        "expected": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Independent expected outcome."
        },
        "actual": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Fixture outcome; must be recomputed when adapted."
        },
        "result": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Fixture analytical result.",
          "enum": [
            "PASS",
            "REVIEW REQUIRED",
            "NOT RECORDED"
          ]
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "evidence identifiers",
          "description": "Semicolon-delimited exact identifiers in the common Evidence register; each must resolve."
        }
      },
      "rows": [
        [
          "Q01",
          "Raw-to-canonical count",
          "30 raw; 27 posted representations; 24 transfers",
          "30 / 27 / 24",
          "PASS",
          "S01;S02;S11"
        ],
        [
          "Q02",
          "Account A close",
          "USD9000",
          "USD9000",
          "PASS",
          "S01;S03"
        ],
        [
          "Q03",
          "Account B close",
          "USD1500",
          "USD1500",
          "PASS",
          "S02;S03"
        ],
        [
          "Q04",
          "Entity close",
          "USD10500",
          "USD10500",
          "PASS",
          "S01;S02;S03"
        ],
        [
          "Q05",
          "External receipts excluding returns",
          "USD42500",
          "USD42500",
          "PASS",
          "S01;S08;S09"
        ],
        [
          "Q06",
          "Supplier gross and linked net",
          "USD40000 gross; USD36600 net",
          "USD40000 / USD36600",
          "PASS",
          "S01;S08"
        ],
        [
          "Q07",
          "T02 invoice difference",
          "USD1000",
          "USD1000",
          "PASS",
          "S01;S05"
        ],
        [
          "Q08",
          "T02 unreversed",
          "USD9000",
          "USD9000",
          "PASS",
          "S01;S08"
        ],
        [
          "Q09",
          "Supported supplier gross",
          "USD19800 of USD40000; 49.5%",
          "USD19800 / USD40000 = 49.5%",
          "PASS",
          "S01;S06"
        ],
        [
          "Q10",
          "Unsupported conclusion gate",
          "No universal explanation or illicit-purpose assertion",
          "Bounded unresolved subset retained",
          "PASS",
          "S01;S04;S06;S10"
        ],
        [
          "Q11",
          "Purpose gates",
          "T02 and T08 remain unresolved",
          "HOLD_EVIDENCE",
          "REVIEW REQUIRED",
          "S01;S05;S10"
        ],
        [
          "Q12",
          "Human disposition",
          "No invented approval",
          "NOT_RECORDED",
          "NOT RECORDED",
          "S12"
        ]
      ],
      "primary_key": [
        "check_id"
      ],
      "grain": "One performed fixture check or explicit unrecorded approval gate.",
      "report_section": 5,
      "formats": {}
    }
  ],
  "findings": [
    {
      "id": "INV-F01",
      "title": "T02 invoice fails amount and beneficiary reconciliation",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "S01",
        "S04",
        "S05"
      ],
      "detail": "T02 is USD11000 to Q while INV-A is USD10000 naming R. The USD1000 difference and beneficiary bridge are separate unresolved questions.",
      "recommendation": "Obtain targeted amount, beneficiary and delivery support; retain the customer explanation as Reported."
    },
    {
      "id": "INV-F02",
      "title": "T08 purpose remains unsupported within the supplied evidence",
      "severity": "MEDIUM",
      "confidence": "MODERATE",
      "claim_class": "Inferred",
      "evidence_ids": [
        "S01",
        "S08",
        "S10"
      ],
      "detail": "T08 paid U USD6000; a linked USD1000 return leaves USD5000 unreversed. Contract-C is inaccessible. This does not establish illicit purpose or confirmed loss.",
      "recommendation": "Request a readable contract and transaction-specific purpose evidence; preserve the return as counterevidence."
    },
    {
      "id": "INV-F03",
      "title": "Rapid onward movement is observable but source attribution is unproven",
      "severity": "LOW",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "S01",
        "S04",
        "S05"
      ],
      "detail": "T02 followed T01 by one hour. Pre-existing USD5000 means temporal order does not prove that the entire debit came from T01.",
      "recommendation": "Record timing separately from source attribution and economic explanation."
    },
    {
      "id": "INV-F04",
      "title": "The unresolved subset must not erase supported supplier activity",
      "severity": "LOW",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "S01",
        "S06"
      ],
      "detail": "Four matched invoice and delivery sets support USD19800 of USD40000 gross supplier debits, or 49.5%. Unreconciled value is not automatically suspicious value.",
      "recommendation": "Keep favorable evidence and denominator definitions in every output."
    }
  ],
  "evidence": [
    {
      "id": "S01",
      "title": "Account A posted ledger",
      "locator": "10-worked-example.md, Raw postings T01\u2013T24",
      "claim_class": "Observed"
    },
    {
      "id": "S02",
      "title": "Account B posted ledger",
      "locator": "10-worked-example.md, Mirror legs T06, T15, T16",
      "claim_class": "Observed"
    },
    {
      "id": "S03",
      "title": "Opening and closing balances",
      "locator": "10-worked-example.md, A 5000\u21929000; B 1000\u21921500",
      "claim_class": "Observed"
    },
    {
      "id": "S04",
      "title": "Customer explanation",
      "locator": "10-worked-example.md, Statement X01",
      "claim_class": "Reported"
    },
    {
      "id": "S05",
      "title": "Invoice INV-A",
      "locator": "10-worked-example.md, Face 10000 USD; supplier R",
      "claim_class": "Observed"
    },
    {
      "id": "S06",
      "title": "Supported invoices and receipts",
      "locator": "10-worked-example.md, INV-B 7500; INV-D 6800; INV-E 4000; INV-F 1500",
      "claim_class": "Observed"
    },
    {
      "id": "S07",
      "title": "Invoice INV-C",
      "locator": "10-worked-example.md, Face 2500 USD; supplier Q",
      "claim_class": "Observed"
    },
    {
      "id": "S08",
      "title": "Return references",
      "locator": "10-worked-example.md, T03\u2192T02; T14\u2192T13; T22\u2192T08",
      "claim_class": "Observed"
    },
    {
      "id": "S09",
      "title": "Account ownership extract",
      "locator": "10-worked-example.md, A and B belong to fictional Entity-J",
      "claim_class": "Observed"
    },
    {
      "id": "S10",
      "title": "Contract file",
      "locator": "10-worked-example.md, Contract-C encrypted attachment",
      "claim_class": "Reported"
    },
    {
      "id": "S11",
      "title": "Receipt manifest",
      "locator": "10-worked-example.md, 30 raw rows: 27 posted representations; 1 duplicate; 1 instruction; 1 pending",
      "claim_class": "Observed"
    },
    {
      "id": "S12",
      "title": "Illustrative review charter",
      "locator": "10-worked-example.md, Fixture policy CP-INV-1",
      "claim_class": "Observed"
    }
  ],
  "metrics": [
    {
      "label": "Canonical transfers",
      "value": 24,
      "method": "30 raw representations minus 1 duplicate, 1 instruction, 1 pending item and 3 own-account mirror representations",
      "format": "#,##0"
    },
    {
      "label": "Entity closing balance USD",
      "value": 10500,
      "method": "Opening6000 + customer receipts42500 + linked returns3400 - supplier debits40000 - cash1000 - fees400; own transfers cancel",
      "format": "$#,##0.00"
    },
    {
      "label": "Supplier gross debit USD",
      "value": 40000,
      "method": "T02+T05+T08+T10+T13+T18+T21+T23",
      "format": "$#,##0.00"
    },
    {
      "label": "Net supplier debit USD",
      "value": 36600,
      "method": "40000 minus linked returns T03/T14/T22 totaling3400",
      "format": "$#,##0.00"
    },
    {
      "label": "Supported supplier gross ratio",
      "value": 0.495,
      "format": "0.0%",
      "method": "Matched invoice and delivery T05/T13/T18/T21 amount19800 divided by gross supplier debit40000; not a suspicious-value rate"
    }
  ],
  "limitations": [
    "All subjects, records and criteria are fictional; no legal or filing determination is made.",
    "Contract-C is inaccessible; beneficiary Q/R linkage and T02 amount difference remain unresolved.",
    "Book reconciliation does not establish source attribution, economic purpose, loss or misconduct.",
    "No actual human decision, external request or approval is recorded."
  ],
  "conclusion": "The two-account ledger reconciles to USD10500, but T02 amount/beneficiary support and T08 purpose remain unresolved. Supported supplier activity totals USD19800 of USD40000 gross; uncertainty must remain bounded to the relevant subset.",
  "report_narrative": [
    [
      "The two-account ledger reconciles to USD10500, but T02 amount/beneficiary support and T08 purpose remain unresolved. Supported supplier activity totals USD19800 of USD40000 gross; uncertainty must remain bounded to the relevant subset.",
      "The package recommends targeted evidence review. It does not conclude that funds were illicit, that an account should close or that a SAR must be filed."
    ],
    [
      "Thirty raw representations include twenty-seven posted account entries, one exact duplicate, one unexecuted instruction and one pending item. Three posted entries are mirror legs of own-account transfers, leaving twenty-four canonical transfers. Event timestamps describe posting; source availability and customer explanations remain separate chronology layers."
    ],
    [
      "INV-F01: T02 is USD11000 to Q while INV-A is USD10000 naming R. The USD1000 difference and beneficiary bridge are separate unresolved questions.",
      "INV-F02: T08 paid U USD6000; a linked USD1000 return leaves USD5000 unreversed. Contract-C is inaccessible. This does not establish illicit purpose or confirmed loss.",
      "INV-F03: T02 followed T01 by one hour. Pre-existing USD5000 means temporal order does not prove that the entire debit came from T01.",
      "INV-F04: Four matched invoice and delivery sets support USD19800 of USD40000 gross supplier debits, or 49.5%. Unreconciled value is not automatically suspicious value."
    ],
    [
      "Account A: USD5000 + USD46900 credits - USD42900 debits = USD9000. Account B: USD1000 + USD1500 credits - USD1000 debits = USD1500. Entity close is USD10500 with zero balance difference.",
      "External customer receipts are USD42500; supplier debits are USD40000 gross and USD36600 after USD3400 of explicitly linked returns. Cash USD1000 and fees USD400 remain separate. Own-account transfers of USD2500 canonical value cancel at entity level."
    ],
    [
      "CL01 remains unresolved because INV-A differs by USD1000 and names R rather than Q. CL02 is contradicted: T03 returns only USD2000 of T02 USD11000. CL03 is contradicted by matched B/D/E/F records totaling USD19800. CL04 remains unresolved while Contract-C is inaccessible. CL05 is contradicted by the A/B ownership and mirror records. CL06 supports timing only.",
      "RQ01/RQ02/RQ05 remain proposed or inaccessible; RQ03/RQ04 are satisfied only for their bounded scope. D02/D03 hold purpose decisions and D04 records no actual human disposition."
    ],
    [
      "S01\u2013S12 preserve source origin, availability and limits. The encrypted contract is not treated as reviewed evidence. Customer explanation remains Reported; the invoice face text is Observed without implying actual performance. Duplicate ledger representations are not independent corroboration."
    ],
    [
      "Obtain the Q/R beneficiary bridge, USD1000 difference explanation and delivery support for T02. Obtain readable Contract-C and transaction-specific support for T08. Preserve matched invoice/delivery evidence and the partial returns. No request has been sent by this fixture."
    ],
    [
      "All subjects, records and criteria are fictional; no legal or filing determination is made.",
      "Contract-C is inaccessible; beneficiary Q/R linkage and T02 amount difference remain unresolved.",
      "Book reconciliation does not establish source attribution, economic purpose, loss or misconduct.",
      "No actual human decision, external request or approval is recorded.",
      "Fixture arithmetic checks pass; material purpose gates remain REVIEW REQUIRED and human disposition NOT RECORDED."
    ]
  ],
  "suite_id": "investigations",
  "version": "1.2.0",
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
      "finding_id": "INV-F01",
      "proposal": "Obtain targeted amount, beneficiary and delivery support; retain the customer explanation as Reported.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-002",
      "finding_id": "INV-F02",
      "proposal": "Request a readable contract and transaction-specific purpose evidence; preserve the return as counterevidence.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-003",
      "finding_id": "INV-F03",
      "proposal": "Record timing separately from source attribution and economic explanation.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-004",
      "finding_id": "INV-F04",
      "proposal": "Keep favorable evidence and denominator definitions in every output.",
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
