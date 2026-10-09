# Trade surveillance: complete fictional example

Every instrument, order, account, group, venue, execution, and market value is fictional. The example uses equity shares with USD prices and a 0.01 USD tick. All event times are on Sep 01, 2026 in ET, with millisecond precision and an authoritative event sequence. All three group windows have complete supplied order-event coverage. No real trader or security is represented.

## Complete raw event population

Quantity means accepted quantity for NEW, executed quantity for FILL, and removed remaining quantity for CANCEL_ACK. There are no replacements, expiries, busts, or open orders in this fixture. The message sequence is authoritative within each instrument. M12 is an exact duplicate source copy of M02.

| Message | Order | Group/account | Instrument | Time ET | Event | Side | Quantity shares | Price USD | Execution |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M01 | O1 | A/A1 | FICT-A | 9:30:00.000 AM ET | NEW | BUY | 1000 | 10.00 | null |
| M02 | O1 | A/A1 | FICT-A | 9:30:00.100 AM ET | FILL | BUY | 200 | 10.00 | X-A1 |
| M03 | O2 | A/A1 | FICT-A | 9:30:00.150 AM ET | NEW | SELL | 100 | 10.01 | null |
| M04 | O2 | A/A1 | FICT-A | 9:30:00.200 AM ET | FILL | SELL | 100 | 10.01 | X-A2 |
| M05 | O1 | A/A1 | FICT-A | 9:30:00.500 AM ET | CANCEL_ACK | BUY | 800 | 10.00 | null |
| M06 | O3 | B/B1 | FICT-B | 9:31:00.000 AM ET | NEW | BUY | 500 | 20.00 | null |
| M07 | O3 | B/B1 | FICT-B | 9:31:00.100 AM ET | CANCEL_ACK | BUY | 500 | 20.00 | null |
| M08 | O4 | C/C1 | FICT-C | 9:32:00.000 AM ET | NEW | BUY | 100 | 30.00 | null |
| M09 | O5 | C/C2 | FICT-C | 9:32:00.050 AM ET | NEW | SELL | 100 | 30.00 | null |
| M10 | O4 | C/C1 | FICT-C | 9:32:00.100 AM ET | FILL | BUY | 100 | 30.00 | X-C1 |
| M11 | O5 | C/C2 | FICT-C | 9:32:00.100 AM ET | FILL | SELL | 100 | 30.00 | X-C1 |
| M12 | O1 | A/A1 | FICT-A | 9:30:00.100 AM ET | FILL | BUY | 200 | 10.00 | X-A1 |

Raw reconciliation: **12 received = 11 processed + 1 duplicate + 0 excluded + 0 unparsed + 0 inaccessible + 0 deferred**. Canonical M01–M11 contain **5 accepted-new events + 4 account-side fill events + 2 cancel acknowledgments = 11**. Unique executions are X-A1, X-A2, and X-C1: **3**, because M10 and M11 describe the two legs of one matched trade.

## Context and benchmark register

SYN-001 contains A's events; SYN-002 B's; SYN-003 C's. SYN-004 is a fictional effective-dated ownership record confirming C1 and C2 share one beneficial-owner group C. It supplies no proof of intentional coordination or strategy relatedness.

SYN-005 supplies A's market benchmark: FICT-A, same venue universe, interval 9:30:00.000 AM through 9:30:00.500 AM ET inclusive, 1,000 unique traded shares including A's 300. Pre-event midpoint is 10.00 USD from bid 9.99 and ask 10.01 immediately before M01; post-event midpoint is 10.01 USD from bid 10.00 and ask 10.02 immediately after M05. At M01 acceptance, the selected same-side depth band contains O1's 1,000 shares and 2,000 external shares. The band definition is exactly the same for numerator and denominator. These data do not establish causal price impact.

SYN-006 supplies B's context: a quote change at 9:31:00.080 AM ET and a contemporaneous risk log recording a repricing cancellation. The exact quote levels are not needed for the screen and are not inferred. Complete B event coverage confirms no opposite-side execution in its supplied window. A's rationale is not supplied. C's strategy independence and self-trade-prevention configuration are not supplied.

## Expected OrderLifecycle

