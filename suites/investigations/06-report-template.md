# Investigation Case Review — fixed report template

Version 1.2.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Decision questions and current assessment**
2. **Scope, chronology method, and coverage**
3. **Findings and contradictions**
4. **Chronology and funds movement**
5. **Competing hypothesis tests and decision gates**
6. **Evidence inventory and provenance**
7. **Proposed investigative actions**
8. **Limitations, quality checks, and reviewer decision**

Keep all eight sections, including a specific limitation if a section cannot be assessed. Within section 1 state the answer, decision implication and unresolved gate before background. Section 2 records jurisdiction, as-of date, population, exclusions and method version. Section 3 carries each finding with class, severity, confidence, evidence, counterevidence and proposed action. Sections 4–5 preserve every domain register in file 05, with one named subsection per table and every row retained. Table metadata fixes placement in section 4 or 5. Section 6 contains exact evidence locators. Section 7 records proposed actions. Section 8 contains limitations, QA outcomes and the named human disposition.

The code's prose is a complete **synthetic specimen**, not boilerplate conclusions for later cases. Replace each `report_narrative` paragraph with case-specific analysis. Do not publish sample judgments as real results. Retain the data label while any synthetic records remain.

## Word and PDF style contract

| Element | Fixed treatment |
| --- | --- |
| Page | Portrait report; 0.75-inch left/right and 0.70-inch top/bottom margins |
| Typeface | Arial 10.5 pt body; 24 pt title; 16 pt first-level and 12 pt second-level headings; sans-serif fallback |
| Color | Ink `#243641`; headings `#344E5F`; neutral table shading; black title |
| Paragraph | 1.12 line spacing; 7 pt after; headings keep with following paragraph |
| Tables | 9 pt minimum; repeat header rows; long domain registers shown as field/value records to avoid tiny columns |
| Figures | No decorative graphics; every quantitative visual needs its unit, scope, denominator and source |
| Footer | Draft for human review; automatic page number |
| PDF | Export the verified Word document or print the HTML template; do not merely rename the extension |
| Dates and money | Archive/field dates `YYYY-MM-DD`; narrative dates `MMM DD, YYYY`; times `h:mm AM/PM ET`; currency symbol and comma separators |

The workbook retains every domain column in order; the report may present the same records vertically for readability. Do not merge duplicate-looking records unless the method supports deduplication. Never hide counterevidence, omit an unresolved record, or replace a null with a favorable sentence.

## Required content review

- Trace each material sentence to its source span, row, calculation or explicit inference. A URL alone is not evidence of retrieval.
- Preserve the distinction between a source allegation and an adjudicated fact. Add the source's date and procedural status where relevant.
- Tie totals and exclusions to the worked population or supplied control totals. When unknown, state the resulting limitation.
- Keep a proposed action distinct from the human disposition and from execution. This renderer records no approval.
- Reopen the actual deliverable. Check page breaks, repeated headers, complete rows, dates, metadata and citations. If visual review is unavailable, say so.

## Complete in-session renderer

For portable case data, write integer fields and report placement as whole-number JSON literals such as `1` and `4`, without a decimal suffix. Python enforces integer types; JavaScript parses `1` and `1.0` as the same number. HTML rejects integers outside JavaScript's safe range, and Excel applies its stricter 15-digit boundary. Preserve exact large identifiers or quantities as text under the declared field contract. These runtime constraints are not identical validators or a guarantee of exact floating-point arithmetic.

The code block is self-contained. Its only runtime dependency is an already available `python-docx`. `DATA` includes all synthetic inputs needed to render the specimen; neither this repository nor a local path is needed in the user's session. Replace data values, not section order or column identifiers. Add evidence and case-specific narrative before calling the result complete.

