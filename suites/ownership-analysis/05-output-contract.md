# Ownership Analysis — output contract

## Report sections in exact order

1. Ownership decision brief
2. Scope and graph method
3. Material findings
4. Direct ownership assessment
5. Ultimate interests and unresolved branches
6. Evidence record
7. Recommended ownership review actions
8. Limitations and human review

## Shared representation rules

The report, workbook, and dashboard are three views of the same findings. Preserve the common Summary, Dashboard, Findings, Evidence, Actions, and QA tabs specified in 07 and add the two domain tables below. Column names are exact and case-sensitive. Do not add attractive but undefined scores, trend lines, probability badges, or numeric severity averages. Text fields may wrap; IDs must remain intact.

Dates use ISO YYYY-MM-DD in data tables and readable dates in prose. Times include timezone. Percentages are stored as percentage points from 0 to 100 in domain tables and displayed with a percent sign; do not accidentally apply a spreadsheet percent format that multiplies them again. Report currency with currency code and full amount; never sum unlike currencies without a stated conversion method and dated rate. Counts are integers. Rates with a zero denominator are NOT ASSESSABLE, not zero percent.

Enumerations: severity is HIGH, MEDIUM, LOW; confidence is HIGH, MODERATE, LOW, NOT ASSESSABLE; claim_class is Observed, Reported, Inferred, Estimated. Human disposition remains PENDING until a real reviewer supplies it. Finding evidence_ids are semicolon-separated stable IDs. Distinguish a finding recommendation from a disposition and preserve both if the human decision differs.

Use empty numeric cells for unavailable values and put UNKNOWN plus the reason in the note field. Never place a numeric-looking dash or fabricated zero in a missing cell. Text UNKNOWN is acceptable in text columns. Show record counts and missing-value counts below every domain table. Aggregate only eligible records under an explicit rule; partial sums must say PARTIAL. Keep raw inputs separate from derived values within each table or evidence note.

The executive answer must state what can be concluded now, what remains unresolved, how much of the intended population was actually reviewed, and the next decision needed. Each finding needs a falsifiable statement, precise scope, source locator, claim class, confidence rationale, severity rationale, alternative explanation, and proposed next action. Unsupported allegations must not be written as facts. Charts are optional; the underlying table and method are mandatory.

## Domain table: OwnershipEdges

Exact columns: `edge_id, owner_id, owned_entity_id, interest_pct, interest_basis, effective_date, evidence_ids, notes`.

edge_id is unique text. owner_id and owned_entity_id refer to resolved nodes or explicitly unresolved pools. interest_pct is numeric percentage points 0 through 100, not a fraction; empty means unknown and requires a note. interest_basis identifies the rights and comparable denominator. effective_date is ISO date or UNKNOWN text when absent. evidence_ids links every edge to its source. notes state source status, share class, completion/proposal status, unresolved rights, and any superseded or conflicting record.

Group subtotals by owned entity, basis, class, and effective date. Do not total the whole edge table across different entities: a graph-wide percentage sum has no meaningful denominator. Direct and derived interests must remain in different tables. Duplicate evidence cannot create duplicate edges.

## Domain table: UltimateInterests

Exact columns: `ultimate_id, target_id, economic_interest_pct, path_ids, resolution_state, control_state, claim_class, evidence_ids, notes`.

ultimate_id identifies a known terminal holder or an explicit unresolved pool. target_id is the target of the calculation. economic_interest_pct is numeric percentage points or empty when the method is not applicable. path_ids lists ordered edge IDs, using `>` within a path and semicolons between paths. resolution_state is RESOLVED ON SUPPLIED GRAPH, UNRESOLVED, CONFLICTING, or NOT CALCULABLE. RESOLVED ON SUPPLIED GRAPH does not mean independently verified in the world.

control_state is NOT ASSESSED, REPORTED RIGHTS, EVIDENCED RIGHTS, or SPECIALIST INTERPRETATION REQUIRED. EVIDENCED RIGHTS means the relevant rights record was reviewed; it does not itself decide a legal control definition. claim_class follows the shared enumeration. notes must include the formula, assumptions, source status, overlap treatment, and relevant rights limitations. An unresolved pool is not an identified ultimate owner.

## Narrative and display requirements

Show the effective graph date, comparable basis, direct reconciliation, path arithmetic, resolved/unresolved totals, control-rights discussion, and legal overlays not performed. Any sanctions illustration belongs in a distinctly labeled scenario with its own result; never relabel economic_interest_pct as blocked ownership. A dashboard may filter by holder or issue state but must retain all source rows in the workbook and keep the full-population denominator visible.
