# Fully populated worked example — Monitoring System Independent Challenge and Validation

**Fictional records only.** The inputs below are deliberately constructed to demonstrate the full method, adverse branches and incomplete decision gates. They are not customer data, a real validation or evidence of an institution's control quality. All parameters are illustrative. The supplied cutoff is Oct 09, 2026.

This suite reviews whether a supplied monitoring component performs the stated function, whether evidence supports its use, and which limitations restrict an opinion. It is independent challenge in an analytical sense: the reviewer forms a reference expectation that can contradict the developer. It does not declare a legally sufficient independent function, validate a real institution, or classify every transaction-monitoring system as a model. Objectivity, qualifications, involvement, escalation standing and organizational arrangements require actual evidence.

The worked case has 24 feature-level units and 24 predeclared tests. A fixed reference rule requires amount>=10000 USD, at least three eligible credits and at least two distinct originators; absent amount produces an unknown result. The supplied implementation incorrectly uses amount>10000 and silently converts absent amount tofalse. A separate challenger removes the originator restriction solely to probe conceptual sensitivity. These deliberately distinct mechanisms support implementation findings, concept limitations and evidence gaps without conflating them.

## Independent source declarations

The independent raw feature table supplies one customer-window per row. The reference R1 tests amount>=10000 USD AND eligible_count>=3 AND originators>=2, returning unknown when amount is absent. Implemented I1 tests amount>10000 with the same count criteria and returns false when amount is absent. Diagnostic C1 retains inclusive amount and event count but drops the originator condition. The matrix labels are supplied fictional outcomes, independent of the rules.

| unit_id | segment | amount_usd | eligible_count | originators | label |
| --- | --- | --- | --- | --- | --- |
| V01 | RETAIL | 9999 | 3 | 2 | NEGATIVE |
| V02 | RETAIL | 10000 | 3 | 2 | POSITIVE |
| V03 | RETAIL | 12000 | 4 | 3 | POSITIVE |
| V04 | RETAIL | 14000 | 2 | 2 | NEGATIVE |
| V05 | RETAIL | 18000 | 5 | 1 | POSITIVE |
| V06 | RETAIL | null | 4 | 3 | UNKNOWN |
| V07 | BUSINESS | 9999 | 3 | 2 | NEGATIVE |
| V08 | BUSINESS | 10000 | 3 | 2 | POSITIVE |
| V09 | BUSINESS | 12000 | 4 | 3 | POSITIVE |
| V10 | BUSINESS | 14000 | 2 | 2 | NEGATIVE |
| V11 | BUSINESS | 18000 | 5 | 1 | POSITIVE |
| V12 | BUSINESS | null | 4 | 3 | UNKNOWN |
| V13 | CORRESPONDENT | 9999 | 3 | 2 | NEGATIVE |
| V14 | CORRESPONDENT | 10000 | 3 | 2 | POSITIVE |
| V15 | CORRESPONDENT | 12000 | 4 | 3 | POSITIVE |
| V16 | CORRESPONDENT | 14000 | 2 | 2 | NEGATIVE |
| V17 | CORRESPONDENT | 18000 | 5 | 1 | POSITIVE |
| V18 | CORRESPONDENT | null | 4 | 3 | UNKNOWN |
| V19 | DIGITAL_SERVICE | 9999 | 3 | 2 | NEGATIVE |
| V20 | DIGITAL_SERVICE | 10000 | 3 | 2 | POSITIVE |
| V21 | DIGITAL_SERVICE | 12000 | 4 | 3 | POSITIVE |
| V22 | DIGITAL_SERVICE | 14000 | 2 | 2 | NEGATIVE |
| V23 | DIGITAL_SERVICE | 18000 | 5 | 1 | POSITIVE |
| V24 | DIGITAL_SERVICE | null | 4 | 3 | UNKNOWN |

## Complete populated output registers

### ComponentInventory

| component_id | name | classification | input_grain | output | theory_basis | limitation | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CMP-01 | Feature construction | DETERMINISTIC_TRANSFORM | Transactions grouped into fixed customer-window | amount_usd;eligible_count;originators | Arithmetic aggregation; raw transaction replay not supplied | Feature values are supplied rather than independently validated | SYN-101 |
| CMP-02 | Reference scenario R1 | DETERMINISTIC_RULE | One customer-window | TRUE;FALSE;UNKNOWN | Fixed inclusive predicates with no fitted statistical component | Multi-originator concept misses single-originator activity | SYN-102 |
| CMP-03 | Implementation I1 | DETERMINISTIC_RULE | One customer-window | TRUE;FALSE | Strict amount comparison and missing-to-zero default | Implementation differs from R1 at boundary and nulls | SYN-102 |
| CMP-04 | Challenger C1 | DETERMINISTIC_RULE | One customer-window | TRUE;FALSE;UNKNOWN | Fixed broader rule removes originator count condition | Diagnostic sensitivity comparison; not a deployment candidate | SYN-102 |
| CMP-05 | Human change disposition | HUMAN_PROCESS | Validation report and unresolved issues | Approve;restrict;reject;request evidence | Not a quantitative model; authority depends on supplied governance | No actual decision or reviewer credentials supplied | SYN-103 |

### ChallengeTests

