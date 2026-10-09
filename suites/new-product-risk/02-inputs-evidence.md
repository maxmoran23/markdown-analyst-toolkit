# Inputs and evidence — New Product Risk and Launch Readiness

## Product input bundle

| Input | Minimum content | Why required |
| --- | --- | --- |
| Product description | Users, purpose, included and excluded activities, lifecycle | Establishes scope and misuse pathways |
| Flow description | Funds, instructions, data, decisions, custody or control, reversals | Exposes responsibility and failure boundaries |
| Scale assumptions | Transaction counts, value, limits, concurrency, jurisdictions | Shows capacity and exposure assumptions |
| Dependencies | Internal systems, providers, fourth parties, staff, reference data | Identifies single points of failure |
| Control design | Objective, trigger, owner, inputs, outputs, evidence | Supports design assessment |
| Approved conditions | Exact wording, condition ID, approving role, timing, criticality | Defines readiness criteria |
| Test evidence | Cases, expected results, actual results, version, date, defects | Supports operation in a bounded environment |
| Exit plan | Pending obligations, access, data, recovery, customer handling | Assesses controlled failure and shutdown |

A product presentation can explain intent but rarely establishes complete flow coverage. Ask for a plain-language walkthrough of one normal transaction and one failure/reversal, using generic or fictional records. Capture where balances, instructions, and decisions reside. A provider sending an instruction is not necessarily the entity holding funds or settling the transfer.

## Required field dictionary

flow_id identifies one directional leg at one boundary. flow_type is FUNDS, DATA, or SERVICE. from_role and to_role identify responsible functions or generic service roles. asset_or_data states the transferred item, unit or currency if relevant, and whether it is a record, instruction, claim, or value. control_dependency identifies what must work before or after that leg. evidence_ids links the supporting design or test material.

condition_id identifies an approved or proposed condition without renumbering it after outcomes are known. flow_id connects the condition to the relevant flow. condition is a falsifiable statement. critical is the explicit approved or analyst-proposed gate classification, not an inferred regulatory label. status distinguishes SATISFIED, PARTIAL, NOT SATISFIED, NOT VERIFIABLE, and NOT APPLICABLE with a reason. The example uses the first four only.

## Evidence granularity

For a screening condition, determine population, configuration version, reference-list scope, matching behavior, escalation path, and test evidence. For a monitoring condition, determine inputs, scenario coverage, missing-data behavior, queue routing, and tested exceptions. A screenshot showing a switch is on establishes configuration visibility, not end-to-end detection performance.

For reconciliation, capture both totals and item status. A ledger can conserve total value while leaving an item unresolved past its criterion. For training, capture the in-scope role population, completion count, date, and relevant content; a course being available is not proof of completion. For exit, capture a rehearsal or other accepted evidence rather than equating a written plan with recoverability.

## Change and scope ledger

Record each difference from the existing activity: new customer type, geography, payment rail, data element, provider, transaction limit, channel, settlement timing, or operating hours. A familiar interface can conceal a different risk profile underneath. Identify which prior control evidence remains relevant and which must be refreshed. Do not reuse a test from an earlier version without checking configuration and population equivalence.

Keep commercial forecasts and provider assurances as Reported unless independently supported. Unknown legal permissions, data rights, or settlement responsibilities remain explicit questions for appropriate reviewers. Do not infer authority to perform an activity from the existence of a technical integration.

## Evidence register and claim discipline

Every material input receives an evidence ID. Use SYN-001 for the fictional worked-example package only; use SRC-001 onward for supplied operational evidence and REF-001 onward for public method references. A public reference supports a methodological statement, not a finding about the supplied population. Keep those two roles separate even when both appear in the same finding.

For each item capture title, origin, source locator, version, publication or creation date if known, retrieval date, period covered, relevant passage or row IDs, accessibility, transformations, and limitations. A locator must let another reviewer find the same passage, cell range, or records. Preserve an original value beside any normalized value. Document rounding, timezone conversion, deduplication, filtering, and joins. Do not alter source records to make them fit a desired conclusion.

Use Observed for facts directly visible in the materials reviewed; Reported for an assertion by a source that has not been independently corroborated; Inferred for an analytical conclusion derived from facts; Estimated for a result that depends on assumptions or an estimating method. Arithmetic directly reconciled to observed inputs can be Observed, with the formula stated. A severity assessment remains a judgment even when its input defect is observed.

Confidence is HIGH, MODERATE, LOW, or NOT ASSESSABLE. Assess the support for each claim rather than borrowing the reputation of the publisher. HIGH requires direct, complete, internally consistent evidence for that narrow claim; MODERATE indicates a defined limitation; LOW indicates material ambiguity; NOT ASSESSABLE means the inputs cannot support a conclusion. Confidence is not the same as severity, evidence class, legal applicability, or action priority.

Links below were reviewed during preparation on 2026-10-09. They are reference starting points. A later session must retrieve the current version or record that it could not verify it. The suite's sample thresholds and workflow gates are author-defined illustrations unless a specific, applicable authority is identified.


## Public method references

| ID | Primary source | Version / reviewed date | Applicability and narrow use |
| --- | --- | --- | --- |
| REF-001 | [OCC 2017-43, New, Modified, or Expanded Bank Products and Services](https://www.occ.gov/news-issuances/bulletins/2017/bulletin-2017-43.html) | October 20, 2017; page notes March 2025 edits; reviewed 2026-10-09 | OCC-supervised banking context; supports lifecycle risk review, testing, and exit planning. Use the current page, including its removal of reputation-risk references. |
| REF-002 | [Federal Reserve SR 23-4, Third-Party Relationships](https://www.federalreserve.gov/supervisionreg/srletters/sr2304.htm) | June 07, 2023; reviewed 2026-10-09 | U.S. banking third-party risk reference; relevant to product dependencies, with institution-specific applicability assessed separately. |

The OCC product bulletin contains older third-party cross-references. Do not assume those historical links are the current general third-party framework. A September 2026 proposal to revise third-party guidance must be distinguished from a finalized replacement; verify source status at the time of use. The product flow taxonomy, condition statuses, thresholds, and example launch criteria here are author-defined methods, not regulator-mandated templates.
