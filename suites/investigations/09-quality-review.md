# Investigation Case Review — quality review and acceptance

## Reperformance protocol

Start from the raw inputs in file 10 or the supplied real-case source manifest. Recalculate without copying the conclusion or displayed metric. Compare the result to the populated tables only after completing the independent calculation. A second pass over the same formula is useful but does not establish organizational independence. Identify the reviewer, tools, source scope and checks actually performed. Leave checks not executed as NOT_TESTED.

For each failed check, record the precise condition, expected result, actual result, affected rows, effect on conclusions, repair and retest result. Do not erase the original failure when it is corrected. A failed total can invalidate a specific metric without invalidating every source statement; scope the consequence. Conversely, a correct total cannot rescue an unsupported identity or a missing human decision. Arithmetic, evidence and authorization are separate acceptance dimensions.

Check every material assertion against its supporting and conflicting evidence. Ensure that a quoted or paraphrased claim preserves the source’s date, scope and procedural status. Test whether the narrative becomes stronger than the underlying table when compressed. “Observed transfer” must not turn into “illicit payment”; “reviewer disagreement” must not turn into “investigator error” before adjudication; “unable to assess” must not become “pass.” Correct the narrative and all downstream views together.

## Artifact parity and completeness

Compare the report, workbook and dashboard to the same validated case version. Every finding identifier, severity, confidence, claim class, evidence link and proposed action must agree. Every domain table row must appear in the delivery set; a readable report may use vertical records, but it must not omit the long fields. If a dashboard filters a table, show filtered and total counts and make clear that a filtered export contains only the visible population. The report’s full-case conclusions remain tied to the unfiltered case.

Check the workbook as a workbook: sheet names, exact column order, numeric types, nulls, formats, formulas and row counts. Values that begin with spreadsheet formula characters remain literal source text. Identifiers and exact large integer strings remain text. A currency display format does not prove the currency of a source row. Reconcile any formula cache or calculation-engine limitation explicitly; an independently computed number does not prove that the workbook viewer recalculated it.

Check the report as a document: all eight headings, readable tables, complete evidence locators, page breaks, repeated headers and draft status. Check the dashboard offline with both themes, filters, empty results, CSV export and narrow layout. Do not claim native Microsoft Office, enterprise Copilot or actual print behavior unless tested in that environment. If visual inspection is unavailable, state that limitation precisely and supply the complete text fallback.

## Release and residual uncertainty

A package can be analytically review-ready while the business decision remains open. Document any unresolved uncertainty that does not prevent a bounded conclusion, why that conclusion is still supportable, and which stronger conclusions remain prohibited. The fixture’s ready state is never evidence of real human authorization. External filing, account action, communication or legal determination stays outside the generated package until separately approved through the applicable process.

Preserve a final checkpoint containing version, as-of date, input count, exclusions, canonical population, main reconciliations, open requests, findings, QA results and actual review status. A later reviewer should be able to identify exactly what changed. If new evidence arrives after release, create an addendum or new version with the affected conclusions; do not silently overwrite the record as though the information had always been available.

## Challenge set for the final reviewer

Challenge the population by selecting one included record, one excluded record and one unresolved record. Reconstruct why each is in its category and whether the rule is applied consistently. If the entire fixture has no unresolved raw rows, do not invent one; use a declared counterfactual to test the missingness rule. Confirm that the actual case and the counterfactual remain separated. A test scenario must not contaminate the final workbook’s case population.

Challenge the largest monetary amount and the most consequential inference separately. The largest amount may be routine and well supported; the consequential inference may concern a smaller identity or source-allocation error. Reperform both without assuming amount alone defines severity. Check that the finding’s proposed action addresses its actual defect. An identity problem is not repaired by correcting a currency display; an omitted source is not repaired by adding an extra disclaimer.

Challenge one favorable conclusion as carefully as an adverse conclusion. Determine whether the supporting evidence matches the same event, period, amount and party. Check whether the absence of contrary evidence reflects a completed bounded search or an unavailable source. A favorable conclusion can be appropriately limited without being undermined. The reviewer’s role is to test support, not to force every case into an adverse outcome.

