# Network and Funds Flow Review — complete worked case

**Fictional training case. All identifiers, parties, amounts, policy criteria, reviewers and outcomes below are synthetic.** The fully populated case demonstrates analytical method and output structure; it is not a completed operational review. All facts needed for its arithmetic are printed below.

## Raw graph fixture and source coverage

Each row is one executed transfer in strictly increasing hour order, starting Sep 02, 2026 at 9:00 AM ET. Hour index 1 is the first event, hour 24 the last. Every amount is native USD. A1 opening 1000 and closing 500; A2 opening 500 and closing 1000. N02 verifies both accounts belong to Entity-A. All other entity labels are recorded counterparties, with no verified beneficial ownership claim.

| edge_id | sender | receiver | amount_usd | explicit_return_of |
| --- | --- | --- | --- | --- |
| E01 | P | A1 | 10000 | null |
| E02 | Q | A1 | 8000 | null |
| E03 | A1 | C | 12000 | null |
| E04 | A1 | A2 | 4000 | null |
| E05 | A2 | D | 3000 | null |
| E06 | R | A1 | 6000 | null |
| E07 | A1 | C | 5000 | null |
| E08 | C | A1 | 1000 | E03 |
| E09 | A1 | E | 2000 | null |
| E10 | E | F | 1500 | null |
| E11 | F | A1 | 1000 | null |
| E12 | A1 | P | 2000 | null |
| E13 | P | A1 | 1500 | null |
| E14 | Q | A1 | 3000 | null |
| E15 | A1 | D | 4500 | null |
| E16 | A2 | A1 | 500 | null |
| E17 | A1 | F | 1000 | null |
| E18 | F | D | 500 | null |
| E19 | R | A1 | 2000 | null |
| E20 | A1 | C | 2500 | null |
| E21 | D | A1 | 1000 | E15 |
| E22 | A1 | E | 1500 | null |
| E23 | E | A1 | 500 | null |
| E24 | A1 | C | 500 | null |

The 28 raw representations comprise these 24 transfers, one duplicate export of E01, one unexecuted instruction describing E03, one pending 250 transfer and one second account-book representation of E04. Those four representations do not create new economic edges. N03 supplies only the explicit links E08→E03 and E21→E15. N04 supplies E10 and E18 as onward extracts, without complete E/F account histories. N07 is a fictional customer statement that the transfers relate to ordinary business settlements; it supplies no exact source-allocation evidence. N06 GP-1 specifies fungible, nonnegative available-balance bounds for the complete pre-E03 A1 pool and declares FIFO/proportional conventions illustrative only.

The complete pre-E03 pool is opening 1000, P receipt 10000 and Q receipt 8000, total 19000. The target debit is 12000. No other credit, debit, overdraft or restricted balance occurs before E03 in this fixture. These are explicit modeling facts; they must not be assumed in a real case with incomplete records.

## Complete edge-by-edge reconstruction

### E01 — hour 1, P to A1

The executed leg is **USD 10,000.00**. After this edge, observed graph-wide leg value totals **USD 10,000.00**. Entity-A boundary inflow to this point is **USD 10,000.00**, while boundary outflow is **USD 0.00**. The review-account balances are A1 **USD 11,000.00** and A2 **USD 500.00**, compared with pre-edge values **USD 1,000.00** and **USD 500.00** respectively.

This edge crosses into the verified review perimeter. Record its immediate sender and positive native amount. Its inclusion in all boundary inflow does not automatically make it new customer-source capital: returns, repeated funds and cycle inflows can also cross inward. Apply the specifically named subset definition before using it in a fan-in or source-receipt metric.

The boundary classification above uses verified A1/A2 grouping only.

### E02 — hour 2, Q to A1

The executed leg is **USD 8,000.00**. After this edge, observed graph-wide leg value totals **USD 18,000.00**. Entity-A boundary inflow to this point is **USD 18,000.00**, while boundary outflow is **USD 0.00**. The review-account balances are A1 **USD 19,000.00** and A2 **USD 500.00**, compared with pre-edge values **USD 11,000.00** and **USD 500.00** respectively.

This edge crosses into the verified review perimeter. Record its immediate sender and positive native amount. Its inclusion in all boundary inflow does not automatically make it new customer-source capital: returns, repeated funds and cycle inflows can also cross inward. Apply the specifically named subset definition before using it in a fan-in or source-receipt metric.

The boundary classification above uses verified A1/A2 grouping only.

### E03 — hour 3, A1 to C

The executed leg is **USD 12,000.00**. After this edge, observed graph-wide leg value totals **USD 30,000.00**. Entity-A boundary inflow to this point is **USD 18,000.00**, while boundary outflow is **USD 12,000.00**. The review-account balances are A1 **USD 7,000.00** and A2 **USD 500.00**, compared with pre-edge values **USD 19,000.00** and **USD 500.00** respectively.

This edge crosses out of the verified review perimeter. Preserve the immediate recipient as recorded and separate transfer count from distinct-recipient count. Source attribution requires the funding pool and any linkage evidence at the time of this debit. A directed edge alone cannot establish ultimate receipt, purpose or control of the recipient.

This is the worked attribution target. The pre-edge A1 pool is 19000: opening 1000, P10000 and Q8000. The 12000 debit requires at least 3000 from P but can use up to 10000 from P. The exact assignment remains unresolved without an additional justified tracing assumption or linkage source.

### E04 — hour 4, A1 to A2

The executed leg is **USD 4,000.00**. After this edge, observed graph-wide leg value totals **USD 34,000.00**. Entity-A boundary inflow to this point is **USD 18,000.00**, while boundary outflow is **USD 12,000.00**. The review-account balances are A1 **USD 3,000.00** and A2 **USD 4,500.00**, compared with pre-edge values **USD 7,000.00** and **USD 500.00** respectively.

