# Network and Funds Flow Review — complete analysis method

## Calculation protocol shared by every analytical stage

Define the unit of analysis before selecting a formula. A source item, raw row, account entry, economic transfer, graph edge, customer, case packet, review vote, defect and action are different units. Count each at its declared grain. Never divide a numerator at one grain by an unrelated denominator because both happen to be integers. If a measure combines grains, explain the mapping. For example, a material-defect case rate counts cases with at least one material defect; it does not count every defect and call the result a case rate.

Write the formula in words and symbols, identify every contributing source row and preserve excluded categories. For a monetary bridge, state opening value, inflows, outflows, adjustments and closing value. For a percentage, state numerator, denominator, eligibility, missing-data treatment and display rounding. For a ratio with a zero denominator, report undefined or not applicable under the stated rule; do not return zero by default. For a bound, state the feasibility assumptions and both endpoints. A range produced by missing data is not a confidence interval.

Use the original numeric precision for calculation. Display rounding is the last step. If allocations are rounded to cents, specify how a residual cent is assigned so component amounts exactly equal the total. Do not silently distribute residuals among records or round each component before calculating a rate unless that is the stated method. Where exact decimal arithmetic matters, preserve source strings and use an appropriate decimal calculation capability if available. If only approximate arithmetic is available, disclose the practical precision limit.

Perform an independent conservation or count check appropriate to the measure. Sum detail rows and compare to the independently supplied total when one exists. If no independent total exists, say so; the same detail summed twice is an internal consistency check, not independent completeness evidence. In a graph, conservation applies only to a complete account or explicitly complete perimeter. In a review sample, original votes reconcile to paired cases and reviewer counts, not to a population count that was never supplied.

Test sensitivity only where an assumption changes the result or decision. Change one assumption at a time, recompute the affected quantities and state whether the conclusion changes. Preserve the base case. Do not mix one scenario’s numerator with another scenario’s denominator. A scenario that changes the ownership perimeter must recompute both incoming and outgoing boundary flows; changing only the favorable side creates an incoherent comparison. A scenario that changes source availability must reconsider assessability, not just substitute a new final label.

## Claim decomposition before evaluation

Split a compound conclusion into its component propositions. A sentence that says a customer sent illicit proceeds to a controlled counterparty may contain claims about the transfer, source of funds, illegality, customer knowledge, beneficiary identity and control. The ledger may establish only the transfer. Give each live proposition a source basis and status. A single well-supported component cannot carry the unsupported remainder. The same discipline applies to quality conclusions: an incorrect number, an unreasonable conclusion and a breached policy are distinct propositions.

For each proposition, identify the strongest available supporting evidence and the strongest material contrary evidence. Explain why each matters. Do not merely list source IDs. State what would be expected if the proposition were true, what would be expected under a reasonable alternative and which observations discriminate between them. If the same observation fits both explanations, it has limited discriminatory value even if it is unusual. Keep that observation in the record without exaggerating what it proves.

Use confidence at the proposition level. Confidence in a posted amount can be high while confidence in its economic purpose is low. Confidence in the existence of a reviewer disagreement can be high while confidence in which reviewer is substantively correct is unavailable. Do not average those states into a numerical score without a defensible model. A composite score can conceal exactly the uncertainty a human needs to see. The suite’s categorical confidence labels are qualitative judgments with stated reasons.

## Controlled exception handling

Handle a missing opening balance by preserving visible flows and withholding any calculation that requires a complete funding pool. Do not assume the balance was zero because the first observed event is a credit. Handle an unknown counterparty identity by retaining the recorded node and an unresolved identity link. Do not merge it into a familiar party. Handle a missing source page by limiting conclusions to the visible sections. Do not copy a clause from a similar document. Handle a missing policy version by separating descriptive analysis from policy failure judgments.

Handle a duplicate candidate by comparing identifiers, timestamps, amounts, parties, source origin and execution status. A repeated amount alone is insufficient. If the candidate cannot be resolved, preserve both possibilities as a count or value sensitivity and explain the effect. Do not delete the record to make totals look cleaner. If a duplicate is confirmed, retain a crosswalk to the canonical record so a later reviewer can see why the raw count exceeds the analytical count.

Handle a negative or impossible balance as a diagnostic signal. Check sign convention, missing postings, ordering, account scope, currency and opening balance. Do not immediately call it impossible behavior or create a balancing transaction. A ledger may allow overdrafts under its product terms; the nonnegative assumption must be supplied if used for attribution bounds. If an attribution model assumes no overdraft and the case violates that assumption, the model’s result is unavailable until the rule is revised or the data corrected.

Handle inconsistent currencies by separating native-unit calculations. Do not add USD and another currency as though they were homogeneous. If conversion is required, use a supplied or verified rate with timestamp, direction, convention and rounding. Preserve native amounts and converted values separately. A historical transaction analysis may require a historical rate rather than a current spot rate. This suite’s fixture uses only USD so the worked arithmetic does not silently introduce an exchange-rate assumption.

