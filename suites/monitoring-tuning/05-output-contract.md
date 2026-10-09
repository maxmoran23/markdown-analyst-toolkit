# Output contract — Monitoring Scenario and Threshold Review

## Immutable presentation and interchange rules

Produce the eight report sections in the order printed below. Keep the six common workbook tabs: Summary, Dashboard, Findings, Evidence, Actions and QA. Append all eight domain tables in the declared order. Do not replace a detailed register with a favorable summary. Column names are stable machine keys even when the report presents them as readable field labels. The report may display long rows vertically, but the workbook retains every column and every record. The dashboard exposes the same case without external data requests.

Store identifiers and source locators as text. Store counts as nonnegative integers, monetary amounts as numeric values with declared currency, rates as fractions and booleans as true or false. Use null for an unknown numeric or boolean result. A rate whose denominator is zero is null with a visible reason. Keep exact numerical values in the interchange representation and apply rounding only for display. A displayed percentage must have its numerator, denominator and inclusion rule available in the accompanying method note.

For currency fields, do not aggregate different currencies without an explicitly supplied conversion method and date. An activity total is not a loss estimate, an illicit-funds total or a statutory threshold. For workload, distinguish hours assumed per case from hours measured in an actual review process. For outcome metrics, distinguish labeled-sample performance from population effectiveness. For completion, distinguish received-row accounting, retrieved-unit coverage, desk review completion, downstream case disposition and whole-review acceptance. These meanings must survive every export.

An evidence key in a domain record must resolve to the common Evidence register. Semicolon-delimited keys represent several distinct sources; do not treat the combined string as one new source. A foreign key must resolve at the declared parent grain. A composite key is unique only when all its components are considered together. Retain nulls for genuinely unavailable links where the field contract permits them, and name the resulting limitation. Do not create dummy parent records merely to make a join pass.

The final findings table separates severity, confidence and evidence class. Severity is the consequence or priority under the stated illustrative rubric; confidence concerns support for the observation; evidence class states how the claim is known. A high-severity uncertainty can have low confidence, while a confidently reproduced arithmetic defect can have a narrow practical consequence. The dashboard must not use one field as a substitute for another. Every recommendation stays distinct from the human disposition and from proof that an action occurred.

## Narrative completion standard

Each required report section needs complete case-specific prose. Do not output headings with instructions to fill them later. The recommendation section states the supported answer and its restrictions first. The scope section gives the period, population, exclusions, unit of analysis and method. The findings section gives facts and counterevidence. The register sections explain material patterns and exceptions without hiding detailed rows. The evidence section distinguishes inspected material from cited context. The action section names prerequisites and unrecorded assignments. The last section reports actual QA work and unresolved decisions.

Use a sentence pattern that makes a claim inspectable: within a specified population, the identified records show a stated result under the declared rule; the result means a bounded consequence because of the cited evidence; the alternative explanation or missing input is explicit; the proposed next step requests a defined piece of evidence or a human decision. Do not mechanically repeat the pattern where a table already carries the information. Use it to check whether a polished paragraph has lost a denominator, basis or qualification.

A fictional specimen can contain completed fictional calculations and populated example review outcomes. It cannot contain an actual human signoff. Preserve the banner and source labels until every fictional value has been replaced and rechecked. Do not retain specimen case IDs in a live deliverable. If only part of the specimen has been replaced, label the whole package as a mixed draft and prevent a conclusion that appears to concern a real institution. Fully populated does not mean every uncertainty must be converted into a favorable fact.

## Required report heading order

1. Candidate recommendation and restrictions
2. Evaluation scope and partition controls
3. Coverage workload and routing findings
4. Complete candidate and population registers
5. Below-threshold review and decision gates
6. Evidence provenance uncertainty and blind spots
7. Validation and change proposals
8. Limitations quality review and human disposition

## Populated report narrative model

### Candidate recommendation and restrictions

