# Decision rules — Monitoring Scenario and Threshold Review

These rules govern the analytical output. They are deliberately explicit so the assistant cannot fill nuanced decisions with an unstated default. They do not authorize operational changes or replace the applicable human process. Use the exact branch that matches the evidence, keep competing interpretations visible and record the evidence needed to move to another state.

## T-R01: Missing score

**Trigger.** An eligible unit has a demonstrably absent, unreadable or invalid score in the inspected source at the frozen cutoff.

**UNKNOWN branch.** If score availability or validity cannot be established, mark its scoring state UNRESOLVED and request the source; do not assign zero or calculate a hit/nonhit result.

**Required branch.** Do not calculate hit status for that unit; retain it as unscored and reconcile separately.

**Forbidden substitution.** A missing score is never zero, a negative label or an exclusion authorized by this suite.

**Exact specimen or boundary case.** U03 score=null would remove one calculable raw decision and require a revised matrix denominator, not an automatic miss.

## T-R02: Unknown label

**Trigger.** The inspected outcome ledger explicitly records UNKNOWN, or the evidence required by the stated label rubric is absent for that unit.

**UNKNOWN branch.** If label status cannot be established, retain an unresolved label outside TP, FP, FN and TN while preserving the unit in population and workload accounting.

**Required branch.** Keep the unit in hit and routing counts; exclude it from the known-label confusion matrix.

**Forbidden substitution.** Do not count UNKNOWN or CENSORED as TN when the score is below threshold.

**Exact specimen or boundary case.** U35 is an UNKNOWN BASE60 hit and remains in raw workload but outside TP/FP.

## T-R03: Censored outcome

**Trigger.** The stated observation window has not matured by the cutoff, or the inspected label ledger explicitly documents CENSORED on that basis.

**UNKNOWN branch.** If maturity dates or the reason for missing outcome are unavailable, retain an unresolved outcome and request timing evidence; do not assert that censoring or a negative outcome has been established.

**Required branch.** Identify the unavailable maturity window and preserve the original cutoff.

**Forbidden substitution.** Do not call a recently unconfirmed concern a negative outcome simply because review has not completed.

**Exact specimen or boundary case.** U36 remains CENSORED and appears in the selected below-threshold draw without a known result.

## T-R04: Threshold equality

**Trigger.** A valid score equals the documented threshold for the unit’s segment and the frozen comparator is explicitly known.

**UNKNOWN branch.** If the score, segment, cutoff or comparator is unknown, do not infer equality treatment; mark the predicate result unresolved and obtain the exact specification.

**Required branch.** Use the exact frozen comparator at full precision.

**Forbidden substitution.** Display rounding cannot change whether the unit qualifies.

**Exact specimen or boundary case.** An added test score 60 must hit BASE60 and miss HIGH75.

## T-R05: Suppressed positive

**Trigger.** A unit has a supported POSITIVE label, meets the frozen raw predicate, and the inspected routing ledger shows that suppression removed its hit.

**UNKNOWN branch.** If label, predicate or suppression evidence is missing, record the unresolved routing/coverage question without asserting a confirmed suppressed positive or a reviewed case.

**Required branch.** Record both the raw detection and downstream loss; route the authorization gap for review.

**Forbidden substitution.** Do not silently delete the suppressed row or count a raw hit as completed review.

**Exact specimen or boundary case.** U33 is detected by every threshold but reaches no case while G17 remains suppressed.

## T-R06: Merged child

**Trigger.** The inspected routing data shows a retained raw hit assigned to the same authorized merge key as another hit, and the specified lead rule identifies it as a child.

**UNKNOWN branch.** If merge identity, eligibility or lead selection is unresolved, retain distinct raw hits and an unresolved routing state; do not collapse cases or credit a nonhit sibling.

**Required branch.** Retain child identity, outcome and source linkage while counting one queued case per group.

**Forbidden substitution.** Do not credit nonhit siblings or merge across partitions.

**Exact specimen or boundary case.** U02 joins U01 in a BASE60 case; both remain separate matrix units.

## T-R07: Known-positive loss

**Trigger.** Exact unit-set comparison shows a supported known positive hit under the baseline and a nonhit under the proposed candidate on the same frozen population and label version.

**UNKNOWN branch.** If either result, label or population alignment is unverified, report a possible loss requiring evidence; do not state an observed loss or treat coverage as unchanged.

**Required branch.** List exact IDs and mechanism; require specific challenge before supporting the candidate.

**Forbidden substitution.** An aggregate precision improvement cannot on its own justify the loss.

**Exact specimen or boundary case.** HIGH75 loses U11 and U23 compared with BASE60.

