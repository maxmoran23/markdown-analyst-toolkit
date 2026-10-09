# Quality review — Control Testing and Evidence Review

## Review sequence and release gate

Review in this order: source completeness, population reconciliation, method and parameter application, independent arithmetic, evidence support, decision restraint, cross-artifact consistency, and presentation. A polished output cannot compensate for a failed earlier gate. Mark each check PASS, FAIL, NOT TESTED, or NOT APPLICABLE, with evidence and a reason. NOT TESTED is not equivalent to PASS. A second pass by the same assistant can challenge its reasoning but does not establish organizational independence.

Reperform at least one ordinary case, one adverse case, one boundary case, and one missing-data case directly from original inputs. For larger datasets, select cases before reading their conclusions and include a sample from records reported as passing. Testing only known failures cannot assess false reassurance. Show the selected IDs and why they cover the relevant branches. If the session cannot execute a calculation, use visible arithmetic and disclose that broader computational validation was not performed.

Check that every finding cites an accessible source location and that every recommendation follows from the stated issue. Remove conclusions that exceed the source population or period. Challenge the strongest conclusion with the most plausible alternative explanation; identify the evidence that would distinguish the explanations. Do not use a generic limitations paragraph to excuse an unsupported headline.

A human reviewer records approval, approval with conditions, return for revision, or unable to conclude. The AI leaves that field Pending human review. An approved draft report is distinct from authorization to deploy, file, close, block, change a policy, or attest to regulatory compliance. If a critical gate fails, provide the completed work with a prominent restriction and a specific recovery step; do not call the whole package final or verified.

For each delivered artifact state: created or supplied as text; opened or not opened; calculations checked or unchecked; interactive features tested or untested. Preserve unresolved defects in the QA tab and report. Do not claim a browser test, file inspection, source refresh, sample selection, or reviewer sign-off that did not occur.


## Domain challenge tests

| Test | Deliberate challenge | Expected result |
| --- | --- | --- |
| CT-Q01 | Remove R06 execution evidence | UNABLE TO CONCLUDE remains in denominator |
| CT-Q02 | Label R03 out of scope after seeing lateness | Reject exclusion without original scope basis |
| CT-Q03 | Count two failed attributes on R03 twice | Reject instance-count inflation |
| CT-Q04 | Present five selected records as full population | Reconcile against eight and fail coverage claim |
| CT-Q05 | Treat preparer and reviewer role as the same | C03 design gap remains visible |
| CT-Q06 | Show zero sample errors as proof of no population errors | Reject unsupported inference |
| CT-Q07 | Supply a passing replacement for R06 | Preserve original missing record and separate supplement |
| CT-Q08 | Correct R03 after period end | Retain original period failure; record subsequent repair separately |

The reviewer should reproduce 5 = 2 + 2 + 1, selection coverage 5/8 = 62.5%, and confirmed sample deviations 2/5 = 40.0%. The conclusive-only rate is 2/4 = 50.0%; it must not erase the missing record. The sensitivity range is 40.0% to 60.0% under the two missing-evidence scenarios, not a confidence interval.

Check that findings do not allege a realized loss without evidence. Confirm that C03's design gap is not averaged away by C01 or C02 passes. Verify that the overall language distinguishes an observed control deviation, an unsupported execution, and a design deficiency. A reviewer can accept the workpaper as accurately restricted while declining to conclude on operating effectiveness.
