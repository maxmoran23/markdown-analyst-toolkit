# Quality review — Monitoring System Independent Challenge and Validation

## Reviewer protocol

Review from the raw evidence toward the conclusion. First reproduce the independent population controls, then the eligibility and exclusion rules, then the derived results, and finally the narrative. Reading a polished conclusion first can anchor the review to the author’s preferred outcome. Preserve the reviewer’s independent expected result before comparing it with the displayed value. A disagreement is evidence to investigate; do not quietly change the expected result to match the implementation.

Use three classes of checks. Structural checks verify unique IDs, row widths, types, enums, resolved links and required fields. Arithmetic checks verify counts, rates, amounts, predicates, joins and conservation equations. Judgment checks ask whether the concept, data, alternative explanation, limitation and recommendation fit the decision question. A structural pass cannot repair a conceptual failure. A reproducible formula cannot turn an unrepresentative sample into a population estimate. A well-supported observation does not supply missing authority to act.

Record the exact scope of each check, the expected result, actual result, evidence and reviewer state. PASS means the stated check matched within its defined scope. FAIL means evidence contradicts the criterion. REVIEW_REQUIRED means a human judgment or unresolved interpretation remains. NOT_TESTED means the procedure was not performed. These states are not interchangeable. A test that could not run must never be marked pass because the template looks plausible. An unresolved dependency can coexist with correct arithmetic, so report both.

## Artifact and session acceptance

Reopen the actual files if the session can create them. Compare the report, workbook and dashboard against one authoritative case representation. Check all required sections and domain tables, all rows, nulls, currencies, decimals, dates, evidence IDs, findings, actions and QA states. Check that filtering changes the visible subset without rewriting the total-scope counts. Export a filtered CSV and compare record identities, not just the header. Confirm that special characters remain literal text and do not become spreadsheet formulas or executable markup.

Inspect the rendered pages for clipped values, lost continuation rows, unreadable columns and orphaned headings. A successful file save does not establish readable rendering. If visual inspection is unavailable, record that limitation. Do not claim testing in Microsoft Office or enterprise Copilot unless it actually occurred in the relevant environment. The supplied fixture checker proves particular arithmetic and table relationships; it does not establish that a language model consistently follows this method on new cases.

A completion statement must name its level. The fixture can be arithmetically complete while operational labels, original transactions, qualified review or human authorization are absent. A report can be copy-ready while no DOCX file was created. A historical desk review can be complete while a downstream referral is open. Preserve these distinctions in the final response. The release gate is not a request to invent acceptance; it is a test of whether the supplied evidence supports the requested completion claim.

## Complete adversarial and boundary test specifications

### Q01: Exact amount threshold

**Isolated input change.** Use amount 10000, count 3, originators 2 and label POSITIVE.

**Required expected result.** R1=true; I1=false; C1=true. This is a known-positive fidelity loss.

**Interpretation.** Equality is a material part of the specification.

### Q02: Just below amount

**Isolated input change.** Use amount 9999.99, count 3 and originators 2.

**Required expected result.** R1=false; I1=false; C1=false.

**Interpretation.** Do not round the input to 10000 before comparison.

### Q03: Just above amount

**Isolated input change.** Use amount 10000.01, count 3 and originators 2.

**Required expected result.** R1=true; I1=true; C1=true.

**Interpretation.** A correct result above the boundary does not disprove an equality defect.

### Q04: Count below boundary

**Isolated input change.** Use amount 14000, count 2 and originators 2.

**Required expected result.** All three variants return false.

**Interpretation.** A high amount does not override the minimum eligible event count.

### Q05: Count at boundary

**Isolated input change.** Use amount 14000, count 3 and originators 2.

**Required expected result.** All three variants return true.

**Interpretation.** The count comparator is also inclusive.

### Q06: Originator below boundary

**Isolated input change.** Use amount 18000, count 5 and originators 1.

**Required expected result.** R1=false; I1=false; C1=true.

**Interpretation.** This is conceptual sensitivity, not an implementation mismatch.

### Q07: Originator at boundary

**Isolated input change.** Use amount 18000, count 5 and originators 2.

**Required expected result.** All three variants return true.

**Interpretation.** The challenger no longer adds a different result for this unit.

### Q08: Amount absent

**Isolated input change.** Use amount null, count 4 and originators 3.

**Required expected result.** R1=unknown; I1=false; C1=unknown.

**Interpretation.** Unknown versus false is a fidelity difference even when the outcome label is unknown.

### Q09: Amount explicitly zero

**Isolated input change.** Use amount 0, count 4 and originators 3.

**Required expected result.** All three variants return false.

**Interpretation.** Zero is actual data and is not equivalent to a missing input.

### Q10: Negative credit amount

**Isolated input change.** Use amount -10000 in this positive-credit aggregate scope.

