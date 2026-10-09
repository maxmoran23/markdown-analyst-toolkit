# Investigation Case Review — complete worked case

**Fictional training case. All identifiers, parties, amounts, policy criteria, reviewers and outcomes below are synthetic.** The fully populated case demonstrates analytical method and output structure; it is not a completed operational review. All facts needed for its arithmetic are printed below.

## Raw fixture and exact source statements

The complete account A posting set is below. Amounts are positive native USD; sender and receiver determine direction. Opening A is 5000, closing A9000; opening B1000, closing B1500. All timestamps contain an explicit ET offset. The selected period is Sep 01–30, 2026.

| event_id | posted_time | sender | receiver | amount_usd | linked_return_of | source_description |
| --- | --- | --- | --- | --- | --- | --- |
| T01 | 2026-09-02T10:00:00-04:00 | P | A | 12000 | null | Receipt described by customer as equipment sale |
| T02 | 2026-09-02T11:00:00-04:00 | A | Q | 11000 | null | Equipment-purpose explanation; invoice names R |
| T03 | 2026-09-04T09:00:00-04:00 | Q | A | 2000 | T02 | Explicit partial return of T02 |
| T04 | 2026-09-05T09:00:00-04:00 | P2 | A | 8000 | null | Second customer receipt |
| T05 | 2026-09-05T12:00:00-04:00 | A | R | 7500 | null | Invoice INV-B and delivery receipt support purpose |
| T06 | 2026-09-06T09:00:00-04:00 | A | B | 500 | null | Same-entity account transfer; both books supplied |
| T07 | 2026-09-08T09:00:00-04:00 | P3 | A | 6000 | null | Customer receipt; remitter identity supported |
| T08 | 2026-09-08T09:20:00-04:00 | A | U | 6000 | null | Purpose explanation absent |
| T09 | 2026-09-10T10:00:00-04:00 | P | A | 3000 | null | Additional customer receipt |
| T10 | 2026-09-10T14:00:00-04:00 | A | Q | 2500 | null | Customer says invoice INV-C settlement |
| T11 | 2026-09-10T16:00:00-04:00 | A | BANK | 100 | null | Posted service fee |
| T12 | 2026-09-12T09:00:00-04:00 | P4 | A | 7000 | null | Customer receipt |
| T13 | 2026-09-12T10:00:00-04:00 | A | R | 6800 | null | Invoice INV-D full amount supported |
| T14 | 2026-09-13T10:00:00-04:00 | R | A | 400 | T13 | Explicit partial return of T13 |
| T15 | 2026-09-14T09:00:00-04:00 | A | B | 1000 | null | Same-entity transfer; both books supplied |
| T16 | 2026-09-15T09:00:00-04:00 | B | A | 1000 | null | Same-entity return transfer; not a supplier refund |
| T17 | 2026-09-17T09:00:00-04:00 | P5 | A | 5000 | null | Customer receipt |
| T18 | 2026-09-17T11:00:00-04:00 | A | V | 4000 | null | Invoice INV-E and delivery support purpose |
| T19 | 2026-09-18T10:00:00-04:00 | A | CASH | 1000 | null | Cash withdrawal; ultimate use uncorroborated |
| T20 | 2026-09-21T09:00:00-04:00 | P5 | A | 1500 | null | Customer receipt |
| T21 | 2026-09-21T12:00:00-04:00 | A | V | 1500 | null | Invoice INV-F and delivery support purpose |
| T22 | 2026-09-23T10:00:00-04:00 | U | A | 1000 | T08 | Explicit partial return of T08 |
| T23 | 2026-09-24T09:00:00-04:00 | A | Q | 700 | null | Adjustment description; supporting memo absent |
| T24 | 2026-09-25T16:00:00-04:00 | A | BANK | 300 | null | Posted service fee |

Account B has exactly three posted mirror representations: T06-B credit 500, T15-B credit 1000 and T16-B debit 1000. They share the economic transfer references T06/T15/T16 respectively. The raw intake contains three additional representations: RAW-DUP-T01 is an exact duplicate of T01; RAW-INSTR-T02 is an unexecuted instruction for 11000 that refers to T02; RAW-PENDING is a pending 2000 debit that never posts within this fixture. Thus 24 A rows plus 3 B mirrors plus 3 noncanonical representations equals 30 received rows.

S04 statement X01 says T02 paid equipment supplierQ, T10 settled INV-C and T19 covered expenses. Those assertions are Reported. S05 INV-A face amount is 10000 and namesR; no Q/R bridge or delivery record is supplied. S06 contains INV-B7500 toR, INV-D6800 toR, INV-E4000 toV and INV-F1500 toV with matching delivery records. S07 INV-C2500 namesQ but lacks delivery corroboration. S08 explicitly links T03→T02, T14→T13 and T22→T08. S09 identifies A/B as accounts of fictional Entity-J only. S10 Contract-C is encrypted and inaccessible. S12 CP-INV-1 requires the separate amount, beneficiary and purpose checks for this fictional exercise and authorizes no legal or filing conclusion.

## Complete transfer-by-transfer analyst walkthrough

### T01 — Customer receipt

At `2026-09-02T10:00:00-04:00`, the supplied posting records `P` to `A` for **USD 12,000.00**. Account A moves from **USD 5,000.00** to **USD 17,000.00**. Cumulative A credits through this row are **USD 12,000.00** and cumulative A debits **USD 0.00**; `5,000 + credits - debits` reproduces the displayed balance.

The source records a receipt from P, while its equipment-sale purpose is a customer account. The review observes the booked credit and preserves purpose separately.

This receipt increases the complete pre-T02 pool to 17000 when added to the supplied 5000 opening. A later debit may draw from either component under fungible-balance assumptions.

Source: S01.

### T02 — Supplier debit with conflicting invoice

