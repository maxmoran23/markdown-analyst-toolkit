# Transaction Monitoring Review: fixed delivery contract

The report is the decision narrative, the workbook is the complete review ledger, and the optional offline dashboard is a view of exactly the same case record. All outputs must preserve the same source population, version, period, criteria, findings, unknowns and human-decision state. The common workbook sheets are Summary, Dashboard, Findings, Evidence, Actions and QA, followed by every domain table below in the declared order. Files 06–08 provide full renderers; their synthetic data must be replaced only with a complete reviewed case record.

Keep identifiers as text, monetary measures numeric in their declared currency, ratios numeric as proportions, and missing values as JSON null or empty spreadsheet cells with an accompanying reason. A string saying null is not a numeric null. A count of zero is permitted only for a complete or explicitly known subset. Never silently change a field name, append a unit to a numeric value, collapse evidence rows or truncate an exception register to fit a page. Use field/value records in a report when a wide table would become unreadable; the workbook retains every exact column.

## Fixed report headings and required coverage

1. **Review priorities and known movement** — Lead with the supported answer, raw outcome counts, unresolved gate and decision implication. Keep known monetary figures explicitly partial where required.
2. **Scope, population, and scenario method** — Identify the exact event period, ingestion cutoff if applicable, source inventory, criteria version, data grain, exclusion conventions and actual readable coverage.
3. **Findings and benign explanations** — Retain each finding ID, claim class, severity rationale, confidence rationale, supporting evidence, competing explanation and proposed next action.
4. **Account flow calculations** — Show the source and canonical calculation trail. Include every declared register assigned to this section and explain its grain before interpreting totals.
5. **Scenario matches and review outcomes** — Preserve all remaining domain registers, including blocked outcomes, overlaps, exceptions, review or delivery states and complete QA evidence.
6. **Evidence and criterion provenance** — Include exact fictional source locators and public-source applicability limits; a method reference cannot stand in for transaction-specific evidence.
7. **Proposed review and data-repair actions** — Separate proposed evidence requests or repairs from accepted, executed or verified actions. Leave absent owners, dates and approvals unprovided.
8. **Limitations, quality checks, and human decision** — State specific residual limitations, performed and unperformed tests, independent-review scope and actual human-disposition state.

## Table-level and field-level operating contracts

The following field cards are operational instructions for populating and reviewing the case, followed by machine-readable typed dictionaries maintained with the same schema. Each field card states the meaning and the corresponding verification behavior. These instructions are part of the runtime attachment; the reader does not need the repository or another suite to interpret a column.

### RawTransactions: Raw source rows and terminal reconciliation

**Grain:** one immutable raw receipt row, including extraction duplicates and unparsed amounts. **Primary key:** `raw_row_id`. The base specimen contains 10 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
raw_row_id | transaction_id | account_id | event_utc | direction | amount_text | currency | counterparty_id | posting_state | ownership_state | terminal_bucket | evidence_ids
```

**`raw_row_id`** — Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `R01; R02`.

**`transaction_id`** — Source economic transaction identifier. Its uniqueness is assessed with account leg and source version; matching amount or narrative alone is insufficient. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `T01; T02`.

**`account_id`** — Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `A; B`.

**`event_utc`** — Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2026-09-01T13:00:00Z; 2026-09-01T14:00:00Z`.

**`direction`** — Canonical CREDIT or DEBIT from the account perspective. Amount remains nonnegative; do not infer direction from a signed display string. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `CREDIT; DEBIT`.

**`amount_text`** — Exact source amount string before parsing. It can contain unreadable text; preserve it as evidence and never sum it directly. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `6000.00; 4000.00`.

**`currency`** — Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `USD`.

**`counterparty_id`** — Supplied counterparty reference for this economic leg. Similar names or repeated identifiers do not independently establish common ownership. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `P01; P02`.

**`posting_state`** — Canonical posting status that determines whether a leg enters the declared posted population. A pending item remains visible outside that population. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `POSTED`.

**`ownership_state`** — Evidence-backed own/external classification for the specific leg and historical period. Unknown ownership is not automatically external or own. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `CONFIRMED_EXTERNAL; CONFIRMED_OWN`.

**`terminal_bucket`** — Exactly one initial raw-row reconciliation outcome. It explains whether the row is processed, duplicate or unreadable; scenario exclusions are a separate layer. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `PROCESSED; DUPLICATE`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SYN-001; SYN-001;SYN-004`.

### CanonicalLedger: Canonical known posted account legs

**Grain:** one readable unique posted economic account leg. **Primary key:** `leg_id`. The base specimen contains 8 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
leg_id | raw_row_id | transaction_id | account_id | event_utc | direction | amount | currency | counterparty_id | ownership_state | scenario_eligible | evidence_ids
```

