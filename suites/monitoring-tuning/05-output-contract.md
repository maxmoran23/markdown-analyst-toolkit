# Output contract — Monitoring Scenario and Threshold Review

## Package and interchange rules

The final package contains a report, workbook, and optional dashboard, plus a visible limitations and QA statement. Use the report headings listed below in exactly that order. Do not rename the workbook tabs or rearrange the domain columns. The common tabs are Summary, Dashboard, Findings, Evidence, Actions, and QA; their exact schemas and styles are in 07-workbook-template.md. Append the two domain tables described here after those common tabs. Templates 06 through 08 control presentation; this file controls analytical semantics.

Identifiers, codes, and source locators are text even when they look numeric. Counts are nonnegative integers; rates are numeric fractions from zero to one and display as percentages to one decimal. Retain the numerator and denominator that produce each rate. Amounts must include an explicit currency and must not be summed across currencies without a named conversion method. Use ISO dates in machine tables and human-readable dates in narrative. A date with an unknown timezone cannot establish an intraday ordering.

Represent an unknown numeric or date value as a blank cell with an explicit explanation in the associated notes, limitation, or QA row. In text interchange use null. Never use zero, a dash, or N/A as a numeric stand-in. Distinguish Unknown, Not supplied, Not applicable, Not tested, and Unreadable in explanatory text. A true zero is a measured result. A zero denominator yields null, not a zero rate. Do not silently exclude failed or unassessed records from the denominator.

Keep evidence IDs as stable strings, separated by semicolons when a table cell needs multiple IDs. Findings must identify the affected population, factual observation, criterion, consequence or uncertainty, recommendation, alternative, and reviewer decision needed. Preserve severity, confidence, and claim class as distinct fields. Actions have a role owner, dependency, expected evidence of completion, and an unapproved proposed due date where relevant. Do not fabricate a person's acceptance or a completed review.

Avoid formulas that depend on locale-specific text interpretation. When calculation tools are available, store numeric values as numbers, preserve formulas where the format supports them, and check cached results or recalculate after reopening. When using text tables, give formulas in a method note and supply reconciled computed values. The same totals must appear in the report, workbook, and dashboard. Format discrepancies are QA failures when they alter meaning.

The dashboard is a view of the same evidence and decisions. Filters must show the denominator used; a filtered count cannot silently replace the full population count. Color accompanies text, never replaces it. Keep the supplied restrained light and dark themes, accessible contrast, visible selected filters, and an explicit fictional-data banner for the example. No external network resources, live source fetches, auto-sends, or operational changes belong in the dashboard.


## Required report heading order

1. Candidate recommendation and restrictions
2. Evaluation scope and comparison method
3. Coverage and workload findings
4. Candidate performance comparison
5. Labelled units and review provenance
6. Evidence uncertainty and blind spots
7. Validation and change proposals
8. Limitations quality review and human disposition

## Domain table: CandidateMetrics

Exact ordered columns: candidate_id, threshold, labelled_alerts, tp, fp, fn, tn, precision, recall, population_alerts.

candidate_id is unique text. threshold is a numeric score cutoff on the declared scale. labelled_alerts,tp,fp,fn,tn,population_alerts are nonnegative integer counts. precision and recall are fractions with null for a zero denominator. labelled_alerts=tp+fp; tp+fp+fn+tn equals the common labelled subset size. population_alerts counts the complete scored eligible population, including unknown labels; it can exceed labelled_alerts. The report states both population and labelled denominators because they are not additional columns in this fixed table.

Preserve candidate comparators and eligibility in the method note. A threshold comparison alone cannot represent a candidate with a different score definition without explaining that change. Do not store percentage strings in numeric rate cells. Workload hours, false-positive rates, and sensitivity bounds can appear in the report and Summary with formulas and denominators stated.

## Domain table: LabelledUnits

Exact ordered columns: unit_id, group_id, score, label, label_source, evidence_ids.

unit_id is unique required text. group_id is required text where dependence can be assessed; null means dependency grouping unavailable and is a limitation. score is numeric; a missing score excludes the unit from the calculable confusion matrix and must be reconciled separately. label is POSITIVE or NEGATIVE in this table; UNKNOWN units remain in the complete input ledger and workload calculation, not in this labelled table. label_source and evidence_ids are required text supporting the rubric and provenance.

For the worked example LabelledUnits has six rows while the complete input ledger has eight. This deliberate difference must be visible in every artifact. The dashboard must label recall “labelled-sample recall” and distinguish total alerts. It cannot show a 100% LOW50 bar without the three-positive denominator and unknown-label limitation.

The report includes incremental IDs between candidates, the capacity assumption, a coverage-versus-workload comparison, and the evidence needed before change approval. An action labelled “deploy” must remain a proposed human decision with prerequisites; default action is further review, not execution.
