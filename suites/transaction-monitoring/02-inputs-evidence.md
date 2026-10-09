# Transaction monitoring: inputs and evidence

## Input dictionary and grain

One canonical transaction is one posted economic leg in one account. Preserve a raw-row identifier in addition to transaction ID: the same transaction can appear in multiple extracts, and a transfer can have two legitimate account legs. Do not deduplicate solely because amount, date, or customer are the same.

| Input | Required fields and types | Meaning and validation |
| --- | --- | --- |
| Transactions | raw_row_id text, transaction_id text, account_id text, event_time timestamp, direction enum CREDIT/DEBIT, amount decimal, currency ISO text, status enum, counterparty_id text/null | Amount is nonnegative; direction carries the sign. Keep the original timestamp and normalized time. |
| Linkage | transfer_group_id text/null, reversal_of text/null, own_transfer boolean/null | Own-account status requires evidence; matching names alone are insufficient. A reversal is an event linked to an original, not permission to delete history. |
| Accounts | account_id, customer_id, product, opening_date, stated_activity, profile_as_of | Use the profile effective during the review period. A later profile cannot retroactively explain earlier activity without a dated basis. |
| Expectations | metric, expected_value or range, period, source_id, approved_by, effective_date | Separate a customer statement from an approved monitoring parameter and from an empirical historical baseline. |
| Scenario specification | scenario_id, version, eligible_population, exclusions, aggregation_key, window, operator, threshold, currency_basis | Every operator must be explicit: greater than differs from greater than or equal. |
| Review evidence | evidence_id, source, exact_locator, obtained_at, claim_class, availability | An invoice supports a stated purpose only to the degree it is independently matched to payment and counterparties. |

Optional fields include channel, originator and beneficiary institution, geography, device reference, merchant category, balance snapshots, settlement date, and relationship history. Their absence is not itself suspicious. Describe which hypotheses can no longer be tested. Do not infer cash from a vague “deposit” description or infer a foreign payment from a nonlocal name.

## Scope manifest and reconciliation

Declare the period as a half-open interval: start inclusive, end exclusive. State whether event time, posting time, or settlement time controls inclusion. Preserve records straddling the boundary in an exception ledger; a batch crossing midnight can otherwise create artificial pass-through patterns. Specify whether the extract is complete for all accounts or only already-alerted accounts. An alert-only extract cannot estimate the proportion of activity missed by monitoring.

Assign each raw row exactly one terminal bucket: processed, duplicate, excluded_by_scope, unparsed, inaccessible, or deferred. Reconcile `received = sum(terminal buckets)`. Then separately classify processed rows as scenario eligible, scenario excluded, or scenario not assessable. These are two different levels; never add scenario exclusions to raw-row exclusions twice.

Reconcile counts by source, account, date, currency, direction, and posting status. Reconcile known amounts by currency. Unknown amounts remain unknown: a count reconciliation can pass while monetary completeness fails. Compare extract controls with source totals when provided. If no source total exists, label the coverage “accessible extract only” and do not call the customer relationship fully reviewed.

Use transaction ID plus account leg and source version to identify a duplicate. When two versions disagree, choose neither silently: obtain the authoritative version or maintain a conflict bucket. Retain duplicate provenance even after excluding it from sums. Document refunds, chargebacks, cancellations, pending items, and reversals separately because their economic meanings differ.

## Evidence quality

An observed posting proves the system recorded that entry, not who ultimately controlled the counterparty. A stated business purpose is Reported until corroborated. A ratio is an Observed calculation from the accessible records; a claim that the ratio indicates possible pass-through activity is Inferred. A modeled missing amount would be Estimated and must never be inserted as a known posting.

Record evidence IDs at transaction, account, scenario, and finding level. Negative results need evidence too: an absent red flag requires sufficient field coverage. A customer response received after analysis must be dated and retained alongside the earlier hypothesis. Do not discard contradictory records simply because a plausible explanation has been found.

## Currency and time conventions

Do not add USD, EUR, token units, or asset quantities directly. If an approved conversion is necessary, retain original amount, original currency, rate, rate timestamp, rate source, converted amount, and rounding rule. Use the transaction-time rate only if that is the stated design; valuation-time rates answer a different question. Convert before aggregation and reconcile the converted ledger.

Use timezone-aware timestamps for elapsed intervals. Daylight-saving changes can produce repeated local times; compare normalized instants. If only dates exist, report whole-day bounds and do not manufacture an hour-level measure. A missing timestamp blocks a timing rule even when total volume is known.


## Public-source register

Sources below were retrieved for package preparation on **2026-10-09**. This records access, not a legal-currency certification. Recheck applicability, amendments, jurisdiction, and institution type for a live task. The methods and illustrative thresholds in this suite are authored analytical conventions, not quotations from or mandates attributed to these sources.

| ID | Source and locator | Publication/version | Applicability and boundary |
| --- | --- | --- | --- |
| AUTH-TM-01 | [FFIEC: Suspicious Activity Reporting](https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04) | Online manual; publication date not stated on accessed section | US bank examination context; contextual basis for documented monitoring and human review. |
| AUTH-TM-02 | [FFIEC: Suspicious Activity Reporting examination procedures](https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04_ep) | Online manual; publication date not stated on accessed section | Control-review context; prompts inspection of monitoring design and transaction testing. |

Record future retrievals separately using source ID, direct URL, publisher, publication date if stated, retrieval timestamp, page or section, exact proposition supported, and status. Guidance cannot establish the facts of a particular case. An accessible page does not establish the correctness of an attached customer assertion.