| test_id | domain | test_name | procedure | expected | actual | result | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C01 | CONCEPT | Objective alignment | Compare the stated purpose with the exact predicate | Identify repeated multi-originator credits in one fixed window | Objective and inclusive amount predicate supplied | PASS | SYN-102 |
| C02 | CONCEPT | Alternative mechanisms | Challenge the two-originator assumption | Document single-originator limitations | V05 V11 V17 V23 are known positives outside that concept | FAIL | SYN-101;SYN-102 |
| C03 | CONCEPT | Rule/model classification | Inspect mathematical design and stated use | Record deterministic rule classification without exempting controls | No fitted parameter or probabilistic estimate; deterministic fixture | PASS | SYN-102 |
| C04 | CONCEPT | Segment transfer | Challenge purpose and coverage separately by segment | Evidence of each segment rationale required | Equal mechanics supplied; no real segment rationale | BLOCKED | SYN-102 |
| D01 | DATA | Population counts | Reconcile independent input manifest | 24 complete unit identifiers across four segments | 24 IDs; six per segment | PASS | SYN-101 |
| D02 | DATA | Amount completeness | Count absent amount inputs without substituting zero | 24 amounts required for full calculability | Four missing amounts: V06 V12 V18 V24 | FAIL | SYN-101 |
| D03 | DATA | Transaction lineage | Request source transaction-to-feature replay | Trace every amount count and originator value | Fixture supplies feature-level records only | BLOCKED | SYN-101 |
| D04 | DATA | Outcome provenance | Review label derivation and maturity | Independent mature labels supporting generalization | Twenty synthetic labels and four unknowns only | BLOCKED | SYN-101 |
| I01 | IMPLEMENTATION | Amount boundary | Compare 9999 10000 and 12000 against inclusive specification | 10000 qualifies when other conditions hold | Implemented strict greater-than loses four boundary positives | FAIL | SYN-101;SYN-102 |
| I02 | IMPLEMENTATION | Count boundary | Reperform the minimum of three eligible events | Count two is below threshold; count three can qualify | V04 V10 V16 V22 rejected consistently | PASS | SYN-101;SYN-102 |
| I03 | IMPLEMENTATION | Originator boundary | Reperform the minimum of two originators | One originator excluded under the frozen concept | V05 V11 V17 V23 excluded consistently | PASS | SYN-101;SYN-102 |
| I04 | IMPLEMENTATION | Missing value behavior | Compare reference unknown with engine default | Missing amount produces unassessable state | Four missing amounts converted to false | FAIL | SYN-101;SYN-102 |
| O01 | OUTCOMES | Reference matrix | Count known labels with the reference predicate | TP8 FP0 FN4 TN8 on twenty known labels | TP8 FP0 FN4 TN8 | PASS | SYN-101;SYN-102 |
| O02 | OUTCOMES | Implemented matrix | Count known labels with implemented predicate | TP4 FP0 FN8 TN8 on twenty known labels | TP4 FP0 FN8 TN8 | PASS | SYN-101;SYN-102 |
| O03 | OUTCOMES | Challenger behavior | Remove originator restriction with all other conditions held | Expose sensitivity to the excluded mechanism | TP12 FP0 FN0 TN8 on the synthetic known subset | PASS | SYN-101;SYN-102 |
| O04 | OUTCOMES | Generalization | Check independent outcome design and test selection | Representative operational evidence required | Constructed examples cannot support effectiveness inference | BLOCKED | SYN-101 |
| G01 | GOVERNANCE | Version lineage | Compare supplied specification and implementation descriptions | Both versions distinguish inclusive and strict comparison | Spec R1 versus implementation I1 recorded | PASS | SYN-102 |
| G02 | GOVERNANCE | Change authorization | Inspect human change decision and permitted scope | Accountable approver and authorization evidence | No operational authorization supplied | BLOCKED | SYN-103 |
| G03 | GOVERNANCE | Validator objectivity | Review involvement expertise conflict and escalation | Named review role with evidence of sufficient objectivity | Fictional role only; no actual reviewer credentials | BLOCKED | SYN-103 |
| G04 | GOVERNANCE | Issue ownership | Trace defects to proposed actions and evidence requirements | Each material defect has a human decision route | Four proposed issue records populated | PASS | SYN-103 |
| M01 | MONITORING | Missingness indicator | Calculate missing amount count and denominator | 4/24 = 16.7% absent | 4/24 = 16.7% | PASS | SYN-101 |
| M02 | MONITORING | Boundary mismatch indicator | Identify present-input implementation differences | 4/20 = 20.0% among present amounts | V02 V08 V14 V20; 4/20 | PASS | SYN-101;SYN-102 |
| M03 | MONITORING | Drift baseline | Inspect the reference period and comparison frame | Comparable independent periods required | Single constructed feature set only | BLOCKED | SYN-101 |
| M04 | MONITORING | Remediation retest | Require corrected replay plus unchanged-case checks | New implementation and all twenty-four outcomes | No corrected implementation supplied | BLOCKED | SYN-103 |

### OutcomeUnits

