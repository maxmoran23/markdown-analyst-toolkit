# Alert Adjudication Quality Review — quality review and acceptance

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
| Q01 | Packet and vote counts | 12 packets;24 votes | 12 / 24 | PASS | Q13 |
| Q02 | Original agreement | 9 of 12;75.0% | 9 / 12 =75.0% | PASS | Q13 |
| Q03 | Reviewer marginals | R1 6/4/2; R2 5/4/3 | 6/4/2;5/4/3 | PASS | Q13 |
| Q04 | Chance agreement | 52/144 =36.1111% | 52/144 | PASS | Q13 |
| Q05 | Cohen kappa | 14/23 =0.6086956522 | 14/23 | PASS | Q13 |
| Q06 | Consensus denominator | 4/12 ACCEPT;6/12 REWORK;2/12 INSUFFICIENT | 33.3%;50.0%;16.7% | PASS | Q14 |
| Q07 | Material defect cases | 6 of 10 assessable;6 of 12 selected | 60.0% assessable;50.0% selected | PASS | Q14;Q15 |
| Q08 | Defect counts | 7 defects:6 material,1 nonmaterial | 7 / 6 / 1 | PASS | Q14;Q15 |
| Q09 | Unknown treatment | C08/C12 not counted as passes | INSUFFICIENT retained | PASS | Q08;Q12;Q14 |
| Q10 | Closure authority | No executed correction or closure | NOT_RECORDED | NOT RECORDED | Q16 |

## Failure injection and dependency retest

Execute the twelve controlled counterexamples in file 04 against separate copies of the raw fixture. For each test, retain the changed input, expected result, actual result and affected outputs. The tests are part of the attachment workflow; they are not a substitute for checking a real case. Their expected results follow the defined fictional assumptions.

### Retest V01

Start with the base data, apply only: Replace both reviewers’ twelve votes with ACCEPT. Independently calculate: Observed agreement 100%; expected agreement 100%; kappa undefined. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V02

Start with the base data, apply only: Delete R2 vote for C12. Independently calculate: Complete pairs 11, original votes 23; pairwise agreement 8/11 under complete-pair analysis. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V03

Start with the base data, apply only: Use final consensus as both reviewers’ original votes. Independently calculate: Apparent agreement 100% would be a post-adjudication artifact. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V04

Start with the base data, apply only: Add a second material defect to C03. Independently calculate: Material defects 7,total defects 8; material affected cases remain 6. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V05

Start with the base data, apply only: Resolve C08 evidence and find its reasoning acceptable. Independently calculate: Consensus ACCEPT5,REWORK6,INSUFFICIENT1; assessable denominator 11; material case 6/11=54.5%. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V06

Start with the base data, apply only: Resolve C12 cutoff and find a demonstrated material defect. Independently calculate: Consensus REWORK7,ACCEPT4,INSUFFICIENT1; selected rework 7/12=58.3%; assessable 7/11=63.6%. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V07

Start with the base data, apply only: Remove nonmaterial punctuation defect D04. Independently calculate: Total defects 6; material defects 6; material affected cases 6; consensus unchanged. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V08

Start with the base data, apply only: Supply a genuine applicable internal policy requiring a specified nonfiling rationale field. Independently calculate: Evaluate actual field presence under that policy; no automatic universal regulatory claim. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V09

Start with the base data, apply only: C05 typo changes beneficiary identifier rather than punctuation. Independently calculate: Materiality must be reassessed; no automatic ACCEPT. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V10

Start with the base data, apply only: Select twelve easy cases instead of the deliberate calibration packets. Independently calculate: Observed quality rates may improve while population inference remains unsupported. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V11

Start with the base data, apply only: Owner reports all seven repairs complete without revised artifacts. Independently calculate: Executed repair and closureverification remain unsubstantiated. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V12

Start with the base data, apply only: A reviewer changes C07 to REWORK because source attribution was not attempted. Independently calculate: Under fixture facts, original bounded handling remains appropriate. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

## Row preservation inventory

| table | expected_rows | key | meaning |
| --- | --- | --- | --- |
| CasePackets | 12 | case_id | One completed case packet selected for calibration, not a random population sample. |
| ReviewVotes | 24 | vote_id | One original blind case-reviewer assessment;24 votes over 12 cases. |
| QualityCriteria | 8 | criterion_id | One supplied illustrative quality criterion; no implied universal legal mandate. |
| DefectRegister | 7 | defect_id | One defect-condition per case/criterion; multiple defects could affect one case. |
| Calibration | 12 | case_id | One paired case assessment; preserve original votes and later consensus. |
| Remediation | 7 | remediation_id | One proposed repair per demonstrated defect; no repair is executed in the fixture. |
| DecisionRecord | 4 | decision_id | One decision boundary separating quality judgment, population inference and business action. |
| ProcessQA | 10 | check_id | One reperformable quality metric or authorization check. |

## Table-by-table review operating cards

