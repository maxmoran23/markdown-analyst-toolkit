# Transaction monitoring: quality review

## Release checks with falsifiable expectations

| Check | Expected evidence | Failure consequence |
| --- | --- | --- |
| Raw reconciliation | Each raw ID assigned once; received equals terminal buckets | DRAFT; repair population ledger |
| Duplicate logic | R09 excluded as exact duplicate of R01; independent equal-amount payments retained | DRAFT; recompute totals |
| Amount completeness | R10 remains unknown; D flagged incomplete; no zero imputation | DRAFT if any complete-coverage claim remains |
| Currency separation | Totals by ISO currency; conversions fully recorded if used | DRAFT; remove invalid combined sum |
| Own-transfer exclusion | C gross totals retained; eligible totals zero with ownership evidence | DRAFT; fix hidden suppression |
| Ratio arithmetic | A 0.95; B 0.96; C and D null | DRAFT; fix calculation and displays |
| Rule/review distinction | A and B both MATCH even though B is explained | DRAFT; restore raw hit count |
| Denominator | Match rate, if shown, states the eligible assessed account count | Remove ambiguous percentage |
| Time ordering | A 2 hours; B 3 hours; precredit debit cannot satisfy rule | DRAFT; fix sequencing |
| Evidence trace | Every finding ID links to exact rows and context | Unsupported finding remains open |
| Decision boundary | No filing, hold, release, suppression, or exit marked executed | Correct the action record |

## Negative and boundary controls

Run these as separate synthetic perturbations, not additions to the base population. With eligible credits 5,000.00 and debits 4,500.00 after exactly 24 hours, TM-01 matches because all operators are inclusive. Change credit to 4,999.99 while preserving a 0.90 ratio: no match on minimum credits. Change ratio to 0.8999: no match on ratio. Change time to 24 hours and one second: no match on time. A debit one second before the first credit is not subsequent. Null amount returns NOT_ASSESSABLE even if other known rows would match.

Duplicate R01 again: raw count increases, canonical amounts and matches do not. Change the duplicate amount without changing its identity: the expected result is a conflict exception, not arbitrary retention. Remove C's ownership evidence: the expected result is an unresolved exclusion basis; do not continue displaying confirmed ownership. Remove B's invoice: B remains a numerical match and loses the supported-explanation outcome.

## Coverage and performance checks

Do not calculate detection recall from the alerted population. Do not label analyst closure rate as precision without adjudicated labels and a defined positive class. Show sample size and selection for any reviewed sample. If only some matches have been investigated, show reviewed and unreviewed counts separately. An unreviewed match cannot be assumed false positive or true positive.

Inspect at least one narrative amount against the canonical ledger, one row after filtering, one omitted/unknown row, and one chart tooltip. Reconcile the report's headline metrics to workbook calculations and dashboard data. Ensure rounded percentage displays do not change threshold decisions. Test text-only delivery when a format cannot be created.

## Review record

Record reviewer name/role, review timestamp with timezone, checks performed, failed checks, corrected items, residual limitations, and release status. Use PASS only for an actually performed check with the expected result. Use NOT TESTED for unperformed checks and explain impact. Analyst self-review and independent review are distinct fields. A user accepting a file download is not analytical signoff.

Permissible analytical releases are DRAFT, READY FOR HUMAN REVIEW, or REVIEWED WITH RECORDED LIMITATIONS. Operational disposition remains in the authorized process. In the worked example, the package can be READY FOR HUMAN REVIEW while account D remains NOT_ASSESSABLE; it cannot be described as a complete assessment of all four accounts.
