# Output contract — Monitoring System Independent Challenge and Validation

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

1. Validation opinion and use restrictions
2. System scope classification and review design
3. Material validation findings
4. Component tests and outcome registers
5. Issue resolution and release gates
6. Evidence provenance and competing interpretations
7. Required remediation and further challenge
8. Limitations quality review and human disposition

## Populated report narrative model

### Validation opinion and use restrictions

Do not support release of I1 on the supplied evidence. The implementation differs from the reference at inclusive boundaries and missing values; broader effectiveness, transaction lineage, objective review and actual authorization remain unresolved.

### System scope classification and review design

The supplied subject is deterministic monitoring logic over 24 feature-level customer-window units. R1 tests amount>=10000, count>=3 and originators>=2; absent amount returns unknown. I1 uses amount>10000 and returns false for absent amount. No universal institutional model classification is implied.

### Material validation findings

Four known positive boundary units are lost. Four missing amounts are silently changed to false. A separate conceptual limitation excludes four single-originator positives. These mechanisms require distinct findings rather than one combined percentage.

### Component tests and outcome registers

R1 gives TP8 FP0 FN4 TN8; I1 gives TP4 FP0 FN8 TN8; C1 gives TP12 FP0 FN0 TN8. All matrices use twenty known labels. Four UNKNOWN labels stay outside; only R1 and C1 retain unknown input states.

### Issue resolution and release gates

The 24 tests distinguish arithmetic passes from failed concepts or implementation and blocked evidence requests. Four issues remain OPEN or BLOCKED. A passed matrix calculation means the arithmetic is right; it does not mean the underlying system meets its intended use.

### Evidence provenance and competing interpretations

SYN-101 contains features, not source transactions. SYN-102 supplies three independent predicate descriptions. SYN-103 records fictional governance gaps. Current public model guidance must be assessed for scope and applicability; this deterministic example is not automatically a model under that definition.

### Required remediation and further challenge

Proposed corrections need versioned implementation evidence, unchanged-case regression tests, feature lineage, independent outcome review and a real human disposition. The challenger is a diagnostic stress of one assumption, not an approved replacement.

### Limitations quality review and human disposition

Reproduce eight mismatches, split four boundary losses from four missing-state differences, and verify each matrix. No probability interval or deployment approval follows from designed fictional examples. Keep the report in a restricted draft state until the stated evidence gates are resolved.

## Domain register purposes and cross-checks

### ComponentInventory

Exact ordered columns: component_id, name, classification, input_grain, output, theory_basis, limitation, evidence_ids.

The specimen contains **5 records** at the key grain `component_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `component_id` is demonstrated by `CMP-01`, `CMP-02`, `CMP-03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

### ChallengeTests

Exact ordered columns: test_id, domain, test_name, procedure, expected, actual, result, evidence_ids.

The specimen contains **24 records** at the key grain `test_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `test_id` is demonstrated by `C01`, `C02`, `C03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

### OutcomeUnits

Exact ordered columns: unit_id, segment, amount_usd, eligible_count, originators, label, reference_hit, implemented_hit, challenger_hit, mismatch, evidence_ids.

The specimen contains **24 records** at the key grain `unit_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `unit_id` is demonstrated by `V01`, `V02`, `V03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

### OutcomeMetrics

Exact ordered columns: variant, population_n, known_n, unknown_n, tp, fp, fn, tn, all_hits, unassessable_n, precision, recall, evidence_ids.

The specimen contains **3 records** at the key grain `variant`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `variant` is demonstrated by `REFERENCE`, `IMPLEMENTED`, `CHALLENGER`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

### IssueRegister

Exact ordered columns: issue_id, linked_tests, severity, affected_ids, issue, closure_evidence, state, evidence_ids.

The specimen contains **4 records** at the key grain `issue_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `issue_id` is demonstrated by `MV-I01`, `MV-I02`, `MV-I03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

### EvidenceProvenance

Exact ordered columns: source_id, source_kind, as_of, availability, unit_count, grain, limitation, evidence_ids.

