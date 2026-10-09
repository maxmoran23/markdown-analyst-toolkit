# Inputs and evidence — Monitoring System Independent Challenge and Validation

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

### E01: System boundary

**Request.** Inventory of components, upstream data, downstream routing and intended uses.

**Supplied specimen.** Five components cover feature construction, R1, I1, C1 and human disposition.

**Insufficiency branch.** A review of one predicate cannot validate source ingestion, analyst review or the whole reporting program.

### E02: Concept statement

**Request.** Mechanism the scenario seeks to identify and activity it intentionally omits.

**Supplied specimen.** Repeated credits from at least two originators in a supplied fixed window.

**Insufficiency branch.** If an important mechanism is excluded, decide whether a separate control covers it; do not alter the concept to fit observed success.

### E03: Classification evidence

**Request.** Mathematical design, estimated outputs, theory basis, parameter fitting and actual use.

**Supplied specimen.** All supplied quantitative components are deterministic arithmetic or fixed rules.

**Insufficiency branch.** Do not apply model guidance solely because software computes a number; inspect the current definition and the real component.

### E04: Reference specification

**Request.** Exact conditions, operators, units, eligibility, null behavior and version.

**Supplied specimen.** R1 uses amount>=10000, count>=3, originators>=2; missing amount produces unknown.

**Insufficiency branch.** A prose instruction such as large repeated credits is insufficient to reconstruct expected outputs without clarification.

### E05: Implementation representation

**Request.** Versioned code, configuration or complete stated behavior for the same inputs.

**Supplied specimen.** I1 uses amount>10000 and false for missing amount.

**Insufficiency branch.** If execution is unavailable, label this as a supplied behavior comparison, not verification of production binary or deployed code.

### E06: Raw feature frame

**Request.** Complete input values with independent source count and keys.

**Supplied specimen.** Twenty-four units, four segments, twenty present and four missing amounts.

**Insufficiency branch.** Do not claim raw transaction lineage from feature-level inputs; request the underlying transformations separately.

### E07: Outcome labels

**Request.** Defined objective, adjudication sources, maturity and review selection.

**Supplied specimen.** Twelve positive, eight negative and four unknown synthetic labels.

**Insufficiency branch.** Constructed examples are useful for boundary tests but unsuitable for a live-effectiveness inference.

### E08: Development evidence

**Request.** Design alternatives, rejected approaches, parameter search and known limitations.

**Supplied specimen.** A declared diagnostic challenger drops the originator condition.

**Insufficiency branch.** A challenger that was optimized on the same labels cannot establish an unbiased performance advantage.

### E09: Change history

**Request.** Specification changes, implementation differences, release records and rollback scope.

**Supplied specimen.** R1 and I1 are named separately; actual deployment approval is not supplied.

**Insufficiency branch.** A version label without immutable content cannot establish which implementation produced a historical output.

### E10: Reviewer standing

**Request.** Qualifications, prior involvement, conflicts, access and escalation rights.

**Supplied specimen.** Only fictional reviewer roles exist in this example.

**Insufficiency branch.** Calling a paragraph independent does not demonstrate reviewer objectivity or legal independence.

### E11: Ongoing monitoring

**Request.** Comparable periods, input quality, output stability, exception age and delayed outcomes.

**Supplied specimen.** The fixture contains one constructed feature set and no drift baseline.

**Insufficiency branch.** A static 24-row example cannot prove long-run stability, reasonable monitoring frequency or a suitable statistical control limit.

### E12: Issue closure evidence

**Request.** Corrected version, full regression replay, unresolved limitations and use decision.

**Supplied specimen.** Four material issue records remain open or blocked.

**Insufficiency branch.** Closing a ticket because a developer says fixed is insufficient evidence that the correction works and avoids new losses.

## Exact source-to-register mapping

**SYN-101 — Twenty-four fictional unit features and independent outcomes.** Location: 10-worked-example.md, complete raw feature ledger. This is fictional source material. Its declared downstream registers are ComponentInventory, ChallengeTests, OutcomeUnits, OutcomeMetrics, IssueRegister, EvidenceProvenance, ProcessQA, ReleaseGates. A value in those registers must remain traceable to the particular input or derived result. The source does not establish a real customer fact, policy or actual approval.

**SYN-102 — Reference R1, implemented I1 and challenger C1 definitions.** Location: 10-worked-example.md, independent predicate specification. This is fictional source material. Its declared downstream registers are ComponentInventory, ChallengeTests, OutcomeUnits, OutcomeMetrics, IssueRegister, EvidenceProvenance, ProcessQA, ReleaseGates. A value in those registers must remain traceable to the particular input or derived result. The source does not establish a real customer fact, policy or actual approval.

**SYN-103 — Fictional challenge records and unresolved governance evidence.** Location: 10-worked-example.md, issue and gate registers. This is fictional source material. Its declared downstream registers are ComponentInventory, ChallengeTests, IssueRegister, EvidenceProvenance, ProcessQA, ReleaseGates. A value in those registers must remain traceable to the particular input or derived result. The source does not establish a real customer fact, policy or actual approval.

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
