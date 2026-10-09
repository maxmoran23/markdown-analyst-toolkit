# Inputs and evidence — Monitoring Scenario and Threshold Review

## Input bundle and comparison contract

| Input | Minimum fields or content | Analytical consequence if missing |
| --- | --- | --- |
| Scenario specification | Purpose, included activity, feature definitions, windows, comparator, exclusions | Cannot reproduce candidate outputs |
| Full population manifest | Grain, period, distinct IDs, eligibility, source counts | Cannot estimate workload coverage reliably |
| Candidate configuration | ID, version, threshold, feature/rule changes | Candidates may not be comparable |
| Scored units | Unit ID, customer/group ID, feature values or score, eligibility | Partial input yields restricted comparison |
| Label ledger | Label definition, source, reviewer, date, independence, uncertainty | Performance claims may be circular or biased |
| Operational context | Current volumes, duplicate suppression, handling time, capacity | Workload estimates remain scenarios |
| Change context | Previous tuning, holdout design, approval route, rollback criteria | No implementation recommendation |

Scores have no inherent unit of suspicion. A score of 75 on one method need not match75 on another. Keep the method, version, transformation, and calibration population attached to every score. If a score is supplied without features, compare its cutoffs but do not claim to have reproduced how the score was generated.

## Minimum unit dictionary

unit_id is the unique evaluation opportunity. group_id identifies the customer, account cluster, or other dependency group used to prevent leakage across evaluation partitions. score is numeric on the explicitly declared scale; the fixture uses0 to 100. label is POSITIVE, NEGATIVE, or UNKNOWN under a named review criterion. label_source identifies the evidence and reviewer process. event_window_start/end define observation timing. label_as_of identifies when the outcome became observable. candidate_id and threshold identify the evaluated version.

POSITIVE should mean the defined target for this evaluation, such as an independently substantiated review-worthy pattern. It does not necessarily mean a filed report, confirmed crime, or regulatory violation. NEGATIVE means the review found the specified target absent within its scope; it is not proof of permanent legitimacy. UNKNOWN includes unreviewed, unresolved, inadequate-evidence, and out-of-window outcomes, with the reason preserved.

## Label provenance and bias

Record whether reviewers saw the original alert, candidate score, threshold, or expected outcome. These can influence adjudication. Use a written label rubric and record disagreements. If multiple reviewers disagree, keep the original labels, adjudication rationale, final label if resolved, and confidence. Do not resolve disagreement by selecting the label that improves a preferred candidate's metrics.

Alerts selected for investigation are enriched by the existing system. Labels drawn only from that queue may omit suspicious activity that never alerted. A candidate evaluated solely against historical filed cases may inherit previous monitoring, investigation, and reporting decisions. Preserve those selection mechanisms in the limitations. To estimate broader coverage, obtain an appropriate reviewed sample from below-threshold and nonalerted activity, with selection probabilities when inference requires them.

## Full population versus evaluation subset

Maintain all units, including unknown labels, for candidate alert-volume calculations when scores are available. Use only evaluable labelled units in the confusion matrix, with the subset count stated. If an unlabelled unit lacks a score too, it is unknown workload rather than a nonalert. A data issue affecting critical feature computation prevents assuming the unit was properly monitored.

Keep development, tuning, validation, and post-change monitoring periods distinct. Prevent the same group appearing in both fitting and holdout partitions where that would leak information. A chronological split can still leak through overlapping lookback windows or labels observed only later. Record these dependencies explicitly.

## Evidence register and claim discipline

Every material input receives an evidence ID. Use SYN-001 for the fictional worked-example package only; use SRC-001 onward for supplied operational evidence and REF-001 onward for public method references. A public reference supports a methodological statement, not a finding about the supplied population. Keep those two roles separate even when both appear in the same finding.

For each item capture title, origin, source locator, version, publication or creation date if known, retrieval date, period covered, relevant passage or row IDs, accessibility, transformations, and limitations. A locator must let another reviewer find the same passage, cell range, or records. Preserve an original value beside any normalized value. Document rounding, timezone conversion, deduplication, filtering, and joins. Do not alter source records to make them fit a desired conclusion.

Use Observed for facts directly visible in the materials reviewed; Reported for an assertion by a source that has not been independently corroborated; Inferred for an analytical conclusion derived from facts; Estimated for a result that depends on assumptions or an estimating method. Arithmetic directly reconciled to observed inputs can be Observed, with the formula stated. A severity assessment remains a judgment even when its input defect is observed.

Confidence is HIGH, MODERATE, LOW, or NOT ASSESSABLE. Assess the support for each claim rather than borrowing the reputation of the publisher. HIGH requires direct, complete, internally consistent evidence for that narrow claim; MODERATE indicates a defined limitation; LOW indicates material ambiguity; NOT ASSESSABLE means the inputs cannot support a conclusion. Confidence is not the same as severity, evidence class, legal applicability, or action priority.

Links below were reviewed during preparation on 2026-10-09. They are reference starting points. A later session must retrieve the current version or record that it could not verify it. The suite's sample thresholds and workflow gates are author-defined illustrations unless a specific, applicable authority is identified.


## Public method references

| ID | Primary source | Version / reviewed date | Applicability and narrow use |
| --- | --- | --- | --- |
| REF-001 | [FFIEC, Suspicious Activity Reporting](https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04) | Online section reviewed 2026-10-09 | U.S. banking examination context; supports understanding and periodically testing monitoring parameters. It does not prescribe these scores or target recall. |
| REF-002 | [Federal Reserve, SR 26-2: Revised Guidance on Model Risk Management](https://www.federalreserve.gov/supervisionreg/srletters/SR 2602.htm) | April 17, 2026; reviewed 2026-10-09 | The letter supersedes SR 11-7 and SR 21-8 and states expected relevance mainly to Federal Reserve-regulated banking organizations above $30 billion in assets. Assess actual applicability separately. |

The current reference set intentionally does not present SR 11-7 as the prevailing letter. Determine whether the reviewed system is within the applicable model-risk framework and what proportionate review is required. This suite's candidate math and synthetic gates are analytical design choices, not regulator-approved performance standards.
