# Output contract — Sampling Design and Assurance Review

## Package rules

Use the exact eight report headings below and exactly two domain tables. The common sheets are Summary, Dashboard, Findings, Evidence, Actions, and QA; defer their exact column names and order to 07-workbook-template.md. Do not add domain-specific fields to common sheets. Store extended frame, draw, and method detail in the report or evidence appendix, with stable locators. Render the same reviewed case record across all formats.

Identifiers and source locators are text. Counts are nonnegative integers. Probabilities and bounds are numeric fractions displayed as percentages to one decimal, while calculation notes retain unrounded values. Unknown numbers are blank in a workbook and null in text interchange, with the reason in notes, limitations, or QA. Zero means a measured zero. A null bound is not 0.0%. A zero denominator produces null.

## Required report heading order

1. Assurance conclusion and restrictions
2. Population scope and selection design
3. Findings and inference barriers
4. Stratum coverage and bounds
5. Selected unit results
6. Evidence and competing interpretations
7. Further testing and reviewer decisions
8. Limitations quality review and human disposition

Section 1 distinguishes actual selected outcomes from a probability-model conclusion. Section 2 preserves the complete frame and selection mechanism. Section 3 separates a failure, missing evidence, and failure to demonstrate a requested assurance threshold. Sections 4 and 5 correspond to SamplingStrata and SampleResults respectively. Section 6 identifies exact source locators and the conditional nature of synthetic randomization. Section 7 states further evidence or design decisions. Section 8 records unresolved human approval and checks actually performed.

## Domain table: SamplingStrata

Exact ordered columns: stratum_id, population_count, probability_selected_count, pass_count, fail_count, unassessed_count, inclusion_probability, upper_bound, conclusion.

| Column | Type / unit | Meaning |
| --- | --- | --- |
| stratum_id | Text, unique key | Pre-outcome stratum |
| population_count | Integer, eligible units | Complete stratum frame; null if unverified count unavailable |
| probability_selected_count | Integer, original probability selections | Excludes targeted supplements |
| pass_count | Integer, conclusive passes | Original selections only |
| fail_count | Integer, conclusive failures | Original selections only |
| unassessed_count | Integer, unresolved selections | Never silently excluded |
| inclusion_probability | Numeric fraction, 0.0% format | Common probability within this simple random stratum |
| upper_bound | Numeric fraction, 0.0% format | One-sided 95% finite bound under file 03, or null |
| conclusion | Required text | Bound target, restriction and decision |

Each row obeys probability_selected_count = pass_count + fail_count + unassessed_count and probability_selected_count <= population_count. The fixture probabilities are 0.75 and 0.5. These table values assume equal probabilities within each stratum; unequal probabilities within a stratum require a redesigned register or approved method rather than misusing a single average. Preserve the change as a new analytical contract.

The fixture's H upper_bound is null because H04 is unresolved. Its L upper_bound is 0.375, for L's original four-unit probability sample only, with alpha 0.05 and the strict tail convention in 03. No overall upper bound is populated. Do not interpret the sum or average of stratum bounds as a population confidence result.

## Domain table: SampleResults

Exact ordered columns: sample_id, stratum_id, population_id, selection_basis, inclusion_probability, result, evidence_ids.

sample_id is a unique text key. stratum_id must resolve in SamplingStrata. population_id identifies the original frame unit. selection_basis is Probability or Judgmental supplement. The exact draw or targeted rationale is held at the referenced evidence locator. result is PASS, FAIL, or UNABLE TO CONCLUDE. evidence_ids is a semicolon-separated string of valid Evidence IDs. Every row, including a missing assessment, must resolve to evidence documenting its status.

inclusion_probability is numeric, displayed as 0.0%, for the actual selection used in inference. It is 0.75 for H original selections, 0.5 for L original selections, and null for the deliberate L07 supplement. L07's null does not assert it had zero chance in the original random design; it records that its observed supplemental inclusion is not a random draw.

SampleResults contains eight rows in the fixture. Exactly seven have Probability basis and reconcile to SamplingStrata. One targeted failure is additional. Overall distinct reviewed IDs total eight, but the statistical sample size remains seven. Dashboard filters must label the selected category, denominator, and inference status. Never divide all eight outcomes by the seven-unit original sample.

## Evidence and rendering semantics

Keep claim class, evidence confidence, statistical confidence level, severity, and reviewer disposition separate. Public references support methods; fictional findings point to SYN-001. Sensitivity estimates of 11.1% and 22.2% are not confidence endpoints. The binomial contrast of 52.7% is not the finite L bound of 37.5%. Display both only with clear method labels.

Before delivery, check that report text, workbook numbers, and dashboard labels retain the missing H04 outcome and targeted L07 result. Filters are views; they must not change stored totals. Themes must work offline with text equivalents for color. If an artifact cannot be generated or inspected, provide the complete text tables and state exactly which format remains unverified.
