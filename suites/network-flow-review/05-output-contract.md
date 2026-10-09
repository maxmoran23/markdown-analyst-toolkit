# Network and Funds Flow Review — complete output contract

## Delivery and authority

The required delivery is a report and workbook or their complete copy-ready equivalents. The offline dashboard is an optional view of the same case data. Preserve the six common sheets Summary, Dashboard, Findings, Evidence, Actions and QA, followed by the exact domain tables below. The report contains eight fixed sections. The workbook contains the row-level ledger. The dashboard contains all domain records with clearly labeled filters. No output receives its own independently edited population or conclusion.

Keep all amounts numeric in their stated native units, all identifiers text, all unavailable values null and every controlled label exact. Display USD with a dollar sign, thousands separators and two decimals; show ratios as percentages to one decimal unless a precision test requires more. Retain full calculation precision until display. A rate’s numerator and denominator belong in its method, and a coefficient is not a percentage merely because it lies between zero and one.

The common Evidence register preserves source identifiers and locators. Domain evidence_ids fields contain semicolon-delimited exact references to that register. An evidence join supports traceability; it does not prove that the source supports the proposition. The quality reviewer must verify the actual span and its limits. A null foreign key is allowed only where the column contract explicitly permits it. Do not insert a fabricated key to satisfy validation.

Every table has a declared grain and primary key. Adding a row may change the population, not just the presentation. Repeated account names, amounts or timestamps are not sufficient grounds for deduplication. A foreign key must refer to the declared parent table and exact referenced columns. Do not join on a display name when an identifier is available. Any adaptation that changes a grain, column type, allowed state or relationship must record a schema-version change and rerun the population and rendering checks.

## Narrative and metric parity

The report must show the principal conclusion, scope, all findings, all domain records, source limitations, proposed actions and quality status. Narrative paragraphs supplied in the fixture are fully populated examples; replace them case by case. Do not keep a paragraph solely because it sounds professional. Each quantified statement must be reproducible from the actual rows. Each interpretive sentence must identify its evidence and surviving alternative.

Metrics are named measures with units, methods and limitations. A count of findings is not a count of transactions. A count of reviewed cases is not a count of review votes. An edge-leg total is not a unique economic amount. A debit net of linked returns is not confirmed loss. Preserve these semantic distinctions in chart labels and summary cards. Charts must not create a stronger claim than their source field supports.

The Actions register contains proposals, owners and dates only when supplied. Leave ownership and due date unassigned until actual authority is known. A proposed request is not a message sent; an accepted action is not an executed correction; an executed correction is not independently verified closure. The QA register identifies checks actually performed, evidence and result. Never mark PASS because a field is populated or because a renderer completed without error.

## Recovery and text fallback

If document generation fails, preserve the analysis and return every required table with its exact header and row count. Split long tables into labeled ranges with repeated headers. Reconcile the combined ranges so no record disappears between messages. Name the unavailable output format and what remains untested. Do not fabricate a download link or describe a Markdown table as a spreadsheet file.

If a source is too large for a cell, preserve the complete source outside the table under an approved case attachment and include an attributed bounded summary with an exact locator. Do not silently truncate a material contradiction. If a numeric value exceeds a file format’s exact precision, retain the original string and calculate under an explicit precision rule. Formatting convenience cannot justify changing the source amount or identifier.

## Exact report headings

1. Decision question and supported flow conclusions
2. Scope, perimeter and normalization
3. Findings and attribution limits
4. Nodes and canonical economic transfers
5. Balance equations, patterns and allocation bounds
6. Evidence and identity provenance
7. Proposed discriminating inquiries
8. Quality checks, limitations and human decision

## Immutable domain schemas and populated operating rules

### Nodes

**Grain:** One distinct supplied account/counterparty node; nine total. **Primary key:** `node_id`. **Report placement:** section 4.

```text
node_id | node_type | entity_id | identity_basis | opening_usd | evidence_ids | scope_limit
```

**Populate from:** N02 account identity/balance record and immediate counterparties in N01/N04. **Required procedure:** Retain nine nodes, including separate A1/A2 accounts linked to verified Entity-A. Do not promote recorded counterparty IDs to beneficial-owner facts.

**Interpretation:** Opening balances are known only for A1/A2. Null openings elsewhere mean missing coverage, not zero funds.

**Change and exception handling:** A new identity bridge changes grouping and requires boundary recalculation. It does not justify rewriting the original source label or assuming historical applicability.

