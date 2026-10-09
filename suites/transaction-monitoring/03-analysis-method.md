# Transaction Monitoring Review: executable analytical procedure

## Precedence, three-valued reasoning and exact comparison

Apply a completeness gate before a numerical conclusion whenever the missing item can change that conclusion. TRUE means the predicate is established from the scoped evidence. FALSE means complete relevant evidence establishes the contrary. UNKNOWN means the predicate cannot be evaluated. Do not map UNKNOWN to FALSE for convenience. At a conjunction, a known false amount criterion may be reportable as a failed necessary condition, but the overall account can still remain NOT_ASSESSABLE if the unresolved source defect prevents the intended complete review. State both facts rather than claiming a complete negative.

Separate calculation state from review state. The source and numeric layers can establish a raw match; customer context may support an explanation; an authorized reviewer may later make a disposition. Each is stored in its own field with evidence and time. Rewriting a raw result after an explanation destroys reproducibility. Equally, a precise formula cannot establish a commercial purpose or an offense. Use the most specific supported wording: the records meet the illustrative predicates; the invoice supports this payment; the source defect blocks this account; authorization is absent.

## Mathematical conventions retained through every layer

Perform all threshold comparisons before rounding. Decimal monetary values are in row currency; ratios are dimensionless. A displayed 90.0% can represent a value below .90. Store enough precision to reproduce the branch and show the unrounded value in the acceptance record where the boundary is material. For elapsed time, compare seconds or exact instants and display hours only afterward. Exactly 24 hours and 24 hours plus one second are different under the authored inclusive endpoint.

Do not fill missing numeric values with zero. A known subtotal of zero means no known contributing amount in the specified subset; it does not prove the complete amount is zero when the population is incomplete. A null ratio can arise from a zero denominator, missing numerator, missing denominator or blocked temporal coverage, and the accompanying state must distinguish them. Do not cap ratios above one. Do not infer a loss from a debit, a unique monetary amount from gross movement or a funding path from a temporal ratio.

A set expansion requires two denominators: membership records and distinct economic records. Rolling windows, scenario overlap and customer-account aggregation can repeat the same leg. Keep stable IDs and calculate unions before unique movement or unique account counts. If two scenarios match the same USD 9500 debit, summing their matching amounts does not create USD 19000 of unique activity. Likewise, one source defect can affect several windows without becoming several defective source rows.

## Counterfactual and correction protocol

Use a fresh copy of the baseline for each independent sensitivity. State exactly which input or parameter changed, which quantities should change and which must remain invariant. A ratio-only counterfactual must keep the credit denominator fixed unless changing it is the purpose of the test. A time-only counterfactual must preserve identities and amounts. A source correction must retain the old value, the replacement evidence, effective time and run cutoff. Do not combine independent perturbations unless explicitly creating and labeling a compound stress case.

For an actual correction, compute a dependency closure: raw source identity, canonical result, exclusion state, account/currency sums, all affected window memberships, rule predicates, raw result, delivery or review proposal, findings and summary figures. Recheck previously negative as well as positive windows. An error can create a false hit, hide a hit or leave the match count unchanged while corrupting amounts. Match-count equality alone does not prove correct repair.

## Independent challenge and bounded handoff

The reviewer should be able to reproduce a material number from raw IDs without trusting the narrative. Give a concrete concern, concrete counterexplanation and discriminating missing evidence for each substantive inference. Ask whether a known ordinary mechanism—settlement, treasury movement, a documented invoice, reversal or delayed feed—explains the pattern. Test that mechanism against dates, parties, amounts and product behavior. Do not list generic alternatives without evaluating the evidence that would distinguish them.

A valid handoff includes exact inputs and formulas, complete tables, unresolved branches, change history, performed checks and unperformed checks. It does not need a fictitious approval to be useful. READY_FOR_HUMAN_REVIEW means the analytical package is internally consistent and its limitations are visible; it does not mean all accounts are assessable, every source is complete or any operational action is authorized.

Each numbered step retains its own entry evidence, operation, calculation target, exit record and interpretation boundary. Preserve contributing IDs and units once in the linked registers. A failed gate returns the affected rows to the earliest dependent step; keep blocked states visible. The numerical targets belong to the fictional baseline and must be independently reproduced for a new case.

## Step 01: Declare the economic unit

**Entry evidence.** Ten raw rows describe one-day USD account legs for A through D, not four complete customer relationships.

**Required operation.** Fix Sep 01, 2026 12:00 AM ET inclusive to Sep 02, 2026 12:00 AM ET exclusive, with event time controlling scope. Preserve this daily rule separately from credit-anchored diagnostics.

