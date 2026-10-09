# Analysis method — Monitoring System Independent Challenge and Validation

The following is an authored operational method for the supplied analytical task. Its sequence and fixture parameters are toolkit choices, not an assertion that a regulator prescribes these exact steps. Execute each applicable stage and retain a specific reason when a stage is blocked or outside scope. The completed specimen in file 10 shows the full record trail.

## M01: Bound the reviewed subject

Draw the path from source events to features, decision logic, routing, analyst action and feedback. Identify which components are actually supplied and tested. An opinion should follow the narrowest material untested boundary.

**Exact specimen checkpoint.** The fixture tests supplied feature-level rules and calculations. Raw transaction ingestion, real routing and actual human decisions are outside its evidence.

**Failure or competing explanation.** If a report says the monitoring system is validated after only replaying a predicate, revise the opinion to the tested component and name the remaining boundaries.

## M02: Classify the component before borrowing a framework

Inspect whether the method produces quantitative estimates using statistical, economic or financial theory, or uses fixed deterministic logic and arithmetic. Examine each component separately in a mixed system.

**Exact specimen checkpoint.** R1, I1 and C1 are fixed rules; the feature transform is arithmetic. No fitted probability or theory-based estimate is supplied. Current SR26-2 applicability is not presumed.

**Failure or competing explanation.** An opaque vendor score cannot be classified from its product name. Request design and use information; preserve UNKNOWN classification until sufficient evidence exists.

## M03: Establish objective challenge

Record who developed, selected, implemented and reviewed the component, their expertise, conflicts and ability to escalate disagreement. The review method should permit a finding that the developer’s conclusion is wrong.

**Exact specimen checkpoint.** Fictional test roles demonstrate the workflow only. Actual reviewer qualifications, authority and objectivity remain unrecorded.

**Failure or competing explanation.** If the same assistant generates a reference by copying the implementation, it has not independently challenged implementation fidelity.

## M04: Translate purpose into explicit invariants

Write the exact eligible population, observation window, financial unit, comparator, minimum event counts, identity rule, missing-data state and intended use. Preserve excluded mechanisms as limitations.

**Exact specimen checkpoint.** R1 requires USD amount>=10000, eligible count>=3 and originators>=2. Unknown amount returns unknown before any comparison.

**Failure or competing explanation.** If a count includes reversed or rejected events while the stated purpose concerns posted credits, a numerically correct threshold can still implement the wrong concept.

## M05: Reconcile supplied features

Use an independent manifest to count unique unit IDs, segments, present fields and excluded records. Check uniqueness and all null-bearing fields before calculating performance.

**Exact specimen checkpoint.** V01 through V24 are unique. Each of four segments has six units. Amounts are present for 20 and missing for 4.

**Failure or competing explanation.** A complete unit-ID count does not imply all features are complete; keep 24-unit population coverage separate from 20-unit amount completeness.

## M06: Challenge transaction lineage

Inspect source transaction IDs, postings, reversals, aggregation boundaries, currency conversions and originator identity resolution where available. Reconstruct a sample from source events independently.

**Exact specimen checkpoint.** The specimen intentionally stops at supplied features, so D03 is BLOCKED. No amount aggregation is represented as independently validated.

**Failure or competing explanation.** Do not repair missing source detail by inventing plausible transactions that sum to the supplied feature amount.

## M07: Construct an independent reference oracle

Write the reference function from R1 before examining I1 outputs. Use tri-state semantics so unknown input remains unknown. Validate at equality and just-below values.

**Exact specimen checkpoint.** R1 returns true for V02,V03,V08,V09,V14,V15,V20,V21;false for 12 other present-amount units;unknown for V06,V12,V18,V24.

**Failure or competing explanation.** A reference function that uses I1’s strict greater-than comparator cannot detect the intended boundary defect.

## M08: Reperform implementation outputs

Execute or reproduce the stated implementation on the same unchanged inputs. Separate actual execution of supplied code from arithmetic emulation of a disclosed behavior.

**Exact specimen checkpoint.** I1 returns true for V03,V09,V15,V21 andfalse for 20 others. The fixture is a behavior-level comparison; it does not inspect a production deployment.

**Failure or competing explanation.** If the live implementation contains an additional eligibility filter, it is a different candidate and requires a new comparison scope rather than being quietly folded into I1.

## M09: Classify mismatches by mechanism

Compare output values including unknown versusfalse. Categorize present-input predicate differences, null handling, transformation differences and routing differences separately.

**Exact specimen checkpoint.** There are 8 differences:4 boundary mismatches at V02,V08,V14,V20 and 4 missing-state mismatches at V06,V12,V18,V24.