**Field-level validation:** `node_id`: text, required, unit identifier; `node_type`: text, required, unit text, allowed ACCOUNT, COUNTERPARTY; `entity_id`: text, required, unit identifier; `identity_basis`: text, required, unit text, allowed VERIFIED, RECORDED; `opening_usd`: number, nullable, unit USD; `evidence_ids`: text, required, unit evidence identifiers; `scope_limit`: text, required, unit text.

### EconomicEdges

**Grain:** One posted economic transfer; duplicate representations and nonexecuted instructions excluded. **Primary key:** `edge_id`. **Report placement:** section 4.

```text
edge_id | hour_index | from_node | to_node | amount_usd | currency | own_transfer | return_of | evidence_ids | identity_status
```

**Populate from:** N01 canonical ledger, N03 return links, N04 onward extracts and N08 order. **Required procedure:** Retain 24 executed transfers with positive amount and exact direction. Exclude the four identified noncanonical raw representations with a crosswalk.

**Interpretation:** Own-transfer flags are true only for E04/E16; return_of is populated only for E08/E21. Those classifications have different aggregation consequences.

**Change and exception handling:** A new posted transfer changes graph and balances. A duplicate representation changes raw inventory only. A revised return link changes net interpretation without removing the gross edge.

**Declared joins:** `from_node` → `Nodes.node_id`; `to_node` → `Nodes.node_id`. Every supplied child key must resolve before release.

**Field-level validation:** `edge_id`: text, required, unit identifier; `hour_index`: integer, required, unit count; `from_node`: text, required, unit identifier; `to_node`: text, required, unit identifier; `amount_usd`: number, required, unit USD; `currency`: text, required, unit text, allowed USD; `own_transfer`: boolean, required, unit flag; `return_of`: text, nullable, unit identifier; `evidence_ids`: text, required, unit evidence identifiers; `identity_status`: text, required, unit text, allowed RECORDED.

### BalanceChecks

**Grain:** One valid equation for a complete supplied perimeter. **Primary key:** `balance_id`. **Report placement:** section 5.

```text
balance_id | perimeter | opening_usd | inflow_usd | outflow_usd | calculated_close_usd | supplied_close_usd | difference_usd | evidence_ids
```

**Populate from:** Complete review-account postings plus supplied opening and closing controls. **Required procedure:** Create A1, A2 and consolidated Entity-A equations; do not add equations for seven partial-visibility nodes.

**Interpretation:** A1=500; A2=1000; entity=1500. Internal E04/E16 amounts cancel in the entity boundary while remaining in account equations.

**Change and exception handling:** A negative balance under a no-overdraft attribution assumption triggers a model feasibility review. Unknown external balances do not automatically fail this table.

**Field-level validation:** `balance_id`: text, required, unit identifier; `perimeter`: text, required, unit text; `opening_usd`: number, required, unit USD; `inflow_usd`: number, required, unit USD; `outflow_usd`: number, required, unit USD; `calculated_close_usd`: number, required, unit USD; `supplied_close_usd`: number, required, unit USD; `difference_usd`: number, required, unit USD; `evidence_ids`: text, required, unit evidence identifiers.

### PatternTests

**Grain:** One defined graph pattern with an explicitly named amount and count. **Primary key:** `pattern_id`. **Report placement:** section 5.

```text
pattern_id | pattern | edge_ids | measure_usd | count | interpretation | evidence_ids
```

**Populate from:** Precisely declared edge sets and node membership. **Required procedure:** Preserve six different pattern measures with their own amount/count interpretation. Do not combine them into a generic suspicious-flow total.

**Interpretation:** P01 count is distinct source nodes; P02 count is boundary transfer legs; P03 count is cycle edges. Metric labels must retain those different units.

**Change and exception handling:** A new edge can change degree, time-respecting paths and boundary totals differently. Recompute exact memberships rather than incrementing every counter.

**Field-level validation:** `pattern_id`: text, required, unit identifier; `pattern`: text, required, unit text; `edge_ids`: text, required, unit text; `measure_usd`: number, required, unit USD; `count`: integer, required, unit count; `interpretation`: text, required, unit text; `evidence_ids`: text, required, unit evidence identifiers.

### AllocationBounds

**Grain:** One marginal or grouped attribution bound under explicitly stated balance constraints. **Primary key:** `allocation_id`. **Report placement:** section 5.

```text
allocation_id | target_edge | source_group | available_usd | other_available_usd | debit_usd | lower_usd | upper_usd | basis | evidence_ids
```

