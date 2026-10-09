# Transaction Monitoring Data Lineage: fixed delivery contract

The report is the decision narrative, the workbook is the complete review ledger, and the optional offline dashboard is a view of exactly the same case record. All outputs must preserve the same source population, version, period, criteria, findings, unknowns and human-decision state. The common workbook sheets are Summary, Dashboard, Findings, Evidence, Actions and QA, followed by every domain table below in the declared order. Files 06–08 provide full renderers; their synthetic data must be replaced only with a complete reviewed case record.

Keep identifiers as text, monetary measures numeric in their declared currency, ratios numeric as proportions, and missing values as JSON null or empty spreadsheet cells with an accompanying reason. A string saying null is not a numeric null. A count of zero is permitted only for a complete or explicitly known subset. Never silently change a field name, append a unit to a numeric value, collapse evidence rows or truncate an exception register to fit a page. Use field/value records in a report when a wide table would become unreadable; the workbook retains every exact column.

## Fixed report headings and required coverage

1. **Lineage conclusion and unresolved coverage** — Lead with the supported answer, raw outcome counts, unresolved gate and decision implication. Keep known monetary figures explicitly partial where required.
2. **Source scope, cutoffs and transformation contract** — Identify the exact event period, ingestion cutoff if applicable, source inventory, criteria version, data grain, exclusion conventions and actual readable coverage.
3. **Defects, exclusions and downstream consequences** — Retain each finding ID, claim class, severity rationale, confidence rationale, supporting evidence, competing explanation and proposed next action.
4. **Source-to-canonical row lineage** — Show the source and canonical calculation trail. Include every declared register assigned to this section and explain its grain before interpreting totals.
5. **Stage controls and rerun impact** — Preserve all remaining domain registers, including blocked outcomes, overlaps, exceptions, review or delivery states and complete QA evidence.
6. **Evidence and transformation provenance** — Include exact fictional source locators and public-source applicability limits; a method reference cannot stand in for transaction-specific evidence.
7. **Proposed repair and reprocessing actions** — Separate proposed evidence requests or repairs from accepted, executed or verified actions. Leave absent owners, dates and approvals unprovided.
8. **Limitations, quality gates and acceptance** — State specific residual limitations, performed and unperformed tests, independent-review scope and actual human-disposition state.

## Table-level and field-level operating contracts

The following field cards are operational instructions for populating and reviewing the case, followed by machine-readable typed dictionaries maintained with the same schema. Each field card states the meaning and the corresponding verification behavior. These instructions are part of the runtime attachment; the reader does not need the repository or another suite to interpret a column.

### SourceRows: Immutable delivered source records

**Grain:** one immutable raw delivered feed record, including later-unavailable and exceptional records. **Primary key:** `raw_row_id`. The base specimen contains 15 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
raw_row_id | transaction_id | account_id | event_utc | ingest_utc | source_direction | amount_text | currency | source_status | source_version | reversal_of | evidence_ids
```

**`raw_row_id`** — Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `X01; X02`.

**`transaction_id`** — Source economic transaction identifier. Its uniqueness is assessed with account leg and source version; matching amount or narrative alone is insufficient. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `TX01; TX02`.

**`account_id`** — Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LA; LB`.

**`event_utc`** — Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2026-09-01T13:00:00Z; 2026-09-01T14:00:00Z`.

**`ingest_utc`** — UTC instant at which the source record became available to the monitoring feed. It controls run visibility separately from economic event-period inclusion. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2026-09-01T13:05:00Z; 2026-09-01T14:05:00Z`.

**`source_direction`** — Unmodified source C or D code. The explicit mapping defines direction; unmapped codes require an exception and cannot be guessed. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `C; D`.

**`amount_text`** — Exact source amount string before parsing. It can contain unreadable text; preserve it as evidence and never sum it directly. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `6000.00; 5400.00`.

**`currency`** — Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `USD; EUR`.

**`source_status`** — Original status code before mapping. P is posted, N pending and R a posted reversal under this particular source contract. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `P; N`.

**`source_version`** — Source-declared record version as text. Later ingestion alone is not evidence of a later authoritative version when this value is unchanged. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `1`.