| unit_id | segment | amount_usd | eligible_count | originators | label | reference_hit | implemented_hit | challenger_hit | mismatch | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | RETAIL | 9999 | 3 | 2 | NEGATIVE | false | false | false | false | SYN-101;SYN-102 |
| V02 | RETAIL | 10000 | 3 | 2 | POSITIVE | true | false | true | true | SYN-101;SYN-102 |
| V03 | RETAIL | 12000 | 4 | 3 | POSITIVE | true | true | true | false | SYN-101;SYN-102 |
| V04 | RETAIL | 14000 | 2 | 2 | NEGATIVE | false | false | false | false | SYN-101;SYN-102 |
| V05 | RETAIL | 18000 | 5 | 1 | POSITIVE | false | false | true | false | SYN-101;SYN-102 |
| V06 | RETAIL | null | 4 | 3 | UNKNOWN | null | false | null | true | SYN-101;SYN-102 |
| V07 | BUSINESS | 9999 | 3 | 2 | NEGATIVE | false | false | false | false | SYN-101;SYN-102 |
| V08 | BUSINESS | 10000 | 3 | 2 | POSITIVE | true | false | true | true | SYN-101;SYN-102 |
| V09 | BUSINESS | 12000 | 4 | 3 | POSITIVE | true | true | true | false | SYN-101;SYN-102 |
| V10 | BUSINESS | 14000 | 2 | 2 | NEGATIVE | false | false | false | false | SYN-101;SYN-102 |
| V11 | BUSINESS | 18000 | 5 | 1 | POSITIVE | false | false | true | false | SYN-101;SYN-102 |
| V12 | BUSINESS | null | 4 | 3 | UNKNOWN | null | false | null | true | SYN-101;SYN-102 |
| V13 | CORRESPONDENT | 9999 | 3 | 2 | NEGATIVE | false | false | false | false | SYN-101;SYN-102 |
| V14 | CORRESPONDENT | 10000 | 3 | 2 | POSITIVE | true | false | true | true | SYN-101;SYN-102 |
| V15 | CORRESPONDENT | 12000 | 4 | 3 | POSITIVE | true | true | true | false | SYN-101;SYN-102 |
| V16 | CORRESPONDENT | 14000 | 2 | 2 | NEGATIVE | false | false | false | false | SYN-101;SYN-102 |
| V17 | CORRESPONDENT | 18000 | 5 | 1 | POSITIVE | false | false | true | false | SYN-101;SYN-102 |
| V18 | CORRESPONDENT | null | 4 | 3 | UNKNOWN | null | false | null | true | SYN-101;SYN-102 |
| V19 | DIGITAL_SERVICE | 9999 | 3 | 2 | NEGATIVE | false | false | false | false | SYN-101;SYN-102 |
| V20 | DIGITAL_SERVICE | 10000 | 3 | 2 | POSITIVE | true | false | true | true | SYN-101;SYN-102 |
| V21 | DIGITAL_SERVICE | 12000 | 4 | 3 | POSITIVE | true | true | true | false | SYN-101;SYN-102 |
| V22 | DIGITAL_SERVICE | 14000 | 2 | 2 | NEGATIVE | false | false | false | false | SYN-101;SYN-102 |
| V23 | DIGITAL_SERVICE | 18000 | 5 | 1 | POSITIVE | false | false | true | false | SYN-101;SYN-102 |
| V24 | DIGITAL_SERVICE | null | 4 | 3 | UNKNOWN | null | false | null | true | SYN-101;SYN-102 |

### OutcomeMetrics

| variant | population_n | known_n | unknown_n | tp | fp | fn | tn | all_hits | unassessable_n | precision | recall | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REFERENCE | 24 | 20 | 4 | 8 | 0 | 4 | 8 | 8 | 4 | 1.0 | 0.6666666666666666 | SYN-101;SYN-102 |
| IMPLEMENTED | 24 | 20 | 4 | 4 | 0 | 8 | 8 | 4 | 0 | 1.0 | 0.3333333333333333 | SYN-101;SYN-102 |
| CHALLENGER | 24 | 20 | 4 | 12 | 0 | 0 | 8 | 12 | 4 | 1.0 | 1.0 | SYN-101;SYN-102 |

### IssueRegister

| issue_id | linked_tests | severity | affected_ids | issue | closure_evidence | state | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MV-I01 | I01;M02 | HIGH | V02;V08;V14;V20 | Strict amount comparison loses inclusive-boundary hits | Corrected version replay of all 24 units plus boundary neighbors | OPEN | SYN-101;SYN-102 |
| MV-I02 | D02;I04 | HIGH | V06;V12;V18;V24 | Absent amounts silently become negative outputs | Explicit unknown route, data recovery and no zero substitution | OPEN | SYN-101;SYN-102 |
| MV-I03 | C02;D03;D04;O04 | HIGH | CMP-01;CMP-02 | Coverage concept and evidence cannot support generalization | Transaction lineage, independent representative outcomes and concept challenge | BLOCKED | SYN-101;SYN-102 |
| MV-I04 | G02;G03;M03;M04 | MEDIUM | CMP-05 | Authorization objectivity and corrected retest not evidenced | Actual reviewer qualifications, conflict assessment, approvals and corrected retest | BLOCKED | SYN-103 |

### EvidenceProvenance

| source_id | source_kind | as_of | availability | unit_count | grain | limitation | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SYN-101 | SYNTHETIC_INPUT | 2026-10-09 | COMPLETE_FIXTURE | 24 | supplied feature-level units | Feature-level completeness does not establish transaction lineage. | SYN-101 |
| SYN-102 | SYNTHETIC_INPUT | 2026-10-09 | COMPLETE_FIXTURE | 3 | predicate definitions | R1 I1 and C1 are fictional rules, not live deployed components. | SYN-102 |
| SYN-103 | SYNTHETIC_DECISION | 2026-10-09 | PARTIAL_FIXTURE | 4 | proposed issue records | Actual change approval and reviewer credentials are absent. | SYN-103 |

### ProcessQA

| check_id | check_scope | expected | actual | status | reviewer | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| MV-Q01 | Feature manifest | 24 unique units and four segments of 6 | 24 unique;6 per segment | PASS | Fictional checker | SYN-101 |
| MV-Q02 | Present and absent amounts | 24=20 present+4 absent | 20 present and 4 null | PASS | Fictional checker | SYN-101 |
| MV-Q03 | Reference result | 8 true;12 false;4 unknown | 8 true;12 false;4 unknown | PASS | Fictional checker | SYN-101;SYN-102 |
| MV-Q04 | Implemented result | Specification-equivalent tri-state result | 4 true;20 false;0 unknown | FAIL | Fictional checker | SYN-101;SYN-102 |
| MV-Q05 | Mismatches | Four boundary and four null-state differences | 8 mismatches; mutually exclusive classes | PASS | Fictional checker | SYN-101;SYN-102 |
| MV-Q06 | Generalization gate | Independent operational data required | Synthetic designed examples only | REVIEW_REQUIRED | NOT_RECORDED | SYN-101 |
| MV-Q07 | Human decision | Actual authorized decision required | NOT_RECORDED | NOT_TESTED | NOT_RECORDED | SYN-103 |