Join `raw_row_id` to `RawTransactions.raw_row_id` using exact text equality. Null is permitted only when the field contract allows it, with the row's reason explaining why no parent record exists.

**`leg_id`** — Unique identifier of one readable canonical posted account leg. It joins to the raw source and is never substituted for a customer identifier. Type `text`; unit `identifier`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `L-T01; L-T02`.

**`raw_row_id`** — Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `R01; R02`.

**`transaction_id`** — Source economic transaction identifier. Its uniqueness is assessed with account leg and source version; matching amount or narrative alone is insufficient. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `T01; T02`.

**`account_id`** — Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `A; B`.

**`event_utc`** — Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2026-09-01T13:00:00Z; 2026-09-01T14:00:00Z`.

**`direction`** — Canonical CREDIT or DEBIT from the account perspective. Amount remains nonnegative; do not infer direction from a signed display string. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `CREDIT; DEBIT`.

**`amount`** — Known nonnegative monetary amount in the row currency. Null means unrecovered source value and blocks the relevant completeness proposition. Type `number`; unit `row currency`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `6000.0; 4000.0`.

**`currency`** — Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `USD`.

**`counterparty_id`** — Supplied counterparty reference for this economic leg. Similar names or repeated identifiers do not independently establish common ownership. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `P01; P02`.

**`ownership_state`** — Evidence-backed own/external classification for the specific leg and historical period. Unknown ownership is not automatically external or own. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `CONFIRMED_EXTERNAL; CONFIRMED_OWN`.

**`scenario_eligible`** — Boolean record-level inclusion flag. True means a known eligible leg, not proof the entire account or window is complete. Type `boolean`; unit `boolean`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `True; False`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SYN-001; SYN-001;SYN-004`.

### Eligibility: Raw-row scenario eligibility decisions

**Grain:** one raw-row decision for the declared daily scenario. **Primary key:** `eligibility_id`. The base specimen contains 10 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
eligibility_id | raw_row_id | leg_id | account_id | scenario_id | eligibility_state | reason | evidence_ids
```

Join `raw_row_id` to `RawTransactions.raw_row_id` using exact text equality. Null is permitted only when the field contract allows it, with the row's reason explaining why no parent record exists.

**`eligibility_id`** — Unique identifier for a raw-row/scenario decision. It preserves reasons for retained, excluded and blocked records without removing source population members. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `EL-R01; EL-R02`.

**`raw_row_id`** — Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `R01; R02`.

**`leg_id`** — Unique identifier of one readable canonical posted account leg. It joins to the raw source and is never substituted for a customer identifier. Type `text`; unit `identifier`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `L-T01; L-T02`.

**`account_id`** — Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `A; B`.

**`scenario_id`** — Exact illustrative scenario identifier. Criteria are versioned outside the identifier in the case manifest and cannot drift between outputs. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `TM-01`.

**`eligibility_state`** — Record-level eligibility conclusion. ELIGIBLE_KNOWN, EXCLUDED_OWN, DUPLICATE and BLOCKED are mutually exclusive in the specimen. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `ELIGIBLE_KNOWN; EXCLUDED_OWN`.

**`reason`** — Specific evidence-backed reason for a state or transition. It identifies the relevant row, rule or missing fact rather than a generic compliance label. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Known external posted leg; account-level completeness checked separately; SYN-004 confirms common customer ownership during period`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SYN-001; SYN-001;SYN-004`.

### AccountFlows: AccountFlows

**Grain:** one account and currency within the fixed daily event period. **Primary key:** `account_id, currency`. The base specimen contains 4 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
account_id | currency | processed_tx_count | credit_total | debit_total | eligible_credit_total | eligible_debit_total | out_in_ratio | population_status
```

**`account_id`** — Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `A; B`.

**`currency`** — Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `USD`.

**`processed_tx_count`** — Count of readable canonical economic legs at account/currency grain. It excludes extraction duplicates and unknown-amount rows but retains own transfers. Type `integer`; unit `count`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `3; 2`.

**`credit_total`** — Known eligible or gross credit subtotal as specified by the table grain. It is not necessarily a complete total when coverage_state or population_status is defective. Type `number`; unit `row currency`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `10000; 5000`.

**`debit_total`** — Known eligible debit subtotal at the table grain. Null is required for a window total dependent on an unknown debit; known subtotals elsewhere remain explicitly partial. Type `number`; unit `row currency`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `9500; 4800`.

**`eligible_credit_total`** — Sum of known credit amounts after stated scenario exclusions. It cannot include confirmed own legs or a copied extraction duplicate. Type `number`; unit `row currency`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `10000; 5000`.

**`eligible_debit_total`** — Sum of known debit amounts after stated scenario exclusions. It is not an attributed or suspicious amount and may exceed eligible credits. Type `number`; unit `row currency`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `9500; 4800`.

