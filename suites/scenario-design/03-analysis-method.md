# Transaction Monitoring Scenario Design: executable analytical procedure

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

## Step 01: State the bounded risk hypothesis

**Entry evidence.** The design targets observed external debits following aggregated eligible credits within a credit-anchored 24-hour interval.

**Required operation.** Describe the mechanism as potential rapid external movement. Explicitly exclude a claim of tracing, criminal purpose, complete relationship coverage or statistically optimal detection.

**Reproduction target.** `unit = account + currency + anchor event + rule version`.

**Exit record.** Populate RULE-SD-01-v1 hypothesis record.

**Failure and interpretation boundary.** Do not start with an alert volume target and infer a risk hypothesis after choosing the parameters.

## Step 02: Freeze the eligible source

**Entry evidence.** E01-E13 cover six fictional accounts and a complete 48-hour event interval, with one unknown amount.

**Required operation.** Keep all thirteen events in EventLedger. M ownership is confirmed own; O has an amount defect. Eligible anchor generation uses external posted credits only.

**Reproduction target.** `13 source events; 11 external events; 2 confirmed-own events`.

**Exit record.** Populate EventLedger and AccountCoverage.

**Failure and interpretation boundary.** Completeness of time coverage does not repair E13 amount. Event retention and assessability are different dimensions.

## Step 03: Define identity and ordering

**Entry evidence.** Every source event has a stable ID, account, currency and UTC instant.

**Required operation.** Use event IDs for joins and deterministic display order. Compare actual instants for the strict subsequent predicate; do not manufacture sequence for N same-time events.

**Reproduction target.** `E10 time = E11 time; strictly greater comparison is false`.

**Exit record.** Populate P07 and WN1.

**Failure and interpretation boundary.** An arbitrary lexical tie-breaker must not turn a simultaneous debit into a subsequent debit.

## Step 04: Choose credit anchors explicitly

**Entry evidence.** J has two eligible credits; K, L, N and O each have one; M has no external anchor.

**Required operation.** Create one window per eligible credit. Do not create debit-anchored or customer-level windows. Retain blocked windows rather than skipping an account after a parse defect.

**Reproduction target.** `2 + 1 + 1 + 1 + 1 = 6 windows`.

**Exit record.** Populate WJ1, WJ2, WK1, WL1, WN1 and WO1.

**Failure and interpretation boundary.** A missing window is a coverage defect when an eligible anchor exists; a blocked window remains in the window count.

## Step 05: Specify closed temporal membership

**Entry evidence.** Each window starts at its anchor and includes an event exactly 24 elapsed hours later.

**Required operation.** Apply anchor <= event <= anchor+24h to same-account, same-currency eligible events. Retain endpoint convention in the specification rather than relying on a system default.

**Reproduction target.** `E05 at exactly +24h is inside WK1`.

**Exit record.** Populate P04 and WindowResults membership lists.

**Failure and interpretation boundary.** The economic source interval is half-open, but these analytical windows are closed; those conventions serve different purposes.

## Step 06: Aggregate credits and debits

**Entry evidence.** Every member event retains its magnitude and direction.

**Required operation.** Sum known amounts only when all relevant amounts are available; WO1 debit_total remains null because E13 is unknown. Preserve account known subtotals separately.

**Reproduction target.** `WJ1 5000/4500; WJ2 2000/4500`.

**Exit record.** Populate WindowResults amounts and AccountCoverage known totals.

**Failure and interpretation boundary.** A null dependent window amount must not become zero because a language or spreadsheet aggregate ignores blanks.

## Step 07: Apply exact amount and ratio predicates

**Entry evidence.** P05 requires credits at least USD 5000 and P06 ratio at least .90.

**Required operation.** Compare the original decimal values before rounding. Store L ratio .899998 and return NO_MATCH even when percentage display would show 90.0%.

**Reproduction target.** `4499.99 / 5000 = .899998 < .90`.

**Exit record.** Populate WL1 and AT03.

**Failure and interpretation boundary.** Do not convert the display back to a decision input. Rounding before comparison changes the specification.

## Step 08: Handle zero and missing denominators

**Entry evidence.** The design distinguishes zero known credits from unknown credit amounts.

**Required operation.** No positive eligible credit produces no credit anchor; a hypothetical complete zero-credit window has no ratio and no match. A relevant unknown credit blocks the affected scope and must be resolved before anchor completeness is claimed.

**Reproduction target.** `undefined ratio is null, never zero or infinity`.

**Exit record.** Populate P01, P05 and P06 branching.

