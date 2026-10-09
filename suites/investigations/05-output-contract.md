# Investigation Case Review — complete output contract

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

1. Decision questions and current assessment
2. Scope, chronology method, and coverage
3. Findings and contradictions
4. Chronology and funds movement
5. Competing hypothesis tests and decision gates
6. Evidence inventory and provenance
7. Proposed investigative actions
8. Limitations, quality checks, and reviewer decision

## Immutable domain schemas and populated operating rules

### CaseTimeline

**Grain:** One canonical transfer touching A; same-entity mirror legs are represented once. **Primary key:** `event_id`. **Report placement:** section 4.

```text
event_id | event_time | from_node | to_node | amount_usd | currency | linked_return_of | account_a_balance_usd | evidence_ids | claim_class | detail
```

**Populate from:** S01 posted ledger, S08 return references and S09 verified A/B grouping. **Required procedure:** Include 24 canonical transfers in exact time order; keep instructions, pending items and duplicate representations in the raw exclusion bridge.

**Interpretation:** The amount is positive; direction comes from from_node/to_node. Account A balance changes once per transfer. B mirror postings do not create extra economic rows.

**Change and exception handling:** A return reference changes linked net calculations but does not delete either event or resolve purpose. A new posted item changes account and entity totals; a duplicate export changes raw count only.

**Field-level validation:** `event_id`: text, required, unit identifier; `event_time`: text, required, unit text; `from_node`: text, required, unit identifier; `to_node`: text, required, unit identifier; `amount_usd`: number, required, unit USD; `currency`: text, required, unit text, allowed USD; `linked_return_of`: text, nullable, unit identifier; `account_a_balance_usd`: number, required, unit USD; `evidence_ids`: text, required, unit evidence identifiers; `claim_class`: text, required, unit text, allowed Observed; `detail`: text, required, unit text.

### AccountBalances

**Grain:** One account-period balance equation. **Primary key:** `account_id`. **Report placement:** section 4.

```text
account_id | opening_usd | credits_usd | debits_usd | calculated_close_usd | supplied_close_usd | difference_usd | evidence_ids
```

**Populate from:** S01/S02 full account postings and S03 supplied opening/closing controls. **Required procedure:** Create one row for A and one for B. Sum credits/debits from each account’s own book, including both representations of internal movements at their proper account grain.

**Interpretation:** Calculated close=opening+credits-debits; difference=calculated-supplied. Entity close is the sum of the two closes, not the sum of their credits.

**Change and exception handling:** A missing opening or supplied close becomes an explicit unavailable control, not a zero. A nonzero difference requires resolution before completeness is claimed.

**Field-level validation:** `account_id`: text, required, unit identifier; `opening_usd`: number, required, unit USD; `credits_usd`: number, required, unit USD; `debits_usd`: number, required, unit USD; `calculated_close_usd`: number, required, unit USD; `supplied_close_usd`: number, required, unit USD; `difference_usd`: number, required, unit USD; `evidence_ids`: text, required, unit evidence identifiers.

### ClaimTests

**Grain:** One proposition, including favorable and contrary alternatives. **Primary key:** `claim_id`. **Report placement:** section 5.

```text
claim_id | proposition | supporting_ids | conflicting_ids | assessment | confidence | discriminator | evidence_ids
```

**Populate from:** Source propositions in S01–S10 and the six printed claim questions. **Required procedure:** Create one row per falsifiable proposition. Preserve supportive, contradictory and missing evidence even when the final assessment is unresolved.

**Interpretation:** CL02/CL03/CL05 are contradicted; CL01/CL04 unresolved; CL06 supports only timing. Confidence refers to the bounded proposition, not the whole subject.

**Change and exception handling:** A new invoice may resolve amount while leaving beneficiary or delivery unknown. Split a compound claim rather than forcing a single favorable label.

**Field-level validation:** `claim_id`: text, required, unit identifier; `proposition`: text, required, unit text; `supporting_ids`: text, required, unit text; `conflicting_ids`: text, required, unit text; `assessment`: text, required, unit text, allowed SUPPORTED, CONTRADICTED, UNRESOLVED, PATTERN_SUPPORTED; `confidence`: text, required, unit text, allowed HIGH, MODERATE, LOW, NOT ASSESSABLE; `discriminator`: text, required, unit text; `evidence_ids`: text, required, unit evidence identifiers.

### Contradictions

**Grain:** One material contradiction or qualification and its exact decision effect. **Primary key:** `contradiction_id`. **Report placement:** section 5.

```text
contradiction_id | claim_id | left_account | right_account | effect | state | evidence_ids
```

