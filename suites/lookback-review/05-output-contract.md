# Output contract — Historical Monitoring Lookback and Remediation Review

## Immutable presentation and interchange rules

Produce the eight report sections in the order printed below. Keep the six common workbook tabs: Summary, Dashboard, Findings, Evidence, Actions and QA. Append all ten domain tables in the declared order. Do not replace a detailed register with a favorable summary. Column names are stable machine keys even when the report presents them as readable field labels. The report may display long rows vertically, but the workbook retains every column and every record. The dashboard exposes the same case without external data requests.

Store identifiers and source locators as text. Store counts as nonnegative integers, monetary amounts as numeric values with declared currency, rates as fractions and booleans as true or false. Use null for an unknown numeric or boolean result. A rate whose denominator is zero is null with a visible reason. Keep exact numerical values in the interchange representation and apply rounding only for display. A displayed percentage must have its numerator, denominator and inclusion rule available in the accompanying method note.

For currency fields, do not aggregate different currencies without an explicitly supplied conversion method and date. An activity total is not a loss estimate, an illicit-funds total or a statutory threshold. For workload, distinguish hours assumed per case from hours measured in an actual review process. For outcome metrics, distinguish labeled-sample performance from population effectiveness. For completion, distinguish received-row accounting, retrieved-unit coverage, desk review completion, downstream case disposition and whole-review acceptance. These meanings must survive every export.

An evidence key in a domain record must resolve to the common Evidence register. Semicolon-delimited keys represent several distinct sources; do not treat the combined string as one new source. A foreign key must resolve at the declared parent grain. A composite key is unique only when all its components are considered together. Retain nulls for genuinely unavailable links where the field contract permits them, and name the resulting limitation. Do not create dummy parent records merely to make a join pass.

The final findings table separates severity, confidence and evidence class. Severity is the consequence or priority under the stated illustrative rubric; confidence concerns support for the observation; evidence class states how the claim is known. A high-severity uncertainty can have low confidence, while a confidently reproduced arithmetic defect can have a narrow practical consequence. The dashboard must not use one field as a substitute for another. Every recommendation stays distinct from the human disposition and from proof that an action occurred.

## Narrative completion standard

Each required report section needs complete case-specific prose. Do not output headings with instructions to fill them later. The recommendation section states the supported answer and its restrictions first. The scope section gives the period, population, exclusions, unit of analysis and method. The findings section gives facts and counterevidence. The register sections explain material patterns and exceptions without hiding detailed rows. The evidence section distinguishes inspected material from cited context. The action section names prerequisites and unrecorded assignments. The last section reports actual QA work and unresolved decisions.

Use a sentence pattern that makes a claim inspectable: within a specified population, the identified records show a stated result under the declared rule; the result means a bounded consequence because of the cited evidence; the alternative explanation or missing input is explicit; the proposed next step requests a defined piece of evidence or a human decision. Do not mechanically repeat the pattern where a table already carries the information. Use it to check whether a polished paragraph has lost a denominator, basis or qualification.

A fictional specimen can contain completed fictional calculations and populated example review outcomes. It cannot contain an actual human signoff. Preserve the banner and source labels until every fictional value has been replaced and rechecked. Do not retain specimen case IDs in a live deliverable. If only part of the specimen has been replaced, label the whole package as a mixed draft and prevent a conclusion that appears to concern a real institution. Fully populated does not mean every uncertainty must be converted into a favorable fact.

## Required report heading order

1. Lookback status and completion restrictions
2. Historical scope defect chronology and population
3. Retrieval review and coverage findings
4. Complete historical population and intake registers
5. Review actions expansion and stopping gates
6. Evidence preservation and unresolved periods
7. Proposed remediation and case-review handoffs
8. Limitations quality review and human disposition

## Populated report narrative model

### Lookback status and completion restrictions

The lookback is incomplete. Twenty-nine of 30 expected historical units are retrieved, twelve desk comparisons are complete, and only six units have no open desk-review action. Six referrals and eighteen other evidence or review dependencies remain unresolved; no filing or whole-review approval is implied.

### Historical scope defect chronology and population

