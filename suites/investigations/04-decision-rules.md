# Investigation Case Review — ordered decision rules

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

**Controlled change:** Replace T03 return 2000 with 11000, keeping explicit T02 link.

**Expected result:** Account A close 18000 and entity close 19500; T02 netzero; supplier net 27600.

**Decision consequence:** The full-reversal claim becomes supported for the supplied period, but the original Q/R invoice bridge and purpose question remain unresolved. Zero residual is not proof of benign purpose.


### V02

**Controlled change:** Remove S09 ownership verification while keeping all posted account rows.

**Expected result:** Account A/B balances still tie; entity consolidation is unverified and must be withheld.

**Decision consequence:** Do not delete own-looking transfers from a purported entity boundary until the grouping is supported. The account-level equations remain valid because they do not require entity ownership.


### V03

**Controlled change:** Change INV-A face amount 10000 to 11000 but keep supplier R.

**Expected result:** Amount difference becomeszero; beneficiary Q/R discrepancy remains.

**Decision consequence:** A passed amount test must not automatically set every invoice dimension to pass. Retain separate identity and performance questions.


### V04

**Controlled change:** Provide a supported Q/R beneficiary bridge, but no explanation of 1000 difference.

**Expected result:** Identitydimension resolves; amount gap remains 1000.

**Decision consequence:** Record which evidence changed the identity assessment, retain the original invoice face amount and keep the amount request open.


### V05

**Controlled change:** Remove T03 explicit return reference while retaining incoming 2000 fromQ.

**Expected result:** External incoming 2000 remains observed; linkedT02 return becomes unestablished and T02 linked net remains 11000.

**Decision consequence:** Present a possible-return hypothesis separately; opposite direction and same party alone do not meet the fixture linkage rule.


### V06

**Controlled change:** Add a confirmed duplicate representation of T05.

**Expected result:** Raw received 31; posted representations before dedupe 28; unique posted 27; canonical 24; monetary totals unchanged.

**Decision consequence:** The countbridge needs a new duplicate record and the same canonical target. A larger source-file size does not mean greater economic activity.


### V07

**Controlled change:** Turn pending USD2000 debit into a new posted external supplier transfer, with full evidence.

**Expected result:** Canonical 25; Aclose 7000; entity close 8500; gross supplier 42000 before any linked return.

**Decision consequence:** Update scope, ledger, balances and every affected metric. Do not merely move the status while leaving the supplied closing balance stale; obtain a revised balance source or report its difference.


### V08

**Controlled change:** Remove opening balances for both accounts.

**Expected result:** Net movement A4000,B500 remains calculable; closing equations cannot be independently anchored.

**Decision consequence:** Do not infer zero openings from the first posting. Source attribution and completeness claims requiring known openings must be held.


### V09

**Controlled change:** Add a second linked T02 return 10000 after the existing 2000.

**Expected result:** Cumulative T02 returns 12000 exceed original 11000 by 1000.

**Decision consequence:** Reject a simple negative-net reversal interpretation. Investigate adjustment, interest, wrong linkage or duplicate return before using a residual.


### V10

**Controlled change:** Customer supplies only a new statement saying every payment was legitimate.

**Expected result:** Posted totals and existing evidence gaps remain unchanged.

**Decision consequence:** The new statement is Reported. It can identify a new hypothesis or request direction but does not independently prove amount, beneficiary or delivery.


### V11

**Controlled change:** Omit T04 credit 8000 and T05 debit 7500 from the analytical chronology.

**Expected result:** Net movement differs by 500, while grosscredits differ 8000 and grossdebits 7500.

**Decision consequence:** A review focused only on the net difference understates the omission. Restore both records and re-evaluate their distinct purpose evidence.


### V12

**Controlled change:** Use T01 funding attribution for T02 under complete pre-debit balance.

**Expected result:** Pre-debit pool 17000; source 12000; other 5000; debit 11000; bounds 6000–11000.

**Decision consequence:** Neither one-hour timing nor matching rounded amounts identifies an exact source allocation. A stated FIFO scenario is an assumption, not observed tracing.


## Populated gate register

| decision_id | gate | status | basis | evidence_ids |
| --- | --- | --- | --- | --- |
| D01 | Population and balance gate | COMPLETE | 30 received rows reduce to 24 canonical transfers and 27 posted account representations; both balances tie. | S01;S02;S03;S11 |
| D02 | T02 purpose and beneficiary gate | HOLD_EVIDENCE | USD1000 invoice difference and Q/R bridge remain unresolved. | S01;S04;S05 |
| D03 | T08 purpose gate | HOLD_EVIDENCE | Readable contract and purpose corroboration absent; partial return does not resolve purpose. | S01;S08;S10 |
| D04 | Human case disposition | NOT_RECORDED | No actual authorized reviewer decision supplied. | S12 |
