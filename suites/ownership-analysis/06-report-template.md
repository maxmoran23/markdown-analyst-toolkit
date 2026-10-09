# Ownership Analysis — fixed report template

Version 1.0.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Ownership decision brief**
2. **Scope and graph method**
3. **Material findings**
4. **Direct ownership assessment**
5. **Ultimate interests and unresolved branches**
6. **Evidence record**
7. **Recommended ownership review actions**
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

DATA = {'slug': 'ownership-analysis', 'title': 'Ownership Analysis', 'summary': 'Trace dated ownership edges, economic paths, unresolved branches, and control rights with separate legal overlays.', 'audience': 'Analysts reviewing layered ownership structures and public ownership disclosures', 'decision': 'Which ultimate economic interests are supported by the dated graph, and what evidence or interpretation remains missing?', 'palette': 'indigo', 'report_sections': ['Ownership decision brief', 'Scope and graph method', 'Material findings', 'Direct ownership assessment', 'Ultimate interests and unresolved branches', 'Evidence record', 'Recommended ownership review actions', 'Limitations and human review'], 'domain_tables': [{'name': 'OwnershipEdges', 'columns': ['edge_id', 'owner_id', 'owned_entity_id', 'interest_pct', 'interest_basis', 'effective_date', 'evidence_ids', 'notes'], 'formats': {'interest_pct': '0.0"%"'}, 'rows': [['OW-01', 'PERSON-A', 'HOLDCO', 60, 'Ordinary economic equity', '2026-09-30', 'SYN-001', 'Fictional supplied schedule'], ['OW-02', 'PERSON-B', 'HOLDCO', 40, 'Ordinary economic equity', '2026-09-30', 'SYN-001', 'Fictional supplied schedule'], ['OW-03', 'HOLDCO', 'TARGET', 50, 'Ordinary economic equity', '2026-09-30', 'SYN-001', 'Intermediate holding'], ['OW-04', 'PERSON-A', 'TARGET', 10, 'Ordinary economic equity', '2026-09-30', 'SYN-001', 'Separate direct holding'], ['OW-05', 'PERSON-C', 'TARGET', 25, 'Ordinary economic equity', '2026-09-30', 'SYN-001', 'Reported veto right assessed separately'], ['OW-06', 'UNKNOWN-POOL', 'TARGET', 15, 'Ordinary economic equity', '2026-09-30', 'SYN-001', 'Amount known; holders unresolved']]}, {'name': 'UltimateInterests', 'columns': ['ultimate_id', 'target_id', 'economic_interest_pct', 'path_ids', 'resolution_state', 'control_state', 'claim_class', 'evidence_ids', 'notes'], 'formats': {'economic_interest_pct': '0.0"%"'}, 'rows': [['PERSON-A', 'TARGET', 40, 'OW-01>OW-03;OW-04', 'RESOLVED ON SUPPLIED GRAPH', 'NOT ASSESSED', 'Estimated', 'SYN-001', '60 percent × 50 percent + 10 percent'], ['PERSON-B', 'TARGET', 20, 'OW-02>OW-03', 'RESOLVED ON SUPPLIED GRAPH', 'NOT ASSESSED', 'Estimated', 'SYN-001', '40 percent × 50 percent'], ['PERSON-C', 'TARGET', 25, 'OW-05', 'RESOLVED ON SUPPLIED GRAPH', 'REPORTED RIGHTS', 'Reported', 'SYN-001', 'Veto scope and legal effect not established'], ['UNKNOWN-POOL', 'TARGET', 15, 'OW-06', 'UNRESOLVED', 'NOT ASSESSED', 'Reported', 'SYN-001', 'Do not allocate residual to known holders']]}], 'findings': [{'id': 'F-01', 'title': 'Unidentified holders account for 15.0%', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'UNKNOWN-POOL holds a reported 15.0% direct target interest without identified underlying holders.', 'recommendation': 'Obtain the missing holder schedule and effective-date evidence.'}, {'id': 'F-02', 'title': 'Known terminal economic interests total 85.0%', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Estimated', 'evidence_ids': ['SYN-001'], 'detail': 'Person A 40.0% + Person B 20.0% + Person C 25.0% under proportional acyclic assumptions.', 'recommendation': 'Preserve path arithmetic, reported-source status, and separate legal questions.'}, {'id': 'F-03', 'title': 'Reported veto right lacks supporting instrument', 'severity': 'MEDIUM', 'confidence': 'LOW', 'claim_class': 'Reported', 'evidence_ids': ['SYN-001'], 'detail': 'Person C reportedly has a veto over certain asset sales; scope and governing document are absent.', 'recommendation': 'Obtain rights evidence before drawing a control conclusion.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional ownership graph', 'locator': '10-worked-example.md, OW-01 through OW-06', 'claim_class': 'Observed'}, {'id': 'REF-CDD', 'title': 'FinCEN CDD overview', 'locator': 'https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule', 'claim_class': 'Observed'}, {'id': 'REF-CDD-2026', 'title': 'FinCEN FIN-2026-R001', 'locator': 'https://www.fincen.gov/system/files/2026-02/FinCEN-Order-CCDExceptiveRelief.pdf', 'claim_class': 'Observed'}, {'id': 'REF-OFAC-401', 'title': 'OFAC FAQ 401', 'locator': 'https://ofac.treasury.gov/faqs/401', 'claim_class': 'Observed'}, {'id': 'REF-OFAC-398', 'title': 'OFAC FAQ 398', 'locator': 'https://ofac.treasury.gov/faqs/398', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Known terminal economic interests', 'value': '85.0%', 'method': '40.0% Person A + 20.0% Person B + 25.0% Person C.', 'format': '#,##0'}, {'label': 'Unresolved economic interest', 'value': '15.0%', 'method': '100.0% less 85.0% known terminal interests.', 'format': '#,##0'}, {'label': 'Direct edges', 'value': '6', 'method': 'Count distinct OW-01 through OW-06; no graph-wide percentage sum.', 'format': '#,##0'}], 'limitations': ['All holdings and rights are fictional reported inputs.', 'Simple path multiplication requires comparable proportional rights and no cycles or overlap.', 'Economic interest, control, legal beneficial ownership, and sanctions propagation are distinct questions.'], 'metadata': {'conclusion': 'The fictional graph supports estimated economic interests of 40.0% for Person A, 20.0% for Person B, and a reported 25.0% for Person C. A further 15.0% remains unresolved, and the reported veto right requires evidence before any control conclusion.'}, 'report_narrative': [['The fictional graph supports estimated economic interests of 40.0% for Person A, 20.0% for Person B, and a reported 25.0% for Person C. A further 15.0% remains unresolved, and the reported veto right requires evidence before any control conclusion.'], ['The review uses six dated direct ownership edges for an acyclic, proportional economic-equity graph. It assesses path arithmetic and unresolved branches separately from control, legal beneficial ownership and sanctions propagation.'], ['F-01: UNKNOWN-POOL holds a reported 15.0% direct target interest without identified underlying holders.', 'F-02: Person A 40.0% + Person B 20.0% + Person C 25.0% under proportional acyclic assumptions.', 'F-03: Person C reportedly has a veto over certain asset sales; scope and governing document are absent.'], ['HOLDCO is owned 60.0% by PERSON-A and 40.0% by PERSON-B. TARGET is held 50.0% by HOLDCO, 10.0% directly by PERSON-A, 25.0% by PERSON-C and 15.0% by unidentified holders. Distinct direct and indirect holdings are retained.'], ['PERSON-A has 60.0% × 50.0% + 10.0% = 40.0%; PERSON-B has 40.0% × 50.0% = 20.0%; PERSON-C has 25.0%. Resolved terminal interests total 85.0%; the 15.0% residual is not reallocated. The reported veto right lacks its supporting instrument.'], ['SYN-001 supplies the fictional reported schedule and rights assertion. The arithmetic is conditional on comparable proportional rights and no overlapping or circular interests; source verification remains distinct from calculation.'], ['Obtain the missing holder schedule and rights instrument. Reassess effective dates, share classes and path overlap before carrying these economic results into any separate legal test.'], ['All holdings and rights are fictional reported inputs.', 'Simple path multiplication requires comparable proportional rights and no cycles or overlap.', 'Economic interest, control, legal beneficial ownership, and sanctions propagation are distinct questions.', 'QA remains pending and no authorized human disposition is recorded.']], 'suite_id': 'ownership-analysis', 'version': '1.0.0', 'as_of': '2026-10-09', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'conclusion': 'The fictional graph supports estimated economic interests of 40.0% for Person A, 20.0% for Person B, and a reported 25.0% for Person C. A further 15.0% remains unresolved, and the reported veto right requires evidence before any control conclusion.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'F-01', 'proposal': 'Obtain the missing holder schedule and effective-date evidence.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'F-02', 'proposal': 'Preserve path arithmetic, reported-source status, and separate legal questions.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'F-03', 'proposal': 'Obtain rights evidence before drawing a control conclusion.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