This is a verified own-account transfer. It changes the two account balances in opposite directions but contributes zero to consolidated external inflow and outflow. Keep the edge for account chronology and transfer-count purposes. The amount remains part of graph-wide leg value, which is why that measure cannot be relabeled external turnover.

The boundary classification above uses verified A1/A2 grouping only.

### E05 — hour 5, A2 to D

The executed leg is **USD 3,000.00**. After this edge, observed graph-wide leg value totals **USD 37,000.00**. Entity-A boundary inflow to this point is **USD 18,000.00**, while boundary outflow is **USD 15,000.00**. The review-account balances are A1 **USD 3,000.00** and A2 **USD 1,500.00**, compared with pre-edge values **USD 3,000.00** and **USD 4,500.00** respectively.

This edge crosses out of the verified review perimeter. Preserve the immediate recipient as recorded and separate transfer count from distinct-recipient count. Source attribution requires the funding pool and any linkage evidence at the time of this debit. A directed edge alone cannot establish ultimate receipt, purpose or control of the recipient.

The boundary classification above uses verified A1/A2 grouping only.

### E06 — hour 6, R to A1

The executed leg is **USD 6,000.00**. After this edge, observed graph-wide leg value totals **USD 43,000.00**. Entity-A boundary inflow to this point is **USD 24,000.00**, while boundary outflow is **USD 15,000.00**. The review-account balances are A1 **USD 9,000.00** and A2 **USD 1,500.00**, compared with pre-edge values **USD 3,000.00** and **USD 1,500.00** respectively.

This edge crosses into the verified review perimeter. Record its immediate sender and positive native amount. Its inclusion in all boundary inflow does not automatically make it new customer-source capital: returns, repeated funds and cycle inflows can also cross inward. Apply the specifically named subset definition before using it in a fan-in or source-receipt metric.

The boundary classification above uses verified A1/A2 grouping only.

### E07 — hour 7, A1 to C

The executed leg is **USD 5,000.00**. After this edge, observed graph-wide leg value totals **USD 48,000.00**. Entity-A boundary inflow to this point is **USD 24,000.00**, while boundary outflow is **USD 20,000.00**. The review-account balances are A1 **USD 4,000.00** and A2 **USD 1,500.00**, compared with pre-edge values **USD 9,000.00** and **USD 1,500.00** respectively.

This edge crosses out of the verified review perimeter. Preserve the immediate recipient as recorded and separate transfer count from distinct-recipient count. Source attribution requires the funding pool and any linkage evidence at the time of this debit. A directed edge alone cannot establish ultimate receipt, purpose or control of the recipient.

The boundary classification above uses verified A1/A2 grouping only.

### E08 — hour 8, C to A1

The executed leg is **USD 1,000.00**. After this edge, observed graph-wide leg value totals **USD 49,000.00**. Entity-A boundary inflow to this point is **USD 25,000.00**, while boundary outflow is **USD 20,000.00**. The review-account balances are A1 **USD 5,000.00** and A2 **USD 1,500.00**, compared with pre-edge values **USD 4,000.00** and **USD 1,500.00** respectively.

The explicit source reference links this return to E03. Preserve both edges and calculate a local net only for that parent. It remains a separate inbound boundary event and can affect temporal paths. The linkage does not establish the original economic purpose or authorize treating every opposite-direction edge as a refund.

The boundary classification above uses verified A1/A2 grouping only.

### E09 — hour 9, A1 to E

The executed leg is **USD 2,000.00**. After this edge, observed graph-wide leg value totals **USD 51,000.00**. Entity-A boundary inflow to this point is **USD 25,000.00**, while boundary outflow is **USD 22,000.00**. The review-account balances are A1 **USD 3,000.00** and A2 **USD 1,500.00**, compared with pre-edge values **USD 5,000.00** and **USD 1,500.00** respectively.

This edge crosses out of the verified review perimeter. Preserve the immediate recipient as recorded and separate transfer count from distinct-recipient count. Source attribution requires the funding pool and any linkage evidence at the time of this debit. A directed edge alone cannot establish ultimate receipt, purpose or control of the recipient.

This is one leg of the ordered A1-E-F-A1 cycle. Keep the three individual amounts 2000,1500,1000 and their order. The minimum capacity 1000 differs from leg sum 4500, while actual same-funds attribution may be zero under the supplied partial visibility.

### E10 — hour 10, E to F

The executed leg is **USD 1,500.00**. After this edge, observed graph-wide leg value totals **USD 52,500.00**. Entity-A boundary inflow to this point is **USD 25,000.00**, while boundary outflow is **USD 22,000.00**. The review-account balances are A1 **USD 3,000.00** and A2 **USD 1,500.00**, compared with pre-edge values **USD 3,000.00** and **USD 1,500.00** respectively.

This supplied onward extract connects two external nodes. It contributes to graph-wide leg value and possible paths, but neither side crosses Entity-A’s account boundary. Complete external-node balances are unavailable, so do not use this isolated record to infer all funding sources or complete onward disposition.

This is one leg of the ordered A1-E-F-A1 cycle. Keep the three individual amounts 2000,1500,1000 and their order. The minimum capacity 1000 differs from leg sum 4500, while actual same-funds attribution may be zero under the supplied partial visibility.

### E11 — hour 11, F to A1

The executed leg is **USD 1,000.00**. After this edge, observed graph-wide leg value totals **USD 53,500.00**. Entity-A boundary inflow to this point is **USD 26,000.00**, while boundary outflow is **USD 22,000.00**. The review-account balances are A1 **USD 4,000.00** and A2 **USD 1,500.00**, compared with pre-edge values **USD 3,000.00** and **USD 1,500.00** respectively.

