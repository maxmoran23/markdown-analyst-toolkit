# Regulatory Change and Obligation Mapping — fixed report template

Version 1.0.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Change priorities and restricted conclusion**
2. **Scope status and applicability method**
3. **Material readiness findings**
4. **Instrument register and date status**
5. **Obligation mapping and readiness**
6. **Source evidence and unresolved authority**
7. **Implementation and verification proposals**
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

DATA = {'slug': 'regulatory-change', 'title': 'Regulatory Change and Obligation Mapping', 'summary': 'Translate a supplied public-source change set into provision-level applicability, readiness, and evidence questions without turning proposals into current obligations.', 'audience': 'Regulatory analysts, control owners, and legal reviewers', 'decision': 'Which changes require verified applicability and implementation action, and which remain watch or research items?', 'palette': 'umber', 'report_sections': ['Change priorities and restricted conclusion', 'Scope status and applicability method', 'Material readiness findings', 'Instrument register and date status', 'Obligation mapping and readiness', 'Source evidence and unresolved authority', 'Implementation and verification proposals', 'Limitations quality review and human disposition'], 'domain_tables': [{'name': 'ChangeRegister', 'columns': ['change_id', 'instrument_status', 'applicability', 'effective_date', 'compliance_date', 'owner_role', 'priority', 'evidence_ids'], 'rows': [['CH01', 'PROPOSED', 'Conditional', None, None, 'Regulatory analysis', 'MEDIUM', 'SYN-001'], ['CH02', 'FINAL_NOT_EFFECTIVE', 'In scope', '2026-11-01', '2026-12-01', 'Records owner', 'MEDIUM', 'SYN-001'], ['CH03', 'EFFECTIVE', 'In scope', '2026-09-01', '2026-10-01', 'Review owner', 'HIGH', 'SYN-001'], ['CH04', 'GUIDANCE', 'Reference only', None, None, 'Governance owner', 'LOW', 'SYN-001'], ['CH05', 'WITHDRAWN', 'Not current', None, None, 'Regulatory analysis', 'LOW', 'SYN-001'], ['CH06', 'STATUS_UNVERIFIED', 'Unresolved', None, None, 'Legal review', 'HIGH', 'SYN-001']]}, {'name': 'ObligationMap', 'columns': ['obligation_id', 'change_id', 'requirement_summary', 'control_id', 'readiness', 'compliance_date', 'evidence_ids'], 'rows': [['OB01', 'CH02', 'Retain a review log under fictional provision2', 'CTRL-LOG', 'BUILD', '2026-12-01', 'SYN-001'], ['OB02', 'CH03', 'Evidence escalation review under fictional provision3a', 'CTRL-REV', 'EVIDENCE GAP', '2026-10-01', 'SYN-001'], ['OB03', 'CH03', 'Complete role training under fictional provision3b', 'CTRL-TRN', 'VERIFIED FOR FIXTURE', '2026-10-01', 'SYN-001'], ['OB04', 'CH01', 'Potential reporting field under proposed provision1', 'CTRL-PROP', 'SCENARIO ONLY', None, 'SYN-001'], ['OB05', 'CH04', 'Consider governance review practice', 'CTRL-GOV', 'REFERENCE ONLY', None, 'SYN-001']]}], 'findings': [{'id': 'RC-F01', 'title': 'Evidence for an effective fictional requirement remains missing', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'OB02 has no retained review evidence as of 2026-10-09; the fictional compliance date is 2026-10-01. A legal breach is not established by missing evidence alone.', 'recommendation': 'Obtain execution evidence and route the applicability and consequence assessment to an authorized reviewer.'}, {'id': 'RC-F02', 'title': 'A near-term claimed change lacks primary-source status confirmation', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'CH06 is supported only by a fictional secondary summary. Its claimed date is not copied into confirmed deadline fields.', 'recommendation': 'Retrieve primary material or keep status unverified and document interim review needs.'}, {'id': 'RC-F03', 'title': 'Future final requirement needs implementation evidence', 'severity': 'MEDIUM', 'confidence': 'MODERATE', 'claim_class': 'Inferred', 'evidence_ids': ['SYN-001'], 'detail': 'OB01 remains in build status ahead of the fictional 2026-12-01 compliance date. Readiness has not been evidenced.', 'recommendation': 'Define accountable milestones and acceptance tests for human approval.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional six-instrument change set and implementation evidence', 'locator': '10-worked-example.md, source cards and obligation mapping', 'claim_class': 'Observed'}, {'id': 'REF-001', 'title': 'National Archives Federal Register Tutorial', 'locator': 'https://www.archives.gov/federal-register/tutorial/text', 'claim_class': 'Reported'}, {'id': 'REF-002', 'title': 'Administrative Procedure Act,5 U.S.C. 553', 'locator': 'https://www.archives.gov/federal-register/laws/administrative-procedure/553.html', 'claim_class': 'Reported'}, {'id': 'REF-003', 'title': 'National Archives Office of the Federal Register FAQs', 'locator': 'https://www.archives.gov/federal-register/faqs', 'claim_class': 'Reported'}], 'metrics': [{'label': 'Tracked instruments', 'value': '6', 'method': 'Distinct CH01–CH06 source cards, preserving proposed, withdrawn, and unverified states.', 'format': '#,##0'}, {'label': 'Confirmed final in-scope instruments', 'value': '2', 'method': 'CH02 final-not-effective plus CH03 effective; excludes guidance and proposals.', 'format': '#,##0'}, {'label': 'Effective mapped evidence coverage', 'value': '1 of 2 (50.0%)', 'method': 'OB03 verified / OB02 and OB03 effective mapped requirements; not a compliance score.', 'format': '#,##0'}], 'limitations': ['All six change instruments and organization facts are fictional.', 'A proposal, guidance item, or secondary report is not a verified current legal obligation.', 'Missing execution evidence does not alone prove legal noncompliance.', 'Readiness counts do not measure the completeness of all applicable legal obligations.'], 'conclusion': 'Prioritize the missing evidence for OB02 and primary-source confirmation for CH06 while planning the future CH02 requirement. One of two effective mapped fixture requirements has verified evidence; this is evidence coverage, not a compliance score.', 'report_narrative': [['Prioritize OB02’s evidence gap and CH06’s missing primary-source confirmation, while planning CH02’s future requirement. One of two effective mapped fixture requirements has verified evidence; this is not a compliance score.'], ['The review is as of Oct 09, 2026 and covers six invented instruments for a fictional Type A entity carrying Activity Q. Status, applicability, dates, and readiness are assessed separately using the complete source cards in SYN-001.'], ['OB02 lacks execution evidence after its explicit fictional compliance date. CH06 has only a secondary claim and no confirmed deadline. OB01 remains in build status ahead of its future compliance date; that supports a readiness concern, not a prediction of missed implementation.'], ['ChangeRegister preserves one proposed, one final-not-effective, one effective, one guidance, one withdrawn, and one unverified item. Only CH02 and CH03 have confirmed effective and compliance dates in the fixture.'], ['ObligationMap has five rows: one future requirement, two effective requirements, one proposal scenario, and one reference item. The effective evidence denominator is OB02 and OB03; only OB03 is verified for the fixture, giving 1/2 = 50.0%.'], ['SYN-001 contains fictional source cards and implementation evidence. CH06’s claimed Oct 15 date remains in the evidence narrative rather than confirmed deadline fields. The National Archives references support research method, not the invented legal requirements.'], ['Propose retrieval of OB02 evidence, primary verification for CH06, and accountable acceptance milestones for OB01. Keep CH01 as scenario planning, CH04 as reference context, and CH05 as historical withdrawal.'], ['QA rejects proposal-to-obligation conversion, comment-date substitution, and breach conclusions from missing evidence alone. Human reviewers retain legal interpretation, applicability, commitments, and final readiness decisions.']], 'suite_id': 'regulatory-change', 'version': '1.0.0', 'as_of': '2026-10-09', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'RC-F01', 'proposal': 'Obtain execution evidence and route the applicability and consequence assessment to an authorized reviewer.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'RC-F02', 'proposal': 'Retrieve primary material or keep status unverified and document interim review needs.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'RC-F03', 'proposal': 'Define accountable milestones and acceptance tests for human approval.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
