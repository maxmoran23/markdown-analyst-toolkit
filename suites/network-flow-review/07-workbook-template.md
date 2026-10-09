# Network and Funds Flow Review — fixed workbook template

Version 1.2.0. The workbook is a generated review snapshot with visible evidence and explicit open decisions. Use an in-session file-creation capability; no terminal, repository checkout or automation is needed.

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
| Nodes | `node_id`, `node_type`, `entity_id`, `identity_basis`, `opening_usd`, `evidence_ids`, `scope_limit` |
| EconomicEdges | `edge_id`, `hour_index`, `from_node`, `to_node`, `amount_usd`, `currency`, `own_transfer`, `return_of`, `evidence_ids`, `identity_status` |
| BalanceChecks | `balance_id`, `perimeter`, `opening_usd`, `inflow_usd`, `outflow_usd`, `calculated_close_usd`, `supplied_close_usd`, `difference_usd`, `evidence_ids` |
| PatternTests | `pattern_id`, `pattern`, `edge_ids`, `measure_usd`, `count`, `interpretation`, `evidence_ids` |
| AllocationBounds | `allocation_id`, `target_edge`, `source_group`, `available_usd`, `other_available_usd`, `debit_usd`, `lower_usd`, `upper_usd`, `basis`, `evidence_ids` |
| AttributionScenarios | `scenario_id`, `method`, `p_usd`, `q_usd`, `opening_usd`, `total_usd`, `status`, `evidence_ids` |
| DecisionRecord | `decision_id`, `question`, `status`, `reason`, `evidence_ids` |
| ProcessQA | `check_id`, `check`, `expected`, `actual`, `result`, `evidence_ids` |

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
- Summary also retains the conclusion, every method and all eight report sections' narrative paragraphs in ordered, individually identified rows. Preserve their exact section names in `method_or_limit`; a workbook handoff must retain the reasoning alongside the domain tables.
- `openpyxl` writes formulas but does not calculate them. Request recalculation in Excel or the available spreadsheet engine, inspect results, and record the outcome. If unavailable, label formula-cache/display behavior **NOT TESTED**; the independently computed check does not prove Excel behavior.

## Complete in-session renderer

For portable case data, write integer fields and report placement as whole-number JSON literals such as `1` and `4`, without a decimal suffix. Python enforces integer types; JavaScript parses `1` and `1.0` as the same number. HTML rejects integers outside JavaScript's safe range, and Excel applies its stricter 15-digit boundary. Preserve exact large identifiers or quantities as text under the declared field contract. These runtime constraints are not identical validators or a guarantee of exact floating-point arithmetic.

Use this block when `openpyxl` is already available in the chat's Python capability. No installation is required or assumed. When unavailable, ask the assistant's approved workbook capability to implement the same schema and style. If that is unavailable too, emit one copy-ready table per sheet and state **XLSX not created**. Never label CSV as a multi-sheet workbook.

The renderer checks required fields, identifiers, evidence joins, sheet names and finite numbers before writing. It rejects cell text above Excel's 32,767-character limit rather than silently truncating evidence. Preserve the complete source separately and put an attributed summary with its exact source locator in the workbook. Passing these structural checks does not establish that a claim or calculation is correct.

Excel numeric precision is limited to 15 significant digits. This renderer rejects numeric magnitudes of 10^15 or larger. Store exact large integers, identifiers and atomic token quantities as text under an explicitly documented domain type and unit. Fractional numeric values remain floating-point approximations; preserve the original source string whenever all decimal digits are material and apply the stated calculation precision before display.

All output formats limit declared decimal display places to 15. This is a portable rendering boundary, not a claim of 15-decimal calculation accuracy. Keep more precise source quantities as exact text with the declared unit when their digits matter.

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

