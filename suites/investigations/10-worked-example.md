# Investigation review: complete fictional case

This is an invented case involving a fictional equipment trader. It contains no real subject, account, contract, invoice, or payment. As-of: Sep 05, 2026 12:00 PM ET. Review scope: the supplied records from Sep 01 through Sep 04, 2026. No complete account statement or opening balance is supplied.

## Complete source-item population

| Item | Evidence | Complete supplied content | Terminal bucket |
| --- | --- | --- | --- |
| I01 | SYN-001 | Profile dated Sep 01, 2026 9:00 AM ET states equipment trading; no independently verified business activity supplied. | processed |
| I02 | SYN-002 | Posted receipt Sep 02, 2026 10:00 AM ET: 12,000.00 USD from Payer-P, transaction IN-01. | processed |
| I03 | SYN-003 | Posted debit Sep 02, 2026 11:00 AM ET: 11,000.00 USD to Supplier-Q, transaction OUT-01. | processed |
| I04 | SYN-004 | Customer statement Sep 03, 2026 9:00 AM ET: OUT-01 paid for equipment described in the supplied invoice. | processed |
| I05 | SYN-005 | Invoice document received Sep 03, 2026 10:00 AM ET; face amount 10,000.00 USD; issuer Supplier-R; reference INV-01; no tax, shipping, or additional invoice supplied. | processed |
| I06 | SYN-006 | Posted return Sep 04, 2026 9:00 AM ET: 2,000.00 USD, transaction RET-01, explicit system link to OUT-01. | processed |
| I07 | SYN-005-DUP | Exact second copy of I05, same content and version; retained locator points to I05. | duplicate |
| I08 | GAP-001 | Contract referenced by customer, but the file is inaccessible; no content can be inspected. | inaccessible |

Received **8 = 6 processed + 1 duplicate + 1 inaccessible + 0 excluded + 0 unparsed + 0 deferred**. The duplicate and inaccessible contract remain in the inventory but do not become events or evidence of contractual terms. The six processed items support six chronology events. The invoice date is not independently established; EV-05 uses the known receipt timestamp, explicitly as a document-receipt event.

## Expected CaseTimeline

| event_id | event_time | event_type | amount | currency | evidence_id | claim_class | detail |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EV-01 | 2026-09-01T09:00:00-04:00 | PROFILE | null | null | SYN-001 | Reported | Profile states equipment trading |
| EV-02 | 2026-09-02T10:00:00-04:00 | CREDIT | 12000 | USD | SYN-002 | Observed | Posted receipt from Payer-P |
| EV-03 | 2026-09-02T11:00:00-04:00 | DEBIT | 11000 | USD | SYN-003 | Observed | Posted payment to Supplier-Q |
| EV-04 | 2026-09-03T09:00:00-04:00 | EXPLANATION | null | null | SYN-004 | Reported | Customer says EV-03 paid for equipment |
| EV-05 | 2026-09-03T10:00:00-04:00 | DOCUMENT | null | null | SYN-005 | Observed | Invoice face amount 10000 USD names Supplier-R |
| EV-06 | 2026-09-04T09:00:00-04:00 | RETURN | 2000 | USD | SYN-006 | Observed | Posted return explicitly linked to EV-03 |

## Exact monetary working

Actual monetary events are EV-02, EV-03, and EV-06. Known credits = 12,000 + 2,000 = **14,000.00 USD**. Known debits = **11,000.00 USD**. Known gross movement = 14,000 + 11,000 = **25,000.00 USD**. Known net ledger movement = 14,000 − 11,000 = **3,000.00 USD**; no ending balance can be calculated without the opening balance and complete account coverage.

Payment-to-invoice difference = 11,000 − 10,000 = **1,000.00 USD**. No evidence establishes why that difference exists. No evidence establishes that Supplier-Q and Supplier-R are the same entity or have an agent relationship. The invoice is therefore a possible explanatory document with unresolved amount and identity questions.

Linked return = **2,000.00 USD**. Net unreversed original debit = 11,000 − 2,000 = **9,000.00 USD**. Return fraction = 2,000/11,000 = **0.181818...**, displayed **18.2%**. The net unreversed amount is not a confirmed loss, criminal proceeds amount, or automatically reportable figure.

The debit followed the receipt by **1 hour**. Debit/receipt ratio = 11,000/12,000 = **0.916666...**, displayed **91.7%**. This temporal pattern does not establish the incoming funds financed the outgoing payment; an opening balance and other activity are absent.

## Expected HypothesisTests

| hypothesis_id | hypothesis | supporting_evidence | conflicting_evidence | missing_evidence | assessment | confidence | next_step |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H-01 | Payment was ordinary equipment settlement | SYN-001;SYN-004;SYN-005 | SYN-003;SYN-005 | Supplier identity bridge and contract | UNRESOLVED | LOW | Match beneficiary and full invoiced amount |
| H-02 | Onward movement lacks a supported purpose | SYN-002;SYN-003;SYN-005 | SYN-004 | Purpose and beneficiary corroboration | PATTERN_SUPPORTED | MODERATE | Obtain discriminating source documents |
| H-03 | Return fully reversed the payment | SYN-006 | SYN-003;SYN-006 | None for arithmetic | CONTRADICTED | HIGH | Record $9,000.00 net unreversed amount |

## Expected findings and inquiry plan

INV-F01, MEDIUM / HIGH / Observed: the invoice does not fully reconcile with the payment. Cite SYN-003 and SYN-005. The observed mismatch requires beneficiary linkage and an explanation of 1,000.00 USD. Do not label the invoice fraudulent.

INV-F02, MEDIUM / MODERATE / Inferred: rapid onward movement has an unresolved economic purpose. Cite SYN-002 through SYN-005. The compatible profile and customer explanation are counterevidence; the mismatch and inaccessible contract leave the purpose uncorroborated. Propose a targeted inquiry, not a criminal conclusion.

INV-F03, LOW / HIGH / Observed: partial return leaves 9,000.00 USD unreversed. Cite SYN-003 and SYN-006. Preserve gross debit and return rather than netting away the chronology. Do not characterize this amount as loss without separate evidence.

Proposed actions: obtain the accessible contract; establish the Supplier-Q/Supplier-R relationship through approved records; obtain a full settlement breakdown; confirm whether further returns exist within an expanded authorized period. All actions are PROPOSED. No request has been sent, case closed, filing made, or account action taken in this example.

## Counterfactual checks

A corroborated 1,000.00 USD transport charge plus verified settlement-agent relationship could resolve the invoice discrepancy. A mere repeated customer assertion cannot. An unlinked return cannot reduce OUT-01's net unreversed value. A later confirmed 9,000.00 USD return brings cumulative returns to 11,000.00 USD and net unreversed value to zero while preserving the original purpose inquiry. These counterfactuals test the dependence of each conclusion on specific evidence rather than on narrative preference.
