# Trade Finance Review — inputs and evidence

## Define the economic unit

A trade is the underlying economic sale or shipment obligation, not the number of documents uploaded. An invoice can have several lines, shipments, credit notes and financing advances. One shipment can satisfy parts of several invoices. Preserve these relationships before comparing values. If the supplied IDs do not resolve the relationships, label allocation unknown rather than select the match that produces a convenient total.

| Input | Required detail | Missing-input effect |
| --- | --- | --- |
| Contract and invoice | Parties, dates, goods, grade, quantity, units, price, terms | Economic obligation or valuation may be unassessable |
| Amendments and credit notes | Effective date, original reference, revised amount | Do not net an unlinked credit or overwrite history |
| Shipment records | Unique consignment, quantity, unit, dates and status | No unsupported claim of delivery or nonshipment |
| Price comparator | Same goods, grade, date, market, quantity and delivery basis | No valid variance without comparability |
| Currency source | Quote convention, rate date, purpose and currency pair | Native totals only until conversion is supported |
| Financing | Actual funded principal, currency, dates, invoice allocation | Face amounts may not equal outstanding funding |
| Repayment and participation | Linked amounts, lifecycle and economic ownership | Potential overlap remains a question, not a finding of duplication |
| Criterion | Contract term, applicable rule or illustrative threshold | No invented universal legal requirement |

## Primary reference and applicability

REF-TBML: [FATF–Egmont Group, Trade-Based Money Laundering: Risk Indicators](https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Trade-Based-Money-Laundering-Risk-Indicators.pdf.coredownload.inline.pdf), March 2021, introductory handling notes and trade-document, commodity and account-activity categories; reviewed on 2026-10-09. This is an international typology reference, not a binding price schedule or conclusive test. It describes indicators that require context and may relate to other activity. The suite's numerical triggers, tables and fictional rates are original analytical conventions, not FATF-prescribed thresholds.

For actual legal or contractual conclusions, identify the relevant jurisdiction, institutional role, instrument, incorporated documentary rules and effective date. Do not presume every commercial invoice is a documentary-credit presentation or that every documentary discrepancy has a financial-crime meaning. This method assesses evidence; it does not decide whether a bank must honor, reject, freeze or finance an instrument.

## Document provenance and joins

Assign stable evidence IDs, with exact attachment page, table row, document number and relevant version. Preserve the party that issued each record, date, access status, source class, language and transformation history in the full case record. Map that detail into the common Evidence fields in 07. A seller-created invoice, carrier record, inspection certificate and funding ledger serve different propositions and may have different independence.

A copied invoice across two lenders may show document reuse without establishing duplicate outstanding finance. A scanned document is not authenticated merely because it looks formal. Record whether authenticity was assessed and by what permitted means. A hash can detect byte changes; it does not establish that goods existed, a signature was authorized or a shipment occurred.

OCR and translation can alter decimal separators, unit abbreviations, dates and product descriptions. Retain the original relevant text next to normalized fields. If a quantity is ambiguous between pieces and cartons, do not calculate a unit-price anomaly until pack size is resolved. For mixed goods, price each homogeneous line separately before aggregating value; a single average can conceal grade differences.

## Currency, units and valuation basis

Store native currency and native amount first. A conversion quote must state direction. USD per EUR is multiplied by EUR; EUR per USD must be inverted for that purpose. Record the rate date and why it is appropriate for the analysis: contract pricing, transaction posting or snapshot comparison. These are not interchangeable. A convenient current rate may distort a historical comparison.

Price comparisons require the same unit, grade, specification, quantity band, date and relevant commercial terms. Freight, insurance, tax, warranties, customization, installation and urgency can legitimately change invoice price. Record whether those components are included in both invoice and benchmark. If they cannot be aligned, keep the raw prices but report comparison NOT ASSESSABLE.

Shipment evidence should distinguish dispatched, loaded, arrived, delivered, returned and canceled. A bill of lading can support a particular carriage fact without establishing final delivery. Do not call a future scheduled shipment missing merely because it has not yet occurred at cutoff. Keep partial shipments, contract tolerance and amended delivery schedules visible.

## Funding allocation and missing evidence

Distinguish facility commitment, instrument face amount, approved advance, actual disbursement, outstanding principal, accrued charges and repayment. The same invoice may support a facility with a permitted advance rate, but the rule must be sourced. Multiple lenders can represent syndication, participation, refinancing or separate obligations; these are hypotheses to test using allocations and dates.

For each funded amount record the economic advance ID, invoice link, disbursement date, repayments through cutoff and any participation relationship. Do not count both a lead lender's full advance and a participant's share as separate money. Do not treat an unexecuted approval as funded. If another lender's status is only a party assertion, retain that claim class and avoid a confirmed overlapping-principal total.

Absence of shipping or financing data is not a clean result. State the missing record, the metric it prevents and the smallest evidence needed to resolve it. Keep unknown rows in the population. A refusal or nonresponse can be reported only if the actual request and response history are supplied; a proposed clarification does not create that history.

## Stable line identity and allocation

Give every homogeneous line a stable line_id linked to one trade_id and its source invoice/line number. Keep product specification, grade and quantity unit at that line. Shipment allocations must identify line_id and consignment ID; a shipment document mentioning only the trade does not establish how much of each mixed product shipped. An unallocated shipment makes the affected line quantity unassessable, not proportionally allocated by guesswork.

Financing remains at the economic advance and trade level unless the source supplies a narrower allocation. One advance funding a two-line trade is one funded amount. Preserve the raw advance ledger in the case record, aggregate distinct line USD values to the trade once, and then compare trade finance with that total. The two domain tables in 05 represent these different grains. Line quantities cannot be aggregated merely because the lines share a trade or an apparent unit label.
