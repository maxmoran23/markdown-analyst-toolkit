# Decision rules — Sampling Design and Assurance Review

## Apply gates in order

| Gate | Required condition | If not met | Permitted next step |
| --- | --- | --- | --- |
| Target | Fixed unit, period, criterion, and estimand | Undefined inference | Agree scope before calculating assurance |
| Frame | Unique eligible units and documented coverage | Supplied-frame restriction | Reconcile omissions and exclusions |
| Design | Known positive selection probabilities and replayable mechanism | Undocumented or judgmental selection | Report selected records only |
| Assessment | Every original selected outcome conclusive | Missingness restriction | Recover evidence or design explicit sensitivity analysis |
| Model | Finite or Bernoulli assumptions fit the target | Unsupported bound | Use the appropriate method or withhold inference |
| Arithmetic | Numerators, denominators, weights and tails verified | Calculation not established | Reperform before disposition |
| Threshold | Approved limit compared with unrounded endpoint | Criterion not established | Obtain human method decision |
| Disposition | Authorized reviewer records judgment | Draft only | Preserve unresolved decision |

Passing the selection gate does not prove the frame complete. Passing the arithmetic gate does not establish reviewer independence. Treat these as separate restrictions. An undocumented randomization can be remedied by recovering the original record; it cannot be repaired by inventing a seed after seeing the outcomes.

## Wording by evidence pattern

| Pattern | Supported wording | Reject |
| --- | --- | --- |
| Judgmental sample with no failures | No failures observed in these selected units | 95% assurance of population effectiveness |
| Probability sample with missing outcome | Observed results plus a missing assessment; estimate restricted | Missing case counted as pass |
| Zero failures under verified finite design | Stated one-sided upper bound for this fixed frame | Zero population failures |
| Large unequal-stratum sample | Weighted estimate using known inclusion probabilities | Raw sample rate as population estimate without justification |
| Targeted supplement finds a failure | Additional observed targeted exception | Add targeted record to random denominator |
| Fully assessed reconciled census | Observed attribute rate for this finite population | Future operations guaranteed correct |
| Threshold not met by bound | Requested assurance is not demonstrated by this design and result | Population failure rate definitely exceeds threshold |

The last distinction is essential. An upper bound above a tolerance means the test does not demonstrate the requested assurance. It does not prove that the true rate is above that tolerance. In the fictional L stratum, U/N = 37.5% exceeds 25.0%; the valid decision is “assurance threshold not demonstrated.” Separately, L07 establishes at least one actual L exception.

## Missingness and changed designs

Retain every selected ID. If an item is proven ineligible under the original rule, preserve its exclusion and apply the rule across the frame. If it is simply unavailable, keep it unresolved. If the criterion expressly requires evidence retention, identify whether the failure is retention, execution, or both. Do not combine a proven retention defect and unknown execution into an unsupported claim of missed performance.

A corrected frame, new stratum boundary, added sample, changed confidence level, or altered tolerable rate creates a method amendment. Record who requested it, when, the original result, the revised plan, and what inference remains valid. Supplemental investigation can be sensible without creating a valid optional-stopping design. A fresh test should have a defined stopping rule before outcomes are reviewed.

## Severity, confidence, and decision ownership

Use HIGH severity for a demonstrated failure with potentially material consequences under the stated fictional objective, MEDIUM for a material evidence or design restriction, and LOW for limited documentation improvements. Do not grade severity by p-value, sample fraction, or confidence endpoint alone. Confidence describes support for a specific claim; a high-confidence observation of a missing artifact does not establish a high-confidence execution failure.

The fixture labels its confirmed approval deviations HIGH and its unresolved evidence gap and assurance restriction MEDIUM. These are illustrative author judgments. An authorized reviewer must assess the actual consequence, applicability, compensating controls, and independence. The assistant cannot certify effectiveness or make an institutional assurance statement by adopting the language of an external standard.

Keep actions concrete: recover a specified artifact, reconcile a specified frame boundary, approve a specified inference method, or investigate a specified failure mechanism. “Increase the sample” is insufficient without a target, design, size rationale, and treatment of prior results. Stop the affected conclusion when a foundational gate fails; continue independent descriptive work that remains supported.
