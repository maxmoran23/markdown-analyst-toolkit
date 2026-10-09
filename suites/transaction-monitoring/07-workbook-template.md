# Transaction Monitoring Review — fixed workbook template

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
| RawTransactions | `raw_row_id`, `transaction_id`, `account_id`, `event_utc`, `direction`, `amount_text`, `currency`, `counterparty_id`, `posting_state`, `ownership_state`, `terminal_bucket`, `evidence_ids` |
| CanonicalLedger | `leg_id`, `raw_row_id`, `transaction_id`, `account_id`, `event_utc`, `direction`, `amount`, `currency`, `counterparty_id`, `ownership_state`, `scenario_eligible`, `evidence_ids` |
| Eligibility | `eligibility_id`, `raw_row_id`, `leg_id`, `account_id`, `scenario_id`, `eligibility_state`, `reason`, `evidence_ids` |
| AccountFlows | `account_id`, `currency`, `processed_tx_count`, `credit_total`, `debit_total`, `eligible_credit_total`, `eligible_debit_total`, `out_in_ratio`, `population_status` |
| WindowDiagnostics | `window_id`, `account_id`, `anchor_leg_id`, `start_utc`, `end_utc`, `observed_leg_ids`, `known_credit_total`, `known_debit_total`, `known_ratio`, `first_debit_hours`, `coverage_state`, `evidence_ids` |
| ScenarioResults | `scenario_result_id`, `account_id`, `scenario_id`, `eligible`, `rule_result`, `first_credit_to_debit_hours`, `review_outcome`, `evidence_ids` |
| ReviewLedger | `review_id`, `scenario_result_id`, `finding_id`, `account_id`, `raw_result`, `explanation_state`, `counterevidence`, `next_evidence`, `human_disposition`, `evidence_ids` |
| ControlTotals | `control_id`, `measure`, `expected_value`, `actual_value`, `unit`, `result`, `calculation`, `evidence_ids` |
| EvidenceProvenance | `evidence_id`, `source_kind`, `source_date`, `availability`, `locator`, `supports`, `limitation` |
| ProcessQA | `check_id`, `check`, `expected`, `actual`, `status`, `reviewer`, `evidence_ids` |

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

