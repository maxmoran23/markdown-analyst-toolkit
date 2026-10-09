# Analysis method — Monitoring Scenario and Threshold Review

## 1. Define the detection question

State the behavior the scenario seeks to identify, the eligible activities, the unit of analysis, the time window, and what a useful alert would mean. Distinguish an observed pattern from an allegation of wrongdoing. Separate detection capability from investigation quality and reporting decisions. A scenario can detect a review-worthy pattern without determining whether a filing is required.

Write the candidate predicate unambiguously. For the fixture it is score greater than or equal to threshold. Equality matters: U04 with score60 alerts under BASE60; U05 with score50 alerts under LOW50. Define missing score treatment, duplicate suppression, aggregation across transactions, and overlapping windows before comparing counts. A change to an aggregation window is a method change, not merely a new threshold.

## 2. Audit data and labels before metrics

Reconcile eligible population, scored population, labelled subset, unknown labels, excluded units, and candidate outputs. Count distinct units and distinct groups. Inspect extreme scores, missing features, unexpected reference values, stale profiles, and repeated units. If customer baselines are missing, do not replace them with an assumed maximum anomaly unless that is an explicit approved design whose effects are evaluated.

Review how labels were obtained. Synthetic labels are known by construction and useful for arithmetic and branch tests. They are not independent evidence of real-world target prevalence or coverage. Labels generated from the scenario's own rule conditions can make apparent recall perfect by definition. State this circularity and obtain independent evidence before performance conclusions.

Inspect negative labels as carefully as positives. A closed alert can mean insufficient information, a documented explanation, or an operational decision; it is not universally a true negative. An unfiled case is not automatically negative. Use the declared rubric and preserve unresolved labels as UNKNOWN.

## 3. Hold the comparison frame constant

Apply each candidate to the same eligible scored population and the same labelled evaluation subset. If a candidate changes eligibility or data dependencies, show both the shared comparison frame and the changed-coverage population. A candidate that drops difficult records cannot claim a fair performance improvement on the remaining easier sample.

Keep tuning and evaluation separate. When thresholds are chosen after seeing evaluation results, the observed winner is selected on that dataset and may overstate future performance. Record the candidates tried, the selection criterion, and the final locked candidate. A fresh holdout or later period is needed for an independent assessment. If it is unavailable, describe the results as exploratory.

Group correlated records. Multiple windows for one customer can share activity and labels. Randomly splitting those rows may let the same pattern appear in both development and holdout. Use group-aware and time-aware partitioning suited to the question. Do not compute a narrow binomial interval that treats dependent windows as independent without justification.

## 4. Build confusion matrices

On the labelled subset, TP is an alerted POSITIVE; FP is an alerted NEGATIVE; FN is a nonalerted POSITIVE; TN is a nonalerted NEGATIVE. Verify TP+FP+FN+TN equals the number of evaluable labelled units. UNKNOWN units do not enter these four cells. Count them separately, including which ones each candidate alerts.

Precision = TP/(TP+FP). Recall = TP/(TP+FN). False-positive rate = FP/(FP+TN). Labelled alert rate = (TP+FP)/labelled units. Total-population alert rate = candidate alerts across all scored eligible units / all scored eligible units. These denominators are different. An alert conversion rate based on filings is a different outcome and should not be relabeled precision.

A zero denominator yields null. No predicted positives makes precision undefined, not100%. No known positives makes recall undefined, not100%. Report counts alongside ratios so a one-case change remains visible. Round display only after calculations. A percentage-point change is the difference between percentages; a relative change divides by the baseline value.

## 5. Compare incremental cases and capacity

For each challenger list newly alerted units, no-longer-alerted units, retained alerts, and retained nonalerts relative to baseline. Attach labels and relevant risk characteristics. A higher threshold may reduce workload while dropping a known positive; show that loss directly rather than hiding it in an average score. A lower threshold may recover a positive while creating additional review workload.

Estimate workload from unique review opportunities after the actual deduplication logic, not raw rule hits. Multiple scenarios can alert on one case. If handling time is assumed, show it as an estimate: alerts times minutes per alert divided by 60 gives hours. Separate first-level handling, escalation, quality review, and rework if they materially differ. Do not assume an unchanged average handling time for a materially different mix of cases.

Capacity is a constraint, not permission to suppress risk. If a candidate exceeds capacity, identify staffing, prioritization, phasing, data improvement, or scenario redesign alternatives. If no candidate meets both coverage and operational constraints, recommend additional work rather than declaring the least bad candidate production-ready.

## 6. Bound what unknown labels could change

For the tiny fixture, enumerate the four possible label assignments to U07 and U08 to show sensitivity. This gives bounds conditional on treating every unknown as either positive or negative under the same rubric. It is not a confidence interval and does not estimate unknown real-world prevalence.

For BASE60, known TP2 and known positives3, U07 alerts and U08 does not. The lowest full-fixture recall is 2/4=50.0% when U07 is negative and U08 positive. The highest is 3/4=75.0% when U07 is positive and U08 negative. For HIGH75 the corresponding range is 25.0% to 50.0%. For LOW50 it is 75.0% to 100%. These ranges demonstrate why100% recall on three known positives cannot prove complete coverage.

For a larger dataset, report unknown-label counts and select a defensible review design. Do not substitute invented labels or an unsupported confidence band. Weighted estimators require actual selection probabilities and appropriate variance methods; if unavailable, keep descriptive subset metrics.

## 7. Challenge robustness and drift

Inspect performance by relevant strata, time periods, data sources, customer groups, and behavioral variants. A stable aggregate can conceal a weak subgroup. Small cells require counts and uncertainty, not overconfident rankings. Examine adjacent thresholds and feature perturbations to detect cliff effects. A missing value, changed currency unit, daylight-saving boundary, or late transaction can change a windowed rule even when the threshold is unchanged.

Define post-change monitoring before proposing deployment: population and alert counts, score distribution, data defects, sampled below-threshold review, backlog, handling time, label drift, and known-case capture. Specify human escalation and rollback triggers with evidence requirements. A successful fixture run supports implementation consistency on the fixture only. It does not replace independent validation or ongoing review.
