# Output contract — Customer Risk Review

## Package and interchange rules

The final package contains a report, workbook, and optional dashboard, plus a visible limitations and QA statement. Use the report headings listed below in exactly that order. Do not rename the workbook tabs or rearrange the domain columns. The common tabs are Summary, Dashboard, Findings, Evidence, Actions, and QA; their exact schemas and styles are in 07-workbook-template.md. Append the two domain tables described here after those common tabs. Templates 06 through 08 control presentation; this file controls analytical semantics.

Identifiers, codes, and source locators are text even when they look numeric. Counts are nonnegative integers; rates are numeric fractions from zero to one and display as percentages to one decimal. Retain the numerator and denominator that produce each rate. Amounts must include an explicit currency and must not be summed across currencies without a named conversion method. Use ISO dates in machine tables and human-readable dates in narrative. A date with an unknown timezone cannot establish an intraday ordering.

Represent an unknown numeric or date value as a blank cell with an explicit explanation in the associated notes, limitation, or QA row. In text interchange use null. Never use zero, a dash, or N/A as a numeric stand-in. Distinguish Unknown, Not supplied, Not applicable, Not tested, and Unreadable in explanatory text. A true zero is a measured result. A zero denominator yields null, not a zero rate. Do not silently exclude failed or unassessed records from the denominator.

Keep evidence IDs as stable strings, separated by semicolons when a table cell needs multiple IDs. Findings must identify the affected population, factual observation, criterion, consequence or uncertainty, recommendation, alternative, and reviewer decision needed. Preserve severity, confidence, and claim class as distinct fields. Actions have a role owner, dependency, expected evidence of completion, and an unapproved proposed due date where relevant. Do not fabricate a person's acceptance or a completed review.

Avoid formulas that depend on locale-specific text interpretation. When calculation tools are available, store numeric values as numbers, preserve formulas where the format supports them, and check cached results or recalculate after reopening. When using text tables, give formulas in a method note and supply reconciled computed values. The same totals must appear in the report, workbook, and dashboard. Format discrepancies are QA failures when they alter meaning.

The dashboard is a view of the same evidence and decisions. Filters must show the denominator used; a filtered count cannot silently replace the full population count. Color accompanies text, never replaces it. Keep the supplied restrained light and dark themes, accessible contrast, visible selected filters, and an explicit fictional-data banner for the example. No external network resources, live source fetches, auto-sends, or operational changes belong in the dashboard.


## Required report heading order

1. Customer review conclusion
2. Population scope and scoring method
3. Material profile findings
4. Customer factor assessment
5. Evidence completeness and review priorities
6. Evidence provenance and alternatives
7. Proposed review actions
8. Limitations quality review and human disposition

## Domain table: CustomerFactors

Exact ordered columns: factor_id, customer_id, dimension, weight, factor_value, contribution, evidence_ids, notes.

factor_id is unique text; customer_id links to ReviewOutcomes. Each customer has exactly one row for each of business, product, geography, channel, and ownership in the exercise. weight is a fraction displayed with 0.0%; all five sum to 1.0. factor_value is an integer from zero to three or null. contribution is numeric index points, not a percentage: factor_value × weight / 3 × 100, or null when the factor is missing. Preserve numeric zero as a real lowest-category assignment. notes explains missingness, source status, or rubric interpretation.

A changed authorized framework can use different factors only as a separately declared case method; the table's ordered columns remain fixed. Preserve the framework, each definition, and mapping in the complete checkpoint. Never reuse the fixture's band cutoffs for an incompatible scale without an explicit illustrative scenario label.

## Domain table: ReviewOutcomes

Exact ordered columns: customer_id, illustrative_score, illustrative_band, complete_items, required_items, completeness, material_gap, review_priority, evidence_ids, rationale.

customer_id is unique text. illustrative_score is a numeric index value or null, not a probability. illustrative_band is LOW, MODERATE, HIGH, or INCOMPLETE under the fixture rules. complete_items and required_items are nonnegative integers with complete_items no greater than required_items. completeness is complete_items/required_items; use null if required_items is zero, with explanation. Display the fraction using 0.0%. material_gap is substantive text or NONE within the supplied scope; it is never a clearance declaration.

review_priority is a proposed work label, separate from illustrative_band. rationale states why the priority follows from the evidence, including any conflict with a simple score ordering. Preserve pending human disposition in the common Actions/QA records according to 07, rather than adding an unauthorized approval column. Domain rows cannot omit C04 merely because its score is null.

## Cross-artifact invariants

The example contains thirty CustomerFactors rows and six ReviewOutcomes rows. Five scores are complete. Two LOW, two MODERATE, and one HIGH total five; one INCOMPLETE completes the population of six. Show that denominator whenever reporting band shares. A score histogram must not convert C04 to zero. Evidence completeness is twenty of twenty-four, while control exception rate is two of eight; these metrics cannot share an unlabeled “coverage” card.

The report includes C04's bounded calculation, C05's low-score material gap, the complete C06 sample, and any proposed override as narrative with evidence IDs. Do not invent a third domain table. Preserve raw source rows and sample results in the case checkpoint and report method notes so the two fixed domain tables remain an output contract rather than a limit on evidence retention.
