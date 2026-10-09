# Decision rules — Monitoring Scenario and Threshold Review

## Ordered recommendation gates

| Gate | Condition | Recommendation status | Required response |
| --- | --- | --- | --- |
| 1 | Missing scope, score meaning, or critical input | Unable to assess | Resolve data contract |
| 2 | Circular labels or alert-only sample | Exploratory only | Limit claims and obtain broader independent review |
| 3 | No protected evaluation or holdout | Candidate for further testing | Do not claim independent validation |
| 4 | Known positive lost relative to baseline | Explicit coverage challenge | Explain cases and obtain risk review |
| 5 | Workload exceeds capacity assumption | Operational constraint unresolved | Evaluate alternatives and assumptions |
| 6 | Candidate performs acceptably on bounded evidence | Further validation supported | Lock configuration and design holdout |
| 7 | Human validation and change approvals absent | No production authority | Keep proposed action pending |

No numeric cutoff in this suite is a legal definition of suspicion, a filing threshold, or an approved production setting. BASE60, HIGH75, LOW50, and capacity five are demonstration values. Their labels identify comparable configurations, not maturity levels.

## Selecting among alternatives

Reject a workload-only recommendation when it loses known positive cases without a defensible, documented risk assessment. Support further investigation of a candidate that improves labelled coverage if the added workload and blind spots remain explicit. Retain the current comparison baseline as a reference point, but do not interpret “retain baseline” as a new endorsement of its effectiveness.

If candidate performance is indistinguishable on a small sample, prefer the simpler interpretation and collect evidence rather than asserting a winner. If a candidate is superior on one subgroup and worse on another, present both; a global average cannot resolve policy trade-offs automatically. If a threshold lies near a concentrated score cluster, small changes can produce large volume shifts; include a local sensitivity analysis.

## Outcome labels and decisions

| Input or observation | Permitted conclusion | Prohibited shortcut |
| --- | --- | --- |
| Label POSITIVE under review rubric | Target pattern present in reviewed unit | Crime proven |
| Label NEGATIVE after bounded review | Defined target not substantiated in that review | Customer permanently low risk |
| Label UNKNOWN | Performance contribution unresolved | Treat as TN |
| Known positive does not alert | False negative under declared rubric | Automatically file a report |
| All synthetic positives alert | Fixture branches captured | Real-world false negatives impossible |
| Candidate reduces alerts | Workload difference observed or estimated | Safe suppression established |

## Human change package

A proposed change includes configuration version, purpose, population, data dependencies, development history, validation evidence, below-threshold review, capacity analysis, unresolved limitations, implementation owner, staged verification, monitoring plan, and rollback criteria. The owner decides whether the evidence is adequate. The assistant may draft the package and identify gaps; it does not deploy settings, close alerts, make a final filing decision, or claim regulator acceptance.

Severity reflects the potential consequence of the observed issue. A lost known positive or material unknown-label gap can be HIGH even when workload improves. A capacity exceedance can be MEDIUM or HIGH depending on consequence; the fixture uses MEDIUM because capacity is an illustrative assumption. Confidence is HIGH in the arithmetic of visible rows, but future performance is NOT ASSESSABLE from this fixture alone. Do not let confidence in calculation become confidence in generalization.
