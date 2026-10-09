# Sampling Design and Assurance Review — complete dashboard template

Version 1.1.0. Use the complete HTML below to create a single downloadable `.html` file in the current session. It includes all style and interaction code. No hosted assets, fonts, CDN, installation, repository access, API key or local server is needed. Where a file tool is unavailable, return the complete HTML as copy-ready text and explicitly state that no file was created.

## Design and behavior contract

| Element | Light | Dark |
| --- | --- | --- |
| Page | `#E4E7E7` muted gray | `#263746` softened navy |
| Panels | `#F1F2EF` stone | `#304655` slate navy |
| Text | `#243641` | `#EFF1EF` |
| Secondary text | `#4E606A` | `#C0CDD3` |
| Suite accent | `#315c75` | `#b0d3e6` |
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
<title>Sampling Design and Assurance Review</title>
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
  "slug": "sampling-assurance",
  "title": "Sampling Design and Assurance Review",
  "summary": "Review a complete selection frame, probability design, missing assessments, and the assurance supported by exact finite-population calculations.",
  "audience": "Reviewers, control testers, and analysts designing selections",
  "decision": "What population conclusion does the selection support, and what evidence or design still blocks assurance?",
  "palette": "slate",
  "report_sections": [
    "Assurance conclusion and restrictions",
    "Population scope and selection design",
    "Findings and inference barriers",
    "Stratum coverage and bounds",
    "Selected unit results",
    "Evidence and competing interpretations",
    "Further testing and reviewer decisions",
    "Limitations quality review and human disposition"
  ],
  "domain_tables": [
    {
      "name": "SamplingStrata",
      "columns": [
        "stratum_id",
        "population_count",
        "probability_selected_count",
        "pass_count",
        "fail_count",
        "unassessed_count",
        "inclusion_probability",
        "upper_bound",
        "conclusion"
      ],
      "formats": {
        "inclusion_probability": "0.0%",
        "upper_bound": "0.0%"
      },
      "rows": [
        [
          "H",
          4,
          3,
          1,
          1,
          1,
          0.75,
          null,
          "H04 unresolved; no completed-outcome bound"
        ],
        [
          "L",
          8,
          4,
          4,
          0,
          0,
          0.5,
          0.375,
          "95% finite upper bound 37.5%; 25.0% assurance threshold not demonstrated"
        ]
      ]
    },
    {
      "name": "SampleResults",
      "columns": [
        "sample_id",
        "stratum_id",
        "population_id",
        "selection_basis",
        "inclusion_probability",
        "result",
        "evidence_ids"
      ],
      "formats": {
        "inclusion_probability": "0.0%"
      },
      "rows": [
        [
          "S01",
          "H",
          "H01",
          "Probability",
          0.75,
          "PASS",
          "SYN-001"
        ],
        [
          "S02",
          "H",
          "H03",
          "Probability",
          0.75,
          "FAIL",
          "SYN-001"
        ],
        [
          "S03",
          "H",
          "H04",
          "Probability",
          0.75,
          "UNABLE TO CONCLUDE",
          "SYN-001"
        ],
        [
          "S04",
          "L",
          "L02",
          "Probability",
          0.5,
          "PASS",
          "SYN-001"
        ],
        [
          "S05",
          "L",
          "L04",
          "Probability",
          0.5,
          "PASS",
          "SYN-001"
        ],
        [
          "S06",
          "L",
          "L06",
          "Probability",
          0.5,
          "PASS",
          "SYN-001"
        ],
        [
          "S07",
          "L",
          "L08",
          "Probability",
          0.5,
          "PASS",
          "SYN-001"
        ],
        [
          "S08",
          "L",
          "L07",
          "Judgmental supplement",
          null,
          "FAIL",
          "SYN-001"
        ]
      ]
    }
  ],
  "findings": [
    {
      "id": "SA-F01",
      "title": "Two observed approval-separation failures in distinct selection categories",
      "severity": "HIGH",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001"
      ],
      "detail": "H03 fails in the seven-unit original probability selection; targeted L07 adds a separate observed failure. Both use the preparer role as reviewer.",
      "recommendation": "Investigate the separation failure mechanism and assess the affected scope without pooling targeted results into the probability sample."
    },
    {
      "id": "SA-F02",
      "title": "H04 missing evidence prevents a completed-outcome H assessment",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Observed",
      "evidence_ids": [
        "SYN-001"
      ],
      "detail": "The original H sample contains one pass, one fail, and one unresolved assessment. The owner statement does not establish execution.",
      "recommendation": "Recover contemporaneous H04 evidence or retain the missingness restriction and obtain an approved treatment."
    },
    {
      "id": "SA-F03",
      "title": "L upper bound does not demonstrate the requested assurance threshold",
      "severity": "MEDIUM",
      "confidence": "HIGH",
      "claim_class": "Estimated",
      "evidence_ids": [
        "SYN-001",
        "REF-002"
      ],
      "detail": "For N=8, n=4, x=0, the largest D with hypergeometric lower-tail probability above 0.05 is 3. The one-sided 95% finite upper bound is 37.5%, exceeding the illustrative 25.0% criterion.",
      "recommendation": "Have an authorized reviewer approve a further design or accept the restricted conclusion; the result does not prove the true rate exceeds 25.0%."
    }
  ],
  "evidence": [
    {
      "id": "SYN-001",
      "title": "Complete fictional frame, recorded draw ranks, criteria, and selected evidence",
      "locator": "10-worked-example.md, complete frame, selection replay, and complete selected outcomes",
      "claim_class": "Observed"
    },
    {
      "id": "REF-001",
      "title": "NIST confidence intervals for proportions; retrieved 2026-10-09",
      "locator": "https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm",
      "claim_class": "Reported"
    },
    {
      "id": "REF-002",
      "title": "NIST hypergeometric cumulative distribution; retrieved 2026-10-09, pp. 1\u20132",
      "locator": "https://itl.nist.gov/div898/software/dataplot/refman2/ch8/hypcdf.pdf",
      "claim_class": "Reported"
    },
    {
      "id": "REF-003",
      "title": "FFIEC Risk-Focused BSA/AML Supervision; retrieved 2026-10-09",
      "locator": "https://bsaaml.ffiec.gov/manual/ScopingAndPlanning/02",
      "claim_class": "Reported"
    }
  ],
  "metrics": [
    {
      "label": "Original probability sample",
      "value": "7 of 12 (58.3%)",
      "method": "Original distinct selections / eligible frame; excludes L07 supplement.",
      "format": "#,##0"
    },
    {
      "label": "Primary unresolved assessment",
      "value": "1 of 7 (14.3%)",
      "method": "H04 UNABLE TO CONCLUDE / all original selections.",
      "format": "#,##0"
    },
    {
      "label": "L finite upper bound",
      "value": 0.375,
      "format": "0.0%",
      "method": "One-sided 95%; N=8,n=4,x=0; largest D with C(8-D,4)/C(8,4)\u003e0.05 is 3; bound 3/8."
    },
    {
      "label": "Distinct reviewed units",
      "value": "8 of 12 (66.7%)",
      "method": "Seven original plus one targeted; descriptive coverage, not an eight-unit probability sample.",
      "format": "#,##0"
    }
  ],
  "limitations": [
    "Fictional uniform draw ranks permit conditional replay but do not prove real-world randomization.",
    "H04 is unresolved; H and overall completed-outcome confidence bounds are withheld.",
    "L07 is targeted and remains outside the original probability inference.",
    "The 11.1% and 22.2% weighted completion scenarios are point-estimate sensitivity results, not confidence limits.",
    "No independent human approval or live frame validation is supplied."
  ],
  "conclusion": "The seven-unit probability sample contains one confirmed exception and one unresolved assessment; a separate targeted review adds one exception. L\u2019s one-sided 95% finite upper bound is 37.5%, above the illustrative 25.0% assurance criterion. H and overall inference remain restricted; human review is pending.",
  "report_narrative": [
    [
      "One confirmed exception and one unresolved assessment occur in the seven-unit probability selection; targeted L07 adds a second observed exception. L\u2019s conditional 95% upper bound is 37.5%, so this exercise does not demonstrate the requested 25.0% assurance."
    ],
    [
      "The complete fictional September frame contains four H and eight L approval opportunities. Zero-based lexicographic combination ranks 2 and 49 select three H and four L units under stipulated independent uniform draws. Inclusion probabilities are 0.75 and 0.5.",
      "The complete SYN-001 frame is H01 (Sep 02, 2026; Probability; prep P1/review Q1 before release), H02 (Sep 08; unselected; not inspected), H03 (Sep 16; Probability; prep P3/review P3 before release), H04 (Sep 24; Probability; owner assertion only, execution artifact missing); L01 (Sep 01; unselected; not inspected), L02 (Sep 04; Probability; prep P2/review Q2 before release), L03 (Sep 09; unselected; not inspected), L04 (Sep 11; Probability; prep P4/review Q4 before release), L05 (Sep 17; unselected; not inspected), L06 (Sep 21; Probability; prep P6/review Q6 before release), L07 (Sep 25; Judgmental supplement; prep P7/review P7 before release), and L08 (Sep 29; Probability; prep P8/review Q8 before release). All abbreviated dates are in 2026. H02, L01, L03 and L05 outcomes remain unknown; unselected is not passed. The fixture stipulates this twelve-unit frame matches its master schedule with no duplicates or exclusions."
    ],
    [
      "H03 and targeted L07 use the same role to prepare and approve. H04 has only an owner assertion and no execution artifact. The L assurance restriction is a statistical decision outcome, not proof that its true failure fraction exceeds 25.0%."
    ],
    [
      "SamplingStrata reconciles H as 3=1+1+1 and L as 4=4+0+0. H\u2019s bound is null. For L, D=3 gives a zero-failure tail of 5/70 and D=4 gives 1/70; the strict alpha=0.05 inversion produces U=3 and U/8=37.5%."
    ],
    [
      "SampleResults contains seven Probability rows and one Judgmental supplement row. Primary confirmed failure share is 1/7=14.3%; all reviewed failures are 2/8=25.0%, a descriptive mixed-selection share. Neither replaces a properly weighted population estimate."
    ],
    [
      "SYN-001 preserves every frame ID and selected observation. H04 could reflect missing retention or missing execution; neither explanation is resolved. NIST supplies method context. The binomial contrast 1-0.05^(1/4)=52.7% uses a different model and is not the finite bound."
    ],
    [
      "Recover H04 evidence, investigate the approval-separation mechanism, and have an authorized reviewer decide whether further testing is warranted. Weighted hypothetical completion estimates are 1/9=11.1% if H04 passes and 2/9=22.2% if it fails; sampling uncertainty remains."
    ],
    [
      "QA must preserve 12 frame units, 7 original selections, and 8 distinct reviewed units, with L07 kept separate. Negative controls reject unweighted pooling, missing-as-pass, and a 95% judgmental claim. Human method approval and final disposition remain unrecorded."
    ]
  ],
  "suite_id": "sampling-assurance",
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
      "finding_id": "SA-F01",
      "proposal": "Investigate the separation failure mechanism and assess the affected scope without pooling targeted results into the probability sample.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-002",
      "finding_id": "SA-F02",
      "proposal": "Recover contemporaneous H04 evidence or retain the missingness restriction and obtain an approved treatment.",
      "owner": null,
      "due_date": null,
      "status": "Proposed"
    },
    {
      "id": "A-003",
      "finding_id": "SA-F03",
      "proposal": "Have an authorized reviewer approve a further design or accept the restricted conclusion; the result does not prove the true rate exceeds 25.0%.",
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