This edge crosses into the verified review perimeter. Record its immediate sender and positive native amount. Its inclusion in all boundary inflow does not automatically make it new customer-source capital: returns, repeated funds and cycle inflows can also cross inward. Apply the specifically named subset definition before using it in a fan-in or source-receipt metric.

This is one leg of the ordered A1-E-F-A1 cycle. Keep the three individual amounts 2000,1500,1000 and their order. The minimum capacity 1000 differs from leg sum 4500, while actual same-funds attribution may be zero under the supplied partial visibility.

### E12 — hour 12, A1 to P

The executed leg is **USD 2,000.00**. After this edge, observed graph-wide leg value totals **USD 55,500.00**. Entity-A boundary inflow to this point is **USD 26,000.00**, while boundary outflow is **USD 24,000.00**. The review-account balances are A1 **USD 2,000.00** and A2 **USD 1,500.00**, compared with pre-edge values **USD 4,000.00** and **USD 1,500.00** respectively.

This edge crosses out of the verified review perimeter. Preserve the immediate recipient as recorded and separate transfer count from distinct-recipient count. Source attribution requires the funding pool and any linkage evidence at the time of this debit. A directed edge alone cannot establish ultimate receipt, purpose or control of the recipient.

The boundary classification above uses verified A1/A2 grouping only.

### E13 — hour 13, P to A1

The executed leg is **USD 1,500.00**. After this edge, observed graph-wide leg value totals **USD 57,000.00**. Entity-A boundary inflow to this point is **USD 27,500.00**, while boundary outflow is **USD 24,000.00**. The review-account balances are A1 **USD 3,500.00** and A2 **USD 1,500.00**, compared with pre-edge values **USD 2,000.00** and **USD 1,500.00** respectively.

This edge crosses into the verified review perimeter. Record its immediate sender and positive native amount. Its inclusion in all boundary inflow does not automatically make it new customer-source capital: returns, repeated funds and cycle inflows can also cross inward. Apply the specifically named subset definition before using it in a fan-in or source-receipt metric.

The boundary classification above uses verified A1/A2 grouping only.

### E14 — hour 14, Q to A1

The executed leg is **USD 3,000.00**. After this edge, observed graph-wide leg value totals **USD 60,000.00**. Entity-A boundary inflow to this point is **USD 30,500.00**, while boundary outflow is **USD 24,000.00**. The review-account balances are A1 **USD 6,500.00** and A2 **USD 1,500.00**, compared with pre-edge values **USD 3,500.00** and **USD 1,500.00** respectively.

This edge crosses into the verified review perimeter. Record its immediate sender and positive native amount. Its inclusion in all boundary inflow does not automatically make it new customer-source capital: returns, repeated funds and cycle inflows can also cross inward. Apply the specifically named subset definition before using it in a fan-in or source-receipt metric.

The boundary classification above uses verified A1/A2 grouping only.

### E15 — hour 15, A1 to D

The executed leg is **USD 4,500.00**. After this edge, observed graph-wide leg value totals **USD 64,500.00**. Entity-A boundary inflow to this point is **USD 30,500.00**, while boundary outflow is **USD 28,500.00**. The review-account balances are A1 **USD 2,000.00** and A2 **USD 1,500.00**, compared with pre-edge values **USD 6,500.00** and **USD 1,500.00** respectively.

This edge crosses out of the verified review perimeter. Preserve the immediate recipient as recorded and separate transfer count from distinct-recipient count. Source attribution requires the funding pool and any linkage evidence at the time of this debit. A directed edge alone cannot establish ultimate receipt, purpose or control of the recipient.

The boundary classification above uses verified A1/A2 grouping only.

### E16 — hour 16, A2 to A1

The executed leg is **USD 500.00**. After this edge, observed graph-wide leg value totals **USD 65,000.00**. Entity-A boundary inflow to this point is **USD 30,500.00**, while boundary outflow is **USD 28,500.00**. The review-account balances are A1 **USD 2,500.00** and A2 **USD 1,000.00**, compared with pre-edge values **USD 2,000.00** and **USD 1,500.00** respectively.

This is a verified own-account transfer. It changes the two account balances in opposite directions but contributes zero to consolidated external inflow and outflow. Keep the edge for account chronology and transfer-count purposes. The amount remains part of graph-wide leg value, which is why that measure cannot be relabeled external turnover.

The boundary classification above uses verified A1/A2 grouping only.

### E17 — hour 17, A1 to F

The executed leg is **USD 1,000.00**. After this edge, observed graph-wide leg value totals **USD 66,000.00**. Entity-A boundary inflow to this point is **USD 30,500.00**, while boundary outflow is **USD 29,500.00**. The review-account balances are A1 **USD 1,500.00** and A2 **USD 1,000.00**, compared with pre-edge values **USD 2,500.00** and **USD 1,000.00** respectively.

This edge crosses out of the verified review perimeter. Preserve the immediate recipient as recorded and separate transfer count from distinct-recipient count. Source attribution requires the funding pool and any linkage evidence at the time of this debit. A directed edge alone cannot establish ultimate receipt, purpose or control of the recipient.

The boundary classification above uses verified A1/A2 grouping only.

### E18 — hour 18, F to D

The executed leg is **USD 500.00**. After this edge, observed graph-wide leg value totals **USD 66,500.00**. Entity-A boundary inflow to this point is **USD 30,500.00**, while boundary outflow is **USD 29,500.00**. The review-account balances are A1 **USD 1,500.00** and A2 **USD 1,000.00**, compared with pre-edge values **USD 1,500.00** and **USD 1,000.00** respectively.