**`out_in_ratio`** — Eligible debit total divided by positive eligible credit total. Stored as a dimensionless ratio and displayed as a percentage without changing decision precision. Type `number`; unit `ratio`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `0.95; 0.96`.

**`population_status`** — Account-level completeness or exclusion state. COMPLETE, OWN_TRANSFER_EXCLUDED and UNPARSED_AMOUNT have different analytical consequences. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `COMPLETE; OWN_TRANSFER_EXCLUDED`.

### WindowDiagnostics: Observed credit-anchored membership; coverage remains incomplete

**Grain:** one eligible credit anchor and its observed closed 24-hour interval. **Primary key:** `window_id`. The base specimen contains 3 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
window_id | account_id | anchor_leg_id | start_utc | end_utc | observed_leg_ids | known_credit_total | known_debit_total | known_ratio | first_debit_hours | coverage_state | evidence_ids
```

Join `anchor_leg_id` to `CanonicalLedger.leg_id` using exact text equality. Null is permitted only when the field contract allows it, with the row's reason explaining why no parent record exists.

**`window_id`** — Stable account/anchor/specification window key. It distinguishes overlapping observations so a membership count cannot be mistaken for unique transactions. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `W-A-T01; W-A-T02`.

**`account_id`** — Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `A; B`.

**`anchor_leg_id`** — Canonical eligible credit that starts a diagnostic window. Only credit anchors are used; a debit cannot silently become an anchor. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `L-T01; L-T02`.

**`start_utc`** — Inclusive UTC instant at the anchor. The applicable window convention determines endpoint inclusion, not the date formatting of the rendered table. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2026-09-01T13:00:00Z; 2026-09-01T14:00:00Z`.

**`end_utc`** — UTC endpoint exactly 24 elapsed hours after the anchor. The scenario-design closed interval includes this instant; the TM diagnostic convention matches it. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2026-09-02T13:00:00Z; 2026-09-02T14:00:00Z`.

**`observed_leg_ids`** — Semicolon-delimited canonical legs observed inside the diagnostic interval. This list is partial when the extract does not cover the entire interval. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `L-T01;L-T02;L-T03; L-T02;L-T03`.

**`known_credit_total`** — Sum of readable credits only at the declared stage, account or observed diagnostic window. The word known is substantive where an unresolved amount exists. Type `number`; unit `row currency`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `10000; 4000`.

**`known_debit_total`** — Sum of readable debits only at the declared stage, account or observed diagnostic window. An unknown debit is not imputed as a measured zero. Type `number`; unit `row currency`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `9500; 4800`.

**`known_ratio`** — Ratio of known observed debits to known observed credits when the denominator is positive. Boundary-incomplete diagnostics do not establish a complete rule result. Type `number`; unit `ratio`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `0.95; 2.375`.

**`first_debit_hours`** — Elapsed hours from anchor to first strictly subsequent eligible debit. Null means no qualifying ordered pair; a contemporaneous debit cannot satisfy the predicate. Type `number`; unit `hours`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2; 1`.

**`coverage_state`** — Completeness state for the exact account/window inputs. COMPLETE, BOUNDARY_INCOMPLETE and AMOUNT_UNKNOWN cannot be collapsed into a binary risk score. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `BOUNDARY_INCOMPLETE`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SYN-001;SYN-006`.

### ScenarioResults: ScenarioResults

**Grain:** one account, daily window and scenario specification. **Primary key:** `scenario_result_id`. The base specimen contains 4 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
scenario_result_id | account_id | scenario_id | eligible | rule_result | first_credit_to_debit_hours | review_outcome | evidence_ids
```

**`scenario_result_id`** — Stable daily account/scenario/window result key. It links to the review register without being replaced after a contextual explanation. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SR-001; SR-002`.

**`account_id`** — Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `A; B`.

**`scenario_id`** — Exact illustrative scenario identifier. Criteria are versioned outside the identifier in the case manifest and cannot drift between outputs. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `TM-01`.

**`eligible`** — Account-result eligibility flag after completeness and exclusion gates. False is distinguished by rule_result as either excluded or not assessable. Type `boolean`; unit `boolean`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `True; False`.

**`rule_result`** — Deterministic raw result under the named specification: MATCH, NO_MATCH, EXCLUDED or NOT_ASSESSABLE. Contextual evidence does not rewrite it. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `MATCH; EXCLUDED`.

**`first_credit_to_debit_hours`** — Elapsed hours from the first eligible daily credit to its first strictly subsequent eligible debit. It screens timing and does not attribute funding. Type `number`; unit `hours`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2; 3`.

