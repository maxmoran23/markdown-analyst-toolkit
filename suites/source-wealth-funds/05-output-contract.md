# Output contract — Source of Wealth and Funds Review

## Package and interchange rules

The final package contains a report, workbook, and optional dashboard, plus a visible limitations and QA statement. Use the report headings listed below in exactly that order. Do not rename the workbook tabs or rearrange the domain columns. The common tabs are Summary, Dashboard, Findings, Evidence, Actions, and QA; their exact schemas and styles are in 07-workbook-template.md. Append the two domain tables described here after those common tabs. Templates 06 through 08 control presentation; this file controls analytical semantics.

Identifiers, codes, and source locators are text even when they look numeric. Counts are nonnegative integers; rates are numeric fractions from zero to one and display as percentages to one decimal. Retain the numerator and denominator that produce each rate. Amounts must include an explicit currency and must not be summed across currencies without a named conversion method. Use ISO dates in machine tables and human-readable dates in narrative. A date with an unknown timezone cannot establish an intraday ordering.

Represent an unknown numeric or date value as a blank cell with an explicit explanation in the associated notes, limitation, or QA row. In text interchange use null. Never use zero, a dash, or N/A as a numeric stand-in. Distinguish Unknown, Not supplied, Not applicable, Not tested, and Unreadable in explanatory text. A true zero is a measured result. A zero denominator yields null, not a zero rate. Do not silently exclude failed or unassessed records from the denominator.

Keep evidence IDs as stable strings, separated by semicolons when a table cell needs multiple IDs. Findings must identify the affected population, factual observation, criterion, consequence or uncertainty, recommendation, alternative, and reviewer decision needed. Preserve severity, confidence, and claim class as distinct fields. Actions have a role owner, dependency, expected evidence of completion, and an unapproved proposed due date where relevant. Do not fabricate a person's acceptance or a completed review.

Avoid formulas that depend on locale-specific text interpretation. When calculation tools are available, store numeric values as numbers, preserve formulas where the format supports them, and check cached results or recalculate after reopening. When using text tables, give formulas in a method note and supply reconciled computed values. The same totals must appear in the report, workbook, and dashboard. Format discrepancies are QA failures when they alter meaning.

The dashboard is a view of the same evidence and decisions. Filters must show the denominator used; a filtered count cannot silently replace the full population count. Color accompanies text, never replaces it. Keep the supplied restrained light and dark themes, accessible contrast, visible selected filters, and an explicit fictional-data banner for the example. No external network resources, live source fetches, auto-sends, or operational changes belong in the dashboard.


## Required report heading order

1. Wealth and funds conclusion
2. Scope valuation dates and reconciliation method
3. Material provenance findings
4. Wealth accumulation bridge
5. Proposed funding trace
6. Evidence chain and alternative explanations
7. Proposed corroboration actions
8. Limitations quality review and human disposition

## Domain table: WealthBridge

Exact ordered columns: event_id, event_date, event_type, original_amount, original_currency, fx_usd_per_unit, usd_wealth_change, cash_effect_usd, evidence_ids, notes.

event_id is unique text. event_date is the date used in the fictional bridge. original_amount is the signed source amount before the event-specific reconciliation described in notes; it may be gross income, gross sale proceeds, or a valuation change. original_currency preserves its unit. fx_usd_per_unit is numeric USD per one original-currency unit. It is one for USD. Do not sum original_amount across unlike currencies or event types.

usd_wealth_change is the event's signed net contribution to the fixture's cumulative wealth bridge. Opening components are included as rows, so the column sum equals closing net wealth. cash_effect_usd similarly includes opening cash and subsequent cash changes. The sale row's original gross value $250,000.00 becomes a $20,000.00 wealth change and $220,000.00 cash effect after removing carrying value and deductions. notes preserves that reconciliation.

Unknown contributions are null and prevent a claim of complete reconciliation. Negative values are legitimate deductions and liabilities, not errors to remove. Monetary cells are numbers formatted to two decimals; reporting currency is explicit in the column names. FX displays four decimals but calculations retain necessary precision. This table has eleven baseline rows.

## Domain table: FundingTrace

Exact ordered columns: trace_id, origin_type, economic_event_id, net_available_usd, allocated_usd, supported_usd, link_status, evidence_ids, notes.

trace_id is a unique document/allocation row. economic_event_id links documents to the same underlying event; it is intentionally repeated for F03 and F06. net_available_usd describes the row's claimed or supported underlying amount with status in link_status; this column is nonadditive across duplicate event rows. allocated_usd is the proposed included amount. supported_usd is the portion supported under the fixture standard, from zero through allocated_usd. The known unsupported F05 allocation has supported_usd zero because none of its claimed origin is supported in the fixture, not because its amount is unknown.

link_status is SUPPORTED_ALLOCATION, UNRESOLVED, or DUPLICATE_EXCLUDED in the example. A duplicate has allocated_usd and supported_usd zero, with its original evidence amount retained in net_available_usd for reconciliation. Sum allocated_usd for the $600,000.00 proposal and supported_usd for $540,000.00. Do not sum net_available_usd to calculate wealth, liquidity, or funding. Six rows include five proposed sources and one duplicate advice record.

## Cross-output requirements

The report must state the separate wealth and proposed-funds dates, opening net wealth, net movement, closing assets and liabilities, cash, and the allocation gap. It must show the inheritance-to-sale quantity bridge, the EUR dividend conversion, gross-to-net deductions, and duplicate handling. Show the 90.0% allocation share as descriptive evidence coverage. Use the fixed common tables in 07 for findings, actions, and QA; do not require common columns absent from that template.

An offline dashboard can display the bridge and allocation side by side. It cannot label the wealth number “verified assets” or the coverage percentage “approval likelihood.” A filter that hides F05 must show the filtered scope and preserve the full-proposal gap nearby. Never allow an example source label to survive into a different case's output without explicit fixture status.