**`reversal_of`** — Original source transaction key for a posted reversal. Null means no link supplied; do not fabricate a relation from equal and opposite amounts. Type `text`; unit `text`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `null; TX08`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LN-E01; LN-E01;LN-E02`.

### FieldMappings: Source-to-canonical transformations and rejection behavior

**Grain:** one explicit source-to-canonical transformation with its failure branch. **Primary key:** `mapping_id`. The base specimen contains 8 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
mapping_id | source_field | target_field | transformation | failure_state | test_locator | evidence_ids
```

**`mapping_id`** — Unique source-to-canonical transformation identifier. It separates the mapping definition from actual row-level transformation outcomes. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `MAP01; MAP02`.

**`source_field`** — Source column or explicit compound key consumed by a mapping. The original source text remains retrievable after transformation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `transaction_id + account_id + source_version; event_utc`.

**`target_field`** — Named canonical concept produced by the mapping. A transformed concept may require several source columns and has its own validation gate. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `canonical identity; event instant`.

**`transformation`** — Complete authored transformation rule for the supplied source. It specifies value mapping, precision and failure behavior without assuming vendor implementation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Exact text tuple; currency and amount are compared payload, not identity; Parse timezone-aware ISO timestamp; normalize UTC without changing instant`.

**`failure_state`** — Required exception category when the mapping cannot be applied. It must propagate to downstream affected windows rather than silently dropping records. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `CONFLICT if same tuple differs; UNPARSED_TIME`.

**`test_locator`** — Exact fictional source examples that exercise the mapping. These are sufficient to reproduce this specimen, not a complete production validation dataset. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `X06 and X07; X12 and X13 are previous ET business date`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LN-E06; LN-E03;LN-E06`.

### LineageLedger: Every source row to one initial terminal state

**Grain:** one raw source row and its initial RUN0 terminal disposition. **Primary key:** `lineage_id`. The base specimen contains 15 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
lineage_id | raw_row_id | canonical_id | terminal_state | reason | run_id | evidence_ids
```

Join `raw_row_id` to `SourceRows.raw_row_id` using exact text equality. Null is permitted only when the field contract allows it, with the row's reason explaining why no parent record exists.

**`lineage_id`** — Unique link between a raw source row and its initial disposition. Each raw row appears once even when it maps to an already retained canonical leg. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LIN-X01; LIN-X02`.

**`raw_row_id`** — Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `X01; X02`.

**`canonical_id`** — Unique canonical output identifier or explicit null for a noncanonical row. A duplicate may point to an existing canonical identifier without adding a row. Type `text`; unit `identifier`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `CL01; CL02`.

**`terminal_state`** — Exactly one initial row disposition for conservation. CANONICAL, DUPLICATE, CONFLICT, PENDING, REVERSAL_PAIR, LATE_DEFERRED and UNPARSED_AMOUNT partition the source. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `CANONICAL; DUPLICATE`.

**`reason`** — Specific evidence-backed reason for a state or transition. It identifies the relevant row, rule or missing fact rather than a generic compliance label. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Unique readable posted leg available by initial cutoff; Same economic tuple and payload as X01; later extraction metadata only`.

**`run_id`** — Snapshot identity with a fixed ingestion cutoff. RUN0 and RUN1 differ in available source information; neither is silently overwritten. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `RUN0`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LN-E01;LN-E06; LN-E01;LN-E02;LN-E06`.

### CanonicalOutput: Known unique posted legs at initial cutoff

**Grain:** one known unique posted account leg available at RUN0 and surviving declared exclusions. **Primary key:** `canonical_id`. The base specimen contains 7 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
canonical_id | raw_row_id | transaction_id | account_id | event_utc | direction | amount | currency | run_id | evidence_ids
```

Join `raw_row_id` to `SourceRows.raw_row_id` using exact text equality. Null is permitted only when the field contract allows it, with the row's reason explaining why no parent record exists.

**`canonical_id`** — Unique canonical output identifier or explicit null for a noncanonical row. A duplicate may point to an existing canonical identifier without adding a row. Type `text`; unit `identifier`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `CL01; CL02`.

**`raw_row_id`** — Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `X01; X02`.

**`transaction_id`** — Source economic transaction identifier. Its uniqueness is assessed with account leg and source version; matching amount or narrative alone is insufficient. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `TX01; TX02`.

**`account_id`** — Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LA; LB`.

