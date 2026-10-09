# Quality review — Monitoring Scenario and Threshold Review

## Reviewer protocol

Review from the raw evidence toward the conclusion. First reproduce the independent population controls, then the eligibility and exclusion rules, then the derived results, and finally the narrative. Reading a polished conclusion first can anchor the review to the author’s preferred outcome. Preserve the reviewer’s independent expected result before comparing it with the displayed value. A disagreement is evidence to investigate; do not quietly change the expected result to match the implementation.

Use three classes of checks. Structural checks verify unique IDs, row widths, types, enums, resolved links and required fields. Arithmetic checks verify counts, rates, amounts, predicates, joins and conservation equations. Judgment checks ask whether the concept, data, alternative explanation, limitation and recommendation fit the decision question. A structural pass cannot repair a conceptual failure. A reproducible formula cannot turn an unrepresentative sample into a population estimate. A well-supported observation does not supply missing authority to act.

Record the exact scope of each check, the expected result, actual result, evidence and reviewer state. PASS means the stated check matched within its defined scope. FAIL means evidence contradicts the criterion. REVIEW_REQUIRED means a human judgment or unresolved interpretation remains. NOT_TESTED means the procedure was not performed. These states are not interchangeable. A test that could not run must never be marked pass because the template looks plausible. An unresolved dependency can coexist with correct arithmetic, so report both.

## Artifact and session acceptance

Reopen the actual files if the session can create them. Compare the report, workbook and dashboard against one authoritative case representation. Check all required sections and domain tables, all rows, nulls, currencies, decimals, dates, evidence IDs, findings, actions and QA states. Check that filtering changes the visible subset without rewriting the total-scope counts. Export a filtered CSV and compare record identities, not just the header. Confirm that special characters remain literal text and do not become spreadsheet formulas or executable markup.

Inspect the rendered pages for clipped values, lost continuation rows, unreadable columns and orphaned headings. A successful file save does not establish readable rendering. If visual inspection is unavailable, record that limitation. Do not claim testing in Microsoft Office or enterprise Copilot unless it actually occurred in the relevant environment. The supplied fixture checker proves particular arithmetic and table relationships; it does not establish that a language model consistently follows this method on new cases.

A completion statement must name its level. The fixture can be arithmetically complete while operational labels, original transactions, qualified review or human authorization are absent. A report can be copy-ready while no DOCX file was created. A historical desk review can be complete while a downstream referral is open. Preserve these distinctions in the final response. The release gate is not a request to invent acceptance; it is a test of whether the supplied evidence supports the requested completion claim.

## Complete adversarial and boundary test specifications

### Q01: Equality at 60

**Isolated input change.** Add an otherwise known-negative eligible unit with score 60 in RETAIL and a new group.

**Required expected result.** BASE60 hit=true;HIGH75=false;LOW50=true;SEGMENTED=true. Each hitting candidate gains one FP and one raw hit.

**Interpretation.** The inclusive boundary is tested without changing a source record or relying on rounded display.

### Q02: Just below 60

**Isolated input change.** Use 59.999 rather than 60 on the same isolated negative unit.

**Required expected result.** BASE60=false;HIGH75=false;LOW50=true;SEGMENTED=true. BASE60 must not gain an alert.

**Interpretation.** Numerical presentation and analytical comparison use different stages.

### Q03: Unknown high score

**Isolated input change.** Change U35 label from UNKNOWN to NEGATIVE without changing its score 62.

**Required expected result.** BASE60 and LOW50 gain one FP; known_n 30; unknown_n 6. Raw hits, routing and workload stay unchanged.

**Interpretation.** Changing labels affects outcome matrices but does not change detection or workload inputs.

### Q04: Unknown positive below threshold

**Isolated input change.** Change U28 from UNKNOWN to POSITIVE with score 31 unchanged.

**Required expected result.** All candidates gain one FN; known positives 17. No candidate gains a hit or workload.

**Interpretation.** Outcome maturation can worsen measured recall without any change in the threshold engine.

### Q05: Censored becomes positive

**Isolated input change.** Change U36 label from CENSORED to POSITIVE at a later explicitly named cutoff.