The specimen contains **3 records** at the key grain `source_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `source_id` is demonstrated by `SYN-101`, `SYN-102`, `SYN-103`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

### ProcessQA

Exact ordered columns: check_id, check_scope, expected, actual, status, reviewer, evidence_ids.

The specimen contains **7 records** at the key grain `check_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `check_id` is demonstrated by `MV-Q01`, `MV-Q02`, `MV-Q03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

### ReleaseGates

Exact ordered columns: gate_id, requirement, current_evidence, gate_state, dependency, permitted_claim, evidence_ids.

The specimen contains **6 records** at the key grain `gate_id`. Preserve each key and every column in the workbook. The report may arrange long rows as field/value records, but must not reduce the register to its most favorable entries. The key is a uniqueness requirement within this table, not permission to deduplicate a different table at the same apparent ID.

The key field `gate_id` is demonstrated by `MV-G01`, `MV-G02`, `MV-G03`. Keep it as text where the contract declares an identifier. A missing or duplicated key blocks a complete export because a reviewer could not trace individual records or compare versions reliably.

<!-- FIELD_CONTRACTS:START -->
## Compiled domain field dictionary

This dictionary is part of this attachment. It fixes the type, null rule, unit, permitted values and record identity used by the embedded renderers. It is generated from the same reviewed case contract; no external file is needed. Raw source defects must be retained as raw text under their declared type. Correcting a malformed value requires evidence, not coercion by the renderer.

### ComponentInventory — field contract

**Record grain:** One reviewed analytical or governance component, identified by component_id, at the stated system boundary.

**Primary key:** `component_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| component_id | text | no | identifier | Stable analytical component identifier. | No additional enum or range constraint | Native value / literal text |
| name | text | no | text | Component purpose and representation. | No additional enum or range constraint | Native value / literal text |
| classification | text | no | text | Toolkit analytical classification; institutional determination absent. | DETERMINISTIC_RULE / DETERMINISTIC_TRANSFORM / HUMAN_PROCESS | Native value / literal text |
| input_grain | text | no | text | Exact unit consumed by the component. | No additional enum or range constraint | Native value / literal text |
| output | text | no | text | Declared output and permitted values. | No additional enum or range constraint | Native value / literal text |
| theory_basis | text | no | text | Whether quantitative theory underpins an estimate or only fixed logic. | No additional enum or range constraint | Native value / literal text |
| limitation | text | no | text | Scope not established by this component. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | identifier | Supporting source IDs. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ChallengeTests — field contract

**Record grain:** One predeclared validation test, identified by test_id, within one validation domain.

**Primary key:** `test_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| test_id | text | no | identifier | Unique validation test key. | No additional enum or range constraint | Native value / literal text |
| domain | text | no | text | Validation dimension. | CONCEPT / DATA / IMPLEMENTATION / OUTCOMES / GOVERNANCE / MONITORING | Native value / literal text |
| test_name | text | no | text | Distinct question challenged. | No additional enum or range constraint | Native value / literal text |
| procedure | text | no | text | Specific reproducible review action. | No additional enum or range constraint | Native value / literal text |
| expected | text | no | text | Predeclared criterion or expected calculation. | No additional enum or range constraint | Native value / literal text |
| actual | text | no | text | Fictional observation and record IDs. | No additional enum or range constraint | Native value / literal text |
| result | text | no | text | PASS meets test criterion; FAIL contradicts it; BLOCKED lacks needed evidence. | PASS / FAIL / BLOCKED | Native value / literal text |
| evidence_ids | text | no | identifier | Sources supporting the stated result. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### OutcomeUnits — field contract

**Record grain:** One feature-level customer-window test unit, identified by unit_id, evaluated by the reference, implementation and challenger.

**Primary key:** `unit_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| unit_id | text | no | identifier | One feature-level customer-window test unit. | No additional enum or range constraint | Native value / literal text |
| segment | text | no | text | Fictional segment label. | RETAIL / BUSINESS / CORRESPONDENT / DIGITAL_SERVICE | Native value / literal text |
| amount_usd | number | yes | USD | Eligible credits in USD for the supplied fixed window; null means absent. | No additional enum or range constraint | $#,##0.00 |
| eligible_count | integer | no | count | Number of eligible posted credits in that window. | No additional enum or range constraint | Native value / literal text |
| originators | integer | no | count | Distinct originator identities under the frozen supplied definition. | No additional enum or range constraint | Native value / literal text |
| label | text | no | text | Synthetic outcome; UNKNOWN stays outside matrices. | POSITIVE / NEGATIVE / UNKNOWN | Native value / literal text |
| reference_hit | boolean | yes | flag | Inclusive amount and count rule; null when amount absent. | No additional enum or range constraint | Native value / literal text |
| implemented_hit | boolean | no | flag | Observed I1 result with strict amount test and missing-to-false defect. | No additional enum or range constraint | Native value / literal text |
| challenger_hit | boolean | yes | flag | Diagnostic rule without originator restriction; null when amount absent. | No additional enum or range constraint | Native value / literal text |
| mismatch | boolean | no | flag | True when reference and implemented values differ, including null versus false. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | identifier | Raw features and independent rule definitions. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### OutcomeMetrics — field contract