Challenge every word implying completeness, certainty or authority. Terms such as all, none, proved, confirmed, compliant, approved, cleared, suspicious and loss require a precise source basis and scope. Replace only the unsupported overstatement, preserving valid observations. Do not weaken an exact arithmetic fact with vague hedging. If the ledger plainly shows a USD2,000.00 return, say so; the uncertainty may concern why it occurred or what decision follows.

Challenge the handoff by asking whether a new reviewer can reproduce the primary result using only the selected suite and supplied case inputs. Required methods cannot live only in an earlier chat or an unrelated suite. If a cross-suite analysis is useful, make its requested inputs and returned findings explicit rather than silently relying on another toolkit. This suite must remain complete for its stated decision question, including its exact schema and missing-data behavior.

## Defect repair order

Repair scope and population defects first because downstream calculations depend on them. Repair identity and source-linkage defects next because they affect joins and aggregation. Repair arithmetic and decision-rule application next. Repair narrative overstatement and output parity after the underlying data are stable. Finally repair presentation defects that do not affect meaning. This order avoids repeatedly polishing a paragraph whose underlying population is still changing.

For each repaired defect, retest the original failure and at least one adjacent dependency. If a return was linked to the wrong payment, retest both the corrected parent and the previous parent’s net amount. If a case moved from INSUFFICIENT to REWORK, retest assessable denominator, material-case count, consensus breakdown and any summary rate. If two graph nodes are merged under newly supplied ownership evidence, retest boundary inflow, boundary outflow, own-transfer flags and balance equations.

A successful retest closes the analytical defect only within its scope. It does not create human approval or external-action evidence. Record the repaired version and the result. If a repair cannot be completed, leave the defect open with the precise reason and its effect on review readiness. Do not convert an open material defect into a generic limitation in order to label the package final.

## Exact base-case acceptance checklist
| check_id | check | expected | actual | result | evidence_ids |
| --- | --- | --- | --- | --- | --- |
| Q01 | Raw-to-canonical count | 30 raw; 27 posted representations; 24 transfers | 30 / 27 / 24 | PASS | S01;S02;S11 |
| Q02 | Account A close | USD9000 | USD9000 | PASS | S01;S03 |
| Q03 | Account B close | USD1500 | USD1500 | PASS | S02;S03 |
| Q04 | Entity close | USD10500 | USD10500 | PASS | S01;S02;S03 |
| Q05 | External receipts excluding returns | USD42500 | USD42500 | PASS | S01;S08;S09 |
| Q06 | Supplier gross and linked net | USD40000 gross; USD36600 net | USD40000 / USD36600 | PASS | S01;S08 |
| Q07 | T02 invoice difference | USD1000 | USD1000 | PASS | S01;S05 |
| Q08 | T02 unreversed | USD9000 | USD9000 | PASS | S01;S08 |
| Q09 | Supported supplier gross | USD19800 of USD40000; 49.5% | USD19800 / USD40000 = 49.5% | PASS | S01;S06 |
| Q10 | Unsupported conclusion gate | No universal explanation or illicit-purpose assertion | Bounded unresolved subset retained | PASS | S01;S04;S06;S10 |
| Q11 | Purpose gates | T02 and T08 remain unresolved | HOLD_EVIDENCE | REVIEW REQUIRED | S01;S05;S10 |
| Q12 | Human disposition | No invented approval | NOT_RECORDED | NOT RECORDED | S12 |

## Failure injection and dependency retest

Execute the twelve controlled counterexamples in file 04 against separate copies of the raw fixture. For each test, retain the changed input, expected result, actual result and affected outputs. The tests are part of the attachment workflow; they are not a substitute for checking a real case. Their expected results follow the defined fictional assumptions.

### Retest V01

Start with the base data, apply only: Replace T03 return 2000 with 11000, keeping explicit T02 link. Independently calculate: Account A close 18000 and entity close 19500; T02 netzero; supplier net 27600. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V02

Start with the base data, apply only: Remove S09 ownership verification while keeping all posted account rows. Independently calculate: Account A/B balances still tie; entity consolidation is unverified and must be withheld. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V03

