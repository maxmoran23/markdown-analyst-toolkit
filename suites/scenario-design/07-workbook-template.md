# Transaction Monitoring Scenario Design — fixed workbook template

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
| EventLedger | `event_id`, `account_id`, `event_utc`, `direction`, `amount`, `currency`, `ownership_state`, `posting_state`, `evidence_ids` |
| PredicateSpec | `predicate_id`, `order`, `field_or_measure`, `operator`, `operand`, `null_result`, `purpose`, `evidence_ids` |
| WindowResults | `window_id`, `account_id`, `anchor_event_id`, `start_utc`, `end_utc`, `event_ids`, `credit_total`, `debit_total`, `ratio`, `first_debit_hours`, `coverage_state`, `rule_result`, `evidence_ids` |
| DeliveryDecisions | `delivery_id`, `window_id`, `raw_result`, `delivery_state`, `group_id`, `reason`, `human_approval`, `evidence_ids` |
| AccountCoverage | `account_id`, `raw_events`, `known_credit_total`, `known_debit_total`, `external_anchor_count`, `window_count`, `coverage_outcome`, `evidence_ids` |
| AcceptanceTests | `test_id`, `test_name`, `expected`, `actual`, `result`, `affected_ids`, `evidence_ids` |
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

DATA = {'slug': 'scenario-design', 'title': 'Transaction Monitoring Scenario Design', 'summary': 'Translate a risk hypothesis into a fully specified, reproducible monitoring rule, with temporal semantics, evidence gates, suppression boundaries and populated acceptance tests.', 'audience': 'Monitoring analysts, scenario owners, data owners and independent control reviewers', 'decision': 'Does the proposed rule implement its stated hypothesis without ambiguous fields, boundary behavior, exclusions or delivery decisions?', 'palette': 'slate', 'as_of': '2026-09-03T04:00:00Z', 'report_sections': ['Proposed rule and acceptance decision', 'Risk hypothesis, source scope and design boundary', 'Design findings and unresolved decisions', 'Predicate and event specification', 'Window outcomes, delivery and acceptance evidence', 'Evidence and authority provenance', 'Proposed design and data actions', 'Limitations, quality gates and human authorization'], 'domain_tables': [{'name': 'EventLedger', 'title': 'Full fictional rule acceptance source', 'columns': ['event_id', 'account_id', 'event_utc', 'direction', 'amount', 'currency', 'ownership_state', 'posting_state', 'evidence_ids'], 'rows': [['E01', 'J', '2026-09-01T13:00:00Z', 'CREDIT', 3000, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E02', 'J', '2026-09-01T14:00:00Z', 'CREDIT', 2000, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E03', 'J', '2026-09-01T15:00:00Z', 'DEBIT', 4500, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E04', 'K', '2026-09-01T13:00:00Z', 'CREDIT', 5000, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E05', 'K', '2026-09-02T13:00:00Z', 'DEBIT', 4500, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E06', 'L', '2026-09-01T13:00:00Z', 'CREDIT', 5000, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E07', 'L', '2026-09-01T15:00:00Z', 'DEBIT', 4499.99, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E08', 'M', '2026-09-01T13:00:00Z', 'CREDIT', 6000, 'USD', 'CONFIRMED_OWN', 'POSTED', 'SD-E01;SD-E02'], ['E09', 'M', '2026-09-01T14:00:00Z', 'DEBIT', 5700, 'USD', 'CONFIRMED_OWN', 'POSTED', 'SD-E01;SD-E02'], ['E10', 'N', '2026-09-01T13:00:00Z', 'CREDIT', 5000, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E11', 'N', '2026-09-01T13:00:00Z', 'DEBIT', 4500, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E12', 'O', '2026-09-01T13:00:00Z', 'CREDIT', 5000, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E13', 'O', '2026-09-01T14:00:00Z', 'DEBIT', None, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01;SD-E03']], 'formats': {'amount': '#,##0.00'}, 'primary_key': ['event_id'], 'column_contracts': {'event_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Immutable synthetic source-event identifier. It survives window expansion and may occur in several window membership lists without becoming another economic event.'}, 'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge.'}, 'event_utc': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant.'}, 'direction': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Canonical CREDIT or DEBIT from the account perspective. Amount remains nonnegative; do not infer direction from a signed display string.'}, 'amount': {'type': 'number', 'nullable': True, 'unit': 'row currency', 'description': 'Known nonnegative monetary amount in the row currency. Null means unrecovered source value and blocks the relevant completeness proposition.'}, 'currency': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount.'}, 'ownership_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Evidence-backed own/external classification for the specific leg and historical period. Unknown ownership is not automatically external or own.'}, 'posting_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Canonical posting status that determines whether a leg enters the declared posted population. A pending item remains visible outside that population.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'grain': 'one unique fictional source event within the complete declared 48-hour interval', 'report_section': 4}, {'name': 'PredicateSpec', 'title': 'Ordered deterministic rule predicates', 'columns': ['predicate_id', 'order', 'field_or_measure', 'operator', 'operand', 'null_result', 'purpose', 'evidence_ids'], 'rows': [['P01', 1, 'data coverage', 'EQUAL', 'COMPLETE', 'NOT_ASSESSABLE', 'Reject relevant missing amount, time, identity or uncovered interval', 'SD-E04'], ['P02', 2, 'posting_state', 'EQUAL', 'POSTED', 'NOT_ASSESSABLE', 'Pending and rejected legs never enter sums', 'SD-E04'], ['P03', 3, 'ownership_state', 'EQUAL', 'EXTERNAL', 'NOT_ASSESSABLE', 'Confirmed own legs excluded; unknown ownership blocks affected window', 'SD-E04'], ['P04', 4, 'event_utc', 'INTERVAL', 'anchor <= t <= anchor + 24 hours', 'NOT_ASSESSABLE', 'Credit-anchored closed window uses normalized UTC instants', 'SD-E04'], ['P05', 5, 'credit_total', 'GREATER_OR_EQUAL', '5000.00 USD', 'NOT_ASSESSABLE', 'Minimum aggregate eligible credits', 'SD-E04'], ['P06', 6, 'debit_total / credit_total', 'GREATER_OR_EQUAL', '0.90', 'NO_MATCH_IF_ZERO_CREDITS', 'Exact comparison before display rounding', 'SD-E04'], ['P07', 7, 'first subsequent debit', 'STRICTLY_AFTER', 'anchor instant', 'NO_MATCH_IF_NONE', 'Same-time debit without sequence is not subsequent', 'SD-E04'], ['P08', 8, 'delivery grouping', 'SAME_ACCOUNT_AND_EVENT_SET', 'same version; same review run', 'NO_GROUP_IF_UNKNOWN', 'Retain raw matches; one delivery group only for exact identical event set', 'SD-E04']], 'formats': {}, 'primary_key': ['predicate_id'], 'column_contracts': {'predicate_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique predicate identifier within the versioned rule. Its declared order controls precedence for blocking defects, exclusions and numeric comparisons.'}, 'order': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Positive integer evaluation precedence. Numeric predicates cannot override an earlier relevant data-completeness failure.'}, 'field_or_measure': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact input field or derived quantity being tested. A business phrase without a computable field mapping does not satisfy this contract.'}, 'operator': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Literal comparison or grouping operation. Inclusive, strict and interval comparisons are deliberately different and must remain explicit.'}, 'operand': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Complete threshold, interval or category against which the predicate compares. Monetary values include currency and durations include elapsed units.'}, 'null_result': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Required branch when input cannot be evaluated. A null-sensitive predicate may block a window rather than defaulting to false or zero.'}, 'purpose': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Bounded reason for the predicate and the mechanism it tests. This is an authored design rationale rather than a legal requirement.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'grain': 'one ordered predicate in RULE-SD-01-v1', 'report_section': 4}, {'name': 'WindowResults', 'title': 'Full anchored calculations and truth states', 'columns': ['window_id', 'account_id', 'anchor_event_id', 'start_utc', 'end_utc', 'event_ids', 'credit_total', 'debit_total', 'ratio', 'first_debit_hours', 'coverage_state', 'rule_result', 'evidence_ids'], 'rows': [['WJ1', 'J', 'E01', '2026-09-01T13:00:00Z', '2026-09-02T13:00:00Z', 'E01;E02;E03', 5000, 4500, 0.9, 2, 'COMPLETE', 'MATCH', 'SD-E01;SD-E04'], ['WJ2', 'J', 'E02', '2026-09-01T14:00:00Z', '2026-09-02T14:00:00Z', 'E02;E03', 2000, 4500, 2.25, 1, 'COMPLETE', 'NO_MATCH', 'SD-E01;SD-E04'], ['WK1', 'K', 'E04', '2026-09-01T13:00:00Z', '2026-09-02T13:00:00Z', 'E04;E05', 5000, 4500, 0.9, 24, 'COMPLETE', 'MATCH', 'SD-E01;SD-E04'], ['WL1', 'L', 'E06', '2026-09-01T13:00:00Z', '2026-09-02T13:00:00Z', 'E06;E07', 5000, 4499.99, 0.899998, 2, 'COMPLETE', 'NO_MATCH', 'SD-E01;SD-E04'], ['WN1', 'N', 'E10', '2026-09-01T13:00:00Z', '2026-09-02T13:00:00Z', 'E10;E11', 5000, 4500, 0.9, None, 'COMPLETE', 'NO_MATCH', 'SD-E01;SD-E04'], ['WO1', 'O', 'E12', '2026-09-01T13:00:00Z', '2026-09-02T13:00:00Z', 'E12;E13', 5000, None, None, 1, 'AMOUNT_UNKNOWN', 'NOT_ASSESSABLE', 'SD-E01;SD-E03;SD-E04']], 'formats': {'credit_total': '#,##0.00', 'debit_total': '#,##0.00', 'ratio': '0.000000', 'first_debit_hours': '0.0'}, 'primary_key': ['window_id'], 'column_contracts': {'window_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable account/anchor/specification window key. It distinguishes overlapping observations so a membership count cannot be mistaken for unique transactions.'}, 'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge.'}, 'anchor_event_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Source eligible credit that starts the specified closed 24-hour window. Same-account membership is explicit and independently reproducible.'}, 'start_utc': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Inclusive UTC instant at the anchor. The applicable window convention determines endpoint inclusion, not the date formatting of the rendered table.'}, 'end_utc': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'UTC endpoint exactly 24 elapsed hours after the anchor. The scenario-design closed interval includes this instant; the TM diagnostic convention matches it.'}, 'event_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited source-event membership in the specific window. Recompute the union separately before calculating unique population movement.'}, 'credit_total': {'type': 'number', 'nullable': False, 'unit': 'row currency', 'description': 'Known eligible or gross credit subtotal as specified by the table grain. It is not necessarily a complete total when coverage_state or population_status is defective.'}, 'debit_total': {'type': 'number', 'nullable': True, 'unit': 'row currency', 'description': 'Known eligible debit subtotal at the table grain. Null is required for a window total dependent on an unknown debit; known subtotals elsewhere remain explicitly partial.'}, 'ratio': {'type': 'number', 'nullable': True, 'unit': 'ratio', 'description': 'Unrounded window debit-to-credit ratio. Null indicates a missing component or no positive denominator; comparisons occur before display rounding.'}, 'first_debit_hours': {'type': 'number', 'nullable': True, 'unit': 'hours', 'description': 'Elapsed hours from anchor to first strictly subsequent eligible debit. Null means no qualifying ordered pair; a contemporaneous debit cannot satisfy the predicate.'}, 'coverage_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Completeness state for the exact account/window inputs. COMPLETE, BOUNDARY_INCOMPLETE and AMOUNT_UNKNOWN cannot be collapsed into a binary risk score.'}, 'rule_result': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Deterministic raw result under the named specification: MATCH, NO_MATCH, EXCLUDED or NOT_ASSESSABLE. Contextual evidence does not rewrite it.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'foreign_keys': [{'columns': ['anchor_event_id'], 'table': 'EventLedger', 'references': ['event_id']}], 'grain': 'one account, eligible credit anchor, currency and rule version', 'report_section': 4}, {'name': 'DeliveryDecisions', 'title': 'Raw result retention and proposed delivery grouping', 'columns': ['delivery_id', 'window_id', 'raw_result', 'delivery_state', 'group_id', 'reason', 'human_approval', 'evidence_ids'], 'rows': [['DL-J1', 'WJ1', 'MATCH', 'PROPOSED_FOR_REVIEW', 'G-J1', 'No earlier identical match; purpose unreviewed', 'NOT_RECORDED', 'SD-E01;SD-E04'], ['DL-J2', 'WJ2', 'NO_MATCH', 'NO_DELIVERY', None, 'Credit total below minimum despite ratio above one', 'NOT_RECORDED', 'SD-E01;SD-E04'], ['DL-K1', 'WK1', 'MATCH', 'PROPOSED_FOR_REVIEW', 'G-K1', 'Exact 24-hour endpoint included', 'NOT_RECORDED', 'SD-E01;SD-E04'], ['DL-L1', 'WL1', 'NO_MATCH', 'NO_DELIVERY', None, '4499.99 / 5000 below .90 before rounding', 'NOT_RECORDED', 'SD-E01;SD-E04'], ['DL-N1', 'WN1', 'NO_MATCH', 'NO_DELIVERY', None, 'No strictly subsequent debit', 'NOT_RECORDED', 'SD-E01;SD-E04'], ['DL-O1', 'WO1', 'NOT_ASSESSABLE', 'DATA_REPAIR_QUEUE', None, 'Debit amount unknown; retain blocked window', 'NOT_RECORDED', 'SD-E03;SD-E04']], 'formats': {}, 'primary_key': ['delivery_id'], 'column_contracts': {'delivery_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique proposal for a window delivery disposition. The record is separate from the raw match so grouping cannot hide a numerical result.'}, 'window_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable account/anchor/specification window key. It distinguishes overlapping observations so a membership count cannot be mistaken for unique transactions.'}, 'raw_result': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Preserved deterministic rule result before human review or delivery grouping. Explanations and grouping decisions must not delete or change it.'}, 'delivery_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Proposed route for a raw outcome: review, no delivery or data repair. It describes the analytical queue decision without performing an external action.'}, 'group_id': {'type': 'text', 'nullable': True, 'unit': 'identifier', 'description': 'Stable proposed delivery-group identifier. Null means the window produces no review group; grouping never erases the underlying result.'}, 'reason': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific evidence-backed reason for a state or transition. It identifies the relevant row, rule or missing fact rather than a generic compliance label.'}, 'human_approval': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Evidence of authorized approval for a design or delivery treatment. NOT_RECORDED is not interchangeable with approved or presumed approved.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'foreign_keys': [{'columns': ['window_id'], 'table': 'WindowResults', 'references': ['window_id']}], 'grain': 'one proposed delivery disposition for a retained raw window result', 'report_section': 5}, {'name': 'AccountCoverage', 'title': 'One row for every source account including excluded accounts', 'columns': ['account_id', 'raw_events', 'known_credit_total', 'known_debit_total', 'external_anchor_count', 'window_count', 'coverage_outcome', 'evidence_ids'], 'rows': [['J', 3, 5000, 4500, 2, 2, 'ASSESSED', 'SD-E01;SD-E04'], ['K', 2, 5000, 4500, 1, 1, 'ASSESSED', 'SD-E01;SD-E04'], ['L', 2, 5000, 4499.99, 1, 1, 'ASSESSED', 'SD-E01;SD-E04'], ['M', 2, 6000, 5700, 0, 0, 'CONFIRMED_OWN_EXCLUDED', 'SD-E01;SD-E02'], ['N', 2, 5000, 4500, 1, 1, 'ASSESSED', 'SD-E01;SD-E04'], ['O', 2, 5000, 0, 1, 1, 'BLOCKED_UNKNOWN_DEBIT', 'SD-E01;SD-E03']], 'formats': {'known_credit_total': '#,##0.00', 'known_debit_total': '#,##0.00'}, 'primary_key': ['account_id'], 'column_contracts': {'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge.'}, 'raw_events': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Count of source events for the account, including excluded and unknown-amount events. It reconciles the retained account frame to the source ledger.'}, 'known_credit_total': {'type': 'number', 'nullable': False, 'unit': 'row currency', 'description': 'Sum of readable credits only at the declared stage, account or observed diagnostic window. The word known is substantive where an unresolved amount exists.'}, 'known_debit_total': {'type': 'number', 'nullable': False, 'unit': 'row currency', 'description': 'Sum of readable debits only at the declared stage, account or observed diagnostic window. An unknown debit is not imputed as a measured zero.'}, 'external_anchor_count': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Number of eligible external credit anchors generated for an account. Confirmed own transfers produce no external-flow anchors.'}, 'window_count': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Count of generated windows for the account, including blocked ones. It is not the count of delivered alerts or unique source legs.'}, 'coverage_outcome': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Account-level outcome that retains excluded and blocked accounts alongside assessed accounts. No-record output is not an acceptable substitute.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'grain': 'one source account, including accounts that generate no external windows', 'report_section': 5}, {'name': 'AcceptanceTests', 'title': 'Explicit specimen test expectations and observed arithmetic', 'columns': ['test_id', 'test_name', 'expected', 'actual', 'result', 'affected_ids', 'evidence_ids'], 'rows': [['AT01', 'All raw events retained', '13', '13', 'PASS', 'E01-E13', 'SD-E01'], ['AT02', 'Raw matching windows', 'WJ1;WK1', 'WJ1;WK1', 'PASS', 'WJ1;WK1', 'SD-E01;SD-E04'], ['AT03', 'Below-ratio boundary', 'WL1 NO_MATCH at .899998', 'WL1 NO_MATCH at .899998', 'PASS', 'WL1', 'SD-E01;SD-E04'], ['AT04', 'Same-time ordering', 'WN1 NO_MATCH', 'WN1 NO_MATCH', 'PASS', 'WN1', 'SD-E01;SD-E04'], ['AT05', 'Missing amount', 'WO1 NOT_ASSESSABLE', 'WO1 NOT_ASSESSABLE', 'PASS', 'WO1', 'SD-E03;SD-E04'], ['AT06', 'Independent operational approval', 'No approval supplied', 'No approval supplied', 'NOT_RECORDED', 'RULE-SD-01-v1', 'SD-E04'], ['AT07', 'Window memberships versus unique events', '13 memberships;11 unique external events', '13 memberships;11 unique external events', 'PASS', 'WJ1;WJ2;WK1;WL1;WN1;WO1', 'SD-E01;SD-E04']], 'formats': {}, 'primary_key': ['test_id'], 'column_contracts': {'test_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique deterministic acceptance-test key. Each test names the affected records and compares a specific expected result to a separately produced actual result.'}, 'test_name': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific acceptance proposition rather than a generic passed label. It names a boundary, count, state or authorization gate.'}, 'expected': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact target result for the named check. This is fixed before execution and may state not supplied when the check concerns authorization.'}, 'actual': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Recorded output of the check. In future sessions, use NOT TESTED until performed; do not copy the specimen result as evidence of a new execution.'}, 'result': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Control result or acceptance state. PASS applies to an executed synthetic check; it is not regulatory assurance or an operational approval.'}, 'affected_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicit source, window or specification keys involved in an acceptance test. Preserve their grain rather than treating every identifier as a transaction.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'grain': 'one explicit deterministic expectation and its authored synthetic actual result', 'report_section': 5}, {'name': 'EvidenceProvenance', 'title': 'Source identity, period, availability and evidential limits', 'columns': ['evidence_id', 'source_kind', 'source_date', 'availability', 'locator', 'supports', 'limitation'], 'rows': [['SD-E01', 'Authored fictional case record', '2026-09-03', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, EventLedger E01-E13; coverage declaration', 'Fictional complete 48-hour event ledger', 'Supports only the stated fictional proposition; no external subject fact or institutional approval'], ['SD-E02', 'Authored fictional case record', '2026-09-03', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, M ownership declaration', 'Fictional common-ownership evidence', 'Supports only the stated fictional proposition; no external subject fact or institutional approval'], ['SD-E03', 'Authored fictional case record', '2026-09-03', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, E13 missing amount notice', 'Fictional extraction exception', 'Supports only the stated fictional proposition; no external subject fact or institutional approval'], ['SD-E04', 'Authored fictional case record', '2026-09-03', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, RULE-SD-01-v1 full specification and acceptance convention', 'Authored illustrative rule specification', 'Supports only the stated fictional proposition; no external subject fact or institutional approval']], 'formats': {}, 'primary_key': ['evidence_id'], 'column_contracts': {'evidence_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Exact unique Evidence key at one source-provenance row. It joins the common Evidence register without combining unrelated sources.'}, 'source_kind': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicitly fictional record type and origin. Authored cases and guidance references must not be mislabeled as actual institutional evidence.'}, 'source_date': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'ISO calendar date of the authored source package, distinct from transaction event dates and evidence retrieval dates.'}, 'availability': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'State of access to the source text. FULL_TEXT_IN_FILE_10 means the complete fictional content is supplied in this suite, not externally verified.'}, 'locator': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact file and section or row reference supporting retrieval of the fictional source. A title alone is insufficient.'}, 'supports': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Bounded proposition the source can establish in the synthetic exercise. It does not certify any broader customer or control conclusion.'}, 'limitation': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific scope restriction or evidential weakness that must accompany use of the source.'}}, 'grain': 'one fictional evidence source with its access state and evidential limit', 'report_section': 5}, {'name': 'ProcessQA', 'title': 'Explicit expected and actual control evidence', 'columns': ['check_id', 'check', 'expected', 'actual', 'status', 'reviewer', 'evidence_ids'], 'rows': [['SQ01', 'Raw matches', 'WJ1 and WK1', 'WJ1 and WK1', 'PASS', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'SD-E01;SD-E04'], ['SQ02', 'Rounding cannot change decision', '.899998 is NO_MATCH', '.899998 is NO_MATCH', 'PASS', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'SD-E01;SD-E04'], ['SQ03', 'Same-time debit', 'WN1 NO_MATCH', 'WN1 NO_MATCH', 'PASS', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'SD-E01;SD-E04'], ['SQ04', 'Unknown amount', 'WO1 remains blocked', 'WO1 remains blocked', 'PASS', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'SD-E03'], ['SQ05', 'Operational approval', 'Not supplied', 'Not supplied', 'NOT RECORDED', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'SD-E04']], 'formats': {}, 'primary_key': ['check_id'], 'column_contracts': {'check_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique process-quality check key retained across output formats. A later rerun creates a dated actual result without changing the original expectation.'}, 'check': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Falsifiable control proposition with defined expected evidence. It must be precise enough for another reviewer to reproduce.'}, 'expected': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact target result for the named check. This is fixed before execution and may state not supplied when the check concerns authorization.'}, 'actual': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Recorded output of the check. In future sessions, use NOT TESTED until performed; do not copy the specimen result as evidence of a new execution.'}, 'status': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Recorded PASS, FAIL, REVIEW REQUIRED, NOT RECORDED or NOT TESTED status for this check, separate from analytical finding severity.'}, 'reviewer': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Identity or role of the actual check performer. The specimen labels authored arithmetic and explicitly records absent independent operational review.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'grain': 'one performed or explicitly unrecorded quality proposition', 'report_section': 5}], 'findings': [{'id': 'SD-F01', 'title': 'Two raw windows meet the authored rule', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SD-E01', 'SD-E04'], 'detail': 'WJ1 and WK1 satisfy the exact predicates. No subject context or operational review outcome has been supplied.', 'recommendation': 'Preserve both raw matches and request authorized review of the proposed specification.'}, {'id': 'SD-F02', 'title': 'One unknown debit blocks a window', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SD-E01', 'SD-E03'], 'detail': 'E13 has unknown amount; WO1 cannot be classified as a clean negative or a numerical match.', 'recommendation': 'Repair E13 and rerun O; retain the original blocked state.'}, {'id': 'SD-F03', 'title': 'Specification tests do not authorize deployment', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SD-E04'], 'detail': 'No institution-specific criteria, independent operating validation or deployment approval is supplied.', 'recommendation': 'Obtain the appropriate human design decision before any operational use.'}], 'evidence': [{'id': 'SD-E01', 'title': 'Fictional complete 48-hour event ledger', 'locator': '10-worked-example.md, EventLedger E01-E13; coverage declaration', 'claim_class': 'Observed'}, {'id': 'SD-E02', 'title': 'Fictional common-ownership evidence', 'locator': '10-worked-example.md, M ownership declaration', 'claim_class': 'Observed'}, {'id': 'SD-E03', 'title': 'Fictional extraction exception', 'locator': '10-worked-example.md, E13 missing amount notice', 'claim_class': 'Observed'}, {'id': 'SD-E04', 'title': 'Authored illustrative rule specification', 'locator': '10-worked-example.md, RULE-SD-01-v1 full specification and acceptance convention', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Raw events', 'value': 13, 'method': 'Count E01 through E13, including one unknown amount', 'format': '#,##0'}, {'label': 'Anchored windows', 'value': 6, 'method': 'Two J anchors plus one K, L, N and O anchor; M excluded', 'format': '#,##0'}, {'label': 'Raw matches', 'value': 2, 'method': 'WJ1 and WK1; no contextual disposition implied', 'format': '#,##0'}, {'label': 'Known gross movement USD', 'value': 54699.99, 'method': '31000 credits plus 23699.99 known debits; E13 unknown', 'format': '$#,##0.00'}], 'limitations': ['All parameters are authored synthetic controls, not approved institutional thresholds.', 'One unknown amount prevents complete gross movement and O assessment.', 'Passing design cases is not a measure of detection recall, precision or production performance.'], 'report_narrative': [['The authored credit-anchored rule yields two raw matching windows, three complete nonmatching windows and one blocked window. Its specification can be reviewed, but deployment authorization is absent.'], ['The complete fictional source covers Sep 01, 2026 12:00 AM ET to Sep 03, 2026 12:00 AM ET exclusive. Thirteen events cover six accounts. M is retained as a confirmed own-transfer exclusion; O has one unknown amount.'], ['J and K meet the exact authored predicates. L fails at an unrounded .899998 ratio even though one-decimal percentage display rounds to 90.0%. N fails strict temporal ordering. O requires data repair.'], ['PredicateSpec fixes data completeness, posting and ownership eligibility, closed 24-hour credit-anchored windows, inclusive USD 5000 and .90 thresholds, strict subsequent-debit timing, and limited exact-set delivery grouping. EventLedger retains every source event.'], ['WindowResults contains six windows and thirteen membership entries over eleven distinct external events. AccountCoverage retains the excluded M account. DeliveryDecisions retains raw states and no human approval. AcceptanceTests records arithmetic checks separately from unrecorded authorization.'], ['All subject facts are fictional and located in file 10. Public FFIEC and Wolfsberg references support control-design context and do not endorse these parameters.'], ['Repair E13; review rule scope, intended risks and untested mechanics; obtain an actual design decision. Do not automatically send alerts, change thresholds or apply suppression.'], ['Known gross movement is $54,699.99, with E13 unknown. No production performance, complete monetary coverage, institutional approval or customer conclusion is established.']], 'conclusion': 'The authored credit-anchored rule yields two raw matching windows, three complete nonmatching windows and one blocked window. Its specification can be reviewed, but deployment authorization is absent.', 'suite_id': 'scenario-design', 'version': '1.2.0', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'SD-F01', 'proposal': 'Preserve both raw matches and request authorized review of the proposed specification.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'SD-F02', 'proposal': 'Repair E13 and rerun O; retain the original blocked state.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'SD-F03', 'proposal': 'Obtain the appropriate human design decision before any operational use.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
