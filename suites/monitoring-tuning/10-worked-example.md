# Fully populated worked example — Monitoring Scenario and Threshold Review

**Fictional records only.** The inputs below are deliberately constructed to demonstrate the full method, adverse branches and incomplete decision gates. They are not customer data, a real validation or evidence of an institution's control quality. All parameters are illustrative. The supplied cutoff is Oct 09, 2026.

The central question is not which threshold creates the smallest queue. It is which predeclared candidate has a defensible coverage and workload tradeoff under the supplied evidence, after the monitoring pipeline has preserved the activity that should reach review. Compare raw detection with routed review separately. A nominal improvement in recall can be defeated by suppression, and a reduction in case count can come from merging rather than a lower false-positive rate. The worked case deliberately includes each mechanism so they cannot be treated as interchangeable.

The fixture is a 36-unit customer-window evaluation with three segments and three protected partitions. Four candidates share the same scores, eligibility and labels. Twenty-nine labels are mature within the fiction; seven are unavailable or censored. Eighteen dependence groups contain pairs of units. G17 is suppressed without supplied current authority. The complete below-threshold frame is retained alongside a six-record illustrative review draw. No statistical population inference, live effectiveness claim or deployment authorization is part of this specimen.

## Independent source declarations

The raw input blocks below define the scores and labels independently of every expected result. Group IDs pair adjacent units within each four-unit segment block; all members of a group share a partition. Every unit is eligible. Segment lead-time assumptions are 1.0,1.5 and 2.0 hours; each additional retained hit in a merged group adds 0.25 hours. G17 is the sole suppressed group, and current suppression authorization is not supplied. The illustrative capacity is 5 hours per partition or 15 hours across the complete fixture.

| partition | segment | four scores in unit order | four labels in unit order |
| --- | --- | --- | --- |
| TRAIN | RETAIL | 82,67,56,32 | POSITIVE,NEGATIVE,POSITIVE,NEGATIVE |
| TRAIN | SMALL_BUSINESS | 88,72,58,44 | POSITIVE,NEGATIVE,POSITIVE,UNKNOWN |
| TRAIN | CORRESPONDENT | 93,77,63,39 | POSITIVE,NEGATIVE,POSITIVE,CENSORED |
| VALIDATION | RETAIL | 79,64,54,28 | POSITIVE,NEGATIVE,POSITIVE,NEGATIVE |
| VALIDATION | SMALL_BUSINESS | 86,69,57,42 | POSITIVE,NEGATIVE,UNKNOWN,NEGATIVE |
| VALIDATION | CORRESPONDENT | 91,74,61,36 | POSITIVE,NEGATIVE,POSITIVE,CENSORED |
| HOLDOUT | RETAIL | 81,66,53,31 | POSITIVE,NEGATIVE,POSITIVE,UNKNOWN |
| HOLDOUT | SMALL_BUSINESS | 84,71,59,41 | POSITIVE,NEGATIVE,POSITIVE,NEGATIVE |
| HOLDOUT | CORRESPONDENT | 94,76,62,37 | POSITIVE,NEGATIVE,UNKNOWN,CENSORED |

The candidate list is frozen before protected results by explicit fictional premise. BASE60 uses 60 in all segments, HIGH7575, LOW5050, and SEGMENTED55/60/65 for RETAIL/SMALL_BUSINESS/CORRESPONDENT. Every comparison is inclusive. The below-threshold selection lists are TRAIN U03/U07, VALIDATION U15/U20 and HOLDOUT U28/U36. Those lists define the first two ranks; remaining nonhits follow source order. They are illustrative assignments, not a claim of random selection.

## Complete populated output registers

### Population

| unit_id | group_id | partition | segment | score | label | label_basis | eligible | suppressed | review_hours | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| U01 | G01 | TRAIN | RETAIL | 82 | POSITIVE | Fictional closed review | true | false | 1 | SYN-001 |
| U02 | G01 | TRAIN | RETAIL | 67 | NEGATIVE | Fictional closed review | true | false | 1 | SYN-001 |
| U03 | G02 | TRAIN | RETAIL | 56 | POSITIVE | Fictional closed review | true | false | 1 | SYN-001 |
| U04 | G02 | TRAIN | RETAIL | 32 | NEGATIVE | Fictional closed review | true | false | 1 | SYN-001 |
| U05 | G03 | TRAIN | SMALL_BUSINESS | 88 | POSITIVE | Fictional closed review | true | false | 1.5 | SYN-001 |
| U06 | G03 | TRAIN | SMALL_BUSINESS | 72 | NEGATIVE | Fictional closed review | true | false | 1.5 | SYN-001 |
| U07 | G04 | TRAIN | SMALL_BUSINESS | 58 | POSITIVE | Fictional closed review | true | false | 1.5 | SYN-001 |
| U08 | G04 | TRAIN | SMALL_BUSINESS | 44 | UNKNOWN | Review evidence unavailable | true | false | 1.5 | SYN-001 |
| U09 | G05 | TRAIN | CORRESPONDENT | 93 | POSITIVE | Fictional closed review | true | false | 2 | SYN-001 |
| U10 | G05 | TRAIN | CORRESPONDENT | 77 | NEGATIVE | Fictional closed review | true | false | 2 | SYN-001 |
| U11 | G06 | TRAIN | CORRESPONDENT | 63 | POSITIVE | Fictional closed review | true | false | 2 | SYN-001 |
| U12 | G06 | TRAIN | CORRESPONDENT | 39 | CENSORED | Outcome window not mature | true | false | 2 | SYN-001 |
| U13 | G07 | VALIDATION | RETAIL | 79 | POSITIVE | Fictional closed review | true | false | 1 | SYN-001 |
| U14 | G07 | VALIDATION | RETAIL | 64 | NEGATIVE | Fictional closed review | true | false | 1 | SYN-001 |
| U15 | G08 | VALIDATION | RETAIL | 54 | POSITIVE | Fictional closed review | true | false | 1 | SYN-001 |
| U16 | G08 | VALIDATION | RETAIL | 28 | NEGATIVE | Fictional closed review | true | false | 1 | SYN-001 |
| U17 | G09 | VALIDATION | SMALL_BUSINESS | 86 | POSITIVE | Fictional closed review | true | false | 1.5 | SYN-001 |
| U18 | G09 | VALIDATION | SMALL_BUSINESS | 69 | NEGATIVE | Fictional closed review | true | false | 1.5 | SYN-001 |
| U19 | G10 | VALIDATION | SMALL_BUSINESS | 57 | UNKNOWN | Review evidence unavailable | true | false | 1.5 | SYN-001 |
| U20 | G10 | VALIDATION | SMALL_BUSINESS | 42 | NEGATIVE | Fictional closed review | true | false | 1.5 | SYN-001 |
| U21 | G11 | VALIDATION | CORRESPONDENT | 91 | POSITIVE | Fictional closed review | true | false | 2 | SYN-001 |
| U22 | G11 | VALIDATION | CORRESPONDENT | 74 | NEGATIVE | Fictional closed review | true | false | 2 | SYN-001 |
| U23 | G12 | VALIDATION | CORRESPONDENT | 61 | POSITIVE | Fictional closed review | true | false | 2 | SYN-001 |
| U24 | G12 | VALIDATION | CORRESPONDENT | 36 | CENSORED | Outcome window not mature | true | false | 2 | SYN-001 |
| U25 | G13 | HOLDOUT | RETAIL | 81 | POSITIVE | Fictional closed review | true | false | 1 | SYN-001 |
| U26 | G13 | HOLDOUT | RETAIL | 66 | NEGATIVE | Fictional closed review | true | false | 1 | SYN-001 |
| U27 | G14 | HOLDOUT | RETAIL | 53 | POSITIVE | Fictional closed review | true | false | 1 | SYN-001 |
| U28 | G14 | HOLDOUT | RETAIL | 31 | UNKNOWN | Review evidence unavailable | true | false | 1 | SYN-001 |
| U29 | G15 | HOLDOUT | SMALL_BUSINESS | 84 | POSITIVE | Fictional closed review | true | false | 1.5 | SYN-001 |
| U30 | G15 | HOLDOUT | SMALL_BUSINESS | 71 | NEGATIVE | Fictional closed review | true | false | 1.5 | SYN-001 |
| U31 | G16 | HOLDOUT | SMALL_BUSINESS | 59 | POSITIVE | Fictional closed review | true | false | 1.5 | SYN-001 |
| U32 | G16 | HOLDOUT | SMALL_BUSINESS | 41 | NEGATIVE | Fictional closed review | true | false | 1.5 | SYN-001 |
| U33 | G17 | HOLDOUT | CORRESPONDENT | 94 | POSITIVE | Fictional closed review | true | true | 2 | SYN-001 |
| U34 | G17 | HOLDOUT | CORRESPONDENT | 76 | NEGATIVE | Fictional closed review | true | true | 2 | SYN-001 |
| U35 | G18 | HOLDOUT | CORRESPONDENT | 62 | UNKNOWN | Review evidence unavailable | true | false | 2 | SYN-001 |
| U36 | G18 | HOLDOUT | CORRESPONDENT | 37 | CENSORED | Outcome window not mature | true | false | 2 | SYN-001 |