**Populate from:** Complete pre-E03 funding pool and GP-1 fungible nonnegative balance assumptions. **Required procedure:** Compute four marginal/grouped attribution intervals. Check total available 19000 can fund debit 12000 before applying endpoint formulas.

**Interpretation:** Lower=max(0,D-O); upper=min(S,D). Grouped P+Q interval is 11000–12000 and cannot be obtained by adding individual minima.

**Change and exception handling:** Missing opening, unseen prior debit or permitted overdraft can invalidate the simple bound. Preserve descriptive graph results while withholding an unsupported attribution interval.

**Declared joins:** `target_edge` → `EconomicEdges.edge_id`. Every supplied child key must resolve before release.

**Field-level validation:** `allocation_id`: text, required, unit identifier; `target_edge`: text, required, unit identifier; `source_group`: text, required, unit text; `available_usd`: number, required, unit USD; `other_available_usd`: number, required, unit USD; `debit_usd`: number, required, unit USD; `lower_usd`: number, required, unit USD; `upper_usd`: number, required, unit USD; `basis`: text, required, unit text; `evidence_ids`: text, required, unit evidence identifiers.

### AttributionScenarios

**Grain:** One feasible assumed allocation vector; alternatives do not describe simultaneous facts. **Primary key:** `scenario_id`. **Report placement:** section 5.

```text
scenario_id | method | p_usd | q_usd | opening_usd | total_usd | status | evidence_ids
```

**Populate from:** The same pool used by AllocationBounds and four declared assumptions. **Required procedure:** Create four feasible allocation vectors, each summing 12000 and respecting source capacities. Keep every row ILLUSTRATIVE_ONLY.

**Interpretation:** Proportional allocation rounds P and opening to cents and assigns the remaining cent-accurate residual to Q. FIFO is opening-first then ordered receipts.

**Change and exception handling:** A convention change affects the point vector, not the observed evidence. The interval remains the main supported conclusion unless actual linkage evidence narrows it.

**Field-level validation:** `scenario_id`: text, required, unit identifier; `method`: text, required, unit text; `p_usd`: number, required, unit USD; `q_usd`: number, required, unit USD; `opening_usd`: number, required, unit USD; `total_usd`: number, required, unit USD; `status`: text, required, unit text, allowed ILLUSTRATIVE_ONLY; `evidence_ids`: text, required, unit evidence identifiers.

### DecisionRecord

**Grain:** One claim boundary or human gate. **Primary key:** `decision_id`. **Report placement:** section 5.

```text
decision_id | question | status | reason | evidence_ids
```

**Populate from:** Identity evidence, graph facts, attribution assumptions and actual authority. **Required procedure:** Record five explicit inference boundaries: grouping supported, full P attribution unresolved, illicit-cycle inference prohibited, unique-capital label prohibited and no human decision.

**Interpretation:** A prohibited inference is a methodological boundary, not a finding that the opposite proposition is true.

**Change and exception handling:** If new evidence narrows attribution or supports purpose, record a new bounded claim. Do not infer wrongdoing from the fact that the prior claim was unresolved.

**Field-level validation:** `decision_id`: text, required, unit identifier; `question`: text, required, unit text; `status`: text, required, unit text, allowed SUPPORTED, CONTRADICTED, UNRESOLVED, PROHIBITED_INFERENCE, NOT_RECORDED; `reason`: text, required, unit text; `evidence_ids`: text, required, unit evidence identifiers.

### ProcessQA

**Grain:** One analytical check, distinct from legal or operational validation. **Primary key:** `check_id`. **Report placement:** section 5.

```text
check_id | check | expected | actual | result | evidence_ids
```

**Populate from:** Counts, graph sums, balance equations, allocation math and authority boundary. **Required procedure:** Keep ten checks and their exact scope. Test all scenario totals and both attribution endpoints, not only the displayed rounded metric.

**Interpretation:** A structural PASS verifies the stated fixture invariant; it does not validate customer identity, complete external visibility or legal conclusions.

**Change and exception handling:** When an edge changes, rerun raw normalization, memberships, balances and affected path/allocation tests before updating report cards.

**Field-level validation:** `check_id`: text, required, unit identifier; `check`: text, required, unit text; `expected`: text, required, unit text; `actual`: text, required, unit text; `result`: text, required, unit text, allowed PASS, NOT RECORDED; `evidence_ids`: text, required, unit evidence identifiers.