### ReleaseGates

| gate_id | requirement | current_evidence | gate_state | dependency | permitted_claim | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| MV-G01 | Reference predicate reproducible | R1 independent replay agrees on 24 units | SATISFIED_FIXTURE_ONLY | SYN-101;SYN-102 | Fixture arithmetic is reproducible | SYN-101;SYN-102 |
| MV-G02 | Implementation equivalence | Eight mismatches including four known-positive boundary losses | FAILED | MV-I01;MV-I02 | Implementation is not equivalent to the supplied specification | SYN-101;SYN-102 |
| MV-G03 | Complete input lineage | Raw transaction detail is outside the supplied fixture | BLOCKED | MV-I03 | Feature-level calculations only | SYN-101 |
| MV-G04 | Representative outcomes | Twenty constructed known labels and four unknowns | BLOCKED | MV-I03 | Synthetic comparisons only; no live effectiveness estimate | SYN-101 |
| MV-G05 | Qualified objective review | Fictional review role; no actual conflict or qualification record | BLOCKED | MV-I04 | Method supports challenge; institutional independence unverified | SYN-103 |
| MV-G06 | Authorized release disposition | No human approval or corrected replay supplied | BLOCKED | MV-I01;MV-I02;MV-I03;MV-I04 | Do not support release on this evidence | SYN-103 |

## Complete record-by-record analytical trace

Every unit below names its exact supplied features, three outputs and the applicable interpretation. The complete source table and registered outputs above remain authoritative. UNKNOWN is a missing predicate outcome; it is not converted to FALSE.

### V01: RETAIL

V01 has amount **9,999.00 USD**, eligible count **3**, originators **2** and label **NEGATIVE**. R1 is **FALSE**, I1 is **FALSE**, and C1 is **FALSE**; the mismatch flag is **false**. V01 is a valid lower-boundary negative. Its amount is below 10000 despite sufficient event and originator counts. Do not round it up or broaden the rule while fixing equality. Sources: SYN-101;SYN-102.

### V02: RETAIL

V02 has amount **10,000.00 USD**, eligible count **3**, originators **2** and label **POSITIVE**. R1 is **TRUE**, I1 is **FALSE**, and C1 is **TRUE**; the mismatch flag is **true**. V02 is one of the four known positive equality-boundary losses. Both count conditions hold. The strict amount comparison in I1 alone defeats the inclusive reference result; a correction must restore this exact ID. Sources: SYN-101;SYN-102.

### V03: RETAIL

V03 has amount **12,000.00 USD**, eligible count **4**, originators **3** and label **POSITIVE**. R1 is **TRUE**, I1 is **TRUE**, and C1 is **TRUE**; the mismatch flag is **false**. V03 is an above-boundary known positive correctly captured by all variants. Its true output must survive a proposed correction; agreement here does not dispose of the separate equality and null failures. Sources: SYN-101;SYN-102.

### V04: RETAIL

V04 has amount **14,000.00 USD**, eligible count **2**, originators **2** and label **NEGATIVE**. R1 is **FALSE**, I1 is **FALSE**, and C1 is **FALSE**; the mismatch flag is **false**. V04 is a valid reference negative because two events are below the required three. The amount does not override that condition. Preserve this false output during a proposed correction. Sources: SYN-101;SYN-102.

### V05: RETAIL

V05 has amount **18,000.00 USD**, eligible count **5**, originators **1** and label **POSITIVE**. R1 is **FALSE**, I1 is **FALSE**, and C1 is **TRUE**; the mismatch flag is **false**. V05 demonstrates the single-originator concept limitation. R1 and I1 agree on exclusion, while C1 includes it. Keep implementation fidelity separate from the known positive that this narrower concept misses. Sources: SYN-101;SYN-102.

### V06: RETAIL

V06 has amount **null**, eligible count **4**, originators **3** and label **UNKNOWN**. R1 is **UNKNOWN**, I1 is **FALSE**, and C1 is **UNKNOWN**; the mismatch flag is **true**. V06 is one of the four null-handling differences. Its label is UNKNOWN, so the difference is not a known positive loss; retain it in the missing-input route and outside the known-label matrices. Sources: SYN-101;SYN-102.

### V07: BUSINESS

V07 has amount **9,999.00 USD**, eligible count **3**, originators **2** and label **NEGATIVE**. R1 is **FALSE**, I1 is **FALSE**, and C1 is **FALSE**; the mismatch flag is **false**. V07 is a valid lower-boundary negative. Its amount is below 10000 despite sufficient event and originator counts. Do not round it up or broaden the rule while fixing equality. Sources: SYN-101;SYN-102.

### V08: BUSINESS

V08 has amount **10,000.00 USD**, eligible count **3**, originators **2** and label **POSITIVE**. R1 is **TRUE**, I1 is **FALSE**, and C1 is **TRUE**; the mismatch flag is **true**. V08 is one of the four known positive equality-boundary losses. Both count conditions hold. The strict amount comparison in I1 alone defeats the inclusive reference result; a correction must restore this exact ID. Sources: SYN-101;SYN-102.

### V09: BUSINESS

V09 has amount **12,000.00 USD**, eligible count **4**, originators **3** and label **POSITIVE**. R1 is **TRUE**, I1 is **TRUE**, and C1 is **TRUE**; the mismatch flag is **false**. V09 is an above-boundary known positive correctly captured by all variants. Its true output must survive a proposed correction; agreement here does not dispose of the separate equality and null failures. Sources: SYN-101;SYN-102.

### V10: BUSINESS

V10 has amount **14,000.00 USD**, eligible count **2**, originators **2** and label **NEGATIVE**. R1 is **FALSE**, I1 is **FALSE**, and C1 is **FALSE**; the mismatch flag is **false**. V10 is a valid reference negative because two events are below the required three. The amount does not override that condition. Preserve this false output during a proposed correction. Sources: SYN-101;SYN-102.