**Populate from:** Both source accounts and the linked ClaimTests row. **Required procedure:** Retain four material differences, including the corrected full-reversal claim and the favorable supported-activity counterexample.

**Interpretation:** Resolved arithmetic and resolved scope remain visible; OPEN denotes an unresolved fact, not a pending formatting task.

**Change and exception handling:** If a source correction resolves a difference, preserve the old and new versions and explain the reason. Do not erase contrary evidence from the chronology.

**Declared joins:** `claim_id` → `ClaimTests.claim_id`. Every supplied child key must resolve before release.

**Field-level validation:** `contradiction_id`: text, required, unit identifier; `claim_id`: text, required, unit identifier; `left_account`: text, required, unit text; `right_account`: text, required, unit text; `effect`: text, required, unit text; `state`: text, required, unit text, allowed OPEN, RESOLVED_ARITHMETIC, RESOLVED_SCOPE; `evidence_ids`: text, required, unit evidence identifiers.

### EvidenceRequests

**Grain:** One decision-sensitive request or satisfied request outcome. **Primary key:** `request_id`. **Report placement:** section 5.

```text
request_id | claim_id | request_text | state | decision_effect | evidence_ids
```

**Populate from:** Live claims, existing source limitations and discriminating information gaps. **Required procedure:** Keep five scoped requests or satisfied outcomes. Request text must identify the event and exact missing linkage, avoiding accusations or unrestricted fishing.

**Interpretation:** RQ01/RQ02/RQ05 cannot be marked executed. RQ03/RQ04 are satisfied for their limited source-retention/ownership purpose, not evidence of full case resolution.

**Change and exception handling:** A partial response closes only the satisfied component. Record readable-but-unlinked documents separately from genuinely corroborating evidence.

**Declared joins:** `claim_id` → `ClaimTests.claim_id`. Every supplied child key must resolve before release.

**Field-level validation:** `request_id`: text, required, unit identifier; `claim_id`: text, required, unit identifier; `request_text`: text, required, unit text; `state`: text, required, unit text, allowed PROPOSED, INACCESSIBLE, SATISFIED_FOR_SCOPE; `decision_effect`: text, required, unit text; `evidence_ids`: text, required, unit evidence identifiers.

### EvidenceProvenance

**Grain:** One source origin or explicitly unavailable supplied item. **Primary key:** `source_id`. **Report placement:** section 5.

```text
source_id | source_title | locator | availability | origin_type | claim_class | limitation
```

**Populate from:** The twelve supplied source origins and availability states. **Required procedure:** Keep inaccessible Contract-C in the manifest. Represent duplicate exports as the same origin, not independent confirmations.

**Interpretation:** Observed describes source-visible content; Reported preserves the customer account or unavailable contract representation. A document’s existence does not establish its substantive assertions.

**Change and exception handling:** A readable replacement gets a version link. A new independent origin can improve corroboration only for the proposition it actually supports.

**Field-level validation:** `source_id`: text, required, unit identifier; `source_title`: text, required, unit text; `locator`: text, required, unit text; `availability`: text, required, unit text, allowed AVAILABLE, INACCESSIBLE; `origin_type`: text, required, unit text; `claim_class`: text, required, unit text, allowed Observed, Reported; `limitation`: text, required, unit text.

### DecisionRecord

**Grain:** One distinct gate; completion is not equivalent to case closure. **Primary key:** `decision_id`. **Report placement:** section 5.

```text
decision_id | gate | status | basis | evidence_ids
```

**Populate from:** Population equations, unresolved purpose tests and actual review authority. **Required procedure:** Keep four gates with different scopes: data complete, T02 hold, T08 hold and human disposition absent.

**Interpretation:** Completion of D01 does not close D02/D03. D04 requires actual supplied human authorization and cannot be inferred from generated artifacts.

**Change and exception handling:** If evidence resolves a purpose gate, record the triggering source and changed claim. Keep the human decision distinct from the assistant recommendation.

**Field-level validation:** `decision_id`: text, required, unit identifier; `gate`: text, required, unit text; `status`: text, required, unit text, allowed COMPLETE, HOLD_EVIDENCE, NOT_RECORDED; `basis`: text, required, unit text; `evidence_ids`: text, required, unit evidence identifiers.

### ProcessQA

**Grain:** One performed fixture check or explicit unrecorded approval gate. **Primary key:** `check_id`. **Report placement:** section 5.

```text
check_id | check | expected | actual | result | evidence_ids
```

**Populate from:** Independent arithmetic and evidence checks in file 09 and the embedded file 10 check. **Required procedure:** Record twelve checks with exact expected and actual results. A passing numeric result does not erase a review-required purpose gate.

