# Quality review — Data Quality and Fitness for Use

## Review sequence and release gate

Review in this order: source completeness, population reconciliation, method and parameter application, independent arithmetic, evidence support, decision restraint, cross-artifact consistency, and presentation. A polished output cannot compensate for a failed earlier gate. Mark each check PASS, FAIL, NOT TESTED, or NOT APPLICABLE, with evidence and a reason. NOT TESTED is not equivalent to PASS. A second pass by the same assistant can challenge its reasoning but does not establish organizational independence.

Reperform at least one ordinary case, one adverse case, one boundary case, and one missing-data case directly from original inputs. For larger datasets, select cases before reading their conclusions and include a sample from records reported as passing. Testing only known failures cannot assess false reassurance. Show the selected IDs and why they cover the relevant branches. If the session cannot execute a calculation, use visible arithmetic and disclose that broader computational validation was not performed.

Check that every finding cites an accessible source location and that every recommendation follows from the stated issue. Remove conclusions that exceed the source population or period. Challenge the strongest conclusion with the most plausible alternative explanation; identify the evidence that would distinguish the explanations. Do not use a generic limitations paragraph to excuse an unsupported headline.

A human reviewer records approval, approval with conditions, return for revision, or unable to conclude. The AI leaves that field Pending human review. An approved draft report is distinct from authorization to deploy, file, close, block, change a policy, or attest to regulatory compliance. If a critical gate fails, provide the completed work with a prominent restriction and a specific recovery step; do not call the whole package final or verified.

For each delivered artifact state: created or supplied as text; opened or not opened; calculations checked or unchecked; interactive features tested or untested. Preserve unresolved defects in the QA tab and report. Do not claim a browser test, file inspection, source refresh, sample selection, or reviewer sign-off that did not occur.


## Domain negative controls

| Challenge | Expected behavior |
| --- | --- |
| Add one hundred passing low-risk checks | Critical restriction remains |
| Count D02 twice in affected-row total | Reject; use distinct union of record IDs |
| Treat ENTITY blank birth date as failure | Reject; DQ03 eligibility is individuals only |
| Accept 1990-02-30 because the format matches | Reject after calendar parsing |
| Remove D06 before reporting duplicates | Reject silent denominator improvement |
| Use one duplicate group as two excess rows | Correct to one group, two affected rows, one excess |
| Mark an unrun reference check as passing | Record UNABLE TO ASSESS |
| Interpret a passing format as verified real-world identity | Restrict claim to checked predicate |
| Treat a corrected output as proof source was repaired | Require source and next-extract evidence |

Recompute each rule from the complete six-row fixture. Confirm eligible checks 6+6+5+6+6=29 and failures1+1+1+2+1=6. Confirm passing checks23. Confirm critical affected IDs D02,D03,D05,D06 and no double counting. A check-pass rate of 79.3% cannot override four critical affected rows.

For fresh datasets, test a zero-row population, zero eligible subgroup, unknown entity type, future date, repeated source row, distinct legitimate accounts under one customer, and an unreadable batch. The test need not invent a result for an unsupported branch: an explicit unassessable state is the expected safeguard. Review whether proposed normalization would destroy information needed to distinguish genuine duplicates from legitimate relationships.