**Required expected result.** All candidates gain one FN; the earlier cutoff remains preserved. Selected below-threshold known positives rise from 3 to 4.

**Interpretation.** Do not backfill a matured outcome into an earlier protected result without versioning.

### Q06: Remove suppression

**Isolated input change.** Remove G17 from the suppression list with all raw inputs fixed.

**Required expected result.** Every candidate gains 2 retained hits,1 queued case,2.25 hours and 1 retained known positive; raw matrices unchanged.

**Interpretation.** Routing correction is distinct from threshold performance.

### Q07: Suppress a nonhit group

**Isolated input change.** Add G18 to suppression while testing BASE60.

**Required expected result.** U35 is the only BASE60 hit in G18; retained hits decrease 1, queued cases decrease 1 and hours decrease 2.0; raw matrix unchanged.

**Interpretation.** The same group may have a different hit composition under another candidate.

### Q08: Remove a merged negative

**Isolated input change.** Exclude U02 from the population with an explicit changed-scope record.

**Required expected result.** For BASE60, FP decreases 1, raw and retained hits decrease 1;G01 remains a case and workload falls 0.25 hours.

**Interpretation.** Removing a child saves only incremental merge time, not the full lead cost.

### Q09: Remove a merged lead

**Isolated input change.** Exclude U01 while leaving U02.

**Required expected result.** For BASE60 TP decreases 1 and U02 becomes G01 lead; case count unchanged and workload falls 0.25 hours.

**Interpretation.** Lead reassignment prevents falsely claiming a full case reduction.

### Q10: All negative labels

**Isolated input change.** Relabel all known positive units NEGATIVE solely in an isolated mathematical test.

**Required expected result.** All candidate recalls=null becauseTP+FN=0; precision remains calculable where known hits exist.

**Interpretation.** No positive denominator means recall is undefined, not perfect.

### Q11: No known hits

**Isolated input change.** Evaluate a 999 threshold on the existing frame.

**Required expected result.** Raw hits 0;TP0 FP0 FN16 TN13; precision=null;recall 0/16=0.0%;queue 0;hours 0.

**Interpretation.** A zero queue is not success when known positives remain below the threshold.

### Q12: One unknown hit only

**Isolated input change.** Use an explicit isolated candidate that selects U35 and no other unit.

**Required expected result.** Raw hits 1;known TP0 FP0;precision=null;unknown-hit count 1;queue 1 and 2.0 hours unless G18 suppressed.

**Interpretation.** Workload can exist without a known-label precision denominator.

### Q13: Group crosses partitions

**Isolated input change.** Change U02 partition to HOLDOUT while G01 remains shared with U01.

**Required expected result.** Partition-integrity check fails; protected-performance interpretation is blocked pending regrouping.

**Interpretation.** A uniqueunitID does not establish independent evaluation.

### Q14: Overlapping candidate definitions

**Isolated input change.** Change LOW50 score definition while retaining its name.

**Required expected result.** Treat the change as a new configuration with a distinct version; pure-threshold comparison no longer holds.

**Interpretation.** Candidate names are not evidence that features and eligibility match.

### Q15: Capacity rises

**Isolated input change.** Keep LOW50 inputs fixed and change illustrative capacity from 15 to 30 hours.

**Required expected result.** The capacity comparison changes from 27>15 to 27<=30; missing labels and G17 routing restrictions remain.

**Interpretation.** Staffing assumptions resolve only capacity, not all deployment gates.

### Q16: Lead review time doubles

**Isolated input change.** Double all segment lead times while retaining the 0.25-hour child increment.

**Required expected result.** Recompute group costs; do not simply double total hours because merge increments remain fixed.

**Interpretation.** Lead and incremental workload components must stay separate.

### Q17: Selected review result unavailable

**Isolated input change.** Remove the U20 review result while retaining its selected flag.

**Required expected result.** Selected count remains 6; known selected results fall from 4 to 3; positive count remains 3 and unavailable results increase.

**Interpretation.** An unavailable result does not erase a selected unit from the denominator.

### Q18: Holdout reused

