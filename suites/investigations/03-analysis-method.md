# Investigation Case Review — complete analysis method

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

## Step 01: Build three chronologies

**Decision question:** What happened, when was it recorded, and when was it available?

**Required inputs:** Posting timestamps, source creation dates, receipt dates and original decision cutoff.

**Procedure:** Keep event time, record time and availability time separate. Sort exact postings by timestamp and stable ID; use intervals when precision is absent. A later explanation is a later source about an earlier event, not an earlier known fact.

**Populated application:** T02 occurs Sep 02 at 11:00 AM ET; T03 return is Sep 04. Do not describe the return as known when T02 first posted.

**Exception and counterexample:** Where only a date is supplied, do not invent a within-day ordering or a one-hour interval. Two date-only events may be unordered.

**Required output:** A chronology with exact dates where supplied, explicit uncertainty where not, and no hindsight leakage.

## Step 02: Reconcile source representations

**Decision question:** How many received rows describe unique booked events?

**Required inputs:** Thirty raw representations and the S11 receipt manifest.

**Procedure:** Remove only exact duplicate representations, unexecuted instruction and pending item from booked totals. Retain three B mirror entries in account ledgers but consolidate them with their A legs at economic-transfer grain.

**Populated application:** 30 raw minus duplicate, instruction and pending equals 27 posted account entries; minus 3 own mirrors equals 24 canonical transfers.

**Exception and counterexample:** Do not subtract the same duplicate twice. Do not infer that every repeated amount is a duplicate; T06 andT15 are distinct own transfers.

**Required output:** A mutually explained received-to-posted-to-canonical bridge.

## Step 03: Reperform account equations

**Decision question:** Do the supplied books reconcile before interpreting purpose?

**Required inputs:** Opening and closing balances for A/B and all posted entries.

**Procedure:** Calculate credits and debits independently per account, then compare calculated and supplied closes. Preserve both values and their difference. Do not repair a mismatch by inserting an undocumented balancing entry.

**Populated application:** A5000+46900-42900=9000; B1000+1500-1000=1500. Both differences are zero.

**Exception and counterexample:** A zero difference proves only the supplied equation within its coverage. Offset omissions can leave net totals unchanged.

**Required output:** Two balance equations and a separate completeness statement.

## Step 04: Consolidate the entity perimeter

**Decision question:** Which movements cross Entity-J’s verified boundary?

**Required inputs:** S09 verifies only A/B ownership; the canonical transfers retain both.

**Procedure:** Exclude own transfers from entity external inflow/outflow while preserving their account effect. Keep customer receipts, supplier payments, returns, cash and fees as separate categories.

**Populated application:** Entity opening 6000 plus 42500 receipts plus 3400 returns minus 40000 supplier debits minus 1000 cash minus 400 fees equals 10500.

**Exception and counterexample:** A similar counterparty name is not an ownership bridge. Never consolidate Q orR because it simplifies the narrative.

**Required output:** A perimeter-consistent flow bridge, with internal movement 2500 reported separately.

## Step 05: Link returns explicitly

**Decision question:** Which original debit does each return reduce?

**Required inputs:** S08 references T03→T02, T14→T13 and T22→T08.

**Procedure:** Match explicit parent references and currency. Keep debit and return gross records. Calculate residual per parent and ensure cumulative linked returns do not exceed original debit unless a separate explained adjustment exists.

**Populated application:** T02 net 9000; T13 net 6400; T08 net 5000. Total linked returns 3400 reduce supplier gross 40000 to 36600.

**Exception and counterexample:** An inbound transfer from the same party is not necessarily a refund. T16 is an own-account movement, not a supplier return.

**Required output:** Gross debit, linked return and net unreversed amount, without a loss label.

## Step 06: Separate invoice tests

**Decision question:** Does the document reconcile amount, beneficiary and performance?

**Required inputs:** INV-A, INV-B/D/E/F, INV-C and posted supplier payments.

**Procedure:** Run amount, name/identifier, economic-purpose and delivery tests separately. Passing one does not satisfy the others. Preserve document face text as observed while performance remains corroborated only by appropriate supporting records.

**Populated application:** INV-A10000 namingR conflicts with T0211000 toQ. INV-C2500 matches T10 amount/name but lacks delivery support.

**Exception and counterexample:** Do not call all 20200 remaining gross supplier value unexplained solely because full invoice/delivery matching exists for 19800. Some partial support remains.

