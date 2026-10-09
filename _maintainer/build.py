"""Regenerate embedded renderers and measured attachment records; no network calls."""
import argparse
import hashlib
import html
import json
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / '_maintainer'
PALETTES = {
    'slate': ('#315c75', '#b0d3e6'),
    'teal': ('#276357', '#a7d8c7'),
    'indigo': ('#4c5180', '#c7cdf2'),
    'umber': ('#735327', '#e9d3aa'),
}
COMMON = {
    'Summary': ['measure','value','method_or_limit'],
    'Dashboard': ['severity','finding_count','denominator'],
    'Findings': ['id','title','severity','confidence','claim_class','evidence_ids','detail','recommendation'],
    'Evidence': ['id','title','locator','claim_class'],
    'Actions': ['action_id','finding_id','proposal','owner','due_date','status'],
    'QA': ['check_id','check','result','evidence'],
}

def prepare(catalog):
    data = dict(catalog)
    data.update(suite_id=data['slug'], version='1.0.0', as_of='2026-10-09',
                notice='Synthetic worked example. Fictional records. Not a completed operational review.')
    data.setdefault('scope', 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.')
    data.setdefault('conclusion', data.get('metadata', {}).get('conclusion') or f"The fictional review records {len(data['findings'])} findings for human assessment. Read the finding-specific evidence and unresolved limitations before making a disposition.")
    data['metrics'] = [dict(metric, format=metric.get('format') or ('$#,##0.00' if metric['label'].endswith('USD') else '#,##0.00' if isinstance(metric['value'], float) else '#,##0')) for metric in data['metrics']]
    data.setdefault('methods', [
        'Confirm the question, authorized scope, period, population and available capabilities.',
        'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.',
        'Apply the suite method and decision rules; test competing explanations and missing inputs.',
        'Populate the fixed domain registers without inventing fields, facts or approvals.',
        'Review calculations and citations; record exceptions and seek the named human disposition.',
    ])
    data.setdefault('actions', [dict(id=f'A-{i:03}',finding_id=f['id'],proposal=f['recommendation'],owner=None,due_date=None,status='Proposed') for i,f in enumerate(data['findings'],1)])
    data.setdefault('qa', [
        dict(id='QA-01',check='Synthetic fixture calculations',result='REVIEW REQUIRED',evidence='Reproduce the arithmetic in file 10.'),
        dict(id='QA-02',check='Evidence support and competing explanations',result='REVIEW REQUIRED',evidence='Compare findings to the exact fixture locators and file 04.'),
        dict(id='QA-03',check='Authorized human disposition',result='NOT RECORDED',evidence='No reviewer identity, decision or approval has been supplied.'),
    ])
    data.setdefault('report_narrative', [
        [data['conclusion'], 'This specimen supports the stated decision question. Its findings are proposals; human disposition remains unrecorded.'],
        [data['scope'], 'Use the detailed procedure in file 03 and decision rules in file 04. Preserve all exceptions and missing-data states.'],
        ['The register below separates observation, consequence, uncertainty and proposed action. Evidence identifiers resolve to the fictional case in file 10.'],
        [f"{data['domain_tables'][0]['name']} preserves the first domain register. Each field and its unit follow file 05; blank values are not negative findings."],
        [f"{data['domain_tables'][1]['name']} preserves the supporting analysis. Record competing explanations and unresolved decisions rather than inferring approval."],
        ['These exact locators point to synthetic case records. The primary authority register in file 02 provides methodological context; it does not substantiate allegations about a subject.'],
        ['Assign an authorized owner and a real due date before accepting an action. The template leaves both unrecorded rather than inventing them.'],
        ['Complete the review in file 09. Keep the report in draft while a material evidence, arithmetic, coverage or authorization defect is unresolved.'],
    ])
    return data

def python_template(name, data):
    return (HERE/'templates'/name).read_text().replace('DATA = None  # __DATA__', 'DATA = '+repr(data))

def dashboard(data):
    light, dark = PALETTES[data['palette']]
    payload=json.dumps(data,ensure_ascii=True,indent=2).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    return (HERE/'templates/dashboard.html').read_text().replace('__TITLE__',html.escape(data['title'])).replace('__LIGHT_ACCENT__',light).replace('__DARK_ACCENT__',dark).replace('__DATA__',payload)

def report_md(data):
    sections='\n'.join(f'{i}. **{heading}**' for i,heading in enumerate(data['report_sections'],1))
    text=f'''# {data['title']} — fixed report template

Version 1.0.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

{sections}

Keep all eight sections, including a specific limitation if a section cannot be assessed. Within section 1 state the answer, decision implication and unresolved gate before background. Section 2 records jurisdiction, as-of date, population, exclusions and method version. Section 3 carries each finding with class, severity, confidence, evidence, counterevidence and proposed action. Sections 4–5 preserve the domain registers in file 05. Section 6 contains exact evidence locators. Section 7 records proposed actions. Section 8 contains limitations, QA outcomes and the named human disposition.

The code's prose is a complete **synthetic specimen**, not boilerplate conclusions for later cases. Replace each `report_narrative` paragraph with case-specific analysis. Do not publish sample judgments as real results. Retain the data label while any synthetic records remain.

## Word and PDF style contract

| Element | Fixed treatment |
| --- | --- |
| Page | Portrait report; 0.75-inch left/right and 0.70-inch top/bottom margins |
| Typeface | Arial 10.5 pt body; 24 pt title; 16 pt first-level and 12 pt second-level headings; sans-serif fallback |
| Color | Ink `#243641`; headings `#344E5F`; neutral table shading; black title |
| Paragraph | 1.12 line spacing; 7 pt after; headings keep with following paragraph |
| Tables | 9 pt minimum; repeat header rows; long domain registers shown as field/value records to avoid tiny columns |
| Figures | No decorative graphics; every quantitative visual needs its unit, scope, denominator and source |
| Footer | Draft for human review; automatic page number |
| PDF | Export the verified Word document or print the HTML template; do not merely rename the extension |
| Dates and money | Archive/field dates `YYYY-MM-DD`; narrative dates `MMM DD, YYYY`; times `h:mm AM/PM ET`; currency symbol and comma separators |

The workbook retains every domain column in order; the report may present the same records vertically for readability. Do not merge duplicate-looking records unless the method supports deduplication. Never hide counterevidence, omit an unresolved record, or replace a null with a favorable sentence.

## Required content review

- Trace each material sentence to its source span, row, calculation or explicit inference. A URL alone is not evidence of retrieval.
- Preserve the distinction between a source allegation and an adjudicated fact. Add the source's date and procedural status where relevant.
- Tie totals and exclusions to the worked population or supplied control totals. When unknown, state the resulting limitation.
- Keep a proposed action distinct from the human disposition and from execution. This renderer records no approval.
- Reopen the actual deliverable. Check page breaks, repeated headers, complete rows, dates, metadata and citations. If visual review is unavailable, say so.

## Complete in-session renderer

The code block is self-contained. Its only runtime dependency is an already available `python-docx`. `DATA` includes all synthetic inputs needed to render the specimen; neither this repository nor a local path is needed in the user's session. Replace data values, not section order or column identifiers. Add evidence and case-specific narrative before calling the result complete.

```python
{python_template('report.py',data)}
```

## Recovery and acceptance

If generation fails, preserve the completed analytical text and the exact error category. Retry only the failed render step after checking the capability; do not redo source judgments to obtain a prettier report. Never claim DOCX or PDF export succeeded unless an openable file exists. A successful renderer run proves file creation, not truth, regulatory compliance, or institutional approval.
'''
    return text

def workbook_md(data):
    schemas={**COMMON,**{t['name']:t['columns'] for t in data['domain_tables']}}
    rows='\n'.join('| '+name+' | `'+ '`, `'.join(cols)+'` |' for name,cols in schemas.items())
    return f'''# {data['title']} — fixed workbook template

Version 1.0.0. The workbook is a generated review snapshot with visible evidence and explicit open decisions. Use an in-session file-creation capability; no terminal, repository checkout or automation is needed.

## Exact workbook schema

Create these sheets in this order. Preserve field spelling and column order. File 05 defines domain types, units, permitted values and interpretation; this file controls the six common sheets.

| Sheet | Ordered columns |
| --- | --- |
{rows}

## Common field contract

| Field group | Contract |
| --- | --- |
| IDs | Nonempty text, stable within a case; unique primary IDs. Foreign keys must resolve before release. Preserve leading zeros. |
| Severity | `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`; severity is separate from evidence confidence. |
| Confidence | `HIGH`, `MODERATE`, `LOW`, `NOT ASSESSABLE`; justify the rating in the analysis. |
| Claim class | `Observed`, `Reported`, `Inferred`, `Estimated`; public-source claims are not automatically Observed. |
| Evidence IDs | Semicolon-delimited stable keys. Use the Evidence sheet's exact ID; no invented source titles. |
| Owner/due date | Explicit `Not provided` until supplied; do not assign an actual person or a guessed deadline. |
| Action state | `Proposed`, `Accepted`, `In progress`, `Blocked`, `Closed`, `Risk accepted`; the fixture starts Proposed. Closure requires recorded evidence. |
| QA result | `PASS`, `FAIL`, `REVIEW REQUIRED`, `NOT RECORDED`, or `NOT TESTED` with exact evidence; no automatic PASS. |
| Null | Domain JSON null becomes an empty Excel cell with a missing-value comment and an associated limitation/QA explanation; it is not zero. Common unassigned action fields display `Not provided`. `Not applicable` requires rationale. |
| Numerics | Preserve native units, currency and scale. Fields ending `_usd` display US dollar currency. Other numbers retain their stated domain unit. |
| Evidence text | Write as text, including values beginning `=`, `+`, `-`, `@`, or whitespace. Do not evaluate source text as a formula. |

## Layout and calculation contract

- Summary first, Dashboard second; Findings, Evidence, Actions and QA next; domain data last in the declared order.
- Arial 11 pt; slate header `#344E5F`, white header text, stone body `#F1F2EF`, pale gray alternate rows `#E2E8E9`; no rainbow tab or cell coloring. Chart bars use the same slate and whole-count axis intervals.
- Freeze top row and first column on data tabs. Enable filters and wrapped text. Give long evidence and recommendation fields 44-character columns. Keep body row heights automatic.
- Highlight HIGH severity with muted rose `#F2DADB` and dark red text `#7F3038`; retain the textual label. Missing data are literal values, not a green/blank cell.
- Landscape A4 printing for compact sheets and A3 for sheets wider than 145 combined character-width units; repeat the header row and identifier column. Fit one page wide with unrestricted pages tall. Inspect actual print readability; use the Word report if the available printer cannot reproduce a wide sheet legibly.
- The Dashboard calculates counts from the Findings severity column using `COUNTIF`. Counts cover **supplied findings**, not the entire transaction/customer population. Use the exact source scope in denominators.
- This is a snapshot generator: after adding or removing records, regenerate the workbook so formulas, validations, filters and chart ranges include every row. Do not assume inserting a row extends all ranges.
- Summary business measures come from validated input calculations. Preserve each method and limitation alongside the value. Recompute them from source when adapting; never retain a specimen metric by accident.
- `openpyxl` writes formulas but does not calculate them. Request recalculation in Excel or the available spreadsheet engine, inspect results, and record the outcome. If unavailable, label formula-cache/display behavior **NOT TESTED**; the independently computed check does not prove Excel behavior.

## Complete in-session renderer

Use this block when `openpyxl` is already available in the chat's Python capability. No installation is required or assumed. When unavailable, ask the assistant's approved workbook capability to implement the same schema and style. If that is unavailable too, emit one copy-ready table per sheet and state **XLSX not created**. Never label CSV as a multi-sheet workbook.

```python
{python_template('workbook.py',data)}
```

## Release checks

Reopen the saved workbook. Confirm exact sheet order and column names, retained row counts, evidence joins, null handling, leading-zero IDs and literal formula-like text. Compare Dashboard counts to a separately tallied Findings column. Record whether formulas recalculated. Filter and sort without losing IDs or detaching notes. Inspect every sheet at normal zoom and print preview; fix clipped text, empty charts, `####`, unreadable tables and missing rows. These artifact checks supplement the analytical gates in file 09.
'''

def dashboard_md(data):
    light,dark=PALETTES[data['palette']]
    return f'''# {data['title']} — complete dashboard template

Version 1.0.0. Use the complete HTML below to create a single downloadable `.html` file in the current session. It includes all style and interaction code. No hosted assets, fonts, CDN, installation, repository access, API key or local server is needed. Where a file tool is unavailable, return the complete HTML as copy-ready text and explicitly state that no file was created.

## Design and behavior contract

| Element | Light | Dark |
| --- | --- | --- |
| Page | `#E4E7E7` muted gray | `#263746` softened navy |
| Panels | `#F1F2EF` stone | `#304655` slate navy |
| Text | `#243641` | `#EFF1EF` |
| Secondary text | `#4E606A` | `#C0CDD3` |
| Suite accent | `{light}` | `{dark}` |
| High / medium / low | `#8A3439` / `#735119` / `#315F54` | `#FFB8B8` / `#F0D393` / `#B1DCC9` |

Use Segoe UI, Calibri or Arial; 15 px body; responsive title; no remote font. Keep the ten fixed dashboard sections and exact domain tables. Navigation identifies analytical sections. It is not an operational case-management interface.

Theme control is keyboard operable and retains the preference when browser storage permits. Storage failure does not stop rendering. Findings search and severity filtering affect the table and CSV export only; coverage metrics and severity/confidence charts remain full-fixture measures and are labeled accordingly. Printing temporarily restores all findings, uses a neutral light print theme, and restores the filter afterward. Table regions scroll independently on small screens with keyboard access. Empty results state what scope is empty; they never imply no underlying risk.

## Populate safely

The JSON in `report-data` is the only data payload. Replace it with the reviewed case data using the same keys and the schemas in file 05. Retain `notice` as a visible synthetic label when using the example. For a real authorized case, replace it with the actual scope/classification and review state only after removing every fixture record. Never fabricate an approval or completed QA check.

Serialize `<`, `>` and `&` in JSON as `\\u003c`, `\\u003e`, `\\u0026` before embedding. Display values through `textContent`; do not insert untrusted evidence with `innerHTML`. This prevents a source string from ending the JSON script element or executing as markup. CSV exports quote all fields and prefix formula-like strings with an apostrophe. The export contains only visible findings and uses a name that states that scope.

## Complete standalone HTML

```html
{dashboard(data)}
```

## Acceptance and delivery

Open the actual file. Check both themes, desktop and narrow screens, keyboard navigation, visible focus, long evidence strings, missing values, empty filters, reset, CSV scope and print preview. Reconcile every displayed metric and chart to its input rows. Verify no network resources are requested. Rendering success does not establish evidence quality or analytical validity. Record untested browser/platform behavior honestly. If a browser blocks downloads or scripting, use the unchanged source data and fixed report/workbook alternatives; do not invent a functioning control.
'''

def instruction_metrics(folder):
    files=sorted(p for p in folder.glob('*.md') if re.match(r'(0[1-9]|10)-',p.name))
    joined=''.join(p.read_text() for p in files)
    return dict(files=len(files),characters=len(joined),bytes=sum(p.stat().st_size for p in files),words=len(joined.split()),tokens=math.ceil(len(joined)/4),low=math.ceil(len(joined)/5),high=math.ceil(len(joined)/3),hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files})