## Completed narrative pattern and adaptation test

Use the eight populated narrative sections in file 10 as a demonstration of the required specificity. For each paragraph, identify the source rows, calculation or decision rule that support it. When adapting, remove the fictional proposition before writing a new one; changing a title or date is not enough. A reviewer should be able to take any quantified sentence and recover its numerator, denominator, unit and scope without asking the assistant what it meant.

All domain records belong in the report or its complete tabular annex as well as the workbook and dashboard. Keep the exact identifiers in every representation. If a table becomes long, split it into labeled contiguous ranges, not selected examples. Preserve the common Evidence register and every semicolon-delimited evidence reference. The completed output remains draft until the applicable quality gates and actual human decision status are accurately recorded.

<!-- FIELD_CONTRACTS:START -->
## Compiled domain field dictionary

This dictionary is part of this attachment. It fixes the type, null rule, unit, permitted values and record identity used by the embedded renderers. It is generated from the same reviewed case contract; no external file is needed. Raw source defects must be retained as raw text under their declared type. Correcting a malformed value requires evidence, not coercion by the renderer.

### Nodes — field contract

**Record grain:** One distinct supplied account/counterparty node; nine total.

**Primary key:** `node_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| node_id | text | no | identifier | Account or counterparty node; aliases are not silently merged. | No additional enum or range constraint | Native value / literal text |
| node_type | text | no | text | Representation type. | ACCOUNT / COUNTERPARTY | Native value / literal text |
| entity_id | text | no | identifier | Recorded or verified entity grouping; beneficial ownership not implied. | No additional enum or range constraint | Native value / literal text |
| identity_basis | text | no | text | Strength and scope of grouping. | VERIFIED / RECORDED | Native value / literal text |
| opening_usd | number | yes | USD | Supplied opening balance for complete review accounts; null elsewhere. | No additional enum or range constraint | $#,##0.00 |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |
| scope_limit | text | no | text | Visibility limitation affecting balance and graph claims. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### EconomicEdges — field contract

**Record grain:** One posted economic transfer; duplicate representations and nonexecuted instructions excluded.

**Primary key:** `edge_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| edge_id | text | no | identifier | Unique canonical economic transfer identifier. | No additional enum or range constraint | Native value / literal text |
| hour_index | integer | no | count | Strict fixture order: hours1–24 after the declared start. | No additional enum or range constraint | #,##0 |
| from_node | text | no | identifier | Immediate recorded sender node. | No additional enum or range constraint | Native value / literal text |
| to_node | text | no | identifier | Immediate recorded receiver node. | No additional enum or range constraint | Native value / literal text |
| amount_usd | number | no | USD | Positive value of this transfer leg; summing paths repeats capital. | No additional enum or range constraint | $#,##0.00 |
| currency | text | no | text | Native monetary unit. | USD | Native value / literal text |
| own_transfer | boolean | no | flag | True only when both accounts belong to verified Entity-A. | No additional enum or range constraint | Native value / literal text |
| return_of | text | yes | identifier | Explicit original debit edge for a linked return; null otherwise. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |
| identity_status | text | no | text | Counterparty labels as recorded; no guilt or control claim. | RECORDED | Native value / literal text |

