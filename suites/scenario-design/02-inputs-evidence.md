# Transaction Monitoring Scenario Design: complete input and evidence contract

## Acquisition manifest and source reconciliation

For each supplied input, record the source owner or origin if known, source identifier, extraction parameters, query version if supplied, extraction time, file identity, expected row count, actual row count, covered accounts, products and dates, currency and status populations, pagination limits, known filters and stated omissions. These are evidence fields, not assumed facts. If no independent control total exists, label the result as a reconciliation of the accessible extract and retain the missing control as a limitation.

Preserve raw source text before normalization. A source row and an economic transaction are different grains. Two rows may be exact extraction copies of one leg, while two equal payments with separate identifiers may be two legitimate events. A transfer can generate two account legs without either being a duplicate. Maintain separate immutable raw IDs and canonical IDs; a deletion from the analytical sums must remain explainable through an exclusion or lineage record. Retain the original order only as source evidence; do not use row order as a surrogate for time or sequencing metadata.

Counts and amounts are independent control dimensions. Every raw row must receive exactly one terminal source disposition, including unparsed, inaccessible or deferred records. Then classify canonical rows for the particular scenario separately. A source-level duplicate is not also counted as an own-transfer exclusion in the same conservation equation. A count equation can pass while monetary completeness is unknown. Sum only numeric amounts in each currency and disclose how many amounts, identities or timestamps remain unresolved.

## Required semantic commitments

| Commitment | Minimum evidence | Prohibited shortcut |
| --- | --- | --- |
| Economic identity | Account leg, source transaction key and applicable version semantics | Deduplicating by equal amounts or names |
| Historical scope | Event-time interval plus historical profile and ownership dates | Applying today's profile to old transactions without a dated basis |
| Run visibility | Ingestion cutoff and source availability evidence | Using a later correction as if the first run knew it |
| Direction | Source mapping or explicit signed-amount convention | Flipping sign twice or interpreting negative as reversal automatically |
| Monetary precision | Original amount string, currency scale and rounding policy | Binary display rounding before threshold comparison |
| Ownership | Reliable identity bridge effective during the period | Treating a similar counterparty name as confirmed own transfer |
| Reversal | Original identifier, amount, currency and scope relationship | Netting unrelated equal and opposite payments |
| Exclusion | Specific criterion, affected record IDs and supporting evidence | Removing inconvenient records from the denominator |
| Review explanation | Documents matched to the actual transaction and parties | Accepting an attractive generic business story |
| Disposition | Named authorized decision and its evidence | Inferring approval from a file being downloaded |

## Time, dates and event ordering

Declare the economic review period as start inclusive and end exclusive. The rolling scenario may use a different endpoint convention, which must be explicitly named rather than inherited accidentally. Normalize timezone-aware instants for duration calculations while preserving their original source representation. A local date without a timezone supports a date-level analysis only. A date field cannot establish a two-hour interval. A timestamp without an offset during a daylight-saving overlap can represent two different instants; retain the ambiguity until resolved.

Distinguish event time, posting time, settlement time and ingestion time. The illustrative examples use event instants for economic scope and ingestion instants only where a run cutoff is specified. A late-arriving row belongs to its economic period but was unavailable to an earlier run. A correction posted today may amend an event last week; both chronology and information availability matter. Record whether a rerun recomputes the historical period, carries a correction forward or uses another documented design. Do not choose the most favorable interpretation after seeing the result.

When two events share an instant and no authoritative sequence exists, classify them as contemporaneous. Deterministic sorting by ID makes output reproducible; it does not prove economic order. A strict subsequent-debit predicate requires a greater instant or an explicitly approved sequence convention. If a transaction's timestamp is uncertain by several minutes, preserve that range and calculate a boundary sensitivity where it can change a result. Do not manufacture seconds to make a test pass.

## Amount, currency and balance evidence

