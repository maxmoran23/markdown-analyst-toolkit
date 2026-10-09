# Analysis method — Data Quality and Fitness for Use

## 1. Define fitness before scoring

Name the consumer, output, consequence of wrong data, and field dependencies. For each critical field trace how a defect could alter the consumer's result. A blank transaction amount affects aggregation; an invalid date affects windows; a missing identifier affects joins; duplicated customers can split or duplicate activity depending on the consumer. Criticality belongs to a use and failure mechanism, not permanently to a column name.

Inventory seven dimensions: completeness, validity, consistency, uniqueness, timeliness, reconciliation, and lineage. Not every dimension has a calculable rate for every extract. Record untested dimensions rather than manufacturing an aggregate completeness claim from the dimensions that happened to be measurable. A format check verifies format; it does not verify the real-world truth of a value.

## 2. Reconcile the population and preserve the original

Start from a read-only representation of the supplied records. Record source count, in-scope count, excluded count, unreadable count, distinct extract keys, distinct business keys, and any source totals. The source count must reconcile to included plus excluded plus unreadable rows according to the chosen extraction method. If a file is partially read, the visible rows are a subset, not the full population.

Retain an original-data table and create derived fields separately. Do not overwrite a malformed date with a guessed date, fill an absent identifier with a sequential number that appears authentic, or drop duplicate records to improve the pass rate. Proposed repairs need source-owner confirmation. The same input and contract version should produce the same defect ledger.

## 3. Apply conditional denominators

Every rule specifies an eligible set before testing. A birth-date rule for individuals has individuals as its denominator. An entity's blank birth date is not a failure of that rule. An active-record freshness rule excludes genuinely inactive records only if the contract says so. Unknown entity type can make applicability unknown; record the unknown eligibility rather than arbitrarily excluding it.

For rule j, let E_j be eligible, F_j be confirmed failures, and U_j be unassessable eligible records. Record pass = E_j minus F_j minus U_j. Confirmed defect rate = F_j / E_j. Unknown rate = U_j / E_j. The absence of a value required by the rule is itself a confirmed completeness failure, not automatically an unassessable record. A rule that cannot run because the reference list is missing is unassessable. Keep those cases separate.

A zero eligible count produces a null rate and Not applicable. It is not a perfect score. Report unknown eligibility separately from known eligibility. If eligibility uncertainty is material to a critical rule, the fitness recommendation is restricted or unable to assess until resolved.

## 4. Test named rules and capture record evidence

For each rule write the predicate in plain language, comparator including equality, null behavior, conditional population, severity mechanism, and parameter source. A calendar parser should reject Feb 30. A code-list check should use the named version. A cross-field check should define which timestamps represent events rather than uploads. A timeliness check should define the as-of date, calendar or business days, and whether equality at the horizon passes.

For uniqueness, distinguish duplicate groups, affected rows, and excess rows. If a key occurs k times, it contributes one duplicate group, k affected rows, and k minus one excess rows. These answer different questions. Mark every member of the group so a reviewer can trace lineage. A duplicate key does not prove the records represent the same real person; it proves a violation of the stated key contract. A many-account customer design may permit repeated customer keys.

A possible match based on similar names is a separate identity-resolution inference. Do not turn a fuzzy similarity score into a confirmed duplicate or an automatic merge. Show the candidate pairs, matching features, conflicting attributes, and the human decision needed. If the use requires unique entity identity, a simple exact-key check has a known coverage limit.

## 5. Separate check counts from affected records

Rules can overlap on one row. In the worked example D02 fails both name completeness and date validity. Count it once in distinct affected-record metrics and twice in rule-failure totals. Similarly, D03 is both invalid by country code and stale. A union of affected IDs is required; summing per-rule defect counts overstates the number of affected records.

Passing-check rate = total passes across rules divided by total eligible rule checks, when every included rule is assessable. This is a diagnostic of the selected rule inventory. It weights rules by eligibility count, may double-count records across checks, and does not measure probability that a row is correct. A rule-average score is a different measure. Never label either one “data accuracy” without defining the method and limitations.

A critical rule failure must remain a visible gate independent of an overall score. Adding many easy low-risk checks must not change a restricted recommendation into an unrestricted one. A critical field could have a low defect rate yet affect the most consequential records; inspect concentration and affected uses rather than only totals.

## 6. Locate defects and assess distribution

Break down failures by source, period, product, jurisdiction where relevant, transformation version, and consumer. A recent source change concentrated in one feed suggests a different remediation path from random data-entry defects. Use these breakdowns as hypotheses about cause. A correlation between a source and failures does not by itself prove that a specific transformation introduced them.

Where source-to-output pairs are available, reperform the transformation for failing and passing records. Check truncation, character encoding, date conventions, timezone changes, join cardinality, null substitution, late-arriving updates, and reference-list version. A systematic one-hour shift might matter for an event-window test even when daily totals agree. Test the actual consuming calculation if the consequence depends on it.

## 7. Remediation and retest

For each issue specify the source owner role, affected IDs, intended correction, evidence required, backfill or restatement implications, downstream consumers, and rollback conditions. A manual patch to the output can mask an upstream defect that will recur on the next extract. If the patch is accepted as a temporary measure, retain its authorization, scope, expiry, and reconciliation evidence.

Retest the original failing records, a fresh post-change extract, and relevant passing records that could be harmed by the change. Reconcile row counts and totals before and after correction. A deduplication fix changes the denominator; report the old six-row extract and new corrected population separately. Do not compare 100% of a smaller repaired population with the old rate without explaining the exclusions and key corrections.

State what the check inventory cannot establish: real-world identity accuracy, unknown upstream omissions, untested semantic defects, and future stability. Passing the visible checks is a bounded observation. The human owner decides whether that evidence is adequate for the intended use.
