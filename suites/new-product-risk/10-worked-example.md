# Worked example — New Product Risk and Launch Readiness

## Fictional product and approved conditions

SYN-001 describes a fictional payment-request workflow for a limited pilot. No actual financial institution, provider, customer, control, or payment appears here. The fixture uses generic roles, an invented approval record, and a test environment. The assessment date is Oct 09, 2026; proposed pilot date is Oct 20, 2026. All thresholds, timing conditions, and critical classifications are illustrative.

The product accepts identity attributes, authenticates a user, receives a payment instruction, routes relevant data to review, sends an approved instruction to a provider, and reconciles settlement events. The provider performs the funds transfer; the request service handles instructions. Keeping those responsibilities separate is part of the test.

## Complete principal flow map

FL01 is DATA from Applicant to Enrollment service: identity attributes, dependent on Enrollment review. FL02 is SERVICE from User channel to Request service: payment instruction, dependent on Authentication and limits. FL03 is DATA from Request service to Review queue: instruction and risk fields, dependent on Screening and monitoring. FL04 is FUNDS from Payment provider to Recipient institution: illustrative payment value, dependent on Approved instruction and settlement. FL05 is DATA from Payment provider to Reconciliation service: status and ledger events, dependent on Reconciliation and exception handling.

The flow document also states that rejected instructions are not sent for settlement, pending instructions remain in an exception queue, and exit must preserve unresolved items. Evidence for those branches is assessed through conditions, not assumed from the diagram.

## Complete condition evidence

| Condition | Criterion and supplied evidence | Critical | Expected status |
| --- | --- | --- | --- |
| LC01 | Primary instruction/funds map is documented and accepted in fixture | Yes | SATISFIED |
| LC02 | Screening configuration and ten named fixture tests have expected outcomes | Yes | SATISFIED |
| LC03 | Owner says monitoring exception test passed; report not supplied | Yes | NOT VERIFIABLE |
| LC04 | Reconciliation identifies all values but one item exceeds timing criterion | Yes | PARTIAL |
| LC05 | All four pilot operator roles have dated completion evidence | No | SATISFIED |
| LC06 | Exit plan written; required rehearsal has not occurred | Yes | NOT SATISFIED |

LC02's ten successful tests support the stated fixture condition; they do not establish universal sanctions or monitoring coverage. LC03's missing report is an evidence gap. LC06 differs because the fixture explicitly states that the rehearsal did not occur. Preserve this distinction.

## Complete reconciliation mini-population

| Test payment | Instruction amount USD | Posted amount USD | Pending amount USD | Age minutes | Expected resolution criterion |
| --- | --- | --- | --- | --- | --- |
| PAY01 |20.00|20.00|0.00|10|Within30 minutes|
| PAY02 |30.00|30.00|0.00|15|Within30 minutes|
| PAY03 |50.00|0.00|50.00|60|Within30 minutes|

Instructions sum 20+30+50=$100.00. Posted sum 20+30+0=$50.00. Pending sum 0+0+50=$50.00. Value conservation holds:100=50+50. PAY03 age60 exceeds criterion 30 by 30 minutes. The evidence supports a timing exception, not a loss or an unauthorized payment allegation. LC04 remains PARTIAL because detection and value reconciliation work while resolution evidence is incomplete.

## Expected domain outputs and arithmetic

FlowMap has exactly five rows FL01–FL05 with the columns in05. LaunchConditions has exactly six rows LC01–LC06, preserving all evidence gaps. Three conditions are satisfied: LC01,LC02,LC05. Three remain unresolved: LC03,LC04,LC06. Completion count 3/6=50.0%. Critical count 5; unresolved critical3/5=60.0%. Training completion4/4=100% for the fictional pilot operators only.

The comparison between100% training and50.0% overall condition completion does not resolve the launch question. The three unresolved critical prerequisites control the recommendation under the fixture's rules.

## Expected findings and recommendation

NP-F01 is HIGH severity, HIGH confidence, Observed for absent monitoring test evidence. NP-F02 is HIGH severity, HIGH confidence, Observed for the unresolved timing exception. NP-F03 is HIGH severity, HIGH confidence, Observed for the unrehearsed exit. Each cites SYN-001 and the relevant condition. Confidence in these facts does not establish the likelihood of future harm.

The draft recommendation is that the evidence does not support launch consideration yet. Obtain LC03's inspectable test, resolve and retest LC04's delayed path, and perform LC06's rehearsal. No amount of passing minor conditions clears these gates automatically. The human decision forum can review scope changes or exceptions, but the assistant cannot waive the criteria.

## Clearance and edge cases

If LC03's report is supplied, verify that it covers this product version, relevant data, exception routing, expected outcomes, and timing. If PAY03 later posts, preserve the original60-minute exception and determine whether the root cause is resolved before retest. If the launch scope removes FL04 funds execution, reassess the actual remaining service rather than assuming all funds-related conditions vanish; pending obligations may still exist.

If the pilot is limited to four operators, verify that access enforces the limit and that backup operators are either trained or excluded. If a provider outage occurs during exit rehearsal, verify that pending records remain recoverable without relying on the unavailable provider. If a condition is approved for post-launch completion, record the approving role, rationale, deadline, monitoring, and residual restriction. The original unresolved state remains in history.
