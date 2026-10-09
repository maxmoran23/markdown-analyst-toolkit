# Monitoring System Independent Challenge and Validation — fixed report template

Version 1.2.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Validation opinion and use restrictions**
2. **System scope classification and review design**
3. **Material validation findings**
4. **Component tests and outcome registers**
5. **Issue resolution and release gates**
6. **Evidence provenance and competing interpretations**
7. **Required remediation and further challenge**
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

DATA = {'slug': 'monitoring-validation', 'title': 'Monitoring System Independent Challenge and Validation', 'summary': 'Challenge monitoring purpose, data, implementation, outcomes, limitations and governance with complete evidence and explicit release gates.', 'audience': 'Monitoring analysts, independent challenge reviewers and accountable human decision makers', 'decision': 'What can an objective reviewer conclude about the supplied monitoring component, and which defects or evidence gaps restrict its use?', 'palette': 'indigo', 'as_of': '2026-10-09', 'scope': 'Complete fictional inputs printed in file 10 only. Public authorities provide context, not evidence about the fictional subjects or an institution-specific mandate.', 'report_sections': ['Validation opinion and use restrictions', 'System scope classification and review design', 'Material validation findings', 'Component tests and outcome registers', 'Issue resolution and release gates', 'Evidence provenance and competing interpretations', 'Required remediation and further challenge', 'Limitations quality review and human disposition'], 'domain_tables': [{'name': 'ComponentInventory', 'columns': ['component_id', 'name', 'classification', 'input_grain', 'output', 'theory_basis', 'limitation', 'evidence_ids'], 'column_contracts': {'component_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable analytical component identifier.'}, 'name': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Component purpose and representation.'}, 'classification': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Toolkit analytical classification; institutional determination absent.', 'enum': ['DETERMINISTIC_RULE', 'DETERMINISTIC_TRANSFORM', 'HUMAN_PROCESS']}, 'input_grain': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact unit consumed by the component.'}, 'output': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Declared output and permitted values.'}, 'theory_basis': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Whether quantitative theory underpins an estimate or only fixed logic.'}, 'limitation': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Scope not established by this component.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Supporting source IDs.'}}, 'primary_key': ['component_id'], 'rows': [['CMP-01', 'Feature construction', 'DETERMINISTIC_TRANSFORM', 'Transactions grouped into fixed customer-window', 'amount_usd;eligible_count;originators', 'Arithmetic aggregation; raw transaction replay not supplied', 'Feature values are supplied rather than independently validated', 'SYN-101'], ['CMP-02', 'Reference scenario R1', 'DETERMINISTIC_RULE', 'One customer-window', 'TRUE;FALSE;UNKNOWN', 'Fixed inclusive predicates with no fitted statistical component', 'Multi-originator concept misses single-originator activity', 'SYN-102'], ['CMP-03', 'Implementation I1', 'DETERMINISTIC_RULE', 'One customer-window', 'TRUE;FALSE', 'Strict amount comparison and missing-to-zero default', 'Implementation differs from R1 at boundary and nulls', 'SYN-102'], ['CMP-04', 'Challenger C1', 'DETERMINISTIC_RULE', 'One customer-window', 'TRUE;FALSE;UNKNOWN', 'Fixed broader rule removes originator count condition', 'Diagnostic sensitivity comparison; not a deployment candidate', 'SYN-102'], ['CMP-05', 'Human change disposition', 'HUMAN_PROCESS', 'Validation report and unresolved issues', 'Approve;restrict;reject;request evidence', 'Not a quantitative model; authority depends on supplied governance', 'No actual decision or reviewer credentials supplied', 'SYN-103']], 'grain': 'One reviewed analytical or governance component, identified by component_id, at the stated system boundary.'}, {'name': 'ChallengeTests', 'columns': ['test_id', 'domain', 'test_name', 'procedure', 'expected', 'actual', 'result', 'evidence_ids'], 'column_contracts': {'test_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique validation test key.'}, 'domain': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Validation dimension.', 'enum': ['CONCEPT', 'DATA', 'IMPLEMENTATION', 'OUTCOMES', 'GOVERNANCE', 'MONITORING']}, 'test_name': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Distinct question challenged.'}, 'procedure': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Specific reproducible review action.'}, 'expected': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Predeclared criterion or expected calculation.'}, 'actual': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Fictional observation and record IDs.'}, 'result': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'PASS meets test criterion; FAIL contradicts it; BLOCKED lacks needed evidence.', 'enum': ['PASS', 'FAIL', 'BLOCKED']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Sources supporting the stated result.'}}, 'primary_key': ['test_id'], 'rows': [['C01', 'CONCEPT', 'Objective alignment', 'Compare the stated purpose with the exact predicate', 'Identify repeated multi-originator credits in one fixed window', 'Objective and inclusive amount predicate supplied', 'PASS', 'SYN-102'], ['C02', 'CONCEPT', 'Alternative mechanisms', 'Challenge the two-originator assumption', 'Document single-originator limitations', 'V05 V11 V17 V23 are known positives outside that concept', 'FAIL', 'SYN-101;SYN-102'], ['C03', 'CONCEPT', 'Rule/model classification', 'Inspect mathematical design and stated use', 'Record deterministic rule classification without exempting controls', 'No fitted parameter or probabilistic estimate; deterministic fixture', 'PASS', 'SYN-102'], ['C04', 'CONCEPT', 'Segment transfer', 'Challenge purpose and coverage separately by segment', 'Evidence of each segment rationale required', 'Equal mechanics supplied; no real segment rationale', 'BLOCKED', 'SYN-102'], ['D01', 'DATA', 'Population counts', 'Reconcile independent input manifest', '24 complete unit identifiers across four segments', '24 IDs; six per segment', 'PASS', 'SYN-101'], ['D02', 'DATA', 'Amount completeness', 'Count absent amount inputs without substituting zero', '24 amounts required for full calculability', 'Four missing amounts: V06 V12 V18 V24', 'FAIL', 'SYN-101'], ['D03', 'DATA', 'Transaction lineage', 'Request source transaction-to-feature replay', 'Trace every amount count and originator value', 'Fixture supplies feature-level records only', 'BLOCKED', 'SYN-101'], ['D04', 'DATA', 'Outcome provenance', 'Review label derivation and maturity', 'Independent mature labels supporting generalization', 'Twenty synthetic labels and four unknowns only', 'BLOCKED', 'SYN-101'], ['I01', 'IMPLEMENTATION', 'Amount boundary', 'Compare 9999 10000 and 12000 against inclusive specification', '10000 qualifies when other conditions hold', 'Implemented strict greater-than loses four boundary positives', 'FAIL', 'SYN-101;SYN-102'], ['I02', 'IMPLEMENTATION', 'Count boundary', 'Reperform the minimum of three eligible events', 'Count two is below threshold; count three can qualify', 'V04 V10 V16 V22 rejected consistently', 'PASS', 'SYN-101;SYN-102'], ['I03', 'IMPLEMENTATION', 'Originator boundary', 'Reperform the minimum of two originators', 'One originator excluded under the frozen concept', 'V05 V11 V17 V23 excluded consistently', 'PASS', 'SYN-101;SYN-102'], ['I04', 'IMPLEMENTATION', 'Missing value behavior', 'Compare reference unknown with engine default', 'Missing amount produces unassessable state', 'Four missing amounts converted to false', 'FAIL', 'SYN-101;SYN-102'], ['O01', 'OUTCOMES', 'Reference matrix', 'Count known labels with the reference predicate', 'TP8 FP0 FN4 TN8 on twenty known labels', 'TP8 FP0 FN4 TN8', 'PASS', 'SYN-101;SYN-102'], ['O02', 'OUTCOMES', 'Implemented matrix', 'Count known labels with implemented predicate', 'TP4 FP0 FN8 TN8 on twenty known labels', 'TP4 FP0 FN8 TN8', 'PASS', 'SYN-101;SYN-102'], ['O03', 'OUTCOMES', 'Challenger behavior', 'Remove originator restriction with all other conditions held', 'Expose sensitivity to the excluded mechanism', 'TP12 FP0 FN0 TN8 on the synthetic known subset', 'PASS', 'SYN-101;SYN-102'], ['O04', 'OUTCOMES', 'Generalization', 'Check independent outcome design and test selection', 'Representative operational evidence required', 'Constructed examples cannot support effectiveness inference', 'BLOCKED', 'SYN-101'], ['G01', 'GOVERNANCE', 'Version lineage', 'Compare supplied specification and implementation descriptions', 'Both versions distinguish inclusive and strict comparison', 'Spec R1 versus implementation I1 recorded', 'PASS', 'SYN-102'], ['G02', 'GOVERNANCE', 'Change authorization', 'Inspect human change decision and permitted scope', 'Accountable approver and authorization evidence', 'No operational authorization supplied', 'BLOCKED', 'SYN-103'], ['G03', 'GOVERNANCE', 'Validator objectivity', 'Review involvement expertise conflict and escalation', 'Named review role with evidence of sufficient objectivity', 'Fictional role only; no actual reviewer credentials', 'BLOCKED', 'SYN-103'], ['G04', 'GOVERNANCE', 'Issue ownership', 'Trace defects to proposed actions and evidence requirements', 'Each material defect has a human decision route', 'Four proposed issue records populated', 'PASS', 'SYN-103'], ['M01', 'MONITORING', 'Missingness indicator', 'Calculate missing amount count and denominator', '4/24 = 16.7% absent', '4/24 = 16.7%', 'PASS', 'SYN-101'], ['M02', 'MONITORING', 'Boundary mismatch indicator', 'Identify present-input implementation differences', '4/20 = 20.0% among present amounts', 'V02 V08 V14 V20; 4/20', 'PASS', 'SYN-101;SYN-102'], ['M03', 'MONITORING', 'Drift baseline', 'Inspect the reference period and comparison frame', 'Comparable independent periods required', 'Single constructed feature set only', 'BLOCKED', 'SYN-101'], ['M04', 'MONITORING', 'Remediation retest', 'Require corrected replay plus unchanged-case checks', 'New implementation and all twenty-four outcomes', 'No corrected implementation supplied', 'BLOCKED', 'SYN-103']], 'grain': 'One predeclared validation test, identified by test_id, within one validation domain.'}, {'name': 'OutcomeUnits', 'columns': ['unit_id', 'segment', 'amount_usd', 'eligible_count', 'originators', 'label', 'reference_hit', 'implemented_hit', 'challenger_hit', 'mismatch', 'evidence_ids'], 'column_contracts': {'unit_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'One feature-level customer-window test unit.'}, 'segment': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Fictional segment label.', 'enum': ['RETAIL', 'BUSINESS', 'CORRESPONDENT', 'DIGITAL_SERVICE']}, 'amount_usd': {'type': 'number', 'nullable': True, 'unit': 'USD', 'description': 'Eligible credits in USD for the supplied fixed window; null means absent.'}, 'eligible_count': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Number of eligible posted credits in that window.'}, 'originators': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Distinct originator identities under the frozen supplied definition.'}, 'label': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Synthetic outcome; UNKNOWN stays outside matrices.', 'enum': ['POSITIVE', 'NEGATIVE', 'UNKNOWN']}, 'reference_hit': {'type': 'boolean', 'nullable': True, 'unit': 'flag', 'description': 'Inclusive amount and count rule; null when amount absent.'}, 'implemented_hit': {'type': 'boolean', 'nullable': False, 'unit': 'flag', 'description': 'Observed I1 result with strict amount test and missing-to-false defect.'}, 'challenger_hit': {'type': 'boolean', 'nullable': True, 'unit': 'flag', 'description': 'Diagnostic rule without originator restriction; null when amount absent.'}, 'mismatch': {'type': 'boolean', 'nullable': False, 'unit': 'flag', 'description': 'True when reference and implemented values differ, including null versus false.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Raw features and independent rule definitions.'}}, 'primary_key': ['unit_id'], 'rows': [['V01', 'RETAIL', 9999, 3, 2, 'NEGATIVE', False, False, False, False, 'SYN-101;SYN-102'], ['V02', 'RETAIL', 10000, 3, 2, 'POSITIVE', True, False, True, True, 'SYN-101;SYN-102'], ['V03', 'RETAIL', 12000, 4, 3, 'POSITIVE', True, True, True, False, 'SYN-101;SYN-102'], ['V04', 'RETAIL', 14000, 2, 2, 'NEGATIVE', False, False, False, False, 'SYN-101;SYN-102'], ['V05', 'RETAIL', 18000, 5, 1, 'POSITIVE', False, False, True, False, 'SYN-101;SYN-102'], ['V06', 'RETAIL', None, 4, 3, 'UNKNOWN', None, False, None, True, 'SYN-101;SYN-102'], ['V07', 'BUSINESS', 9999, 3, 2, 'NEGATIVE', False, False, False, False, 'SYN-101;SYN-102'], ['V08', 'BUSINESS', 10000, 3, 2, 'POSITIVE', True, False, True, True, 'SYN-101;SYN-102'], ['V09', 'BUSINESS', 12000, 4, 3, 'POSITIVE', True, True, True, False, 'SYN-101;SYN-102'], ['V10', 'BUSINESS', 14000, 2, 2, 'NEGATIVE', False, False, False, False, 'SYN-101;SYN-102'], ['V11', 'BUSINESS', 18000, 5, 1, 'POSITIVE', False, False, True, False, 'SYN-101;SYN-102'], ['V12', 'BUSINESS', None, 4, 3, 'UNKNOWN', None, False, None, True, 'SYN-101;SYN-102'], ['V13', 'CORRESPONDENT', 9999, 3, 2, 'NEGATIVE', False, False, False, False, 'SYN-101;SYN-102'], ['V14', 'CORRESPONDENT', 10000, 3, 2, 'POSITIVE', True, False, True, True, 'SYN-101;SYN-102'], ['V15', 'CORRESPONDENT', 12000, 4, 3, 'POSITIVE', True, True, True, False, 'SYN-101;SYN-102'], ['V16', 'CORRESPONDENT', 14000, 2, 2, 'NEGATIVE', False, False, False, False, 'SYN-101;SYN-102'], ['V17', 'CORRESPONDENT', 18000, 5, 1, 'POSITIVE', False, False, True, False, 'SYN-101;SYN-102'], ['V18', 'CORRESPONDENT', None, 4, 3, 'UNKNOWN', None, False, None, True, 'SYN-101;SYN-102'], ['V19', 'DIGITAL_SERVICE', 9999, 3, 2, 'NEGATIVE', False, False, False, False, 'SYN-101;SYN-102'], ['V20', 'DIGITAL_SERVICE', 10000, 3, 2, 'POSITIVE', True, False, True, True, 'SYN-101;SYN-102'], ['V21', 'DIGITAL_SERVICE', 12000, 4, 3, 'POSITIVE', True, True, True, False, 'SYN-101;SYN-102'], ['V22', 'DIGITAL_SERVICE', 14000, 2, 2, 'NEGATIVE', False, False, False, False, 'SYN-101;SYN-102'], ['V23', 'DIGITAL_SERVICE', 18000, 5, 1, 'POSITIVE', False, False, True, False, 'SYN-101;SYN-102'], ['V24', 'DIGITAL_SERVICE', None, 4, 3, 'UNKNOWN', None, False, None, True, 'SYN-101;SYN-102']], 'formats': {'amount_usd': '$#,##0.00'}, 'grain': 'One feature-level customer-window test unit, identified by unit_id, evaluated by the reference, implementation and challenger.'}, {'name': 'OutcomeMetrics', 'columns': ['variant', 'population_n', 'known_n', 'unknown_n', 'tp', 'fp', 'fn', 'tn', 'all_hits', 'unassessable_n', 'precision', 'recall', 'evidence_ids'], 'column_contracts': {'variant': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Frozen comparison variant.', 'enum': ['REFERENCE', 'IMPLEMENTED', 'CHALLENGER']}, 'population_n': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'All supplied units.'}, 'known_n': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Available positive or negative labels.'}, 'unknown_n': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Missing outcome labels excluded from confusion matrix.'}, 'tp': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Known positive and variant true.'}, 'fp': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Known negative and variant true.'}, 'fn': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Known positive and variant false.'}, 'tn': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Known negative and variant false.'}, 'all_hits': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'True outputs across all twenty-four units.'}, 'unassessable_n': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Null outputs due to missing input; separate from unknown labels.'}, 'precision': {'type': 'number', 'nullable': True, 'unit': 'ratio', 'description': 'TP / (TP+FP) on known labels.'}, 'recall': {'type': 'number', 'nullable': True, 'unit': 'ratio', 'description': 'TP / (TP+FN) on known labels.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Feature and predicate sources.'}}, 'primary_key': ['variant'], 'rows': [['REFERENCE', 24, 20, 4, 8, 0, 4, 8, 8, 4, 1.0, 0.6666666666666666, 'SYN-101;SYN-102'], ['IMPLEMENTED', 24, 20, 4, 4, 0, 8, 8, 4, 0, 1.0, 0.3333333333333333, 'SYN-101;SYN-102'], ['CHALLENGER', 24, 20, 4, 12, 0, 0, 8, 12, 4, 1.0, 1.0, 'SYN-101;SYN-102']], 'formats': {'precision': '0.0%', 'recall': '0.0%'}, 'grain': 'One comparison variant summarized across the same complete 24-unit fixture and 20-unit known-label subset.'}, {'name': 'IssueRegister', 'columns': ['issue_id', 'linked_tests', 'severity', 'affected_ids', 'issue', 'closure_evidence', 'state', 'evidence_ids'], 'column_contracts': {'issue_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique issue key.'}, 'linked_tests': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Semicolon-delimited ChallengeTests identifiers.'}, 'severity': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Illustrative prioritization independent of certainty.', 'enum': ['HIGH', 'MEDIUM', 'LOW']}, 'affected_ids': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact affected units or component IDs.'}, 'issue': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Observed deficiency or limitation.'}, 'closure_evidence': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Minimum evidence needed to test a proposed correction.'}, 'state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'No issue is operationally closed in this fixture.', 'enum': ['OPEN', 'BLOCKED']}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Underlying case evidence.'}}, 'primary_key': ['issue_id'], 'rows': [['MV-I01', 'I01;M02', 'HIGH', 'V02;V08;V14;V20', 'Strict amount comparison loses inclusive-boundary hits', 'Corrected version replay of all 24 units plus boundary neighbors', 'OPEN', 'SYN-101;SYN-102'], ['MV-I02', 'D02;I04', 'HIGH', 'V06;V12;V18;V24', 'Absent amounts silently become negative outputs', 'Explicit unknown route, data recovery and no zero substitution', 'OPEN', 'SYN-101;SYN-102'], ['MV-I03', 'C02;D03;D04;O04', 'HIGH', 'CMP-01;CMP-02', 'Coverage concept and evidence cannot support generalization', 'Transaction lineage, independent representative outcomes and concept challenge', 'BLOCKED', 'SYN-101;SYN-102'], ['MV-I04', 'G02;G03;M03;M04', 'MEDIUM', 'CMP-05', 'Authorization objectivity and corrected retest not evidenced', 'Actual reviewer qualifications, conflict assessment, approvals and corrected retest', 'BLOCKED', 'SYN-103']], 'grain': 'One distinct validation issue, identified by issue_id, with linked tests, affected records and closure evidence.'}, {'name': 'EvidenceProvenance', 'columns': ['source_id', 'source_kind', 'as_of', 'availability', 'unit_count', 'grain', 'limitation', 'evidence_ids'], 'column_contracts': {'source_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable source ID resolving to the Evidence register.'}, 'source_kind': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Nature of supplied material.', 'enum': ['SYNTHETIC_INPUT', 'SYNTHETIC_CALCULATION', 'SYNTHETIC_DECISION']}, 'as_of': {'type': 'text', 'nullable': False, 'unit': 'date', 'description': 'Evidence cutoff expressed as ISO date, not a receipt timestamp.'}, 'availability': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Supplied scope status.', 'enum': ['COMPLETE_FIXTURE', 'PARTIAL_FIXTURE']}, 'unit_count': {'type': 'integer', 'nullable': False, 'unit': 'count', 'description': 'Count at the explicitly named grain.'}, 'grain': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'The counting unit for this row.'}, 'limitation': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'What this source cannot establish.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'The same source ID, checked against the Evidence register.'}}, 'primary_key': ['source_id'], 'rows': [['SYN-101', 'SYNTHETIC_INPUT', '2026-10-09', 'COMPLETE_FIXTURE', 24, 'supplied feature-level units', 'Feature-level completeness does not establish transaction lineage.', 'SYN-101'], ['SYN-102', 'SYNTHETIC_INPUT', '2026-10-09', 'COMPLETE_FIXTURE', 3, 'predicate definitions', 'R1 I1 and C1 are fictional rules, not live deployed components.', 'SYN-102'], ['SYN-103', 'SYNTHETIC_DECISION', '2026-10-09', 'PARTIAL_FIXTURE', 4, 'proposed issue records', 'Actual change approval and reviewer credentials are absent.', 'SYN-103']], 'grain': 'One synthetic source_id with its own declared counting unit and availability limit.'}, {'name': 'ProcessQA', 'columns': ['check_id', 'check_scope', 'expected', 'actual', 'status', 'reviewer', 'evidence_ids'], 'column_contracts': {'check_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Stable QA check identifier.'}, 'check_scope': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Exact records or decision being checked.'}, 'expected': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Reference result calculated before inspecting presentation.'}, 'actual': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Observed synthetic result; no operational execution is implied.'}, 'status': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Comparison state.', 'enum': ['PASS', 'FAIL', 'REVIEW_REQUIRED', 'NOT_TESTED']}, 'reviewer': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Fictional review role or NOT_RECORDED; never an actual approval.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Semicolon-delimited source IDs resolving to Evidence.'}}, 'primary_key': ['check_id'], 'rows': [['MV-Q01', 'Feature manifest', '24 unique units and four segments of 6', '24 unique;6 per segment', 'PASS', 'Fictional checker', 'SYN-101'], ['MV-Q02', 'Present and absent amounts', '24=20 present+4 absent', '20 present and 4 null', 'PASS', 'Fictional checker', 'SYN-101'], ['MV-Q03', 'Reference result', '8 true;12 false;4 unknown', '8 true;12 false;4 unknown', 'PASS', 'Fictional checker', 'SYN-101;SYN-102'], ['MV-Q04', 'Implemented result', 'Specification-equivalent tri-state result', '4 true;20 false;0 unknown', 'FAIL', 'Fictional checker', 'SYN-101;SYN-102'], ['MV-Q05', 'Mismatches', 'Four boundary and four null-state differences', '8 mismatches; mutually exclusive classes', 'PASS', 'Fictional checker', 'SYN-101;SYN-102'], ['MV-Q06', 'Generalization gate', 'Independent operational data required', 'Synthetic designed examples only', 'REVIEW_REQUIRED', 'NOT_RECORDED', 'SYN-101'], ['MV-Q07', 'Human decision', 'Actual authorized decision required', 'NOT_RECORDED', 'NOT_TESTED', 'NOT_RECORDED', 'SYN-103']], 'grain': 'One explicitly scoped fixture quality check, identified by check_id, with expected and actual results.'}, {'name': 'ReleaseGates', 'columns': ['gate_id', 'requirement', 'current_evidence', 'gate_state', 'dependency', 'permitted_claim', 'evidence_ids'], 'column_contracts': {'gate_id': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Unique human review gate.'}, 'requirement': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Evidence needed before supporting the stated use.'}, 'current_evidence': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'What is actually supplied.'}, 'gate_state': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'No failed or blocked gate can be treated as satisfied.', 'enum': ['SATISFIED_FIXTURE_ONLY', 'FAILED', 'BLOCKED']}, 'dependency': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Preceding issue or evidence requirement.'}, 'permitted_claim': {'type': 'text', 'nullable': False, 'unit': 'text', 'description': 'Narrow statement that can currently be made.'}, 'evidence_ids': {'type': 'text', 'nullable': False, 'unit': 'identifier', 'description': 'Evidence for the gate.'}}, 'primary_key': ['gate_id'], 'rows': [['MV-G01', 'Reference predicate reproducible', 'R1 independent replay agrees on 24 units', 'SATISFIED_FIXTURE_ONLY', 'SYN-101;SYN-102', 'Fixture arithmetic is reproducible', 'SYN-101;SYN-102'], ['MV-G02', 'Implementation equivalence', 'Eight mismatches including four known-positive boundary losses', 'FAILED', 'MV-I01;MV-I02', 'Implementation is not equivalent to the supplied specification', 'SYN-101;SYN-102'], ['MV-G03', 'Complete input lineage', 'Raw transaction detail is outside the supplied fixture', 'BLOCKED', 'MV-I03', 'Feature-level calculations only', 'SYN-101'], ['MV-G04', 'Representative outcomes', 'Twenty constructed known labels and four unknowns', 'BLOCKED', 'MV-I03', 'Synthetic comparisons only; no live effectiveness estimate', 'SYN-101'], ['MV-G05', 'Qualified objective review', 'Fictional review role; no actual conflict or qualification record', 'BLOCKED', 'MV-I04', 'Method supports challenge; institutional independence unverified', 'SYN-103'], ['MV-G06', 'Authorized release disposition', 'No human approval or corrected replay supplied', 'BLOCKED', 'MV-I01;MV-I02;MV-I03;MV-I04', 'Do not support release on this evidence', 'SYN-103']], 'grain': 'One specific release-evidence gate, identified by gate_id, for the stated component and intended use.'}], 'findings': [{'id': 'MV-F01', 'title': 'Implementation loses inclusive-boundary known positives', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-101', 'SYN-102'], 'detail': 'V02 V08 V14 V20 each have amount 10000, count 3 and originators 2. R1 is true, while I1 uses greater-than and returns false. Four known positives are lost.', 'recommendation': 'Correct the predicate in a separately versioned proposal and replay all 24 units, equality boundaries and unchanged cases.'}, {'id': 'MV-F02', 'title': 'Missing amount values silently become negative outcomes', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-101', 'SYN-102'], 'detail': 'V06 V12 V18 V24 lack amount inputs. R1 and C1 return unknown; I1 returns false. These four records cannot support no-hit assurance.', 'recommendation': 'Preserve unknown outputs, recover missing amounts where possible and define a human exception route with measurable aging.'}, {'id': 'MV-F03', 'title': 'Constructed labels and narrow concept do not establish effectiveness', 'severity': 'HIGH', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-101', 'SYN-102'], 'detail': 'R1 misses four known positives having one originator, and the broader challenger catches them. Raw transaction lineage and independent representative outcomes are not supplied.', 'recommendation': 'Evaluate the concept and alternative mechanisms, obtain independent data and preserve this challenger as diagnostic evidence only.'}, {'id': 'MV-F04', 'title': 'Governance and corrected replay remain unrecorded', 'severity': 'MEDIUM', 'confidence': 'HIGH', 'claim_class': 'Observed', 'evidence_ids': ['SYN-103'], 'detail': 'The example supplies proposed issues and fictional roles, but no real reviewer qualifications, objectivity assessment, approval or corrected implementation replay.', 'recommendation': 'Obtain actual accountable review evidence and keep release disposition unresolved until material gates are addressed.'}], 'evidence': [{'id': 'SYN-101', 'title': 'Twenty-four fictional unit features and independent outcomes', 'locator': '10-worked-example.md, complete raw feature ledger', 'claim_class': 'Observed'}, {'id': 'SYN-102', 'title': 'Reference R1, implemented I1 and challenger C1 definitions', 'locator': '10-worked-example.md, independent predicate specification', 'claim_class': 'Observed'}, {'id': 'SYN-103', 'title': 'Fictional challenge records and unresolved governance evidence', 'locator': '10-worked-example.md, issue and gate registers', 'claim_class': 'Observed'}, {'id': 'REF-001', 'title': 'FFIEC suspicious activity monitoring examination procedures', 'locator': 'https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04_ep', 'claim_class': 'Reported'}, {'id': 'REF-002', 'title': 'Federal Reserve SR 26-2, April 17, 2026', 'locator': 'https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm', 'claim_class': 'Reported'}, {'id': 'REF-003', 'title': 'Federal Reserve, Supervisory Guidance on Model Risk Management', 'locator': 'https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm', 'claim_class': 'Reported'}, {'id': 'REF-004', 'title': 'FinCEN and federal banking agencies, SAR FAQs, October 9, 2025', 'locator': 'https://www.fincen.gov/system/files/2025-10/SAR-FAQs-October-2025.pdf', 'claim_class': 'Reported'}, {'id': 'REF-005', 'title': 'FATF, Guidance for a Risk-Based Approach: The Banking Sector', 'locator': 'https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Risk-Based-Approach-Banking-Sector.pdf.coredownload.pdf', 'claim_class': 'Reported'}, {'id': 'REF-006', 'title': 'NIST, Confidence intervals for proportions', 'locator': 'https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm', 'claim_class': 'Reported'}, {'id': 'REF-007', 'title': 'GAO, Standards for Internal Control in the Federal Government, 2025 revision', 'locator': 'https://www.gao.gov/assets/890/882014.pdf', 'claim_class': 'Reported'}], 'metrics': [{'label': 'Validation tests', 'value': 24, 'method': 'Four predeclared tests in each of six domains.', 'format': '#,##0'}, {'label': 'Implementation differences', 'value': 8, 'method': 'Four inclusive-boundary differences plus four null-versus-false differences.', 'format': '#,##0'}, {'label': 'Reference known-label recall', 'value': 0.6666666666666666, 'format': '0.0%', 'method': '8 true positives / 12 known positive feature units.'}, {'label': 'Implemented known-label recall', 'value': 0.3333333333333333, 'format': '0.0%', 'method': '4 true positives / 12 known positive feature units.'}], 'limitations': ['Every record is fictional; results test this supplied procedure and do not establish operational effectiveness.', 'Illustrative cutoffs, partitions, labels, capacities and severity choices are authored examples, not regulatory thresholds.', 'Human scope approval, deployment authority, case disposition and reporting decisions are not supplied.', 'Missing, censored and unresolved evidence remains visible; no favorable default is permitted.'], 'conclusion': 'Do not support release of I1 on the supplied evidence. The implementation differs from the reference at inclusive boundaries and missing values; broader effectiveness, transaction lineage, objective review and actual authorization remain unresolved.', 'report_narrative': [['Do not support release of I1 on the supplied evidence. The implementation differs from the reference at inclusive boundaries and missing values; broader effectiveness, transaction lineage, objective review and actual authorization remain unresolved.'], ['The supplied subject is deterministic monitoring logic over 24 feature-level customer-window units. R1 tests amount>=10000, count>=3 and originators>=2; absent amount returns unknown. I1 uses amount>10000 and returns false for absent amount. No universal institutional model classification is implied.'], ['Four known positive boundary units are lost. Four missing amounts are silently changed to false. A separate conceptual limitation excludes four single-originator positives. These mechanisms require distinct findings rather than one combined percentage.'], ['R1 gives TP8 FP0 FN4 TN8; I1 gives TP4 FP0 FN8 TN8; C1 gives TP12 FP0 FN0 TN8. All matrices use twenty known labels. Four UNKNOWN labels stay outside; only R1 and C1 retain unknown input states.'], ['The 24 tests distinguish arithmetic passes from failed concepts or implementation and blocked evidence requests. Four issues remain OPEN or BLOCKED. A passed matrix calculation means the arithmetic is right; it does not mean the underlying system meets its intended use.'], ['SYN-101 contains features, not source transactions. SYN-102 supplies three independent predicate descriptions. SYN-103 records fictional governance gaps. Current public model guidance must be assessed for scope and applicability; this deterministic example is not automatically a model under that definition.'], ['Proposed corrections need versioned implementation evidence, unchanged-case regression tests, feature lineage, independent outcome review and a real human disposition. The challenger is a diagnostic stress of one assumption, not an approved replacement.'], ['Reproduce eight mismatches, split four boundary losses from four missing-state differences, and verify each matrix. No probability interval or deployment approval follows from designed fictional examples. Keep the report in a restricted draft state until the stated evidence gates are resolved.']], 'methods': ['Freeze the scope, source versions, population grain, evidence cutoff and decision question before calculating.', 'Reconcile every received, eligible, excluded, duplicate and unresolved record against independent controls.', 'Apply the exact predicates, joins, state transitions and denominators in files 03 through 05.', 'Challenge missing data, counterexamples, boundary conditions and alternative explanations using file 09.', 'Reproduce file 10 before replacing fictional data; preserve approval gaps and incomplete coverage.'], 'actions': [{'id': 'MO-A01', 'finding_id': 'MV-F01', 'proposal': 'Correct the predicate in a separately versioned proposal and replay all 24 units, equality boundaries and unchanged cases.', 'owner': 'Proposed accountable role; assignment not recorded', 'due_date': None, 'status': 'Proposed'}, {'id': 'MO-A02', 'finding_id': 'MV-F02', 'proposal': 'Preserve unknown outputs, recover missing amounts where possible and define a human exception route with measurable aging.', 'owner': 'Proposed accountable role; assignment not recorded', 'due_date': None, 'status': 'Proposed'}, {'id': 'MO-A03', 'finding_id': 'MV-F03', 'proposal': 'Evaluate the concept and alternative mechanisms, obtain independent data and preserve this challenger as diagnostic evidence only.', 'owner': 'Proposed accountable role; assignment not recorded', 'due_date': None, 'status': 'Proposed'}, {'id': 'MO-A04', 'finding_id': 'MV-F04', 'proposal': 'Obtain actual accountable review evidence and keep release disposition unresolved until material gates are addressed.', 'owner': 'Proposed accountable role; assignment not recorded', 'due_date': None, 'status': 'Proposed'}], 'qa': [{'id': 'QA-01', 'check': 'Exact fictional reconciliation', 'result': 'REVIEW REQUIRED', 'evidence': 'Reperform all ProcessQA rows and file 10 checkpoints in this session.'}, {'id': 'QA-02', 'check': 'Evidence and counterevidence', 'result': 'REVIEW REQUIRED', 'evidence': 'Review every field, rule and exception in files 02 through 05.'}, {'id': 'QA-03', 'check': 'Authorized human disposition', 'result': 'NOT RECORDED', 'evidence': 'No operational approval or filing decision is represented by these fictional records.'}], 'suite_id': 'monitoring-validation', 'version': '1.2.0', 'notice': 'Synthetic worked example. Fictional records. Not a completed operational review.'}
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