The independent fictional manifest defines January through June 2026 and five canonical units per month. Initial discovery considered January through March; a documented analytical expansion includes April through June because the mapping defect chronology may continue. Actual institutional scope approval is not supplied.

### Retrieval review and coverage findings

Raw intake reconciles 34 representations to 29 canonical units,3 duplicates and 2 July exclusions. That arithmetic does not cure missing L30. June is 4/5 retrieved. Known canonical activity totals 449500 USD and excludes L30, whose amount is unknown.

### Complete historical population and intake registers

CanonicalUnits preserves all 30 expected records, including the missing placeholder. RetrievalLedger preserves every received representation and alias link. Historical statuses remain separate from current review states, so re-review never rewrites the original decision history.

### Review actions expansion and stopping gates

Six units have completed comparisons with no new information; six have new-information referrals; six need re-review; six await review; five are unable to assess; one is not retrieved. Twelve desk comparisons are complete, but six of those have unresolved handoffs. Twenty-four units retain an open dependency.

### Evidence preservation and unresolved periods

Control evidence, retrieval evidence, review assignments and chronology are separate sources. A retrieved summary does not establish complete supporting documents. The July rows are retained as exclusions while chronology evidence is requested, not silently dropped as irrelevant.

### Proposed remediation and case-review handoffs

Proposed work is to recover L30, obtain support for L25 through L29, finish L13 through L24 reviews, and obtain responsible case-review responses for L07 through L12. Filing, account action and whole-review acceptance remain separate human decisions.

### Limitations quality review and human disposition

Do not report a 100% completion rate from received-row classification or twelve completed desk comparisons. Reperform the thirty-unit state reconciliation, amount conservation, duplicate links and completion gates. The fictional checks establish evidence accounting only, not a completed operational remediation.

## Domain register purposes and cross-checks

### PeriodReconciliation

Exact ordered columns: period, expected_units, retrieved_rows, duplicate_rows, retrieved_units, missing_units, known_amount_usd, coverage_state, evidence_ids.

The specimen contains **6 records** at the key grain `period`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `period` is demonstrated by `2026-01`, `2026-02`, `2026-03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

### CanonicalUnits

Exact ordered columns: unit_id, period, source_id, amount_usd, original_state, defect_affected, review_state, new_information, priority, evidence_ids.

The specimen contains **30 records** at the key grain `unit_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `unit_id` is demonstrated by `L01`, `L02`, `L03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

The join from `period` to `PeriodReconciliation.period` must resolve exactly at the parent key. Check the number of matched, unmatched and multiply matched rows before using the join. A nullable missing link remains visible with its reason; an unexplained nonnull key that does not resolve is an error, not an excluded observation.

### RetrievalLedger

Exact ordered columns: raw_id, unit_id, source_period, classification, canonical_id, raw_amount_usd, evidence_ids.

The specimen contains **34 records** at the key grain `raw_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `raw_id` is demonstrated by `RAW-01`, `RAW-02`, `RAW-03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

The join from `unit_id` to `CanonicalUnits.unit_id` must resolve exactly at the parent key. Check the number of matched, unmatched and multiply matched rows before using the join. A nullable missing link remains visible with its reason; an unexplained nonnull key that does not resolve is an error, not an excluded observation.

The join from `canonical_id` to `CanonicalUnits.unit_id` must resolve exactly at the parent key. Check the number of matched, unmatched and multiply matched rows before using the join. A nullable missing link remains visible with its reason; an unexplained nonnull key that does not resolve is an error, not an excluded observation.

### ReviewActions

Exact ordered columns: action_id, unit_id, review_state, action_state, observed_basis, required_next_step, comparison_id, human_disposition, evidence_ids.

The specimen contains **30 records** at the key grain `action_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `action_id` is demonstrated by `LA-L01`, `LA-L02`, `LA-L03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

The join from `unit_id` to `CanonicalUnits.unit_id` must resolve exactly at the parent key. Check the number of matched, unmatched and multiply matched rows before using the join. A nullable missing link remains visible with its reason; an unexplained nonnull key that does not resolve is an error, not an excluded observation.

### ExpansionDecisions

Exact ordered columns: expansion_id, trigger, proposed_scope, inclusion_rule, stopping_condition, decision_state, evidence_ids.

The specimen contains **6 records** at the key grain `expansion_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `expansion_id` is demonstrated by `EX-01`, `EX-02`, `EX-03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

### EvidenceProvenance

Exact ordered columns: source_id, source_kind, as_of, availability, unit_count, grain, limitation, evidence_ids.

The specimen contains **4 records** at the key grain `source_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `source_id` is demonstrated by `SYN-201`, `SYN-202`, `SYN-203`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

