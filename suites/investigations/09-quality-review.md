# Investigation review: quality review

## Required checks

| Check | Expected result in the example | Failure implication |
| --- | --- | --- |
| Source reconciliation | 8 received = 6 processed + 1 duplicate + 1 inaccessible | Case coverage overstated |
| Event count | 6 chronology rows; only 3 monetary events | Documents mistaken for payments |
| Invoice treatment | Face amount 10,000.00 USD appears in detail, not event amount | Gross flow inflated |
| Amount difference | 11,000 − 10,000 = 1,000.00 USD | Discrepancy misstated |
| Net unreversed | 11,000 − 2,000 = 9,000.00 USD | Return ignored or overapplied |
| Return fraction | 2,000/11,000 = 18.1818...%, display 18.2% | Wrong denominator |
| Knowledge vs event time | Later explanation does not become contemporaneous proof | Retrospective certainty |
| Hypothesis H-01 | UNRESOLVED; invoice does not fully reconcile | Premature benign closure |
| Hypothesis H-03 | CONTRADICTED by partial return arithmetic | Full reversal falsely claimed |
| Human gate | No case closure or filing shown as executed | Unauthorized consequential decision |

## Negative and opposite controls

If a verified contract explains 1,000.00 USD transport and confirms Supplier-Q as the settlement agent for Supplier-R, H-01 may become supported for this payment after the evidence is reviewed. Preserve the original discrepancy and its resolution. If the new document is only a customer assertion, increase the evidence inventory but do not promote the claim to Observed fact.

If the return is unlinked to EV-03, do not subtract it from that payment's net unreversed amount. The report should show a known debit of 11,000.00 USD and a separate 2,000.00 USD credit with unresolved linkage. If a second confirmed 9,000.00 USD return arrives, cumulative linked returns become 11,000.00 USD and net unreversed becomes zero; purpose and original-event questions do not automatically disappear.

If an invoice copy has a changed beneficiary or amount, it is a conflicting version rather than an exact duplicate. If the original contract becomes accessible, it moves from inaccessible to processed with a versioned reconciliation; it is not silently added without changing counts. If event timestamps lose timezone information, hour-level sequencing becomes unverified.

## Claim challenge

Select the strongest assertion in the report and identify every supporting premise. Test whether source wording establishes that premise or only reports it. Remove dependent summaries and repeated-origin sources from the corroboration count. A claim that survives only because an assistant repeated it is unsupported.

Review both concern and mitigation. A customer explanation can be plausible without being corroborated. An invoice discrepancy can be real without proving forgery. A rapid sequence can be observed without proving tracing. Ensure the report uses the narrowest accurate wording and gives the reviewer enough evidence to disagree.

## Visual and file review

Compare timeline order in report, workbook, and dashboard. Verify that null amounts remain blank or null and are not plotted as actual zero-value transactions. Confirm document face values cannot enter flow totals. Ensure the dashboard's filter clearly distinguishes events from sources and hypotheses. Exported files must retain evidence IDs, limitations, and status.

Check date formatting and timezone, exact header order, currency notation, hyperlink destinations, and text escaping. Test the fallback when a downloadable file cannot be created: the same schema must be supplied in chat with no fabricated link. Do not state that an inaccessible source was reviewed.

## Signoff and residual issues

Record actual reviewer, role, timestamp, scope reviewed, test results, corrections, unresolved limitations, and decision authority. Independent review must be identified as such only when actually performed. The expected example release is READY FOR HUMAN REVIEW with an unresolved contract and supplier bridge. It is not a closed case or a filing recommendation.

A reviewer can accept the arithmetic while challenging the hypothesis assessment. Capture that distinction. Retain the final decision, rationale, and evidence in the authorized system only through the actual approved workflow; this attachment suite merely prepares the review package.