### Candidates

| candidate_id | retail_threshold | business_threshold | correspondent_threshold | comparator | freeze_state | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| BASE60 | 60 | 60 | 60 | GREATER_OR_EQUAL | ILLUSTRATIVE_PREFROZEN | SYN-002 |
| HIGH75 | 75 | 75 | 75 | GREATER_OR_EQUAL | ILLUSTRATIVE_PREFROZEN | SYN-002 |
| LOW50 | 50 | 50 | 50 | GREATER_OR_EQUAL | ILLUSTRATIVE_PREFROZEN | SYN-002 |
| SEGMENTED | 55 | 60 | 65 | GREATER_OR_EQUAL | ILLUSTRATIVE_PREFROZEN | SYN-002 |

### CandidateMetrics

| candidate_id | partition | population_n | known_n | tp | fp | fn | tn | unknown_n | raw_hits | retained_hits | queued_cases | workload_hours | precision | recall | retained_positive_hits |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BASE60 | TRAIN | 12 | 10 | 4 | 3 | 2 | 1 | 2 | 7 | 7 | 4 | 7.25 | 0.5714285714285714 | 0.6666666666666666 | 4 |
| BASE60 | VALIDATION | 12 | 10 | 4 | 3 | 1 | 2 | 2 | 7 | 7 | 4 | 7.25 | 0.5714285714285714 | 0.8 | 4 |
| BASE60 | HOLDOUT | 12 | 9 | 3 | 3 | 2 | 1 | 3 | 7 | 5 | 3 | 5.0 | 0.5 | 0.6 | 2 |
| BASE60 | ALL | 36 | 29 | 11 | 9 | 5 | 4 | 7 | 21 | 19 | 11 | 19.5 | 0.55 | 0.6875 | 10 |
| HIGH75 | TRAIN | 12 | 10 | 3 | 1 | 3 | 3 | 2 | 4 | 4 | 3 | 4.75 | 0.75 | 0.5 | 3 |
| HIGH75 | VALIDATION | 12 | 10 | 3 | 0 | 2 | 5 | 2 | 3 | 3 | 3 | 4.5 | 1.0 | 0.6 | 3 |
| HIGH75 | HOLDOUT | 12 | 9 | 3 | 1 | 2 | 3 | 3 | 4 | 2 | 2 | 2.5 | 0.75 | 0.6 | 2 |
| HIGH75 | ALL | 36 | 29 | 9 | 2 | 7 | 11 | 7 | 11 | 9 | 8 | 11.75 | 0.8181818181818182 | 0.5625 | 8 |
| LOW50 | TRAIN | 12 | 10 | 6 | 3 | 0 | 1 | 2 | 9 | 9 | 6 | 9.75 | 0.6666666666666666 | 1.0 | 6 |
| LOW50 | VALIDATION | 12 | 10 | 5 | 3 | 0 | 2 | 2 | 9 | 9 | 6 | 9.75 | 0.625 | 1.0 | 5 |
| LOW50 | HOLDOUT | 12 | 9 | 5 | 3 | 0 | 1 | 3 | 9 | 7 | 5 | 7.5 | 0.625 | 1.0 | 4 |
| LOW50 | ALL | 36 | 29 | 16 | 9 | 0 | 4 | 7 | 27 | 25 | 17 | 27.0 | 0.64 | 1.0 | 15 |
| SEGMENTED | TRAIN | 12 | 10 | 4 | 3 | 2 | 1 | 2 | 7 | 7 | 4 | 6.25 | 0.5714285714285714 | 0.6666666666666666 | 4 |
| SEGMENTED | VALIDATION | 12 | 10 | 3 | 3 | 2 | 2 | 2 | 6 | 6 | 3 | 5.25 | 0.5 | 0.6 | 3 |
| SEGMENTED | HOLDOUT | 12 | 9 | 3 | 3 | 2 | 1 | 3 | 6 | 4 | 2 | 3.0 | 0.5 | 0.6 | 2 |
| SEGMENTED | ALL | 36 | 29 | 10 | 9 | 6 | 4 | 7 | 19 | 17 | 9 | 14.5 | 0.5263157894736842 | 0.625 | 9 |

### AlertRouting