**`event_utc`** — Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2026-09-01T13:00:00Z; 2026-09-01T14:00:00Z`.

**`direction`** — Canonical CREDIT or DEBIT from the account perspective. Amount remains nonnegative; do not infer direction from a signed display string. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `CREDIT; DEBIT`.

**`amount`** — Known nonnegative monetary amount in the row currency. Null means unrecovered source value and blocks the relevant completeness proposition. Type `number`; unit `row currency`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `6000.0; 5400.0`.

**`currency`** — Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `USD; EUR`.

**`run_id`** — Snapshot identity with a fixed ingestion cutoff. RUN0 and RUN1 differ in available source information; neither is silently overwritten. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `RUN0`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LN-E01`.

### StageControls: Counts and known amounts by stage and currency

**Grain:** one pipeline layer, run and currency control population. **Primary key:** `control_id`. The base specimen contains 6 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
control_id | stage | currency | row_count | known_credit_total | known_debit_total | unknown_amount_count | interpretation | evidence_ids
```

**`control_id`** — Unique reconciliation-control key. Controls can test different grains; counts and monetary comparisons are never combined into one unexplained balance. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LC01; LC02`.

**`stage`** — Named source or canonical pipeline layer and run. Its grain must be checked before interpreting totals because raw rows include non-economic duplicates. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Delivered raw; RUN0 canonical`.

**`currency`** — Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `USD; EUR`.

**`row_count`** — Number of records in the named stage and currency. This is counted independently of known amounts and can include unreadable monetary rows. Type `integer`; unit `count`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `14; 1`.

**`known_credit_total`** — Sum of readable credits only at the declared stage, account or observed diagnostic window. The word known is substantive where an unresolved amount exists. Type `number`; unit `row currency`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `35200; 1000`.

**`known_debit_total`** — Sum of readable debits only at the declared stage, account or observed diagnostic window. An unknown debit is not imputed as a measured zero. Type `number`; unit `row currency`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `17500; 0`.

**`unknown_amount_count`** — Count of stage records whose amount is not numeric. It does not measure uncertain amount ranges or conflicted values unless explicitly stated. Type `integer`; unit `count`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `1; 0`.

**`interpretation`** — Specific limitation on the control total, including duplicate/conflict effects or incomplete economic coverage. It travels with the number in every output. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Raw contains duplicate, conflicting alternatives, pending and reversal; not economic total; Separate currency; not added to USD`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LN-E01; LN-E01;LN-E06`.

### RunImpact: Account assessment changes after known late arrival

**Grain:** one account and currency compared across RUN0 and RUN1. **Primary key:** `impact_id`. The base specimen contains 8 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
impact_id | account_id | currency | run0_credit | run0_debit | run0_state | run1_credit | run1_debit | run1_state | change_reason | evidence_ids
```

**`impact_id`** — Stable account/currency change-comparison key. It connects prior and rerun states without presenting the new state as the original conclusion. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `IMP-A; IMP-B`.

**`account_id`** — Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LA; LB`.

**`currency`** — Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `USD; EUR`.

**`run0_credit`** — Known initial-run credit subtotal in row currency. A zero on a blocked account is a known subtotal only and cannot prove no credits exist. Type `number`; unit `row currency`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `6000; 5000`.

**`run0_debit`** — Known initial-run debit subtotal in row currency. Reversal exclusions and missing records are documented separately. Type `number`; unit `row currency`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `5400; 4500`.

**`run0_state`** — Initial downstream assessment after all source defects known to the case are propagated. A known unavailable event makes the account incomplete. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `MATCH; NOT_ASSESSABLE`.

**`run1_credit`** — Known rerun credit subtotal after the declared late event becomes available. Unrelated unresolved defects are not repaired by this increase. Type `number`; unit `row currency`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `6000; 5000`.

**`run1_debit`** — Known rerun debit subtotal under the same scope and transformation rules. Its equality to RUN0 is a checked result rather than an assumption. Type `number`; unit `row currency`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `5400; 4500`.

**`run1_state`** — Downstream assessment at the later cutoff with the same illustrative predicates. State changes require an explicit source or criteria delta. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `MATCH; NOT_ASSESSABLE`.

**`change_reason`** — Exact source delta explaining a before/after result. It distinguishes improved completeness from changed risk or changed threshold. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `No source change; TX05 conflict unresolved; credit zero means known subtotal only`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LN-E01;LN-E06; LN-E02;LN-E06`.