This supplied onward extract connects two external nodes. It contributes to graph-wide leg value and possible paths, but neither side crosses Entity-A’s account boundary. Complete external-node balances are unavailable, so do not use this isolated record to infer all funding sources or complete onward disposition.

The boundary classification above uses verified A1/A2 grouping only.

### E19 — hour 19, R to A1

The executed leg is **USD 2,000.00**. After this edge, observed graph-wide leg value totals **USD 68,500.00**. Entity-A boundary inflow to this point is **USD 32,500.00**, while boundary outflow is **USD 29,500.00**. The review-account balances are A1 **USD 3,500.00** and A2 **USD 1,000.00**, compared with pre-edge values **USD 1,500.00** and **USD 1,000.00** respectively.

This edge crosses into the verified review perimeter. Record its immediate sender and positive native amount. Its inclusion in all boundary inflow does not automatically make it new customer-source capital: returns, repeated funds and cycle inflows can also cross inward. Apply the specifically named subset definition before using it in a fan-in or source-receipt metric.

The boundary classification above uses verified A1/A2 grouping only.

### E20 — hour 20, A1 to C

The executed leg is **USD 2,500.00**. After this edge, observed graph-wide leg value totals **USD 71,000.00**. Entity-A boundary inflow to this point is **USD 32,500.00**, while boundary outflow is **USD 32,000.00**. The review-account balances are A1 **USD 1,000.00** and A2 **USD 1,000.00**, compared with pre-edge values **USD 3,500.00** and **USD 1,000.00** respectively.

This edge crosses out of the verified review perimeter. Preserve the immediate recipient as recorded and separate transfer count from distinct-recipient count. Source attribution requires the funding pool and any linkage evidence at the time of this debit. A directed edge alone cannot establish ultimate receipt, purpose or control of the recipient.

The boundary classification above uses verified A1/A2 grouping only.

### E21 — hour 21, D to A1

The executed leg is **USD 1,000.00**. After this edge, observed graph-wide leg value totals **USD 72,000.00**. Entity-A boundary inflow to this point is **USD 33,500.00**, while boundary outflow is **USD 32,000.00**. The review-account balances are A1 **USD 2,000.00** and A2 **USD 1,000.00**, compared with pre-edge values **USD 1,000.00** and **USD 1,000.00** respectively.

The explicit source reference links this return to E15. Preserve both edges and calculate a local net only for that parent. It remains a separate inbound boundary event and can affect temporal paths. The linkage does not establish the original economic purpose or authorize treating every opposite-direction edge as a refund.

The boundary classification above uses verified A1/A2 grouping only.

### E22 — hour 22, A1 to E

The executed leg is **USD 1,500.00**. After this edge, observed graph-wide leg value totals **USD 73,500.00**. Entity-A boundary inflow to this point is **USD 33,500.00**, while boundary outflow is **USD 33,500.00**. The review-account balances are A1 **USD 500.00** and A2 **USD 1,000.00**, compared with pre-edge values **USD 2,000.00** and **USD 1,000.00** respectively.

This edge crosses out of the verified review perimeter. Preserve the immediate recipient as recorded and separate transfer count from distinct-recipient count. Source attribution requires the funding pool and any linkage evidence at the time of this debit. A directed edge alone cannot establish ultimate receipt, purpose or control of the recipient.

The boundary classification above uses verified A1/A2 grouping only.

### E23 — hour 23, E to A1

The executed leg is **USD 500.00**. After this edge, observed graph-wide leg value totals **USD 74,000.00**. Entity-A boundary inflow to this point is **USD 34,000.00**, while boundary outflow is **USD 33,500.00**. The review-account balances are A1 **USD 1,000.00** and A2 **USD 1,000.00**, compared with pre-edge values **USD 500.00** and **USD 1,000.00** respectively.

This edge crosses into the verified review perimeter. Record its immediate sender and positive native amount. Its inclusion in all boundary inflow does not automatically make it new customer-source capital: returns, repeated funds and cycle inflows can also cross inward. Apply the specifically named subset definition before using it in a fan-in or source-receipt metric.

The boundary classification above uses verified A1/A2 grouping only.

### E24 — hour 24, A1 to C

The executed leg is **USD 500.00**. After this edge, observed graph-wide leg value totals **USD 74,500.00**. Entity-A boundary inflow to this point is **USD 34,000.00**, while boundary outflow is **USD 34,000.00**. The review-account balances are A1 **USD 500.00** and A2 **USD 1,000.00**, compared with pre-edge values **USD 1,000.00** and **USD 1,000.00** respectively.

This edge crosses out of the verified review perimeter. Preserve the immediate recipient as recorded and separate transfer count from distinct-recipient count. Source attribution requires the funding pool and any linkage evidence at the time of this debit. A directed edge alone cannot establish ultimate receipt, purpose or control of the recipient.

The boundary classification above uses verified A1/A2 grouping only.

## Fully populated expected domain outputs

These are the complete expected base-case records. They are not selected examples. Preserve every row when generating the report, workbook and dashboard. The raw facts above and the independent checks below explain the calculations; descriptive decisions additionally require the methods and gates in files 03–04.

### Nodes