## T-R08: No positive labels

**Trigger.** The complete, reconciled known-label subset for the stated partition or segment contains exactly zero POSITIVE labels, so TP+FN is demonstrably zero.

**UNKNOWN branch.** If positive-label coverage or the denominator is unknown, report recall as not assessable for that reason; do not assert that the denominator equals zero or report perfect recall.

**Required branch.** Return recall=null and state that the positive denominator is zero.

**Forbidden substitution.** Do not show 100% recall because no missed positives were observed.

**Exact specimen or boundary case.** A negative-only segment has no estimable known-positive recall in that subset.

## T-R09: No known alerts

**Trigger.** The complete, reconciled known-label comparison shows exactly zero alerted known labels for the stated candidate and subset, so TP+FP is demonstrably zero.

**UNKNOWN branch.** If hit or label completeness is unknown, report precision as not assessable and preserve unresolved hits; do not claim that the known-alert denominator is zero.

**Required branch.** Return precision=null and retain raw unknown hits if present.

**Forbidden substitution.** Do not show 0% or 100% precision from an empty known-alert denominator.

**Exact specimen or boundary case.** A candidate that alerts only U35 has raw workload but no known-label precision.

## T-R10: Holdout reuse

**Trigger.** A documented access or change record shows that protected outcomes were inspected before a later candidate or selection rule was fixed.

**UNKNOWN branch.** If access and freeze history are unavailable, mark holdout independence unverified; do not claim either a protected holdout or a confirmed reuse event without evidence.

**Required branch.** Mark the protected evaluation as consumed and restrict claims to descriptive reuse.

**Forbidden substitution.** Renaming the same data does not create a new holdout.

**Exact specimen or boundary case.** If a fifth threshold is chosen after the four-candidate results are seen, require new protected evidence.

## T-R11: Unevidenced capacity

**Trigger.** The requested workload comparison lacks supplied capacity evidence, or its hours, task scope or productive-time basis is explicitly only an illustrative assumption.

**UNKNOWN branch.** If the capacity basis is unclear, label the capacity gate unresolved and request it; do not select a threshold or assert a staffing shortfall from an invented target.

**Required branch.** Present workload as an assumption-dependent estimate and request measured operating inputs.

**Forbidden substitution.** Do not infer staffing headcount from illustrative lead hours.

**Exact specimen or boundary case.** The 15-hour fixture capacity is a comparison assumption, not an institutional service standard.

## T-R12: Nonprobability below-threshold review

**Trigger.** The documented below-threshold selection is purposive, convenient or constructed, rather than a verified probability sample from a complete frame.

**UNKNOWN branch.** If the selection mechanism or frame completeness is unknown, classify the design as unverified and withhold probability-based prevalence claims or intervals.

**Required branch.** Use findings to identify specific defects and formulate further review; disclose selection.

**Forbidden substitution.** Do not attach design-based prevalence bounds or extrapolated missed counts.

**Exact specimen or boundary case.** The six assigned-rank fixture reviews identify three positives but do not estimate all 15 nonhits.

## Severity and confidence rubric for this specimen

| dimension | decision rule | limit |
| --- | --- | --- |
| HIGH severity | A reproduced loss of intended review, material population gap, silent unknown conversion or major evidence limitation that restricts the central conclusion | Illustrative prioritization; not a statutory rating |
| MEDIUM severity | A material process, lineage or governance weakness requiring correction or human decision, with the immediate effect bounded by the supplied evidence | Do not downgrade merely because the cause is easy to fix |
| LOW severity | A nonmaterial presentation or documentation issue that does not change the population, result or decision | Escalate if it hides a material fact |
| HIGH confidence | Directly inspected evidence or independently reproduced fixture result supports the observation | Does not extend confidence to live effectiveness |
| MODERATE confidence | Partial evidence supports the observation but a credible alternative remains | Name the unresolved alternative |
| LOW confidence | Limited or conflicting material permits only a tentative inference | Do not convert it to an observed finding |
| NOT ASSESSABLE | Necessary evidence is absent and no supported judgment is possible | Maintain the missing-data state rather than inventing a score |

## State-transition record requirements

Every transition must retain prior state, proposed next state, triggering evidence, reason, responsible role and actual disposition when supplied. A state changes because evidence or authorization changed, not because a deadline or dashboard target was reached. Preserve the original transition in the history even when later corrected. A rejected proposal remains visible with its rationale; a reopened item retains the earlier closure basis and the new information that defeated it. The fixture uses completed fictional calculations but leaves actual institutional approvals unrecorded.
