# Network and Funds Flow Review — fixed report template

Version 1.2.0. This file is part of the ten instructional attachments. It contains the full report structure and an optional in-session Python renderer. No terminal is required.

## Delivery path

Use the available approved file-creation capability in the current chat. If Python with `python-docx` is available, execute the complete block below in that session after substituting validated case data. Do not install packages or ask the user to run shell commands. If direct Word authoring is available, reproduce this contract exactly. If neither route works, return the completed report as Markdown with the same headings and tables; label it **copy-ready text; DOCX not created**. A Markdown response is not a downloadable Word file.

## Fixed section order

1. **Decision question and supported flow conclusions**
2. **Scope, perimeter and normalization**
3. **Findings and attribution limits**
4. **Nodes and canonical economic transfers**
5. **Balance equations, patterns and allocation bounds**
6. **Evidence and identity provenance**
7. **Proposed discriminating inquiries**
8. **Quality checks, limitations and human decision**

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
