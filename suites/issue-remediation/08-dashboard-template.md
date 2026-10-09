# Issue Remediation and Closure Review — complete dashboard template

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
<title>Issue Remediation and Closure Review</title>
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
  "slug": "issue-remediation",
  "title": "Issue Remediation and Closure Review",
  "summary": "Assess causal corrective actions, implementation evidence, effectiveness testing, recurrence, and independent closure gates at a fixed reference date.",
  "audience": "Issue owners, assurance reviewers, and remediation coordinators",
  "decision": "Which issues are ready for independent closure review, and which evidence, overdue obligations, or residual-risk gates remain unresolved?",
  "palette": "umber",
  "report_sections": [
    "Closure readiness and unresolved decisions",
    "Issue population and review reference date",
    "Findings and remediation barriers",
    "Issue lifecycle and closure gates",
    "Action evidence and effectiveness results",
    "Evidence causal alternatives and recurrence",
    "Proposed actions and independent review",
    "Limitations quality review and human disposition"
  ],
  "domain_tables": [
    {
      "name": "IssueRegister",
      "columns": [
        "issue_id",
        "severity",
        "root_cause_status",
        "disposition",
        "approved_due_date",
        "days_overdue",
        "closure_gate",
        "evidence_ids"
      ],
      "formats": {
        "approved_due_date": "yyyy-mm-dd",
        "days_overdue": "0"
      },
      "rows": [
        [
          "I01",
          "HIGH",
          "Supported",
          "Reopened",
          "2026-10-02",
          7,
          "Blocked: effectiveness failed",
          "SYN-001"
        ],
        [
          "I02",
          "MEDIUM",
          "Supported",
          "Validation pending",
          "2026-10-10",
          0,
          "Blocked: retest evidence incomplete",
          "SYN-001"
        ],
        [
          "I03",
          "MEDIUM",
          "Supported",
          "Closure review pending",
          "2026-10-07",
          2,
          "Ready for independent closure review",
          "SYN-001"
        ],
        [
          "I04",
          "HIGH",
          "Provisional",
          "Acceptance expired",
          "2026-09-30",
          9,
          "Blocked: acceptance expired and replacement absent",
          "SYN-001"
        ]
      ]
    },
    {
      "name": "ActionEvidence",
      "columns": [
        "action_id",
        "issue_id",
        "action_type",
        "approved_due_date",
        "evidence_status",
        "completion_date",
        "days_overdue",
        "retest_result",
        "evidence_ids"
      ],
      "formats": {
        "approved_due_date": "yyyy-mm-dd",
        "completion_date": "yyyy-mm-dd",
        "days_overdue": "0"
      },
      "rows": [
        [
          "A01",
          "I01",
          "Implementation",
          "2026-09-25",
          "Verified",
          "2026-09-28",
          0,
          "Not applicable",
          "SYN-001"
        ],
        [
          "A02",
          "I01",
          "Effectiveness",
          "2026-10-02",
          "Failed",
          null,
          7,
          "FAIL",
          "SYN-001"
        ],
        [
          "A03",
          "I02",
          "Implementation",
          "2026-10-03",
          "Verified",
          "2026-10-03",
          0,
          "Not applicable",
          "SYN-001"
        ],
        [
          "A04",
          "I02",
          "Effectiveness",
          "2026-10-10",
          "Unresolved",
          null,
          0,
          "UNABLE TO CONCLUDE",
          "SYN-001"
        ],
        [
          "A05",
          "I03",
          "Implementation and effectiveness",
          "2026-09-26",
          "Verified",
          "2026-09-26",
          0,
          "PASS",
          "SYN-001"
        ],
        [
          "A06",
          "I04",
          "Replacement",
          "2026-09-30",
          "Not evidenced",
          null,
          9,
          "Not tested",
          "SYN-001"
        ]
      ]
    }
  ],
  "findings": [
    {
      "id": "IR-F01",
      "title": "I01 failed post-change retest after historical recurrence",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001"
      ],
      "detail": "R06 records a missed daily review on Oct 06 despite the implemented backup roster. A02 failed; the existing action plan also placed its deadline before the end of its six-day window.",
      "recommendation": "Investigate roster adoption and coverage execution, address the failed mechanism, and propose a feasible fresh validation plan."
    },
    {
      "id": "IR-F02",
      "title": "Missing R10 evidence prevents complete archive validation",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001"
      ],
      "detail": "A04 has three PASS and one UNABLE TO CONCLUDE result among four opportunities. The supplied retrieval failure does not establish whether the original artifact exists.",
      "recommendation": "Recover R10 or establish its retention status; retain the four-unit denominator and unresolved gate."
    },
    {
      "id": "IR-F03",
      "title": "Technical closure readiness awaits authorized approval",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001"
      ],
      "detail": "I03 has implementation evidence and four passing fresh retest opportunities, but no current final approval; it is two calendar days overdue at Oct 09.",
      "recommendation": "Submit the complete I03 record to the independent closure reviewer and preserve pending status until a decision is recorded."
    },
    {
      "id": "IR-F04",
      "title": "Temporary acceptance expired without replacement evidence",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001"
      ],
      "detail": "I04 acceptance expired Sep 30. Its Oct 31 extension is only proposed; no replacement artifact is supplied. I04 and A06 are nine days overdue.",
      "recommendation": "Obtain an authorized residual-risk and replacement decision, preserving the expired acceptance and original deadline history."
    }
  ],
  "evidence": [
    {
      "id": "SYN-001",
      "title": "Complete fictional issue chronology, action criteria, decision history and fourteen retest records",
      "locator": "10-worked-example.md, original issues, complete deadline history, action evidence, and raw retest ledger",
      "claim_class": "Observed"
    },
    {
      "id": "REF-001",
      "title": "GAO 2025 Green Book, principle 17, paragraphs 17.05\u201317.08; retrieved 2026-10-09",
      "locator": "https://www.gao.gov/assets/gao-25-107721.pdf",
      "claim_class": "Reported"
    },
    {
      "id": "REF-002",
      "title": "FFIEC BSA/AML Independent Testing; retrieved 2026-10-09",
      "locator": "https://bsaaml.ffiec.gov/manual/AssessingTheBSAAMLComplianceProgram/03",
      "claim_class": "Reported"
    }
  ],
  "metrics": [
    {
      "label": "Evidenced action completions",
      "value": "3 of 6 (50.0%)",
      "method": "A01, A03 and A05 meet individual acceptance criteria; action completion is not issue closure.",
      "format": "#,##0"
    },
    {
      "label": "Current authorized closures",
      "value": "0 of 4 (0.0%)",
      "method": "No current final issue approval exists in the complete fictional decision register.",
      "format": "#,##0"
    },
    {
      "label": "Overdue active issues",
      "value": "3 of 4 (75.0%)",
      "method": "I01 7, I03 2, I04 9 calendar days past approved due dates at end-of-day Oct 09, 2026 ET.",
      "format": "#,##0"
    },
    {
      "label": "Ready for closure review",
      "value": "1 of 4 (25.0%)",
      "method": "I03 meets technical gates; independent human approval remains pending.",
      "format": "#,##0"
    }
  ],
  "limitations": [
    "All issues, actions, authority records and retest observations are fictional.",
    "The miniature retest windows do not support a future or institution-wide effectiveness claim.",
    "I02 has one unresolved retest artifact; I04 has a provisional causal explanation.",
    "I03 is ready for review, not closed; the assistant cannot supply independent approval.",
    "Dates are evaluated at the saved Oct 09, 2026 snapshot, not renderer execution time."
  ],
  "conclusion": "Three of six actions are evidenced complete, but no issue is currently closed. I03 is technically ready for independent closure review; I01 failed retest, I02 has an unresolved retest record, and I04\u2019s acceptance expired without evidenced replacement. Three of four active issues are overdue at Oct 09, 2026.",
  "report_narrative": [
    [
      "Three of six existing actions meet their own acceptance criteria, while all four issues remain active. I03 is ready for independent closure review. I01, I02 and I04 have distinct effectiveness, evidence and acceptance blockers."
    ],
    [
      "The complete fictional snapshot contains four issues and six existing actions at end-of-day Oct 09, 2026 ET. Calendar-day differences use approved current deadlines; proposed extensions do not reset the clock. Fourteen retest opportunities are fully listed."
    ],
    [
      "I01\u2019s R06 retest fails despite roster implementation. I02\u2019s R10 is unresolved. I03 lacks final approval despite technical readiness. I04\u2019s Sep 30 acceptance expired, and its proposed Oct 31 extension has no authorization."
    ],
    [
      "IssueRegister shows overdue days of 7, 0, 2 and 9 for I01\u2013I04. I01 remains Reopened after its Aug 31 closure and Sep 12 recurrence; I03 remains Closure review pending. Three active issues are overdue, or 75.0%."
    ],
    [
      "ActionEvidence contains three Verified actions, one Failed, one Unresolved and one Not evidenced. Current overdue days are 0, 7, 0, 0, 0 and 9. A01\u2019s three historical late days remain separate. A02 retest has 5 PASS and 1 FAIL; A04 has 3 PASS and 1 unresolved; A05 has 4 PASS."
    ],
    [
      "SYN-001 preserves the causal facts, decision history and every retest ID. The backup roster did not establish effective coverage on Oct 06; the mechanism needs further assessment. R10 retrieval failure does not prove nonexistence. I04\u2019s dependency explanation remains provisional. Public guidance supplies method context only."
    ],
    [
      "Proposed follow-ups address failed coverage, recover R10, submit I03 for an actual independent decision, and resolve I04\u2019s expired disposition and replacement plan. A02\u2019s Oct 02 deadline preceded the end of its Oct 01\u201306 observation window and requires a feasible revised plan without erasing the breach."
    ],
    [
      "QA reconciles 6 actions, 4 active issues and 14 retest units, preserving all missing outcomes. Negative controls reject proposed-date substitution, implementation-as-effectiveness and readiness-as-closure. No current final human closure decisions are supplied."
    ]
  ],
  "suite_id": "issue-remediation",
  "version": "1.1.0",
  "notice": "Synthetic worked example. Fictional records. Not a completed operational review.",
  "as_of": "2026-10-09",
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
      "finding_id": "IR-F01",
      "proposal": "Investigate roster adoption and coverage execution, address the failed mechanism, and propose a feasible fresh validation plan.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-002",
      "finding_id": "IR-F02",
      "proposal": "Recover R10 or establish its retention status; retain the four-unit denominator and unresolved gate.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-003",
      "finding_id": "IR-F03",
      "proposal": "Submit the complete I03 record to the independent closure reviewer and preserve pending status until a decision is recorded.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-004",
      "finding_id": "IR-F04",
      "proposal": "Obtain an authorized residual-risk and replacement decision, preserving the expired acceptance and original deadline history.",
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