## Stopping rules and productive continuation

Stop a specific inferential step when its prerequisites are absent. Continue independent descriptive work that remains valid. A blocked source-attribution model does not prevent identifying the observed graph edges. An inaccessible document does not prevent calculating a posted return. A missing historical cutoff does not prevent counting original reviewer votes, but it may prevent judging the original case decision. State exactly which outputs are held and which can proceed.

Do not compensate for missing information by expanding the narrative with speculative possibilities. List only alternatives that are relevant to the supplied facts and capable of affecting the decision. If many possibilities remain, identify the discriminating evidence needed instead of producing an exhaustive imaginary story. The aim is a precise uncertainty record. A long report is useful only when it contains complete reasoning, data and operational steps that the reviewer can inspect.

When analysis produces no material concern under the supplied scope, state the bounded favorable conclusion and the coverage that supports it. Do not manufacture a finding to fill a template. The fixed tables can contain zero findings while retaining evidence, scope, calculations and quality checks. Conversely, do not delete unresolved records to obtain a favorable result. A complete package can legitimately contain no finding, one finding, several findings or an unassessable conclusion.

## Step 01: Define the graph grain

**Decision question:** Does a row represent a message, book entry or executed transfer?

**Required inputs:** The 28 raw representations and their execution status.

**Procedure:** Classify raw records before aggregating. Keep instructions separate from executed transfers. Consolidate a confirmed duplicate with its canonical event and preserve the crosswalk. An own-account transfer may create two book entries but only one economic edge.

**Populated application:** Duplicate E01, instruction E03, pending 250 and the E04 mirror do not add four transfers; the graph contains 24 canonical edges.

**Exception and counterexample:** Three actual onward transfers remain three edges even if their amounts match. Deduplication must not erase genuine repeated movement.

**Required output:** A complete raw-to-canonical bridge with explicit reasons.

## Step 02: Resolve supported identity only

**Decision question:** Which accounts can be grouped into the same entity?

**Required inputs:** The nine-node register and N02 ownership record.

**Procedure:** Maintain account nodes separately from entity grouping. Record the identifier evidence, scope and effective period supporting each grouping. Preserve recorded counterparty labels without upgrading them to verified beneficial ownership.

**Populated application:** A1 and A2 are verified accounts of Entity-A. The other seven node labels remain recorded counterparties with incomplete visibility.

**Exception and counterexample:** Shared names or payment references do not justify an ownership merge. If identity is unresolved, retain separate nodes and model a merger only as a labeled sensitivity.

**Required output:** A grouping map that makes its evidence and limits inspectable.

## Step 03: Preserve temporal feasibility

**Decision question:** Can the directed path occur in the supplied sequence?

**Required inputs:** Hour indices 1–24 and directed edge endpoints.

**Procedure:** Test static topology separately from temporal order. A time-respecting path requires each successive transfer after the preceding transfer under the available timestamp precision. Retain uncertainty intervals when exact ordering is unavailable.

**Populated application:** E09 A1→E, E10 E→F and E11 F→A1 occur in order and form a time-respecting cycle.

**Exception and counterexample:** A cycle in a static drawing may be temporally impossible for the proposed funding story. Do not infer an order from page position when dates are incomplete.

**Required output:** A topology result and a separate temporal result.

## Step 04: Apply conservation within valid perimeters

**Decision question:** Which account balances can actually be reconciled?

**Required inputs:** Complete A1/A2 ledgers with opening and closing balances.

**Procedure:** Calculate account equations first, then consolidate the verified entity while eliminating own-account transfers. Do not require an external counterparty with partial extracts to balance; unobserved activity may exist.

**Populated application:** A1 closes 500, A2 closes 1000 and Entity-A closes 1500. Entity external inflow and outflow are each 34000.

**Exception and counterexample:** A residual at E or F is not proof of a missing transaction because complete counterparty books were never supplied.

**Required output:** Two account equations, one entity equation and explicit unassessed nodes.

## Step 05: Measure fan-in precisely

**Decision question:** Which immediate sources contribute within the named measure?

**Required inputs:** E01/E02/E06/E13/E14/E19 and the sender-node set.

**Procedure:** Count receipts, distinct immediate senders and amount independently. Declare the time window and whether linked returns or cycle inflows belong in the measure. Do not infer common control from concentration.

**Populated application:** P/Q/R provide six receipts totaling 30500 from three distinct recorded sources. Other inbound edges are excluded from this specifically named source-receipt measure.

**Exception and counterexample:** Aliases could affect distinct-node counts; lack of evidence about aliases must be stated rather than guessed.

**Required output:** A measure with exact edge membership and distinct-source membership.

## Step 06: Measure boundary fan-out precisely

