# Alert Adjudication Quality Review — complete output contract

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

1. Quality decision and open gates
2. Scope, supplied criteria and review design
3. Material and nonmaterial findings
4. Case packets and original review votes
5. Criteria, defects, calibration and remediation
6. Evidence and decision-time provenance
7. Proposed repairs and closure tests
8. Quality checks, limitations and human disposition

## Immutable domain schemas and populated operating rules

### CasePackets

**Grain:** One completed case packet selected for calibration, not a random population sample. **Primary key:** `case_id`. **Report placement:** section 4.

```text
case_id | case_topic | raw_packet | consensus | rationale | evidence_ids
```

**Populate from:** Twelve complete fictional packet summaries, Q01–Q12. **Required procedure:** Retain one row per selected packet and distinguish packet facts from later consensus. This is deliberate calibration selection, not a random sample.

**Interpretation:** ACCEPT/REWORK/INSUFFICIENT are quality outcomes, not underlying alert closure or filing decisions.

**Change and exception handling:** A later source can resolve assessability and change consensus. Preserve original packet version and availability chronology so historical review remains reproducible.

**Field-level validation:** `case_id`: text, required, unit identifier; `case_topic`: text, required, unit text; `raw_packet`: text, required, unit text; `consensus`: text, required, unit text, allowed ACCEPT, REWORK, INSUFFICIENT; `rationale`: text, required, unit text; `evidence_ids`: text, required, unit evidence identifiers.

### ReviewVotes

**Grain:** One original blind case-reviewer assessment;24 votes over 12 cases. **Primary key:** `vote_id`. **Report placement:** section 4.

```text
vote_id | case_id | reviewer_id | vote | round | evidence_ids
```

**Populate from:** Q13 original blind round 1 ratings. **Required procedure:** Keep 24 rows: each case appears once for R1 and once for R2. Do not overwrite the vote when discussion produces consensus.

**Interpretation:** Two votes are not two cases. Pair by case ID and packet version before calculating agreement.

**Change and exception handling:** A missing vote reduces complete-pair count; a second round creates new records with an explicit round rather than a duplicate-key overwrite.

**Declared joins:** `case_id` → `CasePackets.case_id`. Every supplied child key must resolve before release.

**Field-level validation:** `vote_id`: text, required, unit identifier; `case_id`: text, required, unit identifier; `reviewer_id`: text, required, unit identifier; `vote`: text, required, unit text, allowed ACCEPT, REWORK, INSUFFICIENT; `round`: integer, required, unit count; `evidence_ids`: text, required, unit evidence identifiers.

### QualityCriteria

**Grain:** One supplied illustrative quality criterion; no implied universal legal mandate. **Primary key:** `criterion_id`. **Report placement:** section 5.

```text
criterion_id | criterion | rule | materiality_class | boundary | evidence_ids
```

**Populate from:** Supplied illustrative policy CP-QA-1. **Required procedure:** Keep eight criterion cards with material, assessability or nonmaterial boundaries. Apply the exact rule to the case condition before assigning a defect.

**Interpretation:** The criterion source is internal illustrative policy, not a universal regulatory mandate. K06 specifically prevents unsupported legal-premise findings.

**Change and exception handling:** A policy change requires effective-date and historical applicability review. A reviewer’s preferred writing style does not automatically become a criterion.

**Field-level validation:** `criterion_id`: text, required, unit identifier; `criterion`: text, required, unit text; `rule`: text, required, unit text; `materiality_class`: text, required, unit text, allowed MATERIAL, ASSESSABILITY, NONMATERIAL; `boundary`: text, required, unit text; `evidence_ids`: text, required, unit evidence identifiers.

### DefectRegister

**Grain:** One defect-condition per case/criterion; multiple defects could affect one case. **Primary key:** `defect_id`. **Report placement:** section 5.

```text
defect_id | case_id | criterion_id | severity | materiality | condition | evidence_ids
```

**Populate from:** Packet facts, applicable criteria and adjudicated demonstrated errors. **Required procedure:** Keep seven defects across seven cases; six are material and one nonmaterial. Do not insert C08/C12 as demonstrated defects solely because they are unassessable.

