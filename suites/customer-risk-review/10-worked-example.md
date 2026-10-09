# Worked example — Customer Risk Review

## Fictional fixture and bounded decision

All subjects, records, amounts, rubric assignments, and review statuses in this example are invented. No row identifies a real customer. The question is which profiles need further review under a teaching rubric as of Sep 30, 2026. There is no prior approved rating, operational system, or human disposition. Public references explain methodological context only; they do not validate these facts.

SYN-001 contains the complete six-customer population below. Five numeric factors are supplied per customer except the explicitly missing C04 geography value. Assignment values are exercise inputs rather than outputs of a predictive model. The reader should reproduce the arithmetic exactly before questioning the policy merits of the weights. Such a policy challenge is appropriate but must not silently change the expected exercise.

## Complete raw customer population

| Customer | Business | Product | Geography | Channel | Ownership | Identity item | Ownership item | Purpose item | Funds item | Case context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C01 | 1 | 1 | 0 | 1 | 0 | Supplied | Supplied | Supplied | Supplied | Simple fictional operating profile |
| C02 | 2 | 2 | 1 | 2 | 1 | Supplied | Supplied | Supplied | Supplied | Broader product and channel exposure |
| C03 | 3 | 2 | 2 | 1 | 3 | Supplied | Missing | Supplied | Supplied | Material control rights unresolved |
| C04 | 1 | 1 | null | 1 | 1 | Supplied | Missing | Supplied | Missing | Activity geography not supplied |
| C05 | 1 | 0 | 0 | 0 | 0 | Supplied | Supplied | Supplied | Missing | Planned third-party receipt unexplained |
| C06 | 2 | 1 | 2 | 2 | 1 | Supplied | Supplied | Supplied | Supplied | Separate control sample has exceptions |

The four evidence-item columns define the completeness checklist. C04's absent geography is a missing factor input, and its absent funds explanation is a separate checklist gap. Do not assume they are interchangeable fields. C03's ownership factor value of three is supplied as a rubric assignment even though decisive rights evidence is missing. A factor assignment can describe opacity while the underlying ownership question remains unresolved.

## Complete raw control sample

SYN-002 contains every supplied control check for C06. These are invented targeted checks, not a random sample of all customer activity. Eight is the full supplied sample size. Its relationship to any larger operating population is unknown.

| Check ID | Outcome | What the exercise says |
| --- | --- | --- |
| K01 | NO EXCEPTION | Required review field present |
| K02 | NO EXCEPTION | Required review field present |
| K03 | EXCEPTION | Relevant review timestamp absent |
| K04 | NO EXCEPTION | Required review field present |
| K05 | NO EXCEPTION | Required review field present |
| K06 | NO EXCEPTION | Required review field present |
| K07 | EXCEPTION | Relevant escalation rationale absent |
| K08 | NO EXCEPTION | Required review field present |

No exception means no exception under this narrow fictional check, not proof that the underlying activity was legitimate. K03 and K07 describe different defects; they are not automatically repeated manifestations of one root cause. Their potential effect on the customer profile requires further context.

## Expected factor arithmetic

Weights in the order shown are 0.30, 0.25, 0.20, 0.15, and 0.10. Formula: score = (0.30B + 0.25P + 0.20G + 0.15C + 0.10O) / 3 × 100. Work at full precision; display one decimal. The weighted numerator is not already a percentage.

| Customer | Weighted numerator | Score before rounding | Display | Band |
| --- | --- | --- | --- | --- |
| C01 | 0.70 | 23.333333 | 23.3 | LOW |
| C02 | 1.70 | 56.666667 | 56.7 | MODERATE |
| C03 | 2.25 | 75.000000 | 75.0 | HIGH |
| C04 | Incomplete | null | Incomplete | INCOMPLETE |
| C05 | 0.30 | 10.000000 | 10.0 | LOW |
| C06 | 1.65 | 55.000000 | 55.0 | MODERATE |

For C02, the five contributions are 20.0, 16.666667, 6.666667, 10.0, and 3.333333. Their sum is 56.666667. C04's known numerator is 0.80. At a hypothetical geography value of zero the score is 26.666667; at three the numerator is 1.40 and the score 46.666667. C04 remains incomplete because neither hypothetical value is observed.

Complete scores: 5/6 = 83.3%. LOW: 2/5 = 40.0% of complete scores, or 2/6 = 33.3% of all profiles. MODERATE has the same two counts. HIGH: 1/5 = 20.0% of complete scores, or 1/6 = 16.7% of all profiles. INCOMPLETE: 1/6 = 16.7% of all profiles. Rounding can make displayed population shares sum to 100.1%; retain raw counts rather than adjusting a category to hide rounding.

Evidence checklist completion: 4 + 4 + 3 + 2 + 3 + 4 = 20 supplied items out of 24 expectations. The rate is 83.333333%, displayed 83.3%. This is numerically equal to score availability by coincidence. C06 exceptions: 2/8 = 25.0%; checks without recorded exceptions: 6/8 = 75.0%. Neither percentage estimates the frequency of crime or the control's population effectiveness.

## Expected interpretation and next evidence

C01 is proposed STANDARD within this limited fixture. C02 is proposed HEIGHTENED because its described complexity warrants contextual review. C03 is proposed SPECIALIST for unresolved ownership/control rights and its high illustrative band. C04 is INCOMPLETE pending factor and checklist evidence. C05 receives TARGETED review of its unexplained planned receipt despite the lowest score. C06 remains HEIGHTENED while the two control exceptions are examined. No proposal is an approved rating.

The next evidence is precise: for C03, rights instruments or a permitted fictional clarification of who can direct the relationship; for C04, the actual activity geography and missing ownership/funds explanation; for C05, the economic origin, sender relationship, and purpose of the planned funds; for C06, the check scope, timestamps, escalation record, and selection method. Do not request real private documents in this public exercise.

## Counterexamples that must change behavior

Replace C04's null with zero without evidence: the displayed score would become 26.7 and LOW, but the expected QA result is FAIL because the input was invented. Reweight its four known factors to sum to one: the resulting score would answer a different method and must not be presented as the original rubric. Delete C05's material gap while leaving its score unchanged: the arithmetic still passes, but the analytical result fails because the recommendation lost its decisive limitation.

Claim that C06's 75.0% no-exception fraction means a 75.0% reduction in risk: reject the interpretation. Duplicate C02's product row: reject the factor population until reconciled. Change C03 ownership from three to one as an explicitly hypothetical sensitivity: score becomes 68.333333 and remains HIGH, with the baseline retained. Insert a score exactly equal to 65 in a boundary-only test: assign HIGH. None of these tests creates evidence for a real customer.

## Record actual checks

Save the raw population, formula, exact intermediate values, expected and observed outputs, and discrepancies. Record which checks were calculated in-session, which were inspected manually, and which could not run. A later render-only session must receive this complete checkpoint. The expected results above are not an executed test log, independent validation, or approval. Actual QA results remain pending until the session performs and records them.
