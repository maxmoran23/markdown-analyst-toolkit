# OSINT Research — quality review

## Domain checks and negative controls

| Check | Test input or procedure | Expected result |
| --- | --- | --- |
| OS-Q01 | Two articles repeat the same press release | One independent source family, with copy lineage retained |
| OS-Q02 | Similar name, different registry number | No merged identity and no transferred adverse event |
| OS-Q03 | Register inaccessible for one of five planned searches | Completion remains four of five, not four of four |
| OS-Q04 | Historical “active” record and later “expired” status | Two dated facts; no automatic conflict without matched period |
| OS-Q05 | Remove primary support for a material claim | Confidence or status changes; citation is not retained as reviewed |
| OS-Q06 | Search returns no result with one spelling only | Negative statement bounded by query and language |
| OS-Q07 | Article describes an allegation later withdrawn | Procedural outcome retained; allegation not presented as finding of fact |
| OS-Q08 | Same total copied into three outputs | Recalculate once from raw claim rows and compare all three |

In the worked example, expect four claims: one SUPPORTED, one CONTRADICTED, one UNRESOLVED, and one IDENTITY UNRESOLVED. Five planned searches have four reviewed rows and one access-limited row. Six source items were reviewed; five are eligible; two articles add no new independent origin to the employee claim. These are expected results of invented data, not an operational quality score.

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