**Interpretation:** Case-level material rates count unique affected cases, while remediation counts defect rows. Severity does not substitute for materiality.

**Change and exception handling:** A second defect on an existing case changes defect count but may leave affected-case count unchanged. Trace each defect to its own closure test.

**Declared joins:** `case_id` → `CasePackets.case_id`; `criterion_id` → `QualityCriteria.criterion_id`. Every supplied child key must resolve before release.

**Field-level validation:** `defect_id`: text, required, unit identifier; `case_id`: text, required, unit identifier; `criterion_id`: text, required, unit identifier; `severity`: text, required, unit text, allowed HIGH, MEDIUM, LOW; `materiality`: text, required, unit text, allowed MATERIAL, NONMATERIAL; `condition`: text, required, unit text; `evidence_ids`: text, required, unit evidence identifiers.

### Calibration

**Grain:** One paired case assessment; preserve original votes and later consensus. **Primary key:** `case_id`. **Report placement:** section 5.

```text
case_id | r1_vote | r2_vote | agreement | consensus | adjudication_reason | evidence_ids
```

**Populate from:** Original paired votes and Q14 later consensus. **Required procedure:** Keep twelve paired rows, original agreement flags and adjudication rationale. Consensus cannot replace the original vote history.

**Interpretation:** Nine original pairs agree; C02/C06/C11 disagree. The reasoned consensus preserves unknowns where evidence is absent.

**Change and exception handling:** New evidence creates a new consensus version or round; it does not improve historical original agreement retrospectively.

**Declared joins:** `case_id` → `CasePackets.case_id`. Every supplied child key must resolve before release.

**Field-level validation:** `case_id`: text, required, unit identifier; `r 1_vote`: text, required, unit text, allowed ACCEPT, REWORK, INSUFFICIENT; `r 2_vote`: text, required, unit text, allowed ACCEPT, REWORK, INSUFFICIENT; `agreement`: boolean, required, unit flag; `consensus`: text, required, unit text, allowed ACCEPT, REWORK, INSUFFICIENT; `adjudication_reason`: text, required, unit text; `evidence_ids`: text, required, unit evidence identifiers.

### Remediation

**Grain:** One proposed repair per demonstrated defect; no repair is executed in the fixture. **Primary key:** `remediation_id`. **Report placement:** section 5.

```text
remediation_id | defect_id | repair | closure_test | status | evidence_ids
```

**Populate from:** Seven demonstrated defects and Q16 proposed repairs. **Required procedure:** Create one targeted repair and closure test per defect. The fixture status is PROPOSED for every row.

**Interpretation:** A corrected field must be checked in all affected outputs and any conclusion relying on it. Optional editorial correction remains separate from substantive rework.

**Change and exception handling:** Executed repair, retest and authorized closure need distinct evidence. An owner statement alone is not a verified closure artifact.

**Declared joins:** `defect_id` → `DefectRegister.defect_id`. Every supplied child key must resolve before release.

**Field-level validation:** `remediation_id`: text, required, unit identifier; `defect_id`: text, required, unit identifier; `repair`: text, required, unit text; `closure_test`: text, required, unit text; `status`: text, required, unit text, allowed PROPOSED; `evidence_ids`: text, required, unit evidence identifiers.

### DecisionRecord

**Grain:** One decision boundary separating quality judgment, population inference and business action. **Primary key:** `decision_id`. **Report placement:** section 5.

```text
decision_id | question | status | basis | evidence_ids
```

**Populate from:** Consensus, selection design and actual closure/filing authority. **Required procedure:** Record four decision boundaries: calibration result, unavailable population inference, unrecorded underlying business disposition and unrecorded repair closure.

**Interpretation:** Quality consensus cannot determine suspicious activity or filing obligations. Deliberate selection cannot justify population extrapolation.

**Change and exception handling:** An actual later human decision can populate the relevant gate, but cannot be inferred from good agreement or a complete workbook.

**Field-level validation:** `decision_id`: text, required, unit identifier; `question`: text, required, unit text; `status`: text, required, unit text, allowed RECORDED, INSUFFICIENT, NOT_RECORDED; `basis`: text, required, unit text; `evidence_ids`: text, required, unit evidence identifiers.

### ProcessQA

