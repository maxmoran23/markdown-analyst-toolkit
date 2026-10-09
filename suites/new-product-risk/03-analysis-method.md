# Analysis method — New Product Risk and Launch Readiness

## 1. Describe the product as a sequence of accountable events

Start with user entry, eligibility, authentication, instruction creation, review, execution, settlement, reconciliation, servicing, and termination as applicable. State which events are in scope. For each event identify the actor, information available, decision made, authority to make it, and retained evidence. Avoid describing an entire provider as a black box when a critical decision occurs inside it.

Map funds, data, and service flows separately. Funds movement describes where value or a claim moves. Data movement describes attributes and records. Service movement describes a request or activity. These may occur at different times and through different parties. Do not sum a $100 instruction, a $100 settlement, and a $100 ledger entry into $300 of economic exposure.

Explain normal, rejected, delayed, duplicated, reversed, and unavailable paths. A product is not fully described by its successful customer journey. Determine what happens when a provider times out after executing a request but before acknowledging it. An automatic retry can create duplication unless the underlying process controls it; whether that risk is real depends on the actual design evidence.

## 2. Identify exposure at each boundary

For each flow leg ask what can go wrong, how it would be detected, who can intervene, and what evidence would remain. Consider identity and authorization, misuse patterns, sanctions or monitoring dependencies where relevant, data quality, operational error, fraud, privacy, security, liquidity or settlement exposure, customer harm, and legal scope. These are analytical categories, not a universal regulatory checklist.

Distinguish inherent exposure from control evidence. A high-value irreversible transfer has different consequences from a reversible draft instruction. A low transaction limit may reduce maximum loss per event but not eliminate misuse, aggregation, or data exposure. Multiple apparently small events can accumulate. State the assumptions that make a pilot limit meaningful, including customer counts, concurrency, daily aggregate value, and connected channels.

Use qualitative risk judgments with explicit reasons unless an approved quantitative method is supplied. Do not manufacture a residual score by subtracting an arbitrary “control effectiveness” percentage from an inherent score. A control's evidence can be incomplete even when its design appears sensible. Unknown support is a limitation, not automatically a high or low probability estimate.

## 3. Trace control dependencies

Connect each risk to the control that prevents, detects, or corrects it. Identify required fields, upstream completeness, reference data, provider service, staff capacity, escalation authority, and exception handling. A monitoring rule can be correctly configured but ineffective for a missing transaction type. A reconciliation can compare two records derived from the same erroneous source and fail to provide independent assurance.

State which party performs each control and which party verifies performance. Outsourcing the activity does not answer how the reviewer knows it occurred. Obtain the relevant service description, evidence access, incident routing, and control responsibilities. A vendor assurance report may cover only part of the product or an earlier period. Map its scope to the actual dependency before relying on it.

Look for common-cause failures. Two providers sharing one infrastructure service may not provide independent resilience. A fallback that needs the failed provider's credentials, data export, or support team may not work during the actual outage. Test the dependency chain rather than counting providers as independent backups.

## 4. Preserve and decompose conditions

Transcribe each approved launch condition with its ID, original wording, timing, and approval reference. If a condition is vague, retain it and add testable subcriteria instead of silently rewriting the obligation. “Monitoring in place” might require design, configuration, data reconciliation, test cases, routing, and staffing evidence. The approving human resolves the interpretation.

Every condition remains in the register. Missing evidence does not delete a row. If a condition truly no longer applies because the product scope changed, retain the rationale and human approval of the change. A condition cannot be waived by relabeling it low risk after the review found it incomplete.

## 5. Verify evidence by stage

SATISFIED means the supplied dated evidence supports every applicable criterion for the assessed version and timing. PARTIAL means some required elements are evidenced and others remain incomplete. NOT SATISFIED means supplied evidence shows the work has not occurred or a required test failed. NOT VERIFIABLE means completion is asserted or implied but sufficient inspectable evidence is absent. These are evidence statuses, not final launch decisions.

A plan is not execution. Deployment is not testing. Testing on one synthetic scenario is not full population coverage. Evidence created after a required pre-launch deadline cannot retroactively satisfy the original timing criterion, although it may support later remediation. A review signature requires context: what was reviewed, by whom in role terms, against which criteria, and with what exceptions.

For data and value reconciliation, check both conservation and timeliness. In the fixture, $100.00 in instructions equals $50.00 posted plus $50.00 pending. The value equation balances, but the pending item remains unresolved beyond the illustrative 30-minute criterion. A total reconciliation can pass while a status or timing criterion fails.

## 6. Test adverse and boundary paths

Select tests based on the flow and failure mechanisms: missing identity data, unsupported payment type, threshold equality, repeated request, provider timeout, late response, missing ledger event, reversal after settlement, unavailable operator, reference-data change, and exit during pending activity. The suite does not execute these on live systems. It reviews supplied test records or helps draft a test plan using fictional inputs.

For each test preserve expected result before execution, observed result, data and configuration version, environment, evidence locator, defect ID, and retest result. A test that failed and was later rerun successfully should show both outcomes and what changed. A successful happy-path demonstration cannot substitute for all adverse-path tests.

## 7. Evaluate readiness without averaging away gates

Count all conditions by status and separately count unresolved critical conditions. A50.0% completion metric is descriptive, not an approval threshold. One missing critical prerequisite can be decisive even when many minor conditions pass. Keep criticality rationale tied to the approved conditions or an explicitly proposed reviewer framework.

Possible recommendations are evidence supports human launch consideration, evidence supports only a bounded conditional proposal, evidence does not support launch consideration yet, or unable to assess. None is a launch authorization. A conditional proposal requires that remaining items can legitimately be completed later, with owner, deadline, monitoring, and acceptance criteria; a critical pre-launch requirement cannot silently become a post-launch task.

## 8. Define pilot, monitoring, and exit together

If a limited pilot is proposed, state participant eligibility, volume and value limits, duration, transaction types, excluded activities, support hours, monitoring frequency, escalation, stop criteria, and reconciliation. The limits must be enforceable and testable. A verbal promise to keep volume low is not a control. Specify who can stop new activity and how pending activity remains serviced.

The exit plan covers new-request suspension, pending funds, open cases, data export and retention, access removal, provider transition, customer communication proposals, and restoration or closure evidence. Test recovery time using the actual dependencies. A fast service restart is not complete recovery if records are inconsistent or outstanding obligations are lost.

After a human decision, retain the approved scope and conditions. Any material expansion requires reassessment of affected flows and evidence. The suite does not schedule monitoring, operate the product, or automatically authorize a future expansion.
