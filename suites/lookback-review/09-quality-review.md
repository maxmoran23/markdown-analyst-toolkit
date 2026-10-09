# Quality review — Historical Monitoring Lookback and Remediation Review

## Reviewer protocol

Review from the raw evidence toward the conclusion. First reproduce the independent population controls, then the eligibility and exclusion rules, then the derived results, and finally the narrative. Reading a polished conclusion first can anchor the review to the author’s preferred outcome. Preserve the reviewer’s independent expected result before comparing it with the displayed value. A disagreement is evidence to investigate; do not quietly change the expected result to match the implementation.

Use three classes of checks. Structural checks verify unique IDs, row widths, types, enums, resolved links and required fields. Arithmetic checks verify counts, rates, amounts, predicates, joins and conservation equations. Judgment checks ask whether the concept, data, alternative explanation, limitation and recommendation fit the decision question. A structural pass cannot repair a conceptual failure. A reproducible formula cannot turn an unrepresentative sample into a population estimate. A well-supported observation does not supply missing authority to act.

Record the exact scope of each check, the expected result, actual result, evidence and reviewer state. PASS means the stated check matched within its defined scope. FAIL means evidence contradicts the criterion. REVIEW_REQUIRED means a human judgment or unresolved interpretation remains. NOT_TESTED means the procedure was not performed. These states are not interchangeable. A test that could not run must never be marked pass because the template looks plausible. An unresolved dependency can coexist with correct arithmetic, so report both.

## Artifact and session acceptance

Reopen the actual files if the session can create them. Compare the report, workbook and dashboard against one authoritative case representation. Check all required sections and domain tables, all rows, nulls, currencies, decimals, dates, evidence IDs, findings, actions and QA states. Check that filtering changes the visible subset without rewriting the total-scope counts. Export a filtered CSV and compare record identities, not just the header. Confirm that special characters remain literal text and do not become spreadsheet formulas or executable markup.

Inspect the rendered pages for clipped values, lost continuation rows, unreadable columns and orphaned headings. A successful file save does not establish readable rendering. If visual inspection is unavailable, record that limitation. Do not claim testing in Microsoft Office or enterprise Copilot unless it actually occurred in the relevant environment. The supplied fixture checker proves particular arithmetic and table relationships; it does not establish that a language model consistently follows this method on new cases.

A completion statement must name its level. The fixture can be arithmetically complete while operational labels, original transactions, qualified review or human authorization are absent. A report can be copy-ready while no DOCX file was created. A historical desk review can be complete while a downstream referral is open. Preserve these distinctions in the final response. The release gate is not a request to invent acceptance; it is a test of whether the supplied evidence supports the requested completion claim.

## Complete adversarial and boundary test specifications

### Q01: Recover L30

**Isolated input change.** Supply RAW-30 with amount 30500 and the matching manifest identity.

**Required expected result.** Retrieved canonical count becomes 30; June becomes 5/5; known activity becomes 480000 USD. Review cannot jump from NOT_RETRIEVED to complete without analysis.

**Interpretation.** Recovery resolves retrieval only.

### Q02: Remove a duplicate copy

**Isolated input change.** Remove RAW-D1 from a newly supplied packet while preserving the earlier version.

**Required expected result.** New raw count is 33, duplicate count 2, canonical count 29 and known canonical activity remains 449500 USD.

**Interpretation.** Raw representation count and canonical scope are different.

### Q03: Duplicate amount conflict

**Isolated input change.** Change RAW-D1 amount from 2500 to 2600.

**Required expected result.** The duplicate identity can remain, but the value conflict blocks unqualified canonical selection for L02 until resolved.

**Interpretation.** Do not average conflicting values.

### Q04: July becomes in scope

**Isolated input change.** Accept an analytical scope proposal including July and provide independent July controls.

**Required expected result.** Rebuild the expected manifest and denominators; the two received July rows alone cannot define complete July coverage.

**Interpretation.** Expansion requires controls, not only found records.

### Q05: Summary retrieved for L30

**Isolated input change.** Supply only a summary without essential activity support.

**Required expected result.** Retrieval coverage becomes 30/30, but L30 moves at most to UNABLE_TO_ASSESS pending needed evidence.

**Interpretation.** Retrieved is not the same as reviewable.

### Q06: Resolve one unable unit

**Isolated input change.** Provide complete L25 support and finish a comparison finding no new information.

**Required expected result.** UNABLE count becomes 4; no-open-action count 7; desk comparisons 13; total expected remains 30.

**Interpretation.** The state change has a separate evidence packet.

### Q07: Resolve one pending unit with referral

**Isolated input change.** Finish L19 comparison and identify new information requiring case assessment.

**Required expected result.** PENDING becomes 5; REFERRED becomes 7; desk comparisons become 13; no-open-action remains 6.

**Interpretation.** Finishing desk work can increase open handoffs.

### Q08: Acknowledge a referral

**Isolated input change.** Receive an actual acknowledgment for L07 without a final decision.

**Required expected result.** The referral remains open; acknowledgment changes but disposition completion does not.

**Interpretation.** Receipt is not resolution.

### Q09: New evidence on a complete unit

