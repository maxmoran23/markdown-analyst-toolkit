# Fraud Incident Review — fixed workbook template

Version 1.0.0. The workbook is a generated review snapshot with visible evidence and explicit open decisions. Use an in-session file-creation capability; no terminal, repository checkout or automation is needed.

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
| IncidentAmounts | `case_id`, `currency`, `requested_amount`, `executed_amount`, `confirmed_return_amount`, `net_unreturned_amount`, `amount_status`, `review_state` |
| VerificationReview | `case_id`, `authorization_basis`, `detail_change`, `independent_verification`, `payment_status`, `time_sensitivity`, `proposed_action`, `evidence_ids` |

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

DATA = {'slug': 'fraud-review', 'title': 'Fraud Incident Review', 'summary': 'Separate payment instructions from actual execution, verify authorization evidence, reconcile returns, and prepare proportionate incident actions for an authorized human responder.', 'audience': 'Fraud analysts, payment-control reviewers, incident coordinators, and quality reviewers', 'decision': 'What is known about authorization, execution, and remaining exposure, and which time-sensitive actions should an authorized responder consider?', 'palette': 'umber', 'report_sections': ['Incident priorities and known exposure', 'Scope, incident population, and amount method', 'Findings and verification gaps', 'Requested, executed, and returned amounts', 'Authorization and incident-response review', 'Evidence and source provenance', 'Proposed actions for authorized responders', 'Limitations, quality checks, and human disposition'], 'domain_tables': [{'name': 'IncidentAmounts', 'columns': ['case_id', 'currency', 'requested_amount', 'executed_amount', 'confirmed_return_amount', 'net_unreturned_amount', 'amount_status', 'review_state'], 'rows': [['F01', 'USD', 40000, 40000, 10000, 30000, 'CONFIRMED', 'SUSPECTED_FRAUD'], ['F02', 'USD', 15000, 0, 0, 0, 'CONFIRMED', 'PREVENTED_REQUEST'], ['F03', 'USD', 12000, None, None, None, 'EXECUTION_UNKNOWN', 'OPEN_ALLEGATION'], ['F04', 'USD', 5000, 5000, 0, 5000, 'CONFIRMED', 'BENIGN_SUPPORTED']], 'formats': {'requested_amount': '#,##0.00', 'executed_amount': '#,##0.00', 'confirmed_return_amount': '#,##0.00', 'net_unreturned_amount': '#,##0.00'}}, {'name': 'VerificationReview', 'columns': ['case_id', 'authorization_basis', 'detail_change', 'independent_verification', 'payment_status', 'time_sensitivity', 'proposed_action', 'evidence_ids'], 'rows': [['F01', 'Impersonated supplier instruction reported', 'New beneficiary', 'Known-channel supplier denial documented', 'EXECUTED_PARTIAL_RETURN', 'HIGH', 'Authorized fraud responder review and recovery assessment', 'SYN-001;SYN-002'], ['F02', 'Suspicious instruction identified before execution', 'New beneficiary', 'Request failed established verification', 'NOT_EXECUTED', 'MEDIUM', 'Preserve instruction and verify cancellation state', 'SYN-003;SYN-004'], ['F03', 'Employee reports unauthorized payroll change', 'Payroll destination changed', 'No independent logs or ledger supplied', 'UNKNOWN', 'HIGH', 'Obtain ledger and access logs through approved incident process', 'SYN-005;SYN-006'], ['F04', 'Amended contract and approved instruction', 'New beneficiary', 'Preexisting trusted-channel confirmation documented', 'EXECUTED', 'LOW', 'Document supported ordinary change and human disposition', 'SYN-007;SYN-008']]}], 'findings': [{'id': 'FR-F01', 'title': 'Suspected supplier impersonation has $30,000.00 unreturned', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001', 'SYN-002'], 'detail': 'F01 has a $40,000.00 posted payment and $10,000.00 confirmed linked return. The supplier denial is documented; ultimate loss and liability remain undecided.', 'recommendation': 'Route to the authorized fraud responder for time-sensitive review and permitted recovery assessment.'}, {'id': 'FR-F02', 'title': 'A prevented request must not be counted as executed loss', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-003', 'SYN-004'], 'detail': 'F02 requested $15,000.00 but the supplied instruction and ledger status confirm no execution.', 'recommendation': 'Retain the attempted request and verify the cancellation remains effective; do not claim an actual loss or proven savings.'}, {'id': 'FR-F03', 'title': 'Payroll allegation has unknown execution status', 'severity': 'HIGH', 'confidence': 'LOW', 'claim_class': 'Reported', 'evidence_ids': ['SYN-005', 'SYN-006'], 'detail': 'F03 reports $12,000.00 at issue, but neither posting records nor access logs are supplied.', 'recommendation': 'Obtain execution and authorization evidence urgently through the approved human process; keep exposure null.'}, {'id': 'FR-F04', 'title': 'A beneficiary change has a supported ordinary explanation', 'severity': 'LOW', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-007', 'SYN-008'], 'detail': 'F04 has a $5,000.00 ordinary payment supported by an amended contract and trusted-channel confirmation.', 'recommendation': 'Document the evidence and seek human disposition; exclude this payment from suspected-fraud exposure totals.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional supplier instruction and denial record', 'locator': '10-worked-example.md, source R01', 'claim_class': 'Reported'}, {'id': 'SYN-002', 'title': 'Fictional F01 ledger and return', 'locator': '10-worked-example.md, source R02', 'claim_class': 'Observed'}, {'id': 'SYN-003', 'title': 'Fictional suspicious request', 'locator': '10-worked-example.md, source R03', 'claim_class': 'Reported'}, {'id': 'SYN-004', 'title': 'Fictional rejected-instruction ledger state', 'locator': '10-worked-example.md, source R04', 'claim_class': 'Observed'}, {'id': 'SYN-005', 'title': 'Fictional payroll complaint', 'locator': '10-worked-example.md, source R05', 'claim_class': 'Reported'}, {'id': 'SYN-006', 'title': 'Fictional missing-source inventory', 'locator': '10-worked-example.md, source R06', 'claim_class': 'Observed'}, {'id': 'SYN-007', 'title': 'Fictional amended contract and confirmation', 'locator': '10-worked-example.md, source R07', 'claim_class': 'Observed'}, {'id': 'SYN-008', 'title': 'Fictional ordinary payment ledger', 'locator': '10-worked-example.md, source R08', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Requests reviewed', 'value': 4, 'method': 'Distinct cases F01–F04', 'format': '#,##0'}, {'label': 'Known requested amount USD', 'value': 72000, 'method': '40000+15000+12000+5000; includes alleged and ordinary requests, not loss', 'format': '$#,##0.00'}, {'label': 'Known suspected-fraud unreturned USD', 'value': 30000, 'method': 'F01 executed40000-return10000; F02 zero; F03 unknown; F04 excluded as ordinary', 'format': '$#,##0.00'}, {'label': 'Confirmed unexecuted request USD', 'value': 15000, 'method': 'F02 request amount with confirmed nonexecution; not measured savings', 'format': '$#,##0.00'}], 'limitations': ['The example does not establish legal liability, customer reimbursement, or final fraud loss.', 'F03 execution and recovery are unknown; its $12,000.00 request is not imputed as loss or zero exposure.', 'No recovery request, account restriction, external contact, or filing is executed by this suite.'], 'conclusion': 'Known suspected-fraud unreturned value is $30,000.00, with one payroll allegation still lacking execution evidence. A $15,000.00 request did not execute, and a supported ordinary $5,000.00 payment is excluded from the suspected-fraud subtotal.', 'report_narrative': [['Known suspected-fraud unreturned value is $30,000.00, with one payroll allegation still lacking execution evidence. A $15,000.00 request did not execute, and a supported ordinary $5,000.00 payment is excluded from the suspected-fraud subtotal.'], ['Four requests are reviewed using separate requested, executed, returned and unresolved amount states. The example contains one unexecuted request, one supported ordinary payment and one allegation without execution evidence.'], ['FR-F01: F01 has a $40,000.00 posted payment and $10,000.00 confirmed linked return. The supplier denial is documented; ultimate loss and liability remain undecided.', 'FR-F02: F02 requested $15,000.00 but the supplied instruction and ledger status confirm no execution.', 'FR-F03: F03 reports $12,000.00 at issue, but neither posting records nor access logs are supplied.', 'FR-F04: F04 has a $5,000.00 ordinary payment supported by an amended contract and trusted-channel confirmation.'], ['Known requested value is $72,000.00. Known suspected-fraud unreturned value is $30,000.00; the $15,000.00 unexecuted request is excluded from that subtotal, as is the supported ordinary $5,000.00 payment.'], ['The payroll allegation remains unresolved because execution evidence is missing. Verification and response steps remain proposed for authorized responders; the analytical record does not claim that funds were frozen, recalled or recovered.'], ['The fictional request, execution and return records in file 10 support distinct amount fields. Reported authorization and fraud allegations remain attributed; no assumption converts missing execution into a confirmed loss.'], ['Prioritize verification and the documented time-sensitive response options through authorized channels. Obtain payroll execution evidence and maintain the separation between suspected-fraud exposure, ordinary payments and unexecuted attempts.'], ['The example does not establish legal liability, customer reimbursement, or final fraud loss.', 'F03 execution and recovery are unknown; its $12,000.00 request is not imputed as loss or zero exposure.', 'No recovery request, account restriction, external contact, or filing is executed by this suite.', 'QA remains pending and no authorized human disposition is recorded.']], 'suite_id': 'fraud-review', 'version': '1.0.0', 'as_of': '2026-10-09', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'FR-F01', 'proposal': 'Route to the authorized fraud responder for time-sensitive review and permitted recovery assessment.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'FR-F02', 'proposal': 'Retain the attempted request and verify the cancellation remains effective; do not claim an actual loss or proven savings.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'FR-F03', 'proposal': 'Obtain execution and authorization evidence urgently through the approved human process; keep exposure null.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-004', 'finding_id': 'FR-F04', 'proposal': 'Document the evidence and seek human disposition; exclude this payment from suspected-fraud exposure totals.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
