# Inputs and evidence — Sampling Design and Assurance Review

## The decision comes before the sample

Name the claim the reviewer wants to make. Estimating the proportion of failed approvals in a fixed quarter is different from finding examples of a failure mechanism, estimating a monetary misstatement, or assessing a continuing process. The first may support a finite-population attribute design; the second may call for targeted investigation; the third needs a monetary sampling model; the fourth needs assumptions about future stability. This suite's numerical fixture concerns binary attributes in a fixed finite frame. Do not import its confidence calculation into a different estimand.

Request the following inputs before choosing a method. Unavailable fields receive an explicit gap and consequence; they do not become zeros.

| Input | Minimum content | Consequence if missing |
| --- | --- | --- |
| Scope and estimand | Period, eligibility, geography if relevant, attribute definition, target population | No defensible population claim |
| Population frame | One stable ID per eligible unit; all included and excluded IDs | Selection cannot be independently replayed |
| Independent control total | Source count, extraction boundary, reconciliation, coverage limitations | Supplied frame only; completeness unverified |
| Selection design | Strata, sizes, probabilities, mechanism, draw record, replacement policy | Selection treated as undocumented or judgmental |
| Outcome criterion | Objective threshold and evidence needed for PASS or FAIL | Assessment cannot be consistently classified |
| Selected evidence | Original artifacts, row locators, availability and result | Missing assessments remain unresolved |
| Inference contract | Target parameter, confidence level, one/two-sided method, tolerable rate | No assurance threshold comparison |
| Review authority | Reviewer role, method approval and requested disposition | Analysis remains a draft |

## Population grain and frame coverage

Write a sentence defining one unit. One transaction, one account, one daily control execution, and one approval opportunity cannot share a denominator without an explicit transformation. A daily control over 500 transactions is one daily execution for an operating test; it is not 500 independent observations. Conversely, one customer with five approvals contributes five opportunities if the question concerns approval correctness. Preserve parent IDs to identify clustering even when the analytical grain is an individual event.

The frame contract contains population_id, eligibility_status, eligibility_reason, stratum_id, source_locator, period, parent_cluster_id if applicable, and outcome_visibility_at_selection. Maintain a counts bridge: raw rows minus confirmed duplicate rows minus ineligible units plus identified omitted units equals eligible frame count. A duplicate removal needs an explanation that two rows represent one unit. Identical values can occur in distinct events. Exclusions are criterion-based, not result-based.

Compare the frame to a separate authorized schedule, ledger total, or extraction control where available. Confirm opening and closing boundaries, timezone, late-arriving records, canceled events, zero-activity periods, and manual channels. A complete list of visible export rows does not establish complete coverage of the intended activity. If omitted units are discovered after selection, preserve the original version and determine whether the probability design must be repeated. Do not quietly add units while retaining old inclusion probabilities.

## Selection manifest and replay information

Retain selection_id, population_id, stratum_id, basis, selection_time, selector_role, frame_version, outcome_visibility, inclusion_probability, draw_record, ordering_rule, algorithm, and any replacement linkage. A genuine simple random sample of n distinct units from N gives each unit probability n/N. That statement depends on the actual mechanism; sorting a convenient list and taking its first n rows does not establish it. A fixed seed without the algorithm, library version, input order, and exact population may not reproduce a draw.

For small exercises, a recorded uniform integer indexing lexicographically ordered combinations makes replay fully specified. The example supplies ranks as fictional inputs and stipulates independent uniform selection before outcomes. It does not claim to have physically performed random draws. In an actual assessment, retain the randomization evidence and method approval, including how the random integer was generated without modulo bias. Avoid selection based on names, availability, outcome values, or a hash whose design was never justified as a probability mechanism.

Keep targeted supplements in their own selection category. A unit's probability of appearing in the original sample can be known while its targeted inclusion has no usable design probability. This distinction matters in the example: L07 had a 0.5 chance of appearing in the probability sample, but its actual supplemental selection was deliberate. The supplemental row's inference probability is null.

## Evidence classification and missingness

Assign stable evidence IDs. SYN-001 denotes the fictional case only; SRC-001 onward denotes accessible case inputs; REF-001 onward denotes public methods. Record title, original locator, date/version, retrieval status, relevant IDs, transformations, and limitations in the analytical record. Common workbook columns remain as specified in 07; put extended provenance in linked report detail rather than changing that schema.

Observed means directly inspectable in the supplied material. Reported means asserted by a source without corroboration. Estimated applies to design-based estimates and confidence bounds. Inferred applies to interpretations connecting facts. Confidence in an observed missing file is not confidence that the underlying activity failed. Use HIGH, MODERATE, LOW, or NOT ASSESSABLE for claim support; the numerical 95% confidence level belongs to the statistical procedure, not this verbal evidence scale.

An inaccessible selected artifact receives UNABLE TO CONCLUDE. Record whether it was missing, unreadable, incomplete, contradictory, or not yet requested. Do not replace it with a passing record and recalculate n as though no problem existed. If retention itself is an explicit tested attribute, the same absence may establish a retention failure while leaving execution unknown. State which attribute drives the outcome.

## Primary method references

| ID | Source and reviewed location | Narrow use and applicability |
| --- | --- | --- |
| REF-001 | [NIST/SEMATECH, confidence intervals for proportions, section 7.2.4.1](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm); reviewed 2026-10-09 | Exact binomial tail inversion and distinction between one- and two-sided confidence limits; a model reference, not sample-design approval |
| REF-002 | [NIST Dataplot, hypergeometric cumulative distribution](https://itl.nist.gov/div898/software/dataplot/refman2/ch8/hypcdf.pdf); reviewed 2026-10-09, pp. 1–2 | Sampling without replacement from a finite population; supports the probability mass function used in the fixture |
| REF-003 | [FFIEC, Risk-Focused BSA/AML Supervision](https://bsaaml.ffiec.gov/manual/ScopingAndPlanning/02); reviewed 2026-10-09 | U.S. supervisory context for relating sample scope to risk and documenting rationale; not a numerical confidence prescription |

A later session must retrieve the relevant source or record that current content is unverified. Public links are locators, not proof of review. The exact example selection, null rules, threshold, and decision gates are the suite author's illustrative analytical choices. Their existence does not make the suite an approved audit methodology.