**Required expected result.** The input eligibility or amount check must reject the negative aggregate before applying the intended credit rule.

**Interpretation.** Do not silently take the absolute value to force a hit.

### Q11: Duplicate unit ID

**Isolated input change.** Add a second V02 record with a different amount.

**Required expected result.** Structural QA fails; preserve both input representations and resolve identity before counting.

**Interpretation.** Dropping an arbitrary row can hide the boundary defect.

### Q12: Unknown outcome on a hit

**Isolated input change.** Change V03 label from POSITIVE to UNKNOWN while keeping features fixed.

**Required expected result.** I1 still has 4 hits; known TP falls from 4 to 3; known_n becomes 19 and unknown_n becomes 5.

**Interpretation.** Labels and implementation outputs have different provenance.

### Q13: Correct only amount operator

**Isolated input change.** Replace I1 greater-than with greater-or-equal while retaining missing-to-false.

**Required expected result.** Four boundary mismatches resolve; four null mismatches remain.

**Interpretation.** A partial patch is not a complete correction.

### Q14: Correct only null handling

**Isolated input change.** Make I1 return unknown for missing amount while retaining strict greater-than.

**Required expected result.** Four null mismatches resolve; four known positive boundary losses remain.

**Interpretation.** The other defect must stay open.

### Q15: Full reference-equivalent correction

**Isolated input change.** Implement R1 exactly on all 24 inputs.

**Required expected result.** All 24 outputs match R1: 8 true, 12 false and 4 unknown.

**Interpretation.** Conceptual limitations and representative-outcome requirements remain.

### Q16: New transaction evidence

**Isolated input change.** Provide complete transaction-to-feature lineage for selected units only.

**Required expected result.** D03 can be reviewed for that limited subset; unprovided units remain outside lineage assurance.

**Interpretation.** Partial new evidence cannot justify a whole-population lineage claim.

### Q17: Favorable validation score

**Isolated input change.** Calculate 12 passed tests divided by 24 total tests.

**Required expected result.** 50.0% is merely a test-state proportion; no validated quality score exists.

**Interpretation.** The four failed tests and eight blocked tests retain their individual consequences.

### Q18: Vendor calls the rule a model

**Isolated input change.** A provider describes a fixed rule as AI without design evidence.

**Required expected result.** Classification remains based on actual design and use; marketing does not establish applicability.

**Interpretation.** Request the mathematical and operational basis before borrowing model-specific claims.

## Reviewer challenge questions by analytical stage

