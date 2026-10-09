# Trade Finance Review — complete fictional example

All counterparties, goods, invoices, shipments, funding records, benchmarks and rates are invented. The five economic trades concern industrial coupling products with the grades shown below; they are not real customer transactions. Cutoff: Sep 30, 2026 5:00 PM ET. The decision is which discrepancies require human clarification. No bank action is performed.

## Complete invoice input, SYN-001

All invoices are dated Sep 01, 2026. Quantity unit is one finished coupling. Amounts contain no freight, insurance, tax, discount or bundled service. Every line is a separate economic invoice; grades are defined only for this exercise.

| Trade / invoice | line_id | Grade | Native currency | Quantity | Native unit price | Native line amount |
| --- | --- | --- | --- | --- | --- | --- |
| T01 / INV-01 | T01-L01 | A | USD | 100 | 10.00 | 1000.00 |
| T02 / INV-02 | T02-L01 | A | USD | 100 | 30.00 | 3000.00 |
| T03 / INV-03 | T03-L01 | A | EUR | 200 | 8.00 | 1600.00 |
| T04 / INV-04 | T04-L01 | B | USD | 100 | 20.00 | 2000.00 |
| T05 / INV-05 | T05-L01 | C | USD | 50 | 40.00 | 2000.00 |

Each native line amount equals quantity multiplied by price exactly. No credit notes or invoice amendments are supplied. T02 has no documentation explaining customization, urgency or added components; their possibility remains an alternative to examine, not an established fact.

## Complete benchmark and FX inputs

SYN-004 contains five fictional independent comparison quotes dated Sep 01, 2026. The supplied fixture expressly matches product specification, grade, quantity band, date, market and delivery cost basis for each comparison. There are no freight, tax or service differences. This declared comparability is an assumption of the fictional exercise, not a claim about real market data.

| Benchmark | line_id | USD price per finished unit |
| --- | --- | --- |
| B01 | T01-L01 | 10.00 |
| B02 | T02-L01 | 10.00 |
| B03 | T03-L01 | 10.00 |
| B04 | T04-L01 | 20.00 |
| B05 | T05-L01 | 40.00 |

SYN-005, FX01: the fictional agreed comparison rate on Sep 01, 2026 is **1.25 USD per EUR**. Apply it to both T03 invoice valuation and its funding comparison for this exercise. It is not a retrieved historical exchange rate. USD lines use 1 USD per USD. No other currencies occur.

## Complete shipment inputs, SYN-002

Each row is one distinct consignment with a supplied carrier record confirming the listed shipped quantity. None is a duplicate delivery receipt. Shipment means dispatched within this fixture; final delivery is not independently established.

| Shipment | line_id | Shipped date | Finished units shipped |
| --- | --- | --- | --- |
| S01 | T01-L01 | 2026-09-10 | 100 |
| S02 | T02-L01 | 2026-09-11 | 100 |
| S03 | T03-L01 | 2026-09-12 | 200 |
| S04 | T04-L01 | 2026-09-15 | 60 |
| S05 | T05-L01 | 2026-09-16 | 50 |

SYN-006, A01: a fictional buyer/seller amendment signed Sep 05, 2026 authorizes T04 shipment of 60 units on Sep 15 and the remaining 40 units on Oct 05. No later shipment record is supplied. At the Sep 30 cutoff the remaining portion is scheduled after cutoff. This supports a timing explanation without claiming those 40 units were shipped.

## Complete funding inputs, SYN-003

All rows are distinct actual advances made Sep 02–03, 2026 and expressly allocated to the stated invoice. The complete supplied lifecycle through cutoff records no principal repayment, cancellation or participation relation among these advances. This is a fictional control-total statement; no additional hidden financing is assumed.

| Advance | Trade | Native currency | Outstanding funded principal |
| --- | --- | --- | --- |
| F01 | T01 | USD | 800.00 |
| F02 | T02 | USD | 2400.00 |
| F03 | T03 | EUR | 1200.00 |
| F04 | T04 | USD | 1600.00 |
| F05A | T05 | USD | 1300.00 |
| F05B | T05 | USD | 1200.00 |

F05A and F05B are from different fictional lenders and are separately disbursed amounts, not duplicate copies of one funding notice. Their broader facility and intercreditor terms are not supplied. The packet therefore supports arithmetic overlap against this invoice but cannot establish deception or rule out another permitted funding basis.

## Population reconciliation

Economic input rows = 5 invoices + 5 benchmarks + 1 FX quote + 5 shipments + 1 amendment + 6 advances = 23. Received 23 = processed 23 + duplicates 0 + exclusions 0 + unparsed 0 + inaccessible received records 0 + deferred 0. There are six evidence bundles, five economic trades and six distinct advances; those different units must not be described as the same count.

