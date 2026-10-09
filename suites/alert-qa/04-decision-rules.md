# Alert Adjudication Quality Review — ordered decision rules

## Decision precedence

Apply scope and evidence gates before interpretive gates. First establish that the record belongs to the declared population. Then establish what is actually observed. Next apply the appropriate normalization and calculation rule. Only then evaluate the inference against the relevant criterion. Finally identify the proposed human action. A high-priority concern does not waive the need to identify its evidence, and a weak evidence base does not necessarily make the potential consequence low priority.

Treat severity as the consequence or priority of the issue under a supplied rubric. Treat confidence as the strength of the bounded proposition. Treat claim class as the kind of statement being made. Treat recommendation as the analyst’s proposed next step. Treat disposition as the human decision. Do not collapse those fields into a single risk score. A HIGH severity evidence gap can carry LOW confidence about the underlying conduct; a LOW severity formatting defect can be observed with HIGH confidence.

If two rules appear to conflict, identify whether they govern the same decision. An inclusion rule may require retaining an unresolved record while a decision rule prevents a conclusive judgment about it. A formatting rule may require every field while the missing-value rule requires null rather than invention. Preserve both requirements. Where applicable policy genuinely conflicts, record the conflict and refer it to the authorized owner; do not select the most convenient rule without a basis.

## Standard finding construction

Write each finding in this order: bounded condition, criterion and its source class, supporting evidence, quantitative or procedural effect, counterevidence, unresolved limitation, severity rationale, confidence rationale, proposed next step and human-decision status. The title should name the actual defect or observation. Do not use a title that assumes a criminal purpose, legal violation or customer intent when the evidence only establishes an unexplained pattern.

A finding paragraph must be specific enough that another reviewer can disagree with a premise. “The case is weak” is not reproducible. “The case conclusion treats a partial return as a full reversal, although the posted debit is $11,000.00 and the linked return is $2,000.00” identifies a testable defect. A recommendation should target that defect: preserve gross and return records, correct the net calculation, and reconsider any conclusion that depended on full reversal.

## Escalation, closure and unknowns

Use PROPOSED_REVIEW when the analysis recommends human attention. Use HOLD_EVIDENCE when a necessary source is absent. Use HOLD_CRITERION when the evaluative standard is missing. Use READY_FOR_HUMAN when the package is complete under the stated analytical checks. Use HUMAN_DECIDED only when a real decision is supplied. These suite states do not override operational case-system labels or create a regulatory filing obligation.

Do not automatically escalate every unknown as wrongdoing or clear every unknown as benign. Identify what decision would change if the unknown were resolved in each plausible direction. Prioritize the evidence request by that decision sensitivity, potential consequence and available corroboration. A request with no effect on any live hypothesis may be less useful than a narrow request that discriminates between the two remaining explanations.

Where a case involves potential SAR considerations, apply the actual institution type, jurisdiction, relevant rule and supplied authority. The October 2025 FinCEN FAQ distinguishes required reporting from documentation of nonfiling decisions. This suite’s narrative and decision ledgers are an authored analytical design. They must not be presented as a universal requirement to document every nonfiling decision. A quality defect based on documentation must identify the applicable supplied policy rather than inventing a regulatory mandate.

## Quantitative and decision counterexamples

Each variant changes only its stated input. Start again from the unmodified base case for the next variant. Keep variant outputs separate from the canonical case and record every affected dependency. A variant’s purpose is to test a rule; it is not a new allegation or an additional transaction in the base population.

### V01

**Controlled change:** Replace both reviewers’ twelve votes with ACCEPT.

**Expected result:** Observed agreement 100%; expected agreement 100%; kappa undefined.

**Decision consequence:** Do not print kappa 1 or divide byzero. The unanimoussingle-category round contains no category variation for the chance-adjusted denominator.


### V02

**Controlled change:** Delete R2 vote for C12.

**Expected result:** Complete pairs 11, original votes 23; pairwise agreement 8/11 under complete-pair analysis.

