# Regulatory Change and Obligation Mapping — fixed workbook template

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
| ChangeRegister | `change_id`, `instrument_status`, `applicability`, `effective_date`, `compliance_date`, `owner_role`, `priority`, `evidence_ids` |
| ObligationMap | `obligation_id`, `change_id`, `requirement_summary`, `control_id`, `readiness`, `compliance_date`, `evidence_ids` |

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

DATA = {'slug': 'regulatory-change', 'title': 'Regulatory Change and Obligation Mapping', 'summary': 'Translate a supplied public-source change set into provision-level applicability, readiness, and evidence questions without turning proposals into current obligations.', 'audience': 'Regulatory analysts, control owners, and legal reviewers', 'decision': 'Which changes require verified applicability and implementation action, and which remain watch or research items?', 'palette': 'umber', 'report_sections': ['Change priorities and restricted conclusion', 'Scope status and applicability method', 'Material readiness findings', 'Instrument register and date status', 'Obligation mapping and readiness', 'Source evidence and unresolved authority', 'Implementation and verification proposals', 'Limitations quality review and human disposition'], 'domain_tables': [{'name': 'ChangeRegister', 'columns': ['change_id', 'instrument_status', 'applicability', 'effective_date', 'compliance_date', 'owner_role', 'priority', 'evidence_ids'], 'rows': [['CH01', 'PROPOSED', 'Conditional', None, None, 'Regulatory analysis', 'MEDIUM', 'SYN-001'], ['CH02', 'FINAL_NOT_EFFECTIVE', 'In scope', '2026-11-01', '2026-12-01', 'Records owner', 'MEDIUM', 'SYN-001'], ['CH03', 'EFFECTIVE', 'In scope', '2026-09-01', '2026-10-01', 'Review owner', 'HIGH', 'SYN-001'], ['CH04', 'GUIDANCE', 'Reference only', None, None, 'Governance owner', 'LOW', 'SYN-001'], ['CH05', 'WITHDRAWN', 'Not current', None, None, 'Regulatory analysis', 'LOW', 'SYN-001'], ['CH06', 'STATUS_UNVERIFIED', 'Unresolved', None, None, 'Legal review', 'HIGH', 'SYN-001']]}, {'name': 'ObligationMap', 'columns': ['obligation_id', 'change_id', 'requirement_summary', 'control_id', 'readiness', 'compliance_date', 'evidence_ids'], 'rows': [['OB01', 'CH02', 'Retain a review log under fictional provision2', 'CTRL-LOG', 'BUILD', '2026-12-01', 'SYN-001'], ['OB02', 'CH03', 'Evidence escalation review under fictional provision3a', 'CTRL-REV', 'EVIDENCE GAP', '2026-10-01', 'SYN-001'], ['OB03', 'CH03', 'Complete role training under fictional provision3b', 'CTRL-TRN', 'VERIFIED FOR FIXTURE', '2026-10-01', 'SYN-001'], ['OB04', 'CH01', 'Potential reporting field under proposed provision1', 'CTRL-PROP', 'SCENARIO ONLY', None, 'SYN-001'], ['OB05', 'CH04', 'Consider governance review practice', 'CTRL-GOV', 'REFERENCE ONLY', None, 'SYN-001']]}], 'findings': [{'id': 'RC-F01', 'title': 'Evidence for an effective fictional requirement remains missing', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'OB02 has no retained review evidence as of 2026-10-09; the fictional compliance date is 2026-10-01. A legal breach is not established by missing evidence alone.', 'recommendation': 'Obtain execution evidence and route the applicability and consequence assessment to an authorized reviewer.'}, {'id': 'RC-F02', 'title': 'A near-term claimed change lacks primary-source status confirmation', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001'], 'detail': 'CH06 is supported only by a fictional secondary summary. Its claimed date is not copied into confirmed deadline fields.', 'recommendation': 'Retrieve primary material or keep status unverified and document interim review needs.'}, {'id': 'RC-F03', 'title': 'Future final requirement needs implementation evidence', 'severity': 'MEDIUM', 'confidence': 'MODERATE', 'claim_class': 'Inferred', 'evidence_ids': ['SYN-001'], 'detail': 'OB01 remains in build status ahead of the fictional 2026-12-01 compliance date. Readiness has not been evidenced.', 'recommendation': 'Define accountable milestones and acceptance tests for human approval.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional six-instrument change set and implementation evidence', 'locator': '10-worked-example.md, source cards and obligation mapping', 'claim_class': 'Observed'}, {'id': 'REF-001', 'title': 'National Archives Federal Register Tutorial', 'locator': 'https://www.archives.gov/federal-register/tutorial/text', 'claim_class': 'Reported'}, {'id': 'REF-002', 'title': 'Administrative Procedure Act,5 U.S.C. 553', 'locator': 'https://www.archives.gov/federal-register/laws/administrative-procedure/553.html', 'claim_class': 'Reported'}, {'id': 'REF-003', 'title': 'National Archives Office of the Federal Register FAQs', 'locator': 'https://www.archives.gov/federal-register/faqs', 'claim_class': 'Reported'}], 'metrics': [{'label': 'Tracked instruments', 'value': '6', 'method': 'Distinct CH01–CH06 source cards, preserving proposed, withdrawn, and unverified states.', 'format': '#,##0'}, {'label': 'Confirmed final in-scope instruments', 'value': '2', 'method': 'CH02 final-not-effective plus CH03 effective; excludes guidance and proposals.', 'format': '#,##0'}, {'label': 'Effective mapped evidence coverage', 'value': '1 of 2 (50.0%)', 'method': 'OB03 verified / OB02 and OB03 effective mapped requirements; not a compliance score.', 'format': '#,##0'}], 'limitations': ['All six change instruments and organization facts are fictional.', 'A proposal, guidance item, or secondary report is not a verified current legal obligation.', 'Missing execution evidence does not alone prove legal noncompliance.', 'Readiness counts do not measure the completeness of all applicable legal obligations.'], 'conclusion': 'Prioritize the missing evidence for OB02 and primary-source confirmation for CH06 while planning the future CH02 requirement. One of two effective mapped fixture requirements has verified evidence; this is evidence coverage, not a compliance score.', 'report_narrative': [['Prioritize OB02’s evidence gap and CH06’s missing primary-source confirmation, while planning CH02’s future requirement. One of two effective mapped fixture requirements has verified evidence; this is not a compliance score.'], ['The review is as of Oct 09, 2026 and covers six invented instruments for a fictional Type A entity carrying Activity Q. Status, applicability, dates, and readiness are assessed separately using the complete source cards in SYN-001.'], ['OB02 lacks execution evidence after its explicit fictional compliance date. CH06 has only a secondary claim and no confirmed deadline. OB01 remains in build status ahead of its future compliance date; that supports a readiness concern, not a prediction of missed implementation.'], ['ChangeRegister preserves one proposed, one final-not-effective, one effective, one guidance, one withdrawn, and one unverified item. Only CH02 and CH03 have confirmed effective and compliance dates in the fixture.'], ['ObligationMap has five rows: one future requirement, two effective requirements, one proposal scenario, and one reference item. The effective evidence denominator is OB02 and OB03; only OB03 is verified for the fixture, giving 1/2 = 50.0%.'], ['SYN-001 contains fictional source cards and implementation evidence. CH06’s claimed Oct 15 date remains in the evidence narrative rather than confirmed deadline fields. The National Archives references support research method, not the invented legal requirements.'], ['Propose retrieval of OB02 evidence, primary verification for CH06, and accountable acceptance milestones for OB01. Keep CH01 as scenario planning, CH04 as reference context, and CH05 as historical withdrawal.'], ['QA rejects proposal-to-obligation conversion, comment-date substitution, and breach conclusions from missing evidence alone. Human reviewers retain legal interpretation, applicability, commitments, and final readiness decisions.']], 'suite_id': 'regulatory-change', 'version': '1.0.0', 'as_of': '2026-10-09', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'RC-F01', 'proposal': 'Obtain execution evidence and route the applicability and consequence assessment to an authorized reviewer.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'RC-F02', 'proposal': 'Retrieve primary material or keep status unverified and document interim review needs.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'RC-F03', 'proposal': 'Define accountable milestones and acceptance tests for human approval.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