LOW50 is a further-validation candidate only. Its known-label raw coverage improves, but G17 suppression removes a known positive, missing outcomes prevent population effectiveness claims, and illustrative workload exceeds capacity. No candidate is authorized for deployment.

### Evaluation scope and partition controls

The 36 fictional units form three disjoint partitions of twelve. Three segments each contain four units per partition. Group pairs never cross partitions. Scores and four candidates are predeclared; the ALL row is descriptive reconciliation rather than an independent evaluation set.

### Coverage workload and routing findings

Raw predicate results, suppression, merged case counts and workload are separate stages. Group G17 suppresses HOLDOUT U33 and U34. A case merge does not automatically credit unhit siblings as detected. The raw and retained positive-unit numerators remain separate.

### Complete candidate and population registers

ALL BASE60 TP11 FP9 FN5 TN4; HIGH75 TP9 FP2 FN7 TN11; LOW50 TP16 FP9 FN0 TN4; SEGMENTED TP10 FP9 FN6 TN4. Each matrix has 29 known labels, with seven other units retained outside the matrix.

### Below-threshold review and decision gates

The complete BASE60 below-threshold frame has fifteen units. Six assigned-rank selections contain three POSITIVE, one NEGATIVE, one UNKNOWN and one CENSORED outcome. Nine frame units remain unreviewed by this draw. The illustrative ranks do not support a random-sample confidence interval.

### Evidence provenance uncertainty and blind spots

The source ledger preserves 36 units, four candidates, one suppression group with incomplete authority, and fifteen below-threshold frame records. Public guidance provides governance context. It does not establish a legal cutoff, a live model classification or approval to suppress activity.

### Validation and change proposals

Proposed work is to establish suppression authority or revise routing, label unavailable outcomes without leakage, validate incremental segment losses, and test capacity on protected data. The human deployment disposition remains NOT_RECORDED.

### Limitations quality review and human disposition

Reperform all candidate matrices and the conservation equations. Validate exact threshold boundaries, merge groups, null rates and missing labels. Passing the fictional checks establishes consistency of this example only; it cannot validate live detection effectiveness.

## Domain register purposes and cross-checks

### Population

Exact ordered columns: unit_id, group_id, partition, segment, score, label, label_basis, eligible, suppressed, review_hours, evidence_ids.

The specimen contains **36 records** at the key grain `unit_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `unit_id` is demonstrated by `U01`, `U02`, `U03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

### Candidates

Exact ordered columns: candidate_id, retail_threshold, business_threshold, correspondent_threshold, comparator, freeze_state, evidence_ids.

The specimen contains **4 records** at the key grain `candidate_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `candidate_id` is demonstrated by `BASE60`, `HIGH75`, `LOW50`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

### CandidateMetrics

Exact ordered columns: candidate_id, partition, population_n, known_n, tp, fp, fn, tn, unknown_n, raw_hits, retained_hits, queued_cases, workload_hours, precision, recall, retained_positive_hits.

The specimen contains **16 records** at the key grain `candidate_id, partition`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `candidate_id` is demonstrated by `BASE60`, `BASE60`, `BASE60`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

The key field `partition` is demonstrated by `TRAIN`, `VALIDATION`, `HOLDOUT`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

The join from `candidate_id` to `Candidates.candidate_id` must resolve exactly at the parent key. Check the number of matched, unmatched and multiply matched rows before using the join. A nullable missing link remains visible with its reason; an unexplained nonnull key that does not resolve is an error, not an excluded observation.

### AlertRouting

Exact ordered columns: hit_id, candidate_id, unit_id, group_id, route_state, case_id, lead_unit_id, routing_basis, evidence_ids.

The specimen contains **78 records** at the key grain `hit_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `hit_id` is demonstrated by `BASE60-U01`, `BASE60-U02`, `BASE60-U05`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

The join from `candidate_id` to `Candidates.candidate_id` must resolve exactly at the parent key. Check the number of matched, unmatched and multiply matched rows before using the join. A nullable missing link remains visible with its reason; an unexplained nonnull key that does not resolve is an error, not an excluded observation.

