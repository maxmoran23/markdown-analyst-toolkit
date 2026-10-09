# Quality review — Source of Wealth and Funds Review

## Wealth and funds checks

| Check | Input | Expected result |
| --- | --- | --- |
| WF-Q01 | Opening assets 400000,600000,500000; debt 200000 | Net $1,300,000.00 |
| WF-Q02 | Salary 300000 less paid tax 90000 | Net cash and wealth $210,000.00 |
| WF-Q03 | EUR100000 at 1.20 USD per EUR, tax USD30000 | Net $90,000.00 |
| WF-Q04 | Inherit 4000 units at USD100 | Wealth +$400,000.00, cash zero |
| WF-Q05 | Sell 2000 units for USD250000 gross, costs 30000 | Net cash $220,000.00; net wealth +$20,000.00 |
| WF-Q06 | Remaining 2000 units at USD100 | Inherited holdings $200,000.00 |
| WF-Q07 | Revaluations 100000 and 60000 | Wealth +$160,000.00; cash zero |
| WF-Q08 | All eleven bridge rows | Wealth $2,060,000.00; cash $800,000.00 |
| WF-Q09 | Five allocations plus duplicate advice | Proposal $600,000.00; supported $540,000.00 |
| WF-Q10 | F06 repeats SALE01 | Zero extra allocation or support |
| WF-Q11 | Third-party proposal not settled | Excluded from owned wealth and cutoff cash |
| WF-Q12 | Change proposed transfer date after cutoff | No backdated cash movement |

Independently rebuild the closing asset values rather than relying only on the bridge total. Confirm gross assets $2,260,000.00 minus debt $200,000.00 equals $2,060,000.00. Recalculate the cash balance directly from gross-to-net events and expenses. Check that taxes appear once and that inheritance and sale are linked through the same units. A row count alone will not catch double-counted economic events.

Negative tests must reject adding $220,000.00 as incremental disposal wealth, adding the duplicate sale advice to funding, treating unrealized appreciation as cash, using the reciprocal FX rate, or interpreting 90.0% support as approval. Test a zero proposed amount separately: the coverage fraction is null because its denominator is zero, not 100%. If all sources are unsupported, the support amount can legitimately be zero while the allocation denominator remains positive.

The fixture's bridge is a consistency exercise using invented records. A successful calculation cannot establish tax compliance, beneficial ownership, document authenticity, lawful provenance, or liquidity in a real account. Record those limits next to the conclusion and preserve unperformed source or artifact checks as NOT RUN.


## Artifact consistency and release gate

Perform checks against the populated outputs, not against the template's existence. For each check record check_id, expected_result, observed_result, status, evidence_or_location, reviewer, and follow_up. Use NOT RUN when the necessary environment is unavailable. A reviewer name remains UNASSIGNED until a real person performs that role. The assistant may record its own mechanical self-check but cannot invent independent review.

Verify that all report headings are present in order; the workbook preserves every tab and column required by 05 and 07; the dashboard uses the same evidence cutoff, counts, units, and finding IDs. A filtered dashboard count must identify its filter. Exported tables must contain all records, including unassessed and excluded records with reasons. Confirm that source URLs are validly formatted and that citations point to the claimed section; opening a link is not a content check.

Check the actual generated workbook for truncated identifiers, converted dates, scientific notation, missing leading zeros, formulas stored as text, and spreadsheet formula injection. Treat imported text beginning with spreadsheet control characters as literal text. Retain the original value in the evidence record. Use numeric cells for ordinary bounded numbers, and text for long exact identifiers or integers whose precision would be lost. If formulas are present, inspect their ranges and cached results; do not assume the file generator calculates them.

For HTML, inspect light and dark modes, readable text contrast, wrapped long labels, keyboard focus, filter reset, empty search results, printed output, and narrow screens when a browser is available. All data and styling must work offline. Escape source text before inserting it into HTML; no external scripts, fonts, tracking pixels, or live data requests are required. If browser inspection was not performed, say so. Do not promote a syntactic HTML check into a claim of visual accessibility compliance.

## Reviewer challenge sequence

Pick the strongest consequential conclusion and try to disprove it. Identify the minimum fact whose reversal would change the decision. Check whether an apparently independent source actually copied another. Recalculate one quantitative result from raw rows without using the displayed total. Read a contradictory record in its original context. Inspect at least one excluded row and one low-severity item to check asymmetric treatment.

Then repeat with an intentionally missing critical field. Expected result: uncertainty becomes visible and a relevant conclusion is qualified or withheld. Next substitute a plausible benign explanation. Expected result: the explanation is evaluated with evidence rather than rejected because the case already has a flag. Finally remove all example data. Expected result: no fictional name, amount, result, or conclusion remains in the live output.

## What passing means

A passing self-check means the specified checks were performed and their expected results were observed on these inputs. It does not establish compliance, investigative accuracy, detection sensitivity, model reliability, universal platform support, or independent validation. Synthetic cases demonstrate arithmetic and decision behavior on constructed examples only. Report failures and tests not run next to the decision, with a responsible role and the exact next evidence needed. Do not hide them in an appendix while the cover declares the case complete.