**Failure and interpretation boundary.** An absent anchor can be a valid exclusion or a data defect; the account coverage ledger distinguishes the reasons.

## Step 09: Apply strict subsequent timing

**Entry evidence.** There must be at least one eligible debit strictly after the anchor and inside the closed window.

**Required operation.** Choose the earliest such debit and calculate elapsed hours. Other contemporaneous debits may be members of the aggregate but cannot satisfy the ordering gate alone.

**Reproduction target.** `WN1 ratio .90 but first_debit_hours null => NO_MATCH`.

**Exit record.** Populate P07, WN1 and AT04.

**Failure and interpretation boundary.** This version deliberately permits same-time amounts in totals while requiring another subsequent debit; changing that design requires a new version and acceptance tests.

## Step 10: Resolve precedence deterministically

**Entry evidence.** Blocking completeness is evaluated before numeric match, while confirmed-own exclusion prevents external anchor generation.

**Required operation.** Return NOT_ASSESSABLE for O before interpreting a partial ratio. Evaluate J second anchor independently: it fails credit minimum even though ratio is 2.25.

**Reproduction target.** `WO1 blocked; WJ2 NO_MATCH on P05`.

**Exit record.** Populate PredicateSpec order and WindowResults.

**Failure and interpretation boundary.** A high ratio cannot override a failed amount floor or a missing-data gate.

## Step 11: Preserve raw results before delivery

**Entry evidence.** WJ1 and WK1 meet the rule; all other windows have explicit states.

**Required operation.** Record raw_result before deciding whether a review item would be delivered. Keep the full match population regardless of later grouping or explanations.

**Reproduction target.** `2 matching windows; 2 unique matching accounts`.

**Exit record.** Populate DeliveryDecisions.

**Failure and interpretation boundary.** A delivery count alone is not the number of raw matches and cannot validate the underlying rule.

## Step 12: Limit duplicate delivery grouping

**Entry evidence.** Only an identical event set for the same account, version and review run can share an analytical delivery group.

**Required operation.** No specimen windows have duplicate matching event sets, so G-J1 and G-K1 stay separate. A future identical rerun can reference the same group with a retained run ledger.

**Reproduction target.** `No grouping reduction in the base case`.

**Exit record.** Populate P08 and DeliveryDecisions group_id.

**Failure and interpretation boundary.** Do not suppress a new event merely because an account already had an alert. Cooldown policies are outside this illustrative grouping rule.

## Step 13: Evaluate data-repair routing

**Entry evidence.** O has a relevant unreadable debit, but no operational queue has been authorized.

**Required operation.** Set the proposed delivery state to DATA_REPAIR_QUEUE, name E13 and its missing amount, and leave human_approval NOT_RECORDED.

**Reproduction target.** `WO1 is one blocked window, not one false positive`.

**Exit record.** Populate DL-O1.

**Failure and interpretation boundary.** A queue label is a proposed workflow outcome, not evidence that a system ticket or external message was created.

## Step 14: Reconcile window expansion

**Entry evidence.** J events E02 and E03 are included in both J windows.

**Required operation.** Count thirteen memberships and eleven distinct external events. Count six source accounts including M, and five externally anchored accounts. Keep all denominators labeled.

**Reproduction target.** `13 memberships minus 2 repeated memberships = 11 unique events`.

**Exit record.** Populate AT07 and AccountCoverage.

**Failure and interpretation boundary.** Never sum window amounts and call them unique monetary movement without a union-based calculation.

## Step 15: Run acceptance before endorsement

**Entry evidence.** The fixture includes exact boundary, near-boundary, same-time, own-transfer and missing-data controls.

**Required operation.** Execute each expected result without editing predicates after seeing a failure. Record failed conditions and required specification changes. Treat specification success separately from platform implementation tests.

**Reproduction target.** `2 MATCH + 3 NO_MATCH + 1 NOT_ASSESSABLE = 6`.

**Exit record.** Populate AcceptanceTests and ProcessQA.

**Failure and interpretation boundary.** A written rule can be coherent even when no production system has implemented it; do not claim implementation validation.

## Step 16: Prepare the design decision

**Entry evidence.** No institution-specific approval, benchmark labels or deployment evidence is supplied.

**Required operation.** Give the reviewer the exact specification, source contract, complete test vectors, counterexamples, limitations and unresolved business decisions. Keep deployment and threshold changes unexecuted.

**Reproduction target.** `Operational human approval = NOT_RECORDED`.

**Exit record.** Populate SD-F03 and final report section.

**Failure and interpretation boundary.** Do not imply that a public reference or synthetic test suite is a substitute for the authorized local design and change process.
