# Output contract — New Product Risk and Launch Readiness

## Package and interchange rules

The final package contains a report, workbook, and optional dashboard, plus a visible limitations and QA statement. Use the report headings listed below in exactly that order. Do not rename the workbook tabs or rearrange the domain columns. The common tabs are Summary, Dashboard, Findings, Evidence, Actions, and QA; their exact schemas and styles are in 07-workbook-template.md. Append the two domain tables described here after those common tabs. Templates 06 through 08 control presentation; this file controls analytical semantics.

Identifiers, codes, and source locators are text even when they look numeric. Counts are nonnegative integers; rates are numeric fractions from zero to one and display as percentages to one decimal. Retain the numerator and denominator that produce each rate. Amounts must include an explicit currency and must not be summed across currencies without a named conversion method. Use ISO dates in machine tables and human-readable dates in narrative. A date with an unknown timezone cannot establish an intraday ordering.

Represent an unknown numeric or date value as a blank cell with an explicit explanation in the associated notes, limitation, or QA row. In text interchange use null. Never use zero, a dash, or N/A as a numeric stand-in. Distinguish Unknown, Not supplied, Not applicable, Not tested, and Unreadable in explanatory text. A true zero is a measured result. A zero denominator yields null, not a zero rate. Do not silently exclude failed or unassessed records from the denominator.

Keep evidence IDs as stable strings, separated by semicolons when a table cell needs multiple IDs. Findings must identify the affected population, factual observation, criterion, consequence or uncertainty, recommendation, alternative, and reviewer decision needed. Preserve severity, confidence, and claim class as distinct fields. Actions have a role owner, dependency, expected evidence of completion, and an unapproved proposed due date where relevant. Do not fabricate a person's acceptance or a completed review.

Avoid formulas that depend on locale-specific text interpretation. When calculation tools are available, store numeric values as numbers, preserve formulas where the format supports them, and check cached results or recalculate after reopening. When using text tables, give formulas in a method note and supply reconciled computed values. The same totals must appear in the report, workbook, and dashboard. Format discrepancies are QA failures when they alter meaning.

The dashboard is a view of the same evidence and decisions. Filters must show the denominator used; a filtered count cannot silently replace the full population count. Color accompanies text, never replaces it. Keep the supplied restrained light and dark themes, accessible contrast, visible selected filters, and an explicit fictional-data banner for the example. No external network resources, live source fetches, auto-sends, or operational changes belong in the dashboard.


## Required report heading order

1. Launch recommendation and unresolved conditions
2. Product scope flow and assessment method
3. Material readiness findings
4. Funds data and service flow map
5. Launch condition verification
6. Evidence and dependency limitations
7. Remediation pilot and exit proposals
8. Limitations quality review and human disposition

## Domain table: FlowMap

Exact ordered columns: flow_id, flow_type, from_role, to_role, asset_or_data, control_dependency, evidence_ids.

All columns are text. flow_id is unique and required. flow_type is FUNDS, DATA, or SERVICE. from_role and to_role are required generic functions or provider roles. asset_or_data explicitly identifies value, data, or instruction; include currency where needed. control_dependency names the relevant safeguard, with detail in Evidence or the report. evidence_ids is required and resolves to the source material. Unknown responsibility is written as Unresolved with a finding, not silently assigned.

One row describes one boundary leg. Multiple rows can involve the same value, so row count is not transaction volume and amounts cannot be summed across legs. Reversals and exception paths must be described even if the five-row fixture shows only the principal path. For a real review add rows using the exact same columns rather than changing the schema.

## Domain table: LaunchConditions

Exact ordered columns: condition_id, flow_id, condition, critical, status, evidence_ids.

condition_id is unique text. flow_id must resolve in FlowMap; a cross-flow condition may cite a primary leg with the other dependencies in the report. condition is the exact or transparently decomposed criterion. critical is Boolean. status is SATISFIED, PARTIAL, NOT SATISFIED, NOT VERIFIABLE, or NOT APPLICABLE. evidence_ids is text and may point to evidence of absence, assertion, or failure as appropriate. No row disappears because it lacks completion evidence.

The report provides criterion timing, evidence date, gap, severity, owner, clearance evidence, and human decision needed for each unresolved condition. Common Actions holds the proposed follow-up. If a condition is not applicable, document the approved scope change and exclude it from an applicable-only metric only with an explicit denominator reconciliation.

Show completion counts and unresolved critical conditions together. The dashboard's leading status is the recommendation, not a weighted completion score. Preserve source version and proposed launch scope so a later expansion cannot inherit the same readiness conclusion without reassessment.