## Exact expected calculations

T01: 100 × USD 10.00 = USD 1,000.00. Comparable price deviation = (10 − 10)/10 × 100 = 0.0%. Shipped gap = 100 − 100 = 0 units. Finance ratio = 800/1,000 × 100 = 80.0%.

T02: 100 × USD 30.00 = USD 3,000.00. Price deviation = (30 − 10)/10 × 100 = 200.0%, above the illustrative greater-than-50.0% trigger. Difference from benchmark extended value is 3,000 − (100 × 10) = USD 2,000.00; this is not proven illicit value. Shipped gap is zero. Finance ratio = 2,400/3,000 = 80.0%.

T03: 200 × EUR 8.00 = EUR 1,600.00; × 1.25 USD/EUR = USD 2,000.00. Comparable unit price = EUR 8.00 × 1.25 = USD 10.00; deviation = 0.0%. Funding EUR 1,200.00 × 1.25 = USD 1,500.00. Finance ratio = 1,500/2,000 = 75.0%. Shipped gap is zero.

T04: 100 × USD 20.00 = USD 2,000.00; price deviation zero. Shipment gap = 100 − 60 = 40 units, 40.0% of invoice quantity. A01 supports PARTIAL_SUPPORTED because the remaining units are not yet due at cutoff. Finance ratio = 1,600/2,000 = 80.0%.

T05: 50 × USD 40.00 = USD 2,000.00; price deviation and shipment gap are zero. Funding = 1,300 + 1,200 = USD 2,500.00. Finance ratio = 2,500/2,000 × 100 = 125.0%. Difference against invoice = USD 500.00. OVERLAP_REVIEW is required; double-financing fraud is not established.

Native invoice totals: USD 8,000.00 and EUR 1,600.00. Converted invoice value = 1,000 + 3,000 + 2,000 + 2,000 + 2,000 = USD 10,000.00. Native funded totals: USD 7,300.00 and EUR 1,200.00. Converted funding = 800 + 2,400 + 1,500 + 1,600 + 1,300 + 1,200 = USD 8,800.00. Aggregate finance ratio = 88.0%. It does not eliminate T05's individual 125.0% exception.

## Expected conclusions and negative controls

InvoiceReview flags only T02 as REVIEW; other lines are WITHIN_ILLUSTRATION under the stated comparable-price test. InvoiceReview records T04-L01 as PARTIAL_SUPPORTED with a 40-unit gap. ShipmentFinance has five unique trade rows, each with the sum of its line USD values and its financing counted once; T05 is OVERLAP_REVIEW. T01 is the ordinary control. T03 demonstrates the currency false-positive control. All five trades remain visible.

TF-F01 is MEDIUM severity, HIGH confidence, Estimated for the calculated price difference. TF-F02 is HIGH severity, HIGH confidence, Estimated for the funded-principal ratio, with intent unresolved. TF-F03 and TF-F04 are LOW severity and HIGH confidence for their bounded currency and schedule explanations. All recommendations remain Proposed and human disposition is NOT REVIEWED.

Duplicate INV-05: invoice denominator remains USD 2,000.00 after supported deduplication. Change B02 to a different product grade: T02 comparison becomes NOT_ASSESSABLE rather than retaining 200.0%. Remove A01: the T04 40-unit gap remains but its timing explanation becomes unverified. Supply a verified F05B full repayment before cutoff: T05 current funding becomes USD 1,300.00 and ratio 65.0%, with historical advances retained. Record actual recomputation and source changes when performing these checks.

## Separate complete mixed-unit edge case

Run MX01 as a separate fixture; exclude it from all five-trade baseline totals above and from the catalog's default specimen. All records are fictional, with cutoff Sep 30, 2026 5:00 PM ET. One economic invoice MX-INV-01 dated Sep 01 contains two homogeneous lines: grade A finished couplings measured in units and grade D resin measured in kilograms. Currency is USD throughout, so fx_to_usd is exactly 1. There are no taxes, fees, credits, discounts or bundled services. Both lines are due for full dispatch by Sep 20, and no extension or cancellation is supplied.

Complete raw invoice lines, evidence SYN-X01:

| line_id | trade_id | goods_and_grade | quantity_unit | invoice_quantity | unit_price_native | currency | invoice_amount_native |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MX01-L01 | MX01 | Finished couplings grade A | unit | 100 | 10 | USD | 1000 |
| MX01-L02 | MX01 | Resin grade D | kg | 50 | 20 | USD | 1000 |

Complete independent fictional benchmarks, evidence SYN-X02: MX-B01 covers MX01-L01 at USD 10.00 per unit; MX-B02 covers MX01-L02 at USD 20.00 per kg. Both are dated Sep 01 and match the respective specification, grade, market, quantity band and cost basis. No variance adjustment is needed.