### ExceptionRegister: Specific defects and required repair evidence

**Grain:** one specific defect or documented controlled treatment and its repair evidence. **Primary key:** `exception_id`. The base specimen contains 4 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
exception_id | account_id | source_rows | exception_type | affected_claim | required_evidence | repair_state | evidence_ids
```

**`exception_id`** — Unique source-defect or controlled-treatment record. Exceptions retain their evidence and cannot be closed merely because a rerun finished. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `EX01; EX02`.

**`account_id`** — Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LC; LF`.

**`source_rows`** — Semicolon-delimited raw-row keys contributing to the exception. Each referenced row remains in the immutable source and lineage registers. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `X06;X07; X12`.

**`exception_type`** — Specific conflict, late-arrival, unreadable-amount or reversal-treatment category. Categories drive different repair and retest requirements. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `CONFLICT; LATE_ARRIVAL`.

**`affected_claim`** — Analytical statement that cannot be supported, or changes meaning, because of the exception. This connects technical defects to monitoring consequences. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Credit amount and LC rule outcome; Initial completeness and LF timing`.

**`required_evidence`** — Concrete source-owner evidence needed to resolve or verify the exception. A verbal assurance does not substitute for the named record. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Authoritative TX05 version history and amount; do not choose maximum; RUN1 ingest receipt and complete lag population`.

**`repair_state`** — Actual evidence state of repair in the specimen. OPEN remains unresolved, RERUN_REPRODUCED verifies the illustrated rerun, DOCUMENTED_ONLY is not operational acceptance. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `OPEN; RERUN_REPRODUCED`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LN-E02; LN-E04`.

### EvidenceProvenance: Source identity, period, availability and evidential limits

**Grain:** one fictional evidence source with its access state and evidential limit. **Primary key:** `evidence_id`. The base specimen contains 6 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
evidence_id | source_kind | source_date | availability | locator | supports | limitation
```

**`evidence_id`** — Exact unique Evidence key at one source-provenance row. It joins the common Evidence register without combining unrelated sources. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LN-E01; LN-E02`.

**`source_kind`** — Explicitly fictional record type and origin. Authored cases and guidance references must not be mislabeled as actual institutional evidence. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Authored fictional case record`.

**`source_date`** — ISO calendar date of the authored source package, distinct from transaction event dates and evidence retrieval dates. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2026-09-02`.

**`availability`** — State of access to the source text. FULL_TEXT_IN_FILE_10 means the complete fictional content is supplied in this suite, not externally verified. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `FULL_TEXT_IN_FILE_10`.

**`locator`** — Exact file and section or row reference supporting retrieval of the fictional source. A title alone is insufficient. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `10-worked-example.md, SourceRows X01-X15; source manifest; 10-worked-example.md, TX05 conflict declaration`.

**`supports`** — Bounded proposition the source can establish in the synthetic exercise. It does not certify any broader customer or control conclusion. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Fictional delivered feed; Fictional conflict notice`.

**`limitation`** — Specific scope restriction or evidential weakness that must accompany use of the source. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Supports only the stated fictional proposition; no external subject fact or institutional approval`.

### ProcessQA: Explicit expected and actual control evidence

**Grain:** one performed or explicitly unrecorded quality proposition. **Primary key:** `check_id`. The base specimen contains 5 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
check_id | check | expected | actual | status | reviewer | evidence_ids
```

**`check_id`** — Unique process-quality check key retained across output formats. A later rerun creates a dated actual result without changing the original expectation. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LQ01; LQ02`.

**`check`** — Falsifiable control proposition with defined expected evidence. It must be precise enough for another reviewer to reproduce. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Initial terminal conservation; RUN1 known USD gross`.

**`expected`** — Exact target result for the named check. This is fixed before execution and may state not supplied when the check concerns authorization. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `15 = 7 + 1 + 2 + 1 + 2 + 1 + 1; 29500.00`.

**`actual`** — Recorded output of the check. In future sessions, use NOT TESTED until performed; do not copy the specimen result as evidence of a new execution. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `15 = 7 + 1 + 2 + 1 + 2 + 1 + 1; 29500.00`.