**Isolated input change.** Add a fifth threshold chosen after seeing HOLDOUT labels.

**Required expected result.** The earlier holdout becomes descriptive reuse; it is not independent evidence for the fifth candidate.

**Interpretation.** Further searching requires fresh protected evidence or an explicitly qualified design.

## Reviewer challenge questions by analytical stage

**M01 — Freeze the analytical unit.** Independently reproduce this checkpoint: Reconcile 36 =29 known +4 UNKNOWN +3 CENSORED. Count the positive and negative labels separately:16 and 13. Every candidate must start from the same 36 records. Then test the adverse branch: If a candidate drops records with unknown labels before calculating workload, its apparent workload advantage is invalid because those records still exist operationally. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M02 — Lock eligibility before scores.** Independently reproduce this checkpoint: All 36 fixture units are eligible. The score cutoff is a candidate decision applied after eligibility, not an eligibility filter. Then test the adverse branch: If an excluded unit is later found to carry the relevant risk mechanism, create a coverage issue and re-scope the comparison; do not silently append it to the best-performing candidate only. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M03 — Protect dependence groups.** Independently reproduce this checkpoint: G01 through G06 are TRAIN, G07 through G12 VALIDATION, and G13 through G18 HOLDOUT. Each group has two units and no cross-partition membership. Then test the adverse branch: If G01 appears in HOLDOUT after a join, freeze interpretation of protected performance until the overlap is removed or a dependence-aware method is justified. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M04 — Separate candidate development from evaluation.** Independently reproduce this checkpoint: The specimen stipulates all four candidates were declared before protected results. That stipulation is an illustrative premise, not evidence that an actual organization operated this way. Then test the adverse branch: If LOW50 was selected after inspecting HOLDOUT labels, report the selection honestly and obtain a new protected evaluation; do not call the old holdout untouched. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M05 — Construct the available-label set.** Independently reproduce this checkpoint: TRAIN has 10 known labels, VALIDATION10 and HOLDOUT9. Their sum is 29; the unavailable counts are 2,2 and 3. Then test the adverse branch: If an unknown unit later becomes positive, update the label version and all affected matrices; preserve the old cutoff results rather than rewriting history. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M06 — Apply the inclusive score predicate.** Independently reproduce this checkpoint: BASE60 uses 60 everywhere; HIGH75 uses 75; LOW50 uses 50; SEGMENTED uses 55 for RETAIL,60 for SMALL_BUSINESS and 65 for CORRESPONDENT. Then test the adverse branch: A score 60 is a BASE60 hit. A score 59.999 is not. Converting 59.999 to 60 for display must not change the stored predicate result. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M07 — Calculate confusion matrices at unit grain.** Independently reproduce this checkpoint: For ALL BASE60 the matrix isTP11 FP9 FN5 TN4. Precision 11/20=55.0%; recall 11/16=68.8%. Seven unavailable labels are outside this matrix. Then test the adverse branch: A merged case containing two raw hit units contributes two units to the unit matrix. Replacing those with one case changes the grain and invalidates direct comparison. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M08 — Measure raw workload separately.** Independently reproduce this checkpoint: Raw hits are 21 for BASE60,11 for HIGH75,27 for LOW50 and 19 for SEGMENTED. These denominators are 36 units, not 29 known labels. Then test the adverse branch: If a report labels 21 as a false-positive count, reject the statement: it includes known positives and unavailable outcomes as well as negatives. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M09 — Replay suppression before merge.** Independently reproduce this checkpoint: G17 removes U33 and U34 when they hit. U33 is a known positive hit for all candidates. U34 hits BASE60, HIGH75, LOW50 and SEGMENTED; two hits are removed from each. Then test the adverse branch: If a candidate appears to save two alerts solely because G17 was omitted upstream, recover the suppressed ledger and restate both raw and retained results. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M10 — Merge only within the declared group.** Independently reproduce this checkpoint: Queued cases are 11,8,17 and 9 respectively. A case-level workload reduction can arise even if raw coverage is unchanged. Then test the adverse branch: A nonhit sibling is not automatically a detected unit because its group has a case. Credit requires explicit evidence that review scope included that sibling and its relevant activity. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M11 — Calculate workload from routed cases.** Independently reproduce this checkpoint: BASE60 requires 19.5 hours, HIGH7511.75, LOW5027.0 and SEGMENTED14.5 over the full supplied frame. The illustrative combined capacity is 15 hours. Then test the adverse branch: Do not set a threshold solely to make workload fit capacity. A lower workload can hide missed positives, incomplete labels, unauthorized suppression or a changed unit of counting. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M12 — Preserve segment and incremental effects.** Independently reproduce this checkpoint: SEGMENTED gains RETAIL U03 relative to BASE60 but loses CORRESPONDENT U11 and U23 and removes UNKNOWN U35. The aggregate known-positive count falls 11 to 10. Then test the adverse branch: A favorable average cannot establish that a segment-specific loss is acceptable. Request explicit rationale and human risk judgment for each material segment effect. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M13 — Review below-threshold activity.** Independently reproduce this checkpoint: BASE60 has 15 nonhits. Assigned ranks select U03,U07,U15,U20,U28,U36. Selected outcomes: 3 POSITIVE, 1 NEGATIVE, 1 UNKNOWN and 1 CENSORED. Nine frame units are not reviewed in this draw. Then test the adverse branch: Do not divide three positives by four known selected labels and call 75% the population missed-positive rate; selection is illustrative and two selected outcomes are unavailable. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M14 — Use uncertainty methods only when justified.** Independently reproduce this checkpoint: No confidence interval is attached to the 36-unit designed fixture. File 10 includes separate mathematical demonstrations labeled as such, with their assumptions and exact inputs. Then test the adverse branch: A narrow interval from thousands of correlated windows does not prove precision if the effective independent information is much smaller or outcomes are selected after alerting. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M15 — Challenge capacity and sensitivity together.** Independently reproduce this checkpoint: Removing G17 suppression adds one correspondent lead and one child, or 2.25 hours, to every candidate. It restores known positive U33 to the routed numerator. Then test the adverse branch: Do not treat an unknown future capacity as an exact number. Supply a range and the conditions under which the chosen candidate would cease to fit it. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M16 — Define change and monitoring gates.** Independently reproduce this checkpoint: LOW50 is further-validation-only. HIGH75 and SEGMENTED are not supported from this case. BASE60 remains a descriptive baseline, not an endorsed live configuration. Then test the adverse branch: A new approved threshold without post-change input controls and rollback evidence can create an unobserved coverage gap; keep the implementation and monitoring dependencies visible. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