**Failure or competing explanation.** Do not report 8 missed positives: the four missing-state units have unknown labels. Only the four boundary mismatches are known positive losses.

## M10: Challenge the excluded mechanism

Review whether the intended concept omits relevant activity and whether complementary controls cover that gap. A faithful implementation can still have a narrow concept.

**Exact specimen checkpoint.** R1 excludes V05,V11,V17,V23 because each has only one originator. All four are supplied positive labels in the fictional case.

**Failure or competing explanation.** A specification pass on originator count does not dispose of the concept concern; keepI03 PASS distinct fromC02 FAIL.

## M11: Use a diagnostic challenger transparently

Change one concept assumption while preserving all other inputs and operators. State the purpose of the comparison before reading the result. Do not treat the challenger as an approved replacement.

**Exact specimen checkpoint.** C1 removes the originator minimum while retaining amount>=10000 and count>=3. It captures 12 known positives with no known negatives in this designed fixture.

**Failure or competing explanation.** The constructed label pattern favors this challenger by design. It does not establish superior real-world precision, calibration or operational value.

## M12: Calculate outcomes at the right denominator

Use known labels only for confusion matrices and reconcile unknown labels separately. Retain input-unassessable counts as a different dimension from unavailable outcome labels.

**Exact specimen checkpoint.** All matrices have 20 known labels:12 positive and 8 negative. R1 recall 8/12;I1 recall 4/12;C1 recall 12/12. Precision is 100% in all three, with different alert counts.

**Failure or competing explanation.** A report showing 100% precision without the 4,8 or 12 true-positive count hides the small designed denominator and cannot support an effectiveness conclusion.

## M13: Separate evidence gaps from adverse results

FAIL requires evidence contradicting a stated criterion. BLOCKED means the necessary evidence is unavailable. Neither becomes PASS because the test was documented.

**Exact specimen checkpoint.** Twenty-four tests yield 12 PASS,4 FAIL and 8 BLOCKED. Missing transaction lineage is BLOCKED, while missing-to-false behavior is FAIL because the supplied behavior contradicts R1.

**Failure or competing explanation.** Do not merge FAIL and BLOCKED into one numerical score unless a clearly supplied scoring rule justifies it; a weighted average can conceal a release-blocking defect.

## M14: Evaluate ongoing monitoring feasibility

Define input completeness, version drift, output changes, exceptions and outcome maturation measures with a baseline and owner. Distinguish distribution changes from performance deterioration.

**Exact specimen checkpoint.** Four missing amounts equal 16.7% of 24 units. Four present-input boundary differences equal 20.0% of 20 present amounts. No time-series drift inference is possible.

**Failure or competing explanation.** An alert-rate change can reflect volume, customer mix or source defects. Request comparable periods and stable definitions before attributing it to model or rule decay.

## M15: Specify closure evidence before accepting a fix

For each issue, state the corrected version, exact replay population, unchanged-case expectations, additional boundaries, source evidence and human acceptance needed.

**Exact specimen checkpoint.** I01 requires corrected inclusive comparison;I04 requires unknown routing. Replaying all 24 units ensures the 12 valid negatives and 4 original true hits are preserved while defects are corrected.

**Failure or competing explanation.** A patch that restores four boundary hits but still turns missing amounts intofalse resolves only one mechanism, not the whole implementation issue set.

## M16: Form a bounded validation opinion

State the conclusion about the reviewed version and intended use, then material defects, limitations, untested components and actions. A narrow reproducibility pass can coexist with an adverse use opinion.

**Exact specimen checkpoint.** Do not support release of I1 on the supplied evidence. R1 arithmetic is reproducible, but implementation differs and effectiveness, lineage and governance evidence remain incomplete.

**Failure or competing explanation.** Avoid a single approved stamp. It would obscure which gates are fixture-only passes, which fail and which require actual institutional evidence.

## Calculation order and invariant handling

The calculation order is reference specification, raw feature checks, independent reference function, implementation replay, exact output comparison, mechanism classification, known-label matrix, diagnostic challenger and bounded opinion. Do not derive the reference expectation from the output being tested. Freeze the comparator and null semantics in a small truth table before evaluating the complete population. The fixture checker uses separately declared raw values and explicit expected ID sets, so a shared formula error cannot be concealed solely by comparing two copied implementations.

Tri-state logic is essential. An input can produceTRUE, FALSE or UNKNOWN under the specification. In this fixture, amount is the only nullable predicate input; a null amount yields UNKNOWN even if another supplied condition would be false. This is an explicit specification choice designed to expose incomplete-input handling. A different real specification may use short-circuit three-valued logic, but that choice must be supplied and tested. Do not silently change the specimen rule to make unknown results disappear.

