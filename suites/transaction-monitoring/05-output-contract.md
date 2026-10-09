# Transaction monitoring: output contract

## Required delivery set

Return a report, a workbook or its exact tables, and an optional offline dashboard. The report is the decision narrative; the workbook is the evidence and calculation ledger; the dashboard is a filtered view of the same records. No output may use a different population, threshold, finding ID, or total. Add an as-of timestamp and a visible `DRAFT — HUMAN REVIEW REQUIRED` status until signoff is recorded.

The common workbook tabs are **Summary, Dashboard, Findings, Evidence, Actions, QA**. Files 06–08 define their rendering and common schemas. The following domain tabs are additional and have immutable column order. A changed header is a contract change, not a cosmetic edit. Keep machine fields in snake_case, numbers numeric, identifiers text, and missing values as empty spreadsheet cells / JSON `null` / Markdown `null`, accompanied by a reason in the designated status or rationale field. Zero means measured zero.

## Fixed report headings

1. Review priorities and known movement
2. Scope, population, and scenario method
3. Findings and benign explanations
4. Account flow calculations
5. Scenario matches and review outcomes
6. Evidence and criterion provenance
7. Proposed review and data-repair actions
8. Limitations, quality checks, and human decision

Every material finding needs its stable ID, condition, criterion, evidence, impact, severity rationale, confidence rationale, counterevidence, recommended next step, and human-decision status. Claim class must be one of `Observed`, `Reported`, `Inferred`, `Estimated`. Severity uses `HIGH`, `MEDIUM`, `LOW`; confidence uses `HIGH`, `MODERATE`, `LOW`, `NOT ASSESSABLE`. Confidence is not a probability unless a separately justified probabilistic method is supplied. High-impact uncertainty can have HIGH severity and LOW confidence.

## Domain tables

### AccountFlows

Exact header:

```text
account_id | currency | processed_tx_count | credit_total | debit_total | eligible_credit_total | eligible_debit_total | out_in_ratio | population_status
```

### ScenarioResults

Exact header:

```text
scenario_result_id | account_id | scenario_id | eligible | rule_result | first_credit_to_debit_hours | review_outcome | evidence_ids
```

| Field group | Type / units / null rule |
| --- | --- |
| account_id, scenario_result_id, scenario_id, currency | Text; never inferred from row order. IDs required. Currency ISO code. |
| processed_tx_count | Nonnegative integer; counts canonical known transactions. |
| credit_total, debit_total, eligible_credit_total, eligible_debit_total | Decimal in row currency; known amounts only. Partial populations require explicit population_status. |
| out_in_ratio | Decimal ratio, not percent points. Null for zero eligible credits or invalid denominator. |
| population_status | COMPLETE, OWN_TRANSFER_EXCLUDED, UNPARSED_AMOUNT, or a documented specific coverage defect. |
| eligible | Boolean; false covers scenario exclusion or blocked assessment, distinguished by rule_result. |
| rule_result | MATCH, NO_MATCH, EXCLUDED, NOT_ASSESSABLE. |
| first_credit_to_debit_hours | Decimal hours; null if no qualifying ordered pair or timing unavailable. |
| review_outcome | ESCALATE_FOR_REVIEW, EXPLANATION_SUPPORTED, OWN_TRANSFER_CONFIRMED, DATA_REPAIR_REQUIRED, OPEN_QUESTION, NO_MATCH_RECORDED. |
| evidence_ids | Semicolon-delimited stable IDs, all resolved in Evidence. |

Use one AccountFlows row per account/currency and one ScenarioResults row per account/scenario/window. The worked example has one window. A multiwindow run adds the window identifier to IDs and records boundaries in Evidence; do not combine windows invisibly. State that ratio is a screen for temporal co-occurrence and does not establish tracing. Narrative must distinguish known gross movement, unique monetary legs, potential suspicious amount if separately supported, and loss; they are not interchangeable. Report raw matches and reviewed outcomes as separate totals.

## Common-table content rules

Summary must contain scope and as-of details, input and exclusion counts, principal metrics with numerator/denominator and units, analytical status, and limitations. Findings contain one row per finding, with evidence IDs that resolve to Evidence. Evidence includes exact locator, source identity, date, claim class, availability, and limitations. Actions distinguish proposed, approved, executed, and verified; no synthetic example has an executed external action. QA records each check, expected result, actual result, pass/fail/not-tested status, and reviewer.

Narrative totals must cite the calculation or table row. Round only display values; calculate from original precision. Display percentages to one decimal and currency to two decimals with the ISO currency stated. Do not convert currency implicitly. Show timezone with human-facing timestamps. Preserve nulls in charts as gaps, never zero-height bars. Filters must expose how many rows are hidden and must not silently relabel filtered results as the full population.

## Required limitations and release block

State input coverage, missing data, attribution uncertainty, criterion provenance, tools not available, and tests not performed. Describe how each affects the supported decision. A generic disclaimer cannot substitute for a known defect. Record analyst, independent reviewer if any, review date, open issues, disposition recommendation, actual reviewer decision, and the evidence of authorization. Use `NOT REVIEWED` when that evidence is absent. A polished document does not demonstrate approval.

A text-only fallback keeps these same fields and headings. Tables may be split across messages with repeated headers and row-range labels, but their combined population must reconcile. Never replace a full ledger with “selected examples” without explicitly changing and labeling the scope.