## Required final QA record

| check_id | check_scope | expected | actual | status | reviewer | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| MT-Q01 | Population conservation | 36 = 29 known + 4 UNKNOWN + 3 CENSORED | 36 = 29 + 4 + 3 | PASS | Fictional checker | SYN-001 |
| MT-Q02 | Partition segregation | 12 units per partition; no group crosses partitions | TRAIN12 VALIDATION12 HOLDOUT12; groups disjoint | PASS | Fictional checker | SYN-001 |
| MT-Q03 | Candidate matrices | Each TP+FP+FN+TN equals known_n | All sixteen matrices reconcile | PASS | Fictional checker | SYN-001;SYN-002 |
| MT-Q04 | Suppression authority | Current authorization plus expiry and coverage evidence | No authorization supplied for G17 | FAIL | Fictional checker | SYN-003 |
| MT-Q05 | Below-threshold frame | 15 frame units; 6 selected; 9 not reviewed | 15 = 6 + 9; selected outcomes P3 N1 U1 C1 | PASS | Fictional checker | SYN-004 |
| MT-Q06 | Holdout authorization | Protected review record and separate human decision | Only an illustrative prefreeze is supplied | REVIEW_REQUIRED | NOT_RECORDED | SYN-002 |

The populated QA rows above describe the fictional case. Reperform them for the current session and add the actual result, rather than copying the specimen PASS labels as evidence that a live review occurred. Preserve every failed or unperformed check in the final report. The independent fixture checker in file 10 must run from its own raw inputs without reading this repository or fetching external data.
