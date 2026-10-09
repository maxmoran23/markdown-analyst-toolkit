# Output contract — Control Testing and Evidence Review

## Package and interchange rules

The final package contains a report, workbook, and optional dashboard, plus a visible limitations and QA statement. Use the report headings listed below in exactly that order. Do not rename the workbook tabs or rearrange the domain columns. The common tabs are Summary, Dashboard, Findings, Evidence, Actions, and QA; their exact schemas and styles are in 07-workbook-template.md. Append the two domain tables described here after those common tabs. Templates 06 through 08 control presentation; this file controls analytical semantics.

Identifiers, codes, and source locators are text even when they look numeric. Counts are nonnegative integers; rates are numeric fractions from zero to one and display as percentages to one decimal. Retain the numerator and denominator that produce each rate. Amounts must include an explicit currency and must not be summed across currencies without a named conversion method. Use ISO dates in machine tables and human-readable dates in narrative. A date with an unknown timezone cannot establish an intraday ordering.

Represent an unknown numeric or date value as a blank cell with an explicit explanation in the associated notes, limitation, or QA row. In text interchange use null. Never use zero, a dash, or N/A as a numeric stand-in. Distinguish Unknown, Not supplied, Not applicable, Not tested, and Unreadable in explanatory text. A true zero is a measured result. A zero denominator yields null, not a zero rate. Do not silently exclude failed or unassessed records from the denominator.

Keep evidence IDs as stable strings, separated by semicolons when a table cell needs multiple IDs. Findings must identify the affected population, factual observation, criterion, consequence or uncertainty, recommendation, alternative, and reviewer decision needed. Preserve severity, confidence, and claim class as distinct fields. Actions have a role owner, dependency, expected evidence of completion, and an unapproved proposed due date where relevant. Do not fabricate a person's acceptance or a completed review.

Avoid formulas that depend on locale-specific text interpretation. When calculation tools are available, store numeric values as numbers, preserve formulas where the format supports them, and check cached results or recalculate after reopening. When using text tables, give formulas in a method note and supply reconciled computed values. The same totals must appear in the report, workbook, and dashboard. Format discrepancies are QA failures when they alter meaning.

The dashboard is a view of the same evidence and decisions. Filters must show the denominator used; a filtered count cannot silently replace the full population count. Color accompanies text, never replaces it. Keep the supplied restrained light and dark themes, accessible contrast, visible selected filters, and an explicit fictional-data banner for the example. No external network resources, live source fetches, auto-sends, or operational changes belong in the dashboard.


## Required report heading order

1. Review conclusion and restrictions
2. Scope and testing method
3. Findings and deviations
4. Control design and coverage
5. Selected instance results
6. Evidence and alternative explanations
7. Remediation and retest plan
8. Limitations quality review and human disposition

The first section states whether the conclusion is bounded to selected records, a reconciled census, or a formally justified statistical inference. The selection section describes both organizational independence and sampling independence separately. The remediation section specifies fresh evidence required for retest; it does not assert closure.

## Domain table: ControlSummary

Exact ordered columns: control_id, population_count, selected_count, pass_count, fail_count, unassessed_count, design_result, conclusion.

| Column | Type / unit | Null and interpretation rule |
| --- | --- | --- |
| control_id | Text key | Required; unique here |
| population_count | Integer, execution opportunities | Null if frame completeness unknown; explain |
| selected_count | Integer, selected applicable instances | Required; zero is allowed |
| pass_count | Integer, PASS outcomes | Required; cannot include missing evidence |
| fail_count | Integer, FAIL outcomes | Required; count instances once |
| unassessed_count | Integer, UNABLE TO CONCLUDE outcomes | Required; preserved in totals |
| design_result | Text enum | Adequate for stated objective; Inadequate; Unable to assess |
| conclusion | Text | Bounded draft conclusion; required |

For each row selected_count = pass_count + fail_count + unassessed_count. Population count must be at least selected count unless a documented unit mismatch is a QA failure requiring correction. No weighted average across controls produces an effectiveness attestation.

## Domain table: TestResults

Exact ordered columns: test_id, control_id, population_id, selection_basis, result, evidence_ids.

All fields are text and required. test_id is unique. control_id must exist in ControlSummary. population_id points to one execution opportunity. selection_basis records Census, Probability with method locator, or Judgmental with reason. result is PASS, FAIL, or UNABLE TO CONCLUDE. Any excluded not-applicable selection belongs in the scope ledger and QA explanation; retain its identity rather than inserting it into the outcome denominator. evidence_ids must resolve in Evidence, even if the evidence item documents an absence or limitation.

Store attribute-level observations, timing calculations, and original record locators in the report appendix or Evidence detail, keyed by test_id. Do not overload result with a sentence that breaks filtering. A single instance with multiple failures is one TestResults row and may support multiple separately described findings. The dashboard must show selected, failed, and unassessed counts together; a green pass rate alone is unacceptable.
