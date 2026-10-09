# Transaction Monitoring Scenario Design: fixed delivery contract

The report is the decision narrative, the workbook is the complete review ledger, and the optional offline dashboard is a view of exactly the same case record. All outputs must preserve the same source population, version, period, criteria, findings, unknowns and human-decision state. The common workbook sheets are Summary, Dashboard, Findings, Evidence, Actions and QA, followed by every domain table below in the declared order. Files 06–08 provide full renderers; their synthetic data must be replaced only with a complete reviewed case record.

Keep identifiers as text, monetary measures numeric in their declared currency, ratios numeric as proportions, and missing values as JSON null or empty spreadsheet cells with an accompanying reason. A string saying null is not a numeric null. A count of zero is permitted only for a complete or explicitly known subset. Never silently change a field name, append a unit to a numeric value, collapse evidence rows or truncate an exception register to fit a page. Use field/value records in a report when a wide table would become unreadable; the workbook retains every exact column.

## Fixed report headings and required coverage

1. **Proposed rule and acceptance decision** — Lead with the supported answer, raw outcome counts, unresolved gate and decision implication. Keep known monetary figures explicitly partial where required.
2. **Risk hypothesis, source scope and design boundary** — Identify the exact event period, ingestion cutoff if applicable, source inventory, criteria version, data grain, exclusion conventions and actual readable coverage.
3. **Design findings and unresolved decisions** — Retain each finding ID, claim class, severity rationale, confidence rationale, supporting evidence, competing explanation and proposed next action.
4. **Predicate and event specification** — Show the source and canonical calculation trail. Include every declared register assigned to this section and explain its grain before interpreting totals.
5. **Window outcomes, delivery and acceptance evidence** — Preserve all remaining domain registers, including blocked outcomes, overlaps, exceptions, review or delivery states and complete QA evidence.
6. **Evidence and authority provenance** — Include exact fictional source locators and public-source applicability limits; a method reference cannot stand in for transaction-specific evidence.
7. **Proposed design and data actions** — Separate proposed evidence requests or repairs from accepted, executed or verified actions. Leave absent owners, dates and approvals unprovided.
8. **Limitations, quality gates and human authorization** — State specific residual limitations, performed and unperformed tests, independent-review scope and actual human-disposition state.

## Table-level and field-level operating contracts

The following field cards are operational instructions for populating and reviewing the case, followed by machine-readable typed dictionaries maintained with the same schema. Each field card states the meaning and the corresponding verification behavior. These instructions are part of the runtime attachment; the reader does not need the repository or another suite to interpret a column.

### EventLedger: Full fictional rule acceptance source

**Grain:** one unique fictional source event within the complete declared 48-hour interval. **Primary key:** `event_id`. The base specimen contains 13 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
event_id | account_id | event_utc | direction | amount | currency | ownership_state | posting_state | evidence_ids
```

**`event_id`** — Immutable synthetic source-event identifier. It survives window expansion and may occur in several window membership lists without becoming another economic event. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `E01; E02`.

**`account_id`** — Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `J; K`.

**`event_utc`** — Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2026-09-01T13:00:00Z; 2026-09-01T14:00:00Z`.

**`direction`** — Canonical CREDIT or DEBIT from the account perspective. Amount remains nonnegative; do not infer direction from a signed display string. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `CREDIT; DEBIT`.

**`amount`** — Known nonnegative monetary amount in the row currency. Null means unrecovered source value and blocks the relevant completeness proposition. Type `number`; unit `row currency`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `3000; 2000`.

**`currency`** — Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `USD`.

**`ownership_state`** — Evidence-backed own/external classification for the specific leg and historical period. Unknown ownership is not automatically external or own. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `EXTERNAL; CONFIRMED_OWN`.

**`posting_state`** — Canonical posting status that determines whether a leg enters the declared posted population. A pending item remains visible outside that population. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `POSTED`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SD-E01; SD-E01;SD-E02`.

### PredicateSpec: Ordered deterministic rule predicates

**Grain:** one ordered predicate in RULE-SD-01-v1. **Primary key:** `predicate_id`. The base specimen contains 8 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
predicate_id | order | field_or_measure | operator | operand | null_result | purpose | evidence_ids
```