**Decision consequence:** Report the missing pair separately and recompute marginals only on the same 11 pairedcases. Do not mix 12-case marginals with 11-case observed agreement.


### V03

**Controlled change:** Use final consensus as both reviewers’ original votes.

**Expected result:** Apparent agreement 100% would be a post-adjudication artifact.

**Decision consequence:** Reject the substitution. Consensus is a later decision; the 24 original votes must remain preserved. Do not report post-discussion agreement as original inter-reviewer reliability.


### V04

**Controlled change:** Add a second material defect to C03.

**Expected result:** Material defects 7,total defects 8; material affected cases remain 6.

**Decision consequence:** Defect rate and affected-case rate diverge. Deduplicate case identifiers before calculating the case rate; retain both defects for remediation.


### V05

**Controlled change:** Resolve C08 evidence and find its reasoning acceptable.

**Expected result:** Consensus ACCEPT5,REWORK6,INSUFFICIENT1; assessable denominator 11; material case 6/11=54.5%.

**Decision consequence:** Original reviewer agreement remains unchanged unless a new blind round is explicitly performed. Do not overwrite historical votes with the new evidence outcome.


### V06

**Controlled change:** Resolve C12 cutoff and find a demonstrated material defect.

**Expected result:** Consensus REWORK7,ACCEPT4,INSUFFICIENT1; selected rework 7/12=58.3%; assessable 7/11=63.6%.

**Decision consequence:** Record the new source and decision-time frame. The new finding is based on resolved evidence, not retroactive conversion of every unknown into failure.


### V07

**Controlled change:** Remove nonmaterial punctuation defect D04.

**Expected result:** Total defects 6; material defects 6; material affected cases 6; consensus unchanged.

**Decision consequence:** This tests that an editorial issue does not drive the substantive pass/rework classification under the supplied rubric.


### V08

**Controlled change:** Supply a genuine applicable internal policy requiring a specified nonfiling rationale field.

**Expected result:** Evaluate actual field presence under that policy; no automatic universal regulatory claim.

**Decision consequence:** A missing field can be an internal policy defect if applicability and effective version are established. The legal-source distinction remains unchanged.


### V09

**Controlled change:** C05 typo changes beneficiary identifier rather than punctuation.

**Expected result:** Materiality must be reassessed; no automatic ACCEPT.

**Decision consequence:** The error label typo does not determine consequence. Inspect whether identity, linkage or outcome is affected and record the resulting criterion-specific defect.


### V10

**Controlled change:** Select twelve easy cases instead of the deliberate calibration packets.

**Expected result:** Observed quality rates may improve while population inference remains unsupported.

**Decision consequence:** Selection design controls generalizability. A lower defect fraction from an easier set does not demonstrate process improvement without a comparable design.


### V11

**Controlled change:** Owner reports all seven repairs complete without revised artifacts.

**Expected result:** Executed repair and closureverification remain unsubstantiated.

**Decision consequence:** Record the owner statement as Reported and request the actual revised records. Do not change remediation to closed on the statement alone.


### V12

**Controlled change:** A reviewer changes C07 to REWORK because source attribution was not attempted.

**Expected result:** Under fixture facts, original bounded handling remains appropriate.

**Decision consequence:** Missingopening balance makes exact attribution unavailable. Penalizing the analyst for refusing to invent it conflicts with the rubric’s substantiation and reviewability rules.


## Populated gate register

| decision_id | question | status | basis | evidence_ids |
| --- | --- | --- | --- | --- |
| D01 | Calibration consensus | RECORDED | 4 ACCEPT,6 REWORK,2 INSUFFICIENT across 12 selected packets | Q14 |
| D02 | Population defect rate | INSUFFICIENT | Deliberate calibration selection does not support population-rate extrapolation | Q15 |
| D03 | Underlying alert or filing dispositions | NOT_RECORDED | Quality consensus does not decide customer conduct or SAR outcome | Q15 |
| D04 | Remediation closure | NOT_RECORDED | Seven proposals exist; no executed repair or closure verification supplied | Q16 |