For every register, verify the complete row count, primary-key uniqueness, declared field types and source joins. Reperform numeric fields before rounding. Check the first, last and a decision-sensitive middle record against raw inputs, then reconcile the entire population; spot checks alone do not prove completeness. A successful file render does not establish analytical correctness. The cards below identify the distinct source, construction, interpretation and change rule for each population.

### CasePackets: 12 records

**Grain and source:** One completed case packet selected for calibration, not a random population sample. Use Twelve complete fictional packet summaries, Q01–Q12. The exact primary key is `case_id`.

**Construction and interpretation:** Retain one row per selected packet and distinguish packet facts from later consensus. This is deliberate calibration selection, not a random sample. ACCEPT/REWORK/INSUFFICIENT are quality outcomes, not underlying alert closure or filing decisions.

**Change-sensitive retest:** A later source can resolve assessability and change consensus. Preserve original packet version and availability chronology so historical review remains reproducible.

### ReviewVotes: 24 records

**Grain and source:** One original blind case-reviewer assessment;24 votes over 12 cases. Use Q13 original blind round 1 ratings. The exact primary key is `vote_id`.

**Construction and interpretation:** Keep 24 rows: each case appears once for R1 and once for R2. Do not overwrite the vote when discussion produces consensus. Two votes are not two cases. Pair by case ID and packet version before calculating agreement.

**Change-sensitive retest:** A missing vote reduces complete-pair count; a second round creates new records with an explicit round rather than a duplicate-key overwrite.

### QualityCriteria: 8 records

**Grain and source:** One supplied illustrative quality criterion; no implied universal legal mandate. Use Supplied illustrative policy CP-QA-1. The exact primary key is `criterion_id`.

**Construction and interpretation:** Keep eight criterion cards with material, assessability or nonmaterial boundaries. Apply the exact rule to the case condition before assigning a defect. The criterion source is internal illustrative policy, not a universal regulatory mandate. K06 specifically prevents unsupported legal-premise findings.

**Change-sensitive retest:** A policy change requires effective-date and historical applicability review. A reviewer’s preferred writing style does not automatically become a criterion.

### DefectRegister: 7 records

**Grain and source:** One defect-condition per case/criterion; multiple defects could affect one case. Use Packet facts, applicable criteria and adjudicated demonstrated errors. The exact primary key is `defect_id`.

**Construction and interpretation:** Keep seven defects across seven cases; six are material and one nonmaterial. Do not insert C08/C12 as demonstrated defects solely because they are unassessable. Case-level material rates count unique affected cases, while remediation counts defect rows. Severity does not substitute for materiality.

**Change-sensitive retest:** A second defect on an existing case changes defect count but may leave affected-case count unchanged. Trace each defect to its own closure test.

### Calibration: 12 records

**Grain and source:** One paired case assessment; preserve original votes and later consensus. Use Original paired votes and Q14 later consensus. The exact primary key is `case_id`.

**Construction and interpretation:** Keep twelve paired rows, original agreement flags and adjudication rationale. Consensus cannot replace the original vote history. Nine original pairs agree; C02/C06/C11 disagree. The reasoned consensus preserves unknowns where evidence is absent.

**Change-sensitive retest:** New evidence creates a new consensus version or round; it does not improve historical original agreement retrospectively.

### Remediation: 7 records

**Grain and source:** One proposed repair per demonstrated defect; no repair is executed in the fixture. Use Seven demonstrated defects and Q16 proposed repairs. The exact primary key is `remediation_id`.

**Construction and interpretation:** Create one targeted repair and closure test per defect. The fixture status is PROPOSED for every row. A corrected field must be checked in all affected outputs and any conclusion relying on it. Optional editorial correction remains separate from substantive rework.

**Change-sensitive retest:** Executed repair, retest and authorized closure need distinct evidence. An owner statement alone is not a verified closure artifact.

### DecisionRecord: 4 records

**Grain and source:** One decision boundary separating quality judgment, population inference and business action. Use Consensus, selection design and actual closure/filing authority. The exact primary key is `decision_id`.

**Construction and interpretation:** Record four decision boundaries: calibration result, unavailable population inference, unrecorded underlying business disposition and unrecorded repair closure. Quality consensus cannot determine suspicious activity or filing obligations. Deliberate selection cannot justify population extrapolation.

**Change-sensitive retest:** An actual later human decision can populate the relevant gate, but cannot be inferred from good agreement or a complete workbook.

### ProcessQA: 10 records

**Grain and source:** One reperformable quality metric or authorization check. Use Original vote arithmetic, consensus counts, defect grain and missingness. The exact primary key is `check_id`.

**Construction and interpretation:** Record ten checks, including 9/12 agreement,52/144 expected agreement and 14/23 kappa. Preserve two unassessable packets in denominator explanations. Six material cases are 50.0% of 12 selected and 60.0% of 10 assessable; neither is a population estimate.

**Change-sensitive retest:** Changing consensus requires recomputing rates, but original agreement stays unchanged unless original votes were actually corrected with documented provenance.
