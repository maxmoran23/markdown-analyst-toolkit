# Quality review — Monitoring Scenario and Threshold Review

## Review sequence and release gate

Review in this order: source completeness, population reconciliation, method and parameter application, independent arithmetic, evidence support, decision restraint, cross-artifact consistency, and presentation. A polished output cannot compensate for a failed earlier gate. Mark each check PASS, FAIL, NOT TESTED, or NOT APPLICABLE, with evidence and a reason. NOT TESTED is not equivalent to PASS. A second pass by the same assistant can challenge its reasoning but does not establish organizational independence.

Reperform at least one ordinary case, one adverse case, one boundary case, and one missing-data case directly from original inputs. For larger datasets, select cases before reading their conclusions and include a sample from records reported as passing. Testing only known failures cannot assess false reassurance. Show the selected IDs and why they cover the relevant branches. If the session cannot execute a calculation, use visible arithmetic and disclose that broader computational validation was not performed.

Check that every finding cites an accessible source location and that every recommendation follows from the stated issue. Remove conclusions that exceed the source population or period. Challenge the strongest conclusion with the most plausible alternative explanation; identify the evidence that would distinguish the explanations. Do not use a generic limitations paragraph to excuse an unsupported headline.

A human reviewer records approval, approval with conditions, return for revision, or unable to conclude. The AI leaves that field Pending human review. An approved draft report is distinct from authorization to deploy, file, close, block, change a policy, or attest to regulatory compliance. If a critical gate fails, provide the completed work with a prominent restriction and a specific recovery step; do not call the whole package final or verified.

For each delivered artifact state: created or supplied as text; opened or not opened; calculations checked or unchecked; interactive features tested or untested. Preserve unresolved defects in the QA tab and report. Do not claim a browser test, file inspection, source refresh, sample selection, or reviewer sign-off that did not occur.


## Domain falsification tests

| Challenge | Expected output |
| --- | --- |
| Treat U07 and U08 as negatives | Reject invented labels; preserve UNKNOWN |
| Recalculate BASE60 with strict greater-than | Fail comparator check because U04 should alert |
| Calculate recall only among alerts | Reject denominator; include nonalerted positives |
| Use labels defined by score threshold | Flag circular performance assessment |
| Move same customer windows into train and holdout | Flag possible dependency leakage |
| Describe LOW50 as100% population recall | Reject; only three known positives captured |
| Recommend HIGH75 solely for lower volume | Show lost U03 and require coverage review |
| Divide total alerts by six labelled rows | Reject mixed denominators |
| Set precision to zero when there are no alerts | Use null for undefined denominator |

Reperform all three confusion matrices from scores, not from the already-computed candidate table. Confirm labelled count 6, known positives3, known negatives3, unknown count 2, complete population 8. Confirm BASE60 total alerts5 versus labelled alerts4; HIGH75 total 3 versus labelled2; LOW50 total 6 versus labelled5.

Check both percentage-point and relative-volume language. BASE60 to HIGH75 changes total alerts from 5 to 3, a 40.0% relative reduction. Labelled recall drops from 66.7% to 33.3%, a 33.3 percentage-point reduction based on exact fractions, not “33.3% fewer positives.” One of the two previously detected known positives is lost. Round only for display.

A reviewer should explicitly reject a claim of live validation based on the fixture. The maximum supported verification is that the arithmetic and specified predicates reproduce the expected fictional results.