| node_id | node_type | entity_id | identity_basis | opening_usd | evidence_ids | scope_limit |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | ACCOUNT | ENTITY-A | VERIFIED | 1000 | N01;N02 | Review account; complete in-period ledger |
| A2 | ACCOUNT | ENTITY-A | VERIFIED | 500 | N01;N02 | Same entity as A1; complete ledger |
| P | COUNTERPARTY | ENTITY-P | RECORDED | null | N01 | Recorded remitter/beneficiary; no beneficial-owner assertion |
| Q | COUNTERPARTY | ENTITY-Q | RECORDED | null | N01 | Recorded remitter; other activity outside scope |
| R | COUNTERPARTY | ENTITY-R | RECORDED | null | N01 | Recorded remitter; other activity outside scope |
| C | COUNTERPARTY | ENTITY-C | RECORDED | null | N01;N03 | Direct counterparty with one linked return |
| D | COUNTERPARTY | ENTITY-D | RECORDED | null | N01;N03 | Direct counterparty with one linked return |
| E | COUNTERPARTY | ENTITY-E | RECORDED | null | N01;N04 | Additional supplied onward record; complete ledger unavailable |
| F | COUNTERPARTY | ENTITY-F | RECORDED | null | N01;N04 | Additional supplied onward record; complete ledger unavailable |

### EconomicEdges

| edge_id | hour_index | from_node | to_node | amount_usd | currency | own_transfer | return_of | evidence_ids | identity_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E01 | 1 | P | A1 | 10000 | USD | false | null | N01 | RECORDED |
| E02 | 2 | Q | A1 | 8000 | USD | false | null | N01 | RECORDED |
| E03 | 3 | A1 | C | 12000 | USD | false | null | N01 | RECORDED |
| E04 | 4 | A1 | A2 | 4000 | USD | true | null | N01 | RECORDED |
| E05 | 5 | A2 | D | 3000 | USD | false | null | N01 | RECORDED |
| E06 | 6 | R | A1 | 6000 | USD | false | null | N01 | RECORDED |
| E07 | 7 | A1 | C | 5000 | USD | false | null | N01 | RECORDED |
| E08 | 8 | C | A1 | 1000 | USD | false | E03 | N01;N03 | RECORDED |
| E09 | 9 | A1 | E | 2000 | USD | false | null | N01 | RECORDED |
| E10 | 10 | E | F | 1500 | USD | false | null | N01;N04 | RECORDED |
| E11 | 11 | F | A1 | 1000 | USD | false | null | N01 | RECORDED |
| E12 | 12 | A1 | P | 2000 | USD | false | null | N01 | RECORDED |
| E13 | 13 | P | A1 | 1500 | USD | false | null | N01 | RECORDED |
| E14 | 14 | Q | A1 | 3000 | USD | false | null | N01 | RECORDED |
| E15 | 15 | A1 | D | 4500 | USD | false | null | N01 | RECORDED |
| E16 | 16 | A2 | A1 | 500 | USD | true | null | N01 | RECORDED |
| E17 | 17 | A1 | F | 1000 | USD | false | null | N01 | RECORDED |
| E18 | 18 | F | D | 500 | USD | false | null | N01;N04 | RECORDED |
| E19 | 19 | R | A1 | 2000 | USD | false | null | N01 | RECORDED |
| E20 | 20 | A1 | C | 2500 | USD | false | null | N01 | RECORDED |
| E21 | 21 | D | A1 | 1000 | USD | false | E15 | N01;N03 | RECORDED |
| E22 | 22 | A1 | E | 1500 | USD | false | null | N01 | RECORDED |
| E23 | 23 | E | A1 | 500 | USD | false | null | N01 | RECORDED |
| E24 | 24 | A1 | C | 500 | USD | false | null | N01 | RECORDED |

### BalanceChecks

| balance_id | perimeter | opening_usd | inflow_usd | outflow_usd | calculated_close_usd | supplied_close_usd | difference_usd | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B01 | A1 | 1000 | 34500 | 35000 | 500 | 500 | 0 | N01;N02 |
| B02 | A2 | 500 | 4000 | 3500 | 1000 | 1000 | 0 | N01;N02 |
| B03 | ENTITY-A | 1500 | 34000 | 34000 | 1500 | 1500 | 0 | N01;N02 |

### PatternTests

| pattern_id | pattern | edge_ids | measure_usd | count | interpretation | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | Distinct external source fan-in | E01;E02;E06;E13;E14;E19 | 30500 | 3 | P/Q/R contribute six transfers; three distinct immediate sources, no common-controller assertion | N01 |
| P02 | External outflow from entity accounts | E03;E05;E07;E09;E12;E15;E17;E20;E22;E24 | 34000 | 10 | Ten boundary exits to five distinct immediate recipients C,D,E,P,F; count field is transfer count, not recipient count | N01;N02 |
| P03 | Time-respecting A1-E-F-A1 cycle | E09;E10;E11 | 1000 | 3 | Minimum-edge capacity USD1000; attributable same-funds circulation range USD0–1000, not proven recycling | N01;N04 |
| P04 | Own-account movements | E04;E16 | 4500 | 2 | Two canonical transfers; collapse at entity boundary, retain account detail | N01;N02 |
| P05 | Explicit linked returns | E08;E21 | 2000 | 2 | Two posted returns reduce only their linked originals; other inbound cycle edges are not inferred refunds | N01;N03 |
| P06 | All canonical edge-leg value | E01–E24 | 74500 | 24 | Gross value across all observed legs; includes repetition, own transfers and onward extracts; not unique source capital | N01;N04 |

### AllocationBounds

| allocation_id | target_edge | source_group | available_usd | other_available_usd | debit_usd | lower_usd | upper_usd | basis | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AL01 | E03 | P receipt E01 | 10000 | 9000 | 12000 | 3000 | 10000 | Complete pre-E03 balance; fungible funding, no priority rule; range not point estimate | N01;N02;N06 |
| AL02 | E03 | Q receipt E02 | 8000 | 11000 | 12000 | 1000 | 8000 | Marginal bounds cannot all be combined arbitrarily; joint allocations must sum 12000 | N01;N02;N06 |
| AL03 | E03 | Opening balance A1 | 1000 | 18000 | 12000 | 0 | 1000 | Opening origin unknown; do not attribute it to P or Q | N01;N02;N06 |
| AL04 | E03 | Combined P+Q receipts | 18000 | 1000 | 12000 | 11000 | 12000 | Combined receipt lower bound differs from sum of individual minima | N01;N02;N06 |

