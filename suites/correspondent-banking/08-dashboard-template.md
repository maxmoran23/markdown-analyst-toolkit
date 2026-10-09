# Correspondent Banking — complete dashboard template

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
<title>Correspondent Banking</title>
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
  "slug": "correspondent-banking",
  "title": "Correspondent Banking",
  "summary": "Review respondent-bank relationships, nested access and payment-information gaps using a bounded, risk-based evidence record.",
  "audience": "Analysts preparing generic correspondent relationship review materials",
  "decision": "Which relationship-specific transparency and due-diligence gaps need authorized follow-up before a human disposition?",
  "palette": "teal",
  "report_sections": [
    "Correspondent relationship decision brief",
    "Scope, legal applicability and payment population",
    "Material relationship and transparency findings",
    "Respondent relationship assessment",
    "Payment transparency and nested access",
    "Evidence and criterion provenance",
    "Proposed relationship-specific actions",
    "Limitations, quality checks and human disposition"
  ],
  "domain_tables": [
    {
      "name": "RelationshipReview",
      "columns": [
        "respondent_id",
        "respondent_name",
        "services",
        "nested_declared",
        "physical_presence",
        "regulated_affiliate",
        "control_evidence",
        "assessment",
        "evidence_ids"
      ],
      "rows": [
        [
          "CB01",
          "Cedar Basin Bank",
          "Commercial payments and NB-01 nested access",
          "YES",
          "DOCUMENTED",
          "NOT_ASSESSED",
          "Policy and limited operating test supplied",
          "LIMITED_SUPPORT",
          "SYN-001;SYN-005;SYN-006"
        ],
        [
          "CB02",
          "Delta Reach Bank",
          "Commercial and remittance payments; no declared nested access",
          "NO",
          "UNKNOWN",
          "UNKNOWN",
          "Questionnaire only; operating test absent",
          "FOLLOW_UP",
          "SYN-002;SYN-005"
        ],
        [
          "CB03",
          "Islet Digital Bank",
          "Own treasury payments",
          "NO",
          "NONE_REPORTED",
          "DOCUMENTED",
          "Affiliation and consolidated-supervision statement supplied",
          "LEGAL_CLASSIFICATION_REVIEW",
          "SYN-003;SYN-005"
        ],
        [
          "CB04",
          "Orchard Plain Bank",
          "Own treasury payments",
          "NO",
          "DOCUMENTED",
          "NOT_ASSESSED",
          "Scoped control test supplied",
          "LIMITED_SUPPORT",
          "SYN-004;SYN-005"
        ]
      ]
    },
    {
      "name": "PaymentReview",
      "columns": [
        "payment_id",
        "respondent_id",
        "underlying_bank_id",
        "amount",
        "currency",
        "initial_missing",
        "cutoff_missing",
        "nested_state",
        "review_state",
        "evidence_ids"
      ],
      "rows": [
        [
          "P01",
          "CB01",
          "NONE_DECLARED",
          100000,
          "USD",
          "NONE",
          "NONE",
          "NOT_INDICATED",
          "COMPLETE",
          "SYN-005"
        ],
        [
          "P02",
          "CB01",
          "NB-01",
          50000,
          "USD",
          "originator_identifier",
          "NONE",
          "DISCLOSED",
          "REPAIRED",
          "SYN-005;SYN-006"
        ],
        [
          "P03",
          "CB01",
          "NB-01",
          25000,
          "USD",
          "NONE",
          "NONE",
          "DISCLOSED",
          "COMPLETE",
          "SYN-005"
        ],
        [
          "P04",
          "CB01",
          "NONE_DECLARED",
          25000,
          "USD",
          "NONE",
          "NONE",
          "NOT_INDICATED",
          "COMPLETE",
          "SYN-005"
        ],
        [
          "P05",
          "CB02",
          "NB-02",
          60000,
          "USD",
          "originator_identifier",
          "originator_identifier",
          "UNDECLARED_OBSERVED",
          "GAP_OPEN",
          "SYN-005"
        ],
        [
          "P06",
          "CB02",
          "NB-02",
          40000,
          "USD",
          "NONE",
          "NONE",
          "UNDECLARED_OBSERVED",
          "COMPLETE",
          "SYN-005"
        ],
        [
          "P07",
          "CB02",
          "NONE_DECLARED",
          20000,
          "USD",
          "beneficiary_identifier",
          "beneficiary_identifier",
          "NOT_INDICATED",
          "GAP_OPEN",
          "SYN-005"
        ],
        [
          "P08",
          "CB03",
          "NONE_DECLARED",
          30000,
          "USD",
          "NONE",
          "NONE",
          "NOT_INDICATED",
          "COMPLETE",
          "SYN-005"
        ],
        [
          "P09",
          "CB03",
          "NONE_DECLARED",
          70000,
          "USD",
          "NONE",
          "NONE",
          "NOT_INDICATED",
          "COMPLETE",
          "SYN-005"
        ],
        [
          "P10",
          "CB04",
          "NONE_DECLARED",
          80000,
          "USD",
          "NONE",
          "NONE",
          "NOT_INDICATED",
          "COMPLETE",
          "SYN-005"
        ]
      ],
      "formats": {
        "amount": "#,##0.00"
      }
    }
  ],
  "findings": [
    {
      "id": "CB-F01",
      "title": "CB02 has undeclared nested access and open field gaps",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-002",
        "SYN-005"
      ],
      "detail": "Two NB-02 payments total USD 100,000; P05 and P07 retain missing illustrative identity fields totaling USD 80,000 at cutoff.",
      "recommendation": "Clarify NB-02 access authority and obtain missing fields through an authorized process."
    },
    {
      "id": "CB-F02",
      "title": "CB01 historical field gap is repaired",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001",
        "SYN-005",
        "SYN-006"
      ],
      "detail": "P02 initially lacked originator identifier; a linked Sep 09 repair supplies it before cutoff.",
      "recommendation": "Preserve the initial defect and review whether the repair process needs further testing."
    },
    {
      "id": "CB-F03",
      "title": "CB03 requires scoped legal classification",
      "severity": "MEDIUM",
      "confidence": "MODERATE",
      "claim_class": "Inferred",
      "evidence_ids": [
        "SYN-003"
      ],
      "detail": "No separate physical presence is reported, but affiliation and consolidated-supervision support are supplied.",
      "recommendation": "Assess the applicable regulated-affiliate definition; do not infer prohibition or approval."
    },
    {
      "id": "CB-F04",
      "title": "CB04 provides a supported ordinary-activity control",
      "severity": "LOW",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-004",
        "SYN-005"
      ],
      "detail": "P10 is a complete own-treasury payment within the stated service scope.",
      "recommendation": "Retain in the population and seek ordinary human disposition."
    }
  ],
  "evidence": [
    {
      "id": "SYN-001",
      "title": "Fictional respondent profile CB01",
      "locator": "10-worked-example.md, profile CB01",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-002",
      "title": "Fictional respondent profile CB02",
      "locator": "10-worked-example.md, profile CB02",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-003",
      "title": "Fictional respondent profile CB03",
      "locator": "10-worked-example.md, profile CB03",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-004",
      "title": "Fictional respondent profile CB04",
      "locator": "10-worked-example.md, profile CB04",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-005",
      "title": "Fictional complete initial payment population",
      "locator": "10-worked-example.md, payment rows P01 through P10 and role note",
      "claim_class": "Observed"
    },
    {
      "id": "SYN-006",
      "title": "Fictional P02 repair",
      "locator": "10-worked-example.md, repair R01",
      "claim_class": "Observed"
    },
    {
      "id": "REF-FATF-CB",
      "title": "FATF correspondent banking guidance, October 2016",
      "locator": "https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Guidance-Correspondent-Banking-Services.pdf; paragraphs 1\u20134, 9",
      "claim_class": "Observed"
    },
    {
      "id": "REF-SHELL",
      "title": "FFIEC foreign shell-bank manual section",
      "locator": "https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/12; applicability in 02",
      "claim_class": "Observed"
    }
  ],
  "metrics": [
    {
      "label": "Payments reviewed",
      "value": 10,
      "method": "Ten distinct payment IDs P01\u2013P10.",
      "format": "#,##0"
    },
    {
      "label": "Reviewed value USD",
      "value": 500000,
      "format": "$#,##0.00",
      "method": "Sum all ten USD payment amounts."
    },
    {
      "label": "Cutoff gap count rate",
      "value": 20.0,
      "format": "0.0\"%\"",
      "method": "P05 and P07 / 10 payments \u00d7 100."
    },
    {
      "label": "Cutoff gap value USD",
      "value": 80000,
      "format": "$#,##0.00",
      "method": "P05 60,000 + P07 20,000; 16.0% of USD 500,000."
    }
  ],
  "limitations": [
    "All respondent profiles, payments and repairs are fictional.",
    "The four-field criterion is illustrative and does not establish legal message compliance.",
    "CB02 physical presence and control operation are not established.",
    "No relationship approval, restriction, communication or human disposition is recorded.",
    "Nested-role uncertainty must use UNRESOLVED; four-field COMPLETE is not a resolved nesting classification."
  ],
  "metadata": {
    "conclusion": "CB02 needs targeted follow-up on USD 100,000 of undeclared nested activity and two open field gaps totaling USD 80,000. CB01 has one repaired historical defect. CB03 requires legal classification review, and CB04 supplies the ordinary-activity control."
  },
  "report_narrative": [
    [
      "CB02 needs targeted follow-up on USD 100,000 of undeclared nested activity and two open field gaps totaling USD 80,000. CB01 has one repaired historical defect. CB03 requires legal classification review, and CB04 supplies the ordinary-activity control."
    ],
    [
      "The fictional review covers four respondents and ten USD payments totaling USD 500,000 through Sep 10, 2026 5:00 PM ET. The four-field criterion is an analytic convention, not a full legal compliance test."
    ],
    [
      "CB-F01 identifies two distinct questions at CB02: service authority and current message fields. CB-F02 preserves an initial defect after repair. CB-F03 keeps regulated-affiliate classification open. CB-F04 retains ordinary treasury activity."
    ],
    [
      "RelationshipReview separates unknown presence at CB02 from reported absence plus affiliate support at CB03. Neither condition produces an automatic shell-bank or exit conclusion."
    ],
    [
      "PaymentReview records three initial gaps, USD 130,000 and 30.0% by count. After the P02 repair, two gaps remain, USD 80,000 and 20.0% by count. Four nested payments total USD 175,000; USD 100,000 was undeclared at the relevant dates.",
      "The separate P06 role-uncertainty variation in file 10 leaves baseline metrics unchanged until explicitly selected; its UNRESOLVED state is distinct from field completeness and from confirmed nested activity."
    ],
    [
      "SYN-001 through SYN-004 support the four relationship profiles. SYN-005 supplies every initial payment and its role; SYN-006 supplies the single pre-cutoff repair. The two REF sources provide bounded methodological context."
    ],
    [
      "Propose CB02 access clarification and field completion, CB01 process review, CB03 legal classification and ordinary CB04 review. No action has been issued or executed."
    ],
    [
      "All respondent profiles, payments and repairs are fictional.",
      "The four-field criterion is illustrative and does not establish legal message compliance.",
      "CB02 physical presence and control operation are not established.",
      "No relationship approval, restriction, communication or human disposition is recorded.",
      "Actual QA outcomes and a named human disposition remain to be recorded.",
      "Nested-role uncertainty must use UNRESOLVED; four-field COMPLETE is not a resolved nesting classification."
    ]
  ],
  "as_of": "2026-09-10 5:00 PM ET",
  "scope": "Four fictional respondent profiles, ten USD payments and one linked repair through Sep 10, 2026 5:00 PM ET. Four-field completeness is an illustrative analytic criterion.",
  "suite_id": "correspondent-banking",
  "version": "1.1.0",
  "notice": "Synthetic worked example. Fictional records. Not a completed operational review.",
  "conclusion": "CB02 needs targeted follow-up on USD 100,000 of undeclared nested activity and two open field gaps totaling USD 80,000. CB01 has one repaired historical defect. CB03 requires legal classification review, and CB04 supplies the ordinary-activity control.",
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
      "finding_id": "CB-F01",
      "proposal": "Clarify NB-02 access authority and obtain missing fields through an authorized process.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-002",
      "finding_id": "CB-F02",
      "proposal": "Preserve the initial defect and review whether the repair process needs further testing.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-003",
      "finding_id": "CB-F03",
      "proposal": "Assess the applicable regulated-affiliate definition; do not infer prohibition or approval.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-004",
      "finding_id": "CB-F04",
      "proposal": "Retain in the population and seek ordinary human disposition.",
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
