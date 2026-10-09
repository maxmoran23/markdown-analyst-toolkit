# Worked example — Issue Remediation and Closure Review

## Fictional scope and standard

SYN-001 contains all fictional inputs below. No organization, person, issue, approval, or operating record is real. The snapshot is end-of-day Oct 09, 2026 ET. Every deadline is a calendar date inclusive through its end. Calendar-day subtraction measures overdue status; weekends and holidays are not excluded. Four issues and six existing actions comprise the complete exercise population, with no exclusions or duplicate IDs.

The author-defined closure standard requires the original defect and cause to be addressed, implementation evidence, a complete fresh retest meeting the issue-specific criterion, recurrence review, a current authorized residual-risk disposition if needed, and final independent human approval. The fictional record contains no current final closure approvals. A technically ready issue therefore remains open. Existing action completion requires evidence of that action's acceptance criterion; an attempted failed validation is not accepted completion.

## Original issues and causal evidence

| ID | Opened | Condition and criterion | Cause evidence and status | Severity |
| --- | --- | --- | --- | --- |
| I01 | 2026-08-01 | Daily queue review missed during staff absence; one documented review required each calendar day | Original schedule has no backup coverage; two missed dates coincide with absence. Supported coverage mechanism within this scope | HIGH |
| I02 | 2026-09-10 | Required reconciliation archive class absent; archive must preserve every execution record | Export configuration excludes class Z; inspected mapping reproduces the exclusion. Supported | MEDIUM |
| I03 | 2026-09-01 | Reconciliation report omitted an eligible category; all defined categories must map into the report | Reproduction shows category K missing from mapping; corrected mapping includes K. Supported | MEDIUM |
| I04 | 2026-09-05 | Temporary manual workaround remains beyond planned replacement; replacement or current authorized temporary disposition required by the fictional standard | Owner attributes delay to dependency availability; no corroborating dependency record or alternative-cause assessment. Provisional | HIGH |

The original fictional causal exhibits are complete for this miniature exercise:

| Exhibit | Raw content | What it supports |
| --- | --- | --- |
| SC01 | Schedule version effective Aug 01: primary role Q each day; alternate field blank for all days | Backup coverage absent in the documented original design |
| AL01 | Aug 10: primary absent, review log says missed; Aug 17: primary absent, review log says missed | Two observed failures coincide with the specified absence condition |
| AL02 | Sep 12: primary absent, review log says missed; register records reopening that date | Same stated mechanism after the recorded Aug 31 closure |
| CF02 | Before Oct 03: export classes A,B; required classes A,B,Z. After Oct 03: export classes A,B,Z | Direct before/after support for the class-Z omission and change |
| CF03 | Before Sep 20: report mapping J,L; required J,K,L. Reproduction with one K row produces zero mapped K rows. After Sep 20: J,K,L, and the same reproduction maps one K row | Direct support for the specific mapping defect and repair |
| ST04 | Owner statement Oct 02: dependency unavailable; underlying dependency status record not supplied | Reported explanation only; competing causes remain untested |

I01's recorded history shows an authorized closure on Aug 31 and a same-mechanism event on Sep 12, followed by a recorded reopening that day. That is an observed historical status in the fictional register, not a new decision by the assistant. The packet contains no later closure. The interval from Aug 31 to Sep 12 is twelve calendar days. A later failed retest does not erase either historical event.

I02's inspected before/after configuration removes the class-Z exclusion on Oct 03, but evidence of ongoing archive operation is still needed. I03's before/after mapping and synthetic reproduction support its defined mechanism and change. Neither configuration artifact alone establishes that all future operations succeed. I04's owner explanation remains an uncorroborated cause hypothesis.

## Complete issue deadline and acceptance history

| Issue | Original due | Approved current due | Approval history | Proposal or acceptance information |
| --- | --- | --- | --- | --- |
| I01 | 2026-09-30 | 2026-10-02 | Authorized issue reviewer approved extension Sep 29 | No further approved extension |
| I02 | 2026-10-10 | 2026-10-10 | Original plan approved Sep 11 | No change proposed |
| I03 | 2026-10-07 | 2026-10-07 | Original plan approved Sep 02 | Closure request submitted Sep 28; final decision absent |
| I04 | 2026-09-15 | 2026-09-30 | Authorized risk owner approved temporary acceptance and due-date extension Sep 14 | Acceptance expired Sep 30; proposed Oct 31 extension submitted Oct 02 has no approval |