At `2026-09-02T11:00:00-04:00`, the supplied posting records `A` to `Q` for **USD 11,000.00**. Account A moves from **USD 17,000.00** to **USD 6,000.00**. Cumulative A credits through this row are **USD 12,000.00** and cumulative A debits **USD 11,000.00**; `5,000 + credits - debits` reproduces the displayed balance.

INV-A names R and has face 10000, while this posted payment goes toQ for 11000. Those are two distinct reconciliation questions. The customer equipment explanation does not itself repair either.

The later linked return 2000 reduces residual to 9000. Keep gross 11000, return 2000 and invoice 10000 separate; adding the invoice to posted payments would double count a document as money.

Source: S01.

### T03 — Explicit linked return

At `2026-09-04T09:00:00-04:00`, the supplied posting records `Q` to `A` for **USD 2,000.00**. Account A moves from **USD 6,000.00** to **USD 8,000.00**. Cumulative A credits through this row are **USD 14,000.00** and cumulative A debits **USD 11,000.00**; `5,000 + credits - debits` reproduces the displayed balance.

S08 links this 2000 receipt to T02. That evidence justifies a return classification rather than merely a possible opposite-direction relationship.

The parent 11000 debit is only partly reversed. Residual 9000 is not confirmed loss, suspicious amount or a reportable amount. The return can be favorable evidence without proving the original purpose.

Source: S01; S08 explicit return linkage.

### T04 — Customer receipt

At `2026-09-05T09:00:00-04:00`, the supplied posting records `P2` to `A` for **USD 8,000.00**. Account A moves from **USD 8,000.00** to **USD 16,000.00**. Cumulative A credits through this row are **USD 22,000.00** and cumulative A debits **USD 11,000.00**; `5,000 + credits - debits` reproduces the displayed balance.

The 8000 receipt is a distinct credit from P2, not a duplicate of the earlier P payment. Its source identifier and date keep the two records separate.

This transaction is paired in time with T05 for descriptive chronology only. The matched invoice and delivery evidence supporting T05 concern its purpose, not an automatic tracing of these particular funds.

Source: S01.

### T05 — Supplier debit with matched support

At `2026-09-05T12:00:00-04:00`, the supplied posting records `A` to `R` for **USD 7,500.00**. Account A moves from **USD 16,000.00** to **USD 8,500.00**. Cumulative A credits through this row are **USD 22,000.00** and cumulative A debits **USD 18,500.00**; `5,000 + credits - debits` reproduces the displayed balance.

INV-B and its supplied delivery receipt match 7500 and counterpartyR. The fixture therefore treats this transaction as part of the fully supported invoice/delivery subset.

Keep it as material counterevidence to the claim that every supplier payment is unexplained. Its inclusion in that 19800 subset does not eliminate unrelated T02 orT08 gaps.

Source: S01.

### T06 — Verified own-account transfer

At `2026-09-06T09:00:00-04:00`, the supplied posting records `A` to `B` for **USD 500.00**. Account A moves from **USD 8,500.00** to **USD 8,000.00**. Cumulative A credits through this row are **USD 22,000.00** and cumulative A debits **USD 19,000.00**; `5,000 + credits - debits` reproduces the displayed balance.

A transfers 500 toB; the B credit is a mirror book entry of the same economic event. S09 supports grouping both accounts under Entity-J.

Account A falls 500 and B rises 500; entity balance is unchanged. Retain both account entries but only one canonical transfer. This is not new customer revenue or external supplier expenditure.

Source: S01.

### T07 — Customer receipt

At `2026-09-08T09:00:00-04:00`, the supplied posting records `P3` to `A` for **USD 6,000.00**. Account A moves from **USD 8,000.00** to **USD 14,000.00**. Cumulative A credits through this row are **USD 28,000.00** and cumulative A debits **USD 19,000.00**; `5,000 + credits - debits` reproduces the displayed balance.

The 6000 receipt from P3 is observed and its remitter identifier is supported within the fixture. It precedes a same-size outward transfer but is not itself proof of a pass-through purpose.

A matching amount can motivate an attribution question, yet pre-existing commingled funds mean equal size alone is not an exact tracing rule.

Source: S01.

### T08 — Supplier debit with inaccessible support

At `2026-09-08T09:20:00-04:00`, the supplied posting records `A` to `U` for **USD 6,000.00**. Account A moves from **USD 14,000.00** to **USD 8,000.00**. Cumulative A credits through this row are **USD 28,000.00** and cumulative A debits **USD 25,000.00**; `5,000 + credits - debits` reproduces the displayed balance.

The 6000 payment toU lacks accessible transaction-specific purpose corroboration. Contract-C exists as a supplied encrypted attachment, but its contents were not reviewed.

A later explicitly linked 1000 return leaves 5000 unreversed. The correct limitation is inaccessible purpose evidence, not an assertion that the contract contains no legitimate terms.

Source: S01.

### T09 — Additional customer receipt

At `2026-09-10T10:00:00-04:00`, the supplied posting records `P` to `A` for **USD 3,000.00**. Account A moves from **USD 8,000.00** to **USD 11,000.00**. Cumulative A credits through this row are **USD 31,000.00** and cumulative A debits **USD 25,000.00**; `5,000 + credits - debits` reproduces the displayed balance.

P appears again with a 3000 credit. The repeated sender is a relationship observation; it does not make this row a duplicate of T01.

Count both posted events and sum their amounts only within a named sender or period measure. Retain their separate dates if assessing timing or subsequent payments.

Source: S01.

### T10 — Partly supported supplier debit

At `2026-09-10T14:00:00-04:00`, the supplied posting records `A` to `Q` for **USD 2,500.00**. Account A moves from **USD 11,000.00** to **USD 8,500.00**. Cumulative A credits through this row are **USD 31,000.00** and cumulative A debits **USD 27,500.00**; `5,000 + credits - debits` reproduces the displayed balance.

