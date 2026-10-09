# OSINT Research — output contract

## Report sections in exact order

1. Research decision brief
2. Scope and coverage method
3. Material findings
4. Claim assessment
5. Search coverage and contradictions
6. Evidence record
7. Recommended research actions
8. Limitations and human review

## Shared representation rules

The report, workbook, and dashboard are three views of the same findings. Preserve the common Summary, Dashboard, Findings, Evidence, Actions, and QA tabs specified in 07 and add the two domain tables below. Column names are exact and case-sensitive. Do not add attractive but undefined scores, trend lines, probability badges, or numeric severity averages. Text fields may wrap; IDs must remain intact.

Dates use ISO YYYY-MM-DD in data tables and readable dates in prose. Times include timezone. Percentages are stored as percentage points from 0 to 100 in domain tables and displayed with a percent sign; do not accidentally apply a spreadsheet percent format that multiplies them again. Report currency with currency code and full amount; never sum unlike currencies without a stated conversion method and dated rate. Counts are integers. Rates with a zero denominator are NOT ASSESSABLE, not zero percent.

Enumerations: severity is HIGH, MEDIUM, LOW; confidence is HIGH, MODERATE, LOW, NOT ASSESSABLE; claim_class is Observed, Reported, Inferred, Estimated. Human disposition remains PENDING until a real reviewer supplies it. Finding evidence_ids are semicolon-separated stable IDs. Distinguish a finding recommendation from a disposition and preserve both if the human decision differs.

Use empty numeric cells for unavailable values and put UNKNOWN plus the reason in the note field. Never place a numeric-looking dash or fabricated zero in a missing cell. Text UNKNOWN is acceptable in text columns. Show record counts and missing-value counts below every domain table. Aggregate only eligible records under an explicit rule; partial sums must say PARTIAL. Keep raw inputs separate from derived values within each table or evidence note.

The executive answer must state what can be concluded now, what remains unresolved, how much of the intended population was actually reviewed, and the next decision needed. Each finding needs a falsifiable statement, precise scope, source locator, claim class, confidence rationale, severity rationale, alternative explanation, and proposed next action. Unsupported allegations must not be written as facts. Charts are optional; the underlying table and method are mandatory.

## Domain table: Claims

Exact columns: `claim_id, proposition, claim_class, status, confidence, support_families, contradiction_ids, evidence_ids, notes`.

claim_id is unique text. proposition is one falsifiable sentence. status is SUPPORTED, CONTRADICTED, UNRESOLVED, or IDENTITY UNRESOLVED. support_families is a nonnegative integer counting original upstream families that support the proposition, not all sources reviewed. contradiction_ids contains source-item IDs separated by semicolons; empty means no contradiction identified in reviewed material, not proof none exists. notes must explain confidence, relevant timing, and any incomplete coverage. Do not replace proposition with a vague topic label.

## Domain table: SearchCoverage

Exact columns: `query_id, question, source_family, scope, review_status, items_reviewed, eligible_items, evidence_ids, limitation`.

query_id is unique text. question links to a research question. source_family is the upstream family identifier. scope records date range, language, source subset, and query variants as applicable. review_status is REVIEWED, PARTIAL, ACCESS LIMITED, or NOT RUN. items_reviewed and eligible_items are nonnegative integers; eligible cannot exceed reviewed. Unknown counts are empty with a limitation explaining why. Different-subject items can be reviewed but ineligible. An access-limited row has zero reviewed only when no content was actually reviewed.

## Domain metrics and narrative minimums

Display material claims by assessment state, planned-search completion, source-item count, and unique-family count with their definitions. No “credibility score” is allowed. The chronology must distinguish event date, publication date, and access date. The contradictions section must retain the strongest opposing evidence even when the analyst prefers another source. The evidence record must say which references were actually reviewed in the session.