**`predicate_id`** — Unique predicate identifier within the versioned rule. Its declared order controls precedence for blocking defects, exclusions and numeric comparisons. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `P01; P02`.

**`order`** — Positive integer evaluation precedence. Numeric predicates cannot override an earlier relevant data-completeness failure. Type `integer`; unit `count`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `1; 2`.

**`field_or_measure`** — Exact input field or derived quantity being tested. A business phrase without a computable field mapping does not satisfy this contract. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `data coverage; posting_state`.

**`operator`** — Literal comparison or grouping operation. Inclusive, strict and interval comparisons are deliberately different and must remain explicit. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `EQUAL; INTERVAL`.

**`operand`** — Complete threshold, interval or category against which the predicate compares. Monetary values include currency and durations include elapsed units. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `COMPLETE; POSTED`.

**`null_result`** — Required branch when input cannot be evaluated. A null-sensitive predicate may block a window rather than defaulting to false or zero. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `NOT_ASSESSABLE; NO_MATCH_IF_ZERO_CREDITS`.

**`purpose`** — Bounded reason for the predicate and the mechanism it tests. This is an authored design rationale rather than a legal requirement. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Reject relevant missing amount, time, identity or uncovered interval; Pending and rejected legs never enter sums`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SD-E04`.

### WindowResults: Full anchored calculations and truth states

**Grain:** one account, eligible credit anchor, currency and rule version. **Primary key:** `window_id`. The base specimen contains 6 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
window_id | account_id | anchor_event_id | start_utc | end_utc | event_ids | credit_total | debit_total | ratio | first_debit_hours | coverage_state | rule_result | evidence_ids
```

Join `anchor_event_id` to `EventLedger.event_id` using exact text equality. Null is permitted only when the field contract allows it, with the row's reason explaining why no parent record exists.

**`window_id`** — Stable account/anchor/specification window key. It distinguishes overlapping observations so a membership count cannot be mistaken for unique transactions. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `WJ1; WJ2`.

**`account_id`** — Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `J; K`.

**`anchor_event_id`** — Source eligible credit that starts the specified closed 24-hour window. Same-account membership is explicit and independently reproducible. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `E01; E02`.

**`start_utc`** — Inclusive UTC instant at the anchor. The applicable window convention determines endpoint inclusion, not the date formatting of the rendered table. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2026-09-01T13:00:00Z; 2026-09-01T14:00:00Z`.

**`end_utc`** — UTC endpoint exactly 24 elapsed hours after the anchor. The scenario-design closed interval includes this instant; the TM diagnostic convention matches it. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2026-09-02T13:00:00Z; 2026-09-02T14:00:00Z`.

**`event_ids`** — Semicolon-delimited source-event membership in the specific window. Recompute the union separately before calculating unique population movement. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `E01;E02;E03; E02;E03`.

**`credit_total`** — Known eligible or gross credit subtotal as specified by the table grain. It is not necessarily a complete total when coverage_state or population_status is defective. Type `number`; unit `row currency`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `5000; 2000`.

**`debit_total`** — Known eligible debit subtotal at the table grain. Null is required for a window total dependent on an unknown debit; known subtotals elsewhere remain explicitly partial. Type `number`; unit `row currency`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `4500; 4499.99`.

**`ratio`** — Unrounded window debit-to-credit ratio. Null indicates a missing component or no positive denominator; comparisons occur before display rounding. Type `number`; unit `ratio`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `0.9; 2.25`.

**`first_debit_hours`** — Elapsed hours from anchor to first strictly subsequent eligible debit. Null means no qualifying ordered pair; a contemporaneous debit cannot satisfy the predicate. Type `number`; unit `hours`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2; 1`.

**`coverage_state`** — Completeness state for the exact account/window inputs. COMPLETE, BOUNDARY_INCOMPLETE and AMOUNT_UNKNOWN cannot be collapsed into a binary risk score. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `COMPLETE; AMOUNT_UNKNOWN`.

