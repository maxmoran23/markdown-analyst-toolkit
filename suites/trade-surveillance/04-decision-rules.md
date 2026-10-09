# Trade surveillance: rules and human gates

## Data prerequisites come first

| Condition | Result | Required treatment |
| --- | --- | --- |
| Missing relevant accepted order, fill, or cancel acknowledgment | NOT_ASSESSABLE | Reconstruct source coverage; retain known events. |
| Cross-feed time uncertainty can reverse ordering | NOT_ASSESSABLE for timing-dependent rule | Report uncertainty bounds and request clock evidence. |
| Quantity conservation fails | DATA_DEFECT | Do not calculate a reliable lifecycle ratio until repaired. |
| Identity mapping needed but unsupported | NOT_ASSESSABLE for ownership/group rule | Obtain effective-dated relationship evidence. |
| Full relevant coverage and criteria false | NO_MATCH | State failed element and bounded scope. |
| Full required coverage and all screen conditions met | MATCH | Contextual human review required. |

A data defect is not a market-conduct finding against a trader. A NO_MATCH is not a general clean bill of conduct. A partial fill does not automatically clear a cancellation concern; a high cancellation ratio does not automatically prove one.

## Illustrative screen register

| ID | Explicit condition | Unit | Expected limitation |
| --- | --- | --- | --- |
| TS-01 | cancelled/new >=0.80; same-group opposite fill occurs while candidate order live; confirmed cancellation follows within <=500 ms | Order and opposite-fill pair | Sequence alone does not establish intent, causation, frequency, or violation. |
| TS-02 | >=3 distinct simultaneously live same-side price levels in same instrument/venue | Group-window | Descriptive layering lead; not complete legal elements. |
| TS-03 | Both sides of a matched execution map to same confirmed beneficial-owner group | Unique execution | Requires strategy/control context; not automatically illegal wash trading. |

All comparison operators are inclusive. At 500 ms TS-01 meets the timing condition; at 501 ms it does not. A cancellation before the opposite fill does not satisfy this version. A canceled order with no opposite fill is NO_MATCH if coverage is complete. A missing opposite-side feed is NOT_ASSESSABLE, not evidence of no execution.

## Prioritization

HIGH priority applies to an observed urgent market-integrity concern or material surveillance coverage defect requiring prompt authorized review. MEDIUM applies to a supported screen match with unresolved context. LOW applies to a bounded negative test or supported ordinary explanation. These are analytical priorities, not sanctions, legal materiality thresholds, or proof of misconduct.

HIGH confidence can apply to reconstructed arithmetic or an absent condition within complete scope. MODERATE applies to an inferred pattern with incomplete intent or economic context. LOW applies to weak or conflicting attribution. NOT ASSESSABLE applies where the proposition cannot be tested. Keep priority and confidence independent.

## Legal-context boundary

The rule register is an authored analytical device. Do not substitute it for the specific applicable securities, derivatives, venue, or jurisdictional requirements. The public-source register identifies contextual authorities; the reviewer must confirm current applicability and all elements before making a legal characterization. A single selected sequence must not be described as satisfying a frequent-pattern requirement without evidence of frequency.

Use “cancellation sequence,” “simultaneous-level observation,” and “same-owner execution” in findings. Terms such as spoofing, layering, and wash trading may identify the surveillance topic or hypothesis, but qualify them as potential indicators or leads unless an authorized determination is supplied and appropriately attributed. Do not invent trader intent from statistical extremes.

## Human-only actions

No threshold crossing authorizes account restriction, order rejection, trading suspension, trader discipline, external notification, rule deployment, or filing. The assistant may prepare the evidence package and proposed review questions. It cannot contact a trader, access restricted communications, change a surveillance rule, or mark an external action complete.

If a local policy is supplied, capture its effective version and exact applicable scope. Distinguish an analytical recommendation from a required supervisory step. An absent policy document is a limitation, not permission to invent one. Proposed actions must have actual owner roles and a factual urgency basis; do not manufacture service deadlines.

## Aggregation and performance restrictions

Do not add matched indicator counts and call them unique incidents when they reuse the same orders. Do not compute market participation from account-side double-counted self-match legs. Do not calculate recall using only already-alerted activity. A lower alert count after a threshold change does not establish improved accuracy. Show changed populations, changed criteria, reviewed labels, and unreviewed observations before drawing performance conclusions.

A benign-context explanation should be documented and challenged against the events, not used to erase the screen match. Preserve the original result, reviewer assessment, and reason for any later change. A fully reconstructed negative control is as important as a positive example for testing whether the method is behaving as specified.
