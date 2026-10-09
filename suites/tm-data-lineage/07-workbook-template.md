# Transaction Monitoring Data Lineage — fixed workbook template

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
| SourceRows | `raw_row_id`, `transaction_id`, `account_id`, `event_utc`, `ingest_utc`, `source_direction`, `amount_text`, `currency`, `source_status`, `source_version`, `reversal_of`, `evidence_ids` |
| FieldMappings | `mapping_id`, `source_field`, `target_field`, `transformation`, `failure_state`, `test_locator`, `evidence_ids` |
| LineageLedger | `lineage_id`, `raw_row_id`, `canonical_id`, `terminal_state`, `reason`, `run_id`, `evidence_ids` |
| CanonicalOutput | `canonical_id`, `raw_row_id`, `transaction_id`, `account_id`, `event_utc`, `direction`, `amount`, `currency`, `run_id`, `evidence_ids` |
| StageControls | `control_id`, `stage`, `currency`, `row_count`, `known_credit_total`, `known_debit_total`, `unknown_amount_count`, `interpretation`, `evidence_ids` |
| RunImpact | `impact_id`, `account_id`, `currency`, `run0_credit`, `run0_debit`, `run0_state`, `run1_credit`, `run1_debit`, `run1_state`, `change_reason`, `evidence_ids` |
| ExceptionRegister | `exception_id`, `account_id`, `source_rows`, `exception_type`, `affected_claim`, `required_evidence`, `repair_state`, `evidence_ids` |
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

