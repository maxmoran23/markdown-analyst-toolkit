# Alert Adjudication Quality Review — fixed workbook template

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
| CasePackets | `case_id`, `case_topic`, `raw_packet`, `consensus`, `rationale`, `evidence_ids` |
| ReviewVotes | `vote_id`, `case_id`, `reviewer_id`, `vote`, `round`, `evidence_ids` |
| QualityCriteria | `criterion_id`, `criterion`, `rule`, `materiality_class`, `boundary`, `evidence_ids` |
| DefectRegister | `defect_id`, `case_id`, `criterion_id`, `severity`, `materiality`, `condition`, `evidence_ids` |
| Calibration | `case_id`, `r1_vote`, `r2_vote`, `agreement`, `consensus`, `adjudication_reason`, `evidence_ids` |
| Remediation | `remediation_id`, `defect_id`, `repair`, `closure_test`, `status`, `evidence_ids` |
| DecisionRecord | `decision_id`, `question`, `status`, `basis`, `evidence_ids` |
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

DATA = {'slug': 'alert-qa', 'title': 'Alert Adjudication Quality Review', 'summary': 'Reperform case reasoning, distinguish demonstrated defects from missing reviewability, calibrate independent judgments and define evidence-based remediation closure.', 'audience': 'Alert quality reviewers, investigation leads and calibration facilitators', 'decision': 'Which supplied adjudications meet the applicable quality rubric, which need substantive repair, and which cannot yet be assessed?', 'palette': 'slate', 'as_of': '2026-09-30T17:00:00-04:00', 'scope': 'Twelve deliberately selected fictional case packets, two original blind reviewers each, supplied illustrative policy CP-QA-1 and a separate consensus round. No random sample or population estimate.', 'report_sections': ['Quality decision and open gates', 'Scope, supplied criteria and review design', 'Material and nonmaterial findings', 'Case packets and original review votes', 'Criteria, defects, calibration and remediation', 'Evidence and decision-time provenance', 'Proposed repairs and closure tests', 'Quality checks, limitations and human disposition'], 'domain_tables': [{'name': 'CasePackets', 'columns': ['case_id', 'case_topic', 'raw_packet', 'consensus', 'rationale', 'evidence_ids'], 'column_contracts': {'case_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique case packet in this deliberately selected calibration set.'}, 'case_topic': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Short topic, not an allegation.'}, 'raw_packet': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Complete bounded fictional facts supplied for this quality question.'}, 'consensus': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Adjudicated quality status under fixture policy.', 'enum': ['ACCEPT', 'REWORK', 'INSUFFICIENT']}, 'rationale': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Case-specific quality reasoning, distinct from underlying case disposition.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['C01', 'Routine pass-through explanation', 'Posted debit 1000; invoice 1000; beneficiary and delivery match; counterevidence considered.', 'ACCEPT', 'No material reasoning defect on supplied packet.', 'Q01;Q14;Q15'], ['C02', 'Omitted contrary invoice', 'Investigator described no business support; packet includes matched invoice 2000 and delivery for the same payment.', 'REWORK', 'Material contrary evidence omitted; outcome must be reconsidered without assuming reversal.', 'Q02;Q14;Q15'], ['C03', 'Partial return treated as full reversal', 'Original debit 11000 and explicitly linked return 2000; narrative says fully reversed.', 'REWORK', 'Correct net 9000 and review conclusion dependent on the error.', 'Q03;Q14;Q15'], ['C04', 'Unsupported identity merge', 'Two beneficiaries have similar names but different supplied identifiers; investigator merged them into one subject.', 'REWORK', 'Split identities and recompute aggregate before reassessing.', 'Q04;Q14;Q15'], ['C05', 'Nonmaterial display defect', 'Ledger and narrative amounts match; one non-substantive punctuation defect in an evidence title.', 'ACCEPT', 'Optional editorial correction; no effect on inference or traceability.', 'Q05;Q14;Q15'], ['C06', 'Relevant timeline gap', 'Two same-period postings 4000 and 3500 omitted from chronology while present in supplied ledger; net effect 500.', 'REWORK', 'Restore both gross events and recompute period totals; net 500 does not excuse omission.', 'Q06;Q14;Q15'], ['C07', 'Bounded unknown handled correctly', 'Opening balance missing; investigator declines source attribution, requests balance and gives descriptive flows only.', 'ACCEPT', 'Properly bounded analysis; unknown is not itself a quality failure.', 'Q07;Q14;Q15'], ['C08', 'Source inaccessible', 'Case conclusion cites an encrypted document unavailable to either reviewer; no equivalent source supplied.', 'INSUFFICIENT', 'Review cannot determine whether the underlying conclusion is supported.', 'Q08;Q14;Q15'], ['C09', 'Different defensible wording', 'Narrative uses unresolved purpose; reviewer prefers insufficient corroboration; both reflect same evidence and scope.', 'ACCEPT', 'Style preference alone is not a defect.', 'Q09;Q14;Q15'], ['C10', 'Observed pattern overstates intent', 'Rapid onward transfers are evidenced; conclusion states intent to launder without supporting intent evidence.', 'REWORK', 'Remove unsupported intent assertion and reconsider bounded analytical conclusion.', 'Q10;Q14;Q15'], ['C11', 'Invented universal documentation rule', 'Reviewer worksheet treats absent nonfiling memorandum as a universal BSA breach; supplied fixture policy only requires a brief case rationale.', 'REWORK', 'Use supplied policy CP-QA-1 and actual case rationale; no universal nonfiling memo requirement.', 'Q11;Q14;Q15'], ['C12', 'Unknown historical cutoff', 'Packet does not identify what evidence was available at original decision date; reviewers see later documents mixed with earlier material.', 'INSUFFICIENT', 'Cannot assess original decision under hindsight without an availability chronology.', 'Q12;Q14;Q15']], 'primary_key': ['case_id'], 'grain': 'One completed case packet selected for calibration, not a random population sample.', 'report_section': 4, 'formats': {}}, {'name': 'ReviewVotes', 'columns': ['vote_id', 'case_id', 'reviewer_id', 'vote', 'round', 'evidence_ids'], 'column_contracts': {'vote_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique case-reviewer vote; retain before adjudication.'}, 'case_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Case packet being evaluated.'}, 'reviewer_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Fictional R1 or R2; not a real reviewer identity.'}, 'vote': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Original independent quality vote.', 'enum': ['ACCEPT', 'REWORK', 'INSUFFICIENT']}, 'round': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Blind round number; fixture is round1.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['V01', 'C01', 'R1', 'ACCEPT', 1, 'Q13;Q01'], ['V02', 'C01', 'R2', 'ACCEPT', 1, 'Q13;Q01'], ['V03', 'C02', 'R1', 'ACCEPT', 1, 'Q13;Q02'], ['V04', 'C02', 'R2', 'REWORK', 1, 'Q13;Q02'], ['V05', 'C03', 'R1', 'REWORK', 1, 'Q13;Q03'], ['V06', 'C03', 'R2', 'REWORK', 1, 'Q13;Q03'], ['V07', 'C04', 'R1', 'REWORK', 1, 'Q13;Q04'], ['V08', 'C04', 'R2', 'REWORK', 1, 'Q13;Q04'], ['V09', 'C05', 'R1', 'ACCEPT', 1, 'Q13;Q05'], ['V10', 'C05', 'R2', 'ACCEPT', 1, 'Q13;Q05'], ['V11', 'C06', 'R1', 'REWORK', 1, 'Q13;Q06'], ['V12', 'C06', 'R2', 'ACCEPT', 1, 'Q13;Q06'], ['V13', 'C07', 'R1', 'ACCEPT', 1, 'Q13;Q07'], ['V14', 'C07', 'R2', 'ACCEPT', 1, 'Q13;Q07'], ['V15', 'C08', 'R1', 'INSUFFICIENT', 1, 'Q13;Q08'], ['V16', 'C08', 'R2', 'INSUFFICIENT', 1, 'Q13;Q08'], ['V17', 'C09', 'R1', 'ACCEPT', 1, 'Q13;Q09'], ['V18', 'C09', 'R2', 'ACCEPT', 1, 'Q13;Q09'], ['V19', 'C10', 'R1', 'REWORK', 1, 'Q13;Q10'], ['V20', 'C10', 'R2', 'REWORK', 1, 'Q13;Q10'], ['V21', 'C11', 'R1', 'ACCEPT', 1, 'Q13;Q11'], ['V22', 'C11', 'R2', 'INSUFFICIENT', 1, 'Q13;Q11'], ['V23', 'C12', 'R1', 'INSUFFICIENT', 1, 'Q13;Q12'], ['V24', 'C12', 'R2', 'INSUFFICIENT', 1, 'Q13;Q12']], 'primary_key': ['vote_id'], 'grain': 'One original blind case-reviewer assessment;24 votes over12 cases.', 'report_section': 4, 'formats': {'round': '#,##0'}, 'foreign_keys': [{'columns': ['case_id'], 'table': 'CasePackets', 'references': ['case_id']}]}, {'name': 'QualityCriteria', 'columns': ['criterion_id', 'criterion', 'rule', 'materiality_class', 'boundary', 'evidence_ids'], 'column_contracts': {'criterion_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable fixture policy criterion.'}, 'criterion': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Quality dimension being assessed.'}, 'rule': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact authored requirement for this exercise.'}, 'materiality_class': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Potential consequence class.', 'enum': ['MATERIAL', 'ASSESSABILITY', 'NONMATERIAL']}, 'boundary': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Constraint preventing overstatement.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['K01', 'Population completeness', 'Include relevant supplied records or a documented scope exclusion.', 'MATERIAL', 'Missing relevant rows can change amounts, chronology or explanation.', 'Q15'], ['K02', 'Calculation accuracy', 'Reperform stated gross, returns, net and denominator calculations.', 'MATERIAL', 'A correct net cannot replace omitted gross events.', 'Q15'], ['K03', 'Identity substantiation', 'Merge subjects only with adequate supplied identifier linkage.', 'MATERIAL', 'Similar names alone cannot support aggregation.', 'Q15'], ['K04', 'Contrary evidence', 'Address material evidence inconsistent with the proposed conclusion.', 'MATERIAL', 'Reviewers need not prefer the contrary explanation, but must evaluate it.', 'Q15'], ['K05', 'Claim strength', 'Match assertion to evidence class and confidence.', 'MATERIAL', 'Observed timing does not establish intent.', 'Q15'], ['K06', 'Criterion authority', 'Attribute a defect to applicable supplied policy or relevant law with scope.', 'MATERIAL', 'Do not invent a universal nonfiling-document requirement.', 'Q15'], ['K07', 'Reviewability', 'Establish source accessibility and decision-time availability.', 'ASSESSABILITY', 'Unable to assess is separate from a demonstrated investigator defect.', 'Q15'], ['K08', 'Presentation clarity', 'Correct editorial issues that affect comprehension or traceability.', 'NONMATERIAL', 'Pure preference with no consequence is not a quality failure.', 'Q15']], 'primary_key': ['criterion_id'], 'grain': 'One supplied illustrative quality criterion; no implied universal legal mandate.', 'report_section': 5, 'formats': {}}, {'name': 'DefectRegister', 'columns': ['defect_id', 'case_id', 'criterion_id', 'severity', 'materiality', 'condition', 'evidence_ids'], 'column_contracts': {'defect_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique demonstrated quality defect; not every unknown becomes a defect.'}, 'case_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Affected case packet.'}, 'criterion_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Applicable supplied criterion.'}, 'severity': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Illustrative severity based on consequence.', 'enum': ['HIGH', 'MEDIUM', 'LOW']}, 'materiality': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Whether error can affect the substantive case reasoning.', 'enum': ['MATERIAL', 'NONMATERIAL']}, 'condition': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific factual or reasoning defect.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['D01', 'C02', 'K04', 'MEDIUM', 'MATERIAL', 'Contrary matched invoice and delivery omitted', 'Q02;Q15'], ['D02', 'C03', 'K02', 'HIGH', 'MATERIAL', 'USD11000 minus USD2000 is USD9000, not zero', 'Q03;Q15'], ['D03', 'C04', 'K03', 'HIGH', 'MATERIAL', 'Unsupported subject merge changes aggregation', 'Q04;Q15'], ['D04', 'C05', 'K08', 'LOW', 'NONMATERIAL', 'Punctuation correction does not affect meaning', 'Q05;Q15'], ['D05', 'C06', 'K01', 'MEDIUM', 'MATERIAL', 'Gross 4000 credit and 3500 debit omitted; net 500', 'Q06;Q15'], ['D06', 'C10', 'K05', 'HIGH', 'MATERIAL', 'Intent claim exceeds evidence of timing', 'Q10;Q15'], ['D07', 'C11', 'K06', 'MEDIUM', 'MATERIAL', 'Universal regulatory documentation premise unsupported', 'Q11;Q15']], 'primary_key': ['defect_id'], 'grain': 'One defect-condition per case/criterion; multiple defects could affect one case.', 'report_section': 5, 'formats': {}, 'foreign_keys': [{'columns': ['case_id'], 'table': 'CasePackets', 'references': ['case_id']}, {'columns': ['criterion_id'], 'table': 'QualityCriteria', 'references': ['criterion_id']}]}, {'name': 'Calibration', 'columns': ['case_id', 'r1_vote', 'r2_vote', 'agreement', 'consensus', 'adjudication_reason', 'evidence_ids'], 'column_contracts': {'case_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Case identifier; one consensus review per case.'}, 'r1_vote': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Original reviewer1 vote.', 'enum': ['ACCEPT', 'REWORK', 'INSUFFICIENT']}, 'r2_vote': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Original reviewer2 vote.', 'enum': ['ACCEPT', 'REWORK', 'INSUFFICIENT']}, 'agreement': {'type': 'boolean', 'nullable': False, 'unit': 'flag', 'description': 'True only if original votes match exactly.'}, 'consensus': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Adjudicated outcome after comparing criteria/evidence.', 'enum': ['ACCEPT', 'REWORK', 'INSUFFICIENT']}, 'adjudication_reason': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Why consensus follows evidence; not majority-rule substitution.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['C01', 'ACCEPT', 'ACCEPT', True, 'ACCEPT', 'No material reasoning defect on supplied packet.', 'Q13;Q14;Q15;Q01'], ['C02', 'ACCEPT', 'REWORK', False, 'REWORK', 'Material contrary evidence omitted; outcome must be reconsidered without assuming reversal.', 'Q13;Q14;Q15;Q02'], ['C03', 'REWORK', 'REWORK', True, 'REWORK', 'Correct net 9000 and review conclusion dependent on the error.', 'Q13;Q14;Q15;Q03'], ['C04', 'REWORK', 'REWORK', True, 'REWORK', 'Split identities and recompute aggregate before reassessing.', 'Q13;Q14;Q15;Q04'], ['C05', 'ACCEPT', 'ACCEPT', True, 'ACCEPT', 'Optional editorial correction; no effect on inference or traceability.', 'Q13;Q14;Q15;Q05'], ['C06', 'REWORK', 'ACCEPT', False, 'REWORK', 'Restore both gross events and recompute period totals; net 500 does not excuse omission.', 'Q13;Q14;Q15;Q06'], ['C07', 'ACCEPT', 'ACCEPT', True, 'ACCEPT', 'Properly bounded analysis; unknown is not itself a quality failure.', 'Q13;Q14;Q15;Q07'], ['C08', 'INSUFFICIENT', 'INSUFFICIENT', True, 'INSUFFICIENT', 'Review cannot determine whether the underlying conclusion is supported.', 'Q13;Q14;Q15;Q08'], ['C09', 'ACCEPT', 'ACCEPT', True, 'ACCEPT', 'Style preference alone is not a defect.', 'Q13;Q14;Q15;Q09'], ['C10', 'REWORK', 'REWORK', True, 'REWORK', 'Remove unsupported intent assertion and reconsider bounded analytical conclusion.', 'Q13;Q14;Q15;Q10'], ['C11', 'ACCEPT', 'INSUFFICIENT', False, 'REWORK', 'Use supplied policy CP-QA-1 and actual case rationale; no universal nonfiling memo requirement.', 'Q13;Q14;Q15;Q11'], ['C12', 'INSUFFICIENT', 'INSUFFICIENT', True, 'INSUFFICIENT', 'Cannot assess original decision under hindsight without an availability chronology.', 'Q13;Q14;Q15;Q12']], 'primary_key': ['case_id'], 'grain': 'One paired case assessment; preserve original votes and later consensus.', 'report_section': 5, 'formats': {}, 'foreign_keys': [{'columns': ['case_id'], 'table': 'CasePackets', 'references': ['case_id']}]}, {'name': 'Remediation', 'columns': ['remediation_id', 'defect_id', 'repair', 'closure_test', 'status', 'evidence_ids'], 'column_contracts': {'remediation_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable proposed repair identifier.'}, 'defect_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Demonstrated defect being addressed.'}, 'repair': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific proposed correction.'}, 'closure_test': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Evidence an independent reviewer would reperform.'}, 'status': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Fixture has proposals only.', 'enum': ['PROPOSED']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['M01', 'D01', 'Evaluate matched invoice and delivery as counterevidence.', 'Revised rationale addresses both sides and any outcome change.', 'PROPOSED', 'Q02;Q16'], ['M02', 'D02', 'Correct gross 11000, return 2000 and net 9000.', 'Recalculate from posted records and inspect affected conclusion.', 'PROPOSED', 'Q03;Q16'], ['M03', 'D03', 'Split unsupported merged subjects.', 'Recompute separate aggregates and verify each identity link.', 'PROPOSED', 'Q04;Q16'], ['M04', 'D04', 'Optionally correct punctuation without altering analytical outcome.', 'Evidence title remains resolvable; no material rework needed.', 'PROPOSED', 'Q05;Q16'], ['M05', 'D05', 'Restore omitted credit 4000 and debit 3500.', 'Reconcile gross flows, net 500 and chronology.', 'PROPOSED', 'Q06;Q16'], ['M06', 'D06', 'Replace unsupported intent assertion with bounded observed pattern.', 'Every remaining proposition matches its evidence class.', 'PROPOSED', 'Q10;Q16'], ['M07', 'D07', 'Apply CP-QA-1 brief-rationale criterion and remove invented legal premise.', 'Assess actual rationale under supplied policy; no automatic regulatory finding.', 'PROPOSED', 'Q11;Q15;Q16']], 'primary_key': ['remediation_id'], 'grain': 'One proposed repair per demonstrated defect; no repair is executed in the fixture.', 'report_section': 5, 'formats': {}, 'foreign_keys': [{'columns': ['defect_id'], 'table': 'DefectRegister', 'references': ['defect_id']}]}, {'name': 'DecisionRecord', 'columns': ['decision_id', 'question', 'status', 'basis', 'evidence_ids'], 'column_contracts': {'decision_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable quality decision gate.'}, 'question': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Decision scope.'}, 'status': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Result under fixture evidence.', 'enum': ['RECORDED', 'INSUFFICIENT', 'NOT_RECORDED']}, 'basis': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact result and denominator meaning.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['D01', 'Calibration consensus', 'RECORDED', '4 ACCEPT,6 REWORK,2 INSUFFICIENT across 12 selected packets', 'Q14'], ['D02', 'Population defect rate', 'INSUFFICIENT', 'Deliberate calibration selection does not support population-rate extrapolation', 'Q15'], ['D03', 'Underlying alert or filing dispositions', 'NOT_RECORDED', 'Quality consensus does not decide customer conduct or SAR outcome', 'Q15'], ['D04', 'Remediation closure', 'NOT_RECORDED', 'Seven proposals exist; no executed repair or closure verification supplied', 'Q16']], 'primary_key': ['decision_id'], 'grain': 'One decision boundary separating quality judgment, population inference and business action.', 'report_section': 5, 'formats': {}}, {'name': 'ProcessQA', 'columns': ['check_id', 'check', 'expected', 'actual', 'result', 'evidence_ids'], 'column_contracts': {'check_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable fixture check.'}, 'check': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Reperformable calculation or boundary.'}, 'expected': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact independent target.'}, 'actual': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Calculated fixture result.'}, 'result': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Analytical result.', 'enum': ['PASS', 'NOT RECORDED']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'evidence identifiers', 'description': 'Semicolon-delimited exact identifiers in the common Evidence register; each must resolve.'}}, 'rows': [['Q01', 'Packet and vote counts', '12 packets;24 votes', '12 / 24', 'PASS', 'Q13'], ['Q02', 'Original agreement', '9 of 12;75.0%', '9 / 12 =75.0%', 'PASS', 'Q13'], ['Q03', 'Reviewer marginals', 'R1 6/4/2; R2 5/4/3', '6/4/2;5/4/3', 'PASS', 'Q13'], ['Q04', 'Chance agreement', '52/144 =36.1111%', '52/144', 'PASS', 'Q13'], ['Q05', 'Cohen kappa', '14/23 =0.6086956522', '14/23', 'PASS', 'Q13'], ['Q06', 'Consensus denominator', '4/12 ACCEPT;6/12 REWORK;2/12 INSUFFICIENT', '33.3%;50.0%;16.7%', 'PASS', 'Q14'], ['Q07', 'Material defect cases', '6 of 10 assessable;6 of 12 selected', '60.0% assessable;50.0% selected', 'PASS', 'Q14;Q15'], ['Q08', 'Defect counts', '7 defects:6 material,1 nonmaterial', '7 / 6 / 1', 'PASS', 'Q14;Q15'], ['Q09', 'Unknown treatment', 'C08/C12 not counted as passes', 'INSUFFICIENT retained', 'PASS', 'Q08;Q12;Q14'], ['Q10', 'Closure authority', 'No executed correction or closure', 'NOT_RECORDED', 'NOT RECORDED', 'Q16']], 'primary_key': ['check_id'], 'grain': 'One reperformable quality metric or authorization check.', 'report_section': 5, 'formats': {}}], 'findings': [{'id': 'AQA-F01', 'title': 'Six packets need substantive rework under the fixture rubric', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['Q02', 'Q03', 'Q04', 'Q06', 'Q10', 'Q11', 'Q14', 'Q15'], 'detail': 'Consensus identifies six material-defect cases among twelve deliberately selected packets. This is 50.0% of selected packets or 60.0% of ten assessable packets; it is not a population defect estimate.', 'recommendation': 'Correct each case-specific defect and reperform its closure test before claiming repair.'}, {'id': 'AQA-F02', 'title': 'Two packets remain unassessable', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['Q08', 'Q12', 'Q14'], 'detail': 'C08 lacks accessible cited evidence; C12 lacks decision-time availability chronology. Neither is counted as an acceptable case or a demonstrated investigator defect.', 'recommendation': 'Obtain the missing reviewability inputs and reassess under the original decision-time frame.'}, {'id': 'AQA-F03', 'title': 'Original reviewer agreement is incomplete', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['Q13', 'Q14'], 'detail': 'Original votes agree on 9/12 cases (75.0%); unweighted Cohen kappa is 14/23, approximately 0.6087. Adjudication later produces consensus without erasing three disagreements.', 'recommendation': 'Use C02/C06/C11 for criterion calibration; preserve original votes and track later rounds separately.'}, {'id': 'AQA-F04', 'title': 'One nonmaterial editorial defect does not require substantive rework', 'severity': 'LOW', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['Q05', 'Q14', 'Q15'], 'detail': 'C05 has one punctuation defect without effect on calculation, evidence linkage or conclusion. Its consensus status remains ACCEPT under the fixture rubric.', 'recommendation': 'Record optional correction without treating style preference as a material quality failure.'}], 'evidence': [{'id': 'Q01', 'title': 'Fictional case packet C01', 'locator': '10-worked-example.md, Raw packet C01', 'claim_class': 'Observed'}, {'id': 'Q02', 'title': 'Fictional case packet C02', 'locator': '10-worked-example.md, Raw packet C02', 'claim_class': 'Observed'}, {'id': 'Q03', 'title': 'Fictional case packet C03', 'locator': '10-worked-example.md, Raw packet C03', 'claim_class': 'Observed'}, {'id': 'Q04', 'title': 'Fictional case packet C04', 'locator': '10-worked-example.md, Raw packet C04', 'claim_class': 'Observed'}, {'id': 'Q05', 'title': 'Fictional case packet C05', 'locator': '10-worked-example.md, Raw packet C05', 'claim_class': 'Observed'}, {'id': 'Q06', 'title': 'Fictional case packet C06', 'locator': '10-worked-example.md, Raw packet C06', 'claim_class': 'Observed'}, {'id': 'Q07', 'title': 'Fictional case packet C07', 'locator': '10-worked-example.md, Raw packet C07', 'claim_class': 'Observed'}, {'id': 'Q08', 'title': 'Fictional case packet C08', 'locator': '10-worked-example.md, Raw packet C08', 'claim_class': 'Observed'}, {'id': 'Q09', 'title': 'Fictional case packet C09', 'locator': '10-worked-example.md, Raw packet C09', 'claim_class': 'Observed'}, {'id': 'Q10', 'title': 'Fictional case packet C10', 'locator': '10-worked-example.md, Raw packet C10', 'claim_class': 'Observed'}, {'id': 'Q11', 'title': 'Fictional case packet C11', 'locator': '10-worked-example.md, Raw packet C11', 'claim_class': 'Observed'}, {'id': 'Q12', 'title': 'Fictional case packet C12', 'locator': '10-worked-example.md, Raw packet C12', 'claim_class': 'Observed'}, {'id': 'Q13', 'title': 'Fictional review votes', 'locator': '10-worked-example.md, Raw votes R1/R2 across C01–C12', 'claim_class': 'Observed'}, {'id': 'Q14', 'title': 'Fictional adjudication minutes', 'locator': '10-worked-example.md, Consensus C01–C12', 'claim_class': 'Observed'}, {'id': 'Q15', 'title': 'Illustrative quality policy CP-QA-1', 'locator': '10-worked-example.md, Eight criterion cards', 'claim_class': 'Observed'}, {'id': 'Q16', 'title': 'Fictional remediation proposals', 'locator': '10-worked-example.md, Remediation D01–D07', 'claim_class': 'Observed'}], 'metrics': [{'label': 'Case packets reviewed', 'value': 12, 'method': 'Unique C01–C12 selected deliberately for calibration', 'format': '#,##0'}, {'label': 'Original review votes', 'value': 24, 'method': 'Two reviewers per case; distinct from case count', 'format': '#,##0'}, {'label': 'Original exact agreement', 'value': 0.75, 'format': '0.0%', 'method': '9 identical original vote pairs /12 paired cases'}, {'label': 'Unweighted Cohen kappa', 'value': 0.6086956521739131, 'format': '0.0000', 'method': '(9/12 -52/144)/(1 -52/144); nominal three-category votes; no universal adequacy cutoff'}, {'label': 'Selected cases needing rework', 'value': 0.5, 'format': '0.0%', 'method': '6 consensus REWORK /12 selected packets; not extrapolated'}, {'label': 'Assessable-case material defect ratio', 'value': 0.6, 'format': '0.0%', 'method': '6 material-defect cases /(12 selected -2 INSUFFICIENT); excluded unknowns displayed separately'}], 'limitations': ['All case packets, reviewers, decisions and policy are fictional.', 'Deliberate calibration selection does not support a population defect estimate or statistical assurance.', 'Quality consensus does not determine suspicious activity, customer conduct or filing obligations.', 'C08/C12 cannot be assessed until their reviewability gaps are resolved.', 'No proposed repair has been executed and no actual authorized closure has been supplied.'], 'conclusion': 'The calibration set contains four acceptable packets, six requiring substantive rework and two unassessable packets. Original reviewer agreement is 75.0% with kappa 0.6087; consensus preserves rather than replaces the original disagreements.', 'report_narrative': [['The calibration set contains four acceptable packets, six requiring substantive rework and two unassessable packets. Original reviewer agreement is 75.0% with kappa 0.6087; consensus preserves rather than replaces the original disagreements.'], ['Twelve deliberately selected fictional case packets, two original blind reviewers each, supplied illustrative policy CP-QA-1 and a separate consensus round. No random sample or population estimate.', 'The supplied rubric separates material reasoning defects, reviewability limitations and nonmaterial presentation issues. Criteria are illustrative internal policy and must not be described as universal legal requirements.'], ['AQA-F01: Consensus identifies six material-defect cases among twelve deliberately selected packets. This is 50.0% of selected packets or 60.0% of ten assessable packets; it is not a population defect estimate.', 'AQA-F02: C08 lacks accessible cited evidence; C12 lacks decision-time availability chronology. Neither is counted as an acceptable case or a demonstrated investigator defect.', 'AQA-F03: Original votes agree on 9/12 cases (75.0%); unweighted Cohen kappa is 14/23, approximately 0.6087. Adjudication later produces consensus without erasing three disagreements.', 'AQA-F04: C05 has one punctuation defect without effect on calculation, evidence linkage or conclusion. Its consensus status remains ACCEPT under the fixture rubric.'], ['C01–C12 are the complete selected packet population. Twenty-four original votes are retained before adjudication. Reviewers agree on C01/C03/C04/C05/C07/C08/C09/C10/C12 and disagree on C02/C06/C11.'], ['R1 marginals are 6 ACCEPT,4 REWORK,2 INSUFFICIENT; R2 marginals are 5/4/3. Chance agreement is(6×5+4×4+2×3)/144=52/144. Kappa is(9/12-52/144)/(1-52/144)=14/23. No universal adequacy threshold is applied.', 'Consensus produces 4 ACCEPT,6 REWORK and 2 INSUFFICIENT. Seven demonstrated defects include 6 material and 1 nonmaterial across 7 cases. Six material cases divide by 12 selected packets for 50.0% or 10 assessable packets for 60.0%; the two unknowns are explicit in both presentations.', 'Seven repairs are proposed with case-specific closure tests. C05 stays ACCEPT because its punctuation defect has no substantive effect. C08/C12 require reviewability inputs, not invented investigator-error findings.'], ['Q01–Q12 are the individual packets; Q13 preserves original votes; Q14 records later consensus; Q15 supplies the illustrative criteria; Q16 contains proposed remediation. Original decision-time availability must be established before applying later evidence to a prior adjudication.'], ['Correct omitted counterevidence, reversal arithmetic, unsupported identity merging, incomplete chronology, unsupported intent and criterion provenance. Obtain accessible evidence for C08 and a decision-time availability chronology for C12. Keep all repairs proposed until execution and independent verification are supplied.'], ['All case packets, reviewers, decisions and policy are fictional.', 'Deliberate calibration selection does not support a population defect estimate or statistical assurance.', 'Quality consensus does not determine suspicious activity, customer conduct or filing obligations.', 'C08/C12 cannot be assessed until their reviewability gaps are resolved.', 'No proposed repair has been executed and no actual authorized closure has been supplied.', 'Fixture metrics reperform correctly. Human business disposition and remediation closure remain NOT_RECORDED.']], 'suite_id': 'alert-qa', 'version': '1.2.0', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.', 'methods': ['Confirm the question, authorized scope, period, population and available capabilities.', 'Preserve evidence identifiers and reconcile received, excluded, duplicate and unresolved records.', 'Apply the suite method and decision rules; test competing explanations and missing inputs.', 'Populate the fixed domain registers without inventing fields, facts or approvals.', 'Review calculations and citations; record exceptions and seek the named human disposition.'], 'actions': [{'id': 'A-001', 'finding_id': 'AQA-F01', 'proposal': 'Correct each case-specific defect and reperform its closure test before claiming repair.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-002', 'finding_id': 'AQA-F02', 'proposal': 'Obtain the missing reviewability inputs and reassess under the original decision-time frame.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-003', 'finding_id': 'AQA-F03', 'proposal': 'Use C02/C06/C11 for criterion calibration; preserve original votes and track later rounds separately.', 'owner': None, 'due_date': None, 'status': 'Proposed'}, {'id': 'A-004', 'finding_id': 'AQA-F04', 'proposal': 'Record optional correction without treating style preference as a material quality failure.', 'owner': None, 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Synthetic fixture calculations', 'result': 'REVIEW REQUIRED', 'evidence': 'Reproduce the arithmetic in file 10.'}, {'id': 'QA-02', 'check': 'Evidence support and competing explanations', 'result': 'REVIEW REQUIRED', 'evidence': 'Compare findings to the exact fixture locators and file 04.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No reviewer identity, decision or approval has been supplied.'}]}
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
