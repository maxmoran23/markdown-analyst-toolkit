# Transaction Monitoring Data Lineage: executable analytical procedure

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

## Step 01: Freeze two independent clocks

**Entry evidence.** Economic scope is one ET day; RUN0 and RUN1 have different ingestion cutoffs.

**Required operation.** Use event instants from 2026-09-01T04:00:00Z inclusive to 2026-09-02T04:00:00Z exclusive. RUN0 visibility ends at 04:00Z and RUN1 at 12:00Z on Sep 02.

**Reproduction target.** `X12 event 23:30Z Sep 01; ingestion 10:00Z Sep 02`.

**Exit record.** Populate SourceRows manifest and two run identities.

**Failure and interpretation boundary.** An event can be economically in scope while unavailable to the earlier run. Do not confuse missing-on-run with out-of-period.

## Step 02: Inventory all delivered rows

**Entry evidence.** The authored delivered package contains fifteen rows, including a known late record.

**Required operation.** Retain the entire delivery and tag each row by run availability. Declare that the review has hindsight about X12 while reproducing what RUN0 could ingest.

**Reproduction target.** `15 delivered = 14 USD + 1 EUR rows`.

**Exit record.** Populate SourceRows and LC01/LC02.

**Failure and interpretation boundary.** A source package assembled later is not proof that RUN0 had every row at its original cutoff.

## Step 03: Map direction and status exactly

**Entry evidence.** This source uses C and D direction codes and P, N, R statuses.

**Required operation.** Map C to CREDIT and D to DEBIT, P to POSTED, N to PENDING, R to REVERSAL_POSTED. Reject unmapped codes rather than treating them as default posted debit.

**Reproduction target.** `X09 N is pending; X11 R is a posted reversal`.

**Exit record.** Populate MAP03 and MAP05.

**Failure and interpretation boundary.** Mapping conventions are source-specific. Another source with the same letters may have different meanings and needs its own contract.

## Step 04: Parse amounts without coercion

**Entry evidence.** Original strings contain decimal amounts and one unreadable entry.

**Required operation.** Use decimal parsing, retain source text, reject negative magnitude and unrecognized separators, and keep X14 amount unknown. Sum only known values at each stage.

**Reproduction target.** `USD raw known credits 35200; debits 17500; one unknown amount`.

**Exit record.** Populate MAP04 and LC01.

**Failure and interpretation boundary.** The raw known sum includes copies, conflicts, pending and reversal rows; it is a source-control value, not economic activity.

## Step 05: Identify exact extraction duplicates

**Entry evidence.** X03 repeats X01 economic identity and payload with later ingestion metadata.

**Required operation.** Map X03 to existing canonical CL01. Preserve its duplicate terminal state but do not create another canonical row or another USD 6000 credit.

**Reproduction target.** `X01 + X03 source credits 12000; retained economic credit 6000`.

**Exit record.** Populate LIN-X03 and CL01.

**Failure and interpretation boundary.** Later extraction time alone does not mean a later authoritative source version.

## Step 06: Quarantine conflicting identity payloads

**Entry evidence.** X06 and X07 share account LC, TX05 and version 1 but disagree on amount.

**Required operation.** Retain both as CONFLICT and select neither. Keep LC known debit USD 1000 while blocking its complete assessment. Request authoritative version history.

**Reproduction target.** `Conflicting alternatives 2000 and 2200; selected amount null`.

**Exit record.** Populate EX01 and LIN-X06/LIN-X07.

**Failure and interpretation boundary.** Do not average values, choose maximum, prefer last row or call the two records separate credits.

## Step 07: Keep pending outside posted output

**Entry evidence.** X09 is a readable USD 7000 credit with pending status.

**Required operation.** Assign PENDING and retain its amount in raw controls but outside canonical posted rows and downstream posted-flow sums. Record LD as NO_POSTED_ACTIVITY for this snapshot.

**Reproduction target.** `Pending credit 7000; LD canonical credit 0`.

**Exit record.** Populate LIN-X09 and IMP-D.

**Failure and interpretation boundary.** If a later authoritative version posts the event, recompute the affected scope; do not pretend the earlier pending state was wrong.

## Step 08: Validate reversal linkage

**Entry evidence.** X11 is a posted debit reversal of LE TX08, matching amount and currency.

**Required operation.** Preserve X10 and X11 raw records. Under this authored illustrative external-flow convention, classify both REVERSAL_PAIR and exclude both from canonical scenario amounts.

**Reproduction target.** `3000 credit + 3000 reversal debit = 6000 posting gross; zero signed change`.

**Exit record.** Populate EX04 and LIN-X10/LIN-X11.

**Failure and interpretation boundary.** Other monitoring designs may retain or separately assess reversal activity. The exclusion must never become a claim that the postings did not happen.

