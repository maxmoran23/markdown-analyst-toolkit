# Analysis method — Sampling Design and Assurance Review

## 1. Freeze the question and design

Write the parameter in words and symbols: for a fixed eligible population of N units, D is the number that fail the predefined attribute, and P = D/N. Declare the period and criterion version. Decide whether a bound, point estimate, discovery exercise, or census is needed. Identify the action that a numerical result would inform. A sample selected to understand a failure is useful even when it cannot estimate its prevalence.

Record the tolerated rate, confidence level, sidedness, sample size, stopping rule, and whether the frame is finite. These are design choices, not outcomes to optimize after results arrive. If the purpose is an upper limit on exceptions, use a one-sided upper limit. A two-sided 95% interval allocates error probability differently and does not have the same upper endpoint. The method below uses alpha = 0.05 and an explicitly stated strict retention convention for integer-valued finite bounds.

## 2. Reconcile the population and stratification

Complete the counts bridge from 02. Validate unique IDs and nonoverlapping, exhaustive strata. A stratum must be defined from information available before outcomes are inspected. Risk-based oversampling can be legitimate probability sampling when every unit's selection chance is known. It does not justify treating all selected records as equally weighted if the sampling fractions differ.

For stratum h, record N_h, n_h, inclusion probability pi_h = n_h/N_h, and analysis weight w_h = 1/pi_h. Sum population counts once across strata. The example's H stratum has N_H = 4, n_H = 3, pi_H = 0.75 and weight 4/3. L has N_L = 8, n_L = 4, pi_L = 0.5 and weight 2. Four passing L selections therefore do not cancel a missing H assessment or validate the same conclusion in H.

Frame coverage and outcome classification are separate uncertainties. A perfect sampling algorithm cannot compensate for missing eligible units. Reclassifying a high-risk unit into another stratum after its result is known changes the design. Preserve the original assignment, explain any correction, and recalculate probabilities only under a defensible revised design.

## 3. Reproduce the selection

For the fixture, sort each stratum by its printed ID. Enumerate all increasing combinations of the required size in lexicographic order, starting rank at zero. H has four combinations; rank 2 yields H01, H03, H04. L has seventy combinations; rank 49 yields L02, L04, L06, L08. The two ranks are stipulated fictional results of independent uniform draws. No undocumented seed or platform random-number generator is needed for replay.

For a real design, verify that the original selector used the approved mechanism before outcomes were visible. Record duplicates, exclusions, and changes. Replacement without retaining the unavailable original creates a response bias risk. A preapproved reserve list still requires treatment of nonresponse and a clear inference method. Do not describe a sample as probability-based merely because a software function has “random” in its name.

The targeted L07 supplement follows a known archive concern and is not part of n_L. It can establish an additional observed exception. It cannot be inserted into the random sample denominator or used to recompute its upper bound. Show both original and supplemental results so the reader does not mistake a no-exception random selection for a no-exception investigation.

## 4. Assess selected units

Classify each selected unit PASS, FAIL, or UNABLE TO CONCLUDE against the frozen criterion. Record attribute-level facts, exact evidence locators, and contradictions. Aggregate an instance once: multiple attribute failures still count as one failed unit for the binary parameter. Preserve separate attribute counts only with their own denominators. A report of completion without the required artifact does not automatically pass; it may also fail to establish nonperformance.

Reconcile n_h = pass_h + fail_h + unable_h for each original stratum. For the fixture H is 3 = 1 + 1 + 1; L is 4 = 4 + 0 + 0. The probability sample total is 7 = 5 + 1 + 1. Adding the targeted failure creates eight reviewed selections with five passes, two failures, and one unresolved assessment. That combined total is descriptive only.

## 5. Compute descriptive rates and weighted scenarios

Selection coverage is n/N; assessment completeness is (pass + fail)/n; confirmed selected exception share is fail/n. Each answers a different question. A conclusive-only exception rate uses fail/(pass + fail), explicitly excluding unresolved outcomes and therefore not repairing their bias. A zero denominator returns null with a reason.

