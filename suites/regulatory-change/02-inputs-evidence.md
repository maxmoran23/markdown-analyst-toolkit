# Inputs and evidence — Regulatory Change and Obligation Mapping

## Input bundle

| Input | Minimum contents | Missing-input treatment |
| --- | --- | --- |
| Source documents | Full primary text, issuer, instrument ID, publication date, relevant provisions | Status and requirements remain unverified |
| Change history | Prior text, amendment, correction, delay, withdrawal, stay if relevant | Do not assume current consolidated effect |
| Generic scope profile | Jurisdiction, entity type, activity, product, threshold facts, exemptions claimed | Applicability unresolved or conditional |
| Existing control map | Control objective, owner role, procedure version, evidence | Gap assessment restricted |
| Implementation record | Design, build, test, training, approvals, operation evidence | Readiness is reported or unknown |
| Review frame | As-of date, covered authorities, period, sources searched or supplied | No completeness claim beyond frame |

Avoid organization names and nonpublic particulars in public examples. Use a generic activity profile sufficient for the applicability test. An unknown fact such as licensing category or transaction scope should become a question for the appropriate reviewer, not an inferred institutional characteristic.

## Instrument and provision dictionary

change_id identifies an instrument or a discrete change version. issuer and jurisdiction identify the authority. instrument_id includes the official citation, docket, or document number where available. instrument_status distinguishes PROPOSED, FINAL_NOT_EFFECTIVE, EFFECTIVE, GUIDANCE, WITHDRAWN, STATUS_UNVERIFIED, and other explicitly documented states. publication_date, effective_date, compliance_date, comment_date, and sunset_date are separate concepts. Record the source locator for every material date.

obligation_id identifies one atomic provision. requirement_summary states actor, action, object, condition, deadline, exceptions, and evidence needed. applicability is In scope, Out of scope, Conditional, or Unresolved, with a fact-to-text rationale. control_id maps to an existing or proposed response. readiness describes implementation evidence, not legal status. review_status captures a human decision separately from the assistant's assessment.

One instrument may contain many provisions with different dates or scope. The ChangeRegister date fields show a single common date only when valid for the instrument's mapped scope. If dates differ, leave the summary date null with “Multiple provision dates” in the report and show exact dates per obligation. Never use the earliest date as if every provision shared it.

## Source hierarchy and exact locators

Prefer enacted text, official publication, issuing authority materials, and authoritative updates for legal status. Use official summaries to navigate, then inspect operative text and dates. Secondary coverage can explain context or identify a potential development, but label its claims Reported until verified. A source may be primary for what an agency said without establishing the legal effect of that statement.

Capture the relevant section, paragraph, page, amendment instruction, definition, exception, and date clause. A citation to a 300-page document without a locator does not support a precise obligation. Retain the prior and revised language in concise paraphrase, with short quotations only when exact wording matters and quotation limits allow. Do not reproduce long copyrighted commentary.

## Verification and conflict log

For every conflict record competing statements, sources, publication/version dates, affected provisions, reason for uncertainty, and the authority needed to resolve it. A later news article does not automatically override an earlier final text. A correction may alter only one provision. A court order may have a particular scope and status; do not extrapolate its effect to all institutions without current legal review.

If browsing or primary retrieval is unavailable, record “supplied source only” and the as-of limitation. A URL in this suite is a research aid, not evidence that the current session opened it. Search coverage should list authorities and date ranges actually checked, including failed or incomplete retrievals.

## Evidence register and claim discipline

Every material input receives an evidence ID. Use SYN-001 for the fictional worked-example package only; use SRC-001 onward for supplied operational evidence and REF-001 onward for public method references. A public reference supports a methodological statement, not a finding about the supplied population. Keep those two roles separate even when both appear in the same finding.

For each item capture title, origin, source locator, version, publication or creation date if known, retrieval date, period covered, relevant passage or row IDs, accessibility, transformations, and limitations. A locator must let another reviewer find the same passage, cell range, or records. Preserve an original value beside any normalized value. Document rounding, timezone conversion, deduplication, filtering, and joins. Do not alter source records to make them fit a desired conclusion.

Use Observed for facts directly visible in the materials reviewed; Reported for an assertion by a source that has not been independently corroborated; Inferred for an analytical conclusion derived from facts; Estimated for a result that depends on assumptions or an estimating method. Arithmetic directly reconciled to observed inputs can be Observed, with the formula stated. A severity assessment remains a judgment even when its input defect is observed.

Confidence is HIGH, MODERATE, LOW, or NOT ASSESSABLE. Assess the support for each claim rather than borrowing the reputation of the publisher. HIGH requires direct, complete, internally consistent evidence for that narrow claim; MODERATE indicates a defined limitation; LOW indicates material ambiguity; NOT ASSESSABLE means the inputs cannot support a conclusion. Confidence is not the same as severity, evidence class, legal applicability, or action priority.

Links below were reviewed during preparation on 2026-10-09. They are reference starting points. A later session must retrieve the current version or record that it could not verify it. The suite's sample thresholds and workflow gates are author-defined illustrations unless a specific, applicable authority is identified.


## Primary reference material

| ID | Source | Version / reviewed date | Applicability and narrow use |
| --- | --- | --- | --- |
| REF-001 | [National Archives, Federal Register Tutorial](https://www.archives.gov/federal-register/tutorial/text) | Online tutorial; reviewed 2026-10-09 | U.S. federal publication context; distinguishes proposals, final documents, and date captions. Actual instruments still control. |
| REF-002 | [National Archives, Administrative Procedure Act,5 U.S.C. 553](https://www.archives.gov/federal-register/laws/administrative-procedure/553.html) | Statutory text as published on source; reviewed 2026-10-09 | U.S. rulemaking context with exceptions. Do not derive a universal effective date by adding30 days. |
| REF-003 | [National Archives, OFR Frequently Asked Questions](https://www.archives.gov/federal-register/faqs) | Online FAQ; reviewed 2026-10-09 | Helps locate publication and codification resources; not an institution-specific applicability opinion. |

The workflow, register states, readiness gates, fictional provisions, and prioritization method below are the suite author's analytical design. For other jurisdictions, use the relevant official publication and legal framework; do not transplant U.S. rulemaking assumptions. These short reference notes do not replace review of operative current text.
