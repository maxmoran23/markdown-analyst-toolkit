# Trade surveillance: sequential method

## 1. Bound the review and select the correct lens

State whether the task is an alert review, a control test, or a scenario-design assessment. Identify instrument, venue, participant group, time window, and the market-conduct question. A short selected sequence can demonstrate how a screen behaves but cannot establish a frequent pattern, trader intent, or a complete market picture.

Choose the legal and rulebook context separately from the analytical screen. A securities rule and a derivatives spoofing provision do not have identical elements or jurisdiction. Use an authorized reviewer for legal characterization. The package should explain the observed conduct and missing facts without declaring a violation from a pattern label.

## 2. Reconstruct order lifecycles before calculating ratios

Start with accepted new events. Apply subsequent partial fills, quantity reductions, cancels, replacements, expiries, rejections, and execution corrections in authoritative sequence. A cancel request does not reduce live quantity until the applicable confirmation. A partial fill followed by cancellation removes only the remaining quantity. An already cancelled order cannot acquire a later effective fill unless a race, correction, or sequencing problem is resolved.

For the simple example, `new_quantity = filled_quantity + cancelled_quantity + remaining_quantity`. O1 begins with 1,000 shares, fills 200, and cancels 800. Counting 1,000 cancelled shares would violate conservation. Keep every message in the audit trail even when duplicates or corrections are excluded from effective quantities.

For replace chains, record initial quantity plus accepted increases, less fills, confirmed reductions, cancellations, expiries, and final remaining quantity. Some systems express replacement quantity as total order quantity and others as remaining quantity. Resolve the semantics from the supplied specification; do not guess. A correct arithmetic formula applied to the wrong field meaning still produces an invalid result.

## 3. Establish sequence confidence

Normalize timestamps to a common instant while preserving raw values and precision. Use authoritative sequence numbers for same-venue ties. Determine clock skew and error bounds for joins across feeds. If a fill is timestamped 100 ms before a cancellation but relative clock uncertainty is 250 ms, the ordering is not established.

Define lifetime as final effective terminal event minus accepted-new time for a fully terminated order. For an open order, the observed age is as-of minus acceptance and is right-censored; it is not completed lifetime. Report separate measures for time to first fill, time to first cancel request, and time to cancel acknowledgment when relevant. Do not substitute one for another without disclosure.

## 4. Compute cancellation measures with named denominators

Quantity cancellation ratio is cancelled quantity divided by accepted new quantity for the declared simple lifecycle. Order cancellation incidence is the number of accepted orders with any confirmed cancellation divided by accepted order count. Message cancellation ratio uses cancel messages over a declared message population. These can differ substantially and must not share the same label.

In group A, cancelled quantity is 800 and accepted quantity is 1,100, giving 72.7272...%. One of two orders has a cancellation, giving 50.0% order cancellation incidence. O1 individually has an 80.0% quantity cancellation ratio. None of these figures alone establishes intent or manipulation. Peer comparisons require comparable instruments, strategies, liquidity, time of day, and market conditions.

Do not aggregate raw quantity ratios across unrelated instruments without a justified weighting scheme. A 1,000-share order in a low-price equity and a 10-contract derivative order have different exposure and market impact. Report per instrument; use counts for cross-instrument inventory and appropriately defined notional only where meaningful.

## 5. Apply the authored opposite-side sequence screen TS-01

The illustrative screen requires a confirmed cancellation of at least 80.0% of an order's accepted quantity, an opposite-side execution by the same supported participant group while that order is live, and cancellation acknowledgment no more than 500 ms after that opposite-side execution. All clocks and event links must be adequate. These parameters are synthetic, not regulatory thresholds or approved production settings.

For O1/O2, O1 is accepted at 9:30:00.000 AM ET, O2 fills at .200, and O1 cancellation is confirmed at .500. The gap is 300 ms; 800/1,000 = 0.80. TS-01 matches. O1's earlier 200-share partial fill is relevant context but neither proves good intent nor establishes bad intent. The screen identifies a sequence worth reviewing.

TS-01 does not require or demonstrate a market-price effect, deceptive intent, repeated behavior, or economic benefit. Do not label its output “spoofing proven.” Investigate repeated sequences, order placement relative to the book, genuine willingness to execute, strategy logic, external events, risk controls, and available communications through authorized channels.

