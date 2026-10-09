# Transaction Monitoring Review — fixed report template

Version 1.1.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Review priorities and known movement**
2. **Scope, population, and scenario method**
3. **Findings and benign explanations**
4. **Account flow calculations**
5. **Scenario matches and review outcomes**
6. **Evidence and criterion provenance**
7. **Proposed review and data-repair actions**
8. **Limitations, quality checks, and human decision**

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

DATA = {'slug': 'transaction-monitoring', 'title': 'Transaction Monitoring Review', 'summary': 'Reconcile a transaction extract, calculate transparent monitoring scenarios, and turn rule matches into reviewable observations with explicit benign explanations.', 'audience': 'Monitoring analysts, scenario owners, and independent control reviewers', 'decision': 'Which scenario matches merit further review, which have supported explanations, and which cannot be assessed because the inputs are incomplete?', 'palette': 'slate', 'report_sections': ['Review priorities and known movement', 'Scope, population, and scenario method', 'Findings and benign explanations', 'Account flow calculations', 'Scenario matches and review outcomes', 'Evidence and criterion provenance', 'Proposed review and data-repair actions', 'Limitations, quality checks, and human decision'], 'domain_tables': [{'name': 'AccountFlows', 'columns': ['account_id', 'currency', 'processed_tx_count', 'credit_total', 'debit_total', 'eligible_credit_total', 'eligible_debit_total', 'out_in_ratio', 'population_status'], 'rows': [['A', 'USD', 3, 10000, 9500, 10000, 9500, 0.95, 'COMPLETE'], ['B', 'USD', 2, 5000, 4800, 5000, 4800, 0.96, 'COMPLETE'], ['C', 'USD', 2, 3000, 3000, 0, 0, None, 'OWN_TRANSFER_EXCLUDED'], ['D', 'USD', 1, 0, 1000, 0, 1000, None, 'UNPARSED_AMOUNT']], 'formats': {'credit_total': '#,##0.00', 'debit_total': '#,##0.00', 'eligible_credit_total': '#,##0.00', 'eligible_debit_total': '#,##0.00', 'out_in_ratio': '0.0%'}}, {'name': 'ScenarioResults', 'columns': ['scenario_result_id', 'account_id', 'scenario_id', 'eligible', 'rule_result', 'first_credit_to_debit_hours', 'review_outcome', 'evidence_ids'], 'rows': [['SR-001', 'A', 'TM-01', True, 'MATCH', 2, 'ESCALATE_FOR_REVIEW', 'SYN-001;SYN-002'], ['SR-002', 'B', 'TM-01', True, 'MATCH', 3, 'EXPLANATION_SUPPORTED', 'SYN-001;SYN-003'], ['SR-003', 'C', 'TM-01', False, 'EXCLUDED', None, 'OWN_TRANSFER_CONFIRMED', 'SYN-001;SYN-004'], ['SR-004', 'D', 'TM-01', False, 'NOT_ASSESSABLE', None, 'DATA_REPAIR_REQUIRED', 'SYN-001;SYN-005']], 'formats': {'first_credit_to_debit_hours': '0.0'}}], 'findings': [{'id': 'TM-F01', 'title': 'Account A meets the illustrative rapid-movement rule', 'severity': 'MEDIUM', 'confidence': 'MODERATE', 'claim_class': 'Inferred', 'evidence_ids': ['SYN-001', 'SYN-002'], 'detail': 'Account A received $10,000.00 and sent $9,500.00 within two hours of the first receipt; the 95.0% ratio meets TM-01. Purpose remains unsupported.', 'recommendation': 'Obtain payment purpose and counterparties; refer to the authorized reviewer.'}, {'id': 'TM-F02', 'title': 'Account B has a supported ordinary-business explanation', 'severity': 'LOW', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001', 'SYN-003'], 'detail': 'The 96.0% rule match is retained; a matched supplier invoice supports the $4,800.00 payment.', 'recommendation': 'Document the explanation and seek human disposition; retain the rule hit.'}, {'id': 'TM-F03', 'title': 'Account D cannot be fully assessed', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001', 'SYN-005'], 'detail': 'One unreadable amount prevents account-level completeness; $1,000.00 is only the known posted debit.', 'recommendation': 'Repair the source extract and recompute D before making an account conclusion.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional transaction extract', 'locator': '10-worked-example.md, raw population R01–R10', 'claim_class': 'Observed'}, {'id': 'SYN-002', 'title': 'Fictional account A profile', 'locator': '10-worked-example.md, context register A', 'claim_class': 'Reported'}, {'id': 'SYN-003', 'title': 'Fictional invoice and matching confirmation', 'locator': '10-worked-example.md, context register B', 'claim_class': 'Observed'}, {'id': 'SYN-004', 'title': 'Fictional ownership confirmation', 'locator': '10-worked-example.md, context register C', 'claim_class': 'Observed'}, {'id': 'SYN-005', 'title': 'Fictional extract defect', 'locator': '10-worked-example.md, raw row R10', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Raw rows', 'value': 10, 'method': 'Count R01–R10 before deduplication', 'format': '#,##0'}, {'label': 'Processed transactions', 'value': 8, 'method': '10 raw minus 1 duplicate minus 1 unparsed', 'format': '#,##0'}, {'label': 'Known gross movement USD', 'value': 36300, 'method': '$18,000.00 credits plus $18,300.00 debits; excludes unknown R10 amount', 'format': '$#,##0.00'}, {'label': 'Rule matches', 'value': 2, 'method': 'A and B match TM-01; C excluded; D not assessable', 'format': '#,##0'}], 'limitations': ['Synthetic rules are illustrative and are not regulatory thresholds.', 'Account D has an unknown amount; total monetary completeness is not established.', 'No opening balances or complete external flow paths are supplied.'], 'conclusion': 'Two accounts match the illustrative rapid-movement rule. One has a supported invoice explanation; the other needs further review. A separate account remains not assessable because an amount is unreadable.', 'report_narrative': [['Two accounts match the illustrative rapid-movement rule. One has a supported invoice explanation; the other needs further review. A separate account remains not assessable because an amount is unreadable.'], ['The ten raw rows reconcile to eight processed transactions after the documented duplicate and exclusion decisions. The fictional scenario uses explicit amount, ratio and timing criteria; unreadable amounts remain outside assessable sums.'], ['TM-F01: Account A received $10,000.00 and sent $9,500.00 within two hours of the first receipt; the 95.0% ratio meets TM-01. Purpose remains unsupported.', 'TM-F02: The 96.0% rule match is retained; a matched supplier invoice supports the $4,800.00 payment.', 'TM-F03: One unreadable amount prevents account-level completeness; $1,000.00 is only the known posted debit.'], ['Known gross movement is $36,300.00 within the captured records. Account totals retain the relationship between incoming and outgoing activity; gross movement is not net loss, customer income or suspicious value.'], ['Two accounts meet the raw illustrative rapid-movement criterion. One has a supported invoice explanation, while the other remains a review lead. An additional account is not assessable because an amount is unreadable; it cannot be scored as a negative.'], ['The synthetic source rows and criterion definitions in file 10 support the arithmetic and matches. The public typology references do not supply a regulatory threshold or evidence of wrongdoing for these fictional accounts.'], ['Review the unexplained match, preserve the invoice explanation without deleting the raw match, and repair the unreadable amount before rerunning the affected account.'], ['Synthetic rules are illustrative and are not regulatory thresholds.', 'Account D has an unknown amount; total monetary completeness is not established.', 'No opening balances or complete external flow paths are supplied.', 'QA remains pending and no authorized human disposition is recorded.']], 'suite_id': 'transaction-monitoring', 'version': '1.1.0', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'as_of': '2026-10-09', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'TM-F01', 'proposal': 'Obtain payment purpose and counterparties; refer to the authorized reviewer.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'TM-F02', 'proposal': 'Document the explanation and seek human disposition; retain the rule hit.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'TM-F03', 'proposal': 'Repair the source extract and recompute D before making an account conclusion.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