INV-C matches 2500 and supplierQ, so amount and immediate beneficiary-name tests pass within the fixture. No delivery corroboration is supplied.

Do not include this row in the complete invoice-and-delivery subset 19800. Also do not describe it as having no support: the correct state is partial support with an identified missing dimension.

Source: S01.

### T11 — Bank fee

At `2026-09-10T16:00:00-04:00`, the supplied posting records `A` to `BANK` for **USD 100.00**. Account A moves from **USD 8,500.00** to **USD 8,400.00**. Cumulative A credits through this row are **USD 31,000.00** and cumulative A debits **USD 27,600.00**; `5,000 + credits - debits` reproduces the displayed balance.

The 100 service charge is a posted debit with a distinct fee purpose in the ledger. It is not a supplier payment.

Keep the fee in account and entity outflow equations while excluding it from the 40000 supplier gross denominator. Category consistency prevents a rate from using a numerator and denominator with different meanings.

Source: S01.

### T12 — Customer receipt

At `2026-09-12T09:00:00-04:00`, the supplied posting records `P4` to `A` for **USD 7,000.00**. Account A moves from **USD 8,400.00** to **USD 15,400.00**. Cumulative A credits through this row are **USD 38,000.00** and cumulative A debits **USD 27,600.00**; `5,000 + credits - debits` reproduces the displayed balance.

The 7000 receipt from P4 is an external customer inflow. It is included in 42500 customer receipts, while later supplier returns are tracked separately.

An analyst should not include every credit in customer receipts because credits also include own-account movements and returns. The ledger classification determines the business measure.

Source: S01.

### T13 — Supported supplier debit with later return

At `2026-09-12T10:00:00-04:00`, the supplied posting records `A` to `R` for **USD 6,800.00**. Account A moves from **USD 15,400.00** to **USD 8,600.00**. Cumulative A credits through this row are **USD 38,000.00** and cumulative A debits **USD 34,400.00**; `5,000 + credits - debits` reproduces the displayed balance.

INV-D and delivery support the 6800 payment toR. It remains in the 19800 gross supported subset even though a later partial return occurs.

Gross supported payment value and net unreversed payment value are separate measures. A return changes the latter; it does not retroactively remove the original supplied invoice/delivery match.

Source: S01.

### T14 — Explicit linked return

At `2026-09-13T10:00:00-04:00`, the supplied posting records `R` to `A` for **USD 400.00**. Account A moves from **USD 8,600.00** to **USD 9,000.00**. Cumulative A credits through this row are **USD 38,400.00** and cumulative A debits **USD 34,400.00**; `5,000 + credits - debits` reproduces the displayed balance.

The 400 receipt fromR explicitly refers to T13. Parent gross 6800 less 400 yields 6400 unreversed.

Retain this return among the total 3400 linked supplier returns. Do not apply it to another R payment such as T05 merely because the counterparty is the same.

Source: S01; S08 explicit return linkage.

### T15 — Verified own-account transfer

At `2026-09-14T09:00:00-04:00`, the supplied posting records `A` to `B` for **USD 1,000.00**. Account A moves from **USD 9,000.00** to **USD 8,000.00**. Cumulative A credits through this row are **USD 38,400.00** and cumulative A debits **USD 35,400.00**; `5,000 + credits - debits` reproduces the displayed balance.

The 1000 A-to-B movement is a new canonical transfer, separate from the earlier 500 movement. Its matching B book entry is a mirror representation.

The amount increases B’s balance and decreases A’s by the same amount. Consolidated balance does not change, but the account-level funding available for later events does.

Source: S01.

### T16 — Verified own-account transfer in the reverse direction

At `2026-09-15T09:00:00-04:00`, the supplied posting records `B` to `A` for **USD 1,000.00**. Account A moves from **USD 8,000.00** to **USD 9,000.00**. Cumulative A credits through this row are **USD 39,400.00** and cumulative A debits **USD 35,400.00**; `5,000 + credits - debits` reproduces the displayed balance.

B sends 1000 back toA. The movement is internal under S09 and is not a refund of a supplier purchase.

The direction reversal resembles a return superficially, but return_of remains null because it is an own-account transfer with different economic classification. Keep it in the 2500 canonical own-transfer total.

Source: S01.

### T17 — Customer receipt

At `2026-09-17T09:00:00-04:00`, the supplied posting records `P5` to `A` for **USD 5,000.00**. Account A moves from **USD 9,000.00** to **USD 14,000.00**. Cumulative A credits through this row are **USD 44,400.00** and cumulative A debits **USD 35,400.00**; `5,000 + credits - debits` reproduces the displayed balance.

P5 pays 5000. The transaction is included in external customer receipts and precedes a 4000 payment toV.

The available matching invoice/delivery evidence for T18 supports that payment’s represented business purpose. The temporal sequence does not alone establish exact source allocation.

Source: S01.

### T18 — Supplier debit with matched support

At `2026-09-17T11:00:00-04:00`, the supplied posting records `A` to `V` for **USD 4,000.00**. Account A moves from **USD 14,000.00** to **USD 10,000.00**. Cumulative A credits through this row are **USD 44,400.00** and cumulative A debits **USD 39,400.00**; `5,000 + credits - debits` reproduces the displayed balance.

INV-E and delivery support 4000 toV. It belongs in the complete supported supplier subset.

Preserve the exact match and favorable implication in ClaimTests and the narrative. A case can contain both supported and unresolved transactions without requiring one universal characterization.

Source: S01.

### T19 — Cash withdrawal

At `2026-09-18T10:00:00-04:00`, the supplied posting records `A` to `CASH` for **USD 1,000.00**. Account A moves from **USD 10,000.00** to **USD 9,000.00**. Cumulative A credits through this row are **USD 44,400.00** and cumulative A debits **USD 40,400.00**; `5,000 + credits - debits` reproduces the displayed balance.