**`rule_result`** — Deterministic raw result under the named specification: MATCH, NO_MATCH, EXCLUDED or NOT_ASSESSABLE. Contextual evidence does not rewrite it. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `MATCH; NO_MATCH`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SD-E01;SD-E04; SD-E01;SD-E03;SD-E04`.

### DeliveryDecisions: Raw result retention and proposed delivery grouping

**Grain:** one proposed delivery disposition for a retained raw window result. **Primary key:** `delivery_id`. The base specimen contains 6 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
delivery_id | window_id | raw_result | delivery_state | group_id | reason | human_approval | evidence_ids
```

Join `window_id` to `WindowResults.window_id` using exact text equality. Null is permitted only when the field contract allows it, with the row's reason explaining why no parent record exists.

**`delivery_id`** — Unique proposal for a window delivery disposition. The record is separate from the raw match so grouping cannot hide a numerical result. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `DL-J1; DL-J2`.

**`window_id`** — Stable account/anchor/specification window key. It distinguishes overlapping observations so a membership count cannot be mistaken for unique transactions. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `WJ1; WJ2`.

**`raw_result`** — Preserved deterministic rule result before human review or delivery grouping. Explanations and grouping decisions must not delete or change it. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `MATCH; NO_MATCH`.

**`delivery_state`** — Proposed route for a raw outcome: review, no delivery or data repair. It describes the analytical queue decision without performing an external action. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `PROPOSED_FOR_REVIEW; NO_DELIVERY`.

**`group_id`** — Stable proposed delivery-group identifier. Null means the window produces no review group; grouping never erases the underlying result. Type `text`; unit `identifier`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `G-J1; null`.

**`reason`** — Specific evidence-backed reason for a state or transition. It identifies the relevant row, rule or missing fact rather than a generic compliance label. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `No earlier identical match; purpose unreviewed; Credit total below minimum despite ratio above one`.

**`human_approval`** — Evidence of authorized approval for a design or delivery treatment. NOT_RECORDED is not interchangeable with approved or presumed approved. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `NOT_RECORDED`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SD-E01;SD-E04; SD-E03;SD-E04`.

### AccountCoverage: One row for every source account including excluded accounts

**Grain:** one source account, including accounts that generate no external windows. **Primary key:** `account_id`. The base specimen contains 6 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
account_id | raw_events | known_credit_total | known_debit_total | external_anchor_count | window_count | coverage_outcome | evidence_ids
```

**`account_id`** — Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `J; K`.

**`raw_events`** — Count of source events for the account, including excluded and unknown-amount events. It reconciles the retained account frame to the source ledger. Type `integer`; unit `count`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `3; 2`.

**`known_credit_total`** — Sum of readable credits only at the declared stage, account or observed diagnostic window. The word known is substantive where an unresolved amount exists. Type `number`; unit `row currency`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `5000; 6000`.

**`known_debit_total`** — Sum of readable debits only at the declared stage, account or observed diagnostic window. An unknown debit is not imputed as a measured zero. Type `number`; unit `row currency`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `4500; 4499.99`.

**`external_anchor_count`** — Number of eligible external credit anchors generated for an account. Confirmed own transfers produce no external-flow anchors. Type `integer`; unit `count`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2; 1`.

**`window_count`** — Count of generated windows for the account, including blocked ones. It is not the count of delivered alerts or unique source legs. Type `integer`; unit `count`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2; 1`.

**`coverage_outcome`** — Account-level outcome that retains excluded and blocked accounts alongside assessed accounts. No-record output is not an acceptable substitute. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `ASSESSED; CONFIRMED_OWN_EXCLUDED`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SD-E01;SD-E04; SD-E01;SD-E02`.

### AcceptanceTests: Explicit specimen test expectations and observed arithmetic

**Grain:** one explicit deterministic expectation and its authored synthetic actual result. **Primary key:** `test_id`. The base specimen contains 7 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
test_id | test_name | expected | actual | result | affected_ids | evidence_ids
```

**`test_id`** — Unique deterministic acceptance-test key. Each test names the affected records and compares a specific expected result to a separately produced actual result. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `AT01; AT02`.

**`test_name`** — Specific acceptance proposition rather than a generic passed label. It names a boundary, count, state or authorization gate. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `All raw events retained; Raw matching windows`.

**`expected`** — Exact target result for the named check. This is fixed before execution and may state not supplied when the check concerns authorization. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `13; WJ1;WK1`.