The join from `unit_id` to `Population.unit_id` must resolve exactly at the parent key. Check the number of matched, unmatched and multiply matched rows before using the join. A nullable missing link remains visible with its reason; an unexplained nonnull key that does not resolve is an error, not an excluded observation.

The join from `lead_unit_id` to `Population.unit_id` must resolve exactly at the parent key. Check the number of matched, unmatched and multiply matched rows before using the join. A nullable missing link remains visible with its reason; an unexplained nonnull key that does not resolve is an error, not an excluded observation.

### BelowThreshold

Exact ordered columns: draw_id, unit_id, partition, frame_n, rank, selected, review_label, design, evidence_ids.

The specimen contains **15 records** at the key grain `draw_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `draw_id` is demonstrated by `BTL-U03`, `BTL-U04`, `BTL-U07`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

The join from `unit_id` to `Population.unit_id` must resolve exactly at the parent key. Check the number of matched, unmatched and multiply matched rows before using the join. A nullable missing link remains visible with its reason; an unexplained nonnull key that does not resolve is an error, not an excluded observation.

### CandidateDecisions

Exact ordered columns: candidate_id, decision_state, coverage_gate, capacity_gate, routing_gate, next_evidence, human_disposition, evidence_ids.

The specimen contains **4 records** at the key grain `candidate_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `candidate_id` is demonstrated by `BASE60`, `HIGH75`, `LOW50`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

The join from `candidate_id` to `Candidates.candidate_id` must resolve exactly at the parent key. Check the number of matched, unmatched and multiply matched rows before using the join. A nullable missing link remains visible with its reason; an unexplained nonnull key that does not resolve is an error, not an excluded observation.

### EvidenceProvenance

Exact ordered columns: source_id, source_kind, as_of, availability, unit_count, grain, limitation, evidence_ids.

The specimen contains **4 records** at the key grain `source_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `source_id` is demonstrated by `SYN-001`, `SYN-002`, `SYN-003`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

### ProcessQA

Exact ordered columns: check_id, check_scope, expected, actual, status, reviewer, evidence_ids.

The specimen contains **6 records** at the key grain `check_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `check_id` is demonstrated by `MT-Q01`, `MT-Q02`, `MT-Q03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

<!-- FIELD_CONTRACTS:START -->
## Compiled domain field dictionary

This dictionary is part of this attachment. It fixes the type, null rule, unit, permitted values and record identity used by the embedded renderers. It is generated from the same reviewed case contract; no external file is needed. Raw source defects must be retained as raw text under their declared type. Correcting a malformed value requires evidence, not coercion by the renderer.

### Population — field contract

**Record grain:** One eligible scored customer-window unit, identified by unit_id, before candidate selection or routing.

**Primary key:** `unit_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| unit_id | text | no | identifier | One scored customer-window; never a transaction count. | No additional enum or range constraint | Native value / literal text |
| group_id | text | no | identifier | Frozen merge/dependence group containing two units in one partition. | No additional enum or range constraint | Native value / literal text |
| partition | text | no | text | Prospectively assigned evaluation partition. | TRAIN / VALIDATION / HOLDOUT | Native value / literal text |
| segment | text | no | text | Frozen customer segment. | RETAIL / SMALL_BUSINESS / CORRESPONDENT | Native value / literal text |
| score | number | no | score | Supplied deterministic score on a 0 to 100 scale. | No additional enum or range constraint | Native value / literal text |
| label | text | no | text | Available fictional review outcome as of cutoff. | POSITIVE / NEGATIVE / UNKNOWN / CENSORED | Native value / literal text |
| label_basis | text | no | text | Provenance or reason the label is not mature. | No additional enum or range constraint | Native value / literal text |
| eligible | boolean | no | flag | Whether the supplied unit meets the frozen population predicate. | No additional enum or range constraint | Native value / literal text |
| suppressed | boolean | no | flag | Whether group G17 is removed by the illustrative suppression list. | No additional enum or range constraint | Native value / literal text |
| review_hours | number | no | hours | Fixed lead-case workload assumption by segment, before merge additions. | No additional enum or range constraint | 0.00 |
| evidence_ids | text | no | identifier | Supporting synthetic source IDs. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### Candidates — field contract

