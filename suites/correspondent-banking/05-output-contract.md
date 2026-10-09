# Correspondent Banking — output contract

## Delivery and canonical record

Use the active stage in 01. Full workflow delivers the fixed report, workbook or complete exact tables, and optional offline dashboard. Analyze preserves the complete case record for later rendering. Render uses that saved record without inventing new analysis. Place **DRAFT — HUMAN REVIEW REQUIRED** and the evidence cutoff prominently until a named human disposition is evidenced.

The common tabs are Summary, Dashboard, Findings, Evidence, Actions and QA. **Their exact columns and accepted common-field states are defined in 07.** Do not add required common columns that the template lacks. Preserve richer source metadata, severity and confidence rationale, counterevidence, action evidence, reviewer notes and QA expectations in the complete case record and relevant existing text fields or report sections. The two domain tables below are additional; retain their exact names, column order and row identifiers.

## Fixed report headings

1. Correspondent relationship decision brief
2. Scope, legal applicability and payment population
3. Material relationship and transparency findings
4. Respondent relationship assessment
5. Payment transparency and nested access
6. Evidence and criterion provenance
7. Proposed relationship-specific actions
8. Limitations, quality checks and human disposition

Section 1 answers the decision question and names the unresolved gate. Section 2 states the population, timing, inclusion rules and calculation approach. Section 3 explains findings and alternatives. Sections 4 and 5 contain the first and second domain registers respectively. Section 6 carries exact evidence locators. Section 7 states proposed actions and actual human decisions separately. Section 8 records limitations, actual QA and unrecorded disposition.

## Domain tables and types

### RelationshipReview

Exact immutable header:

```text
respondent_id | respondent_name | services | nested_declared | physical_presence | regulated_affiliate | control_evidence | assessment | evidence_ids
```

One row per respondent legal entity. respondent_id and respondent_name are stable text. services describes the agreed service scope. nested_declared is YES, NO or UNKNOWN based on an identified representation. physical_presence is DOCUMENTED, NONE_REPORTED or UNKNOWN and is not by itself a legal conclusion. regulated_affiliate is DOCUMENTED, NOT_ASSESSED or UNKNOWN. control_evidence states source and scope. assessment is FOLLOW_UP, LIMITED_SUPPORT or LEGAL_CLASSIFICATION_REVIEW with rationale in the case record. evidence_ids resolve to Evidence. No row denotes approved onboarding or automatic exit.

### PaymentReview

Exact immutable header:

```text
payment_id | respondent_id | underlying_bank_id | amount | currency | initial_missing | cutoff_missing | nested_state | review_state | evidence_ids
```

One row per distinct payment message/economic payment in the fixture. payment_id and respondent_id are required text. underlying_bank_id is an identified downstream institution or NONE_DECLARED; UNKNOWN means evidence is absent. amount is a nonnegative decimal in currency, an ISO code. initial_missing and cutoff_missing list absent illustrative required fields or NONE. nested_state is DISCLOSED, UNDECLARED_OBSERVED, NOT_INDICATED or UNRESOLVED. DISCLOSED means evidenced nested access matches the declared scope; UNDECLARED_OBSERVED means evidenced nested access lacks declaration at the relevant date; NOT_INDICATED means the reviewed role evidence supports no nested use for this payment. UNRESOLVED means the record cannot establish whether the institution is a downstream access user, an ordinary beneficiary, or another role. A known bank identifier can coexist with an unresolved role; use underlying_bank_id UNKNOWN when the identifier itself is missing. Preserve UNRESOLVED separately from both confirmed nested use and NOT_INDICATED. review_state is GAP_OPEN, REPAIRED or COMPLETE for the four-field information criterion only; COMPLETE never resolves an unknown nesting role. evidence_ids are semicolon-delimited. A repair changes the current state without overwriting the original deficiency.

## Evidence, interpretation and display

Findings require a stable ID, condition, criterion, source locator, impact, severity rationale, confidence rationale, counterevidence and recommended next step. Place these explanations in the supported fields and report narrative. Claim class is Observed, Reported, Inferred or Estimated. Severity is HIGH, MEDIUM or LOW. Confidence is HIGH, MODERATE, LOW or NOT ASSESSABLE. A low-confidence concern may warrant urgent information gathering without becoming an established violation.

An evidence ID must resolve to Evidence and a precise source passage. Reserve SYN- identifiers for the fictional case and REF- identifiers for method references. Semicolon-delimit multiple IDs in domain cells; do not fabricate an evidence relationship from a similar-looking record number. Evidence title and locator fields may carry dates and availability when required by the case record. A bare URL is insufficient when the conclusion depends on a particular paragraph or table row.

Numbers remain numeric in workbooks and JSON. Missing values are empty spreadsheet cells, JSON null and Markdown null with a stated reason; zero means a supported measured zero. Native currency, quantity and date units must be visible. Show money to two decimal places with the currency identified, percentages to one decimal, counts as integers, and timestamps with timezone. Percentage-point columns contain values such as 25.0, not the fractional value 0.25; use an explicit percent-sign display, not a spreadsheet percentage conversion. Round at display, after calculations.

All filters must disclose hidden rows and preserve the full-population denominator separately. Unknowns appear as gaps or a distinct unresolved category. Do not draw a zero bar for missing evidence. No artifact may silently drop a contrary finding, represent a selected sample as the whole population, or present a source allegation as an adjudication.

## Release and fallback

The fixture measures completeness of four illustrative identity fields, not compliance with every payment-message rule. Preserve initial and cutoff states. An unknown physical-presence fact is not a finding of prohibited shell-bank activity. A documented regulated-affiliate claim requires the applicable legal definition and human classification; a trade name or group logo is insufficient. No sector-wide exit recommendation follows from the exercise.

Every artifact must preserve the scope, cutoff, source population reconciliation, finding count, principal totals, unresolved cases and human status. A narrative may show a wide record vertically for readability; the workbook still keeps every exact column. Test long source locators and literal text for truncation. Maintain readable light and dark presentation without remote assets. If export or browser testing is unavailable, use complete text tables and state the delivery checks NOT RUN.

Actions default to Proposed in the common action register. Accepted means a recorded human acceptance, not execution. Closed requires closure evidence in the case record. Do not invent owners, deadlines, approvals or completed outreach to fill a template. The final limitations must identify the actual missing fact and its effect, rather than rely on a generic disclaimer. Keep unresolved material defects visible even when other checks pass.
