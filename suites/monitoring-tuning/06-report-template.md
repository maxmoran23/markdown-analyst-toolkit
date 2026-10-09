# Monitoring Scenario and Threshold Review — fixed report template

Version 1.2.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Candidate recommendation and restrictions**
2. **Evaluation scope and partition controls**
3. **Coverage workload and routing findings**
4. **Complete candidate and population registers**
5. **Below-threshold review and decision gates**
6. **Evidence provenance uncertainty and blind spots**
7. **Validation and change proposals**
8. **Limitations quality review and human disposition**

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

DATA = {'slug': 'monitoring-tuning', 'title': 'Monitoring Scenario and Threshold Review', 'summary': 'Evaluate complete monitoring candidates through protected partitions, labels, routing, workload, below-threshold review and human change gates.', 'audience': 'Monitoring analysts, independent challenge reviewers and accountable human decision makers', 'decision': 'Which frozen candidate merits further validation, and which data, routing or governance gaps block a human change decision?', 'palette': 'indigo', 'as_of': '2026-10-09', 'scope': 'Complete fictional inputs printed in file 10 only. Public authorities provide context, not evidence about the fictional subjects or an institution-specific mandate.', 'report_sections': ['Candidate recommendation and restrictions', 'Evaluation scope and partition controls', 'Coverage workload and routing findings', 'Complete candidate and population registers', 'Below-threshold review and decision gates', 'Evidence provenance uncertainty and blind spots', 'Validation and change proposals', 'Limitations quality review and human disposition'], 'domain_tables': [{'name': 'Population', 'columns': ['unit_id', 'group_id', 'partition', 'segment', 'score', 'label', 'label_basis', 'eligible', 'suppressed', 'review_hours', 'evidence_ids'], 'column_contracts': {'unit_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'One scored customer-window; never a transaction count.'}, 'group_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Frozen merge/dependence group containing two units in one partition.'}, 'partition': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Prospectively assigned evaluation partition.', 'enum': ['TRAIN', 'VALIDATION', 'HOLDOUT']}, 'segment': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Frozen customer segment.', 'enum': ['RETAIL', 'SMALL_BUSINESS', 'CORRESPONDENT']}, 'score': {'type': 'number', 'nullable': False, 'unit': 'score', 'description': 'Supplied deterministic score on a 0 to 100 scale.'}, 'label': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Available fictional review outcome as of cutoff.', 'enum': ['POSITIVE', 'NEGATIVE', 'UNKNOWN', 'CENSORED']}, 'label_basis': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Provenance or reason the label is not mature.'}, 'eligible': {'type': 'boolean', 'nullable': False, 'unit': 'flag', 'description': 'Whether the supplied unit meets the frozen population predicate.'}, 'suppressed': {'type': 'boolean', 'nullable': False, 'unit': 'flag', 'description': 'Whether group G17 is removed by the illustrative suppression list.'}, 'review_hours': {'type': 'number', 'nullable': False, 'unit': 'hours', 'description': 'Fixed lead-case workload assumption by segment, before merge additions.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Supporting synthetic source IDs.'}}, 'primary_key': ['unit_id'], 'rows': [['U01', 'G01', 'TRAIN', 'RETAIL', 82, 'POSITIVE', 'Fictional closed review', True, False, 1, 'SYN-001'], ['U02', 'G01', 'TRAIN', 'RETAIL', 67, 'NEGATIVE', 'Fictional closed review', True, False, 1, 'SYN-001'], ['U03', 'G02', 'TRAIN', 'RETAIL', 56, 'POSITIVE', 'Fictional closed review', True, False, 1, 'SYN-001'], ['U04', 'G02', 'TRAIN', 'RETAIL', 32, 'NEGATIVE', 'Fictional closed review', True, False, 1, 'SYN-001'], ['U05', 'G03', 'TRAIN', 'SMALL_BUSINESS', 88, 'POSITIVE', 'Fictional closed review', True, False, 1.5, 'SYN-001'], ['U06', 'G03', 'TRAIN', 'SMALL_BUSINESS', 72, 'NEGATIVE', 'Fictional closed review', True, False, 1.5, 'SYN-001'], ['U07', 'G04', 'TRAIN', 'SMALL_BUSINESS', 58, 'POSITIVE', 'Fictional closed review', True, False, 1.5, 'SYN-001'], ['U08', 'G04', 'TRAIN', 'SMALL_BUSINESS', 44, 'UNKNOWN', 'Review evidence unavailable', True, False, 1.5, 'SYN-001'], ['U09', 'G05', 'TRAIN', 'CORRESPONDENT', 93, 'POSITIVE', 'Fictional closed review', True, False, 2, 'SYN-001'], ['U10', 'G05', 'TRAIN', 'CORRESPONDENT', 77, 'NEGATIVE', 'Fictional closed review', True, False, 2, 'SYN-001'], ['U11', 'G06', 'TRAIN', 'CORRESPONDENT', 63, 'POSITIVE', 'Fictional closed review', True, False, 2, 'SYN-001'], ['U12', 'G06', 'TRAIN', 'CORRESPONDENT', 39, 'CENSORED', 'Outcome window not mature', True, False, 2, 'SYN-001'], ['U13', 'G07', 'VALIDATION', 'RETAIL', 79, 'POSITIVE', 'Fictional closed review', True, False, 1, 'SYN-001'], ['U14', 'G07', 'VALIDATION', 'RETAIL', 64, 'NEGATIVE', 'Fictional closed review', True, False, 1, 'SYN-001'], ['U15', 'G08', 'VALIDATION', 'RETAIL', 54, 'POSITIVE', 'Fictional closed review', True, False, 1, 'SYN-001'], ['U16', 'G08', 'VALIDATION', 'RETAIL', 28, 'NEGATIVE', 'Fictional closed review', True, False, 1, 'SYN-001'], ['U17', 'G09', 'VALIDATION', 'SMALL_BUSINESS', 86, 'POSITIVE', 'Fictional closed review', True, False, 1.5, 'SYN-001'], ['U18', 'G09', 'VALIDATION', 'SMALL_BUSINESS', 69, 'NEGATIVE', 'Fictional closed review', True, False, 1.5, 'SYN-001'], ['U19', 'G10', 'VALIDATION', 'SMALL_BUSINESS', 57, 'UNKNOWN', 'Review evidence unavailable', True, False, 1.5, 'SYN-001'], ['U20', 'G10', 'VALIDATION', 'SMALL_BUSINESS', 42, 'NEGATIVE', 'Fictional closed review', True, False, 1.5, 'SYN-001'], ['U21', 'G11', 'VALIDATION', 'CORRESPONDENT', 91, 'POSITIVE', 'Fictional closed review', True, False, 2, 'SYN-001'], ['U22', 'G11', 'VALIDATION', 'CORRESPONDENT', 74, 'NEGATIVE', 'Fictional closed review', True, False, 2, 'SYN-001'], ['U23', 'G12', 'VALIDATION', 'CORRESPONDENT', 61, 'POSITIVE', 'Fictional closed review', True, False, 2, 'SYN-001'], ['U24', 'G12', 'VALIDATION', 'CORRESPONDENT', 36, 'CENSORED', 'Outcome window not mature', True, False, 2, 'SYN-001'], ['U25', 'G13', 'HOLDOUT', 'RETAIL', 81, 'POSITIVE', 'Fictional closed review', True, False, 1, 'SYN-001'], ['U26', 'G13', 'HOLDOUT', 'RETAIL', 66, 'NEGATIVE', 'Fictional closed review', True, False, 1, 'SYN-001'], ['U27', 'G14', 'HOLDOUT', 'RETAIL', 53, 'POSITIVE', 'Fictional closed review', True, False, 1, 'SYN-001'], ['U28', 'G14', 'HOLDOUT', 'RETAIL', 31, 'UNKNOWN', 'Review evidence unavailable', True, False, 1, 'SYN-001'], ['U29', 'G15', 'HOLDOUT', 'SMALL_BUSINESS', 84, 'POSITIVE', 'Fictional closed review', True, False, 1.5, 'SYN-001'], ['U30', 'G15', 'HOLDOUT', 'SMALL_BUSINESS', 71, 'NEGATIVE', 'Fictional closed review', True, False, 1.5, 'SYN-001'], ['U31', 'G16', 'HOLDOUT', 'SMALL_BUSINESS', 59, 'POSITIVE', 'Fictional closed review', True, False, 1.5, 'SYN-001'], ['U32', 'G16', 'HOLDOUT', 'SMALL_BUSINESS', 41, 'NEGATIVE', 'Fictional closed review', True, False, 1.5, 'SYN-001'], ['U33', 'G17', 'HOLDOUT', 'CORRESPONDENT', 94, 'POSITIVE', 'Fictional closed review', True, True, 2, 'SYN-001'], ['U34', 'G17', 'HOLDOUT', 'CORRESPONDENT', 76, 'NEGATIVE', 'Fictional closed review', True, True, 2, 'SYN-001'], ['U35', 'G18', 'HOLDOUT', 'CORRESPONDENT', 62, 'UNKNOWN', 'Review evidence unavailable', True, False, 2, 'SYN-001'], ['U36', 'G18', 'HOLDOUT', 'CORRESPONDENT', 37, 'CENSORED', 'Outcome window not mature', True, False, 2, 'SYN-001']], 'formats': {'review_hours': '0.00'}, 'grain': 'One eligible scored customer-window unit, identified by unit_id, before candidate selection or routing.'}, {'name': 'Candidates', 'columns': ['candidate_id', 'retail_threshold', 'business_threshold', 'correspondent_threshold', 'comparator', 'freeze_state', 'evidence_ids'], 'column_contracts': {'candidate_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Frozen candidate key.'}, 'retail_threshold': {'type': 'number', 'nullable': False, 'unit': 'score', 'description': 'Inclusive RETAIL score cutoff.'}, 'business_threshold': {'type': 'number', 'nullable': False, 'unit': 'score', 'description': 'Inclusive SMALL_BUSINESS score cutoff.'}, 'correspondent_threshold': {'type': 'number', 'nullable': False, 'unit': 'score', 'description': 'Inclusive CORRESPONDENT score cutoff.'}, 'comparator': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact comparison operator.', 'enum': ['GREATER_OR_EQUAL']}, 'freeze_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'All candidates declared before examining protected results.', 'enum': ['ILLUSTRATIVE_PREFROZEN']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Parameter evidence ID.'}}, 'primary_key': ['candidate_id'], 'rows': [['BASE60', 60, 60, 60, 'GREATER_OR_EQUAL', 'ILLUSTRATIVE_PREFROZEN', 'SYN-002'], ['HIGH75', 75, 75, 75, 'GREATER_OR_EQUAL', 'ILLUSTRATIVE_PREFROZEN', 'SYN-002'], ['LOW50', 50, 50, 50, 'GREATER_OR_EQUAL', 'ILLUSTRATIVE_PREFROZEN', 'SYN-002'], ['SEGMENTED', 55, 60, 65, 'GREATER_OR_EQUAL', 'ILLUSTRATIVE_PREFROZEN', 'SYN-002']], 'grain': 'One frozen candidate configuration, identified by candidate_id, containing all three segment thresholds.'}, {'name': 'CandidateMetrics', 'columns': ['candidate_id', 'partition', 'population_n', 'known_n', 'tp', 'fp', 'fn', 'tn', 'unknown_n', 'raw_hits', 'retained_hits', 'queued_cases', 'workload_hours', 'precision', 'recall', 'retained_positive_hits'], 'column_contracts': {'candidate_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Candidate key.'}, 'partition': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Evaluation partition or ALL descriptive reconciliation.', 'enum': ['TRAIN', 'VALIDATION', 'HOLDOUT', 'ALL']}, 'population_n': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'All eligible supplied units in this partition.'}, 'known_n': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'POSITIVE plus NEGATIVE units only.'}, 'tp': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Known positive unit meeting the raw predicate before routing.'}, 'fp': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Known negative unit meeting the raw predicate.'}, 'fn': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Known positive unit below the raw predicate.'}, 'tn': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Known negative unit below the raw predicate.'}, 'unknown_n': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'UNKNOWN plus CENSORED units outside the confusion matrix.'}, 'raw_hits': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'All units meeting the predicate, including unavailable labels.'}, 'retained_hits': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Raw hits remaining after suppression, before group merge.'}, 'queued_cases': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Distinct retained group IDs; not a unit count.'}, 'workload_hours': {'type': 'number', 'nullable': False, 'unit': 'hours', 'description': 'Lead hours plus 0.25 hours for every additional retained unit in a group.'}, 'precision': {'type': 'number', 'nullable': True, 'unit': 'ratio', 'description': 'TP divided by TP plus FP on available labels.'}, 'recall': {'type': 'number', 'nullable': True, 'unit': 'ratio', 'description': 'TP divided by TP plus FN on available labels.'}, 'retained_positive_hits': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Known positive units reaching a queued case; this does not credit unhit siblings.'}}, 'primary_key': ['candidate_id', 'partition'], 'rows': [['BASE60', 'TRAIN', 12, 10, 4, 3, 2, 1, 2, 7, 7, 4, 7.25, 0.5714285714285714, 0.6666666666666666, 4], ['BASE60', 'VALIDATION', 12, 10, 4, 3, 1, 2, 2, 7, 7, 4, 7.25, 0.5714285714285714, 0.8, 4], ['BASE60', 'HOLDOUT', 12, 9, 3, 3, 2, 1, 3, 7, 5, 3, 5.0, 0.5, 0.6, 2], ['BASE60', 'ALL', 36, 29, 11, 9, 5, 4, 7, 21, 19, 11, 19.5, 0.55, 0.6875, 10], ['HIGH75', 'TRAIN', 12, 10, 3, 1, 3, 3, 2, 4, 4, 3, 4.75, 0.75, 0.5, 3], ['HIGH75', 'VALIDATION', 12, 10, 3, 0, 2, 5, 2, 3, 3, 3, 4.5, 1.0, 0.6, 3], ['HIGH75', 'HOLDOUT', 12, 9, 3, 1, 2, 3, 3, 4, 2, 2, 2.5, 0.75, 0.6, 2], ['HIGH75', 'ALL', 36, 29, 9, 2, 7, 11, 7, 11, 9, 8, 11.75, 0.8181818181818182, 0.5625, 8], ['LOW50', 'TRAIN', 12, 10, 6, 3, 0, 1, 2, 9, 9, 6, 9.75, 0.6666666666666666, 1.0, 6], ['LOW50', 'VALIDATION', 12, 10, 5, 3, 0, 2, 2, 9, 9, 6, 9.75, 0.625, 1.0, 5], ['LOW50', 'HOLDOUT', 12, 9, 5, 3, 0, 1, 3, 9, 7, 5, 7.5, 0.625, 1.0, 4], ['LOW50', 'ALL', 36, 29, 16, 9, 0, 4, 7, 27, 25, 17, 27.0, 0.64, 1.0, 15], ['SEGMENTED', 'TRAIN', 12, 10, 4, 3, 2, 1, 2, 7, 7, 4, 6.25, 0.5714285714285714, 0.6666666666666666, 4], ['SEGMENTED', 'VALIDATION', 12, 10, 3, 3, 2, 2, 2, 6, 6, 3, 5.25, 0.5, 0.6, 3], ['SEGMENTED', 'HOLDOUT', 12, 9, 3, 3, 2, 1, 3, 6, 4, 2, 3.0, 0.5, 0.6, 2], ['SEGMENTED', 'ALL', 36, 29, 10, 9, 6, 4, 7, 19, 17, 9, 14.5, 0.5263157894736842, 0.625, 9]], 'formats': {'workload_hours': '0.00', 'precision': '0.0%', 'recall': '0.0%'}, 'foreign_keys': [{'columns': ['candidate_id'], 'table': 'Candidates', 'references': ['candidate_id']}], 'grain': 'One candidate_id and partition combination, including a separately labeled ALL reconciliation across the three partitions.'}, {'name': 'AlertRouting', 'columns': ['hit_id', 'candidate_id', 'unit_id', 'group_id', 'route_state', 'case_id', 'lead_unit_id', 'routing_basis', 'evidence_ids'], 'column_contracts': {'hit_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique candidate-unit raw hit key.'}, 'candidate_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Candidate responsible for this raw hit.'}, 'unit_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Exact scored unit; lookup label separately.'}, 'group_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Frozen group used for merging only within a partition.'}, 'route_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Mutually exclusive hit routing outcome.', 'enum': ['SUPPRESSED', 'QUEUED_LEAD', 'MERGED_CHILD']}, 'case_id': {'type': 'text', 'nullable': True, 'unit': 'identifier', 'description': 'Candidate-group queued case key; null for suppressed hits.'}, 'lead_unit_id': {'type': 'text', 'nullable': True, 'unit': 'identifier', 'description': 'Smallest hit unit ID in the retained group; null when suppressed.'}, 'routing_basis': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Evidence or missing authorization underlying the route.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Sources for routing inputs and predicate lineage.'}}, 'primary_key': ['hit_id'], 'rows': [['BASE60-U01', 'BASE60', 'U01', 'G01', 'QUEUED_LEAD', 'BASE60-G01', 'U01', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U02', 'BASE60', 'U02', 'G01', 'MERGED_CHILD', 'BASE60-G01', 'U01', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U05', 'BASE60', 'U05', 'G03', 'QUEUED_LEAD', 'BASE60-G03', 'U05', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U06', 'BASE60', 'U06', 'G03', 'MERGED_CHILD', 'BASE60-G03', 'U05', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U09', 'BASE60', 'U09', 'G05', 'QUEUED_LEAD', 'BASE60-G05', 'U09', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U10', 'BASE60', 'U10', 'G05', 'MERGED_CHILD', 'BASE60-G05', 'U09', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U11', 'BASE60', 'U11', 'G06', 'QUEUED_LEAD', 'BASE60-G06', 'U11', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U13', 'BASE60', 'U13', 'G07', 'QUEUED_LEAD', 'BASE60-G07', 'U13', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U14', 'BASE60', 'U14', 'G07', 'MERGED_CHILD', 'BASE60-G07', 'U13', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U17', 'BASE60', 'U17', 'G09', 'QUEUED_LEAD', 'BASE60-G09', 'U17', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U18', 'BASE60', 'U18', 'G09', 'MERGED_CHILD', 'BASE60-G09', 'U17', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U21', 'BASE60', 'U21', 'G11', 'QUEUED_LEAD', 'BASE60-G11', 'U21', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U22', 'BASE60', 'U22', 'G11', 'MERGED_CHILD', 'BASE60-G11', 'U21', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U23', 'BASE60', 'U23', 'G12', 'QUEUED_LEAD', 'BASE60-G12', 'U23', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U25', 'BASE60', 'U25', 'G13', 'QUEUED_LEAD', 'BASE60-G13', 'U25', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U26', 'BASE60', 'U26', 'G13', 'MERGED_CHILD', 'BASE60-G13', 'U25', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U29', 'BASE60', 'U29', 'G15', 'QUEUED_LEAD', 'BASE60-G15', 'U29', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U30', 'BASE60', 'U30', 'G15', 'MERGED_CHILD', 'BASE60-G15', 'U29', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['BASE60-U33', 'BASE60', 'U33', 'G17', 'SUPPRESSED', None, None, 'Unexpired authorization absent', 'SYN-001;SYN-003'], ['BASE60-U34', 'BASE60', 'U34', 'G17', 'SUPPRESSED', None, None, 'Unexpired authorization absent', 'SYN-001;SYN-003'], ['BASE60-U35', 'BASE60', 'U35', 'G18', 'QUEUED_LEAD', 'BASE60-G18', 'U35', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['HIGH75-U01', 'HIGH75', 'U01', 'G01', 'QUEUED_LEAD', 'HIGH75-G01', 'U01', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['HIGH75-U05', 'HIGH75', 'U05', 'G03', 'QUEUED_LEAD', 'HIGH75-G03', 'U05', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['HIGH75-U09', 'HIGH75', 'U09', 'G05', 'QUEUED_LEAD', 'HIGH75-G05', 'U09', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['HIGH75-U10', 'HIGH75', 'U10', 'G05', 'MERGED_CHILD', 'HIGH75-G05', 'U09', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['HIGH75-U13', 'HIGH75', 'U13', 'G07', 'QUEUED_LEAD', 'HIGH75-G07', 'U13', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['HIGH75-U17', 'HIGH75', 'U17', 'G09', 'QUEUED_LEAD', 'HIGH75-G09', 'U17', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['HIGH75-U21', 'HIGH75', 'U21', 'G11', 'QUEUED_LEAD', 'HIGH75-G11', 'U21', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['HIGH75-U25', 'HIGH75', 'U25', 'G13', 'QUEUED_LEAD', 'HIGH75-G13', 'U25', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['HIGH75-U29', 'HIGH75', 'U29', 'G15', 'QUEUED_LEAD', 'HIGH75-G15', 'U29', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['HIGH75-U33', 'HIGH75', 'U33', 'G17', 'SUPPRESSED', None, None, 'Unexpired authorization absent', 'SYN-001;SYN-003'], ['HIGH75-U34', 'HIGH75', 'U34', 'G17', 'SUPPRESSED', None, None, 'Unexpired authorization absent', 'SYN-001;SYN-003'], ['LOW50-U01', 'LOW50', 'U01', 'G01', 'QUEUED_LEAD', 'LOW50-G01', 'U01', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U02', 'LOW50', 'U02', 'G01', 'MERGED_CHILD', 'LOW50-G01', 'U01', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U03', 'LOW50', 'U03', 'G02', 'QUEUED_LEAD', 'LOW50-G02', 'U03', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U05', 'LOW50', 'U05', 'G03', 'QUEUED_LEAD', 'LOW50-G03', 'U05', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U06', 'LOW50', 'U06', 'G03', 'MERGED_CHILD', 'LOW50-G03', 'U05', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U07', 'LOW50', 'U07', 'G04', 'QUEUED_LEAD', 'LOW50-G04', 'U07', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U09', 'LOW50', 'U09', 'G05', 'QUEUED_LEAD', 'LOW50-G05', 'U09', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U10', 'LOW50', 'U10', 'G05', 'MERGED_CHILD', 'LOW50-G05', 'U09', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U11', 'LOW50', 'U11', 'G06', 'QUEUED_LEAD', 'LOW50-G06', 'U11', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U13', 'LOW50', 'U13', 'G07', 'QUEUED_LEAD', 'LOW50-G07', 'U13', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U14', 'LOW50', 'U14', 'G07', 'MERGED_CHILD', 'LOW50-G07', 'U13', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U15', 'LOW50', 'U15', 'G08', 'QUEUED_LEAD', 'LOW50-G08', 'U15', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U17', 'LOW50', 'U17', 'G09', 'QUEUED_LEAD', 'LOW50-G09', 'U17', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U18', 'LOW50', 'U18', 'G09', 'MERGED_CHILD', 'LOW50-G09', 'U17', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U19', 'LOW50', 'U19', 'G10', 'QUEUED_LEAD', 'LOW50-G10', 'U19', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U21', 'LOW50', 'U21', 'G11', 'QUEUED_LEAD', 'LOW50-G11', 'U21', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U22', 'LOW50', 'U22', 'G11', 'MERGED_CHILD', 'LOW50-G11', 'U21', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U23', 'LOW50', 'U23', 'G12', 'QUEUED_LEAD', 'LOW50-G12', 'U23', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U25', 'LOW50', 'U25', 'G13', 'QUEUED_LEAD', 'LOW50-G13', 'U25', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U26', 'LOW50', 'U26', 'G13', 'MERGED_CHILD', 'LOW50-G13', 'U25', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U27', 'LOW50', 'U27', 'G14', 'QUEUED_LEAD', 'LOW50-G14', 'U27', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U29', 'LOW50', 'U29', 'G15', 'QUEUED_LEAD', 'LOW50-G15', 'U29', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U30', 'LOW50', 'U30', 'G15', 'MERGED_CHILD', 'LOW50-G15', 'U29', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U31', 'LOW50', 'U31', 'G16', 'QUEUED_LEAD', 'LOW50-G16', 'U31', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['LOW50-U33', 'LOW50', 'U33', 'G17', 'SUPPRESSED', None, None, 'Unexpired authorization absent', 'SYN-001;SYN-003'], ['LOW50-U34', 'LOW50', 'U34', 'G17', 'SUPPRESSED', None, None, 'Unexpired authorization absent', 'SYN-001;SYN-003'], ['LOW50-U35', 'LOW50', 'U35', 'G18', 'QUEUED_LEAD', 'LOW50-G18', 'U35', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U01', 'SEGMENTED', 'U01', 'G01', 'QUEUED_LEAD', 'SEGMENTED-G01', 'U01', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U02', 'SEGMENTED', 'U02', 'G01', 'MERGED_CHILD', 'SEGMENTED-G01', 'U01', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U03', 'SEGMENTED', 'U03', 'G02', 'QUEUED_LEAD', 'SEGMENTED-G02', 'U03', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U05', 'SEGMENTED', 'U05', 'G03', 'QUEUED_LEAD', 'SEGMENTED-G03', 'U05', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U06', 'SEGMENTED', 'U06', 'G03', 'MERGED_CHILD', 'SEGMENTED-G03', 'U05', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U09', 'SEGMENTED', 'U09', 'G05', 'QUEUED_LEAD', 'SEGMENTED-G05', 'U09', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U10', 'SEGMENTED', 'U10', 'G05', 'MERGED_CHILD', 'SEGMENTED-G05', 'U09', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U13', 'SEGMENTED', 'U13', 'G07', 'QUEUED_LEAD', 'SEGMENTED-G07', 'U13', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U14', 'SEGMENTED', 'U14', 'G07', 'MERGED_CHILD', 'SEGMENTED-G07', 'U13', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U17', 'SEGMENTED', 'U17', 'G09', 'QUEUED_LEAD', 'SEGMENTED-G09', 'U17', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U18', 'SEGMENTED', 'U18', 'G09', 'MERGED_CHILD', 'SEGMENTED-G09', 'U17', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U21', 'SEGMENTED', 'U21', 'G11', 'QUEUED_LEAD', 'SEGMENTED-G11', 'U21', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U22', 'SEGMENTED', 'U22', 'G11', 'MERGED_CHILD', 'SEGMENTED-G11', 'U21', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U25', 'SEGMENTED', 'U25', 'G13', 'QUEUED_LEAD', 'SEGMENTED-G13', 'U25', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U26', 'SEGMENTED', 'U26', 'G13', 'MERGED_CHILD', 'SEGMENTED-G13', 'U25', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U29', 'SEGMENTED', 'U29', 'G15', 'QUEUED_LEAD', 'SEGMENTED-G15', 'U29', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U30', 'SEGMENTED', 'U30', 'G15', 'MERGED_CHILD', 'SEGMENTED-G15', 'U29', 'Same frozen group and partition', 'SYN-001;SYN-003'], ['SEGMENTED-U33', 'SEGMENTED', 'U33', 'G17', 'SUPPRESSED', None, None, 'Unexpired authorization absent', 'SYN-001;SYN-003'], ['SEGMENTED-U34', 'SEGMENTED', 'U34', 'G17', 'SUPPRESSED', None, None, 'Unexpired authorization absent', 'SYN-001;SYN-003']], 'foreign_keys': [{'columns': ['candidate_id'], 'table': 'Candidates', 'references': ['candidate_id']}, {'columns': ['unit_id'], 'table': 'Population', 'references': ['unit_id']}, {'columns': ['lead_unit_id'], 'table': 'Population', 'references': ['unit_id']}], 'grain': 'One raw candidate-unit hit, identified by hit_id, with its suppression or merged-case route.'}, {'name': 'BelowThreshold', 'columns': ['draw_id', 'unit_id', 'partition', 'frame_n', 'rank', 'selected', 'review_label', 'design', 'evidence_ids'], 'column_contracts': {'draw_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique frame-row identifier.'}, 'unit_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'BASE60 nonhit unit.'}, 'partition': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Frozen stratum; five nonhits per partition.', 'enum': ['TRAIN', 'VALIDATION', 'HOLDOUT']}, 'frame_n': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Complete number of eligible nonhits in this stratum.'}, 'rank': {'type': 'integer', 'nullable': False, 'unit': 'rank', 'description': 'Supplied distinct rank within the stratum.'}, 'selected': {'type': 'boolean', 'nullable': False, 'unit': 'flag', 'description': 'True for ranks one and two.'}, 'review_label': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Observed selected-row outcome or NOT_REVIEWED for unselected records.', 'enum': ['POSITIVE', 'NEGATIVE', 'UNKNOWN', 'CENSORED', 'NOT_REVIEWED']}, 'design': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Fixture rank list is illustrative; it makes no random-sampling claim.', 'enum': ['ILLUSTRATIVE_RANK']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Complete supplied frame and draw record.'}}, 'primary_key': ['draw_id'], 'rows': [['BTL-U03', 'U03', 'TRAIN', 5, 1, True, 'POSITIVE', 'ILLUSTRATIVE_RANK', 'SYN-004'], ['BTL-U04', 'U04', 'TRAIN', 5, 3, False, 'NOT_REVIEWED', 'ILLUSTRATIVE_RANK', 'SYN-004'], ['BTL-U07', 'U07', 'TRAIN', 5, 2, True, 'POSITIVE', 'ILLUSTRATIVE_RANK', 'SYN-004'], ['BTL-U08', 'U08', 'TRAIN', 5, 4, False, 'NOT_REVIEWED', 'ILLUSTRATIVE_RANK', 'SYN-004'], ['BTL-U12', 'U12', 'TRAIN', 5, 5, False, 'NOT_REVIEWED', 'ILLUSTRATIVE_RANK', 'SYN-004'], ['BTL-U15', 'U15', 'VALIDATION', 5, 1, True, 'POSITIVE', 'ILLUSTRATIVE_RANK', 'SYN-004'], ['BTL-U16', 'U16', 'VALIDATION', 5, 3, False, 'NOT_REVIEWED', 'ILLUSTRATIVE_RANK', 'SYN-004'], ['BTL-U19', 'U19', 'VALIDATION', 5, 4, False, 'NOT_REVIEWED', 'ILLUSTRATIVE_RANK', 'SYN-004'], ['BTL-U20', 'U20', 'VALIDATION', 5, 2, True, 'NEGATIVE', 'ILLUSTRATIVE_RANK', 'SYN-004'], ['BTL-U24', 'U24', 'VALIDATION', 5, 5, False, 'NOT_REVIEWED', 'ILLUSTRATIVE_RANK', 'SYN-004'], ['BTL-U27', 'U27', 'HOLDOUT', 5, 3, False, 'NOT_REVIEWED', 'ILLUSTRATIVE_RANK', 'SYN-004'], ['BTL-U28', 'U28', 'HOLDOUT', 5, 1, True, 'UNKNOWN', 'ILLUSTRATIVE_RANK', 'SYN-004'], ['BTL-U31', 'U31', 'HOLDOUT', 5, 4, False, 'NOT_REVIEWED', 'ILLUSTRATIVE_RANK', 'SYN-004'], ['BTL-U32', 'U32', 'HOLDOUT', 5, 5, False, 'NOT_REVIEWED', 'ILLUSTRATIVE_RANK', 'SYN-004'], ['BTL-U36', 'U36', 'HOLDOUT', 5, 2, True, 'CENSORED', 'ILLUSTRATIVE_RANK', 'SYN-004']], 'foreign_keys': [{'columns': ['unit_id'], 'table': 'Population', 'references': ['unit_id']}], 'grain': 'One unit in the complete BASE60 nonhit frame within its frozen partition, whether selected for review or not.'}, {'name': 'CandidateDecisions', 'columns': ['candidate_id', 'decision_state', 'coverage_gate', 'capacity_gate', 'routing_gate', 'next_evidence', 'human_disposition', 'evidence_ids'], 'column_contracts': {'candidate_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Candidate key.'}, 'decision_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Current proposed analytical recommendation.', 'enum': ['BASELINE_ONLY', 'DO_NOT_SUPPORT', 'FURTHER_VALIDATION_ONLY']}, 'coverage_gate': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Explicit known-positive and unknown-label assessment.'}, 'capacity_gate': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Illustrative hours gate; never the only selection criterion.'}, 'routing_gate': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Status of suppression verification.'}, 'next_evidence': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Concrete prerequisite for further consideration.'}, 'human_disposition': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Operational approval is absent.', 'enum': ['NOT_RECORDED']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Sources underlying the recommendation.'}}, 'primary_key': ['candidate_id'], 'rows': [['BASE60', 'BASELINE_ONLY', 'Raw known recall 11/16; retained positive hits 10', 'ALL workload 19.5 hours; illustrative combined capacity 15 hours; no staffing-only selection', 'G17 authorization unverified', 'Resolve suppression and missing labels before change assessment', 'NOT_RECORDED', 'SYN-001;SYN-003'], ['HIGH75', 'DO_NOT_SUPPORT', 'Raw known recall 9/16; retained positive hits 8', 'ALL workload 11.75 hours; illustrative combined capacity 15 hours; no staffing-only selection', 'G17 authorization unverified', 'Challenge losses U11 and U23 against gains; no automatic acceptance', 'NOT_RECORDED', 'SYN-001;SYN-002;SYN-003'], ['LOW50', 'FURTHER_VALIDATION_ONLY', 'Raw known recall 16/16; retained positive hits 15', 'ALL workload 27 hours; illustrative combined capacity 15 hours; no staffing-only selection', 'G17 authorization unverified', 'Representative labels, routing repair, capacity and protected retest', 'NOT_RECORDED', 'SYN-001;SYN-002;SYN-003'], ['SEGMENTED', 'DO_NOT_SUPPORT', 'Raw known recall 10/16; retained positive hits 9', 'ALL workload 14.5 hours; illustrative combined capacity 15 hours; no staffing-only selection', 'G17 authorization unverified', 'Resolve correspondent sensitivity and RETAIL boundary changes', 'NOT_RECORDED', 'SYN-001;SYN-002;SYN-003']], 'foreign_keys': [{'columns': ['candidate_id'], 'table': 'Candidates', 'references': ['candidate_id']}], 'grain': 'One proposed analytical disposition for one candidate_id at the case cutoff; this is not a human deployment approval.'}, {'name': 'EvidenceProvenance', 'columns': ['source_id', 'source_kind', 'as_of', 'availability', 'unit_count', 'grain', 'limitation', 'evidence_ids'], 'column_contracts': {'source_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable source ID resolving to the Evidence register.'}, 'source_kind': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Nature of supplied material.', 'enum': ['SYNTHETIC_INPUT', 'SYNTHETIC_CALCULATION', 'SYNTHETIC_DECISION']}, 'as_of': {'type': 'text', 'nullable': False, 'unit': 'date', 'description': 'Evidence cutoff expressed as ISO date, not a receipt timestamp.'}, 'availability': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Supplied scope status.', 'enum': ['COMPLETE_FIXTURE', 'PARTIAL_FIXTURE']}, 'unit_count': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Count at the explicitly named grain.'}, 'grain': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'The counting unit for this row.'}, 'limitation': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'What this source cannot establish.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'The same source ID, checked against the Evidence register.'}}, 'primary_key': ['source_id'], 'rows': [['SYN-001', 'SYNTHETIC_INPUT', '2026-10-09', 'COMPLETE_FIXTURE', 36, 'scored customer-window units', 'Labels are fictional and dependent within merge groups.', 'SYN-001'], ['SYN-002', 'SYNTHETIC_INPUT', '2026-10-09', 'COMPLETE_FIXTURE', 4, 'candidate configurations', 'Parameter values are illustrative, not approved live settings.', 'SYN-002'], ['SYN-003', 'SYNTHETIC_INPUT', '2026-10-09', 'PARTIAL_FIXTURE', 1, 'suppressed group', 'Suppression exists in the fixture but authorization and expiry evidence are absent.', 'SYN-003'], ['SYN-004', 'SYNTHETIC_INPUT', '2026-10-09', 'COMPLETE_FIXTURE', 15, 'BASE60 below-threshold frame units', 'Six assigned ranks are selected; design does not establish probability sampling.', 'SYN-004']], 'grain': 'One synthetic source_id with its own declared counting unit and availability limit.'}, {'name': 'ProcessQA', 'columns': ['check_id', 'check_scope', 'expected', 'actual', 'status', 'reviewer', 'evidence_ids'], 'column_contracts': {'check_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable QA check identifier.'}, 'check_scope': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact records or decision being checked.'}, 'expected': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Reference result calculated before inspecting presentation.'}, 'actual': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Observed synthetic result; no operational execution is implied.'}, 'status': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Comparison state.', 'enum': ['PASS', 'FAIL', 'REVIEW_REQUIRED', 'NOT_TESTED']}, 'reviewer': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Fictional review role or NOT_RECORDED; never an actual approval.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Semicolon-delimited source IDs resolving to Evidence.'}}, 'primary_key': ['check_id'], 'rows': [['MT-Q01', 'Population conservation', '36 = 29 known + 4 UNKNOWN + 3 CENSORED', '36 = 29 + 4 + 3', 'PASS', 'Fictional checker', 'SYN-001'], ['MT-Q02', 'Partition segregation', '12 units per partition; no group crosses partitions', 'TRAIN12 VALIDATION12 HOLDOUT12; groups disjoint', 'PASS', 'Fictional checker', 'SYN-001'], ['MT-Q03', 'Candidate matrices', 'Each TP+FP+FN+TN equals known_n', 'All sixteen matrices reconcile', 'PASS', 'Fictional checker', 'SYN-001;SYN-002'], ['MT-Q04', 'Suppression authority', 'Current authorization plus expiry and coverage evidence', 'No authorization supplied for G17', 'FAIL', 'Fictional checker', 'SYN-003'], ['MT-Q05', 'Below-threshold frame', '15 frame units; 6 selected; 9 not reviewed', '15 = 6 + 9; selected outcomes P3 N1 U1 C1', 'PASS', 'Fictional checker', 'SYN-004'], ['MT-Q06', 'Holdout authorization', 'Protected review record and separate human decision', 'Only an illustrative prefreeze is supplied', 'REVIEW_REQUIRED', 'NOT_RECORDED', 'SYN-002']], 'grain': 'One explicitly scoped fixture quality check, identified by check_id, with expected and actual results.'}], 'findings': [{'id': 'MT-F01', 'title': 'Suppression removes a known positive from every candidate', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001', 'SYN-003'], 'detail': 'G17 contains HOLDOUT U33 POSITIVE and U34 NEGATIVE. U33 is a raw hit under all four candidates, but the suppressed group reaches no queued case. The supplied record contains no valid suppression authorization.', 'recommendation': 'Keep routing assurance blocked; obtain scope, reason, expiry, approver and covered-activity evidence, then replay all candidates.'}, {'id': 'MT-F02', 'title': 'Lowest threshold increases raw known coverage and workload', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001', 'SYN-002', 'SYN-003'], 'detail': 'LOW50 has 16/16 known positive raw hits and 27 workload hours against an illustrative 15-hour combined capacity. Retained known positive hits are 15/16 after suppression.', 'recommendation': 'Further validate labels and segment behavior, repair routing and assess staffing; do not deploy from the synthetic result.'}, {'id': 'MT-F03', 'title': 'Unknown and censored labels limit population performance claims', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001', 'SYN-004'], 'detail': 'Twenty-nine of thirty-six units have known labels. Four UNKNOWN and three CENSORED units remain outside confusion matrices, including both hit and nonhit records.', 'recommendation': 'Preserve unavailable labels, obtain independent review and assess outcome maturity before any population recall inference.'}, {'id': 'MT-F04', 'title': 'Segmented cutoffs lose correspondent known positives', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-001', 'SYN-002'], 'detail': 'SEGMENTED moves the correspondent cutoff to 65. TRAIN U11 score 63 and VALIDATION U23 score 61 are known positives caught by BASE60 and missed by SEGMENTED. RETAIL U03 score 56 is gained, so the combined result hides opposite segment effects.', 'recommendation': 'Retain incremental unit IDs and require explicit segment challenge; aggregate workload cannot resolve the coverage tradeoff.'}], 'evidence': [{'id': 'SYN-001', 'title': 'Fictional 36-unit population, label and dependence register', 'locator': '10-worked-example.md, raw population and unit-by-unit trace', 'claim_class': 'Observed'}, {'id': 'SYN-002', 'title': 'Four predeclared fictional score candidates', 'locator': '10-worked-example.md, frozen candidate input table', 'claim_class': 'Observed'}, {'id': 'SYN-003', 'title': 'Fictional G17 suppression and group-routing policy', 'locator': '10-worked-example.md, routing input and complete hit ledger', 'claim_class': 'Observed'}, {'id': 'SYN-004', 'title': 'Fictional complete below-threshold frame and assigned ranks', 'locator': '10-worked-example.md, complete fifteen-row frame', 'claim_class': 'Observed'}, {'id': 'REF-001', 'title': 'FFIEC suspicious activity monitoring examination procedures', 'locator': 'https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04_ep', 'claim_class': 'Reported'}, {'id': 'REF-002', 'title': 'Federal Reserve SR 26-2, April 17, 2026', 'locator': 'https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm', 'claim_class': 'Reported'}, {'id': 'REF-003', 'title': 'Federal Reserve, Supervisory Guidance on Model Risk Management', 'locator': 'https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm', 'claim_class': 'Reported'}, {'id': 'REF-004', 'title': 'FinCEN and federal banking agencies, SAR FAQs, October 9, 2025', 'locator': 'https://www.fincen.gov/system/files/2025-10/SAR-FAQs-October-2025.pdf', 'claim_class': 'Reported'}, {'id': 'REF-005', 'title': 'FATF, Guidance for a Risk-Based Approach: The Banking Sector', 'locator': 'https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Risk-Based-Approach-Banking-Sector.pdf.coredownload.pdf', 'claim_class': 'Reported'}, {'id': 'REF-006', 'title': 'NIST, Confidence intervals for proportions', 'locator': 'https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm', 'claim_class': 'Reported'}, {'id': 'REF-007', 'title': 'GAO, Standards for Internal Control in the Federal Government, 2025 revision', 'locator': 'https://www.gao.gov/assets/890/882014.pdf', 'claim_class': 'Reported'}], 'metrics': [{'label': 'Scored units', 'value': 36, 'method': 'Complete frozen unit register; one customer-window per row.', 'format': '#,##0'}, {'label': 'Known labels', 'value': 29, 'method': '16 POSITIVE plus 13 NEGATIVE; excludes 4 UNKNOWN and 3 CENSORED.', 'format': '#,##0'}, {'label': 'LOW50 raw known recall', 'value': 1.0, 'format': '0.0%', 'method': '16 raw positive hits / 16 known positive units; not population recall.'}, {'label': 'LOW50 workload hours', 'value': 27.0, 'format': '0.00', 'method': 'Retained group lead hours plus 0.25 per additional hit after suppression.'}], 'limitations': ['Every record is fictional; results test this supplied procedure and do not establish operational effectiveness.', 'Illustrative cutoffs, partitions, labels, capacities and severity choices are authored examples, not regulatory thresholds.', 'Human scope approval, deployment authority, case disposition and reporting decisions are not supplied.', 'Missing, censored and unresolved evidence remains visible; no favorable default is permitted.'], 'conclusion': 'LOW50 is a further-validation candidate only. Its known-label raw coverage improves, but G17 suppression removes a known positive, missing outcomes prevent population effectiveness claims, and illustrative workload exceeds capacity. No candidate is authorized for deployment.', 'report_narrative': [['LOW50 is a further-validation candidate only. Its known-label raw coverage improves, but G17 suppression removes a known positive, missing outcomes prevent population effectiveness claims, and illustrative workload exceeds capacity. No candidate is authorized for deployment.'], ['The 36 fictional units form three disjoint partitions of twelve. Three segments each contain four units per partition. Group pairs never cross partitions. Scores and four candidates are predeclared; the ALL row is descriptive reconciliation rather than an independent evaluation set.'], ['Raw predicate results, suppression, merged case counts and workload are separate stages. Group G17 suppresses HOLDOUT U33 and U34. A case merge does not automatically credit unhit siblings as detected. The raw and retained positive-unit numerators remain separate.'], ['ALL BASE60 TP11 FP9 FN5 TN4; HIGH75 TP9 FP2 FN7 TN11; LOW50 TP16 FP9 FN0 TN4; SEGMENTED TP10 FP9 FN6 TN4. Each matrix has 29 known labels, with seven other units retained outside the matrix.'], ['The complete BASE60 below-threshold frame has fifteen units. Six assigned-rank selections contain three POSITIVE, one NEGATIVE, one UNKNOWN and one CENSORED outcome. Nine frame units remain unreviewed by this draw. The illustrative ranks do not support a random-sample confidence interval.'], ['The source ledger preserves 36 units, four candidates, one suppression group with incomplete authority, and fifteen below-threshold frame records. Public guidance provides governance context. It does not establish a legal cutoff, a live model classification or approval to suppress activity.'], ['Proposed work is to establish suppression authority or revise routing, label unavailable outcomes without leakage, validate incremental segment losses, and test capacity on protected data. The human deployment disposition remains NOT_RECORDED.'], ['Reperform all candidate matrices and the conservation equations. Validate exact threshold boundaries, merge groups, null rates and missing labels. Passing the fictional checks establishes consistency of this example only; it cannot validate live detection effectiveness.']], 'methods': ['Freeze the scope, source versions, population grain, evidence cutoff and decision question before calculating.', 'Reconcile every received, eligible, excluded, duplicate and unresolved record against independent controls.', 'Apply the exact predicates, joins, state transitions and denominators in files 03 through 05.', 'Challenge missing data, counterexamples, boundary conditions and alternative explanations using file 09.', 'Reproduce file 10 before replacing fictional data; preserve approval gaps and incomplete coverage.'], 'actions': [{'id': 'MO-A01', 'finding_id': 'MT-F01', 'proposal': 'Keep routing assurance blocked; obtain scope, reason, expiry, approver and covered-activity evidence, then replay all candidates.', 'owner': 'Proposed accountable role; assignment not recorded', 'due_date': None, 'status': 'Proposed'}, {'id': 'MO-A02', 'finding_id': 'MT-F02', 'proposal': 'Further validate labels and segment behavior, repair routing and assess staffing; do not deploy from the synthetic result.', 'owner': 'Proposed accountable role; assignment not recorded', 'due_date': None, 'status': 'Proposed'}, {'id': 'MO-A03', 'finding_id': 'MT-F03', 'proposal': 'Preserve unavailable labels, obtain independent review and assess outcome maturity before any population recall inference.', 'owner': 'Proposed accountable role; assignment not recorded', 'due_date': None, 'status': 'Proposed'}, {'id': 'MO-A04', 'finding_id': 'MT-F04', 'proposal': 'Retain incremental unit IDs and require explicit segment challenge; aggregate workload cannot resolve the coverage tradeoff.', 'owner': 'Proposed accountable role; assignment not recorded', 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Exact fictional reconciliation', 'result': 'REVIEW REQUIRED', 'evidence': 'Reperform all ProcessQA rows and file 10 checkpoints in this session.'}, {'id': 'QA-02', 'check': 'Evidence and counterevidence', 'result': 'REVIEW REQUIRED', 'evidence': 'Review every field, rule and exception in files 02 through 05.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No operational approval or filing decision is represented by these fictional records.'}], 'suite_id': 'monitoring-tuning', 'version': '1.2.0', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.'}
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