The 1000 debit is a cash withdrawal. The customer says it covered expenses, but the ultimate use is uncorroborated in the supplied fixture.

Keep the cash category separate from supplier electronic payments and fees. No beneficiary identity or eventual economic use can be inferred from the cash debit alone.

Source: S01.

### T20 — Additional customer receipt

At `2026-09-21T09:00:00-04:00`, the supplied posting records `P5` to `A` for **USD 1,500.00**. Account A moves from **USD 9,000.00** to **USD 10,500.00**. Cumulative A credits through this row are **USD 45,900.00** and cumulative A debits **USD 40,400.00**; `5,000 + credits - debits` reproduces the displayed balance.

The 1500 payment from P5 is distinct from its earlier 5000 receipt. Both belong to customer-receipt totals, while each remains a separate chronological event.

A repeated payer and differing amounts are normal ledger relationships to record. Additional context would be needed to infer coordination, unusual fragmentation or a specific commercial purpose.

Source: S01.

### T21 — Supplier debit with matched support

At `2026-09-21T12:00:00-04:00`, the supplied posting records `A` to `V` for **USD 1,500.00**. Account A moves from **USD 10,500.00** to **USD 9,000.00**. Cumulative A credits through this row are **USD 45,900.00** and cumulative A debits **USD 41,900.00**; `5,000 + credits - debits` reproduces the displayed balance.

INV-F and delivery support 1500 toV. With T05,T13,T18, this completes the four-event 19800 gross supported subset.

Reproduce the subtotal as 7500+6800+4000+1500. Do not add T10 merely because its amount and name match; the fixture’s subset definition also requires delivery evidence.

Source: S01.

### T22 — Explicit linked return

At `2026-09-23T10:00:00-04:00`, the supplied posting records `U` to `A` for **USD 1,000.00**. Account A moves from **USD 9,000.00** to **USD 10,000.00**. Cumulative A credits through this row are **USD 46,900.00** and cumulative A debits **USD 41,900.00**; `5,000 + credits - debits` reproduces the displayed balance.

U returns 1000 with reference toT08. This reduces the parent 6000 debit to 5000 unreversed.

A partial return can be relevant counterevidence but does not resolve the inaccessible contract or explain the original transfer. Keep arithmetic completion and purpose uncertainty as separate states.

Source: S01; S08 explicit return linkage.

### T23 — Supplier adjustment with absent memo

At `2026-09-24T09:00:00-04:00`, the supplied posting records `A` to `Q` for **USD 700.00**. Account A moves from **USD 10,000.00** to **USD 9,300.00**. Cumulative A credits through this row are **USD 46,900.00** and cumulative A debits **USD 42,600.00**; `5,000 + credits - debits` reproduces the displayed balance.

The 700 payment toQ is recorded as an adjustment, but no supporting memo is supplied. The description is observed ledger text rather than proof of its economic basis.

It belongs in gross supplier debits because it is a posted payment to the supplier node. Its unresolved support does not justify changing the amount or excluding it from the denominator.

Source: S01.

### T24 — Bank fee

At `2026-09-25T16:00:00-04:00`, the supplied posting records `A` to `BANK` for **USD 300.00**. Account A moves from **USD 9,300.00** to **USD 9,000.00**. Cumulative A credits through this row are **USD 46,900.00** and cumulative A debits **USD 42,900.00**; `5,000 + credits - debits` reproduces the displayed balance.

The 300 service fee is the second posted bank charge. Combined with T11, fees total 400.

The final A balance becomes 9000. A correct final balance must coexist with the unresolved purpose and identity questions; reconciliation does not answer those different investigative propositions.

Source: S01.

## Fully populated expected domain outputs

These are the complete expected base-case records. They are not selected examples. Preserve every row when generating the report, workbook and dashboard. The raw facts above and the independent checks below explain the calculations; descriptive decisions additionally require the methods and gates in files 03–04.

### CaseTimeline