| hit_id | candidate_id | unit_id | group_id | route_state | case_id | lead_unit_id | routing_basis | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BASE60-U01 | BASE60 | U01 | G01 | QUEUED_LEAD | BASE60-G01 | U01 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U02 | BASE60 | U02 | G01 | MERGED_CHILD | BASE60-G01 | U01 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U05 | BASE60 | U05 | G03 | QUEUED_LEAD | BASE60-G03 | U05 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U06 | BASE60 | U06 | G03 | MERGED_CHILD | BASE60-G03 | U05 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U09 | BASE60 | U09 | G05 | QUEUED_LEAD | BASE60-G05 | U09 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U10 | BASE60 | U10 | G05 | MERGED_CHILD | BASE60-G05 | U09 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U11 | BASE60 | U11 | G06 | QUEUED_LEAD | BASE60-G06 | U11 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U13 | BASE60 | U13 | G07 | QUEUED_LEAD | BASE60-G07 | U13 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U14 | BASE60 | U14 | G07 | MERGED_CHILD | BASE60-G07 | U13 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U17 | BASE60 | U17 | G09 | QUEUED_LEAD | BASE60-G09 | U17 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U18 | BASE60 | U18 | G09 | MERGED_CHILD | BASE60-G09 | U17 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U21 | BASE60 | U21 | G11 | QUEUED_LEAD | BASE60-G11 | U21 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U22 | BASE60 | U22 | G11 | MERGED_CHILD | BASE60-G11 | U21 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U23 | BASE60 | U23 | G12 | QUEUED_LEAD | BASE60-G12 | U23 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U25 | BASE60 | U25 | G13 | QUEUED_LEAD | BASE60-G13 | U25 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U26 | BASE60 | U26 | G13 | MERGED_CHILD | BASE60-G13 | U25 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U29 | BASE60 | U29 | G15 | QUEUED_LEAD | BASE60-G15 | U29 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U30 | BASE60 | U30 | G15 | MERGED_CHILD | BASE60-G15 | U29 | Same frozen group and partition | SYN-001;SYN-003 |
| BASE60-U33 | BASE60 | U33 | G17 | SUPPRESSED | null | null | Unexpired authorization absent | SYN-001;SYN-003 |
| BASE60-U34 | BASE60 | U34 | G17 | SUPPRESSED | null | null | Unexpired authorization absent | SYN-001;SYN-003 |
| BASE60-U35 | BASE60 | U35 | G18 | QUEUED_LEAD | BASE60-G18 | U35 | Same frozen group and partition | SYN-001;SYN-003 |
| HIGH75-U01 | HIGH75 | U01 | G01 | QUEUED_LEAD | HIGH75-G01 | U01 | Same frozen group and partition | SYN-001;SYN-003 |
| HIGH75-U05 | HIGH75 | U05 | G03 | QUEUED_LEAD | HIGH75-G03 | U05 | Same frozen group and partition | SYN-001;SYN-003 |
| HIGH75-U09 | HIGH75 | U09 | G05 | QUEUED_LEAD | HIGH75-G05 | U09 | Same frozen group and partition | SYN-001;SYN-003 |
| HIGH75-U10 | HIGH75 | U10 | G05 | MERGED_CHILD | HIGH75-G05 | U09 | Same frozen group and partition | SYN-001;SYN-003 |
| HIGH75-U13 | HIGH75 | U13 | G07 | QUEUED_LEAD | HIGH75-G07 | U13 | Same frozen group and partition | SYN-001;SYN-003 |
| HIGH75-U17 | HIGH75 | U17 | G09 | QUEUED_LEAD | HIGH75-G09 | U17 | Same frozen group and partition | SYN-001;SYN-003 |
| HIGH75-U21 | HIGH75 | U21 | G11 | QUEUED_LEAD | HIGH75-G11 | U21 | Same frozen group and partition | SYN-001;SYN-003 |
| HIGH75-U25 | HIGH75 | U25 | G13 | QUEUED_LEAD | HIGH75-G13 | U25 | Same frozen group and partition | SYN-001;SYN-003 |
| HIGH75-U29 | HIGH75 | U29 | G15 | QUEUED_LEAD | HIGH75-G15 | U29 | Same frozen group and partition | SYN-001;SYN-003 |
| HIGH75-U33 | HIGH75 | U33 | G17 | SUPPRESSED | null | null | Unexpired authorization absent | SYN-001;SYN-003 |
| HIGH75-U34 | HIGH75 | U34 | G17 | SUPPRESSED | null | null | Unexpired authorization absent | SYN-001;SYN-003 |
| LOW50-U01 | LOW50 | U01 | G01 | QUEUED_LEAD | LOW50-G01 | U01 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U02 | LOW50 | U02 | G01 | MERGED_CHILD | LOW50-G01 | U01 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U03 | LOW50 | U03 | G02 | QUEUED_LEAD | LOW50-G02 | U03 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U05 | LOW50 | U05 | G03 | QUEUED_LEAD | LOW50-G03 | U05 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U06 | LOW50 | U06 | G03 | MERGED_CHILD | LOW50-G03 | U05 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U07 | LOW50 | U07 | G04 | QUEUED_LEAD | LOW50-G04 | U07 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U09 | LOW50 | U09 | G05 | QUEUED_LEAD | LOW50-G05 | U09 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U10 | LOW50 | U10 | G05 | MERGED_CHILD | LOW50-G05 | U09 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U11 | LOW50 | U11 | G06 | QUEUED_LEAD | LOW50-G06 | U11 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U13 | LOW50 | U13 | G07 | QUEUED_LEAD | LOW50-G07 | U13 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U14 | LOW50 | U14 | G07 | MERGED_CHILD | LOW50-G07 | U13 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U15 | LOW50 | U15 | G08 | QUEUED_LEAD | LOW50-G08 | U15 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U17 | LOW50 | U17 | G09 | QUEUED_LEAD | LOW50-G09 | U17 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U18 | LOW50 | U18 | G09 | MERGED_CHILD | LOW50-G09 | U17 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U19 | LOW50 | U19 | G10 | QUEUED_LEAD | LOW50-G10 | U19 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U21 | LOW50 | U21 | G11 | QUEUED_LEAD | LOW50-G11 | U21 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U22 | LOW50 | U22 | G11 | MERGED_CHILD | LOW50-G11 | U21 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U23 | LOW50 | U23 | G12 | QUEUED_LEAD | LOW50-G12 | U23 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U25 | LOW50 | U25 | G13 | QUEUED_LEAD | LOW50-G13 | U25 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U26 | LOW50 | U26 | G13 | MERGED_CHILD | LOW50-G13 | U25 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U27 | LOW50 | U27 | G14 | QUEUED_LEAD | LOW50-G14 | U27 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U29 | LOW50 | U29 | G15 | QUEUED_LEAD | LOW50-G15 | U29 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U30 | LOW50 | U30 | G15 | MERGED_CHILD | LOW50-G15 | U29 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U31 | LOW50 | U31 | G16 | QUEUED_LEAD | LOW50-G16 | U31 | Same frozen group and partition | SYN-001;SYN-003 |
| LOW50-U33 | LOW50 | U33 | G17 | SUPPRESSED | null | null | Unexpired authorization absent | SYN-001;SYN-003 |
| LOW50-U34 | LOW50 | U34 | G17 | SUPPRESSED | null | null | Unexpired authorization absent | SYN-001;SYN-003 |
| LOW50-U35 | LOW50 | U35 | G18 | QUEUED_LEAD | LOW50-G18 | U35 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U01 | SEGMENTED | U01 | G01 | QUEUED_LEAD | SEGMENTED-G01 | U01 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U02 | SEGMENTED | U02 | G01 | MERGED_CHILD | SEGMENTED-G01 | U01 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U03 | SEGMENTED | U03 | G02 | QUEUED_LEAD | SEGMENTED-G02 | U03 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U05 | SEGMENTED | U05 | G03 | QUEUED_LEAD | SEGMENTED-G03 | U05 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U06 | SEGMENTED | U06 | G03 | MERGED_CHILD | SEGMENTED-G03 | U05 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U09 | SEGMENTED | U09 | G05 | QUEUED_LEAD | SEGMENTED-G05 | U09 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U10 | SEGMENTED | U10 | G05 | MERGED_CHILD | SEGMENTED-G05 | U09 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U13 | SEGMENTED | U13 | G07 | QUEUED_LEAD | SEGMENTED-G07 | U13 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U14 | SEGMENTED | U14 | G07 | MERGED_CHILD | SEGMENTED-G07 | U13 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U17 | SEGMENTED | U17 | G09 | QUEUED_LEAD | SEGMENTED-G09 | U17 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U18 | SEGMENTED | U18 | G09 | MERGED_CHILD | SEGMENTED-G09 | U17 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U21 | SEGMENTED | U21 | G11 | QUEUED_LEAD | SEGMENTED-G11 | U21 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U22 | SEGMENTED | U22 | G11 | MERGED_CHILD | SEGMENTED-G11 | U21 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U25 | SEGMENTED | U25 | G13 | QUEUED_LEAD | SEGMENTED-G13 | U25 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U26 | SEGMENTED | U26 | G13 | MERGED_CHILD | SEGMENTED-G13 | U25 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U29 | SEGMENTED | U29 | G15 | QUEUED_LEAD | SEGMENTED-G15 | U29 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U30 | SEGMENTED | U30 | G15 | MERGED_CHILD | SEGMENTED-G15 | U29 | Same frozen group and partition | SYN-001;SYN-003 |
| SEGMENTED-U33 | SEGMENTED | U33 | G17 | SUPPRESSED | null | null | Unexpired authorization absent | SYN-001;SYN-003 |
| SEGMENTED-U34 | SEGMENTED | U34 | G17 | SUPPRESSED | null | null | Unexpired authorization absent | SYN-001;SYN-003 |

### BelowThreshold