### ProcessQA

Exact ordered columns: check_id, check_scope, expected, actual, status, reviewer, evidence_ids.

The specimen contains **8 records** at the key grain `check_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `check_id` is demonstrated by `LB-Q01`, `LB-Q02`, `LB-Q03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

### CompletionGates

Exact ordered columns: gate_id, gate, numerator, denominator, state, residual, permitted_statement, evidence_ids.

The specimen contains **6 records** at the key grain `gate_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `gate_id` is demonstrated by `LB-G01`, `LB-G02`, `LB-G03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

## Additional historical comparison and chronology contracts

ComparisonPackets is keyed by comparison_id and joins one completed desk-comparison packet to CanonicalUnits. Historical cutoff, original source and facts, original rationale, recovered date and source, current facts, path, material delta and expected route must all be populated. Semicolon-delimited historical_fact_ids and current_fact_ids resolve to the exact fact dictionary printed in file10. The material_delta flag is true only when the current material fact set adds a fact absent from the historical set under the declared illustrative relevance criterion. A completed referral packet is not a completed receiving-case disposition. ReviewActions.comparison_id resolves to this table for L01 through L12; it remains null for records without a completed comparison.

DefectChronology is keyed by chronology_id. Its dated records distinguish plans, runtime snapshots, unavailable checkpoints, defect reproduction and proposed correction. A plan is not runtime proof, discovery is not exposure onset, and a sandbox correction is not deployment. SourcePathInputs in file10 supplies the per-unit raw path and version needed for the impact predicate. A missing path or version produces an unknown impact flag. Preserve July's unresolved boundary even though the current analytical scope ends in June.

<!-- FIELD_CONTRACTS:START -->
## Compiled domain field dictionary

This dictionary is part of this attachment. It fixes the type, null rule, unit, permitted values and record identity used by the embedded renderers. It is generated from the same reviewed case contract; no external file is needed. Raw source defects must be retained as raw text under their declared type. Correcting a malformed value requires evidence, not coercion by the renderer.

### PeriodReconciliation — field contract

**Record grain:** One historical calendar month in the frozen January–June scope, reconciling expected canonical units to received representations.

**Primary key:** `period`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| period | text | no | month | Calendar month in the frozen January through June scope. | No additional enum or range constraint | Native value / literal text |
| expected_units | integer | no | count | Independent control-manifest canonical count. | No additional enum or range constraint | Native value / literal text |
| retrieved_rows | integer | no | count | Received rows in this period before duplicate removal. | No additional enum or range constraint | Native value / literal text |
| duplicate_rows | integer | no | count | Additional representations of an already received canonical unit. | No additional enum or range constraint | Native value / literal text |
| retrieved_units | integer | no | count | Distinct in-scope canonical units with some retrieved material. | No additional enum or range constraint | Native value / literal text |
| missing_units | integer | no | count | Control units absent from retrieval. | No additional enum or range constraint | Native value / literal text |
| known_amount_usd | number | no | USD | Sum of available canonical amounts only; excludes missing amount. | No additional enum or range constraint | $#,##0.00 |
| coverage_state | text | no | text | Whether counts fully reconcile; says nothing about review completeness. | RECONCILED / PARTIAL | Native value / literal text |
| evidence_ids | text | no | identifier | Independent control and retrieval sources. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### CanonicalUnits — field contract

**Record grain:** One independently expected historical review unit, identified by unit_id, including an unretrieved placeholder when source evidence is absent.

