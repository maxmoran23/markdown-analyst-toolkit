# Investigation Case Review — fixed workbook template

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
| CaseTimeline | `event_id`, `event_time`, `from_node`, `to_node`, `amount_usd`, `currency`, `linked_return_of`, `account_a_balance_usd`, `evidence_ids`, `claim_class`, `detail` |
| AccountBalances | `account_id`, `opening_usd`, `credits_usd`, `debits_usd`, `calculated_close_usd`, `supplied_close_usd`, `difference_usd`, `evidence_ids` |
| ClaimTests | `claim_id`, `proposition`, `supporting_ids`, `conflicting_ids`, `assessment`, `confidence`, `discriminator`, `evidence_ids` |
| Contradictions | `contradiction_id`, `claim_id`, `left_account`, `right_account`, `effect`, `state`, `evidence_ids` |
| EvidenceRequests | `request_id`, `claim_id`, `request_text`, `state`, `decision_effect`, `evidence_ids` |
| EvidenceProvenance | `source_id`, `source_title`, `locator`, `availability`, `origin_type`, `claim_class`, `limitation` |
| DecisionRecord | `decision_id`, `gate`, `status`, `basis`, `evidence_ids` |
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

DATA = {'slug': 'investigations', 'title': 'Investigation Case Review', 'summary': 'Reconstruct a full case chronology, reconcile account and entity flows, test competing claims, preserve contradictions and produce a bounded human decision package.', 'audience': 'Investigators, case reviewers and quality-assurance analysts', 'decision': 'Which propositions survive a complete chronology, reconciliation and contrary-evidence review, and what evidence or human decision is still required?', 'palette': 'indigo', 'as_of': '2026-09-30T17:00:00-04:00', 'scope': 'Fictional Entity-J, accounts A/B, Sep 01–30, 2026; 30 received raw representations, 27 posted account entries and 24 canonical transfers, all USD. Sources are printed in file 10.', 'report_sections': ['Decision questions and current assessment', 'Scope, chronology method, and coverage', 'Findings and contradictions', 'Chronology and funds movement', 'Competing hypothesis tests and decision gates', 'Evidence inventory and provenance', 'Proposed investigative actions', 'Limitations, quality checks, and reviewer decision'], 'domain_tables': [{'name': 'CaseTimeline', 'columns': ['event_id', 'event_time', 'from_node', 'to_node', 'amount_usd', 'currency', 'linked_return_of', 'account_a_balance_usd', 'evidence_ids', 'claim_class', 'detail'], 'column_contracts': {'event_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique canonical economic transfer identifier, not source-row number.'}, 'event_time': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact posted timestamp in ISO-8601 with offset; human narrative uses ET.'}, 'from_node': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Recorded immediate sender node; ultimate ownership not inferred.'}, 'to_node': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Recorded immediate receiver node; purpose not inferred.'}, 'amount_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Positive booked USD amount of one canonical transfer.'}, 'currency': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Native currency of every monetary record.', 'enum': ['USD']}, 'linked_return_of': {'type': 'text', 'nullable': True, 'unit': 'identifier', 'description': 'Parent debit event for explicitly linked return; null otherwise.'}, 'account_a_balance_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Account A running balance after this event, opening USD5000.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}, 'claim_class': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Class of the proposition visible in this event row.', 'enum': ['Observed']}, 'detail': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Bounded event description including unresolved purpose where relevant.'}}, 'rows': [['T01', '2026-09-02T10:00:00-04:00', 'P', 'A', 12000, 'USD', None, 17000, 'S01', 'Observed', 'Receipt described by customer as equipment sale'], ['T02', '2026-09-02T11:00:00-04:00', 'A', 'Q', 11000, 'USD', None, 6000, 'S01', 'Observed', 'Equipment-purpose explanation; invoice names R'], ['T03', '2026-09-04T09:00:00-04:00', 'Q', 'A', 2000, 'USD', 'T02', 8000, 'S01;S08', 'Observed', 'Explicit partial return of T02'], ['T04', '2026-09-05T09:00:00-04:00', 'P2', 'A', 8000, 'USD', None, 16000, 'S01', 'Observed', 'Second customer receipt'], ['T05', '2026-09-05T12:00:00-04:00', 'A', 'R', 7500, 'USD', None, 8500, 'S01', 'Observed', 'Invoice INV-B and delivery receipt support purpose'], ['T06', '2026-09-06T09:00:00-04:00', 'A', 'B', 500, 'USD', None, 8000, 'S01;S09', 'Observed', 'Same-entity account transfer; both books supplied'], ['T07', '2026-09-08T09:00:00-04:00', 'P3', 'A', 6000, 'USD', None, 14000, 'S01', 'Observed', 'Customer receipt; remitter identity supported'], ['T08', '2026-09-08T09:20:00-04:00', 'A', 'U', 6000, 'USD', None, 8000, 'S01', 'Observed', 'Purpose explanation absent'], ['T09', '2026-09-10T10:00:00-04:00', 'P', 'A', 3000, 'USD', None, 11000, 'S01', 'Observed', 'Additional customer receipt'], ['T10', '2026-09-10T14:00:00-04:00', 'A', 'Q', 2500, 'USD', None, 8500, 'S01', 'Observed', 'Customer says invoice INV-C settlement'], ['T11', '2026-09-10T16:00:00-04:00', 'A', 'BANK', 100, 'USD', None, 8400, 'S01', 'Observed', 'Posted service fee'], ['T12', '2026-09-12T09:00:00-04:00', 'P4', 'A', 7000, 'USD', None, 15400, 'S01', 'Observed', 'Customer receipt'], ['T13', '2026-09-12T10:00:00-04:00', 'A', 'R', 6800, 'USD', None, 8600, 'S01', 'Observed', 'Invoice INV-D full amount supported'], ['T14', '2026-09-13T10:00:00-04:00', 'R', 'A', 400, 'USD', 'T13', 9000, 'S01;S08', 'Observed', 'Explicit partial return of T13'], ['T15', '2026-09-14T09:00:00-04:00', 'A', 'B', 1000, 'USD', None, 8000, 'S01;S09', 'Observed', 'Same-entity transfer; both books supplied'], ['T16', '2026-09-15T09:00:00-04:00', 'B', 'A', 1000, 'USD', None, 9000, 'S01;S09', 'Observed', 'Same-entity return transfer; not a supplier refund'], ['T17', '2026-09-17T09:00:00-04:00', 'P5', 'A', 5000, 'USD', None, 14000, 'S01', 'Observed', 'Customer receipt'], ['T18', '2026-09-17T11:00:00-04:00', 'A', 'V', 4000, 'USD', None, 10000, 'S01', 'Observed', 'Invoice INV-E and delivery support purpose'], ['T19', '2026-09-18T10:00:00-04:00', 'A', 'CASH', 1000, 'USD', None, 9000, 'S01', 'Observed', 'Cash withdrawal; ultimate use uncorroborated'], ['T20', '2026-09-21T09:00:00-04:00', 'P5', 'A', 1500, 'USD', None, 10500, 'S01', 'Observed', 'Customer receipt'], ['T21', '2026-09-21T12:00:00-04:00', 'A', 'V', 1500, 'USD', None, 9000, 'S01', 'Observed', 'Invoice INV-F and delivery support purpose'], ['T22', '2026-09-23T10:00:00-04:00', 'U', 'A', 1000, 'USD', 'T08', 10000, 'S01;S08', 'Observed', 'Explicit partial return of T08'], ['T23', '2026-09-24T09:00:00-04:00', 'A', 'Q', 700, 'USD', None, 9300, 'S01', 'Observed', 'Adjustment description; supporting memo absent'], ['T24', '2026-09-25T16:00:00-04:00', 'A', 'BANK', 300, 'USD', None, 9000, 'S01', 'Observed', 'Posted service fee']], 'primary_key': ['event_id'], 'grain': 'One canonical transfer touching A; same-entity mirror legs are represented once.', 'report_section': 4, 'formats': {'amount_usd': '$#,##0.00', 'account_a_balance_usd': '$#,##0.00'}}, {'name': 'AccountBalances', 'columns': ['account_id', 'opening_usd', 'credits_usd', 'debits_usd', 'calculated_close_usd', 'supplied_close_usd', 'difference_usd', 'evidence_ids'], 'column_contracts': {'account_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Account identifier in the supplied two-account perimeter.'}, 'opening_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Supplied opening balance, not inferred from first transaction.'}, 'credits_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Sum of positive postings to this account, including own-account mirrors.'}, 'debits_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Sum of outgoing postings from this account, including own-account mirrors.'}, 'calculated_close_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Opening plus credits minus debits.'}, 'supplied_close_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Independent supplied close from S03.'}, 'difference_usd': {'type': 'number', 'nullable': False, 'unit': 'USD', 'description': 'Calculated close minus supplied close.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['A', 5000, 46900, 42900, 9000, 9000, 0, 'S01;S03'], ['B', 1000, 1500, 1000, 1500, 1500, 0, 'S02;S03']], 'primary_key': ['account_id'], 'grain': 'One account-period balance equation.', 'report_section': 4, 'formats': {'opening_usd': '$#,##0.00', 'credits_usd': '$#,##0.00', 'debits_usd': '$#,##0.00', 'calculated_close_usd': '$#,##0.00', 'supplied_close_usd': '$#,##0.00', 'difference_usd': '$#,##0.00'}}, {'name': 'ClaimTests', 'columns': ['claim_id', 'proposition', 'supporting_ids', 'conflicting_ids', 'assessment', 'confidence', 'discriminator', 'evidence_ids'], 'column_contracts': {'claim_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable falsifiable claim identifier.'}, 'proposition': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Bounded question that can be supported, contradicted or unresolved.'}, 'supporting_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon references or explicit NONE_LOCATED; narrative explains meaning.'}, 'conflicting_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Semicolon references or explicit NONE_LOCATED.'}, 'assessment': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Outcome under the printed evidence.', 'enum': ['SUPPORTED', 'CONTRADICTED', 'UNRESOLVED', 'PATTERN_SUPPORTED']}, 'confidence': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Confidence in this bounded proposition.', 'enum': ['HIGH', 'MODERATE', 'LOW', 'NOT ASSESSABLE']}, 'discriminator': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Evidence capable of changing the assessment.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['CL01', 'T02 is fully reconciled equipment settlement', 'S04;S05', 'S01;S05', 'UNRESOLVED', 'LOW', 'Beneficiary bridge plus USD1000 difference and delivery evidence', 'S01;S04;S05'], ['CL02', 'T03 fully reversed T02', 'S08', 'S01;S08', 'CONTRADICTED', 'HIGH', 'No additional source needed for the supplied-period arithmetic', 'S01;S08'], ['CL03', 'Every supplier payment is unexplained', 'S01', 'S06', 'CONTRADICTED', 'HIGH', 'Matched B/D/E/F records are material counterevidence', 'S01;S06'], ['CL04', 'T08 purpose is substantiated', 'NONE_LOCATED', 'S01', 'UNRESOLVED', 'LOW', 'Contract, invoice and beneficiary-purpose evidence', 'S01;S10'], ['CL05', 'Own-account transfers create external turnover', 'S01', 'S02;S09', 'CONTRADICTED', 'HIGH', 'Entity aggregation removes three own transfers', 'S01;S02;S09'], ['CL06', 'Rapid onward timing pattern exists for T01/T02', 'S01', 'NONE_LOCATED', 'PATTERN_SUPPORTED', 'HIGH', 'Timing established; source allocation and purpose remain separate', 'S01;S04;S05']], 'primary_key': ['claim_id'], 'grain': 'One proposition, including favorable and contrary alternatives.', 'report_section': 5, 'formats': {}}, {'name': 'Contradictions', 'columns': ['contradiction_id', 'claim_id', 'left_account', 'right_account', 'effect', 'state', 'evidence_ids'], 'column_contracts': {'contradiction_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable difference identifier.'}, 'claim_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Claim being challenged or qualified.'}, 'left_account': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'One source-supported representation.'}, 'right_account': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Conflicting or qualifying representation.'}, 'effect': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact consequence for a live decision.'}, 'state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Resolution state.', 'enum': ['OPEN', 'RESOLVED_ARITHMETIC', 'RESOLVED_SCOPE']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['CT01', 'CL01', 'T02 paid Q USD11000', 'INV-A names R USD10000', 'Amount gap USD1000 and identity bridge remain separate', 'OPEN', 'S01;S05'], ['CT02', 'CL02', 'Return described as full reversal', 'Linked posted return USD2000 against USD11000', 'Net unreversed T02 is USD9000', 'RESOLVED_ARITHMETIC', 'S01;S08'], ['CT03', 'CL03', 'All supplier activity described as unsupported', 'INV-B/D/E/F support USD19800 gross supplier payments', 'Do not generalize unresolved subset to all USD40000 gross supplier debits', 'RESOLVED_SCOPE', 'S01;S06'], ['CT04', 'CL05', 'Account credits summed as new external funds', 'A/B internal mirrors total USD2500 canonical own transfer value', 'Entity external inflow excludes both directions of own transfers', 'RESOLVED_SCOPE', 'S01;S02;S09']], 'primary_key': ['contradiction_id'], 'grain': 'One material contradiction or qualification and its exact decision effect.', 'report_section': 5, 'formats': {}, 'foreign_keys': [{'columns': ['claim_id'], 'table': 'ClaimTests', 'references': ['claim_id']}]}, {'name': 'EvidenceRequests', 'columns': ['request_id', 'claim_id', 'request_text', 'state', 'decision_effect', 'evidence_ids'], 'column_contracts': {'request_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable proposed request identifier.'}, 'claim_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Decision-sensitive claim this request serves.'}, 'request_text': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Narrow question, records and period; no accusation.'}, 'state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Fixture request status.', 'enum': ['PROPOSED', 'INACCESSIBLE', 'SATISFIED_FOR_SCOPE']}, 'decision_effect': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'What changes if evidence supports or contradicts the claim.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['RQ01', 'CL01', 'Provide beneficiary bridge Q/R, explanation of USD1000 difference and delivery evidence for T02.', 'PROPOSED', 'Can resolve purpose/amount/beneficiary separately; cannot retroactively invent receipt', 'S01;S04;S05'], ['RQ02', 'CL04', 'Provide readable Contract-C and supporting T08 purpose documents.', 'INACCESSIBLE', 'Readable contract may support represented terms; payment purpose still needs linkage', 'S01;S10'], ['RQ03', 'CL03', 'Retain INV-B/D/E/F and delivery matches in favorable evidence set.', 'SATISFIED_FOR_SCOPE', 'Prevents claim that every supplier payment lacks support', 'S06'], ['RQ04', 'CL05', 'Retain supplied A/B ownership extract and mirrored postings.', 'SATISFIED_FOR_SCOPE', 'Supports perimeter netting only for A/B', 'S02;S09'], ['RQ05', 'CL06', 'Obtain allocation evidence only if attribution of T01 funds to T02 is decision-material.', 'PROPOSED', 'Could narrow source attribution; chronological proximity alone cannot do so', 'S01']], 'primary_key': ['request_id'], 'grain': 'One decision-sensitive request or satisfied request outcome.', 'report_section': 5, 'formats': {}, 'foreign_keys': [{'columns': ['claim_id'], 'table': 'ClaimTests', 'references': ['claim_id']}]}, {'name': 'EvidenceProvenance', 'columns': ['source_id', 'source_title', 'locator', 'availability', 'origin_type', 'claim_class', 'limitation'], 'column_contracts': {'source_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Exact identifier in common Evidence register.'}, 'source_title': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Fictional source name.'}, 'locator': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact raw-data locator in file 10.'}, 'availability': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Availability distinct from reliability.', 'enum': ['AVAILABLE', 'INACCESSIBLE']}, 'origin_type': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Origin family relevant to independence.'}, 'claim_class': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Class applicable to source description.', 'enum': ['Observed', 'Reported']}, 'limitation': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific proposition this source cannot establish.'}}, 'rows': [['S01', 'Account A posted ledger', 'Raw postings T01–T24', 'AVAILABLE', 'SYSTEM_EXPORT', 'Observed', 'Complete stated account-period posting set; does not establish purpose'], ['S02', 'Account B posted ledger', 'Mirror legs T06, T15, T16', 'AVAILABLE', 'SYSTEM_EXPORT', 'Observed', 'Ownership extract identifies A and B as same entity; mirror legs do not create new economic transfers'], ['S03', 'Opening and closing balances', 'A 5000→9000; B 1000→1500', 'AVAILABLE', 'BALANCE_RECORD', 'Observed', 'Balances cover stated September perimeter only'], ['S04', 'Customer explanation', 'Statement X01', 'AVAILABLE', 'CUSTOMER_STATEMENT', 'Reported', 'T02 said to pay equipment supplier Q; T10 said to settle INV-C; T19 said to cover expenses'], ['S05', 'Invoice INV-A', 'Face 10000 USD; supplier R', 'AVAILABLE', 'CUSTOMER_DOCUMENT', 'Observed', 'Document text observed; actual delivery and beneficiary bridge absent'], ['S06', 'Supported invoices and receipts', 'INV-B 7500; INV-D 6800; INV-E 4000; INV-F 1500', 'AVAILABLE', 'CUSTOMER_DOCUMENT', 'Observed', 'Matched amounts and counterparties; supplied delivery records corroborate within fixture'], ['S07', 'Invoice INV-C', 'Face 2500 USD; supplier Q', 'AVAILABLE', 'CUSTOMER_DOCUMENT', 'Observed', 'Amount and name match T10; no delivery record supplied'], ['S08', 'Return references', 'T03→T02; T14→T13; T22→T08', 'AVAILABLE', 'SYSTEM_EXPORT', 'Observed', 'Explicit linkage; amounts are partial, not full reversals'], ['S09', 'Account ownership extract', 'A and B belong to fictional Entity-J', 'AVAILABLE', 'ACCOUNT_RECORD', 'Observed', 'No ownership linkage supplied for Q, R, U or V'], ['S10', 'Contract file', 'Contract-C encrypted attachment', 'INACCESSIBLE', 'CUSTOMER_DOCUMENT', 'Reported', 'Filename supplied; text not accessible and cannot corroborate terms'], ['S11', 'Receipt manifest', '30 raw rows: 27 posted representations; 1 duplicate; 1 instruction; 1 pending', 'AVAILABLE', 'INTAKE_MANIFEST', 'Observed', 'Includes one T01 duplicate, unexecuted T02 instruction and pending USD2000 debit; exact exclusions in file 10'], ['S12', 'Illustrative review charter', 'Fixture policy CP-INV-1', 'AVAILABLE', 'ILLUSTRATIVE_POLICY', 'Observed', 'Requires amount/beneficiary/purpose checks for this exercise; no legal filing conclusion authorized']], 'primary_key': ['source_id'], 'grain': 'One source origin or explicitly unavailable supplied item.', 'report_section': 5, 'formats': {}}, {'name': 'DecisionRecord', 'columns': ['decision_id', 'gate', 'status', 'basis', 'evidence_ids'], 'column_contracts': {'decision_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable analytical gate identifier.'}, 'gate': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Decision being recorded.'}, 'status': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Analytical state distinct from human disposition.', 'enum': ['COMPLETE', 'HOLD_EVIDENCE', 'NOT_RECORDED']}, 'basis': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Case-specific reason.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['D01', 'Population and balance gate', 'COMPLETE', '30 received rows reduce to 24 canonical transfers and 27 posted account representations; both balances tie.', 'S01;S02;S03;S11'], ['D02', 'T02 purpose and beneficiary gate', 'HOLD_EVIDENCE', 'USD1000 invoice difference and Q/R bridge remain unresolved.', 'S01;S04;S05'], ['D03', 'T08 purpose gate', 'HOLD_EVIDENCE', 'Readable contract and purpose corroboration absent; partial return does not resolve purpose.', 'S01;S08;S10'], ['D04', 'Human case disposition', 'NOT_RECORDED', 'No actual authorized reviewer decision supplied.', 'S12']], 'primary_key': ['decision_id'], 'grain': 'One distinct gate; completion is not equivalent to case closure.', 'report_section': 5, 'formats': {}}, {'name': 'ProcessQA', 'columns': ['check_id', 'check', 'expected', 'actual', 'result', 'evidence_ids'], 'column_contracts': {'check_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable reperformable check.'}, 'check': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific invariant or calculation.'}, 'expected': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Independent expected outcome.'}, 'actual': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Fixture outcome; must be recomputed when adapted.'}, 'result': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Fixture analytical result.', 'enum': ['PASS', 'REVIEW REQUIRED', 'NOT RECORDED']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['Q01', 'Raw-to-canonical count', '30 raw; 27 posted representations; 24 transfers', '30 / 27 / 24', 'PASS', 'S01;S02;S11'], ['Q02', 'Account A close', 'USD9000', 'USD9000', 'PASS', 'S01;S03'], ['Q03', 'Account B close', 'USD1500', 'USD1500', 'PASS', 'S02;S03'], ['Q04', 'Entity close', 'USD10500', 'USD10500', 'PASS', 'S01;S02;S03'], ['Q05', 'External receipts excluding returns', 'USD42500', 'USD42500', 'PASS', 'S01;S08;S09'], ['Q06', 'Supplier gross and linked net', 'USD40000 gross; USD36600 net', 'USD40000 / USD36600', 'PASS', 'S01;S08'], ['Q07', 'T02 invoice difference', 'USD1000', 'USD1000', 'PASS', 'S01;S05'], ['Q08', 'T02 unreversed', 'USD9000', 'USD9000', 'PASS', 'S01;S08'], ['Q09', 'Supported supplier gross', 'USD19800 of USD40000; 49.5%', 'USD19800 / USD40000 = 49.5%', 'PASS', 'S01;S06'], ['Q10', 'Unsupported conclusion gate', 'No universal explanation or illicit-purpose assertion', 'Bounded unresolved subset retained', 'PASS', 'S01;S04;S06;S10'], ['Q11', 'Purpose gates', 'T02 and T08 remain unresolved', 'HOLD_EVIDENCE', 'REVIEW REQUIRED', 'S01;S05;S10'], ['Q12', 'Human disposition', 'No invented approval', 'NOT_RECORDED', 'NOT RECORDED', 'S12']], 'primary_key': ['check_id'], 'grain': 'One performed fixture check or explicit unrecorded approval gate.', 'report_section': 5, 'formats': {}}], 'findings': [{'id': 'INV-F01', 'title': 'T02 invoice fails amount and beneficiary reconciliation', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['S01', 'S04', 'S05'], 'detail': 'T02 is USD11000 to Q while INV-A is USD10000 naming R. The USD1000 difference and beneficiary bridge are separate unresolved questions.', 'recommendation': 'Obtain targeted amount, beneficiary and delivery support; retain the customer explanation as Reported.'}, {'id': 'INV-F02', 'title': 'T08 purpose remains unsupported within the supplied evidence', 'severity': 'MEDIUM', 'confidence': 'MODERATE', 'claim_class': 'Inferred', 'evidence_ids': ['S01', 'S08', 'S10'], 'detail': 'T08 paid U USD6000; a linked USD1000 return leaves USD5000 unreversed. Contract-C is inaccessible. This does not establish illicit purpose or confirmed loss.', 'recommendation': 'Request a readable contract and transaction-specific purpose evidence; preserve the return as counterevidence.'}, {'id': 'INV-F03', 'title': 'Rapid onward movement is observable but source attribution is unproven', 'severity': 'LOW', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['S01', 'S04', 'S05'], 'detail': 'T02 followed T01 by one hour. Pre-existing USD5000 means temporal order does not prove that the entire debit came from T01.', 'recommendation': 'Record timing separately from source attribution and economic explanation.'}, {'id': 'INV-F04', 'title': 'The unresolved subset must not erase supported supplier activity', 'severity': 'LOW', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['S01', 'S06'], 'detail': 'Four matched invoice and delivery sets support USD19800 of USD40000 gross supplier debits, or 49.5%. Unreconciled value is not automatically suspicious value.', 'recommendation': 'Keep favorable evidence and denominator definitions in every output.'}], 'evidence': [{'id': 'S01', 'title': 'Account A posted ledger', 'locator': '10-worked-example.md, Raw postings T01–T24', 'claim_class': 'Observed'}, {'id': 'S02', 'title': 'Account B posted ledger', 'locator': '10-worked-example.md, Mirror legs T06, T15, T16', 'claim_class': 'Observed'}, {'id': 'S03', 'title': 'Opening and closing balances', 'locator': '10-worked-example.md, A 5000→9000; B 1000→1500', 'claim_class': 'Observed'}, {'id': 'S04', 'title': 'Customer explanation', 'locator': '10-worked-example.md, Statement X01', 'claim_class': 'Reported'}, {'id': 'S05', 'title': 'Invoice INV-A', 'locator': '10-worked-example.md, Face 10000 USD; supplier R', 'claim_class': 'Observed'}, {'id': 'S06', 'title': 'Supported invoices and receipts', 'locator': '10-worked-example.md, INV-B 7500; INV-D 6800; INV-E 4000; INV-F 1500', 'claim_class': 'Observed'}, {'id': 'S07', 'title': 'Invoice INV-C', 'locator': '10-worked-example.md, Face 2500 USD; supplier Q', 'claim_class': 'Observed'}, {'id': 'S08', 'title': 'Return references', 'locator': '10-worked-example.md, T03→T02; T14→T13; T22→T08', 'claim_class': 'Observed'}, {'id': 'S09', 'title': 'Account ownership extract', 'locator': '10-worked-example.md, A and B belong to fictional Entity-J', 'claim_class': 'Observed'}, {'id': 'S10', 'title': 'Contract file', 'locator': '10-worked-example.md, Contract-C encrypted attachment', 'claim_class': 'Reported'}, {'id': 'S11', 'title': 'Receipt manifest', 'locator': '10-worked-example.md, 30 raw rows: 27 posted representations; 1 duplicate; 1 instruction; 1 pending', 'claim_class': 'Observed'}, {'id': 'S12', 'title': 'Illustrative review charter', 'locator': '10-worked-example.md, Fixture policy CP-INV-1', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Canonical transfers', 'value': 24, 'method': '30 raw representations minus 1 duplicate, 1 instruction, 1 pending item and 3 own-account mirror representations', 'format': '#,##0'}, {'label': 'Entity closing balance USD', 'value': 10500, 'method': 'Opening6000 + customer receipts42500 + linked returns3400 - supplier debits40000 - cash1000 - fees400; own transfers cancel', 'format': '$#,##0.00'}, {'label': 'Supplier gross debit USD', 'value': 40000, 'method': 'T02+T05+T08+T10+T13+T18+T21+T23', 'format': '$#,##0.00'}, {'label': 'Net supplier debit USD', 'value': 36600, 'method': '40000 minus linked returns T03/T14/T22 totaling3400', 'format': '$#,##0.00'}, {'label': 'Supported supplier gross ratio', 'value': 0.495, 'format': '0.0%', 'method': 'Matched invoice and delivery T05/T13/T18/T21 amount19800 divided by gross supplier debit40000; not a suspicious-value rate'}], 'limitations': ['All subjects, records and criteria are fictional; no legal or filing determination is made.', 'Contract-C is inaccessible; beneficiary Q/R linkage and T02 amount difference remain unresolved.', 'Book reconciliation does not establish source attribution, economic purpose, loss or misconduct.', 'No actual human decision, external request or approval is recorded.'], 'conclusion': 'The two-account ledger reconciles to USD10500, but T02 amount/beneficiary support and T08 purpose remain unresolved. Supported supplier activity totals USD19800 of USD40000 gross; uncertainty must remain bounded to the relevant subset.', 'report_narrative': [['The two-account ledger reconciles to USD10500, but T02 amount/beneficiary support and T08 purpose remain unresolved. Supported supplier activity totals USD19800 of USD40000 gross; uncertainty must remain bounded to the relevant subset.', 'The package recommends targeted evidence review. It does not conclude that funds were illicit, that an account should close or that a SAR must be filed.'], ['Thirty raw representations include twenty-seven posted account entries, one exact duplicate, one unexecuted instruction and one pending item. Three posted entries are mirror legs of own-account transfers, leaving twenty-four canonical transfers. Event timestamps describe posting; source availability and customer explanations remain separate chronology layers.'], ['INV-F01: T02 is USD11000 to Q while INV-A is USD10000 naming R. The USD1000 difference and beneficiary bridge are separate unresolved questions.', 'INV-F02: T08 paid U USD6000; a linked USD1000 return leaves USD5000 unreversed. Contract-C is inaccessible. This does not establish illicit purpose or confirmed loss.', 'INV-F03: T02 followed T01 by one hour. Pre-existing USD5000 means temporal order does not prove that the entire debit came from T01.', 'INV-F04: Four matched invoice and delivery sets support USD19800 of USD40000 gross supplier debits, or 49.5%. Unreconciled value is not automatically suspicious value.'], ['Account A: USD5000 + USD46900 credits - USD42900 debits = USD9000. Account B: USD1000 + USD1500 credits - USD1000 debits = USD1500. Entity close is USD10500 with zero balance difference.', 'External customer receipts are USD42500; supplier debits are USD40000 gross and USD36600 after USD3400 of explicitly linked returns. Cash USD1000 and fees USD400 remain separate. Own-account transfers of USD2500 canonical value cancel at entity level.'], ['CL01 remains unresolved because INV-A differs by USD1000 and names R rather than Q. CL02 is contradicted: T03 returns only USD2000 of T02 USD11000. CL03 is contradicted by matched B/D/E/F records totaling USD19800. CL04 remains unresolved while Contract-C is inaccessible. CL05 is contradicted by the A/B ownership and mirror records. CL06 supports timing only.', 'RQ01/RQ02/RQ05 remain proposed or inaccessible; RQ03/RQ04 are satisfied only for their bounded scope. D02/D03 hold purpose decisions and D04 records no actual human disposition.'], ['S01–S12 preserve source origin, availability and limits. The encrypted contract is not treated as reviewed evidence. Customer explanation remains Reported; the invoice face text is Observed without implying actual performance. Duplicate ledger representations are not independent corroboration.'], ['Obtain the Q/R beneficiary bridge, USD1000 difference explanation and delivery support for T02. Obtain readable Contract-C and transaction-specific support for T08. Preserve matched invoice/delivery evidence and the partial returns. No request has been sent by this fixture.'], ['All subjects, records and criteria are fictional; no legal or filing determination is made.', 'Contract-C is inaccessible; beneficiary Q/R linkage and T02 amount difference remain unresolved.', 'Book reconciliation does not establish source attribution, economic purpose, loss or misconduct.', 'No actual human decision, external request or approval is recorded.', 'Fixture arithmetic checks pass; material purpose gates remain REVIEW REQUIRED and human disposition NOT RECORDED.']], 'suite_id': 'investigations', 'version': '1.2.0', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'INV-F01', 'proposal': 'Obtain targeted amount, beneficiary and delivery support; retain the customer explanation as Reported.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'INV-F02', 'proposal': 'Request a readable contract and transaction-specific purpose evidence; preserve the return as counterevidence.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'INV-F03', 'proposal': 'Record timing separately from source attribution and economic explanation.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-004', 'finding_id': 'INV-F04', 'proposal': 'Keep favorable evidence and denominator definitions in every output.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