## Step 09: Apply initial ingestion cutoff

**Entry evidence.** X12 is economically in period but ingested after RUN0 cutoff.

**Required operation.** Assign LATE_DEFERRED for RUN0; retain LF known debit USD 3600 and mark its assessment NOT_ASSESSABLE because the reviewer knows its initial feed is incomplete.

**Reproduction target.** `RUN0 LF credit known subtotal 0; complete source contains later credit 4000`.

**Exit record.** Populate LIN-X12, EX02 and IMP-F.

**Failure and interpretation boundary.** Do not label RUN0 LF a clean negative based on an incomplete feed, even though the late credit ultimately fails the minimum threshold.

## Step 10: Preserve separate currency populations

**Entry evidence.** X15 is a readable EUR 1000 posted credit.

**Required operation.** Include it in canonical output and EUR stage controls. Exclude it only from the illustrative USD rule, with a visible currency coverage state.

**Reproduction target.** `RUN0 canonical USD rows 6; EUR rows 1`.

**Exit record.** Populate CL07, LC04 and IMP-H.

**Failure and interpretation boundary.** Do not discard non-USD records at ingestion to make USD reconciliation easier, and do not invent an FX rate.

## Step 11: Conserve initial terminal states

**Entry evidence.** Every raw record has exactly one initial terminal disposition.

**Required operation.** Count canonical, duplicate, conflict, pending, reversal-pair, late-deferred and unparsed rows independently, then compare their sum to fifteen.

**Reproduction target.** `15 = 7 + 1 + 2 + 1 + 2 + 1 + 1`.

**Exit record.** Populate LineageLedger and LQ01.

**Failure and interpretation boundary.** The two conflicting rows represent one unresolved transaction identity; row conservation and identity counts answer different questions.

## Step 12: Produce the initial canonical layer

**Entry evidence.** Known, unique, posted and initially available legs survive the declared treatment rules.

**Required operation.** Retain CL01-CL07. Recalculate per-currency credits, debits and counts directly from these rows, keeping LC and LG blocked despite their known subtotals.

**Reproduction target.** `USD credits 11000; debits 14500; gross 25500; EUR credits 1000`.

**Exit record.** Populate CanonicalOutput and LC03/LC04.

**Failure and interpretation boundary.** Canonical completeness means only the stated filtering result here, not complete economic coverage of every account.

## Step 13: Reproduce the later run

**Entry evidence.** RUN1 cutoff permits X12 and changes no other source fact.

**Required operation.** Add the USD 4000 LF credit to a separate RUN1 canonical view; retain every initial row and unchanged exclusion. Recalculate affected LF amount and timing predicates.

**Reproduction target.** `USD credits 15000; debits 14500; gross 29500`.

**Exit record.** Populate LC05/LC06 and RunImpact.

**Failure and interpretation boundary.** A rerun that changes unaffected accounts, currency totals or prior IDs without an explained source delta fails change control.

## Step 14: Compare downstream consequences

**Entry evidence.** The illustrative downstream daily rule uses USD 5000 credits, .90 ratio and subsequent debit within 24 hours.

**Required operation.** LA and LB remain matches. LF now has 4000 credit, 3600 debit, .90 ratio and .5-hour sequence, but fails the minimum credit amount. LC and LG remain blocked.

**Reproduction target.** `LF NOT_ASSESSABLE -> NO_MATCH; two matches unchanged`.

**Exit record.** Populate IMP-A through IMP-H.

**Failure and interpretation boundary.** Improved completeness does not necessarily increase alerts. Do not optimize a repair acceptance criterion around obtaining a preferred alert count.

## Step 15: Specify repair evidence and dependencies

**Entry evidence.** TX05 conflict and X14 unreadable amount remain unresolved after RUN1.

**Required operation.** Request the authoritative TX05 version history and a corrected X14 source with source controls. Map every correction to canonical, account, window, raw result and report changes.

**Reproduction target.** `Open monetary defects remain two account scopes`.

**Exit record.** Populate ExceptionRegister EX01 and EX03.

**Failure and interpretation boundary.** A corrected file is not accepted until its source identity, controls, unchanged populations and dependent results are verified.

## Step 16: Deliver lineage acceptance with limits

**Entry evidence.** All source rows, mappings, exclusions, controls and rerun changes are populated.

**Required operation.** Provide a reproducible row-level trail and state which numerical propositions remain partial. Record independent acceptance as unrecorded and operational reprocessing as not performed.

**Reproduction target.** `Count conservation PASS; complete economic monetary total unresolved`.

**Exit record.** Populate ProcessQA and final report section.

**Failure and interpretation boundary.** A complete lineage map can explain an incomplete monitoring population; it cannot convert unresolved source values into complete assurance.