| event_id | event_time | from_node | to_node | amount_usd | currency | linked_return_of | account_a_balance_usd | evidence_ids | claim_class | detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T01 | 2026-09-02T10:00:00-04:00 | P | A | 12000 | USD | null | 17000 | S01 | Observed | Receipt described by customer as equipment sale |
| T02 | 2026-09-02T11:00:00-04:00 | A | Q | 11000 | USD | null | 6000 | S01 | Observed | Equipment-purpose explanation; invoice names R |
| T03 | 2026-09-04T09:00:00-04:00 | Q | A | 2000 | USD | T02 | 8000 | S01;S08 | Observed | Explicit partial return of T02 |
| T04 | 2026-09-05T09:00:00-04:00 | P2 | A | 8000 | USD | null | 16000 | S01 | Observed | Second customer receipt |
| T05 | 2026-09-05T12:00:00-04:00 | A | R | 7500 | USD | null | 8500 | S01 | Observed | Invoice INV-B and delivery receipt support purpose |
| T06 | 2026-09-06T09:00:00-04:00 | A | B | 500 | USD | null | 8000 | S01;S09 | Observed | Same-entity account transfer; both books supplied |
| T07 | 2026-09-08T09:00:00-04:00 | P3 | A | 6000 | USD | null | 14000 | S01 | Observed | Customer receipt; remitter identity supported |
| T08 | 2026-09-08T09:20:00-04:00 | A | U | 6000 | USD | null | 8000 | S01 | Observed | Purpose explanation absent |
| T09 | 2026-09-10T10:00:00-04:00 | P | A | 3000 | USD | null | 11000 | S01 | Observed | Additional customer receipt |
| T10 | 2026-09-10T14:00:00-04:00 | A | Q | 2500 | USD | null | 8500 | S01 | Observed | Customer says invoice INV-C settlement |
| T11 | 2026-09-10T16:00:00-04:00 | A | BANK | 100 | USD | null | 8400 | S01 | Observed | Posted service fee |
| T12 | 2026-09-12T09:00:00-04:00 | P4 | A | 7000 | USD | null | 15400 | S01 | Observed | Customer receipt |
| T13 | 2026-09-12T10:00:00-04:00 | A | R | 6800 | USD | null | 8600 | S01 | Observed | Invoice INV-D full amount supported |
| T14 | 2026-09-13T10:00:00-04:00 | R | A | 400 | USD | T13 | 9000 | S01;S08 | Observed | Explicit partial return of T13 |
| T15 | 2026-09-14T09:00:00-04:00 | A | B | 1000 | USD | null | 8000 | S01;S09 | Observed | Same-entity transfer; both books supplied |
| T16 | 2026-09-15T09:00:00-04:00 | B | A | 1000 | USD | null | 9000 | S01;S09 | Observed | Same-entity return transfer; not a supplier refund |
| T17 | 2026-09-17T09:00:00-04:00 | P5 | A | 5000 | USD | null | 14000 | S01 | Observed | Customer receipt |
| T18 | 2026-09-17T11:00:00-04:00 | A | V | 4000 | USD | null | 10000 | S01 | Observed | Invoice INV-E and delivery support purpose |
| T19 | 2026-09-18T10:00:00-04:00 | A | CASH | 1000 | USD | null | 9000 | S01 | Observed | Cash withdrawal; ultimate use uncorroborated |
| T20 | 2026-09-21T09:00:00-04:00 | P5 | A | 1500 | USD | null | 10500 | S01 | Observed | Customer receipt |
| T21 | 2026-09-21T12:00:00-04:00 | A | V | 1500 | USD | null | 9000 | S01 | Observed | Invoice INV-F and delivery support purpose |
| T22 | 2026-09-23T10:00:00-04:00 | U | A | 1000 | USD | T08 | 10000 | S01;S08 | Observed | Explicit partial return of T08 |
| T23 | 2026-09-24T09:00:00-04:00 | A | Q | 700 | USD | null | 9300 | S01 | Observed | Adjustment description; supporting memo absent |
| T24 | 2026-09-25T16:00:00-04:00 | A | BANK | 300 | USD | null | 9000 | S01 | Observed | Posted service fee |

### AccountBalances

| account_id | opening_usd | credits_usd | debits_usd | calculated_close_usd | supplied_close_usd | difference_usd | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | 5000 | 46900 | 42900 | 9000 | 9000 | 0 | S01;S03 |
| B | 1000 | 1500 | 1000 | 1500 | 1500 | 0 | S02;S03 |

### ClaimTests

| claim_id | proposition | supporting_ids | conflicting_ids | assessment | confidence | discriminator | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CL01 | T02 is fully reconciled equipment settlement | S04;S05 | S01;S05 | UNRESOLVED | LOW | Beneficiary bridge plus USD1000 difference and delivery evidence | S01;S04;S05 |
| CL02 | T03 fully reversed T02 | S08 | S01;S08 | CONTRADICTED | HIGH | No additional source needed for the supplied-period arithmetic | S01;S08 |
| CL03 | Every supplier payment is unexplained | S01 | S06 | CONTRADICTED | HIGH | Matched B/D/E/F records are material counterevidence | S01;S06 |
| CL04 | T08 purpose is substantiated | NONE_LOCATED | S01 | UNRESOLVED | LOW | Contract, invoice and beneficiary-purpose evidence | S01;S10 |
| CL05 | Own-account transfers create external turnover | S01 | S02;S09 | CONTRADICTED | HIGH | Entity aggregation removes three own transfers | S01;S02;S09 |
| CL06 | Rapid onward timing pattern exists for T01/T02 | S01 | NONE_LOCATED | PATTERN_SUPPORTED | HIGH | Timing established; source allocation and purpose remain separate | S01;S04;S05 |

### Contradictions

| contradiction_id | claim_id | left_account | right_account | effect | state | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| CT01 | CL01 | T02 paid Q USD11000 | INV-A names R USD10000 | Amount gap USD1000 and identity bridge remain separate | OPEN | S01;S05 |
| CT02 | CL02 | Return described as full reversal | Linked posted return USD2000 against USD11000 | Net unreversed T02 is USD9000 | RESOLVED_ARITHMETIC | S01;S08 |
| CT03 | CL03 | All supplier activity described as unsupported | INV-B/D/E/F support USD19800 gross supplier payments | Do not generalize unresolved subset to all USD40000 gross supplier debits | RESOLVED_SCOPE | S01;S06 |
| CT04 | CL05 | Account credits summed as new external funds | A/B internal mirrors total USD2500 canonical own transfer value | Entity external inflow excludes both directions of own transfers | RESOLVED_SCOPE | S01;S02;S09 |

### EvidenceRequests

| request_id | claim_id | request_text | state | decision_effect | evidence_ids |
| --- | --- | --- | --- | --- | --- |
| RQ01 | CL01 | Provide beneficiary bridge Q/R, explanation of USD1000 difference and delivery evidence for T02. | PROPOSED | Can resolve purpose/amount/beneficiary separately; cannot retroactively invent receipt | S01;S04;S05 |
| RQ02 | CL04 | Provide readable Contract-C and supporting T08 purpose documents. | INACCESSIBLE | Readable contract may support represented terms; payment purpose still needs linkage | S01;S10 |
| RQ03 | CL03 | Retain INV-B/D/E/F and delivery matches in favorable evidence set. | SATISFIED_FOR_SCOPE | Prevents claim that every supplier payment lacks support | S06 |
| RQ04 | CL05 | Retain supplied A/B ownership extract and mirrored postings. | SATISFIED_FOR_SCOPE | Supports perimeter netting only for A/B | S02;S09 |
| RQ05 | CL06 | Obtain allocation evidence only if attribution of T01 funds to T02 is decision-material. | PROPOSED | Could narrow source attribution; chronological proximity alone cannot do so | S01 |