def build_record(data, metrics):
    m=metrics
    rows='\n'.join(f'| `{name}` | `{digest}` |' for name,digest in m['hashes'].items())
    return f'''# {data['title']} — build record

Version 1.0.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | {m['files']} | Files 01–10; README and this record excluded |
| Instructional words | {m['words']:,} | Whitespace-separated tokens, including code |
| UTF-8 bytes | {m['bytes']:,} | Sum of files 01–10 |
| Characters | {m['characters']:,} | Unicode characters across files 01–10 |
| Estimated attachment tokens | {m['tokens']:,} | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | {m['low']:,}–{m['high']:,} | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | {m['tokens']*4:,}–{m['tokens']*10:,} | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
| Actual authoring/reasoning/input tokens | Not available | No complete per-suite generation telemetry captured |
| Actual monetary build cost | Not available | No token billing attribution or assumed model price |
| Elapsed effort | Not attributed per suite | Parallel authoring and shared template work overlap |

The build-budget range is intentionally an estimate of resources one might reserve to reproduce the workflow, not a claim about tokens spent on this release. It cannot establish value, model quality or elapsed human labor. The attachment estimate excludes your data, conversation history and generated answer. Reserve room for all three. A file-count limit does not imply the content fits a model's context or was fully attended to.

## Creation sequence

| Stage | Work performed | Evidence available |
| --- | --- | --- |
| 1. Scope | Mapped the specialist task to existing public toolkit methods | Root coverage map and suite README |
| 2. Method | Authored inputs, method, decision rules and exceptions | Files 01–04 |
| 3. Contract | Fixed field names, narrative roles and deliverable layouts | Files 05–08 |
| 4. Case | Added a complete fictional example with expected results and edge cases | File 10 and maintainer catalog |
| 5. Review | Defined falsifiable analytical and delivery checks | File 09; actual release checks are listed in the root verification record |
| 6. Package | Measured files, embedded renderers and created checksummed bundles | This record, release assets and root verification record |

Stage order describes the workflow, not a fabricated hourly timeline. A listed acceptance test is not evidence it passed. See [release verification](https://github.com/maxmoran23/markdown-analyst-toolkit/blob/v1.0.0/docs/VERIFICATION.md) for checks actually performed and limits, including lack of testing in an enterprise Copilot tenant.

## Instructional file integrity

| File | SHA-256 |
| --- | --- |
{rows}

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
'''

