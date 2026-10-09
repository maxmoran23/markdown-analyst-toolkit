# Digital Asset Review — quality review

## Domain and adversarial checks

| Check | Test input | Expected result |
| --- | --- | --- |
| DA-Q01 | 100000000 atomic units, decimals 6 | 100.000000 display units |
| DA-Q02 | Same atomic amount, unknown decimals | No human-unit quantity invented |
| DA-Q03 | Duplicate event across two pages | One event, one duplicate, preserved lineage |
| DA-Q04 | Two logs in one transaction with different indices | Both retained |
| DA-Q05 | Failed attempted 20-unit transfer | Excluded from settled outflow; attempt retained |
| DA-Q06 | Five-unit self event | Separate SELF total, no directional inflation |
| DA-Q07 | One atomic unit unsolicited inbound | 0.000001 retained; no intent inference |
| DA-Q08 | Same ticker on a different contract | Separate asset total |
| DA-Q09 | Remove execution status | UNKNOWN and excluded from settled totals |
| DA-Q10 | Vendor label without supporting evidence | UNVERIFIED LABEL, not identified owner |
| DA-Q11 | Partial capture with net positive flow | No unsupported ending-balance claim |
| DA-Q12 | Atomic integer longer than spreadsheet precision | Preserved as exact text |

For the fixture, expect six raw rows, one proven duplicate, five unique records, four eligible successful events, and one failed attempt. Directional totals are 100.000001 PAPER in and 40.000000 PAPER out; self activity is 5.000000 PAPER; captured net directional flow is 60.000001 PAPER. Counterparty eligible-event counts sum to four. No fiat value or real-world attribution is established.

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