| draw_id | unit_id | partition | frame_n | rank | selected | review_label | design | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTL-U03 | U03 | TRAIN | 5 | 1 | true | POSITIVE | ILLUSTRATIVE_RANK | SYN-004 |
| BTL-U04 | U04 | TRAIN | 5 | 3 | false | NOT_REVIEWED | ILLUSTRATIVE_RANK | SYN-004 |
| BTL-U07 | U07 | TRAIN | 5 | 2 | true | POSITIVE | ILLUSTRATIVE_RANK | SYN-004 |
| BTL-U08 | U08 | TRAIN | 5 | 4 | false | NOT_REVIEWED | ILLUSTRATIVE_RANK | SYN-004 |
| BTL-U12 | U12 | TRAIN | 5 | 5 | false | NOT_REVIEWED | ILLUSTRATIVE_RANK | SYN-004 |
| BTL-U15 | U15 | VALIDATION | 5 | 1 | true | POSITIVE | ILLUSTRATIVE_RANK | SYN-004 |
| BTL-U16 | U16 | VALIDATION | 5 | 3 | false | NOT_REVIEWED | ILLUSTRATIVE_RANK | SYN-004 |
| BTL-U19 | U19 | VALIDATION | 5 | 4 | false | NOT_REVIEWED | ILLUSTRATIVE_RANK | SYN-004 |
| BTL-U20 | U20 | VALIDATION | 5 | 2 | true | NEGATIVE | ILLUSTRATIVE_RANK | SYN-004 |
| BTL-U24 | U24 | VALIDATION | 5 | 5 | false | NOT_REVIEWED | ILLUSTRATIVE_RANK | SYN-004 |
| BTL-U27 | U27 | HOLDOUT | 5 | 3 | false | NOT_REVIEWED | ILLUSTRATIVE_RANK | SYN-004 |
| BTL-U28 | U28 | HOLDOUT | 5 | 1 | true | UNKNOWN | ILLUSTRATIVE_RANK | SYN-004 |
| BTL-U31 | U31 | HOLDOUT | 5 | 4 | false | NOT_REVIEWED | ILLUSTRATIVE_RANK | SYN-004 |
| BTL-U32 | U32 | HOLDOUT | 5 | 5 | false | NOT_REVIEWED | ILLUSTRATIVE_RANK | SYN-004 |
| BTL-U36 | U36 | HOLDOUT | 5 | 2 | true | CENSORED | ILLUSTRATIVE_RANK | SYN-004 |

### CandidateDecisions

| candidate_id | decision_state | coverage_gate | capacity_gate | routing_gate | next_evidence | human_disposition | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BASE60 | BASELINE_ONLY | Raw known recall 11/16; retained positive hits 10 | ALL workload 19.5 hours; illustrative combined capacity 15 hours; no staffing-only selection | G17 authorization unverified | Resolve suppression and missing labels before change assessment | NOT_RECORDED | SYN-001;SYN-003 |
| HIGH75 | DO_NOT_SUPPORT | Raw known recall 9/16; retained positive hits 8 | ALL workload 11.75 hours; illustrative combined capacity 15 hours; no staffing-only selection | G17 authorization unverified | Challenge losses U11 and U23 against gains; no automatic acceptance | NOT_RECORDED | SYN-001;SYN-002;SYN-003 |
| LOW50 | FURTHER_VALIDATION_ONLY | Raw known recall 16/16; retained positive hits 15 | ALL workload 27 hours; illustrative combined capacity 15 hours; no staffing-only selection | G17 authorization unverified | Representative labels, routing repair, capacity and protected retest | NOT_RECORDED | SYN-001;SYN-002;SYN-003 |
| SEGMENTED | DO_NOT_SUPPORT | Raw known recall 10/16; retained positive hits 9 | ALL workload 14.5 hours; illustrative combined capacity 15 hours; no staffing-only selection | G17 authorization unverified | Resolve correspondent sensitivity and RETAIL boundary changes | NOT_RECORDED | SYN-001;SYN-002;SYN-003 |

### EvidenceProvenance

| source_id | source_kind | as_of | availability | unit_count | grain | limitation | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SYN-001 | SYNTHETIC_INPUT | 2026-10-09 | COMPLETE_FIXTURE | 36 | scored customer-window units | Labels are fictional and dependent within merge groups. | SYN-001 |
| SYN-002 | SYNTHETIC_INPUT | 2026-10-09 | COMPLETE_FIXTURE | 4 | candidate configurations | Parameter values are illustrative, not approved live settings. | SYN-002 |
| SYN-003 | SYNTHETIC_INPUT | 2026-10-09 | PARTIAL_FIXTURE | 1 | suppressed group | Suppression exists in the fixture but authorization and expiry evidence are absent. | SYN-003 |
| SYN-004 | SYNTHETIC_INPUT | 2026-10-09 | COMPLETE_FIXTURE | 15 | BASE60 below-threshold frame units | Six assigned ranks are selected; design does not establish probability sampling. | SYN-004 |

### ProcessQA

| check_id | check_scope | expected | actual | status | reviewer | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| MT-Q01 | Population conservation | 36 = 29 known + 4 UNKNOWN + 3 CENSORED | 36 = 29 + 4 + 3 | PASS | Fictional checker | SYN-001 |
| MT-Q02 | Partition segregation | 12 units per partition; no group crosses partitions | TRAIN12 VALIDATION12 HOLDOUT12; groups disjoint | PASS | Fictional checker | SYN-001 |
| MT-Q03 | Candidate matrices | Each TP+FP+FN+TN equals known_n | All sixteen matrices reconcile | PASS | Fictional checker | SYN-001;SYN-002 |
| MT-Q04 | Suppression authority | Current authorization plus expiry and coverage evidence | No authorization supplied for G17 | FAIL | Fictional checker | SYN-003 |
| MT-Q05 | Below-threshold frame | 15 frame units; 6 selected; 9 not reviewed | 15 = 6 + 9; selected outcomes P3 N1 U1 C1 | PASS | Fictional checker | SYN-004 |
| MT-Q06 | Holdout authorization | Protected review record and separate human decision | Only an illustrative prefreeze is supplied | REVIEW_REQUIRED | NOT_RECORDED | SYN-002 |

## Complete record-by-record analytical trace

### U01: TRAIN / RETAIL

The raw source supplies score **82**, label **POSITIVE**, dependence group **G01**, and a segment lead-time assumption of **1 hours**. The eligible flag is true. Candidate raw hits are BASE60, HIGH75, LOW50, SEGMENTED; raw nonhits are none. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

This unit contributes one TP to each hitting candidate and one FN to each nonhitting candidate within its own partition. It also contributes one to the common known-positive denominator. A change in its hit state is a coverage change that requires an exact-ID explanation; aggregate precision cannot dispose of that change.

For each hitting candidate, look up all other hit units in this same group and partition. The smallest unit ID leads the case and later IDs become merged children. Charge the lead time once and add 0.25 hours per child. Do not credit an unhit sibling as detected without a separate supplied review-scope rule.

### U02: TRAIN / RETAIL

The raw source supplies score **67**, label **NEGATIVE**, dependence group **G01**, and a segment lead-time assumption of **1 hours**. The eligible flag is true. Candidate raw hits are BASE60, LOW50, SEGMENTED; raw nonhits are HIGH75. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

This unit contributes one FP to each hitting candidate and one TN to each nonhitting candidate within its own partition. The negative label is a supplied fictional review outcome, not proof of harmlessness beyond the defined label rubric. It remains operational workload whenever the predicate hits, even if the expected outcome is negative.

### U03: TRAIN / RETAIL

The raw source supplies score **56**, label **POSITIVE**, dependence group **G02**, and a segment lead-time assumption of **1 hours**. The eligible flag is true. Candidate raw hits are LOW50, SEGMENTED; raw nonhits are BASE60, HIGH75. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

This unit belongs to the complete BASE60 below-threshold frame. Its supplied rank is **1** in a five-unit partition frame; selected is **true** and the recorded draw result is **POSITIVE**. The complete frame retains it whether selected or not. The assigned-rank fixture makes no probability-sampling claim.

### U04: TRAIN / RETAIL

The raw source supplies score **32**, label **NEGATIVE**, dependence group **G02**, and a segment lead-time assumption of **1 hours**. The eligible flag is true. Candidate raw hits are none; raw nonhits are BASE60, HIGH75, LOW50, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

This unit belongs to the complete BASE60 below-threshold frame. Its supplied rank is **3** in a five-unit partition frame; selected is **false** and the recorded draw result is **NOT_REVIEWED**. The complete frame retains it whether selected or not. The assigned-rank fixture makes no probability-sampling claim.

### U05: TRAIN / SMALL_BUSINESS

The raw source supplies score **88**, label **POSITIVE**, dependence group **G03**, and a segment lead-time assumption of **1.5 hours**. The eligible flag is true. Candidate raw hits are BASE60, HIGH75, LOW50, SEGMENTED; raw nonhits are none. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U06: TRAIN / SMALL_BUSINESS

The raw source supplies score **72**, label **NEGATIVE**, dependence group **G03**, and a segment lead-time assumption of **1.5 hours**. The eligible flag is true. Candidate raw hits are BASE60, LOW50, SEGMENTED; raw nonhits are HIGH75. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U07: TRAIN / SMALL_BUSINESS