**M01 — Bound the reviewed subject.** Independently reproduce this checkpoint: The fixture tests supplied feature-level rules and calculations. Raw transaction ingestion, real routing and actual human decisions are outside its evidence. Then test the adverse branch: If a report says the monitoring system is validated after only replaying a predicate, revise the opinion to the tested component and name the remaining boundaries. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M02 — Classify the component before borrowing a framework.** Independently reproduce this checkpoint: R1, I1 and C1 are fixed rules; the feature transform is arithmetic. No fitted probability or theory-based estimate is supplied. Current SR26-2 applicability is not presumed. Then test the adverse branch: An opaque vendor score cannot be classified from its product name. Request design and use information; preserve UNKNOWN classification until sufficient evidence exists. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M03 — Establish objective challenge.** Independently reproduce this checkpoint: Fictional test roles demonstrate the workflow only. Actual reviewer qualifications, authority and objectivity remain unrecorded. Then test the adverse branch: If the same assistant generates a reference by copying the implementation, it has not independently challenged implementation fidelity. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M04 — Translate purpose into explicit invariants.** Independently reproduce this checkpoint: R1 requires USD amount>=10000, eligible count>=3 and originators>=2. Unknown amount returns unknown before any comparison. Then test the adverse branch: If a count includes reversed or rejected events while the stated purpose concerns posted credits, a numerically correct threshold can still implement the wrong concept. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M05 — Reconcile supplied features.** Independently reproduce this checkpoint: V01 through V24 are unique. Each of four segments has six units. Amounts are present for 20 and missing for 4. Then test the adverse branch: A complete unit-ID count does not imply all features are complete; keep 24-unit population coverage separate from 20-unit amount completeness. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M06 — Challenge transaction lineage.** Independently reproduce this checkpoint: The specimen intentionally stops at supplied features, so D03 is BLOCKED. No amount aggregation is represented as independently validated. Then test the adverse branch: Do not repair missing source detail by inventing plausible transactions that sum to the supplied feature amount. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M07 — Construct an independent reference oracle.** Independently reproduce this checkpoint: R1 returns true for V02,V03,V08,V09,V14,V15,V20,V21;false for 12 other present-amount units;unknown for V06,V12,V18,V24. Then test the adverse branch: A reference function that uses I1’s strict greater-than comparator cannot detect the intended boundary defect. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M08 — Reperform implementation outputs.** Independently reproduce this checkpoint: I1 returns true for V03,V09,V15,V21 andfalse for 20 others. The fixture is a behavior-level comparison; it does not inspect a production deployment. Then test the adverse branch: If the live implementation contains an additional eligibility filter, it is a different candidate and requires a new comparison scope rather than being quietly folded into I1. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M09 — Classify mismatches by mechanism.** Independently reproduce this checkpoint: There are 8 differences:4 boundary mismatches at V02,V08,V14,V20 and 4 missing-state mismatches at V06,V12,V18,V24. Then test the adverse branch: Do not report 8 missed positives: the four missing-state units have unknown labels. Only the four boundary mismatches are known positive losses. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M10 — Challenge the excluded mechanism.** Independently reproduce this checkpoint: R1 excludes V05,V11,V17,V23 because each has only one originator. All four are supplied positive labels in the fictional case. Then test the adverse branch: A specification pass on originator count does not dispose of the concept concern; keepI03 PASS distinct fromC02 FAIL. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M11 — Use a diagnostic challenger transparently.** Independently reproduce this checkpoint: C1 removes the originator minimum while retaining amount>=10000 and count>=3. It captures 12 known positives with no known negatives in this designed fixture. Then test the adverse branch: The constructed label pattern favors this challenger by design. It does not establish superior real-world precision, calibration or operational value. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M12 — Calculate outcomes at the right denominator.** Independently reproduce this checkpoint: All matrices have 20 known labels:12 positive and 8 negative. R1 recall 8/12;I1 recall 4/12;C1 recall 12/12. Precision is 100% in all three, with different alert counts. Then test the adverse branch: A report showing 100% precision without the 4,8 or 12 true-positive count hides the small designed denominator and cannot support an effectiveness conclusion. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M13 — Separate evidence gaps from adverse results.** Independently reproduce this checkpoint: Twenty-four tests yield 12 PASS,4 FAIL and 8 BLOCKED. Missing transaction lineage is BLOCKED, while missing-to-false behavior is FAIL because the supplied behavior contradicts R1. Then test the adverse branch: Do not merge FAIL and BLOCKED into one numerical score unless a clearly supplied scoring rule justifies it; a weighted average can conceal a release-blocking defect. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M14 — Evaluate ongoing monitoring feasibility.** Independently reproduce this checkpoint: Four missing amounts equal 16.7% of 24 units. Four present-input boundary differences equal 20.0% of 20 present amounts. No time-series drift inference is possible. Then test the adverse branch: An alert-rate change can reflect volume, customer mix or source defects. Request comparable periods and stable definitions before attributing it to model or rule decay. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M15 — Specify closure evidence before accepting a fix.** Independently reproduce this checkpoint: I01 requires corrected inclusive comparison;I04 requires unknown routing. Replaying all 24 units ensures the 12 valid negatives and 4 original true hits are preserved while defects are corrected. Then test the adverse branch: A patch that restores four boundary hits but still turns missing amounts intofalse resolves only one mechanism, not the whole implementation issue set. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M16 — Form a bounded validation opinion.** Independently reproduce this checkpoint: Do not support release of I1 on the supplied evidence. R1 arithmetic is reproducible, but implementation differs and effectiveness, lineage and governance evidence remain incomplete. Then test the adverse branch: Avoid a single approved stamp. It would obscure which gates are fixture-only passes, which fail and which require actual institutional evidence. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

## Required final QA record

| check_id | check_scope | expected | actual | status | reviewer | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| MV-Q01 | Feature manifest | 24 unique units and four segments of 6 | 24 unique;6 per segment | PASS | Fictional checker | SYN-101 |
| MV-Q02 | Present and absent amounts | 24=20 present+4 absent | 20 present and 4 null | PASS | Fictional checker | SYN-101 |
| MV-Q03 | Reference result | 8 true;12 false;4 unknown | 8 true;12 false;4 unknown | PASS | Fictional checker | SYN-101;SYN-102 |
| MV-Q04 | Implemented result | Specification-equivalent tri-state result | 4 true;20 false;0 unknown | FAIL | Fictional checker | SYN-101;SYN-102 |
| MV-Q05 | Mismatches | Four boundary and four null-state differences | 8 mismatches; mutually exclusive classes | PASS | Fictional checker | SYN-101;SYN-102 |
| MV-Q06 | Generalization gate | Independent operational data required | Synthetic designed examples only | REVIEW_REQUIRED | NOT_RECORDED | SYN-101 |
| MV-Q07 | Human decision | Actual authorized decision required | NOT_RECORDED | NOT_TESTED | NOT_RECORDED | SYN-103 |

The populated QA rows above describe the fictional case. Reperform them for the current session and add the actual result, rather than copying the specimen PASS labels as evidence that a live review occurred. Preserve every failed or unperformed check in the final report. The independent fixture checker in file 10 must run from its own raw inputs without reading this repository or fetching external data.