**Interpretation:** Nine quantity/coverage checks, the overstatement boundary and remaining authority states must be read according to their individual scope.

**Change and exception handling:** If a source changes, rerun the affected checks and adjacent dependent totals. Preserve failed-before-repair history outside the current clean result view.

**Field-level validation:** `check_id`: text, required, unit identifier; `check`: text, required, unit text; `expected`: text, required, unit text; `actual`: text, required, unit text; `result`: text, required, unit text, allowed PASS, REVIEW REQUIRED, NOT RECORDED; `evidence_ids`: text, required, unit evidence identifiers.

## Completed narrative pattern and adaptation test

Use the eight populated narrative sections in file 10 as a demonstration of the required specificity. For each paragraph, identify the source rows, calculation or decision rule that support it. When adapting, remove the fictional proposition before writing a new one; changing a title or date is not enough. A reviewer should be able to take any quantified sentence and recover its numerator, denominator, unit and scope without asking the assistant what it meant.

All domain records belong in the report or its complete tabular annex as well as the workbook and dashboard. Keep the exact identifiers in every representation. If a table becomes long, split it into labeled contiguous ranges, not selected examples. Preserve the common Evidence register and every semicolon-delimited evidence reference. The completed output remains draft until the applicable quality gates and actual human decision status are accurately recorded.

<!-- FIELD_CONTRACTS:START -->
## Compiled domain field dictionary

This dictionary is part of this attachment. It fixes the type, null rule, unit, permitted values and record identity used by the embedded renderers. It is generated from the same reviewed case contract; no external file is needed. Raw source defects must be retained as raw text under their declared type. Correcting a malformed value requires evidence, not coercion by the renderer.

### CaseTimeline — field contract

**Record grain:** One canonical transfer touching A; same-entity mirror legs are represented once.

**Primary key:** `event_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| event_id | text | no | identifier | Unique canonical economic transfer identifier, not source-row number. | No additional enum or range constraint | Native value / literal text |
| event_time | text | no | text | Exact posted timestamp in ISO-8601 with offset; human narrative uses ET. | No additional enum or range constraint | Native value / literal text |
| from_node | text | no | identifier | Recorded immediate sender node; ultimate ownership not inferred. | No additional enum or range constraint | Native value / literal text |
| to_node | text | no | identifier | Recorded immediate receiver node; purpose not inferred. | No additional enum or range constraint | Native value / literal text |
| amount_usd | number | no | USD | Positive booked USD amount of one canonical transfer. | No additional enum or range constraint | $#,##0.00 |
| currency | text | no | text | Native currency of every monetary record. | USD | Native value / literal text |
| linked_return_of | text | yes | identifier | Parent debit event for explicitly linked return; null otherwise. | No additional enum or range constraint | Native value / literal text |
| account_a_balance_usd | number | no | USD | Account A running balance after this event, opening USD5000. | No additional enum or range constraint | $#,##0.00 |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |
| claim_class | text | no | text | Class of the proposition visible in this event row. | Observed | Native value / literal text |
| detail | text | no | text | Bounded event description including unresolved purpose where relevant. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### AccountBalances — field contract

**Record grain:** One account-period balance equation.

**Primary key:** `account_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| account_id | text | no | identifier | Account identifier in the supplied two-account perimeter. | No additional enum or range constraint | Native value / literal text |
| opening_usd | number | no | USD | Supplied opening balance, not inferred from first transaction. | No additional enum or range constraint | $#,##0.00 |
| credits_usd | number | no | USD | Sum of positive postings to this account, including own-account mirrors. | No additional enum or range constraint | $#,##0.00 |
| debits_usd | number | no | USD | Sum of outgoing postings from this account, including own-account mirrors. | No additional enum or range constraint | $#,##0.00 |
| calculated_close_usd | number | no | USD | Opening plus credits minus debits. | No additional enum or range constraint | $#,##0.00 |
| supplied_close_usd | number | no | USD | Independent supplied close from S03. | No additional enum or range constraint | $#,##0.00 |
| difference_usd | number | no | USD | Calculated close minus supplied close. | No additional enum or range constraint | $#,##0.00 |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ClaimTests — field contract

**Record grain:** One proposition, including favorable and contrary alternatives.