**`review_outcome`** — Proposed contextual assessment distinct from raw rule_result. No value in this field constitutes an authorized filing or relationship decision. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `ESCALATE_FOR_REVIEW; EXPLANATION_SUPPORTED`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SYN-001;SYN-002; SYN-001;SYN-003`.

### ReviewLedger: Contextual review and unrecorded human disposition

**Grain:** one contextual review of a retained daily scenario result. **Primary key:** `review_id`. The base specimen contains 4 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
review_id | scenario_result_id | finding_id | account_id | raw_result | explanation_state | counterevidence | next_evidence | human_disposition | evidence_ids
```

Join `scenario_result_id` to `ScenarioResults.scenario_result_id` using exact text equality. Null is permitted only when the field contract allows it, with the row's reason explaining why no parent record exists.

**`review_id`** — Unique contextual review record. It joins the exact raw scenario result and retains the relevant finding or an explained null when no finding is raised. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `RV-A; RV-B`.

**`scenario_result_id`** — Stable daily account/scenario/window result key. It links to the review register without being replaced after a contextual explanation. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SR-001; SR-002`.

**`finding_id`** — Stable key to the Findings register. Nullable only where a documented review outcome raises no separate finding; absence is not a missing case record. Type `text`; unit `identifier`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `TM-F01; TM-F02`.

**`account_id`** — Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `A; B`.

**`raw_result`** — Preserved deterministic rule result before human review or delivery grouping. Explanations and grouping decisions must not delete or change it. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `MATCH; EXCLUDED`.

**`explanation_state`** — Scope-limited state of the explanation evidence. Supported documentation for one payment does not become an assurance about the whole account. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `UNSUPPORTED; SUPPORTED_FOR_T05`.

**`counterevidence`** — Strongest supplied limitation or competing interpretation that tempers the proposed concern. It may identify missing evidence without treating missingness as guilt. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `No opening balance or onward P03 records; timing does not trace funds; One invoice does not establish relationship-wide legitimacy`.

**`next_evidence`** — Specific discriminating document or control record needed for the next decision. It is a request proposal, not evidence that retrieval occurred. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Invoice or contract matching T03 plus counterparty role; Reviewer assessment of invoice linkage and remaining scope`.

**`human_disposition`** — Recorded authorized human decision. NOT_RECORDED is required in this specimen because no real person has approved or closed anything. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `NOT_RECORDED`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SYN-001;SYN-002; SYN-001;SYN-003`.

### ControlTotals: Count and monetary reconciliation with known limits

**Grain:** one explicitly named count or monetary reconciliation proposition. **Primary key:** `control_id`. The base specimen contains 7 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
control_id | measure | expected_value | actual_value | unit | result | calculation | evidence_ids
```

**`control_id`** — Unique reconciliation-control key. Controls can test different grains; counts and monetary comparisons are never combined into one unexplained balance. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `CT-01; CT-02`.

**`measure`** — Precisely named control measure including known versus complete scope. A passing count measure cannot substitute for unknown monetary completeness. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Received rows; Canonical known legs`.

**`expected_value`** — Independent expected numerical control value when known. Null records a proposition whose true value is unavailable rather than a failed zero comparison. Type `number`; unit `row unit`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `10; 8`.

**`actual_value`** — Reproduced value from the supplied rows. Null remains null when the corresponding measure is unavailable; never enter an attractive expected value by copying. Type `number`; unit `row unit`. Nullable: `true`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `10; 8`.

**`unit`** — Physical or analytical unit of the control, such as USD, rows, legs or account windows. The label determines what can validly be added or divided. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `rows; legs`.

**`result`** — Control result or acceptance state. PASS applies to an executed synthetic check; it is not regulatory assurance or an operational approval. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `PASS; NOT_ASSESSABLE`.

**`calculation`** — Explicit arithmetic or set-membership expression supporting the control. It retains unknown components instead of replacing them with a rounded display. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `8 processed + 1 duplicate + 1 unparsed; L-T01 through L-T08`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SYN-001; SYN-001;SYN-005`.

### EvidenceProvenance: Source identity, period, availability and evidential limits

**Grain:** one fictional evidence source with its access state and evidential limit. **Primary key:** `evidence_id`. The base specimen contains 6 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
evidence_id | source_kind | source_date | availability | locator | supports | limitation
```

**`evidence_id`** — Exact unique Evidence key at one source-provenance row. It joins the common Evidence register without combining unrelated sources. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SYN-001; SYN-002`.

**`source_kind`** — Explicitly fictional record type and origin. Authored cases and guidance references must not be mislabeled as actual institutional evidence. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Authored fictional case record; Authored fictional context record`.

**`source_date`** — ISO calendar date of the authored source package, distinct from transaction event dates and evidence retrieval dates. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `2026-09-02`.

**`availability`** — State of access to the source text. FULL_TEXT_IN_FILE_10 means the complete fictional content is supplied in this suite, not externally verified. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `FULL_TEXT_IN_FILE_10`.

**`locator`** — Exact file and section or row reference supporting retrieval of the fictional source. A title alone is insufficient. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `10-worked-example.md, raw population R01–R10; 10-worked-example.md, context register A`.

**`supports`** — Bounded proposition the source can establish in the synthetic exercise. It does not certify any broader customer or control conclusion. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Fictional transaction extract; Fictional account A profile`.