DATA = {'slug': 'tm-data-lineage', 'title': 'Transaction Monitoring Data Lineage', 'summary': 'Reconcile source-to-monitoring transformations, population counts, currency totals, exceptions and late-change effects with a complete row-level lineage specimen.', 'audience': 'Monitoring analysts, scenario owners, data owners and independent control reviewers', 'decision': 'Can a reviewer reproduce which source records reached monitoring, which did not, and exactly how a correction changes the downstream assessment?', 'palette': 'slate', 'as_of': '2026-09-02T12:00:00Z', 'report_sections': ['Lineage conclusion and unresolved coverage', 'Source scope, cutoffs and transformation contract', 'Defects, exclusions and downstream consequences', 'Source-to-canonical row lineage', 'Stage controls and rerun impact', 'Evidence and transformation provenance', 'Proposed repair and reprocessing actions', 'Limitations, quality gates and acceptance'], 'domain_tables': [{'name': 'SourceRows', 'title': 'Immutable delivered source records', 'columns': ['raw_row_id', 'transaction_id', 'account_id', 'event_utc', 'ingest_utc', 'source_direction', 'amount_text', 'currency', 'source_status', 'source_version', 'reversal_of', 'evidence_ids'], 'rows': [['X01', 'TX01', 'LA', '2026-09-01T13:00:00Z', '2026-09-01T13:05:00Z', 'C', '6000.00', 'USD', 'P', '1', None, 'LN-E01'], ['X02', 'TX02', 'LA', '2026-09-01T14:00:00Z', '2026-09-01T14:05:00Z', 'D', '5400.00', 'USD', 'P', '1', None, 'LN-E01'], ['X03', 'TX01', 'LA', '2026-09-01T13:00:00Z', '2026-09-01T15:00:00Z', 'C', '6000.00', 'USD', 'P', '1', None, 'LN-E01'], ['X04', 'TX03', 'LB', '2026-09-01T13:00:00Z', '2026-09-01T13:05:00Z', 'C', '5000.00', 'USD', 'P', '1', None, 'LN-E01'], ['X05', 'TX04', 'LB', '2026-09-01T14:00:00Z', '2026-09-01T14:05:00Z', 'D', '4500.00', 'USD', 'P', '1', None, 'LN-E01'], ['X06', 'TX05', 'LC', '2026-09-01T13:00:00Z', '2026-09-01T13:05:00Z', 'C', '2000.00', 'USD', 'P', '1', None, 'LN-E01'], ['X07', 'TX05', 'LC', '2026-09-01T13:00:00Z', '2026-09-01T13:06:00Z', 'C', '2200.00', 'USD', 'P', '1', None, 'LN-E01;LN-E02'], ['X08', 'TX06', 'LC', '2026-09-01T14:00:00Z', '2026-09-01T14:05:00Z', 'D', '1000.00', 'USD', 'P', '1', None, 'LN-E01'], ['X09', 'TX07', 'LD', '2026-09-01T13:00:00Z', '2026-09-01T13:05:00Z', 'C', '7000.00', 'USD', 'N', '1', None, 'LN-E01'], ['X10', 'TX08', 'LE', '2026-09-01T13:00:00Z', '2026-09-01T13:05:00Z', 'C', '3000.00', 'USD', 'P', '1', None, 'LN-E01'], ['X11', 'TX09', 'LE', '2026-09-01T14:00:00Z', '2026-09-01T14:05:00Z', 'D', '3000.00', 'USD', 'R', '1', 'TX08', 'LN-E01;LN-E03'], ['X12', 'TX10', 'LF', '2026-09-01T23:30:00Z', '2026-09-02T10:00:00Z', 'C', '4000.00', 'USD', 'P', '1', None, 'LN-E01;LN-E04'], ['X13', 'TX11', 'LF', '2026-09-02T00:00:00Z', '2026-09-02T00:05:00Z', 'D', '3600.00', 'USD', 'P', '1', None, 'LN-E01'], ['X14', 'TX12', 'LG', '2026-09-01T13:00:00Z', '2026-09-01T13:05:00Z', 'C', 'unreadable', 'USD', 'P', '1', None, 'LN-E01;LN-E05'], ['X15', 'TX13', 'LH', '2026-09-01T13:00:00Z', '2026-09-01T13:05:00Z', 'C', '1000.00', 'EUR', 'P', '1', None, 'LN-E01']], 'formats': {}, 'primary_key': ['raw_row_id'], 'column_contracts': {'raw_row_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable.'}, 'transaction_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Source economic transaction identifier. Its uniqueness is assessed with account leg and source version; matching amount or narrative alone is insufficient.'}, 'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge.'}, 'event_utc': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant.'}, 'ingest_utc': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'UTC instant at which the source record became available to the monitoring feed. It controls run visibility separately from economic event-period inclusion.'}, 'source_direction': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Unmodified source C or D code. The explicit mapping defines direction; unmapped codes require an exception and cannot be guessed.'}, 'amount_text': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact source amount string before parsing. It can contain unreadable text; preserve it as evidence and never sum it directly.'}, 'currency': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount.'}, 'source_status': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Original status code before mapping. P is posted, N pending and R a posted reversal under this particular source contract.'}, 'source_version': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Source-declared record version as text. Later ingestion alone is not evidence of a later authoritative version when this value is unchanged.'}, 'reversal_of': {'type': 'text', 'nullable': True, 'unit': 'text', 'description': 'Original source transaction key for a posted reversal. Null means no link supplied; do not fabricate a relation from equal and opposite amounts.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'grain': 'one immutable raw delivered feed record, including later-unavailable and exceptional records', 'report_section': 4}, {'name': 'FieldMappings', 'title': 'Source-to-canonical transformations and rejection behavior', 'columns': ['mapping_id', 'source_field', 'target_field', 'transformation', 'failure_state', 'test_locator', 'evidence_ids'], 'rows': [['MAP01', 'transaction_id + account_id + source_version', 'canonical identity', 'Exact text tuple; currency and amount are compared payload, not identity', 'CONFLICT if same tuple differs', 'X06 and X07', 'LN-E06'], ['MAP02', 'event_utc', 'event instant', 'Parse timezone-aware ISO timestamp; normalize UTC without changing instant', 'UNPARSED_TIME', 'X12 and X13 are previous ET business date', 'LN-E06'], ['MAP03', 'source_direction', 'direction', 'C -> CREDIT; D -> DEBIT; no other mapping', 'UNMAPPED_DIRECTION', 'X01 C; X02 D', 'LN-E06'], ['MAP04', 'amount_text', 'amount', 'Decimal nonnegative; retain original string; no thousands separator guessing', 'UNPARSED_AMOUNT', 'X14 unreadable', 'LN-E06'], ['MAP05', 'source_status', 'posting_state', 'P -> POSTED; N -> PENDING; R -> REVERSAL_POSTED', 'UNMAPPED_STATUS', 'X09 pending; X11 linked reversal', 'LN-E06'], ['MAP06', 'currency', 'currency', 'Preserve uppercase ISO code; no conversion in this case', 'UNKNOWN_CURRENCY', 'X15 EUR stays EUR', 'LN-E06'], ['MAP07', 'reversal_of', 'reversal link', 'Resolve original same-account transaction and exact amount/currency before paired exclusion', 'UNRESOLVED_REVERSAL', 'X11 refers TX08 at LE, USD 3000', 'LN-E03;LN-E06'], ['MAP08', 'ingest_utc', 'cutoff eligibility', 'Include if ingest instant <= run cutoff; apply event scope separately', 'LATE_DEFERRED', 'X12 appears only in rerun', 'LN-E04;LN-E06']], 'formats': {}, 'primary_key': ['mapping_id'], 'column_contracts': {'mapping_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique source-to-canonical transformation identifier. It separates the mapping definition from actual row-level transformation outcomes.'}, 'source_field': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Source column or explicit compound key consumed by a mapping. The original source text remains retrievable after transformation.'}, 'target_field': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Named canonical concept produced by the mapping. A transformed concept may require several source columns and has its own validation gate.'}, 'transformation': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Complete authored transformation rule for the supplied source. It specifies value mapping, precision and failure behavior without assuming vendor implementation.'}, 'failure_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Required exception category when the mapping cannot be applied. It must propagate to downstream affected windows rather than silently dropping records.'}, 'test_locator': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact fictional source examples that exercise the mapping. These are sufficient to reproduce this specimen, not a complete production validation dataset.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'grain': 'one explicit source-to-canonical transformation with its failure branch', 'report_section': 4}, {'name': 'LineageLedger', 'title': 'Every source row to one initial terminal state', 'columns': ['lineage_id', 'raw_row_id', 'canonical_id', 'terminal_state', 'reason', 'run_id', 'evidence_ids'], 'rows': [['LIN-X01', 'X01', 'CL01', 'CANONICAL', 'Unique readable posted leg available by initial cutoff', 'RUN0', 'LN-E01;LN-E06'], ['LIN-X02', 'X02', 'CL02', 'CANONICAL', 'Unique readable posted leg available by initial cutoff', 'RUN0', 'LN-E01;LN-E06'], ['LIN-X03', 'X03', 'CL01', 'DUPLICATE', 'Same economic tuple and payload as X01; later extraction metadata only', 'RUN0', 'LN-E01;LN-E06'], ['LIN-X04', 'X04', 'CL03', 'CANONICAL', 'Unique readable posted leg available by initial cutoff', 'RUN0', 'LN-E01;LN-E06'], ['LIN-X05', 'X05', 'CL04', 'CANONICAL', 'Unique readable posted leg available by initial cutoff', 'RUN0', 'LN-E01;LN-E06'], ['LIN-X06', 'X06', None, 'CONFLICT', 'Same TX05 identity; conflicting amount; neither selected', 'RUN0', 'LN-E01;LN-E06'], ['LIN-X07', 'X07', None, 'CONFLICT', 'Same TX05 identity; conflicting amount; neither selected', 'RUN0', 'LN-E01;LN-E02;LN-E06'], ['LIN-X08', 'X08', 'CL05', 'CANONICAL', 'Unique readable posted leg available by initial cutoff', 'RUN0', 'LN-E01;LN-E06'], ['LIN-X09', 'X09', None, 'PENDING', 'Not posted at supplied status; retain outside posted ledger', 'RUN0', 'LN-E01;LN-E06'], ['LIN-X10', 'X10', None, 'REVERSAL_PAIR', 'Exact linked original and reversal preserved but netted out of external-flow scenario', 'RUN0', 'LN-E01;LN-E06'], ['LIN-X11', 'X11', None, 'REVERSAL_PAIR', 'Exact linked original and reversal preserved but netted out of external-flow scenario', 'RUN0', 'LN-E01;LN-E03;LN-E06'], ['LIN-X12', 'X12', None, 'LATE_DEFERRED', 'Event in period, ingestion after initial cutoff; add only in rerun', 'RUN0', 'LN-E01;LN-E04;LN-E06'], ['LIN-X13', 'X13', 'CL06', 'CANONICAL', 'Unique readable posted leg available by initial cutoff', 'RUN0', 'LN-E01;LN-E06'], ['LIN-X14', 'X14', None, 'UNPARSED_AMOUNT', 'Posted amount cannot be recovered; LG blocked', 'RUN0', 'LN-E01;LN-E05;LN-E06'], ['LIN-X15', 'X15', 'CL07', 'CANONICAL', 'Unique readable posted leg available by initial cutoff', 'RUN0', 'LN-E01;LN-E06']], 'formats': {}, 'primary_key': ['lineage_id'], 'column_contracts': {'lineage_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique link between a raw source row and its initial disposition. Each raw row appears once even when it maps to an already retained canonical leg.'}, 'raw_row_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable.'}, 'canonical_id': {'type': 'text', 'nullable': True, 'unit': 'identifier', 'description': 'Unique canonical output identifier or explicit null for a noncanonical row. A duplicate may point to an existing canonical identifier without adding a row.'}, 'terminal_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exactly one initial row disposition for conservation. CANONICAL, DUPLICATE, CONFLICT, PENDING, REVERSAL_PAIR, LATE_DEFERRED and UNPARSED_AMOUNT partition the source.'}, 'reason': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific evidence-backed reason for a state or transition. It identifies the relevant row, rule or missing fact rather than a generic compliance label.'}, 'run_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Snapshot identity with a fixed ingestion cutoff. RUN0 and RUN1 differ in available source information; neither is silently overwritten.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'foreign_keys': [{'columns': ['raw_row_id'], 'table': 'SourceRows', 'references': ['raw_row_id']}], 'grain': 'one raw source row and its initial RUN0 terminal disposition', 'report_section': 4}, {'name': 'CanonicalOutput', 'title': 'Known unique posted legs at initial cutoff', 'columns': ['canonical_id', 'raw_row_id', 'transaction_id', 'account_id', 'event_utc', 'direction', 'amount', 'currency', 'run_id', 'evidence_ids'], 'rows': [['CL01', 'X01', 'TX01', 'LA', '2026-09-01T13:00:00Z', 'CREDIT', 6000.0, 'USD', 'RUN0', 'LN-E01'], ['CL02', 'X02', 'TX02', 'LA', '2026-09-01T14:00:00Z', 'DEBIT', 5400.0, 'USD', 'RUN0', 'LN-E01'], ['CL03', 'X04', 'TX03', 'LB', '2026-09-01T13:00:00Z', 'CREDIT', 5000.0, 'USD', 'RUN0', 'LN-E01'], ['CL04', 'X05', 'TX04', 'LB', '2026-09-01T14:00:00Z', 'DEBIT', 4500.0, 'USD', 'RUN0', 'LN-E01'], ['CL05', 'X08', 'TX06', 'LC', '2026-09-01T14:00:00Z', 'DEBIT', 1000.0, 'USD', 'RUN0', 'LN-E01'], ['CL06', 'X13', 'TX11', 'LF', '2026-09-02T00:00:00Z', 'DEBIT', 3600.0, 'USD', 'RUN0', 'LN-E01'], ['CL07', 'X15', 'TX13', 'LH', '2026-09-01T13:00:00Z', 'CREDIT', 1000.0, 'EUR', 'RUN0', 'LN-E01']], 'formats': {'amount': '#,##0.00'}, 'primary_key': ['canonical_id'], 'column_contracts': {'canonical_id': {'type': 'text', 'nullable': True, 'unit': 'identifier', 'description': 'Unique canonical output identifier or explicit null for a noncanonical row. A duplicate may point to an existing canonical identifier without adding a row.'}, 'raw_row_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable.'}, 'transaction_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Source economic transaction identifier. Its uniqueness is assessed with account leg and source version; matching amount or narrative alone is insufficient.'}, 'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge.'}, 'event_utc': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant.'}, 'direction': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Canonical CREDIT or DEBIT from the account perspective. Amount remains nonnegative; do not infer direction from a signed display string.'}, 'amount': {'type': 'number', 'nullable': True, 'unit': 'row currency', 'description': 'Known nonnegative monetary amount in the row currency. Null means unrecovered source value and blocks the relevant completeness proposition.'}, 'currency': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount.'}, 'run_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Snapshot identity with a fixed ingestion cutoff. RUN0 and RUN1 differ in available source information; neither is silently overwritten.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'foreign_keys': [{'columns': ['raw_row_id'], 'table': 'SourceRows', 'references': ['raw_row_id']}], 'grain': 'one known unique posted account leg available at RUN0 and surviving declared exclusions', 'report_section': 5}, {'name': 'StageControls', 'title': 'Counts and known amounts by stage and currency', 'columns': ['control_id', 'stage', 'currency', 'row_count', 'known_credit_total', 'known_debit_total', 'unknown_amount_count', 'interpretation', 'evidence_ids'], 'rows': [['LC01', 'Delivered raw', 'USD', 14, 35200, 17500, 1, 'Raw contains duplicate, conflicting alternatives, pending and reversal; not economic total', 'LN-E01'], ['LC02', 'Delivered raw', 'EUR', 1, 1000, 0, 0, 'Separate currency; not added to USD', 'LN-E01'], ['LC03', 'RUN0 canonical', 'USD', 6, 11000, 14500, 0, 'Known partial posted population; LC conflict, LF late, LG unknown remain blocked', 'LN-E01;LN-E06'], ['LC04', 'RUN0 canonical', 'EUR', 1, 1000, 0, 0, 'Preserved EUR leg; USD scenario exclusion separately disclosed', 'LN-E01;LN-E06'], ['LC05', 'RUN1 canonical', 'USD', 7, 15000, 14500, 0, 'Adds X12 USD 4000 credit; unresolved conflict and parse defect remain', 'LN-E04;LN-E06'], ['LC06', 'RUN1 canonical', 'EUR', 1, 1000, 0, 0, 'EUR unchanged', 'LN-E01;LN-E06']], 'formats': {'known_credit_total': '#,##0.00', 'known_debit_total': '#,##0.00'}, 'primary_key': ['control_id'], 'column_contracts': {'control_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique reconciliation-control key. Controls can test different grains; counts and monetary comparisons are never combined into one unexplained balance.'}, 'stage': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Named source or canonical pipeline layer and run. Its grain must be checked before interpreting totals because raw rows include non-economic duplicates.'}, 'currency': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount.'}, 'row_count': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Number of records in the named stage and currency. This is counted independently of known amounts and can include unreadable monetary rows.'}, 'known_credit_total': {'type': 'number', 'nullable': False, 'unit': 'row currency', 'description': 'Sum of readable credits only at the declared stage, account or observed diagnostic window. The word known is substantive where an unresolved amount exists.'}, 'known_debit_total': {'type': 'number', 'nullable': False, 'unit': 'row currency', 'description': 'Sum of readable debits only at the declared stage, account or observed diagnostic window. An unknown debit is not imputed as a measured zero.'}, 'unknown_amount_count': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Count of stage records whose amount is not numeric. It does not measure uncertain amount ranges or conflicted values unless explicitly stated.'}, 'interpretation': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific limitation on the control total, including duplicate/conflict effects or incomplete economic coverage. It travels with the number in every output.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'grain': 'one pipeline layer, run and currency control population', 'report_section': 5}, {'name': 'RunImpact', 'title': 'Account assessment changes after known late arrival', 'columns': ['impact_id', 'account_id', 'currency', 'run0_credit', 'run0_debit', 'run0_state', 'run1_credit', 'run1_debit', 'run1_state', 'change_reason', 'evidence_ids'], 'rows': [['IMP-A', 'LA', 'USD', 6000, 5400, 'MATCH', 6000, 5400, 'MATCH', 'No source change', 'LN-E01;LN-E06'], ['IMP-B', 'LB', 'USD', 5000, 4500, 'MATCH', 5000, 4500, 'MATCH', 'No source change', 'LN-E01;LN-E06'], ['IMP-C', 'LC', 'USD', 0, 1000, 'NOT_ASSESSABLE', 0, 1000, 'NOT_ASSESSABLE', 'TX05 conflict unresolved; credit zero means known subtotal only', 'LN-E02;LN-E06'], ['IMP-D', 'LD', 'USD', 0, 0, 'NO_POSTED_ACTIVITY', 0, 0, 'NO_POSTED_ACTIVITY', 'Pending source retained; no posted leg', 'LN-E01;LN-E06'], ['IMP-E', 'LE', 'USD', 0, 0, 'REVERSAL_PAIR_EXCLUDED', 0, 0, 'REVERSAL_PAIR_EXCLUDED', 'Original and reversal retained outside illustrative flow totals', 'LN-E03;LN-E06'], ['IMP-F', 'LF', 'USD', 0, 3600, 'NOT_ASSESSABLE', 4000, 3600, 'NO_MATCH', 'Late credit repaired; ratio .90 but 4000 below illustrative 5000 minimum', 'LN-E04;LN-E06'], ['IMP-G', 'LG', 'USD', 0, 0, 'NOT_ASSESSABLE', 0, 0, 'NOT_ASSESSABLE', 'Unknown posted credit remains; zeros are known subtotals', 'LN-E05;LN-E06'], ['IMP-H', 'LH', 'EUR', 1000, 0, 'CURRENCY_EXCLUDED', 1000, 0, 'CURRENCY_EXCLUDED', 'USD-only rule; EUR preserved in lineage', 'LN-E01;LN-E06']], 'formats': {'run0_credit': '#,##0.00', 'run0_debit': '#,##0.00', 'run1_credit': '#,##0.00', 'run1_debit': '#,##0.00'}, 'primary_key': ['impact_id'], 'column_contracts': {'impact_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable account/currency change-comparison key. It connects prior and rerun states without presenting the new state as the original conclusion.'}, 'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge.'}, 'currency': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount.'}, 'run0_credit': {'type': 'number', 'nullable': False, 'unit': 'row currency', 'description': 'Known initial-run credit subtotal in row currency. A zero on a blocked account is a known subtotal only and cannot prove no credits exist.'}, 'run0_debit': {'type': 'number', 'nullable': False, 'unit': 'row currency', 'description': 'Known initial-run debit subtotal in row currency. Reversal exclusions and missing records are documented separately.'}, 'run0_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Initial downstream assessment after all source defects known to the case are propagated. A known unavailable event makes the account incomplete.'}, 'run1_credit': {'type': 'number', 'nullable': False, 'unit': 'row currency', 'description': 'Known rerun credit subtotal after the declared late event becomes available. Unrelated unresolved defects are not repaired by this increase.'}, 'run1_debit': {'type': 'number', 'nullable': False, 'unit': 'row currency', 'description': 'Known rerun debit subtotal under the same scope and transformation rules. Its equality to RUN0 is a checked result rather than an assumption.'}, 'run1_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Downstream assessment at the later cutoff with the same illustrative predicates. State changes require an explicit source or criteria delta.'}, 'change_reason': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact source delta explaining a before/after result. It distinguishes improved completeness from changed risk or changed threshold.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'grain': 'one account and currency compared across RUN0 and RUN1', 'report_section': 5}, {'name': 'ExceptionRegister', 'title': 'Specific defects and required repair evidence', 'columns': ['exception_id', 'account_id', 'source_rows', 'exception_type', 'affected_claim', 'required_evidence', 'repair_state', 'evidence_ids'], 'rows': [['EX01', 'LC', 'X06;X07', 'CONFLICT', 'Credit amount and LC rule outcome', 'Authoritative TX05 version history and amount; do not choose maximum', 'OPEN', 'LN-E02'], ['EX02', 'LF', 'X12', 'LATE_ARRIVAL', 'Initial completeness and LF timing', 'RUN1 ingest receipt and complete lag population', 'RERUN_REPRODUCED', 'LN-E04'], ['EX03', 'LG', 'X14', 'UNPARSED_AMOUNT', 'Credit total and LG rule outcome', 'Corrected signed source extract and source amount control', 'OPEN', 'LN-E05'], ['EX04', 'LE', 'X10;X11', 'REVERSAL_TREATMENT', 'Difference between posting gross and illustrative external flow', 'Exact reversal link, currency and amount, plus stated exclusion convention', 'DOCUMENTED_ONLY', 'LN-E03;LN-E06']], 'formats': {}, 'primary_key': ['exception_id'], 'column_contracts': {'exception_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique source-defect or controlled-treatment record. Exceptions retain their evidence and cannot be closed merely because a rerun finished.'}, 'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge.'}, 'source_rows': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited raw-row keys contributing to the exception. Each referenced row remains in the immutable source and lineage registers.'}, 'exception_type': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific conflict, late-arrival, unreadable-amount or reversal-treatment category. Categories drive different repair and retest requirements.'}, 'affected_claim': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Analytical statement that cannot be supported, or changes meaning, because of the exception. This connects technical defects to monitoring consequences.'}, 'required_evidence': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Concrete source-owner evidence needed to resolve or verify the exception. A verbal assurance does not substitute for the named record.'}, 'repair_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Actual evidence state of repair in the specimen. OPEN remains unresolved, RERUN_REPRODUCED verifies the illustrated rerun, DOCUMENTED_ONLY is not operational acceptance.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'grain': 'one specific defect or documented controlled treatment and its repair evidence', 'report_section': 5}, {'name': 'EvidenceProvenance', 'title': 'Source identity, period, availability and evidential limits', 'columns': ['evidence_id', 'source_kind', 'source_date', 'availability', 'locator', 'supports', 'limitation'], 'rows': [['LN-E01', 'Authored fictional case record', '2026-09-02', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, SourceRows X01-X15; source manifest', 'Fictional delivered feed', 'Supports only the stated fictional proposition; no external subject fact or institutional approval'], ['LN-E02', 'Authored fictional case record', '2026-09-02', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, TX05 conflict declaration', 'Fictional conflict notice', 'Supports only the stated fictional proposition; no external subject fact or institutional approval'], ['LN-E03', 'Authored fictional case record', '2026-09-02', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, TX08/TX09 reversal declaration', 'Fictional exact reversal link', 'Supports only the stated fictional proposition; no external subject fact or institutional approval'], ['LN-E04', 'Authored fictional case record', '2026-09-02', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, X12 cutoff declaration and RUN1 receipt', 'Fictional late-arrival notice', 'Supports only the stated fictional proposition; no external subject fact or institutional approval'], ['LN-E05', 'Authored fictional case record', '2026-09-02', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, X14 parse-defect declaration', 'Fictional unreadable amount', 'Supports only the stated fictional proposition; no external subject fact or institutional approval'], ['LN-E06', 'Authored fictional case record', '2026-09-02', 'FULL_TEXT_IN_FILE_10', '10-worked-example.md, FieldMappings, run cutoffs and illustrative TM-01 predicates', 'Authored transformation and downstream rule', 'Supports only the stated fictional proposition; no external subject fact or institutional approval']], 'formats': {}, 'primary_key': ['evidence_id'], 'column_contracts': {'evidence_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Exact unique Evidence key at one source-provenance row. It joins the common Evidence register without combining unrelated sources.'}, 'source_kind': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicitly fictional record type and origin. Authored cases and guidance references must not be mislabeled as actual institutional evidence.'}, 'source_date': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'ISO calendar date of the authored source package, distinct from transaction event dates and evidence retrieval dates.'}, 'availability': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'State of access to the source text. FULL_TEXT_IN_FILE_10 means the complete fictional content is supplied in this suite, not externally verified.'}, 'locator': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact file and section or row reference supporting retrieval of the fictional source. A title alone is insufficient.'}, 'supports': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Bounded proposition the source can establish in the synthetic exercise. It does not certify any broader customer or control conclusion.'}, 'limitation': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific scope restriction or evidential weakness that must accompany use of the source.'}}, 'grain': 'one fictional evidence source with its access state and evidential limit', 'report_section': 5}, {'name': 'ProcessQA', 'title': 'Explicit expected and actual control evidence', 'columns': ['check_id', 'check', 'expected', 'actual', 'status', 'reviewer', 'evidence_ids'], 'rows': [['LQ01', 'Initial terminal conservation', '15 = 7 + 1 + 2 + 1 + 2 + 1 + 1', '15 = 7 + 1 + 2 + 1 + 2 + 1 + 1', 'PASS', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'LN-E01;LN-E06'], ['LQ02', 'RUN1 known USD gross', '29500.00', '29500.00', 'PASS', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'LN-E01;LN-E04'], ['LQ03', 'Distinct currencies', 'USD and EUR separate', 'USD and EUR separate', 'PASS', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'LN-E01'], ['LQ04', 'Conflict not selected', 'X06 and X07 both quarantined', 'X06 and X07 both quarantined', 'PASS', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'LN-E02'], ['LQ05', 'Independent acceptance', 'Not supplied', 'Not supplied', 'NOT RECORDED', 'Authored specimen arithmetic; independent operational reviewer not supplied', 'LN-E06']], 'formats': {}, 'primary_key': ['check_id'], 'column_contracts': {'check_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique process-quality check key retained across output formats. A later rerun creates a dated actual result without changing the original expectation.'}, 'check': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Falsifiable control proposition with defined expected evidence. It must be precise enough for another reviewer to reproduce.'}, 'expected': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact target result for the named check. This is fixed before execution and may state not supplied when the check concerns authorization.'}, 'actual': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Recorded output of the check. In future sessions, use NOT TESTED until performed; do not copy the specimen result as evidence of a new execution.'}, 'status': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Recorded PASS, FAIL, REVIEW REQUIRED, NOT RECORDED or NOT TESTED status for this check, separate from analytical finding severity.'}, 'reviewer': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Identity or role of the actual check performer. The specimen labels authored arithmetic and explicitly records absent independent operational review.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation.'}}, 'grain': 'one performed or explicitly unrecorded quality proposition', 'report_section': 5}], 'findings': [{'id': 'LN-F01', 'title': 'Conflicting versions block LC', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['LN-E01', 'LN-E02'], 'detail': 'X06 and X07 share the TX05 identity but disagree between USD 2000 and USD 2200; neither is selected. LC remains not assessable.', 'recommendation': 'Obtain an authoritative version history, resolve TX05 and rerun every affected window.'}, {'id': 'LN-F02', 'title': 'Known late credit changes LF assessment', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['LN-E01', 'LN-E04', 'LN-E06'], 'detail': 'RUN1 adds X12 USD 4000 credit. LF changes from not assessable to no match because .90 satisfies the ratio but USD 4000 fails the credit minimum.', 'recommendation': 'Preserve RUN0 and RUN1 and verify the wider lag population before accepting complete coverage.'}, {'id': 'LN-F03', 'title': 'Unreadable posted credit remains unresolved', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['LN-E01', 'LN-E05'], 'detail': 'X14 amount is unknown; LG contributes no known amount but cannot be treated as a zero-activity negative.', 'recommendation': 'Request corrected source evidence and reconcile the replacement to source totals.'}], 'evidence': [{'id': 'LN-E01', 'title': 'Fictional delivered feed', 'locator': '10-worked-example.md, SourceRows X01-X15; source manifest', 'claim_class': 'Observed'}, {'id': 'LN-E02', 'title': 'Fictional conflict notice', 'locator': '10-worked-example.md, TX05 conflict declaration', 'claim_class': 'Observed'}, {'id': 'LN-E03', 'title': 'Fictional exact reversal link', 'locator': '10-worked-example.md, TX08/TX09 reversal declaration', 'claim_class': 'Observed'}, {'id': 'LN-E04', 'title': 'Fictional late-arrival notice', 'locator': '10-worked-example.md, X12 cutoff declaration and RUN1 receipt', 'claim_class': 'Observed'}, {'id': 'LN-E05', 'title': 'Fictional unreadable amount', 'locator': '10-worked-example.md, X14 parse-defect declaration', 'claim_class': 'Observed'}, {'id': 'LN-E06', 'title': 'Authored transformation and downstream rule', 'locator': '10-worked-example.md, FieldMappings, run cutoffs and illustrative TM-01 predicates', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Delivered rows', 'value': 15, 'method': 'Count X01-X15 including post-cutoff record', 'format': '#,##0'}, {'label': 'Initial canonical rows', 'value': 7, 'method': 'Six USD plus one EUR known unique posted leg', 'format': '#,##0'}, {'label': 'Rerun canonical rows', 'value': 8, 'method': 'RUN0 seven plus late X12; unresolved defects unchanged', 'format': '#,##0'}, {'label': 'RUN1 known USD gross', 'value': 29500, 'method': 'USD 15000 credits plus USD 14500 debits; excludes unknown/conflicting amounts', 'format': '#,##0'}], 'limitations': ['Source-row reconciliation does not establish a complete economic monetary total.', 'The posting reversal pair is excluded only by this authored illustrative flow convention; actual monitoring designs may retain reversal activity.', 'RUN1 repairs one known late event, not an independently proven complete late-arrival population.', 'EUR remains separate and is outside the illustrative USD rule.'], 'report_narrative': [['Every one of fifteen delivered rows has an explicit initial lineage state. Seven known rows reach RUN0; eight reach RUN1 after a late credit. Two accounts remain blocked by unresolved source defects.'], ['The event review period is Sep 01, 2026 12:00 AM ET to Sep 02, 2026 12:00 AM ET exclusive. RUN0 ingestion cutoff is Sep 02, 2026 12:00 AM ET. RUN1 cutoff is Sep 02, 2026 8:00 AM ET. The delivered set intentionally includes a row unavailable at RUN0.'], ['TX05 conflicts between two same-version amounts, X14 is unreadable, and X12 arrives after the first cutoff. Reversal and pending records are controlled exclusions, not discarded evidence.'], ['SourceRows contains fifteen rows; FieldMappings defines eight transformations; LineageLedger gives every raw row one initial terminal state; CanonicalOutput retains seven RUN0 rows. One exact duplicate points to CL01 without increasing totals.'], ['Initial USD canonical movement is $25,500.00; RUN1 is $29,500.00, a $4,000.00 credit increase. EUR $1,000.00 remains separate. LF becomes a complete no-match under the illustrative credit minimum while LC and LG remain blocked. RunImpact preserves eight account/currency records.'], ['All row facts and controls are fictional. Public monitoring examination guidance supplies context for checking data and filtering; it does not establish a required transformation or threshold here.'], ['Resolve TX05; recover X14; review all known late arrivals; retain before/after counts, amounts and affected windows. No operational reprocessing or rule change is performed by this package.'], ['Count reconciliation succeeds while economic monetary completeness remains unresolved. The demonstrated pipeline is a synthetic review design, not production data assurance or monitoring validation.']], 'conclusion': 'Every one of fifteen delivered rows has an explicit initial lineage state. Seven known rows reach RUN0; eight reach RUN1 after a late credit. Two accounts remain blocked by unresolved source defects.', 'suite_id': 'tm-data-lineage', 'version': '1.2.0', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'scope': 'Only the complete fictional inputs printed in file 10 are in scope. Public guidance supplies method context and is not evidence about the fictional subjects.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'LN-F01', 'proposal': 'Obtain an authoritative version history, resolve TX05 and rerun every affected window.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'LN-F02', 'proposal': 'Preserve RUN0 and RUN1 and verify the wider lag population before accepting complete coverage.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'LN-F03', 'proposal': 'Request corrected source evidence and reconcile the replacement to source totals.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
