# Adverse Media — output contract

## Delivery and canonical record

Use the active stage in 01. Full workflow delivers the fixed report, workbook or complete exact tables, and optional offline dashboard. Analyze preserves the complete case record for later rendering. Render uses that saved record without inventing new analysis. Place **DRAFT — HUMAN REVIEW REQUIRED** and the evidence cutoff prominently until a named human disposition is evidenced.

The common tabs are Summary, Dashboard, Findings, Evidence, Actions and QA. **Their exact columns and accepted common-field states are defined in 07.** Do not add required common columns that the template lacks. Preserve richer source metadata, severity and confidence rationale, counterevidence, action evidence, reviewer notes and QA expectations in the complete case record and relevant existing text fields or report sections. The two domain tables below are additional; retain their exact names, column order and row identifiers.

## Fixed report headings

1. Adverse-information decision brief
2. Scope, identity and search coverage
3. Material findings and competing accounts
4. Event assessment and current status
5. Source lineage and identity review
6. Evidence, chronology and corrections
7. Proposed review and clarification actions
8. Limitations, quality checks and human disposition

Section 1 answers the decision question and names the unresolved gate. Section 2 states the population, timing, inclusion rules and calculation approach. Section 3 explains findings and alternatives. Sections 4 and 5 contain the first and second domain registers respectively. Section 6 carries exact evidence locators. Section 7 states proposed actions and actual human decisions separately. Section 8 records limitations, actual QA and unrecorded disposition.

## Domain tables and types

### EventAssessment

Exact immutable header:

```text
event_id | subject_id | event_summary | identity_state | procedural_status | adverse_origin_families | current_assessment | confidence | evidence_ids | next_step
```

One row per distinct event candidate, including different-subject and unresolved candidates. event_id and subject_id are stable text. event_summary names the conduct and source attribution. identity_state is MATCHED, UNRESOLVED or DIFFERENT_SUBJECT. procedural_status is ALLEGATION_UNRESOLVED, DISMISSED, FINAL_ORDER or a documented case-specific status; these are separate from identity. adverse_origin_families is an integer count of eligible upstream adverse-assertion origins, never a conviction count. current_assessment states the bounded meaning at cutoff. confidence uses the common scale. evidence_ids resolve to Evidence, and next_step is proposed only.

### SourceReview

Exact immutable header:

```text
source_id | event_id | family_id | source_role | identity_state | eligible_for_event | publication_date | evidence_id | assessment_note
```

One row per reviewed source item. source_id is the raw item ID. event_id is the linked event or CONTEXT for a pure identity record. family_id tracks the upstream origin; different domains can share it. source_role is IDENTITY, ORIGINAL_REPORT, SYNDICATED_COPY, CHARGE_NOTICE, STATUS_UPDATE, FINAL_ORDER, DIFFERENT_SUBJECT_REPORT, ALLEGATION or SUBJECT_RESPONSE. identity_state records the exact match decision. eligible_for_event is YES, NO or CONTEXT and is not a truth label. publication_date is ISO date. evidence_id resolves to Evidence. assessment_note preserves source limits, copying and the response or reversal direction.

## Evidence, interpretation and display

Findings require a stable ID, condition, criterion, source locator, impact, severity rationale, confidence rationale, counterevidence and recommended next step. Place these explanations in the supported fields and report narrative. Claim class is Observed, Reported, Inferred or Estimated. Severity is HIGH, MEDIUM or LOW. Confidence is HIGH, MODERATE, LOW or NOT ASSESSABLE. A low-confidence concern may warrant urgent information gathering without becoming an established violation.

An evidence ID must resolve to Evidence and a precise source passage. Reserve SYN- identifiers for the fictional case and REF- identifiers for method references. Semicolon-delimit multiple IDs in domain cells; do not fabricate an evidence relationship from a similar-looking record number. Evidence title and locator fields may carry dates and availability when required by the case record. A bare URL is insufficient when the conclusion depends on a particular paragraph or table row.

Numbers remain numeric in workbooks and JSON. Missing values are empty spreadsheet cells, JSON null and Markdown null with a stated reason; zero means a supported measured zero. Native currency, quantity and date units must be visible. Show money to two decimal places with the currency identified, percentages to one decimal, counts as integers, and timestamps with timezone. Percentage-point columns contain values such as 25.0, not the fractional value 0.25; use an explicit percent-sign display, not a spreadsheet percentage conversion. Round at display, after calculations.

All filters must disclose hidden rows and preserve the full-population denominator separately. Unknowns appear as gaps or a distinct unresolved category. Do not draw a zero bar for missing evidence. No artifact may silently drop a contrary finding, represent a selected sample as the whole population, or present a source allegation as an adjudication.

## Release and fallback

Keep event counts separate from source-item counts. The example has four event candidates, three attributable events, nine reviewed source items and one uncompleted planned search. A dismissal updates EV-01; it does not erase historical receipt of the charge or prove the underlying conduct occurred. EV-03 stays visible as a different-subject negative control. A subject response is recorded and assessed, never automatically accepted or treated as obstruction.

Every artifact must preserve the scope, cutoff, source population reconciliation, finding count, principal totals, unresolved cases and human status. A narrative may show a wide record vertically for readability; the workbook still keeps every exact column. Test long source locators and literal text for truncation. Maintain readable light and dark presentation without remote assets. If export or browser testing is unavailable, use complete text tables and state the delivery checks NOT RUN.

Actions default to Proposed in the common action register. Accepted means a recorded human acceptance, not execution. Closed requires closure evidence in the case record. Do not invent owners, deadlines, approvals or completed outreach to fill a template. The final limitations must identify the actual missing fact and its effect, rather than rely on a generic disclaimer. Keep unresolved material defects visible even when other checks pass.