**Reproduction target.** `received rows = 10; distinct accounts = 4; currency set = {USD}`.

**Exit record.** Populate RawTransactions scope and immutable IDs.

**Failure and interpretation boundary.** Do not widen this daily extract to a complete rolling 24-hour look-forward interval or claim all related accounts were reviewed.

## Step 02: Partition raw receipts

**Entry evidence.** R09 repeats T01 at A with identical economic payload; R10 has an unknown amount.

**Required operation.** Retain R01-R08 as readable unique posted legs, mark R09 duplicate of R01, and mark R10 unparsed without changing its posting or scope evidence.

**Reproduction target.** `10 = 8 processed + 1 duplicate + 1 unparsed`.

**Exit record.** Populate Ten terminal decisions and eight canonical records.

**Failure and interpretation boundary.** A count balance does not establish monetary completeness. Excluding R10 from numeric sums does not exclude D from review coverage.

## Step 03: Verify canonical identity

**Entry evidence.** Transaction identifiers are paired with account identity and source version.

**Required operation.** Compare duplicate payload fields, including direction, amount, currency, event time and counterparty. Preserve extraction metadata differences without inventing another economic leg.

**Reproduction target.** `T01 at A appears twice in raw rows and once as L-T01`.

**Exit record.** Populate CanonicalLedger and raw-to-leg joins.

**Failure and interpretation boundary.** A changed amount under the same identity is a conflict, not an exact duplicate; do not choose first, latest or largest without authoritative version evidence.

## Step 04: Calculate gross account movement

**Entry evidence.** Canonical amounts are known and nonnegative; direction carries the sign.

**Required operation.** Group by account and currency, count canonical legs and separately sum credit and debit magnitude. Retain C own transfers in gross movement.

**Reproduction target.** `credits 18000; debits 18300; gross 36300; signed movement -300 USD`.

**Exit record.** Populate AccountFlows gross columns and CT-03/CT-04.

**Failure and interpretation boundary.** These are known totals only. Opening balances and the unreadable debit prevent an ending-balance or complete gross claim.

## Step 05: Evaluate ownership evidence

**Entry evidence.** SYN-004 establishes common ownership for C during the historical period.

**Required operation.** Exclude only T06 and T07 from TM-01 external-flow sums. Preserve each exclusion reason and the ownership locator. Other accounts remain externally classified as supplied.

**Reproduction target.** `own-transfer gross = 3000 + 3000 = 6000 USD`.

**Exit record.** Populate Eligibility rows EL-R06 and EL-R07.

**Failure and interpretation boundary.** A confirmed own-transfer exclusion does not clear C from other scenarios or justify excluding unrelated third-party legs.

## Step 06: Propagate source incompleteness

**Entry evidence.** T09 is a relevant posted D event with unknown debit amount.

**Required operation.** Keep T08 USD 1000 as known eligible debit, but set D account assessment to NOT_ASSESSABLE. Preserve null ratio and blocked eligibility.

**Reproduction target.** `D known debit = 1000; D complete debit = 1000 + unknown`.

**Exit record.** Populate AccountFlows D and SR-004.

**Failure and interpretation boundary.** Do not call D a clean negative because its known credit subtotal is zero; the complete ledger is unresolved.

## Step 07: Compute eligible ratios

**Entry evidence.** Own transfers are removed only after gross reconciliation.

**Required operation.** Calculate A 9500/10000 and B 4800/5000 using original numeric precision. Leave C and D ratios null because their eligible credit denominators are zero, with D additionally blocked.

**Reproduction target.** `A .95; B .96; C null; D null`.

**Exit record.** Populate AccountFlows out_in_ratio.

**Failure and interpretation boundary.** The portfolio known ratio 15300/15000 = 1.02 is not the account-level rule and must not create a portfolio alert.

## Step 08: Establish temporal sequence

**Entry evidence.** Events have explicit UTC instants and reliable daily coverage as supplied.

**Required operation.** For each complete eligible account, identify the first credit and the earliest debit strictly after it. A debit before the anchor does not satisfy timing; equal timestamps require a separate sequence convention.

**Reproduction target.** `A 2 hours; B 3 hours`.

**Exit record.** Populate ScenarioResults first_credit_to_debit_hours.

**Failure and interpretation boundary.** Sorting equal timestamps by transaction ID improves reproducibility only; it does not establish that funds arrived before departure.

## Step 09: Evaluate daily TM-01

**Entry evidence.** The illustrative daily credit minimum is USD 5000, ratio .90 and first subsequent debit within 24 elapsed hours.