I04's temporary acceptance explicitly covered only this fictional workaround through Sep 30, with weekly monitoring. Its authorized scope, role, and period are stipulated in SYN-001. It does not purport to waive a law or regulatory obligation. No renewal, new acceptance, or replacement implementation appears in the complete supplied decision register. The Oct 31 proposal cannot alter either the due date or expiry for this snapshot.

## Complete existing action plan and evidence

| Action | Issue | Deliverable and acceptance criterion | Approved due | Evidence actually supplied | Accepted completion |
| --- | --- | --- | --- | --- | --- |
| A01 | I01 | Implement backup coverage roster; issued roster plus adoption acknowledgment | 2026-09-25 | Roster and acknowledgment dated Sep 28, effective Sep 29 | 2026-09-28 |
| A02 | I01 | Validate six daily post-change opportunities; all six reviews evidenced and timely | 2026-10-02 | Six logs Oct 01–06, including missed Oct 06 review | null |
| A03 | I02 | Correct class-Z export mapping; inspected diff and deployment record | 2026-10-03 | Diff and deployment dated Oct 03, effective before the Oct 05 retest | 2026-10-03 |
| A04 | I02 | Validate four post-change archive opportunities; all four execution artifacts retained | 2026-10-10 | Three artifacts accessible, one missing for Oct 08 | null |
| A05 | I03 | Correct mapping and validate four fresh opportunities; all categories included and four passes | 2026-09-26 | Mapping corrected Sep 20; independent validator's complete four-day record Sep 23–26 passes | 2026-09-26 |
| A06 | I04 | Replace workaround; inspected implementation plus defined validation | 2026-09-30 | Owner reports dependency delay; no replacement artifact or retest | null |

Owner roles are Queue owner for A01/A02, Archive owner for A03/A04, Reporting owner for A05, and Transition owner for A06. Validator role V is organizationally separate from these implementer roles in this fictional exercise. V's inspected retest record supports testing evidence but is not final issue closure approval. The authorized closure reviewer has not recorded a current decision for any issue.

A02's original validation deadline is already inconsistent with completing a six-day Oct 01–06 observation window by Oct 02. Preserve that plan defect: the retest finished late and failed; do not silently revise its due date to Oct 06. This is an additional action-planning concern for review. A01's implementation was accepted three days late; it is currently completed, so its current overdue measure is zero while historical lateness remains three.

## Complete raw retest evidence

Each row is one required daily opportunity. These are complete miniature windows, not a random sample of future operations. The supplied logs explicitly identify the review or archive evidence status; “unknown” does not mean no error.

| Retest ID | Action | Date | Supplied fact | Outcome |
| --- | --- | --- | --- | --- |
| R01 | A02 | 2026-10-01 | Timely daily review retained | PASS |
| R02 | A02 | 2026-10-02 | Timely daily review retained | PASS |
| R03 | A02 | 2026-10-03 | Timely daily review retained | PASS |
| R04 | A02 | 2026-10-04 | Timely daily review retained | PASS |
| R05 | A02 | 2026-10-05 | Timely daily review retained | PASS |
| R06 | A02 | 2026-10-06 | Log records no review while primary role absent | FAIL |
| R07 | A04 | 2026-10-05 | Required class-Z execution artifact retained | PASS |
| R08 | A04 | 2026-10-06 | Required class-Z execution artifact retained | PASS |
| R09 | A04 | 2026-10-07 | Required class-Z execution artifact retained | PASS |
| R10 | A04 | 2026-10-08 | Retrieval failed; archive existence and retention unknown | UNABLE TO CONCLUDE |
| R11 | A05 | 2026-09-23 | Category K included; source and output totals reconcile | PASS |
| R12 | A05 | 2026-09-24 | Category K included; source and output totals reconcile | PASS |
| R13 | A05 | 2026-09-25 | Category K included; source and output totals reconcile | PASS |
| R14 | A05 | 2026-09-26 | Category K included; source and output totals reconcile | PASS |

