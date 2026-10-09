# Typology and Red-Flag Review — fixed workbook template

Version 1.1.0. The workbook is a generated review snapshot with visible evidence and explicit open decisions. Use an in-session file-creation capability; no terminal, repository checkout or automation is needed.

## Exact workbook schema

Create these sheets in this order. Preserve field spelling and column order. File 05 defines domain types, units, permitted values and interpretation; this file controls the six common sheets.

| Sheet | Ordered columns |
| --- | --- |
| Summary | `measure`, `value`, `method_or_limit` |
| Dashboard | `severity`, `finding_count`, `denominator` |
| Findings | `id`, `title`, `severity`, `confidence`, `claim_class`, `evidence_ids`, `detail`, `recommendation` |
| Evidence | `id`, `title`, `locator`, `claim_class` |
| Actions | `action_id`, `finding_id`, `proposal`, `owner`, `due_date`, `status` |
| QA | `check_id`, `check`, `result`, `evidence` |
| IndicatorObservations | `observation_id`, `case_id`, `indicator_id`, `state`, `measured_value`, `unit`, `criterion`, `evidence_ids`, `interpretation` |
| HypothesisReview | `case_id`, `concern_hypothesis`, `benign_hypothesis`, `support_state`, `next_evidence`, `priority`, `confidence`, `proposed_outcome` |

## Common field contract

| Field group | Contract |
| --- | --- |
| IDs | Nonempty text, stable within a case; unique primary IDs. Foreign keys must resolve before release. Preserve leading zeros. |
| Severity | `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`; severity is separate from evidence confidence. |
| Confidence | `HIGH`, `MODERATE`, `LOW`, `NOT ASSESSABLE`; justify the rating in the analysis. |
| Claim class | `Observed`, `Reported`, `Inferred`, `Estimated`; public-source claims are not automatically Observed. |
| Evidence IDs | Semicolon-delimited stable keys. Use the Evidence sheet's exact ID; no invented source titles. |
| Owner/due date | Explicit `Not provided` until supplied; do not assign an actual person or a guessed deadline. |
| Action state | `Proposed`, `Accepted`, `In progress`, `Blocked`, `Closed`, `Risk accepted`; the fixture starts Proposed. Closure requires recorded evidence. |
| QA result | `PASS`, `FAIL`, `REVIEW REQUIRED`, `NOT RECORDED`, or `NOT TESTED` with exact evidence; no automatic PASS. |
| Null | Domain JSON null becomes an empty Excel cell with a missing-value comment and an associated limitation/QA explanation; it is not zero. Common unassigned action fields display `Not provided`. `Not applicable` requires rationale. |
| Numerics | Preserve native units, currency and scale. Fields ending `_usd` display US dollar currency. Other numbers retain their stated domain unit. |
| Evidence text | Write as text, including values beginning `=`, `+`, `-`, `@`, or whitespace. Do not evaluate source text as a formula. |

## Layout and calculation contract

- Summary first, Dashboard second; Findings, Evidence, Actions and QA next; domain data last in the declared order.
- Arial 11 pt; slate header `#344E5F`, white header text, stone body `#F1F2EF`, pale gray alternate rows `#E2E8E9`; no rainbow tab or cell coloring. Chart bars use the same slate and whole-count axis intervals.
- Freeze top row and first column on data tabs. Enable filters and wrapped text. Give long evidence and recommendation fields 44-character columns. Keep body row heights automatic.
- Highlight HIGH severity with muted rose `#F2DADB` and dark red text `#7F3038`; retain the textual label. Missing data are literal values, not a green/blank cell.
- Landscape A4 printing for compact sheets and A3 for sheets wider than 145 combined character-width units; repeat the header row and identifier column. Fit one page wide with unrestricted pages tall. Inspect actual print readability; use the Word report if the available printer cannot reproduce a wide sheet legibly.
- The Dashboard calculates counts from the Findings severity column using `COUNTIF`. Counts cover **supplied findings**, not the entire transaction/customer population. Use the exact source scope in denominators.
- This is a snapshot generator: after adding or removing records, regenerate the workbook so formulas, validations, filters and chart ranges include every row. Do not assume inserting a row extends all ranges.
- Summary business measures come from validated input calculations. Preserve each method and limitation alongside the value. Recompute them from source when adapting; never retain a specimen metric by accident.
- `openpyxl` writes formulas but does not calculate them. Request recalculation in Excel or the available spreadsheet engine, inspect results, and record the outcome. If unavailable, label formula-cache/display behavior **NOT TESTED**; the independently computed check does not prove Excel behavior.

