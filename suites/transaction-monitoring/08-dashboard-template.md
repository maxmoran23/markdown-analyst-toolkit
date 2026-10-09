# Transaction Monitoring Review — complete dashboard template

Version 1.2.0. Use the complete HTML below to create a single downloadable `.html` file in the current session. It includes all style and interaction code. No hosted assets, fonts, CDN, installation, repository access, API key or local server is needed. Where a file tool is unavailable, return the complete HTML as copy-ready text and explicitly state that no file was created.

## Design and behavior contract

| Element | Light | Dark |
| --- | --- | --- |
| Page | `#E4E7E7` muted gray | `#263746` softened navy |
| Panels | `#F1F2EF` stone | `#304655` slate navy |
| Text | `#243641` | `#EFF1EF` |
| Secondary text | `#4E606A` | `#C0CDD3` |
| Suite accent | `#315c75` | `#b0d3e6` |
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
<title>Transaction Monitoring Review</title>
<style>
:root{--bg:#e4e7e7;--panel:#f1f2ef;--ink:#243641;--muted:#4e606a;--line:#9baab0;--accent:#315c75;--soft:#d4dee2;--high:#8a3439;--medium:#735119;--low:#315f54;--focus:#005f9c;--radius:8px}
:root[data-theme=dark]{--bg:#263746;--panel:#304655;--ink:#eff1ef;--muted:#c0cdd3;--line:#6b8291;--accent:#b0d3e6;--soft:#3c5667;--high:#ffb8b8;--medium:#f0d393;--low:#b1dcc9;--focus:#9bd3fa}
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
  "slug": "transaction-monitoring",
  "title": "Transaction Monitoring Review",
  "summary": "Reconcile a transaction extract, calculate transparent monitoring scenarios, and turn rule matches into reviewable observations with explicit benign explanations.",
  "audience": "Monitoring analysts, scenario owners, and independent control reviewers",
  "decision": "Which scenario matches merit further review, which have supported explanations, and which cannot be assessed because the inputs are incomplete?",
  "palette": "slate",
  "report_sections": [
    "Review priorities and known movement",
    "Scope, population, and scenario method",
    "Findings and benign explanations",
    "Account flow calculations",
    "Scenario matches and review outcomes",
    "Evidence and criterion provenance",
    "Proposed review and data-repair actions",
    "Limitations, quality checks, and human decision"
  ],
  "domain_tables": [
    {
      "name": "RawTransactions",
      "title": "Raw source rows and terminal reconciliation",
      "columns": [
        "raw_row_id",
        "transaction_id",
        "account_id",
        "event_utc",
        "direction",
        "amount_text",
        "currency",
        "counterparty_id",
        "posting_state",
        "ownership_state",
        "terminal_bucket",
        "evidence_ids"
      ],
      "rows": [
        [
          "R01",
          "T01",
          "A",
          "2026-09-01T13:00:00Z",
          "CREDIT",
          "6000.00",
          "USD",
          "P01",
          "POSTED",
          "CONFIRMED_EXTERNAL",
          "PROCESSED",
          "SYN-001"
        ],
        [
          "R02",
          "T02",
          "A",
          "2026-09-01T14:00:00Z",
          "CREDIT",
          "4000.00",
          "USD",
          "P02",
          "POSTED",
          "CONFIRMED_EXTERNAL",
          "PROCESSED",
          "SYN-001"
        ],
        [
          "R03",
          "T03",
          "A",
          "2026-09-01T15:00:00Z",
          "DEBIT",
          "9500.00",
          "USD",
          "P03",
          "POSTED",
          "CONFIRMED_EXTERNAL",
          "PROCESSED",
          "SYN-001"
        ],
        [
          "R04",
          "T04",
          "B",
          "2026-09-01T13:00:00Z",
          "CREDIT",
          "5000.00",
          "USD",
          "P04",
          "POSTED",
          "CONFIRMED_EXTERNAL",
          "PROCESSED",
          "SYN-001"
        ],
        [
          "R05",
          "T05",
          "B",
          "2026-09-01T16:00:00Z",
          "DEBIT",
          "4800.00",
          "USD",
          "P05",
          "POSTED",
          "CONFIRMED_EXTERNAL",
          "PROCESSED",
          "SYN-001"
        ],
        [
          "R06",
          "T06",
          "C",
          "2026-09-01T13:00:00Z",
          "CREDIT",
          "3000.00",
          "USD",
          "C-OWN-1",
          "POSTED",
          "CONFIRMED_OWN",
          "PROCESSED",
          "SYN-001;SYN-004"
        ],
        [
          "R07",
          "T07",
          "C",
          "2026-09-01T14:00:00Z",
          "DEBIT",
          "3000.00",
          "USD",
          "C-OWN-2",
          "POSTED",
          "CONFIRMED_OWN",
          "PROCESSED",
          "SYN-001;SYN-004"
        ],
        [
          "R08",
          "T08",
          "D",
          "2026-09-01T17:00:00Z",
          "DEBIT",
          "1000.00",
          "USD",
          "P06",
          "POSTED",
          "CONFIRMED_EXTERNAL",
          "PROCESSED",
          "SYN-001"
        ],
        [
          "R09",
          "T01",
          "A",
          "2026-09-01T13:00:00Z",
          "CREDIT",
          "6000.00",
          "USD",
          "P01",
          "POSTED",
          "CONFIRMED_EXTERNAL",
          "DUPLICATE",
          "SYN-001"
        ],
        [
          "R10",
          "T09",
          "D",
          "2026-09-01T18:00:00Z",
          "DEBIT",
          "unreadable",
          "USD",
          "P07",
          "POSTED",
          "CONFIRMED_EXTERNAL",
          "UNPARSED",
          "SYN-001;SYN-005"
        ]
      ],
      "formats": {},
      "primary_key": [
        "raw_row_id"
      ],
      "column_contracts": {
        "raw_row_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable."
        },
        "transaction_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Source economic transaction identifier. Its uniqueness is assessed with account leg and source version; matching amount or narrative alone is insufficient."
        },
        "account_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge."
        },
        "event_utc": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant."
        },
        "direction": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Canonical CREDIT or DEBIT from the account perspective. Amount remains nonnegative; do not infer direction from a signed display string."
        },
        "amount_text": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact source amount string before parsing. It can contain unreadable text; preserve it as evidence and never sum it directly."
        },
        "currency": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount."
        },
        "counterparty_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Supplied counterparty reference for this economic leg. Similar names or repeated identifiers do not independently establish common ownership."
        },
        "posting_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Canonical posting status that determines whether a leg enters the declared posted population. A pending item remains visible outside that population."
        },
        "ownership_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Evidence-backed own/external classification for the specific leg and historical period. Unknown ownership is not automatically external or own."
        },
        "terminal_bucket": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exactly one initial raw-row reconciliation outcome. It explains whether the row is processed, duplicate or unreadable; scenario exclusions are a separate layer."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation."
        }
      },
      "grain": "one immutable raw receipt row, including extraction duplicates and unparsed amounts",
      "report_section": 4
    },
    {
      "name": "CanonicalLedger",
      "title": "Canonical known posted account legs",
      "columns": [
        "leg_id",
        "raw_row_id",
        "transaction_id",
        "account_id",
        "event_utc",
        "direction",
        "amount",
        "currency",
        "counterparty_id",
        "ownership_state",
        "scenario_eligible",
        "evidence_ids"
      ],
      "rows": [
        [
          "L-T01",
          "R01",
          "T01",
          "A",
          "2026-09-01T13:00:00Z",
          "CREDIT",
          6000.0,
          "USD",
          "P01",
          "CONFIRMED_EXTERNAL",
          true,
          "SYN-001"
        ],
        [
          "L-T02",
          "R02",
          "T02",
          "A",
          "2026-09-01T14:00:00Z",
          "CREDIT",
          4000.0,
          "USD",
          "P02",
          "CONFIRMED_EXTERNAL",
          true,
          "SYN-001"
        ],
        [
          "L-T03",
          "R03",
          "T03",
          "A",
          "2026-09-01T15:00:00Z",
          "DEBIT",
          9500.0,
          "USD",
          "P03",
          "CONFIRMED_EXTERNAL",
          true,
          "SYN-001"
        ],
        [
          "L-T04",
          "R04",
          "T04",
          "B",
          "2026-09-01T13:00:00Z",
          "CREDIT",
          5000.0,
          "USD",
          "P04",
          "CONFIRMED_EXTERNAL",
          true,
          "SYN-001"
        ],
        [
          "L-T05",
          "R05",
          "T05",
          "B",
          "2026-09-01T16:00:00Z",
          "DEBIT",
          4800.0,
          "USD",
          "P05",
          "CONFIRMED_EXTERNAL",
          true,
          "SYN-001"
        ],
        [
          "L-T06",
          "R06",
          "T06",
          "C",
          "2026-09-01T13:00:00Z",
          "CREDIT",
          3000.0,
          "USD",
          "C-OWN-1",
          "CONFIRMED_OWN",
          false,
          "SYN-001;SYN-004"
        ],
        [
          "L-T07",
          "R07",
          "T07",
          "C",
          "2026-09-01T14:00:00Z",
          "DEBIT",
          3000.0,
          "USD",
          "C-OWN-2",
          "CONFIRMED_OWN",
          false,
          "SYN-001;SYN-004"
        ],
        [
          "L-T08",
          "R08",
          "T08",
          "D",
          "2026-09-01T17:00:00Z",
          "DEBIT",
          1000.0,
          "USD",
          "P06",
          "CONFIRMED_EXTERNAL",
          true,
          "SYN-001"
        ]
      ],
      "formats": {
        "amount": "#,##0.00"
      },
      "primary_key": [
        "leg_id"
      ],
      "column_contracts": {
        "leg_id": {
          "type": "text",
          "nullable": true,
          "unit": "identifier",
          "description": "Unique identifier of one readable canonical posted account leg. It joins to the raw source and is never substituted for a customer identifier."
        },
        "raw_row_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable."
        },
        "transaction_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Source economic transaction identifier. Its uniqueness is assessed with account leg and source version; matching amount or narrative alone is insufficient."
        },
        "account_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge."
        },
        "event_utc": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant."
        },
        "direction": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Canonical CREDIT or DEBIT from the account perspective. Amount remains nonnegative; do not infer direction from a signed display string."
        },
        "amount": {
          "type": "number",
          "nullable": true,
          "unit": "row currency",
          "description": "Known nonnegative monetary amount in the row currency. Null means unrecovered source value and blocks the relevant completeness proposition."
        },
        "currency": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount."
        },
        "counterparty_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Supplied counterparty reference for this economic leg. Similar names or repeated identifiers do not independently establish common ownership."
        },
        "ownership_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Evidence-backed own/external classification for the specific leg and historical period. Unknown ownership is not automatically external or own."
        },
        "scenario_eligible": {
          "type": "boolean",
          "nullable": false,
          "unit": "boolean",
          "description": "Boolean record-level inclusion flag. True means a known eligible leg, not proof the entire account or window is complete."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation."
        }
      },
      "foreign_keys": [
        {
          "columns": [
            "raw_row_id"
          ],
          "table": "RawTransactions",
          "references": [
            "raw_row_id"
          ]
        }
      ],
      "grain": "one readable unique posted economic account leg",
      "report_section": 4
    },
    {
      "name": "Eligibility",
      "title": "Raw-row scenario eligibility decisions",
      "columns": [
        "eligibility_id",
        "raw_row_id",
        "leg_id",
        "account_id",
        "scenario_id",
        "eligibility_state",
        "reason",
        "evidence_ids"
      ],
      "rows": [
        [
          "EL-R01",
          "R01",
          "L-T01",
          "A",
          "TM-01",
          "ELIGIBLE_KNOWN",
          "Known external posted leg; account-level completeness checked separately",
          "SYN-001"
        ],
        [
          "EL-R02",
          "R02",
          "L-T02",
          "A",
          "TM-01",
          "ELIGIBLE_KNOWN",
          "Known external posted leg; account-level completeness checked separately",
          "SYN-001"
        ],
        [
          "EL-R03",
          "R03",
          "L-T03",
          "A",
          "TM-01",
          "ELIGIBLE_KNOWN",
          "Known external posted leg; account-level completeness checked separately",
          "SYN-001"
        ],
        [
          "EL-R04",
          "R04",
          "L-T04",
          "B",
          "TM-01",
          "ELIGIBLE_KNOWN",
          "Known external posted leg; account-level completeness checked separately",
          "SYN-001"
        ],
        [
          "EL-R05",
          "R05",
          "L-T05",
          "B",
          "TM-01",
          "ELIGIBLE_KNOWN",
          "Known external posted leg; account-level completeness checked separately",
          "SYN-001"
        ],
        [
          "EL-R06",
          "R06",
          "L-T06",
          "C",
          "TM-01",
          "EXCLUDED_OWN",
          "SYN-004 confirms common customer ownership during period",
          "SYN-001;SYN-004"
        ],
        [
          "EL-R07",
          "R07",
          "L-T07",
          "C",
          "TM-01",
          "EXCLUDED_OWN",
          "SYN-004 confirms common customer ownership during period",
          "SYN-001;SYN-004"
        ],
        [
          "EL-R08",
          "R08",
          "L-T08",
          "D",
          "TM-01",
          "ELIGIBLE_KNOWN",
          "Known external posted leg; account-level completeness checked separately",
          "SYN-001"
        ],
        [
          "EL-R09",
          "R09",
          "L-T01",
          "A",
          "TM-01",
          "DUPLICATE",
          "Exact second extraction of R01; not another account leg",
          "SYN-001"
        ],
        [
          "EL-R10",
          "R10",
          null,
          "D",
          "TM-01",
          "BLOCKED",
          "Posted in-scope amount unreadable; blocks D completeness",
          "SYN-001;SYN-005"
        ]
      ],
      "formats": {},
      "primary_key": [
        "eligibility_id"
      ],
      "column_contracts": {
        "eligibility_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique identifier for a raw-row/scenario decision. It preserves reasons for retained, excluded and blocked records without removing source population members."
        },
        "raw_row_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable."
        },
        "leg_id": {
          "type": "text",
          "nullable": true,
          "unit": "identifier",
          "description": "Unique identifier of one readable canonical posted account leg. It joins to the raw source and is never substituted for a customer identifier."
        },
        "account_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge."
        },
        "scenario_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Exact illustrative scenario identifier. Criteria are versioned outside the identifier in the case manifest and cannot drift between outputs."
        },
        "eligibility_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Record-level eligibility conclusion. ELIGIBLE_KNOWN, EXCLUDED_OWN, DUPLICATE and BLOCKED are mutually exclusive in the specimen."
        },
        "reason": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Specific evidence-backed reason for a state or transition. It identifies the relevant row, rule or missing fact rather than a generic compliance label."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation."
        }
      },
      "foreign_keys": [
        {
          "columns": [
            "raw_row_id"
          ],
          "table": "RawTransactions",
          "references": [
            "raw_row_id"
          ]
        }
      ],
      "grain": "one raw-row decision for the declared daily scenario",
      "report_section": 4
    },
    {
      "name": "AccountFlows",
      "columns": [
        "account_id",
        "currency",
        "processed_tx_count",
        "credit_total",
        "debit_total",
        "eligible_credit_total",
        "eligible_debit_total",
        "out_in_ratio",
        "population_status"
      ],
      "rows": [
        [
          "A",
          "USD",
          3,
          10000,
          9500,
          10000,
          9500,
          0.95,
          "COMPLETE"
        ],
        [
          "B",
          "USD",
          2,
          5000,
          4800,
          5000,
          4800,
          0.96,
          "COMPLETE"
        ],
        [
          "C",
          "USD",
          2,
          3000,
          3000,
          0,
          0,
          null,
          "OWN_TRANSFER_EXCLUDED"
        ],
        [
          "D",
          "USD",
          1,
          0,
          1000,
          0,
          1000,
          null,
          "UNPARSED_AMOUNT"
        ]
      ],
      "formats": {
        "credit_total": "#,##0.00",
        "debit_total": "#,##0.00",
        "eligible_credit_total": "#,##0.00",
        "eligible_debit_total": "#,##0.00",
        "out_in_ratio": "0.0%"
      },
      "primary_key": [
        "account_id",
        "currency"
      ],
      "column_contracts": {
        "account_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge."
        },
        "currency": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount."
        },
        "processed_tx_count": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Count of readable canonical economic legs at account/currency grain. It excludes extraction duplicates and unknown-amount rows but retains own transfers."
        },
        "credit_total": {
          "type": "number",
          "nullable": false,
          "unit": "row currency",
          "description": "Known eligible or gross credit subtotal as specified by the table grain. It is not necessarily a complete total when coverage_state or population_status is defective."
        },
        "debit_total": {
          "type": "number",
          "nullable": true,
          "unit": "row currency",
          "description": "Known eligible debit subtotal at the table grain. Null is required for a window total dependent on an unknown debit; known subtotals elsewhere remain explicitly partial."
        },
        "eligible_credit_total": {
          "type": "number",
          "nullable": false,
          "unit": "row currency",
          "description": "Sum of known credit amounts after stated scenario exclusions. It cannot include confirmed own legs or a copied extraction duplicate."
        },
        "eligible_debit_total": {
          "type": "number",
          "nullable": false,
          "unit": "row currency",
          "description": "Sum of known debit amounts after stated scenario exclusions. It is not an attributed or suspicious amount and may exceed eligible credits."
        },
        "out_in_ratio": {
          "type": "number",
          "nullable": true,
          "unit": "ratio",
          "description": "Eligible debit total divided by positive eligible credit total. Stored as a dimensionless ratio and displayed as a percentage without changing decision precision."
        },
        "population_status": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Account-level completeness or exclusion state. COMPLETE, OWN_TRANSFER_EXCLUDED and UNPARSED_AMOUNT have different analytical consequences."
        }
      },
      "title": "AccountFlows",
      "grain": "one account and currency within the fixed daily event period",
      "report_section": 5
    },
    {
      "name": "WindowDiagnostics",
      "title": "Observed credit-anchored membership; coverage remains incomplete",
      "columns": [
        "window_id",
        "account_id",
        "anchor_leg_id",
        "start_utc",
        "end_utc",
        "observed_leg_ids",
        "known_credit_total",
        "known_debit_total",
        "known_ratio",
        "first_debit_hours",
        "coverage_state",
        "evidence_ids"
      ],
      "rows": [
        [
          "W-A-T01",
          "A",
          "L-T01",
          "2026-09-01T13:00:00Z",
          "2026-09-02T13:00:00Z",
          "L-T01;L-T02;L-T03",
          10000,
          9500,
          0.95,
          2,
          "BOUNDARY_INCOMPLETE",
          "SYN-001;SYN-006"
        ],
        [
          "W-A-T02",
          "A",
          "L-T02",
          "2026-09-01T14:00:00Z",
          "2026-09-02T14:00:00Z",
          "L-T02;L-T03",
          4000,
          9500,
          2.375,
          1,
          "BOUNDARY_INCOMPLETE",
          "SYN-001;SYN-006"
        ],
        [
          "W-B-T04",
          "B",
          "L-T04",
          "2026-09-01T13:00:00Z",
          "2026-09-02T13:00:00Z",
          "L-T04;L-T05",
          5000,
          4800,
          0.96,
          3,
          "BOUNDARY_INCOMPLETE",
          "SYN-001;SYN-006"
        ]
      ],
      "formats": {
        "known_credit_total": "#,##0.00",
        "known_debit_total": "#,##0.00",
        "known_ratio": "0.0%",
        "first_debit_hours": "0.0"
      },
      "primary_key": [
        "window_id"
      ],
      "column_contracts": {
        "window_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable account/anchor/specification window key. It distinguishes overlapping observations so a membership count cannot be mistaken for unique transactions."
        },
        "account_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge."
        },
        "anchor_leg_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Canonical eligible credit that starts a diagnostic window. Only credit anchors are used; a debit cannot silently become an anchor."
        },
        "start_utc": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Inclusive UTC instant at the anchor. The applicable window convention determines endpoint inclusion, not the date formatting of the rendered table."
        },
        "end_utc": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "UTC endpoint exactly 24 elapsed hours after the anchor. The scenario-design closed interval includes this instant; the TM diagnostic convention matches it."
        },
        "observed_leg_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited canonical legs observed inside the diagnostic interval. This list is partial when the extract does not cover the entire interval."
        },
        "known_credit_total": {
          "type": "number",
          "nullable": false,
          "unit": "row currency",
          "description": "Sum of readable credits only at the declared stage, account or observed diagnostic window. The word known is substantive where an unresolved amount exists."
        },
        "known_debit_total": {
          "type": "number",
          "nullable": false,
          "unit": "row currency",
          "description": "Sum of readable debits only at the declared stage, account or observed diagnostic window. An unknown debit is not imputed as a measured zero."
        },
        "known_ratio": {
          "type": "number",
          "nullable": true,
          "unit": "ratio",
          "description": "Ratio of known observed debits to known observed credits when the denominator is positive. Boundary-incomplete diagnostics do not establish a complete rule result."
        },
        "first_debit_hours": {
          "type": "number",
          "nullable": true,
          "unit": "hours",
          "description": "Elapsed hours from anchor to first strictly subsequent eligible debit. Null means no qualifying ordered pair; a contemporaneous debit cannot satisfy the predicate."
        },
        "coverage_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Completeness state for the exact account/window inputs. COMPLETE, BOUNDARY_INCOMPLETE and AMOUNT_UNKNOWN cannot be collapsed into a binary risk score."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation."
        }
      },
      "foreign_keys": [
        {
          "columns": [
            "anchor_leg_id"
          ],
          "table": "CanonicalLedger",
          "references": [
            "leg_id"
          ]
        }
      ],
      "grain": "one eligible credit anchor and its observed closed 24-hour interval",
      "report_section": 5
    },
    {
      "name": "ScenarioResults",
      "columns": [
        "scenario_result_id",
        "account_id",
        "scenario_id",
        "eligible",
        "rule_result",
        "first_credit_to_debit_hours",
        "review_outcome",
        "evidence_ids"
      ],
      "rows": [
        [
          "SR-001",
          "A",
          "TM-01",
          true,
          "MATCH",
          2,
          "ESCALATE_FOR_REVIEW",
          "SYN-001;SYN-002"
        ],
        [
          "SR-002",
          "B",
          "TM-01",
          true,
          "MATCH",
          3,
          "EXPLANATION_SUPPORTED",
          "SYN-001;SYN-003"
        ],
        [
          "SR-003",
          "C",
          "TM-01",
          false,
          "EXCLUDED",
          null,
          "OWN_TRANSFER_CONFIRMED",
          "SYN-001;SYN-004"
        ],
        [
          "SR-004",
          "D",
          "TM-01",
          false,
          "NOT_ASSESSABLE",
          null,
          "DATA_REPAIR_REQUIRED",
          "SYN-001;SYN-005"
        ]
      ],
      "formats": {
        "first_credit_to_debit_hours": "0.0"
      },
      "primary_key": [
        "scenario_result_id"
      ],
      "column_contracts": {
        "scenario_result_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable daily account/scenario/window result key. It links to the review register without being replaced after a contextual explanation."
        },
        "account_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge."
        },
        "scenario_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Exact illustrative scenario identifier. Criteria are versioned outside the identifier in the case manifest and cannot drift between outputs."
        },
        "eligible": {
          "type": "boolean",
          "nullable": false,
          "unit": "boolean",
          "description": "Account-result eligibility flag after completeness and exclusion gates. False is distinguished by rule_result as either excluded or not assessable."
        },
        "rule_result": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Deterministic raw result under the named specification: MATCH, NO_MATCH, EXCLUDED or NOT_ASSESSABLE. Contextual evidence does not rewrite it."
        },
        "first_credit_to_debit_hours": {
          "type": "number",
          "nullable": true,
          "unit": "hours",
          "description": "Elapsed hours from the first eligible daily credit to its first strictly subsequent eligible debit. It screens timing and does not attribute funding."
        },
        "review_outcome": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Proposed contextual assessment distinct from raw rule_result. No value in this field constitutes an authorized filing or relationship decision."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation."
        }
      },
      "title": "ScenarioResults",
      "grain": "one account, daily window and scenario specification",
      "report_section": 5
    },
    {
      "name": "ReviewLedger",
      "title": "Contextual review and unrecorded human disposition",
      "columns": [
        "review_id",
        "scenario_result_id",
        "finding_id",
        "account_id",
        "raw_result",
        "explanation_state",
        "counterevidence",
        "next_evidence",
        "human_disposition",
        "evidence_ids"
      ],
      "rows": [
        [
          "RV-A",
          "SR-001",
          "TM-F01",
          "A",
          "MATCH",
          "UNSUPPORTED",
          "No opening balance or onward P03 records; timing does not trace funds",
          "Invoice or contract matching T03 plus counterparty role",
          "NOT_RECORDED",
          "SYN-001;SYN-002"
        ],
        [
          "RV-B",
          "SR-002",
          "TM-F02",
          "B",
          "MATCH",
          "SUPPORTED_FOR_T05",
          "One invoice does not establish relationship-wide legitimacy",
          "Reviewer assessment of invoice linkage and remaining scope",
          "NOT_RECORDED",
          "SYN-001;SYN-003"
        ],
        [
          "RV-C",
          "SR-003",
          null,
          "C",
          "EXCLUDED",
          "OWNERSHIP_CONFIRMED",
          "Exclusion applies only to external-flow TM-01",
          "Retain SYN-004 and check any other applicable scenario separately",
          "NOT_RECORDED",
          "SYN-001;SYN-004"
        ],
        [
          "RV-D",
          "SR-004",
          "TM-F03",
          "D",
          "NOT_ASSESSABLE",
          "SOURCE_DEFECT",
          "Known debit does not bound unreadable T09 value",
          "Corrected T09 amount and source control total",
          "NOT_RECORDED",
          "SYN-001;SYN-005"
        ]
      ],
      "formats": {},
      "primary_key": [
        "review_id"
      ],
      "column_contracts": {
        "review_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique contextual review record. It joins the exact raw scenario result and retains the relevant finding or an explained null when no finding is raised."
        },
        "scenario_result_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable daily account/scenario/window result key. It links to the review register without being replaced after a contextual explanation."
        },
        "finding_id": {
          "type": "text",
          "nullable": true,
          "unit": "identifier",
          "description": "Stable key to the Findings register. Nullable only where a documented review outcome raises no separate finding; absence is not a missing case record."
        },
        "account_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge."
        },
        "raw_result": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Preserved deterministic rule result before human review or delivery grouping. Explanations and grouping decisions must not delete or change it."
        },
        "explanation_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Scope-limited state of the explanation evidence. Supported documentation for one payment does not become an assurance about the whole account."
        },
        "counterevidence": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Strongest supplied limitation or competing interpretation that tempers the proposed concern. It may identify missing evidence without treating missingness as guilt."
        },
        "next_evidence": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Specific discriminating document or control record needed for the next decision. It is a request proposal, not evidence that retrieval occurred."
        },
        "human_disposition": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Recorded authorized human decision. NOT_RECORDED is required in this specimen because no real person has approved or closed anything."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation."
        }
      },
      "foreign_keys": [
        {
          "columns": [
            "scenario_result_id"
          ],
          "table": "ScenarioResults",
          "references": [
            "scenario_result_id"
          ]
        }
      ],
      "grain": "one contextual review of a retained daily scenario result",
      "report_section": 5
    },
    {
      "name": "ControlTotals",
      "title": "Count and monetary reconciliation with known limits",
      "columns": [
        "control_id",
        "measure",
        "expected_value",
        "actual_value",
        "unit",
        "result",
        "calculation",
        "evidence_ids"
      ],
      "rows": [
        [
          "CT-01",
          "Received rows",
          10,
          10,
          "rows",
          "PASS",
          "8 processed + 1 duplicate + 1 unparsed",
          "SYN-001"
        ],
        [
          "CT-02",
          "Canonical known legs",
          8,
          8,
          "legs",
          "PASS",
          "L-T01 through L-T08",
          "SYN-001"
        ],
        [
          "CT-03",
          "Known credits",
          18000,
          18000,
          "USD",
          "PASS",
          "6000 + 4000 + 5000 + 3000",
          "SYN-001"
        ],
        [
          "CT-04",
          "Known debits",
          18300,
          18300,
          "USD",
          "PASS",
          "9500 + 4800 + 3000 + 1000",
          "SYN-001"
        ],
        [
          "CT-05",
          "Complete monetary population",
          null,
          null,
          "USD",
          "NOT_ASSESSABLE",
          "T09 amount unknown; known gross is 36300, not complete gross",
          "SYN-001;SYN-005"
        ],
        [
          "CT-06",
          "Daily rule matches",
          2,
          2,
          "account windows",
          "PASS",
          "SR-001 and SR-002",
          "SYN-001"
        ],
        [
          "CT-07",
          "Distinct observed rolling legs",
          5,
          5,
          "legs",
          "PASS",
          "Union T01,T02,T03,T04,T05; membership count 7",
          "SYN-001;SYN-006"
        ]
      ],
      "formats": {},
      "primary_key": [
        "control_id"
      ],
      "column_contracts": {
        "control_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique reconciliation-control key. Controls can test different grains; counts and monetary comparisons are never combined into one unexplained balance."
        },
        "measure": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Precisely named control measure including known versus complete scope. A passing count measure cannot substitute for unknown monetary completeness."
        },
        "expected_value": {
          "type": "number",
          "nullable": true,
          "unit": "row unit",
          "description": "Independent expected numerical control value when known. Null records a proposition whose true value is unavailable rather than a failed zero comparison."
        },
        "actual_value": {
          "type": "number",
          "nullable": true,
          "unit": "row unit",
          "description": "Reproduced value from the supplied rows. Null remains null when the corresponding measure is unavailable; never enter an attractive expected value by copying."
        },
        "unit": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Physical or analytical unit of the control, such as USD, rows, legs or account windows. The label determines what can validly be added or divided."
        },
        "result": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Control result or acceptance state. PASS applies to an executed synthetic check; it is not regulatory assurance or an operational approval."
        },
        "calculation": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Explicit arithmetic or set-membership expression supporting the control. It retains unknown components instead of replacing them with a rounded display."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation."
        }
      },
      "grain": "one explicitly named count or monetary reconciliation proposition",
      "report_section": 5
    },
    {
      "name": "EvidenceProvenance",
      "title": "Source identity, period, availability and evidential limits",
      "columns": [
        "evidence_id",
        "source_kind",
        "source_date",
        "availability",
        "locator",
        "supports",
        "limitation"
      ],
      "rows": [
        [
          "SYN-001",
          "Authored fictional case record",
          "2026-09-02",
          "FULL_TEXT_IN_FILE_10",
          "10-worked-example.md, raw population R01\u2013R10",
          "Fictional transaction extract",
          "Supports only the stated fictional proposition; no external subject fact or institutional approval"
        ],
        [
          "SYN-002",
          "Authored fictional context record",
          "2026-09-02",
          "FULL_TEXT_IN_FILE_10",
          "10-worked-example.md, context register A",
          "Fictional account A profile",
          "Supports only the stated fictional proposition; no external subject fact or institutional approval"
        ],
        [
          "SYN-003",
          "Authored fictional case record",
          "2026-09-02",
          "FULL_TEXT_IN_FILE_10",
          "10-worked-example.md, context register B",
          "Fictional invoice and matching confirmation",
          "Supports only the stated fictional proposition; no external subject fact or institutional approval"
        ],
        [
          "SYN-004",
          "Authored fictional case record",
          "2026-09-02",
          "FULL_TEXT_IN_FILE_10",
          "10-worked-example.md, context register C",
          "Fictional ownership confirmation",
          "Supports only the stated fictional proposition; no external subject fact or institutional approval"
        ],
        [
          "SYN-005",
          "Authored fictional case record",
          "2026-09-02",
          "FULL_TEXT_IN_FILE_10",
          "10-worked-example.md, raw row R10",
          "Fictional extract defect",
          "Supports only the stated fictional proposition; no external subject fact or institutional approval"
        ],
        [
          "SYN-006",
          "Authored fictional case record",
          "2026-09-02",
          "FULL_TEXT_IN_FILE_10",
          "10-worked-example.md, Window diagnostic convention; coverage stops Sep 02, 2026 12:00 AM ET",
          "Fictional diagnostic window specification",
          "Supports only the stated fictional proposition; no external subject fact or institutional approval"
        ]
      ],
      "formats": {},
      "primary_key": [
        "evidence_id"
      ],
      "column_contracts": {
        "evidence_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Exact unique Evidence key at one source-provenance row. It joins the common Evidence register without combining unrelated sources."
        },
        "source_kind": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Explicitly fictional record type and origin. Authored cases and guidance references must not be mislabeled as actual institutional evidence."
        },
        "source_date": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "ISO calendar date of the authored source package, distinct from transaction event dates and evidence retrieval dates."
        },
        "availability": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "State of access to the source text. FULL_TEXT_IN_FILE_10 means the complete fictional content is supplied in this suite, not externally verified."
        },
        "locator": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact file and section or row reference supporting retrieval of the fictional source. A title alone is insufficient."
        },
        "supports": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Bounded proposition the source can establish in the synthetic exercise. It does not certify any broader customer or control conclusion."
        },
        "limitation": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Specific scope restriction or evidential weakness that must accompany use of the source."
        }
      },
      "grain": "one fictional evidence source with its access state and evidential limit",
      "report_section": 5
    },
    {
      "name": "ProcessQA",
      "title": "Explicit expected and actual control evidence",
      "columns": [
        "check_id",
        "check",
        "expected",
        "actual",
        "status",
        "reviewer",
        "evidence_ids"
      ],
      "rows": [
        [
          "TQ01",
          "All source rows have one terminal bucket",
          "10 = 8 + 1 + 1",
          "10 = 8 + 1 + 1",
          "PASS",
          "Authored specimen arithmetic; independent operational reviewer not supplied",
          "SYN-001"
        ],
        [
          "TQ02",
          "Daily rule hits remain after B explanation",
          "A and B MATCH",
          "A and B MATCH",
          "PASS",
          "Authored specimen arithmetic; independent operational reviewer not supplied",
          "SYN-001;SYN-003"
        ],
        [
          "TQ03",
          "Rolling coverage",
          "Three windows BOUNDARY_INCOMPLETE",
          "Three windows BOUNDARY_INCOMPLETE",
          "PASS",
          "Authored specimen arithmetic; independent operational reviewer not supplied",
          "SYN-001;SYN-006"
        ],
        [
          "TQ04",
          "Complete monetary population",
          "No complete total established",
          "T09 amount unknown",
          "REVIEW REQUIRED",
          "Authored specimen arithmetic; independent operational reviewer not supplied",
          "SYN-005"
        ],
        [
          "TQ05",
          "Independent human disposition",
          "Not supplied",
          "Not supplied",
          "NOT RECORDED",
          "Authored specimen arithmetic; independent operational reviewer not supplied",
          "SYN-001"
        ]
      ],
      "formats": {},
      "primary_key": [
        "check_id"
      ],
      "column_contracts": {
        "check_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique process-quality check key retained across output formats. A later rerun creates a dated actual result without changing the original expectation."
        },
        "check": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Falsifiable control proposition with defined expected evidence. It must be precise enough for another reviewer to reproduce."
        },
        "expected": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact target result for the named check. This is fixed before execution and may state not supplied when the check concerns authorization."
        },
        "actual": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Recorded output of the check. In future sessions, use NOT TESTED until performed; do not copy the specimen result as evidence of a new execution."
        },
        "status": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Recorded PASS, FAIL, REVIEW REQUIRED, NOT RECORDED or NOT TESTED status for this check, separate from analytical finding severity."
        },
        "reviewer": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Identity or role of the actual check performer. The specimen labels authored arithmetic and explicitly records absent independent operational review."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation."
        }
      },
      "grain": "one performed or explicitly unrecorded quality proposition",
      "report_section": 5
    }
  ],
  "findings": [
    {
      "id": "TM-F01",
      "title": "Account A meets the illustrative rapid-movement rule",
      "severity": "MEDIUM",
      "confidence": "MODERATE",
      "claim_class": "Inferred",
      "evidence_ids": [
        "SYN-001",
        "SYN-002"
      ],
      "detail": "Account A received $10,000.00 and sent $9,500.00 within two hours of the first receipt; the 95.0% ratio meets TM-01. Purpose remains unsupported.",
      "recommendation": "Obtain payment purpose and counterparties; refer to the authorized reviewer."
    },
    {
      "id": "TM-F02",
      "title": "Account B has a supported ordinary-business explanation",
      "severity": "LOW",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001",
        "SYN-003"
      ],
      "detail": "The 96.0% rule match is retained; a matched supplier invoice supports the $4,800.00 payment.",
      "recommendation": "Document the explanation and seek human disposition; retain the rule hit."
    },
    {
      "id": "TM-F03",
      "title": "Account D cannot be fully assessed",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001",
        "SYN-005"
      ],
      "detail": "One unreadable amount prevents account-level completeness; $1,000.00 is only the known posted debit.",
      "recommendation": "Repair the source extract and recompute D before making an account conclusion."
    }
  ],
  "evidence": [
    {
      "id": "SYN-001",
      "title": "Fictional transaction extract",
      "locator": "10-worked-example.md, raw population R01\u2013R10",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-002",
      "title": "Fictional account A profile",
      "locator": "10-worked-example.md, context register A",
      "claim_class": "Reported"
    },
    {
      "id": "SYN-003",
      "title": "Fictional invoice and matching confirmation",
      "locator": "10-worked-example.md, context register B",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-004",
      "title": "Fictional ownership confirmation",
      "locator": "10-worked-example.md, context register C",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-005",
      "title": "Fictional extract defect",
      "locator": "10-worked-example.md, raw row R10",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-006",
      "title": "Fictional diagnostic window specification",
      "locator": "10-worked-example.md, Window diagnostic convention; coverage stops Sep 02, 2026 12:00 AM ET",
      "claim_class": "Observed"
    }
  ],
  "metrics": [
    {
      "label": "Raw rows",
      "value": 10,
      "method": "Count R01\u2013R10 before deduplication",
      "format": "#,##0"
    },
    {
      "label": "Processed transactions",
      "value": 8,
      "method": "10 raw minus 1 duplicate minus 1 unparsed",
      "format": "#,##0"
    },
    {
      "label": "Known gross movement USD",
      "value": 36300,
      "method": "$18,000.00 credits plus $18,300.00 debits; excludes unknown R10 amount",
      "format": "$#,##0.00"
    },
    {
      "label": "Rule matches",
      "value": 2,
      "method": "A and B match TM-01; C excluded; D not assessable",
      "format": "#,##0"
    }
  ],
  "limitations": [
    "Synthetic rules are illustrative and are not regulatory thresholds.",
    "Account D has an unknown amount; total monetary completeness is not established.",
    "No opening balances or complete external flow paths are supplied.",
    "The three rolling-window diagnostics extend beyond the extract end; known observed sums are reproducible but a complete rolling-rule result is not available."
  ],
  "conclusion": "Two accounts match the illustrative rapid-movement rule. One has a supported invoice explanation; the other needs further review. A separate account remains not assessable because an amount is unreadable.",
  "report_narrative": [
    [
      "Two accounts match the illustrative rapid-movement rule. One has a supported invoice explanation; the other needs further review. A separate account remains not assessable because an amount is unreadable."
    ],
    [
      "The ten raw rows reconcile to eight processed transactions after the documented duplicate and exclusion decisions. The fictional scenario uses explicit amount, ratio and timing criteria; unreadable amounts remain outside assessable sums."
    ],
    [
      "TM-F01: Account A received $10,000.00 and sent $9,500.00 within two hours of the first receipt; the 95.0% ratio meets TM-01. Purpose remains unsupported.",
      "TM-F02: The 96.0% rule match is retained; a matched supplier invoice supports the $4,800.00 payment.",
      "TM-F03: One unreadable amount prevents account-level completeness; $1,000.00 is only the known posted debit."
    ],
    [
      "Known gross movement is $36,300.00 within the captured records. Account totals retain the relationship between incoming and outgoing activity; gross movement is not net loss, customer income or suspicious value.",
      "RawTransactions retains all ten rows; CanonicalLedger contains the eight readable unique posted legs. Eligibility retains ten separate reasons. Credit-anchored diagnostics contain seven memberships over five distinct legs; their known membership gross of $42,800.00 is overlapping and is not unique movement. All three diagnostic windows extend beyond the supplied observation boundary and cannot be represented as complete rolling-window assessments."
    ],
    [
      "Two accounts meet the raw illustrative rapid-movement criterion. One has a supported invoice explanation, while the other remains a review lead. An additional account is not assessable because an amount is unreadable; it cannot be scored as a negative.",
      "Daily TM-01 and diagnostic rolling windows are separate measures. ReviewLedger retains four account review records with no human disposition recorded; the supported B invoice does not remove SR-002. ControlTotals preserves the failed monetary-completeness proposition even though row reconciliation passes."
    ],
    [
      "The synthetic source rows and criterion definitions in file 10 support the arithmetic and matches. The public typology references do not supply a regulatory threshold or evidence of wrongdoing for these fictional accounts."
    ],
    [
      "Review the unexplained match, preserve the invoice explanation without deleting the raw match, and repair the unreadable amount before rerunning the affected account."
    ],
    [
      "Synthetic rules are illustrative and are not regulatory thresholds.",
      "Account D has an unknown amount; total monetary completeness is not established.",
      "No opening balances or complete external flow paths are supplied.",
      "QA remains pending and no authorized human disposition is recorded."
    ]
  ],
  "as_of": "2026-09-02T04:00:00Z",
  "scope": "Fictional USD account legs with event instants from 2026-09-01T04:00:00Z inclusive to 2026-09-02T04:00:00Z exclusive. Extraction completeness is asserted only for the ten supplied rows; R10 has an unreadable amount.",
  "suite_id": "transaction-monitoring",
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
      "finding_id": "TM-F01",
      "proposal": "Obtain payment purpose and counterparties; refer to the authorized reviewer.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-002",
      "finding_id": "TM-F02",
      "proposal": "Document the explanation and seek human disposition; retain the rule hit.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-003",
      "finding_id": "TM-F03",
      "proposal": "Repair the source extract and recompute D before making an account conclusion.",
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