def replace_block(text, label, content):
    start,end=f'<!-- {label}:START -->',f'<!-- {label}:END -->'
    block=start+'\n'+content.strip()+'\n'+end
    return re.sub(re.escape(start)+r'.*?'+re.escape(end),lambda _:block,text,flags=re.S) if start in text else text.rstrip()+'\n\n'+block+'\n'

def generate(check=False):
    changed=[]
    def put(path, value):
        if not path.exists() or path.read_text()!=value:
            changed.append(str(path.relative_to(ROOT)))
            if not check:
                path.write_text(value)
    for src in sorted((HERE/'catalog').glob('*.json')):
        data=prepare(json.loads(src.read_text()))
        folder=ROOT/'suites'/data['slug']
        folder.mkdir(parents=True,exist_ok=True)
        for name,content in [('06-report-template.md',report_md(data)),('07-workbook-template.md',workbook_md(data)),('08-dashboard-template.md',dashboard_md(data))]:
            put(folder/name,content)
        if not check:
            metrics=instruction_metrics(folder)
        else:
            metrics=instruction_metrics(folder)
        put(folder/'11-build-record.md',build_record(data,metrics))
        readme=folder/'README.md'
        if readme.exists():
            m=metrics
            block=f'''## Build and attachment budget

The ten instructional files contain **{m['words']:,} words** and approximately **{m['tokens']:,} attachment tokens** (characters ÷ 4, rounded up; code included). This is content size, not build consumption. An illustrative reproduction budget is **{m['tokens']*4:,}–{m['tokens']*10:,} tokens** (4–10× content; heuristic, not observed usage). Actual generation tokens and monetary cost were not captured per suite.

Creation sequence: scope mapping → domain methods → fixed output contracts → complete fictional example → review checks → packaged release. [Build details and hashes](11-build-record.md) show the method; [verification](https://github.com/maxmoran23/markdown-analyst-toolkit/blob/v1.0.0/docs/VERIFICATION.md) records what was actually tested.

[Download this 12-file Markdown suite](https://github.com/maxmoran23/markdown-analyst-toolkit/releases/download/v1.0.0/{data['slug']}.zip). Unzip and attach files 01–10. The README and build record are for browsing. If ZIP downloads are restricted, open a file on GitHub, choose Raw, and save its Markdown text using approved controls; do not bypass an organizational restriction.'''
            put(readme,replace_block(readme.read_text(),'BUILD',block))
    if changed:
        print(('STALE: ' if check else 'Generated: ')+', '.join(changed))
    else:
        print('Generated files are current.')
    return 1 if check and changed else 0

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    raise SystemExit(generate(parser.parse_args().check))
