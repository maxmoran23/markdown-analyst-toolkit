# Digital Asset Review — worked fictional example

## Scope and fixture

All network, address, contract, transaction, and event labels below are invented and are not valid live-network identifiers. SYN-001 is the complete fictional fixture. The review concerns subject SUBJECT on FICTIONAL-EVM, asset PAPER-CONTRACT with stipulated decimals 6, during a fictional capture window 2026-09-01 through 2026-09-30. The asset symbol PAPER is a display label; no market price, backing, redemption right, or fiat equivalence is stipulated.

The source capture has six raw rows. Successful rows have sufficient settled status for this exercise; the example does not prescribe a universal confirmation count. The failed row is an attempted-action record supplied by the source, not an actual successful transfer log. No private keys, wallets, real names, or customer records are involved.

## Raw captured rows

| Raw row | Transaction/index | From | To | Atomic amount | State | Evidence note |
| --- | --- | --- | --- | ---: | --- | --- |
| R-01 | TX-01 / 0 | CP-A | SUBJECT | 100000000 | SUCCESS | First page |
| R-02 | TX-02 / 0 | SUBJECT | CP-B | 40000000 | SUCCESS | First page |
| R-03 | TX-03 / 0 | SUBJECT | SUBJECT | 5000000 | SUCCESS | First page |
| R-04 | TX-04 / 0 | CP-C | SUBJECT | 1 | SUCCESS | Second page; unsolicited small amount |
| R-05 | TX-05 / not applicable | SUBJECT | CP-B | 20000000 | FAILED | Requested amount only; no successful log |
| R-06 | TX-01 / 0 | CP-A | SUBJECT | 100000000 | SUCCESS | Second page repeats R-01 exactly |

A supplied explorer label calls CP-B a service address but provides no supporting identity evidence. Keep it UNVERIFIED LABEL. CP-A and CP-C are UNATTRIBUTED. SUBJECT's self row means the same exact fictional address appears on both sides; it does not establish the identity of a person controlling it.

## Normalize and reconcile

Assign EV-01 to R-01 and link R-06 as its duplicate capture. EV-02 through EV-05 correspond to R-02 through R-05. The key for successful events is chain, transaction, contract, and event index. R-06 matches all those fields and the content. The failed attempt has no log index and must not be forced into a fabricated successful-log identity.

Raw reconciliation: 6 rows = 5 unique records + 1 confirmed duplicate. Unique-record reconciliation: 5 = 4 eligible successful events + 1 failed attempted action. Included-event reconciliation: 4 = 2 IN + 1 OUT + 1 SELF. These are distinct denominators, each with its own meaning.

## Exact unit arithmetic

Scale factor is 10^6 = 1,000,000 atomic units per PAPER unit. EV-01 is 100,000,000 / 1,000,000 = 100.000000 PAPER. EV-02 is 40.000000 PAPER. EV-03 is 5.000000 PAPER. EV-04 is 1 / 1,000,000 = 0.000001 PAPER. EV-05 requested 20.000000 PAPER, but execution failed and it contributes zero to settled outflow under the stated method.

Eligible directional inflow atomic amount is 100,000,000 + 1 = 100,000,001, or 100.000001 PAPER. Eligible directional outflow is 40,000,000, or 40.000000 PAPER. Net captured directional flow is 100,000,001 − 40,000,000 = 60,000,001 atomic units = 60.000001 PAPER. SELF activity is separately 5,000,000 atomic units = 5.000000 PAPER.

Do not add SELF to both IN and OUT, even though doing so would leave the net unchanged: it would inflate gross activity. Do not include the failed requested amount: doing so would falsely produce outflow 60.000000 and net 40.000001. Do not double-count R-06: doing so would falsely produce inflow 200.000001. The tiny transfer remains visible at full precision instead of being rounded away.

## Expected counterparty table

| counterparty_id | asset_id | in_units | out_units | self_units | eligible_event_count | attribution_state | evidence_ids | notes |
| --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| CP-A | PAPER-CONTRACT | 100.000000 | 0.000000 | 0.000000 | 1 | UNATTRIBUTED | SYN-001 | Duplicate removed once |
| CP-B | PAPER-CONTRACT | 0.000000 | 40.000000 | 0.000000 | 1 | UNVERIFIED LABEL | SYN-001 | Failed attempt not included |
| SUBJECT | PAPER-CONTRACT | 0.000000 | 0.000000 | 5.000000 | 1 | SELF ADDRESS | SYN-001 | Not a separate external counterparty |
| CP-C | PAPER-CONTRACT | 0.000001 | 0.000000 | 0.000000 | 1 | UNATTRIBUTED | SYN-001 | Unsolicited transfer retained |

Eligible-event counts total 1 + 1 + 1 + 1 = 4. External observed counterparties total three, excluding SUBJECT. CP-B is the only eligible outbound counterparty, but this concentration within one small capture does not establish risk or business purpose. No outgoing relationship should be inferred from the failed attempt beyond the observed attempt record.

## Expected findings

F-01, MEDIUM consequence, HIGH confidence, Observed: one duplicate capture and one failed attempt require distinct handling. The reconciliation supports four eligible successful events. Retain both exclusions in the audit trail and show exact inclusion rules.

F-02, HIGH consequence, HIGH confidence, Observed: the available label does not establish CP-B's real-world identity. The high confidence concerns the absence of supporting identity evidence in this fixture. Obtain independent attribution evidence before using the label in a consequential claim.

F-03, MEDIUM consequence, HIGH confidence, Estimated: captured net directional flow is 60.000001 PAPER under the stipulated scale and inclusion method. It is not an ending balance or fiat value. No opening balance, complete native-fee accounting, or market-price evidence was supplied.

## Boundary variants

If decimals are removed, preserve every atomic amount and set display quantities and human-unit totals unavailable. If a second contract also uses PAPER as its symbol, keep its events in a separate asset group. If TX-01 includes another valid event at index 1, retain it rather than deduplicating by transaction. If the source cannot distinguish two identical-looking events, report ambiguity and alternate totals instead of pretending the duplicate is proven.

If EV-02 becomes pending, remove it from settled outflow and increase the unresolved count; do not silently delete it. If the capture includes another address asserted to belong to SUBJECT's owner, keep that association as a separate claim before aggregating. If a verified attribution later identifies CP-B, preserve the attribution date and scope and do not retroactively assume the label covered all historical control.

## Review conclusion

The fixture is technically review-ready only within its stipulated capture and schema. It provides no conclusion about wrongdoing, customer identity, sanctions status, legal service-provider classification, or source of wealth. The demonstrated outcome is transparent reconciliation of a small fictional event set. A human reviewer determines whether more ledger, attribution, protocol, or legal evidence is needed for the actual question.
