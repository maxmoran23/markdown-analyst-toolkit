# Output contract — Data Quality and Fitness for Use

## Package and interchange rules

The final package contains a report, workbook, and optional dashboard, plus a visible limitations and QA statement. Use the report headings listed below in exactly that order. Do not rename the workbook tabs or rearrange the domain columns. The common tabs are Summary, Dashboard, Findings, Evidence, Actions, and QA; their exact schemas and styles are in 07-workbook-template.md. Append the two domain tables described here after those common tabs. Templates 06 through 08 control presentation; this file controls analytical semantics.

Identifiers, codes, and source locators are text even when they look numeric. Counts are nonnegative integers; rates are numeric fractions from zero to one and display as percentages to one decimal. Retain the numerator and denominator that produce each rate. Amounts must include an explicit currency and must not be summed across currencies without a named conversion method. Use ISO dates in machine tables and human-readable dates in narrative. A date with an unknown timezone cannot establish an intraday ordering.

Represent an unknown numeric or date value as a blank cell with an explicit explanation in the associated notes, limitation, or QA row. In text interchange use null. Never use zero, a dash, or N/A as a numeric stand-in. Distinguish Unknown, Not supplied, Not applicable, Not tested, and Unreadable in explanatory text. A true zero is a measured result. A zero denominator yields null, not a zero rate. Do not silently exclude failed or unassessed records from the denominator.

Keep evidence IDs as stable strings, separated by semicolons when a table cell needs multiple IDs. Findings must identify the affected population, factual observation, criterion, consequence or uncertainty, recommendation, alternative, and reviewer decision needed. Preserve severity, confidence, and claim class as distinct fields. Actions have a role owner, dependency, expected evidence of completion, and an unapproved proposed due date where relevant. Do not fabricate a person's acceptance or a completed review.

Avoid formulas that depend on locale-specific text interpretation. When calculation tools are available, store numeric values as numbers, preserve formulas where the format supports them, and check cached results or recalculate after reopening. When using text tables, give formulas in a method note and supply reconciled computed values. The same totals must appear in the report, workbook, and dashboard. Format discrepancies are QA failures when they alter meaning.

The dashboard is a view of the same evidence and decisions. Filters must show the denominator used; a filtered count cannot silently replace the full population count. Color accompanies text, never replaces it. Keep the supplied restrained light and dark themes, accessible contrast, visible selected filters, and an explicit fictional-data banner for the example. No external network resources, live source fetches, auto-sends, or operational changes belong in the dashboard.


## Required report heading order

1. Fitness recommendation and restrictions
2. Scope data contract and method
3. Material defects and findings
4. Record population and lineage
5. Rule outcomes and hard gates
6. Evidence and source limitations
7. Remediation reconciliation and retest
8. Limitations quality review and human disposition

## Domain table: DataRecords

Exact ordered columns: record_id, customer_id, entity_type, full_name, date_of_birth, country_code, last_refresh.

All fields preserve supplied source text. record_id is required and unique. customer_id can repeat so the defect remains observable; never use it as the extract-row key. entity_type is expected INDIVIDUAL or ENTITY, but invalid supplied values remain visible. full_name may be null and is a defect when required. date_of_birth retains raw input text so impossible dates can be shown rather than silently converted; an entity blank is not applicable. country_code is raw text against a named reference set. last_refresh is source date text and can be null or invalid, with a corresponding rule result or limitation.

Do not coerce source dates into valid spreadsheet dates when that would hide invalid text. In a new dataset retain required source fields beyond these seven in a separate evidence attachment, rather than silently expanding or rearranging the controlled domain schema. The report identifies which additional fields supported checks.

## Domain table: RuleResults

Exact ordered columns: rule_id, dimension, eligible_count, defect_count, defect_rate, critical, gate_result.

rule_id and dimension are required text. eligible_count and defect_count are nonnegative integers; defect_count cannot exceed eligible_count. defect_rate is a numeric fraction equal to defect_count/eligible_count, null for zero eligibility. critical is a Boolean, not the text “yes.” gate_result is PASS, RESTRICT, REVIEW, NOT APPLICABLE, or UNABLE TO ASSESS. In the example there are no unassessable eligible checks. For a new input that contains them, document their count per rule in Evidence and QA and do not let gate_result be PASS.

The rule count table is not the record defect ledger. The report or Evidence detail must identify all failing record IDs per rule, the raw value, expected condition, and parameter version. This supports reproducing both rule totals and the distinct union of affected records. Critical-affected rate, duplicate-group count, excess-row count, and check-pass rate are different metrics and require distinct labels.

The dashboard shows critical gates before diagnostic averages. A high average never removes the restricted status. Present total input rows, distinct business keys, critical-affected rows, unassessed rules, and supporting issues together. If the user filters to one source, preserve a visible full-population total and clearly label the filtered denominator.
