# Fraud review: output contract

## Required delivery set

Return a report, a workbook or its exact tables, and an optional offline dashboard. The report is the decision narrative; the workbook is the evidence and calculation ledger; the dashboard is a filtered view of the same records. No output may use a different population, threshold, finding ID, or total. Add an as-of timestamp and a visible `DRAFT — HUMAN REVIEW REQUIRED` status until signoff is recorded.

The common workbook tabs are **Summary, Dashboard, Findings, Evidence, Actions, QA**. Files 06–08 define their rendering and common schemas. The following domain tabs are additional and have immutable column order. A changed header is a contract change, not a cosmetic edit. Keep machine fields in snake_case, numbers numeric, identifiers text, and missing values as empty spreadsheet cells / JSON `null` / Markdown `null`, accompanied by a reason in the designated status or rationale field. Zero means measured zero.

## Fixed report headings

1. Incident priorities and known exposure
2. Scope, incident population, and amount method
3. Findings and verification gaps
4. Requested, executed, and returned amounts
5. Authorization and incident-response review
6. Evidence and source provenance
7. Proposed actions for authorized responders
8. Limitations, quality checks, and human disposition

Every material finding needs its stable ID, condition, criterion, evidence, impact, severity rationale, confidence rationale, counterevidence, recommended next step, and human-decision status. Claim class must be one of `Observed`, `Reported`, `Inferred`, `Estimated`. Severity uses `HIGH`, `MEDIUM`, `LOW`; confidence uses `HIGH`, `MODERATE`, `LOW`, `NOT ASSESSABLE`. Confidence is not a probability unless a separately justified probabilistic method is supplied. High-impact uncertainty can have HIGH severity and LOW confidence.

## Domain tables

### IncidentAmounts

Exact header:

```text
case_id | currency | requested_amount | executed_amount | confirmed_return_amount | net_unreturned_amount | amount_status | review_state
```

### VerificationReview

Exact header:

```text
case_id | authorization_basis | detail_change | independent_verification | payment_status | time_sensitivity | proposed_action | evidence_ids
```

| Column | Type, units, and null rules |
| --- | --- |
| case_id | Required stable text; one incident per row in both domain tables. |
| currency | ISO currency code. |
| requested_amount | Nonnegative decimal in row currency; can be Reported, with source class disclosed. |
| executed_amount | Confirmed posted decimal; zero only for confirmed nonexecution; null if unknown. |
| confirmed_return_amount | Realized linked decimal; zero only when complete supplied evidence supports no return; null if unknown. |
| net_unreturned_amount | executed_amount minus confirmed_return_amount; null when either operand unknown. Ordinary payments can have nonzero values without being losses. |
| amount_status | CONFIRMED, EXECUTION_UNKNOWN, RETURN_UNKNOWN, or documented conflict. |
| review_state | SUSPECTED_FRAUD, PREVENTED_REQUEST, OPEN_ALLEGATION, BENIGN_SUPPORTED. |
| authorization_basis, detail_change, independent_verification | Text stating evidence and limits, not binary assumptions of legitimacy. |
| payment_status | EXECUTED_PARTIAL_RETURN, NOT_EXECUTED, UNKNOWN, EXECUTED, or other explicitly documented lifecycle state. |
| time_sensitivity | HIGH, MEDIUM, LOW; explain basis in finding or action. |
| proposed_action | Human action recommendation only. |
| evidence_ids | Semicolon-delimited source IDs resolving to Evidence. |

Narrative must show the reviewed population, amount inclusion rules, known subtotal versus unresolved amount, current as-of time, authorization uncertainty, and actual action status. Call F01's $30,000.00 known suspected-fraud unreturned value; do not call it final loss. F04's $5,000.00 ordinary payment remains in the flow table but outside that subtotal. Display unknown F03 amounts visibly in all outputs.

## Common-table content rules

Summary must contain scope and as-of details, input and exclusion counts, principal metrics with numerator/denominator and units, analytical status, and limitations. Findings contain one row per finding, with evidence IDs that resolve to Evidence. Evidence includes exact locator, source identity, date, claim class, availability, and limitations. Actions distinguish proposed, approved, executed, and verified; no synthetic example has an executed external action. QA records each check, expected result, actual result, pass/fail/not-tested status, and reviewer.

Narrative totals must cite the calculation or table row. Round only display values; calculate from original precision. Display percentages to one decimal and currency to two decimals with the ISO currency stated. Do not convert currency implicitly. Show timezone with human-facing timestamps. Preserve nulls in charts as gaps, never zero-height bars. Filters must expose how many rows are hidden and must not silently relabel filtered results as the full population.

## Required limitations and release block

State input coverage, missing data, attribution uncertainty, criterion provenance, tools not available, and tests not performed. Describe how each affects the supported decision. A generic disclaimer cannot substitute for a known defect. Record analyst, independent reviewer if any, review date, open issues, disposition recommendation, actual reviewer decision, and the evidence of authorization. Use `NOT REVIEWED` when that evidence is absent. A polished document does not demonstrate approval.

A text-only fallback keeps these same fields and headings. Tables may be split across messages with repeated headers and row-range labels, but their combined population must reconcile. Never replace a full ledger with “selected examples” without explicitly changing and labeling the scope.
