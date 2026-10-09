# Typology and red flags: output contract

## Required delivery set

Return a report, a workbook or its exact tables, and an optional offline dashboard. The report is the decision narrative; the workbook is the evidence and calculation ledger; the dashboard is a filtered view of the same records. No output may use a different population, threshold, finding ID, or total. Add an as-of timestamp and a visible `DRAFT — HUMAN REVIEW REQUIRED` status until signoff is recorded.

The common workbook tabs are **Summary, Dashboard, Findings, Evidence, Actions, QA**. Files 06–08 define their rendering and common schemas. The following domain tabs are additional and have immutable column order. A changed header is a contract change, not a cosmetic edit. Keep machine fields in snake_case, numbers numeric, identifiers text, and missing values as empty spreadsheet cells / JSON `null` / Markdown `null`, accompanied by a reason in the designated status or rationale field. Zero means measured zero.

## Fixed report headings

1. Review priorities and indicator counts
2. Scope and indicator methodology
3. Findings and alternative explanations
4. Indicator observations
5. Competing hypotheses by case
6. Evidence and source applicability
7. Proposed inquiry actions
8. Limitations, quality checks, and human review

Every material finding needs its stable ID, condition, criterion, evidence, impact, severity rationale, confidence rationale, counterevidence, recommended next step, and human-decision status. Claim class must be one of `Observed`, `Reported`, `Inferred`, `Estimated`. Severity uses `HIGH`, `MEDIUM`, `LOW`; confidence uses `HIGH`, `MODERATE`, `LOW`, `NOT ASSESSABLE`. Confidence is not a probability unless a separately justified probabilistic method is supplied. High-impact uncertainty can have HIGH severity and LOW confidence.

## Domain tables

### IndicatorObservations

Exact header:

```text
observation_id | case_id | indicator_id | state | measured_value | unit | criterion | evidence_ids | interpretation
```

### HypothesisReview

Exact header:

```text
case_id | concern_hypothesis | benign_hypothesis | support_state | next_evidence | priority | confidence | proposed_outcome
```

| Column | Type, unit, and null behavior |
| --- | --- |
| observation_id, case_id, indicator_id | Required stable text identifiers. |
| state | PRESENT, ABSENT, INDETERMINATE, NOT_APPLICABLE. |
| measured_value | Decimal or integer with unit; null when no valid measure can be formed or the test does not apply. |
| unit | ratio, distinct_payers, distinct_payees, posted_events, or another explicitly declared unit. |
| criterion | Text giving exact operator, period, eligibility, and threshold. |
| evidence_ids | Semicolon-delimited references to original case evidence. |
| interpretation | One bounded statement that does not assert criminality. |
| concern_hypothesis, benign_hypothesis | Text; both specific to case facts, not stock disclaimers. |
| support_state | PATTERN_ONLY, BENIGN_SUPPORTED, PATTERN_NOT_MET, INSUFFICIENT_EVIDENCE. |
| next_evidence | Specific discriminating evidence, or a reason no additional inquiry is proposed for this indicator. |
| priority, confidence | Priority HIGH/MEDIUM/LOW; confidence HIGH/MODERATE/LOW/NOT ASSESSABLE. |
| proposed_outcome | FURTHER_REVIEW, DOCUMENT_LIMITED_EXCLUSION, OBTAIN_SOURCE, RECORD_NEGATIVE. |

IndicatorObservations uses one row per planned case-indicator test. HypothesisReview uses one row per case. Keep the test-plan count and case count separate. Narrative must identify correlated indicators, source-origin dependence, strongest counterevidence, and the claim that additional evidence could change. Count unknown observations explicitly in both workbook and dashboard; do not show them as an empty success category.

## Common-table content rules

Summary must contain scope and as-of details, input and exclusion counts, principal metrics with numerator/denominator and units, analytical status, and limitations. Findings contain one row per finding, with evidence IDs that resolve to Evidence. Evidence includes exact locator, source identity, date, claim class, availability, and limitations. Actions distinguish proposed, approved, executed, and verified; no synthetic example has an executed external action. QA records each check, expected result, actual result, pass/fail/not-tested status, and reviewer.

Narrative totals must cite the calculation or table row. Round only display values; calculate from original precision. Display percentages to one decimal and currency to two decimals with the ISO currency stated. Do not convert currency implicitly. Show timezone with human-facing timestamps. Preserve nulls in charts as gaps, never zero-height bars. Filters must expose how many rows are hidden and must not silently relabel filtered results as the full population.

## Required limitations and release block

State input coverage, missing data, attribution uncertainty, criterion provenance, tools not available, and tests not performed. Describe how each affects the supported decision. A generic disclaimer cannot substitute for a known defect. Record analyst, independent reviewer if any, review date, open issues, disposition recommendation, actual reviewer decision, and the evidence of authorization. Use `NOT REVIEWED` when that evidence is absent. A polished document does not demonstrate approval.

A text-only fallback keeps these same fields and headings. Tables may be split across messages with repeated headers and row-range labels, but their combined population must reconcile. Never replace a full ledger with “selected examples” without explicitly changing and labeling the scope.