Retain amounts as nonnegative magnitude with direction in a separate field for these specimens. Preserve original strings and use decimal arithmetic for threshold calculations. If an actual source uses signed amounts, document exactly one mapping to the canonical convention and test both signs, zero and invalid combinations. A negative magnitude under a nonnegative schema is a validation failure; taking its absolute value can hide a source error. A legitimate zero-value verification event can remain in event counts while adding zero to movement, if its posting and product semantics are explicitly supported.

Never add currencies or asset units directly. Conversion requires original amount, source currency, destination currency, rate, rate direction, source, rate time and rounding rule. A USD-per-EUR rate is not interchangeable with EUR-per-USD. Transaction-time conversion and valuation-time conversion answer different questions. Reconcile original-currency totals before converted totals, and preserve both. None of these fictional specimens needs an exchange rate; the lineage EUR row remains separate and outside the USD-only screen.

Gross movement adds credits and debits; signed movement subtracts debits from credits. Neither equals ending balance without a verified opening balance and complete adjustments. Gross movement counts the two sides of a round trip. It is not unique funds, customer income, customer loss, suspicious value or criminal proceeds. Ratios can exceed one when preexisting funds finance outflows. Do not cap a ratio to obtain a more intuitive display. A zero denominator yields null and the specified rule branch, not infinity or an invented zero ratio.

## Context and evidence requests

A transaction posting establishes that the source recorded an entry. It does not alone establish beneficial control, ultimate destination, commercial purpose or legality. A stated business description is Reported. A matched invoice can corroborate one payment to the extent parties, amount, date and reference agree. It does not explain unrelated activity. A later customer response must retain its received date and cannot be silently backdated into an earlier review. Contradictory evidence stays in the record even when one explanation appears plausible.

Request the smallest specific evidence that can resolve a material branch: the authoritative transaction version for a conflict; the corrected amount and extraction controls for a parse defect; the ownership bridge for an own-transfer exclusion; the invoice and payment reference for a purpose claim; the complete boundary interval for a rolling-window calculation; or the run receipt for a late arrival. Name the affected IDs and the decision that remains blocked. Avoid blanket requests for every conceivable document when a narrow record would answer the actual question.

## Data-quality effects are hypothesis-specific

Classify a defect by affected propositions. An unreadable counterparty narrative may not block amount arithmetic but can block purpose analysis. An unknown amount blocks relevant sums and amount predicates. An unresolved timezone can leave gross movement known while blocking timing. A duplicate can inflate counts and sums without changing source account coverage. Missing whole accounts can invalidate relationship-wide conclusions even if every provided row parses perfectly. Explain these differences rather than assigning one global completeness percentage and assuming all decisions share it.

Build a repair dependency chain from raw row to canonical leg, account/currency subtotal, window membership, raw rule state, review result and report metric. A correction triggers every dependent recalculation, including windows that previously did not match. Retain old and new values and the change reason. A repair is not complete merely because the source owner sent a replacement file; the replacement must reconcile, preserve unaffected controls and pass the affected acceptance cases.

## Case-specific required populations and acquisition questions

Before accepting this population, confirm its scope, identity key, time basis and relation to the upstream source. Compare the first and last record and every exceptional row to their locators. A derived register is not an independent source control; retain the raw input and the transformation that generated it. If an input needed for this register is unavailable, name the affected field and downstream claim rather than leaving a header-only table or inventing a default.

### EventLedger source obligation

Acquire enough evidence to populate one unique fictional source event within the complete declared 48-hour interval. The exact fields are `event_id`, `account_id`, `event_utc`, `direction`, `amount`, `currency`, `ownership_state`, `posting_state`, `evidence_ids`. The specimen contains 13 complete records at this grain, including the explicit missing-value states printed in file 10.

### PredicateSpec source obligation

