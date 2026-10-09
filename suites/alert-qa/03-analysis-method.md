# Alert Adjudication Quality Review — complete analysis method

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

## Step 01: Freeze the reviewable packet

**Decision question:** What evidence could the original analyst have considered?

**Required inputs:** Original case text, attachments, decision timestamp, source availability chronology and version.

**Procedure:** Retain the original case and make later evidence a separate layer. Judge the historical reasoning against its available record; assess a later source as a new fact or a correction with a stated effective time. Preserve the difference between unreasonable original reasoning and a reasonable decision overtaken by later events.

**Populated application:** C12 combines later documents with earlier material without availability dates. The original decision cannot be assessed, so consensus is INSUFFICIENT.

**Exception and counterexample:** Do not cure the missing cutoff by using the latest document date. Do not assume every attachment existed when the case was decided.

**Required output:** An evidence-at-decision snapshot or an explicit assessability hold.

## Step 02: Apply supplied criteria before preferences

**Decision question:** What makes a condition a quality defect?

**Required inputs:** CP-QA-1, its eight criteria and the actual case proposition.

**Procedure:** Map each proposed defect to an applicable criterion. State whether the criterion is internal policy, procedure, legal requirement or authored review method. Check its effective date and scope. A stricter reviewer preference is not automatically a failed requirement.

**Populated application:** C11 must be evaluated against the supplied brief-rationale policy. The absence of a nonfiling memorandum is not itself a universal BSA violation.

**Exception and counterexample:** A reviewer may recommend better explanatory practice without mislabeling the recommendation as a mandatory legal requirement.

**Required output:** Criterion-linked findings with source class and a practical consequence.

## Step 03: Separate assessability from correctness

**Decision question:** Can the reviewer determine whether the conclusion is supported?

**Required inputs:** Readable source set, coverage and decision-time record.

**Procedure:** Use INSUFFICIENT when a necessary review input is absent. Do not translate that state into ACCEPT or automatic REWORK. If an independent demonstrated defect is visible despite an overall evidence gap, record the defect and the broader assessability limitation separately.

**Populated application:** C08 cites an inaccessible encrypted document. Its conclusion is unassessable on this packet; the reviewer cannot truthfully say the document contains no support.

**Exception and counterexample:** Do not reward missing evidence by excluding the case invisibly from the denominator. Show unknowns alongside assessable results.

**Required output:** A transparent unknown category and a narrow request for the missing review input.

## Step 04: Reperform calculations and gross coverage

**Decision question:** Does the claimed result follow from all relevant rows?

**Required inputs:** Posted amounts, explicit return linkage and chronology source set.

**Procedure:** Calculate gross debits, returns, residual amounts and population totals independently. Check whether a correct net masks omitted gross events. Identify the exact case conclusion that would change if the calculation is repaired.

**Populated application:** C03 has debit 11000 and linked return 2000, so residual 9000. C06 omits credit 4000 and debit 3500; net 500 cannot stand in for both missing events.

**Exception and counterexample:** Offset omissions may produce a correct closing balance. A balance tie is not a complete chronology test.

**Required output:** Reproducible calculation defects and an outcome-dependency review.

## Step 05: Test identity substantiation

**Decision question:** Did the analyst combine subjects beyond the supplied evidence?

**Required inputs:** Source identifiers, alias links and the aggregation being used.

**Procedure:** Inspect each merge that changes the case amount, chronology or inference. Require a supplied identity bridge appropriate to the proposition. Preserve similar names as separate records until the bridge is supported; show alternative aggregation only as a scenario.

**Populated application:** C04 merges similarly named beneficiaries despite different supplied identifiers. Split the subjects and recompute each aggregate before reassessing the pattern.

**Exception and counterexample:** Different identifiers can sometimes reflect the same subject, but that requires evidence. Similarity alone does not establish either sameness or difference conclusively.

**Required output:** An identity-specific defect with a clear recalculation path.

## Step 06: Evaluate counterevidence

**Decision question:** Did the case address material contrary information fairly?

**Required inputs:** All sources relevant to the challenged condition, including favorable records.

**Procedure:** Identify the strongest contrary source and test its relationship to the same payment, date and party. Determine whether it changes the condition, confidence or proposed action. The reviewer need not adopt the alternative explanation, but must distinguish reasoned rejection from omission.

**Populated application:** C02 includes a matched invoice and delivery evidence while the narrative asserts no business support. That assertion requires correction and reconsideration.

**Exception and counterexample:** A disagreement about weighting is not automatically an omission defect. Read the actual reasoning and compare it to the applicable criterion.