**`limitation`** — Specific scope restriction or evidential weakness that must accompany use of the source. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Supports only the stated fictional proposition; no external subject fact or institutional approval`.

### ProcessQA: Explicit expected and actual control evidence

**Grain:** one performed or explicitly unrecorded quality proposition. **Primary key:** `check_id`. The base specimen contains 5 rows. Later cases must populate the entire declared grain, including excluded and blocked records; the specimen count is a reproduction target, not a required production sample size.

Exact header:

```text
check_id | check | expected | actual | status | reviewer | evidence_ids
```

**`check_id`** — Unique process-quality check key retained across output formats. A later rerun creates a dated actual result without changing the original expectation. Type `text`; unit `identifier`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `TQ01; TQ02`.

**`check`** — Falsifiable control proposition with defined expected evidence. It must be precise enough for another reviewer to reproduce. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `All source rows have one terminal bucket; Daily rule hits remain after B explanation`.

**`expected`** — Exact target result for the named check. This is fixed before execution and may state not supplied when the check concerns authorization. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `10 = 8 + 1 + 1; A and B MATCH`.

**`actual`** — Recorded output of the check. In future sessions, use NOT TESTED until performed; do not copy the specimen result as evidence of a new execution. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `10 = 8 + 1 + 1; A and B MATCH`.

**`status`** — Recorded PASS, FAIL, REVIEW REQUIRED, NOT RECORDED or NOT TESTED status for this check, separate from analytical finding severity. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `PASS; REVIEW REQUIRED`.

**`reviewer`** — Identity or role of the actual check performer. The specimen labels authored arithmetic and explicitly records absent independent operational review. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `Authored specimen arithmetic; independent operational reviewer not supplied`.

**`evidence_ids`** — Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. Type `text`; unit `text`. Nullable: `false`; any null must retain the associated unresolved or inapplicable state. Base specimen values: `SYN-001; SYN-001;SYN-003`.

## Narrative-to-data consistency and artifact limits

For every headline number, retain the measure, value, unit, formula, scope and limitation. A formatted dollar amount cannot hide a mixed-currency sum, and a percentage must identify its numerator and denominator. Reconcile report statements to the exact domain rows rather than to a chart label. Keep raw matches, proposed explanations, exclusions, blocked records and human dispositions separate; they overlap conceptually and cannot be added as if they were one terminal transaction partition.

EvidenceProvenance supplements the common Evidence sheet with source kind, date, availability, exact locator, supported proposition and limitation. ProcessQA supplements the common QA sheet with fixed expected and actual values and the actual reviewer basis. Do not reduce these registers to a single passed badge. Preserve NOT RECORDED for human authorization and REVIEW REQUIRED or NOT TESTED where appropriate. Completed synthetic arithmetic is not an independent operational assessment.

If an output cannot be created, deliver all exact headings and tables as copy-ready Markdown with an explicit format failure. Do not rename text as XLSX or claim a file exists without an openable artifact. Preserve the canonical case data so a later render can reproduce it without repeating or inventing analysis. Any changed source, parameter or conclusion requires a new reviewed case record and affected quality checks before new artifacts are accepted.

<!-- FIELD_CONTRACTS:START -->
## Compiled domain field dictionary

This dictionary is part of this attachment. It fixes the type, null rule, unit, permitted values and record identity used by the embedded renderers. It is generated from the same reviewed case contract; no external file is needed. Raw source defects must be retained as raw text under their declared type. Correcting a malformed value requires evidence, not coercion by the renderer.

### RawTransactions — field contract

**Record grain:** one immutable raw receipt row, including extraction duplicates and unparsed amounts

**Primary key:** `raw_row_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| raw_row_id | text | no | identifier | Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable. | No additional enum or range constraint | Native value / literal text |
| transaction_id | text | no | identifier | Source economic transaction identifier. Its uniqueness is assessed with account leg and source version; matching amount or narrative alone is insufficient. | No additional enum or range constraint | Native value / literal text |
| account_id | text | no | identifier | Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. | No additional enum or range constraint | Native value / literal text |
| event_utc | text | no | text | Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant. | No additional enum or range constraint | Native value / literal text |
| direction | text | no | text | Canonical CREDIT or DEBIT from the account perspective. Amount remains nonnegative; do not infer direction from a signed display string. | No additional enum or range constraint | Native value / literal text |
| amount_text | text | no | text | Exact source amount string before parsing. It can contain unreadable text; preserve it as evidence and never sum it directly. | No additional enum or range constraint | Native value / literal text |
| currency | text | no | text | Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. | No additional enum or range constraint | Native value / literal text |
| counterparty_id | text | no | identifier | Supplied counterparty reference for this economic leg. Similar names or repeated identifiers do not independently establish common ownership. | No additional enum or range constraint | Native value / literal text |
| posting_state | text | no | text | Canonical posting status that determines whether a leg enters the declared posted population. A pending item remains visible outside that population. | No additional enum or range constraint | Native value / literal text |
| ownership_state | text | no | text | Evidence-backed own/external classification for the specific leg and historical period. Unknown ownership is not automatically external or own. | No additional enum or range constraint | Native value / literal text |
| terminal_bucket | text | no | text | Exactly one initial raw-row reconciliation outcome. It explains whether the row is processed, duplicate or unreadable; scenario exclusions are a separate layer. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### CanonicalLedger — field contract