**Isolated input change.** Receive credible additional information for L01 after its comparison.

**Required expected result.** Reopen L01 with a new state entry; preserve COMP-L01 and the earlier cutoff.

**Interpretation.** Prior completion is not silently deleted or retroactively rewritten.

### Q10: Independent manifest increases

**Isolated input change.** A new control identifies an additional May unit L33.

**Required expected result.** Expected count becomes 31; May expected count 6; missing units increase until retrieval resolves; recalculate every rate.

**Interpretation.** Do not hide a newly expected unit outside the denominator.

### Q11: Manifest shares the defect

**Isolated input change.** Learn that the control manifest used the same broken mapping as retrieval.

**Required expected result.** Completeness assurance is blocked pending an independent control; matching counts are insufficient.

**Interpretation.** A common source defect can survive perfect reconciliation.

### Q12: False historical closure inference

**Isolated input change.** An originally CLOSED record has not been re-reviewed.

**Required expected result.** Its current state remains PENDING_REVIEW or REREVIEW_REQUIRED as supported; it is not complete.

**Interpretation.** Historical status cannot answer the current question.

### Q13: Unknown amount treated as zero

**Isolated input change.** Replace L30 amount null with zero without source evidence.

**Required expected result.** QA fails; restore null and the unknown-amount limitation.

**Interpretation.** A total must not manufacture data availability.

### Q14: Unmatched raw identity

**Isolated input change.** Add a received row whose canonical key is uncertain.

**Required expected result.** Add an unresolved intake bucket and hold identity-dependent aggregation; do not force a match.

**Interpretation.** Complete intake accounting includes unresolved records.

### Q15: All received rows classified

**Isolated input change.** Confirm that all 34 received rows are assigned a bucket.

**Required expected result.** Only intake accounting is 100%; retrieval remains 29/30, desk comparison 12/30 and no-open-action 6/30.

**Interpretation.** Do not borrow the highest percentage for a broader completion claim.

### Q16: Human accepts a limitation

**Isolated input change.** Receive an actual authorized restricted acceptance concerning missing L30.

**Required expected result.** Preserve the missing unit and restricted claim; do not change the record to observed or reviewed.

**Interpretation.** Acceptance changes a decision state, not the underlying evidence.

### Q17: Scope end uncertain

**Isolated input change.** The corrected mapping date is unknown while July records exist.

**Required expected result.** EX-06 remains open and the boundary claim stays qualified; request version and continuity evidence.

**Interpretation.** No confirmed July issue does not prove the absence of exposure.

### Q18: Report deadline arrives

**Isolated input change.** A requested submission date occurs while 24 dependencies remain open.

**Required expected result.** Deliver accurate interim status with open units; do not convert pending states to completed ones.

**Interpretation.** A deadline changes delivery timing, not evidential completion.

## Reviewer challenge questions by analytical stage

