# Output contract — Regulatory Change and Obligation Mapping

## Package and interchange rules

The final package contains a report, workbook, and optional dashboard, plus a visible limitations and QA statement. Use the report headings listed below in exactly that order. Do not rename the workbook tabs or rearrange the domain columns. The common tabs are Summary, Dashboard, Findings, Evidence, Actions, and QA; their exact schemas and styles are in 07-workbook-template.md. Append the two domain tables described here after those common tabs. Templates 06 through 08 control presentation; this file controls analytical semantics.

Identifiers, codes, and source locators are text even when they look numeric. Counts are nonnegative integers; rates are numeric fractions from zero to one and display as percentages to one decimal. Retain the numerator and denominator that produce each rate. Amounts must include an explicit currency and must not be summed across currencies without a named conversion method. Use ISO dates in machine tables and human-readable dates in narrative. A date with an unknown timezone cannot establish an intraday ordering.

Represent an unknown numeric or date value as a blank cell with an explicit explanation in the associated notes, limitation, or QA row. In text interchange use null. Never use zero, a dash, or N/A as a numeric stand-in. Distinguish Unknown, Not supplied, Not applicable, Not tested, and Unreadable in explanatory text. A true zero is a measured result. A zero denominator yields null, not a zero rate. Do not silently exclude failed or unassessed records from the denominator.

Keep evidence IDs as stable strings, separated by semicolons when a table cell needs multiple IDs. Findings must identify the affected population, factual observation, criterion, consequence or uncertainty, recommendation, alternative, and reviewer decision needed. Preserve severity, confidence, and claim class as distinct fields. Actions have a role owner, dependency, expected evidence of completion, and an unapproved proposed due date where relevant. Do not fabricate a person's acceptance or a completed review.

Avoid formulas that depend on locale-specific text interpretation. When calculation tools are available, store numeric values as numbers, preserve formulas where the format supports them, and check cached results or recalculate after reopening. When using text tables, give formulas in a method note and supply reconciled computed values. The same totals must appear in the report, workbook, and dashboard. Format discrepancies are QA failures when they alter meaning.

The dashboard is a view of the same evidence and decisions. Filters must show the denominator used; a filtered count cannot silently replace the full population count. Color accompanies text, never replaces it. Keep the supplied restrained light and dark themes, accessible contrast, visible selected filters, and an explicit fictional-data banner for the example. No external network resources, live source fetches, auto-sends, or operational changes belong in the dashboard.


## Required report heading order

1. Change priorities and restricted conclusion
2. Scope status and applicability method
3. Material readiness findings
4. Instrument register and date status
5. Obligation mapping and readiness
6. Source evidence and unresolved authority
7. Implementation and verification proposals
8. Limitations quality review and human disposition

## Domain table: ChangeRegister

Exact ordered columns: change_id, instrument_status, applicability, effective_date, compliance_date, owner_role, priority, evidence_ids.

change_id is a unique text key. instrument_status is the declared state from 04. applicability is required text with a rationale in the report. effective_date and compliance_date are dates or null; do not place comment or internal planning dates here. owner_role is a generic accountable role, null when unassigned with an action to resolve. priority is HIGH, MEDIUM, or LOW. evidence_ids resolves to sources actually reviewed.

A date is confirmed only by the appropriate source. A claimed date from secondary coverage belongs in the evidence narrative, not the confirmed date column. Where an instrument has multiple relevant dates, the register may use null with a clear Multiple provision dates explanation and exact dates in ObligationMap. Source publication dates and retrieval dates remain in Evidence, separate from effective dates.

## Domain table: ObligationMap

Exact ordered columns: obligation_id, change_id, requirement_summary, control_id, readiness, compliance_date, evidence_ids.

obligation_id is unique required text. change_id must exist in ChangeRegister. requirement_summary is an atomic paraphrase with its provision locator in Evidence. control_id is text, null for an unmapped gap. readiness is text from the declared review framework; the worked example uses BUILD, EVIDENCE GAP, VERIFIED FOR FIXTURE, SCENARIO ONLY, and REFERENCE ONLY. compliance_date is a date or null and must agree with the applicable provision. evidence_ids are required.

The map may include scenario and reference rows, but they cannot enter current-obligation coverage denominators. For the fixture, effective mapped requirements are OB02 and OB03 only. OB01 is future final work; OB04 is proposal planning; OB05 is reference context. Label readiness metrics with this exact population.

The report must include source status, applicability rationale, material date provenance, changed versus unchanged provisions, owner dependencies, missing evidence, and a human disposition. The dashboard separates instrument status from implementation readiness and includes an as-of date. It must not count withdrawn items as current obligations or display unresolved legal dates as confirmed countdowns.
