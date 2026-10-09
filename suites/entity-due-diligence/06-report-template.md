# Entity Due Diligence — fixed report template

Version 1.0.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Entity decision brief**
2. **Scope and review method**
3. **Material findings**
4. **Ownership assessment**
5. **Profile and evidence gaps**
6. **Evidence record**
7. **Recommended diligence actions**
8. **Limitations and human review**

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

DATA = {'slug': 'entity-due-diligence', 'title': 'Entity Due Diligence', 'summary': 'Build an identity-resolved entity profile with ownership, permissions, business purpose, and explicit evidence gaps.', 'audience': 'Analysts conducting generic public-source entity diligence', 'decision': 'Is the profile sufficiently supported for the stated research purpose, or what evidence and specialist review are needed?', 'palette': 'umber', 'report_sections': ['Entity decision brief', 'Scope and review method', 'Material findings', 'Ownership assessment', 'Profile and evidence gaps', 'Evidence record', 'Recommended diligence actions', 'Limitations and human review'], 'domain_tables': [{'name': 'Ownership', 'columns': ['edge_id', 'owner_id', 'owned_entity_id', 'interest_pct', 'interest_basis', 'effective_date', 'source_status', 'evidence_ids', 'notes'], 'rows': [['O-01', 'PERSON-A', 'HOLDCO-A', 60, 'Ordinary economic equity', '2026-09-30', 'REPORTED', 'SYN-001', 'Fictional ownership schedule'], ['O-02', 'PERSON-B', 'HOLDCO-A', 40, 'Ordinary economic equity', '2026-09-30', 'REPORTED', 'SYN-001', 'Fictional ownership schedule'], ['O-03', 'HOLDCO-A', 'ENTITY-Q', 70, 'Ordinary economic equity', '2026-09-30', 'REPORTED', 'SYN-001', 'Do not confuse with sanctions propagation'], ['O-04', 'PERSON-C', 'ENTITY-Q', 20, 'Ordinary economic equity', '2026-09-30', 'REPORTED', 'SYN-001', 'Direct interest'], ['O-05', 'UNKNOWN-POOL', 'ENTITY-Q', 10, 'Ordinary economic equity', '2026-09-30', 'UNKNOWN', 'SYN-001', 'Underlying holders not supplied']], 'formats': {'interest_pct': '0.0"%"'}}, {'name': 'ProfileGaps', 'columns': ['item_id', 'dimension', 'expected_evidence', 'observed_state', 'materiality', 'assessment', 'evidence_ids', 'next_step'], 'rows': [['P-01', 'Legal identity', 'Registry identifier and status', 'ENTITY-Q active in supplied fictional extract', 'HIGH', 'SUPPORTED', 'SYN-001', 'Refresh for actual decision date'], ['P-02', 'Ownership', 'Complete dated ownership schedule', '10 percent terminal ownership unresolved', 'HIGH', 'INCOMPLETE', 'SYN-001', 'Identify underlying holders and control rights'], ['P-03', 'Business purpose', 'Product and expected-activity description', 'Company reports monthly receipts of $600,000.00', 'MEDIUM', 'REPORTED', 'SYN-001', 'Corroborate business model and expected counterparties'], ['P-04', 'License', 'Entity-specific permission for proposed service', 'Group license belongs to separate ENTITY-R', 'HIGH', 'UNRESOLVED', 'SYN-001', 'Obtain target entity permission or scope rationale'], ['P-05', 'Adverse event', 'Underlying order and current procedural status', 'Article references a proceeding; order absent', 'MEDIUM', 'NOT ASSESSED', 'SYN-001', 'Obtain public underlying record']]}], 'findings': [{'id': 'F-01', 'title': 'Terminal ownership remains incomplete', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': '10.0% of comparable economic ownership has no identified underlying holder in the fictional schedule.', 'recommendation': 'Obtain missing holder details and separate control-right evidence.'}, {'id': 'F-02', 'title': 'Target permission has not been demonstrated', 'severity': 'HIGH', 'confidence': 'MODERATE', 'claim_class': 'Inferred', 'evidence_ids': ['SYN-001'], 'detail': 'The supplied group license names ENTITY-R while the contemplated service concerns ENTITY-Q.', 'recommendation': 'Resolve target-entity scope and applicable permission requirements.'}, {'id': 'F-03', 'title': 'Receipts annualization is assumption-dependent', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': '$7,200,000.00 is a constant-month scenario from reported $600,000.00 monthly receipts.', 'recommendation': 'Seek comparable financial evidence before relying on capacity claims.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional entity diligence case', 'locator': '10-worked-example.md, ownership and profile records', 'claim_class': 'Observed'}, {'id': 'REF-CDD', 'title': 'FinCEN CDD overview', 'locator': 'https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule', 'claim_class': 'Observed'}, {'id': 'REF-CDD-2026', 'title': 'FinCEN FIN-2026-R001', 'locator': 'https://www.fincen.gov/system/files/2026-02/FinCEN-Order-CCDExceptiveRelief.pdf', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Resolved terminal economic interest', 'value': '90.0%', 'method': '42.0% Person A + 28.0% Person B + 20.0% Person C under stated comparable-equity assumptions.', 'format': '#,##0'}, {'label': 'Unresolved terminal interest', 'value': '10.0%', 'method': '100.0% less 90.0% known terminal interests.', 'format': '#,##0'}, {'label': 'Annualized receipts scenario', 'value': '$7,200,000.00', 'method': 'Reported $600,000.00 monthly receipts × 12; constant-month assumption, not annual revenue.', 'format': '#,##0'}], 'limitations': ['All facts are fictional and ownership assertions are not independently verified.', 'Economic equity multiplication does not determine sanctions blocking or legal beneficial-owner status.', 'Control rights, target permission, and underlying adverse-event record are absent.'], 'metadata': {'conclusion': 'The fictional profile resolves 90.0% of comparable terminal economic ownership, leaving 10.0% unidentified. Target-entity permission, control rights, and the underlying adverse-event record remain unresolved; the receipts annualization is only a scenario.'}, 'report_narrative': [['The fictional profile resolves 90.0% of comparable terminal economic ownership, leaving 10.0% unidentified. Target-entity permission, control rights, and the underlying adverse-event record remain unresolved; the receipts annualization is only a scenario.'], ['The review concerns fictional ENTITY-Q, the dated ownership schedule, reported business profile and supplied group license. The legal identity, economic ownership, control rights, activity expectations and entity-specific permission are assessed separately.'], ['F-01: 10.0% of comparable economic ownership has no identified underlying holder in the fictional schedule.', 'F-02: The supplied group license names ENTITY-R while the contemplated service concerns ENTITY-Q.', 'F-03: $7,200,000.00 is a constant-month scenario from reported $600,000.00 monthly receipts.'], ['PERSON-A has a 42.0% proportional economic interest through HOLDCO-A; PERSON-B has 28.0%; PERSON-C holds 20.0% directly. The remaining 10.0% is unresolved, and these calculations do not identify control rights or determine sanctions status.'], ['The group license names ENTITY-R, so permission for ENTITY-Q is unproven. Reported monthly receipts of $600,000.00 imply a $7,200,000.00 constant-month annualized scenario, not verified annual revenue. The underlying adverse-event order is absent.'], ['SYN-001 supplies the fictional registry, schedule and profile assertions. The group license and news reference retain their entity and procedural limits; public methodology references do not corroborate fictional subject facts.'], ['Obtain the missing holders, rights instruments, target-specific permission and underlying public order before accepting the unresolved dimensions. Corroborate receipts with comparable financial evidence.'], ['All facts are fictional and ownership assertions are not independently verified.', 'Economic equity multiplication does not determine sanctions blocking or legal beneficial-owner status.', 'Control rights, target permission, and underlying adverse-event record are absent.', 'QA remains pending and no authorized human disposition is recorded.']], 'suite_id': 'entity-due-diligence', 'version': '1.0.0', 'as_of': '2026-10-09', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'conclusion': 'The fictional profile resolves 90.0% of comparable terminal economic ownership, leaving 10.0% unidentified. Target-entity permission, control rights, and the underlying adverse-event record remain unresolved; the receipts annualization is only a scenario.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'F-01', 'proposal': 'Obtain missing holder details and separate control-right evidence.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'F-02', 'proposal': 'Resolve target-entity scope and applicable permission requirements.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'F-03', 'proposal': 'Seek comparable financial evidence before relying on capacity claims.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
