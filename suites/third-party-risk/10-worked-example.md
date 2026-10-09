# Worked example — Third-Party Service and Assurance Review

## Fictional service and dependence

SYN-001 describes a fictional review decision service and its supporting providers. All service roles, evidence, metrics, records, contract terms, and test outcomes are invented. No real vendor, customer, account, or assurance report is represented. The assessment date is Oct 09, 2026.

SV01 is the Primary provider's Review decision service, using Customer attributes and depending on SV02 storage and SV03 reference data. SV02 is a Storage subcontractor holding Stored customer attributes. SV03 is a Reference supplier delivering a Reference dataset. SV04 is a Support subcontractor with Privileged support access and a dependency on SV01. SV05 is a Proposed fallback provider that also depends on SV02 storage. None of the alternatives has been demonstrated to replace the full service independently.

The fictional review declares five critical criteria and one supporting scope criterion. These classifications and targets are illustrative. They are not prescribed assurance requirements for every service.

## Complete assurance evidence package

| Review | Supplied evidence | Expected result | Critical |
| --- | --- | --- | --- |
| AR01 | Current service description identifies boundaries and responsible roles | SUPPORTED | No |
| AR02 | Assurance report covers2025 calendar year, excludes storage subcontractor; later management assertion supplied | PARTIAL | Yes |
| AR03 | Recovery rehearsal restores defined service in6 hours with 20-minute data lag | FAILED | Yes |
| AR04 | Exit rehearsal returns985 of 1000 expected record IDs;15 unexplained | FAILED | Yes |
| AR05 | Customer-side access review required; owner says done but record absent | UNVERIFIED | Yes |
| AR06 | Incident-notification schedule drafted; current executed contract does not include it | PARTIAL | Yes |

AR02's report period ends Dec 31, 2025. It does not have an invented expiry date. At Oct 09, 2026, the period-end-to-assessment interval is 282 calendar days. The later assertion may provide management's account of changes, but it is not independent testing of that interval. Storage exclusion is a scope limitation, not proof of failed storage controls.

AR03's fixture criterion is recovery within 4 hours and data lag no more than 15 minutes. Observed6 hours exceeds the recovery criterion by 2 hours; observed 20-minute lag exceeds the lag criterion by 5 minutes. These are test deviations. They do not establish that production records were lost or an actual outage occurred.

AR04's expected population contains IDs X0001 through X1000 inclusive. The returned export contains X0001 through X0985 inclusive. The missing IDs are X0986 through X1000, exactly 15. This compact range fully defines the fictional population without requiring a 1000-row attachment. A reviewer can reconstruct the count as1000−985=15.

## Expected domain outputs

ServiceDependencies has exactly five rows SV01–SV05, preserving the shared SV02 dependency. dependency_id is null for SV02 and SV03 because this fixture supplies no deeper layer; the limitation is that further dependencies were not assessed. AssuranceReview has six rows AR01–AR06 with the statuses shown. AR01 is the only noncritical criterion and the only supported one.

Total criteria=6. SUPPORTED=1. PARTIAL=2. FAILED=2. UNVERIFIED=1. Reconciliation1+2+2+1=6. Supported fraction=1/6=16.7%. Critical unresolved=5/5=100%. These counts describe the specified fixture criteria; they are not a rating of the whole vendor market or a quantified probability of service failure.

Exit return rate=985/1000=98.5%. Missing-record rate=15/1000=1.5%. The high return rate does not satisfy the complete-export criterion because no exclusion explains the 15 records. If the service has legitimate retention exclusions, they must be supported and applied to the expected population transparently; they cannot be invented after the mismatch is seen.

## Expected findings and recommendation

TP-F01 is HIGH severity, HIGH confidence, Observed for the report's limited period and storage exclusion. TP-F02 is HIGH severity, HIGH confidence, Observed for the recovery and lag test failures. TP-F03 is HIGH severity, HIGH confidence, Observed for the export shortfall. AR05 and AR06 also remain visible as unresolved reliance conditions, even if summarized within the action plan rather than separate headline findings.

The draft recommendation is that the evidence does not support unrestricted reliance or acceptance yet. Resolve the assurance coverage, recoverability, portability, customer-side control, and contract support questions. A restricted relationship could be considered only with a documented scope, feasible interim measures, and authorized human acceptance. The assistant does not onboard, renew, terminate, or transfer data.

## Proposed clearance evidence

For AR02, obtain relevant current-period and storage-control evidence, then assess scope and exceptions. For AR03, address the recovery bottleneck and repeat a scenario that includes the shared storage dependency. For AR04, locate or explain each missing ID and repeat export, import, permissions, and reconciliation tests. For AR05, inspect the required customer-side access review evidence. For AR06, obtain the executed agreement or a legal-reviewed statement of current terms; a negotiation draft alone remains partial.

## Edge cases and interpretation

If a new report is issued tomorrow but covers only the same2025 period, the uncovered2026 interval remains. If SV05 moves to a different storage provider, verify the changed architecture and test it before calling the fallback independent. If all missing export records are later recovered, preserve the original failed rehearsal and identify the change before recording a successful retest. If the recovery target is formally revised from 4 to 8 hours after the test, show the original failure and new criterion separately; a changed target does not erase the historical result.

If the service is narrowed so it no longer stores customer attributes or performs a critical decision, reassess the relationship and criticality rather than mechanically carrying forward the same gate set. If no public screening research was performed, say so; do not claim a clean legal or adverse-media history. If a human accepts an exception, keep the evidence results unchanged and attach the authorized disposition, expiry, monitoring, and reopening triggers.
