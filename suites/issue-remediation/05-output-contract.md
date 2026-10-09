# Output contract — Issue Remediation and Closure Review

## Fixed package

Use the eight report sections and two domain tables below. The common Summary, Dashboard, Findings, Evidence, Actions, and QA sheets follow the exact columns and order in 07-workbook-template.md. ActionEvidence is the domain register of existing case actions; the common Actions sheet contains proposed review follow-ups linked to Findings. Do not combine these populations or assign the same count to both.

Identifiers and status enums are text. Counts and day differences are numeric integers. Dates use YYYY-MM-DD in structured records and display as dates where the writer supports them. Date strings may be preserved as ISO text when the renderer's date support is unavailable; disclose that format limitation. Percentages are numeric fractions or clearly labeled display strings with their numerators and denominators preserved in method notes. No monetary aggregation is part of this example.

Unknown dates are null in interchange and blank in workbook cells with an explanation. Unknown values never become zero. For a completed action, current days_overdue is measured zero under this suite's rule; historical lateness is stored in the report detail. For an open action with an unknown approved due date, days_overdue is null and the exception remains visible in QA.

## Required report heading order

1. Closure readiness and unresolved decisions
2. Issue population and review reference date
3. Findings and remediation barriers
4. Issue lifecycle and closure gates
5. Action evidence and effectiveness results
6. Evidence causal alternatives and recurrence
7. Proposed actions and independent review
8. Limitations quality review and human disposition

Section 1 states what is closure-ready, blocked, and actually approved. Section 2 declares the reference date, included issues, calendar, and status completeness. Section 3 states evidence-backed findings. Sections 4 and 5 correspond to IssueRegister and ActionEvidence. Section 6 preserves chronology, causal support, alternatives, and retest record IDs. Section 7 records proposals and actual decisions separately. Section 8 names limitations and checks that remain incomplete.

## Domain table: IssueRegister

Exact ordered columns: issue_id, severity, root_cause_status, disposition, approved_due_date, days_overdue, closure_gate, evidence_ids.

| Column | Type / allowed values | Interpretation |
| --- | --- | --- |
| issue_id | Unique text key | Stable original issue identity |
| severity | HIGH, MEDIUM, LOW, CRITICAL | Consequence-based judgment, separately explained |
| root_cause_status | Supported, Provisional, Unresolved | Support for the causal mechanism |
| disposition | Text lifecycle state | Current observed or draft analytical status, explained |
| approved_due_date | ISO date or null | Operative approved issue deadline |
| days_overdue | Integer calendar days or null | Reference date minus operative due date while unclosed |
| closure_gate | Required text | First or material remaining gate and decision |
| evidence_ids | Semicolon-separated text | IDs resolving in common Evidence |

The example states are Reopened, Validation pending, Closure review pending, and Acceptance expired. All four remain active; none has an authorized current closure. A historical closure of I01 is preserved in the chronology, not counted as its current status. I03's “Ready for independent closure review” gate is not an approved closure.

The issue clock is separate from the action clock. Every date calculation uses the end-of-day Oct 09, 2026 ET snapshot in the fixture. Do not use a renderer's execution date as the reference date. If the case record is stale, label it stale and retain its original calculation until the analyst authorizes a new snapshot.

## Domain table: ActionEvidence

Exact ordered columns: action_id, issue_id, action_type, approved_due_date, evidence_status, completion_date, days_overdue, retest_result, evidence_ids.

action_id is unique text. issue_id must exist in IssueRegister. action_type is required descriptive text that distinguishes implementation, effectiveness, or a combined deliverable. approved_due_date and completion_date are ISO dates or null. completion_date means accepted completion under that action's criterion; a failed test execution is retained in report detail and does not become a successful completion date.

evidence_status is Verified, Failed, Unresolved, or Not evidenced. Verified means this action's acceptance criterion is evidenced, not that its issue is closed. days_overdue is a nonnegative integer or null under the method in 03. retest_result is PASS, FAIL, UNABLE TO CONCLUDE, Not tested, or Not applicable. Implementation-only actions use Not applicable because their effectiveness is covered by another action. “Not applicable” does not mean validation is unnecessary for the issue.

Each evidence_ids value resolves to common Evidence. The fixture has six action rows, of which three are Verified, one Failed, one Unresolved, and one Not evidenced. Exactly two unresolved actions are overdue. Retest units and outcomes remain in the report/evidence detail keyed to action_id; do not put a comma-separated set of outcomes into a numeric cell.

## Consistency and presentation rules

The three verified actions yield 3/6 = 50.0% action completion under the fictional criteria. Zero of four issues are closed. Three of four active issues are overdue. One of four is technically ready for closure review. These measures must appear with their distinct denominators and meanings. No composite “remediation effectiveness percentage” may average them.

Preserve the expired acceptance and unapproved extension proposal in every output. Never render a green closed badge for I03 or I04. Filters show their scope and denominator, and nulls retain visible reasons. The dashboard uses the same offline light/dark template and records as the workbook and report. Inspect generated artifacts where capabilities allow; otherwise return the full content and identify the unverified format.