Foreign key: `from_node` resolves to `Nodes (node_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Foreign key: `to_node` resolves to `Nodes (node_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### BalanceChecks — field contract

**Record grain:** One valid equation for a complete supplied perimeter.

**Primary key:** `balance_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| balance_id | text | no | identifier | Unique account/perimeter equation identifier. | No additional enum or range constraint | Native value / literal text |
| perimeter | text | no | text | Account or consolidated entity being reconciled. | No additional enum or range constraint | Native value / literal text |
| opening_usd | number | no | USD | Supplied opening balance. | No additional enum or range constraint | $#,##0.00 |
| inflow_usd | number | no | USD | Recorded credits; consolidated excludes own transfers. | No additional enum or range constraint | $#,##0.00 |
| outflow_usd | number | no | USD | Recorded debits; consolidated excludes own transfers. | No additional enum or range constraint | $#,##0.00 |
| calculated_close_usd | number | no | USD | Opening plus inflow minus outflow. | No additional enum or range constraint | $#,##0.00 |
| supplied_close_usd | number | no | USD | Independent supplied closing amount. | No additional enum or range constraint | $#,##0.00 |
| difference_usd | number | no | USD | Calculated minus supplied close. | No additional enum or range constraint | $#,##0.00 |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### PatternTests — field contract

**Record grain:** One defined graph pattern with an explicitly named amount and count.

**Primary key:** `pattern_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| pattern_id | text | no | identifier | Stable graph observation identifier. | No additional enum or range constraint | Native value / literal text |
| pattern | text | no | text | Precisely defined topology or temporal pattern. | No additional enum or range constraint | Native value / literal text |
| edge_ids | text | no | text | Semicolon-delimited canonical edges, not raw representations. | No additional enum or range constraint | Native value / literal text |
| measure_usd | number | no | USD | Named measure described in interpretation; never generic illicit value. | No additional enum or range constraint | $#,##0.00 |
| count | integer | no | count | Pattern-specific edge/node count described in interpretation. | No additional enum or range constraint | #,##0 |
| interpretation | text | no | text | Bounded observation and what it does not establish. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### AllocationBounds — field contract

**Record grain:** One marginal or grouped attribution bound under explicitly stated balance constraints.

**Primary key:** `allocation_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| allocation_id | text | no | identifier | Stable source-to-target attribution question. | No additional enum or range constraint | Native value / literal text |
| target_edge | text | no | identifier | Debit edge whose funding is being bounded. | No additional enum or range constraint | Native value / literal text |
| source_group | text | no | text | Eligible source class at the instant before the debit. | No additional enum or range constraint | Native value / literal text |
| available_usd | number | no | USD | Source amount available under the fixture before E03. | No additional enum or range constraint | $#,##0.00 |
| other_available_usd | number | no | USD | All other eligible opening/inflow balances before E03. | No additional enum or range constraint | $#,##0.00 |
| debit_usd | number | no | USD | Target debit value. | No additional enum or range constraint | $#,##0.00 |
| lower_usd | number | no | USD | max(0,debit-other available), subject to feasible total balance. | No additional enum or range constraint | $#,##0.00 |
| upper_usd | number | no | USD | min(source available,debit), not a chosen estimate. | No additional enum or range constraint | $#,##0.00 |
| basis | text | no | text | Model assumptions and stronger claim prohibited. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Foreign key: `target_edge` resolves to `EconomicEdges (edge_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### AttributionScenarios — field contract

**Record grain:** One feasible assumed allocation vector; alternatives do not describe simultaneous facts.

**Primary key:** `scenario_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| scenario_id | text | no | identifier | Stable illustrative allocation scenario. | No additional enum or range constraint | Native value / literal text |
| method | text | no | text | Explicit assumed allocation convention, not observed tracing. | No additional enum or range constraint | Native value / literal text |
| p_usd | number | no | USD | Assigned P funding to E03 under this convention. | No additional enum or range constraint | $#,##0.00 |
| q_usd | number | no | USD | Assigned Q funding to E03 under this convention. | No additional enum or range constraint | $#,##0.00 |
| opening_usd | number | no | USD | Assigned opening balance to E03. | No additional enum or range constraint | $#,##0.00 |
| total_usd | number | no | USD | Sum assigned to E03; exactly12000 at displayed cent precision. | No additional enum or range constraint | $#,##0.00 |
| status | text | no | text | Epistemic status. | ILLUSTRATIVE_ONLY | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### DecisionRecord — field contract

**Record grain:** One claim boundary or human gate.

**Primary key:** `decision_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| decision_id | text | no | identifier | Stable decision gate. | No additional enum or range constraint | Native value / literal text |
| question | text | no | text | Exact proposition requiring a conclusion. | No additional enum or range constraint | Native value / literal text |
| status | text | no | text | Bounded result. | SUPPORTED / CONTRADICTED / UNRESOLVED / PROHIBITED_INFERENCE / NOT_RECORDED | Native value / literal text |
| reason | text | no | text | Why the result follows from visibility and method. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ProcessQA — field contract

**Record grain:** One analytical check, distinct from legal or operational validation.

**Primary key:** `check_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| check_id | text | no | identifier | Stable quality check. | No additional enum or range constraint | Native value / literal text |
| check | text | no | text | Reperformable rule. | No additional enum or range constraint | Native value / literal text |
| expected | text | no | text | Expected fixture result. | No additional enum or range constraint | Native value / literal text |
| actual | text | no | text | Observed fixture result or explicit unknown. | No additional enum or range constraint | Native value / literal text |
| result | text | no | text | Result of analytical fixture check. | PASS / NOT RECORDED | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.
<!-- FIELD_CONTRACTS:END -->
