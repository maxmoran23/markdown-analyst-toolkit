# Trade Finance Review — output contract

## Delivery and canonical record

Use the active stage in 01. Full workflow delivers the fixed report, workbook or complete exact tables, and optional offline dashboard. Analyze preserves the complete case record for later rendering. Render uses that saved record without inventing new analysis. Place **DRAFT — HUMAN REVIEW REQUIRED** and the evidence cutoff prominently until a named human disposition is evidenced.

The common tabs are Summary, Dashboard, Findings, Evidence, Actions and QA. **Their exact columns and accepted common-field states are defined in 07.** Do not add required common columns that the template lacks. Preserve richer source metadata, severity and confidence rationale, counterevidence, action evidence, reviewer notes and QA expectations in the complete case record and relevant existing text fields or report sections. The two domain tables below are additional; retain their exact names, column order and row identifiers.

## Fixed report headings

1. Trade review decision brief
2. Scope, economic trades and calculation basis
3. Material anomalies and legitimate alternatives
4. Invoice-line price and shipment reconciliation
5. Trade totals and financing reconciliation
6. Evidence and document lineage
7. Proposed trade clarification actions
8. Limitations, quality checks and human disposition

Section 1 answers the decision question and names the unresolved gate. Section 2 states the population, timing, inclusion rules and calculation approach. Section 3 explains findings and alternatives. Sections 4 and 5 contain the first and second domain registers respectively. Section 6 carries exact evidence locators. Section 7 states proposed actions and actual human decisions separately. Section 8 records limitations, actual QA and unrecorded disposition.

## Domain tables and types

### InvoiceReview

Exact immutable header:

```text
line_id | trade_id | currency | quantity_unit | invoice_quantity | shipped_quantity | shipment_gap_quantity | shipment_state | unit_price_native | invoice_amount_native | fx_to_usd | invoice_usd | comparable_unit_usd | benchmark_unit_usd | price_variance_pct | price_state | evidence_ids
```

One row per homogeneous economic invoice line. line_id is required stable text and globally unique within the case; trade_id is required stable text and may repeat across lines of one economic trade. Preserve the source invoice number, line number and product/grade in the evidence locator and complete case record. Never use trade_id alone as the line key. currency is the native ISO code. quantity_unit preserves the line's unit, and invoice_quantity is a positive decimal in that unit. shipped_quantity is cumulative distinct shipment quantity allocated to that line through cutoff; shipment_gap_quantity equals that line's invoice_quantity minus shipped_quantity. Both are null if allocation or comparable units cannot be established. shipment_state is COMPLETE, PARTIAL_SUPPORTED, UNEXPLAINED or NOT_ASSESSABLE. Do not add kilograms, pieces, cartons or different product grades into a trade-level quantity or gap.

unit_price_native and invoice_amount_native are decimals in native currency. fx_to_usd is USD per one native-currency unit, explicitly one for USD. invoice_usd is this line's derived USD value, not the whole invoice repeated on every line. comparable_unit_usd and benchmark_unit_usd are prices per that line's stated unit; the benchmark is null if comparability fails. price_variance_pct contains percentage points, such as 200 for 200.0%, not 2. price_state is WITHIN_ILLUSTRATION, REVIEW or NOT_ASSESSABLE. evidence_ids must include both valuation and line-specific shipping support and resolve to Evidence. Zero shipped quantity requires a complete relevant source basis; unknown shipment is null, not zero.

### ShipmentFinance

Exact immutable header:

```text
trade_id | invoice_usd_total | finance_usd | finance_to_invoice_pct | overlap_state | review_rationale | evidence_ids
```

Exactly one row per unique economic trade_id, with a many-lines-to-one-trade relationship from InvoiceReview. invoice_usd_total equals the sum of all distinct, complete line invoice_usd values for that trade. If any required line value, conversion or population completeness is unresolved, the total is null; preserve any known subtotal and missing-line count in review_rationale. finance_usd is attributed outstanding funded principal counted once per distinct economic advance and translated on the stated basis. It is never copied onto each invoice line for summation. finance_to_invoice_pct equals finance_usd / invoice_usd_total × 100 and is null if either operand or the positive denominator is unassessable. Funded value is not a loss.

overlap_state is SINGLE_FUNDING, OVERLAP_REVIEW or NOT_ASSESSABLE. SINGLE_FUNDING indicates one evidenced current funded advance, not universal clearance; multiple documented participations in one economic advance are consolidated first. review_rationale summarizes line-specific shipment issues by line_id without inventing an aggregate quantity, and states legitimate financing alternatives and missing support. evidence_ids are semicolon-delimited source IDs. Trade-level sums must use this unique trade table; an expanded join to multiple lines must not repeat invoice_usd_total or finance_usd in portfolio totals.

## Evidence, interpretation and display

Findings require a stable ID, condition, criterion, source locator, impact, severity rationale, confidence rationale, counterevidence and recommended next step. Place these explanations in the supported fields and report narrative. Claim class is Observed, Reported, Inferred or Estimated. Severity is HIGH, MEDIUM or LOW. Confidence is HIGH, MODERATE, LOW or NOT ASSESSABLE. A low-confidence concern may warrant urgent information gathering without becoming an established violation.

An evidence ID must resolve to Evidence and a precise source passage. Reserve SYN- identifiers for the fictional case and REF- identifiers for method references. Semicolon-delimit multiple IDs in domain cells; do not fabricate an evidence relationship from a similar-looking record number. Evidence title and locator fields may carry dates and availability when required by the case record. A bare URL is insufficient when the conclusion depends on a particular paragraph or table row.

Numbers remain numeric in workbooks and JSON. Missing values are empty spreadsheet cells, JSON null and Markdown null with a stated reason; zero means a supported measured zero. Native currency, quantity and date units must be visible. Show money to two decimal places with the currency identified, percentages to one decimal, counts as integers, and timestamps with timezone. Percentage-point columns contain values such as 25.0, not the fractional value 0.25; use an explicit percent-sign display, not a spreadsheet percentage conversion. Round at display, after calculations.

All filters must disclose hidden rows and preserve the full-population denominator separately. Unknowns appear as gaps or a distinct unresolved category. Do not draw a zero bar for missing evidence. No artifact may silently drop a contrary finding, represent a selected sample as the whole population, or present a source allegation as an adjudication.

## Release and fallback

The example contains five economic trades and six distinct finance advances. A duplicate copy of an invoice is not a second trade. A lender participation or disclosed refinancing can explain several documents without two outstanding advances; only actual funded principal with current allocation enters the overlap calculation. State that the illustrative price trigger is greater than 50.0% absolute comparable-price deviation and the overlap trigger is greater than 100.0% finance-to-invoice value. Neither is a regulatory threshold or proof of laundering.

Every artifact must preserve the scope, cutoff, source population reconciliation, finding count, principal totals, unresolved cases and human status. A narrative may show a wide record vertically for readability; the workbook still keeps every exact column. Test long source locators and literal text for truncation. Maintain readable light and dark presentation without remote assets. If export or browser testing is unavailable, use complete text tables and state the delivery checks NOT RUN.

Actions default to Proposed in the common action register. Accepted means a recorded human acceptance, not execution. Closed requires closure evidence in the case record. Do not invent owners, deadlines, approvals or completed outreach to fill a template. The final limitations must identify the actual missing fact and its effect, rather than rely on a generic disclaimer. Keep unresolved material defects visible even when other checks pass.