**Primary key:** `unit_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| unit_id | text | no | identifier | One expected historical review unit from the independent manifest. | No additional enum or range constraint | Native value / literal text |
| period | text | no | month | Manifest month, not the latest retrieval date. | No additional enum or range constraint | Native value / literal text |
| source_id | text | yes | identifier | Canonical retrieval row; null for not-retrieved unit L30. | No additional enum or range constraint | Native value / literal text |
| amount_usd | number | yes | USD | Supplied unit activity amount; absent for L30. Not a loss amount. | No additional enum or range constraint | $#,##0.00 |
| original_state | text | no | text | Historical status preserved unchanged. | CLOSED / ESCALATED / NOT_GENERATED / UNKNOWN | Native value / literal text |
| defect_affected | boolean | yes | flag | Known impact flag; null when the missing record prevents assessment. | No additional enum or range constraint | Native value / literal text |
| review_state | text | no | text | Current lookback review state, separate from historical state. | REVIEW_COMPLETE_NO_NEW / REFERRED_FOR_CASE_REVIEW / REREVIEW_REQUIRED / PENDING_REVIEW / UNABLE_TO_ASSESS / NOT_RETRIEVED | Native value / literal text |
| new_information | boolean | yes | flag | Comparison outcome; null when review or evidence is incomplete. | No additional enum or range constraint | Native value / literal text |
| priority | text | no | text | Illustrative attention priority; not a legal deadline. | HIGH / MEDIUM | Native value / literal text |
| evidence_ids | text | no | identifier | Exact control and retrieved evidence sources. | No additional enum or range constraint | Native value / literal text |

Foreign key: `period` resolves to `PeriodReconciliation (period)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### RetrievalLedger — field contract

**Record grain:** One received source representation, identified by raw_id, before canonical deduplication or scope exclusion.

