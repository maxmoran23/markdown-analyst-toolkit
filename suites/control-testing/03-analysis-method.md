# Analysis method — Control Testing and Evidence Review

## 1. Build a testable objective

Write the risk as an event and consequence: an item requiring independent approval could be released without challenge. Write the control as a response: a separate reviewer checks specified attributes before release and retains evidence. Write the test as observable criteria: a reviewer different from the preparer; review preceding release; specified attributes addressed; contemporaneous evidence retrievable. Do not replace these with the vague criterion “control is effective.”

Decompose a multi-step control into attributes. A single population instance can fail several attributes, but it counts once as a failed instance in the overall deviation rate. Keep attribute failures separately for diagnosis. For example, late review and missing rationale on the same record are two attribute failures and one failed instance. Attribute rates use the number of eligible attribute tests, not the whole population by default.

## 2. Assess design before operation

For each control ask whether its trigger covers the risk; inputs contain the information needed; performer has the authority and capability; frequency can prevent or detect the consequence; review provides meaningful challenge; exception handling reaches a decision owner; evidence is retained; and the process has a way to detect its own missing executions. These are analytical prompts, not an exhaustive regulatory checklist.

Conclude Adequate for stated objective, Inadequate, or Unable to assess. “Adequate” is bounded by the stated objective, evidence, and period. If a design is inadequate, test execution where useful to show exposure or compensating activity, but do not let perfect compliance with a flawed procedure rescue the design. If an additional control is said to compensate, inspect its design and relevant execution rather than accepting its title.

## 3. Establish selection logic before results

Choose census, probability sample, judgmental sample, or a combination with separate ledgers. Census means every eligible opportunity in the reconciled frame was evaluated. It does not prove the frame itself was complete. Probability sampling requires a known selection mechanism and defensible inference assumptions. Judgmental selection targets risk, change, prior errors, unusual activity, and ordinary cases; it supports conclusions about selected items and identified issues, not a general population error estimate.

Document the practical reason for the sample size, the intended assurance claim, anticipated missing evidence, and coverage of relevant strata. Do not call a fixed number such as 25 a universal requirement. A high-frequency automated control, a quarterly manual control, and a one-time release have different execution populations. The relationship between sample size and assurance depends on the question, expected deviations, tolerable deviation, confidence method, population structure, and sampling design.

For a simple random independent Bernoulli approximation with zero observed deviations, a one-sided 95% upper bound is 1 minus 0.05 raised to the power 1/n. At n=30 this is about 9.5%; zero observed errors does not imply zero possible errors. The approximation is not automatically appropriate for a finite population sampled without replacement, clustered records, weighted stratification, or judgmental selection. Use an approved finite-population or design-based method if a statistical assurance statement is required. If the session cannot calculate and explain that method, restrict the conclusion rather than inventing a confidence interval.

Repeated cases handled by the same person, on the same day, through the same system batch, may share failures. Thirty near-identical instances are not necessarily thirty independent opportunities. Record clusters and time coverage. Separate evidence from independent reviewers is also different from statistically independent sample observations; neither guarantees the other.

## 4. Reperform the control

Read original evidence in sequence. Capture the relevant value, expected value, actual timing, role relationship, and result for each attribute. Recalculate amounts or dates when they determine the outcome. A sign-off icon does not show what was reviewed. A checklist saying “complete” may need supporting material if the criterion requires actual reconciliation or challenge.

Use PASS only where all applicable attributes are supported. Use FAIL for an evidenced deviation from a defined criterion. Use UNABLE TO CONCLUDE when material evidence or a criterion is unavailable. Use NOT APPLICABLE only where the criterion genuinely does not apply, with a rationale approved for the test design. If at least one attribute fails and another is unassessed, the instance is FAIL and the unassessed attribute remains visible; do not discard it.

## 5. Calculate results without losing gaps

Let selected be all original and approved additional selected instances; report the two groups separately if their methods differ. Let pass, fail, and unable be mutually exclusive final instance outcomes. For applicable tested instances, selected = pass + fail + unable. If any selected instance is excluded as genuinely not applicable, show that exclusion and reconcile the original selected count first.

Selection coverage = selected / eligible population. Observed sample deviation rate = fail / selected. Evidence gap rate = unable / selected. Conclusive deviation rate = fail / (pass + fail). Present the last rate only beside the original selected denominator and gap count, because dropping unavailable cases can distort the impression of success. No one of these measures is the population deviation rate for a judgmental sample.

A conservative sensitivity describes how results would differ if all unable cases failed versus if all passed. The range is fail / selected through (fail + unable) / selected. This is a scenario range, not a statistical confidence interval and not proof about what happened. It helps show whether obtaining the missing evidence could change a conclusion.

## 6. Evaluate cause and implication

Separate condition, criterion, cause, and consequence. The condition is the observed deviation. The criterion is the requirement used for the test. The cause is often an inference requiring additional evidence. The consequence can be an observed outcome or a plausible exposure; distinguish them. A late review establishes lateness, not necessarily a financial loss or missed suspicious activity.

Consider plausible alternatives: missing archive versus missing execution; a documented holiday versus an unexplained timing failure; approved delegation versus self-review; one local error versus a systemic scheduling defect. State what evidence would resolve the distinction. Expand scope when the identified failure mechanism could affect additional instances, but retain the initial sample findings and avoid rewriting the original selection rationale after the fact.

## 7. Retest remediation

A remediation promise is not closure evidence. Specify the changed design, implementation date, affected population, operation period, retest criteria, and reviewer. Use fresh instances generated after the change, together with any required historical correction evidence. Reusing the original corrected record may prove a repair to that item, but not sustained control operation. Closure requires a human decision that cites the retest evidence and explicitly addresses residual limitations.
