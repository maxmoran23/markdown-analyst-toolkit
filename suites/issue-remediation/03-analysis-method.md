# Analysis method — Issue Remediation and Closure Review

## 1. Freeze the review population and clock

Inventory every issue and action in scope. Reconcile source counts to the working registers before filtering by status. Preserve merged or superseded IDs with linkage rather than deleting their history. State the period, snapshot date, timezone, and whether the status record is complete. A dashboard titled “current issues” is not proof that closed or recurring items were included.

The fixture uses end-of-day Oct 09, 2026 ET as its reference. For an issue without an authorized closure, current days_overdue = max(0, reference_date - approved_current_due_date) in calendar days. A completed action has current days_overdue = 0 after its defined acceptance criteria are evidenced; separately show historical lateness = max(0, accepted_completion_date - approved_due_date). These measures answer different questions. An issue ready for approval can still be overdue while approval remains absent.

Use approved dates only. Preserve a proposed extension as a pending decision, not an operative deadline. Approval after a breach does not erase the historical breach; show original and revised views when relevant. If approval authority or timing is unknown, the extension is not established. An expired risk acceptance cannot silently renew itself.

## 2. Restate each issue without losing the original criterion

Construct condition, criterion, consequence, scope, and evidence. The condition describes what was observed; the criterion describes what should have happened. Consequence distinguishes actual observed effects from plausible exposure. Scope identifies the population in which the observation is supported and the broader population still requiring investigation.

Avoid turning every issue into a documentation problem merely because producing a document is easy. If the defect was missed reviews, revising a procedure may be useful implementation evidence but does not demonstrate that reviews occurred. Conversely, if the issue was record retention, a file's absence can be a direct retention failure even when the underlying operation is unknown. Keep the original failure criterion visible when drafting closure tests.

## 3. Challenge the root-cause mechanism

Write a cause statement with a causal chain: the triggering condition, the failed preventive or detective safeguard, and the resulting defect. Separate primary mechanism, contributing conditions, and detection gap. For each link, identify supporting evidence and a falsification test. Prefer mechanisms that predict where else the defect should appear and what should change after intervention.

Classify root_cause_status as Supported, Provisional, or Unresolved. Supported means direct evidence reasonably corroborates the defined mechanism within scope; it does not establish a universal cause. Provisional means the explanation fits but alternatives remain material. Unresolved means current evidence cannot distinguish plausible mechanisms. A manager's confident explanation is still a source assertion.

In the fixture, I01's schedule lacks backup coverage on absences and the missed reviews coincide with that condition. That supports a coverage mechanism, but the new roster's mere existence is not proof it operates. I02's export configuration excludes one archive class, and the before/after mapping shows the correction. I03's reproduction shows a particular mapping defect. I04's dependency explanation lacks sufficient direct evidence to exclude local scheduling or ownership failures, so it remains Provisional.

## 4. Map causes to corrective actions and acceptance criteria

Give each action an owner role, deliverable, dependency, due date, and evidence-based acceptance criterion. Distinguish containment, repair of historical affected records, preventive redesign, implementation, and effectiveness testing. Containment can reduce immediate exposure while leaving the root cause unresolved. Repairing old cases does not establish that new cases will be handled correctly.

Use a cause-to-action map. Every supported mechanism needs a relevant action or an explicitly governed residual-risk disposition. Every action needs a reason it can change the mechanism or verify the change. A collection of tasks with no causal link may be busywork. A single action called “fix process” is not testable until its deliverable and criterion are defined.

For implementation, ask what changed, where, when it became effective, whether all affected channels were included, and how adoption was checked. For effectiveness, ask what fresh opportunities would expose the original failure, over which period, and with what evidence. The fixture records implementation and effectiveness as separate actions for I01 and I02 to make this distinction visible. I03's combined action has both criteria explicitly satisfied before it receives Verified status.

## 5. Inspect completion evidence

