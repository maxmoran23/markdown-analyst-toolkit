# Inputs and evidence — Monitoring Scenario and Threshold Review

## Intake accounting and evidence preservation

Create a source inventory before reading for conclusions. For each source record the source ID, descriptive title, supplier role, received representation, effective date, extraction period, original grain, control total, applicable population, known exclusions, availability and limitations. If the material is a screenshot, state that sortable rows and hidden fields are unavailable. If it is an export, identify whether it represents transactions, alerts, cases, customers, customer-windows or a joined view. An export row count is not automatically the number of unique economic events.

Keep the raw supplied representation intact. Corrections belong in a derived register with original value, corrected value, reason, evidence and reviewer state. Do not delete a duplicate before preserving its alias and the rule that selects the canonical record. A repeated identifier with different values is a conflict, not a harmless duplicate. Preserve both versions and resolve which one is authoritative for the stated cutoff. A later correction may be authoritative prospectively without changing what was available to a historical reviewer.

Reconciliation needs an independent comparator. Counting an extract twice establishes internal consistency, not completeness. Request a source-system control report, manifest, period total or separately generated inventory. Identify whether that comparator uses the same filters and whether it could share the same defect. If the extract and control both originate from a broken join, agreement does not rule out missing records. Document the common dependency and seek a different control where the missing population could materially change the answer.

## Nulls, timing and identity

A blank numeric value is null, not zero. A missing label is not a negative outcome. An unavailable archive period is not a period without activity. A missing approval is not an implied acceptance. Retain an explanation for each null-bearing field or class of nulls. Distinguish not supplied, unreadable, not applicable, not yet mature, not tested and not retrievable. These states can have different implications even if the display uses a blank cell for the numeric value.

Use the event time for activity sequencing, the system processing time for operational delay, the evidence receipt time for what was known when, and the review decision time for the state history. Do not substitute one timestamp for another. If a timezone is absent, do not infer intraday ordering or a precise lag. A date-only boundary should use an explicit inclusive date convention. Corrected exports should retain the original event period and the later receipt date so retrospective evidence does not masquerade as contemporaneously available information.

Resolve identity at the declared grain. A customer with multiple accounts may create several source rows but one review unit, while one joint account may require several distinct subject records. The fixture supplies stable IDs; a live session must examine the identity mapping actually supplied. Treat an unresolved mapping as a coverage and attribution limitation. Do not join on names alone, drop a row with an unmatched key, or combine customer histories merely because a display label appears similar.

## Source review and public references

The public references below were accessed for this suite’s build on Oct 09, 2026. They support short contextual statements, not the fictional facts or every authored procedural detail. The detailed decision rules, tests, schemas and case scenarios in this suite are original toolkit design choices. Their illustrative parameters are not agency-prescribed requirements. Check the current publication, jurisdiction, regulated population and effective period before applying external guidance to a real question.

A source register should retain a precise location such as a section, paragraph, table, test ID or record range. A home-page link is not evidence of a specific claim. If you cannot retrieve a cited source during the session, say that the source was referenced but not independently reviewed in that session. Do not manufacture a quotation or page number. Avoid carrying old supervisory language forward when a newer document explicitly supersedes it or a page directs readers to more recent guidance on the specific topic.

## Complete evidence request specifications

### E01: Population frame

**Request.** A complete customer-window list, population control totals, eligibility predicate and source cutoff.

**Supplied specimen.** U01 through U36, twelve units in each partition, all eligible.

**Insufficiency branch.** If only alerted units are provided, recall and false-negative counts are not estimable; preserve the supplied subset and request nonalerted coverage.

### E02: Feature definition

**Request.** Score scale, feature period, algorithm version, missing-score behavior and feature availability date.

**Supplied specimen.** A supplied deterministic 0–100 score for every unit.

**Insufficiency branch.** If score definitions differ between candidates, this is not a pure threshold comparison; replay a common feature basis or label the distinct change.

### E03: Dependence map

**Request.** Group IDs connecting related units, accounts, customers or temporal windows.

**Supplied specimen.** Two units per group G01 through G18; groups never cross partitions.

**Insufficiency branch.** A random row split can leak the same entity into both training and holdout; stop the independence claim and regroup before evaluation.

### E04: Partition ledger

**Request.** Frozen assignment, chronological boundaries, development access and all accesses to protected outcomes.

**Supplied specimen.** TRAIN, VALIDATION and HOLDOUT each contain twelve units.

**Insufficiency branch.** A holdout inspected during candidate construction is consumed; do not restore independence merely by renaming the file.

### E05: Candidate configurations

**Request.** Segment cutoffs, comparison operator, eligibility differences, version and freeze point.

**Supplied specimen.** BASE60, HIGH75, LOW50 and SEGMENTED with inclusive comparisons.

**Insufficiency branch.** An unspecified equality boundary can change which known positives count; do not infer greater-than from an informal phrase such as above threshold.

### E06: Label provenance

**Request.** Adjudication rubric, evidence source, review date, disagreement process and maturity cutoff.

**Supplied specimen.** POSITIVE16, NEGATIVE13, UNKNOWN4 and CENSORED3.

**Insufficiency branch.** A SAR filing, analyst escalation or previous alert is a process outcome, not automatically ground truth for criminal activity or the detection objective.

### E07: Routing inputs

**Request.** Group merge predicate, lead selection, suppression list and current evidence of authorization.

**Supplied specimen.** G17 suppressed; lowest unit ID leads each retained candidate-group case.

**Insufficiency branch.** If a suppressed group has no valid authority, retain the raw hit and suppression exception; never erase it from the population or declare the queue fully reviewed.

### E08: Workload assumptions