**Grain:** One reperformable quality metric or authorization check. **Primary key:** `check_id`. **Report placement:** section 5.

```text
check_id | check | expected | actual | result | evidence_ids
```

**Populate from:** Original vote arithmetic, consensus counts, defect grain and missingness. **Required procedure:** Record ten checks, including 9/12 agreement,52/144 expected agreement and 14/23 kappa. Preserve two unassessable packets in denominator explanations.

**Interpretation:** Six material cases are 50.0% of 12 selected and 60.0% of 10 assessable; neither is a population estimate.

**Change and exception handling:** Changing consensus requires recomputing rates, but original agreement stays unchanged unless original votes were actually corrected with documented provenance.

**Field-level validation:** `check_id`: text, required, unit identifier; `check`: text, required, unit text; `expected`: text, required, unit text; `actual`: text, required, unit text; `result`: text, required, unit text, allowed PASS, NOT RECORDED; `evidence_ids`: text, required, unit evidence identifiers.

## Completed narrative pattern and adaptation test

Use the eight populated narrative sections in file 10 as a demonstration of the required specificity. For each paragraph, identify the source rows, calculation or decision rule that support it. When adapting, remove the fictional proposition before writing a new one; changing a title or date is not enough. A reviewer should be able to take any quantified sentence and recover its numerator, denominator, unit and scope without asking the assistant what it meant.

All domain records belong in the report or its complete tabular annex as well as the workbook and dashboard. Keep the exact identifiers in every representation. If a table becomes long, split it into labeled contiguous ranges, not selected examples. Preserve the common Evidence register and every semicolon-delimited evidence reference. The completed output remains draft until the applicable quality gates and actual human decision status are accurately recorded.

<!-- FIELD_CONTRACTS:START -->
## Compiled domain field dictionary

This dictionary is part of this attachment. It fixes the type, null rule, unit, permitted values and record identity used by the embedded renderers. It is generated from the same reviewed case contract; no external file is needed. Raw source defects must be retained as raw text under their declared type. Correcting a malformed value requires evidence, not coercion by the renderer.

### CasePackets — field contract

**Record grain:** One completed case packet selected for calibration, not a random population sample.

**Primary key:** `case_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| case_id | text | no | identifier | Unique case packet in this deliberately selected calibration set. | No additional enum or range constraint | Native value / literal text |
| case_topic | text | no | text | Short topic, not an allegation. | No additional enum or range constraint | Native value / literal text |
| raw_packet | text | no | text | Complete bounded fictional facts supplied for this quality question. | No additional enum or range constraint | Native value / literal text |
| consensus | text | no | text | Adjudicated quality status under fixture policy. | ACCEPT / REWORK / INSUFFICIENT | Native value / literal text |
| rationale | text | no | text | Case-specific quality reasoning, distinct from underlying case disposition. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ReviewVotes — field contract

**Record grain:** One original blind case-reviewer assessment;24 votes over12 cases.

**Primary key:** `vote_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| vote_id | text | no | identifier | Unique case-reviewer vote; retain before adjudication. | No additional enum or range constraint | Native value / literal text |
| case_id | text | no | identifier | Case packet being evaluated. | No additional enum or range constraint | Native value / literal text |
| reviewer_id | text | no | identifier | Fictional R1 or R2; not a real reviewer identity. | No additional enum or range constraint | Native value / literal text |
| vote | text | no | text | Original independent quality vote. | ACCEPT / REWORK / INSUFFICIENT | Native value / literal text |
| round | integer | no | count | Blind round number; fixture is round1. | No additional enum or range constraint | #,##0 |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Foreign key: `case_id` resolves to `CasePackets (case_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### QualityCriteria — field contract

**Record grain:** One supplied illustrative quality criterion; no implied universal legal mandate.

