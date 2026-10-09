# Analysis method — Monitoring Scenario and Threshold Review

The following is an authored operational method for the supplied analytical task. Its sequence and fixture parameters are toolkit choices, not an assertion that a regulator prescribes these exact steps. Execute each applicable stage and retain a specific reason when a stage is blocked or outside scope. The completed specimen in file 10 shows the full record trail.

## M01: Freeze the analytical unit

Define one record as one eligible customer-window with one score at the cutoff. Preserve the window start, end, grouping identity and source controls in a real case. In the fixture, U01 through U36 are already the supplied units; there is no implied transaction-level reconstruction.

**Exact specimen checkpoint.** Reconcile 36 =29 known +4 UNKNOWN +3 CENSORED. Count the positive and negative labels separately:16 and 13. Every candidate must start from the same 36 records.

**Failure or competing explanation.** If a candidate drops records with unknown labels before calculating workload, its apparent workload advantage is invalid because those records still exist operationally.

## M02: Lock eligibility before scores

Write the inclusion predicate independently of whether a unit scores high or already alerted. Eligibility may depend on product, time, ownership or channel, but not on the outcome you are trying to evaluate. Preserve each excluded unit and reason outside the core comparison.

**Exact specimen checkpoint.** All 36 fixture units are eligible. The score cutoff is a candidate decision applied after eligibility, not an eligibility filter.

**Failure or competing explanation.** If an excluded unit is later found to carry the relevant risk mechanism, create a coverage issue and re-scope the comparison; do not silently append it to the best-performing candidate only.

## M03: Protect dependence groups

Assign all related units to the same partition where the intended evaluation assumes group independence. Inspect cross-account and overlapping-window relationships instead of trusting unique row IDs. A row can be unique while its information is duplicated elsewhere.

**Exact specimen checkpoint.** G01 through G06 are TRAIN, G07 through G12 VALIDATION, and G13 through G18 HOLDOUT. Each group has two units and no cross-partition membership.

**Failure or competing explanation.** If G01 appears in HOLDOUT after a join, freeze interpretation of protected performance until the overlap is removed or a dependence-aware method is justified.

## M04: Separate candidate development from evaluation

Use training material to define candidate ideas, validation material for documented comparison, and protected holdout evidence only after candidate and decision rules are frozen. Record the order of access and every revision.

**Exact specimen checkpoint.** The specimen stipulates all four candidates were declared before protected results. That stipulation is an illustrative premise, not evidence that an actual organization operated this way.

**Failure or competing explanation.** If LOW50 was selected after inspecting HOLDOUT labels, report the selection honestly and obtain a new protected evaluation; do not call the old holdout untouched.

## M05: Construct the available-label set

Use POSITIVE and NEGATIVE only when the supplied rubric and cutoff support that state. Keep UNKNOWN for unavailable evidence and CENSORED for outcomes whose observation window has not matured. Neither is a negative.

**Exact specimen checkpoint.** TRAIN has 10 known labels, VALIDATION10 and HOLDOUT9. Their sum is 29; the unavailable counts are 2,2 and 3.

**Failure or competing explanation.** If an unknown unit later becomes positive, update the label version and all affected matrices; preserve the old cutoff results rather than rewriting history.

## M06: Apply the inclusive score predicate

For each candidate, select the threshold using the frozen segment and compare score>=threshold. Do not round the score before comparison unless the specification says to. The fixture scores are integers, but the rule also defines equality and nearby decimals.

**Exact specimen checkpoint.** BASE60 uses 60 everywhere; HIGH75 uses 75; LOW50 uses 50; SEGMENTED uses 55 for RETAIL,60 for SMALL_BUSINESS and 65 for CORRESPONDENT.

**Failure or competing explanation.** A score 60 is a BASE60 hit. A score 59.999 is not. Converting 59.999 to 60 for display must not change the stored predicate result.

## M07: Calculate confusion matrices at unit grain

Within each partition, TP means a known positive raw hit, FP a known negative raw hit, FN a known positive nonhit and TN a known negative nonhit. Sum all four and compare with the known-label denominator before computing rates.

**Exact specimen checkpoint.** For ALL BASE60 the matrix isTP11 FP9 FN5 TN4. Precision 11/20=55.0%; recall 11/16=68.8%. Seven unavailable labels are outside this matrix.

**Failure or competing explanation.** A merged case containing two raw hit units contributes two units to the unit matrix. Replacing those with one case changes the grain and invalidates direct comparison.

## M08: Measure raw workload separately

Count every eligible predicate hit whether its outcome is positive, negative, unknown or censored. This is a detection-stage count, not a case count or an analyst productivity measure.

**Exact specimen checkpoint.** Raw hits are 21 for BASE60,11 for HIGH75,27 for LOW50 and 19 for SEGMENTED. These denominators are 36 units, not 29 known labels.

**Failure or competing explanation.** If a report labels 21 as a false-positive count, reject the statement: it includes known positives and unavailable outcomes as well as negatives.

## M09: Replay suppression before merge

Apply the supplied suppression list to raw hits and preserve the eliminated unit IDs and reason. A suppression may be authorized in a real process, but its existence in an extract does not establish validity.

**Exact specimen checkpoint.** G17 removes U33 and U34 when they hit. U33 is a known positive hit for all candidates. U34 hits BASE60, HIGH75, LOW50 and SEGMENTED; two hits are removed from each.

**Failure or competing explanation.** If a candidate appears to save two alerts solely because G17 was omitted upstream, recover the suppressed ledger and restate both raw and retained results.

## M10: Merge only within the declared group

Create one queued case per candidate and retained group. Select the lexicographically smallest hit unit as lead. Keep the children and their IDs in the case lineage. Do not merge across candidates, partitions or unrelated groups.