| order_id | group_id | instrument_id | side | new_quantity | filled_quantity | cancelled_quantity | remaining_quantity | lifetime_ms | cancel_quantity_ratio | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| O1 | A | FICT-A | BUY | 1000 | 200 | 800 | 0 | 500 | 0.8 | SYN-001 |
| O2 | A | FICT-A | SELL | 100 | 100 | 0 | 0 | 50 | 0.0 | SYN-001 |
| O3 | B | FICT-B | BUY | 500 | 0 | 500 | 0 | 100 | 1.0 | SYN-002 |
| O4 | C | FICT-C | BUY | 100 | 100 | 0 | 0 | 100 | 0.0 | SYN-003;SYN-004 |
| O5 | C | FICT-C | SELL | 100 | 100 | 0 | 0 | 50 | 0.0 | SYN-003;SYN-004 |

## Exact arithmetic

FICT-A accepted quantity is 1,100 shares = 300 filled + 800 cancelled + 0 remaining. FICT-B is 500 = 0 + 500 + 0. FICT-C account-side quantity is 200 = 200 + 0 + 0. Do not use a cross-instrument sum as economic exposure.

O1 lifetime = .500 − .000 = **500 ms**. O2 = .200 − .150 = **50 ms**. O3 = **100 ms**; O4 = **100 ms**; O5 = **50 ms**. O1 cancellation ratio = 800/1,000 = **80.0%**. Group A quantity cancellation ratio = 800/1,100 = **72.7% displayed**; A order cancellation incidence = 1/2 = **50.0%**.

O2 fills while O1 remains live. O1 cancellation occurs .500 − .200 = **300 ms** after that opposite fill. TS-01 matches inclusive 500 ms and 80.0% conditions. A has one simultaneous buy price level, so TS-02 is NO_MATCH. B has no opposite fill and therefore TS-01 is NO_MATCH despite a 100.0% cancellation ratio.

C's two 100-share account-side fill legs are one **100-share unique execution**. Its one-sided market notional is 100 × 30.00 = **3,000.00 USD**; adding both account-side legs yields 6,000.00 USD, a different accounting measure. The example's unique execution notionals are 2,000.00 USD for X-A1, 1,001.00 USD for X-A2, and 3,000.00 USD for X-C1, total **6,001.00 USD**. This sum is turnover, not profit or manipulative proceeds.

A participation = 300/1,000 = **30.0%**. Displayed depth share = 1,000/(1,000+2,000) = **33.3% displayed**. Midpoint change = (10.01−10.00)/10.00 × 10,000 = **10.0 basis points**. None of these proves that A caused the change.

## Expected SurveillanceObservations

| observation_id | group_id | scenario_id | state | measured_value | unit | criterion | review_priority | confidence | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TS-O1 | A | TS-01 | MATCH | 300 | milliseconds | cancel<=500ms after opposite fill; cancelled/new>=0.80 | MEDIUM | MODERATE | SYN-001;SYN-005 |
| TS-O2 | A | TS-02 | NO_MATCH | 1 | simultaneous_price_levels | at least 3 same-side price levels | LOW | HIGH | SYN-001 |
| TS-O3 | B | TS-01 | NO_MATCH | null | milliseconds | opposite-side execution required | LOW | HIGH | SYN-002;SYN-006 |
| TS-O4 | C | TS-03 | MATCH | 100 | unique_executed_shares | execution between confirmed same-owner accounts | MEDIUM | MODERATE | SYN-003;SYN-004 |

## Expected findings and limits

TS-F01 is MEDIUM severity, MODERATE confidence, Inferred: A's cancellation/opposite-fill sequence is a review lead. The partial fill is countercontext; intent, repetition, causation, and economic benefit are not established. Seek broader authorized evidence and strategy context.

TS-F02 is LOW severity, HIGH confidence, Observed: B has no opposite execution in complete supplied coverage, with a documented quote-change context. Retain the negative test; do not infer market manipulation from cancellation ratio alone.

TS-F03 is MEDIUM severity, MODERATE confidence, Inferred: C's same-owner execution merits strategy and control review. It is one trade, not two, and does not establish illegal wash trading. No trading restriction, disciplinary action, external report, or rule change is executed.

Four planned observations reconcile to **2 MATCH + 2 NO_MATCH + 0 NOT_ASSESSABLE + 0 DATA_DEFECT**. The intentionally complete fixture does not eliminate missing-data behavior: remove the clock basis, opposite-side coverage, or ownership evidence and the relevant observation must become NOT_ASSESSABLE. At a 501 ms gap A fails the timing condition; at 500 ms it matches. Three sequential nonoverlapping price levels do not satisfy the simultaneous-layer screen.
