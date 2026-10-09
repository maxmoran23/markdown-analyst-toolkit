# Quality review — Issue Remediation and Closure Review

## Start with the original defect

Compare the closure recommendation to the original condition, criterion, consequence, and scope. A reviewer should be able to explain how the proposed action interrupts the failure mechanism and which fresh observations demonstrate that change. If the only answer is “the owner completed the ticket,” the review has not established effectiveness.

| Check | Reperformance | Failure signal |
| --- | --- | --- |
| Population | Reconcile all issues and actions, including reopenings | Closed or difficult items silently omitted |
| Cause | Trace each causal link and alternative | Symptom relabeled as root cause |
| Actions | Map each deliverable to a mechanism and criterion | Documents collected without testable purpose |
| Dates | Recalculate against the saved reference date | Current clock or proposed extension substituted |
| Evidence | Open the original locator and assess what it proves | Status report treated as execution evidence |
| Retest | Count every planned or selected unit and outcome | Missing artifact removed from denominator |
| Recurrence | Compare prior and new failure mechanisms | Similar title treated as sufficient linkage |
| Closure | Check every gate and actual independent disposition | Readiness or acceptance displayed as closure |

## Required example reperformance

The complete issue population is four and the existing action population is six. Three actions meet their individual acceptance criteria. None of the four issues has current authorized closure. Current issue overdue days are I01 7, I02 0, I03 2, and I04 9 at Oct 09, 2026. Three of four issues are therefore overdue, or 75.0%. I03 remains overdue while final approval is pending even though its technical gates are satisfied.

Current action overdue days are A01 0, A02 7, A03 0, A04 0, A05 0, and A06 9. A01 was accepted Sep 28 against a Sep 25 due date, so its historical lateness is three days. Show that separately. Open actions are A02, A04, and A06; two of three are overdue, or 66.7%. Do not report 2/6 as the overdue-open-action share without labeling that different denominator.

Recount A02's six retest units: five PASS and one FAIL. Recount A04's four: three PASS and one UNABLE TO CONCLUDE. Recount A05's four: four PASS. The overall fourteen retest opportunities have twelve passes, one failure, and one unresolved assessment. That aggregate is a reconciliation only, not a portfolio effectiveness estimate. I01's Aug 31 closure to Sep 12 recurrence interval is twelve calendar days.

## Negative controls

1. Replace I04's approved Sep 30 due date with its unapproved Oct 31 proposal. The authorization and deadline-history checks must reject it; days_overdue remains nine.
2. Use today's date at render time instead of the saved Oct 09 snapshot. The frozen-record check must reject the changed overdue results.
3. Delete A04's missing R10 record and call the retest three of three passed. The population reconciliation must reject it; the original window has four opportunities.
4. Mark A01's Verified implementation as proof that I01 is effective. The dependent failed A02 retest must block that conclusion.
5. Mark I03 Closed because its four retest records passed. The independent-approval gate must reject it; the correct state is Closure review pending.
6. Treat I04's expired acceptance as completed remediation. The risk-acceptance gate must reject it.
7. Turn A02's Oct 06 failed-test execution into a successful completion_date. The acceptance-criterion check must reject it.
8. Set A01's current overdue days to three. The clock check must reject the current measure while retaining three historical late days.
9. Call twelve of fourteen retest passes a population-wide effectiveness rate. The scope and heterogeneous-issue check must reject it.
10. Rewrite I01's original opened date as its Sep 12 reopening date. The chronology check must preserve both original and episode dates.

Preserve the mutation, expected rejection, actual result, and any defect found. A list of planned checks is not evidence they ran. When calculations can be performed, capture inputs and formulas rather than a screenshot of final totals alone.

## Counterevidence and independence review

For I01, consider whether the Oct 06 failure involved roster adoption, a different absence condition, or an unrelated execution failure. The recurrence warrants investigation; it does not prove every causal link. For I02, distinguish a missing archive artifact from a demonstrated missed reconciliation. For I03, test whether the four-day window covers the stated risk adequately; a short successful census establishes only its bounded observation. For I04, verify acceptance scope and authority before treating even the historical acceptance as valid.

Confirm the reviewer was not responsible for implementing the action where the applicable standard requires independence. The assistant is a drafting and analysis aid, not the independent authority. Source citations do not create reviewer qualification. GAO and FFIEC provide context within their own applicability; they do not prescribe the example's dates, percentages, or severity labels.

## Artifact and checkpoint checks

Validate exact report headings, table columns, status values, native day counts, date handling, nulls, and evidence foreign keys. Check that common Actions contains proposed follow-ups while ActionEvidence contains the six existing case actions. A chart of one must not use the denominator of the other. Reopen files and test dashboard themes and filters where tools permit; record unavailable checks honestly.

Save source versions, reference date, deadline history, issue/action joins, root-cause reasoning, implementation evidence, every retest unit, recurrence timeline, calculations, negative-control outcomes, and actual human decisions. Render only that complete record. If new evidence changes a gate, revise the analysis and log the change before rendering again. Never update only the headline while leaving supporting tables on the old conclusion.
