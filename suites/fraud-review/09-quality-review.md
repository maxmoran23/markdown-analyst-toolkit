# Fraud review: quality review

## Falsifiable checks

| Check | Expected result | Failure significance |
| --- | --- | --- |
| Source population | 8 source records, 4 cases; no duplicates or exclusions | Missing or double-counted incident |
| Requests | 40,000 + 15,000 + 12,000 + 5,000 = 72,000.00 USD | Request and execution confusion |
| Known executions | F01 40,000 + F02 0 + F04 5,000 = 45,000.00 USD; F03 unknown | False complete-total claim |
| Linked returns | F01 10,000.00 USD; F03 unknown | Requested recovery counted as realized |
| F01 net | 40,000 − 10,000 = 30,000.00 USD | Incorrect exposure arithmetic |
| F02 state | NOT_EXECUTED, executed 0, unreturned 0 | Attempt counted as loss |
| F03 state | Execution, returns, net all null | Missing evidence converted to favorable zero |
| F04 treatment | 5,000.00 USD flow retained; excluded from suspected-fraud subtotal | Ordinary activity labeled loss |
| Known suspected-fraud subtotal | 30,000.00 USD with F03 gap disclosed | Misleading complete exposure |
| Action state | All next steps proposed; none executed | Invented operational activity |

## Opposite and edge tests

Change F01's return to “requested, pending” without a posted credit. Confirmed return becomes unknown or zero only if complete evidence establishes no realized return as of the timestamp; do not subtract the requested 10,000.00 USD. The package must disclose the pending status and avoid keeping a falsely reduced net figure.

Add a second system copy of the same confirmed return reference. The canonical return stays 10,000.00 USD. Add a distinct confirmed 5,000.00 USD linked return: cumulative returns become 15,000.00 USD and F01 net becomes 25,000.00 USD. Add an unlinked 5,000.00 USD credit: no change to F01 until linkage is established.

Supply F03 with a confirmed rejected instruction and complete no-execution status: executed becomes zero and the incident changes from unknown execution to an unexecuted request after review. Supply a confirmed 12,000.00 USD debit instead: executed becomes 12,000.00 USD; recovery and net remain unknown until return coverage is established. Do not fill both fields from the complaint.

Remove F04's independent verification record: the ordinary explanation weakens and becomes unresolved; the new-payee change alone still does not prove fraud. Add a valid customer reimbursement to F01 without a recipient return: do not reduce external unreturned funds; record allocation of exposure separately if supported.

## Evidence and interpretation challenge

Check each claim of authorization against its actual evidence. Did a confirmation use a preexisting trusted channel? Is a supplier denial a documented statement rather than direct knowledge of attacker identity? Are technical events attributed to a person without sufficient support? Are valid credentials being mistaken for genuine intent? Narrow any unsupported statement.

Challenge the benign case as carefully as the suspicious case. Confirm the amendment, timing, beneficiary, and verification apply to the actual payment. Keep contradictions visible. Do not equate a control's successful operation in F02 with demonstrated control effectiveness across the population.

## Cross-artifact review

Compare the same amount and status in report, workbook, and dashboard. Check that nulls remain visible and never become zero bars or blank “passed” badges. Filters must retain a visible count of hidden and unresolved incidents. All currency figures require ISO currency and two decimal display precision. Timestamps need timezone.

Test exported data for exact column order and text-safe treatment of source messages. An instruction beginning with a spreadsheet formula marker must be stored as text. Ensure no raw sensitive identifier is unnecessarily reproduced. No chart should label requested amount as loss or use a single stacked bar that double counts requested and executed amounts.

## Review and release

Record reviewer, role, timestamp, checks performed, corrections, unresolved defects, and final analytical release state. The expected example is READY FOR HUMAN REVIEW with F03 unresolved. It is not a final financial-loss certification, a reimbursement determination, a filing decision, or proof that recovery succeeded beyond the supplied return.

A failed reconciliation or incorrect null treatment blocks release as a reviewed package. A disclosed unavailable source can remain as a limitation if the reviewer receives a clearly bounded result. Record actual independent review separately from assistant self-checks; do not invent signoff because the document is complete.