**Record grain:** One comparison variant summarized across the same complete 24-unit fixture and 20-unit known-label subset.

**Primary key:** `variant`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| variant | text | no | text | Frozen comparison variant. | REFERENCE / IMPLEMENTED / CHALLENGER | Native value / literal text |
| population_n | integer | no | count | All supplied units. | No additional enum or range constraint | Native value / literal text |
| known_n | integer | no | count | Available positive or negative labels. | No additional enum or range constraint | Native value / literal text |
| unknown_n | integer | no | count | Missing outcome labels excluded from confusion matrix. | No additional enum or range constraint | Native value / literal text |
| tp | integer | no | count | Known positive and variant true. | No additional enum or range constraint | Native value / literal text |
| fp | integer | no | count | Known negative and variant true. | No additional enum or range constraint | Native value / literal text |
| fn | integer | no | count | Known positive and variant false. | No additional enum or range constraint | Native value / literal text |
| tn | integer | no | count | Known negative and variant false. | No additional enum or range constraint | Native value / literal text |
| all_hits | integer | no | count | True outputs across all twenty-four units. | No additional enum or range constraint | Native value / literal text |
| unassessable_n | integer | no | count | Null outputs due to missing input; separate from unknown labels. | No additional enum or range constraint | Native value / literal text |
| precision | number | yes | ratio | TP / (TP+FP) on known labels. | No additional enum or range constraint | 0.0% |
| recall | number | yes | ratio | TP / (TP+FN) on known labels. | No additional enum or range constraint | 0.0% |
| evidence_ids | text | no | identifier | Feature and predicate sources. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### IssueRegister — field contract

**Record grain:** One distinct validation issue, identified by issue_id, with linked tests, affected records and closure evidence.

**Primary key:** `issue_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| issue_id | text | no | identifier | Unique issue key. | No additional enum or range constraint | Native value / literal text |
| linked_tests | text | no | identifier | Semicolon-delimited ChallengeTests identifiers. | No additional enum or range constraint | Native value / literal text |
| severity | text | no | text | Illustrative prioritization independent of certainty. | HIGH / MEDIUM / LOW | Native value / literal text |
| affected_ids | text | no | text | Exact affected units or component IDs. | No additional enum or range constraint | Native value / literal text |
| issue | text | no | text | Observed deficiency or limitation. | No additional enum or range constraint | Native value / literal text |
| closure_evidence | text | no | text | Minimum evidence needed to test a proposed correction. | No additional enum or range constraint | Native value / literal text |
| state | text | no | text | No issue is operationally closed in this fixture. | OPEN / BLOCKED | Native value / literal text |
| evidence_ids | text | no | identifier | Underlying case evidence. | No additional enum or range constraint | Native value / literal text |

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

### ReleaseGates — field contract

**Record grain:** One specific release-evidence gate, identified by gate_id, for the stated component and intended use.

**Primary key:** `gate_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| gate_id | text | no | identifier | Unique human review gate. | No additional enum or range constraint | Native value / literal text |
| requirement | text | no | text | Evidence needed before supporting the stated use. | No additional enum or range constraint | Native value / literal text |
| current_evidence | text | no | text | What is actually supplied. | No additional enum or range constraint | Native value / literal text |
| gate_state | text | no | text | No failed or blocked gate can be treated as satisfied. | SATISFIED_FIXTURE_ONLY / FAILED / BLOCKED | Native value / literal text |
| dependency | text | no | text | Preceding issue or evidence requirement. | No additional enum or range constraint | Native value / literal text |
| permitted_claim | text | no | text | Narrow statement that can currently be made. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | identifier | Evidence for the gate. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.
<!-- FIELD_CONTRACTS:END -->
