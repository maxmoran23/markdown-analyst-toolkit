# Digital Asset Review — fixed report template

Version 1.0.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Digital asset review brief**
2. **Scope and ledger method**
3. **Material findings**
4. **Event reconciliation**
5. **Counterparty and attribution assessment**
6. **Evidence record**
7. **Recommended review actions**
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

DATA = {'slug': 'digital-asset-review', 'title': 'Digital Asset Review', 'summary': 'Reconcile public-ledger events and token units while separating transaction facts from real-world attribution.', 'audience': 'Analysts reviewing public blockchain evidence and data-quality limitations', 'decision': 'What activity is supported by the supplied capture, and what attribution or completeness gaps remain?', 'palette': 'teal', 'report_sections': ['Digital asset review brief', 'Scope and ledger method', 'Material findings', 'Event reconciliation', 'Counterparty and attribution assessment', 'Evidence record', 'Recommended review actions', 'Limitations and human review'], 'domain_tables': [{'name': 'LedgerEvents', 'columns': ['event_id', 'chain_id', 'tx_id', 'event_index', 'asset_id', 'raw_amount', 'decimals', 'display_units', 'direction', 'execution_state', 'included', 'evidence_ids', 'notes'], 'rows': [['EV-01', 'FICTIONAL-EVM', 'TX-01', 0, 'PAPER-CONTRACT', '100000000', 6, '100.000000', 'IN', 'SUCCESS', True, 'SYN-001', 'Duplicate raw capture R-06 linked and removed once'], ['EV-02', 'FICTIONAL-EVM', 'TX-02', 0, 'PAPER-CONTRACT', '40000000', 6, '40.000000', 'OUT', 'SUCCESS', True, 'SYN-001', 'Transfer to CP-B'], ['EV-03', 'FICTIONAL-EVM', 'TX-03', 0, 'PAPER-CONTRACT', '5000000', 6, '5.000000', 'SELF', 'SUCCESS', True, 'SYN-001', 'Separate self activity; excluded from directional totals'], ['EV-04', 'FICTIONAL-EVM', 'TX-04', 0, 'PAPER-CONTRACT', '1', 6, '0.000001', 'IN', 'SUCCESS', True, 'SYN-001', 'Small unsolicited transfer; no attribution inference'], ['EV-05', 'FICTIONAL-EVM', 'TX-05', None, 'PAPER-CONTRACT', '20000000', 6, '20.000000', 'OUT', 'FAILED', False, 'SYN-001', 'Attempted amount from supplied record; no successful event log']]}, {'name': 'Counterparties', 'columns': ['counterparty_id', 'asset_id', 'in_units', 'out_units', 'self_units', 'eligible_event_count', 'attribution_state', 'evidence_ids', 'notes'], 'rows': [['CP-A', 'PAPER-CONTRACT', '100.000000', '0.000000', '0.000000', 1, 'UNATTRIBUTED', 'SYN-001', 'Raw duplicate not counted twice'], ['CP-B', 'PAPER-CONTRACT', '0.000000', '40.000000', '0.000000', 1, 'UNVERIFIED LABEL', 'SYN-001', 'Supplied explorer label not identity evidence'], ['SUBJECT', 'PAPER-CONTRACT', '0.000000', '0.000000', '5.000000', 1, 'SELF ADDRESS', 'SYN-001', 'Same exact fictional address; no separate counterparty'], ['CP-C', 'PAPER-CONTRACT', '0.000001', '0.000000', '0.000000', 1, 'UNATTRIBUTED', 'SYN-001', 'Unsolicited small inbound amount retained']]}], 'findings': [{'id': 'F-01', 'title': 'Duplicate and failed records need distinct treatment', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'Six raw rows reconcile to five unique records and four eligible successful events.', 'recommendation': 'Preserve duplicate lineage and failed-attempt exclusion.'}, {'id': 'F-02', 'title': 'Counterparty identity is not established by the label', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'CP-B has an explorer-style label without supporting identity evidence.', 'recommendation': 'Obtain independent attribution evidence before consequential reliance.'}, {'id': 'F-03', 'title': 'Captured net flow is not an ending balance', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Estimated', 'evidence_ids': ['SYN-001'], 'detail': '100.000001 PAPER in less 40.000000 PAPER out equals 60.000001 PAPER under the stipulated method.', 'recommendation': 'Keep balance, fiat value, and completeness limitations explicit.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional digital asset capture', 'locator': '10-worked-example.md, R-01 through R-06', 'claim_class': 'Observed'}, {'id': 'REF-ETH-TX', 'title': 'Ethereum transactions documentation', 'locator': 'https://ethereum.org/developers/docs/transactions/', 'claim_class': 'Observed'}, {'id': 'REF-ETH-RPC', 'title': 'Ethereum JSON-RPC documentation', 'locator': 'https://ethereum.org/developers/docs/apis/json-rpc/', 'claim_class': 'Observed'}, {'id': 'REF-ERC20', 'title': 'ERC-20 standard', 'locator': 'https://eips.ethereum.org/EIPS/eip-20', 'claim_class': 'Observed'}, {'id': 'REF-BTC', 'title': 'Bitcoin transactions developer guide', 'locator': 'https://developer.bitcoin.org/devguide/transactions.html', 'claim_class': 'Observed'}, {'id': 'REF-FATF-VA', 'title': 'FATF virtual asset guidance', 'locator': 'https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Raw to unique records', 'value': '6 to 5', 'method': 'Six capture rows less one proven repeated event.', 'format': '#,##0'}, {'label': 'Eligible successful events', 'value': '4', 'method': 'Five unique records less one failed attempt.', 'format': '#,##0'}, {'label': 'Captured net directional flow', 'value': '60.000001 PAPER', 'method': '(100000000 + 1 - 40000000) / 10^6; excludes SELF and FAILED.', 'format': '#,##0'}], 'limitations': ['All network and address labels are fictional; no live-chain validation is implied.', 'No opening balance, fiat price, or complete native-fee accounting is supplied.', 'Explorer-style labels do not establish identity, intent, or legal status.'], 'metadata': {'conclusion': 'Six fictional capture rows reconcile to five unique records and four eligible successful events. Captured net directional flow is 60.000001 PAPER; it is not an ending balance, fiat value, or evidence of counterparty identity.'}, 'report_narrative': [['Six fictional capture rows reconcile to five unique records and four eligible successful events. Captured net directional flow is 60.000001 PAPER; it is not an ending balance, fiat value, or evidence of counterparty identity.'], ['The fictional EVM-style capture contains six raw rows for one token with six decimal places. Records are reconciled by event identity and execution status before directional amounts are summed; exact atomic values remain text.'], ['F-01: Six raw rows reconcile to five unique records and four eligible successful events.', 'F-02: CP-B has an explorer-style label without supporting identity evidence.', 'F-03: 100.000001 PAPER in less 40.000000 PAPER out equals 60.000001 PAPER under the stipulated method.'], ['One duplicate leaves five unique records. Four are successful eligible events; the failed 20.000000 PAPER attempt is excluded. The 5.000000 PAPER self transfer remains visible but does not inflate directional totals.'], ['Inbound 100.000001 PAPER less outbound 40.000000 PAPER produces captured net flow of 60.000001 PAPER. CP-B remains an unverified label; the tiny CP-C inbound transfer provides no identity or intent inference.'], ['SYN-001 supplies the raw captures, event identities and label assertion. No opening balance, fiat price, complete native-fee ledger or independent attribution evidence is supplied.'], ['Preserve duplicate lineage and exact units, obtain independent attribution before consequential reliance, and keep net captured flow separate from ending balance and fiat exposure.'], ['All network and address labels are fictional; no live-chain validation is implied.', 'No opening balance, fiat price, or complete native-fee accounting is supplied.', 'Explorer-style labels do not establish identity, intent, or legal status.', 'QA remains pending and no authorized human disposition is recorded.']], 'suite_id': 'digital-asset-review', 'version': '1.0.0', 'as_of': '2026-10-09', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'conclusion': 'Six fictional capture rows reconcile to five unique records and four eligible successful events. Captured net directional flow is 60.000001 PAPER; it is not an ending balance, fiat value, or evidence of counterparty identity.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'F-01', 'proposal': 'Preserve duplicate lineage and failed-attempt exclusion.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'F-02', 'proposal': 'Obtain independent attribution evidence before consequential reliance.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'F-03', 'proposal': 'Keep balance, fiat value, and completeness limitations explicit.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
