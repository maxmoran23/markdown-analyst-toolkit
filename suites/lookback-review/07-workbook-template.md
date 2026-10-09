# Historical Monitoring Lookback and Remediation Review — fixed workbook template

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
| PeriodReconciliation | `period`, `expected_units`, `retrieved_rows`, `duplicate_rows`, `retrieved_units`, `missing_units`, `known_amount_usd`, `coverage_state`, `evidence_ids` |
| CanonicalUnits | `unit_id`, `period`, `source_id`, `amount_usd`, `original_state`, `defect_affected`, `review_state`, `new_information`, `priority`, `evidence_ids` |
| RetrievalLedger | `raw_id`, `unit_id`, `source_period`, `classification`, `canonical_id`, `raw_amount_usd`, `evidence_ids` |
| ReviewActions | `action_id`, `unit_id`, `review_state`, `action_state`, `observed_basis`, `required_next_step`, `comparison_id`, `human_disposition`, `evidence_ids` |
| ExpansionDecisions | `expansion_id`, `trigger`, `proposed_scope`, `inclusion_rule`, `stopping_condition`, `decision_state`, `evidence_ids` |
| EvidenceProvenance | `source_id`, `source_kind`, `as_of`, `availability`, `unit_count`, `grain`, `limitation`, `evidence_ids` |
| ProcessQA | `check_id`, `check_scope`, `expected`, `actual`, `status`, `reviewer`, `evidence_ids` |
| CompletionGates | `gate_id`, `gate`, `numerator`, `denominator`, `state`, `residual`, `permitted_statement`, `evidence_ids` |
| ComparisonPackets | `comparison_id`, `unit_id`, `historical_cutoff`, `historical_source`, `historical_fact_ids`, `historical_facts`, `historical_rationale`, `recovered_date`, `recovered_source`, `current_fact_ids`, `current_observation`, `source_path`, `material_delta`, `expected_route`, `evidence_ids` |
| DefectChronology | `chronology_id`, `event_date`, `source_locator`, `mapping_version`, `record_kind`, `observed_fact`, `boundary_limit`, `evidence_ids` |

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