### V11: BUSINESS

V11 has amount **18,000.00 USD**, eligible count **5**, originators **1** and label **POSITIVE**. R1 is **FALSE**, I1 is **FALSE**, and C1 is **TRUE**; the mismatch flag is **false**. V11 demonstrates the single-originator concept limitation. R1 and I1 agree on exclusion, while C1 includes it. Keep implementation fidelity separate from the known positive that this narrower concept misses. Sources: SYN-101;SYN-102.

### V12: BUSINESS

V12 has amount **null**, eligible count **4**, originators **3** and label **UNKNOWN**. R1 is **UNKNOWN**, I1 is **FALSE**, and C1 is **UNKNOWN**; the mismatch flag is **true**. V12 is one of the four null-handling differences. Its label is UNKNOWN, so the difference is not a known positive loss; retain it in the missing-input route and outside the known-label matrices. Sources: SYN-101;SYN-102.

### V13: CORRESPONDENT

V13 has amount **9,999.00 USD**, eligible count **3**, originators **2** and label **NEGATIVE**. R1 is **FALSE**, I1 is **FALSE**, and C1 is **FALSE**; the mismatch flag is **false**. V13 is a valid lower-boundary negative. Its amount is below 10000 despite sufficient event and originator counts. Do not round it up or broaden the rule while fixing equality. Sources: SYN-101;SYN-102.

### V14: CORRESPONDENT

V14 has amount **10,000.00 USD**, eligible count **3**, originators **2** and label **POSITIVE**. R1 is **TRUE**, I1 is **FALSE**, and C1 is **TRUE**; the mismatch flag is **true**. V14 is one of the four known positive equality-boundary losses. Both count conditions hold. The strict amount comparison in I1 alone defeats the inclusive reference result; a correction must restore this exact ID. Sources: SYN-101;SYN-102.

### V15: CORRESPONDENT

V15 has amount **12,000.00 USD**, eligible count **4**, originators **3** and label **POSITIVE**. R1 is **TRUE**, I1 is **TRUE**, and C1 is **TRUE**; the mismatch flag is **false**. V15 is an above-boundary known positive correctly captured by all variants. Its true output must survive a proposed correction; agreement here does not dispose of the separate equality and null failures. Sources: SYN-101;SYN-102.

### V16: CORRESPONDENT

V16 has amount **14,000.00 USD**, eligible count **2**, originators **2** and label **NEGATIVE**. R1 is **FALSE**, I1 is **FALSE**, and C1 is **FALSE**; the mismatch flag is **false**. V16 is a valid reference negative because two events are below the required three. The amount does not override that condition. Preserve this false output during a proposed correction. Sources: SYN-101;SYN-102.

### V17: CORRESPONDENT

V17 has amount **18,000.00 USD**, eligible count **5**, originators **1** and label **POSITIVE**. R1 is **FALSE**, I1 is **FALSE**, and C1 is **TRUE**; the mismatch flag is **false**. V17 demonstrates the single-originator concept limitation. R1 and I1 agree on exclusion, while C1 includes it. Keep implementation fidelity separate from the known positive that this narrower concept misses. Sources: SYN-101;SYN-102.

### V18: CORRESPONDENT

V18 has amount **null**, eligible count **4**, originators **3** and label **UNKNOWN**. R1 is **UNKNOWN**, I1 is **FALSE**, and C1 is **UNKNOWN**; the mismatch flag is **true**. V18 is one of the four null-handling differences. Its label is UNKNOWN, so the difference is not a known positive loss; retain it in the missing-input route and outside the known-label matrices. Sources: SYN-101;SYN-102.

### V19: DIGITAL_SERVICE

V19 has amount **9,999.00 USD**, eligible count **3**, originators **2** and label **NEGATIVE**. R1 is **FALSE**, I1 is **FALSE**, and C1 is **FALSE**; the mismatch flag is **false**. V19 is a valid lower-boundary negative. Its amount is below 10000 despite sufficient event and originator counts. Do not round it up or broaden the rule while fixing equality. Sources: SYN-101;SYN-102.

### V20: DIGITAL_SERVICE

V20 has amount **10,000.00 USD**, eligible count **3**, originators **2** and label **POSITIVE**. R1 is **TRUE**, I1 is **FALSE**, and C1 is **TRUE**; the mismatch flag is **true**. V20 is one of the four known positive equality-boundary losses. Both count conditions hold. The strict amount comparison in I1 alone defeats the inclusive reference result; a correction must restore this exact ID. Sources: SYN-101;SYN-102.

### V21: DIGITAL_SERVICE

V21 has amount **12,000.00 USD**, eligible count **4**, originators **3** and label **POSITIVE**. R1 is **TRUE**, I1 is **TRUE**, and C1 is **TRUE**; the mismatch flag is **false**. V21 is an above-boundary known positive correctly captured by all variants. Its true output must survive a proposed correction; agreement here does not dispose of the separate equality and null failures. Sources: SYN-101;SYN-102.

### V22: DIGITAL_SERVICE

V22 has amount **14,000.00 USD**, eligible count **2**, originators **2** and label **NEGATIVE**. R1 is **FALSE**, I1 is **FALSE**, and C1 is **FALSE**; the mismatch flag is **false**. V22 is a valid reference negative because two events are below the required three. The amount does not override that condition. Preserve this false output during a proposed correction. Sources: SYN-101;SYN-102.

### V23: DIGITAL_SERVICE