## 6. Examine layering and book context without overclaiming

The illustrative TS-02 asks whether at least three distinct same-side price levels from the participant are simultaneously live in the same instrument and venue within the window. It is a descriptive screen, not the complete legal or rulebook definition of layering. Count overlapping intervals, not every price visited over a day. Replaced orders at sequential prices do not necessarily represent simultaneous layers.

For A, only one same-side buy price level is live; TS-02 is NO_MATCH. The presence of an opposite-side sell order does not create a second buy layer. If order-book completeness is missing, the full-window state becomes NOT_ASSESSABLE rather than a clean negative.

When measuring displayed depth share, specify side, price range, instant, venue, and whether reviewed orders are included in the denominator. A participant's 1,000 shares plus 2,000 external shares produces 1,000/3,000 = 33.3% displayed share. Dividing by the external 2,000 instead produces 50.0% relative-to-external size, a different measure. Label each correctly.

## 7. Review same-owner executions as a separate lead

TS-03 identifies an execution whose two matched account-side legs map to the same supported beneficial-owner group. Deduplicate the market trade by execution ID. In the example O4 and O5 each fill 100 shares in X-C1; this is 200 account-side filled shares but one unique 100-share execution.

Review whether strategies are related, whether interaction was intended, whether self-trade prevention was configured and effective, whether the pattern recurs, and whether the ownership mapping was valid at the time. Accidental interaction, independent strategies, and technical control failures are possible explanations. Neither common ownership nor a self-match alone establishes illegal wash trading.

If contra identity is missing, do not infer a self-match merely from identical price, quantity, and timestamp. If ownership is reported but unverified, label the attribution accordingly and keep the rule state conditional or NOT_ASSESSABLE. Market-wide wash-trading estimates require much broader data and a justified methodology.

## 8. Align market benchmarks and benefit claims

Participant execution participation equals unique relevant executed shares divided by market traded shares for the same instrument, window, and venue universe. Both numerator and denominator must use compatible one-sided trade counting. A has 300 unique executed shares in a 1,000-share market window, yielding 30.0%. Do not divide A's fills by a daily market volume and call the result subsecond participation.

Price change in basis points is `(post_mid - pre_mid) / pre_mid * 10,000`, with benchmark timestamps and quote quality stated. A move from 10.00 to 10.01 USD equals 10.0 basis points. That is co-occurrence, not causal impact. External market movement, news, correlated products, and other participants can explain the change.

A sale at 10.01 against a pre-event midpoint 10.00 has a 10.0-basis-point favorable price difference for that sale under the stated convention. It is not trading profit, which needs inventory, cost basis, fees, hedges, and broader positions. Do not infer a manipulative gain by multiplying a benchmark difference without a justified counterfactual.

## 9. Test ordinary explanations and data defects

For B, the supplied market quote changes before cancellation, and a risk log records a price-response cancellation. The complete window contains no opposite-side fill, so TS-01 is NO_MATCH independently of the explanation. The context is useful but does not establish that every strategy action is legitimate.

Consider adverse selection, inventory limits, hedging, repricing, technical retries, venue rejects, market halts, auction rules, and genuine order amendment as potential explanations when supported. Do not use a generic list to dismiss a specific concern. Test each explanation against exact timing, affected orders, and independent records.

A sequence gap, clock mismatch, duplicate fill, missing cancel acknowledgment, or incorrect replace mapping can create a false pattern. Escalate material data defects separately from market-conduct concerns. Repair and rerun affected observations before representing a completed surveillance review.

## 10. Prepare human review and scenario feedback

For each observation preserve rule result, evidence class, confidence, priority, counterevidence, unresolved elements, and proposed next inquiry. Count unique affected groups separately from rule matches. Do not infer detection accuracy from this designed example, and do not deploy a rule change based on a few selected sequences.

A human reviewer determines whether further inquiry, expanded sampling, legal analysis, trader engagement, control remediation, or an external report is appropriate. This package neither executes those actions nor restricts trading. Maintain a clear boundary between a surveillance lead and a legal conclusion.