Complete shipment allocation, evidence SYN-X03:

| consignment_id | line_id | quantity_unit | shipped_quantity | shipped_date |
| --- | --- | --- | --- | --- |
| MX-S01 | MX01-L01 | unit | 80 | 2026-09-15 |
| MX-S02 | MX01-L02 | kg | 50 | 2026-09-16 |

The supplied carrier population is complete through cutoff for both lines, so no other shipped quantities are implied. The first line has an unexplained 20-unit shortfall after its scheduled date. The second line is complete. Neither record demonstrates final delivery beyond its stated dispatched quantity.

Complete finance input, evidence SYN-X04: advance MX-F01 is one USD 1,500.00 disbursement on Sep 02, allocated to the entire MX01 trade. The complete supplied lifecycle shows zero repayments through cutoff, no other advance, no participation and no line-specific advance allocation. Outstanding principal is USD 1,500.00 once. The line containing a shipment gap does not become an additional funded advance.

Raw-record reconciliation: two invoice lines + two benchmarks + two shipment allocations + one advance = seven received and seven processed economic input records; zero duplicates, exclusions, unparsed, inaccessible received records or deferred records. These records form one economic trade and four evidence bundles. The USD conversion convention does not create another economic record.

The variant's complete Evidence register uses the common 07 schema:

| id | title | locator | claim_class |
| --- | --- | --- | --- |
| SYN-X01 | Fictional mixed-unit invoice | 10-worked-example.md, Separate complete mixed-unit edge case, raw invoice lines MX01-L01 and MX01-L02 | Observed |
| SYN-X02 | Fictional mixed-unit benchmarks | 10-worked-example.md, Separate complete mixed-unit edge case, benchmark statements MX-B01 and MX-B02 | Observed |
| SYN-X03 | Fictional line shipment allocation | 10-worked-example.md, Separate complete mixed-unit edge case, MX-S01 and MX-S02 plus completeness statement | Observed |
| SYN-X04 | Fictional single trade advance | 10-worked-example.md, Separate complete mixed-unit edge case, MX-F01 and lifecycle statement | Observed |

Expected InvoiceReview in the exact 05 schema:

| line_id | trade_id | currency | quantity_unit | invoice_quantity | shipped_quantity | shipment_gap_quantity | shipment_state | unit_price_native | invoice_amount_native | fx_to_usd | invoice_usd | comparable_unit_usd | benchmark_unit_usd | price_variance_pct | price_state | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MX01-L01 | MX01 | USD | unit | 100 | 80 | 20 | UNEXPLAINED | 10 | 1000 | 1 | 1000 | 10 | 10 | 0 | WITHIN_ILLUSTRATION | SYN-X01;SYN-X02;SYN-X03 |
| MX01-L02 | MX01 | USD | kg | 50 | 50 | 0 | COMPLETE | 20 | 1000 | 1 | 1000 | 20 | 20 | 0 | WITHIN_ILLUSTRATION | SYN-X01;SYN-X02;SYN-X03 |

Expected ShipmentFinance in the exact 05 schema:

| trade_id | invoice_usd_total | finance_usd | finance_to_invoice_pct | overlap_state | review_rationale | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| MX01 | 2000 | 1500 | 75 | SINGLE_FUNDING | MX01-L01 has an unexplained 20-unit gap; MX01-L02 is complete in kg; one funded advance only | SYN-X01;SYN-X03;SYN-X04 |

Calculations: MX01-L01 is 100 × USD 10.00 = USD 1,000.00, with 100 − 80 = 20 units unshipped. MX01-L02 is 50 kg × USD 20.00/kg = USD 1,000.00, with 50 − 50 = 0 kg unshipped. Both comparable price variances are zero. Trade invoice total = 1,000 + 1,000 = USD 2,000.00. Finance ratio = 1,500/2,000 × 100 = 75.0%. There is no meaningful combined quantity of 150 or aggregate quantity gap mixing units and kg. Joining the USD 1,500.00 advance to both line rows and summing USD 3,000.00 would be an error; the unique trade table preserves USD 1,500.00.

Expected edge finding MX-F01: MEDIUM severity, HIGH confidence, Observed for the narrow 20-unit shipment gap in MX01-L01, with evidence SYN-X01 and SYN-X03. Propose obtaining a line-specific shipping explanation. Do not characterize the entire invoice as unshipped, infer laundering, or manufacture overlapping finance. The proposal is not executed and human disposition remains NOT REVIEWED. For a negative test, remove the MX-S01 allocation and its line-completeness support: MX01-L01 shipped_quantity and shipment_gap_quantity become null, with NOT_ASSESSABLE, while the trade's funded principal remains USD 1,500.00. Record actual test results separately from these expected outcomes.
