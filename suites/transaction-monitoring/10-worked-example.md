# Transaction monitoring: complete fictional example

All entities, records, invoices, and observations below are invented for arithmetic and reasoning checks. No production validation is claimed. Review period: 2026-09-01 12:00 AM ET inclusive to 2026-09-02 12:00 AM ET exclusive. All monetary values are USD. All records are POSTED except the unreadable amount in R10, whose posting status is known but value is not.

## Complete raw input population — SYN-001

| raw_row_id | transaction_id | account_id | event_time ET | direction | amount | counterparty_id | own_transfer |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | T01 | A | Sep 01, 2026 9:00 AM ET | CREDIT | 6000.00 | P01 | false |
| R02 | T02 | A | Sep 01, 2026 10:00 AM ET | CREDIT | 4000.00 | P02 | false |
| R03 | T03 | A | Sep 01, 2026 11:00 AM ET | DEBIT | 9500.00 | P03 | false |
| R04 | T04 | B | Sep 01, 2026 9:00 AM ET | CREDIT | 5000.00 | P04 | false |
| R05 | T05 | B | Sep 01, 2026 12:00 PM ET | DEBIT | 4800.00 | P05 | false |
| R06 | T06 | C | Sep 01, 2026 9:00 AM ET | CREDIT | 3000.00 | C-OWN-1 | true |
| R07 | T07 | C | Sep 01, 2026 10:00 AM ET | DEBIT | 3000.00 | C-OWN-2 | true |
| R08 | T08 | D | Sep 01, 2026 1:00 PM ET | DEBIT | 1000.00 | P06 | false |
| R09 | T01 | A | Sep 01, 2026 9:00 AM ET | CREDIT | 6000.00 | P01 | false |
| R10 | T09 | D | Sep 01, 2026 2:00 PM ET | DEBIT | unreadable | P07 | false |

R09 is a second extract copy of the exact same T01 account leg and source version, not a second economic event. R10 has no recoverable numeric amount. Do not infer its value from nearby rows.

## Context register

| Evidence ID | Account | Full supplied context | Evidential limit |
| --- | --- | --- | --- |
| SYN-002 | A | Fictional account profile states small consulting receipts and ordinary supplier payments. No invoice, contract, opening balance, or explanation for P03 supplied. | Profile is a report of expected activity, not proof of actual purpose. |
| SYN-003 | B | Fictional invoice INV-B-01 for 4,800.00 USD names P05 and is matched to T05; independent payment reference confirms the invoice identifier. | Supports this payment; does not validate every aspect of B. |
| SYN-004 | C | Fictional ownership register confirms C-OWN-1 and C-OWN-2 belong to the same customer as C during the review period. | Supports exclusion from TM-01 external-flow screen only. |
| SYN-005 | D | Source exception confirms T09 is in scope and posted but its amount field failed extraction. | Monetary completeness and D's ratio cannot be established. |

## Reconciliation and exact arithmetic

Received 10 = processed 8 + duplicate 1 + unparsed 1 + out-of-scope 0 + inaccessible 0 + deferred 0. Processed population is R01–R08. It contains 4 credits and 4 debits across 4 accounts. Credits are 6,000 + 4,000 + 5,000 + 3,000 = **18,000.00 USD**. Known debits are 9,500 + 4,800 + 3,000 + 1,000 = **18,300.00 USD**. Known gross movement is 18,000 + 18,300 = **36,300.00 USD**. Known signed movement is 18,000 − 18,300 = **−300.00 USD**. These are partial monetary totals because R10 is unknown.

After own-transfer exclusion, known eligible credits are 15,000.00 USD and known eligible debits are 15,300.00 USD. This cross-account ratio is not TM-01's account-level rule and must not be used as an alert. C's 6,000.00 USD gross movement remains in the AccountFlows table. A and B supply 5 fully assessable eligible transactions; D supplies one known eligible transaction plus one unparsed event and is blocked.

A: 9,500 / 10,000 = **0.95**; first subsequent debit is 11:00 AM minus 9:00 AM = **2 hours**. B: 4,800 / 5,000 = **0.96**; elapsed **3 hours**. C: eligible credits and debits both zero; ratio null, not 0.00. D: eligible known credits zero; ratio null, with the additional amount defect preventing assessment.

## Expected AccountFlows

| account_id | currency | processed_tx_count | credit_total | debit_total | eligible_credit_total | eligible_debit_total | out_in_ratio | population_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | USD | 3 | 10000 | 9500 | 10000 | 9500 | 0.95 | COMPLETE |
| B | USD | 2 | 5000 | 4800 | 5000 | 4800 | 0.96 | COMPLETE |
| C | USD | 2 | 3000 | 3000 | 0 | 0 | null | OWN_TRANSFER_EXCLUDED |
| D | USD | 1 | 0 | 1000 | 0 | 1000 | null | UNPARSED_AMOUNT |

## Expected ScenarioResults

| scenario_result_id | account_id | scenario_id | eligible | rule_result | first_credit_to_debit_hours | review_outcome | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SR-001 | A | TM-01 | True | MATCH | 2 | ESCALATE_FOR_REVIEW | SYN-001;SYN-002 |
| SR-002 | B | TM-01 | True | MATCH | 3 | EXPLANATION_SUPPORTED | SYN-001;SYN-003 |
| SR-003 | C | TM-01 | False | EXCLUDED | null | OWN_TRANSFER_CONFIRMED | SYN-001;SYN-004 |
| SR-004 | D | TM-01 | False | NOT_ASSESSABLE | null | DATA_REPAIR_REQUIRED | SYN-001;SYN-005 |

## Expected findings and reviewer handoff

TM-F01 is MEDIUM severity, MODERATE confidence, Inferred: A meets an illustrative rapid-movement pattern, but purpose remains unsupported. Request purpose and counterparty evidence and send the analytical package to the authorized reviewer. Do not label A a money launderer or describe the $9,500.00 as criminal proceeds.

TM-F02 is LOW severity, HIGH confidence, Observed: B remains a raw rule match with an invoice-supported explanation. The finding is about the supplied documentation, not an automatic account clearance. The reviewer may accept, reject, or seek further corroboration of that explanation.

TM-F03 is HIGH severity, HIGH confidence, Observed: D's source defect blocks a complete assessment. The high confidence applies to the presence of the defect, not to a suspicion about D. Ask the data owner for a corrected source and recompute affected metrics. Do not remove D from the population to improve completeness.

There are **2 numerical matches**, **1 supported explanation**, **1 proposed further-review referral**, **1 own-transfer exclusion**, and **1 blocked account**. The last three categories belong to different review states; do not add them to raw transactions. Among the two fully assessed eligible accounts, the illustrative rule match rate is 2/2 = 100.0%; this tiny designed sample is not an operational performance estimate.

## Expected control outcomes

R09 has no effect on canonical amounts. R10 prevents monetary completeness. Removing B's invoice leaves the rule match unchanged but changes its contextual outcome to OPEN_QUESTION. Removing C's ownership evidence invalidates the confirmed exclusion. Replacing A's debit with 8,999.00 gives 0.8999 and NO_MATCH on ratio, with all other factors held fixed; it does not prove the payment benign. A separate zero-credit complete account returns NO_MATCH with ratio null, whereas D remains NOT_ASSESSABLE because its ledger is incomplete.
