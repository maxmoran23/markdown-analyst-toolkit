# Ownership Analysis — fixed workbook template

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
| OwnershipEdges | `edge_id`, `owner_id`, `owned_entity_id`, `interest_pct`, `interest_basis`, `effective_date`, `evidence_ids`, `notes` |
| UltimateInterests | `ultimate_id`, `target_id`, `economic_interest_pct`, `path_ids`, `resolution_state`, `control_state`, `claim_class`, `evidence_ids`, `notes` |

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

DATA = {'slug': 'ownership-analysis', 'title': 'Ownership Analysis', 'summary': 'Trace dated ownership edges, economic paths, unresolved branches, and control rights with separate legal overlays.', 'audience': 'Analysts reviewing layered ownership structures and public ownership disclosures', 'decision': 'Which ultimate economic interests are supported by the dated graph, and what evidence or interpretation remains missing?', 'palette': 'indigo', 'report_sections': ['Ownership decision brief', 'Scope and graph method', 'Material findings', 'Direct ownership assessment', 'Ultimate interests and unresolved branches', 'Evidence record', 'Recommended ownership review actions', 'Limitations and human review'], 'domain_tables': [{'name': 'OwnershipEdges', 'columns': ['edge_id', 'owner_id', 'owned_entity_id', 'interest_pct', 'interest_basis', 'effective_date', 'evidence_ids', 'notes'], 'formats': {'interest_pct': '0.0"%"'}, 'rows': [['OW-01', 'PERSON-A', 'HOLDCO', 60, 'Ordinary economic equity', '2026-09-30', 'SYN-001', 'Fictional supplied schedule'], ['OW-02', 'PERSON-B', 'HOLDCO', 40, 'Ordinary economic equity', '2026-09-30', 'SYN-001', 'Fictional supplied schedule'], ['OW-03', 'HOLDCO', 'TARGET', 50, 'Ordinary economic equity', '2026-09-30', 'SYN-001', 'Intermediate holding'], ['OW-04', 'PERSON-A', 'TARGET', 10, 'Ordinary economic equity', '2026-09-30', 'SYN-001', 'Separate direct holding'], ['OW-05', 'PERSON-C', 'TARGET', 25, 'Ordinary economic equity', '2026-09-30', 'SYN-001', 'Reported veto right assessed separately'], ['OW-06', 'UNKNOWN-POOL', 'TARGET', 15, 'Ordinary economic equity', '2026-09-30', 'SYN-001', 'Amount known; holders unresolved']]}, {'name': 'UltimateInterests', 'columns': ['ultimate_id', 'target_id', 'economic_interest_pct', 'path_ids', 'resolution_state', 'control_state', 'claim_class', 'evidence_ids', 'notes'], 'formats': {'economic_interest_pct': '0.0"%"'}, 'rows': [['PERSON-A', 'TARGET', 40, 'OW-01>OW-03;OW-04', 'RESOLVED ON SUPPLIED GRAPH', 'NOT ASSESSED', 'Estimated', 'SYN-001', '60 percent × 50 percent + 10 percent'], ['PERSON-B', 'TARGET', 20, 'OW-02>OW-03', 'RESOLVED ON SUPPLIED GRAPH', 'NOT ASSESSED', 'Estimated', 'SYN-001', '40 percent × 50 percent'], ['PERSON-C', 'TARGET', 25, 'OW-05', 'RESOLVED ON SUPPLIED GRAPH', 'REPORTED RIGHTS', 'Reported', 'SYN-001', 'Veto scope and legal effect not established'], ['UNKNOWN-POOL', 'TARGET', 15, 'OW-06', 'UNRESOLVED', 'NOT ASSESSED', 'Reported', 'SYN-001', 'Do not allocate residual to known holders']]}], 'findings': [{'id': 'F-01', 'title': 'Unidentified holders account for 15.0%', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'UNKNOWN-POOL holds a reported 15.0% direct target interest without identified underlying holders.', 'recommendation': 'Obtain the missing holder schedule and effective-date evidence.'}, {'id': 'F-02', 'title': 'Known terminal economic interests total 85.0%', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Estimated', 'evidence_ids': ['SYN-001'], 'detail': 'Person A 40.0% + Person B 20.0% + Person C 25.0% under proportional acyclic assumptions.', 'recommendation': 'Preserve path arithmetic, reported-source status, and separate legal questions.'}, {'id': 'F-03', 'title': 'Reported veto right lacks supporting instrument', 'severity': 'MEDIUM', 'confidence': 'LOW', 'claim_class': 'Reported', 'evidence_ids': ['SYN-001'], 'detail': 'Person C reportedly has a veto over certain asset sales; scope and governing document are absent.', 'recommendation': 'Obtain rights evidence before drawing a control conclusion.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional ownership graph', 'locator': '10-worked-example.md, OW-01 through OW-06', 'claim_class': 'Observed'}, {'id': 'REF-CDD', 'title': 'FinCEN CDD overview', 'locator': 'https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule', 'claim_class': 'Observed'}, {'id': 'REF-CDD-2026', 'title': 'FinCEN FIN-2026-R001', 'locator': 'https://www.fincen.gov/system/files/2026-02/FinCEN-Order-CCDExceptiveRelief.pdf', 'claim_class': 'Observed'}, {'id': 'REF-OFAC-401', 'title': 'OFAC FAQ 401', 'locator': 'https://ofac.treasury.gov/faqs/401', 'claim_class': 'Observed'}, {'id': 'REF-OFAC-398', 'title': 'OFAC FAQ 398', 'locator': 'https://ofac.treasury.gov/faqs/398', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Known terminal economic interests', 'value': '85.0%', 'method': '40.0% Person A + 20.0% Person B + 25.0% Person C.', 'format': '#,##0'}, {'label': 'Unresolved economic interest', 'value': '15.0%', 'method': '100.0% less 85.0% known terminal interests.', 'format': '#,##0'}, {'label': 'Direct edges', 'value': '6', 'method': 'Count distinct OW-01 through OW-06; no graph-wide percentage sum.', 'format': '#,##0'}], 'limitations': ['All holdings and rights are fictional reported inputs.', 'Simple path multiplication requires comparable proportional rights and no cycles or overlap.', 'Economic interest, control, legal beneficial ownership, and sanctions propagation are distinct questions.'], 'metadata': {'conclusion': 'The fictional graph supports estimated economic interests of 40.0% for Person A, 20.0% for Person B, and a reported 25.0% for Person C. A further 15.0% remains unresolved, and the reported veto right requires evidence before any control conclusion.'}, 'report_narrative': [['The fictional graph supports estimated economic interests of 40.0% for Person A, 20.0% for Person B, and a reported 25.0% for Person C. A further 15.0% remains unresolved, and the reported veto right requires evidence before any control conclusion.'], ['The review uses six dated direct ownership edges for an acyclic, proportional economic-equity graph. It assesses path arithmetic and unresolved branches separately from control, legal beneficial ownership and sanctions propagation.'], ['F-01: UNKNOWN-POOL holds a reported 15.0% direct target interest without identified underlying holders.', 'F-02: Person A 40.0% + Person B 20.0% + Person C 25.0% under proportional acyclic assumptions.', 'F-03: Person C reportedly has a veto over certain asset sales; scope and governing document are absent.'], ['HOLDCO is owned 60.0% by PERSON-A and 40.0% by PERSON-B. TARGET is held 50.0% by HOLDCO, 10.0% directly by PERSON-A, 25.0% by PERSON-C and 15.0% by unidentified holders. Distinct direct and indirect holdings are retained.'], ['PERSON-A has 60.0% × 50.0% + 10.0% = 40.0%; PERSON-B has 40.0% × 50.0% = 20.0%; PERSON-C has 25.0%. Resolved terminal interests total 85.0%; the 15.0% residual is not reallocated. The reported veto right lacks its supporting instrument.'], ['SYN-001 supplies the fictional reported schedule and rights assertion. The arithmetic is conditional on comparable proportional rights and no overlapping or circular interests; source verification remains distinct from calculation.'], ['Obtain the missing holder schedule and rights instrument. Reassess effective dates, share classes and path overlap before carrying these economic results into any separate legal test.'], ['All holdings and rights are fictional reported inputs.', 'Simple path multiplication requires comparable proportional rights and no cycles or overlap.', 'Economic interest, control, legal beneficial ownership, and sanctions propagation are distinct questions.', 'QA remains pending and no authorized human disposition is recorded.']], 'suite_id': 'ownership-analysis', 'version': '1.0.0', 'as_of': '2026-10-09', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'conclusion': 'The fictional graph supports estimated economic interests of 40.0% for Person A, 20.0% for Person B, and a reported 25.0% for Person C. A further 15.0% remains unresolved, and the reported veto right requires evidence before any control conclusion.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'F-01', 'proposal': 'Obtain the missing holder schedule and effective-date evidence.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'F-02', 'proposal': 'Preserve path arithmetic, reported-source status, and separate legal questions.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'F-03', 'proposal': 'Obtain rights evidence before drawing a control conclusion.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
