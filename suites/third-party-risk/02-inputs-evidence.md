# Inputs and evidence — Third-Party Service and Assurance Review

## Required input bundle

| Input | Minimum contents | Why it matters |
| --- | --- | --- |
| Service scope | Contracting entity, service version, users, activities, locations | Prevents reliance on evidence for the wrong service |
| Criticality facts | Failure consequence, time tolerance, alternatives, volume | Sets proportionate review depth |
| Data and access | Data classes, storage, processing, privileges, retention | Identifies information and control exposure |
| Dependencies | Subcontractors, hosting, reference sources, support, fallback | Exposes shared and fourth-party failure paths |
| Contract materials | Current executed terms, schedules, changes, responsibilities | Separates enforceable commitments from proposals |
| Assurance evidence | Report scope, period, opinion, exceptions, exclusions, user controls | Defines what was actually examined |
| Operating evidence | Incidents, service metrics, recovery tests, change history | Supports current performance assessment |
| Exit materials | Export format, completeness, access removal, assistance, transition | Tests whether reliance can end safely |

Legal entity identification matters for contracting and public-source research, but avoid treating a same-name search result as the same entity. Keep identifiers and jurisdictional details supplied for the reviewed relationship. If identity is ambiguous, restrict identity-based claims. The fixture uses only generic fictional provider roles and needs no real entity research.

## Service dependency dictionary

service_id identifies one service or dependency. provider_role is the primary provider, subcontractor, reference supplier, support provider, or proposed fallback. service_function describes what it does in this relationship. data_access identifies actual or claimed data exposure and privilege. dependency_id links other service IDs and may contain multiple values separated by semicolons. substitutability describes a tested alternative, an untested possibility, or no immediate substitute. evidence_ids points to the source for each assertion.

A dependency list supplied by the primary provider may be Reported and incomplete. Preserve that limitation. A contract allowing unrestricted subcontracting is not proof of which entities currently perform the service. A fourth party may have no direct contract with the customer; identify what visibility and control the customer actually has through the prime relationship.

## Assurance review dictionary

review_id is a unique assessment criterion. domain identifies scope, security, resilience, contract, user control, exit, or another defined topic. criterion is an observable requirement for this intended use. critical is the stated gate classification, with rationale. result is SUPPORTED, PARTIAL, FAILED, UNVERIFIED, or NOT APPLICABLE. The first four apply to the fixture. SUPPORTED means the supplied evidence supports that criterion within its scope, not that the whole provider is safe.

For each assurance report capture issuer, report type, service/system description, period covered, issue date, management assertion, opinion, relevant test exceptions, excluded components, complementary user controls, and subservice treatment where provided. A bridge letter is a later management assertion; do not silently present it as an extension of independent testing. A report may remain useful after its period ends, but the uncovered interval is a limitation requiring assessment.

## Financial and legal evidence boundaries

Where viability matters, distinguish audited statements, management accounts, forecasts, and unsupported claims. A cash-runway calculation depends on burn rate, available cash, commitments, funding assumptions, and period consistency. Do not infer imminent failure from one loss figure or solvency from positive revenue. The core fixture does not require a financial score.

For public enforcement, licensing, ownership, or adverse-information checks, record the sources and exact search scope actually covered. No hit is a bounded search result, not proof of no issue. PEP status, geography, or media allegations require context and identity verification; they are not automatic rejection criteria. Refer unresolved legal significance to the appropriate human reviewer.

## Evidence register and claim discipline

Every material input receives an evidence ID. Use SYN-001 for the fictional worked-example package only; use SRC-001 onward for supplied operational evidence and REF-001 onward for public method references. A public reference supports a methodological statement, not a finding about the supplied population. Keep those two roles separate even when both appear in the same finding.

For each item capture title, origin, source locator, version, publication or creation date if known, retrieval date, period covered, relevant passage or row IDs, accessibility, transformations, and limitations. A locator must let another reviewer find the same passage, cell range, or records. Preserve an original value beside any normalized value. Document rounding, timezone conversion, deduplication, filtering, and joins. Do not alter source records to make them fit a desired conclusion.

Use Observed for facts directly visible in the materials reviewed; Reported for an assertion by a source that has not been independently corroborated; Inferred for an analytical conclusion derived from facts; Estimated for a result that depends on assumptions or an estimating method. Arithmetic directly reconciled to observed inputs can be Observed, with the formula stated. A severity assessment remains a judgment even when its input defect is observed.

Confidence is HIGH, MODERATE, LOW, or NOT ASSESSABLE. Assess the support for each claim rather than borrowing the reputation of the publisher. HIGH requires direct, complete, internally consistent evidence for that narrow claim; MODERATE indicates a defined limitation; LOW indicates material ambiguity; NOT ASSESSABLE means the inputs cannot support a conclusion. Confidence is not the same as severity, evidence class, legal applicability, or action priority.

Links below were reviewed during preparation on 2026-10-09. They are reference starting points. A later session must retrieve the current version or record that it could not verify it. The suite's sample thresholds and workflow gates are author-defined illustrations unless a specific, applicable authority is identified.


## Current public reference set

| ID | Primary source | Version / reviewed date | Applicability and narrow use |
| --- | --- | --- | --- |
| REF-001 | [Federal Reserve SR 23-4, Interagency Guidance on Third-Party Relationships](https://www.federalreserve.gov/supervisionreg/srletters/sr2304.htm) | June 07, 2023; reviewed 2026-10-09 | U.S. banking supervisory context; supports proportionate lifecycle review. Assess actual institutional applicability. |
| REF-002 | [OCC 2024-11, Third-Party Relationships: A Guide for Community Banks](https://www.occ.gov/news-issuances/bulletins/2024/bulletin-2024-11.html) | May 03, 2024; reviewed 2026-10-09 | Voluntary resource aimed at community banks; not an exhaustive checklist or substitute for applicable requirements. |
| REF-003 | [OCC 2026-46, Proposed Third-Party Risk Management Guidance](https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-46.html) | September 11, 2026; reviewed 2026-10-09 | Proposal at review date. Track possible change; do not treat as finalized replacement guidance. |

The September 2026 proposal distinguishes planned revision from current final guidance. Recheck source status in a later session. The suite does not treat supervisory guidance as a statute, promise regulator acceptance, or impose identical diligence on every service. Its specific criteria, classifications, recovery targets, and example decisions are author-defined review methods.
