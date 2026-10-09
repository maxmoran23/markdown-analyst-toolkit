# Transaction Monitoring Data Lineage — complete dashboard template

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
<title>Transaction Monitoring Data Lineage</title>
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
  "slug": "tm-data-lineage",
  "title": "Transaction Monitoring Data Lineage",
  "summary": "Reconcile source-to-monitoring transformations, population counts, currency totals, exceptions and late-change effects with a complete row-level lineage specimen.",
  "audience": "Monitoring analysts, scenario owners, data owners and independent control reviewers",
  "decision": "Can a reviewer reproduce which source records reached monitoring, which did not, and exactly how a correction changes the downstream assessment?",
  "palette": "slate",
  "as_of": "2026-09-02T12:00:00Z",
  "report_sections": [
    "Lineage conclusion and unresolved coverage",
    "Source scope, cutoffs and transformation contract",
    "Defects, exclusions and downstream consequences",
    "Source-to-canonical row lineage",
    "Stage controls and rerun impact",
    "Evidence and transformation provenance",
    "Proposed repair and reprocessing actions",
    "Limitations, quality gates and acceptance"
  ],
  "domain_tables": [
    {
      "name": "SourceRows",
      "title": "Immutable delivered source records",
      "columns": [
        "raw_row_id",
        "transaction_id",
        "account_id",
        "event_utc",
        "ingest_utc",
        "source_direction",
        "amount_text",
        "currency",
        "source_status",
        "source_version",
        "reversal_of",
        "evidence_ids"
      ],
      "rows": [
        [
          "X01",
          "TX01",
          "LA",
          "2026-09-01T13:00:00Z",
          "2026-09-01T13:05:00Z",
          "C",
          "6000.00",
          "USD",
          "P",
          "1",
          null,
          "LN-E01"
        ],
        [
          "X02",
          "TX02",
          "LA",
          "2026-09-01T14:00:00Z",
          "2026-09-01T14:05:00Z",
          "D",
          "5400.00",
          "USD",
          "P",
          "1",
          null,
          "LN-E01"
        ],
        [
          "X03",
          "TX01",
          "LA",
          "2026-09-01T13:00:00Z",
          "2026-09-01T15:00:00Z",
          "C",
          "6000.00",
          "USD",
          "P",
          "1",
          null,
          "LN-E01"
        ],
        [
          "X04",
          "TX03",
          "LB",
          "2026-09-01T13:00:00Z",
          "2026-09-01T13:05:00Z",
          "C",
          "5000.00",
          "USD",
          "P",
          "1",
          null,
          "LN-E01"
        ],
        [
          "X05",
          "TX04",
          "LB",
          "2026-09-01T14:00:00Z",
          "2026-09-01T14:05:00Z",
          "D",
          "4500.00",
          "USD",
          "P",
          "1",
          null,
          "LN-E01"
        ],
        [
          "X06",
          "TX05",
          "LC",
          "2026-09-01T13:00:00Z",
          "2026-09-01T13:05:00Z",
          "C",
          "2000.00",
          "USD",
          "P",
          "1",
          null,
          "LN-E01"
        ],
        [
          "X07",
          "TX05",
          "LC",
          "2026-09-01T13:00:00Z",
          "2026-09-01T13:06:00Z",
          "C",
          "2200.00",
          "USD",
          "P",
          "1",
          null,
          "LN-E01;LN-E02"
        ],
        [
          "X08",
          "TX06",
          "LC",
          "2026-09-01T14:00:00Z",
          "2026-09-01T14:05:00Z",
          "D",
          "1000.00",
          "USD",
          "P",
          "1",
          null,
          "LN-E01"
        ],
        [
          "X09",
          "TX07",
          "LD",
          "2026-09-01T13:00:00Z",
          "2026-09-01T13:05:00Z",
          "C",
          "7000.00",
          "USD",
          "N",
          "1",
          null,
          "LN-E01"
        ],
        [
          "X10",
          "TX08",
          "LE",
          "2026-09-01T13:00:00Z",
          "2026-09-01T13:05:00Z",
          "C",
          "3000.00",
          "USD",
          "P",
          "1",
          null,
          "LN-E01"
        ],
        [
          "X11",
          "TX09",
          "LE",
          "2026-09-01T14:00:00Z",
          "2026-09-01T14:05:00Z",
          "D",
          "3000.00",
          "USD",
          "R",
          "1",
          "TX08",
          "LN-E01;LN-E03"
        ],
        [
          "X12",
          "TX10",
          "LF",
          "2026-09-01T23:30:00Z",
          "2026-09-02T10:00:00Z",
          "C",
          "4000.00",
          "USD",
          "P",
          "1",
          null,
          "LN-E01;LN-E04"
        ],
        [
          "X13",
          "TX11",
          "LF",
          "2026-09-02T00:00:00Z",
          "2026-09-02T00:05:00Z",
          "D",
          "3600.00",
          "USD",
          "P",
          "1",
          null,
          "LN-E01"
        ],
        [
          "X14",
          "TX12",
          "LG",
          "2026-09-01T13:00:00Z",
          "2026-09-01T13:05:00Z",
          "C",
          "unreadable",
          "USD",
          "P",
          "1",
          null,
          "LN-E01;LN-E05"
        ],
        [
          "X15",
          "TX13",
          "LH",
          "2026-09-01T13:00:00Z",
          "2026-09-01T13:05:00Z",
          "C",
          "1000.00",
          "EUR",
          "P",
          "1",
          null,
          "LN-E01"
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
        "ingest_utc": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "UTC instant at which the source record became available to the monitoring feed. It controls run visibility separately from economic event-period inclusion."
        },
        "source_direction": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Unmodified source C or D code. The explicit mapping defines direction; unmapped codes require an exception and cannot be guessed."
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
        "source_status": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Original status code before mapping. P is posted, N pending and R a posted reversal under this particular source contract."
        },
        "source_version": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Source-declared record version as text. Later ingestion alone is not evidence of a later authoritative version when this value is unchanged."
        },
        "reversal_of": {
          "type": "text",
          "nullable": true,
          "unit": "text",
          "description": "Original source transaction key for a posted reversal. Null means no link supplied; do not fabricate a relation from equal and opposite amounts."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation."
        }
      },
      "grain": "one immutable raw delivered feed record, including later-unavailable and exceptional records",
      "report_section": 4
    },
    {
      "name": "FieldMappings",
      "title": "Source-to-canonical transformations and rejection behavior",
      "columns": [
        "mapping_id",
        "source_field",
        "target_field",
        "transformation",
        "failure_state",
        "test_locator",
        "evidence_ids"
      ],
      "rows": [
        [
          "MAP01",
          "transaction_id + account_id + source_version",
          "canonical identity",
          "Exact text tuple; currency and amount are compared payload, not identity",
          "CONFLICT if same tuple differs",
          "X06 and X07",
          "LN-E06"
        ],
        [
          "MAP02",
          "event_utc",
          "event instant",
          "Parse timezone-aware ISO timestamp; normalize UTC without changing instant",
          "UNPARSED_TIME",
          "X12 and X13 are previous ET business date",
          "LN-E06"
        ],
        [
          "MAP03",
          "source_direction",
          "direction",
          "C -\u003e CREDIT; D -\u003e DEBIT; no other mapping",
          "UNMAPPED_DIRECTION",
          "X01 C; X02 D",
          "LN-E06"
        ],
        [
          "MAP04",
          "amount_text",
          "amount",
          "Decimal nonnegative; retain original string; no thousands separator guessing",
          "UNPARSED_AMOUNT",
          "X14 unreadable",
          "LN-E06"
        ],
        [
          "MAP05",
          "source_status",
          "posting_state",
          "P -\u003e POSTED; N -\u003e PENDING; R -\u003e REVERSAL_POSTED",
          "UNMAPPED_STATUS",
          "X09 pending; X11 linked reversal",
          "LN-E06"
        ],
        [
          "MAP06",
          "currency",
          "currency",
          "Preserve uppercase ISO code; no conversion in this case",
          "UNKNOWN_CURRENCY",
          "X15 EUR stays EUR",
          "LN-E06"
        ],
        [
          "MAP07",
          "reversal_of",
          "reversal link",
          "Resolve original same-account transaction and exact amount/currency before paired exclusion",
          "UNRESOLVED_REVERSAL",
          "X11 refers TX08 at LE, USD 3000",
          "LN-E03;LN-E06"
        ],
        [
          "MAP08",
          "ingest_utc",
          "cutoff eligibility",
          "Include if ingest instant \u003c= run cutoff; apply event scope separately",
          "LATE_DEFERRED",
          "X12 appears only in rerun",
          "LN-E04;LN-E06"
        ]
      ],
      "formats": {},
      "primary_key": [
        "mapping_id"
      ],
      "column_contracts": {
        "mapping_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique source-to-canonical transformation identifier. It separates the mapping definition from actual row-level transformation outcomes."
        },
        "source_field": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Source column or explicit compound key consumed by a mapping. The original source text remains retrievable after transformation."
        },
        "target_field": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Named canonical concept produced by the mapping. A transformed concept may require several source columns and has its own validation gate."
        },
        "transformation": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Complete authored transformation rule for the supplied source. It specifies value mapping, precision and failure behavior without assuming vendor implementation."
        },
        "failure_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Required exception category when the mapping cannot be applied. It must propagate to downstream affected windows rather than silently dropping records."
        },
        "test_locator": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact fictional source examples that exercise the mapping. These are sufficient to reproduce this specimen, not a complete production validation dataset."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation."
        }
      },
      "grain": "one explicit source-to-canonical transformation with its failure branch",
      "report_section": 4
    },
    {
      "name": "LineageLedger",
      "title": "Every source row to one initial terminal state",
      "columns": [
        "lineage_id",
        "raw_row_id",
        "canonical_id",
        "terminal_state",
        "reason",
        "run_id",
        "evidence_ids"
      ],
      "rows": [
        [
          "LIN-X01",
          "X01",
          "CL01",
          "CANONICAL",
          "Unique readable posted leg available by initial cutoff",
          "RUN0",
          "LN-E01;LN-E06"
        ],
        [
          "LIN-X02",
          "X02",
          "CL02",
          "CANONICAL",
          "Unique readable posted leg available by initial cutoff",
          "RUN0",
          "LN-E01;LN-E06"
        ],
        [
          "LIN-X03",
          "X03",
          "CL01",
          "DUPLICATE",
          "Same economic tuple and payload as X01; later extraction metadata only",
          "RUN0",
          "LN-E01;LN-E06"
        ],
        [
          "LIN-X04",
          "X04",
          "CL03",
          "CANONICAL",
          "Unique readable posted leg available by initial cutoff",
          "RUN0",
          "LN-E01;LN-E06"
        ],
        [
          "LIN-X05",
          "X05",
          "CL04",
          "CANONICAL",
          "Unique readable posted leg available by initial cutoff",
          "RUN0",
          "LN-E01;LN-E06"
        ],
        [
          "LIN-X06",
          "X06",
          null,
          "CONFLICT",
          "Same TX05 identity; conflicting amount; neither selected",
          "RUN0",
          "LN-E01;LN-E06"
        ],
        [
          "LIN-X07",
          "X07",
          null,
          "CONFLICT",
          "Same TX05 identity; conflicting amount; neither selected",
          "RUN0",
          "LN-E01;LN-E02;LN-E06"
        ],
        [
          "LIN-X08",
          "X08",
          "CL05",
          "CANONICAL",
          "Unique readable posted leg available by initial cutoff",
          "RUN0",
          "LN-E01;LN-E06"
        ],
        [
          "LIN-X09",
          "X09",
          null,
          "PENDING",
          "Not posted at supplied status; retain outside posted ledger",
          "RUN0",
          "LN-E01;LN-E06"
        ],
        [
          "LIN-X10",
          "X10",
          null,
          "REVERSAL_PAIR",
          "Exact linked original and reversal preserved but netted out of external-flow scenario",
          "RUN0",
          "LN-E01;LN-E06"
        ],
        [
          "LIN-X11",
          "X11",
          null,
          "REVERSAL_PAIR",
          "Exact linked original and reversal preserved but netted out of external-flow scenario",
          "RUN0",
          "LN-E01;LN-E03;LN-E06"
        ],
        [
          "LIN-X12",
          "X12",
          null,
          "LATE_DEFERRED",
          "Event in period, ingestion after initial cutoff; add only in rerun",
          "RUN0",
          "LN-E01;LN-E04;LN-E06"
        ],
        [
          "LIN-X13",
          "X13",
          "CL06",
          "CANONICAL",
          "Unique readable posted leg available by initial cutoff",
          "RUN0",
          "LN-E01;LN-E06"
        ],
        [
          "LIN-X14",
          "X14",
          null,
          "UNPARSED_AMOUNT",
          "Posted amount cannot be recovered; LG blocked",
          "RUN0",
          "LN-E01;LN-E05;LN-E06"
        ],
        [
          "LIN-X15",
          "X15",
          "CL07",
          "CANONICAL",
          "Unique readable posted leg available by initial cutoff",
          "RUN0",
          "LN-E01;LN-E06"
        ]
      ],
      "formats": {},
      "primary_key": [
        "lineage_id"
      ],
      "column_contracts": {
        "lineage_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique link between a raw source row and its initial disposition. Each raw row appears once even when it maps to an already retained canonical leg."
        },
        "raw_row_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable."
        },
        "canonical_id": {
          "type": "text",
          "nullable": true,
          "unit": "identifier",
          "description": "Unique canonical output identifier or explicit null for a noncanonical row. A duplicate may point to an existing canonical identifier without adding a row."
        },
        "terminal_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exactly one initial row disposition for conservation. CANONICAL, DUPLICATE, CONFLICT, PENDING, REVERSAL_PAIR, LATE_DEFERRED and UNPARSED_AMOUNT partition the source."
        },
        "reason": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Specific evidence-backed reason for a state or transition. It identifies the relevant row, rule or missing fact rather than a generic compliance label."
        },
        "run_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Snapshot identity with a fixed ingestion cutoff. RUN0 and RUN1 differ in available source information; neither is silently overwritten."
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
          "table": "SourceRows",
          "references": [
            "raw_row_id"
          ]
        }
      ],
      "grain": "one raw source row and its initial RUN0 terminal disposition",
      "report_section": 4
    },
    {
      "name": "CanonicalOutput",
      "title": "Known unique posted legs at initial cutoff",
      "columns": [
        "canonical_id",
        "raw_row_id",
        "transaction_id",
        "account_id",
        "event_utc",
        "direction",
        "amount",
        "currency",
        "run_id",
        "evidence_ids"
      ],
      "rows": [
        [
          "CL01",
          "X01",
          "TX01",
          "LA",
          "2026-09-01T13:00:00Z",
          "CREDIT",
          6000.0,
          "USD",
          "RUN0",
          "LN-E01"
        ],
        [
          "CL02",
          "X02",
          "TX02",
          "LA",
          "2026-09-01T14:00:00Z",
          "DEBIT",
          5400.0,
          "USD",
          "RUN0",
          "LN-E01"
        ],
        [
          "CL03",
          "X04",
          "TX03",
          "LB",
          "2026-09-01T13:00:00Z",
          "CREDIT",
          5000.0,
          "USD",
          "RUN0",
          "LN-E01"
        ],
        [
          "CL04",
          "X05",
          "TX04",
          "LB",
          "2026-09-01T14:00:00Z",
          "DEBIT",
          4500.0,
          "USD",
          "RUN0",
          "LN-E01"
        ],
        [
          "CL05",
          "X08",
          "TX06",
          "LC",
          "2026-09-01T14:00:00Z",
          "DEBIT",
          1000.0,
          "USD",
          "RUN0",
          "LN-E01"
        ],
        [
          "CL06",
          "X13",
          "TX11",
          "LF",
          "2026-09-02T00:00:00Z",
          "DEBIT",
          3600.0,
          "USD",
          "RUN0",
          "LN-E01"
        ],
        [
          "CL07",
          "X15",
          "TX13",
          "LH",
          "2026-09-01T13:00:00Z",
          "CREDIT",
          1000.0,
          "EUR",
          "RUN0",
          "LN-E01"
        ]
      ],
      "formats": {
        "amount": "#,##0.00"
      },
      "primary_key": [
        "canonical_id"
      ],
      "column_contracts": {
        "canonical_id": {
          "type": "text",
          "nullable": true,
          "unit": "identifier",
          "description": "Unique canonical output identifier or explicit null for a noncanonical row. A duplicate may point to an existing canonical identifier without adding a row."
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
        "run_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Snapshot identity with a fixed ingestion cutoff. RUN0 and RUN1 differ in available source information; neither is silently overwritten."
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
          "table": "SourceRows",
          "references": [
            "raw_row_id"
          ]
        }
      ],
      "grain": "one known unique posted account leg available at RUN0 and surviving declared exclusions",
      "report_section": 5
    },
    {
      "name": "StageControls",
      "title": "Counts and known amounts by stage and currency",
      "columns": [
        "control_id",
        "stage",
        "currency",
        "row_count",
        "known_credit_total",
        "known_debit_total",
        "unknown_amount_count",
        "interpretation",
        "evidence_ids"
      ],
      "rows": [
        [
          "LC01",
          "Delivered raw",
          "USD",
          14,
          35200,
          17500,
          1,
          "Raw contains duplicate, conflicting alternatives, pending and reversal; not economic total",
          "LN-E01"
        ],
        [
          "LC02",
          "Delivered raw",
          "EUR",
          1,
          1000,
          0,
          0,
          "Separate currency; not added to USD",
          "LN-E01"
        ],
        [
          "LC03",
          "RUN0 canonical",
          "USD",
          6,
          11000,
          14500,
          0,
          "Known partial posted population; LC conflict, LF late, LG unknown remain blocked",
          "LN-E01;LN-E06"
        ],
        [
          "LC04",
          "RUN0 canonical",
          "EUR",
          1,
          1000,
          0,
          0,
          "Preserved EUR leg; USD scenario exclusion separately disclosed",
          "LN-E01;LN-E06"
        ],
        [
          "LC05",
          "RUN1 canonical",
          "USD",
          7,
          15000,
          14500,
          0,
          "Adds X12 USD 4000 credit; unresolved conflict and parse defect remain",
          "LN-E04;LN-E06"
        ],
        [
          "LC06",
          "RUN1 canonical",
          "EUR",
          1,
          1000,
          0,
          0,
          "EUR unchanged",
          "LN-E01;LN-E06"
        ]
      ],
      "formats": {
        "known_credit_total": "#,##0.00",
        "known_debit_total": "#,##0.00"
      },
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
        "stage": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Named source or canonical pipeline layer and run. Its grain must be checked before interpreting totals because raw rows include non-economic duplicates."
        },
        "currency": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount."
        },
        "row_count": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Number of records in the named stage and currency. This is counted independently of known amounts and can include unreadable monetary rows."
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
        "unknown_amount_count": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Count of stage records whose amount is not numeric. It does not measure uncertain amount ranges or conflicted values unless explicitly stated."
        },
        "interpretation": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Specific limitation on the control total, including duplicate/conflict effects or incomplete economic coverage. It travels with the number in every output."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation."
        }
      },
      "grain": "one pipeline layer, run and currency control population",
      "report_section": 5
    },
    {
      "name": "RunImpact",
      "title": "Account assessment changes after known late arrival",
      "columns": [
        "impact_id",
        "account_id",
        "currency",
        "run0_credit",
        "run0_debit",
        "run0_state",
        "run1_credit",
        "run1_debit",
        "run1_state",
        "change_reason",
        "evidence_ids"
      ],
      "rows": [
        [
          "IMP-A",
          "LA",
          "USD",
          6000,
          5400,
          "MATCH",
          6000,
          5400,
          "MATCH",
          "No source change",
          "LN-E01;LN-E06"
        ],
        [
          "IMP-B",
          "LB",
          "USD",
          5000,
          4500,
          "MATCH",
          5000,
          4500,
          "MATCH",
          "No source change",
          "LN-E01;LN-E06"
        ],
        [
          "IMP-C",
          "LC",
          "USD",
          0,
          1000,
          "NOT_ASSESSABLE",
          0,
          1000,
          "NOT_ASSESSABLE",
          "TX05 conflict unresolved; credit zero means known subtotal only",
          "LN-E02;LN-E06"
        ],
        [
          "IMP-D",
          "LD",
          "USD",
          0,
          0,
          "NO_POSTED_ACTIVITY",
          0,
          0,
          "NO_POSTED_ACTIVITY",
          "Pending source retained; no posted leg",
          "LN-E01;LN-E06"
        ],
        [
          "IMP-E",
          "LE",
          "USD",
          0,
          0,
          "REVERSAL_PAIR_EXCLUDED",
          0,
          0,
          "REVERSAL_PAIR_EXCLUDED",
          "Original and reversal retained outside illustrative flow totals",
          "LN-E03;LN-E06"
        ],
        [
          "IMP-F",
          "LF",
          "USD",
          0,
          3600,
          "NOT_ASSESSABLE",
          4000,
          3600,
          "NO_MATCH",
          "Late credit repaired; ratio .90 but 4000 below illustrative 5000 minimum",
          "LN-E04;LN-E06"
        ],
        [
          "IMP-G",
          "LG",
          "USD",
          0,
          0,
          "NOT_ASSESSABLE",
          0,
          0,
          "NOT_ASSESSABLE",
          "Unknown posted credit remains; zeros are known subtotals",
          "LN-E05;LN-E06"
        ],
        [
          "IMP-H",
          "LH",
          "EUR",
          1000,
          0,
          "CURRENCY_EXCLUDED",
          1000,
          0,
          "CURRENCY_EXCLUDED",
          "USD-only rule; EUR preserved in lineage",
          "LN-E01;LN-E06"
        ]
      ],
      "formats": {
        "run0_credit": "#,##0.00",
        "run0_debit": "#,##0.00",
        "run1_credit": "#,##0.00",
        "run1_debit": "#,##0.00"
      },
      "primary_key": [
        "impact_id"
      ],
      "column_contracts": {
        "impact_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable account/currency change-comparison key. It connects prior and rerun states without presenting the new state as the original conclusion."
        },
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
        "run0_credit": {
          "type": "number",
          "nullable": false,
          "unit": "row currency",
          "description": "Known initial-run credit subtotal in row currency. A zero on a blocked account is a known subtotal only and cannot prove no credits exist."
        },
        "run0_debit": {
          "type": "number",
          "nullable": false,
          "unit": "row currency",
          "description": "Known initial-run debit subtotal in row currency. Reversal exclusions and missing records are documented separately."
        },
        "run0_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Initial downstream assessment after all source defects known to the case are propagated. A known unavailable event makes the account incomplete."
        },
        "run1_credit": {
          "type": "number",
          "nullable": false,
          "unit": "row currency",
          "description": "Known rerun credit subtotal after the declared late event becomes available. Unrelated unresolved defects are not repaired by this increase."
        },
        "run1_debit": {
          "type": "number",
          "nullable": false,
          "unit": "row currency",
          "description": "Known rerun debit subtotal under the same scope and transformation rules. Its equality to RUN0 is a checked result rather than an assumption."
        },
        "run1_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Downstream assessment at the later cutoff with the same illustrative predicates. State changes require an explicit source or criteria delta."
        },
        "change_reason": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact source delta explaining a before/after result. It distinguishes improved completeness from changed risk or changed threshold."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation."
        }
      },
      "grain": "one account and currency compared across RUN0 and RUN1",
      "report_section": 5
    },
    {
      "name": "ExceptionRegister",
      "title": "Specific defects and required repair evidence",
      "columns": [
        "exception_id",
        "account_id",
        "source_rows",
        "exception_type",
        "affected_claim",
        "required_evidence",
        "repair_state",
        "evidence_ids"
      ],
      "rows": [
        [
          "EX01",
          "LC",
          "X06;X07",
          "CONFLICT",
          "Credit amount and LC rule outcome",
          "Authoritative TX05 version history and amount; do not choose maximum",
          "OPEN",
          "LN-E02"
        ],
        [
          "EX02",
          "LF",
          "X12",
          "LATE_ARRIVAL",
          "Initial completeness and LF timing",
          "RUN1 ingest receipt and complete lag population",
          "RERUN_REPRODUCED",
          "LN-E04"
        ],
        [
          "EX03",
          "LG",
          "X14",
          "UNPARSED_AMOUNT",
          "Credit total and LG rule outcome",
          "Corrected signed source extract and source amount control",
          "OPEN",
          "LN-E05"
        ],
        [
          "EX04",
          "LE",
          "X10;X11",
          "REVERSAL_TREATMENT",
          "Difference between posting gross and illustrative external flow",
          "Exact reversal link, currency and amount, plus stated exclusion convention",
          "DOCUMENTED_ONLY",
          "LN-E03;LN-E06"
        ]
      ],
      "formats": {},
      "primary_key": [
        "exception_id"
      ],
      "column_contracts": {
        "exception_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique source-defect or controlled-treatment record. Exceptions retain their evidence and cannot be closed merely because a rerun finished."
        },
        "account_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge."
        },
        "source_rows": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited raw-row keys contributing to the exception. Each referenced row remains in the immutable source and lineage registers."
        },
        "exception_type": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Specific conflict, late-arrival, unreadable-amount or reversal-treatment category. Categories drive different repair and retest requirements."
        },
        "affected_claim": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Analytical statement that cannot be supported, or changes meaning, because of the exception. This connects technical defects to monitoring consequences."
        },
        "required_evidence": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Concrete source-owner evidence needed to resolve or verify the exception. A verbal assurance does not substitute for the named record."
        },
        "repair_state": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Actual evidence state of repair in the specimen. OPEN remains unresolved, RERUN_REPRODUCED verifies the illustrated rerun, DOCUMENTED_ONLY is not operational acceptance."
        },
        "evidence_ids": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation."
        }
      },
      "grain": "one specific defect or documented controlled treatment and its repair evidence",
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
          "LN-E01",
          "Authored fictional case record",
          "2026-09-02",
          "FULL_TEXT_IN_FILE_10",
          "10-worked-example.md, SourceRows X01-X15; source manifest",
          "Fictional delivered feed",
          "Supports only the stated fictional proposition; no external subject fact or institutional approval"
        ],
        [
          "LN-E02",
          "Authored fictional case record",
          "2026-09-02",
          "FULL_TEXT_IN_FILE_10",
          "10-worked-example.md, TX05 conflict declaration",
          "Fictional conflict notice",
          "Supports only the stated fictional proposition; no external subject fact or institutional approval"
        ],
        [
          "LN-E03",
          "Authored fictional case record",
          "2026-09-02",
          "FULL_TEXT_IN_FILE_10",
          "10-worked-example.md, TX08/TX09 reversal declaration",
          "Fictional exact reversal link",
          "Supports only the stated fictional proposition; no external subject fact or institutional approval"
        ],
        [
          "LN-E04",
          "Authored fictional case record",
          "2026-09-02",
          "FULL_TEXT_IN_FILE_10",
          "10-worked-example.md, X12 cutoff declaration and RUN1 receipt",
          "Fictional late-arrival notice",
          "Supports only the stated fictional proposition; no external subject fact or institutional approval"
        ],
        [
          "LN-E05",
          "Authored fictional case record",
          "2026-09-02",
          "FULL_TEXT_IN_FILE_10",
          "10-worked-example.md, X14 parse-defect declaration",
          "Fictional unreadable amount",
          "Supports only the stated fictional proposition; no external subject fact or institutional approval"
        ],
        [
          "LN-E06",
          "Authored fictional case record",
          "2026-09-02",
          "FULL_TEXT_IN_FILE_10",
          "10-worked-example.md, FieldMappings, run cutoffs and illustrative TM-01 predicates",
          "Authored transformation and downstream rule",
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
          "LQ01",
          "Initial terminal conservation",
          "15 = 7 + 1 + 2 + 1 + 2 + 1 + 1",
          "15 = 7 + 1 + 2 + 1 + 2 + 1 + 1",
          "PASS",
          "Authored specimen arithmetic; independent operational reviewer not supplied",
          "LN-E01;LN-E06"
        ],
        [
          "LQ02",
          "RUN1 known USD gross",
          "29500.00",
          "29500.00",
          "PASS",
          "Authored specimen arithmetic; independent operational reviewer not supplied",
          "LN-E01;LN-E04"
        ],
        [
          "LQ03",
          "Distinct currencies",
          "USD and EUR separate",
          "USD and EUR separate",
          "PASS",
          "Authored specimen arithmetic; independent operational reviewer not supplied",
          "LN-E01"
        ],
        [
          "LQ04",
          "Conflict not selected",
          "X06 and X07 both quarantined",
          "X06 and X07 both quarantined",
          "PASS",
          "Authored specimen arithmetic; independent operational reviewer not supplied",
          "LN-E02"
        ],
        [
          "LQ05",
          "Independent acceptance",
          "Not supplied",
          "Not supplied",
          "NOT RECORDED",
          "Authored specimen arithmetic; independent operational reviewer not supplied",
          "LN-E06"
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
      "id": "LN-F01",
      "title": "Conflicting versions block LC",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "LN-E01",
        "LN-E02"
      ],
      "detail": "X06 and X07 share the TX05 identity but disagree between USD 2000 and USD 2200; neither is selected. LC remains not assessable.",
      "recommendation": "Obtain an authoritative version history, resolve TX05 and rerun every affected window."
    },
    {
      "id": "LN-F02",
      "title": "Known late credit changes LF assessment",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "LN-E01",
        "LN-E04",
        "LN-E06"
      ],
      "detail": "RUN1 adds X12 USD 4000 credit. LF changes from not assessable to no match because .90 satisfies the ratio but USD 4000 fails the credit minimum.",
      "recommendation": "Preserve RUN0 and RUN1 and verify the wider lag population before accepting complete coverage."
    },
    {
      "id": "LN-F03",
      "title": "Unreadable posted credit remains unresolved",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "LN-E01",
        "LN-E05"
      ],
      "detail": "X14 amount is unknown; LG contributes no known amount but cannot be treated as a zero-activity negative.",
      "recommendation": "Request corrected source evidence and reconcile the replacement to source totals."
    }
  ],
  "evidence": [
    {
      "id": "LN-E01",
      "title": "Fictional delivered feed",
      "locator": "10-worked-example.md, SourceRows X01-X15; source manifest",
      "claim_class": "Observed"
    },
    {
      "id": "LN-E02",
      "title": "Fictional conflict notice",
      "locator": "10-worked-example.md, TX05 conflict declaration",
      "claim_class": "Observed"
    },
    {
      "id": "LN-E03",
      "title": "Fictional exact reversal link",
      "locator": "10-worked-example.md, TX08/TX09 reversal declaration",
      "claim_class": "Observed"
    },
    {
      "id": "LN-E04",
      "title": "Fictional late-arrival notice",
      "locator": "10-worked-example.md, X12 cutoff declaration and RUN1 receipt",
      "claim_class": "Observed"
    },
    {
      "id": "LN-E05",
      "title": "Fictional unreadable amount",
      "locator": "10-worked-example.md, X14 parse-defect declaration",
      "claim_class": "Observed"
    },
    {
      "id": "LN-E06",
      "title": "Authored transformation and downstream rule",
      "locator": "10-worked-example.md, FieldMappings, run cutoffs and illustrative TM-01 predicates",
      "claim_class": "Observed"
    }
  ],
  "metrics": [
    {
      "label": "Delivered rows",
      "value": 15,
      "method": "Count X01-X15 including post-cutoff record",
      "format": "#,##0"
    },
    {
      "label": "Initial canonical rows",
      "value": 7,
      "method": "Six USD plus one EUR known unique posted leg",
      "format": "#,##0"
    },
    {
      "label": "Rerun canonical rows",
      "value": 8,
      "method": "RUN0 seven plus late X12; unresolved defects unchanged",
      "format": "#,##0"
    },
    {
      "label": "RUN1 known USD gross",
      "value": 29500,
      "method": "USD 15000 credits plus USD 14500 debits; excludes unknown/conflicting amounts",
      "format": "#,##0"
    }
  ],
  "limitations": [
    "Source-row reconciliation does not establish a complete economic monetary total.",
    "The posting reversal pair is excluded only by this authored illustrative flow convention; actual monitoring designs may retain reversal activity.",
    "RUN1 repairs one known late event, not an independently proven complete late-arrival population.",
    "EUR remains separate and is outside the illustrative USD rule."
  ],
  "report_narrative": [
    [
      "Every one of fifteen delivered rows has an explicit initial lineage state. Seven known rows reach RUN0; eight reach RUN1 after a late credit. Two accounts remain blocked by unresolved source defects."
    ],
    [
      "The event review period is Sep 01, 2026 12:00 AM ET to Sep 02, 2026 12:00 AM ET exclusive. RUN0 ingestion cutoff is Sep 02, 2026 12:00 AM ET. RUN1 cutoff is Sep 02, 2026 8:00 AM ET. The delivered set intentionally includes a row unavailable at RUN0."
    ],
    [
      "TX05 conflicts between two same-version amounts, X14 is unreadable, and X12 arrives after the first cutoff. Reversal and pending records are controlled exclusions, not discarded evidence."
    ],
    [
      "SourceRows contains fifteen rows; FieldMappings defines eight transformations; LineageLedger gives every raw row one initial terminal state; CanonicalOutput retains seven RUN0 rows. One exact duplicate points to CL01 without increasing totals."
    ],
    [
      "Initial USD canonical movement is $25,500.00; RUN1 is $29,500.00, a $4,000.00 credit increase. EUR $1,000.00 remains separate. LF becomes a complete no-match under the illustrative credit minimum while LC and LG remain blocked. RunImpact preserves eight account/currency records."
    ],
    [
      "All row facts and controls are fictional. Public monitoring examination guidance supplies context for checking data and filtering; it does not establish a required transformation or threshold here."
    ],
    [
      "Resolve TX05; recover X14; review all known late arrivals; retain before/after counts, amounts and affected windows. No operational reprocessing or rule change is performed by this package."
    ],
    [
      "Count reconciliation succeeds while economic monetary completeness remains unresolved. The demonstrated pipeline is a synthetic review design, not production data assurance or monitoring validation."
    ]
  ],
  "conclusion": "Every one of fifteen delivered rows has an explicit initial lineage state. Seven known rows reach RUN0; eight reach RUN1 after a late credit. Two accounts remain blocked by unresolved source defects.",
  "suite_id": "tm-data-lineage",
  "version": "1.2.0",
  "notice": "Synthetic worked example. Fictional records. Not a completed operational review.",
  "scope": "Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.",
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
      "finding_id": "LN-F01",
      "proposal": "Obtain an authoritative version history, resolve TX05 and rerun every affected window.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-002",
      "finding_id": "LN-F02",
      "proposal": "Preserve RUN0 and RUN1 and verify the wider lag population before accepting complete coverage.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-003",
      "finding_id": "LN-F03",
      "proposal": "Request corrected source evidence and reconcile the replacement to source totals.",
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