**Decision question:** How many transfers and counterparties receive entity outflow?

**Required inputs:** All edges from A1/A2 to nodes outside verified Entity-A.

**Procedure:** Build the boundary transfer set and recipient set separately. Exclude only verified own transfers. Preserve gross transfers even when later returns occur, and report any net measure separately.

**Populated application:** Ten external debits total 34000 and reach five distinct immediate recipients C,D,E,P,F.

**Exception and counterexample:** The transfer count is ten while recipient count is five. A chart label must not interchange those units.

**Required output:** Transfer count, distinct recipient count and gross boundary outflow with explicit units.

## Step 07: Treat cycles as bounded patterns

**Decision question:** What quantity can the observed cycle support?

**Required inputs:** Cycle legs E09=2000, E10=1500 and E11=1000.

**Procedure:** Calculate minimum-edge capacity as a structural upper constraint, then evaluate whether source visibility establishes a positive lower attribution bound. Preserve possible alternative funding at intermediate nodes.

**Populated application:** Cycle capacity is 1000; same-funds attribution may range 0–1000. The sum of its three legs 4500 is not unique cycle capital.

**Exception and counterexample:** No supplied full E/F balances establish that the returned 1000 originated in E09. The topology remains observed even when source attribution is unknown.

**Required output:** Edges, order, capacity, attribution interval and purpose limitation.

## Step 08: Bound commingled source attribution

**Decision question:** What must or may have funded a specific debit?

**Required inputs:** Before E03: opening 1000, P receipt 10000 and Q receipt 8000.

**Procedure:** For source S, other available O and debit D, compute lower=max(0,D-O) and upper=min(S,D), checking that the funding pool is complete and feasible. State the nonnegative fungible-balance assumptions.

**Populated application:** P funding of E03 lies 3000–10000; Q1000–8000; opening 0–1000; combined P+Q11000–12000.

**Exception and counterexample:** Marginal endpoints cannot be combined freely. The individual minima sum 4000 and do not constitute a feasible 12000 allocation vector.

**Required output:** Bounds with assumptions, feasibility and prohibition on a false point estimate.

## Step 09: Compare allocation conventions honestly

**Decision question:** How much does an assumed tracing convention change the assigned amount?

**Required inputs:** The same pre-E03 pool and target debit 12000.

**Procedure:** Apply each convention to the same inputs, label it illustrative and check the component total. Preserve the rounding rule and residual allocation. Keep interval bounds as the evidence-supported conclusion.

**Populated application:** Opening-first FIFO assigns P10000,Q1000,opening 1000. Proportional allocation assigns 6315.79,5052.63,631.58 after cent rounding.

**Exception and counterexample:** Neither method creates observed tracing evidence. Choosing a convenient convention without disclosure overstates certainty.

**Required output:** Feasible alternative vectors with their assumption labels and exact totals.

## Step 10: Link returns locally

**Decision question:** Which original edge can a posted return offset?

**Required inputs:** Explicit N03 links E08→E03 and E21→E15.

**Procedure:** Keep original and return edges, calculate local net amounts and preserve the timing of both. Do not remove the historical gross transfer or cycle from the graph. Require explicit linkage before treating a later inbound payment as a refund.

**Populated application:** E03 net is 11000 and E15 net 3500 after their 1000 returns; total linked returns 2000. E11/E23 are not inferred refunds.

**Exception and counterexample:** Same counterparty and opposite direction do not establish reversal semantics.

**Required output:** Gross topology plus separately linked local net values.

## Step 11: Make visibility limits operational

**Decision question:** Which missing records could change an attribution claim?

**Required inputs:** Complete review-account books and partial onward extracts.

**Procedure:** Identify unobserved openings, inflows and outflows at external nodes. Determine which missing source could narrow a live bound or test purpose. Avoid unrestricted requests unrelated to the decision.

**Populated application:** E may fund E10 from another source and F may fund E11 independently of E10. Those alternatives preserve the observed edges.

**Exception and counterexample:** Absence of an edge in the supplied graph does not establish absence of a transaction in the real world.

**Required output:** A targeted evidence request and a bounded statement of graph coverage.

## Step 12: Separate topology from human adjudication

**Decision question:** What decision is actually supported by the network review?

**Required inputs:** Pattern register, source bounds, purpose explanation and applicable supplied criteria.

**Procedure:** Present observed pattern, quantified limits, reasonable alternative and proposed discriminating inquiry. Do not equate degree, centrality, connection or cycle presence with knowledge, common control or illicit intent.

**Populated application:** The cycle can support a purpose review while the same-funds amount remains 0–1000. A human must evaluate the broader case under actual policy.

**Exception and counterexample:** A high-degree node may be a legitimate processor; graph structure alone cannot resolve economic purpose.

**Required output:** A bounded human review question without an automatic guilt or filing outcome.