Acquire enough evidence to populate one ordered predicate in RULE-SD-01-v1. The exact fields are `predicate_id`, `order`, `field_or_measure`, `operator`, `operand`, `null_result`, `purpose`, `evidence_ids`. The specimen contains 8 complete records at this grain, including the explicit missing-value states printed in file 10.

### WindowResults source obligation

Acquire enough evidence to populate one account, eligible credit anchor, currency and rule version. The exact fields are `window_id`, `account_id`, `anchor_event_id`, `start_utc`, `end_utc`, `event_ids`, `credit_total`, `debit_total`, `ratio`, `first_debit_hours`, `coverage_state`, `rule_result`, `evidence_ids`. The specimen contains 6 complete records at this grain, including the explicit missing-value states printed in file 10.

### DeliveryDecisions source obligation

Acquire enough evidence to populate one proposed delivery disposition for a retained raw window result. The exact fields are `delivery_id`, `window_id`, `raw_result`, `delivery_state`, `group_id`, `reason`, `human_approval`, `evidence_ids`. The specimen contains 6 complete records at this grain, including the explicit missing-value states printed in file 10.

### AccountCoverage source obligation

Acquire enough evidence to populate one source account, including accounts that generate no external windows. The exact fields are `account_id`, `raw_events`, `known_credit_total`, `known_debit_total`, `external_anchor_count`, `window_count`, `coverage_outcome`, `evidence_ids`. The specimen contains 6 complete records at this grain, including the explicit missing-value states printed in file 10.

### AcceptanceTests source obligation

Acquire enough evidence to populate one explicit deterministic expectation and its authored synthetic actual result. The exact fields are `test_id`, `test_name`, `expected`, `actual`, `result`, `affected_ids`, `evidence_ids`. The specimen contains 7 complete records at this grain, including the explicit missing-value states printed in file 10.

### EvidenceProvenance source obligation

Acquire enough evidence to populate one fictional evidence source with its access state and evidential limit. The exact fields are `evidence_id`, `source_kind`, `source_date`, `availability`, `locator`, `supports`, `limitation`. The specimen contains 4 complete records at this grain, including the explicit missing-value states printed in file 10.

### ProcessQA source obligation

Acquire enough evidence to populate one performed or explicitly unrecorded quality proposition. The exact fields are `check_id`, `check`, `expected`, `actual`, `status`, `reviewer`, `evidence_ids`. The specimen contains 5 complete records at this grain, including the explicit missing-value states printed in file 10.

## Primary public-source register and bounded use

The following primary pages were accessed on Oct 09, 2026 for this authored package. Access records are not a legal currency certification. Read the applicable current source in a permitted environment before relying on it for an actual institution. The numerical parameters, specimen data, workflow gates and formulas below are authored analytical conventions; these publishers do not prescribe or approve them.

| Source ID | Primary reference | Exact contextual use | Boundary |
| --- | --- | --- | --- |
| AUTH-01 | [FFIEC Suspicious Activity Reporting](https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04), sections on transaction and surveillance monitoring | Context for documented filtering, testing and contextual review | US bank examination material; does not establish a universal threshold or approve this rule |
| AUTH-02 | [FFIEC examination procedures](https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04_ep), transaction and surveillance monitoring and transaction testing | Context for inspecting scope, source information and actual results | Examination procedure context, not evidence about the fictional subjects |
| AUTH-03 | [Wolfsberg Monitoring for Suspicious Activity, Part I](https://wolfsberg-group.org/resources/general/168/) | Industry perspective on considering customer attributes and behavior alongside transactions | Industry guidance, not law; not a source of specimen parameters |

Keep a future retrieval record with publisher, title, direct URL, retrieved time, page or section, source date if shown, proposition supported and unresolved applicability. A source-register entry cannot be used as evidence that a particular customer document is genuine. A search result excerpt cannot substitute for an unread source. If a link is unavailable, use NOT RETRIEVED and narrow the authority claim; preserve the original authored method as an explicitly illustrative method rather than inventing the missing guidance.