DATA = {'slug': 'transaction-monitoring', 'title': 'Transaction Monitoring Review', 'summary': 'Reconcile a transaction extract, calculate transparent monitoring scenarios, and turn rule matches into reviewable observations with explicit benign explanations.', 'audience': 'Monitoring analysts, scenario owners, and independent control reviewers', 'decision': 'Which scenario matches merit further review, which have supported explanations, and which cannot be assessed because the inputs are incomplete?', 'palette': 'slate', 'report_sections': ['Review priorities and known movement', 'Scope, population, and scenario method', 'Findings and benign explanations', 'Account flow calculations', 'Scenario matches and review outcomes', 'Evidence and criterion provenance', 'Proposed review and data-repair actions', 'Limitations, quality checks, and human decision'], 'domain_tables': [{'name': 'RawTransactions', 'title': 'Raw source rows and terminal reconciliation', 'columns': ['raw_row_id', 'transaction_id', 'account_id', 'event_utc', 'direction', 'amount_text', 'currency', 'counterparty_id', 'posting_state', 'ownership_state', 'terminal_bucket', 'evidence_ids'], 'rows': [['R01', 'T01', 'A', '2026-09-01T13:00:00Z', 'CREDIT', '6000.00', 'USD', 'P01', 'POSTED', 'CONFIRMED_EXTERNAL', 'PROCESSED', 'SYN-001'], ['R02', 'T02', 'A', '2026-09-01T14:00:00Z', 'CREDIT', '4000.00', 'USD', 'P02', 'POSTED', 'CONFIRMED_EXTERNAL', 'PROCESSED', 'SYN-001'], ['R03', 'T03', 'A', '2026-09-01T15:00:00Z', 'DEBIT', '9500.00', 'USD', 'P03', 'POSTED', 'CONFIRMED_EXTERNAL', 'PROCESSED', 'SYN-001'], ['R04', 'T04', 'B', '2026-09-01T13:00:00Z', 'CREDIT', '5000.00', 'USD', 'P04', 'POSTED', 'CONFIRMED_EXTERNAL', 'PROCESSED', 'SYN-001'], ['R05', 'T05', 'B', '2026-09-01T16:00:00Z', 'DEBIT', '4800.00', 'USD', 'P05', 'POSTED', 'CONFIRMED_EXTERNAL', 'PROCESSED', 'SYN-001'], ['R06', 'T06', 'C', '2026-09-01T13:00:00Z', 'CREDIT', '3000.00', 'USD', 'C-OWN-1', 'POSTED', 'CONFIRMED_OWN', 'PROCESSED', 'SYN-001;SYN-004'], ['R07', 'T07', 'C', '2026-09-01T14:00:00Z', 'DEBIT', '3000.00', 'USD', 'C-OWN-2', 'POSTED', 'CONFIRMED_OWN', 'PROCESSED', 'SYN-001;SYN-004'], ['R08', 'T08', 'D', '2026-09-01T17:00:00Z', 'DEBIT', '1000.00', 'USD', 'P06', 'POSTED', 'CONFIRMED_EXTERNAL', 'PROCESSED', 'SYN-001'], ['R09', 'T01', 'A', '2026-09-01T13:00:00Z', 'CREDIT', '6000.00', 'USD', 'P01', 'POSTED', 'CONFIRMED_EXTERNAL', 'DUPLICATE', 'SYN-001'], ['R10', 'T09', 'D', '2026-09-01T18:00:00Z', 'DEBIT', 'unreadable', 'USD', 'P07', 'POSTED', 'CONFIRMED_EXTERNAL', 'UNPARSED', 'SYN-001;SYN-005']], 'formats': {}, 'primary_key': ['raw_row_id'], 'column_contracts': {'raw_row_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable.'}, 'transaction_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Source economic transaction identifier. Its uniqueness is assessed with account leg and source version; matching amount or narrative alone is insufficient.'}, 'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge.'}, 'event_utc': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant.'}, 'direction': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Canonical CREDIT or DEBIT from the account perspective. Amount remains nonnegative; do not infer direction from a signed display string.'}, 'amount_text': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact source amount string before parsing. It can contain unreadable text; preserve it as evidence and never sum it directly.'}, 'currency': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount.'}, 'counterparty_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Supplied counterparty reference for this economic leg. Similar names or repeated identifiers do not independently establish common ownership.'}, 'posting_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Canonical posting status that determines whether a leg enters the declared posted population. A pending item remains visible outside that population.'}, 'ownership_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Evidence-backed own/external classification for the specific leg and historical period. Unknown ownership is not automatically external or own.'}, 'terminal_bucket': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exactly one initial raw-row reconciliation outcome. It explains whether the row is processed, duplicate or unreadable; scenario exclusions are a separate layer.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'grain': 'one immutable raw receipt row, including extraction duplicates and unparsed amounts', 'report_section': 4}, {'name': 'CanonicalLedger', 'title': 'Canonical known posted account legs', 'columns': ['leg_id', 'raw_row_id', 'transaction_id', 'account_id', 'event_utc', 'direction', 'amount', 'currency', 'counterparty_id', 'ownership_state', 'scenario_eligible', 'evidence_ids'], 'rows': [['L-T01', 'R01', 'T01', 'A', '2026-09-01T13:00:00Z', 'CREDIT', 6000.0, 'USD', 'P01', 'CONFIRMED_EXTERNAL', True, 'SYN-001'], ['L-T02', 'R02', 'T02', 'A', '2026-09-01T14:00:00Z', 'CREDIT', 4000.0, 'USD', 'P02', 'CONFIRMED_EXTERNAL', True, 'SYN-001'], ['L-T03', 'R03', 'T03', 'A', '2026-09-01T15:00:00Z', 'DEBIT', 9500.0, 'USD', 'P03', 'CONFIRMED_EXTERNAL', True, 'SYN-001'], ['L-T04', 'R04', 'T04', 'B', '2026-09-01T13:00:00Z', 'CREDIT', 5000.0, 'USD', 'P04', 'CONFIRMED_EXTERNAL', True, 'SYN-001'], ['L-T05', 'R05', 'T05', 'B', '2026-09-01T16:00:00Z', 'DEBIT', 4800.0, 'USD', 'P05', 'CONFIRMED_EXTERNAL', True, 'SYN-001'], ['L-T06', 'R06', 'T06', 'C', '2026-09-01T13:00:00Z', 'CREDIT', 3000.0, 'USD', 'C-OWN-1', 'CONFIRMED_OWN', False, 'SYN-001;SYN-004'], ['L-T07', 'R07', 'T07', 'C', '2026-09-01T14:00:00Z', 'DEBIT', 3000.0, 'USD', 'C-OWN-2', 'CONFIRMED_OWN', False, 'SYN-001;SYN-004'], ['L-T08', 'R08', 'T08', 'D', '2026-09-01T17:00:00Z', 'DEBIT', 1000.0, 'USD', 'P06', 'CONFIRMED_EXTERNAL', True, 'SYN-001']], 'formats': {'amount': '#,##0.00'}, 'primary_key': ['leg_id'], 'column_contracts': {'leg_id': {'type': 'text', 'nullable': True, 'unit': 'identifier', 'description': 'Unique identifier of one readable canonical posted account leg. It joins to the raw source and is never substituted for a customer identifier.'}, 'raw_row_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable.'}, 'transaction_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Source economic transaction identifier. Its uniqueness is assessed with account leg and source version; matching amount or narrative alone is insufficient.'}, 'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge.'}, 'event_utc': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant.'}, 'direction': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Canonical CREDIT or DEBIT from the account perspective. Amount remains nonnegative; do not infer direction from a signed display string.'}, 'amount': {'type': 'number', 'nullable': True, 'unit': 'row currency', 'description': 'Known nonnegative monetary amount in the row currency. Null means unrecovered source value and blocks the relevant completeness proposition.'}, 'currency': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount.'}, 'counterparty_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Supplied counterparty reference for this economic leg. Similar names or repeated identifiers do not independently establish common ownership.'}, 'ownership_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Evidence-backed own/external classification for the specific leg and historical period. Unknown ownership is not automatically external or own.'}, 'scenario_eligible': {'type': 'boolean', 'nullable': False, 'unit': 'boolean', 'description': 'Boolean record-level inclusion flag. True means a known eligible leg, not proof the entire account or window is complete.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'foreign_keys': [{'columns': ['raw_row_id'], 'table': 'RawTransactions', 'references': ['raw_row_id']}], 'grain': 'one readable unique posted economic account leg', 'report_section': 4}, {'name': 'Eligibility', 'title': 'Raw-row scenario eligibility decisions', 'columns': ['eligibility_id', 'raw_row_id', 'leg_id', 'account_id', 'scenario_id', 'eligibility_state', 'reason', 'evidence_ids'], 'rows': [['EL-R01', 'R01', 'L-T01', 'A', 'TM-01', 'ELIGIBLE_KNOWN', 'Known external posted leg; account-level completeness checked separately', 'SYN-001'], ['EL-R02', 'R02', 'L-T02', 'A', 'TM-01', 'ELIGIBLE_KNOWN', 'Known external posted leg; account-level completeness checked separately', 'SYN-001'], ['EL-R03', 'R03', 'L-T03', 'A', 'TM-01', 'ELIGIBLE_KNOWN', 'Known external posted leg; account-level completeness checked separately', 'SYN-001'], ['EL-R04', 'R04', 'L-T04', 'B', 'TM-01', 'ELIGIBLE_KNOWN', 'Known external posted leg; account-level completeness checked separately', 'SYN-001'], ['EL-R05', 'R05', 'L-T05', 'B', 'TM-01', 'ELIGIBLE_KNOWN', 'Known external posted leg; account-level completeness checked separately', 'SYN-001'], ['EL-R06', 'R06', 'L-T06', 'C', 'TM-01', 'EXCLUDED_OWN', 'SYN-004 confirms common customer ownership during period', 'SYN-001;SYN-004'], ['EL-R07', 'R07', 'L-T07', 'C', 'TM-01', 'EXCLUDED_OWN', 'SYN-004 confirms common customer ownership during period', 'SYN-001;SYN-004'], ['EL-R08', 'R08', 'L-T08', 'D', 'TM-01', 'ELIGIBLE_KNOWN', 'Known external posted leg; account-level completeness checked separately', 'SYN-001'], ['EL-R09', 'R09', 'L-T01', 'A', 'TM-01', 'DUPLICATE', 'Exact second extraction of R01; not another account leg', 'SYN-001'], ['EL-R10', 'R10', None, 'D', 'TM-01', 'BLOCKED', 'Posted in-scope amount unreadable; blocks D completeness', 'SYN-001;SYN-005']], 'formats': {}, 'primary_key': ['eligibility_id'], 'column_contracts': {'eligibility_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique identifier for a raw-row/scenario decision. It preserves reasons for retained, excluded and blocked records without removing source population members.'}, 'raw_row_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable.'}, 'leg_id': {'type': 'text', 'nullable': True, 'unit': 'identifier', 'description': 'Unique identifier of one readable canonical posted account leg. It joins to the raw source and is never substituted for a customer identifier.'}, 'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge.'}, 'scenario_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Exact illustrative scenario identifier. Criteria are versioned outside the identifier in the case manifest and cannot drift between outputs.'}, 'eligibility_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Record-level eligibility conclusion. ELIGIBLE_KNOWN, EXCLUDED_OWN, DUPLICATE and BLOCKED are mutually exclusive in the specimen.'}, 'reason': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific evidence-backed reason for a state or transition. It identifies the relevant row, rule or missing fact rather than a generic compliance label.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'foreign_keys': [{'columns': ['raw_row_id'], 'table': 'RawTransactions', 'references': ['raw_row_id']}], 'grain': 'one raw-row decision for the declared daily scenario', 'report_section': 4}, {'name': 'AccountFlows', 'columns': ['account_id', 'currency', 'processed_tx_count', 'credit_total', 'debit_total', 'eligible_credit_total', 'eligible_debit_total', 'out_in_ratio', 'population_status'], 'rows': [['A', 'USD', 3, 10000, 9500, 10000, 9500, 0.95, 'COMPLETE'], ['B', 'USD', 2, 5000, 4800, 5000, 4800, 0.96, 'COMPLETE'], ['C', 'USD', 2, 3000, 3000, 0, 0, None, 'OWN_TRANSFER_EXCLUDED'], ['D', 'USD', 1, 0, 1000, 0, 1000, None, 'UNPARSED_AMOUNT']], 'formats': {'credit_total': '#,##0.00', 'debit_total': '#,##0.00', 'eligible_credit_total': '#,##0.00', 'eligible_debit_total': '#,##0.00', 'out_in_ratio': '0.0%'}, 'primary_key': ['account_id', 'currency'], 'column_contracts': {'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge.'}, 'currency': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount.'}, 'processed_tx_count': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Count of readable canonical economic legs at account/currency grain. It excludes extraction duplicates and unknown-amount rows but retains own transfers.'}, 'credit_total': {'type': 'number', 'nullable': False, 'unit': 'row currency', 'description': 'Known eligible or gross credit subtotal as specified by the table grain. It is not necessarily a complete total when coverage_state or population_status is defective.'}, 'debit_total': {'type': 'number', 'nullable': True, 'unit': 'row currency', 'description': 'Known eligible debit subtotal at the table grain. Null is required for a window total dependent on an unknown debit; known subtotals elsewhere remain explicitly partial.'}, 'eligible_credit_total': {'type': 'number', 'nullable': False, 'unit': 'row currency', 'description': 'Sum of known credit amounts after stated scenario exclusions. It cannot include confirmed own legs or a copied extraction duplicate.'}, 'eligible_debit_total': {'type': 'number', 'nullable': False, 'unit': 'row currency', 'description': 'Sum of known debit amounts after stated scenario exclusions. It is not an attributed or suspicious amount and may exceed eligible credits.'}, 'out_in_ratio': {'type': 'number', 'nullable': True, 'unit': 'ratio', 'description': 'Eligible debit total divided by positive eligible credit total. Stored as a dimensionless ratio and displayed as a percentage without changing decision precision.'}, 'population_status': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Account-level completeness or exclusion state. COMPLETE, OWN_TRANSFER_EXCLUDED and UNPARSED_AMOUNT have different analytical consequences.'}}, 'title': 'AccountFlows', 'grain': 'one account and currency within the fixed daily event period', 'report_section': 5}, {'name': 'WindowDiagnostics', 'title': 'Observed credit-anchored membership; coverage remains incomplete', 'columns': ['window_id', 'account_id', 'anchor_leg_id', 'start_utc', 'end_utc', 'observed_leg_ids', 'known_credit_total', 'known_debit_total', 'known_ratio', 'first_debit_hours', 'coverage_state', 'evidence_ids'], 'rows': [['W-A-T01', 'A', 'L-T01', '2026-09-01T13:00:00Z', '2026-09-02T13:00:00Z', 'L-T01;L-T02;L-T03', 10000, 9500, 0.95, 2, 'BOUNDARY_INCOMPLETE', 'SYN-001;SYN-006'], ['W-A-T02', 'A', 'L-T02', '2026-09-01T14:00:00Z', '2026-09-02T14:00:00Z', 'L-T02;L-T03', 4000, 9500, 2.375, 1, 'BOUNDARY_INCOMPLETE', 'SYN-001;SYN-006'], ['W-B-T04', 'B', 'L-T04', '2026-09-01T13:00:00Z', '2026-09-02T13:00:00Z', 'L-T04;L-T05', 5000, 4800, 0.96, 3, 'BOUNDARY_INCOMPLETE', 'SYN-001;SYN-006']], 'formats': {'known_credit_total': '#,##0.00', 'known_debit_total': '#,##0.00', 'known_ratio': '0.0%', 'first_debit_hours': '0.0'}, 'primary_key': ['window_id'], 'column_contracts': {'window_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable account/anchor/specification window key. It distinguishes overlapping observations so a membership count cannot be mistaken for unique transactions.'}, 'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge.'}, 'anchor_leg_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Canonical eligible credit that starts a diagnostic window. Only credit anchors are used; a debit cannot silently become an anchor.'}, 'start_utc': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Inclusive UTC instant at the anchor. The applicable window convention determines endpoint inclusion, not the date formatting of the rendered table.'}, 'end_utc': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'UTC endpoint exactly 24 elapsed hours after the anchor. The scenario-design closed interval includes this instant; the TM diagnostic convention matches it.'}, 'observed_leg_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited canonical legs observed inside the diagnostic interval. This list is partial when the extract does not cover the entire interval.'}, 'known_credit_total': {'type': 'number', 'nullable': False, 'unit': 'row currency', 'description': 'Sum of readable credits only at the declared stage, account or observed diagnostic window. The word known is substantive where an unresolved amount exists.'}, 'known_debit_total': {'type': 'number', 'nullable': False, 'unit': 'row currency', 'description': 'Sum of readable debits only at the declared stage, account or observed diagnostic window. An unknown debit is not imputed as a measured zero.'}, 'known_ratio': {'type': 'number', 'nullable': True, 'unit': 'ratio', 'description': 'Ratio of known observed debits to known observed credits when the denominator is positive. Boundary-incomplete diagnostics do not establish a complete rule result.'}, 'first_debit_hours': {'type': 'number', 'nullable': True, 'unit': 'hours', 'description': 'Elapsed hours from anchor to first strictly subsequent eligible debit. Null means no qualifying ordered pair; a contemporaneous debit cannot satisfy the predicate.'}, 'coverage_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Completeness state for the exact account/window inputs. COMPLETE, BOUNDARY_INCOMPLETE and AMOUNT_UNKNOWN cannot be collapsed into a binary risk score.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'foreign_keys': [{'columns': ['anchor_leg_id'], 'table': 'CanonicalLedger', 'references': ['leg_id']}], 'grain': 'one eligible credit anchor and its observed closed 24-hour interval', 'report_section': 5}, {'name': 'ScenarioResults', 'columns': ['scenario_result_id', 'account_id', 'scenario_id', 'eligible', 'rule_result', 'first_credit_to_debit_hours', 'review_outcome', 'evidence_ids'], 'rows': [['SR-001', 'A', 'TM-01', True, 'MATCH', 2, 'ESCALATE_FOR_REVIEW', 'SYN-001;SYN-002'], ['SR-002', 'B', 'TM-01', True, 'MATCH', 3, 'EXPLANATION_SUPPORTED', 'SYN-001;SYN-003'], ['SR-003', 'C', 'TM-01', False, 'EXCLUDED', None, 'OWN_TRANSFER_CONFIRMED', 'SYN-001;SYN-004'], ['SR-004', 'D', 'TM-01', False, 'NOT_ASSESSABLE', None, 'DATA_REPAIR_REQUIRED', 'SYN-001;SYN-005']], 'formats': {'first_credit_to_debit_hours': '0.0'}, 'primary_key': ['scenario_result_id'], 'column_contracts': {'scenario_result_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable daily account/scenario/window result key. It links to the review register without being replaced after a contextual explanation.'}, 'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge.'}, 'scenario_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Exact illustrative scenario identifier. Criteria are versioned outside the identifier in the case manifest and cannot drift between outputs.'}, 'eligible': {'type': 'boolean', 'nullable': False, 'unit': 'boolean', 'description': 'Account-result eligibility flag after completeness and exclusion gates. False is distinguished by rule_result as either excluded or not assessable.'}, 'rule_result': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Deterministic raw result under the named specification: MATCH, NO_MATCH, EXCLUDED or NOT_ASSESSABLE. Contextual evidence does not rewrite it.'}, 'first_credit_to_debit_hours': {'type': 'number', 'nullable': True, 'unit': 'hours', 'description': 'Elapsed hours from the first eligible daily credit to its first strictly subsequent eligible debit. It screens timing and does not attribute funding.'}, 'review_outcome': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Proposed contextual assessment distinct from raw rule_result. No value in this field constitutes an authorized filing or relationship decision.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'title': 'ScenarioResults', 'grain': 'one account, daily window and scenario specification', 'report_section': 5}, {'name': 'ReviewLedger', 'title': 'Contextual review and unrecorded human disposition', 'columns': ['review_id', 'scenario_result_id', 'finding_id', 'account_id', 'raw_result', 'explanation_state', 'counterevidence', 'next_evidence', 'human_disposition', 'evidence_ids'], 'rows': [['RV-A', 'SR-001', 'TM-F01', 'A', 'MATCH', 'UNSUPPORTED', 'No opening balance or onward P03 records; timing does not trace funds', 'Invoice or contract matching T03 plus counterparty role', 'NOT_RECORDED', 'SYN-001;SYN-002'], ['RV-B', 'SR-002', 'TM-F02', 'B', 'MATCH', 'SUPPORTED_FOR_T05', 'One invoice does not establish relationship-wide legitimacy', 'Reviewer assessment of invoice linkage and remaining scope', 'NOT_RECORDED', 'SYN-001;SYN-003'], ['RV-C', 'SR-003', None, 'C', 'EXCLUDED', 'OWNERSHIP_CONFIRMED', 'Exclusion applies only to external-flow TM-01', 'Retain SYN-004 and check any other applicable scenario separately', 'NOT_RECORDED', 'SYN-001;SYN-004'], ['RV-D', 'SR-004', 'TM-F03', 'D', 'NOT_ASSESSABLE', 'SOURCE_DEFECT', 'Known debit does not bound unreadable T09 value', 'Corrected T09 amount and source control total', 'NOT_RECORDED', 'SYN-001;SYN-005']], 'formats': {}, 'primary_key': ['review_id'], 'column_contracts': {'review_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique contextual review record. It joins the exact raw scenario result and retains the relevant finding or an explained null when no finding is raised.'}, 'scenario_result_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable daily account/scenario/window result key. It links to the review register without being replaced after a contextual explanation.'}, 'finding_id': {'type': 'text', 'nullable': True, 'unit': 'identifier', 'description': 'Stable key to the Findings register. Nullable only where a documented review outcome raises no separate finding; absence is not a missing case record.'}, 'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge.'}, 'raw_result': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Preserved deterministic rule result before human review or delivery grouping. Explanations and grouping decisions must not delete or change it.'}, 'explanation_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Scope-limited state of the explanation evidence. Supported documentation for one payment does not become an assurance about the whole account.'}, 'counterevidence': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Strongest supplied limitation or competing interpretation that tempers the proposed concern. It may identify missing evidence without treating missingness as guilt.'}, 'next_evidence': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific discriminating document or control record needed for the next decision. It is a request proposal, not evidence that retrieval occurred.'}, 'human_disposition': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Recorded authorized human decision. NOT_RECORDED is required in this specimen because no real person has approved or closed anything.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'foreign_keys': [{'columns': ['scenario_result_id'], 'table': 'ScenarioResults', 'references': ['scenario_result_id']}], 'grain': 'one contextual review of a retained daily scenario result', 'report_section': 5}, {'name': 'ControlTotals', 'title': 'Count and monetary reconciliation with known limits', 'columns': ['control_id', 'measure', 'expected_value', 'actual_value', 'unit', 'result', 'calculation', 'evidence_ids'], 'rows': [['CT-01', 'Received rows', 10, 10, 'rows', 'PASS', '8 processed + 1 duplicate + 1 unparsed', 'SYN-001'], ['CT-02', 'Canonical known legs', 8, 8, 'legs', 'PASS', 'L-T01 through L-T08', 'SYN-001'], ['CT-03', 'Known credits', 18000, 18000, 'USD', 'PASS', '6000 + 4000 + 5000 + 3000', 'SYN-001'], ['CT-04', 'Known debits', 18300, 18300, 'USD', 'PASS', '9500 + 4800 + 3000 + 1000', 'SYN-001'], ['CT-05', 'Complete monetary population', None, None, 'USD', 'NOT_ASSESSABLE', 'T09 amount unknown; known gross is 36300, not complete gross', 'SYN-001;SYN-005'], ['CT-06', 'Daily rule matches', 2, 2, 'account windows', 'PASS', 'SR-001 and SR-002', 'SYN-001'], ['CT-07', 'Distinct observed rolling legs', 5, 5, 'legs', 'PASS', 'Union T01,T02,T03,T04,T05; membership count 7', 'SYN-001;SYN-006']], 'formats': {}, 'primary_key': ['control_id'], 'column_contracts': {'control_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique reconciliation-control key. Controls can test different grains; counts and monetary comparisons are never combined into one unexplained balance.'}, 'measure': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Precisely named control measure including known versus complete scope. A passing count measure cannot substitute for unknown monetary completeness.'}, 'expected_value': {'type': 'number', 'nullable': True, 'unit': 'row unit', 'description': 'Independent expected numerical control value when known. Null records a proposition whose true value is unavailable rather than a failed zero comparison.'}, 'actual_value': {'type': 'number', 'nullable': True, 'unit': 'row unit', 'description': 'Reproduced value from the supplied rows. Null remains null when the corresponding measure is unavailable; never enter an attractive expected value by copying.'}, 'unit': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Physical or analytical unit of the control, such as USD, rows, legs or account windows. The label determines what can validly be added or divided.'}, 'result': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Control result or acceptance state. PASS applies to an executed synthetic check; it is not regulatory assurance or an operational approval.'}, 'calculation': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicit arithmetic or set-membership expression supporting the control. It retains unknown components instead of replacing them with a rounded display.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'grain': 'one explicitly named count or monetary reconciliation proposition', 'report_section': 5}, {'name': 'EvidenceProvenance', 'title': 'Source identity, period, availability and evidential limits', 'columns': ['evidence_id', 'source_kind', 'source_date', 'availability', 'locator', 'supports', 'limitation'], 'rows': [['SYN-001', 'Authored fictional case record', '2026-09-02', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, raw population R01–R10', 'Fictional transaction extract', 'Supports only the stated fictional proposition; no external subject fact or institutional approval'], ['SYN-002', 'Authored fictional context record', '2026-09-02', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, context register A', 'Fictional account A profile', 'Supports only the stated fictional proposition; no external subject fact or institutional approval'], ['SYN-003', 'Authored fictional case record', '2026-09-02', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, context register B', 'Fictional invoice and matching confirmation', 'Supports only the stated fictional proposition; no external subject fact or institutional approval'], ['SYN-004', 'Authored fictional case record', '2026-09-02', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, context register C', 'Fictional ownership confirmation', 'Supports only the stated fictional proposition; no external subject fact or institutional approval'], ['SYN-005', 'Authored fictional case record', '2026-09-02', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, raw row R10', 'Fictional extract defect', 'Supports only the stated fictional proposition; no external subject fact or institutional approval'], ['SYN-006', 'Authored fictional case record', '2026-09-02', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, Window diagnostic convention; coverage stops Sep 02, 2026 12:00 AM ET', 'Fictional diagnostic window specification', 'Supports only the stated fictional proposition; no external subject fact or institutional approval']], 'formats': {}, 'primary_key': ['evidence_id'], 'column_contracts': {'evidence_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Exact unique Evidence key at one source-provenance row. It joins the common Evidence register without combining unrelated sources.'}, 'source_kind': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicitly fictional record type and origin. Authored cases and guidance references must not be mislabeled as actual institutional evidence.'}, 'source_date': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'ISO calendar date of the authored source package, distinct from transaction event dates and evidence retrieval dates.'}, 'availability': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'State of access to the source text. FULL_TEXT_IN_FILE_10 means the complete fictional content is supplied in this suite, not externally verified.'}, 'locator': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact file and section or row reference supporting retrieval of the fictional source. A title alone is insufficient.'}, 'supports': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Bounded proposition the source can establish in the synthetic exercise. It does not certify any broader customer or control conclusion.'}, 'limitation': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific scope restriction or evidential weakness that must accompany use of the source.'}}, 'grain': 'one fictional evidence source with its access state and evidential limit', 'report_section': 5}, {'name': 'ProcessQA', 'title': 'Explicit expected and actual control evidence', 'columns': ['check_id', 'check', 'expected', 'actual', 'status', 'reviewer', 'evidence_ids'], 'rows': [['TQ01', 'All source rows have one terminal bucket', '10 = 8 + 1 + 1', '10 = 8 + 1 + 1', 'PASS', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'SYN-001'], ['TQ02', 'Daily rule hits remain after B explanation', 'A and B MATCH', 'A and B MATCH', 'PASS', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'SYN-001;SYN-003'], ['TQ03', 'Rolling coverage', 'Three windows BOUNDARY_INCOMPLETE', 'Three windows BOUNDARY_INCOMPLETE', 'PASS', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'SYN-001;SYN-006'], ['TQ04', 'Complete monetary population', 'No complete total established', 'T09 amount unknown', 'REVIEW REQUIRED', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'SYN-005'], ['TQ05', 'Independent human disposition', 'Not supplied', 'Not supplied', 'NOT RECORDED', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'SYN-001']], 'formats': {}, 'primary_key': ['check_id'], 'column_contracts': {'check_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique process-quality check key retained across output formats. A later rerun creates a dated actual result without changing the original expectation.'}, 'check': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Falsifiable control proposition with defined expected evidence. It must be precise enough for another reviewer to reproduce.'}, 'expected': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact target result for the named check. This is fixed before execution and may state not supplied when the check concerns authorization.'}, 'actual': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Recorded output of the check. In future sessions, use NOT TESTED until performed; do not copy the specimen result as evidence of a new execution.'}, 'status': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Recorded PASS, FAIL, REVIEW REQUIRED, NOT RECORDED or NOT TESTED status for this check, separate from analytical finding severity.'}, 'reviewer': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Identity or role of the actual check performer. The specimen labels authored arithmetic and explicitly records absent independent operational review.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'grain': 'one performed or explicitly unrecorded quality proposition', 'report_section': 5}], 'findings': [{'id': 'TM-F01', 'title': 'Account A meets the illustrative rapid-movement rule', 'severity': 'MEDIUM', 'confidence': 'MODERATE', 'claim_class': 'Inferred', 'evidence_ids': ['SYN-001', 'SYN-002'], 'detail': 'Account A received $10,000.00 and sent $9,500.00 within two hours of the first receipt; the 95.0% ratio meets TM-01. Purpose remains unsupported.', 'recommendation': 'Obtain payment purpose and counterparties; refer to the authorized reviewer.'}, {'id': 'TM-F02', 'title': 'Account B has a supported ordinary-business explanation', 'severity': 'LOW', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001', 'SYN-003'], 'detail': 'The 96.0% rule match is retained; a matched supplier invoice supports the $4,800.00 payment.', 'recommendation': 'Document the explanation and seek human disposition; retain the rule hit.'}, {'id': 'TM-F03', 'title': 'Account D cannot be fully assessed', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001', 'SYN-005'], 'detail': 'One unreadable amount prevents account-level completeness; $1,000.00 is only the known posted debit.', 'recommendation': 'Repair the source extract and recompute D before making an account conclusion.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional transaction extract', 'locator': '10-worked-example.md, raw population R01–R10', 'claim_class': 'Observed'}, {'id': 'SYN-002', 'title': 'Fictional account A profile', 'locator': '10-worked-example.md, context register A', 'claim_class': 'Reported'}, {'id': 'SYN-003', 'title': 'Fictional invoice and matching confirmation', 'locator': '10-worked-example.md, context register B', 'claim_class': 'Observed'}, {'id': 'SYN-004', 'title': 'Fictional ownership confirmation', 'locator': '10-worked-example.md, context register C', 'claim_class': 'Observed'}, {'id': 'SYN-005', 'title': 'Fictional extract defect', 'locator': '10-worked-example.md, raw row R10', 'claim_class': 'Observed'}, {'id': 'SYN-006', 'title': 'Fictional diagnostic window specification', 'locator': '10-worked-example.md, Window diagnostic convention; coverage stops Sep 02, 2026 12:00 AM ET', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Raw rows', 'value': 10, 'method': 'Count R01–R10 before deduplication', 'format': '#,##0'}, {'label': 'Processed transactions', 'value': 8, 'method': '10 raw minus 1 duplicate minus 1 unparsed', 'format': '#,##0'}, {'label': 'Known gross movement USD', 'value': 36300, 'method': '$18,000.00 credits plus $18,300.00 debits; excludes unknown R10 amount', 'format': '$#,##0.00'}, {'label': 'Rule matches', 'value': 2, 'method': 'A and B match TM-01; C excluded; D not assessable', 'format': '#,##0'}], 'limitations': ['Synthetic rules are illustrative and are not regulatory thresholds.', 'Account D has an unknown amount; total monetary completeness is not established.', 'No opening balances or complete external flow paths are supplied.', 'The three rolling-window diagnostics extend beyond the extract end; known observed sums are reproducible but a complete rolling-rule result is not available.'], 'conclusion': 'Two accounts match the illustrative rapid-movement rule. One has a supported invoice explanation; the other needs further review. A separate account remains not assessable because an amount is unreadable.', 'report_narrative': [['Two accounts match the illustrative rapid-movement rule. One has a supported invoice explanation; the other needs further review. A separate account remains not assessable because an amount is unreadable.'], ['The ten raw rows reconcile to eight processed transactions after the documented duplicate and exclusion decisions. The fictional scenario uses explicit amount, ratio and timing criteria; unreadable amounts remain outside assessable sums.'], ['TM-F01: Account A received $10,000.00 and sent $9,500.00 within two hours of the first receipt; the 95.0% ratio meets TM-01. Purpose remains unsupported.', 'TM-F02: The 96.0% rule match is retained; a matched supplier invoice supports the $4,800.00 payment.', 'TM-F03: One unreadable amount prevents account-level completeness; $1,000.00 is only the known posted debit.'], ['Known gross movement is $36,300.00 within the captured records. Account totals retain the relationship between incoming and outgoing activity; gross movement is not net loss, customer income or suspicious value.', 'RawTransactions retains all ten rows; CanonicalLedger contains the eight readable unique posted legs. Eligibility retains ten separate reasons. Credit-anchored diagnostics contain seven memberships over five distinct legs; their known membership gross of $42,800.00 is overlapping and is not unique movement. All three diagnostic windows extend beyond the supplied observation boundary and cannot be represented as complete rolling-window assessments.'], ['Two accounts meet the raw illustrative rapid-movement criterion. One has a supported invoice explanation, while the other remains a review lead. An additional account is not assessable because an amount is unreadable; it cannot be scored as a negative.', 'Daily TM-01 and diagnostic rolling windows are separate measures. ReviewLedger retains four account review records with no human disposition recorded; the supported B invoice does not remove SR-002. ControlTotals preserves the failed monetary-completeness proposition even though row reconciliation passes.'], ['The synthetic source rows and criterion definitions in file 10 support the arithmetic and matches. The public typology references do not supply a regulatory threshold or evidence of wrongdoing for these fictional accounts.'], ['Review the unexplained match, preserve the invoice explanation without deleting the raw match, and repair the unreadable amount before rerunning the affected account.'], ['Synthetic rules are illustrative and are not regulatory thresholds.', 'Account D has an unknown amount; total monetary completeness is not established.', 'No opening balances or complete external flow paths are supplied.', 'QA remains pending and no authorized human disposition is recorded.']], 'as_of': '2026-09-02T04:00:00Z', 'scope': 'Fictional USD account legs with event instants from 2026-09-01T04:00:00Z inclusive to 2026-09-02T04:00:00Z exclusive. Extraction completeness is asserted only for the ten supplied rows; R10 has an unreadable amount.', 'suite_id': 'transaction-monitoring', 'version': '1.2.0', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'TM-F01', 'proposal': 'Obtain payment purpose and counterparties; refer to the authorized reviewer.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'TM-F02', 'proposal': 'Document the explanation and seek human disposition; retain the rule hit.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'TM-F03', 'proposal': 'Repair the source extract and recompute D before making an account conclusion.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