The raw source supplies score **58**, label **POSITIVE**, dependence group **G04**, and a segment lead-time assumption of **1.5 hours**. The eligible flag is true. Candidate raw hits are LOW50; raw nonhits are BASE60, HIGH75, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

This unit belongs to the complete BASE60 below-threshold frame. Its supplied rank is **2** in a five-unit partition frame; selected is **true** and the recorded draw result is **POSITIVE**. The complete frame retains it whether selected or not. The assigned-rank fixture makes no probability-sampling claim.

### U08: TRAIN / SMALL_BUSINESS

The raw source supplies score **44**, label **UNKNOWN**, dependence group **G04**, and a segment lead-time assumption of **1.5 hours**. The eligible flag is true. Candidate raw hits are none; raw nonhits are BASE60, HIGH75, LOW50, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

The UNKNOWN outcome remains outside TP, FP, FN and TN. The unit still contributes to the full population and any raw-hit, routing and workload counts. Its label basis is: Review evidence unavailable. Do not convert it into a negative to complete the matrix or erase it because a known outcome is unavailable.

This unit belongs to the complete BASE60 below-threshold frame. Its supplied rank is **4** in a five-unit partition frame; selected is **false** and the recorded draw result is **NOT_REVIEWED**. The complete frame retains it whether selected or not. The assigned-rank fixture makes no probability-sampling claim.

### U09: TRAIN / CORRESPONDENT

The raw source supplies score **93**, label **POSITIVE**, dependence group **G05**, and a segment lead-time assumption of **2 hours**. The eligible flag is true. Candidate raw hits are BASE60, HIGH75, LOW50, SEGMENTED; raw nonhits are none. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U10: TRAIN / CORRESPONDENT

The raw source supplies score **77**, label **NEGATIVE**, dependence group **G05**, and a segment lead-time assumption of **2 hours**. The eligible flag is true. Candidate raw hits are BASE60, HIGH75, LOW50, SEGMENTED; raw nonhits are none. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U11: TRAIN / CORRESPONDENT

The raw source supplies score **63**, label **POSITIVE**, dependence group **G06**, and a segment lead-time assumption of **2 hours**. The eligible flag is true. Candidate raw hits are BASE60, LOW50; raw nonhits are HIGH75, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U12: TRAIN / CORRESPONDENT

The raw source supplies score **39**, label **CENSORED**, dependence group **G06**, and a segment lead-time assumption of **2 hours**. The eligible flag is true. Candidate raw hits are none; raw nonhits are BASE60, HIGH75, LOW50, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

The CENSORED outcome remains outside TP, FP, FN and TN. The unit still contributes to the full population and any raw-hit, routing and workload counts. Its label basis is: Outcome window not mature. Do not convert it into a negative to complete the matrix or erase it because a known outcome is unavailable.

This unit belongs to the complete BASE60 below-threshold frame. Its supplied rank is **5** in a five-unit partition frame; selected is **false** and the recorded draw result is **NOT_REVIEWED**. The complete frame retains it whether selected or not. The assigned-rank fixture makes no probability-sampling claim.

### U13: VALIDATION / RETAIL

The raw source supplies score **79**, label **POSITIVE**, dependence group **G07**, and a segment lead-time assumption of **1 hours**. The eligible flag is true. Candidate raw hits are BASE60, HIGH75, LOW50, SEGMENTED; raw nonhits are none. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U14: VALIDATION / RETAIL

The raw source supplies score **64**, label **NEGATIVE**, dependence group **G07**, and a segment lead-time assumption of **1 hours**. The eligible flag is true. Candidate raw hits are BASE60, LOW50, SEGMENTED; raw nonhits are HIGH75. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U15: VALIDATION / RETAIL

The raw source supplies score **54**, label **POSITIVE**, dependence group **G08**, and a segment lead-time assumption of **1 hours**. The eligible flag is true. Candidate raw hits are LOW50; raw nonhits are BASE60, HIGH75, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

This unit belongs to the complete BASE60 below-threshold frame. Its supplied rank is **1** in a five-unit partition frame; selected is **true** and the recorded draw result is **POSITIVE**. The complete frame retains it whether selected or not. The assigned-rank fixture makes no probability-sampling claim.

### U16: VALIDATION / RETAIL

The raw source supplies score **28**, label **NEGATIVE**, dependence group **G08**, and a segment lead-time assumption of **1 hours**. The eligible flag is true. Candidate raw hits are none; raw nonhits are BASE60, HIGH75, LOW50, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U17: VALIDATION / SMALL_BUSINESS

The raw source supplies score **86**, label **POSITIVE**, dependence group **G09**, and a segment lead-time assumption of **1.5 hours**. The eligible flag is true. Candidate raw hits are BASE60, HIGH75, LOW50, SEGMENTED; raw nonhits are none. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U18: VALIDATION / SMALL_BUSINESS

The raw source supplies score **69**, label **NEGATIVE**, dependence group **G09**, and a segment lead-time assumption of **1.5 hours**. The eligible flag is true. Candidate raw hits are BASE60, LOW50, SEGMENTED; raw nonhits are HIGH75. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U19: VALIDATION / SMALL_BUSINESS

The raw source supplies score **57**, label **UNKNOWN**, dependence group **G10**, and a segment lead-time assumption of **1.5 hours**. The eligible flag is true. Candidate raw hits are LOW50; raw nonhits are BASE60, HIGH75, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U20: VALIDATION / SMALL_BUSINESS

The raw source supplies score **42**, label **NEGATIVE**, dependence group **G10**, and a segment lead-time assumption of **1.5 hours**. The eligible flag is true. Candidate raw hits are none; raw nonhits are BASE60, HIGH75, LOW50, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

This unit belongs to the complete BASE60 below-threshold frame. Its supplied rank is **2** in a five-unit partition frame; selected is **true** and the recorded draw result is **NEGATIVE**. The complete frame retains it whether selected or not. The assigned-rank fixture makes no probability-sampling claim.

### U21: VALIDATION / CORRESPONDENT

The raw source supplies score **91**, label **POSITIVE**, dependence group **G11**, and a segment lead-time assumption of **2 hours**. The eligible flag is true. Candidate raw hits are BASE60, HIGH75, LOW50, SEGMENTED; raw nonhits are none. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U22: VALIDATION / CORRESPONDENT

The raw source supplies score **74**, label **NEGATIVE**, dependence group **G11**, and a segment lead-time assumption of **2 hours**. The eligible flag is true. Candidate raw hits are BASE60, LOW50, SEGMENTED; raw nonhits are HIGH75. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U23: VALIDATION / CORRESPONDENT

The raw source supplies score **61**, label **POSITIVE**, dependence group **G12**, and a segment lead-time assumption of **2 hours**. The eligible flag is true. Candidate raw hits are BASE60, LOW50; raw nonhits are HIGH75, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U24: VALIDATION / CORRESPONDENT

The raw source supplies score **36**, label **CENSORED**, dependence group **G12**, and a segment lead-time assumption of **2 hours**. The eligible flag is true. Candidate raw hits are none; raw nonhits are BASE60, HIGH75, LOW50, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U25: HOLDOUT / RETAIL

The raw source supplies score **81**, label **POSITIVE**, dependence group **G13**, and a segment lead-time assumption of **1 hours**. The eligible flag is true. Candidate raw hits are BASE60, HIGH75, LOW50, SEGMENTED; raw nonhits are none. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U26: HOLDOUT / RETAIL

The raw source supplies score **66**, label **NEGATIVE**, dependence group **G13**, and a segment lead-time assumption of **1 hours**. The eligible flag is true. Candidate raw hits are BASE60, LOW50, SEGMENTED; raw nonhits are HIGH75. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U27: HOLDOUT / RETAIL

The raw source supplies score **53**, label **POSITIVE**, dependence group **G14**, and a segment lead-time assumption of **1 hours**. The eligible flag is true. Candidate raw hits are LOW50; raw nonhits are BASE60, HIGH75, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U28: HOLDOUT / RETAIL

The raw source supplies score **31**, label **UNKNOWN**, dependence group **G14**, and a segment lead-time assumption of **1 hours**. The eligible flag is true. Candidate raw hits are none; raw nonhits are BASE60, HIGH75, LOW50, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

