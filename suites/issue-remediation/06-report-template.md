# Issue Remediation and Closure Review — fixed report template

Version 1.1.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Closure readiness and unresolved decisions**
2. **Issue population and review reference date**
3. **Findings and remediation barriers**
4. **Issue lifecycle and closure gates**
5. **Action evidence and effectiveness results**
6. **Evidence causal alternatives and recurrence**
7. **Proposed actions and independent review**
8. **Limitations quality review and human disposition**

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
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

DATA = {'slug': 'issue-remediation', 'title': 'Issue Remediation and Closure Review', 'summary': 'Assess causal corrective actions, implementation evidence, effectiveness testing, recurrence, and independent closure gates at a fixed reference date.', 'audience': 'Issue owners, assurance reviewers, and remediation coordinators', 'decision': 'Which issues are ready for independent closure review, and which evidence, overdue obligations, or residual-risk gates remain unresolved?', 'palette': 'umber', 'report_sections': ['Closure readiness and unresolved decisions', 'Issue population and review reference date', 'Findings and remediation barriers', 'Issue lifecycle and closure gates', 'Action evidence and effectiveness results', 'Evidence causal alternatives and recurrence', 'Proposed actions and independent review', 'Limitations quality review and human disposition'], 'domain_tables': [{'name': 'IssueRegister', 'columns': ['issue_id', 'severity', 'root_cause_status', 'disposition', 'approved_due_date', 'days_overdue', 'closure_gate', 'evidence_ids'], 'formats': {'approved_due_date': 'yyyy-mm-dd', 'days_overdue': '0'}, 'rows': [['I01', 'HIGH', 'Supported', 'Reopened', '2026-10-02', 7, 'Blocked: effectiveness failed', 'SYN-001'], ['I02', 'MEDIUM', 'Supported', 'Validation pending', '2026-10-10', 0, 'Blocked: retest evidence incomplete', 'SYN-001'], ['I03', 'MEDIUM', 'Supported', 'Closure review pending', '2026-10-07', 2, 'Ready for independent closure review', 'SYN-001'], ['I04', 'HIGH', 'Provisional', 'Acceptance expired', '2026-09-30', 9, 'Blocked: acceptance expired and replacement absent', 'SYN-001']]}, {'name': 'ActionEvidence', 'columns': ['action_id', 'issue_id', 'action_type', 'approved_due_date', 'evidence_status', 'completion_date', 'days_overdue', 'retest_result', 'evidence_ids'], 'formats': {'approved_due_date': 'yyyy-mm-dd', 'completion_date': 'yyyy-mm-dd', 'days_overdue': '0'}, 'rows': [['A01', 'I01', 'Implementation', '2026-09-25', 'Verified', '2026-09-28', 0, 'Not applicable', 'SYN-001'], ['A02', 'I01', 'Effectiveness', '2026-10-02', 'Failed', None, 7, 'FAIL', 'SYN-001'], ['A03', 'I02', 'Implementation', '2026-10-03', 'Verified', '2026-10-03', 0, 'Not applicable', 'SYN-001'], ['A04', 'I02', 'Effectiveness', '2026-10-10', 'Unresolved', None, 0, 'UNABLE TO CONCLUDE', 'SYN-001'], ['A05', 'I03', 'Implementation and effectiveness', '2026-09-26', 'Verified', '2026-09-26', 0, 'PASS', 'SYN-001'], ['A06', 'I04', 'Replacement', '2026-09-30', 'Not evidenced', None, 9, 'Not tested', 'SYN-001']]}], 'findings': [{'id': 'IR-F01', 'title': 'I01 failed post-change retest after historical recurrence', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'R06 records a missed daily review on Oct 06 despite the implemented backup roster. A02 failed; the existing action plan also placed its deadline before the end of its six-day window.', 'recommendation': 'Investigate roster adoption and coverage execution, address the failed mechanism, and propose a feasible fresh validation plan.'}, {'id': 'IR-F02', 'title': 'Missing R10 evidence prevents complete archive validation', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'A04 has three PASS and one UNABLE TO CONCLUDE result among four opportunities. The supplied retrieval failure does not establish whether the original artifact exists.', 'recommendation': 'Recover R10 or establish its retention status; retain the four-unit denominator and unresolved gate.'}, {'id': 'IR-F03', 'title': 'Technical closure readiness awaits authorized approval', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'I03 has implementation evidence and four passing fresh retest opportunities, but no current final approval; it is two calendar days overdue at Oct 09.', 'recommendation': 'Submit the complete I03 record to the independent closure reviewer and preserve pending status until a decision is recorded.'}, {'id': 'IR-F04', 'title': 'Temporary acceptance expired without replacement evidence', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'I04 acceptance expired Sep 30. Its Oct 31 extension is only proposed; no replacement artifact is supplied. I04 and A06 are nine days overdue.', 'recommendation': 'Obtain an authorized residual-risk and replacement decision, preserving the expired acceptance and original deadline history.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Complete fictional issue chronology, action criteria, decision history and fourteen retest records', 'locator': '10-worked-example.md, original issues, complete deadline history, action evidence, and raw retest ledger', 'claim_class': 'Observed'}, {'id': 'REF-001', 'title': 'GAO 2025 Green Book, principle 17, paragraphs 17.05–17.08; retrieved 2026-10-09', 'locator': 'https://www.gao.gov/assets/gao-25-107721.pdf', 'claim_class': 'Reported'}, {'id': 'REF-002', 'title': 'FFIEC BSA/AML Independent Testing; retrieved 2026-10-09', 'locator': 'https://bsaaml.ffiec.gov/manual/AssessingTheBSAAMLComplianceProgram/03', 'claim_class': 'Reported'}], 'metrics': [{'label': 'Evidenced action completions', 'value': '3 of 6 (50.0%)', 'method': 'A01, A03 and A05 meet individual acceptance criteria; action completion is not issue closure.', 'format': '#,##0'}, {'label': 'Current authorized closures', 'value': '0 of 4 (0.0%)', 'method': 'No current final issue approval exists in the complete fictional decision register.', 'format': '#,##0'}, {'label': 'Overdue active issues', 'value': '3 of 4 (75.0%)', 'method': 'I01 7, I03 2, I04 9 calendar days past approved due dates at end-of-day Oct 09, 2026 ET.', 'format': '#,##0'}, {'label': 'Ready for closure review', 'value': '1 of 4 (25.0%)', 'method': 'I03 meets technical gates; independent human approval remains pending.', 'format': '#,##0'}], 'limitations': ['All issues, actions, authority records and retest observations are fictional.', 'The miniature retest windows do not support a future or institution-wide effectiveness claim.', 'I02 has one unresolved retest artifact; I04 has a provisional causal explanation.', 'I03 is ready for review, not closed; the assistant cannot supply independent approval.', 'Dates are evaluated at the saved Oct 09, 2026 snapshot, not renderer execution time.'], 'conclusion': 'Three of six actions are evidenced complete, but no issue is currently closed. I03 is technically ready for independent closure review; I01 failed retest, I02 has an unresolved retest record, and I04’s acceptance expired without evidenced replacement. Three of four active issues are overdue at Oct 09, 2026.', 'report_narrative': [['Three of six existing actions meet their own acceptance criteria, while all four issues remain active. I03 is ready for independent closure review. I01, I02 and I04 have distinct effectiveness, evidence and acceptance blockers.'], ['The complete fictional snapshot contains four issues and six existing actions at end-of-day Oct 09, 2026 ET. Calendar-day differences use approved current deadlines; proposed extensions do not reset the clock. Fourteen retest opportunities are fully listed.'], ['I01’s R06 retest fails despite roster implementation. I02’s R10 is unresolved. I03 lacks final approval despite technical readiness. I04’s Sep 30 acceptance expired, and its proposed Oct 31 extension has no authorization.'], ['IssueRegister shows overdue days of 7, 0, 2 and 9 for I01–I04. I01 remains Reopened after its Aug 31 closure and Sep 12 recurrence; I03 remains Closure review pending. Three active issues are overdue, or 75.0%.'], ['ActionEvidence contains three Verified actions, one Failed, one Unresolved and one Not evidenced. Current overdue days are 0, 7, 0, 0, 0 and 9. A01’s three historical late days remain separate. A02 retest has 5 PASS and 1 FAIL; A04 has 3 PASS and 1 unresolved; A05 has 4 PASS.'], ['SYN-001 preserves the causal facts, decision history and every retest ID. The backup roster did not establish effective coverage on Oct 06; the mechanism needs further assessment. R10 retrieval failure does not prove nonexistence. I04’s dependency explanation remains provisional. Public guidance supplies method context only.'], ['Proposed follow-ups address failed coverage, recover R10, submit I03 for an actual independent decision, and resolve I04’s expired disposition and replacement plan. A02’s Oct 02 deadline preceded the end of its Oct 01–06 observation window and requires a feasible revised plan without erasing the breach.'], ['QA reconciles 6 actions, 4 active issues and 14 retest units, preserving all missing outcomes. Negative controls reject proposed-date substitution, implementation-as-effectiveness and readiness-as-closure. No current final human closure decisions are supplied.']], 'suite_id': 'issue-remediation', 'version': '1.1.0', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'as_of': '2026-10-09', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'IR-F01', 'proposal': 'Investigate roster adoption and coverage execution, address the failed mechanism, and propose a feasible fresh validation plan.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'IR-F02', 'proposal': 'Recover R10 or establish its retention status; retain the four-unit denominator and unresolved gate.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'IR-F03', 'proposal': 'Submit the complete I03 record to the independent closure reviewer and preserve pending status until a decision is recorded.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-004', 'finding_id': 'IR-F04', 'proposal': 'Obtain an authorized residual-risk and replacement decision, preserving the expired acceptance and original deadline history.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
"""Validate the data boundary shared by catalogs and standalone Python renderers."""
import math
import re

SCHEMA_COMMON = {'Summary', 'Dashboard', 'Findings', 'Evidence', 'Actions', 'QA'}

def case_errors(data, complete=False):
    errors = []
    if not isinstance(data, dict):
        return ['case data must be an object']
    def string(value):
        return isinstance(value, str) and bool(value.strip())
    if complete:
        for key in ['suite_id','version','as_of','notice','scope','conclusion']:
            if not string(data.get(key)):errors.append(key+' must be nonempty text in a complete case')
        if not isinstance(data.get('methods'),list) or not data['methods'] or not all(string(x) for x in data['methods']):errors.append('complete case methods must contain text')
        for key in ['actions','qa']:
            if not isinstance(data.get(key),list):errors.append(key+' must be a list in a complete case')
        if data.get('suite_id')!=data.get('slug'):errors.append('complete case suite_id must match the safe slug')
    for key in ['slug','title','summary','audience','decision','palette']:
        if not string(data.get(key)):
            errors.append(key + ' must be nonempty text')
    if not re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', data.get('slug','') if isinstance(data.get('slug'),str) else ''):
        errors.append('slug must be a safe lowercase identifier')
    if data.get('palette') not in ('slate','teal','indigo','umber'):
        errors.append('unknown palette')
    for key in ['report_sections','report_narrative','domain_tables','findings','evidence','metrics','limitations']:
        if not isinstance(data.get(key), list):
            errors.append(key + ' must be a list')
    if errors:
        return errors
    if len(data['report_sections']) != 8 or not all(string(x) for x in data['report_sections']) or len(set(data['report_sections'])) != 8:
        errors.append('eight distinct report headings required')
    narrative = data['report_narrative']
    if len(narrative) != 8 or any(not isinstance(section,list) or not section or not all(string(p) for p in section) for section in narrative):
        errors.append('eight populated case-specific narrative sections required')
    if not all(string(x) for x in data['limitations']):
        errors.append('limitations must contain text')
    if len(data['domain_tables']) != 2:
        errors.append('exactly two domain tables required')
    names = {x.casefold() for x in SCHEMA_COMMON}
    for index, table in enumerate(data['domain_tables']):
        label = f'domain table {index + 1}'
        if not isinstance(table,dict):
            errors.append(label+' must be an object'); continue
        name = table.get('name')
        if not string(name) or len(name)>31 or re.search(r'[\\/*?:\[\]]',name) or name.startswith("'") or name.endswith("'") or name.casefold() in names:
            errors.append('invalid or duplicate sheet '+str(name))
        else:
            names.add(name.casefold())
        columns, rows = table.get('columns'), table.get('rows')
        if not isinstance(columns,list) or not columns or not all(string(c) for c in columns):
            errors.append(label+' requires nonempty text columns'); continue
        if len(set(columns)) != len(columns):
            errors.append('duplicate columns in '+str(name))
        if not isinstance(rows,list):
            errors.append(label+' rows must be a list'); continue
        for row_number,row in enumerate(rows,1):
            if not isinstance(row,list) or len(row)!=len(columns):
                errors.append(f'row width mismatch in {name}, row {row_number}')
            elif any(isinstance(value,(dict,list)) for value in row):
                errors.append(f'nested domain cell in {name}, row {row_number}')
        formats = table.get('formats',{})
        if not isinstance(formats,dict) or any(k not in columns or not string(v) for k,v in formats.items()):
            errors.append(label+' formats must name existing columns')
    def records(key,fields):
        valid=[]
        for index,row in enumerate(data[key]):
            if not isinstance(row,dict) or any(field not in row for field in fields):
                errors.append(f'{key} row {index+1} missing required fields'); continue
            valid.append(row)
        return valid
    evidence_rows=records('evidence',['id','title','locator','claim_class'])
    findings=records('findings',['id','title','severity','confidence','claim_class','evidence_ids','detail','recommendation'])
    evidence_ids=[e['id'] for e in evidence_rows if string(e['id'])]
    finding_ids=[f['id'] for f in findings if string(f['id'])]
    if len(evidence_ids)!=len(evidence_rows):errors.append('invalid evidence ID')
    if len(finding_ids)!=len(findings):errors.append('invalid finding ID')
    if len(set(evidence_ids))!=len(evidence_ids):errors.append('duplicate evidence ID')
    if len(set(finding_ids))!=len(finding_ids):errors.append('duplicate finding ID')
    classes=('Observed','Reported','Inferred','Estimated')
    for row in evidence_rows:
        if any(not string(row[k]) for k in ['title','locator']) or row['claim_class'] not in classes:
            errors.append('invalid evidence text or claim class')
    for row in findings:
        refs=row['evidence_ids']
        if not isinstance(refs,list) or not refs or not all(string(x) and x in evidence_ids for x in refs):
            errors.append('unresolved evidence key in '+str(row['id']))
        if row['severity'] not in ('CRITICAL','HIGH','MEDIUM','LOW'):errors.append('invalid severity in '+str(row['id']))
        if row['confidence'] not in ('HIGH','MODERATE','LOW','NOT ASSESSABLE'):errors.append('invalid confidence in '+str(row['id']))
        if row['claim_class'] not in classes:errors.append('invalid claim class in '+str(row['id']))
        if any(not string(row[k]) for k in ['title','detail','recommendation']):errors.append('invalid finding text')
    for row in records('metrics',['label','value','method']):
        if not string(row['label']) or not string(row['method']) or isinstance(row['value'],(dict,list)):
            errors.append('invalid metric label, method or scalar value')
        if 'format' in row and not string(row['format']):errors.append('invalid metric format')
    for key,fields in [('actions',['id','finding_id','proposal','owner','due_date','status']),('qa',['id','check','result','evidence'])]:
        if key not in data:continue
        if not isinstance(data[key],list):
            errors.append(key+' must be a list');continue
        rows=records(key,fields);ids=[r['id'] for r in rows if string(r['id'])]
        if len(ids)!=len(rows) or len(ids)!=len(set(ids)):errors.append('invalid or duplicate '+key+' ID')
        if key=='actions':
            for row in rows:
                if row['finding_id'] not in finding_ids:errors.append('unresolved action finding key')
                if row['status'] not in ('Proposed','Accepted','In progress','Blocked','Closed','Risk accepted'):errors.append('invalid action state')
                if not string(row['proposal']) or any(row[k] is not None and not string(row[k]) for k in ['owner','due_date']):errors.append('invalid action text')
        else:
            for row in rows:
                if not string(row['check']) or not string(row['evidence']):errors.append('invalid QA text')
                if row['result'] not in ('PASS','FAIL','REVIEW REQUIRED','NOT RECORDED','NOT TESTED'):errors.append('invalid QA result')
    def visit(value):
        if isinstance(value,float) and not math.isfinite(value):
            errors.append('non-finite numeric value')
        elif isinstance(value,str):
            if re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',value):errors.append('unsupported control character')
        elif isinstance(value,list):
            for item in value:visit(item)
        elif isinstance(value,dict):
            for item in value.values():visit(item)
    visit(data)
    return list(dict.fromkeys(errors))

def require_case(data):
    problems=case_errors(data, complete=True)
    if problems:
        raise ValueError('Case data rejected: '+ '; '.join(problems))

require_case(DATA)

OUTPUT = Path(DATA['suite_id'] + '-report.docx')
doc = Document()
doc.core_properties.author = 'Markdown Analyst Toolkit'
doc.core_properties.title = DATA['title']
doc.core_properties.subject = DATA['notice']
section = doc.sections[0]
section.top_margin = section.bottom_margin = Inches(0.7)
section.left_margin = section.right_margin = Inches(0.75)
normal = doc.styles['Normal']
normal.font.name = 'Arial'
normal.font.size = Pt(10.5)
normal.font.color.rgb = RGBColor.from_string('243641')
normal.paragraph_format.space_after = Pt(7)
normal.paragraph_format.line_spacing = 1.12
for name, size in [('Title',24), ('Heading 1',16), ('Heading 2',12)]:
    style = doc.styles[name]
    style.font.name = 'Arial'
    style.font.size = Pt(size)
    style.font.color.rgb = RGBColor.from_string('000000' if name=='Title' else '344E5F')
    style.paragraph_format.keep_with_next = True
    style.paragraph_format.space_before = Pt(14)
    style.paragraph_format.space_after = Pt(7)
for style in [normal, doc.styles['Title'], doc.styles['Heading 1'], doc.styles['Heading 2'], doc.styles['List Bullet']]:
    style.font.name = 'Arial'
    fonts = style.element.get_or_add_rPr().rFonts
    if fonts is not None:
        for key in list(fonts.attrib):
            if 'theme' in key.lower():
                del fonts.attrib[key]
    for border in list(style.element.iter(qn('w:pBdr'))):
        border.getparent().remove(border)

def text(value):
    return 'Not provided' if value is None else '; '.join(map(str,value)) if isinstance(value,list) else str(value)

def formatted(value, fmt):
    if not isinstance(value, (int,float)) or not fmt:
        return text(value)
    if fmt == '0.0%':
        return f'{value:.1%}'
    if fmt == '0.0"%"':
        return f'{value:.1f}%'
    decimal = re.search(r'\.([0#]+)', fmt)
    places = len(decimal.group(1)) if decimal else 0
    number = f'{value:,}' + ('.'+'0'*places if places else '') if isinstance(value,int) else f'{value:,.{places}f}'
    return ('$' if '$' in fmt else '') + number

def table(headers, rows, keep_together=False, widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = 'Table Grid'
    if widths:
        t.autofit = False
        for column,width in zip(t.columns,widths):column.width=Inches(width)
    for i,h in enumerate(headers):
        t.rows[0].cells[i].text = h
    repeat = OxmlElement('w:tblHeader')
    t.rows[0]._tr.get_or_add_trPr().append(repeat)
    for values in rows:
        cells=t.add_row().cells
        for i,v in enumerate(values):
            cells[i].text=text(v)
    for row_index,row in enumerate(t.rows):
        row._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
        for cell_index,cell in enumerate(row.cells):
            if widths:cell.width=Inches(widths[cell_index])
            shading=OxmlElement('w:shd')
            shading.set(qn('w:fill'),'344E5F' if row_index==0 else 'E2E8E9' if row_index%2 else 'F1F2EF')
            cell._tc.get_or_add_tcPr().append(shading)
            for p in cell.paragraphs:
                p.paragraph_format.space_after=Pt(4)
                if keep_together and row_index<len(t.rows)-1:
                    p.paragraph_format.keep_with_next=True
                for run in p.runs:
                    run.font.name='Arial'
                    run.font.size=Pt(9)
                    run.font.color.rgb=RGBColor.from_string('FFFFFF' if row_index==0 else '243641')
                    run.font.bold=row_index==0
    doc.add_paragraph()
    return t

doc.add_paragraph(DATA['title'], 'Title')
doc.add_paragraph(f"Version {DATA['version']} | As of {DATA['as_of']} | Draft for human review")
doc.add_paragraph(DATA['notice'])
doc.add_paragraph(DATA['summary'])
doc.add_paragraph('Decision supported: '+DATA['decision'])
for index, heading in enumerate(DATA['report_sections']):
    doc.add_heading(heading, level=1)
    for paragraph in DATA['report_narrative'][index]:
        doc.add_paragraph(paragraph)
    if index == 0:
        table(['Measure','Value','Calculation or limit'], [[m['label'],formatted(m['value'],m.get('format')),m['method']] for m in DATA['metrics']])
    elif index == 2:
        for f in DATA['findings']:
            doc.add_heading(f["id"]+' '+f['title'], level=2)
            meta=doc.add_paragraph(f"{f['severity']} severity | {f['confidence']} confidence | {f['claim_class']} | Evidence: {', '.join(f['evidence_ids'])}")
            meta.paragraph_format.keep_with_next=True
            doc.add_paragraph(f['detail'])
            doc.add_paragraph('Proposed action: '+f['recommendation'])
    elif index in (3,4):
        # Wide data stay readable as vertical records; workbook retains tabular schema.
        source = DATA['domain_tables'][index-3]
        doc.add_paragraph(source['name'])
        for row in source['rows']:
            table(['Field','Value'], [(key,formatted(value,source.get('formats',{}).get(key))) for key,value in zip(source['columns'],row)],keep_together=True)
        missing = sum(value is None for row in source['rows'] for value in row)
        doc.add_paragraph(f"Domain record count: {len(source['rows'])}. Missing (null) cells: {missing}. Empty text follows the field-specific contract.")
    elif index == 5:
        table(['Evidence ID','Source or fixture','Exact locator','Claim class'], [[e['id'],e['title'],e['locator'],e['claim_class']] for e in DATA['evidence']],widths=[1.0,2.0,2.8,1.2])
    elif index == 6:
        for a in DATA['actions']:
            doc.add_paragraph(f"{a['id']} / {a['finding_id']}: {a['proposal']} Owner: {text(a['owner'])}. Due: {text(a['due_date'])}. State: {a['status']}")
    elif index == 7:
        for value in DATA['limitations']:
            doc.add_paragraph(value, style='List Bullet')
        table(['Check','Result','Evidence'], [[q['check'],q['result'],q['evidence']] for q in DATA['qa']])
footer = section.footer.paragraphs[0]
footer.add_run('Draft for human review | Page ')
field=OxmlElement('w:fldSimple')
field.set(qn('w:instr'),'PAGE')
footer._p.append(field)
doc.save(OUTPUT)
print(str(OUTPUT))

```

## Recovery and acceptance

If generation fails, preserve the completed analytical text and the exact error category. Retry only the failed render step after checking the capability; do not redo source judgments to obtain a prettier report. Never claim DOCX or PDF export succeeded unless an openable file exists. A successful renderer run proves file creation, not truth, regulatory compliance, or institutional approval.