With complete stratified probability outcomes, the point estimator is P_hat = sum_h(N_h * d_h/n_h)/N. Equivalently, estimate the total as sum of y_i/pi_i across sampled units, then divide by N. Use the probabilities appropriate to the actual design. Do not average stratum percentages equally or substitute the pooled d/n when sampling fractions differ.

When a selected outcome is missing, this suite withholds a single complete estimate. It displays two transparent sensitivity scenarios: classify every unresolved selected unit as a pass, and classify every unresolved selected unit as a fail. In the fixture the weighted estimates are (4*1/3 + 8*0/4)/12 = 1/9 and (4*2/3 + 8*0/4)/12 = 2/9. They display as 11.1% and 22.2%. These are estimates under hypothetical completions of selected outcomes, not population identification bounds or a confidence interval. Unselected outcomes add sampling uncertainty. The judgmental L07 result remains separate.

## 6. Invert the finite-population distribution

For simple random sampling without replacement within a stratum, X is hypergeometric conditional on N, n, and D. The exact probability is Pr(X = k | D) = C(D,k) C(N-D,n-k) / C(N,n), where C(a,b) is zero for infeasible b. Compute the lower tail F_D(x) by summing feasible k from zero through the observed x. NIST's hypergeometric reference in 02 defines the underlying distribution; the inversion and discrete endpoint convention here are shown so they can be independently checked.

Define the one-sided conservative 95% upper integer bound U as the largest D in 0 through N satisfying F_D(x) > 0.05. Values with F_D(x) <= 0.05 are rejected by this rule. Report U/N. Using a non-strict convention can differ at an exact equality; state and retain the chosen rule. “Exact” refers to the finite-distribution calculation and its coverage under the design, not certainty about an individual population or immunity to classification errors.

For the L sample N = 8, n = 4, x = 0, F_D(0) = C(8-D,4)/C(8,4). D = 3 gives 5/70 = 0.0714286; D = 4 gives 1/70 = 0.0142857. U = 3, and U/N = 37.5%. Zero observed random-sample exceptions therefore fails to support the illustrative requirement that this upper bound be at most 25.0%. The separate observed L07 failure reinforces why “no exceptions in L” would be false, but is not used to modify this originally specified bound.

The H probability sample has an unresolved binary outcome. Withhold its completed-outcome bound pending resolution or a separately justified conservative missingness analysis. Do not add two nominal stratum bounds and claim 95% simultaneous population coverage. Simultaneous inference requires an approved joint method or explicit error allocation, such as a justified Bonferroni construction; this suite does not compute an overall confidence bound for the incomplete fixture.

## 7. Show the binomial contrast and sample-size limits

An independent Bernoulli model with n trials, zero failures, and a constant failure probability p gives Pr(X = 0) = (1-p)^n. Equating that tail to alpha produces p_U = 1 - alpha^(1/n). For n = 4 and alpha = 0.05, p_U = 0.5271291955, or 52.7%. This is a model-based contrast, not the chosen finite L result. The finite correction is material because half the L population was selected without replacement. Do not use a normal Wald interval that collapses to [0,0] after zero failures.

For a prespecified binomial zero-failure acceptance plan and tolerated probability t, n must satisfy n >= log(alpha)/log(1-t), rounded up. This formula does not guarantee that zero failures will be observed, validate a judgmental sample, or establish future process stability. For the finite case, search candidate n using the hypergeometric rule and the actual integer population, rather than rounding a binomial answer without analysis. A census removes sampling uncertainty for the fixed frame only when every eligible unit is correctly assessed.

## 8. Form the restricted conclusion

Lead with observed failures and evidence gaps, then state the permitted inference. Separate the random sample, targeted findings, incomplete H stratum, and L bound. Explain what would change the decision: recover H04 evidence, validate the frame and randomization for a real use, or approve an appropriate further design. Increasing a judgmental sample does not cure unknown inclusion probabilities. Repeatedly sampling until a desired result appears invalidates an unadjusted fixed-sample interpretation.

Preserve the entire analytical record before rendering: frame, exclusions, draw transcript, criteria, outcomes, calculations, method parameters, source register, alternatives, and pending approvals. The report, workbook, and dashboard must all reproduce the same denominators and qualify the same bound. Human review decides whether a restricted conclusion meets the original business question.