**`actual`** — Recorded output of the check. In future sessions, use NOT TESTED until performed; do not copy the specimen result as evidence of a new execution. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `13; WJ1;WK1`.

**`result`** — Control result or acceptance state. PASS applies to an executed synthetic check; it is not regulatory assurance or an operational approval. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `PASS; NOT_RECORDED`.

**`affected_ids`** — Explicit source, window or specification keys involved in an acceptance test. Preserve their grain rather than treating every identifier as a transaction. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `E01-E13; WJ1;WK1`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SD-E01; SD-E01;SD-E04`.

### EvidenceProvenance: Source identity, period, availability and evidential limits

**Grain:** one fictional evidence source with its access state and evidential limit. **Primary key:** `evidence_id`. The base specimen contains 4 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
evidence_id | source_kind | source_date | availability | locator | supports | limitation
```

**`evidence_id`** — Exact unique Evidence key at one source-provenance row. It joins the common Evidence register without combining unrelated sources. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SD-E01; SD-E02`.

**`source_kind`** — Explicitly fictional record type and origin. Authored cases and guidance references must not be mislabeled as actual institutional evidence. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Authored fictional case record`.

**`source_date`** — ISO calendar date of the authored source package, distinct from transaction event dates and evidence retrieval dates. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2026-09-03`.

**`availability`** — State of access to the source text. FULL_TEXT_IN_FILE_10 means the complete fictional content is supplied in this suite, not externally verified. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `FULL_TEXT_IN_FILE_10`.

**`locator`** — Exact file and section or row reference supporting retrieval of the fictional source. A title alone is insufficient. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `10-worked-example.md, EventLedger E01-E13; coverage declaration; 10-worked-example.md, M ownership declaration`.

**`supports`** — Bounded proposition the source can establish in the synthetic exercise. It does not certify any broader customer or control conclusion. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Fictional complete 48-hour event ledger; Fictional common-ownership evidence`.

**`limitation`** — Specific scope restriction or evidential weakness that must accompany use of the source. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Supports only the stated fictional proposition; no external subject fact or institutional approval`.

### ProcessQA: Explicit expected and actual control evidence

**Grain:** one performed or explicitly unrecorded quality proposition. **Primary key:** `check_id`. The base specimen contains 5 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
check_id | check | expected | actual | status | reviewer | evidence_ids
```

**`check_id`** — Unique process-quality check key retained across output formats. A later rerun creates a dated actual result without changing the original expectation. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SQ01; SQ02`.

**`check`** — Falsifiable control proposition with defined expected evidence. It must be precise enough for another reviewer to reproduce. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Raw matches; Rounding cannot change decision`.

**`expected`** — Exact target result for the named check. This is fixed before execution and may state not supplied when the check concerns authorization. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `WJ1 and WK1; .899998 is NO_MATCH`.

**`actual`** — Recorded output of the check. In future sessions, use NOT TESTED until performed; do not copy the specimen result as evidence of a new execution. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `WJ1 and WK1; .899998 is NO_MATCH`.

**`status`** — Recorded PASS, FAIL, REVIEW REQUIRED, NOT RECORDED or NOT TESTED status for this check, separate from analytical finding severity. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `PASS; NOT RECORDED`.

**`reviewer`** — Identity or role of the actual check performer. The specimen labels authored arithmetic and explicitly records absent independent operational review. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Authored specimen arithmetic; independent operational reviewer not supplied`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SD-E01;SD-E04; SD-E03`.

## Narrative-to-data consistency and artifact limits

For every headline number, retain the measure, value, unit, formula, scope and limitation. A formatted dollar amount cannot hide a mixed-currency sum, and a percentage must identify its numerator and denominator. Reconcile report statements to the exact domain rows rather than to a chart label. Keep raw matches, proposed explanations, exclusions, blocked records and human dispositions separate; they overlap conceptually and cannot be added as if they were one terminal transaction partition.

EvidenceProvenance supplements the common Evidence sheet with source kind, date, availability, exact locator, supported proposition and limitation. ProcessQA supplements the common QA sheet with fixed expected and actual values and the actual reviewer basis. Do not reduce these registers to a single passed badge. Preserve NOT RECORDED for human authorization and REVIEW REQUIRED or NOT TESTED where appropriate. Completed synthetic arithmetic is not an independent operational assessment.