### AttributionScenarios

| scenario_id | method | p_usd | q_usd | opening_usd | total_usd | status | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AS01 | Opening-first then FIFO receipts | 10000 | 1000 | 1000 | 12000 | ILLUSTRATIVE_ONLY | N01;N02;N06 |
| AS02 | Proportional available balance; cent residual to Q | 6315.79 | 5052.63 | 631.58 | 12000 | ILLUSTRATIVE_ONLY | N01;N02;N06 |
| AS03 | Minimum P feasible allocation | 3000 | 8000 | 1000 | 12000 | ILLUSTRATIVE_ONLY | N01;N02;N06 |
| AS04 | Maximum P feasible allocation | 10000 | 2000 | 0 | 12000 | ILLUSTRATIVE_ONLY | N01;N02;N06 |

### DecisionRecord

| decision_id | question | status | reason | evidence_ids |
| --- | --- | --- | --- | --- |
| D01 | A1/A2 belong to same entity | SUPPORTED | N02 verifies this grouping only; no extension to other nodes | N02 |
| D02 | P funded all E03 | CONTRADICTED | Under GP-1, P can fund at most USD10000 of E03 USD12000; exact contribution remains unresolved within USD3000–10000 | N01;N02;N06 |
| D03 | A1-E-F-A1 proves illicit cycling | PROHIBITED_INFERENCE | Topology and capacity do not prove same funds, purpose or knowledge | N01;N04 |
| D04 | USD74500 is unique suspicious capital | PROHIBITED_INFERENCE | It is gross value of repeated observed legs with different perimeter meanings | N01;N04 |
| D05 | Human disposition | NOT_RECORDED | No actual authorized decision supplied | N06 |

### ProcessQA

| check_id | check | expected | actual | result | evidence_ids |
| --- | --- | --- | --- | --- | --- |
| Q01 | Raw normalization | 28 raw to 24 edges | 24 | PASS | N01;N05 |
| Q02 | Nodes and unique keys | 9 nodes;24 unique edges | 9 / 24 | PASS | N01;N02 |
| Q03 | Gross edge value | USD74500 | USD74500 | PASS | N01 |
| Q04 | Entity external boundary | USD34000 in and USD34000 out | USD34000 / USD34000 | PASS | N01;N02 |
| Q05 | Complete-account balances | A1 USD500; A2 USD1000 | USD500 / USD1000 | PASS | N01;N02 |
| Q06 | P funding bound | USD3000–10000 | USD3000–10000 | PASS | N01;N02;N06 |
| Q07 | Cycle attribution bound | USD0–1000, subject to supplied visibility | USD0–1000 | PASS | N01;N04 |
| Q08 | Scenario allocations | Every row sums USD12000 | Four rows tie | PASS | N01;N02;N06 |
| Q09 | Unknown counterpart balances | No balance equations asserted for P/Q/R/C/D/E/F | Unassessed | PASS | N01;N04 |
| Q10 | Human decision | Not supplied | NOT_RECORDED | NOT RECORDED | N06 |

## Complete expected report narrative

This is the populated fictional report body, in the exact eight-section order. It gives a complete narrative answer while the domain registers above supply all underlying rows. Adaptation requires new source-based paragraphs, not cosmetic changes to these conclusions.

### Decision question and supported flow conclusions

The 24-transfer graph reconciles Entity-A to USD1500 closing balance. It supports a time-respecting cycle and concentrated flows, while P funding of E03 remains bounded at USD3000–10000 and same-funds cycle attribution at USD0–1000.

### Scope, perimeter and normalization

Fictional nine-node graph with 24 ordered posted transfers, complete A1/A2 ledgers, partial counterparty visibility and USD native units. No external investigation or identity discovery is performed.

Twenty-eight raw representations reduce to 24 canonical transfers. One duplicate, one instruction, one pending item and one own-transfer mirror are excluded as independent economic edges.

### Findings and attribution limits

NET-F01: E09/E10/E11 form a time-respecting A1-E-F-A1 cycle. Its minimum-edge capacity is USD1000, while attribution of the same funds may range from zero to USD1000.

NET-F02: All 24 canonical legs sum USD74500; Entity-A external inflow and outflow are each USD34000. Those measures answer different questions and cannot be labeled unique capital.

NET-F03: Immediately before E03, A1 contains opening 1000, P10000 and Q8000. P funding of the 12000 debit is bounded by 3000–10000 under fungible balance constraints.

### Nodes and canonical economic transfers

Nine nodes preserve A1/A2 as separate accounts within verified Entity-A. Other entity labels are recorded counterparties, without a beneficial ownership assertion. All 24 edges retain temporal order, positive native amount, return linkage and own-transfer flag.

### Balance equations, patterns and allocation bounds

A1 reconciles 1000+34500-35000=500; A2 reconciles 500+4000-3500=1000. Consolidated external inflow/outflow are both 34000; own transfers 4500 cancel. Gross edge-leg value 74500 is a different graph-wide measure.

P/Q/R provide six receipts totaling 30500. Five distinct external recipients receive ten Entity-A boundary debits totaling 34000. Explicit returns E08/E21 total 2000; E11/E23 are not inferred refunds.

Before E03, available balance is 19000. P bound is 3000–10000, Q1000–8000, opening 0–1000 and combinedP+Q11000–12000. The four feasible allocation scenarios each sum 12000; they are alternatives, not observed source tracing. The A1-E-F-A1 cycle capacity is 1000, with same-funds attribution 0–1000 under incomplete counterparty visibility.