**`status`** — Recorded PASS, FAIL, REVIEW REQUIRED, NOT RECORDED or NOT TESTED status for this check, separate from analytical finding severity. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `PASS; NOT RECORDED`.

**`reviewer`** — Identity or role of the actual check performer. The specimen labels authored arithmetic and explicitly records absent independent operational review. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Authored specimen arithmetic; independent operational reviewer not supplied`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `LN-E01;LN-E06; LN-E01;LN-E04`.

## Narrative-to-data consistency and artifact limits

For every headline number, retain the measure, value, unit, formula, scope and limitation. A formatted dollar amount cannot hide a mixed-currency sum, and a percentage must identify its numerator and denominator. Reconcile report statements to the exact domain rows rather than to a chart label. Keep raw matches, proposed explanations, exclusions, blocked records and human dispositions separate; they overlap conceptually and cannot be added as if they were one terminal transaction partition.

EvidenceProvenance supplements the common Evidence sheet with source kind, date, availability, exact locator, supported proposition and limitation. ProcessQA supplements the common QA sheet with fixed expected and actual values and the actual reviewer basis. Do not reduce these registers to a single passed badge. Preserve NOT RECORDED for human authorization and REVIEW REQUIRED or NOT TESTED where appropriate. Completed synthetic arithmetic is not an independent operational assessment.

If an output cannot be created, deliver all exact headings and tables as copy-ready Markdown with an explicit format failure. Do not rename text as XLSX or claim a file exists without an openable artifact. Preserve the canonical case data so a later render can reproduce it without repeating or inventing analysis. Any changed source, parameter or conclusion requires a new reviewed case record and affected quality checks before new artifacts are accepted.

<!-- FIELD_CONTRACTS:START -->
## Compiled domain field dictionary

This dictionary is part of this attachment. It fixes the type, null rule, unit, permitted values and record identity used by the embedded renderers. It is generated from the same reviewed case contract; no external file is needed. Raw source defects must be retained as raw text under their declared type. Correcting a malformed value requires evidence, not coercion by the renderer.

### SourceRows — field contract

**Record grain:** one immutable raw delivered feed record, including later-unavailable and exceptional records

**Primary key:** `raw_row_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| raw_row_id | text | no | identifier | Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable. | No additional enum or range constraint | Native value / literal text |
| transaction_id | text | no | identifier | Source economic transaction identifier. Its uniqueness is assessed with account leg and source version; matching amount or narrative alone is insufficient. | No additional enum or range constraint | Native value / literal text |
| account_id | text | no | identifier | Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. | No additional enum or range constraint | Native value / literal text |
| event_utc | text | no | text | Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant. | No additional enum or range constraint | Native value / literal text |
| ingest_utc | text | no | text | UTC instant at which the source record became available to the monitoring feed. It controls run visibility separately from economic event-period inclusion. | No additional enum or range constraint | Native value / literal text |
| source_direction | text | no | text | Unmodified source C or D code. The explicit mapping defines direction; unmapped codes require an exception and cannot be guessed. | No additional enum or range constraint | Native value / literal text |
| amount_text | text | no | text | Exact source amount string before parsing. It can contain unreadable text; preserve it as evidence and never sum it directly. | No additional enum or range constraint | Native value / literal text |
| currency | text | no | text | Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. | No additional enum or range constraint | Native value / literal text |
| source_status | text | no | text | Original status code before mapping. P is posted, N pending and R a posted reversal under this particular source contract. | No additional enum or range constraint | Native value / literal text |
| source_version | text | no | text | Source-declared record version as text. Later ingestion alone is not evidence of a later authoritative version when this value is unchanged. | No additional enum or range constraint | Native value / literal text |
| reversal_of | text | yes | text | Original source transaction key for a posted reversal. Null means no link supplied; do not fabricate a relation from equal and opposite amounts. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### FieldMappings — field contract

**Record grain:** one explicit source-to-canonical transformation with its failure branch