```python
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

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

OUTPUT = Path(DATA['suite_id'] + '-report.docx')
doc = Document()
doc.core_properties.author = 'Markdown Analyst Toolkit'
doc.core_properties.title = DATA['title']
doc.core_properties.subject = DATA['notice']
section = doc.sections[0]
section.top_margin = section.bottom_margin = Inches(0.7)
section.left_margin = section.right_margin = Inches(0.75)
normal = doc.styles['Normal']
normal.font.name = 'Arial'
normal.font.size = Pt(10.5)
normal.font.color.rgb = RGBColor.from_string('243641')
normal.paragraph_format.space_after = Pt(7)
normal.paragraph_format.line_spacing = 1.12
for name, size in [('Title',24), ('Heading 1',16), ('Heading 2',12)]:
    style = doc.styles[name]
    style.font.name = 'Arial'
    style.font.size = Pt(size)
    style.font.color.rgb = RGBColor.from_string('000000' if name=='Title' else '344E5F')
    style.paragraph_format.keep_with_next = True
    style.paragraph_format.space_before = Pt(14)
    style.paragraph_format.space_after = Pt(7)
for style in [normal, doc.styles['Title'], doc.styles['Heading 1'], doc.styles['Heading 2'], doc.styles['List Bullet']]:
    style.font.name = 'Arial'
    fonts = style.element.get_or_add_rPr().rFonts
    if fonts is not None:
        for key in list(fonts.attrib):
            if 'theme' in key.lower():
                del fonts.attrib[key]
    for border in list(style.element.iter(qn('w:pBdr'))):
        border.getparent().remove(border)

def text(value):
    return 'Not provided' if value is None else str(value).lower() if isinstance(value,bool) else '; '.join(map(str,value)) if isinstance(value,list) else str(value)

def formatted(value, fmt):
    if type(value) not in (int,float) or not fmt:
        return text(value)
    if fmt == '0.0%':
        return f'{value:.1%}'
    if fmt == '0.0"%"':
        return f'{value:.1f}%'
    decimal = re.search(r'\.([0#]+)', fmt)
    places = len(decimal.group(1)) if decimal else 0
    number = f'{value:,}' + ('.'+'0'*places if places else '') if isinstance(value,int) else f'{value:,.{places}f}'
    return ('$' if '$' in fmt else '') + number

def table(headers, rows, keep_together=False, widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = 'Table Grid'
    if widths:
        t.autofit = False
        for column,width in zip(t.columns,widths):column.width=Inches(width)
    for i,h in enumerate(headers):
        t.rows[0].cells[i].text = h
    repeat = OxmlElement('w:tblHeader')
    t.rows[0]._tr.get_or_add_trPr().append(repeat)
    for values in rows:
        cells=t.add_row().cells
        for i,v in enumerate(values):
            cells[i].text=text(v)
    for row_index,row in enumerate(t.rows):
        if row_index==0 or max(len(cell.text) for cell in row.cells)<=1200:
            row._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
        for cell_index,cell in enumerate(row.cells):
            if widths:cell.width=Inches(widths[cell_index])
            shading=OxmlElement('w:shd')
            shading.set(qn('w:fill'),'344E5F' if row_index==0 else 'E2E8E9' if row_index%2 else 'F1F2EF')
            cell._tc.get_or_add_tcPr().append(shading)
            for p in cell.paragraphs:
                p.paragraph_format.space_after=Pt(4)
                if keep_together and row_index<len(t.rows)-1:
                    p.paragraph_format.keep_with_next=True
                for run in p.runs:
                    run.font.name='Arial'
                    run.font.size=Pt(9)
                    run.font.color.rgb=RGBColor.from_string('FFFFFF' if row_index==0 else '243641')
                    run.font.bold=row_index==0
    doc.add_paragraph()
    return t

doc.add_paragraph(DATA['title'], 'Title')
doc.add_paragraph(f"Version {DATA['version']} | As of {DATA['as_of']} | Draft for human review")
doc.add_paragraph(DATA['notice'])
doc.add_paragraph(DATA['summary'])
doc.add_paragraph('Decision supported: '+DATA['decision'])
for index, heading in enumerate(DATA['report_sections']):
    doc.add_heading(heading, level=1)
    for paragraph in DATA['report_narrative'][index]:
        doc.add_paragraph(paragraph)
    if index == 0:
        table(['Measure','Value','Calculation or limit'], [[m['label'],formatted(m['value'],m.get('format')),m['method']] for m in DATA['metrics']])
    elif index == 2:
        for f in DATA['findings']:
            doc.add_heading(f["id"]+' '+f['title'], level=2)
            meta=doc.add_paragraph(f"{f['severity']} severity | {f['confidence']} confidence | {f['claim_class']} | Evidence: {', '.join(f['evidence_ids'])}")
            meta.paragraph_format.keep_with_next=True
            doc.add_paragraph(f['detail'])
            doc.add_paragraph('Proposed action: '+f['recommendation'])
    elif index in (3,4):
        for position,source in enumerate(DATA['domain_tables']):
            if source.get('report_section',4 if position==0 else 5)!=index+1:continue
            doc.add_heading(source['name'],level=2)
            if source.get('grain'):doc.add_paragraph('Record grain: '+source['grain'])
            if not source['rows']:
                doc.add_paragraph('No records supplied. Declared columns: '+', '.join(source['columns'])+'. An empty register does not establish a clean population.')
            for number,row in enumerate(source['rows'],1):
                label=doc.add_paragraph(f"{source['name']} / record {number} of {len(source['rows'])}")
                label.paragraph_format.keep_with_next=True
                # Long records may continue between field rows instead of overflowing a page.
                table(['Field','Value'], [(key,formatted(value,source.get('formats',{}).get(key))) for key,value in zip(source['columns'],row)],keep_together=False,widths=[2.0,5.0])
            missing = sum(value is None for row in source['rows'] for value in row)
            doc.add_paragraph(f"Domain record count: {len(source['rows'])}. Missing (null) cells: {missing}. Empty text follows the field-specific contract.")
    elif index == 5:
        table(['Evidence ID','Source or fixture','Exact locator','Claim class'], [[e['id'],e['title'],e['locator'],e['claim_class']] for e in DATA['evidence']],widths=[1.0,2.0,2.8,1.2])
    elif index == 6:
        for a in DATA['actions']:
            doc.add_paragraph(f"{a['id']} / {a['finding_id']}: {a['proposal']} Owner: {text(a['owner'])}. Due: {text(a['due_date'])}. State: {a['status']}")
    elif index == 7:
        for value in DATA['limitations']:
            doc.add_paragraph(value, style='List Bullet')
        table(['Check ID','Check','Result','Evidence'], [[q['id'],q['check'],q['result'],q['evidence']] for q in DATA['qa']])
footer = section.footer.paragraphs[0]
footer.add_run('Draft for human review | Page ')
field=OxmlElement('w:fldSimple')
field.set(qn('w:instr'),'PAGE')
footer._p.append(field)
doc.save(OUTPUT)
print(str(OUTPUT))

```

## Recovery and acceptance

If generation fails, preserve the completed analytical text and the exact error category. Retry only the failed render step after checking the capability; do not redo source judgments to obtain a prettier report. Never claim DOCX or PDF export succeeded unless an openable file exists. A successful renderer run proves file creation, not truth, regulatory compliance, or institutional approval.