If an output cannot be created, deliver all exact headings and tables as copy-ready Markdown with an explicit format failure. Do not rename text as XLSX or claim a file exists without an openable artifact. Preserve the canonical case data so a later render can reproduce it without repeating or inventing analysis. Any changed source, parameter or conclusion requires a new reviewed case record and affected quality checks before new artifacts are accepted.

<!-- FIELD_CONTRACTS:START -->
## Compiled domain field dictionary

This dictionary is part of this attachment. It fixes the type, null rule, unit, permitted values and record identity used by the embedded renderers. It is generated from the same reviewed case contract; no external file is needed. Raw source defects must be retained as raw text under their declared type. Correcting a malformed value requires evidence, not coercion by the renderer.

### EventLedger — field contract

**Record grain:** one unique fictional source event within the complete declared 48-hour interval

**Primary key:** `event_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| event_id | text | no | identifier | Immutable synthetic source-event identifier. It survives window expansion and may occur in several window membership lists without becoming another economic event. | No additional enum or range constraint | Native value / literal text |
| account_id | text | no | identifier | Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. | No additional enum or range constraint | Native value / literal text |
| event_utc | text | no | text | Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant. | No additional enum or range constraint | Native value / literal text |
| direction | text | no | text | Canonical CREDIT or DEBIT from the account perspective. Amount remains nonnegative; do not infer direction from a signed display string. | No additional enum or range constraint | Native value / literal text |
| amount | number | yes | row currency | Known nonnegative monetary amount in the row currency. Null means unrecovered source value and blocks the relevant completeness proposition. | No additional enum or range constraint | #,##0.00 |
| currency | text | no | text | Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. | No additional enum or range constraint | Native value / literal text |
| ownership_state | text | no | text | Evidence-backed own/external classification for the specific leg and historical period. Unknown ownership is not automatically external or own. | No additional enum or range constraint | Native value / literal text |
| posting_state | text | no | text | Canonical posting status that determines whether a leg enters the declared posted population. A pending item remains visible outside that population. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### PredicateSpec — field contract

**Record grain:** one ordered predicate in RULE-SD-01-v1

**Primary key:** `predicate_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| predicate_id | text | no | identifier | Unique predicate identifier within the versioned rule. Its declared order controls precedence for blocking defects, exclusions and numeric comparisons. | No additional enum or range constraint | Native value / literal text |
| order | integer | no | count | Positive integer evaluation precedence. Numeric predicates cannot override an earlier relevant data-completeness failure. | No additional enum or range constraint | Native value / literal text |
| field_or_measure | text | no | text | Exact input field or derived quantity being tested. A business phrase without a computable field mapping does not satisfy this contract. | No additional enum or range constraint | Native value / literal text |
| operator | text | no | text | Literal comparison or grouping operation. Inclusive, strict and interval comparisons are deliberately different and must remain explicit. | No additional enum or range constraint | Native value / literal text |
| operand | text | no | text | Complete threshold, interval or category against which the predicate compares. Monetary values include currency and durations include elapsed units. | No additional enum or range constraint | Native value / literal text |
| null_result | text | no | text | Required branch when input cannot be evaluated. A null-sensitive predicate may block a window rather than defaulting to false or zero. | No additional enum or range constraint | Native value / literal text |
| purpose | text | no | text | Bounded reason for the predicate and the mechanism it tests. This is an authored design rationale rather than a legal requirement. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### WindowResults — field contract

**Record grain:** one account, eligible credit anchor, currency and rule version