Mismatch counts and outcome errors are different. A reference UNKNOWN versus implementationFALSE difference establishes a null-handling mismatch without establishing a missed known positive. A referenceTRUE versus implementationFALSE difference on a known positive establishes both a fidelity mismatch and a known positive loss. A referenceFALSE on a known positive can be a conceptual coverage limitation even when implementation agrees. The case therefore has 8 fidelity mismatches but only 4 known positive implementation losses; the other 4 known positives missed by R1 concern the originator concept.

A test-state tally summarizes the review register, not system quality. The 24 tests have 12 PASS,4 FAIL and 8 BLOCKED. There is no defined weight that converts those states into a validated percentage. An arithmetic test canpass while its subject’s result is adverse. Outcome matrix reproduction is such a test: the reviewer correctly reproduces I1’s inferior matrix. A failed conceptual or implementation test may be sufficient to restrict use even if many administrative checks pass. The opinion follows the material findings and intended use, not an average score.

## Independent transaction-to-feature replay workpaper

The primary specimen deliberately supplies feature-level records only. Its D03 lineage test therefore remains BLOCKED. The separate demonstration below shows what additional source evidence and calculations a reviewer would need; it does not retrospectively supply the original transactions for V01 through V24. Keep its ID prefix X distinct from the primary V population, and do not add these rows to any primary-case outcome denominator. Its purpose is to make the lineage procedure concrete enough that the assistant does not invent transaction treatment.

For this demonstration only, define a fixed customer-window from May 01, 2026, 12:00 AM UTC through May 30, 2026, 11:59:59 PM UTC, inclusive at second precision. Eligible events are posted USD credits whose original transaction has not been fully reversed. Exclude both the original and reversing representation when the supplied reversal linkage proves a full reversal. Pending, rejected, debit and out-of-window events are excluded. Count economic eligible credits, not ledger representations. Count distinct originator keys after the supplied identity mapping, which here maps A to A, B to B and every other key to itself. These are explicit illustrative rules; a real source specification may treat reversals or posting dates differently and must be tested on its own terms.

| source_id | event_date_utc | type | state | amount_usd | originator | reversal_link | reference eligibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| X01 | 2026-05-01 | CREDIT | POSTED | 4000 | A | null | Included |
| X02 | 2026-05-15 | CREDIT | POSTED | 3500 | B | null | Included |
| X03 | 2026-05-30 | CREDIT | POSTED | 2500 | A | null | Included |
| X04 | 2026-04-30 | CREDIT | POSTED | 6000 | C | null | Before window |
| X05 | 2026-05-31 | CREDIT | POSTED | 7000 | D | null | After window |
| X06 | 2026-05-20 | CREDIT | POSTED | 9000 | E | X07 | Fully reversed original |
| X07 | 2026-05-21 | REVERSAL | POSTED | -9000 | E | X06 | Reversal representation |
| X08 | 2026-05-22 | CREDIT | PENDING | 1000 | F | null | Not posted |
| X09 | 2026-05-23 | DEBIT | POSTED | 2000 | G | null | Wrong direction |
| X10 | 2026-05-25 | CREDIT | REJECTED | 3000 | H | null | Rejected |

The independent feature expectation is amount 4000+3500+2500=10000 USD, eligible_count=3 and originators=2 because A appears twice and B once. The reference R1 must return TRUE and implementation I1 must return FALSE at that exact amount boundary. The ten received representations reconcile to three eligible credits and seven excluded representations, with every exclusion reason preserved. An originator count of three would be wrong: it counts transactions rather than distinct mapped identities. An eligible_count of four could indicate that the fully reversed original was retained; a count of five could indicate that both original and reversal were treated as positive events. Identify the mechanism from exact source IDs instead of guessing from the aggregate discrepancy.

A reviewer should now compare the supplied production feature output with the independently constructed feature expectation. If the amount is wrong but the count and originator count match, inspect sign, amount scale, currency and source-field selection. If all three are inflated, inspect duplicate joins or eligibility before assuming a monetary-conversion problem. If amount is correct but event count is wrong, inspect whether reversals net to zero while still being counted as events. If originator count alone is wrong, inspect identity mapping and whether a null or blank identifier is being counted as a distinct originator. One aggregate mismatch can have several plausible causes; the evidence should determine which transformation failed.

Preserve the received event time and posting time separately. This demonstration uses date-only rows within an explicitly declared second-precision window for illustration, but it does not establish exact intraday timestamps. A real boundary replay needs actual timestamps and timezone normalization. A date-only May 30 record can be included under a date-based specification, while it cannot establish compliance with a narrower intraday cutoff. Do not fabricate midnight timestamps to force a join or infer the order of same-day events. If the reversal arrived after the feature cutoff, distinguish what the historical implementation could know from a later corrected economic view.