**Primary key:** `claim_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| claim_id | text | no | identifier | Stable falsifiable claim identifier. | No additional enum or range constraint | Native value / literal text |
| proposition | text | no | text | Bounded question that can be supported, contradicted or unresolved. | No additional enum or range constraint | Native value / literal text |
| supporting_ids | text | no | text | Semicolon references or explicit NONE_LOCATED; narrative explains meaning. | No additional enum or range constraint | Native value / literal text |
| conflicting_ids | text | no | text | Semicolon references or explicit NONE_LOCATED. | No additional enum or range constraint | Native value / literal text |
| assessment | text | no | text | Outcome under the printed evidence. | SUPPORTED / CONTRADICTED / UNRESOLVED / PATTERN_SUPPORTED | Native value / literal text |
| confidence | text | no | text | Confidence in this bounded proposition. | HIGH / MODERATE / LOW / NOT ASSESSABLE | Native value / literal text |
| discriminator | text | no | text | Evidence capable of changing the assessment. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### Contradictions — field contract

**Record grain:** One material contradiction or qualification and its exact decision effect.

**Primary key:** `contradiction_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| contradiction_id | text | no | identifier | Stable difference identifier. | No additional enum or range constraint | Native value / literal text |
| claim_id | text | no | identifier | Claim being challenged or qualified. | No additional enum or range constraint | Native value / literal text |
| left_account | text | no | text | One source-supported representation. | No additional enum or range constraint | Native value / literal text |
| right_account | text | no | text | Conflicting or qualifying representation. | No additional enum or range constraint | Native value / literal text |
| effect | text | no | text | Exact consequence for a live decision. | No additional enum or range constraint | Native value / literal text |
| state | text | no | text | Resolution state. | OPEN / RESOLVED_ARITHMETIC / RESOLVED_SCOPE | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Foreign key: `claim_id` resolves to `ClaimTests (claim_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### EvidenceRequests — field contract

**Record grain:** One decision-sensitive request or satisfied request outcome.

**Primary key:** `request_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| request_id | text | no | identifier | Stable proposed request identifier. | No additional enum or range constraint | Native value / literal text |
| claim_id | text | no | identifier | Decision-sensitive claim this request serves. | No additional enum or range constraint | Native value / literal text |
| request_text | text | no | text | Narrow question, records and period; no accusation. | No additional enum or range constraint | Native value / literal text |
| state | text | no | text | Fixture request status. | PROPOSED / INACCESSIBLE / SATISFIED_FOR_SCOPE | Native value / literal text |
| decision_effect | text | no | text | What changes if evidence supports or contradicts the claim. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Foreign key: `claim_id` resolves to `ClaimTests (claim_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### EvidenceProvenance — field contract

**Record grain:** One source origin or explicitly unavailable supplied item.

**Primary key:** `source_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| source_id | text | no | identifier | Exact identifier in common Evidence register. | No additional enum or range constraint | Native value / literal text |
| source_title | text | no | text | Fictional source name. | No additional enum or range constraint | Native value / literal text |
| locator | text | no | text | Exact raw-data locator in file 10. | No additional enum or range constraint | Native value / literal text |
| availability | text | no | text | Availability distinct from reliability. | AVAILABLE / INACCESSIBLE | Native value / literal text |
| origin_type | text | no | text | Origin family relevant to independence. | No additional enum or range constraint | Native value / literal text |
| claim_class | text | no | text | Class applicable to source description. | Observed / Reported | Native value / literal text |
| limitation | text | no | text | Specific proposition this source cannot establish. | No additional enum or range constraint | Native value / literal text |


### DecisionRecord — field contract

**Record grain:** One distinct gate; completion is not equivalent to case closure.

**Primary key:** `decision_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| decision_id | text | no | identifier | Stable analytical gate identifier. | No additional enum or range constraint | Native value / literal text |
| gate | text | no | text | Decision being recorded. | No additional enum or range constraint | Native value / literal text |
| status | text | no | text | Analytical state distinct from human disposition. | COMPLETE / HOLD_EVIDENCE / NOT_RECORDED | Native value / literal text |
| basis | text | no | text | Case-specific reason. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ProcessQA — field contract

**Record grain:** One performed fixture check or explicit unrecorded approval gate.

**Primary key:** `check_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| check_id | text | no | identifier | Stable reperformable check. | No additional enum or range constraint | Native value / literal text |
| check | text | no | text | Specific invariant or calculation. | No additional enum or range constraint | Native value / literal text |
| expected | text | no | text | Independent expected outcome. | No additional enum or range constraint | Native value / literal text |
| actual | text | no | text | Fixture outcome; must be recomputed when adapted. | No additional enum or range constraint | Native value / literal text |
| result | text | no | text | Fixture analytical result. | PASS / REVIEW REQUIRED / NOT RECORDED | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.
<!-- FIELD_CONTRACTS:END -->