Start with the base data, apply only: Change INV-A face amount 10000 to 11000 but keep supplier R. Independently calculate: Amount difference becomeszero; beneficiary Q/R discrepancy remains. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V04

Start with the base data, apply only: Provide a supported Q/R beneficiary bridge, but no explanation of 1000 difference. Independently calculate: Identitydimension resolves; amount gap remains 1000. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V05

Start with the base data, apply only: Remove T03 explicit return reference while retaining incoming 2000 fromQ. Independently calculate: External incoming 2000 remains observed; linkedT02 return becomes unestablished and T02 linked net remains 11000. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V06

Start with the base data, apply only: Add a confirmed duplicate representation of T05. Independently calculate: Raw received 31; posted representations before dedupe 28; unique posted 27; canonical 24; monetary totals unchanged. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V07

Start with the base data, apply only: Turn pending USD2000 debit into a new posted external supplier transfer, with full evidence. Independently calculate: Canonical 25; Aclose 7000; entity close 8500; gross supplier 42000 before any linked return. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V08

Start with the base data, apply only: Remove opening balances for both accounts. Independently calculate: Net movement A4000,B500 remains calculable; closing equations cannot be independently anchored. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V09

Start with the base data, apply only: Add a second linked T02 return 10000 after the existing 2000. Independently calculate: Cumulative T02 returns 12000 exceed original 11000 by 1000. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V10

Start with the base data, apply only: Customer supplies only a new statement saying every payment was legitimate. Independently calculate: Posted totals and existing evidence gaps remain unchanged. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V11

Start with the base data, apply only: Omit T04 credit 8000 and T05 debit 7500 from the analytical chronology. Independently calculate: Net movement differs by 500, while grosscredits differ 8000 and grossdebits 7500. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V12

Start with the base data, apply only: Use T01 funding attribution for T02 under complete pre-debit balance. Independently calculate: Pre-debit pool 17000; source 12000; other 5000; debit 11000; bounds 6000–11000. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

## Row preservation inventory

| table | expected_rows | key | meaning |
| --- | --- | --- | --- |
| CaseTimeline | 24 | event_id | One canonical transfer touching A; same-entity mirror legs are represented once. |
| AccountBalances | 2 | account_id | One account-period balance equation. |
| ClaimTests | 6 | claim_id | One proposition, including favorable and contrary alternatives. |
| Contradictions | 4 | contradiction_id | One material contradiction or qualification and its exact decision effect. |
| EvidenceRequests | 5 | request_id | One decision-sensitive request or satisfied request outcome. |
| EvidenceProvenance | 12 | source_id | One source origin or explicitly unavailable supplied item. |
| DecisionRecord | 4 | decision_id | One distinct gate; completion is not equivalent to case closure. |
| ProcessQA | 12 | check_id | One performed fixture check or explicit unrecorded approval gate. |

## Table-by-table review operating cards

For every register, verify the complete row count, primary-key uniqueness, declared field types and source joins. Reperform numeric fields before rounding. Check the first, last and a decision-sensitive middle record against raw inputs, then reconcile the entire population; spot checks alone do not prove completeness. A successful file render does not establish analytical correctness. The cards below identify the distinct source, construction, interpretation and change rule for each population.

### CaseTimeline: 24 records

**Grain and source:** One canonical transfer touching A; same-entity mirror legs are represented once. Use S01 posted ledger, S08 return references and S09 verified A/B grouping. The exact primary key is `event_id`.

**Construction and interpretation:** Include 24 canonical transfers in exact time order; keep instructions, pending items and duplicate representations in the raw exclusion bridge. The amount is positive; direction comes from from_node/to_node. Account A balance changes once per transfer. B mirror postings do not create extra economic rows.

**Change-sensitive retest:** A return reference changes linked net calculations but does not delete either event or resolve purpose. A new posted item changes account and entity totals; a duplicate export changes raw count only.

**Intentional missing values:** `linked_return_of`. Verify each null retains the meaning declared in file 05 rather than becoming zero or a favorable inference.

### AccountBalances: 2 records

**Grain and source:** One account-period balance equation. Use S01/S02 full account postings and S03 supplied opening/closing controls. The exact primary key is `account_id`.

