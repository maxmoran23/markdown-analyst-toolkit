# Investigation review: output contract

## Required delivery set

Return a report, a workbook or its exact tables, and an optional offline dashboard. The report is the decision narrative; the workbook is the evidence and calculation ledger; the dashboard is a filtered view of the same records. No output may use a different population, threshold, finding ID, or total. Add an as-of timestamp and a visible `DRAFT — HUMAN REVIEW REQUIRED` status until signoff is recorded.

The common workbook tabs are **Summary, Dashboard, Findings, Evidence, Actions, QA**. Files 06–08 define their rendering and common schemas. The following domain tabs are additional and have immutable column order. A changed header is a contract change, not a cosmetic edit. Keep machine fields in snake_case, numbers numeric, identifiers text, and missing values as empty spreadsheet cells / JSON `null` / Markdown `null`, accompanied by a reason in the designated status or rationale field. Zero means measured zero.

## Fixed report headings

1. Decision questions and current assessment
2. Scope, chronology method, and coverage
3. Findings and contradictions
4. Chronology and funds movement
5. Competing hypothesis tests
6. Evidence inventory and provenance
7. Proposed investigative actions
8. Limitations, quality checks, and reviewer decision

Every material finding needs its stable ID, condition, criterion, evidence, impact, severity rationale, confidence rationale, counterevidence, recommended next step, and human-decision status. Claim class must be one of `Observed`, `Reported`, `Inferred`, `Estimated`. Severity uses `HIGH`, `MEDIUM`, `LOW`; confidence uses `HIGH`, `MODERATE`, `LOW`, `NOT ASSESSABLE`. Confidence is not a probability unless a separately justified probabilistic method is supplied. High-impact uncertainty can have HIGH severity and LOW confidence.

## Domain tables

### CaseTimeline

Exact header:

```text
event_id | event_time | event_type | amount | currency | evidence_id | claim_class | detail
```

### HypothesisTests

Exact header:

```text
hypothesis_id | hypothesis | supporting_evidence | conflicting_evidence | missing_evidence | assessment | confidence | next_step
```

| Field | Type and handling |
| --- | --- |
| event_id, evidence_id, hypothesis_id | Required text identifiers; each must resolve. |
| event_time | ISO-8601 timestamp with offset when exact; a declared date/interval when not exact. Human displays use 12-hour timezone notation. |
| event_type | PROFILE, CREDIT, DEBIT, EXPLANATION, DOCUMENT, RETURN; additional declared types require a schema-version note. |
| amount | Decimal only for actual monetary event rows; null for profile, explanation, and document rows. Invoice face amount belongs in detail, not transaction amount. |
| currency | ISO code for monetary rows; null for nonmonetary events. |
| claim_class | Observed, Reported, Inferred, Estimated; applies to the row's proposition. |
| detail | Bounded description with no unstated causal claim. |
| hypothesis | One falsifiable proposition. |
| supporting_evidence, conflicting_evidence | Semicolon-delimited IDs; use explicit “none located within scope” in narrative when a list is empty. |
| missing_evidence | Specific required evidence or “None for [bounded proposition]”. |
| assessment | SUPPORTED, PATTERN_SUPPORTED, UNRESOLVED, CONTRADICTED. |
| confidence | HIGH, MODERATE, LOW, NOT ASSESSABLE. |
| next_step | Proposed inquiry or recording action; not an executed action. |

CaseTimeline contains one canonical event per row. HypothesisTests contains one proposition per row. Narrative must separately state gross flow, linked return, net unreversed value, alleged loss, and confirmed loss; mark the latter two unknown if not supported. Include a contradiction register in findings or report text with both evidence sides and the effect on the decision. Never add invoice face values to payment totals.

## Common-table content rules

Summary must contain scope and as-of details, input and exclusion counts, principal metrics with numerator/denominator and units, analytical status, and limitations. Findings contain one row per finding, with evidence IDs that resolve to Evidence. Evidence includes exact locator, source identity, date, claim class, availability, and limitations. Actions distinguish proposed, approved, executed, and verified; no synthetic example has an executed external action. QA records each check, expected result, actual result, pass/fail/not-tested status, and reviewer.

Narrative totals must cite the calculation or table row. Round only display values; calculate from original precision. Display percentages to one decimal and currency to two decimals with the ISO currency stated. Do not convert currency implicitly. Show timezone with human-facing timestamps. Preserve nulls in charts as gaps, never zero-height bars. Filters must expose how many rows are hidden and must not silently relabel filtered results as the full population.

## Required limitations and release block

State input coverage, missing data, attribution uncertainty, criterion provenance, tools not available, and tests not performed. Describe how each affects the supported decision. A generic disclaimer cannot substitute for a known defect. Record analyst, independent reviewer if any, review date, open issues, disposition recommendation, actual reviewer decision, and the evidence of authorization. Use `NOT REVIEWED` when that evidence is absent. A polished document does not demonstrate approval.

A text-only fallback keeps these same fields and headings. Tables may be split across messages with repeated headers and row-range labels, but their combined population must reconcile. Never replace a full ledger with “selected examples” without explicitly changing and labeling the scope.
