# Analysis method — Customer Risk Review

## 1. Define the relationship and the decision boundary

State whether the review asks about onboarding research, a periodic profile refresh, a material change, or a challenge to a previous rating. Define the cutoff, evidence horizon, included products, customer IDs, related parties, and exclusions. A relationship with no observed activity may still have a proposed activity profile; label it anticipated. An existing customer whose historic activity is unavailable is not equivalent to an inactive customer. Preserve UNKNOWN rather than filling the absence with zero.

Construct a customer-to-account map when necessary. Select the level at which factors are assigned before calculating totals. If one customer has three accounts, count the customer once in relationship metrics and explain how account-specific product or channel differences enter the profile. Separate joint customers where their ownership and purpose differ. Do not let convenient spreadsheet layout decide the analytical grain.

## 2. Normalize facts before assigning factors

Create concise evidence statements for business model, products, geographic exposure, channel, and ownership. Each statement should identify source, date, what is observed, what is reported, and any competing explanation. Avoid categorical proxies when better facts are available. A complicated ownership chart may be fully explained; a simple chart may hide missing control rights. Record complexity and opacity as different observations rather than treating every multi-layer structure as unexplained.

Compare amounts only after aligning currency, period, and basis. For example, three months of gross receipts do not equal annual net income. A rise from zero activity has no finite percentage increase; show the absolute change and a zero-baseline explanation. Expected turnover is an input assertion, not an independently measured capacity estimate. Where a factor depends on activity levels, show the original amount, normalization, and cutoff applied.

## 3. Apply a declared rubric without silently repairing it

In the fictional exercise, each factor takes an integer value from zero to three and the five weights sum to one. Contributions are factor value multiplied by weight, divided by three, and multiplied by one hundred. Their sum is an illustrative index from zero to one hundred. Zero means the lowest category within this fictional rubric, not an absence of financial-crime exposure. Three means the highest category within the rubric, not certainty of wrongdoing.

The declared weights are business 0.30, product 0.25, geography 0.20, channel 0.15, and ownership 0.10. Do not confuse a weight of 0.30 with thirty score points irrespective of the input. A business value of two contributes 20.0 points: 2 × 0.30 / 3 × 100. A product value of one contributes about 8.3333 points. Keep full precision during calculation and round only displayed scores to one decimal.

Bands use the unrounded score: LOW below 35; MODERATE at least 35 and below 65; HIGH at least 65. Displaying 35.0 after rounding a value slightly below 35 does not change its band. Any framework with thresholds near rounded display values needs a method note preserving the governing unrounded value. This prevents unexplained disagreement between an output table and its summary count.

## 4. Preserve missingness and calculate bounded illustrations

If one factor is unavailable, withhold the composite score and complete band. Do not replace the value with zero, average the remaining factors, or redistribute the missing factor's weight. Those alternatives change the question and can make incomplete customers appear easier to review. A partial sum can be useful diagnostically if clearly labelled and never used as the complete result.

A range can show whether the missing value could alter an illustrative band. Set the missing factor to the minimum and maximum of its declared scale solely for sensitivity analysis. C04's known contribution is 26.6667; geography can add zero through twenty points. The range is therefore 26.7–46.7, spanning LOW and MODERATE. This is an arithmetic range under a fictional scale, not a confidence interval, probability distribution, or estimated rating. Do not present the midpoint as an expected score.

## 5. Assess evidence completeness independently

Count supplied checklist items over the predeclared expected items, retaining every customer in the denominator. In the example each customer has four expected items, so six customers create twenty-four expectations. The complete-item counts 4, 4, 3, 2, 3, and 4 sum to twenty. Completeness is twenty divided by twenty-four, or 83.3%. Factor score availability is five divided by six, also 83.3%, but those equal percentages describe different objects and must carry different labels.

Receipt alone does not establish adequacy. Capture a material gap even where a document arrived. The fixed fixture checklist records whether required explanatory content is supplied, while actual document authenticity remains outside the exercise. If a purported ownership statement lacks the relevant rights, an input can be physically present but the ownership question unresolved. Document this convention before counting so reviewers do not mistake a completion metric for validation.

## 6. Evaluate mitigants without double credit

Map every proposed mitigating fact to the concern it addresses, the affected period, evidence of operation, and residual uncertainty. A control can help detect an issue without eliminating inherent exposure. Preserve the inherent score and describe control evidence separately unless a supplied authorized methodology explicitly defines a residual calculation. If it does, reproduce that method and make its assumptions visible; do not invent a discount rate.

C06's eight check results describe one supplied sample. Two exceptions yield a 25.0% descriptive exception fraction. The complement, 75.0%, is the fraction of sample checks without recorded exceptions; it is not a control effectiveness percentage and cannot reduce C06's score from 55 to 13.75. Examine what failed, whether selection was targeted, whether failures share a cause, and whether coverage excludes relevant activity. A larger sample is not automatically representative if the selection mechanism remains biased.

## 7. Separate findings, priority, and decision

A finding states an observation, criterion, implication, and evidence. Priority organizes further review. Human disposition records an authorized choice, its reasoning, conditions, and date. Do not merge them in a single “risk” field. C05's score of ten remains the correct illustrative arithmetic while its unsupported planned third-party funds call for targeted review. The correct response is to expose the tension, not alter the score retrospectively to make the narrative appear consistent.

Record why a gap matters to the stated decision. An ownership rights gap may prevent understanding who can direct the relationship. An outdated incidental address may have lower impact when legal identity and activity geography remain established. Avoid universal mandatory escalation rules disconnected from scope. Where law or a supplied policy requires specialist review, identify its source, applicability, and responsible role without asserting that the suite itself grants authority.

## 8. Challenge changes and write a reproducible recommendation

For repeat reviews, decompose movement into input changes, weight or rule changes, and overrides. Recompute the earlier case under the earlier rules before comparing with the new case. If a framework changed, show a same-input comparison to isolate its effect. Otherwise, a rating increase could merely reflect altered methodology. An unexplained override should remain unresolved even when the reviewer has seniority.

Test at least one benign alternative and one adverse alternative for the most consequential finding. A third-party transfer could be a documented commercial settlement rather than unexplained wealth, but that possibility does not establish provenance. A control exception could be a late record entry rather than an undetected event, but that requires timestamps and scope evidence. State what observation would distinguish the alternatives. Recommend evidence collection and review priorities with dependencies; leave actual customer decisions to their authorized owners.
