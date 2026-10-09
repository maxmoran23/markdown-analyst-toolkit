# Network and Funds Flow Review — quality review and acceptance

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
| Q01 | Raw normalization | 28 raw to 24 edges | 24 | PASS | N01;N05 |
| Q02 | Nodes and unique keys | 9 nodes;24 unique edges | 9 / 24 | PASS | N01;N02 |
| Q03 | Gross edge value | USD74500 | USD74500 | PASS | N01 |
| Q04 | Entity external boundary | USD34000 in and USD34000 out | USD34000 / USD34000 | PASS | N01;N02 |
| Q05 | Complete-account balances | A1 USD500; A2 USD1000 | USD500 / USD1000 | PASS | N01;N02 |
| Q06 | P funding bound | USD3000–10000 | USD3000–10000 | PASS | N01;N02;N06 |
| Q07 | Cycle attribution bound | USD0–1000, subject to supplied visibility | USD0–1000 | PASS | N01;N04 |
| Q08 | Scenario allocations | Every row sums USD12000 | Four rows tie | PASS | N01;N02;N06 |
| Q09 | Unknown counterpart balances | No balance equations asserted for P/Q/R/C/D/E/F | Unassessed | PASS | N01;N04 |
| Q10 | Human decision | Not supplied | NOT_RECORDED | NOT RECORDED | N06 |

## Failure injection and dependency retest

Execute the twelve controlled counterexamples in file 04 against separate copies of the raw fixture. For each test, retain the changed input, expected result, actual result and affected outputs. The tests are part of the attachment workflow; they are not a substitute for checking a real case. Their expected results follow the defined fictional assumptions.

### Retest V01

Start with the base data, apply only: Remove A1 opening balance 1000 without replacing it. Independently calculate: E03 attribution bounds unavailable; visible edge amounts unchanged. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V02

Start with the base data, apply only: Add an independently observed pre-E03 outside credit 5000. Independently calculate: P lower becomes 0 and upper 10000; target debit remains 12000. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V03

Start with the base data, apply only: Change E03 debit 12000 to 20000 with same 19000 available pool. Independently calculate: Nonnegative pool feasibility fails by 1000. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V04

Start with the base data, apply only: Assume verified identity groups C into Entity-A, with adequate complete-account evidence newly supplied. Independently calculate: Boundary classification changes for everyC edge; currentEntity-A equation cannot simply be reused. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V05

Start with the base data, apply only: Reverse the temporal order of E10 and E11 only. Independently calculate: Static cycle remains; E09-E10-E11 is no longer time-respecting. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V06

Start with the base data, apply only: Double every amount and supplied A1/A2 balance. Independently calculate: Gross legs 149000; entity in/out 68000 each; P bound 6000–20000; cycle capacity 2000. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V07

Start with the base data, apply only: Add a raw duplicate of E03 with identical executionreference. Independently calculate: Raw count 29; canonical edges 24; gross legs 74500 unchanged. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V08

Start with the base data, apply only: Change E11 value 1000 to 2500 with all else unchanged. Independently calculate: Cyclecapacity becomes 1500, the minimum of 2000/1500/2500; A1 closing rises 1500 before source close update. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V09

Start with the base data, apply only: Treat E11 as a refund of E09 without source linkage. Independently calculate: No legitimate base case change permitted. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V10

Start with the base data, apply only: Set all pre-E03 P,Q andopening amounts tozero with debit 12000. Independently calculate: Funding pool infeasible; no attributionbound. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V11

Start with the base data, apply only: Combine the individual P/Q/opening lower endpoints 3000/1000/0. Independently calculate: Sum 4000, not 12000; vector infeasible. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

### Retest V12

Start with the base data, apply only: Use pro-rata amounts without cent residual check. Independently calculate: Exact values P6315.789473...,Q5052.631578...,opening 631.578947...; displayed cents tie 12000 in this fixture. Then inspect whether the finding, metric, narrative and decision gate changed consistently. The test passes only when the correct change occurs and unaffected source facts remain unchanged. Record any unavailable capability as NOT_TESTED; do not infer successful execution from reading this expected answer.

## Row preservation inventory

| table | expected_rows | key | meaning |
| --- | --- | --- | --- |
| Nodes | 9 | node_id | One distinct supplied account/counterparty node; nine total. |
| EconomicEdges | 24 | edge_id | One posted economic transfer; duplicate representations and nonexecuted instructions excluded. |
| BalanceChecks | 3 | balance_id | One valid equation for a complete supplied perimeter. |
| PatternTests | 6 | pattern_id | One defined graph pattern with an explicitly named amount and count. |
| AllocationBounds | 4 | allocation_id | One marginal or grouped attribution bound under explicitly stated balance constraints. |
| AttributionScenarios | 4 | scenario_id | One feasible assumed allocation vector; alternatives do not describe simultaneous facts. |
| DecisionRecord | 5 | decision_id | One claim boundary or human gate. |
| ProcessQA | 10 | check_id | One analytical check, distinct from legal or operational validation. |

## Table-by-table review operating cards

For every register, verify the complete row count, primary-key uniqueness, declared field types and source joins. Reperform numeric fields before rounding. Check the first, last and a decision-sensitive middle record against raw inputs, then reconcile the entire population; spot checks alone do not prove completeness. A successful file render does not establish analytical correctness. The cards below identify the distinct source, construction, interpretation and change rule for each population.