**Request.** Lead review time by segment, incremental merged-unit time, available productive hours and task scope.

**Supplied specimen.** RETAIL1 hour, SMALL_BUSINESS1.5 hours, CORRESPONDENT2 hours;0.25 per additional hit.

**Insufficiency branch.** Assumed hours are not measured productivity. Do not scale a synthetic case to staffing headcount without volumes, leave, QA, escalation and arrival-pattern evidence.

### E09: Below-threshold frame

**Request.** Every eligible nonhit for the reference candidate, stratum and selection record.

**Supplied specimen.** Fifteen BASE60 nonhits, five per partition, two selected per partition.

**Insufficiency branch.** A convenience list of interesting misses can locate defects but cannot estimate the missed-positive rate for all nonhits.

### E10: Sensitivity design

**Request.** Predeclared threshold grid, parameters held fixed and outcome measures.

**Supplied specimen.** Four supplied candidates and exact incremental unit identities.

**Insufficiency branch.** Trying many cutoffs and reporting only the best creates selection bias; report the search process and reserve new protected evidence.

### E11: Change and rollback evidence

**Request.** Proposed implementation diff, approval route, replay scope, launch restrictions and rollback conditions.

**Supplied specimen.** No real deployment or rollback authorization is supplied.

**Insufficiency branch.** A notebook comparison is not an implementation verification. A rollback plan that cannot identify the previous version is incomplete.

### E12: Monitoring after change

**Request.** Comparable source completeness, score distributions, alert arrivals, suppression changes and delayed labels.

**Supplied specimen.** Only the single fictional frame is supplied; drift inference is unavailable.

**Insufficiency branch.** A changed hit rate may reflect input mix, volume or missingness rather than deteriorating detection. Request those decompositions before attributing cause.

## Exact source-to-register mapping

**SYN-001 — Fictional 36-unit population, label and dependence register.** Location: 10-worked-example.md, raw population and unit-by-unit trace. This is fictional source material. Its declared downstream registers are Population, AlertRouting, CandidateDecisions, EvidenceProvenance, ProcessQA. A value in those registers must remain traceable to the particular input or derived result. The source does not establish a real customer fact, policy or actual approval.

**SYN-002 — Four predeclared fictional score candidates.** Location: 10-worked-example.md, frozen candidate input table. This is fictional source material. Its declared downstream registers are Candidates, CandidateDecisions, EvidenceProvenance, ProcessQA. A value in those registers must remain traceable to the particular input or derived result. The source does not establish a real customer fact, policy or actual approval.

**SYN-003 — Fictional G17 suppression and group-routing policy.** Location: 10-worked-example.md, routing input and complete hit ledger. This is fictional source material. Its declared downstream registers are AlertRouting, CandidateDecisions, EvidenceProvenance, ProcessQA. A value in those registers must remain traceable to the particular input or derived result. The source does not establish a real customer fact, policy or actual approval.

**SYN-004 — Fictional complete below-threshold frame and assigned ranks.** Location: 10-worked-example.md, complete fifteen-row frame. This is fictional source material. Its declared downstream registers are BelowThreshold, EvidenceProvenance, ProcessQA. A value in those registers must remain traceable to the particular input or derived result. The source does not establish a real customer fact, policy or actual approval.

## Primary-source context and applicability limits

### REF-001: FFIEC suspicious activity monitoring examination procedures

[FFIEC suspicious activity monitoring examination procedures](https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04_ep). Context for monitoring process review, programming verification and resource considerations; the page identifies newer SAR FAQs for selected topics. Accessed for this build on Oct 09, 2026.

### REF-002: Federal Reserve SR 26-2, April 17, 2026

[Federal Reserve SR 26-2, April 17, 2026](https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm). Current interagency model-risk guidance replaces SR 11-7 and SR 21-8; its scope and applicability must be assessed rather than assumed. Accessed for this build on Oct 09, 2026.

### REF-003: Federal Reserve, Supervisory Guidance on Model Risk Management

[Federal Reserve, Supervisory Guidance on Model Risk Management](https://www.federalreserve.gov/frrs/guidance/supervisory-guidance-on-model-risk-management.htm). The definition excludes simple arithmetic and deterministic rules without statistical, economic or financial theory. Generative and agentic AI are outside this guidance. Validation rigor is contextual. Accessed for this build on Oct 09, 2026.

### REF-004: FinCEN and federal banking agencies, SAR FAQs, October 9, 2025

[FinCEN and federal banking agencies, SAR FAQs, October 9, 2025](https://www.fincen.gov/system/files/2025-10/SAR-FAQs-October-2025.pdf). Use the current questions and answers when considering the specific reporting topics they address; this toolkit does not make filing decisions. Accessed for this build on Oct 09, 2026.

### REF-005: FATF, Guidance for a Risk-Based Approach: The Banking Sector

[FATF, Guidance for a Risk-Based Approach: The Banking Sector](https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Risk-Based-Approach-Banking-Sector.pdf.coredownload.pdf). Public international risk-based context; national implementation and the relevant entity obligations must be separately established. Accessed for this build on Oct 09, 2026.

### REF-006: NIST, Confidence intervals for proportions

[NIST, Confidence intervals for proportions](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm). Reference for binomial proportion interval methods; sampling design, dependence, selection and outcome ascertainment determine whether an interval is meaningful. Accessed for this build on Oct 09, 2026.

### REF-007: GAO, Standards for Internal Control in the Federal Government, 2025 revision

[GAO, Standards for Internal Control in the Federal Government, 2025 revision](https://www.gao.gov/assets/890/882014.pdf). A federal-government internal-control reference used here only as a design analogy for monitoring deficiencies and corrective action; not a banking legal requirement. Accessed for this build on Oct 09, 2026.
