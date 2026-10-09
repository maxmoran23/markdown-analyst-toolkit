# Third-Party Service and Assurance Review — fixed report template

Version 1.0.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Service reliance recommendation and restrictions**
2. **Relationship scope and assessment method**
3. **Material assurance findings**
4. **Service and fourth-party dependencies**
5. **Assurance evidence and test outcomes**
6. **Source provenance and coverage limitations**
7. **Remediation exit and review proposals**
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

DATA = {'slug': 'third-party-risk', 'title': 'Third-Party Service and Assurance Review', 'summary': 'Assess a defined service relationship, trace outsourced dependencies, and test whether supplied assurance supports the controls being relied upon.', 'audience': 'Third-party reviewers, service owners, and risk decision forums', 'decision': 'Does the evidence support reliance on the proposed service, and what must be resolved before a human acceptance decision?', 'palette': 'teal', 'report_sections': ['Service reliance recommendation and restrictions', 'Relationship scope and assessment method', 'Material assurance findings', 'Service and fourth-party dependencies', 'Assurance evidence and test outcomes', 'Source provenance and coverage limitations', 'Remediation exit and review proposals', 'Limitations quality review and human disposition'], 'domain_tables': [{'name': 'ServiceDependencies', 'columns': ['service_id', 'provider_role', 'service_function', 'data_access', 'dependency_id', 'substitutability', 'evidence_ids'], 'rows': [['SV01', 'Primary provider', 'Review decision service', 'Customer attributes', 'SV02;SV03', 'No immediate substitute', 'SYN-001'], ['SV02', 'Storage subcontractor', 'Hosted records', 'Stored customer attributes', None, 'Shared dependency', 'SYN-001'], ['SV03', 'Reference supplier', 'Reference data feed', 'Reference dataset', None, 'Alternative untested', 'SYN-001'], ['SV04', 'Support subcontractor', 'Incident support', 'Privileged support access', 'SV01', 'Alternative untested', 'SYN-001'], ['SV05', 'Proposed fallback provider', 'Fallback review service', 'Customer attributes', 'SV02', 'Shares storage dependency', 'SYN-001']]}, {'name': 'AssuranceReview', 'columns': ['review_id', 'domain', 'criterion', 'critical', 'result', 'evidence_ids'], 'rows': [['AR01', 'Service scope', 'Confirm service boundaries and accountable roles', False, 'SUPPORTED', 'SYN-001'], ['AR02', 'Assurance coverage', 'Evidence required controls for relevant period and subcontractor', True, 'PARTIAL', 'SYN-001'], ['AR03', 'Recovery', 'Demonstrate recovery within 4 hours and lag<=15 minutes', True, 'FAILED', 'SYN-001'], ['AR04', 'Exit', 'Reconcile complete export of 1000 test records', True, 'FAILED', 'SYN-001'], ['AR05', 'User controls', 'Evidence required customer-side access review', True, 'UNVERIFIED', 'SYN-001'], ['AR06', 'Contract', 'Confirm executed incident-notification terms', True, 'PARTIAL', 'SYN-001']]}], 'findings': [{'id': 'TP-F01', 'title': 'Assurance scope does not cover the entire relied-on service', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'The supplied report ends 2025-12-31 and excludes the storage subcontractor; a provider assertion does not extend independent testing.', 'recommendation': 'Obtain current and subcontractor-relevant evidence or propose an explicitly restricted reliance decision.'}, {'id': 'TP-F02', 'title': 'Recovery rehearsal misses the illustrative service criteria', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'Recovery takes6 hours against 4; observed replication lag20 minutes exceeds 15.', 'recommendation': 'Address the failure mechanism and retest service, data, and dependent controls.'}, {'id': 'TP-F03', 'title': 'Exit export has an unexplained record shortfall', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': '985 of 1000 fixture records are returned;15 remain unexplained.', 'recommendation': 'Reconcile missing IDs and repeat an end-to-end exit test before relying on portability.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional service relationship and six assurance checks', 'locator': '10-worked-example.md, dependency inventory and assurance evidence', 'claim_class': 'Observed'}, {'id': 'REF-001', 'title': 'Federal Reserve SR 23-4 Interagency Guidance on Third-Party Relationships', 'locator': 'https://www.federalreserve.gov/supervisionreg/srletters/sr2304.htm', 'claim_class': 'Reported'}, {'id': 'REF-002', 'title': 'OCC 2024-11 Third-Party Relationships: A Guide for Community Banks', 'locator': 'https://www.occ.gov/news-issuances/bulletins/2024/bulletin-2024-11.html', 'claim_class': 'Reported'}, {'id': 'REF-003', 'title': 'OCC 2026-46 Proposed Third-Party Risk Management Guidance', 'locator': 'https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-46.html', 'claim_class': 'Reported'}], 'metrics': [{'label': 'Mapped service dependencies', 'value': '5', 'method': 'Count SV01–SV05; fallback and primary share SV02.', 'format': '#,##0'}, {'label': 'Supported review criteria', 'value': '1 of 6 (16.7%)', 'method': 'SUPPORTED / six specified fixture criteria; no weighted acceptance score.', 'format': '#,##0'}, {'label': 'Exit record return', 'value': '985 of 1000 (98.5%)', 'method': 'Returned records / expected fixture population;15 unreconciled prevents completeness claim.', 'format': '#,##0'}], 'limitations': ['All providers, service facts, records, contract clauses, and tests are fictional.', 'An assurance report is limited by scope, period, exceptions, and user responsibilities.', 'A report period ending does not by itself mean the report has expired.', 'No onboarding, contracting, termination, or data transfer is authorized.'], 'conclusion': 'The fictional service review has unresolved assurance, recovery, exit, user-control, and contract conditions. The evidence does not support unrestricted reliance; remediation, retest, and an authorized human disposition are required.', 'report_narrative': [['The fixture does not support unrestricted reliance on the service. Assurance coverage, recovery, exit completeness, user-control evidence, and contract support remain unresolved and require human disposition.'], ['The unit of review is a fictional decision service and its five mapped dependencies. The six review criteria include five critical reliance conditions; targets are illustrative and tailored to this fixture.'], ['The assurance report leaves a later coverage interval and excludes storage. Recovery and data-lag tests miss their criteria, while the exit export omits fifteen expected records. Missing user-control evidence and unsigned contract terms remain additional conditions.'], ['The primary provider SV01 and proposed fallback SV05 share storage dependency SV02. The fallback therefore cannot be treated as independent protection from that storage failure without further architecture and recovery evidence.'], ['AssuranceReview contains one SUPPORTED, two PARTIAL, two FAILED, and one UNVERIFIED result. Recovery takes six hours against four, data lag is twenty minutes against fifteen, and export returns 985 of 1,000 expected records, or 98.5%.'], ['SYN-001 defines the complete fictional service and test package. A report period ending is not an invented expiry, and a management bridge assertion is not independent testing. The September 2026 third-party guidance source is a proposal, separately labelled from existing final references.'], ['Propose relevant assurance coverage, a recovery retest including shared storage, full exit reconciliation, inspection of customer-side access review, and executed-term verification. Any conditional reliance requires feasible interim measures and authorized acceptance.'], ['QA rejects unsupported permanent-loss claims, blanket certification reliance, and averaging away critical failures. No onboarding, renewal, contract acceptance, termination, or data transfer occurred.']], 'suite_id': 'third-party-risk', 'version': '1.0.0', 'as_of': '2026-10-09', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'TP-F01', 'proposal': 'Obtain current and subcontractor-relevant evidence or propose an explicitly restricted reliance decision.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'TP-F02', 'proposal': 'Address the failure mechanism and retest service, data, and dependent controls.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'TP-F03', 'proposal': 'Reconcile missing IDs and repeat an end-to-end exit test before relying on portability.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