**Exact specimen checkpoint.** Queued cases are 11,8,17 and 9 respectively. A case-level workload reduction can arise even if raw coverage is unchanged.

**Failure or competing explanation.** A nonhit sibling is not automatically a detected unit because its group has a case. Credit requires explicit evidence that review scope included that sibling and its relevant activity.

## M11: Calculate workload from routed cases

For each queued group, add the segment lead time and 0.25 hours for each additional retained hit after the first. Sum group costs without rounding intermediate values. The fixture assumes all group units share a segment.

**Exact specimen checkpoint.** BASE60 requires 19.5 hours, HIGH7511.75, LOW5027.0 and SEGMENTED14.5 over the full supplied frame. The illustrative combined capacity is 15 hours.

**Failure or competing explanation.** Do not set a threshold solely to make workload fit capacity. A lower workload can hide missed positives, incomplete labels, unauthorized suppression or a changed unit of counting.

## M12: Preserve segment and incremental effects

Compare candidate and baseline hit sets by exact IDs, partition and segment. Report added known positives, removed known positives, changed negative hits and unavailable outcomes separately.

**Exact specimen checkpoint.** SEGMENTED gains RETAIL U03 relative to BASE60 but loses CORRESPONDENT U11 and U23 and removes UNKNOWN U35. The aggregate known-positive count falls 11 to 10.

**Failure or competing explanation.** A favorable average cannot establish that a segment-specific loss is acceptable. Request explicit rationale and human risk judgment for each material segment effect.

## M13: Review below-threshold activity

Construct the complete nonhit frame for a named reference candidate, fix the selection design and preserve all unselected records. Explain whether the design is probability-based, purposive or a constructed test.

**Exact specimen checkpoint.** BASE60 has 15 nonhits. Assigned ranks select U03,U07,U15,U20,U28,U36. Selected outcomes: 3 POSITIVE, 1 NEGATIVE, 1 UNKNOWN and 1 CENSORED. Nine frame units are not reviewed in this draw.

**Failure or competing explanation.** Do not divide three positives by four known selected labels and call 75% the population missed-positive rate; selection is illustrative and two selected outcomes are unavailable.

## M14: Use uncertainty methods only when justified

Choose the estimand and sampling design before an interval. Binomial intervals assume a relevant trial model; finite-population sampling without replacement may require a hypergeometric treatment. Dependence, deliberate selection and incomplete labels can invalidate a simple interval.

**Exact specimen checkpoint.** No confidence interval is attached to the 36-unit designed fixture. File 10 includes separate mathematical demonstrations labeled as such, with their assumptions and exact inputs.

**Failure or competing explanation.** A narrow interval from thousands of correlated windows does not prove precision if the effective independent information is much smaller or outcomes are selected after alerting.

## M15: Challenge capacity and sensitivity together

Vary one assumption at a time, then evaluate combined plausible changes. Keep unit coverage and routed workload side by side. Examine larger arrival volume, slower review, loss of suppression authority and more complete labels as separate scenarios.

**Exact specimen checkpoint.** Removing G17 suppression adds one correspondent lead and one child, or 2.25 hours, to every candidate. It restores known positive U33 to the routed numerator.

**Failure or competing explanation.** Do not treat an unknown future capacity as an exact number. Supply a range and the conditions under which the chosen candidate would cease to fit it.

## M16: Define change and monitoring gates

Tie a recommendation to data completeness, label design, candidate freeze, routing evidence, implementation replay, capacity plan and human authorization. A candidate can be promising while every deployment gate remains unresolved.

**Exact specimen checkpoint.** LOW50 is further-validation-only. HIGH75 and SEGMENTED are not supported from this case. BASE60 remains a descriptive baseline, not an endorsed live configuration.

**Failure or competing explanation.** A new approved threshold without post-change input controls and rollback evidence can create an unobserved coverage gap; keep the implementation and monitoring dependencies visible.

## Calculation order and invariant handling

The calculation order is population freeze, partition and segment lookup, label classification, candidate predicate, raw matrix and hit count, suppression, merge, workload, incremental comparison, below-threshold review and decision gates. Changing that order can change the meaning of results. For example, suppressing G17 before the raw matrix makes the threshold look less effective while hiding the routing defect. Merging before countingTP andFP changes the unit of analysis. Removing unavailable labels before workload understates operational activity.

LetH(c) be the set of eligible units with score at least the candidate’s segment threshold. LetK be the units with known positive or negative labels. The raw confusion matrix usesH(c) intersectK. LetS be the suppression group set. Retained hitsR(c) areH(c) whose group is not inS. Queued casesQ(c) are the distinct candidate-group pairs represented inR(c). Workload is the sum acrossQ(c) of lead hours plus 0.25 times the number of retained child hits beyond the lead. These are nested but differently grained objects; never replace one denominator with another.

Precision usesTP/(TP+FP). Recall usesTP/(TP+FN). Known-label false-positive rate, if requested, usesFP/(FP+TN), which is not one minus precision. Alert yield and escalation rate require separately defined downstream outcomes and cannot be inferred from the supplied labels. Retained-positive coverage uses known positive raw hits that survive suppression divided by all known positives; it does not credit unhit siblings. Population effectiveness cannot be calculated because the labels are incomplete and the fixture is designed rather than representative.

For an added or removed unit, preserve the baseline hit, candidate hit, label state, segment, partition, routing state and workload contribution. Workload is not additive by raw unit alone because removing a lead can promote a child without eliminating the case’s lead cost. Recompute the whole affected group. If U01 is removed while U02 stillhits, the group still incurs its one-hour lead cost; only the extra 0.25 child cost disappears. This is why summing nominal per-alert savings can overstate capacity relief.