V23 has amount **18,000.00 USD**, eligible count **5**, originators **1** and label **POSITIVE**. R1 is **FALSE**, I1 is **FALSE**, and C1 is **TRUE**; the mismatch flag is **false**. V23 demonstrates the single-originator concept limitation. R1 and I1 agree on exclusion, while C1 includes it. Keep implementation fidelity separate from the known positive that this narrower concept misses. Sources: SYN-101;SYN-102.

### V24: DIGITAL_SERVICE

V24 has amount **null**, eligible count **4**, originators **3** and label **UNKNOWN**. R1 is **UNKNOWN**, I1 is **FALSE**, and C1 is **UNKNOWN**; the mismatch flag is **true**. V24 is one of the four null-handling differences. Its label is UNKNOWN, so the difference is not a known positive loss; retain it in the missing-input route and outside the known-label matrices. Sources: SYN-101;SYN-102.

## Complete finding narratives and next decisions

### MV-F01: Implementation loses inclusive-boundary known positives

Severity: **HIGH**. Confidence in the fictional observation: **HIGH**. Evidence class: **Observed**. Evidence: SYN-101, SYN-102.

V02 V08 V14 V20 each have amount 10000, count 3 and originators 2. R1 is true, while I1 uses greater-than and returns false. Four known positives are lost.

Proposed action: Correct the predicate in a separately versioned proposal and replay all 24 units, equality boundaries and unchanged cases.

The observation is bounded by the supplied fixture. It does not establish the prevalence of this issue in a live population or the legality of a particular institution's practice. A reviewer should challenge the affected IDs, exact calculation and possible alternative explanation, then record a separate human disposition if actual authority and evidence are supplied. No owner acceptance, operational execution or final signoff is represented here.

### MV-F02: Missing amount values silently become negative outcomes

Severity: **HIGH**. Confidence in the fictional observation: **HIGH**. Evidence class: **Observed**. Evidence: SYN-101, SYN-102.

V06 V12 V18 V24 lack amount inputs. R1 and C1 return unknown; I1 returns false. These four records cannot support no-hit assurance.

Proposed action: Preserve unknown outputs, recover missing amounts where possible and define a human exception route with measurable aging.

### MV-F03: Constructed labels and narrow concept do not establish effectiveness

Severity: **HIGH**. Confidence in the fictional observation: **HIGH**. Evidence class: **Observed**. Evidence: SYN-101, SYN-102.

R1 misses four known positives having one originator, and the broader challenger catches them. Raw transaction lineage and independent representative outcomes are not supplied.

Proposed action: Evaluate the concept and alternative mechanisms, obtain independent data and preserve this challenger as diagnostic evidence only.

### MV-F04: Governance and corrected replay remain unrecorded

Severity: **MEDIUM**. Confidence in the fictional observation: **HIGH**. Evidence class: **Observed**. Evidence: SYN-103.

The example supplies proposed issues and fictional roles, but no real reviewer qualifications, objectivity assessment, approval or corrected implementation replay.

Proposed action: Obtain actual accountable review evidence and keep release disposition unresolved until material gates are addressed.

## Boundary variations and expected interpretation

### Variation 01: Exact amount threshold

Change only this input: Use amount 10000, count 3, originators 2 and label POSITIVE.

Expected result: R1=true; I1=false; C1=true. This is a known-positive fidelity loss.

Required narrative: Equality is a material part of the specification. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 02: Just below amount

Change only this input: Use amount 9999.99, count 3 and originators 2.

Expected result: R1=false; I1=false; C1=false.

Required narrative: Do not round the input to 10000 before comparison. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 03: Just above amount

Change only this input: Use amount 10000.01, count 3 and originators 2.

Expected result: R1=true; I1=true; C1=true.

Required narrative: A correct result above the boundary does not disprove an equality defect. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 04: Count below boundary

Change only this input: Use amount 14000, count 2 and originators 2.

Expected result: All three variants return false.

Required narrative: A high amount does not override the minimum eligible event count. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 05: Count at boundary

Change only this input: Use amount 14000, count 3 and originators 2.

Expected result: All three variants return true.

Required narrative: The count comparator is also inclusive. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 06: Originator below boundary

Change only this input: Use amount 18000, count 5 and originators 1.

Expected result: R1=false; I1=false; C1=true.

Required narrative: This is conceptual sensitivity, not an implementation mismatch. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 07: Originator at boundary

Change only this input: Use amount 18000, count 5 and originators 2.

Expected result: All three variants return true.

Required narrative: The challenger no longer adds a different result for this unit. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 08: Amount absent

Change only this input: Use amount null, count 4 and originators 3.

Expected result: R1=unknown; I1=false; C1=unknown.

Required narrative: Unknown versus false is a fidelity difference even when the outcome label is unknown. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 09: Amount explicitly zero

Change only this input: Use amount 0, count 4 and originators 3.

Expected result: All three variants return false.

Required narrative: Zero is actual data and is not equivalent to a missing input. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 10: Negative credit amount

Change only this input: Use amount -10000 in this positive-credit aggregate scope.

Expected result: The input eligibility or amount check must reject the negative aggregate before applying the intended credit rule.

Required narrative: Do not silently take the absolute value to force a hit. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 11: Duplicate unit ID

Change only this input: Add a second V02 record with a different amount.

Expected result: Structural QA fails; preserve both input representations and resolve identity before counting.

Required narrative: Dropping an arbitrary row can hide the boundary defect. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 12: Unknown outcome on a hit

Change only this input: Change V03 label from POSITIVE to UNKNOWN while keeping features fixed.

Expected result: I1 still has 4 hits; known TP falls from 4 to 3; known_n becomes 19 and unknown_n becomes 5.

Required narrative: Labels and implementation outputs have different provenance. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 13: Correct only amount operator

Change only this input: Replace I1 greater-than with greater-or-equal while retaining missing-to-false.

Expected result: Four boundary mismatches resolve; four null mismatches remain.

Required narrative: A partial patch is not a complete correction. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 14: Correct only null handling

