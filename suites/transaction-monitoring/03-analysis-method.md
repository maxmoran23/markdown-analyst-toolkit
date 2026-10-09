# Transaction monitoring: sequential method

## 1. Establish the question before running a rule

Separate an alert review from a scenario-design review. Alert review asks whether identified activity has a supported explanation or warrants further human investigation. Scenario-design review asks whether the rule, input mapping, and eligible population behave as intended. The same data may support both tasks, but a disposition of one alert does not validate the scenario and a successful scenario test does not establish suspicious activity.

Record the precise unit: transaction, account-window, customer-window, or connected group. Use the account-window unit in the worked example. If a customer has several accounts, first calculate each account and then aggregate using a documented identity bridge. Count each economic leg once within the selected measure. A customer-level transfer between two owned accounts can be excluded from external flow while remaining visible in account-level gross activity.

## 2. Build the canonical ledger

Parse the complete raw population and retain raw IDs. Normalize timestamps and direction. Reject impossible negative amounts under a nonnegative-amount schema, rather than flipping sign twice. Retain legitimate zero-value verification events separately from monetary totals. Resolve duplicates only using a documented identity key and inspect conflicting values. Freeze the canonical ledger and its reconciliation before computing scenarios.

For each account and currency compute credit count, debit count, credit total, debit total, and net change. Net change equals credits minus debits; it does not equal ending balance without a verified opening balance and all adjustments. Gross movement equals credits plus debits and counts both sides of a round trip. Do not describe gross movement as unique funds laundered or financial loss.

Create an eligibility ledger that identifies excluded own transfers, rejected/pending payments, out-of-period legs, reversals, and rows missing required fields. Keep known totals for incomplete accounts, but label them partial. A partially known account must not appear among clean negatives.

## 3. Define TM-01 without hidden defaults

The worked example uses an authored illustrative rapid-movement rule:

- Unit: one account and USD in the complete review window.
- Candidate: at least one eligible credit and a subsequent eligible debit; all required amounts and timestamps readable.
- Eligible credits sum to at least $5.00,000.00.
- Eligible debits divided by eligible credits are at least 0.90.
- The elapsed time from first eligible credit to first subsequent eligible debit is no more than 24 hours.
- Confirmed own-account transfers are excluded from both eligible numerator and denominator.
- A relevant unresolved source defect returns NOT_ASSESSABLE, not NO_MATCH.

These parameters illustrate a transparent specification. They are not filing thresholds, recommendations for deployment, or claims of statistical optimization. The timing test is deliberately a simple screen; it does not show that all debits were funded by those credits. Opening balances, credit/debit interleaving, and other credits can explain apparent pass-through.

Calculate `out_in_ratio = eligible_debit_total / eligible_credit_total` only for a positive denominator. Leave it null otherwise. A ratio greater than one is possible when preexisting funds finance debits; do not cap it at one. An empty denominator is not zero risk. Express the display as a percentage without changing the stored ratio.

## 4. Preserve ordering and attribution limits

Sort by event instant and deterministic transaction ID tie-breaker. A debit at exactly the same timestamp as a credit is contemporaneous, not proven subsequent, unless sequencing metadata establishes order. State the tie rule. A debit before the first credit cannot satisfy the timing test. Incomplete boundary data can make the first visible credit differ from the first actual credit.

Do not describe value as traced merely because amounts resemble each other. A strict tracing analysis would require a declared allocation method, balance constraints, fees, and ambiguity bounds. For a simple screen, write “debits followed credits within the observed window.” Identify flows that cannot be attributed to a particular receipt. Where running balances are available, test whether proposed allocations would require a negative balance.

When evaluating rolling windows, generate stable account-window identifiers and retain overlap membership. One transaction can legitimately participate in several rolling windows, but deduplicate it when computing portfolio movement. Report scenario matches as account-window counts and unique affected accounts separately. A daily window and a rolling 24-hour window do not have the same boundary behavior.

## 5. Add contextual measures only when the data supports them

Velocity is event count per elapsed unit, with the unit and eligible observation time stated. Counterparty concentration can be measured as largest counterparty amount divided by total relevant direction amount; resolve identity before aggregating. A new-beneficiary flag needs a complete lookback or must read “not observed in supplied lookback.” A dormant-to-active flag needs a defined inactivity period and complete activity coverage.

For expected-activity comparisons, compare like periods and like units. A weekly observation cannot be divided by an annual estimate without a justified seasonality assumption. Historical medians and quantiles need the actual observation count, zero-activity periods, exclusions, and window length. Do not infer anomalous behavior merely because a customer belongs to a small or poorly matched peer group.

If proposing a threshold change, show sensitivity across candidate thresholds and preserve the same population. Count matches, unique accounts, reviewed positives, explanations, and unreviewed observations. Precision requires adjudicated labels; recall requires knowledge of positives outside the alert set. An increased alert rate alone is neither improved detection nor degraded accuracy. Never tune on the worked example and claim deployment performance.

## 6. Review each match and each blocked account

For every match, inspect customer purpose, product mechanics, normal business cycles, invoices, treasury sweeps, settlement batching, loan funding, property transactions, gifts, and refunds as relevant. Test a benign explanation against amounts, dates, identities, and actual documents. A verbal assurance alone is a Reported explanation; supporting records may increase confidence, but do not erase the original trigger.

Write the strongest supported concern and the strongest supported counterexplanation. Specify the one missing record most likely to distinguish them. Assign review outcome independently from rule result: MATCH may become EXPLANATION_SUPPORTED, ESCALATE_FOR_REVIEW, or OPEN_QUESTION. EXCLUDED means excluded from this scenario, not outside all monitoring. NOT_ASSESSABLE means the rule cannot be applied reliably.

Inspect a negative control just below each threshold, a boundary case exactly on it, a known benign match, a missing-data case, a duplicate, and a confirmed own transfer. This checks intended behavior and guards against favorable conclusions created by parsing errors.

## 7. Produce the decision package

Report raw population, processed population, known amounts, scenario eligibility, matches, unique accounts, and human review states. Display separate coverage and outcome metrics. Document data repair as an action with scope and recomputation requirements. Retain calculation precision and show the formula used for every headline figure. Do not extrapolate from the four fictional accounts to an institution's customers.

The reviewer receives a proposed next step and its evidential basis. The package does not decide whether a filing, account restriction, relationship exit, or law-enforcement contact is appropriate. Any such decision needs the authorized process and its current criteria.