**Primary key:** `criterion_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| criterion_id | text | no | identifier | Stable fixture policy criterion. | No additional enum or range constraint | Native value / literal text |
| criterion | text | no | text | Quality dimension being assessed. | No additional enum or range constraint | Native value / literal text |
| rule | text | no | text | Exact authored requirement for this exercise. | No additional enum or range constraint | Native value / literal text |
| materiality_class | text | no | text | Potential consequence class. | MATERIAL / ASSESSABILITY / NONMATERIAL | Native value / literal text |
| boundary | text | no | text | Constraint preventing overstatement. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### DefectRegister — field contract

**Record grain:** One defect-condition per case/criterion; multiple defects could affect one case.

**Primary key:** `defect_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| defect_id | text | no | identifier | Unique demonstrated quality defect; not every unknown becomes a defect. | No additional enum or range constraint | Native value / literal text |
| case_id | text | no | identifier | Affected case packet. | No additional enum or range constraint | Native value / literal text |
| criterion_id | text | no | identifier | Applicable supplied criterion. | No additional enum or range constraint | Native value / literal text |
| severity | text | no | text | Illustrative severity based on consequence. | HIGH / MEDIUM / LOW | Native value / literal text |
| materiality | text | no | text | Whether error can affect the substantive case reasoning. | MATERIAL / NONMATERIAL | Native value / literal text |
| condition | text | no | text | Specific factual or reasoning defect. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Foreign key: `case_id` resolves to `CasePackets (case_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Foreign key: `criterion_id` resolves to `QualityCriteria (criterion_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### Calibration — field contract

**Record grain:** One paired case assessment; preserve original votes and later consensus.

**Primary key:** `case_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| case_id | text | no | identifier | Case identifier; one consensus review per case. | No additional enum or range constraint | Native value / literal text |
| r1_vote | text | no | text | Original reviewer1 vote. | ACCEPT / REWORK / INSUFFICIENT | Native value / literal text |
| r2_vote | text | no | text | Original reviewer2 vote. | ACCEPT / REWORK / INSUFFICIENT | Native value / literal text |
| agreement | boolean | no | flag | True only if original votes match exactly. | No additional enum or range constraint | Native value / literal text |
| consensus | text | no | text | Adjudicated outcome after comparing criteria/evidence. | ACCEPT / REWORK / INSUFFICIENT | Native value / literal text |
| adjudication_reason | text | no | text | Why consensus follows evidence; not majority-rule substitution. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Foreign key: `case_id` resolves to `CasePackets (case_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### Remediation — field contract

**Record grain:** One proposed repair per demonstrated defect; no repair is executed in the fixture.

**Primary key:** `remediation_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| remediation_id | text | no | identifier | Stable proposed repair identifier. | No additional enum or range constraint | Native value / literal text |
| defect_id | text | no | identifier | Demonstrated defect being addressed. | No additional enum or range constraint | Native value / literal text |
| repair | text | no | text | Specific proposed correction. | No additional enum or range constraint | Native value / literal text |
| closure_test | text | no | text | Evidence an independent reviewer would reperform. | No additional enum or range constraint | Native value / literal text |
| status | text | no | text | Fixture has proposals only. | PROPOSED | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Foreign key: `defect_id` resolves to `DefectRegister (defect_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### DecisionRecord — field contract

**Record grain:** One decision boundary separating quality judgment, population inference and business action.

**Primary key:** `decision_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| decision_id | text | no | identifier | Stable quality decision gate. | No additional enum or range constraint | Native value / literal text |
| question | text | no | text | Decision scope. | No additional enum or range constraint | Native value / literal text |
| status | text | no | text | Result under fixture evidence. | RECORDED / INSUFFICIENT / NOT_RECORDED | Native value / literal text |
| basis | text | no | text | Exact result and denominator meaning. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ProcessQA — field contract

**Record grain:** One reperformable quality metric or authorization check.

**Primary key:** `check_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| check_id | text | no | identifier | Stable fixture check. | No additional enum or range constraint | Native value / literal text |
| check | text | no | text | Reperformable calculation or boundary. | No additional enum or range constraint | Native value / literal text |
| expected | text | no | text | Exact independent target. | No additional enum or range constraint | Native value / literal text |
| actual | text | no | text | Calculated fixture result. | No additional enum or range constraint | Native value / literal text |
| result | text | no | text | Analytical result. | PASS / NOT RECORDED | Native value / literal text |
| evidence_ids | text | no | evidence identifiers | Semicolon-delimited exact identifiers in the common Evidence register; each must resolve. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.
<!-- FIELD_CONTRACTS:END -->