**Construction and interpretation:** Create one row for A and one for B. Sum credits/debits from each account’s own book, including both representations of internal movements at their proper account grain. Calculated close=opening+credits-debits; difference=calculated-supplied. Entity close is the sum of the two closes, not the sum of their credits.

**Change-sensitive retest:** A missing opening or supplied close becomes an explicit unavailable control, not a zero. A nonzero difference requires resolution before completeness is claimed.

### ClaimTests: 6 records

**Grain and source:** One proposition, including favorable and contrary alternatives. Use Source propositions in S01–S10 and the six printed claim questions. The exact primary key is `claim_id`.

**Construction and interpretation:** Create one row per falsifiable proposition. Preserve supportive, contradictory and missing evidence even when the final assessment is unresolved. CL02/CL03/CL05 are contradicted; CL01/CL04 unresolved; CL06 supports only timing. Confidence refers to the bounded proposition, not the whole subject.

**Change-sensitive retest:** A new invoice may resolve amount while leaving beneficiary or delivery unknown. Split a compound claim rather than forcing a single favorable label.

### Contradictions: 4 records

**Grain and source:** One material contradiction or qualification and its exact decision effect. Use Both source accounts and the linked ClaimTests row. The exact primary key is `contradiction_id`.

**Construction and interpretation:** Retain four material differences, including the corrected full-reversal claim and the favorable supported-activity counterexample. Resolved arithmetic and resolved scope remain visible; OPEN denotes an unresolved fact, not a pending formatting task.

**Change-sensitive retest:** If a source correction resolves a difference, preserve the old and new versions and explain the reason. Do not erase contrary evidence from the chronology.

### EvidenceRequests: 5 records

**Grain and source:** One decision-sensitive request or satisfied request outcome. Use Live claims, existing source limitations and discriminating information gaps. The exact primary key is `request_id`.

**Construction and interpretation:** Keep five scoped requests or satisfied outcomes. Request text must identify the event and exact missing linkage, avoiding accusations or unrestricted fishing. RQ01/RQ02/RQ05 cannot be marked executed. RQ03/RQ04 are satisfied for their limited source-retention/ownership purpose, not evidence of full case resolution.

**Change-sensitive retest:** A partial response closes only the satisfied component. Record readable-but-unlinked documents separately from genuinely corroborating evidence.

### EvidenceProvenance: 12 records

**Grain and source:** One source origin or explicitly unavailable supplied item. Use The twelve supplied source origins and availability states. The exact primary key is `source_id`.

**Construction and interpretation:** Keep inaccessible Contract-C in the manifest. Represent duplicate exports as the same origin, not independent confirmations. Observed describes source-visible content; Reported preserves the customer account or unavailable contract representation. A document’s existence does not establish its substantive assertions.

**Change-sensitive retest:** A readable replacement gets a version link. A new independent origin can improve corroboration only for the proposition it actually supports.

### DecisionRecord: 4 records

**Grain and source:** One distinct gate; completion is not equivalent to case closure. Use Population equations, unresolved purpose tests and actual review authority. The exact primary key is `decision_id`.

**Construction and interpretation:** Keep four gates with different scopes: data complete, T02 hold, T08 hold and human disposition absent. Completion of D01 does not close D02/D03. D04 requires actual supplied human authorization and cannot be inferred from generated artifacts.

**Change-sensitive retest:** If evidence resolves a purpose gate, record the triggering source and changed claim. Keep the human decision distinct from the assistant recommendation.

### ProcessQA: 12 records

**Grain and source:** One performed fixture check or explicit unrecorded approval gate. Use Independent arithmetic and evidence checks in file 09 and the embedded file 10 check. The exact primary key is `check_id`.

**Construction and interpretation:** Record twelve checks with exact expected and actual results. A passing numeric result does not erase a review-required purpose gate. Nine quantity/coverage checks, the overstatement boundary and remaining authority states must be read according to their individual scope.

**Change-sensitive retest:** If a source changes, rerun the affected checks and adjacent dependent totals. Preserve failed-before-repair history outside the current clean result view.