### EvidenceProvenance

| source_id | source_title | locator | availability | origin_type | claim_class | limitation |
| --- | --- | --- | --- | --- | --- | --- |
| S01 | Account A posted ledger | Raw postings T01–T24 | AVAILABLE | SYSTEM_EXPORT | Observed | Complete stated account-period posting set; does not establish purpose |
| S02 | Account B posted ledger | Mirror legs T06, T15, T16 | AVAILABLE | SYSTEM_EXPORT | Observed | Ownership extract identifies A and B as same entity; mirror legs do not create new economic transfers |
| S03 | Opening and closing balances | A 5000→9000; B 1000→1500 | AVAILABLE | BALANCE_RECORD | Observed | Balances cover stated September perimeter only |
| S04 | Customer explanation | Statement X01 | AVAILABLE | CUSTOMER_STATEMENT | Reported | T02 said to pay equipment supplier Q; T10 said to settle INV-C; T19 said to cover expenses |
| S05 | Invoice INV-A | Face 10000 USD; supplier R | AVAILABLE | CUSTOMER_DOCUMENT | Observed | Document text observed; actual delivery and beneficiary bridge absent |
| S06 | Supported invoices and receipts | INV-B 7500; INV-D 6800; INV-E 4000; INV-F 1500 | AVAILABLE | CUSTOMER_DOCUMENT | Observed | Matched amounts and counterparties; supplied delivery records corroborate within fixture |
| S07 | Invoice INV-C | Face 2500 USD; supplier Q | AVAILABLE | CUSTOMER_DOCUMENT | Observed | Amount and name match T10; no delivery record supplied |
| S08 | Return references | T03→T02; T14→T13; T22→T08 | AVAILABLE | SYSTEM_EXPORT | Observed | Explicit linkage; amounts are partial, not full reversals |
| S09 | Account ownership extract | A and B belong to fictional Entity-J | AVAILABLE | ACCOUNT_RECORD | Observed | No ownership linkage supplied for Q, R, U or V |
| S10 | Contract file | Contract-C encrypted attachment | INACCESSIBLE | CUSTOMER_DOCUMENT | Reported | Filename supplied; text not accessible and cannot corroborate terms |
| S11 | Receipt manifest | 30 raw rows: 27 posted representations; 1 duplicate; 1 instruction; 1 pending | AVAILABLE | INTAKE_MANIFEST | Observed | Includes one T01 duplicate, unexecuted T02 instruction and pending USD2000 debit; exact exclusions in file 10 |
| S12 | Illustrative review charter | Fixture policy CP-INV-1 | AVAILABLE | ILLUSTRATIVE_POLICY | Observed | Requires amount/beneficiary/purpose checks for this exercise; no legal filing conclusion authorized |

### DecisionRecord

| decision_id | gate | status | basis | evidence_ids |
| --- | --- | --- | --- | --- |
| D01 | Population and balance gate | COMPLETE | 30 received rows reduce to 24 canonical transfers and 27 posted account representations; both balances tie. | S01;S02;S03;S11 |
| D02 | T02 purpose and beneficiary gate | HOLD_EVIDENCE | USD1000 invoice difference and Q/R bridge remain unresolved. | S01;S04;S05 |
| D03 | T08 purpose gate | HOLD_EVIDENCE | Readable contract and purpose corroboration absent; partial return does not resolve purpose. | S01;S08;S10 |
| D04 | Human case disposition | NOT_RECORDED | No actual authorized reviewer decision supplied. | S12 |

### ProcessQA

| check_id | check | expected | actual | result | evidence_ids |
| --- | --- | --- | --- | --- | --- |
| Q01 | Raw-to-canonical count | 30 raw; 27 posted representations; 24 transfers | 30 / 27 / 24 | PASS | S01;S02;S11 |
| Q02 | Account A close | USD9000 | USD9000 | PASS | S01;S03 |
| Q03 | Account B close | USD1500 | USD1500 | PASS | S02;S03 |
| Q04 | Entity close | USD10500 | USD10500 | PASS | S01;S02;S03 |
| Q05 | External receipts excluding returns | USD42500 | USD42500 | PASS | S01;S08;S09 |
| Q06 | Supplier gross and linked net | USD40000 gross; USD36600 net | USD40000 / USD36600 | PASS | S01;S08 |
| Q07 | T02 invoice difference | USD1000 | USD1000 | PASS | S01;S05 |
| Q08 | T02 unreversed | USD9000 | USD9000 | PASS | S01;S08 |
| Q09 | Supported supplier gross | USD19800 of USD40000; 49.5% | USD19800 / USD40000 = 49.5% | PASS | S01;S06 |
| Q10 | Unsupported conclusion gate | No universal explanation or illicit-purpose assertion | Bounded unresolved subset retained | PASS | S01;S04;S06;S10 |
| Q11 | Purpose gates | T02 and T08 remain unresolved | HOLD_EVIDENCE | REVIEW REQUIRED | S01;S05;S10 |
| Q12 | Human disposition | No invented approval | NOT_RECORDED | NOT RECORDED | S12 |

## Complete expected report narrative

This is the populated fictional report body, in the exact eight-section order. It gives a complete narrative answer while the domain registers above supply all underlying rows. Adaptation requires new source-based paragraphs, not cosmetic changes to these conclusions.

### Decision questions and current assessment

The two-account ledger reconciles to USD10500, but T02 amount/beneficiary support and T08 purpose remain unresolved. Supported supplier activity totals USD19800 of USD40000 gross; uncertainty must remain bounded to the relevant subset.

