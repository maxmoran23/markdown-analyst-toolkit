# Inputs and evidence — Historical Monitoring Lookback and Remediation Review

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

### E01: Defect chronology

**Request.** Discovery date, earliest possible impact, affected versions, corrected versions and uncertainty.

**Supplied specimen.** Mapping defect described across January through June; July continuity unresolved.

**Insufficiency branch.** Do not use the remediation date as proof that no earlier or later activity was affected.

### E02: Initial scope decision

**Request.** Population, historical period, products, channels, entities and rationale.

**Supplied specimen.** Initial discovery review January through March; analytical fixture includesApril through June.

**Insufficiency branch.** If actual scope approval is absent, label the scope as an analytical assumption and retain the human approval gap.

### E03: Independent control manifest

**Request.** Complete expected historical unit IDs and period totals from a separate control.

**Supplied specimen.** Thirty expected units, five per month, including L30.

**Insufficiency branch.** A retrieval count alone cannot establish completeness; missing records cannot identify themselves.

### E04: Raw retrieval inventory

**Request.** Every received representation, source identifier, source period and amount.

**Supplied specimen.** Thirty-four rows including three duplicates and two July records.

**Insufficiency branch.** Preserve duplicates and exclusions in intake accounting rather than deleting them before reconciliation.

### E05: Canonical identity rule

**Request.** Stable event or case identity, alias mapping and conflict resolution.

**Supplied specimen.** RAW-D1 duplicates L02, RAW-D2 duplicates L12, RAW-D3 duplicates L22.

**Insufficiency branch.** Similar names or amounts alone do not establish that records are duplicates; conflicting versions need explicit resolution.

### E06: Historical decision record

**Request.** Original status, rationale, evidence available then and relevant decision time.

**Supplied specimen.** CLOSED, ESCALATED or NOT_GENERATED preserved separately from current review state.

**Insufficiency branch.** A historical closed status does not prove current evidence was reviewed or that the original rationale survives a newly discovered defect.

### E07: Recovered supporting evidence

**Request.** Underlying activity, customer context, source messages and relevant investigation material.

**Supplied specimen.** L25 through L29 have retrieved summaries but lack essential supporting evidence.

**Insufficiency branch.** Receipt of a summary cannot be treated as full evidential availability.

### E08: Current comparison packet

**Request.** What changed, what remains consistent, new facts and competing explanations.

**Supplied specimen.** Six no-new-information comparisons and six new-information referrals.

**Insufficiency branch.** New information requires assessment; it does not automatically establish suspicious activity or a filing duty.

### E09: Review queue and priorities

**Request.** Assigned states, risk rationale, dependencies, aging basis and responsible roles.

**Supplied specimen.** Six re-reviews, six pending reviews, five unassessable units and one missing unit.

**Insufficiency branch.** An illustrativeHIGH label is not a legal deadline or proof of an actual assignment.

### E10: Expansion triggers

**Request.** Evidence connecting the defect to adjacent periods, related populations or new mechanisms.

**Supplied specimen.** Six explicit expansion and recovery proposals.

**Insufficiency branch.** Do not expand indefinitely by intuition or stop because the current staffing budget has been consumed.

### E11: Downstream handoff evidence

**Request.** Referral contents, intended recipient role, acknowledgment and decision returned.

**Supplied specimen.** Six referrals remain open; no actual acknowledgment supplied.

**Insufficiency branch.** A draft referral, email template or action row is not delivery evidence.

### E12: Completion and retention evidence

**Request.** Resolved population accounting, review state, material limitations and authorized acceptance.

**Supplied specimen.** Whole-lookback acceptance is unrecorded and material work remains.

**Insufficiency branch.** This suite does not prescribe a universal retention period or authorize destruction of historical records.

## Exact source-to-register mapping

**SYN-201 — Independent fictional historical control manifest.** Location: 10-worked-example.md, thirty-unit manifest and six-period control totals. This is fictional source material. Its declared downstream registers are PeriodReconciliation, CanonicalUnits, ExpansionDecisions, EvidenceProvenance, ProcessQA, CompletionGates. A value in those registers must remain traceable to the particular input or derived result. The source does not establish a real customer fact, policy or actual approval.

**SYN-202 — Fictional archive retrieval with duplicates exclusions and missing unit.** Location: 10-worked-example.md, complete thirty-four-row retrieval ledger. This is fictional source material. Its declared downstream registers are PeriodReconciliation, CanonicalUnits, RetrievalLedger, ExpansionDecisions, EvidenceProvenance, ProcessQA, CompletionGates. A value in those registers must remain traceable to the particular input or derived result. The source does not establish a real customer fact, policy or actual approval.

**SYN-203 — Fictional comparison outcomes and incomplete review states.** Location: 10-worked-example.md, complete unit and review-action registers. This is fictional source material. Its declared downstream registers are ReviewActions, ExpansionDecisions, EvidenceProvenance, ProcessQA, CompletionGates. A value in those registers must remain traceable to the particular input or derived result. The source does not establish a real customer fact, policy or actual approval.

**SYN-204 — Fictional defect chronology and scope-boundary evidence.** Location: 10-worked-example.md, dated scope assumptions and unresolved July question. This is fictional source material. Its declared downstream registers are ExpansionDecisions, EvidenceProvenance, CompletionGates. A value in those registers must remain traceable to the particular input or derived result. The source does not establish a real customer fact, policy or actual approval.

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
