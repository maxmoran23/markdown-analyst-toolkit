# Trade Finance Review — analysis method

## 1. Reconcile documents to trades

Inventory every received document and every economic record extracted from it. Link invoice number, line, buyer, seller, contract and effective version to one trade ID. Assign each homogeneous line its own immutable line_id and preserve the one-trade-to-many-lines relationship. Do not deduplicate separate lines on trade_id alone. Preserve originals, amendments, credit notes, cancellations and duplicates. A document can contain several rows; record both document count and economic-row count without treating them as interchangeable.

Reconcile received rows into processed, duplicate, excluded, unparsed, inaccessible and deferred categories. Then reconcile invoice lines to trade obligations, shipments and funding advances. The absence of a control total limits completeness even if every uploaded document was processed. Keep unresolved joins visible rather than dropping them to obtain a balanced table.

## 2. Validate line arithmetic in native units

For each line calculate invoice quantity × unit price and compare it with the supplied line amount before conversion. Identify discounts, tax, freight or other adjustments explicitly. A tolerance should reflect actual contractual or rounding rules; the fictional example uses exact arithmetic and no adjustments. Do not label an arithmetically correct invoice economically reasonable merely because it multiplies correctly.

Normalize unit names only when their equivalence is supported. One carton may contain multiple pieces; a metric tonne and a short ton are not identical. Preserve conversion factors and their sources. Mixed grades or product bundles require separate lines or a disclosed allocation method. If the allocation cannot be supported, decline the affected unit-price comparison while retaining the invoice total.

## 3. Convert for comparable valuation

Use the documented conversion convention. Invoice USD = native invoice amount × USD per native-currency unit. Comparable unit USD = native unit price × the same supported conversion rate when the contractual basis makes that appropriate. A USD invoice uses a rate of one. If a quoted rate uses the opposite direction, invert it explicitly and show the calculation.

The fictional T03 line is 200 units × EUR 8.00 = EUR 1,600.00. At 1.25 USD per EUR, the invoice is USD 2,000.00 and each unit is USD 10.00. A direct comparison of EUR 8.00 with a USD 10.00 benchmark would invent a 20.0% discount by mixing currencies. The normalized variance is zero. Currency correction can remove an apparent anomaly without establishing every other trade fact.

Native totals should remain visible even where a common currency is used for analysis. Distinguish conversion at disbursement from conversion at the review snapshot. If invoice and funding conversion dates differ, explain the resulting valuation basis. Do not mislabel currency translation movement as extra financing or unexplained trade value.

## 4. Test comparable pricing

Before calculating variance, test benchmark suitability: goods, specification, grade, quantity band, date, market and delivery cost basis. Record the comparison's limitations and source independence. A broad commodity index may be a context indicator while being unsuitable for a customized finished product. A benchmark supplied by the seller may be useful but is not independent confirmation of its own price.

For a valid positive benchmark, price variance percentage = (comparable unit price − benchmark unit price) / benchmark unit price × 100. A null or zero benchmark makes the ratio unassessable; do not divide by zero or use a substitute value. The fixture's review trigger is absolute deviation greater than 50.0%, purely illustrative. Record the direction and amount of a deviation, not just a red flag.

Test legitimate explanations: quality, intellectual property, urgency, small production lot, warranty, freight, insurance, taxes, installation, bundled service, transfer-pricing method or data error. An explanation must fit the actual document terms and have support. It is not enough that a benign explanation is conceivable; conversely, failure to prove it from a limited packet does not prove laundering.

## 5. Reconcile shipment quantities and timing

Aggregate only distinct consignments allocated to the same line_id through cutoff. Avoid counting a carrier manifest and delivery receipt for the same shipment twice. Compare cumulative shipped quantity with that line's invoice obligation in the same unit and specification. Store shipped quantity, gap and status on the InvoiceReview line. Shipment gap = line invoice quantity − supported shipped quantity. Never sum a kilogram gap with a piece gap, or merge grades solely because their unit labels match. A negative gap calls for excess-shipment or allocation review; it is not silently converted to zero.

Interpret timing using the contract and amendments. An approved split shipment can explain a positive gap before the remaining delivery is due. A shipment document dated after cutoff cannot establish delivery by cutoff. Check cancellations, substitutions, returns, tolerances and partial invoicing before describing a discrepancy as unexplained. A shipping gap concerns evidence and timing; it does not by itself demonstrate nonexistent goods.

T04's 100-unit invoice and 60-unit shipment give a 40-unit gap. Its supplied schedule makes the remaining 40 units due after cutoff, so PARTIAL_SUPPORTED is appropriate. If that schedule is removed, the number stays 40 but the interpretation becomes unresolved. Distinguish a numerical change from a change in evidential explanation.

## 6. Reconcile current funded principal

Build the advance-level ledger from distinct actual disbursements less verified linked principal repayments through cutoff. Exclude undrawn commitments and duplicate participations. Translate using the documented analytic basis and assign each amount to a supported invoice or trade. A financing document with no allocation cannot be assigned to the most convenient invoice merely to calculate a ratio.

First aggregate distinct line invoice_usd values to one invoice_usd_total per trade_id. Then join the separately deduplicated trade funding ledger to that unique trade total. Finance-to-invoice percentage = attributed outstanding funded principal / comparable trade invoice_usd_total × 100. Store each trade's finance_usd once in ShipmentFinance; never attach a full advance to every line and sum the expanded rows. The fixture's review trigger is greater than 100.0%, an illustration that directs examination of allocation and possible overlapping finance. It is not a universal maximum advance rate. Fees, other collateral, receivables pools and approved facility terms can change the correct denominator or legitimate financing structure.

T05 has two distinct advances expressly allocated to the same invoice: USD 1,300.00 and USD 1,200.00, with no repayments or participation relationship supplied. Total current principal is USD 2,500.00 against USD 2,000.00 invoice value, or 125.0%. The USD 500.00 difference is an arithmetic excess against this denominator, not proved illicit proceeds, loss or double-financing fraud. Obtain the allocation and intercreditor evidence that could change the interpretation.

## 7. Aggregate without hiding concentrations

Sum invoice and funded values only after native-currency and allocation reconciliation. Portfolio invoice value can be summed from distinct InvoiceReview lines or from unique ShipmentFinance trade totals; both results must agree. Portfolio funding comes only from unique trade-level financing rows. A many-to-one display join is permitted for navigation but not as a new source of additive trade totals. In the fixture, invoices total USD 10,000.00 and finance USD 8,800.00, yielding an aggregate 88.0% ratio. That portfolio ratio does not remove the individual T05 125.0% exception. Summing percentages or averaging trade percentages without stating weights would answer a different question.

Count price, shipment and financing anomalies separately, then identify their overlap by trade ID. Do not sum affected invoice values across overlapping flags without deduplicating the union. The same document defect may explain several symptoms; multiple flags are not automatically independent corroboration. Preserve all benign and unresolved trades in the population.

## 8. Form a bounded recommendation

Describe the observed discrepancy, expected contractual or illustrative criterion, relevant evidence and strongest alternatives. Name what information could resolve it and who must make any operational decision. A price review may need comparable product terms; a shipment review may need a consignment update; a funding review may need current lender allocation. Do not request every possible document when a narrower fact would settle the question.

Conclude at the strength of the evidence. The fictional case supports a price inquiry and a funding-overlap inquiry. It also demonstrates that currency normalization and an authorized partial shipment can explain apparent anomalies. It does not establish money laundering, fraudulent documents, a sanctions breach or a duty to reject an instrument.