**Record grain:** one readable unique posted economic account leg

**Primary key:** `leg_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| leg_id | text | yes | identifier | Unique identifier of one readable canonical posted account leg. It joins to the raw source and is never substituted for a customer identifier. | No additional enum or range constraint | Native value / literal text |
| raw_row_id | text | no | identifier | Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable. | No additional enum or range constraint | Native value / literal text |
| transaction_id | text | no | identifier | Source economic transaction identifier. Its uniqueness is assessed with account leg and source version; matching amount or narrative alone is insufficient. | No additional enum or range constraint | Native value / literal text |
| account_id | text | no | identifier | Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. | No additional enum or range constraint | Native value / literal text |
| event_utc | text | no | text | Timezone-aware economic event instant serialized in UTC. The source-local representation belongs in evidence; elapsed comparisons use this instant. | No additional enum or range constraint | Native value / literal text |
| direction | text | no | text | Canonical CREDIT or DEBIT from the account perspective. Amount remains nonnegative; do not infer direction from a signed display string. | No additional enum or range constraint | Native value / literal text |
| amount | number | yes | row currency | Known nonnegative monetary amount in the row currency. Null means unrecovered source value and blocks the relevant completeness proposition. | No additional enum or range constraint | #,##0.00 |
| currency | text | no | text | Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. | No additional enum or range constraint | Native value / literal text |
| counterparty_id | text | no | identifier | Supplied counterparty reference for this economic leg. Similar names or repeated identifiers do not independently establish common ownership. | No additional enum or range constraint | Native value / literal text |
| ownership_state | text | no | text | Evidence-backed own/external classification for the specific leg and historical period. Unknown ownership is not automatically external or own. | No additional enum or range constraint | Native value / literal text |
| scenario_eligible | boolean | no | boolean | Boolean record-level inclusion flag. True means a known eligible leg, not proof the entire account or window is complete. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Foreign key: `raw_row_id` resolves to `RawTransactions (raw_row_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### Eligibility — field contract

**Record grain:** one raw-row decision for the declared daily scenario

**Primary key:** `eligibility_id`

**Report placement:** section 4. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| eligibility_id | text | no | identifier | Unique identifier for a raw-row/scenario decision. It preserves reasons for retained, excluded and blocked records without removing source population members. | No additional enum or range constraint | Native value / literal text |
| raw_row_id | text | no | identifier | Immutable identifier of one delivered source row. Repeated economic transactions retain distinct raw-row identifiers so extraction duplicates remain countable. | No additional enum or range constraint | Native value / literal text |
| leg_id | text | yes | identifier | Unique identifier of one readable canonical posted account leg. It joins to the raw source and is never substituted for a customer identifier. | No additional enum or range constraint | Native value / literal text |
| account_id | text | no | identifier | Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. | No additional enum or range constraint | Native value / literal text |
| scenario_id | text | no | identifier | Exact illustrative scenario identifier. Criteria are versioned outside the identifier in the case manifest and cannot drift between outputs. | No additional enum or range constraint | Native value / literal text |
| eligibility_state | text | no | text | Record-level eligibility conclusion. ELIGIBLE_KNOWN, EXCLUDED_OWN, DUPLICATE and BLOCKED are mutually exclusive in the specimen. | No additional enum or range constraint | Native value / literal text |
| reason | text | no | text | Specific evidence-backed reason for a state or transition. It identifies the relevant row, rule or missing fact rather than a generic compliance label. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Foreign key: `raw_row_id` resolves to `RawTransactions (raw_row_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### AccountFlows — field contract

**Record grain:** one account and currency within the fixed daily event period

**Primary key:** `account_id + currency`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| account_id | text | no | identifier | Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. | No additional enum or range constraint | Native value / literal text |
| currency | text | no | text | Explicit row currency. USD and EUR remain separate; the specimen contains no foreign-exchange conversion or implicit base-currency amount. | No additional enum or range constraint | Native value / literal text |
| processed_tx_count | integer | no | count | Count of readable canonical economic legs at account/currency grain. It excludes extraction duplicates and unknown-amount rows but retains own transfers. | No additional enum or range constraint | Native value / literal text |
| credit_total | number | no | row currency | Known eligible or gross credit subtotal as specified by the table grain. It is not necessarily a complete total when coverage_state or population_status is defective. | No additional enum or range constraint | #,##0.00 |
| debit_total | number | yes | row currency | Known eligible debit subtotal at the table grain. Null is required for a window total dependent on an unknown debit; known subtotals elsewhere remain explicitly partial. | No additional enum or range constraint | #,##0.00 |
| eligible_credit_total | number | no | row currency | Sum of known credit amounts after stated scenario exclusions. It cannot include confirmed own legs or a copied extraction duplicate. | No additional enum or range constraint | #,##0.00 |
| eligible_debit_total | number | no | row currency | Sum of known debit amounts after stated scenario exclusions. It is not an attributed or suspicious amount and may exceed eligible credits. | No additional enum or range constraint | #,##0.00 |
| out_in_ratio | number | yes | ratio | Eligible debit total divided by positive eligible credit total. Stored as a dimensionless ratio and displayed as a percentage without changing decision precision. | No additional enum or range constraint | 0.0% |
| population_status | text | no | text | Account-level completeness or exclusion state. COMPLETE, OWN_TRANSFER_EXCLUDED and UNPARSED_AMOUNT have different analytical consequences. | No additional enum or range constraint | Native value / literal text |


### WindowDiagnostics — field contract

**Record grain:** one eligible credit anchor and its observed closed 24-hour interval

**Primary key:** `window_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| window_id | text | no | identifier | Stable account/anchor/specification window key. It distinguishes overlapping observations so a membership count cannot be mistaken for unique transactions. | No additional enum or range constraint | Native value / literal text |
| account_id | text | no | identifier | Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. | No additional enum or range constraint | Native value / literal text |
| anchor_leg_id | text | no | identifier | Canonical eligible credit that starts a diagnostic window. Only credit anchors are used; a debit cannot silently become an anchor. | No additional enum or range constraint | Native value / literal text |
| start_utc | text | no | text | Inclusive UTC instant at the anchor. The applicable window convention determines endpoint inclusion, not the date formatting of the rendered table. | No additional enum or range constraint | Native value / literal text |
| end_utc | text | no | text | UTC endpoint exactly 24 elapsed hours after the anchor. The scenario-design closed interval includes this instant; the TM diagnostic convention matches it. | No additional enum or range constraint | Native value / literal text |
| observed_leg_ids | text | no | text | Semicolon-delimited canonical legs observed inside the diagnostic interval. This list is partial when the extract does not cover the entire interval. | No additional enum or range constraint | Native value / literal text |
| known_credit_total | number | no | row currency | Sum of readable credits only at the declared stage, account or observed diagnostic window. The word known is substantive where an unresolved amount exists. | No additional enum or range constraint | #,##0.00 |
| known_debit_total | number | no | row currency | Sum of readable debits only at the declared stage, account or observed diagnostic window. An unknown debit is not imputed as a measured zero. | No additional enum or range constraint | #,##0.00 |
| known_ratio | number | yes | ratio | Ratio of known observed debits to known observed credits when the denominator is positive. Boundary-incomplete diagnostics do not establish a complete rule result. | No additional enum or range constraint | 0.0% |
| first_debit_hours | number | yes | hours | Elapsed hours from anchor to first strictly subsequent eligible debit. Null means no qualifying ordered pair; a contemporaneous debit cannot satisfy the predicate. | No additional enum or range constraint | 0.0 |
| coverage_state | text | no | text | Completeness state for the exact account/window inputs. COMPLETE, BOUNDARY_INCOMPLETE and AMOUNT_UNKNOWN cannot be collapsed into a binary risk score. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Foreign key: `anchor_leg_id` resolves to `CanonicalLedger (leg_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ScenarioResults — field contract

**Record grain:** one account, daily window and scenario specification

**Primary key:** `scenario_result_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| scenario_result_id | text | no | identifier | Stable daily account/scenario/window result key. It links to the review register without being replaced after a contextual explanation. | No additional enum or range constraint | Native value / literal text |
| account_id | text | no | identifier | Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. | No additional enum or range constraint | Native value / literal text |
| scenario_id | text | no | identifier | Exact illustrative scenario identifier. Criteria are versioned outside the identifier in the case manifest and cannot drift between outputs. | No additional enum or range constraint | Native value / literal text |
| eligible | boolean | no | boolean | Account-result eligibility flag after completeness and exclusion gates. False is distinguished by rule_result as either excluded or not assessable. | No additional enum or range constraint | Native value / literal text |
| rule_result | text | no | text | Deterministic raw result under the named specification: MATCH, NO_MATCH, EXCLUDED or NOT_ASSESSABLE. Contextual evidence does not rewrite it. | No additional enum or range constraint | Native value / literal text |
| first_credit_to_debit_hours | number | yes | hours | Elapsed hours from the first eligible daily credit to its first strictly subsequent eligible debit. It screens timing and does not attribute funding. | No additional enum or range constraint | 0.0 |
| review_outcome | text | no | text | Proposed contextual assessment distinct from raw rule_result. No value in this field constitutes an authorized filing or relationship decision. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ReviewLedger — field contract

**Record grain:** one contextual review of a retained daily scenario result

**Primary key:** `review_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| review_id | text | no | identifier | Unique contextual review record. It joins the exact raw scenario result and retains the relevant finding or an explained null when no finding is raised. | No additional enum or range constraint | Native value / literal text |
| scenario_result_id | text | no | identifier | Stable daily account/scenario/window result key. It links to the review register without being replaced after a contextual explanation. | No additional enum or range constraint | Native value / literal text |
| finding_id | text | yes | identifier | Stable key to the Findings register. Nullable only where a documented review outcome raises no separate finding; absence is not a missing case record. | No additional enum or range constraint | Native value / literal text |
| account_id | text | no | identifier | Fictional account key at the declared grain. Account and customer are different units; no aggregation across accounts occurs without an explicit bridge. | No additional enum or range constraint | Native value / literal text |
| raw_result | text | no | text | Preserved deterministic rule result before human review or delivery grouping. Explanations and grouping decisions must not delete or change it. | No additional enum or range constraint | Native value / literal text |
| explanation_state | text | no | text | Scope-limited state of the explanation evidence. Supported documentation for one payment does not become an assurance about the whole account. | No additional enum or range constraint | Native value / literal text |
| counterevidence | text | no | text | Strongest supplied limitation or competing interpretation that tempers the proposed concern. It may identify missing evidence without treating missingness as guilt. | No additional enum or range constraint | Native value / literal text |
| next_evidence | text | no | text | Specific discriminating document or control record needed for the next decision. It is a request proposal, not evidence that retrieval occurred. | No additional enum or range constraint | Native value / literal text |
| human_disposition | text | no | text | Recorded authorized human decision. NOT_RECORDED is required in this specimen because no real person has approved or closed anything. | No additional enum or range constraint | Native value / literal text |
| evidence_ids | text | no | text | Semicolon-delimited exact Evidence keys. Every key must resolve, support the row proposition and retain its claim class and scope limitation. | No additional enum or range constraint | Native value / literal text |

Foreign key: `scenario_result_id` resolves to `ScenarioResults (scenario_result_id)`. A composite key may be entirely null only where each field allows null; partially missing keys are rejected.
Every non-null evidence key must resolve to the common Evidence register. Multiple keys use semicolons; unresolved or empty references block generation.

### ControlTotals — field contract

**Record grain:** one explicitly named count or monetary reconciliation proposition

**Primary key:** `control_id`

**Report placement:** section 5. Empty tables retain their schema and zero-record state.

| Field | Type | Null allowed | Unit | Definition | Allowed values / bounds | Display |
| --- | --- | --- | --- | --- | --- | --- |
| control_id | text | no | identifier | Unique reconciliation-control key. Controls can test different grains; counts and monetary comparisons are never combined into one unexplained balance. | No additional enum or range constraint | Native value / literal text |
| measure | text | no | text | Precisely named control measure including known versus complete scope. A passing count measure cannot substitute for unknown monetary completeness. | No additional enum or range constraint | Native value / literal text |
| expected_value | number | yes | row unit | Independent expected numerical control value when known. Null records a proposition whose true value is unavailable rather than a failed zero comparison. | No additional enum or range constraint | Native value / literal text |
| actual_value | number | yes | row unit | Reproduced value from the supplied rows. Null remains null when the corresponding measure is unavailable; never enter an attractive expected value by copying. | No additional enum or range constraint | Native value / literal text |
| unit | text | no | text | Physical or analytical unit of the control, such as USD, rows, legs or account windows. The label determines what can validly be added or divided. | No additional enum or range constraint | Native value / literal text |
| result | text | no | text | Control result or acceptance state. PASS applies to an executed synthetic check; it is not regulatory assurance or an operational approval. | No additional enum or range constraint | Native value / literal text |
| calculation | text | no | text | Explicit arithmetic or set-membership expression supporting the control. It retains unknown components instead of replacing them with a rounded display. | No additional enum or range constraint | Native value / literal text |
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