DATA = {'slug': 'lookback-review', 'title': 'Historical Monitoring Lookback and Remediation Review', 'summary': 'Define and reconcile a historical monitoring review from defect scope through retrieval, deduplication, re-review, expansion and evidence-preserving completion gates.', 'audience': 'Monitoring analysts, independent challenge reviewers and accountable human decision makers', 'decision': 'Which historical units remain exposed or unresolved, and what evidence is necessary before a human can accept the lookback scope and completion?', 'palette': 'indigo', 'as_of': '2026-10-09', 'scope': 'Complete fictional inputs printed in file 10 only. Public authorities provide context, not evidence about the fictional subjects or an institution-specific mandate.', 'report_sections': ['Lookback status and completion restrictions', 'Historical scope defect chronology and population', 'Retrieval review and coverage findings', 'Complete historical population and intake registers', 'Review actions expansion and stopping gates', 'Evidence preservation and unresolved periods', 'Proposed remediation and case-review handoffs', 'Limitations quality review and human disposition'], 'domain_tables': [{'name': 'PeriodReconciliation', 'columns': ['period', 'expected_units', 'retrieved_rows', 'duplicate_rows', 'retrieved_units', 'missing_units', 'known_amount_usd', 'coverage_state', 'evidence_ids'], 'column_contracts': {'period': {'type': 'text', 'nullable': False, 'unit': 'month', 'description': 'Calendar month in the frozen January through June scope.'}, 'expected_units': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Independent control-manifest canonical count.'}, 'retrieved_rows': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Received rows in this period before duplicate removal.'}, 'duplicate_rows': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Additional representations of an already received canonical unit.'}, 'retrieved_units': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Distinct in-scope canonical units with some retrieved material.'}, 'missing_units': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Control units absent from retrieval.'}, 'known_amount_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Sum of available canonical amounts only; excludes missing amount.'}, 'coverage_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Whether counts fully reconcile; says nothing about review completeness.', 'enum': ['RECONCILED', 'PARTIAL']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Independent control and retrieval sources.'}}, 'primary_key': ['period'], 'rows': [['2026-01', 5, 6, 1, 5, 0, 17500, 'RECONCILED', 'SYN-201;SYN-202'], ['2026-02', 5, 5, 0, 5, 0, 42500, 'RECONCILED', 'SYN-201;SYN-202'], ['2026-03', 5, 6, 1, 5, 0, 67500, 'RECONCILED', 'SYN-201;SYN-202'], ['2026-04', 5, 5, 0, 5, 0, 92500, 'RECONCILED', 'SYN-201;SYN-202'], ['2026-05', 5, 6, 1, 5, 0, 117500, 'RECONCILED', 'SYN-201;SYN-202'], ['2026-06', 5, 4, 0, 4, 1, 112000, 'PARTIAL', 'SYN-201;SYN-202']], 'formats': {'known_amount_usd': '$#,##0.00'}, 'grain': 'One historical calendar month in the frozen January–June scope, reconciling expected canonical units to received representations.'}, {'name': 'CanonicalUnits', 'columns': ['unit_id', 'period', 'source_id', 'amount_usd', 'original_state', 'defect_affected', 'review_state', 'new_information', 'priority', 'evidence_ids'], 'column_contracts': {'unit_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'One expected historical review unit from the independent manifest.'}, 'period': {'type': 'text', 'nullable': False, 'unit': 'month', 'description': 'Manifest month, not the latest retrieval date.'}, 'source_id': {'type': 'text', 'nullable': True, 'unit': 'identifier', 'description': 'Canonical retrieval row; null for not-retrieved unit L30.'}, 'amount_usd': {'type': 'number', 'nullable': True, 'unit': 'USD', 'description': 'Supplied unit activity amount; absent for L30. Not a loss amount.'}, 'original_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Historical status preserved unchanged.', 'enum': ['CLOSED', 'ESCALATED', 'NOT_GENERATED', 'UNKNOWN']}, 'defect_affected': {'type': 'boolean', 'nullable': True, 'unit': 'flag', 'description': 'Known impact flag; null when the missing record prevents assessment.'}, 'review_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Current lookback review state, separate from historical state.', 'enum': ['REVIEW_COMPLETE_NO_NEW', 'REFERRED_FOR_CASE_REVIEW', 'REREVIEW_REQUIRED', 'PENDING_REVIEW', 'UNABLE_TO_ASSESS', 'NOT_RETRIEVED']}, 'new_information': {'type': 'boolean', 'nullable': True, 'unit': 'flag', 'description': 'Comparison outcome; null when review or evidence is incomplete.'}, 'priority': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Illustrative attention priority; not a legal deadline.', 'enum': ['HIGH', 'MEDIUM']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Exact control and retrieved evidence sources.'}}, 'primary_key': ['unit_id'], 'rows': [['L01', '2026-01', 'RAW-01', 1500, 'CLOSED', True, 'REVIEW_COMPLETE_NO_NEW', False, 'MEDIUM', 'SYN-201;SYN-202;SYN-205'], ['L02', '2026-01', 'RAW-02', 2500, 'ESCALATED', True, 'REVIEW_COMPLETE_NO_NEW', False, 'MEDIUM', 'SYN-201;SYN-202;SYN-205'], ['L03', '2026-01', 'RAW-03', 3500, 'NOT_GENERATED', False, 'REVIEW_COMPLETE_NO_NEW', False, 'MEDIUM', 'SYN-201;SYN-202;SYN-205'], ['L04', '2026-01', 'RAW-04', 4500, 'CLOSED', True, 'REVIEW_COMPLETE_NO_NEW', False, 'MEDIUM', 'SYN-201;SYN-202;SYN-205'], ['L05', '2026-01', 'RAW-05', 5500, 'ESCALATED', True, 'REVIEW_COMPLETE_NO_NEW', False, 'MEDIUM', 'SYN-201;SYN-202;SYN-205'], ['L06', '2026-02', 'RAW-06', 6500, 'NOT_GENERATED', False, 'REVIEW_COMPLETE_NO_NEW', False, 'MEDIUM', 'SYN-201;SYN-202;SYN-205'], ['L07', '2026-02', 'RAW-07', 7500, 'CLOSED', True, 'REFERRED_FOR_CASE_REVIEW', True, 'HIGH', 'SYN-201;SYN-202;SYN-205'], ['L08', '2026-02', 'RAW-08', 8500, 'ESCALATED', True, 'REFERRED_FOR_CASE_REVIEW', True, 'HIGH', 'SYN-201;SYN-202;SYN-205'], ['L09', '2026-02', 'RAW-09', 9500, 'NOT_GENERATED', False, 'REFERRED_FOR_CASE_REVIEW', True, 'HIGH', 'SYN-201;SYN-202;SYN-205'], ['L10', '2026-02', 'RAW-10', 10500, 'CLOSED', True, 'REFERRED_FOR_CASE_REVIEW', True, 'HIGH', 'SYN-201;SYN-202;SYN-205'], ['L11', '2026-03', 'RAW-11', 11500, 'ESCALATED', True, 'REFERRED_FOR_CASE_REVIEW', True, 'HIGH', 'SYN-201;SYN-202;SYN-205'], ['L12', '2026-03', 'RAW-12', 12500, 'NOT_GENERATED', False, 'REFERRED_FOR_CASE_REVIEW', True, 'HIGH', 'SYN-201;SYN-202;SYN-205'], ['L13', '2026-03', 'RAW-13', 13500, 'CLOSED', True, 'REREVIEW_REQUIRED', None, 'HIGH', 'SYN-201;SYN-202'], ['L14', '2026-03', 'RAW-14', 14500, 'ESCALATED', True, 'REREVIEW_REQUIRED', None, 'HIGH', 'SYN-201;SYN-202'], ['L15', '2026-03', 'RAW-15', 15500, 'NOT_GENERATED', False, 'REREVIEW_REQUIRED', None, 'HIGH', 'SYN-201;SYN-202'], ['L16', '2026-04', 'RAW-16', 16500, 'CLOSED', True, 'REREVIEW_REQUIRED', None, 'HIGH', 'SYN-201;SYN-202'], ['L17', '2026-04', 'RAW-17', 17500, 'ESCALATED', True, 'REREVIEW_REQUIRED', None, 'HIGH', 'SYN-201;SYN-202'], ['L18', '2026-04', 'RAW-18', 18500, 'NOT_GENERATED', False, 'REREVIEW_REQUIRED', None, 'HIGH', 'SYN-201;SYN-202'], ['L19', '2026-04', 'RAW-19', 19500, 'CLOSED', True, 'PENDING_REVIEW', None, 'MEDIUM', 'SYN-201;SYN-202'], ['L20', '2026-04', 'RAW-20', 20500, 'ESCALATED', True, 'PENDING_REVIEW', None, 'MEDIUM', 'SYN-201;SYN-202'], ['L21', '2026-05', 'RAW-21', 21500, 'NOT_GENERATED', False, 'PENDING_REVIEW', None, 'MEDIUM', 'SYN-201;SYN-202'], ['L22', '2026-05', 'RAW-22', 22500, 'CLOSED', True, 'PENDING_REVIEW', None, 'MEDIUM', 'SYN-201;SYN-202'], ['L23', '2026-05', 'RAW-23', 23500, 'ESCALATED', True, 'PENDING_REVIEW', None, 'MEDIUM', 'SYN-201;SYN-202'], ['L24', '2026-05', 'RAW-24', 24500, 'NOT_GENERATED', False, 'PENDING_REVIEW', None, 'MEDIUM', 'SYN-201;SYN-202'], ['L25', '2026-05', 'RAW-25', 25500, 'CLOSED', True, 'UNABLE_TO_ASSESS', None, 'HIGH', 'SYN-201;SYN-202'], ['L26', '2026-06', 'RAW-26', 26500, 'ESCALATED', True, 'UNABLE_TO_ASSESS', None, 'HIGH', 'SYN-201;SYN-202'], ['L27', '2026-06', 'RAW-27', 27500, 'NOT_GENERATED', False, 'UNABLE_TO_ASSESS', None, 'HIGH', 'SYN-201;SYN-202'], ['L28', '2026-06', 'RAW-28', 28500, 'CLOSED', True, 'UNABLE_TO_ASSESS', None, 'HIGH', 'SYN-201;SYN-202'], ['L29', '2026-06', 'RAW-29', 29500, 'ESCALATED', True, 'UNABLE_TO_ASSESS', None, 'HIGH', 'SYN-201;SYN-202'], ['L30', '2026-06', None, None, 'UNKNOWN', None, 'NOT_RETRIEVED', None, 'HIGH', 'SYN-201']], 'formats': {'amount_usd': '$#,##0.00'}, 'foreign_keys': [{'columns': ['period'], 'table': 'PeriodReconciliation', 'references': ['period']}], 'grain': 'One independently expected historical review unit, identified by unit_id, including an unretrieved placeholder when source evidence is absent.'}, {'name': 'RetrievalLedger', 'columns': ['raw_id', 'unit_id', 'source_period', 'classification', 'canonical_id', 'raw_amount_usd', 'evidence_ids'], 'column_contracts': {'raw_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique received representation identifier.'}, 'unit_id': {'type': 'text', 'nullable': True, 'unit': 'identifier', 'description': 'Matched in-scope canonical unit; null for out-of-scope July records.'}, 'source_period': {'type': 'text', 'nullable': False, 'unit': 'month', 'description': 'Historical month associated with the received record.'}, 'classification': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exactly one intake accounting bucket.', 'enum': ['CANONICAL', 'DUPLICATE', 'OUT_OF_SCOPE']}, 'canonical_id': {'type': 'text', 'nullable': True, 'unit': 'identifier', 'description': 'Retained canonical unit for matching rows; null when out of scope.'}, 'raw_amount_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Amount on this raw representation before deduplication; do not aggregate as canonical activity.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Retrieval input source.'}}, 'primary_key': ['raw_id'], 'rows': [['RAW-01', 'L01', '2026-01', 'CANONICAL', 'L01', 1500, 'SYN-202'], ['RAW-02', 'L02', '2026-01', 'CANONICAL', 'L02', 2500, 'SYN-202'], ['RAW-03', 'L03', '2026-01', 'CANONICAL', 'L03', 3500, 'SYN-202'], ['RAW-04', 'L04', '2026-01', 'CANONICAL', 'L04', 4500, 'SYN-202'], ['RAW-05', 'L05', '2026-01', 'CANONICAL', 'L05', 5500, 'SYN-202'], ['RAW-06', 'L06', '2026-02', 'CANONICAL', 'L06', 6500, 'SYN-202'], ['RAW-07', 'L07', '2026-02', 'CANONICAL', 'L07', 7500, 'SYN-202'], ['RAW-08', 'L08', '2026-02', 'CANONICAL', 'L08', 8500, 'SYN-202'], ['RAW-09', 'L09', '2026-02', 'CANONICAL', 'L09', 9500, 'SYN-202'], ['RAW-10', 'L10', '2026-02', 'CANONICAL', 'L10', 10500, 'SYN-202'], ['RAW-11', 'L11', '2026-03', 'CANONICAL', 'L11', 11500, 'SYN-202'], ['RAW-12', 'L12', '2026-03', 'CANONICAL', 'L12', 12500, 'SYN-202'], ['RAW-13', 'L13', '2026-03', 'CANONICAL', 'L13', 13500, 'SYN-202'], ['RAW-14', 'L14', '2026-03', 'CANONICAL', 'L14', 14500, 'SYN-202'], ['RAW-15', 'L15', '2026-03', 'CANONICAL', 'L15', 15500, 'SYN-202'], ['RAW-16', 'L16', '2026-04', 'CANONICAL', 'L16', 16500, 'SYN-202'], ['RAW-17', 'L17', '2026-04', 'CANONICAL', 'L17', 17500, 'SYN-202'], ['RAW-18', 'L18', '2026-04', 'CANONICAL', 'L18', 18500, 'SYN-202'], ['RAW-19', 'L19', '2026-04', 'CANONICAL', 'L19', 19500, 'SYN-202'], ['RAW-20', 'L20', '2026-04', 'CANONICAL', 'L20', 20500, 'SYN-202'], ['RAW-21', 'L21', '2026-05', 'CANONICAL', 'L21', 21500, 'SYN-202'], ['RAW-22', 'L22', '2026-05', 'CANONICAL', 'L22', 22500, 'SYN-202'], ['RAW-23', 'L23', '2026-05', 'CANONICAL', 'L23', 23500, 'SYN-202'], ['RAW-24', 'L24', '2026-05', 'CANONICAL', 'L24', 24500, 'SYN-202'], ['RAW-25', 'L25', '2026-05', 'CANONICAL', 'L25', 25500, 'SYN-202'], ['RAW-26', 'L26', '2026-06', 'CANONICAL', 'L26', 26500, 'SYN-202'], ['RAW-27', 'L27', '2026-06', 'CANONICAL', 'L27', 27500, 'SYN-202'], ['RAW-28', 'L28', '2026-06', 'CANONICAL', 'L28', 28500, 'SYN-202'], ['RAW-29', 'L29', '2026-06', 'CANONICAL', 'L29', 29500, 'SYN-202'], ['RAW-D1', 'L02', '2026-01', 'DUPLICATE', 'L02', 2500, 'SYN-202'], ['RAW-D2', 'L12', '2026-03', 'DUPLICATE', 'L12', 12500, 'SYN-202'], ['RAW-D3', 'L22', '2026-05', 'DUPLICATE', 'L22', 22500, 'SYN-202'], ['RAW-X31', None, '2026-07', 'OUT_OF_SCOPE', None, 31500, 'SYN-202'], ['RAW-X32', None, '2026-07', 'OUT_OF_SCOPE', None, 32500, 'SYN-202']], 'formats': {'raw_amount_usd': '$#,##0.00'}, 'foreign_keys': [{'columns': ['unit_id'], 'table': 'CanonicalUnits', 'references': ['unit_id']}, {'columns': ['canonical_id'], 'table': 'CanonicalUnits', 'references': ['unit_id']}], 'grain': 'One received source representation, identified by raw_id, before canonical deduplication or scope exclusion.'}, {'name': 'ReviewActions', 'columns': ['action_id', 'unit_id', 'review_state', 'action_state', 'observed_basis', 'required_next_step', 'comparison_id', 'human_disposition', 'evidence_ids'], 'column_contracts': {'action_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique historical-unit action identifier.'}, 'unit_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Canonical unit requiring or receiving review.'}, 'review_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'State replicated from CanonicalUnits to permit reconciliation.', 'enum': ['REVIEW_COMPLETE_NO_NEW', 'REFERRED_FOR_CASE_REVIEW', 'REREVIEW_REQUIRED', 'PENDING_REVIEW', 'UNABLE_TO_ASSESS', 'NOT_RETRIEVED']}, 'action_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Operational work position; a handoff is not closed.', 'enum': ['DESK_REVIEW_COMPLETE', 'HANDOFF_OPEN', 'REVIEW_OPEN', 'EVIDENCE_BLOCKED', 'RETRIEVAL_BLOCKED']}, 'observed_basis': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Fictional basis supporting this work state.'}, 'required_next_step': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific evidence-preserving work proposal.'}, 'comparison_id': {'type': 'text', 'nullable': True, 'unit': 'identifier', 'description': 'Populated comparison packet ID for the twelve desk-complete units; null where no completed packet exists.'}, 'human_disposition': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Actual institutional acceptance is absent.', 'enum': ['NOT_RECORDED']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Review-state source.'}}, 'primary_key': ['action_id'], 'rows': [['LA-L01', 'L01', 'REVIEW_COMPLETE_NO_NEW', 'DESK_REVIEW_COMPLETE', 'Fictional re-review found no new information within supplied scope', 'Preserve comparison and independent QA; no filing judgment inferred', 'COMP-L01', 'NOT_RECORDED', 'SYN-203;SYN-205'], ['LA-L02', 'L02', 'REVIEW_COMPLETE_NO_NEW', 'DESK_REVIEW_COMPLETE', 'Fictional re-review found no new information within supplied scope', 'Preserve comparison and independent QA; no filing judgment inferred', 'COMP-L02', 'NOT_RECORDED', 'SYN-203;SYN-205'], ['LA-L03', 'L03', 'REVIEW_COMPLETE_NO_NEW', 'DESK_REVIEW_COMPLETE', 'Fictional re-review found no new information within supplied scope', 'Preserve comparison and independent QA; no filing judgment inferred', 'COMP-L03', 'NOT_RECORDED', 'SYN-203;SYN-205'], ['LA-L04', 'L04', 'REVIEW_COMPLETE_NO_NEW', 'DESK_REVIEW_COMPLETE', 'Fictional re-review found no new information within supplied scope', 'Preserve comparison and independent QA; no filing judgment inferred', 'COMP-L04', 'NOT_RECORDED', 'SYN-203;SYN-205'], ['LA-L05', 'L05', 'REVIEW_COMPLETE_NO_NEW', 'DESK_REVIEW_COMPLETE', 'Fictional re-review found no new information within supplied scope', 'Preserve comparison and independent QA; no filing judgment inferred', 'COMP-L05', 'NOT_RECORDED', 'SYN-203;SYN-205'], ['LA-L06', 'L06', 'REVIEW_COMPLETE_NO_NEW', 'DESK_REVIEW_COMPLETE', 'Fictional re-review found no new information within supplied scope', 'Preserve comparison and independent QA; no filing judgment inferred', 'COMP-L06', 'NOT_RECORDED', 'SYN-203;SYN-205'], ['LA-L07', 'L07', 'REFERRED_FOR_CASE_REVIEW', 'HANDOFF_OPEN', 'New information exists in comparison packet', 'Obtain authorized case review acknowledgment and decision evidence', 'COMP-L07', 'NOT_RECORDED', 'SYN-203;SYN-205'], ['LA-L08', 'L08', 'REFERRED_FOR_CASE_REVIEW', 'HANDOFF_OPEN', 'New information exists in comparison packet', 'Obtain authorized case review acknowledgment and decision evidence', 'COMP-L08', 'NOT_RECORDED', 'SYN-203;SYN-205'], ['LA-L09', 'L09', 'REFERRED_FOR_CASE_REVIEW', 'HANDOFF_OPEN', 'New information exists in comparison packet', 'Obtain authorized case review acknowledgment and decision evidence', 'COMP-L09', 'NOT_RECORDED', 'SYN-203;SYN-205'], ['LA-L10', 'L10', 'REFERRED_FOR_CASE_REVIEW', 'HANDOFF_OPEN', 'New information exists in comparison packet', 'Obtain authorized case review acknowledgment and decision evidence', 'COMP-L10', 'NOT_RECORDED', 'SYN-203;SYN-205'], ['LA-L11', 'L11', 'REFERRED_FOR_CASE_REVIEW', 'HANDOFF_OPEN', 'New information exists in comparison packet', 'Obtain authorized case review acknowledgment and decision evidence', 'COMP-L11', 'NOT_RECORDED', 'SYN-203;SYN-205'], ['LA-L12', 'L12', 'REFERRED_FOR_CASE_REVIEW', 'HANDOFF_OPEN', 'New information exists in comparison packet', 'Obtain authorized case review acknowledgment and decision evidence', 'COMP-L12', 'NOT_RECORDED', 'SYN-203;SYN-205'], ['LA-L13', 'L13', 'REREVIEW_REQUIRED', 'REVIEW_OPEN', 'Prior reasoning does not address changed defect context', 'Reperform analysis against recovered evidence and preserve original rationale', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L14', 'L14', 'REREVIEW_REQUIRED', 'REVIEW_OPEN', 'Prior reasoning does not address changed defect context', 'Reperform analysis against recovered evidence and preserve original rationale', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L15', 'L15', 'REREVIEW_REQUIRED', 'REVIEW_OPEN', 'Prior reasoning does not address changed defect context', 'Reperform analysis against recovered evidence and preserve original rationale', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L16', 'L16', 'REREVIEW_REQUIRED', 'REVIEW_OPEN', 'Prior reasoning does not address changed defect context', 'Reperform analysis against recovered evidence and preserve original rationale', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L17', 'L17', 'REREVIEW_REQUIRED', 'REVIEW_OPEN', 'Prior reasoning does not address changed defect context', 'Reperform analysis against recovered evidence and preserve original rationale', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L18', 'L18', 'REREVIEW_REQUIRED', 'REVIEW_OPEN', 'Prior reasoning does not address changed defect context', 'Reperform analysis against recovered evidence and preserve original rationale', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L19', 'L19', 'PENDING_REVIEW', 'REVIEW_OPEN', 'No completed desk review record supplied', 'Assign reviewer and preserve priority; completion cannot be inferred', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L20', 'L20', 'PENDING_REVIEW', 'REVIEW_OPEN', 'No completed desk review record supplied', 'Assign reviewer and preserve priority; completion cannot be inferred', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L21', 'L21', 'PENDING_REVIEW', 'REVIEW_OPEN', 'No completed desk review record supplied', 'Assign reviewer and preserve priority; completion cannot be inferred', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L22', 'L22', 'PENDING_REVIEW', 'REVIEW_OPEN', 'No completed desk review record supplied', 'Assign reviewer and preserve priority; completion cannot be inferred', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L23', 'L23', 'PENDING_REVIEW', 'REVIEW_OPEN', 'No completed desk review record supplied', 'Assign reviewer and preserve priority; completion cannot be inferred', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L24', 'L24', 'PENDING_REVIEW', 'REVIEW_OPEN', 'No completed desk review record supplied', 'Assign reviewer and preserve priority; completion cannot be inferred', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L25', 'L25', 'UNABLE_TO_ASSESS', 'EVIDENCE_BLOCKED', 'Retrieved summary lacks essential supporting evidence', 'Recover missing support or record qualified scope limitation', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L26', 'L26', 'UNABLE_TO_ASSESS', 'EVIDENCE_BLOCKED', 'Retrieved summary lacks essential supporting evidence', 'Recover missing support or record qualified scope limitation', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L27', 'L27', 'UNABLE_TO_ASSESS', 'EVIDENCE_BLOCKED', 'Retrieved summary lacks essential supporting evidence', 'Recover missing support or record qualified scope limitation', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L28', 'L28', 'UNABLE_TO_ASSESS', 'EVIDENCE_BLOCKED', 'Retrieved summary lacks essential supporting evidence', 'Recover missing support or record qualified scope limitation', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L29', 'L29', 'UNABLE_TO_ASSESS', 'EVIDENCE_BLOCKED', 'Retrieved summary lacks essential supporting evidence', 'Recover missing support or record qualified scope limitation', None, 'NOT_RECORDED', 'SYN-203'], ['LA-L30', 'L30', 'NOT_RETRIEVED', 'RETRIEVAL_BLOCKED', 'Control manifest names a unit absent from retrieval', 'Recover archive record or retain unreconciled coverage gap', None, 'NOT_RECORDED', 'SYN-203']], 'foreign_keys': [{'columns': ['unit_id'], 'table': 'CanonicalUnits', 'references': ['unit_id']}, {'columns': ['comparison_id'], 'table': 'ComparisonPackets', 'references': ['comparison_id']}], 'grain': 'One current lookback work action for one canonical unit, identified by action_id, with a separate comparison and human-disposition state.'}, {'name': 'ExpansionDecisions', 'columns': ['expansion_id', 'trigger', 'proposed_scope', 'inclusion_rule', 'stopping_condition', 'decision_state', 'evidence_ids'], 'column_contracts': {'expansion_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable scope-change or stopping decision key.'}, 'trigger': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific new evidence or observed condition.'}, 'proposed_scope': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Bounded additional review population or work.'}, 'inclusion_rule': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact predicate for the proposed change.'}, 'stopping_condition': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Evidence needed to stop the associated work.'}, 'decision_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Proposals do not invent actual human acceptance.', 'enum': ['PROPOSED', 'BLOCKED']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Supporting scope or defect evidence.'}}, 'primary_key': ['expansion_id'], 'rows': [['EX-01', 'Initial January through March review cannot exclude later mapping impact', 'Extend analytical fixture through June 30', 'Manifest period 2026-04 through 2026-06', 'Reconcile all fifteen added canonical units and impact evidence', 'PROPOSED', 'SYN-201;SYN-204'], ['EX-02', 'L30 missing despite independent June control count', 'Recover June archive and linkage records', 'Canonical unit L30 plus source representations matching its key', 'L30 recovered or documented unreconciled coverage limitation remains', 'BLOCKED', 'SYN-201;SYN-202'], ['EX-03', 'Six comparison packets identify new information', 'Route L07 through L12 to authorized case review', 'new_information=true', 'Acknowledged referral and later authorized decision evidence', 'PROPOSED', 'SYN-203'], ['EX-04', 'Six prior reviews do not address revised defect context', 'Re-review L13 through L18', 'review_state=REREVIEW_REQUIRED', 'Complete fresh comparison preserving historical record', 'PROPOSED', 'SYN-203'], ['EX-05', 'Five retrieved summaries lack essential support', 'Recover support for L25 through L29', 'review_state=UNABLE_TO_ASSESS', 'Support recovered and reviewed or qualified scope limit retained', 'BLOCKED', 'SYN-203'], ['EX-06', 'July rows are outside current analytical boundary', 'Assess whether defect evidence crosses June 30 before adding July', 'Mapping continuity evidence beyond 2026-06-30', 'Documented boundary evidence; no silent inclusion or dismissal', 'PROPOSED', 'SYN-202;SYN-204']], 'grain': 'One bounded scope-change, recovery or review proposal, identified by expansion_id, with its trigger and stopping condition.'}, {'name': 'EvidenceProvenance', 'columns': ['source_id', 'source_kind', 'as_of', 'availability', 'unit_count', 'grain', 'limitation', 'evidence_ids'], 'column_contracts': {'source_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable source ID resolving to the Evidence register.'}, 'source_kind': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Nature of supplied material.', 'enum': ['SYNTHETIC_INPUT', 'SYNTHETIC_CALCULATION', 'SYNTHETIC_DECISION']}, 'as_of': {'type': 'text', 'nullable': False, 'unit': 'date', 'description': 'Evidence cutoff expressed as ISO date, not a receipt timestamp.'}, 'availability': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Supplied scope status.', 'enum': ['COMPLETE_FIXTURE', 'PARTIAL_FIXTURE']}, 'unit_count': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Count at the explicitly named grain.'}, 'grain': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'The counting unit for this row.'}, 'limitation': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'What this source cannot establish.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'The same source ID, checked against the Evidence register.'}}, 'primary_key': ['source_id'], 'rows': [['SYN-201', 'SYNTHETIC_INPUT', '2026-10-09', 'COMPLETE_FIXTURE', 30, 'expected canonical historical units', 'Manifest counts do not supply absent record content.', 'SYN-201'], ['SYN-202', 'SYNTHETIC_INPUT', '2026-10-09', 'PARTIAL_FIXTURE', 34, 'received representations including duplicates and exclusions', 'One expected canonical unit is missing; retrieved summaries may lack support.', 'SYN-202'], ['SYN-203', 'SYNTHETIC_DECISION', '2026-10-09', 'PARTIAL_FIXTURE', 30, 'review-state assignments', 'Twelve desk comparisons complete; six have no open unit action; actual institutional disposition not supplied.', 'SYN-203'], ['SYN-204', 'SYNTHETIC_INPUT', '2026-10-09', 'PARTIAL_FIXTURE', 7, 'dated mapping-version records', 'July continuity and actual production correction remain unverified.', 'SYN-204'], ['SYN-205', 'SYNTHETIC_INPUT', '2026-10-09', 'COMPLETE_FIXTURE', 12, 'historical/current comparison packets', 'Completed desk comparison is separate from actual case disposition.', 'SYN-205']], 'grain': 'One synthetic source_id with its own declared counting unit and availability limit.'}, {'name': 'ProcessQA', 'columns': ['check_id', 'check_scope', 'expected', 'actual', 'status', 'reviewer', 'evidence_ids'], 'column_contracts': {'check_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable QA check identifier.'}, 'check_scope': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact records or decision being checked.'}, 'expected': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Reference result calculated before inspecting presentation.'}, 'actual': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Observed synthetic result; no operational execution is implied.'}, 'status': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Comparison state.', 'enum': ['PASS', 'FAIL', 'REVIEW_REQUIRED', 'NOT_TESTED']}, 'reviewer': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Fictional review role or NOT_RECORDED; never an actual approval.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Semicolon-delimited source IDs resolving to Evidence.'}}, 'primary_key': ['check_id'], 'rows': [['LB-Q01', 'Raw intake accounting', '34=29 canonical+3 duplicate+2 out-of-scope', '34=29+3+2', 'PASS', 'Fictional checker', 'SYN-202'], ['LB-Q02', 'Expected scope accounting', '30=29 retrieved+1 missing', '30=29+1;L30 absent', 'PASS', 'Fictional checker', 'SYN-201;SYN-202'], ['LB-Q03', 'Full retrieval coverage', 'All 30 expected units retrieved', '29/30 retrieved; June 4/5', 'FAIL', 'Fictional checker', 'SYN-201;SYN-202'], ['LB-Q04', 'Canonical amount conservation', 'Known amounts 449500; missing unit excluded explicitly', '449500 known; L30 amount null', 'PASS', 'Fictional checker', 'SYN-201;SYN-202'], ['LB-Q05', 'Desk review completion', '6 no-new plus 6 referred =12 examined', '12/30 examined;6 handoffs still open', 'PASS', 'Fictional checker', 'SYN-203'], ['LB-Q06', 'Whole-lookback completion', 'No material unresolved review retrieval or handoff', '24 units retain open dependency;6 desk-complete only', 'FAIL', 'Fictional checker', 'SYN-203'], ['LB-Q07', 'No missing-to-negative conversion', 'L30 remains not retrieved and impact unknown', 'L30 source amount impact and new_information remain null', 'PASS', 'Fictional checker', 'SYN-201'], ['LB-Q08', 'Filing or closure decision', 'Separate authorized human process required', 'NOT_RECORDED', 'NOT_TESTED', 'NOT_RECORDED', 'SYN-203']], 'grain': 'One explicitly scoped fixture quality check, identified by check_id, with expected and actual results.'}, {'name': 'CompletionGates', 'columns': ['gate_id', 'gate', 'numerator', 'denominator', 'state', 'residual', 'permitted_statement', 'evidence_ids'], 'column_contracts': {'gate_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique stopping or completion gate.'}, 'gate': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Evidence required for the stated completion claim.'}, 'numerator': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Satisfied units at the stated denominator grain.'}, 'denominator': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Complete in-scope population for this gate.'}, 'state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'SATISFIED_FIXTURE_ONLY does not mean operational signoff.', 'enum': ['SATISFIED_FIXTURE_ONLY', 'FAILED', 'BLOCKED']}, 'residual': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific unresolved gap.'}, 'permitted_statement': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Narrow completion statement supported by the record.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Evidence supporting the gate.'}}, 'primary_key': ['gate_id'], 'rows': [['LB-G01', 'Raw rows assigned an intake bucket', 34, 34, 'SATISFIED_FIXTURE_ONLY', 'None within supplied intake', 'All received rows classified; expected population still missing one', 'SYN-202'], ['LB-G02', 'Expected canonical units retrieved', 29, 30, 'FAILED', 'L30 not retrieved', 'Retrieval coverage 29/30; no complete-coverage claim', 'SYN-201;SYN-202'], ['LB-G03', 'Desk comparison completed', 12, 30, 'FAILED', '18 not desk-complete', '12 comparisons completed, including 6 unresolved referrals', 'SYN-203'], ['LB-G04', 'Desk review with no open unit action', 6, 30, 'FAILED', '24 units retain review evidence retrieval or handoff dependency', '6 units have completed no-new-information comparisons', 'SYN-203'], ['LB-G05', 'Referred units acknowledged and disposed', 0, 6, 'BLOCKED', 'No actual receiving-case decision evidence', 'Six handoffs remain open', 'SYN-203'], ['LB-G06', 'Authorized whole-review acceptance', 0, 1, 'BLOCKED', 'Actual approval and accepted limitations absent', 'Lookback remains incomplete', 'SYN-203;SYN-204']], 'grain': 'One distinct completion claim, identified by gate_id, with its own expressly stated numerator and denominator grain.'}, {'name': 'ComparisonPackets', 'columns': ['comparison_id', 'unit_id', 'historical_cutoff', 'historical_source', 'historical_fact_ids', 'historical_facts', 'historical_rationale', 'recovered_date', 'recovered_source', 'current_fact_ids', 'current_observation', 'source_path', 'material_delta', 'expected_route', 'evidence_ids'], 'column_contracts': {'comparison_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique populated historical/current packet ID.'}, 'unit_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Canonical unit whose desk comparison is documented.'}, 'historical_cutoff': {'type': 'text', 'nullable': False, 'unit': 'date', 'description': 'Date through which the fictional historical packet was available.'}, 'historical_source': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Printed historical source packet locator.'}, 'historical_fact_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Semicolon-delimited material facts available historically.'}, 'historical_facts': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Concrete facts actually present in the original packet.'}, 'historical_rationale': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Original reasoning preserved without retrospective rewriting.'}, 'recovered_date': {'type': 'text', 'nullable': False, 'unit': 'date', 'description': 'Date newly retrieved source material became available.'}, 'recovered_source': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Printed recovered source packet locator.'}, 'current_fact_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Complete current material fact set; additions drive the new-information test.'}, 'current_observation': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Concrete current facts and whether they differ from the historical basis.'}, 'source_path': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Supplied source feed path, not inferred from historical disposition.', 'enum': ['PATH_A', 'PATH_B', 'PATH_C']}, 'material_delta': {'type': 'boolean', 'nullable': False, 'unit': 'flag', 'description': 'True exactly when the current material fact set adds a fact outside the historical set.'}, 'expected_route': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Completed comparison result; referral disposition remains open.', 'enum': ['REVIEW_COMPLETE_NO_NEW', 'REFERRED_FOR_CASE_REVIEW']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Source for the complete packet and fact dictionary.'}}, 'primary_key': ['comparison_id'], 'rows': [['COMP-L01', 'L01', '2026-01-31', 'HIST-L01', 'L01-F1;L01-F2', 'Payroll credits from two identified employers matched the supplied pay records.', 'The historical review already inspected both payer identities and pay records.', '2026-10-02', 'REC-L01', 'L01-F1;L01-F2', 'Both payer identities, amounts and pay-record matches are unchanged; corrected monitoring count adds no unseen fact.', 'PATH_A', False, 'REVIEW_COMPLETE_NO_NEW', 'SYN-205'], ['COMP-L02', 'L02', '2026-01-31', 'HIST-L02', 'L02-F1;L02-F2', 'Four originators and the complete activity were already included in the earlier escalation packet.', 'Historical escalation expressly covered all four identified originators.', '2026-10-02', 'REC-L02', 'L02-F1;L02-F2', 'Recovered source messages match the four identities and activity already escalated; no additional party or transaction is found.', 'PATH_B', False, 'REVIEW_COMPLETE_NO_NEW', 'SYN-205'], ['COMP-L03', 'L03', '2026-01-31', 'HIST-L03', 'L03-F1;L03-F2', 'One documented transfer from the same beneficial owner matched the account ownership evidence.', 'The correctly mapped control path produced no scenario hit and the underlying ownership fact was documented.', '2026-10-02', 'REC-L03', 'L03-F1;L03-F2', 'The source-path replay and ownership documentation are unchanged.', 'PATH_C', False, 'REVIEW_COMPLETE_NO_NEW', 'SYN-205'], ['COMP-L04', 'L04', '2026-01-31', 'HIST-L04', 'L04-F1;L04-F2', 'Three commercial payers matched the supplied invoices and recorded business counterparties.', 'Historical closure relied on inspected invoice and counterparty matches, not the defective aggregate alone.', '2026-10-02', 'REC-L04', 'L04-F1;L04-F2', 'Recovered messages preserve the same three payers and invoice references with no contradiction.', 'PATH_A', False, 'REVIEW_COMPLETE_NO_NEW', 'SYN-205'], ['COMP-L05', 'L05', '2026-01-31', 'HIST-L05', 'L05-F1;L05-F2', 'Five originators and their activity were fully described in the earlier escalation.', 'The historical packet included the source messages and all five counterparties.', '2026-10-02', 'REC-L05', 'L05-F1;L05-F2', 'The replay identifies the same five parties already in that packet; no new transaction or identity is added.', 'PATH_B', False, 'REVIEW_COMPLETE_NO_NEW', 'SYN-205'], ['COMP-L06', 'L06', '2026-02-28', 'HIST-L06', 'L06-F1;L06-F2', 'A single internal operating transfer matched the supplied account mapping.', 'The control path mapped the actual originator and the activity remained outside the scenario concept.', '2026-10-02', 'REC-L06', 'L06-F1;L06-F2', 'The original source and current replay agree on the same internal account and purpose.', 'PATH_C', False, 'REVIEW_COMPLETE_NO_NEW', 'SYN-205'], ['COMP-L07', 'L07', '2026-02-28', 'HIST-L07', 'L07-F1;L07-F2', 'The historical summary described all credits as transfers from the same customer-controlled account.', 'Closure relied on the one-originator summary and did not include underlying payment messages.', '2026-10-02', 'REC-L07', 'L07-F1;L07-F2;L07-F3', 'Recovered messages identify four third-party originator IDs; three are absent from the historical packet and their purpose is unsupported.', 'PATH_A', True, 'REFERRED_FOR_CASE_REVIEW', 'SYN-205'], ['COMP-L08', 'L08', '2026-02-28', 'HIST-L08', 'L08-F1;L08-F2', 'The prior escalation packet identified two originators and stated that it covered the complete relationship.', 'The earlier referral scope was limited to those two identities and their supplied activity.', '2026-10-02', 'REC-L08', 'L08-F1;L08-F2;L08-F3', 'Recovered messages identify seven originators; five additional identities were outside the earlier scope.', 'PATH_B', True, 'REFERRED_FOR_CASE_REVIEW', 'SYN-205'], ['COMP-L09', 'L09', '2026-02-28', 'HIST-L09', 'L09-F1;L09-F2', 'The control-path unit showed one payer and a supplier-payment explanation.', 'No scenario hit was generated; the supplied original packet contained the stated supplier rationale.', '2026-10-02', 'REC-L09', 'L09-F1;L09-F2;L09-F3', 'A newly recovered contract names a different economic supplier than the payment message, creating an identity-purpose inconsistency unrelated to the mapping defect.', 'PATH_C', True, 'REFERRED_FOR_CASE_REVIEW', 'SYN-205'], ['COMP-L10', 'L10', '2026-02-28', 'HIST-L10', 'L10-F1;L10-F2', 'The historical review treated the credits as customer self-funding based on the summary identity.', 'Closure relied on apparent common ownership without the underlying message identities.', '2026-10-02', 'REC-L10', 'L10-F1;L10-F2;L10-F3', 'Five distinct third-party originators appear in recovered messages and the claimed ownership link is not supported.', 'PATH_A', True, 'REFERRED_FOR_CASE_REVIEW', 'SYN-205'], ['COMP-L11', 'L11', '2026-03-31', 'HIST-L11', 'L11-F1;L11-F2', 'The prior escalation described three counterparties and excluded no known message records.', 'Its stated scope and rationale addressed those three named parties only.', '2026-10-02', 'REC-L11', 'L11-F1;L11-F2;L11-F3', 'The corrected message grouping identifies three additional counterparties, including activity outside the original referral narrative.', 'PATH_B', True, 'REFERRED_FOR_CASE_REVIEW', 'SYN-205'], ['COMP-L12', 'L12', '2026-03-31', 'HIST-L12', 'L12-F1;L12-F2', 'The control-path unit had one identified payer and an equipment-sale explanation.', 'The original source did not contradict the stated sale purpose and the monitoring predicate did not hit.', '2026-10-02', 'REC-L12', 'L12-F1;L12-F2;L12-F3', 'A newly recovered invoice describes consulting services instead of equipment, creating a material purpose contradiction independent of mapping.', 'PATH_C', True, 'REFERRED_FOR_CASE_REVIEW', 'SYN-205']], 'foreign_keys': [{'columns': ['unit_id'], 'table': 'CanonicalUnits', 'references': ['unit_id']}], 'grain': 'One completed fictional historical-versus-current desk-comparison packet for one canonical unit, identified by comparison_id.'}, {'name': 'DefectChronology', 'columns': ['chronology_id', 'event_date', 'source_locator', 'mapping_version', 'record_kind', 'observed_fact', 'boundary_limit', 'evidence_ids'], 'column_contracts': {'chronology_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique chronology event ID.'}, 'event_date': {'type': 'text', 'nullable': False, 'unit': 'date', 'description': 'Date of the supplied event or missing historical checkpoint.'}, 'source_locator': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Exact fictional record locator printed in this table.'}, 'mapping_version': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Known mapping version or explicit UNKNOWN.'}, 'record_kind': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Nature of the timing evidence.', 'enum': ['CHANGE_RECORD', 'RUNTIME_SNAPSHOT', 'UNAVAILABLE', 'DEFECT_REPRODUCTION', 'PROPOSED_CORRECTION']}, 'observed_fact': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Concrete fact supplied by the record.'}, 'boundary_limit': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'What the record cannot establish about scope or completion.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Chronology source ID.'}}, 'primary_key': ['chronology_id'], 'rows': [['DC-01', '2025-12-29', 'CR-MAP-04', 'MAP-1', 'CHANGE_RECORD', 'Deployment plan enables PATH_A and PATH_B identity mapping on January01; PATH_C retains correct source-originator mapping.', 'Plan is not proof of runtime before January01.', 'SYN-204'], ['DC-02', '2026-01-01', 'CFG-JAN-01', 'MAP-1', 'RUNTIME_SNAPSHOT', 'PATH_A and PATH_B use customer_id instead of payment_originator_id in the monitoring originator key; PATH_C uses payment_originator_id.', 'The established mechanism can collapse distinct originators on affected paths.', 'SYN-204'], ['DC-03', '2026-03-31', 'CFG-MAR-31', 'MAP-1', 'RUNTIME_SNAPSHOT', 'The same two affected mappings remain active in the archived configuration.', 'Supports the initial January–March discovery scope, not a March end to exposure.', 'SYN-204'], ['DC-04', '2026-06-30', 'CFG-JUN-30', 'MAP-1', 'RUNTIME_SNAPSHOT', 'The affected PATH_A and PATH_B configuration is still present in the June archive.', 'Supports analytical extension through June; missing L30 still lacks its own source path.', 'SYN-204'], ['DC-05', '2026-07-01', 'CFG-JUL-MISSING', 'UNKNOWN', 'UNAVAILABLE', 'No July runtime configuration or mapping continuity evidence is supplied.', 'July exposure remains unresolved; received July records alone cannot settle the boundary.', 'SYN-204'], ['DC-06', '2026-09-28', 'REPRO-0928', 'MAP-1', 'DEFECT_REPRODUCTION', 'A separate reproduction confirms distinct payment-originator IDs collapse to the customer key on PATH_A and PATH_B.', 'Discovery date is not the exposure start date.', 'SYN-204'], ['DC-07', '2026-10-01', 'SANDBOX-MAP-2', 'MAP-2', 'PROPOSED_CORRECTION', 'Sandbox proposal maps PATH_A and PATH_B to payment_originator_id and preserves PATH_C.', 'No production deployment or acceptance is evidenced.', 'SYN-204']], 'grain': 'One dated mapping-version evidence event or explicitly unavailable historical checkpoint, identified by chronology_id.'}], 'findings': [{'id': 'LB-F01', 'title': 'Expected historical unit remains absent from retrieval', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-201', 'SYN-202'], 'detail': 'The independent manifest names 30 units. Twenty-nine distinct in-scope units are retrieved; L30 is absent. June coverage is 4/5 even though raw intake rows all have classification buckets.', 'recommendation': 'Recover L30 and its source lineage or retain the explicit unreconciled population limitation; do not close the lookback as complete.'}, {'id': 'LB-F02', 'title': 'Most units retain a review or evidence dependency', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-201', 'SYN-203', 'SYN-205'], 'detail': 'Only six no-new-information desk reviews have no open unit action. Six referrals, six re-reviews, six pending reviews, five unassessable summaries and one missing unit account for 24 unresolved unit dependencies.', 'recommendation': 'Assign and complete each distinct evidence, retrieval, re-review and referral route; report progress with all 30 expected units as denominator.'}, {'id': 'LB-F03', 'title': 'Three duplicate rows and two July exclusions can distort activity totals', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-202'], 'detail': 'Raw intake has 34 representations:29 canonical, three duplicates of L02 L12 L22, and two July records. Known canonical activity is 449500 USD; duplicate and excluded amounts must not inflate it.', 'recommendation': 'Preserve alias links and excluded rows, verify canonical selection and investigate the July scope boundary separately.'}, {'id': 'LB-F04', 'title': 'Historical desk review does not decide filing or case closure', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-203', 'SYN-204', 'SYN-205'], 'detail': 'Six new-information referrals remain unacknowledged in the fictional record. No actual authorized filing, nonfiling, account action or whole-review disposition is supplied.', 'recommendation': 'Carry open handoffs until the responsible human process returns evidence; preserve this lookback as an analytical review with explicit limits.'}], 'evidence': [{'id': 'SYN-201', 'title': 'Independent fictional historical control manifest', 'locator': '10-worked-example.md, thirty-unit manifest and six-period control totals', 'claim_class': 'Observed'}, {'id': 'SYN-202', 'title': 'Fictional archive retrieval with duplicates exclusions and missing unit', 'locator': '10-worked-example.md, complete thirty-four-row retrieval ledger', 'claim_class': 'Observed'}, {'id': 'SYN-203', 'title': 'Fictional comparison outcomes and incomplete review states', 'locator': '10-worked-example.md, complete unit and review-action registers', 'claim_class': 'Observed'}, {'id': 'SYN-204', 'title': 'Dated fictional mapping-version chronology and source-path impact register', 'locator': '10-worked-example.md, DefectChronology and SourcePathInputs', 'claim_class': 'Observed'}, {'id': 'REF-001', 'title': 'FFIEC suspicious activity monitoring examination procedures', 'locator': 'https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04_ep', 'claim_class': 'Reported'}, {'id': 'REF-002', 'title': 'Federal Reserve SR 26-2, April 17, 2026', 'locator': 'https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm', 'claim_class': 'Reported'}, {'id': 'REF-003', 'title': 'Federal Reserve, Supervisory Guidance on Model Risk Management', 'locator': 'https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm', 'claim_class': 'Reported'}, {'id': 'REF-004', 'title': 'FinCEN and federal banking agencies, SAR FAQs, October 9, 2025', 'locator': 'https://www.fincen.gov/system/files/2025-10/SAR-FAQs-October-2025.pdf', 'claim_class': 'Reported'}, {'id': 'REF-005', 'title': 'FATF, Guidance for a Risk-Based Approach: The Banking Sector', 'locator': 'https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Risk-Based-Approach-Banking-Sector.pdf.coredownload.pdf', 'claim_class': 'Reported'}, {'id': 'REF-006', 'title': 'NIST, Confidence intervals for proportions', 'locator': 'https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm', 'claim_class': 'Reported'}, {'id': 'REF-007', 'title': 'GAO, Standards for Internal Control in the Federal Government, 2025 revision', 'locator': 'https://www.gao.gov/assets/890/882014.pdf', 'claim_class': 'Reported'}, {'id': 'SYN-205', 'title': 'Complete fictional historical/current comparison packets and material fact dictionary', 'locator': '10-worked-example.md, ComparisonPackets and exact historical/current source facts', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Expected historical units', 'value': 30, 'method': 'Independent six-period manifest with five canonical units per month.', 'format': '#,##0'}, {'label': 'Retrieved canonical units', 'value': 29, 'method': '34 received rows minus 3 duplicates minus 2 out-of-scope rows.', 'format': '#,##0'}, {'label': 'Desk comparisons completed', 'value': 12, 'method': '6 no-new-information comparisons plus 6 referrals; referral work remains open.', 'format': '#,##0'}, {'label': 'Known canonical activity USD', 'value': 449500, 'format': '$#,##0.00', 'method': 'Sum of L01 through L29 once; L30 amount is unknown.'}], 'limitations': ['Every record is fictional; results test this supplied procedure and do not establish operational effectiveness.', 'Illustrative cutoffs, partitions, labels, capacities and severity choices are authored examples, not regulatory thresholds.', 'Human scope approval, deployment authority, case disposition and reporting decisions are not supplied.', 'Missing, censored and unresolved evidence remains visible; no favorable default is permitted.'], 'conclusion': 'The lookback is incomplete. Twenty-nine of 30 expected historical units are retrieved, twelve desk comparisons are complete, and only six units have no open desk-review action. Six referrals and eighteen other evidence or review dependencies remain unresolved; no filing or whole-review approval is implied.', 'report_narrative': [['The lookback is incomplete. Twenty-nine of 30 expected historical units are retrieved, twelve desk comparisons are complete, and only six units have no open desk-review action. Six referrals and eighteen other evidence or review dependencies remain unresolved; no filing or whole-review approval is implied.'], ['The independent manifest defines January through June2026 and five units per month. Dated MAP-1 snapshots on January01, March31 and June30 show PATH_A and PATH_B using customer_id instead of payment_originator_id; PATH_C remains correctly mapped. July configuration evidence is unavailable. Analytical expansion through June follows that chronology; actual institutional scope acceptance is not supplied.'], ['Raw intake reconciles 34 representations to 29 canonical units,3 duplicates and 2 July exclusions. That arithmetic does not cure missing L30. June is 4/5 retrieved. Known canonical activity totals 449500 USD and excludes L30, whose amount is unknown.'], ['CanonicalUnits preserves all 30 expected records, including the missing placeholder. RetrievalLedger preserves every received representation and alias link. Historical statuses remain separate from current review states, so re-review never rewrites the original decision history.'], ['Twelve complete historical/current packets support the desk-comparison count. COMP-L01 through COMP-L06 retain the same material fact sets and identify no newly material information; COMP-L07 through COMP-L12 add concrete identity, scope or purpose facts and require referral. Six other units need re-review, six await review, five lack essential support and one is not retrieved. All six referrals have completed comparison packets but no actual receiving disposition.'], ['ComparisonPackets prints original facts, rationale, cutoff, recovered evidence, material fact sets and expected routes. DefectChronology supplies dated version evidence and the unresolved July boundary. SourcePathInputs identifies each retrieved unit’s feed path; L30 remains unknown. These sources support the fictional analytical result but not an actual institutional decision.'], ['Proposed work is to recover L30, obtain support for L25 through L29, finish L13 through L24 reviews, and obtain responsible case-review responses for L07 through L12. Filing, account action and whole-review acceptance remain separate human decisions.'], ['Do not report a 100% completion rate from received-row classification or twelve completed desk comparisons. Reperform the thirty-unit state reconciliation, amount conservation, duplicate links and completion gates. The fictional checks establish evidence accounting only, not a completed operational remediation.']], 'methods': ['Freeze the scope, source versions, population grain, evidence cutoff and decision question before calculating.', 'Reconcile every received, eligible, excluded, duplicate and unresolved record against independent controls.', 'Apply the exact predicates, joins, state transitions and denominators in files 03 through 05.', 'Challenge missing data, counterexamples, boundary conditions and alternative explanations using file 09.', 'Reproduce file 10 before replacing fictional data; preserve approval gaps and incomplete coverage.'], 'actions': [{'id': 'LO-A01', 'finding_id': 'LB-F01', 'proposal': 'Recover L30 and its source lineage or retain the explicit unreconciled population limitation; do not close the lookback as complete.', 'owner': 'Proposed accountable role; assignment not recorded', 'due_date': None, 'status': 'Proposed'}, {'id': 'LO-A02', 'finding_id': 'LB-F02', 'proposal': 'Assign and complete each distinct evidence, retrieval, re-review and referral route; report progress with all 30 expected units as denominator.', 'owner': 'Proposed accountable role; assignment not recorded', 'due_date': None, 'status': 'Proposed'}, {'id': 'LO-A03', 'finding_id': 'LB-F03', 'proposal': 'Preserve alias links and excluded rows, verify canonical selection and investigate the July scope boundary separately.', 'owner': 'Proposed accountable role; assignment not recorded', 'due_date': None, 'status': 'Proposed'}, {'id': 'LO-A04', 'finding_id': 'LB-F04', 'proposal': 'Carry open handoffs until the responsible human process returns evidence; preserve this lookback as an analytical review with explicit limits.', 'owner': 'Proposed accountable role; assignment not recorded', 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Exact fictional reconciliation', 'result': 'REVIEW REQUIRED', 'evidence': 'Reperform all ProcessQA rows and file 10 checkpoints in this session.'}, {'id': 'QA-02', 'check': 'Evidence and counterevidence', 'result': 'REVIEW REQUIRED', 'evidence': 'Review every field, rule and exception in files 02 through 05.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No operational approval or filing decision is represented by these fictional records.'}], 'suite_id': 'lookback-review', 'version': '1.2.0', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.'}
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