The package recommends targeted evidence review. It does not conclude that funds were illicit, that an account should close or that a SAR must be filed.

### Scope, chronology method, and coverage

Thirty raw representations include twenty-seven posted account entries, one exact duplicate, one unexecuted instruction and one pending item. Three posted entries are mirror legs of own-account transfers, leaving twenty-four canonical transfers. Event timestamps describe posting; source availability and customer explanations remain separate chronology layers.

### Findings and contradictions

INV-F01: T02 is USD11000 to Q while INV-A is USD10000 naming R. The USD1000 difference and beneficiary bridge are separate unresolved questions.

INV-F02: T08 paid U USD6000; a linked USD1000 return leaves USD5000 unreversed. Contract-C is inaccessible. This does not establish illicit purpose or confirmed loss.

INV-F03: T02 followed T01 by one hour. Pre-existing USD5000 means temporal order does not prove that the entire debit came from T01.

INV-F04: Four matched invoice and delivery sets support USD19800 of USD40000 gross supplier debits, or 49.5%. Unreconciled value is not automatically suspicious value.

### Chronology and funds movement

Account A: USD5000 + USD46900 credits - USD42900 debits = USD9000. Account B: USD1000 + USD1500 credits - USD1000 debits = USD1500. Entity close is USD10500 with zero balance difference.

External customer receipts are USD42500; supplier debits are USD40000 gross and USD36600 after USD3400 of explicitly linked returns. Cash USD1000 and fees USD400 remain separate. Own-account transfers of USD2500 canonical value cancel at entity level.

### Competing hypothesis tests and decision gates

CL01 remains unresolved because INV-A differs by USD1000 and names R rather than Q. CL02 is contradicted: T03 returns only USD2000 of T02 USD11000. CL03 is contradicted by matched B/D/E/F records totaling USD19800. CL04 remains unresolved while Contract-C is inaccessible. CL05 is contradicted by the A/B ownership and mirror records. CL06 supports timing only.

RQ01/RQ02/RQ05 remain proposed or inaccessible; RQ03/RQ04 are satisfied only for their bounded scope. D02/D03 hold purpose decisions and D04 records no actual human disposition.

### Evidence inventory and provenance

S01–S12 preserve source origin, availability and limits. The encrypted contract is not treated as reviewed evidence. Customer explanation remains Reported; the invoice face text is Observed without implying actual performance. Duplicate ledger representations are not independent corroboration.

### Proposed investigative actions

Obtain the Q/R beneficiary bridge, USD1000 difference explanation and delivery support for T02. Obtain readable Contract-C and transaction-specific support for T08. Preserve matched invoice/delivery evidence and the partial returns. No request has been sent by this fixture.

### Limitations, quality checks, and reviewer decision

All subjects, records and criteria are fictional; no legal or filing determination is made.

Contract-C is inaccessible; beneficiary Q/R linkage and T02 amount difference remain unresolved.

Book reconciliation does not establish source attribution, economic purpose, loss or misconduct.

No actual human decision, external request or approval is recorded.

Fixture arithmetic checks pass; material purpose gates remain REVIEW REQUIRED and human disposition NOT RECORDED.

### Complete finding statements

**INV-F01 — T02 invoice fails amount and beneficiary reconciliation.** Severity `MEDIUM`; confidence `HIGH`; claim class `Observed`. Evidence: S01, S04, S05. T02 is USD11000 to Q while INV-A is USD10000 naming R. The USD1000 difference and beneficiary bridge are separate unresolved questions. Proposed action: Obtain targeted amount, beneficiary and delivery support; retain the customer explanation as Reported. Actual human decision: NOT_RECORDED.

**INV-F02 — T08 purpose remains unsupported within the supplied evidence.** Severity `MEDIUM`; confidence `MODERATE`; claim class `Inferred`. Evidence: S01, S08, S10. T08 paid U USD6000; a linked USD1000 return leaves USD5000 unreversed. Contract-C is inaccessible. This does not establish illicit purpose or confirmed loss. Proposed action: Request a readable contract and transaction-specific purpose evidence; preserve the return as counterevidence. Actual human decision: NOT_RECORDED.

**INV-F03 — Rapid onward movement is observable but source attribution is unproven.** Severity `LOW`; confidence `HIGH`; claim class `Observed`. Evidence: S01, S04, S05. T02 followed T01 by one hour. Pre-existing USD5000 means temporal order does not prove that the entire debit came from T01. Proposed action: Record timing separately from source attribution and economic explanation. Actual human decision: NOT_RECORDED.

**INV-F04 — The unresolved subset must not erase supported supplier activity.** Severity `LOW`; confidence `HIGH`; claim class `Observed`. Evidence: S01, S06. Four matched invoice and delivery sets support USD19800 of USD40000 gross supplier debits, or 49.5%. Unreconciled value is not automatically suspicious value. Proposed action: Keep favorable evidence and denominator definitions in every output. Actual human decision: NOT_RECORDED.

## Standalone in-session arithmetic and table reproduction

This block uses only the Python standard library and printed fixture inputs. Run it only if an approved Python capability already exists in the current session; no terminal, installation, repository file or network is required. It independently derives the quantitative tables, checks count/amount/denominator invariants and exposes CHECKED_TABLES for exact row comparison. Successful arithmetic does not validate every qualitative judgment or establish real human authorization.