Change only this input: Make I1 return unknown for missing amount while retaining strict greater-than.

Expected result: Four null mismatches resolve; four known positive boundary losses remain.

Required narrative: The other defect must stay open. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 15: Full reference-equivalent correction

Change only this input: Implement R1 exactly on all 24 inputs.

Expected result: All 24 outputs match R1: 8 true, 12 false and 4 unknown.

Required narrative: Conceptual limitations and representative-outcome requirements remain. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 16: New transaction evidence

Change only this input: Provide complete transaction-to-feature lineage for selected units only.

Expected result: D03 can be reviewed for that limited subset; unprovided units remain outside lineage assurance.

Required narrative: Partial new evidence cannot justify a whole-population lineage claim. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 17: Favorable validation score

Change only this input: Calculate 12 passed tests divided by 24 total tests.

Expected result: 50.0% is merely a test-state proportion; no validated quality score exists.

Required narrative: The four failed tests and eight blocked tests retain their individual consequences. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 18: Vendor calls the rule a model

Change only this input: A provider describes a fixed rule as AI without design evidence.

Expected result: Classification remains based on actual design and use; marketing does not establish applicability.

Required narrative: Request the mathematical and operational basis before borrowing model-specific claims. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

## Embedded independent fixture check

The following complete standard-library Python block is optional in-session verification. It has no repository, file, network or installation dependency. It starts from the raw fixture declarations, derives results and checks independent expected ID sets, counts and boundary values. If execution is unavailable, reperform the printed equations and mark the executable check NOT_TESTED. Passing this block establishes the stated fixture relationships only.

<!-- FIXTURE_CHECK:START -->
```python
# Pure Python; no repository, files, packages or network required.
from collections import Counter
RAW = [['V01', 'RETAIL', 9999, 3, 2, 'NEGATIVE'], ['V02', 'RETAIL', 10000, 3, 2, 'POSITIVE'], ['V03', 'RETAIL', 12000, 4, 3, 'POSITIVE'], ['V04', 'RETAIL', 14000, 2, 2, 'NEGATIVE'], ['V05', 'RETAIL', 18000, 5, 1, 'POSITIVE'], ['V06', 'RETAIL', None, 4, 3, 'UNKNOWN'], ['V07', 'BUSINESS', 9999, 3, 2, 'NEGATIVE'], ['V08', 'BUSINESS', 10000, 3, 2, 'POSITIVE'], ['V09', 'BUSINESS', 12000, 4, 3, 'POSITIVE'], ['V10', 'BUSINESS', 14000, 2, 2, 'NEGATIVE'], ['V11', 'BUSINESS', 18000, 5, 1, 'POSITIVE'], ['V12', 'BUSINESS', None, 4, 3, 'UNKNOWN'], ['V13', 'CORRESPONDENT', 9999, 3, 2, 'NEGATIVE'], ['V14', 'CORRESPONDENT', 10000, 3, 2, 'POSITIVE'], ['V15', 'CORRESPONDENT', 12000, 4, 3, 'POSITIVE'], ['V16', 'CORRESPONDENT', 14000, 2, 2, 'NEGATIVE'], ['V17', 'CORRESPONDENT', 18000, 5, 1, 'POSITIVE'], ['V18', 'CORRESPONDENT', None, 4, 3, 'UNKNOWN'], ['V19', 'DIGITAL_SERVICE', 9999, 3, 2, 'NEGATIVE'], ['V20', 'DIGITAL_SERVICE', 10000, 3, 2, 'POSITIVE'], ['V21', 'DIGITAL_SERVICE', 12000, 4, 3, 'POSITIVE'], ['V22', 'DIGITAL_SERVICE', 14000, 2, 2, 'NEGATIVE'], ['V23', 'DIGITAL_SERVICE', 18000, 5, 1, 'POSITIVE'], ['V24', 'DIGITAL_SERVICE', None, 4, 3, 'UNKNOWN']]
def reference(amount,count,originators):
    return None if amount is None else amount>=10000 and count>=3 and originators>=2
def implemented(amount,count,originators):
    return False if amount is None else amount>10000 and count>=3 and originators>=2
def challenger(amount,count,originators):
    return None if amount is None else amount>=10000 and count>=3
rows=[]
for uid,segment,amount,count,originators,label in RAW:
    r=reference(amount,count,originators);i=implemented(amount,count,originators);c=challenger(amount,count,originators)
    rows.append([uid,segment,amount,count,originators,label,r,i,c,r!=i,"SYN-101;SYN-102"])
assert len(rows)==24 and len({r[0] for r in rows})==24
assert {r[0] for r in rows if r[6] is True} == {"V02","V03","V08","V09","V14","V15","V20","V21"}
assert {r[0] for r in rows if r[7] is True} == {"V03","V09","V15","V21"}
assert {r[0] for r in rows if r[6] is None} == {"V06","V12","V18","V24"}
assert sum(r[9] for r in rows)==8
matrices=[]
for label,column in [("REFERENCE",6),("IMPLEMENTED",7),("CHALLENGER",8)]:
    known=[r for r in rows if r[5] in ("POSITIVE","NEGATIVE")]
    tp=sum(r[column] is True and r[5]=="POSITIVE" for r in known)
    fp=sum(r[column] is True and r[5]=="NEGATIVE" for r in known)
    fn=sum(r[column] is False and r[5]=="POSITIVE" for r in known)
    tn=sum(r[column] is False and r[5]=="NEGATIVE" for r in known)
    matrices.append([label,24,20,4,tp,fp,fn,tn,sum(r[column] is True for r in rows),
        sum(r[column] is None for r in rows),tp/(tp+fp),tp/(tp+fn),"SYN-101;SYN-102"])
assert [r[4:8] for r in matrices]==[[8,0,4,8],[4,0,8,8],[12,0,0,8]]
assert reference(10000,3,2) is True and implemented(10000,3,2) is False
assert reference(9999.99,3,2) is False and reference(10000.01,3,2) is True
assert reference(14000,2,2) is False and reference(14000,3,2) is True
assert reference(18000,5,1) is False and challenger(18000,5,1) is True
assert reference(None,4,3) is None and implemented(None,4,3) is False
assert reference(0,4,3) is False
# Correcting only one mechanism leaves exactly four differences.
operator_only=lambda a,c,o: False if a is None else a>=10000 and c>=3 and o>=2
null_only=lambda a,c,o: None if a is None else a>10000 and c>=3 and o>=2
assert sum(reference(r[2],r[3],r[4])!=operator_only(r[2],r[3],r[4]) for r in RAW)==4
assert sum(reference(r[2],r[3],r[4])!=null_only(r[2],r[3],r[4]) for r in RAW)==4
TEST_RESULTS = ['PASS', 'FAIL', 'PASS', 'BLOCKED', 'PASS', 'FAIL', 'BLOCKED', 'BLOCKED', 'FAIL', 'PASS', 'PASS', 'FAIL', 'PASS', 'PASS', 'PASS', 'BLOCKED', 'PASS', 'BLOCKED', 'BLOCKED', 'PASS', 'PASS', 'PASS', 'BLOCKED', 'BLOCKED']
assert Counter(TEST_RESULTS)=={"PASS":12,"FAIL":4,"BLOCKED":8}
# Separate lineage demonstration from file 03; it is not evidence for primary V units.
lineage = [
    ("X01","2026-05-01","CREDIT","POSTED",4000,"A",None),
    ("X02","2026-05-15","CREDIT","POSTED",3500,"B",None),
    ("X03","2026-05-30","CREDIT","POSTED",2500,"A",None),
    ("X04","2026-04-30","CREDIT","POSTED",6000,"C",None),
    ("X05","2026-05-31","CREDIT","POSTED",7000,"D",None),
    ("X06","2026-05-20","CREDIT","POSTED",9000,"E","X07"),
    ("X07","2026-05-21","REVERSAL","POSTED",-9000,"E","X06"),
    ("X08","2026-05-22","CREDIT","PENDING",1000,"F",None),
    ("X09","2026-05-23","DEBIT","POSTED",2000,"G",None),
    ("X10","2026-05-25","CREDIT","REJECTED",3000,"H",None)]
eligible_events = [e for e in lineage if "2026-05-01"<=e[1]<= "2026-05-30"
    and e[2]=="CREDIT" and e[3]=="POSTED" and e[6] is None]
assert [e[0] for e in eligible_events]==["X01","X02","X03"]
features=(sum(e[4] for e in eligible_events),len(eligible_events),len({e[5] for e in eligible_events}))
assert features==(10000,3,2)
assert reference(*features) is True and implemented(*features) is False
assert len(lineage)-len(eligible_events)==7
CHECKED_TABLES={"OutcomeUnits":rows,"OutcomeMetrics":matrices}
print("Monitoring validation fixture: 24 units, three matrices, eight differences and 24 test states passed.")
```
<!-- FIXTURE_CHECK:END -->

