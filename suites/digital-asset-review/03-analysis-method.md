# Digital Asset Review — analysis method

## 1. Define the unit of analysis

Specify whether each source row is a transaction, successful transfer event, attempted action, internal execution trace, unspent output, address balance, or vendor attribution. Do not combine these row types as interchangeable “transactions.” A single transaction can generate several transfer events, and a balance snapshot is a state measurement rather than another flow row.

Freeze the subject, network, assets, and block/time window. Use chain plus address/contract identity as the namespace. An identical address string on another network is a separate scope unless evidence establishes a relevant relationship. Preserve source casing where meaningful and validate using the chain's actual address rules; do not lower-case every chain by habit. The fictional example uses labels that are deliberately not real addresses.

## 2. Inventory capture completeness

Record each supplied page or file, query range, sort order, pagination cursor, source limit, row count, and retrieval time. Determine whether a source claims a complete history, a capped result, or a sampled view. Compare page boundaries for gaps and repeats. A final page with fewer rows than the limit can help describe the capture but is not universal proof of completeness if filters or provider limitations remain.

Classify missing coverage explicitly: absent time intervals, unqueried token types, missing internal traces, unavailable historical states, source errors, or unknown provider limits. If completeness cannot be established, label all sums “within supplied capture.” Do not imply that the subject has no other assets or activity. An explorer's address summary can provide a useful comparison only when its scope, cutoff, event definition, and asset coverage match.

## 3. Normalize without losing precision

Keep atomic amounts as exact integer strings. Validate that they contain permitted integer syntax and record the asset's decimal scale from evidence. Derive display quantity as atomic amount divided by 10 to the decimals power, using exact decimal arithmetic where available. If decimals are unknown, retain raw units and withhold human-unit totals. Never infer decimals from the number of zeros or a popular ticker.

Do not send large atomic integers through spreadsheet floating-point cells. Preserve them as text and present display quantities as exact decimal strings when necessary. Ordinary small counts can remain numeric. State that precise arithmetic is only as reliable as the captured amount and scale. A malicious or nonstandard token can emit misleading metadata or events; a neat decimal conversion does not establish economic value.

Keep asset identity separate from display symbol. Two contracts called PAPER remain separate assets. If fiat valuation is requested, add an explicit price source, price time, quote currency, method, and liquidity caveat. Do not value a token at one dollar because its name resembles a stablecoin. Missing prices produce unvalued quantities, not zero-dollar balances.

## 4. Deduplicate by event identity and provenance

Use the strongest chain-appropriate event key. For account-based logs, a network, transaction identifier, contract, and event/log index can distinguish events. For UTXO outputs, use network, transaction ID, and output index. For traces, preserve the trace path or source-specific unique key. Record the actual key supported by the source; do not invent missing indices.

Remove a row only when evidence establishes it is a repeat capture of the same event. If two rows share a transaction but have distinct log indices, retain both. If unique event fields are absent and equal-looking rows could be distinct, mark the duplication ambiguous and withhold a falsely exact total or provide bounded alternatives. Keep raw-row IDs and the surviving event ID so excluded duplicates remain auditable.

## 5. Determine execution and directional treatment

Separate success, failed, pending, and unknown execution states. Include only eligible successful value events in settled flow totals under the stated method. A failed attempt's requested amount stays in the event record with included=false; fees or other effects need their own correctly denominated treatment. A pending entry is not settled and may later change. A missing status is not success.

Relative to one subject address, classify successful events as IN, OUT, SELF, or OTHER. SELF requires the exact same subject on both sides under validated identity rules; a vendor claim that two different addresses share an owner is a separate clustering hypothesis. Track SELF quantity separately rather than adding it to both directional inflow and outflow. Retain zero and small unsolicited transfers as distinct activity, with an explicit display policy.

For a set of addresses, define whether transfers within the set are internal and ensure a value is not counted once for each constituent address. Do not assume the set is one owner; state whether it is a user-defined analytical set or an evidenced cluster. Cross-chain bridges and wrapped assets require separate event linkage and asset accounting, not simple summation across network totals.

## 6. Reconcile counts and amounts

First reconcile raw rows = unique events + confirmed duplicate rows. Then reconcile unique events = included eligible events + excluded execution-state events + unresolved events, under mutually exclusive categories. Within included events, reconcile directional and self/other counts. Keep counts separate from amounts; an event count can be valid even when an amount is unknown.

For each asset separately, sum eligible IN and OUT atomic amounts and scale only with known decimals. Net captured directional flow is IN minus OUT. It is not an ending balance without an opening balance and complete accounting for all relevant changes. Native fees are a separate asset from token flows. Rebasing, mint/burn behavior, contract mechanics, and omitted events can also prevent a simple flow-to-balance reconciliation.

Compare counterparty subtotals with event totals using the same inclusion criteria. A counterparty's event count is the number of eligible events, not the number of raw capture rows. If a row is excluded from settled sums, it must still appear in the event ledger and exclusion count. Never silently delete failed or ambiguous records to make totals match.

## 7. Assess labels and patterns independently

Maintain the attribution claim separately from the ledger observation. Record who applied a label, what evidence they provide, when it was current, whether it refers to an address or cluster, and whether independent corroboration exists. An explorer label, community tag, or vendor category is Reported unless its underlying support is assessed. A direct ledger transfer can be Observed while the recipient's real-world identity remains unknown.

Describe patterns using falsifiable measurements: repeated transfers, interval distribution, value concentration, rapid onward movement within a defined window, or a specific interaction. Avoid inferring intent, illicit source, common ownership, or money laundering from pattern alone. Evaluate alternatives such as exchange sweeps, internal treasury movement, payment batching, contract mechanics, spam, or testing.

If measuring exposure, define direct versus multi-hop, direction, time, asset, denominator, attribution version, and flow-allocation method. A path in a graph is not proof that particular funds followed that path. Do not label a fixed percentage “tainted” without a justified methodology and human interpretation. This pack does not provide a universal illicit-exposure threshold.

## 8. Produce a bounded conclusion

State the observed activity, exact units, capture scope, execution exclusions, attribution limits, and evidence needed next. Distinguish technical data-quality issues from investigative questions. Recommend obtaining missing pages, receipts, metadata, or attribution evidence where those would resolve the uncertainty. The output may guide further review but does not connect wallets, send transactions, freeze assets, file reports, or determine guilt.
