# OSINT Research — fixed report template

Version 1.0.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Research decision brief**
2. **Scope and coverage method**
3. **Material findings**
4. **Claim assessment**
5. **Search coverage and contradictions**
6. **Evidence record**
7. **Recommended research actions**
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

DATA = {'slug': 'osint-research', 'title': 'OSINT Research', 'summary': 'Assess public claims with identity resolution, source lineage, contradictions, and bounded search coverage.', 'audience': 'Researchers and analysts preparing evidence-backed public-source briefs', 'decision': 'Which claims are sufficiently supported to cite, and what must be resolved first?', 'palette': 'slate', 'report_sections': ['Research decision brief', 'Scope and coverage method', 'Material findings', 'Claim assessment', 'Search coverage and contradictions', 'Evidence record', 'Recommended research actions', 'Limitations and human review'], 'domain_tables': [{'name': 'Claims', 'columns': ['claim_id', 'proposition', 'claim_class', 'status', 'confidence', 'support_families', 'contradiction_ids', 'evidence_ids', 'notes'], 'rows': [['C-01', 'Aster Quay Research is recorded active in the fictional registry', 'Observed', 'SUPPORTED', 'HIGH', 1, '', 'SYN-001', 'Registry status only; does not establish operating activity'], ['C-02', 'Aster Quay Research has a current research-services license', 'Reported', 'CONTRADICTED', 'MODERATE', 1, 'D-03', 'SYN-001', 'Company page says current; fictional regulator extract shows expired'], ['C-03', 'Aster Quay Research has 240 employees', 'Reported', 'UNRESOLVED', 'LOW', 1, '', 'SYN-001', 'Two publications repeat the same company statement'], ['C-04', 'The alleged award was granted to the subject', 'Reported', 'IDENTITY UNRESOLVED', 'NOT ASSESSABLE', 0, '', 'SYN-001', 'Award names a similarly named entity with a different registration ID']]}, {'name': 'SearchCoverage', 'columns': ['query_id', 'question', 'source_family', 'scope', 'review_status', 'items_reviewed', 'eligible_items', 'evidence_ids', 'limitation'], 'rows': [['Q-01', 'Legal identity', 'F-REG', 'Fictional registry extract', 'REVIEWED', 1, 1, 'SYN-001', 'Supplied snapshot only'], ['Q-02', 'Current license', 'F-LIC', 'Fictional license extract', 'REVIEWED', 1, 1, 'SYN-001', 'Status at snapshot date only'], ['Q-03', 'Employee count', 'F-COMPANY', 'Company page plus two repeated stories', 'REVIEWED', 3, 3, 'SYN-001', 'One upstream assertion'], ['Q-04', 'Award identity', 'F-AWARD', 'Fictional award register', 'REVIEWED', 1, 0, 'SYN-001', 'Different registration identifier'], ['Q-05', 'Court outcome', 'F-COURT', 'Requested fictional docket', 'ACCESS LIMITED', 0, 0, 'SYN-001', 'No docket supplied']]}], 'findings': [{'id': 'F-01', 'title': 'License claim conflicts with supplied register', 'severity': 'HIGH', 'confidence': 'MODERATE', 'claim_class': 'Inferred', 'evidence_ids': ['SYN-001'], 'detail': 'Fictional D-02 claims a current license while D-03 records expiration for AQ-104.', 'recommendation': 'Obtain current licensing and renewal evidence before relying on the claim.'}, {'id': 'F-02', 'title': 'Staffing reports share one origin', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'D-02, D-04, and D-05 repeat one company assertion of 240 employees.', 'recommendation': 'Attribute the figure or seek independent measurement.'}, {'id': 'F-03', 'title': 'Award record identifies a different entity', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'D-06 names AQ-901 rather than target AQ-104.', 'recommendation': 'Exclude from support unless identity linkage is evidenced.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional OSINT case', 'locator': '10-worked-example.md, D-01 through D-06 and Q-05 gap', 'claim_class': 'Observed'}, {'id': 'REF-PROV', 'title': 'W3C PROV Overview', 'locator': 'https://www.w3.org/TR/prov-overview/', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Material claims', 'value': '4', 'method': 'Count distinct C-01 through C-04.', 'format': '#,##0'}, {'label': 'Planned-search completion', 'value': '80.0%', 'method': '4 REVIEWED planned searches / 5 planned searches × 100.', 'format': '#,##0'}, {'label': 'Eligible source items', 'value': '5 of 6', 'method': 'Six reviewed items less D-06 different-identifier item.', 'format': '#,##0'}], 'limitations': ['All case data are fictional; no operational validation is implied.', 'Five planned searches do not represent the entire public information universe.', 'A register status is bounded to its date, identity, and scope.'], 'metadata': {'conclusion': 'One of four fictional claims is supported within the supplied registry scope. The license claim is contradicted, the staffing claim has one upstream origin, and the award identity is unresolved; one planned search remains access-limited.'}, 'report_narrative': [['One of four fictional claims is supported within the supplied registry scope. The license claim is contradicted, the staffing claim has one upstream origin, and the award identity is unresolved; one planned search remains access-limited.'], ['The review tests four propositions about fictional AQ-104 against six supplied items and five planned searches. Four searches were completed; the absent court docket remains a coverage gap.'], ['F-01: Fictional D-02 claims a current license while D-03 records expiration for AQ-104.', 'F-02: D-02, D-04, and D-05 repeat one company assertion of 240 employees.', 'F-03: D-06 names AQ-901 rather than target AQ-104.'], ['The active registry entry supports legal status at its cutoff only. The licensing statement is contradicted, the 240-employee assertion has only one upstream origin, and the award cannot be attributed across different registration identifiers.'], ['Five of six reviewed items are eligible for the subject. Three staffing publications count as one source family. Completing four of five searches gives 80.0% planned-search completion, with no claim about the completeness of the public record.'], ['SYN-001 resolves to D-01 through D-06 and the search plan in file 10. D-03 contradicts the licensing claim; D-06 identifies AQ-901 rather than AQ-104. No court outcome is evidenced.'], ['Prioritize current licensing evidence, independent staffing support, and the missing docket. Keep the award excluded unless identity linkage is demonstrated.'], ['All case data are fictional; no operational validation is implied.', 'Five planned searches do not represent the entire public information universe.', 'A register status is bounded to its date, identity, and scope.', 'QA remains pending and no authorized human disposition is recorded.']], 'suite_id': 'osint-research', 'version': '1.0.0', 'as_of': '2026-10-09', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'conclusion': 'One of four fictional claims is supported within the supplied registry scope. The license claim is contradicted, the staffing claim has one upstream origin, and the award identity is unresolved; one planned search remains access-limited.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'F-01', 'proposal': 'Obtain current licensing and renewal evidence before relying on the claim.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'F-02', 'proposal': 'Attribute the figure or seek independent measurement.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'F-03', 'proposal': 'Exclude from support unless identity linkage is evidenced.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