R10 differs from the original demonstrated class exclusion: retrieval failure does not establish whether the record exists. Obtain a reliable retrieval or retention audit before deciding that specific attribute. A04 remains unresolved. R06 demonstrates a missed review despite the new roster; investigate adoption and coverage execution before claiming the redesign works.

## Expected fixed registers

IssueRegister contains I01/HIGH/Supported/Reopened/2026-10-02/7/“Blocked: effectiveness failed”; I02/MEDIUM/Supported/Validation pending/2026-10-10/0/“Blocked: retest evidence incomplete”; I03/MEDIUM/Supported/Closure review pending/2026-10-07/2/“Ready for independent closure review”; I04/HIGH/Provisional/Acceptance expired/2026-09-30/9/“Blocked: acceptance expired and replacement absent”. Every row references SYN-001.

ActionEvidence contains A01/I01/Implementation/2026-09-25/Verified/2026-09-28/0/Not applicable; A02/I01/Effectiveness/2026-10-02/Failed/null/7/FAIL; A03/I02/Implementation/2026-10-03/Verified/2026-10-03/0/Not applicable; A04/I02/Effectiveness/2026-10-10/Unresolved/null/0/UNABLE TO CONCLUDE; A05/I03/Implementation and effectiveness/2026-09-26/Verified/2026-09-26/0/PASS; A06/I04/Replacement/2026-09-30/Not evidenced/null/9/Not tested. Every row references SYN-001.

## Expected arithmetic

| Measure | Calculation | Expected result |
| --- | --- | --- |
| Verified existing actions | A01 + A03 + A05 | 3/6 = 50.0% |
| Active issues | All four have no current closure | 4 |
| Authorized current closures | None supplied | 0/4 = 0.0% |
| Technical closure readiness | I03 only | 1/4 = 25.0% |
| Overdue active issues | I01, I03, I04 | 3/4 = 75.0% |
| Overdue open actions | A02 and A06 among A02,A04,A06 | 2/3 = 66.7% |
| I01 and A02 overdue | Oct 09 minus Oct 02 | 7 calendar days |
| I03 overdue | Oct 09 minus Oct 07 | 2 calendar days |
| I04 and A06 overdue | Oct 09 minus Sep 30 | 9 calendar days |
| A01 historical lateness | Sep 28 minus Sep 25 | 3 calendar days |
| Recurrence interval | Sep 12 minus Aug 31 | 12 calendar days |
| A02 retest | 5 pass + 1 fail | 6; failure share 1/6 = 16.7% |
| A04 retest | 3 pass + 1 unresolved | 4; unresolved share 1/4 = 25.0% |
| A05 retest | 4 pass | 4; all within this bounded window |

An optional in-session calculation can parse the printed ISO dates and subtract date objects. Do not substitute business-day arithmetic. No monetary amount, risk score, or statistical assurance estimate is required. The fourteen retest rows reconcile to twelve passes, one failure, and one unresolved result; that total does not establish an effectiveness percentage across different controls and windows.

## Expected findings and bounded conclusion

IR-F01 is HIGH, HIGH confidence, Observed: I01's post-change retest failed on R06 after its historical reopening; A01's completion does not resolve effectiveness. IR-F02 is MEDIUM, HIGH confidence, Observed: R10 remains unavailable, preventing complete A04 validation. IR-F03 is MEDIUM, HIGH confidence, Observed: I03 meets the fictional technical criteria but lacks final closure approval and is two days overdue. IR-F04 is HIGH, HIGH confidence for the documented expiry, Observed: I04's acceptance has expired, its extension is only proposed, and replacement evidence is absent. The underlying causal hypothesis remains Provisional.

The expected recommendation is to keep I01 and I02 blocked pending corrective investigation or evidence recovery, submit I03 for actual independent closure review, and obtain an authorized I04 disposition while preserving the expired acceptance and overdue status. No new approval is implied. The expected conclusion is: “Three of six actions are evidenced complete, but no issue is currently closed. I03 is technically ready for independent closure review; I01 failed retest, I02 has an unresolved retest record, and I04's acceptance expired without evidenced replacement. Three of four active issues are overdue at Oct 09, 2026.”

Run all ten negative controls in 09 and retain actual results. The decisive traps are counting implementation as effectiveness, counting readiness as closure, deleting a missing retest, and letting an unapproved extension rewrite the clock.
