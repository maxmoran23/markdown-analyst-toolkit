# Alert Adjudication Quality Review — complete dashboard template

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
<title>Alert Adjudication Quality Review</title>
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
  "slug": "alert-qa",
  "title": "Alert Adjudication Quality Review",
  "summary": "Reperform case reasoning, distinguish demonstrated defects from missing reviewability, calibrate independent judgments and define evidence-based remediation closure.",
  "audience": "Alert quality reviewers, investigation leads and calibration facilitators",
  "decision": "Which supplied adjudications meet the applicable quality rubric, which need substantive repair, and which cannot yet be assessed?",
  "palette": "slate",
  "as_of": "2026-09-30T17:00:00-04:00",
  "scope": "Twelve deliberately selected fictional case packets, two original blind reviewers each, supplied illustrative policy CP-QA-1 and a separate consensus round. No random sample or population estimate.",
  "report_sections": [
    "Quality decision and open gates",
    "Scope, supplied criteria and review design",
    "Material and nonmaterial findings",
    "Case packets and original review votes",
    "Criteria, defects, calibration and remediation",
    "Evidence and decision-time provenance",
    "Proposed repairs and closure tests",
    "Quality checks, limitations and human disposition"
  ],
  "domain_tables": [
    {
      "name": "CasePackets",
      "columns": [
        "case_id",
        "case_topic",
        "raw_packet",
        "consensus",
        "rationale",
        "evidence_ids"
      ],
      "column_contracts": {
        "case_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique case packet in this deliberately selected calibration set."
        },
        "case_topic": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Short topic, not an allegation."
        },
        "raw_packet": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Complete bounded fictional facts supplied for this quality question."
        },
        "consensus": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Adjudicated quality status under fixture policy.",
          "enum": [
            "ACCEPT",
            "REWORK",
            "INSUFFICIENT"
          ]
        },
        "rationale": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Case-specific quality reasoning, distinct from underlying case disposition."
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
          "C01",
          "Routine pass-through explanation",
          "Posted debit 1000; invoice 1000; beneficiary and delivery match; counterevidence considered.",
          "ACCEPT",
          "No material reasoning defect on supplied packet.",
          "Q01;Q14;Q15"
        ],
        [
          "C02",
          "Omitted contrary invoice",
          "Investigator described no business support; packet includes matched invoice 2000 and delivery for the same payment.",
          "REWORK",
          "Material contrary evidence omitted; outcome must be reconsidered without assuming reversal.",
          "Q02;Q14;Q15"
        ],
        [
          "C03",
          "Partial return treated as full reversal",
          "Original debit 11000 and explicitly linked return 2000; narrative says fully reversed.",
          "REWORK",
          "Correct net 9000 and review conclusion dependent on the error.",
          "Q03;Q14;Q15"
        ],
        [
          "C04",
          "Unsupported identity merge",
          "Two beneficiaries have similar names but different supplied identifiers; investigator merged them into one subject.",
          "REWORK",
          "Split identities and recompute aggregate before reassessing.",
          "Q04;Q14;Q15"
        ],
        [
          "C05",
          "Nonmaterial display defect",
          "Ledger and narrative amounts match; one non-substantive punctuation defect in an evidence title.",
          "ACCEPT",
          "Optional editorial correction; no effect on inference or traceability.",
          "Q05;Q14;Q15"
        ],
        [
          "C06",
          "Relevant timeline gap",
          "Two same-period postings 4000 and 3500 omitted from chronology while present in supplied ledger; net effect 500.",
          "REWORK",
          "Restore both gross events and recompute period totals; net 500 does not excuse omission.",
          "Q06;Q14;Q15"
        ],
        [
          "C07",
          "Bounded unknown handled correctly",
          "Opening balance missing; investigator declines source attribution, requests balance and gives descriptive flows only.",
          "ACCEPT",
          "Properly bounded analysis; unknown is not itself a quality failure.",
          "Q07;Q14;Q15"
        ],
        [
          "C08",
          "Source inaccessible",
          "Case conclusion cites an encrypted document unavailable to either reviewer; no equivalent source supplied.",
          "INSUFFICIENT",
          "Review cannot determine whether the underlying conclusion is supported.",
          "Q08;Q14;Q15"
        ],
        [
          "C09",
          "Different defensible wording",
          "Narrative uses unresolved purpose; reviewer prefers insufficient corroboration; both reflect same evidence and scope.",
          "ACCEPT",
          "Style preference alone is not a defect.",
          "Q09;Q14;Q15"
        ],
        [
          "C10",
          "Observed pattern overstates intent",
          "Rapid onward transfers are evidenced; conclusion states intent to launder without supporting intent evidence.",
          "REWORK",
          "Remove unsupported intent assertion and reconsider bounded analytical conclusion.",
          "Q10;Q14;Q15"
        ],
        [
          "C11",
          "Invented universal documentation rule",
          "Reviewer worksheet treats absent nonfiling memorandum as a universal BSA breach; supplied fixture policy only requires a brief case rationale.",
          "REWORK",
          "Use supplied policy CP-QA-1 and actual case rationale; no universal nonfiling memo requirement.",
          "Q11;Q14;Q15"
        ],
        [
          "C12",
          "Unknown historical cutoff",
          "Packet does not identify what evidence was available at original decision date; reviewers see later documents mixed with earlier material.",
          "INSUFFICIENT",
          "Cannot assess original decision under hindsight without an availability chronology.",
          "Q12;Q14;Q15"
        ]
      ],
      "primary_key": [
        "case_id"
      ],
      "grain": "One completed case packet selected for calibration, not a random population sample.",
      "report_section": 4,
      "formats": {}
    },
    {
      "name": "ReviewVotes",
      "columns": [
        "vote_id",
        "case_id",
        "reviewer_id",
        "vote",
        "round",
        "evidence_ids"
      ],
      "column_contracts": {
        "vote_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique case-reviewer vote; retain before adjudication."
        },
        "case_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Case packet being evaluated."
        },
        "reviewer_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Fictional R1 or R2; not a real reviewer identity."
        },
        "vote": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Original independent quality vote.",
          "enum": [
            "ACCEPT",
            "REWORK",
            "INSUFFICIENT"
          ]
        },
        "round": {
          "type": "integer",
          "nullable": false,
          "unit": "count",
          "description": "Blind round number; fixture is round1."
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
          "V01",
          "C01",
          "R1",
          "ACCEPT",
          1,
          "Q13;Q01"
        ],
        [
          "V02",
          "C01",
          "R2",
          "ACCEPT",
          1,
          "Q13;Q01"
        ],
        [
          "V03",
          "C02",
          "R1",
          "ACCEPT",
          1,
          "Q13;Q02"
        ],
        [
          "V04",
          "C02",
          "R2",
          "REWORK",
          1,
          "Q13;Q02"
        ],
        [
          "V05",
          "C03",
          "R1",
          "REWORK",
          1,
          "Q13;Q03"
        ],
        [
          "V06",
          "C03",
          "R2",
          "REWORK",
          1,
          "Q13;Q03"
        ],
        [
          "V07",
          "C04",
          "R1",
          "REWORK",
          1,
          "Q13;Q04"
        ],
        [
          "V08",
          "C04",
          "R2",
          "REWORK",
          1,
          "Q13;Q04"
        ],
        [
          "V09",
          "C05",
          "R1",
          "ACCEPT",
          1,
          "Q13;Q05"
        ],
        [
          "V10",
          "C05",
          "R2",
          "ACCEPT",
          1,
          "Q13;Q05"
        ],
        [
          "V11",
          "C06",
          "R1",
          "REWORK",
          1,
          "Q13;Q06"
        ],
        [
          "V12",
          "C06",
          "R2",
          "ACCEPT",
          1,
          "Q13;Q06"
        ],
        [
          "V13",
          "C07",
          "R1",
          "ACCEPT",
          1,
          "Q13;Q07"
        ],
        [
          "V14",
          "C07",
          "R2",
          "ACCEPT",
          1,
          "Q13;Q07"
        ],
        [
          "V15",
          "C08",
          "R1",
          "INSUFFICIENT",
          1,
          "Q13;Q08"
        ],
        [
          "V16",
          "C08",
          "R2",
          "INSUFFICIENT",
          1,
          "Q13;Q08"
        ],
        [
          "V17",
          "C09",
          "R1",
          "ACCEPT",
          1,
          "Q13;Q09"
        ],
        [
          "V18",
          "C09",
          "R2",
          "ACCEPT",
          1,
          "Q13;Q09"
        ],
        [
          "V19",
          "C10",
          "R1",
          "REWORK",
          1,
          "Q13;Q10"
        ],
        [
          "V20",
          "C10",
          "R2",
          "REWORK",
          1,
          "Q13;Q10"
        ],
        [
          "V21",
          "C11",
          "R1",
          "ACCEPT",
          1,
          "Q13;Q11"
        ],
        [
          "V22",
          "C11",
          "R2",
          "INSUFFICIENT",
          1,
          "Q13;Q11"
        ],
        [
          "V23",
          "C12",
          "R1",
          "INSUFFICIENT",
          1,
          "Q13;Q12"
        ],
        [
          "V24",
          "C12",
          "R2",
          "INSUFFICIENT",
          1,
          "Q13;Q12"
        ]
      ],
      "primary_key": [
        "vote_id"
      ],
      "grain": "One original blind case-reviewer assessment;24 votes over12 cases.",
      "report_section": 4,
      "formats": {
        "round": "#,##0"
      },
      "foreign_keys": [
        {
          "columns": [
            "case_id"
          ],
          "table": "CasePackets",
          "references": [
            "case_id"
          ]
        }
      ]
    },
    {
      "name": "QualityCriteria",
      "columns": [
        "criterion_id",
        "criterion",
        "rule",
        "materiality_class",
        "boundary",
        "evidence_ids"
      ],
      "column_contracts": {
        "criterion_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable fixture policy criterion."
        },
        "criterion": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Quality dimension being assessed."
        },
        "rule": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact authored requirement for this exercise."
        },
        "materiality_class": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Potential consequence class.",
          "enum": [
            "MATERIAL",
            "ASSESSABILITY",
            "NONMATERIAL"
          ]
        },
        "boundary": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Constraint preventing overstatement."
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
          "K01",
          "Population completeness",
          "Include relevant supplied records or a documented scope exclusion.",
          "MATERIAL",
          "Missing relevant rows can change amounts, chronology or explanation.",
          "Q15"
        ],
        [
          "K02",
          "Calculation accuracy",
          "Reperform stated gross, returns, net and denominator calculations.",
          "MATERIAL",
          "A correct net cannot replace omitted gross events.",
          "Q15"
        ],
        [
          "K03",
          "Identity substantiation",
          "Merge subjects only with adequate supplied identifier linkage.",
          "MATERIAL",
          "Similar names alone cannot support aggregation.",
          "Q15"
        ],
        [
          "K04",
          "Contrary evidence",
          "Address material evidence inconsistent with the proposed conclusion.",
          "MATERIAL",
          "Reviewers need not prefer the contrary explanation, but must evaluate it.",
          "Q15"
        ],
        [
          "K05",
          "Claim strength",
          "Match assertion to evidence class and confidence.",
          "MATERIAL",
          "Observed timing does not establish intent.",
          "Q15"
        ],
        [
          "K06",
          "Criterion authority",
          "Attribute a defect to applicable supplied policy or relevant law with scope.",
          "MATERIAL",
          "Do not invent a universal nonfiling-document requirement.",
          "Q15"
        ],
        [
          "K07",
          "Reviewability",
          "Establish source accessibility and decision-time availability.",
          "ASSESSABILITY",
          "Unable to assess is separate from a demonstrated investigator defect.",
          "Q15"
        ],
        [
          "K08",
          "Presentation clarity",
          "Correct editorial issues that affect comprehension or traceability.",
          "NONMATERIAL",
          "Pure preference with no consequence is not a quality failure.",
          "Q15"
        ]
      ],
      "primary_key": [
        "criterion_id"
      ],
      "grain": "One supplied illustrative quality criterion; no implied universal legal mandate.",
      "report_section": 5,
      "formats": {}
    },
    {
      "name": "DefectRegister",
      "columns": [
        "defect_id",
        "case_id",
        "criterion_id",
        "severity",
        "materiality",
        "condition",
        "evidence_ids"
      ],
      "column_contracts": {
        "defect_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Unique demonstrated quality defect; not every unknown becomes a defect."
        },
        "case_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Affected case packet."
        },
        "criterion_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Applicable supplied criterion."
        },
        "severity": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Illustrative severity based on consequence.",
          "enum": [
            "HIGH",
            "MEDIUM",
            "LOW"
          ]
        },
        "materiality": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Whether error can affect the substantive case reasoning.",
          "enum": [
            "MATERIAL",
            "NONMATERIAL"
          ]
        },
        "condition": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Specific factual or reasoning defect."
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
          "C02",
          "K04",
          "MEDIUM",
          "MATERIAL",
          "Contrary matched invoice and delivery omitted",
          "Q02;Q15"
        ],
        [
          "D02",
          "C03",
          "K02",
          "HIGH",
          "MATERIAL",
          "USD11000 minus USD2000 is USD9000, not zero",
          "Q03;Q15"
        ],
        [
          "D03",
          "C04",
          "K03",
          "HIGH",
          "MATERIAL",
          "Unsupported subject merge changes aggregation",
          "Q04;Q15"
        ],
        [
          "D04",
          "C05",
          "K08",
          "LOW",
          "NONMATERIAL",
          "Punctuation correction does not affect meaning",
          "Q05;Q15"
        ],
        [
          "D05",
          "C06",
          "K01",
          "MEDIUM",
          "MATERIAL",
          "Gross 4000 credit and 3500 debit omitted; net 500",
          "Q06;Q15"
        ],
        [
          "D06",
          "C10",
          "K05",
          "HIGH",
          "MATERIAL",
          "Intent claim exceeds evidence of timing",
          "Q10;Q15"
        ],
        [
          "D07",
          "C11",
          "K06",
          "MEDIUM",
          "MATERIAL",
          "Universal regulatory documentation premise unsupported",
          "Q11;Q15"
        ]
      ],
      "primary_key": [
        "defect_id"
      ],
      "grain": "One defect-condition per case/criterion; multiple defects could affect one case.",
      "report_section": 5,
      "formats": {},
      "foreign_keys": [
        {
          "columns": [
            "case_id"
          ],
          "table": "CasePackets",
          "references": [
            "case_id"
          ]
        },
        {
          "columns": [
            "criterion_id"
          ],
          "table": "QualityCriteria",
          "references": [
            "criterion_id"
          ]
        }
      ]
    },
    {
      "name": "Calibration",
      "columns": [
        "case_id",
        "r1_vote",
        "r2_vote",
        "agreement",
        "consensus",
        "adjudication_reason",
        "evidence_ids"
      ],
      "column_contracts": {
        "case_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Case identifier; one consensus review per case."
        },
        "r1_vote": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Original reviewer1 vote.",
          "enum": [
            "ACCEPT",
            "REWORK",
            "INSUFFICIENT"
          ]
        },
        "r2_vote": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Original reviewer2 vote.",
          "enum": [
            "ACCEPT",
            "REWORK",
            "INSUFFICIENT"
          ]
        },
        "agreement": {
          "type": "boolean",
          "nullable": false,
          "unit": "flag",
          "description": "True only if original votes match exactly."
        },
        "consensus": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Adjudicated outcome after comparing criteria/evidence.",
          "enum": [
            "ACCEPT",
            "REWORK",
            "INSUFFICIENT"
          ]
        },
        "adjudication_reason": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Why consensus follows evidence; not majority-rule substitution."
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
          "C01",
          "ACCEPT",
          "ACCEPT",
          true,
          "ACCEPT",
          "No material reasoning defect on supplied packet.",
          "Q13;Q14;Q15;Q01"
        ],
        [
          "C02",
          "ACCEPT",
          "REWORK",
          false,
          "REWORK",
          "Material contrary evidence omitted; outcome must be reconsidered without assuming reversal.",
          "Q13;Q14;Q15;Q02"
        ],
        [
          "C03",
          "REWORK",
          "REWORK",
          true,
          "REWORK",
          "Correct net 9000 and review conclusion dependent on the error.",
          "Q13;Q14;Q15;Q03"
        ],
        [
          "C04",
          "REWORK",
          "REWORK",
          true,
          "REWORK",
          "Split identities and recompute aggregate before reassessing.",
          "Q13;Q14;Q15;Q04"
        ],
        [
          "C05",
          "ACCEPT",
          "ACCEPT",
          true,
          "ACCEPT",
          "Optional editorial correction; no effect on inference or traceability.",
          "Q13;Q14;Q15;Q05"
        ],
        [
          "C06",
          "REWORK",
          "ACCEPT",
          false,
          "REWORK",
          "Restore both gross events and recompute period totals; net 500 does not excuse omission.",
          "Q13;Q14;Q15;Q06"
        ],
        [
          "C07",
          "ACCEPT",
          "ACCEPT",
          true,
          "ACCEPT",
          "Properly bounded analysis; unknown is not itself a quality failure.",
          "Q13;Q14;Q15;Q07"
        ],
        [
          "C08",
          "INSUFFICIENT",
          "INSUFFICIENT",
          true,
          "INSUFFICIENT",
          "Review cannot determine whether the underlying conclusion is supported.",
          "Q13;Q14;Q15;Q08"
        ],
        [
          "C09",
          "ACCEPT",
          "ACCEPT",
          true,
          "ACCEPT",
          "Style preference alone is not a defect.",
          "Q13;Q14;Q15;Q09"
        ],
        [
          "C10",
          "REWORK",
          "REWORK",
          true,
          "REWORK",
          "Remove unsupported intent assertion and reconsider bounded analytical conclusion.",
          "Q13;Q14;Q15;Q10"
        ],
        [
          "C11",
          "ACCEPT",
          "INSUFFICIENT",
          false,
          "REWORK",
          "Use supplied policy CP-QA-1 and actual case rationale; no universal nonfiling memo requirement.",
          "Q13;Q14;Q15;Q11"
        ],
        [
          "C12",
          "INSUFFICIENT",
          "INSUFFICIENT",
          true,
          "INSUFFICIENT",
          "Cannot assess original decision under hindsight without an availability chronology.",
          "Q13;Q14;Q15;Q12"
        ]
      ],
      "primary_key": [
        "case_id"
      ],
      "grain": "One paired case assessment; preserve original votes and later consensus.",
      "report_section": 5,
      "formats": {},
      "foreign_keys": [
        {
          "columns": [
            "case_id"
          ],
          "table": "CasePackets",
          "references": [
            "case_id"
          ]
        }
      ]
    },
    {
      "name": "Remediation",
      "columns": [
        "remediation_id",
        "defect_id",
        "repair",
        "closure_test",
        "status",
        "evidence_ids"
      ],
      "column_contracts": {
        "remediation_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable proposed repair identifier."
        },
        "defect_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Demonstrated defect being addressed."
        },
        "repair": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Specific proposed correction."
        },
        "closure_test": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Evidence an independent reviewer would reperform."
        },
        "status": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Fixture has proposals only.",
          "enum": [
            "PROPOSED"
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
          "M01",
          "D01",
          "Evaluate matched invoice and delivery as counterevidence.",
          "Revised rationale addresses both sides and any outcome change.",
          "PROPOSED",
          "Q02;Q16"
        ],
        [
          "M02",
          "D02",
          "Correct gross 11000, return 2000 and net 9000.",
          "Recalculate from posted records and inspect affected conclusion.",
          "PROPOSED",
          "Q03;Q16"
        ],
        [
          "M03",
          "D03",
          "Split unsupported merged subjects.",
          "Recompute separate aggregates and verify each identity link.",
          "PROPOSED",
          "Q04;Q16"
        ],
        [
          "M04",
          "D04",
          "Optionally correct punctuation without altering analytical outcome.",
          "Evidence title remains resolvable; no material rework needed.",
          "PROPOSED",
          "Q05;Q16"
        ],
        [
          "M05",
          "D05",
          "Restore omitted credit 4000 and debit 3500.",
          "Reconcile gross flows, net 500 and chronology.",
          "PROPOSED",
          "Q06;Q16"
        ],
        [
          "M06",
          "D06",
          "Replace unsupported intent assertion with bounded observed pattern.",
          "Every remaining proposition matches its evidence class.",
          "PROPOSED",
          "Q10;Q16"
        ],
        [
          "M07",
          "D07",
          "Apply CP-QA-1 brief-rationale criterion and remove invented legal premise.",
          "Assess actual rationale under supplied policy; no automatic regulatory finding.",
          "PROPOSED",
          "Q11;Q15;Q16"
        ]
      ],
      "primary_key": [
        "remediation_id"
      ],
      "grain": "One proposed repair per demonstrated defect; no repair is executed in the fixture.",
      "report_section": 5,
      "formats": {},
      "foreign_keys": [
        {
          "columns": [
            "defect_id"
          ],
          "table": "DefectRegister",
          "references": [
            "defect_id"
          ]
        }
      ]
    },
    {
      "name": "DecisionRecord",
      "columns": [
        "decision_id",
        "question",
        "status",
        "basis",
        "evidence_ids"
      ],
      "column_contracts": {
        "decision_id": {
          "type": "text",
          "nullable": false,
          "unit": "identifier",
          "description": "Stable quality decision gate."
        },
        "question": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Decision scope."
        },
        "status": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Result under fixture evidence.",
          "enum": [
            "RECORDED",
            "INSUFFICIENT",
            "NOT_RECORDED"
          ]
        },
        "basis": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact result and denominator meaning."
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
          "Calibration consensus",
          "RECORDED",
          "4 ACCEPT,6 REWORK,2 INSUFFICIENT across 12 selected packets",
          "Q14"
        ],
        [
          "D02",
          "Population defect rate",
          "INSUFFICIENT",
          "Deliberate calibration selection does not support population-rate extrapolation",
          "Q15"
        ],
        [
          "D03",
          "Underlying alert or filing dispositions",
          "NOT_RECORDED",
          "Quality consensus does not decide customer conduct or SAR outcome",
          "Q15"
        ],
        [
          "D04",
          "Remediation closure",
          "NOT_RECORDED",
          "Seven proposals exist; no executed repair or closure verification supplied",
          "Q16"
        ]
      ],
      "primary_key": [
        "decision_id"
      ],
      "grain": "One decision boundary separating quality judgment, population inference and business action.",
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
          "description": "Stable fixture check."
        },
        "check": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Reperformable calculation or boundary."
        },
        "expected": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Exact independent target."
        },
        "actual": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Calculated fixture result."
        },
        "result": {
          "type": "text",
          "nullable": false,
          "unit": "text",
          "description": "Analytical result.",
          "enum": [
            "PASS",
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
          "Packet and vote counts",
          "12 packets;24 votes",
          "12 / 24",
          "PASS",
          "Q13"
        ],
        [
          "Q02",
          "Original agreement",
          "9 of 12;75.0%",
          "9 / 12 =75.0%",
          "PASS",
          "Q13"
        ],
        [
          "Q03",
          "Reviewer marginals",
          "R1 6/4/2; R2 5/4/3",
          "6/4/2;5/4/3",
          "PASS",
          "Q13"
        ],
        [
          "Q04",
          "Chance agreement",
          "52/144 =36.1111%",
          "52/144",
          "PASS",
          "Q13"
        ],
        [
          "Q05",
          "Cohen kappa",
          "14/23 =0.6086956522",
          "14/23",
          "PASS",
          "Q13"
        ],
        [
          "Q06",
          "Consensus denominator",
          "4/12 ACCEPT;6/12 REWORK;2/12 INSUFFICIENT",
          "33.3%;50.0%;16.7%",
          "PASS",
          "Q14"
        ],
        [
          "Q07",
          "Material defect cases",
          "6 of 10 assessable;6 of 12 selected",
          "60.0% assessable;50.0% selected",
          "PASS",
          "Q14;Q15"
        ],
        [
          "Q08",
          "Defect counts",
          "7 defects:6 material,1 nonmaterial",
          "7 / 6 / 1",
          "PASS",
          "Q14;Q15"
        ],
        [
          "Q09",
          "Unknown treatment",
          "C08/C12 not counted as passes",
          "INSUFFICIENT retained",
          "PASS",
          "Q08;Q12;Q14"
        ],
        [
          "Q10",
          "Closure authority",
          "No executed correction or closure",
          "NOT_RECORDED",
          "NOT RECORDED",
          "Q16"
        ]
      ],
      "primary_key": [
        "check_id"
      ],
      "grain": "One reperformable quality metric or authorization check.",
      "report_section": 5,
      "formats": {}
    }
  ],
  "findings": [
    {
      "id": "AQA-F01",
      "title": "Six packets need substantive rework under the fixture rubric",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "Q02",
        "Q03",
        "Q04",
        "Q06",
        "Q10",
        "Q11",
        "Q14",
        "Q15"
      ],
      "detail": "Consensus identifies six material-defect cases among twelve deliberately selected packets. This is 50.0% of selected packets or 60.0% of ten assessable packets; it is not a population defect estimate.",
      "recommendation": "Correct each case-specific defect and reperform its closure test before claiming repair."
    },
    {
      "id": "AQA-F02",
      "title": "Two packets remain unassessable",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "Q08",
        "Q12",
        "Q14"
      ],
      "detail": "C08 lacks accessible cited evidence; C12 lacks decision-time availability chronology. Neither is counted as an acceptable case or a demonstrated investigator defect.",
      "recommendation": "Obtain the missing reviewability inputs and reassess under the original decision-time frame."
    },
    {
      "id": "AQA-F03",
      "title": "Original reviewer agreement is incomplete",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "Q13",
        "Q14"
      ],
      "detail": "Original votes agree on 9/12 cases (75.0%); unweighted Cohen kappa is 14/23, approximately 0.6087. Adjudication later produces consensus without erasing three disagreements.",
      "recommendation": "Use C02/C06/C11 for criterion calibration; preserve original votes and track later rounds separately."
    },
    {
      "id": "AQA-F04",
      "title": "One nonmaterial editorial defect does not require substantive rework",
      "severity": "LOW",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "Q05",
        "Q14",
        "Q15"
      ],
      "detail": "C05 has one punctuation defect without effect on calculation, evidence linkage or conclusion. Its consensus status remains ACCEPT under the fixture rubric.",
      "recommendation": "Record optional correction without treating style preference as a material quality failure."
    }
  ],
  "evidence": [
    {
      "id": "Q01",
      "title": "Fictional case packet C01",
      "locator": "10-worked-example.md, Raw packet C01",
      "claim_class": "Observed"
    },
    {
      "id": "Q02",
      "title": "Fictional case packet C02",
      "locator": "10-worked-example.md, Raw packet C02",
      "claim_class": "Observed"
    },
    {
      "id": "Q03",
      "title": "Fictional case packet C03",
      "locator": "10-worked-example.md, Raw packet C03",
      "claim_class": "Observed"
    },
    {
      "id": "Q04",
      "title": "Fictional case packet C04",
      "locator": "10-worked-example.md, Raw packet C04",
      "claim_class": "Observed"
    },
    {
      "id": "Q05",
      "title": "Fictional case packet C05",
      "locator": "10-worked-example.md, Raw packet C05",
      "claim_class": "Observed"
    },
    {
      "id": "Q06",
      "title": "Fictional case packet C06",
      "locator": "10-worked-example.md, Raw packet C06",
      "claim_class": "Observed"
    },
    {
      "id": "Q07",
      "title": "Fictional case packet C07",
      "locator": "10-worked-example.md, Raw packet C07",
      "claim_class": "Observed"
    },
    {
      "id": "Q08",
      "title": "Fictional case packet C08",
      "locator": "10-worked-example.md, Raw packet C08",
      "claim_class": "Observed"
    },
    {
      "id": "Q09",
      "title": "Fictional case packet C09",
      "locator": "10-worked-example.md, Raw packet C09",
      "claim_class": "Observed"
    },
    {
      "id": "Q10",
      "title": "Fictional case packet C10",
      "locator": "10-worked-example.md, Raw packet C10",
      "claim_class": "Observed"
    },
    {
      "id": "Q11",
      "title": "Fictional case packet C11",
      "locator": "10-worked-example.md, Raw packet C11",
      "claim_class": "Observed"
    },
    {
      "id": "Q12",
      "title": "Fictional case packet C12",
      "locator": "10-worked-example.md, Raw packet C12",
      "claim_class": "Observed"
    },
    {
      "id": "Q13",
      "title": "Fictional review votes",
      "locator": "10-worked-example.md, Raw votes R1/R2 across C01\u2013C12",
      "claim_class": "Observed"
    },
    {
      "id": "Q14",
      "title": "Fictional adjudication minutes",
      "locator": "10-worked-example.md, Consensus C01\u2013C12",
      "claim_class": "Observed"
    },
    {
      "id": "Q15",
      "title": "Illustrative quality policy CP-QA-1",
      "locator": "10-worked-example.md, Eight criterion cards",
      "claim_class": "Observed"
    },
    {
      "id": "Q16",
      "title": "Fictional remediation proposals",
      "locator": "10-worked-example.md, Remediation D01\u2013D07",
      "claim_class": "Observed"
    }
  ],
  "metrics": [
    {
      "label": "Case packets reviewed",
      "value": 12,
      "method": "Unique C01\u2013C12 selected deliberately for calibration",
      "format": "#,##0"
    },
    {
      "label": "Original review votes",
      "value": 24,
      "method": "Two reviewers per case; distinct from case count",
      "format": "#,##0"
    },
    {
      "label": "Original exact agreement",
      "value": 0.75,
      "format": "0.0%",
      "method": "9 identical original vote pairs /12 paired cases"
    },
    {
      "label": "Unweighted Cohen kappa",
      "value": 0.6086956521739131,
      "format": "0.0000",
      "method": "(9/12 -52/144)/(1 -52/144); nominal three-category votes; no universal adequacy cutoff"
    },
    {
      "label": "Selected cases needing rework",
      "value": 0.5,
      "format": "0.0%",
      "method": "6 consensus REWORK /12 selected packets; not extrapolated"
    },
    {
      "label": "Assessable-case material defect ratio",
      "value": 0.6,
      "format": "0.0%",
      "method": "6 material-defect cases /(12 selected -2 INSUFFICIENT); excluded unknowns displayed separately"
    }
  ],
  "limitations": [
    "All case packets, reviewers, decisions and policy are fictional.",
    "Deliberate calibration selection does not support a population defect estimate or statistical assurance.",
    "Quality consensus does not determine suspicious activity, customer conduct or filing obligations.",
    "C08/C12 cannot be assessed until their reviewability gaps are resolved.",
    "No proposed repair has been executed and no actual authorized closure has been supplied."
  ],
  "conclusion": "The calibration set contains four acceptable packets, six requiring substantive rework and two unassessable packets. Original reviewer agreement is 75.0% with kappa 0.6087; consensus preserves rather than replaces the original disagreements.",
  "report_narrative": [
    [
      "The calibration set contains four acceptable packets, six requiring substantive rework and two unassessable packets. Original reviewer agreement is 75.0% with kappa 0.6087; consensus preserves rather than replaces the original disagreements."
    ],
    [
      "Twelve deliberately selected fictional case packets, two original blind reviewers each, supplied illustrative policy CP-QA-1 and a separate consensus round. No random sample or population estimate.",
      "The supplied rubric separates material reasoning defects, reviewability limitations and nonmaterial presentation issues. Criteria are illustrative internal policy and must not be described as universal legal requirements."
    ],
    [
      "AQA-F01: Consensus identifies six material-defect cases among twelve deliberately selected packets. This is 50.0% of selected packets or 60.0% of ten assessable packets; it is not a population defect estimate.",
      "AQA-F02: C08 lacks accessible cited evidence; C12 lacks decision-time availability chronology. Neither is counted as an acceptable case or a demonstrated investigator defect.",
      "AQA-F03: Original votes agree on 9/12 cases (75.0%); unweighted Cohen kappa is 14/23, approximately 0.6087. Adjudication later produces consensus without erasing three disagreements.",
      "AQA-F04: C05 has one punctuation defect without effect on calculation, evidence linkage or conclusion. Its consensus status remains ACCEPT under the fixture rubric."
    ],
    [
      "C01\u2013C12 are the complete selected packet population. Twenty-four original votes are retained before adjudication. Reviewers agree on C01/C03/C04/C05/C07/C08/C09/C10/C12 and disagree on C02/C06/C11."
    ],
    [
      "R1 marginals are 6 ACCEPT,4 REWORK,2 INSUFFICIENT; R2 marginals are 5/4/3. Chance agreement is(6\u00d75+4\u00d74+2\u00d73)/144=52/144. Kappa is(9/12-52/144)/(1-52/144)=14/23. No universal adequacy threshold is applied.",
      "Consensus produces 4 ACCEPT,6 REWORK and 2 INSUFFICIENT. Seven demonstrated defects include 6 material and 1 nonmaterial across 7 cases. Six material cases divide by 12 selected packets for 50.0% or 10 assessable packets for 60.0%; the two unknowns are explicit in both presentations.",
      "Seven repairs are proposed with case-specific closure tests. C05 stays ACCEPT because its punctuation defect has no substantive effect. C08/C12 require reviewability inputs, not invented investigator-error findings."
    ],
    [
      "Q01\u2013Q12 are the individual packets; Q13 preserves original votes; Q14 records later consensus; Q15 supplies the illustrative criteria; Q16 contains proposed remediation. Original decision-time availability must be established before applying later evidence to a prior adjudication."
    ],
    [
      "Correct omitted counterevidence, reversal arithmetic, unsupported identity merging, incomplete chronology, unsupported intent and criterion provenance. Obtain accessible evidence for C08 and a decision-time availability chronology for C12. Keep all repairs proposed until execution and independent verification are supplied."
    ],
    [
      "All case packets, reviewers, decisions and policy are fictional.",
      "Deliberate calibration selection does not support a population defect estimate or statistical assurance.",
      "Quality consensus does not determine suspicious activity, customer conduct or filing obligations.",
      "C08/C12 cannot be assessed until their reviewability gaps are resolved.",
      "No proposed repair has been executed and no actual authorized closure has been supplied.",
      "Fixture metrics reperform correctly. Human business disposition and remediation closure remain NOT_RECORDED."
    ]
  ],
  "suite_id": "alert-qa",
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
      "finding_id": "AQA-F01",
      "proposal": "Correct each case-specific defect and reperform its closure test before claiming repair.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-002",
      "finding_id": "AQA-F02",
      "proposal": "Obtain the missing reviewability inputs and reassess under the original decision-time frame.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-003",
      "finding_id": "AQA-F03",
      "proposal": "Use C02/C06/C11 for criterion calibration; preserve original votes and track later rounds separately.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-004",
      "finding_id": "AQA-F04",
      "proposal": "Record optional correction without treating style preference as a material quality failure.",
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
