# Network and Funds Flow Review — ordered decision rules

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

**Controlled change:** Remove A1 opening balance 1000 without replacing it.

**Expected result:** E03 attribution bounds unavailable; visible edge amounts unchanged.

**Decision consequence:** Do not use a zero opening as a hidden assumption. The graph remains inspectable while the funding pool lacks a necessary boundary condition.


### V02

**Controlled change:** Add an independently observed pre-E03 outside credit 5000.

**Expected result:** P lower becomes 0 and upper 10000; target debit remains 12000.

**Decision consequence:** The added source enlarges other available funds from 9000 to 14000, showing why incomplete coverage can invalidate a positive attribution lower bound.


### V03

**Controlled change:** Change E03 debit 12000 to 20000 with same 19000 available pool.

**Expected result:** Nonnegative pool feasibility fails by 1000.

**Decision consequence:** Do not report bounds from the original formula until missing funds, overdraft terms, ordering or amount error is resolved. A mathematically computed endpoint can be meaningless under failed assumptions.


### V04

**Controlled change:** Assume verified identity groups C into Entity-A, with adequate complete-account evidence newly supplied.

**Expected result:** Boundary classification changes for everyC edge; currentEntity-A equation cannot simply be reused.

**Decision consequence:** This is a perimeter change requiring C opening, complete postings and close. Removing C transfers without adding C balances creates an incomplete consolidation.


### V05

**Controlled change:** Reverse the temporal order of E10 and E11 only.

**Expected result:** Static cycle remains; E09-E10-E11 is no longer time-respecting.

**Decision consequence:** Topology and temporal evidence answer different questions. Do not retain the temporal-cycle label after changing the order.


### V06

**Controlled change:** Double every amount and supplied A1/A2 balance.

**Expected result:** Gross legs 149000; entity in/out 68000 each; P bound 6000–20000; cycle capacity 2000.

**Decision consequence:** This scale test should preserve counts, categories and ratios while doubling every monetary measure. It detects hidden literal specimen values in derived outputs.


### V07

**Controlled change:** Add a raw duplicate of E03 with identical executionreference.

**Expected result:** Raw count 29; canonical edges 24; gross legs 74500 unchanged.

**Decision consequence:** Retain a duplicate crosswalk and inspect whether the duplicate is a representation or a genuinely separate executed transfer before applying this result.


### V08

**Controlled change:** Change E11 value 1000 to 2500 with all else unchanged.

**Expected result:** Cyclecapacity becomes 1500, the minimum of 2000/1500/2500; A1 closing rises 1500 before source close update.

**Decision consequence:** The attribution lower bound remainszero under partial counterparty visibility. Update account close comparison and avoid assuming the increased return came from E10.


### V09

**Controlled change:** Treat E11 as a refund of E09 without source linkage.

**Expected result:** No legitimate base case change permitted.

**Decision consequence:** The required evidence is absent. Record the hypothetical as a separate scenario or request; do not change return_of simply because it creates an attractive net number.


### V10

**Controlled change:** Set all pre-E03 P,Q andopening amounts tozero with debit 12000.

**Expected result:** Funding pool infeasible; no attributionbound.

**Decision consequence:** An empty eligible pool is not a zero-percent source contribution result for a funded debit. It indicates missing data or a violated model.


### V11

**Controlled change:** Combine the individual P/Q/opening lower endpoints 3000/1000/0.

**Expected result:** Sum 4000, not 12000; vector infeasible.

**Decision consequence:** Marginal minima are attained under different allocations. A combined report must respect joint conservation rather than adding independently extreme values.


### V12

**Controlled change:** Use pro-rata amounts without cent residual check.

**Expected result:** Exact values P6315.789473...,Q5052.631578...,opening 631.578947...; displayed cents tie 12000 in this fixture.

**Decision consequence:** Other datasets can leave a one-cent residual. Use the specified residual assignment and retain exact unrounded basis rather than silently accepting a mismatch.


## Populated gate register

| decision_id | question | status | reason | evidence_ids |
| --- | --- | --- | --- | --- |
| D01 | A1/A2 belong to same entity | SUPPORTED | N02 verifies this grouping only; no extension to other nodes | N02 |
| D02 | P funded all E03 | CONTRADICTED | Under GP-1, P can fund at most USD10000 of E03 USD12000; exact contribution remains unresolved within USD3000–10000 | N01;N02;N06 |
| D03 | A1-E-F-A1 proves illicit cycling | PROHIBITED_INFERENCE | Topology and capacity do not prove same funds, purpose or knowledge | N01;N04 |
| D04 | USD74500 is unique suspicious capital | PROHIBITED_INFERENCE | It is gross value of repeated observed legs with different perimeter meanings | N01;N04 |
| D05 | Human disposition | NOT_RECORDED | No actual authorized decision supplied | N06 |
