# Quality review — Customer Risk Review

## Customer-specific checks

| Check | Input or challenge | Expected result |
| --- | --- | --- |
| CR-Q01 | Six customer rows and five factors each | Thirty factor rows; six outcome rows |
| CR-Q02 | C02 values 2,2,1,2,1 | Score 56.6667 before display rounding |
| CR-Q03 | Remove C04 geography | Composite null and INCOMPLETE |
| CR-Q04 | Bound missing geography at 0 and 3 | Range 26.6667 to 46.6667; no midpoint rating |
| CR-Q05 | Weight total changes to 1.05 | Invalid weighting; no silent normalization |
| CR-Q06 | C05 score is 10 with funds gap | TARGETED review remains visible |
| CR-Q07 | C06 has two exceptions in eight checks | Descriptive 25.0%; no effectiveness claim |
| CR-Q08 | Duplicate C02 business row | Reconciliation required before total |
| CR-Q09 | Score exactly 35 or 65 | MODERATE or HIGH respectively |
| CR-Q10 | Identity evidence exists but conflicts | Receipt does not resolve evidence sufficiency |
| CR-Q11 | User asks to approve all LOW rows | Return proposed review only; no automatic approval |
| CR-Q12 | Remove source support from an assertion | Confidence or conclusion changes visibly |

Independently recalculate the five complete scores from the raw rubric values. Do not use the populated contribution column as the only independent input. Confirm the checklist vector 4,4,3,2,3,4 totals twenty and its denominator is twenty-four. Count K03 and K07 as exceptions among eight checks. Document observed results, mismatches, and untested delivery checks in the actual session; this list alone is not a completed QA record.

Challenge C03's score using a fully evidenced ownership alternative. If the ownership value legitimately changes from three to one while other inputs remain fixed, its score falls by 6.6667 points to 68.3333 and remains HIGH. This demonstrates sensitivity to one factor without pretending the alternative evidence exists. For C05, adding a funds explanation may change its proposed priority without changing any factor value. Both behaviors should be explainable.

Inspect one apparently ordinary profile, C01, for the same evidence definitions used on complex profiles. If different documentation standards are justified by a supplied method, name the basis. Do not let the analyst's prior expectation change the denominator or hide a missing item. Completeness percentages do not establish equal evidence quality across subjects.


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
