# Output contract — Jurisdiction Risk and Exposure Review

## Package and interchange rules

The final package contains a report, workbook, and optional dashboard, plus a visible limitations and QA statement. Use the report headings listed below in exactly that order. Do not rename the workbook tabs or rearrange the domain columns. The common tabs are Summary, Dashboard, Findings, Evidence, Actions, and QA; their exact schemas and styles are in 07-workbook-template.md. Append the two domain tables described here after those common tabs. Templates 06 through 08 control presentation; this file controls analytical semantics.

Identifiers, codes, and source locators are text even when they look numeric. Counts are nonnegative integers; rates are numeric fractions from zero to one and display as percentages to one decimal. Retain the numerator and denominator that produce each rate. Amounts must include an explicit currency and must not be summed across currencies without a named conversion method. Use ISO dates in machine tables and human-readable dates in narrative. A date with an unknown timezone cannot establish an intraday ordering.

Represent an unknown numeric or date value as a blank cell with an explicit explanation in the associated notes, limitation, or QA row. In text interchange use null. Never use zero, a dash, or N/A as a numeric stand-in. Distinguish Unknown, Not supplied, Not applicable, Not tested, and Unreadable in explanatory text. A true zero is a measured result. A zero denominator yields null, not a zero rate. Do not silently exclude failed or unassessed records from the denominator.

Keep evidence IDs as stable strings, separated by semicolons when a table cell needs multiple IDs. Findings must identify the affected population, factual observation, criterion, consequence or uncertainty, recommendation, alternative, and reviewer decision needed. Preserve severity, confidence, and claim class as distinct fields. Actions have a role owner, dependency, expected evidence of completion, and an unapproved proposed due date where relevant. Do not fabricate a person's acceptance or a completed review.

Avoid formulas that depend on locale-specific text interpretation. When calculation tools are available, store numeric values as numbers, preserve formulas where the format supports them, and check cached results or recalculate after reopening. When using text tables, give formulas in a method note and supply reconciled computed values. The same totals must appear in the report, workbook, and dashboard. Format discrepancies are QA failures when they alter meaning.

The dashboard is a view of the same evidence and decisions. Filters must show the denominator used; a filtered count cannot silently replace the full population count. Color accompanies text, never replaces it. Keep the supplied restrained light and dark themes, accessible contrast, visible selected filters, and an explicit fictional-data banner for the example. No external network resources, live source fetches, auto-sends, or operational changes belong in the dashboard.


## Required report heading order

1. Jurisdiction exposure conclusion
2. Scope dates and allocation method
3. Material geographic findings
4. Jurisdiction context assessment
5. Exposure allocation and overlap
6. Source applicability and uncertainty
7. Proposed specialist and evidence actions
8. Limitations quality review and human disposition

## Domain table: JurisdictionFactors

Exact ordered columns: jurisdiction_id, aml_category, sanctions_scope, corruption_context, source_date, as_of_date, evidence_ids, limitation.

jurisdiction_id is stable text. In the example J-A through J-D are fictional codes. aml_category records the exact contextual category and fixture status; it is not a sanctions field. sanctions_scope records a scoped question or assessment state, never a blanket inference from AML category. corruption_context is qualitative contextual evidence with provenance and limitations. There is no numeric country score in this contract.

source_date and as_of_date are ISO dates in tables. They are distinct: source_date identifies the supplied snapshot date; as_of_date identifies the review cutoff. Their presence does not prove the snapshot is operative at cutoff. evidence_ids identifies source support and limitation states the relevance boundary. The example has four rows. UNKNOWN destination is a mapping gap, not an invented fifth jurisdiction with assumed country factors.

## Domain table: ExposureMapping

Exact ordered columns: exposure_id, subject_id, destination_id, intermediary_id, amount, currency, exposure_role, include_in_total, evidence_ids, notes.

exposure_id identifies a unique economic transfer in the fixture. subject_id identifies the fictional customer without asserting that a transfer count is a customer count. destination_id may be null with a reason. intermediary_id is a separately supplied route role. amount is numeric original-currency value; currency is required text. exposure_role specifies the primary allocation role. include_in_total is Boolean and exclusions require reasons. The eight fixture rows all have true.

The primary role is BENEFICIARY_JURISDICTION. Do not create a duplicate row and include its full amount again merely to represent the intermediary. More complicated multileg source evidence belongs in the complete saved ledger with deduplication rules, while this table retains one resolved economic-event row for the selected population. Null destination remains included in the total.

## Report and display requirements

Show the total value, mapped value, unknown value, unique transfer count, role-specific allocation, and any union method. Keep original currency visible next to monetary amounts. For the single-currency fixture USD amounts may display with dollar signs. A mixed-currency artifact needs separate panels or a clearly documented conversion; a generic “amount” sum is not sufficient.

The report must include the five destination buckets including UNKNOWN, J-D's 25.0% destination share, its 40.0% any-nexus share, the 25.0%–35.0% unknown-allocation scenario, and the unresolved scope question. Narrative percentage values are fractions expressed to one decimal; no numeric percentage column is required by these domain tables. The common schemas remain those in 07. Do not add a third domain table to accommodate a convenient chart.