**Primary key:** `window_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| window_id | text | no | identifier | Stable account/anchor/specification window key. It distinguishes overlapping observations so a membership count cannot be mistaken for unique transactions. | No additional enum or range constraint | Native value / literal text |
| account_id | text | no | identifier | Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. | No additional enum or range constraint | Native value / literal text |
| anchor_event_id | text | no | identifier | Source eligible credit that starts the specified closed 24-hour window. Same-account membership is explicit and independently reproducible. | No additional enum or range constraint | Native value / literal text |
| start_utc | text | no | text | Inclusive UTC instant at the anchor. The applicable window convention determines endpoint inclusion, not the date formatting of the rendered table. | No additional enum or range constraint | Native value / literal text |
| end_utc | text | no | text | UTC endpoint exactly 24 elapsed hours after the anchor. The scenario-design closed interval includes this instant; the TM diagnostic convention matches it. | No additional enum or range constraint | Native value / literal text |
| event_ids | text | no | text | Semicolon-delimited source-event membership in the specific window. Recompute the union separately before calculating unique population movement. | No additional enum or range constraint | Native value / literal text |
| credit_total | number | no | row currency | Known eligible or gross credit subtotal as specified by the table grain. It is not necessarily a complete total when coverage_state or population_status is defective. | No additional enum or range constraint | #,##0.00 |
| debit_total | number | yes | row currency | Known eligible debit subtotal at the table grain. Null is required for a window total dependent on an unknown debit; known subtotals elsewhere remain explicitly partial. | No additional enum or range constraint | #,##0.00 |
| ratio | number | yes | ratio | Unrounded window debit-to-credit ratio. Null indicates a missing component or no positive denominator; comparisons occur before display rounding. | No additional enum or range constraint | 0.000000 |
| first_debit_hours | number | yes | hours | Elapsed hours from anchor to first strictly subsequent eligible debit. Null means no qualifying ordered pair; a contemporaneous debit cannot satisfy the predicate. | No additional enum or range constraint | 0.0 |
| coverage_state | text | no | text | Completeness state for the exact account/window inputs. COMPLETE, BOUNDARY_INCOMPLETE and AMOUNT_UNKNOWN cannot be collapsed into a binary risk score. | No additional enum or range constraint | Native value / literal text |
| rule_result | text | no | text | Deterministic raw result under the named specification: MATCH, NO_MATCH, EXCLUDED or NOT_ASSESSABLE. Contextual evidence does not rewrite it. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Foreign key: `anchor_event_id` resolves to `EventLedger (event_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### DeliveryDecisions — field contract

**Record grain:** one proposed delivery disposition for a retained raw window result

**Primary key:** `delivery_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| delivery_id | text | no | identifier | Unique proposal for a window delivery disposition. The record is separate from the raw match so grouping cannot hide a numerical result. | No additional enum or range constraint | Native value / literal text |
| window_id | text | no | identifier | Stable account/anchor/specification window key. It distinguishes overlapping observations so a membership count cannot be mistaken for unique transactions. | No additional enum or range constraint | Native value / literal text |
| raw_result | text | no | text | Preserved deterministic rule result before human review or delivery grouping. Explanations and grouping decisions must not delete or change it. | No additional enum or range constraint | Native value / literal text |
| delivery_state | text | no | text | Proposed route for a raw outcome: review, no delivery or data repair. It describes the analytical queue decision without performing an external action. | No additional enum or range constraint | Native value / literal text |
| group_id | text | yes | identifier | Stable proposed delivery-group identifier. Null means the window produces no review group; grouping never erases the underlying result. | No additional enum or range constraint | Native value / literal text |
| reason | text | no | text | Specific evidence-backed reason for a state or transition. It identifies the relevant row, rule or missing fact rather than a generic compliance label. | No additional enum or range constraint | Native value / literal text |
| human_approval | text | no | text | Evidence of authorized approval for a design or delivery treatment. NOT_RECORDED is not interchangeable with approved or presumed approved. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Foreign key: `window_id` resolves to `WindowResults (window_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### AccountCoverage — field contract

**Record grain:** one source account, including accounts that generate no external windows

**Primary key:** `account_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| account_id | text | no | identifier | Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. | No additional enum or range constraint | Native value / literal text |
| raw_events | integer | no | count | Count of source events for the account, including excluded and unknown-amount events. It reconciles the retained account frame to the source ledger. | No additional enum or range constraint | Native value / literal text |
| known_credit_total | number | no | row currency | Sum of readable credits only at the declared stage, account or observed diagnostic window. The word known is substantive where an unresolved amount exists. | No additional enum or range constraint | #,##0.00 |
| known_debit_total | number | no | row currency | Sum of readable debits only at the declared stage, account or observed diagnostic window. An unknown debit is not imputed as a measured zero. | No additional enum or range constraint | #,##0.00 |
| external_anchor_count | integer | no | count | Number of eligible external credit anchors generated for an account. Confirmed own transfers produce no external-flow anchors. | No additional enum or range constraint | Native value / literal text |
| window_count | integer | no | count | Count of generated windows for the account, including blocked ones. It is not the count of delivered alerts or unique source legs. | No additional enum or range constraint | Native value / literal text |
| coverage_outcome | text | no | text | Account-level outcome that retains excluded and blocked accounts alongside assessed accounts. No-record output is not an acceptable substitute. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### AcceptanceTests — field contract

**Record grain:** one explicit deterministic expectation and its authored synthetic actual result

**Primary key:** `test_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| test_id | text | no | identifier | Unique deterministic acceptance-test key. Each test names the affected records and compares a specific expected result to a separately produced actual result. | No additional enum or range constraint | Native value / literal text |
| test_name | text | no | text | Specific acceptance proposition rather than a generic passed label. It names a boundary, count, state or authorization gate. | No additional enum or range constraint | Native value / literal text |
| expected | text | no | text | Exact target result for the named check. This is fixed before execution and may state not supplied when the check concerns authorization. | No additional enum or range constraint | Native value / literal text |
| actual | text | no | text | Recorded output of the check. In future sessions, use NOT TESTED until performed; do not copy the specimen result as evidence of a new execution. | No additional enum or range constraint | Native value / literal text |
| result | text | no | text | Control result or acceptance state. PASS applies to an executed synthetic check; it is not regulatory assurance or an operational approval. | No additional enum or range constraint | Native value / literal text |
| affected_ids | text | no | text | Explicit source, window or specification keys involved in an acceptance test. Preserve their grain rather than treating every identifier as a transaction. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### EvidenceProvenance — field contract

**Record grain:** one fictional evidence source with its access state and evidential limit

**Primary key:** `evidence_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| evidence_id | text | no | identifier | Exact unique Evidence key at one source-provenance row. It joins the common Evidence register without combining unrelated sources. | No additional enum or range constraint | Native value / literal text |
| source_kind | text | no | text | Explicitly fictional record type and origin. Authored cases and guidance references must not be mislabeled as actual institutional evidence. | No additional enum or range constraint | Native value / literal text |
| source_date | text | no | text | ISO calendar date of the authored source package, distinct from transaction event dates and evidence retrieval dates. | No additional enum or range constraint | Native value / literal text |
| availability | text | no | text | State of access to the source text. FULL_TEXT_IN_FILE_10 means the complete fictional content is supplied in this suite, not externally verified. | No additional enum or range constraint | Native value / literal text |
| locator | text | no | text | Exact file and section or row reference supporting retrieval of the fictional source. A title alone is insufficient. | No additional enum or range constraint | Native value / literal text |
| supports | text | no | text | Bounded proposition the source can establish in the synthetic exercise. It does not certify any broader customer or control conclusion. | No additional enum or range constraint | Native value / literal text |
| limitation | text | no | text | Specific scope restriction or evidential weakness that must accompany use of the source. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ProcessQA — field contract

**Record grain:** one performed or explicitly unrecorded quality proposition

**Primary key:** `check_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| check_id | text | no | identifier | Unique process-quality check key retained across output formats. A later rerun creates a dated actual result without changing the original expectation. | No additional enum or range constraint | Native value / literal text |
| check | text | no | text | Falsifiable control proposition with defined expected evidence. It must be precise enough for another reviewer to reproduce. | No additional enum or range constraint | Native value / literal text |
| expected | text | no | text | Exact target result for the named check. This is fixed before execution and may state not supplied when the check concerns authorization. | No additional enum or range constraint | Native value / literal text |
| actual | text | no | text | Recorded output of the check. In future sessions, use NOT TESTED until performed; do not copy the specimen result as evidence of a new execution. | No additional enum or range constraint | Native value / literal text |
| status | text | no | text | Recorded PASS, FAIL, REVIEW REQUIRED, NOT RECORDED or NOT TESTED status for this check, separate from analytical finding severity. | No additional enum or range constraint | Native value / literal text |
| reviewer | text | no | text | Identity or role of the actual check performer. The specimen labels authored arithmetic and explicitly records absent independent operational review. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.
<!-- FIELD_CONTRACTS:END -->