### Evidence and identity provenance

N01/N02 establish supplied transfer and account grouping facts. N03 supplies explicit return references. N04 supplies only the stated onward extracts. N07 is a customer purpose statement and remains Reported. No source establishes illicit purpose.

### Proposed discriminating inquiries

If attribution affects a live decision, request complete relevant counterparty balance coverage, explicit remittance/settlement linkage and purpose documents. Keep the request proportionate to the disputed proposition; do not expand it into unrestricted identity discovery.

### Quality checks, limitations and human decision

All graph records and grouping evidence are fictional.

Only A1/A2 have complete balance coverage; external-node source attribution cannot be inferred from partial extracts.

A cycle does not prove same-funds circulation, common control, knowledge or illicit purpose.

Source allocation conventions are illustrative assumptions; marginal bounds are not freely combinable.

No authorized human disposition or external inquiry has occurred.

Fixture checks pass within their stated scope; actual human disposition remains NOT_RECORDED.

### Complete finding statements

**NET-F01 — Graph topology supports a cycle, with uncertain source allocation.** Severity `MEDIUM`; confidence `HIGH`; claim class `Observed`. Evidence: N01, N04. E09/E10/E11 form a time-respecting A1-E-F-A1 cycle. Its minimum-edge capacity is USD1000, while attribution of the same funds may range from zero to USD1000. Proposed action: Retain the cycle as a bounded pattern; request source/purpose evidence only if it affects a live decision. Actual human decision: NOT_RECORDED.

**NET-F02 — Gross leg value materially exceeds entity boundary flow.** Severity `LOW`; confidence `HIGH`; claim class `Observed`. Evidence: N01, N02, N04. All 24 canonical legs sum USD74500; Entity-A external inflow and outflow are each USD34000. Those measures answer different questions and cannot be labeled unique capital. Proposed action: Label every measure by perimeter, transfer grain and return treatment. Actual human decision: NOT_RECORDED.

**NET-F03 — P-to-E03 source attribution cannot be a single observed number.** Severity `MEDIUM`; confidence `HIGH`; claim class `Inferred`. Evidence: N01, N02, N06. Immediately before E03, A1 contains opening 1000, P10000 and Q8000. P funding of the 12000 debit is bounded by 3000–10000 under fungible balance constraints. Proposed action: Use bounds as the conclusion and retain FIFO/proportional values only as illustrative sensitivities. Actual human decision: NOT_RECORDED.

## Standalone in-session arithmetic and table reproduction

This block uses only the Python standard library and printed fixture inputs. Run it only if an approved Python capability already exists in the current session; no terminal, installation, repository file or network is required. It independently derives the quantitative tables, checks count/amount/denominator invariants and exposes CHECKED_TABLES for exact row comparison. Successful arithmetic does not validate every qualitative judgment or establish real human authorization.