**Primary key:** `mapping_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| mapping_id | text | no | identifier | Unique source-to-canonical transformation identifier. It separates the mapping definition from actual row-level transformation outcomes. | No additional enum or range constraint | Native value / literal text |
| source_field | text | no | text | Source column or explicit compound key consumed by a mapping. The original source text remains retrievable after transformation. | No additional enum or range constraint | Native value / literal text |
| target_field | text | no | text | Named canonical concept produced by the mapping. A transformed concept may require several source columns and has its own validation gate. | No additional enum or range constraint | Native value / literal text |
| transformation | text | no | text | Complete authored transformation rule for the supplied source. It specifies value mapping, precision and failure behavior without assuming vendor implementation. | No additional enum or range constraint | Native value / literal text |
| failure_state | text | no | text | Required exception category when the mapping cannot be applied. It must propagate to downstream affected windows rather than silently dropping records. | No additional enum or range constraint | Native value / literal text |
| test_locator | text | no | text | Exact fictional source examples that exercise the mapping. These are sufficient to reproduce this specimen, not a complete production validation dataset. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### LineageLedger — field contract

**Record grain:** one raw source row and its initial RUN0 terminal disposition

**Primary key:** `lineage_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| lineage_id | text | no | identifier | Unique link between a raw source row and its initial disposition. Each raw row appears once even when it maps to an already retained canonical leg. | No additional enum or range constraint | Native value / literal text |
| raw_row_id | text | no | identifier | Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable. | No additional enum or range constraint | Native value / literal text |
| canonical_id | text | yes | identifier | Unique canonical output identifier or explicit null for a noncanonical row. A duplicate may point to an existing canonical identifier without adding a row. | No additional enum or range constraint | Native value / literal text |
| terminal_state | text | no | text | Exactly one initial row disposition for conservation. CANONICAL, DUPLICATE, CONFLICT, PENDING, REVERSAL_PAIR, LATE_DEFERRED and UNPARSED_AMOUNT partition the source. | No additional enum or range constraint | Native value / literal text |
| reason | text | no | text | Specific evidence-backed reason for a state or transition. It identifies the relevant row, rule or missing fact rather than a generic compliance label. | No additional enum or range constraint | Native value / literal text |
| run_id | text | no | identifier | Snapshot identity with a fixed ingestion cutoff. RUN0 and RUN1 differ in available source information; neither is silently overwritten. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Foreign key: `raw_row_id` resolves to `SourceRows (raw_row_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### CanonicalOutput — field contract

**Record grain:** one known unique posted account leg available at RUN0 and surviving declared exclusions

**Primary key:** `canonical_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| canonical_id | text | yes | identifier | Unique canonical output identifier or explicit null for a noncanonical row. A duplicate may point to an existing canonical identifier without adding a row. | No additional enum or range constraint | Native value / literal text |
| raw_row_id | text | no | identifier | Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable. | No additional enum or range constraint | Native value / literal text |
| transaction_id | text | no | identifier | Source economic transaction identifier. Its uniqueness is assessed with account leg and source version; matching amount or narrative alone is insufficient. | No additional enum or range constraint | Native value / literal text |
| account_id | text | no | identifier | Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. | No additional enum or range constraint | Native value / literal text |
| event_utc | text | no | text | Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant. | No additional enum or range constraint | Native value / literal text |
| direction | text | no | text | Canonical CREDIT or DEBIT from the account perspective. Amount remains nonnegative; do not infer direction from a signed display string. | No additional enum or range constraint | Native value / literal text |
| amount | number | yes | row currency | Known nonnegative monetary amount in the row currency. Null means unrecovered source value and blocks the relevant completeness proposition. | No additional enum or range constraint | #,##0.00 |
| currency | text | no | text | Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. | No additional enum or range constraint | Native value / literal text |
| run_id | text | no | identifier | Snapshot identity with a fixed ingestion cutoff. RUN0 and RUN1 differ in available source information; neither is silently overwritten. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Foreign key: `raw_row_id` resolves to `SourceRows (raw_row_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### StageControls — field contract

**Record grain:** one pipeline layer, run and currency control population

**Primary key:** `control_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| control_id | text | no | identifier | Unique reconciliation-control key. Controls can test different grains; counts and monetary comparisons are never combined into one unexplained balance. | No additional enum or range constraint | Native value / literal text |
| stage | text | no | text | Named source or canonical pipeline layer and run. Its grain must be checked before interpreting totals because raw rows include non-economic duplicates. | No additional enum or range constraint | Native value / literal text |
| currency | text | no | text | Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. | No additional enum or range constraint | Native value / literal text |
| row_count | integer | no | count | Number of records in the named stage and currency. This is counted independently of known amounts and can include unreadable monetary rows. | No additional enum or range constraint | Native value / literal text |
| known_credit_total | number | no | row currency | Sum of readable credits only at the declared stage, account or observed diagnostic window. The word known is substantive where an unresolved amount exists. | No additional enum or range constraint | #,##0.00 |
| known_debit_total | number | no | row currency | Sum of readable debits only at the declared stage, account or observed diagnostic window. An unknown debit is not imputed as a measured zero. | No additional enum or range constraint | #,##0.00 |
| unknown_amount_count | integer | no | count | Count of stage records whose amount is not numeric. It does not measure uncertain amount ranges or conflicted values unless explicitly stated. | No additional enum or range constraint | Native value / literal text |
| interpretation | text | no | text | Specific limitation on the control total, including duplicate/conflict effects or incomplete economic coverage. It travels with the number in every output. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### RunImpact — field contract