**Record grain:** One frozen candidate configuration, identified by candidate_id, containing all three segment thresholds.

**Primary key:** `candidate_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| candidate_id | text | no | identifier | Frozen candidate key. | No additional enum or range constraint | Native value / literal text |
| retail_threshold | number | no | score | Inclusive RETAIL score cutoff. | No additional enum or range constraint | Native value / literal text |
| business_threshold | number | no | score | Inclusive SMALL_BUSINESS score cutoff. | No additional enum or range constraint | Native value / literal text |
| correspondent_threshold | number | no | score | Inclusive CORRESPONDENT score cutoff. | No additional enum or range constraint | Native value / literal text |
| comparator | text | no | text | Exact comparison operator. | GREATER_OR_EQUAL | Native value / literal text |
| freeze_state | text | no | text | All candidates declared before examining protected results. | ILLUSTRATIVE_PREFROZEN | Native value / literal text |
| evidence_ids | text | no | identifier | Parameter evidence ID. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### CandidateMetrics — field contract

**Record grain:** One candidate_id and partition combination, including a separately labeled ALL reconciliation across the three partitions.

**Primary key:** `candidate_id + partition`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| candidate_id | text | no | identifier | Candidate key. | No additional enum or range constraint | Native value / literal text |
| partition | text | no | text | Evaluation partition or ALL descriptive reconciliation. | TRAIN / VALIDATION / HOLDOUT / ALL | Native value / literal text |
| population_n | integer | no | count | All eligible supplied units in this partition. | No additional enum or range constraint | Native value / literal text |
| known_n | integer | no | count | POSITIVE plus NEGATIVE units only. | No additional enum or range constraint | Native value / literal text |
| tp | integer | no | count | Known positive unit meeting the raw predicate before routing. | No additional enum or range constraint | Native value / literal text |
| fp | integer | no | count | Known negative unit meeting the raw predicate. | No additional enum or range constraint | Native value / literal text |
| fn | integer | no | count | Known positive unit below the raw predicate. | No additional enum or range constraint | Native value / literal text |
| tn | integer | no | count | Known negative unit below the raw predicate. | No additional enum or range constraint | Native value / literal text |
| unknown_n | integer | no | count | UNKNOWN plus CENSORED units outside the confusion matrix. | No additional enum or range constraint | Native value / literal text |
| raw_hits | integer | no | count | All units meeting the predicate, including unavailable labels. | No additional enum or range constraint | Native value / literal text |
| retained_hits | integer | no | count | Raw hits remaining after suppression, before group merge. | No additional enum or range constraint | Native value / literal text |
| queued_cases | integer | no | count | Distinct retained group IDs; not a unit count. | No additional enum or range constraint | Native value / literal text |
| workload_hours | number | no | hours | Lead hours plus 0.25 hours for every additional retained unit in a group. | No additional enum or range constraint | 0.00 |
| precision | number | yes | ratio | TP divided by TP plus FP on available labels. | No additional enum or range constraint | 0.0% |
| recall | number | yes | ratio | TP divided by TP plus FN on available labels. | No additional enum or range constraint | 0.0% |
| retained_positive_hits | integer | no | count | Known positive units reaching a queued case; this does not credit unhit siblings. | No additional enum or range constraint | Native value / literal text |

Foreign key: `candidate_id` resolves to `Candidates (candidate_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.

### AlertRouting — field contract

**Record grain:** One raw candidate-unit hit, identified by hit_id, with its suppression or merged-case route.

**Primary key:** `hit_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| hit_id | text | no | identifier | Unique candidate-unit raw hit key. | No additional enum or range constraint | Native value / literal text |
| candidate_id | text | no | identifier | Candidate responsible for this raw hit. | No additional enum or range constraint | Native value / literal text |
| unit_id | text | no | identifier | Exact scored unit; lookup label separately. | No additional enum or range constraint | Native value / literal text |
| group_id | text | no | identifier | Frozen group used for merging only within a partition. | No additional enum or range constraint | Native value / literal text |
| route_state | text | no | text | Mutually exclusive hit routing outcome. | SUPPRESSED / QUEUED_LEAD / MERGED_CHILD | Native value / literal text |
| case_id | text | yes | identifier | Candidate-group queued case key; null for suppressed hits. | No additional enum or range constraint | Native value / literal text |
| lead_unit_id | text | yes | identifier | Smallest hit unit ID in the retained group; null when suppressed. | No additional enum or range constraint | Native value / literal text |
| routing_basis | text | no | text | Evidence or missing authorization underlying the route. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | identifier | Sources for routing inputs and predicate lineage. | No additional enum or range constraint | Native value / literal text |

Foreign key: `candidate_id` resolves to `Candidates (candidate_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Foreign key: `unit_id` resolves to `Population (unit_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Foreign key: `lead_unit_id` resolves to `Population (unit_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### BelowThreshold — field contract

**Record grain:** One unit in the complete BASE60 nonhit frame within its frozen partition, whether selected for review or not.

**Primary key:** `draw_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| draw_id | text | no | identifier | Unique frame-row identifier. | No additional enum or range constraint | Native value / literal text |
| unit_id | text | no | identifier | BASE60 nonhit unit. | No additional enum or range constraint | Native value / literal text |
| partition | text | no | text | Frozen stratum; five nonhits per partition. | TRAIN / VALIDATION / HOLDOUT | Native value / literal text |
| frame_n | integer | no | count | Complete number of eligible nonhits in this stratum. | No additional enum or range constraint | Native value / literal text |
| rank | integer | no | rank | Supplied distinct rank within the stratum. | No additional enum or range constraint | Native value / literal text |
| selected | boolean | no | flag | True for ranks one and two. | No additional enum or range constraint | Native value / literal text |
| review_label | text | no | text | Observed selected-row outcome or NOT_REVIEWED for unselected records. | POSITIVE / NEGATIVE / UNKNOWN / CENSORED / NOT_REVIEWED | Native value / literal text |
| design | text | no | text | Fixture rank list is illustrative; it makes no random-sampling claim. | ILLUSTRATIVE_RANK | Native value / literal text |
| evidence_ids | text | no | identifier | Complete supplied frame and draw record. | No additional enum or range constraint | Native value / literal text |

Foreign key: `unit_id` resolves to `Population (unit_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### CandidateDecisions — field contract

**Record grain:** One proposed analytical disposition for one candidate_id at the case cutoff; this is not a human deployment approval.

**Primary key:** `candidate_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| candidate_id | text | no | identifier | Candidate key. | No additional enum or range constraint | Native value / literal text |
| decision_state | text | no | text | Current proposed analytical recommendation. | BASELINE_ONLY / DO_NOT_SUPPORT / FURTHER_VALIDATION_ONLY | Native value / literal text |
| coverage_gate | text | no | text | Explicit known-positive and unknown-label assessment. | No additional enum or range constraint | Native value / literal text |
| capacity_gate | text | no | text | Illustrative hours gate; never the only selection criterion. | No additional enum or range constraint | Native value / literal text |
| routing_gate | text | no | text | Status of suppression verification. | No additional enum or range constraint | Native value / literal text |
| next_evidence | text | no | text | Concrete prerequisite for further consideration. | No additional enum or range constraint | Native value / literal text |
| human_disposition | text | no | text | Operational approval is absent. | NOT_RECORDED | Native value / literal text |
| evidence_ids | text | no | identifier | Sources underlying the recommendation. | No additional enum or range constraint | Native value / literal text |

Foreign key: `candidate_id` resolves to `Candidates (candidate_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
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
<!-- FIELD_CONTRACTS:END -->
