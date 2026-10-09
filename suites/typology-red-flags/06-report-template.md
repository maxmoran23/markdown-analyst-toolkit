# Typology and Red-Flag Review — fixed report template

Version 1.0.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Review priorities and indicator counts**
2. **Scope and indicator methodology**
3. **Findings and alternative explanations**
4. **Indicator observations**
5. **Competing hypotheses by case**
6. **Evidence and source applicability**
7. **Proposed inquiry actions**
8. **Limitations, quality checks, and human review**

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

DATA = {'slug': 'typology-red-flags', 'title': 'Typology and Red-Flag Review', 'summary': 'Translate evidence into explicit indicator observations, test ordinary explanations, and build a defensible inquiry plan without treating a red flag as proof of misconduct.', 'audience': 'Financial-crime analysts, typology researchers, and control-design reviewers', 'decision': 'Which indicators are actually supported, which remain indeterminate, and what additional evidence would distinguish a concerning explanation from an ordinary one?', 'palette': 'teal', 'report_sections': ['Review priorities and indicator counts', 'Scope and indicator methodology', 'Findings and alternative explanations', 'Indicator observations', 'Competing hypotheses by case', 'Evidence and source applicability', 'Proposed inquiry actions', 'Limitations, quality checks, and human review'], 'domain_tables': [{'name': 'IndicatorObservations', 'columns': ['observation_id', 'case_id', 'indicator_id', 'state', 'measured_value', 'unit', 'criterion', 'evidence_ids', 'interpretation'], 'rows': [['O-01', 'A', 'RF-01', 'PRESENT', 0.95, 'ratio', 'credit>=5000 USD; ratio>=0.90; elapsed<=24h', 'SYN-001', 'Rapid movement pattern; purpose unresolved'], ['O-02', 'A', 'RF-02', 'ABSENT', 2, 'distinct_payers', 'at least 3 distinct payers', 'SYN-001', 'Two payers; criterion not met'], ['O-03', 'B', 'RF-01', 'NOT_APPLICABLE', None, 'ratio', 'exclude confirmed own transfers', 'SYN-002', 'Ownership evidence supports limited exclusion'], ['O-04', 'C', 'RF-03', 'INDETERMINATE', None, 'posted_events', 'at least 3 posted events in 24h', 'SYN-003', 'Reported events lack transaction corroboration'], ['O-05', 'D', 'RF-04', 'ABSENT', 1, 'distinct_payees', 'at least 3 distinct payees in 24h', 'SYN-004', 'One visible payment; complete stated window']]}, {'name': 'HypothesisReview', 'columns': ['case_id', 'concern_hypothesis', 'benign_hypothesis', 'support_state', 'next_evidence', 'priority', 'confidence', 'proposed_outcome'], 'rows': [['A', 'Unexplained rapid onward movement', 'Ordinary consolidated supplier settlement', 'PATTERN_ONLY', 'Purpose and counterparty records', 'MEDIUM', 'MODERATE', 'FURTHER_REVIEW'], ['B', 'Concealed onward transfer', 'Movement between confirmed owned accounts', 'BENIGN_SUPPORTED', 'No extra inquiry for RF-01 on supplied facts', 'LOW', 'HIGH', 'DOCUMENT_LIMITED_EXCLUSION'], ['C', 'Repeated related payments', 'Duplicate descriptions of one event', 'INSUFFICIENT_EVIDENCE', 'Original ledger and timestamps', 'MEDIUM', 'LOW', 'OBTAIN_SOURCE'], ['D', 'Distribution across multiple beneficiaries', 'One ordinary invoice payment', 'PATTERN_NOT_MET', 'None for RF-04 within stated scope', 'LOW', 'HIGH', 'RECORD_NEGATIVE']]}], 'findings': [{'id': 'RF-F01', 'title': 'One observed rapid-movement indicator requires context', 'severity': 'MEDIUM', 'confidence': 'MODERATE', 'claim_class': 'Inferred', 'evidence_ids': ['SYN-001'], 'detail': 'A has a 95.0% outward-to-inward ratio within two hours, but the distinct-payer indicator is absent.', 'recommendation': 'Seek purpose and counterparty evidence without converting the indicator into a criminal conclusion.'}, {'id': 'RF-F02', 'title': 'A narrative-only repetition claim is indeterminate', 'severity': 'MEDIUM', 'confidence': 'LOW', 'claim_class': 'Reported', 'evidence_ids': ['SYN-003'], 'detail': 'C is reported to have three payments, but no original ledger or event times are supplied.', 'recommendation': 'Obtain original events and test whether the descriptions refer to unique posted payments.'}, {'id': 'RF-F03', 'title': 'Own transfers and a single payee provide negative controls', 'severity': 'LOW', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-002', 'SYN-004'], 'detail': 'B is excluded from RF-01 on confirmed ownership; D does not meet the three-payee criterion.', 'recommendation': 'Retain these limited results without declaring either relationship universally low risk.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional case A ledger', 'locator': '10-worked-example.md, events E01–E03', 'claim_class': 'Observed'}, {'id': 'SYN-002', 'title': 'Fictional case B ledger and ownership record', 'locator': '10-worked-example.md, events E04–E05 and ownership note', 'claim_class': 'Observed'}, {'id': 'SYN-003', 'title': 'Fictional uncorroborated case C referral', 'locator': '10-worked-example.md, record N01', 'claim_class': 'Reported'}, {'id': 'SYN-004', 'title': 'Fictional case D ledger', 'locator': '10-worked-example.md, event E06', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Indicator observations', 'value': 5, 'method': 'Count O-01 through O-05', 'format': '#,##0'}, {'label': 'Present indicators', 'value': 1, 'method': 'O-01 only; count states independently of case count', 'format': '#,##0'}, {'label': 'Indeterminate indicators', 'value': 1, 'method': 'O-04 lacks original transaction evidence', 'format': '#,##0'}, {'label': 'Known gross movement USD', 'value': 27500, 'method': 'Sum E01–E06; excludes reported amount in N01', 'format': '$#,##0.00'}], 'limitations': ['Indicator thresholds are authored illustrations rather than regulatory criteria.', 'Case C has a referral narrative but no transaction ledger.', 'No indicator establishes intent, beneficial ownership, or underlying criminal conduct.'], 'conclusion': 'One of five planned observations is present, two are absent, one is indeterminate, and one is not applicable. The supported pattern warrants a targeted inquiry; no indicator establishes criminal conduct.', 'report_narrative': [['One of five planned observations is present, two are absent, one is indeterminate, and one is not applicable. The supported pattern warrants a targeted inquiry; no indicator establishes criminal conduct.'], ['The review covers five planned indicator observations and their explicit applicability tests. The fictional thresholds support reproducible method checks; they are not universal reporting or risk-acceptance criteria.'], ['RF-F01: A has a 95.0% outward-to-inward ratio within two hours, but the distinct-payer indicator is absent.', 'RF-F02: C is reported to have three payments, but no original ledger or event times are supplied.', 'RF-F03: B is excluded from RF-01 on confirmed ownership; D does not meet the three-payee criterion.'], ['Of five observations, one is present, two absent, one indeterminate and one not applicable. Known gross movement is $27,500.00. These states retain separate denominators, and the amount is not a measure of illicit proceeds.'], ['The present pattern supports a targeted inquiry alongside the documented competing explanation. Missing evidence leaves one observation indeterminate; lack of applicability is not a favorable test result.'], ['File 10 supplies the complete synthetic observations, case hypotheses and evidence IDs. Public typology sources inform the review vocabulary, while their indicator descriptions do not establish subject-specific facts.'], ['Seek the evidence that distinguishes the competing hypotheses and resolves the indeterminate observation. Escalate only through the authorized review process; retain all absent and inapplicable observations in the population.'], ['Indicator thresholds are authored illustrations rather than regulatory criteria.', 'Case C has a referral narrative but no transaction ledger.', 'No indicator establishes intent, beneficial ownership, or underlying criminal conduct.', 'QA remains pending and no authorized human disposition is recorded.']], 'suite_id': 'typology-red-flags', 'version': '1.0.0', 'as_of': '2026-10-09', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'RF-F01', 'proposal': 'Seek purpose and counterparty evidence without converting the indicator into a criminal conclusion.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'RF-F02', 'proposal': 'Obtain original events and test whether the descriptions refer to unique posted payments.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'RF-F03', 'proposal': 'Retain these limited results without declaring either relationship universally low risk.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