DATA = {'slug': 'network-flow-review', 'title': 'Network and Funds Flow Review', 'summary': 'Normalize economic transfers, preserve identity evidence, reconcile account and entity boundaries, and distinguish graph patterns from provable source attribution.', 'audience': 'Financial investigators and analysts reviewing supplied transaction networks', 'decision': 'What graph relationships and funds-flow quantities are supported, and where does commingling or incomplete visibility prevent attribution?', 'palette': 'teal', 'as_of': '2026-09-03T09:00:00-04:00', 'scope': 'Fictional nine-node graph with 24 ordered posted transfers, complete A1/A2 ledgers, partial counterparty visibility and USD native units. No external investigation or identity discovery is performed.', 'report_sections': ['Decision question and supported flow conclusions', 'Scope, perimeter and normalization', 'Findings and attribution limits', 'Nodes and canonical economic transfers', 'Balance equations, patterns and allocation bounds', 'Evidence and identity provenance', 'Proposed discriminating inquiries', 'Quality checks, limitations and human decision'], 'domain_tables': [{'name': 'Nodes', 'columns': ['node_id', 'node_type', 'entity_id', 'identity_basis', 'opening_usd', 'evidence_ids', 'scope_limit'], 'column_contracts': {'node_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Account or counterparty node; aliases are not silently merged.'}, 'node_type': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Representation type.', 'enum': ['ACCOUNT', 'COUNTERPARTY']}, 'entity_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Recorded or verified entity grouping; beneficial ownership not implied.'}, 'identity_basis': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Strength and scope of grouping.', 'enum': ['VERIFIED', 'RECORDED']}, 'opening_usd': {'type': 'number', 'nullable': True, 'unit': 'USD', 'description': 'Supplied opening balance for complete review accounts; null elsewhere.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}, 'scope_limit': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Visibility limitation affecting balance and graph claims.'}}, 'rows': [['A1', 'ACCOUNT', 'ENTITY-A', 'VERIFIED', 1000, 'N01;N02', 'Review account; complete in-period ledger'], ['A2', 'ACCOUNT', 'ENTITY-A', 'VERIFIED', 500, 'N01;N02', 'Same entity as A1; complete ledger'], ['P', 'COUNTERPARTY', 'ENTITY-P', 'RECORDED', None, 'N01', 'Recorded remitter/beneficiary; no beneficial-owner assertion'], ['Q', 'COUNTERPARTY', 'ENTITY-Q', 'RECORDED', None, 'N01', 'Recorded remitter; other activity outside scope'], ['R', 'COUNTERPARTY', 'ENTITY-R', 'RECORDED', None, 'N01', 'Recorded remitter; other activity outside scope'], ['C', 'COUNTERPARTY', 'ENTITY-C', 'RECORDED', None, 'N01;N03', 'Direct counterparty with one linked return'], ['D', 'COUNTERPARTY', 'ENTITY-D', 'RECORDED', None, 'N01;N03', 'Direct counterparty with one linked return'], ['E', 'COUNTERPARTY', 'ENTITY-E', 'RECORDED', None, 'N01;N04', 'Additional supplied onward record; complete ledger unavailable'], ['F', 'COUNTERPARTY', 'ENTITY-F', 'RECORDED', None, 'N01;N04', 'Additional supplied onward record; complete ledger unavailable']], 'primary_key': ['node_id'], 'grain': 'One distinct supplied account/counterparty node; nine total.', 'report_section': 4, 'formats': {'opening_usd': '$#,##0.00'}}, {'name': 'EconomicEdges', 'columns': ['edge_id', 'hour_index', 'from_node', 'to_node', 'amount_usd', 'currency', 'own_transfer', 'return_of', 'evidence_ids', 'identity_status'], 'column_contracts': {'edge_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique canonical economic transfer identifier.'}, 'hour_index': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Strict fixture order: hours1–24 after the declared start.'}, 'from_node': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Immediate recorded sender node.'}, 'to_node': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Immediate recorded receiver node.'}, 'amount_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Positive value of this transfer leg; summing paths repeats capital.'}, 'currency': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Native monetary unit.', 'enum': ['USD']}, 'own_transfer': {'type': 'boolean', 'nullable': False, 'unit': 'flag', 'description': 'True only when both accounts belong to verified Entity-A.'}, 'return_of': {'type': 'text', 'nullable': True, 'unit': 'identifier', 'description': 'Explicit original debit edge for a linked return; null otherwise.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}, 'identity_status': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Counterparty labels as recorded; no guilt or control claim.', 'enum': ['RECORDED']}}, 'rows': [['E01', 1, 'P', 'A1', 10000, 'USD', False, None, 'N01', 'RECORDED'], ['E02', 2, 'Q', 'A1', 8000, 'USD', False, None, 'N01', 'RECORDED'], ['E03', 3, 'A1', 'C', 12000, 'USD', False, None, 'N01', 'RECORDED'], ['E04', 4, 'A1', 'A2', 4000, 'USD', True, None, 'N01', 'RECORDED'], ['E05', 5, 'A2', 'D', 3000, 'USD', False, None, 'N01', 'RECORDED'], ['E06', 6, 'R', 'A1', 6000, 'USD', False, None, 'N01', 'RECORDED'], ['E07', 7, 'A1', 'C', 5000, 'USD', False, None, 'N01', 'RECORDED'], ['E08', 8, 'C', 'A1', 1000, 'USD', False, 'E03', 'N01;N03', 'RECORDED'], ['E09', 9, 'A1', 'E', 2000, 'USD', False, None, 'N01', 'RECORDED'], ['E10', 10, 'E', 'F', 1500, 'USD', False, None, 'N01;N04', 'RECORDED'], ['E11', 11, 'F', 'A1', 1000, 'USD', False, None, 'N01', 'RECORDED'], ['E12', 12, 'A1', 'P', 2000, 'USD', False, None, 'N01', 'RECORDED'], ['E13', 13, 'P', 'A1', 1500, 'USD', False, None, 'N01', 'RECORDED'], ['E14', 14, 'Q', 'A1', 3000, 'USD', False, None, 'N01', 'RECORDED'], ['E15', 15, 'A1', 'D', 4500, 'USD', False, None, 'N01', 'RECORDED'], ['E16', 16, 'A2', 'A1', 500, 'USD', True, None, 'N01', 'RECORDED'], ['E17', 17, 'A1', 'F', 1000, 'USD', False, None, 'N01', 'RECORDED'], ['E18', 18, 'F', 'D', 500, 'USD', False, None, 'N01;N04', 'RECORDED'], ['E19', 19, 'R', 'A1', 2000, 'USD', False, None, 'N01', 'RECORDED'], ['E20', 20, 'A1', 'C', 2500, 'USD', False, None, 'N01', 'RECORDED'], ['E21', 21, 'D', 'A1', 1000, 'USD', False, 'E15', 'N01;N03', 'RECORDED'], ['E22', 22, 'A1', 'E', 1500, 'USD', False, None, 'N01', 'RECORDED'], ['E23', 23, 'E', 'A1', 500, 'USD', False, None, 'N01', 'RECORDED'], ['E24', 24, 'A1', 'C', 500, 'USD', False, None, 'N01', 'RECORDED']], 'primary_key': ['edge_id'], 'grain': 'One posted economic transfer; duplicate representations and nonexecuted instructions excluded.', 'report_section': 4, 'formats': {'hour_index': '#,##0', 'amount_usd': '$#,##0.00'}, 'foreign_keys': [{'columns': ['from_node'], 'table': 'Nodes', 'references': ['node_id']}, {'columns': ['to_node'], 'table': 'Nodes', 'references': ['node_id']}]}, {'name': 'BalanceChecks', 'columns': ['balance_id', 'perimeter', 'opening_usd', 'inflow_usd', 'outflow_usd', 'calculated_close_usd', 'supplied_close_usd', 'difference_usd', 'evidence_ids'], 'column_contracts': {'balance_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique account/perimeter equation identifier.'}, 'perimeter': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Account or consolidated entity being reconciled.'}, 'opening_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Supplied opening balance.'}, 'inflow_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Recorded credits; consolidated excludes own transfers.'}, 'outflow_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Recorded debits; consolidated excludes own transfers.'}, 'calculated_close_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Opening plus inflow minus outflow.'}, 'supplied_close_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Independent supplied closing amount.'}, 'difference_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Calculated minus supplied close.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['B01', 'A1', 1000, 34500, 35000, 500, 500, 0, 'N01;N02'], ['B02', 'A2', 500, 4000, 3500, 1000, 1000, 0, 'N01;N02'], ['B03', 'ENTITY-A', 1500, 34000, 34000, 1500, 1500, 0, 'N01;N02']], 'primary_key': ['balance_id'], 'grain': 'One valid equation for a complete supplied perimeter.', 'report_section': 5, 'formats': {'opening_usd': '$#,##0.00', 'inflow_usd': '$#,##0.00', 'outflow_usd': '$#,##0.00', 'calculated_close_usd': '$#,##0.00', 'supplied_close_usd': '$#,##0.00', 'difference_usd': '$#,##0.00'}}, {'name': 'PatternTests', 'columns': ['pattern_id', 'pattern', 'edge_ids', 'measure_usd', 'count', 'interpretation', 'evidence_ids'], 'column_contracts': {'pattern_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable graph observation identifier.'}, 'pattern': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Precisely defined topology or temporal pattern.'}, 'edge_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited canonical edges, not raw representations.'}, 'measure_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Named measure described in interpretation; never generic illicit value.'}, 'count': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Pattern-specific edge/node count described in interpretation.'}, 'interpretation': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Bounded observation and what it does not establish.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['P01', 'Distinct external source fan-in', 'E01;E02;E06;E13;E14;E19', 30500, 3, 'P/Q/R contribute six transfers; three distinct immediate sources, no common-controller assertion', 'N01'], ['P02', 'External outflow from entity accounts', 'E03;E05;E07;E09;E12;E15;E17;E20;E22;E24', 34000, 10, 'Ten boundary exits to five distinct immediate recipients C,D,E,P,F; count field is transfer count, not recipient count', 'N01;N02'], ['P03', 'Time-respecting A1-E-F-A1 cycle', 'E09;E10;E11', 1000, 3, 'Minimum-edge capacity USD1000; attributable same-funds circulation range USD0–1000, not proven recycling', 'N01;N04'], ['P04', 'Own-account movements', 'E04;E16', 4500, 2, 'Two canonical transfers; collapse at entity boundary, retain account detail', 'N01;N02'], ['P05', 'Explicit linked returns', 'E08;E21', 2000, 2, 'Two posted returns reduce only their linked originals; other inbound cycle edges are not inferred refunds', 'N01;N03'], ['P06', 'All canonical edge-leg value', 'E01–E24', 74500, 24, 'Gross value across all observed legs; includes repetition, own transfers and onward extracts; not unique source capital', 'N01;N04']], 'primary_key': ['pattern_id'], 'grain': 'One defined graph pattern with an explicitly named amount and count.', 'report_section': 5, 'formats': {'measure_usd': '$#,##0.00', 'count': '#,##0'}}, {'name': 'AllocationBounds', 'columns': ['allocation_id', 'target_edge', 'source_group', 'available_usd', 'other_available_usd', 'debit_usd', 'lower_usd', 'upper_usd', 'basis', 'evidence_ids'], 'column_contracts': {'allocation_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable source-to-target attribution question.'}, 'target_edge': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Debit edge whose funding is being bounded.'}, 'source_group': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Eligible source class at the instant before the debit.'}, 'available_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Source amount available under the fixture before E03.'}, 'other_available_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'All other eligible opening/inflow balances before E03.'}, 'debit_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Target debit value.'}, 'lower_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'max(0,debit-other available), subject to feasible total balance.'}, 'upper_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'min(source available,debit), not a chosen estimate.'}, 'basis': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Model assumptions and stronger claim prohibited.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['AL01', 'E03', 'P receipt E01', 10000, 9000, 12000, 3000, 10000, 'Complete pre-E03 balance; fungible funding, no priority rule; range not point estimate', 'N01;N02;N06'], ['AL02', 'E03', 'Q receipt E02', 8000, 11000, 12000, 1000, 8000, 'Marginal bounds cannot all be combined arbitrarily; joint allocations must sum 12000', 'N01;N02;N06'], ['AL03', 'E03', 'Opening balance A1', 1000, 18000, 12000, 0, 1000, 'Opening origin unknown; do not attribute it to P or Q', 'N01;N02;N06'], ['AL04', 'E03', 'Combined P+Q receipts', 18000, 1000, 12000, 11000, 12000, 'Combined receipt lower bound differs from sum of individual minima', 'N01;N02;N06']], 'primary_key': ['allocation_id'], 'grain': 'One marginal or grouped attribution bound under explicitly stated balance constraints.', 'report_section': 5, 'formats': {'available_usd': '$#,##0.00', 'other_available_usd': '$#,##0.00', 'debit_usd': '$#,##0.00', 'lower_usd': '$#,##0.00', 'upper_usd': '$#,##0.00'}, 'foreign_keys': [{'columns': ['target_edge'], 'table': 'EconomicEdges', 'references': ['edge_id']}]}, {'name': 'AttributionScenarios', 'columns': ['scenario_id', 'method', 'p_usd', 'q_usd', 'opening_usd', 'total_usd', 'status', 'evidence_ids'], 'column_contracts': {'scenario_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable illustrative allocation scenario.'}, 'method': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicit assumed allocation convention, not observed tracing.'}, 'p_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Assigned P funding to E03 under this convention.'}, 'q_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Assigned Q funding to E03 under this convention.'}, 'opening_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Assigned opening balance to E03.'}, 'total_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Sum assigned to E03; exactly12000 at displayed cent precision.'}, 'status': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Epistemic status.', 'enum': ['ILLUSTRATIVE_ONLY']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['AS01', 'Opening-first then FIFO receipts', 10000, 1000, 1000, 12000, 'ILLUSTRATIVE_ONLY', 'N01;N02;N06'], ['AS02', 'Proportional available balance; cent residual to Q', 6315.79, 5052.63, 631.58, 12000, 'ILLUSTRATIVE_ONLY', 'N01;N02;N06'], ['AS03', 'Minimum P feasible allocation', 3000, 8000, 1000, 12000, 'ILLUSTRATIVE_ONLY', 'N01;N02;N06'], ['AS04', 'Maximum P feasible allocation', 10000, 2000, 0, 12000, 'ILLUSTRATIVE_ONLY', 'N01;N02;N06']], 'primary_key': ['scenario_id'], 'grain': 'One feasible assumed allocation vector; alternatives do not describe simultaneous facts.', 'report_section': 5, 'formats': {'p_usd': '$#,##0.00', 'q_usd': '$#,##0.00', 'opening_usd': '$#,##0.00', 'total_usd': '$#,##0.00'}}, {'name': 'DecisionRecord', 'columns': ['decision_id', 'question', 'status', 'reason', 'evidence_ids'], 'column_contracts': {'decision_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable decision gate.'}, 'question': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact proposition requiring a conclusion.'}, 'status': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Bounded result.', 'enum': ['SUPPORTED', 'CONTRADICTED', 'UNRESOLVED', 'PROHIBITED_INFERENCE', 'NOT_RECORDED']}, 'reason': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Why the result follows from visibility and method.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['D01', 'A1/A2 belong to same entity', 'SUPPORTED', 'N02 verifies this grouping only; no extension to other nodes', 'N02'], ['D02', 'P funded all E03', 'CONTRADICTED', 'Under GP-1, P can fund at most USD10000 of E03 USD12000; exact contribution remains unresolved within USD3000–10000', 'N01;N02;N06'], ['D03', 'A1-E-F-A1 proves illicit cycling', 'PROHIBITED_INFERENCE', 'Topology and capacity do not prove same funds, purpose or knowledge', 'N01;N04'], ['D04', 'USD74500 is unique suspicious capital', 'PROHIBITED_INFERENCE', 'It is gross value of repeated observed legs with different perimeter meanings', 'N01;N04'], ['D05', 'Human disposition', 'NOT_RECORDED', 'No actual authorized decision supplied', 'N06']], 'primary_key': ['decision_id'], 'grain': 'One claim boundary or human gate.', 'report_section': 5, 'formats': {}}, {'name': 'ProcessQA', 'columns': ['check_id', 'check', 'expected', 'actual', 'result', 'evidence_ids'], 'column_contracts': {'check_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable quality check.'}, 'check': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Reperformable rule.'}, 'expected': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Expected fixture result.'}, 'actual': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Observed fixture result or explicit unknown.'}, 'result': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Result of analytical fixture check.', 'enum': ['PASS', 'NOT RECORDED']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['Q01', 'Raw normalization', '28 raw to 24 edges', '24', 'PASS', 'N01;N05'], ['Q02', 'Nodes and unique keys', '9 nodes;24 unique edges', '9 / 24', 'PASS', 'N01;N02'], ['Q03', 'Gross edge value', 'USD74500', 'USD74500', 'PASS', 'N01'], ['Q04', 'Entity external boundary', 'USD34000 in and USD34000 out', 'USD34000 / USD34000', 'PASS', 'N01;N02'], ['Q05', 'Complete-account balances', 'A1 USD500; A2 USD1000', 'USD500 / USD1000', 'PASS', 'N01;N02'], ['Q06', 'P funding bound', 'USD3000–10000', 'USD3000–10000', 'PASS', 'N01;N02;N06'], ['Q07', 'Cycle attribution bound', 'USD0–1000, subject to supplied visibility', 'USD0–1000', 'PASS', 'N01;N04'], ['Q08', 'Scenario allocations', 'Every row sums USD12000', 'Four rows tie', 'PASS', 'N01;N02;N06'], ['Q09', 'Unknown counterpart balances', 'No balance equations asserted for P/Q/R/C/D/E/F', 'Unassessed', 'PASS', 'N01;N04'], ['Q10', 'Human decision', 'Not supplied', 'NOT_RECORDED', 'NOT RECORDED', 'N06']], 'primary_key': ['check_id'], 'grain': 'One analytical check, distinct from legal or operational validation.', 'report_section': 5, 'formats': {}}], 'findings': [{'id': 'NET-F01', 'title': 'Graph topology supports a cycle, with uncertain source allocation', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['N01', 'N04'], 'detail': 'E09/E10/E11 form a time-respecting A1-E-F-A1 cycle. Its minimum-edge capacity is USD1000, while attribution of the same funds may range from zero to USD1000.', 'recommendation': 'Retain the cycle as a bounded pattern; request source/purpose evidence only if it affects a live decision.'}, {'id': 'NET-F02', 'title': 'Gross leg value materially exceeds entity boundary flow', 'severity': 'LOW', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['N01', 'N02', 'N04'], 'detail': 'All 24 canonical legs sum USD74500; Entity-A external inflow and outflow are each USD34000. Those measures answer different questions and cannot be labeled unique capital.', 'recommendation': 'Label every measure by perimeter, transfer grain and return treatment.'}, {'id': 'NET-F03', 'title': 'P-to-E03 source attribution cannot be a single observed number', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Inferred', 'evidence_ids': ['N01', 'N02', 'N06'], 'detail': 'Immediately before E03, A1 contains opening 1000, P10000 and Q8000. P funding of the 12000 debit is bounded by 3000–10000 under fungible balance constraints.', 'recommendation': 'Use bounds as the conclusion and retain FIFO/proportional values only as illustrative sensitivities.'}], 'evidence': [{'id': 'N01', 'title': 'Fictional canonical transfer ledger', 'locator': '10-worked-example.md, Raw edges E01–E24', 'claim_class': 'Observed'}, {'id': 'N02', 'title': 'Fictional account identity and balances', 'locator': '10-worked-example.md, A1/A2 ownership and balances', 'claim_class': 'Observed'}, {'id': 'N03', 'title': 'Fictional return references', 'locator': '10-worked-example.md, E08→E03 and E21→E15', 'claim_class': 'Observed'}, {'id': 'N04', 'title': 'Fictional onward transfer extracts', 'locator': '10-worked-example.md, E10 and E18', 'claim_class': 'Observed'}, {'id': 'N05', 'title': 'Fictional raw intake manifest', 'locator': '10-worked-example.md, 28 raw representations', 'claim_class': 'Observed'}, {'id': 'N06', 'title': 'Illustrative graph method charter', 'locator': '10-worked-example.md, Fixture GP-1; source allocation bounds', 'claim_class': 'Observed'}, {'id': 'N07', 'title': 'Customer purpose statement', 'locator': '10-worked-example.md, Statement G-X01', 'claim_class': 'Reported'}, {'id': 'N08', 'title': 'Fictional period and temporal order', 'locator': '10-worked-example.md, Hour-index E01 through E24', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Canonical transfers', 'value': 24, 'method': '28 raw representations minus duplicateE01, instructionE03, pending250 and own mirrorE04', 'format': '#,##0'}, {'label': 'All observed edge-leg value USD', 'value': 74500, 'method': 'Sum24 canonical amounts; repeated flow and own transfers retained; not unique capital', 'format': '$#,##0.00'}, {'label': 'Entity external inflow USD', 'value': 34000, 'method': 'Edges into A1/A2 from outside their verified entity, including returns and cycle inbound', 'format': '$#,##0.00'}, {'label': 'Entity external outflow USD', 'value': 34000, 'method': 'Edges out of A1/A2 to outside their verified entity; own transfers excluded', 'format': '$#,##0.00'}, {'label': 'P funding lower bound USD', 'value': 3000, 'method': 'max(0,E03 12000 minus other eligible9000)', 'format': '$#,##0.00'}, {'label': 'P funding upper bound USD', 'value': 10000, 'method': 'min(P eligible10000,E03 12000)', 'format': '$#,##0.00'}], 'limitations': ['All graph records and grouping evidence are fictional.', 'Only A1/A2 have complete balance coverage; external-node source attribution cannot be inferred from partial extracts.', 'A cycle does not prove same-funds circulation, common control, knowledge or illicit purpose.', 'Source allocation conventions are illustrative assumptions; marginal bounds are not freely combinable.', 'No authorized human disposition or external inquiry has occurred.'], 'conclusion': 'The 24-transfer graph reconciles Entity-A to USD1500 closing balance. It supports a time-respecting cycle and concentrated flows, while P funding of E03 remains bounded at USD3000–10000 and same-funds cycle attribution at USD0–1000.', 'report_narrative': [['The 24-transfer graph reconciles Entity-A to USD1500 closing balance. It supports a time-respecting cycle and concentrated flows, while P funding of E03 remains bounded at USD3000–10000 and same-funds cycle attribution at USD0–1000.'], ['Fictional nine-node graph with 24 ordered posted transfers, complete A1/A2 ledgers, partial counterparty visibility and USD native units. No external investigation or identity discovery is performed.', 'Twenty-eight raw representations reduce to 24 canonical transfers. One duplicate, one instruction, one pending item and one own-transfer mirror are excluded as independent economic edges.'], ['NET-F01: E09/E10/E11 form a time-respecting A1-E-F-A1 cycle. Its minimum-edge capacity is USD1000, while attribution of the same funds may range from zero to USD1000.', 'NET-F02: All 24 canonical legs sum USD74500; Entity-A external inflow and outflow are each USD34000. Those measures answer different questions and cannot be labeled unique capital.', 'NET-F03: Immediately before E03, A1 contains opening 1000, P10000 and Q8000. P funding of the 12000 debit is bounded by 3000–10000 under fungible balance constraints.'], ['Nine nodes preserve A1/A2 as separate accounts within verified Entity-A. Other entity labels are recorded counterparties, without a beneficial ownership assertion. All 24 edges retain temporal order, positive native amount, return linkage and own-transfer flag.'], ['A1 reconciles 1000+34500-35000=500; A2 reconciles 500+4000-3500=1000. Consolidated external inflow/outflow are both 34000; own transfers 4500 cancel. Gross edge-leg value 74500 is a different graph-wide measure.', 'P/Q/R provide six receipts totaling 30500. Five distinct external recipients receive ten Entity-A boundary debits totaling 34000. Explicit returns E08/E21 total 2000; E11/E23 are not inferred refunds.', 'Before E03, available balance is 19000. P bound is 3000–10000, Q1000–8000, opening 0–1000 and combinedP+Q11000–12000. The four feasible allocation scenarios each sum 12000; they are alternatives, not observed source tracing. The A1-E-F-A1 cycle capacity is 1000, with same-funds attribution 0–1000 under incomplete counterparty visibility.'], ['N01/N02 establish supplied transfer and account grouping facts. N03 supplies explicit return references. N04 supplies only the stated onward extracts. N07 is a customer purpose statement and remains Reported. No source establishes illicit purpose.'], ['If attribution affects a live decision, request complete relevant counterparty balance coverage, explicit remittance/settlement linkage and purpose documents. Keep the request proportionate to the disputed proposition; do not expand it into unrestricted identity discovery.'], ['All graph records and grouping evidence are fictional.', 'Only A1/A2 have complete balance coverage; external-node source attribution cannot be inferred from partial extracts.', 'A cycle does not prove same-funds circulation, common control, knowledge or illicit purpose.', 'Source allocation conventions are illustrative assumptions; marginal bounds are not freely combinable.', 'No authorized human disposition or external inquiry has occurred.', 'Fixture checks pass within their stated scope; actual human disposition remains NOT_RECORDED.']], 'suite_id': 'network-flow-review', 'version': '1.2.0', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'NET-F01', 'proposal': 'Retain the cycle as a bounded pattern; request source/purpose evidence only if it affects a live decision.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'NET-F02', 'proposal': 'Label every measure by perimeter, transfer grain and return treatment.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'NET-F03', 'proposal': 'Use bounds as the conclusion and retain FIFO/proportional values only as illustrative sensitivities.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
    def valid_format(value):
        return string(value) and all(len(m)<=15 for m in re.findall(r'\.([0#]+)',value))
    def scalar_matches(value,expected):
        return isinstance(value,str) if expected=='text' else type(value) is bool if expected=='boolean' else type(value) is int if expected=='integer' else type(value) in (int,float)
    def key_value(value):
        # Python aliases True with 1; record joins must retain scalar identity.
        return ('number',value) if type(value) in (int,float) else (type(value).__name__,value)
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
    if not 2 <= len(data['domain_tables']) <= 12:
        errors.append('between two and twelve domain tables required')
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
        if not isinstance(formats,dict) or any(k not in columns or not valid_format(v) for k,v in formats.items()):
            errors.append(label+' formats must name existing columns and use at most 15 decimal places')
        placement=table.get('report_section',4 if index==0 else 5)
        if type(placement) is not int or placement not in (4,5):
            errors.append(label+' report_section must be 4 or 5')
        if 'grain' in table and not string(table['grain']):errors.append(label+' grain must be nonempty text')
        contracts=table.get('column_contracts')
        if 'column_contracts' in table and contracts is None:errors.append(label+' column_contracts must be an object')
        if contracts is not None:
            if not isinstance(contracts,dict) or set(contracts)!=set(columns):
                errors.append(label+' column_contracts must define every column exactly');continue
            for column,spec in contracts.items():
                field=f'{name}.{column}'
                if not isinstance(spec,dict) or spec.get('type') not in ('text','integer','number','boolean') or type(spec.get('nullable')) is not bool or not string(spec.get('unit')) or not string(spec.get('description')):
                    errors.append('invalid field contract '+field);continue
                enum=spec.get('enum')
                if 'enum' in spec and (not isinstance(enum,list) or not enum or any(isinstance(v,(dict,list)) or v is None for v in enum)):
                    errors.append('invalid field enum '+field);continue
                if enum is not None and (any(not scalar_matches(v,spec['type']) for v in enum) or len(set(enum))!=len(enum)):
                    errors.append('enum must contain distinct values of the declared type in '+field)
                for bound in ('minimum','maximum'):
                    if bound in spec and (spec['type'] not in ('number','integer') or type(spec[bound]) not in (int,float) or type(spec[bound]) is float and not math.isfinite(spec[bound])):
                        errors.append('invalid numeric bound '+field)
                if type(spec.get('minimum')) in (int,float) and type(spec.get('maximum')) in (int,float) and spec['minimum']>spec['maximum']:
                    errors.append('minimum exceeds maximum in '+field)
                for row_number,row in enumerate(rows,1):
                    if not isinstance(row,list) or len(row)!=len(columns):continue
                    value=row[columns.index(column)]
                    if value is None:
                        if not spec['nullable']:errors.append(f'null prohibited in {field}, row {row_number}')
                        continue
                    expected=spec['type']
                    valid=scalar_matches(value,expected)
                    if not valid:
                        errors.append(f'wrong {expected} type in {field}, row {row_number}');continue
                    if enum is not None and value not in enum:
                        errors.append(f'value outside enum in {field}, row {row_number}')
                    if type(value) in (int,float):
                        for bound,operator in [('minimum',lambda a,b:a<b),('maximum',lambda a,b:a>b)]:
                            if type(spec.get(bound)) in (int,float) and operator(value,spec[bound]):errors.append(f'value outside {bound} in {field}, row {row_number}')
        key=table.get('primary_key')
        if contracts is not None and key is None:errors.append(label+' typed table requires primary_key')
        if key is not None:
            if not isinstance(key,list) or not key or any(not isinstance(c,str) or c not in columns for c in key) or len(set(key))!=len(key):
                errors.append(label+' invalid primary_key')
            else:
                seen=set()
                for row_number,row in enumerate(rows,1):
                    if not isinstance(row,list) or len(row)!=len(columns) or any(isinstance(v,(dict,list)) for v in row):continue
                    values=tuple(row[columns.index(c)] for c in key)
                    if any(v is None or isinstance(v,str) and not v.strip() for v in values):errors.append(f'empty primary key in {name}, row {row_number}')
                    identity=tuple(key_value(v) for v in values)
                    if identity in seen:errors.append(f'duplicate primary key in {name}, row {row_number}')
                    seen.add(identity)
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
    tables={t['name']:t for t in data['domain_tables'] if isinstance(t,dict) and isinstance(t.get('name'),str)}
    for source in tables.values():
        columns,rows=source.get('columns'),source.get('rows')
        if not isinstance(columns,list) or not isinstance(rows,list):continue
        for row_number,row in enumerate(rows,1):
            if not isinstance(row,list) or len(row)!=len(columns):continue
            for column,value in zip(columns,row):
                if not isinstance(column,str) or value is None:continue
                if column=='evidence_ids' or column.endswith('_evidence_ids') or column=='evidence_id' or column.endswith('_evidence_id'):
                    refs=[v.strip() for v in value.split(';')] if isinstance(value,str) else []
                    if not refs or any(ref not in evidence_ids for ref in refs):errors.append(f'unresolved domain evidence key in {source["name"]}, row {row_number}')
        joins=source.get('foreign_keys',[])
        if not isinstance(joins,list):errors.append('foreign_keys must be a list in '+source['name']);continue
        for join in joins:
            if not isinstance(join,dict):errors.append('invalid foreign key in '+source['name']);continue
            left,right=join.get('columns'),join.get('references')
            target=tables.get(join.get('table')) if isinstance(join.get('table'),str) else None
            if not isinstance(left,list) or not left or not isinstance(right,list) or len(left)!=len(right) or any(not isinstance(c,str) or c not in columns for c in left) or target is None or not isinstance(target.get('columns'),list) or any(not isinstance(c,str) or c not in target['columns'] for c in right):
                errors.append('invalid foreign key in '+source['name']);continue
            target_rows=target.get('rows',[])
            keys=[tuple(key_value(row[target['columns'].index(c)]) for c in right) for row in target_rows if isinstance(row,list) and len(row)==len(target['columns']) and all(not isinstance(v,(dict,list)) for v in row)] if isinstance(target_rows,list) else []
            if len(keys)!=len(set(keys)):errors.append('foreign key target is not unique in '+source['name']);continue
            for row_number,row in enumerate(rows,1):
                if not isinstance(row,list) or len(row)!=len(columns) or any(isinstance(v,(dict,list)) for v in row):continue
                values=tuple(row[columns.index(c)] for c in left)
                if all(v is None for v in values):continue
                if any(v is None for v in values) or tuple(key_value(v) for v in values) not in keys:errors.append(f'unresolved domain foreign key in {source["name"]}, row {row_number}')
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
        if 'format' in row and not valid_format(row['format']):errors.append('invalid metric format; at most 15 decimal places')
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
            if re.search(r'[\ud800-\udfff\ufffe\uffff]',value):errors.append('unsupported XML Unicode code point')
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
summary_rows += [['conclusion', DATA['conclusion'], 'Case-specific conclusion; human disposition remains separate']]
summary_rows += [[f'method_{i:02}', value, 'Applied method'] for i,value in enumerate(DATA['methods'],1)]
summary_rows += [[f'report_section_{section:02}_paragraph_{paragraph:02}', value, DATA['report_sections'][section-1]]
                 for section,paragraphs in enumerate(DATA['report_narrative'],1)
                 for paragraph,value in enumerate(paragraphs,1)]
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
    for column,spec in t.get('column_contracts',{}).items():
        index=t['columns'].index(column)+1
        contract=f"{spec['description']} Type: {spec['type']}. Unit: {spec['unit']}. Nullable: {spec['nullable']}."
        if column in t.get('primary_key',[]):contract+=' Part of the primary key.'
        if 'enum' in spec:contract+=' Allowed values: '+', '.join(map(str,spec['enum']))+'.'
        ws.cell(1,index).comment=Comment(contract,'Toolkit')
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
