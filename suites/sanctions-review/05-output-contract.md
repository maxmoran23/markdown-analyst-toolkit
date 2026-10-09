# Sanctions Review — output contract

## Report sections in exact order

1. Sanctions review brief
2. Scope and applicable authority
3. Material findings
4. Ownership propagation assessment
5. Identity and nexus assessment
6. Evidence record
7. Recommended review actions
8. Limitations and human disposition

## Shared representation rules

The report, workbook, and dashboard are three views of the same findings. Preserve the common Summary, Dashboard, Findings, Evidence, Actions, and QA tabs specified in 07 and add the two domain tables below. Column names are exact and case-sensitive. Do not add attractive but undefined scores, trend lines, probability badges, or numeric severity averages. Text fields may wrap; IDs must remain intact.

Dates use ISO YYYY-MM-DD in data tables and readable dates in prose. Times include timezone. Percentages are stored as percentage points from 0 to 100 in domain tables and displayed with a percent sign; do not accidentally apply a spreadsheet percent format that multiplies them again. Report currency with currency code and full amount; never sum unlike currencies without a stated conversion method and dated rate. Counts are integers. Rates with a zero denominator are NOT ASSESSABLE, not zero percent.

Enumerations: severity is HIGH, MEDIUM, LOW; confidence is HIGH, MODERATE, LOW, NOT ASSESSABLE; claim_class is Observed, Reported, Inferred, Estimated. Human disposition remains PENDING until a real reviewer supplies it. Finding evidence_ids are semicolon-separated stable IDs. Distinguish a finding recommendation from a disposition and preserve both if the human decision differs.

Use empty numeric cells for unavailable values and put UNKNOWN plus the reason in the note field. Never place a numeric-looking dash or fabricated zero in a missing cell. Text UNKNOWN is acceptable in text columns. Show record counts and missing-value counts below every domain table. Aggregate only eligible records under an explicit rule; partial sums must say PARTIAL. Keep raw inputs separate from derived values within each table or evidence note.

The executive answer must state what can be concluded now, what remains unresolved, how much of the intended population was actually reviewed, and the next decision needed. Each finding needs a falsifiable statement, precise scope, source locator, claim class, confidence rationale, severity rationale, alternative explanation, and proposed next action. Unsupported allegations must not be written as facts. Charts are optional; the underlying table and method are mandatory.

## Domain table: OwnershipEdges

Exact columns: `edge_id, owner_id, owned_entity_id, interest_pct, basis, effective_date, evidence_ids, notes`.

edge_id is unique text; owner_id and owned_entity_id map to identity records. interest_pct is percentage points 0 through 100 and refers to the direct holding only. basis identifies the comparable ownership class or explains the rights. effective_date records the represented snapshot. notes must flag unsupported assumptions, disputed rights, range bounds, unknown residuals, and any inability to reconcile. Missing percentages are blank with UNKNOWN in notes. Do not populate them using a guessed equal division.

## Domain table: ReviewDecisions

Exact columns: `subject_id, identity_state, authority_scope, known_blocked_pct, ownership_result, other_nexus, review_state, evidence_ids, rationale`.

subject_id is unique per scoped decision; use a compound ID when different jurisdictions require separate rows. identity_state is SUPPORTED MATCH, SUPPORTED NONMATCH, UNRESOLVED, or RESOLVED IN FIXTURE. authority_scope names the actual authority and bounded question. known_blocked_pct is a derived numeric percentage-point sum of distinct direct stakes held by established blocked holders in the scoped illustration; it is not ultimate economic ownership. It is blank when the applicable test or comparable graph is unavailable.

ownership_result is THRESHOLD MET, THRESHOLD NOT MET ON SUPPLIED FACTS, INDETERMINATE, or NOT ASSESSED. other_nexus must explicitly say NOT ASSESSED or summarize each assessed nexus with its evidence. review_state is HUMAN REVIEW REQUIRED, EVIDENCE REQUIRED, or HUMAN DISPOSITION RECORDED. rationale must list contributing edge IDs, rule source, pass sequence, critical assumptions, and unresolved questions.

## Required report details

Include a dated rule record, identity comparison, propagation trace, other-nexus inventory, authorization assessment, and unresolved evidence request. Show counts of subjects by ownership_result without calling them clear or blocked operationally. If a human decision is later supplied, record its exact scope and evidence version in Actions; do not overwrite the analytical history. The dashboard must use the same neutral labels and may not turn THRESHOLD NOT MET into a green “cleared” badge.
