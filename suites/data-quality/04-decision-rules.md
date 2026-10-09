# Decision rules — Data Quality and Fitness for Use

## Fitness decision table

| Priority | Condition | Draft recommendation | Required explanation |
| --- | --- | --- | --- |
| 1 | Intended use or critical contract unknown | Unable to assess | Missing decision dependency |
| 2 | Population completeness or critical eligibility materially unknown | Restrict or unable to assess | Affected denominator and recovery evidence |
| 3 | Any approved critical gate breached | Restricted use | Every breached rule and affected use |
| 4 | No critical breach, supporting issues exceed agreed tolerance | Review before use | Supporting issue and mitigation proposal |
| 5 | All required checks assessable and within approved criteria | Eligible for human acceptance | Scope, criteria, limits, reviewer pending |

“Restricted use” is a proposed review status in this package. It does not block, quarantine, delete, or change a production feed. Specify which consumer or conclusion should be withheld and what evidence would remove the restriction. Some unaffected uses may remain supportable, but the assistant cannot authorize them simply because they appear low risk.

## Example rule contract

| Rule | Predicate | Eligible population | Critical | Example threshold and boundary |
| --- | --- | --- | --- | --- |
| DQ01 | full_name absent after whitespace check | All six active rows | Yes | Any failure restricts; zero defects required to pass |
| DQ02 | country_code outside US,CA,GB | All six rows | Yes | Any failure restricts |
| DQ03 | birth date absent or calendar-invalid | Five individuals | Yes | Any failure restricts |
| DQ04 | customer_id repeated at one-row-per-customer grain | All six rows | Yes | Both group members fail |
| DQ05 | as-of minus last_refresh greater than 365 calendar days | All six rows | No | More than zero failures prompts review; exactly 365 passes |

These values demonstrate behavior. They are neither legal standards nor recommendations for every institution. Replace them with an approved, purpose-specific contract for a new review and record the change. A missing refresh date is a freshness evidence failure under this example, while a future refresh date is a separate validity concern that requires a named additional rule before its rate is combined.

## Alternatives and exceptions

If a critical value is missing, an independently documented alternate field may sometimes support a narrower use. Assess the alternate's provenance, semantic equivalence, completeness, and consumer acceptance. Do not impute a value because it seems plausible. If records have legitimate multiple business relationships, revise the grain and rerun uniqueness checks; do not waive duplicates individually while leaving the contract wrong.

An exception requires an authorized owner, scope, rationale, duration, compensating evidence, affected consumer, and expiry or review trigger. The assistant drafts the proposal and leaves approval pending. A temporary exception does not convert defective data to clean data; show both the defect and the accepted constraint if a human later supplies approval.

## Severity and confidence

HIGH concerns an evidenced defect that can undermine a critical use, a material unreconciled population, or a systematic failure mechanism. MEDIUM concerns a substantive supporting issue, stale evidence, or a limited ambiguity requiring remediation. LOW concerns a minor issue with limited demonstrated consequence. A large number of trivial formatting defects does not automatically outrank a single critical identity or amount error. Explain materiality using the purpose and affected records, not an invented universal cutoff.

Confidence describes the evidence for the defect and its proposed consequence separately. The impossible date in D02 is HIGH confidence as a validity failure; its actual effect on a particular downstream system is NOT ASSESSABLE without that system's behavior. Retain this distinction in the finding detail.
