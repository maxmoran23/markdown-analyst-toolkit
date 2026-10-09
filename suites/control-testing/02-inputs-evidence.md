# Inputs and evidence — Control Testing and Evidence Review

## Required input bundle

| Input | Minimum contents | Why it matters | Missing-input treatment |
| --- | --- | --- | --- |
| Control inventory | ID, objective, risk, owner role, performer role, frequency, trigger | Connects the procedure to a specific purpose | Design conclusion restricted |
| Criterion | Required steps, timing, evidence, exceptions, governing version | Defines a falsifiable result | No pass/fail until established |
| Population manifest | Grain, period, source, expected count, exclusions, IDs | Establishes the selection frame | No population coverage claim |
| Execution evidence | Time, performer, reviewer, relevant output, source locator | Supports operation | Unable to conclude unless alternate evidence is accepted |
| Prior findings | Issue, cause, promised action, status, closure evidence | Tests recurrence and remediation | State history unavailable |
| Reviewer context | Role separation, involvement, skills, reporting route | Supports independence assessment | Independence unassessed |

The population grain is a control execution opportunity, not necessarily a transaction. A daily reconciliation over ten thousand transactions is one control instance if the test objective concerns daily performance. A case-by-case approval is one instance per approval event. A test of transaction correctness uses transaction grain. State which question is being answered before calculating coverage.

## Minimum input dictionary

Use population_id as a stable text key. control_id joins to the inventory. period_start and period_end define the review window. trigger_at identifies when the execution became due; due_at records the actual criterion-derived deadline; performed_at and reviewed_at are distinct. performer_role and reviewer_role are role identifiers. evidence_locator points to the original artifact. risk_stratum records the selection characteristic before outcomes are inspected. scope_status is Included or Excluded; exclusion_reason is required for Excluded. evidence_status is Available, Partial, Missing, or Unreadable.

Unknown due dates do not become the period end. Unknown completion dates do not become the file modification timestamp. A document upload timestamp may show when evidence was uploaded, not when a review occurred. Preserve that distinction. A manager's statement that all cases were reviewed is Reported; a contemporaneous record can support an Observed statement about the documented event.

## Population reconciliation

Record the count at extraction, after scope exclusions, after duplicate analysis, selected, actually tested, conclusive, and unable to conclude. Keep an exclusion ledger with IDs and reasons. Exact duplicate extract rows may be removed from the selection frame only after confirming that they represent the same execution opportunity. Similar names or timestamps are not sufficient. Multiple records for one event can be separate pieces of evidence rather than duplicates.

A population file supplied by the process owner is not automatically complete. Compare its stated count and boundaries to an independently available total, schedule, source report, or period register. If none is available, say the frame was supplied and unverified. A monthly control with no execution row for a month may represent an omitted opportunity, which must remain visible rather than disappear from the denominator.

## Selection manifest

For each selected ID retain selection basis, stratum, selection date, selector role, initial outcome visibility, replacement if any, and rationale. Selection after reviewing outcomes is potentially biased. Never replace an unavailable record with a convenient passing record without retaining the unavailable item and explaining the change. Supplemental targeted samples must remain separate from the original sample when reporting rates.

## Evidence register and claim discipline

Every material input receives an evidence ID. Use SYN-001 for the fictional worked-example package only; use SRC-001 onward for supplied operational evidence and REF-001 onward for public method references. A public reference supports a methodological statement, not a finding about the supplied population. Keep those two roles separate even when both appear in the same finding.

For each item capture title, origin, source locator, version, publication or creation date if known, retrieval date, period covered, relevant passage or row IDs, accessibility, transformations, and limitations. A locator must let another reviewer find the same passage, cell range, or records. Preserve an original value beside any normalized value. Document rounding, timezone conversion, deduplication, filtering, and joins. Do not alter source records to make them fit a desired conclusion.

Use Observed for facts directly visible in the materials reviewed; Reported for an assertion by a source that has not been independently corroborated; Inferred for an analytical conclusion derived from facts; Estimated for a result that depends on assumptions or an estimating method. Arithmetic directly reconciled to observed inputs can be Observed, with the formula stated. A severity assessment remains a judgment even when its input defect is observed.

Confidence is HIGH, MODERATE, LOW, or NOT ASSESSABLE. Assess the support for each claim rather than borrowing the reputation of the publisher. HIGH requires direct, complete, internally consistent evidence for that narrow claim; MODERATE indicates a defined limitation; LOW indicates material ambiguity; NOT ASSESSABLE means the inputs cannot support a conclusion. Confidence is not the same as severity, evidence class, legal applicability, or action priority.

Links below were reviewed during preparation on 2026-10-09. They are reference starting points. A later session must retrieve the current version or record that it could not verify it. The suite's sample thresholds and workflow gates are author-defined illustrations unless a specific, applicable authority is identified.


## Public method references

| ID | Primary source | Version / reviewed date | Applicability and narrow use |
| --- | --- | --- | --- |
| REF-001 | [FFIEC, BSA/AML Independent Testing](https://bsaaml.ffiec.gov/manual/AssessingTheBSAAMLComplianceProgram/03) | March 2020 section; reviewed 2026-10-09 | U.S. banking examination context; supports documenting scope, procedures, findings, and independence. It does not set this suite's sample size. |
| REF-002 | [FFIEC, Risk-Focused BSA/AML Supervision](https://bsaaml.ffiec.gov/manual/ScopingAndPlanning/02) | 2020 section; reviewed 2026-10-09 | U.S. examination method reference; supports relating testing to risk. It does not certify the sufficiency of a supplied sample. |

These are supervisory reference materials. Determine the institution type, applicable requirements, and approved testing methodology separately. The arithmetic, statuses, selection ledger, and example criteria here are the suite author's analytical design, not quoted regulatory prescriptions.
