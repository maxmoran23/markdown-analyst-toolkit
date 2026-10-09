# Output contract — Third-Party Service and Assurance Review

## Package and interchange rules

The final package contains a report, workbook, and optional dashboard, plus a visible limitations and QA statement. Use the report headings listed below in exactly that order. Do not rename the workbook tabs or rearrange the domain columns. The common tabs are Summary, Dashboard, Findings, Evidence, Actions, and QA; their exact schemas and styles are in 07-workbook-template.md. Append the two domain tables described here after those common tabs. Templates 06 through 08 control presentation; this file controls analytical semantics.

Identifiers, codes, and source locators are text even when they look numeric. Counts are nonnegative integers; rates are numeric fractions from zero to one and display as percentages to one decimal. Retain the numerator and denominator that produce each rate. Amounts must include an explicit currency and must not be summed across currencies without a named conversion method. Use ISO dates in machine tables and human-readable dates in narrative. A date with an unknown timezone cannot establish an intraday ordering.

Represent an unknown numeric or date value as a blank cell with an explicit explanation in the associated notes, limitation, or QA row. In text interchange use null. Never use zero, a dash, or N/A as a numeric stand-in. Distinguish Unknown, Not supplied, Not applicable, Not tested, and Unreadable in explanatory text. A true zero is a measured result. A zero denominator yields null, not a zero rate. Do not silently exclude failed or unassessed records from the denominator.

Keep evidence IDs as stable strings, separated by semicolons when a table cell needs multiple IDs. Findings must identify the affected population, factual observation, criterion, consequence or uncertainty, recommendation, alternative, and reviewer decision needed. Preserve severity, confidence, and claim class as distinct fields. Actions have a role owner, dependency, expected evidence of completion, and an unapproved proposed due date where relevant. Do not fabricate a person's acceptance or a completed review.

Avoid formulas that depend on locale-specific text interpretation. When calculation tools are available, store numeric values as numbers, preserve formulas where the format supports them, and check cached results or recalculate after reopening. When using text tables, give formulas in a method note and supply reconciled computed values. The same totals must appear in the report, workbook, and dashboard. Format discrepancies are QA failures when they alter meaning.

The dashboard is a view of the same evidence and decisions. Filters must show the denominator used; a filtered count cannot silently replace the full population count. Color accompanies text, never replaces it. Keep the supplied restrained light and dark themes, accessible contrast, visible selected filters, and an explicit fictional-data banner for the example. No external network resources, live source fetches, auto-sends, or operational changes belong in the dashboard.


## Required report heading order

1. Service reliance recommendation and restrictions
2. Relationship scope and assessment method
3. Material assurance findings
4. Service and fourth-party dependencies
5. Assurance evidence and test outcomes
6. Source provenance and coverage limitations
7. Remediation exit and review proposals
8. Limitations quality review and human disposition

## Domain table: ServiceDependencies

Exact ordered columns: service_id, provider_role, service_function, data_access, dependency_id, substitutability, evidence_ids.

All fields are text; service_id is required and unique. provider_role and service_function are required. data_access must distinguish known access from reported or unknown access in its explanatory evidence. dependency_id is null for no dependency identified within the mapped scope, not proof that none exists; otherwise use semicolon-separated IDs that resolve in this table. substitutability is a descriptive supported statement, not a numeric risk score. evidence_ids is required.

Check dependency references for missing IDs and cycles. A cycle may represent a real reciprocal dependency or an incorrect map; investigate rather than deleting it automatically. A provider can appear in several service rows because the unit is a service. Do not collapse those rows into one supplier score if doing so hides access or criticality differences.

## Domain table: AssuranceReview

Exact ordered columns: review_id, domain, criterion, critical, result, evidence_ids.

review_id is unique required text. domain and criterion are required text. critical is Boolean. result is SUPPORTED, PARTIAL, FAILED, UNVERIFIED, or NOT APPLICABLE. evidence_ids resolves to the supplied records, including evidence of test failure or scope exclusions. Evidence detail records period, service version, assessor, limitations, and exact locator. Absence of a report should have an explicit missing-evidence entry rather than an empty citation.

The report identifies each assurance gap's affected service, consequence, evidence source, required follow-up, and human decision. Common Actions holds proposed owners and milestones. If a renewal has prior evidence, compare periods and scope changes without replacing the current evidence requirement with the prior approval.

Metrics distinguish supported criteria, failed criteria, unverified criteria, and partial coverage. The dashboard leads with material unresolved dependencies and the recommendation. An export return rate of 98.5% must be accompanied by the fifteen-record gap and must not be colored as a complete exit. A certification badge or aggregate score cannot override the detailed conditions.