For partial reversals, the full-reversal rule above is insufficient. Request the policy and data representation for remaining economic amount, whether the original event still counts toward frequency, and how an originator should contribute after partial cancellation. For chargebacks, returns and corrections, inspect whether the relationship represents cancellation of the original event or a new event with independent risk meaning. Do not extend the demonstration's full-reversal treatment to those mechanisms by analogy alone. Mark the unsupported branch as requiring a supplied specification, and write a dedicated boundary case once that specification is known.

For cross-currency activity, do not apply the USD threshold to a bare numeric amount in another currency. A valid replay requires the original currency, original amount, rate source, rate date, direction of conversion and rounding convention. If those are absent, the converted amount is unassessable even when the event count is known. Keep the conversion uncertainty separate from label uncertainty. A reviewer can verify three eligible event identities without being able to verify their USD aggregate. That partial result must not be promoted into a complete predicate outcome when the amount condition remains unresolved.

A feature replay sample should cover each material transformation branch: inclusion boundaries, time boundaries, posting states, reversals, duplicate joins, identity maps, missing amounts, currency conversion and valid negative controls. The reviewer should explain why those branches matter for this specific scenario. Ten carefully constructed events can expose a defect, but cannot estimate its prevalence or establish that every operational pathway is correct. Use source-population evidence to assess impact after reproducing the mechanism, and preserve separate tests for whether a proposed correction handles affected and unaffected records.

## Opinion construction under different evidence states

An implementation-fidelity opinion can be favorable on a bounded set while the overall use opinion remains restricted. Suppose a proposed I2 reproduces R1 on all 24 primary units and the X lineage demonstration. The supported statement is that I2 matches the supplied reference on those tested records and paths. The remaining four single-originator positive labels still challenge the narrow concept, the primary population still lacks independently supplied transaction lineage, the outcome design remains constructed, and actual reviewer qualifications and authorization are still absent. Do not convert a corrected predicate into an unrestricted system approval.

A conditional use recommendation needs a precisely described permitted purpose, version, population and restriction. For example, a reviewer may recommend further controlled evaluation of I2 on a separately obtained population while withholding production-release support. The recommendation should specify which evidence is needed next and what condition would invalidate the evaluation. It must not imply that the assistant can authorize a pilot, bypass governance or accept risk. An actual human decision, if supplied later, belongs in the disposition record with its scope and evidence, not as a retroactive rewrite of the analytical recommendation.

An adverse opinion should distinguish defects that are demonstrated from concerns that remain unassessed. In the primary fixture, the equality comparator and missing-to-false behavior are reproduced defects. Transaction lineage, representative effectiveness, reviewer objectivity and real authorization are evidence gaps. The single-originator cases are a demonstrated limitation of the chosen concept within the constructed example, but do not quantify live missed activity. This separation tells the recipient what to correct, what to investigate and what cannot yet be concluded. Calling every item a failed model would obscure those differences and assume an unsupported classification.

An inconclusive opinion is appropriate when essential material is unavailable and no supplied evidence establishes how the component behaves. It should still identify the precise unperformed tests and the work that was completed. For example, a reviewer may reconcile the feature manifest while being unable to inspect an opaque score algorithm or reproduce its outputs. State that limitation directly. Do not assign a numerical validation score to compensate for missing evidence, and do not treat the lack of a demonstrated defect as proof that the component performs as intended.

## Correction acceptance and regression sequence

Freeze the original input population and expected reference values before accepting a proposed implementation correction. Run the corrected behavior on every primary unit, preserve old and new outputs, and separately count restored boundary hits, preserved positive hits, preserved valid negatives and restored unknown states. For a reference-equivalent correction, the expected counts are four restored boundary positives, four preserved above-boundary positives, twelve preserved valid negatives and four unknown outputs. Those classes sum to 24 and do not overlap. Any additional true output among the twelve reference negatives is an unintended concept change unless explicitly documented as a new specification.

Next rerun exact equality and neighboring values, minimum event count, originator boundary, missing amount and explicit zero. Compare raw feature checks before interpreting output changes. A data repair that changes input values and a code repair that changes the predicate should be evaluated separately where possible; otherwise the reviewer may be unable to attribute the improvement. Retain the original feature values and label version so a later review can reconstruct what changed. Finally, assess the issue-specific closure evidence and the human acceptance record. A technically correct replay supports closure of the reproduced mechanism only; broader concept, data and governance limitations remain until their own evidence is supplied.