### Nodes: 9 records

**Grain and source:** One distinct supplied account/counterparty node; nine total. Use N02 account identity/balance record and immediate counterparties in N01/N04. The exact primary key is `node_id`.

**Construction and interpretation:** Retain nine nodes, including separate A1/A2 accounts linked to verified Entity-A. Do not promote recorded counterparty IDs to beneficial-owner facts. Opening balances are known only for A1/A2. Null openings elsewhere mean missing coverage, not zero funds.

**Change-sensitive retest:** A new identity bridge changes grouping and requires boundary recalculation. It does not justify rewriting the original source label or assuming historical applicability.

**Intentional missing values:** `opening_usd`. Verify each null retains the meaning declared in file 05 rather than becoming zero or a favorable inference.

### EconomicEdges: 24 records

**Grain and source:** One posted economic transfer; duplicate representations and nonexecuted instructions excluded. Use N01 canonical ledger, N03 return links, N04 onward extracts and N08 order. The exact primary key is `edge_id`.

**Construction and interpretation:** Retain 24 executed transfers with positive amount and exact direction. Exclude the four identified noncanonical raw representations with a crosswalk. Own-transfer flags are true only for E04/E16; return_of is populated only for E08/E21. Those classifications have different aggregation consequences.

**Change-sensitive retest:** A new posted transfer changes graph and balances. A duplicate representation changes raw inventory only. A revised return link changes net interpretation without removing the gross edge.

**Intentional missing values:** `return_of`. Verify each null retains the meaning declared in file 05 rather than becoming zero or a favorable inference.

### BalanceChecks: 3 records

**Grain and source:** One valid equation for a complete supplied perimeter. Use Complete review-account postings plus supplied opening and closing controls. The exact primary key is `balance_id`.

**Construction and interpretation:** Create A1, A2 and consolidated Entity-A equations; do not add equations for seven partial-visibility nodes. A1=500; A2=1000; entity=1500. Internal E04/E16 amounts cancel in the entity boundary while remaining in account equations.

**Change-sensitive retest:** A negative balance under a no-overdraft attribution assumption triggers a model feasibility review. Unknown external balances do not automatically fail this table.

### PatternTests: 6 records

**Grain and source:** One defined graph pattern with an explicitly named amount and count. Use Precisely declared edge sets and node membership. The exact primary key is `pattern_id`.

**Construction and interpretation:** Preserve six different pattern measures with their own amount/count interpretation. Do not combine them into a generic suspicious-flow total. P01 count is distinct source nodes; P02 count is boundary transfer legs; P03 count is cycle edges. Metric labels must retain those different units.

**Change-sensitive retest:** A new edge can change degree, time-respecting paths and boundary totals differently. Recompute exact memberships rather than incrementing every counter.

### AllocationBounds: 4 records

**Grain and source:** One marginal or grouped attribution bound under explicitly stated balance constraints. Use Complete pre-E03 funding pool and GP-1 fungible nonnegative balance assumptions. The exact primary key is `allocation_id`.

**Construction and interpretation:** Compute four marginal/grouped attribution intervals. Check total available 19000 can fund debit 12000 before applying endpoint formulas. Lower=max(0,D-O); upper=min(S,D). Grouped P+Q interval is 11000–12000 and cannot be obtained by adding individual minima.

**Change-sensitive retest:** Missing opening, unseen prior debit or permitted overdraft can invalidate the simple bound. Preserve descriptive graph results while withholding an unsupported attribution interval.

### AttributionScenarios: 4 records

**Grain and source:** One feasible assumed allocation vector; alternatives do not describe simultaneous facts. Use The same pool used by AllocationBounds and four declared assumptions. The exact primary key is `scenario_id`.

**Construction and interpretation:** Create four feasible allocation vectors, each summing 12000 and respecting source capacities. Keep every row ILLUSTRATIVE_ONLY. Proportional allocation rounds P and opening to cents and assigns the remaining cent-accurate residual to Q. FIFO is opening-first then ordered receipts.

**Change-sensitive retest:** A convention change affects the point vector, not the observed evidence. The interval remains the main supported conclusion unless actual linkage evidence narrows it.

### DecisionRecord: 5 records

**Grain and source:** One claim boundary or human gate. Use Identity evidence, graph facts, attribution assumptions and actual authority. The exact primary key is `decision_id`.

**Construction and interpretation:** Record five explicit inference boundaries: grouping supported, full P attribution unresolved, illicit-cycle inference prohibited, unique-capital label prohibited and no human decision. A prohibited inference is a methodological boundary, not a finding that the opposite proposition is true.

**Change-sensitive retest:** If new evidence narrows attribution or supports purpose, record a new bounded claim. Do not infer wrongdoing from the fact that the prior claim was unresolved.

### ProcessQA: 10 records

**Grain and source:** One analytical check, distinct from legal or operational validation. Use Counts, graph sums, balance equations, allocation math and authority boundary. The exact primary key is `check_id`.

**Construction and interpretation:** Keep ten checks and their exact scope. Test all scenario totals and both attribution endpoints, not only the displayed rounded metric. A structural PASS verifies the stated fixture invariant; it does not validate customer identity, complete external visibility or legal conclusions.

**Change-sensitive retest:** When an edge changes, rerun raw normalization, memberships, balances and affected path/allocation tests before updating report cards.