<!-- FIXTURE_CHECK:START -->
```python
from decimal import Decimal
POSTINGS = [('T01', '2026-09-02T10:00:00-04:00', 'P', 'A', 12000, None, 'Receipt described by customer as equipment sale'), ('T02', '2026-09-02T11:00:00-04:00', 'A', 'Q', 11000, None, 'Equipment-purpose explanation; invoice names R'), ('T03', '2026-09-04T09:00:00-04:00', 'Q', 'A', 2000, 'T02', 'Explicit partial return of T02'), ('T04', '2026-09-05T09:00:00-04:00', 'P2', 'A', 8000, None, 'Second customer receipt'), ('T05', '2026-09-05T12:00:00-04:00', 'A', 'R', 7500, None, 'Invoice INV-B and delivery receipt support purpose'), ('T06', '2026-09-06T09:00:00-04:00', 'A', 'B', 500, None, 'Same-entity account transfer; both books supplied'), ('T07', '2026-09-08T09:00:00-04:00', 'P3', 'A', 6000, None, 'Customer receipt; remitter identity supported'), ('T08', '2026-09-08T09:20:00-04:00', 'A', 'U', 6000, None, 'Purpose explanation absent'), ('T09', '2026-09-10T10:00:00-04:00', 'P', 'A', 3000, None, 'Additional customer receipt'), ('T10', '2026-09-10T14:00:00-04:00', 'A', 'Q', 2500, None, 'Customer says invoice INV-C settlement'), ('T11', '2026-09-10T16:00:00-04:00', 'A', 'BANK', 100, None, 'Posted service fee'), ('T12', '2026-09-12T09:00:00-04:00', 'P4', 'A', 7000, None, 'Customer receipt'), ('T13', '2026-09-12T10:00:00-04:00', 'A', 'R', 6800, None, 'Invoice INV-D full amount supported'), ('T14', '2026-09-13T10:00:00-04:00', 'R', 'A', 400, 'T13', 'Explicit partial return of T13'), ('T15', '2026-09-14T09:00:00-04:00', 'A', 'B', 1000, None, 'Same-entity transfer; both books supplied'), ('T16', '2026-09-15T09:00:00-04:00', 'B', 'A', 1000, None, 'Same-entity return transfer; not a supplier refund'), ('T17', '2026-09-17T09:00:00-04:00', 'P5', 'A', 5000, None, 'Customer receipt'), ('T18', '2026-09-17T11:00:00-04:00', 'A', 'V', 4000, None, 'Invoice INV-E and delivery support purpose'), ('T19', '2026-09-18T10:00:00-04:00', 'A', 'CASH', 1000, None, 'Cash withdrawal; ultimate use uncorroborated'), ('T20', '2026-09-21T09:00:00-04:00', 'P5', 'A', 1500, None, 'Customer receipt'), ('T21', '2026-09-21T12:00:00-04:00', 'A', 'V', 1500, None, 'Invoice INV-F and delivery support purpose'), ('T22', '2026-09-23T10:00:00-04:00', 'U', 'A', 1000, 'T08', 'Explicit partial return of T08'), ('T23', '2026-09-24T09:00:00-04:00', 'A', 'Q', 700, None, 'Adjustment description; supporting memo absent'), ('T24', '2026-09-25T16:00:00-04:00', 'A', 'BANK', 300, None, 'Posted service fee')]
# Raw posted mirror rows belong to B; they are not new economic transfers.
MIRRORS = [('T06-B','T06',500),('T15-B','T15',1000),('T16-B','T16',-1000)]
NONCANONICAL = [('RAW-DUP-T01','DUPLICATE',12000),('RAW-INSTR-T02','INSTRUCTION',11000),('RAW-PENDING','PENDING',2000)]
assert len(POSTINGS)+len(MIRRORS)+len(NONCANONICAL)==30
assert len(POSTINGS)+len(MIRRORS)==27
balance=5000; timeline=[]
for eid,dt,fr,to,amount,linked,note in POSTINGS:
    balance += amount if to=='A' else -amount
    refs='S01'+(';S08' if linked else '')+(';S09' if fr=='B' or to=='B' else '')
    timeline.append([eid,dt,fr,to,amount,'USD',linked,balance,refs,'Observed',note])
credits=sum(x[4] for x in POSTINGS if x[3]=='A')
debits=sum(x[4] for x in POSTINGS if x[2]=='A')
bcredits=sum(x[2] for x in MIRRORS if x[2]>0)
bdebits=-sum(x[2] for x in MIRRORS if x[2]<0)
assert (credits,debits,bcredits,bdebits)==(46900,42900,1500,1000)
assert (balance,1000+bcredits-bdebits)==(9000,1500)
rows=[['A',5000,credits,debits,5000+credits-debits,9000,5000+credits-debits-9000,'S01;S03'],['B',1000,bcredits,bdebits,1000+bcredits-bdebits,1500,1000+bcredits-bdebits-1500,'S02;S03']]
suppliers={'Q','R','U','V'}
gross=sum(x[4] for x in POSTINGS if x[2]=='A' and x[3] in suppliers)
returns=sum(x[4] for x in POSTINGS if x[5] is not None)
receipts=sum(x[4] for x in POSTINGS if x[2] in {'P','P2','P3','P4','P5'})
own=sum(x[4] for x in POSTINGS if {x[2],x[3]}=={'A','B'})
supported=sum(x[4] for x in POSTINGS if x[0] in {'T05','T13','T18','T21'})
assert (gross,returns,receipts,own,supported)==(40000,3400,42500,2500,19800)
assert gross-returns==36600 and Decimal(supported)/Decimal(gross)==Decimal('0.495')
assert 6000+receipts+returns-gross-1000-400==10500
assert 11000-2000==9000 and 11000-10000==1000
assert (max(0,11000-5000),min(12000,11000))==(6000,11000)
# A full linked replacement return changes arithmetic, not beneficiary corroboration.
assert 11000-11000==0 and 40000-(11000+400+1000)==27600
# Infeasible over-return must be detected, not represented as negative loss.
assert 2000+10000>11000
CHECKED_TABLES={'CaseTimeline':timeline,'AccountBalances':rows}
print('PASS: raw30; posted27; canonical24; closes9000/1500; gross40000; returns3400; net36600; supported49.5%')
```
<!-- FIXTURE_CHECK:END -->