<!-- FIXTURE_CHECK:START -->
```python
from decimal import Decimal, ROUND_HALF_UP
EDGES = [('E01', 'P', 'A1', 10000, None), ('E02', 'Q', 'A1', 8000, None), ('E03', 'A1', 'C', 12000, None), ('E04', 'A1', 'A2', 4000, None), ('E05', 'A2', 'D', 3000, None), ('E06', 'R', 'A1', 6000, None), ('E07', 'A1', 'C', 5000, None), ('E08', 'C', 'A1', 1000, 'E03'), ('E09', 'A1', 'E', 2000, None), ('E10', 'E', 'F', 1500, None), ('E11', 'F', 'A1', 1000, None), ('E12', 'A1', 'P', 2000, None), ('E13', 'P', 'A1', 1500, None), ('E14', 'Q', 'A1', 3000, None), ('E15', 'A1', 'D', 4500, None), ('E16', 'A2', 'A1', 500, None), ('E17', 'A1', 'F', 1000, None), ('E18', 'F', 'D', 500, None), ('E19', 'R', 'A1', 2000, None), ('E20', 'A1', 'C', 2500, None), ('E21', 'D', 'A1', 1000, 'E15'), ('E22', 'A1', 'E', 1500, None), ('E23', 'E', 'A1', 500, None), ('E24', 'A1', 'C', 500, None)]
NONCANONICAL=[('duplicateE01',10000),('instructionE03',12000),('pending',250),('mirrorE04',4000)]
assert len(EDGES)+len(NONCANONICAL)==28
own={'A1','A2'}
rows=[]
for n,(eid,fr,to,amount,linked) in enumerate(EDGES,1):
    refs='N01'+(';N03' if linked else '')+(';N04' if eid in ('E10','E18') else '')
    rows.append([eid,n,fr,to,amount,'USD',fr in own and to in own,linked,refs,'RECORDED'])
def flows(nodes):
    inc=sum(a for eid,fr,to,a,link in EDGES if to in nodes and fr not in nodes)
    out=sum(a for eid,fr,to,a,link in EDGES if fr in nodes and to not in nodes)
    return inc,out
balances=[]
for bid,node,opening,close in [('B01','A1',1000,500),('B02','A2',500,1000),('B03','ENTITY-A',1500,1500)]:
    inc,out=flows(own if node=='ENTITY-A' else {node})
    calculated=opening+inc-out
    balances.append([bid,node,opening,inc,out,calculated,close,calculated-close,'N01;N02'])
assert flows(own)==(34000,34000)
assert sum(x[3] for x in EDGES)==74500
assert all(x[7]==0 for x in balances)
assert len({x[1] for x in EDGES}|{x[2] for x in EDGES})==9
byid={x[0]:x for x in EDGES}
cycle=['E09','E10','E11']
assert min(byid[x][3] for x in cycle)==1000
assert sum(byid[x][3] for x in cycle)==4500
assert [next(i for i,e in enumerate(EDGES) if e[0]==k) for k in cycle]==sorted(next(i for i,e in enumerate(EDGES) if e[0]==k) for k in cycle)
patterns=[]
PATTERN_RULES = [('P01', 'Distinct external source fan-in', 'E01;E02;E06;E13;E14;E19', 'P/Q/R contribute six transfers; three distinct immediate sources, no common-controller assertion', 'N01'), ('P02', 'External outflow from entity accounts', 'E03;E05;E07;E09;E12;E15;E17;E20;E22;E24', 'Ten boundary exits to five distinct immediate recipients C,D,E,P,F; count field is transfer count, not recipient count', 'N01;N02'), ('P03', 'Time-respecting A1-E-F-A1 cycle', 'E09;E10;E11', 'Minimum-edge capacity USD1000; attributable same-funds circulation range USD0–1000, not proven recycling', 'N01;N04'), ('P04', 'Own-account movements', 'E04;E16', 'Two canonical transfers; collapse at entity boundary, retain account detail', 'N01;N02'), ('P05', 'Explicit linked returns', 'E08;E21', 'Two posted returns reduce only their linked originals; other inbound cycle edges are not inferred refunds', 'N01;N03'), ('P06', 'All canonical edge-leg value', 'E01–E24', 'Gross value across all observed legs; includes repetition, own transfers and onward extracts; not unique source capital', 'N01;N04')]
for pid,label,members,meaning,refs in PATTERN_RULES:
    selected=EDGES if members=='E01–E24' else [byid[k] for k in members.split(';')]
    amount=min(x[3] for x in selected) if pid=='P03' else sum(x[3] for x in selected)
    count=len({x[1] for x in selected}) if pid=='P01' else len(selected)
    patterns.append([pid,label,members,amount,count,meaning,refs])
assert len({to for eid,fr,to,a,link in EDGES if fr in own and to not in own})==5
TARGET='E03'
pre_target=EDGES[:next(i for i,e in enumerate(EDGES) if e[0]==TARGET)]
opening_available=1000
source_values={'P receipt E01':sum(a for eid,fr,to,a,link in pre_target if fr=='P' and to=='A1'), 'Q receipt E02':sum(a for eid,fr,to,a,link in pre_target if fr=='Q' and to=='A1'), 'Opening balance A1':opening_available}
source_values['Combined P+Q receipts']=source_values['P receipt E01']+source_values['Q receipt E02']
available=opening_available+sum(a if to=='A1' else -a if fr=='A1' else 0 for eid,fr,to,a,link in pre_target)
RULE_METADATA = [('AL01', 'E03', 'P receipt E01', 'Complete pre-E03 balance; fungible funding, no priority rule; range not point estimate', 'N01;N02;N06'), ('AL02', 'E03', 'Q receipt E02', 'Marginal bounds cannot all be combined arbitrarily; joint allocations must sum 12000', 'N01;N02;N06'), ('AL03', 'E03', 'Opening balance A1', 'Opening origin unknown; do not attribute it to P or Q', 'N01;N02;N06'), ('AL04', 'E03', 'Combined P+Q receipts', 'Combined receipt lower bound differs from sum of individual minima', 'N01;N02;N06')]
RULES=[(aid,target,source,source_values[source],available-source_values[source],byid[target][3],basis,refs) for aid,target,source,basis,refs in RULE_METADATA]
bounds=[]
for aid,target,source,s,o,d,basis,refs in RULES:
    assert d<=s+o
    bounds.append([aid,target,source,s,o,d,max(0,d-o),min(s,d),basis,refs])
assert (bounds[0][6],bounds[0][7])==(3000,10000)
assert byid[TARGET][3] > bounds[0][7]  # All of E03 cannot be funded by P under GP-1.
assert sum(r[6] for r in bounds[:3])==4000 # marginal minima are not a joint allocation
pool=Decimal(available); debit=Decimal(byid[TARGET][3])
p=(debit*Decimal(source_values['P receipt E01'])/pool).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
opening=(debit*Decimal(opening_available)/pool).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
q=debit-p-opening
fifo_opening=min(opening_available,int(debit))
fifo_p=min(source_values['P receipt E01'],int(debit)-fifo_opening)
fifo_q=int(debit)-fifo_opening-fifo_p
scenarios=[['AS01','Opening-first then FIFO receipts',fifo_p,fifo_q,fifo_opening,int(debit),'ILLUSTRATIVE_ONLY','N01;N02;N06'],['AS02','Proportional available balance; cent residual to Q',float(p),float(q),float(opening),12000,'ILLUSTRATIVE_ONLY','N01;N02;N06'],['AS03','Minimum P feasible allocation',bounds[0][6],source_values['Q receipt E02'],int(debit)-bounds[0][6]-source_values['Q receipt E02'],int(debit),'ILLUSTRATIVE_ONLY','N01;N02;N06'],['AS04','Maximum P feasible allocation',bounds[0][7],int(debit)-bounds[0][7],0,int(debit),'ILLUSTRATIVE_ONLY','N01;N02;N06']]
assert all(sum(Decimal(str(v)) for v in r[2:5])==Decimal(12000) for r in scenarios)
assert max(0,12000-14000)==0 # additional unseen source destroys positive lower bound
assert 20000>19000 # model infeasibility, not an attribution result
CHECKED_TABLES={'EconomicEdges':rows,'BalanceChecks':balances,'PatternTests':patterns,'AllocationBounds':bounds,'AttributionScenarios':scenarios}
print('PASS: raw28; edges24; nodes9; legs74500; boundary34000/34000; P3000–10000; cycle0–1000; vectors12000')
```
<!-- FIXTURE_CHECK:END -->
