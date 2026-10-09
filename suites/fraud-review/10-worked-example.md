# Fraud review: complete fictional example

All incidents, counterparties, instructions, contracts, and ledger records are fictional. As-of: Sep 05, 2026 12:00 PM ET. All amounts are USD. The task is to assess the four supplied incidents and prepare proposed actions for an authorized responder; no action is executed.

## Complete eight-record input population

| Record | Evidence | Case | Supplied facts | Claim class |
| --- | --- | --- | --- | --- |
| R01 | SYN-001 | F01 | Instruction Sep 01, 2026 9:00 AM ET requests 40,000.00 USD to a new beneficiary. A documented callback using the preexisting supplier contact records supplier denial of the instruction. No attacker identity established. | Reported |
| R02 | SYN-002 | F01 | Ledger confirms 40,000.00 USD executed Sep 01, 2026 10:00 AM ET, payment PAY-01. A distinct realized 10,000.00 USD return Sep 02, 2026 11:00 AM ET links explicitly to PAY-01. Complete supplied return coverage through as-of. | Observed |
| R03 | SYN-003 | F02 | Suspicious request Sep 02, 2026 9:00 AM ET seeks 15,000.00 USD to changed beneficiary details; established verification failed. | Reported |
| R04 | SYN-004 | F02 | Instruction status rejected; complete supplied execution history confirms no payment and no return through as-of. | Observed |
| R05 | SYN-005 | F03 | Employee complaint Sep 04, 2026 9:00 AM ET alleges an unauthorized payroll destination change and 12,000.00 USD at issue. No original instruction or transaction ID supplied. | Reported |
| R06 | SYN-006 | F03 | Inventory confirms ledger and access logs are not supplied. It contains no execution or recovery facts. | Observed |
| R07 | SYN-007 | F04 | Signed fictional contract amendment changes supplier beneficiary; documented confirmation used an established trusted channel before payment. Amount 5,000.00 USD. | Observed |
| R08 | SYN-008 | F04 | Ledger confirms ordinary 5,000.00 USD payment Sep 03, 2026 2:00 PM ET; complete supplied return history shows no return. | Observed |

Source reconciliation: **8 received = 8 processed + 0 duplicates + 0 exclusions + 0 unparsed + 0 inaccessible + 0 deferred**. R06 is an accessible inventory record establishing that relevant source data is missing; it does not mean the ledger was processed. There are four case records, three visible instructions/contract requests plus one reported amount, two confirmed executed payments, one confirmed unexecuted request, and one unknown execution state.

## Expected IncidentAmounts

| case_id | currency | requested_amount | executed_amount | confirmed_return_amount | net_unreturned_amount | amount_status | review_state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F01 | USD | 40000 | 40000 | 10000 | 30000 | CONFIRMED | SUSPECTED_FRAUD |
| F02 | USD | 15000 | 0 | 0 | 0 | CONFIRMED | PREVENTED_REQUEST |
| F03 | USD | 12000 | null | null | null | EXECUTION_UNKNOWN | OPEN_ALLEGATION |
| F04 | USD | 5000 | 5000 | 0 | 5000 | CONFIRMED | BENIGN_SUPPORTED |

## Exact arithmetic and scope

All known requested or reported amounts total 40,000 + 15,000 + 12,000 + 5,000 = **72,000.00 USD**. This includes ordinary F04 and reported F03. It is not fraud loss. The first three cases' suspected/alleged request amounts total **67,000.00 USD**; that is also not executed exposure.

Known executed amount = 40,000 + 0 + 5,000 = **45,000.00 USD**, with F03 unresolved and excluded from the numeric sum. Confirmed linked realized returns total **10,000.00 USD** from F01; F03 recovery remains unknown. F01 net unreturned = 40,000 − 10,000 = **30,000.00 USD**. F02 net = 0 − 0 = **0.00 USD**. F04 net = 5,000 − 0 = **5,000.00 USD**, a normal unreturned payment rather than fraud exposure.

Known net unreturned across assessable cases is 30,000 + 0 + 5,000 = **35,000.00 USD**. The **known suspected-fraud unreturned subtotal is 30,000.00 USD**, excluding ordinary F04 and retaining F03 as an explicit unresolved gap. Do not call 30,000.00 USD complete exposure or a permanent lower bound; later returns can reduce it and new execution evidence can change the scope.

F01's returned fraction is 10,000/40,000 = **25.0%**. F02 has a confirmed unexecuted request amount of **15,000.00 USD**; avoided loss is not observed. F03's requested amount of **12,000.00 USD** must not be copied into executed, return, or net columns.

## Expected VerificationReview

| case_id | authorization_basis | detail_change | independent_verification | payment_status | time_sensitivity | proposed_action | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F01 | Impersonated supplier instruction reported | New beneficiary | Known-channel supplier denial documented | EXECUTED_PARTIAL_RETURN | HIGH | Authorized fraud responder review and recovery assessment | SYN-001;SYN-002 |
| F02 | Suspicious instruction identified before execution | New beneficiary | Request failed established verification | NOT_EXECUTED | MEDIUM | Preserve instruction and verify cancellation state | SYN-003;SYN-004 |
| F03 | Employee reports unauthorized payroll change | Payroll destination changed | No independent logs or ledger supplied | UNKNOWN | HIGH | Obtain ledger and access logs through approved incident process | SYN-005;SYN-006 |
| F04 | Amended contract and approved instruction | New beneficiary | Preexisting trusted-channel confirmation documented | EXECUTED | LOW | Document supported ordinary change and human disposition | SYN-007;SYN-008 |

## Expected findings and proposed actions

FR-F01: HIGH severity, HIGH confidence, Observed for the narrow monetary statement. A suspected supplier-impersonation incident has 30,000.00 USD unreturned. The supplier denial is Reported evidence and does not establish perpetrator identity. Propose prompt authorized fraud-response review and assessment of permitted recovery routes. Final liability and loss are undecided.

FR-F02: MEDIUM severity, HIGH confidence, Observed. The 15,000.00 USD request did not execute within complete supplied status coverage. Preserve the instruction and cancellation evidence. Do not report 15,000.00 USD loss or proven savings.

FR-F03: HIGH severity, LOW confidence, Reported. A payroll allegation has unknown execution and authorization status. Propose urgent acquisition of ledger and access evidence through the approved human process. The urgency does not justify inventing execution or accepting the complaint as a final determination.

FR-F04: LOW severity, HIGH confidence, Observed. A beneficiary change has corroborated ordinary-business support. Retain the 5,000.00 USD payment in the population and exclude it from the suspected-fraud subtotal. Seek human disposition rather than automatic clearance.

All actions are PROPOSED. No call, recall, hold, access restriction, reimbursement, filing, or external notification occurred as part of this example.

## Expected adversarial outcomes

Duplicate the 10,000.00 USD return reference: totals do not change. Add a distinct confirmed 5,000.00 USD return linked to PAY-01: F01 net becomes 25,000.00 USD. Replace the return record with an unconfirmed recall request: 30,000.00 USD can no longer be asserted as confirmed net. Supply a confirmed rejection for F03: execution becomes zero after the record is verified. Remove F04's independent confirmation: its ordinary explanation becomes unresolved, but a changed beneficiary still does not establish fraud. These tests protect the distinction between instructions, execution, recovery, interpretation, and human action.
