# Digital Asset Review — output contract

## Report sections in exact order

1. Digital asset review brief
2. Scope and ledger method
3. Material findings
4. Event reconciliation
5. Counterparty and attribution assessment
6. Evidence record
7. Recommended review actions
8. Limitations and human review

## Shared representation rules

The report, workbook, and dashboard are three views of the same findings. Preserve the common Summary, Dashboard, Findings, Evidence, Actions, and QA tabs specified in 07 and add the two domain tables below. Column names are exact and case-sensitive. Do not add attractive but undefined scores, trend lines, probability badges, or numeric severity averages. Text fields may wrap; IDs must remain intact.

Dates use ISO YYYY-MM-DD in data tables and readable dates in prose. Times include timezone. Percentages are stored as percentage points from 0 to 100 in domain tables and displayed with a percent sign; do not accidentally apply a spreadsheet percent format that multiplies them again. Report currency with currency code and full amount; never sum unlike currencies without a stated conversion method and dated rate. Counts are integers. Rates with a zero denominator are NOT ASSESSABLE, not zero percent.

Enumerations: severity is HIGH, MEDIUM, LOW; confidence is HIGH, MODERATE, LOW, NOT ASSESSABLE; claim_class is Observed, Reported, Inferred, Estimated. Human disposition remains PENDING until a real reviewer supplies it. Finding evidence_ids are semicolon-separated stable IDs. Distinguish a finding recommendation from a disposition and preserve both if the human decision differs.

Use empty numeric cells for unavailable values and put UNKNOWN plus the reason in the note field. Never place a numeric-looking dash or fabricated zero in a missing cell. Text UNKNOWN is acceptable in text columns. Show record counts and missing-value counts below every domain table. Aggregate only eligible records under an explicit rule; partial sums must say PARTIAL. Keep raw inputs separate from derived values within each table or evidence note.

The executive answer must state what can be concluded now, what remains unresolved, how much of the intended population was actually reviewed, and the next decision needed. Each finding needs a falsifiable statement, precise scope, source locator, claim class, confidence rationale, severity rationale, alternative explanation, and proposed next action. Unsupported allegations must not be written as facts. Charts are optional; the underlying table and method are mandatory.

## Domain table: LedgerEvents

Exact columns: `event_id, chain_id, tx_id, event_index, asset_id, raw_amount, decimals, display_units, direction, execution_state, included, evidence_ids, notes`.

event_id is a unique text row ID. chain_id, tx_id, and asset_id are text identifiers, never abbreviated in exported data. event_index is a nonnegative integer or empty when inapplicable/unavailable; explain absence in notes. raw_amount is an exact nonnegative integer string stored as text. decimals is a nonnegative integer supported by metadata; empty means unknown. display_units is an exact decimal string or empty if scale is unknown. Do not force long values into imprecise numeric spreadsheet cells.

direction is IN, OUT, SELF, or OTHER. execution_state is SUCCESS, FAILED, PENDING, or UNKNOWN. included is Boolean and means eligible for the settled-event population; SELF can be included in event counts while excluded from directional amounts. notes must explain every exclusion, duplicate lineage, event-type distinction, missing index, and source limitation. A failed attempt can show its requested amount, but notes must say it is not a successful event amount.

## Domain table: Counterparties

Exact columns: `counterparty_id, asset_id, in_units, out_units, self_units, eligible_event_count, attribution_state, evidence_ids, notes`.

counterparty_id is the exact address or stable pseudonymous ID within the stated network. Each asset gets its own row. in_units, out_units, and self_units are exact decimal strings under the same scale as the source events. Unknown is blank with a note; zero is legitimate only when the included capture contains none in that direction. eligible_event_count is a nonnegative integer. attribution_state is UNATTRIBUTED, UNVERIFIED LABEL, CORROBORATED CLAIM, or SELF ADDRESS. CORROBORATED CLAIM still needs scope, evidence, and confidence in notes; it is not a universal identity guarantee.

## Required metrics and report details

Show raw rows, confirmed duplicates, unique events, included events, excluded/unknown events, and per-asset directional and self totals. Distinguish captured net flow from balance. Identify the exact capture window and missing event types. The counterparty section must separately discuss ledger facts and labels. Graphs may illustrate connections but cannot silently introduce identity clusters or multi-hop attribution. Never display rounded headline values without access to the exact quantities and units.
