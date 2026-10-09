# Source of Wealth and Funds Review — fixed report template

Version 1.1.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Wealth and funds conclusion**
2. **Scope valuation dates and reconciliation method**
3. **Material provenance findings**
4. **Wealth accumulation bridge**
5. **Proposed funding trace**
6. **Evidence chain and alternative explanations**
7. **Proposed corroboration actions**
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

DATA = {'slug': 'source-wealth-funds', 'title': 'Source of Wealth and Funds Review', 'summary': 'Reconcile wealth accumulation and particular funding sources with dated asset, income, tax, FX, and transfer evidence.', 'audience': 'Analysts preparing generic source-of-wealth and source-of-funds review drafts', 'decision': 'What wealth accumulation and proposed funding can be explained from the supplied evidence, and which provenance or entitlement gaps remain?', 'palette': 'umber', 'report_sections': ['Wealth and funds conclusion', 'Scope valuation dates and reconciliation method', 'Material provenance findings', 'Wealth accumulation bridge', 'Proposed funding trace', 'Evidence chain and alternative explanations', 'Proposed corroboration actions', 'Limitations quality review and human disposition'], 'domain_tables': [{'name': 'WealthBridge', 'columns': ['event_id', 'event_date', 'event_type', 'original_amount', 'original_currency', 'fx_usd_per_unit', 'usd_wealth_change', 'cash_effect_usd', 'evidence_ids', 'notes'], 'rows': [['W01', '2025-01-01', 'OPENING_CASH', 400000, 'USD', 1, 400000, 400000, 'SYN-001', 'Opening stock; not period income'], ['W02', '2025-01-01', 'OPENING_SECURITIES', 600000, 'USD', 1, 600000, 0, 'SYN-001', 'Existing holdings; separate from inherited securities'], ['W03', '2025-01-01', 'OPENING_PROPERTY', 500000, 'USD', 1, 500000, 0, 'SYN-001', 'Gross property value before debt'], ['W04', '2025-01-01', 'OPENING_DEBT', -200000, 'USD', 1, -200000, 0, 'SYN-001', 'Liability deducted once; no period repayment'], ['W05', '2025-06-30', 'SALARY_NET', 300000, 'USD', 1, 210000, 210000, 'SYN-002', 'Gross salary 300000 less fictional tax paid 90000'], ['W06', '2025-07-01', 'INHERITED_SECURITIES', 400000, 'USD', 1, 400000, 0, 'SYN-003', 'Noncash inherited stock of assets; no sale receipt yet'], ['W07', '2025-08-01', 'PARTIAL_DISPOSAL', 250000, 'USD', 1, 20000, 220000, 'SYN-003', 'Carrying amount removed 200000; fee 10000; fictional tax paid 20000'], ['W08', '2025-08-15', 'DIVIDEND_NET', 100000, 'EUR', 1.2, 90000, 90000, 'SYN-004', 'Gross EUR100000 × 1.20 = USD120000; fictional tax paid USD30000'], ['W09', '2025-09-30', 'LIVING_EXPENSE', -120000, 'USD', 1, -120000, -120000, 'SYN-005', 'Period expense paid from cash'], ['W10', '2025-09-30', 'PROPERTY_REVALUATION', 100000, 'USD', 1, 100000, 0, 'SYN-005', 'Unrealized change; no funding cash'], ['W11', '2025-09-30', 'SECURITIES_REVALUATION', 60000, 'USD', 1, 60000, 0, 'SYN-005', 'Unrealized change on pre-existing holdings only']], 'formats': {'original_amount': '#,##0.00', 'fx_usd_per_unit': '0.0000', 'usd_wealth_change': '#,##0.00', 'cash_effect_usd': '#,##0.00'}}, {'name': 'FundingTrace', 'columns': ['trace_id', 'origin_type', 'economic_event_id', 'net_available_usd', 'allocated_usd', 'supported_usd', 'link_status', 'evidence_ids', 'notes'], 'rows': [['F01', 'SALARY', 'SALARY01', 210000, 180000, 180000, 'SUPPORTED_ALLOCATION', 'SYN-002;SYN-006', 'Remaining net salary cash 30000 is unallocated'], ['F02', 'DIVIDEND', 'DIV01', 90000, 90000, 90000, 'SUPPORTED_ALLOCATION', 'SYN-004;SYN-006', 'Net dividend only; gross not added'], ['F03', 'INHERITED_ASSET_SALE', 'SALE01', 220000, 220000, 220000, 'SUPPORTED_ALLOCATION', 'SYN-003;SYN-006', 'Same asset already included in wealth bridge'], ['F04', 'OPENING_CASH', 'CASH01', 400000, 50000, 50000, 'SUPPORTED_ALLOCATION', 'SYN-001;SYN-006', 'Opening stock used; not new wealth creation'], ['F05', 'UNRELATED_THIRD_PARTY', 'UNKNOWN01', 60000, 60000, 0, 'UNRESOLVED', 'SYN-006', 'Claimed contribution; sender origin and entitlement absent'], ['F06', 'DUPLICATE_SALE_ADVICE', 'SALE01', 220000, 0, 0, 'DUPLICATE_EXCLUDED', 'SYN-003', 'Second document for F03 event; not additional money']], 'formats': {'net_available_usd': '#,##0.00', 'allocated_usd': '#,##0.00', 'supported_usd': '#,##0.00'}}], 'findings': [{'id': 'WF-F01', 'title': 'Proposed third-party contribution remains unsupported', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-006'], 'detail': '$60,000.00 of the proposed $600,000.00 funding has no supplied origin or entitlement explanation.', 'recommendation': 'Obtain the sender relationship, economic origin, entitlement, and transfer rationale before relying on that allocation.'}, {'id': 'WF-F02', 'title': 'Inheritance and disposal are the same underlying assets', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-003'], 'detail': 'The $400,000.00 inherited securities stock includes the $200,000.00 carrying amount sold for $220,000.00 net cash. Only $20,000.00 is incremental net wealth from disposal.', 'recommendation': 'Retain the asset bridge and reject adding all net sale cash as new wealth.'}, {'id': 'WF-F03', 'title': 'Unrealized gains are not funding cash', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-005'], 'detail': 'Property and existing securities revaluations add $160,000.00 to the wealth scenario and zero cash.', 'recommendation': 'Separate valuation support from liquidity and funding provenance.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional opening balance sheet', 'locator': '10-worked-example.md, opening asset and liability population', 'claim_class': 'Observed'}, {'id': 'SYN-002', 'title': 'Fictional gross salary and tax schedule', 'locator': '10-worked-example.md, complete period-event population', 'claim_class': 'Observed'}, {'id': 'SYN-003', 'title': 'Fictional inheritance and partial sale records', 'locator': '10-worked-example.md, securities quantity and disposal bridge', 'claim_class': 'Observed'}, {'id': 'SYN-004', 'title': 'Fictional dividend FX and tax schedule', 'locator': '10-worked-example.md, complete period-event population', 'claim_class': 'Observed'}, {'id': 'SYN-005', 'title': 'Fictional expenses and closing valuations', 'locator': '10-worked-example.md, closing reconciliation', 'claim_class': 'Observed'}, {'id': 'SYN-006', 'title': 'Fictional proposed funding allocation', 'locator': '10-worked-example.md, full funding population', 'claim_class': 'Observed'}, {'id': 'REF-PEP', 'title': 'FATF 2013 PEP guidance, paragraphs 86–94', 'locator': 'https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Guidance-PEP-Rec12-22.pdf', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Closing net wealth scenario', 'value': '$2,060,000.00', 'method': 'Opening net wealth $1,300,000.00 plus net period wealth changes $760,000.00.', 'format': '#,##0'}, {'label': 'Supported proposed allocation', 'value': '$540,000.00 of $600,000.00 (90.0%)', 'method': 'Sum supported_usd across F01–F06 / sum allocated_usd; duplicate F06 contributes zero.', 'format': '#,##0'}, {'label': 'Unsupported proposed allocation', 'value': '$60,000.00 (10.0%)', 'method': 'Proposed $600,000.00 less supported $540,000.00; F05 is unresolved.', 'format': '#,##0'}, {'label': 'Closing cash before proposed transfer', 'value': '$800,000.00', 'method': 'Opening cash $400,000.00 + salary $210,000.00 + sale $220,000.00 + dividend $90,000.00 − expenses $120,000.00.', 'format': '#,##0'}], 'limitations': ['All balances, tax charges, valuations, exchange rates, and source records are fictional.', 'The wealth bridge is a scenario with assumed completeness, not verified net worth or a tax determination.', 'Supported allocation means document support within the fixture, not tracing particular currency units through a commingled account.', 'The proposed third-party contribution is excluded from owned wealth pending entitlement and origin evidence.', 'A funded amount or plausible wealth profile does not establish lawful origin or authorize a transaction.'], 'conclusion': 'The fictional wealth bridge reconciles to $2,060,000.00 net wealth and $800,000.00 cash at cutoff. Of a separate proposed $600,000.00 funding allocation, $540,000.00 is supported within the fixture and $60,000.00 from an unrelated third party remains unexplained.', 'report_narrative': [['The fictional wealth bridge reconciles to $2,060,000.00 net wealth and $800,000.00 cash at cutoff. Of a separate proposed $600,000.00 funding allocation, $540,000.00 is supported within the fixture and $60,000.00 from an unrelated third party remains unexplained.'], ['The wealth period is Jan 01–Sep 30, 2025. Opening net wealth is $1,300,000.00. The proposed funding is dated Oct 01, 2025 and has not occurred in this fixture. USD is the reporting currency; the dividend uses a fictional 1.20 USD-per-EUR conversion.'], ['The $60,000.00 third-party proposal has no supplied economic-origin or entitlement evidence. Inherited securities and their partial-sale proceeds cannot be counted as two independent sources of wealth. Unrealized appreciation raises a valuation scenario but provides no funding cash.'], ['The bridge adds net salary $210,000.00, inheritance $400,000.00, net disposal gain $20,000.00, net dividend $90,000.00, and revaluations $160,000.00, less living expenses $120,000.00. Closing assets total $2,260,000.00 less debt $200,000.00.', "SYN-003 supplies 4,000 inherited units at $100.00 per unit ($400,000.00). Of these, 2,000 units are sold at $125.00 ($250,000.00 gross); $10,000.00 fees and $20,000.00 paid fictional tax leave $220,000.00 cash. Remove the sold $200,000.00 carrying amount to obtain $20,000.00 incremental wealth. The remaining 2,000 units retain the fixture's $100.00 carrying value ($200,000.00) at Sep 30, 2025. These are exercise values, not tax-basis determinations."], ['The proposed allocation is salary $180,000.00, dividend $90,000.00, inherited-asset sale $220,000.00, opening cash $50,000.00, and unresolved third-party funds $60,000.00. Duplicate sale advice F06 adds zero. Supported allocations total $540,000.00.'], ['SYN-001 through SYN-006 supply all fictional balances, events, and proposed allocations. FATF 2013 paragraphs 86–94 inform the distinction between overall wealth origin and particular funds origin in a PEP context; this exercise does not determine PEP status or universal legal obligations.'], ['Request the third party’s economic origin, relationship, entitlement, and proposed transfer purpose in a permitted fictional or public form. Corroborate dates, inheritance rights, sale deductions, and valuations before relying on a real-world analogue. Keep tax and legal interpretation with qualified reviewers.'], ['QA must reconcile opening $1,300,000.00, net movement $760,000.00, closing $2,060,000.00, cash $800,000.00, and supported funding $540,000.00. The scenario does not verify tax compliance, lawful origin, actual liquidity, or human approval.']], 'as_of': '2025-09-30', 'scope': 'Fictional wealth bridge from Jan 01 through Sep 30, 2025; a separate proposed Oct 01, 2025 funding allocation is not a completed event at the wealth cutoff.', 'suite_id': 'source-wealth-funds', 'version': '1.1.0', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'WF-F01', 'proposal': 'Obtain the sender relationship, economic origin, entitlement, and transfer rationale before relying on that allocation.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'WF-F02', 'proposal': 'Retain the asset bridge and reject adding all net sale cash as new wealth.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'WF-F03', 'proposal': 'Separate valuation support from liquidity and funding provenance.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
