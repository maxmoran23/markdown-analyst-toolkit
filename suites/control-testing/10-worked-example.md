# Worked example — Control Testing and Evidence Review

## Fictional scenario and criteria

SYN-001 contains the entire fictional population, definitions, and evidence below. No organization, individual, customer, or operational event is real. The review period is Sep 01–30, 2026. “Business day” in this miniature example means Monday through Friday with no holidays; that assumption is for arithmetic only. A live test must use the applicable approved calendar and cutoff rules.

C01 requires a queue review no later than one business day after receipt. C02 requires a documented reconciliation with the execution evidence retained. C03 is intended to require a separate approval before release, but its written procedure allows the preparer to approve. C01 and C02 designs are adequate for these narrow fictional objectives. C03's design is inadequate. All criteria are illustrative author-defined test conditions.

## Complete population of eight opportunities

| Population ID | Control | Trigger or period | Due / required evidence | Selected | Selection rationale |
| --- | --- | --- | --- | --- | --- |
| R01 | C01 | Sep 01, 2026 receipt | Review by Sep 02 | Yes | Ordinary case |
| R02 | C01 | Sep 03, 2026 receipt | Review by Sep 04 | No | Outside judgmental selection |
| R03 | C01 | Sep 07, 2026 receipt | Review by Sep 08 | Yes | Elevated-risk case |
| R04 | C01 | Sep 10, 2026 receipt | Review by Sep 11 | No | Outside judgmental selection |
| R05 | C02 | Week ending Sep 11 | Retained reconciliation | Yes | Ordinary case |
| R06 | C02 | Week ending Sep 18 | Retained reconciliation | Yes | Archive gap targeted |
| R07 | C02 | Week ending Sep 25 | Retained reconciliation | No | Outside judgmental selection |
| R08 | C03 | Sep 30, 2026 release | Separate approver before release | Yes | Census of one release |

All eight records are included in the supplied frame. There are no exclusions or duplicates. For demonstration the frame count is reconciled to the same fictional master schedule; this is not independent evidence about a real process. C01 and C02 selection is judgmental and deliberately includes a known archive concern. Do not infer a statistical rate from it. C03 has a census of its one fictional event.

## Complete selected evidence ledger

| Test | Record | Directly supplied evidence | Attribute result | Instance result |
| --- | --- | --- | --- | --- |
| T01 | R01 | Receipt Sep 01; review Sep 02; reviewer log retained | Timely | PASS |
| T02 | R03 | Receipt Sep 07; review Sep 09; reviewer log retained | Two business days after receipt versus one allowed | FAIL |
| T03 | R05 | Reconciliation shows totals matched; execution and review records retained | Required steps evidenced | PASS |
| T04 | R06 | Owner says completed; no execution artifact accessible | Execution unverified | UNABLE TO CONCLUDE |
| T05 | R08 | Preparation and approval both role P1; release follows approval | No separate reviewer | FAIL |

R03 was reviewed one business day after its due date, or two business days after receipt. These are different measurements; do not call both “two days late.” R06's owner statement is Reported. The missing archive is Observed in the supplied evidence package. Actual nonperformance is not established. R08 fails the control objective even though it follows the flawed written procedure; keep the design and objective-based execution observations distinguishable.

## Expected domain outputs

ControlSummary has exactly three rows: C01 population 4, selected 2, pass 1, fail 1, unassessed 0, design Adequate for stated objective, conclusion Sample deviation; C02 population 3, selected 2, pass 1, fail 0, unassessed 1, same design status, conclusion Unable to conclude; C03 population 1, selected 1, pass 0, fail 1, unassessed 0, design Inadequate, conclusion Design and operation gap.

TestResults has T01/R01/PASS, T02/R03/FAIL, T03/R05/PASS, T04/R06/UNABLE TO CONCLUDE, and T05/R08/FAIL. Each row points to SYN-001 and the corresponding control. Selection basis is Judgmental ordinary case, Judgmental elevated risk, Judgmental ordinary case, Judgmental missing archive, and Census of one event, respectively.

## Reproducible arithmetic

Population = 4 + 3 + 1 = 8. Selected = 2 + 2 + 1 = 5. Outcomes = 2 pass + 2 fail + 1 unable = 5. Selection coverage = 5/8 = 0.625 = 62.5%. Confirmed deviations among selected = 2/5 = 40.0%. Unable-to-conclude rate = 1/5 = 20.0%. Conclusive deviation rate = 2/(2+2) = 50.0%. If R06 later passes, selected deviation rate remains 40.0%; if it later fails, that rate becomes 3/5 = 60.0%. Neither scenario estimates the full population failure rate.

## Expected findings and restricted conclusion

CT-F01 is HIGH severity, HIGH confidence, Observed: R03 missed the illustrative timing criterion. CT-F02 is MEDIUM severity, HIGH confidence, Observed: evidence for R06 is missing; actual execution remains unassessed. CT-F03 is HIGH severity, HIGH confidence, Observed: C03 lacks separation of preparer and approver in both design and R08 execution. Confidence applies to these narrow statements, not to any unseen population.

The draft conclusion is: “Two confirmed deviations and one unresolved evidence gap were identified among five selected instances from eight supplied opportunities. C03's design does not meet its stated separation objective. Judgmental selection limits broader inference. Human review is required for scope expansion, severity acceptance, and remediation.” It must not say that 40.0% of the process fails or that the overall program is ineffective.

## Edge cases to reperform

If the approved calendar declares Sep 07 a nonbusiness day, recalculate R03 from the actual cutoff rule; do not import that change into the original example silently. If a recovered R06 artifact is only a later reconstruction, assess whether it proves execution or merely describes what should have happened. If R08 gains a second review after release, record corrective action without rewriting the historical failure. If R02 is added as a supplemental sample, preserve the original five-record results and report the expanded selection separately. If every selected record passes after a fresh retest, the human reviewer still needs evidence that the design change is in place and that the retest period is appropriate.
