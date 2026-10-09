# Trade surveillance: inputs and evidence

## Specify market structure before interpreting behavior

Record instrument class, venue, session, tick size, quantity unit, contract multiplier if any, order types, auction status, and applicable rulebook. A share, futures contract, option contract, and token unit are different measures. The example uses fictional equity instruments denominated in USD; the CFTC source is comparative context for derivatives, not a rule applied to these fictional equities.

| Input | Required fields | Purpose and validation |
| --- | --- | --- |
| Order events | message_id, order_id, parent_id, account_id, event_type, exchange_time, sequence_id, side, quantity, price, instrument_id, venue | Distinguish accepted new orders, fills, cancel requests, cancel acknowledgments, replaces, rejects, expiries, and corrections. |
| Executions | execution_id, order_id, quantity, price, trade_time, contra_order_id if known, correction_status | One account-side fill leg; a shared execution ID can identify both sides of one trade. |
| Ownership and control | account_id, beneficial_owner_group, strategy_id, desk_id, evidence_id, effective_dates | Separate common ownership from common strategy control or intentional coordination. |
| Market context | instrument, venue scope, time interval, best bid/ask, depth definition, trade volume, source, sequence quality | Benchmark must align with the metric's instrument, window, and venue coverage. |
| Clock metadata | timestamp_precision, timezone, synchronization_basis, known_offset, uncertainty | Required for subsecond ordering and cross-feed joins. |
| Strategy context | authorized strategy description, risk events, configuration version, change history | A reported rationale is not proof; corroborate against actual event behavior. |
| Scenario specification | scenario_id, version, eligibility, window, thresholds, exclusions, evidence prerequisites | Preserve exact operators and distinguish authored screen from legal criterion. |

## Message and quantity dictionary

New quantity means accepted order quantity, not a rejected request. Filled quantity means confirmed executed quantity after corrections. Cancelled quantity means the remaining quantity removed by a confirmed cancellation, not the original order size after a partial fill. Remaining quantity is outstanding live quantity at the as-of time. A cancel request can race with a fill; until the acknowledgment is known, do not assume cancellation succeeded.

A replacement may amend price, reduce quantity, increase quantity, or create a new linked order ID. Use the venue's actual semantics. Do not count full replacement quantity as entirely new economic interest unless that is the declared measure. Preserve original and replacement chains. A trade bust reverses an execution's effective status while remaining part of the audit trail.

## Population reconciliation

Reconcile raw messages into processed, duplicates, out-of-scope, unparsed, inaccessible, and deferred. Reconcile lifecycle quantities separately per order. For a simple order without increases or busts: accepted quantity equals filled + cancelled + expired + remaining. Do not use that simple identity for a replace chain without accounting for additions and reductions.

Maintain separate counts for accepted orders, raw messages, fill legs, unique executions, cancelled orders, cancel messages, and affected groups. One order can have many fills and messages. Two account-side fills can be one market trade. A ratio's denominator must name which unit it uses.

If source sequence numbers have gaps, record the affected instrument and interval. A complete internal order file may still omit market-wide context or activity at other firms. An isolated extract cannot establish the absence of opposite-side execution across all venues. Limit negative statements to the actual observed scope.

## Time normalization and source precedence

Preserve raw timestamps, normalized instants, precision, and source. Use exchange sequence where reliable for ordering events within a venue. Do not sort by arrival at the analyst's file system. For cross-venue feeds, estimate or obtain clock uncertainty; if uncertainty overlaps the proposed event ordering, label the sequence ambiguous rather than inventing milliseconds.

Timestamps rounded to a second cannot support a claim that a cancellation followed a fill by 300 ms. Events with equal timestamps need sequence evidence. Daylight-saving changes, session boundaries, overnight trading dates, halts, and auctions require explicit treatment. Do not compare continuous-market behavior with auction mechanics as if they were identical.

## Ownership and attribution

Use effective-dated evidence for beneficial ownership. Common ownership does not establish common intent. Orders from separate strategies may interact unintentionally; similar order sizes or matching names do not establish beneficial ownership. A same-owner execution is a surveillance lead requiring contextual assessment, not an automatic illegal-wash-trading conclusion.

A strategy label supplied by a trader is Reported until corroborated. A risk-control log establishes recorded control activity, but the reason and effectiveness still require review. Do not infer intent from a high cancellation rate, partial fill, profit, or a single sequence alone.

## Benchmark provenance

Record whether market volume includes the reviewed participant, whether both trade sides have been counted, whether off-venue prints are included, and whether corrections are applied. Record best-bid/ask source and whether the price is consolidated or venue-specific. A same-day average volume is not interchangeable with volume in a 500 ms interval. A denominator of zero or unknown produces null, not zero participation.


## Public-source register

Sources below were retrieved for package preparation on **2026-10-09**. This records access, not a legal-currency certification. Recheck applicability, amendments, jurisdiction, and institution type for a live task. The methods and illustrative thresholds in this suite are authored analytical conventions, not quotations from or mandates attributed to these sources.

| ID | Source and locator | Publication/version | Applicability and boundary |
| --- | --- | --- | --- |
| AUTH-TS-01 | [FINRA Rule 5210: Publication of Transactions and Quotations](https://www.finra.org/rules-guidance/rulebooks/finra-rules/5210) | Current online text retrieved 2026-10-09; supplementary material .02 and .03 | US FINRA-member context; self-trade and disruptive-activity provisions require careful contextual application. |
| AUTH-TS-02 | [FINRA Rule 2020](https://www.finra.org/rules-guidance/rulebooks/finra-rules/2020) | Current online text retrieved 2026-10-09 | General FINRA prohibition context; not a numerical detection rule. |
| AUTH-TS-03 | [CFTC: Antidisruptive Practices Authority, Interpretive Guidance and Policy Statement](https://www.cftc.gov/LawRegulation/FederalRegister/FinalRules/2013-12365.html) | 2013-05-28, 78 FR 31890 | Derivatives-specific context concerning intent and legitimate cancellations; not automatically applicable to securities. |
| AUTH-TS-04 | [SEC staff: Market Access Rule FAQs](https://www.sec.gov/rules-regulations/staff-guidance/trading-markets-frequently-asked-questions/divisionsmarketregfaq-0) | Staff FAQ page, retrieved 2026-10-09 | Market-access control context; staff guidance is distinct from the controlling rule and from a case conclusion. |

Record future retrievals separately using source ID, direct URL, publisher, publication date if stated, retrieval timestamp, page or section, exact proposition supported, and status. Guidance cannot establish the facts of a particular case. An accessible page does not establish the correctness of an attached customer assertion.
