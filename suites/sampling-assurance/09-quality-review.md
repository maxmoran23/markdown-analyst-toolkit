# Quality review — Sampling Design and Assurance Review

## Review the claim before the formatting

Reperform the analysis from the raw frame and selection instructions, not from the expected totals alone. Confirm that the requested parameter matches the unit actually tested. Ask a second reviewer to identify a plausible way the conclusion could be wrong: an omitted channel, an outcome-dependent draw, a missing assessment correlated with failure, a duplicated unit, or an incorrect probability model. A polished dashboard cannot settle these questions.

| Check | Procedure | Required evidence |
| --- | --- | --- |
| Stage | Compare attachments and saved record to 01 | Actual accessible filenames and body checks |
| Grain | State what one population row represents | Scope and attribute definition |
| Frame | Reconcile raw, excluded, duplicate and included counts | ID-level bridge and independent total if available |
| Design | Replay selection with original order and draw record | Selected IDs and selection audit trail |
| Probabilities | Confirm every eligible unit's chance | n_h/N_h and design explanation |
| Outcomes | Recount PASS, FAIL and unresolved | All original selected IDs retained |
| Inference | Recalculate tails and integer endpoint | Unrounded values and alpha convention |
| Supplements | Keep targeted results outside probability counts | Separate selection basis and totals |
| Rendering | Match all artifacts to the reviewed record | Reopened files or explicit untested status |

## Mandatory example checks

Reproduce H rank 2 from the four size-three combinations and L rank 49 from the seventy size-four combinations. Expected primary IDs are H01, H03, H04, L02, L04, L06, and L08. Expected additional targeted ID is L07. Confirm that H02, L01, L03, and L05 were not assessed. Unselected does not mean passed.

Reconcile the frame at twelve, primary selection at seven, and total distinct reviewed at eight. Primary outcomes are five passes, one failure, and one unresolved; all reviewed outcomes are five passes, two failures, and one unresolved. Verify primary coverage 7/12 = 58.3%, distinct review coverage 8/12 = 66.7%, primary confirmed-failure share 1/7 = 14.3%, and primary unresolved share 1/7 = 14.3%. A conclusive primary share of 1/6 = 16.7% has a different denominator and does not resolve missingness.

Check unequal-stratum weights and the two completion scenarios: 1/9 = 11.1% and 2/9 = 22.2%. They must be labeled hypothetical point estimates. Verify L's zero-failure tail at D = 3 and D = 4, its integer bound U = 3, and its 37.5% upper rate. Confirm that 37.5% exceeds the illustrative 25.0% acceptance limit while not proving the true rate exceeds it. H and overall bounds remain null.

## Negative controls that must fail

1. Change H04 to PASS merely because its execution is reported complete. The missing-evidence check must reject the unsupported classification.
2. Insert L07 into n_L and calculate a new random-sample rate. The design and supplement checks must reject the mixed denominator.
3. Use 1/7 as the stratified population estimate without weights. The unequal-inclusion check must reject it, even before addressing missingness.
4. Call the 11.1%–22.2% sensitivity range a 95% interval. The inference-label check must reject it.
5. Call the binomial 52.7% number the exact finite L bound. The model check must reject it.
6. Assert that a 95% upper bound guarantees 95% of records passed or assigns 95% probability to the fixed unknown D. The interpretation check must reject both statements.
7. Change a frame ID after drawing while retaining the same manifest. The frame-version check must fail.
8. Replace a missing record and delete its original row. The original-selection reconciliation must fail.
9. Sum nominal stratum bounds into a 95% overall bound. The simultaneous-inference check must reject the unsupported confidence claim.

Record each mutation, the rule it violates, and the observed rejection. Saying “negative controls reviewed” without the mutations and results is not a preserved example check.

## Source and independence challenge

Verify source passages against the actual statistical claim. NIST's binomial tail formula does not establish that a sample was randomly selected. FFIEC's risk-focused discussion does not require this fixture's 25.0% threshold or endorse its sample size. A cited title alone is insufficient to support a numerical method. Keep retrieved, not retrieved, superseded, and inaccessible statuses visible.

Ask who chose the sample, performed the assessment, and approved the conclusion. Random selection is not organizational independence. An assistant cannot declare itself an independent audit function. The example stipulates uniform draws for teaching; it has no evidence of real-world randomization or live frame completeness.

## Delivery and restart checkpoint

Inspect exact report headings, sheet names, columns, numeric formats, nulls, evidence foreign keys, and legend text. Reopen generated files if a compatible reader exists. Test dashboard filters and both themes, and check that full population totals remain distinguishable from filtered results. Record unavailable visual or formula checks instead of claiming them passed.

Save the suite version, raw inputs, frame, design, draw ranks, outcomes, calculations, failed negative controls, reviewer comments, and unresolved decisions. Render from that complete checkpoint. If any interpretation or evidence changes, return to Analyze for the affected scope and preserve both versions. Completion of arithmetic is a QA result; it is not approval of an assurance opinion.