This unit belongs to the complete BASE60 below-threshold frame. Its supplied rank is **1** in a five-unit partition frame; selected is **true** and the recorded draw result is **UNKNOWN**. The complete frame retains it whether selected or not. The assigned-rank fixture makes no probability-sampling claim.

### U29: HOLDOUT / SMALL_BUSINESS

The raw source supplies score **84**, label **POSITIVE**, dependence group **G15**, and a segment lead-time assumption of **1.5 hours**. The eligible flag is true. Candidate raw hits are BASE60, HIGH75, LOW50, SEGMENTED; raw nonhits are none. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U30: HOLDOUT / SMALL_BUSINESS

The raw source supplies score **71**, label **NEGATIVE**, dependence group **G15**, and a segment lead-time assumption of **1.5 hours**. The eligible flag is true. Candidate raw hits are BASE60, LOW50, SEGMENTED; raw nonhits are HIGH75. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U31: HOLDOUT / SMALL_BUSINESS

The raw source supplies score **59**, label **POSITIVE**, dependence group **G16**, and a segment lead-time assumption of **1.5 hours**. The eligible flag is true. Candidate raw hits are LOW50; raw nonhits are BASE60, HIGH75, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U32: HOLDOUT / SMALL_BUSINESS

The raw source supplies score **41**, label **NEGATIVE**, dependence group **G16**, and a segment lead-time assumption of **1.5 hours**. The eligible flag is true. Candidate raw hits are none; raw nonhits are BASE60, HIGH75, LOW50, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U33: HOLDOUT / CORRESPONDENT

The raw source supplies score **94**, label **POSITIVE**, dependence group **G17**, and a segment lead-time assumption of **2 hours**. The eligible flag is true. Candidate raw hits are BASE60, HIGH75, LOW50, SEGMENTED; raw nonhits are none. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

G17 suppression removes this raw hit from every candidate queue. Keep the raw predicate result and the suppressed route together. No case is created, no lead or child time is charged, and no retained-positive credit is allowed. The missing authorization is a routing deficiency, not a reason to change the raw score or label.

### U34: HOLDOUT / CORRESPONDENT

The raw source supplies score **76**, label **NEGATIVE**, dependence group **G17**, and a segment lead-time assumption of **2 hours**. The eligible flag is true. Candidate raw hits are BASE60, HIGH75, LOW50, SEGMENTED; raw nonhits are none. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

G17 suppression removes this raw hit from every candidate queue. Keep the raw predicate result and the suppressed route together. No case is created, no lead or child time is charged, and no retained-positive credit is allowed. The missing authorization is a routing deficiency, not a reason to change the raw score or label.

### U35: HOLDOUT / CORRESPONDENT

The raw source supplies score **62**, label **UNKNOWN**, dependence group **G18**, and a segment lead-time assumption of **2 hours**. The eligible flag is true. Candidate raw hits are BASE60, LOW50; raw nonhits are HIGH75, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

### U36: HOLDOUT / CORRESPONDENT

The raw source supplies score **37**, label **CENSORED**, dependence group **G18**, and a segment lead-time assumption of **2 hours**. The eligible flag is true. Candidate raw hits are none; raw nonhits are BASE60, HIGH75, LOW50, SEGMENTED. These outcomes follow the inclusive segment cutoffs and do not depend on the label.

This unit belongs to the complete BASE60 below-threshold frame. Its supplied rank is **2** in a five-unit partition frame; selected is **true** and the recorded draw result is **CENSORED**. The complete frame retains it whether selected or not. The assigned-rank fixture makes no probability-sampling claim.

## Complete finding narratives and next decisions

### MT-F01: Suppression removes a known positive from every candidate

Severity: **HIGH**. Confidence in the fictional observation: **HIGH**. Evidence class: **Observed**. Evidence: SYN-001, SYN-003.

G17 contains HOLDOUT U33 POSITIVE and U34 NEGATIVE. U33 is a raw hit under all four candidates, but the suppressed group reaches no queued case. The supplied record contains no valid suppression authorization.

Proposed action: Keep routing assurance blocked; obtain scope, reason, expiry, approver and covered-activity evidence, then replay all candidates.

The observation is bounded by the supplied fixture. It does not establish the prevalence of this issue in a live population or the legality of a particular institution's practice. A reviewer should challenge the affected IDs, exact calculation and possible alternative explanation, then record a separate human disposition if actual authority and evidence are supplied. No owner acceptance, operational execution or final signoff is represented here.

### MT-F02: Lowest threshold increases raw known coverage and workload

Severity: **HIGH**. Confidence in the fictional observation: **HIGH**. Evidence class: **Observed**. Evidence: SYN-001, SYN-002, SYN-003.

LOW50 has 16/16 known positive raw hits and 27 workload hours against an illustrative 15-hour combined capacity. Retained known positive hits are 15/16 after suppression.

Proposed action: Further validate labels and segment behavior, repair routing and assess staffing; do not deploy from the synthetic result.

### MT-F03: Unknown and censored labels limit population performance claims

Severity: **HIGH**. Confidence in the fictional observation: **HIGH**. Evidence class: **Observed**. Evidence: SYN-001, SYN-004.

Twenty-nine of thirty-six units have known labels. Four UNKNOWN and three CENSORED units remain outside confusion matrices, including both hit and nonhit records.

Proposed action: Preserve unavailable labels, obtain independent review and assess outcome maturity before any population recall inference.

### MT-F04: Segmented cutoffs lose correspondent known positives

Severity: **MEDIUM**. Confidence in the fictional observation: **HIGH**. Evidence class: **Observed**. Evidence: SYN-001, SYN-002.

SEGMENTED moves the correspondent cutoff to 65. TRAIN U11 score 63 and VALIDATION U23 score 61 are known positives caught by BASE60 and missed by SEGMENTED. RETAIL U03 score 56 is gained, so the combined result hides opposite segment effects.

Proposed action: Retain incremental unit IDs and require explicit segment challenge; aggregate workload cannot resolve the coverage tradeoff.

## Boundary variations and expected interpretation

### Variation 01: Equality at 60

Change only this input: Add an otherwise known-negative eligible unit with score 60 in RETAIL and a new group.

Expected result: BASE60 hit=true;HIGH75=false;LOW50=true;SEGMENTED=true. Each hitting candidate gains one FP and one raw hit.

Required narrative: The inclusive boundary is tested without changing a source record or relying on rounded display. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 02: Just below 60

Change only this input: Use 59.999 rather than 60 on the same isolated negative unit.

Expected result: BASE60=false;HIGH75=false;LOW50=true;SEGMENTED=true. BASE60 must not gain an alert.

Required narrative: Numerical presentation and analytical comparison use different stages. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 03: Unknown high score

Change only this input: Change U35 label from UNKNOWN to NEGATIVE without changing its score 62.

Expected result: BASE60 and LOW50 gain one FP; known_n 30; unknown_n 6. Raw hits, routing and workload stay unchanged.

Required narrative: Changing labels affects outcome matrices but does not change detection or workload inputs. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 04: Unknown positive below threshold

Change only this input: Change U28 from UNKNOWN to POSITIVE with score 31 unchanged.

Expected result: All candidates gain one FN; known positives 17. No candidate gains a hit or workload.

Required narrative: Outcome maturation can worsen measured recall without any change in the threshold engine. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 05: Censored becomes positive

Change only this input: Change U36 label from CENSORED to POSITIVE at a later explicitly named cutoff.

Expected result: All candidates gain one FN; the earlier cutoff remains preserved. Selected below-threshold known positives rise from 3 to 4.

Required narrative: Do not backfill a matured outcome into an earlier protected result without versioning. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 06: Remove suppression

Change only this input: Remove G17 from the suppression list with all raw inputs fixed.

Expected result: Every candidate gains 2 retained hits,1 queued case,2.25 hours and 1 retained known positive; raw matrices unchanged.

Required narrative: Routing correction is distinct from threshold performance. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 07: Suppress a nonhit group

Change only this input: Add G18 to suppression while testing BASE60.

Expected result: U35 is the only BASE60 hit in G18; retained hits decrease 1, queued cases decrease 1 and hours decrease 2.0; raw matrix unchanged.

