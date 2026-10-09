# Entity Due Diligence — output contract

## Report sections in exact order

1. Entity decision brief
2. Scope and review method
3. Material findings
4. Ownership assessment
5. Profile and evidence gaps
6. Evidence record
7. Recommended diligence actions
8. Limitations and human review

## Shared representation rules

The report, workbook, and dashboard are three views of the same findings. Preserve the common Summary, Dashboard, Findings, Evidence, Actions, and QA tabs specified in 07 and add the two domain tables below. Column names are exact and case-sensitive. Do not add attractive but undefined scores, trend lines, probability badges, or numeric severity averages. Text fields may wrap; IDs must remain intact.

Dates use ISO YYYY-MM-DD in data tables and readable dates in prose. Times include timezone. Percentages are stored as percentage points from 0 to 100 in domain tables and displayed with a percent sign; do not accidentally apply a spreadsheet percent format that multiplies them again. Report currency with currency code and full amount; never sum unlike currencies without a stated conversion method and dated rate. Counts are integers. Rates with a zero denominator are NOT ASSESSABLE, not zero percent.

Enumerations: severity is HIGH, MEDIUM, LOW; confidence is HIGH, MODERATE, LOW, NOT ASSESSABLE; claim_class is Observed, Reported, Inferred, Estimated. Human disposition remains PENDING until a real reviewer supplies it. Finding evidence_ids are semicolon-separated stable IDs. Distinguish a finding recommendation from a disposition and preserve both if the human decision differs.

Use empty numeric cells for unavailable values and put UNKNOWN plus the reason in the note field. Never place a numeric-looking dash or fabricated zero in a missing cell. Text UNKNOWN is acceptable in text columns. Show record counts and missing-value counts below every domain table. Aggregate only eligible records under an explicit rule; partial sums must say PARTIAL. Keep raw inputs separate from derived values within each table or evidence note.

The executive answer must state what can be concluded now, what remains unresolved, how much of the intended population was actually reviewed, and the next decision needed. Each finding needs a falsifiable statement, precise scope, source locator, claim class, confidence rationale, severity rationale, alternative explanation, and proposed next action. Unsupported allegations must not be written as facts. Charts are optional; the underlying table and method are mandatory.

## Domain table: Ownership

Exact columns: `edge_id, owner_id, owned_entity_id, interest_pct, interest_basis, effective_date, source_status, evidence_ids, notes`.

edge_id is unique text. owner_id and owned_entity_id are stable internal IDs linked to the identity record. interest_pct is numeric percentage points from 0 through 100; unknown is empty, not zero. interest_basis must identify ordinary economic equity, voting rights, profit rights, or other clearly described basis. effective_date is the date of the represented holding. source_status is VERIFIED RECORD, REPORTED, UNKNOWN, or CONFLICTING; VERIFIED RECORD means the record was verified as the relevant record, not that every underlying representation was independently proved. notes identify share class, source locator, limitations, and residual treatment.

For each owned entity and comparable basis/date, display subtotal, unresolved residual, and reconciliation status. A synthetic UNKNOWN-POOL row represents a known residual amount with unknown underlying holders. It must not be treated as an identified person. Show derived ultimate interests in the report alongside the complete path and formula; do not add derived edges to the direct-edge table and then double-count them.

## Domain table: ProfileGaps

Exact columns: `item_id, dimension, expected_evidence, observed_state, materiality, assessment, evidence_ids, next_step`.

item_id is unique text. dimension identifies the factual question. expected_evidence names what would resolve it. observed_state is a concise evidence-backed description. materiality is HIGH, MEDIUM, or LOW for the intended decision. assessment is SUPPORTED, REPORTED, INCOMPLETE, UNRESOLVED, NOT ASSESSED, or NOT APPLICABLE. next_step specifies the exact request, not “perform more diligence.” A supported row remains in the table so the reviewed population is visible.

## Required interpretation

Ownership assessment must separately discuss identity resolution, economic interests, control, unresolved branches, and applicable legal questions. Profile assessment must include business model, permissions, material adverse information, and evidence gaps even when a section is NOT ASSESSED. Show known and unknown counts without assigning favorable scores to unknowns. The report must not call the entity approved, compliant, safe, or fully verified on the basis of this public-source review.
