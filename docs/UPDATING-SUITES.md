# Update a suite without losing the case history

Download the entire new suite from one versioned release. Keep the previous folder
and any case outputs in your approved location until the transition is reviewed.
Do not combine an old decision-rules file with a new renderer simply because their
filenames match.

1. Read the release notes and the selected suite's build record. Confirm the suite ID,
   version and twelve-file inventory. The release manifest and checksums support
   maintainer verification; ordinary use does not require a terminal.
2. Finish or save the current case checkpoint, including source versions, every domain
   row, assumptions, calculations and unresolved checks. Label its originating version.
3. Start a new session with the new suite's Example check stage. Reproduce the printed
   example and negative controls. Preserve the actual result; a prior-version pass
   does not establish current behavior.
4. Compare the method and output contract before moving an existing case. Identify
   changed fields, units, thresholds, source applicability, missing-value treatment,
   review gates and capability assumptions. Record “no change found” only for the
   material actually compared.
5. Reapply affected calculations and judgments to the same source snapshot. Show old
   and new results, with the reason for each difference. If source data also changed,
   separate the effect of the new method from the effect of the new evidence.
6. Keep the earlier report distinguishable. Request the required human review for any
   changed consequential recommendation. Re-render only after the updated case record
   is reconciled.

## What is stable and what still needs review

| Surface | Release intention | User check |
| --- | --- | --- |
| File roles | Twelve suite files, ten instructional attachments | Inventory and readable content |
| Versioned downloads | Prior releases remain separately addressable | Download the intended version |
| Domain schemas | Fixed within the selected suite/version | Compare old and new file 05 before migrating a case |
| Report/workbook/dashboard | Generated from one canonical specimen structure | Actual case values, formatting and untested capabilities |
| Public authority references | Dated and scoped method context | Reconfirm applicability and current status for the actual decision |
| Model behavior | No deterministic-output guarantee | Rerun the example and inspect the new session's work |

For a rejected or unusable new result, keep the verified prior artifact and the failed
new draft clearly labeled. Do not silently relabel one as the other. A rollback of the
presentation does not reverse a factual correction; retain the correction and the
reason the new rendering was not accepted.