Required narrative: The same group may have a different hit composition under another candidate. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 08: Remove a merged negative

Change only this input: Exclude U02 from the population with an explicit changed-scope record.

Expected result: For BASE60, FP decreases 1, raw and retained hits decrease 1;G01 remains a case and workload falls 0.25 hours.

Required narrative: Removing a child saves only incremental merge time, not the full lead cost. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 09: Remove a merged lead

Change only this input: Exclude U01 while leaving U02.

Expected result: For BASE60 TP decreases 1 and U02 becomes G01 lead; case count unchanged and workload falls 0.25 hours.

Required narrative: Lead reassignment prevents falsely claiming a full case reduction. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 10: All negative labels

Change only this input: Relabel all known positive units NEGATIVE solely in an isolated mathematical test.

Expected result: All candidate recalls=null becauseTP+FN=0; precision remains calculable where known hits exist.

Required narrative: No positive denominator means recall is undefined, not perfect. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 11: No known hits

Change only this input: Evaluate a 999 threshold on the existing frame.

Expected result: Raw hits 0;TP0 FP0 FN16 TN13; precision=null;recall 0/16=0.0%;queue 0;hours 0.

Required narrative: A zero queue is not success when known positives remain below the threshold. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 12: One unknown hit only

Change only this input: Use an explicit isolated candidate that selects U35 and no other unit.

Expected result: Raw hits 1;known TP0 FP0;precision=null;unknown-hit count 1;queue 1 and 2.0 hours unless G18 suppressed.

Required narrative: Workload can exist without a known-label precision denominator. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 13: Group crosses partitions

Change only this input: Change U02 partition to HOLDOUT while G01 remains shared with U01.

Expected result: Partition-integrity check fails; protected-performance interpretation is blocked pending regrouping.

Required narrative: A uniqueunitID does not establish independent evaluation. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 14: Overlapping candidate definitions

Change only this input: Change LOW50 score definition while retaining its name.

Expected result: Treat the change as a new configuration with a distinct version; pure-threshold comparison no longer holds.

Required narrative: Candidate names are not evidence that features and eligibility match. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 15: Capacity rises

Change only this input: Keep LOW50 inputs fixed and change illustrative capacity from 15 to 30 hours.

Expected result: The capacity comparison changes from 27>15 to 27<=30; missing labels and G17 routing restrictions remain.

Required narrative: Staffing assumptions resolve only capacity, not all deployment gates. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 16: Lead review time doubles

Change only this input: Double all segment lead times while retaining the 0.25-hour child increment.

Expected result: Recompute group costs; do not simply double total hours because merge increments remain fixed.

Required narrative: Lead and incremental workload components must stay separate. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 17: Selected review result unavailable

Change only this input: Remove the U20 review result while retaining its selected flag.

Expected result: Selected count remains 6; known selected results fall from 4 to 3; positive count remains 3 and unavailable results increase.

Required narrative: An unavailable result does not erase a selected unit from the denominator. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 18: Holdout reused

Change only this input: Add a fifth threshold chosen after seeing HOLDOUT labels.

Expected result: The earlier holdout becomes descriptive reuse; it is not independent evidence for the fifth candidate.

Required narrative: Further searching requires fresh protected evidence or an explicitly qualified design. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

## Separate statistical demonstrations with explicit assumptions

These demonstrations do not estimate the performance of the constructed 36-unit case. For a separate set of 10 independent Bernoulli trials with 3 observed successes, a two-sided 95%Wilson interval uses z=1.959963984540054, p=0.3, denominator 1+z²/n, center(p+z²/(2 n))/denominator, and half-width z×sqrt(p(1-p)/n+z²/(4 n²))/denominator. The result is approximately 10.78%to 60.32%. This requires an appropriate independent-trial interpretation; it cannot repair purposive selection or unknown outcomes in the tuning fixture.

For a separate finite frame of 20 units, a simple random sample without replacement of 5 units and zero observed defects, the probability of observing zero when the frame containsD defects is choose(20-D,5)/choose(20,5). AtD=8 that probability is 792/15504, approximately 5.11%; atD=9 it is 462/15504, approximately 2.98%. An upper bound defined by retaining integerD values whose zero-observation probability is at least 5%is 8 defects, or 40%of that finite frame. This is not the rule-of-three approximation and not an estimate for the 15-unit assigned-rank frame. The sampling design and complete defect ascertainment are required premises.

A percentage confidence label must specify the estimand and construction. It is not a probability that the unknown fixed population value lies in a particular realized interval under a frequentist interpretation. When labels are incomplete, add an explicit missing-outcome sensitivity analysis instead of treating unresolved records as failures or successes without explanation. When related windows are clustered, use a design that respects the clusters rather than pretending every window adds an independent trial.

## Embedded independent fixture check

The following complete standard-library Python block is optional in-session verification. It has no repository, file, network or installation dependency. It starts from the raw fixture declarations, derives results and checks independent expected ID sets, counts and boundary values. If execution is unavailable, reperform the printed equations and mark the executable check NOT_TESTED. Passing this block establishes the stated fixture relationships only.

