# Fraud Incident Review — fixed report template

Version 1.0.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Incident priorities and known exposure**
2. **Scope, incident population, and amount method**
3. **Findings and verification gaps**
4. **Requested, executed, and returned amounts**
5. **Authorization and incident-response review**
6. **Evidence and source provenance**
7. **Proposed actions for authorized responders**
8. **Limitations, quality checks, and human disposition**

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

DATA = {'slug': 'fraud-review', 'title': 'Fraud Incident Review', 'summary': 'Separate payment instructions from actual execution, verify authorization evidence, reconcile returns, and prepare proportionate incident actions for an authorized human responder.', 'audience': 'Fraud analysts, payment-control reviewers, incident coordinators, and quality reviewers', 'decision': 'What is known about authorization, execution, and remaining exposure, and which time-sensitive actions should an authorized responder consider?', 'palette': 'umber', 'report_sections': ['Incident priorities and known exposure', 'Scope, incident population, and amount method', 'Findings and verification gaps', 'Requested, executed, and returned amounts', 'Authorization and incident-response review', 'Evidence and source provenance', 'Proposed actions for authorized responders', 'Limitations, quality checks, and human disposition'], 'domain_tables': [{'name': 'IncidentAmounts', 'columns': ['case_id', 'currency', 'requested_amount', 'executed_amount', 'confirmed_return_amount', 'net_unreturned_amount', 'amount_status', 'review_state'], 'rows': [['F01', 'USD', 40000, 40000, 10000, 30000, 'CONFIRMED', 'SUSPECTED_FRAUD'], ['F02', 'USD', 15000, 0, 0, 0, 'CONFIRMED', 'PREVENTED_REQUEST'], ['F03', 'USD', 12000, None, None, None, 'EXECUTION_UNKNOWN', 'OPEN_ALLEGATION'], ['F04', 'USD', 5000, 5000, 0, 5000, 'CONFIRMED', 'BENIGN_SUPPORTED']], 'formats': {'requested_amount': '#,##0.00', 'executed_amount': '#,##0.00', 'confirmed_return_amount': '#,##0.00', 'net_unreturned_amount': '#,##0.00'}}, {'name': 'VerificationReview', 'columns': ['case_id', 'authorization_basis', 'detail_change', 'independent_verification', 'payment_status', 'time_sensitivity', 'proposed_action', 'evidence_ids'], 'rows': [['F01', 'Impersonated supplier instruction reported', 'New beneficiary', 'Known-channel supplier denial documented', 'EXECUTED_PARTIAL_RETURN', 'HIGH', 'Authorized fraud responder review and recovery assessment', 'SYN-001;SYN-002'], ['F02', 'Suspicious instruction identified before execution', 'New beneficiary', 'Request failed established verification', 'NOT_EXECUTED', 'MEDIUM', 'Preserve instruction and verify cancellation state', 'SYN-003;SYN-004'], ['F03', 'Employee reports unauthorized payroll change', 'Payroll destination changed', 'No independent logs or ledger supplied', 'UNKNOWN', 'HIGH', 'Obtain ledger and access logs through approved incident process', 'SYN-005;SYN-006'], ['F04', 'Amended contract and approved instruction', 'New beneficiary', 'Preexisting trusted-channel confirmation documented', 'EXECUTED', 'LOW', 'Document supported ordinary change and human disposition', 'SYN-007;SYN-008']]}], 'findings': [{'id': 'FR-F01', 'title': 'Suspected supplier impersonation has $30,000.00 unreturned', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001', 'SYN-002'], 'detail': 'F01 has a $40,000.00 posted payment and $10,000.00 confirmed linked return. The supplier denial is documented; ultimate loss and liability remain undecided.', 'recommendation': 'Route to the authorized fraud responder for time-sensitive review and permitted recovery assessment.'}, {'id': 'FR-F02', 'title': 'A prevented request must not be counted as executed loss', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-003', 'SYN-004'], 'detail': 'F02 requested $15,000.00 but the supplied instruction and ledger status confirm no execution.', 'recommendation': 'Retain the attempted request and verify the cancellation remains effective; do not claim an actual loss or proven savings.'}, {'id': 'FR-F03', 'title': 'Payroll allegation has unknown execution status', 'severity': 'HIGH', 'confidence': 'LOW', 'claim_class': 'Reported', 'evidence_ids': ['SYN-005', 'SYN-006'], 'detail': 'F03 reports $12,000.00 at issue, but neither posting records nor access logs are supplied.', 'recommendation': 'Obtain execution and authorization evidence urgently through the approved human process; keep exposure null.'}, {'id': 'FR-F04', 'title': 'A beneficiary change has a supported ordinary explanation', 'severity': 'LOW', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-007', 'SYN-008'], 'detail': 'F04 has a $5,000.00 ordinary payment supported by an amended contract and trusted-channel confirmation.', 'recommendation': 'Document the evidence and seek human disposition; exclude this payment from suspected-fraud exposure totals.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional supplier instruction and denial record', 'locator': '10-worked-example.md, source R01', 'claim_class': 'Reported'}, {'id': 'SYN-002', 'title': 'Fictional F01 ledger and return', 'locator': '10-worked-example.md, source R02', 'claim_class': 'Observed'}, {'id': 'SYN-003', 'title': 'Fictional suspicious request', 'locator': '10-worked-example.md, source R03', 'claim_class': 'Reported'}, {'id': 'SYN-004', 'title': 'Fictional rejected-instruction ledger state', 'locator': '10-worked-example.md, source R04', 'claim_class': 'Observed'}, {'id': 'SYN-005', 'title': 'Fictional payroll complaint', 'locator': '10-worked-example.md, source R05', 'claim_class': 'Reported'}, {'id': 'SYN-006', 'title': 'Fictional missing-source inventory', 'locator': '10-worked-example.md, source R06', 'claim_class': 'Observed'}, {'id': 'SYN-007', 'title': 'Fictional amended contract and confirmation', 'locator': '10-worked-example.md, source R07', 'claim_class': 'Observed'}, {'id': 'SYN-008', 'title': 'Fictional ordinary payment ledger', 'locator': '10-worked-example.md, source R08', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Requests reviewed', 'value': 4, 'method': 'Distinct cases F01–F04', 'format': '#,##0'}, {'label': 'Known requested amount USD', 'value': 72000, 'method': '40000+15000+12000+5000; includes alleged and ordinary requests, not loss', 'format': '$#,##0.00'}, {'label': 'Known suspected-fraud unreturned USD', 'value': 30000, 'method': 'F01 executed40000-return10000; F02 zero; F03 unknown; F04 excluded as ordinary', 'format': '$#,##0.00'}, {'label': 'Confirmed unexecuted request USD', 'value': 15000, 'method': 'F02 request amount with confirmed nonexecution; not measured savings', 'format': '$#,##0.00'}], 'limitations': ['The example does not establish legal liability, customer reimbursement, or final fraud loss.', 'F03 execution and recovery are unknown; its $12,000.00 request is not imputed as loss or zero exposure.', 'No recovery request, account restriction, external contact, or filing is executed by this suite.'], 'conclusion': 'Known suspected-fraud unreturned value is $30,000.00, with one payroll allegation still lacking execution evidence. A $15,000.00 request did not execute, and a supported ordinary $5,000.00 payment is excluded from the suspected-fraud subtotal.', 'report_narrative': [['Known suspected-fraud unreturned value is $30,000.00, with one payroll allegation still lacking execution evidence. A $15,000.00 request did not execute, and a supported ordinary $5,000.00 payment is excluded from the suspected-fraud subtotal.'], ['Four requests are reviewed using separate requested, executed, returned and unresolved amount states. The example contains one unexecuted request, one supported ordinary payment and one allegation without execution evidence.'], ['FR-F01: F01 has a $40,000.00 posted payment and $10,000.00 confirmed linked return. The supplier denial is documented; ultimate loss and liability remain undecided.', 'FR-F02: F02 requested $15,000.00 but the supplied instruction and ledger status confirm no execution.', 'FR-F03: F03 reports $12,000.00 at issue, but neither posting records nor access logs are supplied.', 'FR-F04: F04 has a $5,000.00 ordinary payment supported by an amended contract and trusted-channel confirmation.'], ['Known requested value is $72,000.00. Known suspected-fraud unreturned value is $30,000.00; the $15,000.00 unexecuted request is excluded from that subtotal, as is the supported ordinary $5,000.00 payment.'], ['The payroll allegation remains unresolved because execution evidence is missing. Verification and response steps remain proposed for authorized responders; the analytical record does not claim that funds were frozen, recalled or recovered.'], ['The fictional request, execution and return records in file 10 support distinct amount fields. Reported authorization and fraud allegations remain attributed; no assumption converts missing execution into a confirmed loss.'], ['Prioritize verification and the documented time-sensitive response options through authorized channels. Obtain payroll execution evidence and maintain the separation between suspected-fraud exposure, ordinary payments and unexecuted attempts.'], ['The example does not establish legal liability, customer reimbursement, or final fraud loss.', 'F03 execution and recovery are unknown; its $12,000.00 request is not imputed as loss or zero exposure.', 'No recovery request, account restriction, external contact, or filing is executed by this suite.', 'QA remains pending and no authorized human disposition is recorded.']], 'suite_id': 'fraud-review', 'version': '1.0.0', 'as_of': '2026-10-09', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'FR-F01', 'proposal': 'Route to the authorized fraud responder for time-sensitive review and permitted recovery assessment.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'FR-F02', 'proposal': 'Retain the attempted request and verify the cancellation remains effective; do not claim an actual loss or proven savings.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'FR-F03', 'proposal': 'Obtain execution and authorization evidence urgently through the approved human process; keep exposure null.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-004', 'finding_id': 'FR-F04', 'proposal': 'Document the evidence and seek human disposition; exclude this payment from suspected-fraud exposure totals.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
    places = 2 if '.00' in fmt else 1 if '.0' in fmt else 0
    return ('$' if '$' in fmt else '') + f'{value:,.{places}f}'

def table(headers, rows, keep_together=False):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = 'Table Grid'
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
        for cell in row.cells:
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
        table(['Evidence ID','Source or fixture','Exact locator'], [[e['id'],e['title'],e['locator']] for e in DATA['evidence']])
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