**Record grain:** one account and currency compared across RUN0 and RUN1

**Primary key:** `impact_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| impact_id | text | no | identifier | Stable account/currency change-comparison key. It connects prior and rerun states without presenting the new state as the original conclusion. | No additional enum or range constraint | Native value / literal text |
| account_id | text | no | identifier | Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. | No additional enum or range constraint | Native value / literal text |
| currency | text | no | text | Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. | No additional enum or range constraint | Native value / literal text |
| run0_credit | number | no | row currency | Known initial-run credit subtotal in row currency. A zero on a blocked account is a known subtotal only and cannot prove no credits exist. | No additional enum or range constraint | #,##0.00 |
| run0_debit | number | no | row currency | Known initial-run debit subtotal in row currency. Reversal exclusions and missing records are documented separately. | No additional enum or range constraint | #,##0.00 |
| run0_state | text | no | text | Initial downstream assessment after all source defects known to the case are propagated. A known unavailable event makes the account incomplete. | No additional enum or range constraint | Native value / literal text |
| run1_credit | number | no | row currency | Known rerun credit subtotal after the declared late event becomes available. Unrelated unresolved defects are not repaired by this increase. | No additional enum or range constraint | #,##0.00 |
| run1_debit | number | no | row currency | Known rerun debit subtotal under the same scope and transformation rules. Its equality to RUN0 is a checked result rather than an assumption. | No additional enum or range constraint | #,##0.00 |
| run1_state | text | no | text | Downstream assessment at the later cutoff with the same illustrative predicates. State changes require an explicit source or criteria delta. | No additional enum or range constraint | Native value / literal text |
| change_reason | text | no | text | Exact source delta explaining a before/after result. It distinguishes improved completeness from changed risk or changed threshold. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ExceptionRegister — field contract

**Record grain:** one specific defect or documented controlled treatment and its repair evidence

**Primary key:** `exception_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| exception_id | text | no | identifier | Unique source-defect or controlled-treatment record. Exceptions retain their evidence and cannot be closed merely because a rerun finished. | No additional enum or range constraint | Native value / literal text |
| account_id | text | no | identifier | Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. | No additional enum or range constraint | Native value / literal text |
| source_rows | text | no | text | Semicolon-delimited raw-row keys contributing to the exception. Each referenced row remains in the immutable source and lineage registers. | No additional enum or range constraint | Native value / literal text |
| exception_type | text | no | text | Specific conflict, late-arrival, unreadable-amount or reversal-treatment category. Categories drive different repair and retest requirements. | No additional enum or range constraint | Native value / literal text |
| affected_claim | text | no | text | Analytical statement that cannot be supported, or changes meaning, because of the exception. This connects technical defects to monitoring consequences. | No additional enum or range constraint | Native value / literal text |
| required_evidence | text | no | text | Concrete source-owner evidence needed to resolve or verify the exception. A verbal assurance does not substitute for the named record. | No additional enum or range constraint | Native value / literal text |
| repair_state | text | no | text | Actual evidence state of repair in the specimen. OPEN remains unresolved, RERUN_REPRODUCED verifies the illustrated rerun, DOCUMENTED_ONLY is not operational acceptance. | No additional enum or range constraint | Native value / literal text |
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