**Primary key:** `raw_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| raw_id | text | no | identifier | Unique received representation identifier. | No additional enum or range constraint | Native value / literal text |
| unit_id | text | yes | identifier | Matched in-scope canonical unit; null for out-of-scope July records. | No additional enum or range constraint | Native value / literal text |
| source_period | text | no | month | Historical month associated with the received record. | No additional enum or range constraint | Native value / literal text |
| classification | text | no | text | Exactly one intake accounting bucket. | CANONICAL / DUPLICATE / OUT_OF_SCOPE | Native value / literal text |
| canonical_id | text | yes | identifier | Retained canonical unit for matching rows; null when out of scope. | No additional enum or range constraint | Native value / literal text |
| raw_amount_usd | number | no | USD | Amount on this raw representation before deduplication; do not aggregate as canonical activity. | No additional enum or range constraint | $#,##0.00 |
| evidence_ids | text | no | identifier | Retrieval input source. | No additional enum or range constraint | Native value / literal text |

Foreign key: `unit_id` resolves to `CanonicalUnits (unit_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Foreign key: `canonical_id` resolves to `CanonicalUnits (unit_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ReviewActions — field contract

**Record grain:** One current lookback work action for one canonical unit, identified by action_id, with a separate comparison and human-disposition state.

**Primary key:** `action_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| action_id | text | no | identifier | Unique historical-unit action identifier. | No additional enum or range constraint | Native value / literal text |
| unit_id | text | no | identifier | Canonical unit requiring or receiving review. | No additional enum or range constraint | Native value / literal text |
| review_state | text | no | text | State replicated from CanonicalUnits to permit reconciliation. | REVIEW_COMPLETE_NO_NEW / REFERRED_FOR_CASE_REVIEW / REREVIEW_REQUIRED / PENDING_REVIEW / UNABLE_TO_ASSESS / NOT_RETRIEVED | Native value / literal text |
| action_state | text | no | text | Operational work position; a handoff is not closed. | DESK_REVIEW_COMPLETE / HANDOFF_OPEN / REVIEW_OPEN / EVIDENCE_BLOCKED / RETRIEVAL_BLOCKED | Native value / literal text |
| observed_basis | text | no | text | Fictional basis supporting this work state. | No additional enum or range constraint | Native value / literal text |
| required_next_step | text | no | text | Specific evidence-preserving work proposal. | No additional enum or range constraint | Native value / literal text |
| comparison_id | text | yes | identifier | Populated comparison packet ID for the twelve desk-complete units; null where no completed packet exists. | No additional enum or range constraint | Native value / literal text |
| human_disposition | text | no | text | Actual institutional acceptance is absent. | NOT_RECORDED | Native value / literal text |
| evidence_ids | text | no | identifier | Review-state source. | No additional enum or range constraint | Native value / literal text |

Foreign key: `unit_id` resolves to `CanonicalUnits (unit_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Foreign key: `comparison_id` resolves to `ComparisonPackets (comparison_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ExpansionDecisions — field contract

**Record grain:** One bounded scope-change, recovery or review proposal, identified by expansion_id, with its trigger and stopping condition.

**Primary key:** `expansion_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| expansion_id | text | no | identifier | Stable scope-change or stopping decision key. | No additional enum or range constraint | Native value / literal text |
| trigger | text | no | text | Specific new evidence or observed condition. | No additional enum or range constraint | Native value / literal text |
| proposed_scope | text | no | text | Bounded additional review population or work. | No additional enum or range constraint | Native value / literal text |
| inclusion_rule | text | no | text | Exact predicate for the proposed change. | No additional enum or range constraint | Native value / literal text |
| stopping_condition | text | no | text | Evidence needed to stop the associated work. | No additional enum or range constraint | Native value / literal text |
| decision_state | text | no | text | Proposals do not invent actual human acceptance. | PROPOSED / BLOCKED | Native value / literal text |
| evidence_ids | text | no | identifier | Supporting scope or defect evidence. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### EvidenceProvenance — field contract

**Record grain:** One synthetic source_id with its own declared counting unit and availability limit.

**Primary key:** `source_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| source_id | text | no | identifier | Stable source ID resolving to the Evidence register. | No additional enum or range constraint | Native value / literal text |
| source_kind | text | no | text | Nature of supplied material. | SYNTHETIC_INPUT / SYNTHETIC_CALCULATION / SYNTHETIC_DECISION | Native value / literal text |
| as_of | text | no | date | Evidence cutoff expressed as ISO date, not a receipt timestamp. | No additional enum or range constraint | Native value / literal text |
| availability | text | no | text | Supplied scope status. | COMPLETE_FIXTURE / PARTIAL_FIXTURE | Native value / literal text |
| unit_count | integer | no | count | Count at the explicitly named grain. | No additional enum or range constraint | Native value / literal text |
| grain | text | no | text | The counting unit for this row. | No additional enum or range constraint | Native value / literal text |
| limitation | text | no | text | What this source cannot establish. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | identifier | The same source ID, checked against the Evidence register. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ProcessQA — field contract

**Record grain:** One explicitly scoped fixture quality check, identified by check_id, with expected and actual results.

**Primary key:** `check_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| check_id | text | no | identifier | Stable QA check identifier. | No additional enum or range constraint | Native value / literal text |
| check_scope | text | no | text | Exact records or decision being checked. | No additional enum or range constraint | Native value / literal text |
| expected | text | no | text | Reference result calculated before inspecting presentation. | No additional enum or range constraint | Native value / literal text |
| actual | text | no | text | Observed synthetic result; no operational execution is implied. | No additional enum or range constraint | Native value / literal text |
| status | text | no | text | Comparison state. | PASS / FAIL / REVIEW_REQUIRED / NOT_TESTED | Native value / literal text |
| reviewer | text | no | text | Fictional review role or NOT_RECORDED; never an actual approval. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | identifier | Semicolon-delimited source IDs resolving to Evidence. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### CompletionGates — field contract

**Record grain:** One distinct completion claim, identified by gate_id, with its own expressly stated numerator and denominator grain.

**Primary key:** `gate_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| gate_id | text | no | identifier | Unique stopping or completion gate. | No additional enum or range constraint | Native value / literal text |
| gate | text | no | text | Evidence required for the stated completion claim. | No additional enum or range constraint | Native value / literal text |
| numerator | integer | no | count | Satisfied units at the stated denominator grain. | No additional enum or range constraint | Native value / literal text |
| denominator | integer | no | count | Complete in-scope population for this gate. | No additional enum or range constraint | Native value / literal text |
| state | text | no | text | SATISFIED_FIXTURE_ONLY does not mean operational signoff. | SATISFIED_FIXTURE_ONLY / FAILED / BLOCKED | Native value / literal text |
| residual | text | no | text | Specific unresolved gap. | No additional enum or range constraint | Native value / literal text |
| permitted_statement | text | no | text | Narrow completion statement supported by the record. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | identifier | Evidence supporting the gate. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ComparisonPackets — field contract

**Record grain:** One completed fictional historical-versus-current desk-comparison packet for one canonical unit, identified by comparison_id.

**Primary key:** `comparison_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| comparison_id | text | no | identifier | Unique populated historical/current packet ID. | No additional enum or range constraint | Native value / literal text |
| unit_id | text | no | identifier | Canonical unit whose desk comparison is documented. | No additional enum or range constraint | Native value / literal text |
| historical_cutoff | text | no | date | Date through which the fictional historical packet was available. | No additional enum or range constraint | Native value / literal text |
| historical_source | text | no | identifier | Printed historical source packet locator. | No additional enum or range constraint | Native value / literal text |
| historical_fact_ids | text | no | identifier | Semicolon-delimited material facts available historically. | No additional enum or range constraint | Native value / literal text |
| historical_facts | text | no | text | Concrete facts actually present in the original packet. | No additional enum or range constraint | Native value / literal text |
| historical_rationale | text | no | text | Original reasoning preserved without retrospective rewriting. | No additional enum or range constraint | Native value / literal text |
| recovered_date | text | no | date | Date newly retrieved source material became available. | No additional enum or range constraint | Native value / literal text |
| recovered_source | text | no | identifier | Printed recovered source packet locator. | No additional enum or range constraint | Native value / literal text |
| current_fact_ids | text | no | identifier | Complete current material fact set; additions drive the new-information test. | No additional enum or range constraint | Native value / literal text |
| current_observation | text | no | text | Concrete current facts and whether they differ from the historical basis. | No additional enum or range constraint | Native value / literal text |
| source_path | text | no | text | Supplied source feed path, not inferred from historical disposition. | PATH_A / PATH_B / PATH_C | Native value / literal text |
| material_delta | boolean | no | flag | True exactly when the current material fact set adds a fact outside the historical set. | No additional enum or range constraint | Native value / literal text |
| expected_route | text | no | text | Completed comparison result; referral disposition remains open. | REVIEW_COMPLETE_NO_NEW / REFERRED_FOR_CASE_REVIEW | Native value / literal text |
| evidence_ids | text | no | identifier | Source for the complete packet and fact dictionary. | No additional enum or range constraint | Native value / literal text |

Foreign key: `unit_id` resolves to `CanonicalUnits (unit_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### DefectChronology — field contract

**Record grain:** One dated mapping-version evidence event or explicitly unavailable historical checkpoint, identified by chronology_id.

**Primary key:** `chronology_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| chronology_id | text | no | identifier | Unique chronology event ID. | No additional enum or range constraint | Native value / literal text |
| event_date | text | no | date | Date of the supplied event or missing historical checkpoint. | No additional enum or range constraint | Native value / literal text |
| source_locator | text | no | identifier | Exact fictional record locator printed in this table. | No additional enum or range constraint | Native value / literal text |
| mapping_version | text | no | text | Known mapping version or explicit UNKNOWN. | No additional enum or range constraint | Native value / literal text |
| record_kind | text | no | text | Nature of the timing evidence. | CHANGE_RECORD / RUNTIME_SNAPSHOT / UNAVAILABLE / DEFECT_REPRODUCTION / PROPOSED_CORRECTION | Native value / literal text |
| observed_fact | text | no | text | Concrete fact supplied by the record. | No additional enum or range constraint | Native value / literal text |
| boundary_limit | text | no | text | What the record cannot establish about scope or completion. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | identifier | Chronology source ID. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.
<!-- FIELD_CONTRACTS:END -->