<!-- FIXTURE_CHECK:START -->
```python
# Pure Python; no repository, files, packages or network required.
from collections import Counter
from math import comb, sqrt
RAW = [('TRAIN', 'RETAIL', [82, 67, 56, 32], ['POSITIVE', 'NEGATIVE', 'POSITIVE', 'NEGATIVE']), ('TRAIN', 'SMALL_BUSINESS', [88, 72, 58, 44], ['POSITIVE', 'NEGATIVE', 'POSITIVE', 'UNKNOWN']), ('TRAIN', 'CORRESPONDENT', [93, 77, 63, 39], ['POSITIVE', 'NEGATIVE', 'POSITIVE', 'CENSORED']), ('VALIDATION', 'RETAIL', [79, 64, 54, 28], ['POSITIVE', 'NEGATIVE', 'POSITIVE', 'NEGATIVE']), ('VALIDATION', 'SMALL_BUSINESS', [86, 69, 57, 42], ['POSITIVE', 'NEGATIVE', 'UNKNOWN', 'NEGATIVE']), ('VALIDATION', 'CORRESPONDENT', [91, 74, 61, 36], ['POSITIVE', 'NEGATIVE', 'POSITIVE', 'CENSORED']), ('HOLDOUT', 'RETAIL', [81, 66, 53, 31], ['POSITIVE', 'NEGATIVE', 'POSITIVE', 'UNKNOWN']), ('HOLDOUT', 'SMALL_BUSINESS', [84, 71, 59, 41], ['POSITIVE', 'NEGATIVE', 'POSITIVE', 'NEGATIVE']), ('HOLDOUT', 'CORRESPONDENT', [94, 76, 62, 37], ['POSITIVE', 'NEGATIVE', 'UNKNOWN', 'CENSORED'])]
CANDIDATES = [('BASE60', 60, 60, 60), ('HIGH75', 75, 75, 75), ('LOW50', 50, 50, 50), ('SEGMENTED', 55, 60, 65)]
units = []
for block, (partition, segment, scores, labels) in enumerate(RAW):
    for j, (score, label) in enumerate(zip(scores, labels)):
        uid = f"U{block * 4 + j + 1:02}"
        group = f"G{block * 2 + j // 2 + 1:02}"
        units.append(dict(unit_id=uid, group_id=group, partition=partition,
            segment=segment, score=score, label=label, eligible=True,
            suppressed=group == "G17", review_hours={"RETAIL":1,
            "SMALL_BUSINESS":1.5,"CORRESPONDENT":2}[segment],
            evidence_ids="SYN-001"))
def hit(unit, candidate):
    index = ["RETAIL","SMALL_BUSINESS","CORRESPONDENT"].index(unit["segment"])
    return unit["eligible"] and unit["score"] >= candidate[index + 1]
def metrics(candidate, partition, source=units):
    selected = [u for u in source if partition == "ALL" or u["partition"] == partition]
    known = [u for u in selected if u["label"] in ("POSITIVE","NEGATIVE")]
    raw_hits = [u for u in selected if hit(u,candidate)]
    retained = [u for u in raw_hits if not u["suppressed"]]
    groups = sorted({u["group_id"] for u in retained})
    tp = sum(hit(u,candidate) and u["label"] == "POSITIVE" for u in known)
    fp = sum(hit(u,candidate) and u["label"] == "NEGATIVE" for u in known)
    fn = sum(not hit(u,candidate) and u["label"] == "POSITIVE" for u in known)
    tn = sum(not hit(u,candidate) and u["label"] == "NEGATIVE" for u in known)
    hours = 0
    for group in groups:
        members = [u for u in retained if u["group_id"] == group]
        hours += members[0]["review_hours"] + .25 * (len(members)-1)
    kept_positive = sum(u["label"] == "POSITIVE" for u in retained)
    return [candidate[0],partition,len(selected),len(known),tp,fp,fn,tn,
        len(selected)-len(known),len(raw_hits),len(retained),len(groups),hours,
        tp/(tp+fp) if tp+fp else None,tp/(tp+fn) if tp+fn else None,kept_positive]
rows = [metrics(c,p) for c in CANDIDATES for p in ("TRAIN","VALIDATION","HOLDOUT","ALL")]
expected_all = {
    "BASE60":(11,9,5,4,21,19,11,19.5,10),
    "HIGH75":(9,2,7,11,11,9,8,11.75,8),
    "LOW50":(16,9,0,4,27,25,17,27.0,15),
    "SEGMENTED":(10,9,6,4,19,17,9,14.5,9)}
for row in rows:
    assert sum(row[4:8]) == row[3]
    assert row[2] == row[3] + row[8]
    if row[1] == "ALL":
        assert tuple(row[4:8]+row[9:13]+[row[15]]) == expected_all[row[0]]
assert Counter(u["label"] for u in units) == {"POSITIVE":16,"NEGATIVE":13,"UNKNOWN":4,"CENSORED":3}
assert all(len({u["partition"] for u in units if u["group_id"] == g}) == 1 for g in {u["group_id"] for u in units})
routing = []
for candidate in CANDIDATES:
    hits = [u for u in units if hit(u,candidate)]
    for u in hits:
        members = sorted(x["unit_id"] for x in hits if x["group_id"] == u["group_id"])
        state = "SUPPRESSED" if u["suppressed"] else "QUEUED_LEAD" if u["unit_id"] == members[0] else "MERGED_CHILD"
        routing.append([candidate[0]+"-"+u["unit_id"],candidate[0],u["unit_id"],u["group_id"],state,
            None if u["suppressed"] else candidate[0]+"-"+u["group_id"],
            None if u["suppressed"] else members[0],
            "Unexpired authorization absent" if u["suppressed"] else "Same frozen group and partition",
            "SYN-001;SYN-003"])
assert len(routing) == 78
selection = {"TRAIN":["U03","U07"],"VALIDATION":["U15","U20"],"HOLDOUT":["U28","U36"]}
draws = []
for partition in selection:
    frame = [u for u in units if u["partition"] == partition and not hit(u,CANDIDATES[0])]
    assert len(frame) == 5
    order = selection[partition]+[u["unit_id"] for u in frame if u["unit_id"] not in selection[partition]]
    for u in frame:
        selected = u["unit_id"] in selection[partition]
        draws.append(["BTL-"+u["unit_id"],u["unit_id"],partition,5,order.index(u["unit_id"])+1,
            selected,u["label"] if selected else "NOT_REVIEWED","ILLUSTRATIVE_RANK","SYN-004"])
assert len(draws)==15 and sum(r[5] for r in draws)==6
assert Counter(r[6] for r in draws if r[5]) == {"POSITIVE":3,"NEGATIVE":1,"UNKNOWN":1,"CENSORED":1}
# Independent boundary and routing mutations.
probe = dict(units[0],score=60)
assert hit(probe,CANDIDATES[0]) and not hit(probe,CANDIDATES[1])
probe["score"] = 59.999
assert not hit(probe,CANDIDATES[0])
unblocked = [dict(u,suppressed=False) for u in units]
for c in CANDIDATES:
    before, after = metrics(c,"ALL"), metrics(c,"ALL",unblocked)
    assert before[4:8] == after[4:8]
    assert after[10]-before[10]==2 and after[11]-before[11]==1
    assert after[12]-before[12]==2.25 and after[15]-before[15]==1
negative_only = [dict(u,label="NEGATIVE") if u["label"] in ("POSITIVE","NEGATIVE") else dict(u) for u in units]
assert metrics(CANDIDATES[0],"ALL",negative_only)[14] is None
assert metrics(("NONE",999,999,999),"ALL")[13] is None
# Separate mathematical illustrations, not inferences about the designed fixture.
n,x,z=10,3,1.959963984540054
p=x/n; denominator=1+z*z/n
center=(p+z*z/(2*n))/denominator
half=z*sqrt(p*(1-p)/n+z*z/(4*n*n))/denominator
assert round(center-half,4)==0.1078 and round(center+half,4)==0.6032
N,n=20,5
possible=[D for D in range(N+1) if (comb(N-D,n) if N-D>=n else 0)/comb(N,n)>=.05]
assert max(possible)==8
CHECKED_TABLES={"CandidateMetrics":rows,"AlertRouting":routing,"BelowThreshold":draws}
print("Monitoring tuning fixture: matrices, routing, full draw frame and boundary checks passed.")
```
<!-- FIXTURE_CHECK:END -->

## Completed analytical recommendation

LOW50 is a further-validation candidate only. Its known-label raw coverage improves, but G17 suppression removes a known positive, missing outcomes prevent population effectiveness claims, and illustrative workload exceeds capacity. No candidate is authorized for deployment.

**Candidate recommendation and restrictions.** LOW50 is a further-validation candidate only. Its known-label raw coverage improves, but G17 suppression removes a known positive, missing outcomes prevent population effectiveness claims, and illustrative workload exceeds capacity. No candidate is authorized for deployment.

**Evaluation scope and partition controls.** The 36 fictional units form three disjoint partitions of twelve. Three segments each contain four units per partition. Group pairs never cross partitions. Scores and four candidates are predeclared; the ALL row is descriptive reconciliation rather than an independent evaluation set.

**Coverage workload and routing findings.** Raw predicate results, suppression, merged case counts and workload are separate stages. Group G17 suppresses HOLDOUT U33 and U34. A case merge does not automatically credit unhit siblings as detected. The raw and retained positive-unit numerators remain separate.

**Complete candidate and population registers.** ALL BASE60 TP11 FP9 FN5 TN4; HIGH75 TP9 FP2 FN7 TN11; LOW50 TP16 FP9 FN0 TN4; SEGMENTED TP10 FP9 FN6 TN4. Each matrix has 29 known labels, with seven other units retained outside the matrix.

**Below-threshold review and decision gates.** The complete BASE60 below-threshold frame has fifteen units. Six assigned-rank selections contain three POSITIVE, one NEGATIVE, one UNKNOWN and one CENSORED outcome. Nine frame units remain unreviewed by this draw. The illustrative ranks do not support a random-sample confidence interval.

**Evidence provenance uncertainty and blind spots.** The source ledger preserves 36 units, four candidates, one suppression group with incomplete authority, and fifteen below-threshold frame records. Public guidance provides governance context. It does not establish a legal cutoff, a live model classification or approval to suppress activity.

**Validation and change proposals.** Proposed work is to establish suppression authority or revise routing, label unavailable outcomes without leakage, validate incremental segment losses, and test capacity on protected data. The human deployment disposition remains NOT_RECORDED.

**Limitations quality review and human disposition.** Reperform all candidate matrices and the conservation equations. Validate exact threshold boundaries, merge groups, null rates and missing labels. Passing the fictional checks establishes consistency of this example only; it cannot validate live detection effectiveness.

## Next-session change control

When new evidence arrives, preserve this specimen or the prior real-case version, assign the new source its own ID and cutoff, and identify the affected methods and tables. Recalculate the complete relevant denominator rather than editing one favorable headline. Update the finding, action, limitation and human-decision records together. A resolved arithmetic issue does not automatically resolve evidence, concept or authorization gates, and a new source can create additional review work even while it improves retrieval coverage.
