# Data Quality and Fitness for Use — fixed report template

Version 1.0.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Fitness recommendation and restrictions**
2. **Scope data contract and method**
3. **Material defects and findings**
4. **Record population and lineage**
5. **Rule outcomes and hard gates**
6. **Evidence and source limitations**
7. **Remediation reconciliation and retest**
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

DATA = {'slug': 'data-quality', 'title': 'Data Quality and Fitness for Use', 'summary': 'Assess whether a defined dataset can support a specific analytical or control purpose, with record-level defects and explicit release restrictions.', 'audience': 'Data stewards, control analysts, and review teams', 'decision': 'Is the supplied dataset sufficiently supported for the stated use, and which defects require human resolution?', 'palette': 'teal', 'report_sections': ['Fitness recommendation and restrictions', 'Scope data contract and method', 'Material defects and findings', 'Record population and lineage', 'Rule outcomes and hard gates', 'Evidence and source limitations', 'Remediation reconciliation and retest', 'Limitations quality review and human disposition'], 'domain_tables': [{'name': 'DataRecords', 'columns': ['record_id', 'customer_id', 'entity_type', 'full_name', 'date_of_birth', 'country_code', 'last_refresh'], 'rows': [['D01', 'P001', 'INDIVIDUAL', 'Aster Vale', '1985-04-12', 'US', '2026-09-20'], ['D02', 'P002', 'INDIVIDUAL', None, '1990-02-30', 'CA', '2026-09-20'], ['D03', 'P003', 'INDIVIDUAL', 'Briar Lake', '1977-08-03', 'ZZ', '2024-09-30'], ['D04', 'P004', 'ENTITY', 'Cedar Sample Ltd', None, 'GB', '2026-09-20'], ['D05', 'P005', 'INDIVIDUAL', 'Dune Rowan', '1988-06-11', 'US', '2026-09-20'], ['D06', 'P005', 'INDIVIDUAL', 'Dune Rowan', '1988-06-11', 'US', '2026-09-20']]}, {'name': 'RuleResults', 'columns': ['rule_id', 'dimension', 'eligible_count', 'defect_count', 'defect_rate', 'critical', 'gate_result'], 'rows': [['DQ01', 'Completeness', 6, 1, 0.16666666666666666, True, 'RESTRICT'], ['DQ02', 'Validity', 6, 1, 0.16666666666666666, True, 'RESTRICT'], ['DQ03', 'Validity', 5, 1, 0.2, True, 'RESTRICT'], ['DQ04', 'Uniqueness', 6, 2, 0.3333333333333333, True, 'RESTRICT'], ['DQ05', 'Timeliness', 6, 1, 0.16666666666666666, False, 'REVIEW']], 'formats': {'defect_rate': '0.0%'}}], 'findings': [{'id': 'DQ-F01', 'title': 'Critical validity and completeness defects prevent an unrestricted recommendation', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'D02 has a blank name and impossible date; D03 has a code outside the fictional approved set.', 'recommendation': 'Propose restricted use pending source-owner correction and record-level retest.'}, {'id': 'DQ-F02', 'title': 'Duplicated customer key affects two supplied records', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'P005 appears on D05 and D06 where the contract requires one row per customer. Two affected rows form one duplicate group and one excess row.', 'recommendation': 'Resolve source lineage before any merge or removal; reconcile corrected counts.'}, {'id': 'DQ-F03', 'title': 'One refresh date exceeds the illustrative freshness horizon', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'D03 is 730 days old at 2026-09-30 against a 365-day illustration.', 'recommendation': 'Obtain current evidence or document a permitted limitation for the intended use.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional six-record customer extract and rule contract', 'locator': '10-worked-example.md, complete input and rule outcomes', 'claim_class': 'Observed'}, {'id': 'REF-001', 'title': 'BCBS Principles for effective risk data aggregation and risk reporting', 'locator': 'https://www.bis.org/publ/bcbs239.pdf', 'claim_class': 'Reported'}, {'id': 'REF-002', 'title': 'BCBS 239 implementation newsletter, 2026', 'locator': 'https://www.bis.org/publications/implementation-principles-effective-risk-data-aggregation-and-risk-reporting-bcbs-239-principles', 'claim_class': 'Reported'}], 'metrics': [{'label': 'Supplied rows', 'value': '6', 'method': 'Count all original record IDs, retaining both duplicate-group members.', 'format': '#,##0'}, {'label': 'Critical-affected rows', 'value': '4 of 6 (66.7%)', 'method': 'Distinct union D02,D03,D05,D06 / all six records.', 'format': '#,##0'}, {'label': 'Passing rule checks', 'value': '23 of 29 (79.3%)', 'method': 'Eligible rule checks29 minus six failures; diagnostic only, no release authority.', 'format': '#,##0'}], 'limitations': ['The allowed codes and 365-day horizon are fictional contractual examples.', 'The check inventory cannot detect every possible data defect.', 'Duplicate keys establish a contract breach, not authority to merge records.', 'No source-system correction or feed restriction was executed.'], 'conclusion': 'Four of six fictional records are affected by critical defects, so the evidence supports a restricted-use recommendation. The 79.3% diagnostic check-pass rate cannot override critical gates; correction and acceptance remain human decisions.', 'report_narrative': [['Four of six fictional records are affected by critical defects. The draft recommendation is restricted use pending source-confirmed correction and human acceptance; a 79.3% diagnostic check-pass rate cannot override the critical gates.'], ['The extract has six active rows, five distinct customer keys, and a one-row-per-customer contract. The fixture uses five rules, a limited US/CA/GB code set, and a 365-day freshness horizon; these are illustrative contractual choices.'], ['D02 has a blank name and impossible birth date; D03 has an unapproved code and stale refresh date; D05 and D06 share the same customer key. Duplicate keys breach this contract but do not authorize a merge or deletion.'], ['DataRecords preserves all six original rows, including nulls and invalid date text. There are no exclusions. The key P005 forms one duplicate group, two affected rows, and one excess row; these counts describe different aspects of the defect.'], ['Rule eligibility totals 6 + 6 + 5 + 6 + 6 = 29 checks; six fail and 23 pass. The ENTITY row D04 is outside the individual birth-date denominator. Critical affected IDs are the distinct union D02, D03, D05, D06, or 4/6 = 66.7%.'], ['SYN-001 supports the record-level arithmetic and rule outcomes. The public BCBS sources provide method context only; they do not prescribe the fictional code list, freshness horizon, or zero-failure gates. Upstream real-world accuracy is outside this fixture.'], ['Propose source-owner correction for D02 and D03, lineage resolution for P005, and current refresh evidence. Retest the corrected extract and reconcile any approved removal to the original six records; do not improve rates by silently dropping defects.'], ['QA checks calendar validity, conditional eligibility, duplicate accounting, and distinct affected-row totals. Actual feed acceptance, source correction, or use restrictions require an authorized human decision; no production action occurred.']], 'suite_id': 'data-quality', 'version': '1.0.0', 'as_of': '2026-10-09', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'DQ-F01', 'proposal': 'Propose restricted use pending source-owner correction and record-level retest.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'DQ-F02', 'proposal': 'Resolve source lineage before any merge or removal; reconcile corrected counts.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'DQ-F03', 'proposal': 'Obtain current evidence or document a permitted limitation for the intended use.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