**Required output:** A dimension-specific conclusion that identifies exact missing linkage.

## Step 07: Test competing propositions

**Decision question:** Which explanation would the evidence falsify?

**Required inputs:** Six ClaimTests and their source links.

**Procedure:** Phrase each hypothesis so evidence could contradict it. Include the ordinary-business explanation, a bounded unresolved-purpose explanation and the full-reversal claim. Evaluate both supporting and conflicting records.

**Populated application:** CL03 every supplier payment is unexplained is contradicted by 19800 matched invoice/delivery value; CL02 full reversal is arithmetically contradicted.

**Exception and counterexample:** Do not require an innocent explanation to prove every detail while accepting a suspicious explanation without equivalent scrutiny.

**Required output:** Claim-specific status and confidence, with decision-sensitive missing evidence.

## Step 08: Control causal language

**Decision question:** What does rapid timing establish?

**Required inputs:** T01 at 10:00 AM andT02 at 11:00 AM plus opening balance 5000.

**Procedure:** Calculate elapsed time, describe ordering, and then test whether a source-allocation assertion is justified. The account was commingled; payment timing alone cannot identify the exact funds used.

**Populated application:** BeforeT02, A has 17000. Attributing T01 funds to 11000 debit is bounded by 6000–11000 under simple fungible balance assumptions, not an observed 11000 assignment.

**Exception and counterexample:** Do not use the network allocation formula if earlier unknown debits or missing opening balances make the pre-debit pool incomplete.

**Required output:** One-hour observed timing and separately bounded attribution assumptions.

## Step 09: Prioritize requests by decision effect

**Decision question:** Which missing evidence could change the live assessment?

**Required inputs:** RQ01–RQ05 linked to exact claims.

**Procedure:** For each request state the proposition, needed source, period, source owner category, possible responses and effect. Combine related questions only when doing so preserves distinct amount, beneficiary and purpose tests.

**Populated application:** RQ01 asks Q/R bridge,1000 difference and delivery; each can resolve independently. RQ02 asks readable Contract-C but readability alone does not prove execution.

**Exception and counterexample:** Do not request every possible document without a decision reason. Do not claim a request was sent merely because the draft exists.

**Required output:** Proposed, satisfied or inaccessible request state with narrow acceptance criteria.

## Step 10: Write the bounded factual narrative

**Decision question:** Can a reader separate facts, reports and inferences?

**Required inputs:** Canonical ledger, claims, contradictions and source limitations.

**Procedure:** Start with scope and actual assessment. State key amounts with rows, customer explanation with attribution, unresolved conflict with both sides and proposed next step. Include favorable evidence in the main narrative.

**Populated application:** Describe T02 gross 11000, linkedreturn 2000, net 9000, invoice 10000 toR, reported equipmentpurpose and missingbridge.

**Exception and counterexample:** Do not describe 9000 as loss, suspicious value or reportable amount without separately applicable evidence and criteria.

**Required output:** A factual narrative that remains valid even if the human disposition differs.

## Step 11: Assess closure readiness

**Decision question:** Which checks can complete while purpose remains unresolved?

**Required inputs:** DecisionRecord D01–D04 and ProcessQA.

**Procedure:** Separate data reconciliation readiness from substantive case disposition. Mark complete arithmetic checks accurately while retaining evidence holds. Identify the human authority required for the actual case decision.

**Populated application:** D01 is complete; D02/D03 hold evidence; D04 not recorded. This is not an inconsistent state.

**Exception and counterexample:** Do not turn all QA checks green to match an executive summary. A package can be complete for escalation with open evidence questions.

**Required output:** A precise handoff identifying what is ready and what remains undecided.

## Step 12: Handle late evidence as a controlled revision

**Decision question:** What changes if a later source arrives?

**Required inputs:** Prior version, new source identifier, availability timestamp and affected claims.

**Procedure:** Retain the prior assessment, record the new evidence and rerun only affected calculations and implications, then check parity across outputs. Distinguish correction of an old error from a genuinely new fact.

**Populated application:** A later 9000 return linkedT02 would make cumulative returns 11000 and netzero; it would not resolve why the original invoice namedR.

**Exception and counterexample:** A late invoice matching 11000 cannot be treated as available at the initial review date without evidence of prior availability.

**Required output:** An addendum with old/new values, affected conclusions and remaining uncertainty.