## Completed analytical recommendation

Do not support release of I1 on the supplied evidence. The implementation differs from the reference at inclusive boundaries and missing values; broader effectiveness, transaction lineage, objective review and actual authorization remain unresolved.

**Validation opinion and use restrictions.** Do not support release of I1 on the supplied evidence. The implementation differs from the reference at inclusive boundaries and missing values; broader effectiveness, transaction lineage, objective review and actual authorization remain unresolved.

**System scope classification and review design.** The supplied subject is deterministic monitoring logic over 24 feature-level customer-window units. R1 tests amount>=10000, count>=3 and originators>=2; absent amount returns unknown. I1 uses amount>10000 and returns false for absent amount. No universal institutional model classification is implied.

**Material validation findings.** Four known positive boundary units are lost. Four missing amounts are silently changed to false. A separate conceptual limitation excludes four single-originator positives. These mechanisms require distinct findings rather than one combined percentage.

**Component tests and outcome registers.** R1 gives TP8 FP0 FN4 TN8; I1 gives TP4 FP0 FN8 TN8; C1 gives TP12 FP0 FN0 TN8. All matrices use twenty known labels. Four UNKNOWN labels stay outside; only R1 and C1 retain unknown input states.

**Issue resolution and release gates.** The 24 tests distinguish arithmetic passes from failed concepts or implementation and blocked evidence requests. Four issues remain OPEN or BLOCKED. A passed matrix calculation means the arithmetic is right; it does not mean the underlying system meets its intended use.

**Evidence provenance and competing interpretations.** SYN-101 contains features, not source transactions. SYN-102 supplies three independent predicate descriptions. SYN-103 records fictional governance gaps. Current public model guidance must be assessed for scope and applicability; this deterministic example is not automatically a model under that definition.

**Required remediation and further challenge.** Proposed corrections need versioned implementation evidence, unchanged-case regression tests, feature lineage, independent outcome review and a real human disposition. The challenger is a diagnostic stress of one assumption, not an approved replacement.

**Limitations quality review and human disposition.** Reproduce eight mismatches, split four boundary losses from four missing-state differences, and verify each matrix. No probability interval or deployment approval follows from designed fictional examples. Keep the report in a restricted draft state until the stated evidence gates are resolved.

## Next-session change control

When new evidence arrives, preserve this specimen or the prior real-case version, assign the new source its own ID and cutoff, and identify the affected methods and tables. Recalculate the complete relevant denominator rather than editing one favorable headline. Update the finding, action, limitation and human-decision records together. A resolved arithmetic issue does not automatically resolve evidence, concept or authorization gates, and a new source can create additional review work even while it improves retrieval coverage.