Classify each action's evidence_status as Verified, Failed, Unresolved, or Not evidenced. Verified means the action's stated acceptance criterion is evidenced; it does not mean the whole issue is closed. Failed means inspected evidence demonstrates the criterion was not met. Unresolved means a material portion cannot be assessed. Not evidenced means required implementation or completion support has not been supplied.

Retain completion_date only when completion under that action's criterion is evidenced. An attempted retest with a failure is not a completed successful validation. Its execution date stays in retest detail, while its accepted completion date remains null. If the deliverable was merely to perform a diagnostic test, different acceptance criteria could apply; preserve the explicit original definition rather than switching to it after failure.

A reconstructed artifact may explain a past activity but lack contemporaneous support. Label its evidentiary limit. A control owner can certify its own action as complete in an operational system, but an independent review still needs inspectable evidence and defined acceptance criteria. Do not equate the status vocabulary of a ticketing tool with this suite's evidence classification.

## 6. Reperform effectiveness testing

Confirm the change was effective before the retest window. Use fresh units capable of exhibiting the original failure mechanism. A retest consisting only of repaired historical cases answers whether those cases were corrected, not whether the new process prevents recurrence. Include the affected exception path, relevant volumes, operating modes, and coverage conditions in the scope rationale.

Reconcile the complete retest frame, selected IDs, selection basis, PASS, FAIL, and UNABLE TO CONCLUDE. A small census covers its fixed period; a judgmental sample supports observations in selected units; a probability sample requires its own inference method. The fixture uses complete small fictional post-change windows and makes no long-run assurance claim. Missing evidence remains in the denominator. Record defects at unit and attribute level without counting the same unit twice.

I01 has five passes and one failure among six post-change opportunities. I02 has three passes and one unresolved among four. I03 has four passes in a four-opportunity post-change window, with the prescribed implementation evidence present. These are different outcomes. Do not combine them into an overall “92% effective” score that conceals a failed issue and an incomplete issue.

## 7. Review recurrence and residual risk

Match new observations to the prior condition, criterion, cause, and affected scope. A similar title alone does not establish recurrence. A different symptom can still reflect the same mechanism. Distinguish ongoing failure before a change, failed validation after the change, and recurrence after authorized closure. Record the historical closure even if later evidence undermines its rationale.

The fixture records I01 closed Aug 31, a similar failure observed Sep 12, and reopening that day. The interval is twelve calendar days. The post-change retest failure on Oct 06 then shows that the subsequent action has not demonstrated effectiveness. It does not by itself prove the earlier closure reviewer acted improperly. Examine the prior evidence, scope, and decision separately.

Risk acceptance needs explicit authority, covered risk, rationale, limits, compensating measures, review cadence, expiry, and re-entry conditions. A due date extension and a risk acceptance are not interchangeable. Acceptance cannot establish an action was completed or a control effective. Where a nonwaivable obligation applies, a business acceptance cannot make noncompliance permissible; obtain appropriate human legal or compliance assessment rather than inventing authority.

## 8. Apply closure gates and preserve the decision

Evaluate seven distinct gates: original scope and impact addressed; causal explanation adequate; relevant actions implemented; fresh effectiveness evidence sufficient; recurrence reviewed; residual risk disposition current and authorized; independent closure approval recorded. A gate may be Not applicable only with a reason. Missing evidence is not a pass. The final gate cannot be satisfied by the assistant.

Issue dispositions in the fixture are Reopened, Validation pending, Closure review pending, and Acceptance expired. I03 is ready for independent closure review because its technical evidence meets the fictional criteria; it is not Closed because no final approval exists. I04 remains active after its acceptance expiry and lacks replacement evidence. I01 remains blocked by a failed retest. I02 remains blocked by an unresolved retest record.

Produce a draft recommendation with alternatives. An evidence recovery request, wider retest, redesign, restricted acceptance, or closure review should name its dependency and decision owner. Preserve every unresolved gate in the same record used by all renderers. If a later reviewer approves closure, record their actual decision, scope, date, conditions, and monitoring obligation; do not erase the original finding or its historical overdue periods.