**Required operation.** Apply completeness first, then confirmed all-own exclusion, then positive-credit and subsequent-debit gates, then the inclusive numeric predicates. Preserve the predicate that determines each result.

**Reproduction target.** `A MATCH; B MATCH; C EXCLUDED; D NOT_ASSESSABLE`.

**Exit record.** Populate Four daily ScenarioResults rows.

**Failure and interpretation boundary.** A raw result cannot be altered to fit a contextual explanation, and an explanation cannot substitute for a failed numeric gate.

## Step 10: Construct diagnostic rolling windows

**Entry evidence.** Three eligible known credit anchors exist: T01, T02 and T04.

**Required operation.** Create one closed interval from each anchor through anchor plus 24 elapsed hours. Include only same-account eligible known legs; preserve all membership IDs. Mark all three intervals BOUNDARY_INCOMPLETE because extraction ends earlier.

**Reproduction target.** `W-A-T01 10000/9500; W-A-T02 4000/9500; W-B-T04 5000/4800`.

**Exit record.** Populate WindowDiagnostics with observed memberships.

**Failure and interpretation boundary.** Do not promote an observed diagnostic ratio to a complete rolling rule result. The missing look-forward interval can change both numerator and denominator.

## Step 11: Control overlapping membership

**Entry evidence.** A T02 and T03 occur in both A diagnostic windows.

**Required operation.** Report seven membership entries separately from the five distinct observed eligible legs. Calculate portfolio movement from the union of legs, not a sum of window totals.

**Reproduction target.** `diagnostic membership gross 42800; unique observed gross 29300 USD`.

**Exit record.** Populate CT-07 and diagnostic narrative.

**Failure and interpretation boundary.** Overlapping monetary sums measure repeated window exposure, not unique activity, suspicious amount or customer loss.

## Step 12: Test ordinary explanations

**Entry evidence.** B has a matched USD 4800 invoice and independent payment reference.

**Required operation.** Check document amount, parties, date and actual T05 reference. Preserve the supported scope as T05 only, retain the raw match, and record absent human disposition.

**Reproduction target.** `B remains MATCH; explanation SUPPORTED_FOR_T05`.

**Exit record.** Populate ReviewLedger RV-B and TM-F02.

**Failure and interpretation boundary.** An invoice does not automatically prove genuineness, explain every other payment or authorize an account-level clearance.

## Step 13: Develop discriminating evidence requests

**Entry evidence.** A profile describes consulting receipts but supplies no P03 purpose document.

**Required operation.** State the pattern as temporal co-occurrence. Request an invoice or contract linked to T03 and counterparty role information, and identify opening-balance evidence if funding attribution matters.

**Reproduction target.** `T03 = USD 9500; A observed gross = USD 19500`.

**Exit record.** Populate RV-A next_evidence and TM-F01.

**Failure and interpretation boundary.** Do not label USD 9500 as criminal proceeds or traced funds. There is no supplied evidence of ultimate destination or offense.

## Step 14: Prioritize coverage repair

**Entry evidence.** D incompleteness can change any amount-dependent conclusion.

**Required operation.** Separate the confidence in the extract defect from any inference about D. Propose recovery of T09 amount plus source control totals and recomputation of all D measures.

**Reproduction target.** `HIGH severity concerns the coverage defect; HIGH confidence concerns its existence`.

**Exit record.** Populate RV-D and TM-F03.

**Failure and interpretation boundary.** A high-severity source issue is not high-confidence suspicion about the customer.

## Step 15: Reconcile review and rule populations

**Entry evidence.** Four accounts remain visible through all review layers.

**Required operation.** Report two raw matches, one supported explanation, one proposed further review, one own-transfer exclusion and one blocked account with their distinct denominators. Do not add these different-state measures as if mutually exclusive raw transactions.

**Reproduction target.** `match rate within assessed eligible accounts = 2/2 = 100.0%`.

**Exit record.** Populate Summary methods and report headings 1 and 5.

**Failure and interpretation boundary.** This deliberately tiny example cannot estimate an operational alert rate, precision, recall or detection effectiveness.

## Step 16: Freeze the human review package

**Entry evidence.** All intermediate tables and evidence keys are retained, with D and boundary limitations visible.

**Required operation.** Populate every report heading and every table; run arithmetic, joins, cross-format and negative controls. Keep all proposed actions unapproved until genuine disposition evidence is supplied.

**Reproduction target.** `READY_FOR_HUMAN_REVIEW can coexist with D NOT_ASSESSABLE`.

**Exit record.** Populate ProcessQA, report, workbook and optional dashboard.

**Failure and interpretation boundary.** Do not claim a complete four-account assessment or completed escalation merely because artifacts were successfully rendered.
