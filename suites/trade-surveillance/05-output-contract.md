# Trade surveillance: output contract

## Required delivery set

Return a report, a workbook or its exact tables, and an optional offline dashboard. The report is the decision narrative; the workbook is the evidence and calculation ledger; the dashboard is a filtered view of the same records. No output may use a different population, threshold, finding ID, or total. Add an as-of timestamp and a visible `DRAFT — HUMAN REVIEW REQUIRED` status until signoff is recorded.

The common workbook tabs are **Summary, Dashboard, Findings, Evidence, Actions, QA**. Files 06–08 define their rendering and common schemas. The following domain tabs are additional and have immutable column order. A changed header is a contract change, not a cosmetic edit. Keep machine fields in snake_case, numbers numeric, identifiers text, and missing values as empty spreadsheet cells / JSON `null` / Markdown `null`, accompanied by a reason in the designated status or rationale field. Zero means measured zero.

## Fixed report headings

1. Surveillance leads and review priorities
2. Scope, sequence reconstruction, and benchmarks
3. Findings and alternative explanations
4. Order lifecycle reconciliation
5. Scenario observations and denominator checks
6. Evidence and rule applicability
7. Proposed surveillance-review actions
8. Limitations, negative controls, and human decision

Every material finding needs its stable ID, condition, criterion, evidence, impact, severity rationale, confidence rationale, counterevidence, recommended next step, and human-decision status. Claim class must be one of `Observed`, `Reported`, `Inferred`, `Estimated`. Severity uses `HIGH`, `MEDIUM`, `LOW`; confidence uses `HIGH`, `MODERATE`, `LOW`, `NOT ASSESSABLE`. Confidence is not a probability unless a separately justified probabilistic method is supplied. High-impact uncertainty can have HIGH severity and LOW confidence.

## Domain tables

### OrderLifecycle

Exact header:

```text
order_id | group_id | instrument_id | side | new_quantity | filled_quantity | cancelled_quantity | remaining_quantity | lifetime_ms | cancel_quantity_ratio | evidence_ids
```

### SurveillanceObservations

Exact header:

```text
observation_id | group_id | scenario_id | state | measured_value | unit | criterion | review_priority | confidence | evidence_ids
```

| Field | Type, unit, and null handling |
| --- | --- |
| order_id, group_id, instrument_id, observation_id, scenario_id | Required stable text IDs; group mapping requires dated evidence. |
| side | BUY or SELL. |
| new_quantity, filled_quantity, cancelled_quantity, remaining_quantity | Nonnegative quantities in instrument units; integer shares in the example. Do not combine unlike instrument units. |
| lifetime_ms | Decimal milliseconds from acceptance to effective final state; null if not measurable. Open order age is not final lifetime. |
| cancel_quantity_ratio | Fraction cancelled/new, numeric; null for invalid/unknown denominator. Display one decimal percent. |
| evidence_ids | Semicolon-delimited IDs resolving to Evidence. |
| state | MATCH, NO_MATCH, NOT_ASSESSABLE, DATA_DEFECT. |
| measured_value | Numeric with unit; null when a required event is absent or unknown. State distinguishes a complete negative from missing data. |
| unit | milliseconds, simultaneous_price_levels, unique_executed_shares, or another explicitly declared unit. |
| criterion | Text with exact operators, timing, and eligibility. |
| review_priority | HIGH, MEDIUM, LOW. |
| confidence | HIGH, MODERATE, LOW, NOT ASSESSABLE. |

OrderLifecycle is one effective order lifecycle per row, with replace-chain semantics stated. SurveillanceObservations is one planned group-scenario test per row. Include raw message reconciliation and benchmark dictionary in the report or Evidence. Narrative must distinguish order count, event-message count, fill legs, unique executions, quantity, notional, and market-volume denominator. Every price-effect or participation measure names its window, instrument, source, and counting convention. Do not display a screen match as a legal verdict.

## Common-table content rules

Summary must contain scope and as-of details, input and exclusion counts, principal metrics with numerator/denominator and units, analytical status, and limitations. Findings contain one row per finding, with evidence IDs that resolve to Evidence. Evidence includes exact locator, source identity, date, claim class, availability, and limitations. Actions distinguish proposed, approved, executed, and verified; no synthetic example has an executed external action. QA records each check, expected result, actual result, pass/fail/not-tested status, and reviewer.

Narrative totals must cite the calculation or table row. Round only display values; calculate from original precision. Display percentages to one decimal and currency to two decimals with the ISO currency stated. Do not convert currency implicitly. Show timezone with human-facing timestamps. Preserve nulls in charts as gaps, never zero-height bars. Filters must expose how many rows are hidden and must not silently relabel filtered results as the full population.

## Required limitations and release block

State input coverage, missing data, attribution uncertainty, criterion provenance, tools not available, and tests not performed. Describe how each affects the supported decision. A generic disclaimer cannot substitute for a known defect. Record analyst, independent reviewer if any, review date, open issues, disposition recommendation, actual reviewer decision, and the evidence of authorization. Use `NOT REVIEWED` when that evidence is absent. A polished document does not demonstrate approval.

A text-only fallback keeps these same fields and headings. Tables may be split across messages with repeated headers and row-range labels, but their combined population must reconcile. Never replace a full ledger with “selected examples” without explicitly changing and labeling the scope.