## Complete in-session renderer

Use this block when `openpyxl` is already available in the chat's Python capability. No installation is required or assumed. When unavailable, ask the assistant's approved workbook capability to implement the same schema and style. If that is unavailable too, emit one copy-ready table per sheet and state **XLSX not created**. Never label CSV as a multi-sheet workbook.

The renderer checks required fields, identifiers, evidence joins, sheet names and finite numbers before writing. It rejects cell text above Excel's 32,767-character limit rather than silently truncating evidence. Preserve the complete source separately and put an attributed summary with its exact source locator in the workbook. Passing these structural checks does not establish that a claim or calculation is correct.

Excel numeric precision is limited to 15 significant digits. This renderer rejects numeric magnitudes of 10^15 or larger. Store exact large integers, identifiers and atomic token quantities as text under an explicitly documented domain type and unit. Fractional numeric values remain floating-point approximations; preserve the original source string whenever all decimal digits are material and apply the stated calculation precision before display.

The storage limits are documented in [Microsoft's Excel specifications](https://support.microsoft.com/en-us/excel/excel-specifications-and-limits). They do not establish the behavior of every available file reader; inspect the actual delivered file.

```python
from pathlib import Path
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from openpyxl.workbook.properties import CalcProperties
from openpyxl.comments import Comment

DATA = {'slug': 'typology-red-flags', 'title': 'Typology and Red-Flag Review', 'summary': 'Translate evidence into explicit indicator observations, test ordinary explanations, and build a defensible inquiry plan without treating a red flag as proof of misconduct.', 'audience': 'Financial-crime analysts, typology researchers, and control-design reviewers', 'decision': 'Which indicators are actually supported, which remain indeterminate, and what additional evidence would distinguish a concerning explanation from an ordinary one?', 'palette': 'teal', 'report_sections': ['Review priorities and indicator counts', 'Scope and indicator methodology', 'Findings and alternative explanations', 'Indicator observations', 'Competing hypotheses by case', 'Evidence and source applicability', 'Proposed inquiry actions', 'Limitations, quality checks, and human review'], 'domain_tables': [{'name': 'IndicatorObservations', 'columns': ['observation_id', 'case_id', 'indicator_id', 'state', 'measured_value', 'unit', 'criterion', 'evidence_ids', 'interpretation'], 'rows': [['O-01', 'A', 'RF-01', 'PRESENT', 0.95, 'ratio', 'credit>=5000 USD; ratio>=0.90; elapsed<=24h', 'SYN-001', 'Rapid movement pattern; purpose unresolved'], ['O-02', 'A', 'RF-02', 'ABSENT', 2, 'distinct_payers', 'at least 3 distinct payers', 'SYN-001', 'Two payers; criterion not met'], ['O-03', 'B', 'RF-01', 'NOT_APPLICABLE', None, 'ratio', 'exclude confirmed own transfers', 'SYN-002', 'Ownership evidence supports limited exclusion'], ['O-04', 'C', 'RF-03', 'INDETERMINATE', None, 'posted_events', 'at least 3 posted events in 24h', 'SYN-003', 'Reported events lack transaction corroboration'], ['O-05', 'D', 'RF-04', 'ABSENT', 1, 'distinct_payees', 'at least 3 distinct payees in 24h', 'SYN-004', 'One visible payment; complete stated window']]}, {'name': 'HypothesisReview', 'columns': ['case_id', 'concern_hypothesis', 'benign_hypothesis', 'support_state', 'next_evidence', 'priority', 'confidence', 'proposed_outcome'], 'rows': [['A', 'Unexplained rapid onward movement', 'Ordinary consolidated supplier settlement', 'PATTERN_ONLY', 'Purpose and counterparty records', 'MEDIUM', 'MODERATE', 'FURTHER_REVIEW'], ['B', 'Concealed onward transfer', 'Movement between confirmed owned accounts', 'BENIGN_SUPPORTED', 'No extra inquiry for RF-01 on supplied facts', 'LOW', 'HIGH', 'DOCUMENT_LIMITED_EXCLUSION'], ['C', 'Repeated related payments', 'Duplicate descriptions of one event', 'INSUFFICIENT_EVIDENCE', 'Original ledger and timestamps', 'MEDIUM', 'LOW', 'OBTAIN_SOURCE'], ['D', 'Distribution across multiple beneficiaries', 'One ordinary invoice payment', 'PATTERN_NOT_MET', 'None for RF-04 within stated scope', 'LOW', 'HIGH', 'RECORD_NEGATIVE']]}], 'findings': [{'id': 'RF-F01', 'title': 'One observed rapid-movement indicator requires context', 'severity': 'MEDIUM', 'confidence': 'MODERATE', 'claim_class': 'Inferred', 'evidence_ids': ['SYN-001'], 'detail': 'A has a 95.0% outward-to-inward ratio within two hours, but the distinct-payer indicator is absent.', 'recommendation': 'Seek purpose and counterparty evidence without converting the indicator into a criminal conclusion.'}, {'id': 'RF-F02', 'title': 'A narrative-only repetition claim is indeterminate', 'severity': 'MEDIUM', 'confidence': 'LOW', 'claim_class': 'Reported', 'evidence_ids': ['SYN-003'], 'detail': 'C is reported to have three payments, but no original ledger or event times are supplied.', 'recommendation': 'Obtain original events and test whether the descriptions refer to unique posted payments.'}, {'id': 'RF-F03', 'title': 'Own transfers and a single payee provide negative controls', 'severity': 'LOW', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-002', 'SYN-004'], 'detail': 'B is excluded from RF-01 on confirmed ownership; D does not meet the three-payee criterion.', 'recommendation': 'Retain these limited results without declaring either relationship universally low risk.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional case A ledger', 'locator': '10-worked-example.md, events E01–E03', 'claim_class': 'Observed'}, {'id': 'SYN-002', 'title': 'Fictional case B ledger and ownership record', 'locator': '10-worked-example.md, events E04–E05 and ownership note', 'claim_class': 'Observed'}, {'id': 'SYN-003', 'title': 'Fictional uncorroborated case C referral', 'locator': '10-worked-example.md, record N01', 'claim_class': 'Reported'}, {'id': 'SYN-004', 'title': 'Fictional case D ledger', 'locator': '10-worked-example.md, event E06', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Indicator observations', 'value': 5, 'method': 'Count O-01 through O-05', 'format': '#,##0'}, {'label': 'Present indicators', 'value': 1, 'method': 'O-01 only; count states independently of case count', 'format': '#,##0'}, {'label': 'Indeterminate indicators', 'value': 1, 'method': 'O-04 lacks original transaction evidence', 'format': '#,##0'}, {'label': 'Known gross movement USD', 'value': 27500, 'method': 'Sum E01–E06; excludes reported amount in N01', 'format': '$#,##0.00'}], 'limitations': ['Indicator thresholds are authored illustrations rather than regulatory criteria.', 'Case C has a referral narrative but no transaction ledger.', 'No indicator establishes intent, beneficial ownership, or underlying criminal conduct.'], 'conclusion': 'One of five planned observations is present, two are absent, one is indeterminate, and one is not applicable. The supported pattern warrants a targeted inquiry; no indicator establishes criminal conduct.', 'report_narrative': [['One of five planned observations is present, two are absent, one is indeterminate, and one is not applicable. The supported pattern warrants a targeted inquiry; no indicator establishes criminal conduct.'], ['The review covers five planned indicator observations and their explicit applicability tests. The fictional thresholds support reproducible method checks; they are not universal reporting or risk-acceptance criteria.'], ['RF-F01: A has a 95.0% outward-to-inward ratio within two hours, but the distinct-payer indicator is absent.', 'RF-F02: C is reported to have three payments, but no original ledger or event times are supplied.', 'RF-F03: B is excluded from RF-01 on confirmed ownership; D does not meet the three-payee criterion.'], ['Of five observations, one is present, two absent, one indeterminate and one not applicable. Known gross movement is $27,500.00. These states retain separate denominators, and the amount is not a measure of illicit proceeds.'], ['The present pattern supports a targeted inquiry alongside the documented competing explanation. Missing evidence leaves one observation indeterminate; lack of applicability is not a favorable test result.'], ['File 10 supplies the complete synthetic observations, case hypotheses and evidence IDs. Public typology sources inform the review vocabulary, while their indicator descriptions do not establish subject-specific facts.'], ['Seek the evidence that distinguishes the competing hypotheses and resolves the indeterminate observation. Escalate only through the authorized review process; retain all absent and inapplicable observations in the population.'], ['Indicator thresholds are authored illustrations rather than regulatory criteria.', 'Case C has a referral narrative but no transaction ledger.', 'No indicator establishes intent, beneficial ownership, or underlying criminal conduct.', 'QA remains pending and no authorized human disposition is recorded.']], 'suite_id': 'typology-red-flags', 'version': '1.1.0', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'as_of': '2026-10-09', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'RF-F01', 'proposal': 'Seek purpose and counterparty evidence without converting the indicator into a criminal conclusion.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'RF-F02', 'proposal': 'Obtain original events and test whether the descriptions refer to unique posted payments.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'RF-F03', 'proposal': 'Retain these limited results without declaring either relationship universally low risk.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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

OUTPUT = Path(DATA['suite_id'] + '-review.xlsx')
wb = Workbook()
wb.remove(wb.active)
wb.calculation = CalcProperties(calcId=191029, fullCalcOnLoad=True)
wb.properties.creator = 'Markdown Analyst Toolkit'
wb.properties.title = DATA['title']
wb.properties.description = DATA['notice']
ink, muted, header, paper, stripe = '243641', '4E606A', '344E5F', 'F1F2EF', 'E2E8E9'
line = Side(style='thin', color='B8C3C8')

def literal(cell, value):
    if value is None:
        cell.value = None
        cell.comment = Comment('Missing value. Preserve the associated limitation or QA explanation; this is not zero.', 'Toolkit')
        return
    elif isinstance(value, (list, dict)):
        value = '; '.join(map(str, value)) if isinstance(value, list) else str(value)
    if isinstance(value, str) and len(value) > 32767:
        raise ValueError('Excel cell text exceeds 32767 characters; use an evidence summary with an exact source locator and preserve the full source separately.')
    if isinstance(value, (int, float)) and not isinstance(value, bool) and abs(value) >= 10**15:
        raise ValueError('Excel numeric value exceeds 15-digit precision; preserve exact digits as text with a documented domain type and unit instead of silently rounding.')
    cell.value = value
    # Evidence text is data even when it starts with a spreadsheet formula marker.
    if isinstance(value, str):
        cell.data_type = 's'

def sheet(name):
    ws = wb.create_sheet(name)
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = 'B2'
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.print_options.horizontalCentered = True
    ws.print_title_rows = '1:1'
    ws.oddHeader.center.text = DATA['title'].replace('&', '&&')
    ws.oddFooter.left.text = 'Draft for human review'
    ws.oddFooter.right.text = 'Page &P of &N'
    return ws

def populate(ws, columns, rows, table_name=None, formats=None):
    formats = formats or {}
    for col, value in enumerate(columns, 1):
        literal(ws.cell(1, col), value)
    for row_number, values in enumerate(rows, 2):
        if len(values) != len(columns):
            raise ValueError(f'{ws.title}: row {row_number} has wrong column count')
        for col, value in enumerate(values, 1):
            literal(ws.cell(row_number, col), value)
    if table_name and rows:
        tab = Table(displayName=table_name, ref=ws.dimensions)
        tab.tableStyleInfo = TableStyleInfo(name='TableStyleMedium2', showRowStripes=True)
        ws.add_table(tab)
    ws.auto_filter.ref = ws.dimensions
    for col, name in enumerate(columns, 1):
        letter = ws.cell(1, col).column_letter
        long = any(word in name for word in ('detail', 'recommendation', 'proposal', 'method', 'locator', 'rationale'))
        ws.column_dimensions[letter].width = 44 if long else 30 if name in ('title','check') else max(14, min(25, len(name) + 3))
        for cells in ws.iter_rows(min_row=2, min_col=col, max_col=col):
            cell = cells[0]
            if isinstance(cell.value, (float, int)):
                cell.number_format = formats.get(name) or ('$' + '#,##0.00;[Red]($#,##0.00);$0.00' if name.endswith('_usd') else '#,##0.00' if isinstance(cell.value, float) else '#,##0')
    return ws

summary = sheet('Summary')
summary_rows = [
    ['suite', DATA['title'], DATA['suite_id']],
    ['version', DATA['version'], 'Template version'],
    ['as_of', DATA['as_of'], 'Source cutoff, not file creation time'],
    ['status', 'DRAFT', 'Human disposition is not recorded'],
    ['scope', DATA['scope'], 'Coverage must reconcile before release'],
    ['decision_supported', DATA['decision'], 'Decision question; not approval'],
    ['data_label', DATA['notice'], 'Retain synthetic label for examples'],
]
summary_rows += [[m['label'], m['value'], m['method']] for m in DATA['metrics']]
summary_rows += [['limitation', value, 'Preserve in every exported format'] for value in DATA['limitations']]
populate(summary, ['measure', 'value', 'method_or_limit'], summary_rows)
for row_number, metric in enumerate(DATA['metrics'], 9):
    if isinstance(metric['value'], (int, float)):
        summary.cell(row_number, 2).number_format = metric.get('format', '#,##0.00')
summary.column_dimensions['A'].width = 30
summary.column_dimensions['B'].width = 70
summary.column_dimensions['C'].width = 80
dashboard = sheet('Dashboard')
dashboard.append(['severity', 'finding_count', 'denominator'])
finding_columns = ['id', 'title', 'severity', 'confidence', 'claim_class', 'evidence_ids', 'detail', 'recommendation']
findings = populate(sheet('Findings'), finding_columns,
                    [[f[k] for k in finding_columns] for f in DATA['findings']], 'FindingRegister')
for row, level in enumerate(['CRITICAL', 'HIGH', 'MEDIUM', 'LOW'], 2):
    literal(dashboard.cell(row, 1), level)
    dashboard.cell(row, 2, f'=COUNTIF(Findings!C2:C{max(2,len(DATA["findings"])+1)},A{row})')
    literal(dashboard.cell(row, 3), 'All supplied findings; not all underlying activity')
dashboard['A7'] = 'This is a generated snapshot. Regenerate after adding or removing rows.'
dashboard['A8'] = 'Open in a calculating spreadsheet application to refresh formula values.'
dashboard.merge_cells('A7:C7')
dashboard.merge_cells('A8:C8')
dashboard.column_dimensions['A'].width = 27
dashboard.column_dimensions['B'].width = 22
dashboard.column_dimensions['C'].width = 60
chart = BarChart()
chart.title = 'Findings by severity'
chart.y_axis.title = 'Findings'
chart.x_axis.title = 'Severity'
chart.add_data(Reference(dashboard, min_col=2, min_row=1, max_row=5), titles_from_data=True)
chart.set_categories(Reference(dashboard, min_col=1, min_row=2, max_row=5))
chart.style = 13
chart.y_axis.majorUnit = 1
chart.y_axis.scaling.min = 0
chart.series[0].graphicalProperties.solidFill = header
chart.series[0].graphicalProperties.line.solidFill = header
chart.width, chart.height = 23, 10
chart.legend = None
dashboard.add_chart(chart, 'A10')
ev_cols = ['id', 'title', 'locator', 'claim_class']
populate(sheet('Evidence'), ev_cols, [[e[k] for k in ev_cols] for e in DATA['evidence']], 'EvidenceRegister')
action_cols = ['action_id', 'finding_id', 'proposal', 'owner', 'due_date', 'status']
actions = populate(sheet('Actions'), action_cols,
                   [[a['id'], a['finding_id'], a['proposal'], a['owner'] or 'Not provided', a['due_date'] or 'Not provided', a['status']] for a in DATA['actions']], 'ActionRegister')
dv = DataValidation(type='list', formula1='"Proposed,Accepted,In progress,Blocked,Closed,Risk accepted"', allow_blank=False)
dv.errorTitle = 'Use a defined action state'
dv.error = 'Use the list. Closed requires closure evidence in the case record.'
dv.showErrorMessage = True
dv.errorStyle = 'stop'
actions.add_data_validation(dv)
dv.add(f'F2:F{max(2,len(DATA["actions"])+1)}')
qa_cols = ['check_id', 'check', 'result', 'evidence']
populate(sheet('QA'), qa_cols, [[q['id'], q['check'], q['result'], q['evidence']] for q in DATA['qa']], 'QARegister')
for i, t in enumerate(DATA['domain_tables'], 1):
    ws = populate(sheet(t['name']), t['columns'], t['rows'], f'DomainRegister{i}', t.get('formats'))
    stats_row = len(t['rows']) + 3
    literal(ws.cell(stats_row, 1), 'Domain record count')
    literal(ws.cell(stats_row, 2), len(t['rows']))
    literal(ws.cell(stats_row + 1, 1), 'Missing (null) cells')
    literal(ws.cell(stats_row + 1, 2), sum(value is None for row in t['rows'] for value in row))
for ws in wb:
    for row in ws.iter_rows():
        for cell in row:
            cell.font = Font(name='Arial', size=11, color=ink)
            cell.alignment = Alignment(vertical='top', wrap_text=True)
            cell.fill = PatternFill('solid', fgColor=paper if cell.row % 2 else stripe)
            cell.border = Border(bottom=line)
            if cell.row == 1:
                cell.font = Font(name='Arial', size=11, color='FFFFFF', bold=True)
                cell.fill = PatternFill('solid', fgColor=header)
    ws.row_dimensions[1].height = 32
    if sum(dim.width for dim in ws.column_dimensions.values()) > 145:
        ws.page_setup.paperSize = ws.PAPERSIZE_A3
    ws.print_title_cols = 'A:A'
    # No fixed body height: Excel can expand wrapped evidence without clipping.
    ws.print_area = ws.dimensions if ws.title != 'Dashboard' else 'A1:H31'
findings.conditional_formatting.add(f'C2:C{max(2,len(DATA["findings"])+1)}',
    CellIsRule(operator='equal', formula=['"HIGH"'], fill=PatternFill('solid',fgColor='F2DADB'),font=Font(color='7F3038')))
for ws in [summary, dashboard]:
    ws.freeze_panes = 'A2'
summary['A1'].comment = Comment(DATA['notice'] + ' Use file 05 for domain field meanings and file 09 for release checks.', 'Toolkit')
wb.save(OUTPUT)
print(str(OUTPUT))

```

## Release checks

Reopen the saved workbook. Confirm exact sheet order and column names, retained row counts, evidence joins, null handling, leading-zero IDs and literal formula-like text. Compare Dashboard counts to a separately tallied Findings column. Record whether formulas recalculated. Filter and sort without losing IDs or detaching notes. Inspect every sheet at normal zoom and print preview; fix clipped text, empty charts, `####`, unreadable tables and missing rows. These artifact checks supplement the analytical gates in file 09.