**M01 — Write the defect hypothesis.** Independently reproduce this checkpoint: The fixture describes a mapping defect relevant to January through June. Its exact effect on L30 cannot be assessed because the record is absent. Then test the adverse branch: Do not label every in-scope unit affected merely because it falls in the period; preserve known affected, known unaffected and unassessable impact states. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M02 — Set an evidence-based historical boundary.** Independently reproduce this checkpoint: The analytical fixture includes all 30 manifest units from January through June. July rows are preserved as exclusions while continuity evidence is requested. Then test the adverse branch: If later evidence shows the same defect in July, propose expansion and reconcile a new denominator; do not quietly add July findings while retaining a 30-unit completion rate. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M03 — Freeze the independent manifest.** Independently reproduce this checkpoint: Five units per month produce 30 expected units. L30 remains in CanonicalUnits with missing source and amount. Then test the adverse branch: If the original manifest was generated using the same broken mapping, its agreement with retrieval cannot prove completeness; seek a genuinely different control. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M04 — Inventory all received representations.** Independently reproduce this checkpoint: The fixture has 34 raw rows. Twenty-nine are canonical,3 duplicate and 2 out of scope. Every raw row is accounted for exactlyonce. Then test the adverse branch: A raw row with conflicting identity is unresolved, not automatically a duplicate selected to make totals reconcile. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M05 — Resolve duplicates without losing history.** Independently reproduce this checkpoint: RAW-D1 maps to L02, RAW-D2 to L12 and RAW-D3 to L22. Their amounts match the canonical record in this fixture. Then test the adverse branch: If RAW-D1 changes the amount, flag a source conflict and state which version is authoritative for which cutoff before summing activity. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M06 — Reconcile counts by period.** Independently reproduce this checkpoint: January throughMay each retrieve 5/5. June retrieves 4/5. Total 29/30 remains incomplete even though all 34 received rows were classified. Then test the adverse branch: A surplus duplicate inMarch cannot offset a missing canonical unit inJune; distinct-grain counts must never be netted together. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M07 — Reconcile financial amounts at canonical grain.** Independently reproduce this checkpoint: Known activity for L01 through L29 is 449500 USD. L30 isnull. Duplicate amounts 37500 and July amounts 64000 are excluded from that canonical sum. Then test the adverse branch: Do not call 449500 the complete scoped activity amount, a loss, or illicit funds. It is only the known canonical amount in the supplied fixture. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M08 — Preserve original and current states.** Independently reproduce this checkpoint: Original CLOSED, ESCALATED and NOT_GENERATED states remain unchanged. Current review states determine lookback workload separately. Then test the adverse branch: A current referral cannot be backdated into the original decision record. Preserve the chronology and distinguish correction from historical fact. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M09 — Assess defect exposure per unit.** Independently reproduce this checkpoint: Twenty of 29 retrieved units have defect_affected=true,9 false. L30 impact isnull. These flags do not determine whether review is complete or whether reporting is required. Then test the adverse branch: Afalse impact flag means the defined defect predicate was not met on available evidence; it does not establish that the unit has no other risk. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M10 — Triage for fresh comparison.** Independently reproduce this checkpoint: L01–L06 have complete no-new-information comparisons;L07–L12 require case review;L13–L18 require re-review;L19–L24 are pending;L25–L29 areunable;L30 ismissing. Then test the adverse branch: If a completed unit receives new material evidence, reopen its current lookback state with a new transition; preserve the prior completion packet. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M11 — Perform a historical-versus-current comparison.** Independently reproduce this checkpoint: Six completed comparisons find no new information within their supplied scope. Six others identify new information and remain in an open referral route. Then test the adverse branch: No-new-information means the comparison found no material difference within the reviewed evidence; it is not an exoneration or a conclusion about all activity. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M12 — Route cases with explicit handoff tracking.** Independently reproduce this checkpoint: All six L07–L12 referrals remainHANDOFF_OPEN. No actual receiving acknowledgment or decision is supplied. Then test the adverse branch: Do not mark a referral closed because a report was created or a proposed action row names a recipient role. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M13 — Control scope expansion.** Independently reproduce this checkpoint: EX-01 addresses April–June; EX-02, missing L30; EX-03, referrals; EX-04, re-reviews; EX-05, missing support; and EX-06, July continuity. All are proposed or blocked. Then test the adverse branch: A new finding outside the original scope requires a visible denominator change and revised plan; it cannot be hidden as a narrative aside. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M14 — Measure progress using distinct completion levels.** Independently reproduce this checkpoint: The fixture has 34/34 raw accounting,29/30 retrieval,12/30 desk comparison,6/30 no-open-action,0/6 referral disposition and 0/1 whole-review approval. Then test the adverse branch: Do not choose the largest percentage as the headline completion rate. State exactly which work layer each numerator represents. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M15 — Define stopping evidence before closing.** Independently reproduce this checkpoint: Twenty-four units retain an open dependency, including six referrals and eighteen other review or evidence gaps. The lookback remains incomplete. Then test the adverse branch: A human may choose a restricted acceptance in a real process, but the record must state the limit and authority; this fixture contains no such acceptance. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

**M16 — Preserve a defensible completion package.** Independently reproduce this checkpoint: The case package contains all 30 expected units and all 34 received representations. Missing L30 stays visible rather than disappearing from the final report. Then test the adverse branch: Do not delete source records or prescribe a retention period from this suite; use the applicable supplied requirements and authorized records process. Record whether the original recommendation survives, narrows or changes. A reviewer should identify a specific contrary record or missing input, rather than responding only that the method appears reasonable.

## Required final QA record

| check_id | check_scope | expected | actual | status | reviewer | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| LB-Q01 | Raw intake accounting | 34=29 canonical+3 duplicate+2 out-of-scope | 34=29+3+2 | PASS | Fictional checker | SYN-202 |
| LB-Q02 | Expected scope accounting | 30=29 retrieved+1 missing | 30=29+1;L30 absent | PASS | Fictional checker | SYN-201;SYN-202 |
| LB-Q03 | Full retrieval coverage | All 30 expected units retrieved | 29/30 retrieved; June 4/5 | FAIL | Fictional checker | SYN-201;SYN-202 |
| LB-Q04 | Canonical amount conservation | Known amounts 449500; missing unit excluded explicitly | 449500 known; L30 amount null | PASS | Fictional checker | SYN-201;SYN-202 |
| LB-Q05 | Desk review completion | 6 no-new plus 6 referred =12 examined | 12/30 examined;6 handoffs still open | PASS | Fictional checker | SYN-203 |
| LB-Q06 | Whole-lookback completion | No material unresolved review retrieval or handoff | 24 units retain open dependency;6 desk-complete only | FAIL | Fictional checker | SYN-203 |
| LB-Q07 | No missing-to-negative conversion | L30 remains not retrieved and impact unknown | L30 source amount impact and new_information remain null | PASS | Fictional checker | SYN-201 |
| LB-Q08 | Filing or closure decision | Separate authorized human process required | NOT_RECORDED | NOT_TESTED | NOT_RECORDED | SYN-203 |

The populated QA rows above describe the fictional case. Reperform them for the current session and add the actual result, rather than copying the specimen PASS labels as evidence that a live review occurred. Preserve every failed or unperformed check in the final report. The independent fixture checker in file 10 must run from its own raw inputs without reading this repository or fetching external data.