**Required output:** A finding that identifies the omitted proposition and its possible decision effect.

## Step 07: Classify materiality by consequence

**Decision question:** Could correction change the substantive reasoning or required process?

**Required inputs:** Defect condition, affected fields and the supplied materiality rule.

**Procedure:** Use MATERIAL for errors capable of changing identity, amount, evidence evaluation, claim strength or an applicable required process. Use NONMATERIAL for bounded editorial issues with no such consequence. Explain the effect rather than relying on an error label.

**Populated application:** C05 has punctuation without loss of meaning or source traceability, so it remains ACCEPT. C10 asserts intent beyond observed timing and needs substantive REWORK.

**Exception and counterexample:** A typographical error in an account identifier or amount can be material. Conversely, a different defensible phrase need not be a defect.

**Required output:** A reasoned materiality label separate from severity and confidence.

## Step 08: Preserve original independent votes

**Decision question:** What did each reviewer conclude before seeing the other assessment?

**Required inputs:** Two reviewers, twelve packets, recorded round and packet version.

**Procedure:** Capture each original vote and criterion basis before discussion. Keep later consensus in a separate record. If blinding was not maintained, describe that limitation rather than calling the round independent. Track repeated rounds separately.

**Populated application:** The fixture contains 24 original votes and 12 paired cases. Reviewers disagree on C02, C06 and C11 before consensus.

**Exception and counterexample:** Replacing original ratings with final consensus would manufacture perfect agreement and erase the calibration signal.

**Required output:** A durable vote ledger with timing, round and later adjudication linkage.

## Step 09: Calculate nominal agreement correctly

**Decision question:** How does observed agreement compare with the recorded category marginals?

**Required inputs:** Complete paired ACCEPT, REWORK and INSUFFICIENT votes.

**Procedure:** Compute observed agreement, each reviewer’s category counts, chance agreement from marginal products and unweighted Cohen kappa when its denominator is nonzero. Preserve the three categories as nominal outcomes; do not apply ordinal weights without a justified ordered scale.

**Populated application:** Observed agreement is 9/12. Marginal products total 52, so expected agreement 52/144 and kappa 14/23, approximately 0.6087.

**Exception and counterexample:** Kappa is not accuracy, a probability that a review is correct or a universal adequacy verdict. If expected agreement equals one, kappa is undefined.

**Required output:** Agreement, marginals, kappa and the limitations needed to interpret them.

## Step 10: Adjudicate through evidence

**Decision question:** Why should the final consensus differ from an original vote?

**Required inputs:** Original ratings, applicable criterion and exact source span.

**Procedure:** Describe the disputed premise, compare each reviewer’s criterion interpretation and decide the bounded issue under the supplied authority. Preserve the reason, unresolved question and any resulting policy clarification. Do not treat majority preference as independent truth.

**Populated application:** C02 resolves to REWORK for omitted contrary evidence; C06 for missing relevant rows; C11 for the unsupported universal legal premise.

**Exception and counterexample:** Consensus may still be INSUFFICIENT when the needed evidence is absent. Discussion cannot create a missing source.

**Required output:** A calibration decision that explains the substantive rule for future cases.

## Step 11: Use explicit quality denominators

**Decision question:** Which cases and defects are included in each reported rate?

**Required inputs:** Twelve selected cases, two unassessable cases, six material-defect cases and seven total defects.

**Procedure:** Report selected-case and assessable-case rates separately, retaining unknown counts. Count affected cases uniquely and defects at their own grain. Describe the selection mechanism before considering extrapolation.

**Populated application:** Six of twelve selected cases require rework,50.0%. Six of ten assessable cases have a material defect,60.0%. Seven defects include one nonmaterial issue.

**Exception and counterexample:** The selected calibration set is deliberate, so neither rate estimates the population defect rate. Dividing seven defects by twelve does not produce a case-failure rate.

**Required output:** Rates whose numerator, denominator, selection and missingness are visible.

## Step 12: Verify repairs before closure

**Decision question:** What would demonstrate that the specific defect is fixed?

**Required inputs:** Proposed repair, revised case version and independently reperformable closure test.

**Procedure:** Distinguish proposal, execution, retest and authorized closure. Reopen the corrected artifact and inspect every dependent calculation or sentence. A repair can be partial; identify any remaining defect explicitly.

**Populated application:** M02 requires gross 11000, return 2000 and residual 9000 to agree across tables and narrative, followed by reconsideration of the prior full-reversal conclusion.

**Exception and counterexample:** A statement that the case was fixed is not closure evidence. The fixture includes proposals only and records no executed repair.

**Required output:** Verified correction within scope or a clear open-remediation state.
