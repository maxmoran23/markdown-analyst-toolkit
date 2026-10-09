# Transaction Monitoring Review: complete fictional case and alternate controls

All records are fictional. The base exercise is the original four-account daily screen, now with all intermediate registers populated. Event scope is Sep 01, 2026 12:00 AM ET through Sep 02, 2026 12:00 AM ET exclusive. USD amounts remain in USD. The source asserts that the ten supplied rows are the complete delivered extract for that period, but R10 amount cannot be recovered. This is not a claim of complete relationship history or external onward-flow coverage.

SYN-001 is the ten-row RawTransactions register below. R09 repeats the exact same T01 account leg as R01; it is not a second credit. SYN-002 is A's fictional historical profile: small consulting receipts and ordinary supplier payments, with no supplied invoice, contract, opening balance or P03 explanation. This profile is Reported expected activity. SYN-003 is fictional invoice INV-B-01 for USD 4800 naming P05 and matched to T05, plus an independent payment reference confirming the invoice identifier. It supports that payment's proposed ordinary-business explanation only. SYN-004 confirms that C-OWN-1 and C-OWN-2 share the same customer ownership as C during the review period. SYN-005 confirms T09 is posted and in period but amount extraction failed. SYN-006 is the authored diagnostic convention: credit-anchored closed 24-hour intervals, with source coverage ending at the stated daily extract boundary.

Received ten equals eight readable canonical legs plus one duplicate and one unparsed amount. Credits total 6000 + 4000 + 5000 + 3000 = USD 18000. Known debits total 9500 + 4800 + 3000 + 1000 = USD 18300. Known gross is USD 36300 and known signed movement is -USD 300. These are partial monetary values because T09 is unknown. C own-transfer gross is USD 6000; eligible known credits are USD 15000 and eligible known debits USD 15300. The resulting cross-account ratio 1.02 is not TM-01's account-level rule.

A has USD 10000 credits, USD 9500 debits, .95 ratio and two-hour sequence; B has USD 5000 credits, USD 4800 debits, .96 ratio and three-hour sequence. Both match daily TM-01. C is excluded only from the external-flow screen with its gross records retained. D has USD 1000 known debit plus unknown T09 and remains not assessable. A's pattern needs purpose evidence; B's invoice-supported explanation leaves its raw match unchanged; D needs source repair. No human disposition is supplied.

The diagnostic windows have observed membership sets T01/T02/T03, T02/T03 and T04/T05. Their known gross values are USD 19500, USD 13500 and USD 9800: overlapping sum USD 42800. The union of five legs has unique known gross USD 29300. Seven memberships exceed five unique legs because T02 and T03 repeat. Every diagnostic endpoint falls after extraction ends, so all three coverage states remain BOUNDARY_INCOMPLETE. These windows are not new complete rolling matches and do not replace the four daily account outcomes.

## Complete populated source and expected result registers

All rows below belong to the baseline. They are printed in full so the assistant can reproduce the case without importing any repository file. The later alternate controls are independent perturbations and must not be added to these baseline counts or monetary totals.

### RawTransactions

Grain: one immutable raw receipt row, including extraction duplicates and unparsed amounts.

| raw_row_id | transaction_id | account_id | event_utc | direction | amount_text | currency | counterparty_id | posting_state | ownership_state | terminal_bucket | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | T01 | A | 2026-09-01T13:00:00Z | CREDIT | 6000.00 | USD | P01 | POSTED | CONFIRMED_EXTERNAL | PROCESSED | SYN-001 |
| R02 | T02 | A | 2026-09-01T14:00:00Z | CREDIT | 4000.00 | USD | P02 | POSTED | CONFIRMED_EXTERNAL | PROCESSED | SYN-001 |
| R03 | T03 | A | 2026-09-01T15:00:00Z | DEBIT | 9500.00 | USD | P03 | POSTED | CONFIRMED_EXTERNAL | PROCESSED | SYN-001 |
| R04 | T04 | B | 2026-09-01T13:00:00Z | CREDIT | 5000.00 | USD | P04 | POSTED | CONFIRMED_EXTERNAL | PROCESSED | SYN-001 |
| R05 | T05 | B | 2026-09-01T16:00:00Z | DEBIT | 4800.00 | USD | P05 | POSTED | CONFIRMED_EXTERNAL | PROCESSED | SYN-001 |
| R06 | T06 | C | 2026-09-01T13:00:00Z | CREDIT | 3000.00 | USD | C-OWN-1 | POSTED | CONFIRMED_OWN | PROCESSED | SYN-001;SYN-004 |
| R07 | T07 | C | 2026-09-01T14:00:00Z | DEBIT | 3000.00 | USD | C-OWN-2 | POSTED | CONFIRMED_OWN | PROCESSED | SYN-001;SYN-004 |
| R08 | T08 | D | 2026-09-01T17:00:00Z | DEBIT | 1000.00 | USD | P06 | POSTED | CONFIRMED_EXTERNAL | PROCESSED | SYN-001 |
| R09 | T01 | A | 2026-09-01T13:00:00Z | CREDIT | 6000.00 | USD | P01 | POSTED | CONFIRMED_EXTERNAL | DUPLICATE | SYN-001 |
| R10 | T09 | D | 2026-09-01T18:00:00Z | DEBIT | unreadable | USD | P07 | POSTED | CONFIRMED_EXTERNAL | UNPARSED | SYN-001;SYN-005 |

### CanonicalLedger

Grain: one readable unique posted economic account leg.

| leg_id | raw_row_id | transaction_id | account_id | event_utc | direction | amount | currency | counterparty_id | ownership_state | scenario_eligible | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L-T01 | R01 | T01 | A | 2026-09-01T13:00:00Z | CREDIT | 6000.0 | USD | P01 | CONFIRMED_EXTERNAL | true | SYN-001 |
| L-T02 | R02 | T02 | A | 2026-09-01T14:00:00Z | CREDIT | 4000.0 | USD | P02 | CONFIRMED_EXTERNAL | true | SYN-001 |
| L-T03 | R03 | T03 | A | 2026-09-01T15:00:00Z | DEBIT | 9500.0 | USD | P03 | CONFIRMED_EXTERNAL | true | SYN-001 |
| L-T04 | R04 | T04 | B | 2026-09-01T13:00:00Z | CREDIT | 5000.0 | USD | P04 | CONFIRMED_EXTERNAL | true | SYN-001 |
| L-T05 | R05 | T05 | B | 2026-09-01T16:00:00Z | DEBIT | 4800.0 | USD | P05 | CONFIRMED_EXTERNAL | true | SYN-001 |
| L-T06 | R06 | T06 | C | 2026-09-01T13:00:00Z | CREDIT | 3000.0 | USD | C-OWN-1 | CONFIRMED_OWN | false | SYN-001;SYN-004 |
| L-T07 | R07 | T07 | C | 2026-09-01T14:00:00Z | DEBIT | 3000.0 | USD | C-OWN-2 | CONFIRMED_OWN | false | SYN-001;SYN-004 |
| L-T08 | R08 | T08 | D | 2026-09-01T17:00:00Z | DEBIT | 1000.0 | USD | P06 | CONFIRMED_EXTERNAL | true | SYN-001 |

### Eligibility

Grain: one raw-row decision for the declared daily scenario.

| eligibility_id | raw_row_id | leg_id | account_id | scenario_id | eligibility_state | reason | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EL-R01 | R01 | L-T01 | A | TM-01 | ELIGIBLE_KNOWN | Known external posted leg; account-level completeness checked separately | SYN-001 |
| EL-R02 | R02 | L-T02 | A | TM-01 | ELIGIBLE_KNOWN | Known external posted leg; account-level completeness checked separately | SYN-001 |
| EL-R03 | R03 | L-T03 | A | TM-01 | ELIGIBLE_KNOWN | Known external posted leg; account-level completeness checked separately | SYN-001 |
| EL-R04 | R04 | L-T04 | B | TM-01 | ELIGIBLE_KNOWN | Known external posted leg; account-level completeness checked separately | SYN-001 |
| EL-R05 | R05 | L-T05 | B | TM-01 | ELIGIBLE_KNOWN | Known external posted leg; account-level completeness checked separately | SYN-001 |
| EL-R06 | R06 | L-T06 | C | TM-01 | EXCLUDED_OWN | SYN-004 confirms common customer ownership during period | SYN-001;SYN-004 |
| EL-R07 | R07 | L-T07 | C | TM-01 | EXCLUDED_OWN | SYN-004 confirms common customer ownership during period | SYN-001;SYN-004 |
| EL-R08 | R08 | L-T08 | D | TM-01 | ELIGIBLE_KNOWN | Known external posted leg; account-level completeness checked separately | SYN-001 |
| EL-R09 | R09 | L-T01 | A | TM-01 | DUPLICATE | Exact second extraction of R01; not another account leg | SYN-001 |
| EL-R10 | R10 | null | D | TM-01 | BLOCKED | Posted in-scope amount unreadable; blocks D completeness | SYN-001;SYN-005 |

### AccountFlows

Grain: one account and currency within the fixed daily event period.

| account_id | currency | processed_tx_count | credit_total | debit_total | eligible_credit_total | eligible_debit_total | out_in_ratio | population_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | USD | 3 | 10000 | 9500 | 10000 | 9500 | 0.95 | COMPLETE |
| B | USD | 2 | 5000 | 4800 | 5000 | 4800 | 0.96 | COMPLETE |
| C | USD | 2 | 3000 | 3000 | 0 | 0 | null | OWN_TRANSFER_EXCLUDED |
| D | USD | 1 | 0 | 1000 | 0 | 1000 | null | UNPARSED_AMOUNT |

### WindowDiagnostics

Grain: one eligible credit anchor and its observed closed 24-hour interval.

| window_id | account_id | anchor_leg_id | start_utc | end_utc | observed_leg_ids | known_credit_total | known_debit_total | known_ratio | first_debit_hours | coverage_state | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W-A-T01 | A | L-T01 | 2026-09-01T13:00:00Z | 2026-09-02T13:00:00Z | L-T01;L-T02;L-T03 | 10000 | 9500 | 0.95 | 2 | BOUNDARY_INCOMPLETE | SYN-001;SYN-006 |
| W-A-T02 | A | L-T02 | 2026-09-01T14:00:00Z | 2026-09-02T14:00:00Z | L-T02;L-T03 | 4000 | 9500 | 2.375 | 1 | BOUNDARY_INCOMPLETE | SYN-001;SYN-006 |
| W-B-T04 | B | L-T04 | 2026-09-01T13:00:00Z | 2026-09-02T13:00:00Z | L-T04;L-T05 | 5000 | 4800 | 0.96 | 3 | BOUNDARY_INCOMPLETE | SYN-001;SYN-006 |

### ScenarioResults

Grain: one account, daily window and scenario specification.

| scenario_result_id | account_id | scenario_id | eligible | rule_result | first_credit_to_debit_hours | review_outcome | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SR-001 | A | TM-01 | true | MATCH | 2 | ESCALATE_FOR_REVIEW | SYN-001;SYN-002 |
| SR-002 | B | TM-01 | true | MATCH | 3 | EXPLANATION_SUPPORTED | SYN-001;SYN-003 |
| SR-003 | C | TM-01 | false | EXCLUDED | null | OWN_TRANSFER_CONFIRMED | SYN-001;SYN-004 |
| SR-004 | D | TM-01 | false | NOT_ASSESSABLE | null | DATA_REPAIR_REQUIRED | SYN-001;SYN-005 |

### ReviewLedger

Grain: one contextual review of a retained daily scenario result.

| review_id | scenario_result_id | finding_id | account_id | raw_result | explanation_state | counterevidence | next_evidence | human_disposition | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RV-A | SR-001 | TM-F01 | A | MATCH | UNSUPPORTED | No opening balance or onward P03 records; timing does not trace funds | Invoice or contract matching T03 plus counterparty role | NOT_RECORDED | SYN-001;SYN-002 |
| RV-B | SR-002 | TM-F02 | B | MATCH | SUPPORTED_FOR_T05 | One invoice does not establish relationship-wide legitimacy | Reviewer assessment of invoice linkage and remaining scope | NOT_RECORDED | SYN-001;SYN-003 |
| RV-C | SR-003 | null | C | EXCLUDED | OWNERSHIP_CONFIRMED | Exclusion applies only to external-flow TM-01 | Retain SYN-004 and check any other applicable scenario separately | NOT_RECORDED | SYN-001;SYN-004 |
| RV-D | SR-004 | TM-F03 | D | NOT_ASSESSABLE | SOURCE_DEFECT | Known debit does not bound unreadable T09 value | Corrected T09 amount and source control total | NOT_RECORDED | SYN-001;SYN-005 |

### ControlTotals

Grain: one explicitly named count or monetary reconciliation proposition.

| control_id | measure | expected_value | actual_value | unit | result | calculation | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CT-01 | Received rows | 10 | 10 | rows | PASS | 8 processed + 1 duplicate + 1 unparsed | SYN-001 |
| CT-02 | Canonical known legs | 8 | 8 | legs | PASS | L-T01 through L-T08 | SYN-001 |
| CT-03 | Known credits | 18000 | 18000 | USD | PASS | 6000 + 4000 + 5000 + 3000 | SYN-001 |
| CT-04 | Known debits | 18300 | 18300 | USD | PASS | 9500 + 4800 + 3000 + 1000 | SYN-001 |
| CT-05 | Complete monetary population | null | null | USD | NOT_ASSESSABLE | T09 amount unknown; known gross is 36300, not complete gross | SYN-001;SYN-005 |
| CT-06 | Daily rule matches | 2 | 2 | account windows | PASS | SR-001 and SR-002 | SYN-001 |
| CT-07 | Distinct observed rolling legs | 5 | 5 | legs | PASS | Union T01,T02,T03,T04,T05; membership count 7 | SYN-001;SYN-006 |

### EvidenceProvenance

Grain: one fictional evidence source with its access state and evidential limit.

| evidence_id | source_kind | source_date | availability | locator | supports | limitation |
| --- | --- | --- | --- | --- | --- | --- |
| SYN-001 | Authored fictional case record | 2026-09-02 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, raw population R01–R10 | Fictional transaction extract | Supports only the stated fictional proposition; no external subject fact or institutional approval |
| SYN-002 | Authored fictional context record | 2026-09-02 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, context register A | Fictional account A profile | Supports only the stated fictional proposition; no external subject fact or institutional approval |
| SYN-003 | Authored fictional case record | 2026-09-02 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, context register B | Fictional invoice and matching confirmation | Supports only the stated fictional proposition; no external subject fact or institutional approval |
| SYN-004 | Authored fictional case record | 2026-09-02 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, context register C | Fictional ownership confirmation | Supports only the stated fictional proposition; no external subject fact or institutional approval |
| SYN-005 | Authored fictional case record | 2026-09-02 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, raw row R10 | Fictional extract defect | Supports only the stated fictional proposition; no external subject fact or institutional approval |
| SYN-006 | Authored fictional case record | 2026-09-02 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, Window diagnostic convention; coverage stops Sep 02, 2026 12:00 AM ET | Fictional diagnostic window specification | Supports only the stated fictional proposition; no external subject fact or institutional approval |

### ProcessQA

Grain: one performed or explicitly unrecorded quality proposition.

| check_id | check | expected | actual | status | reviewer | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| TQ01 | All source rows have one terminal bucket | 10 = 8 + 1 + 1 | 10 = 8 + 1 + 1 | PASS | Authored specimen arithmetic; independent operational reviewer not supplied | SYN-001 |
| TQ02 | Daily rule hits remain after B explanation | A and B MATCH | A and B MATCH | PASS | Authored specimen arithmetic; independent operational reviewer not supplied | SYN-001;SYN-003 |
| TQ03 | Rolling coverage | Three windows BOUNDARY_INCOMPLETE | Three windows BOUNDARY_INCOMPLETE | PASS | Authored specimen arithmetic; independent operational reviewer not supplied | SYN-001;SYN-006 |
| TQ04 | Complete monetary population | No complete total established | T09 amount unknown | REVIEW REQUIRED | Authored specimen arithmetic; independent operational reviewer not supplied | SYN-005 |
| TQ05 | Independent human disposition | Not supplied | Not supplied | NOT RECORDED | Authored specimen arithmetic; independent operational reviewer not supplied | SYN-001 |

## Full finding and action specimen

### TM-F01: Account A meets the illustrative rapid-movement rule

Severity `MEDIUM`; confidence `MODERATE`; claim class `Inferred`; evidence `SYN-001;SYN-002`. Account A received $10,000.00 and sent $9,500.00 within two hours of the first receipt; the 95.0% ratio meets TM-01. Purpose remains unsupported. Proposed next step: Obtain payment purpose and counterparties; refer to the authorized reviewer. Human disposition is NOT_RECORDED; no external action is represented as executed. The rationale concerns this specific observed condition, not a broader allegation or certification.

### TM-F02: Account B has a supported ordinary-business explanation

Severity `LOW`; confidence `HIGH`; claim class `Observed`; evidence `SYN-001;SYN-003`. The 96.0% rule match is retained; a matched supplier invoice supports the $4,800.00 payment. Proposed next step: Document the explanation and seek human disposition; retain the rule hit. Human disposition is NOT_RECORDED; no external action is represented as executed. The rationale concerns this specific observed condition, not a broader allegation or certification.

### TM-F03: Account D cannot be fully assessed

Severity `HIGH`; confidence `HIGH`; claim class `Observed`; evidence `SYN-001;SYN-005`. One unreadable amount prevents account-level completeness; $1,000.00 is only the known posted debit. Proposed next step: Repair the source extract and recompute D before making an account conclusion. Human disposition is NOT_RECORDED; no external action is represented as executed. The rationale concerns this specific observed condition, not a broader allegation or certification.

## Independently reset alternate controls

For every alternate, record the deciding predicate and compare actual output with the fixed expected result. On divergence, identify the first differing source, mapping, membership, arithmetic or review branch; do not rewrite the expectation to match the first answer. Confirm consistent results across requested artifacts. Each control tests only its stated behavior.

For each control, start from a fresh baseline or the expressly stated independent account. Record the exact change, expected branch, protected invariants and actual output. Do not carry one control's changes into the next. The specimen supplies complete expected conclusions only where all necessary inputs are stated; a deliberately underspecified change must remain NOT COMPUTED rather than guessed.

### T01: controlled alternate

**Changed input or criterion:** Change only A T03 amount to 8999.00 USD.

**Exact expected result:** A credit 10000; debit 8999; ratio .8999; elapsed 2 hours; NO_MATCH on ratio.

**Other quantities and protected conditions:** Known gross becomes 35799; B remains MATCH; C excluded; D blocked.

**Interpretation tested:** A ratio display may round to 90.0%, but .8999 remains below .90.

### T02: controlled alternate

**Changed input or criterion:** Change only A T03 amount to 9000.00 USD.

**Exact expected result:** A ratio .90; elapsed 2 hours; MATCH at the inclusive ratio boundary.

**Other quantities and protected conditions:** Known gross becomes 35800; source counts stay 10 raw and 8 canonical.

**Interpretation tested:** The boundary operator is greater than or equal, not strictly greater.

### T03: controlled alternate

**Changed input or criterion:** Use a separate complete account with credit 5000 and debit 4500 exactly 24 hours later.

**Exact expected result:** Credit minimum, ratio and elapsed limits all pass; MATCH.

**Other quantities and protected conditions:** Two known legs and gross 9500; ratio .90; elapsed 24 hours.

**Interpretation tested:** This is a separate full-coverage test, not an extra row in the one-day baseline.

### T04: controlled alternate

**Changed input or criterion:** Use separate complete credit 4999.99 and debit 4500 at +2 hours.

**Exact expected result:** Ratio exceeds .90, but credit below 5000; NO_MATCH on minimum.

**Other quantities and protected conditions:** Gross 9499.99; same two-leg identity and time scope.

**Interpretation tested:** A strong ratio does not compensate for a failed necessary amount predicate.

### T05: controlled alternate

**Changed input or criterion:** Use separate complete credit 5000 and debit 4500 at +24 hours and one second.

**Exact expected result:** Ratio .90; elapsed 24.0002777778 hours; NO_MATCH on timing.

**Other quantities and protected conditions:** Gross 9500; amounts and identities unchanged from T03.

**Interpretation tested:** An inclusive 24-hour limit still excludes one second beyond it.

### T06: controlled alternate

**Changed input or criterion:** Use separate complete credit 5000 and debit 4500 one second before the credit.

**Exact expected result:** No strictly subsequent debit; timing null; NO_MATCH.

**Other quantities and protected conditions:** Both legs remain in gross totals; gross 9500.

**Interpretation tested:** A preceding payment must not become a subsequent payment through lexical sorting.

### T07: controlled alternate

**Changed input or criterion:** Set B debit instant equal to its credit instant with no sequence evidence.

**Exact expected result:** B ratio .96; first subsequent timing null; NO_MATCH on ordering.

**Other quantities and protected conditions:** Gross, canonical count and invoice record remain unchanged.

**Interpretation tested:** Supported commercial context cannot replace the numerical temporal predicate.

### T08: controlled alternate

**Changed input or criterion:** Add an exact extraction copy of R01 under new raw ID R11.

**Exact expected result:** 11 raw = 8 processed + 2 duplicates + 1 unparsed; two daily matches.

**Other quantities and protected conditions:** Known credits 18000, debits 18300 and gross 36300 unchanged.

**Interpretation tested:** Raw receipt count changes while unique economic movement does not.

### T09: controlled alternate

**Changed input or criterion:** Change R09 amount to 6100 while retaining the same T01 account/version identity.

**Exact expected result:** T01 becomes conflicting; A cannot be completely assessed until authority resolves 6000 versus 6100.

**Other quantities and protected conditions:** Do not retain a fabricated 6050 average or silently choose either source.

**Interpretation tested:** The base raw count remains ten, but its terminal partition must be revised to conflict semantics.

### T10: controlled alternate

**Changed input or criterion:** Add a distinct new A credit T10 of 6000 at 9:00 AM ET with its own valid identity.

**Exact expected result:** A credits 16000; debit 9500; ratio .59375; NO_MATCH on ratio.

**Other quantities and protected conditions:** Known gross becomes 42300; canonical count 9; raw count 11.

**Interpretation tested:** Equal time and amount do not justify deduplication of a distinct valid payment.

### T11: controlled alternate

**Changed input or criterion:** Remove only SYN-003 invoice linkage from B context.

**Exact expected result:** B remains MATCH at .96 and 3 hours; explanation becomes OPEN_QUESTION.

**Other quantities and protected conditions:** Raw rows, canonical rows, amounts and match count unchanged.

**Interpretation tested:** Review outcome changes without rewriting the raw trigger.

### T12: controlled alternate

**Changed input or criterion:** Remove only C historical ownership evidence.

**Exact expected result:** Confirmed own-transfer exclusion is unsupported; C ownership-dependent assessment is unresolved.

**Other quantities and protected conditions:** C gross credit and debit remain 3000 each; raw movement unchanged.

**Interpretation tested:** Do not continue showing OWN_TRANSFER_CONFIRMED merely because the source boolean remains true.

### T13: controlled alternate

**Changed input or criterion:** Repair D T09 as a posted debit of 2000 with authoritative correction evidence.

**Exact expected result:** D complete credit 0; debit 3000; ratio null; NO_MATCH on no credits.

**Other quantities and protected conditions:** Canonical count becomes 9; known gross becomes 38300; D no longer blocked on amount.

**Interpretation tested:** Repair requires source controls and affected rerun, not replacing unreadable with a guessed value.

### T14: controlled alternate

**Changed input or criterion:** Repair D T09 instead as a posted debit of zero, explicitly verified as a legitimate zero event.

**Exact expected result:** D complete debit 1000; canonical count 9; no eligible credit; NO_MATCH.

**Other quantities and protected conditions:** Known gross remains 36300 even though completeness improves.

**Interpretation tested:** Zero is a measured value only after authoritative evidence; unchanged gross does not mean unchanged coverage.

### T15: controlled alternate

**Changed input or criterion:** Change A T03 magnitude to -9500 under the nonnegative schema.

**Exact expected result:** Reject the value as a contract defect; A becomes NOT_ASSESSABLE.

**Other quantities and protected conditions:** Do not flip direction or take absolute value automatically.

**Interpretation tested:** A negative display convention must be mapped explicitly before analysis.

### T16: controlled alternate

**Changed input or criterion:** Give A an additional complete posted debit of 2000 at 1:00 PM ET.

**Exact expected result:** A credit 10000; debit 11500; ratio 1.15; MATCH.

**Other quantities and protected conditions:** Known gross becomes 38300; ratio is not capped at 1.

**Interpretation tested:** Existing balance could fund the excess; the screen does not establish tracing.

### T17: controlled alternate

**Changed input or criterion:** Extend observed coverage through each diagnostic endpoint and affirm no additional events.

**Exact expected result:** All three diagnostic windows become COMPLETE with amounts unchanged.

**Other quantities and protected conditions:** Window ratios .95, 2.375 and .96; seven memberships and five unique legs remain.

**Interpretation tested:** Coverage evidence changes, not arithmetic; the diagnostic still has a different unit from daily TM-01.

### T18: controlled alternate

**Changed input or criterion:** Extend A diagnostic coverage and add an external 10000 credit after the daily extraction end but before W-A-T01 end.

**Exact expected result:** W-A-T01 known full credits 20000; debits 9500; ratio .475.

**Other quantities and protected conditions:** Original daily A remains 10000/9500 at its fixed source period.

**Interpretation tested:** Incomplete look-forward coverage can change a visible apparent match by enlarging its denominator.

### T19: controlled alternate

**Changed input or criterion:** Change A debit timestamp to a date-only Sep 01 value.

**Exact expected result:** Amount totals remain known; hour-level timing is NOT_ASSESSABLE.

**Other quantities and protected conditions:** A gross remains 19500; source amount controls unchanged.

**Interpretation tested:** A calendar date does not justify a fabricated two-hour sequence.

### T20: controlled alternate

**Changed input or criterion:** Supply an EUR 1000 credit as a new separate-currency A leg without an FX convention.

**Exact expected result:** Retain EUR totals separately; USD TM-01 remains computed on USD only.

**Other quantities and protected conditions:** Do not report combined monetary gross 37300 USD.

**Interpretation tested:** Non-USD scope needs an explicit scenario basis or a documented conversion.

### T21: controlled alternate

**Changed input or criterion:** Use fall-back local times 1:30 AM at UTC-04 and 1:30 AM at UTC-05 for an independent credit/debit pair.

**Exact expected result:** Normalized instants differ by one hour; strict subsequent timing passes.

**Other quantities and protected conditions:** Local clock labels match but their offsets are different.

**Interpretation tested:** If offsets are omitted, the ordering is ambiguous rather than zero elapsed time.

### T22: controlled alternate

**Changed input or criterion:** A reviewer supplies a supported explanation for A after the calculation.

**Exact expected result:** A raw MATCH remains; proposed explanation may change with dated evidence.

**Other quantities and protected conditions:** Two daily raw matches remain; human disposition requires an actual recorded decision.

**Interpretation tested:** Do not delete TM-F01 history or retroactively label the initial missing purpose as previously explained.

### T23: controlled alternate

**Changed input or criterion:** Count all rolling membership gross values as if independent economic records.

**Exact expected result:** The proposed 42800 total is overlapping and cannot replace unique observed gross 29300.

**Other quantities and protected conditions:** Repeated A T02 and T03 contribute 13500 of overlap.

**Interpretation tested:** The control checks the monetary union, not merely row-count duplication.

### T24: controlled alternate

**Changed input or criterion:** Try to report complete all-account gross from the base case.

**Exact expected result:** Reject the completeness claim; 36300 is known gross plus unknown T09 magnitude.

**Other quantities and protected conditions:** Ten rows reconcile by count while complete monetary value is unavailable.

**Interpretation tested:** Do not assume an unknown amount is immaterial without evidence.

## Baseline completion and interpretation

The exercise is complete only when source conservation, table grains, arithmetic, null behavior, raw outcomes, review limits and actual QA state all agree. The alternate controls challenge different failure modes and do not produce an operational performance estimate. Keep the fictional label on every rendered artifact. Preserve human approval as unrecorded and do not send a message, create a production alert, suppress activity or execute a filing based on this example.

## Standalone fixture reproduction

This optional block uses only the Python standard library already available in the session. It contains the complete printed raw source values, derives canonical and analytical records, asserts independent expected controls, and exposes CHECKED_TABLES for comparison with the fixed artifact data. It reads no files, calls no network and installs nothing. Run it only in a permitted in-session Python capability; otherwise reproduce the printed arithmetic manually and record unperformed code checks as NOT TESTED. Successful execution proves only these synthetic calculations.

<!-- FIXTURE_CHECK:START -->
```python
from decimal import Decimal
from datetime import datetime, timedelta
from collections import Counter, defaultdict

def dec(value):
    return Decimal(str(value))

def instant(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

def utc(value):
    return value.isoformat().replace("+00:00", "Z")

def total(rows, direction):
    return sum((dec(r["amount"]) for r in rows if r["direction"] == direction and r["amount"] is not None), Decimal(0))

def numeric(value):
    return None if value is None else float(value)

CHECKED_TABLES = {}

RAW_COLUMNS = ['raw_row_id', 'transaction_id', 'account_id', 'event_utc', 'direction', 'amount_text', 'currency', 'counterparty_id', 'posting_state', 'ownership_state', 'terminal_bucket', 'evidence_ids']
RAW = [['R01', 'T01', 'A', '2026-09-01T13:00:00Z', 'CREDIT', '6000.00', 'USD', 'P01', 'POSTED', 'CONFIRMED_EXTERNAL', 'PROCESSED', 'SYN-001'], ['R02', 'T02', 'A', '2026-09-01T14:00:00Z', 'CREDIT', '4000.00', 'USD', 'P02', 'POSTED', 'CONFIRMED_EXTERNAL', 'PROCESSED', 'SYN-001'], ['R03', 'T03', 'A', '2026-09-01T15:00:00Z', 'DEBIT', '9500.00', 'USD', 'P03', 'POSTED', 'CONFIRMED_EXTERNAL', 'PROCESSED', 'SYN-001'], ['R04', 'T04', 'B', '2026-09-01T13:00:00Z', 'CREDIT', '5000.00', 'USD', 'P04', 'POSTED', 'CONFIRMED_EXTERNAL', 'PROCESSED', 'SYN-001'], ['R05', 'T05', 'B', '2026-09-01T16:00:00Z', 'DEBIT', '4800.00', 'USD', 'P05', 'POSTED', 'CONFIRMED_EXTERNAL', 'PROCESSED', 'SYN-001'], ['R06', 'T06', 'C', '2026-09-01T13:00:00Z', 'CREDIT', '3000.00', 'USD', 'C-OWN-1', 'POSTED', 'CONFIRMED_OWN', 'PROCESSED', 'SYN-001;SYN-004'], ['R07', 'T07', 'C', '2026-09-01T14:00:00Z', 'DEBIT', '3000.00', 'USD', 'C-OWN-2', 'POSTED', 'CONFIRMED_OWN', 'PROCESSED', 'SYN-001;SYN-004'], ['R08', 'T08', 'D', '2026-09-01T17:00:00Z', 'DEBIT', '1000.00', 'USD', 'P06', 'POSTED', 'CONFIRMED_EXTERNAL', 'PROCESSED', 'SYN-001'], ['R09', 'T01', 'A', '2026-09-01T13:00:00Z', 'CREDIT', '6000.00', 'USD', 'P01', 'POSTED', 'CONFIRMED_EXTERNAL', 'DUPLICATE', 'SYN-001'], ['R10', 'T09', 'D', '2026-09-01T18:00:00Z', 'DEBIT', 'unreadable', 'USD', 'P07', 'POSTED', 'CONFIRMED_EXTERNAL', 'UNPARSED', 'SYN-001;SYN-005']]

raw = [dict(zip(RAW_COLUMNS,row)) for row in RAW]
seen = {}; canonical = []; dispositions = []
for r in raw:
    identity=(r['transaction_id'],r['account_id'])
    if identity in seen:
        original=seen[identity]
        assert all(r[k]==original[k] for k in ['event_utc','direction','amount_text','currency','counterparty_id','posting_state','ownership_state'])
        dispositions.append('DUPLICATE'); continue
    seen[identity]=r
    try: amount=dec(r['amount_text'])
    except Exception:
        dispositions.append('UNPARSED'); continue
    assert amount >= 0
    c=dict(r,leg_id='L-'+r['transaction_id'],amount=amount,scenario_eligible=r['ownership_state']=='CONFIRMED_EXTERNAL')
    canonical.append(c);dispositions.append('PROCESSED')
assert Counter(dispositions)=={'PROCESSED':8,'DUPLICATE':1,'UNPARSED':1}
CHECKED_TABLES['CanonicalLedger']=[[r['leg_id'],r['raw_row_id'],r['transaction_id'],r['account_id'],r['event_utc'],r['direction'],float(r['amount']),r['currency'],r['counterparty_id'],r['ownership_state'],r['scenario_eligible'],r['evidence_ids']] for r in canonical]
elig=[]
for r,state in zip(raw,dispositions):
    leg='L-'+r['transaction_id']
    if state=='DUPLICATE':state,reason='DUPLICATE','Exact second extraction of R01; not another account leg'
    elif state=='UNPARSED':state,reason,leg='BLOCKED','Posted in-scope amount unreadable; blocks D completeness',None
    elif r['ownership_state']=='CONFIRMED_OWN':state,reason='EXCLUDED_OWN','SYN-004 confirms common customer ownership during period'
    else:state,reason='ELIGIBLE_KNOWN','Known external posted leg; account-level completeness checked separately'
    elig.append(['EL-'+r['raw_row_id'],r['raw_row_id'],leg,r['account_id'],'TM-01',state,reason,r['evidence_ids']])
CHECKED_TABLES['Eligibility']=elig
flows=[];results=[]
for account in sorted({r['account_id'] for r in raw}):
    rows=[r for r in canonical if r['account_id']==account]
    eligible=[r for r in rows if r['scenario_eligible']]
    incomplete=any(r['account_id']==account and state=='UNPARSED' for r,state in zip(raw,dispositions))
    c=total(rows,'CREDIT');d=total(rows,'DEBIT');ec=total(eligible,'CREDIT');ed=total(eligible,'DEBIT')
    ratio=ed/ec if ec>0 else None
    status='UNPARSED_AMOUNT' if incomplete else 'OWN_TRANSFER_EXCLUDED' if not eligible else 'COMPLETE'
    flows.append([account,'USD',len(rows),float(c),float(d),float(ec),float(ed),numeric(ratio),status])
    credits=sorted([r for r in eligible if r['direction']=='CREDIT'],key=lambda r:(r['event_utc'],r['transaction_id']))
    later=[r for r in eligible if credits and r['direction']=='DEBIT' and instant(r['event_utc'])>instant(credits[0]['event_utc'])]
    hours=(min(instant(r['event_utc']) for r in later)-instant(credits[0]['event_utc'])).total_seconds()/3600 if later else None
    result='NOT_ASSESSABLE' if incomplete else 'EXCLUDED' if not eligible else 'MATCH' if ec>=5000 and ratio is not None and ratio>=dec('.90') and hours is not None and hours<=24 else 'NO_MATCH'
    outcome={'A':'ESCALATE_FOR_REVIEW','B':'EXPLANATION_SUPPORTED','C':'OWN_TRANSFER_CONFIRMED','D':'DATA_REPAIR_REQUIRED'}[account]
    refs={'A':'SYN-001;SYN-002','B':'SYN-001;SYN-003','C':'SYN-001;SYN-004','D':'SYN-001;SYN-005'}[account]
    results.append([f'SR-{len(results)+1:03}',account,'TM-01',not incomplete and bool(eligible),result,hours,outcome,refs])
CHECKED_TABLES['AccountFlows']=flows
CHECKED_TABLES['ScenarioResults']=results
windows=[]
for anchor in [r for r in canonical if r['scenario_eligible'] and r['direction']=='CREDIT']:
    start=instant(anchor['event_utc']);end=start+timedelta(hours=24)
    members=[r for r in canonical if r['scenario_eligible'] and r['account_id']==anchor['account_id'] and start<=instant(r['event_utc'])<=end]
    c=total(members,'CREDIT');d=total(members,'DEBIT')
    later=[instant(r['event_utc']) for r in members if r['direction']=='DEBIT' and instant(r['event_utc'])>start]
    coverage='COMPLETE' if end<instant('2026-09-02T04:00:00Z') else 'BOUNDARY_INCOMPLETE'
    windows.append(['W-'+anchor['account_id']+'-'+anchor['transaction_id'],anchor['account_id'],anchor['leg_id'],utc(start),utc(end),';'.join(r['leg_id'] for r in members),float(c),float(d),numeric(d/c if c else None),(min(later)-start).total_seconds()/3600 if later else None,coverage,'SYN-001;SYN-006'])
CHECKED_TABLES['WindowDiagnostics']=windows
union={leg for r in windows for leg in r[5].split(';')}
credit=total(canonical,'CREDIT');debit=total(canonical,'DEBIT')
CHECKED_TABLES['ControlTotals']=[
['CT-01','Received rows',10,len(raw),'rows','PASS','8 processed + 1 duplicate + 1 unparsed','SYN-001'],
['CT-02','Canonical known legs',8,len(canonical),'legs','PASS','L-T01 through L-T08','SYN-001'],
['CT-03','Known credits',18000,float(credit),'USD','PASS','6000 + 4000 + 5000 + 3000','SYN-001'],
['CT-04','Known debits',18300,float(debit),'USD','PASS','9500 + 4800 + 3000 + 1000','SYN-001'],
['CT-05','Complete monetary population',None,None,'USD','NOT_ASSESSABLE','T09 amount unknown; known gross is 36300, not complete gross','SYN-001;SYN-005'],
['CT-06','Daily rule matches',2,sum(r[4]=='MATCH' for r in results),'account windows','PASS','SR-001 and SR-002','SYN-001'],
['CT-07','Distinct observed rolling legs',5,len(union),'legs','PASS','Union T01,T02,T03,T04,T05; membership count 7','SYN-001;SYN-006']]
assert credit==18000 and debit==18300 and credit+debit==36300
assert sum(r[6]+r[7] for r in windows)==42800
assert sum(float(r['amount']) for r in canonical if r['leg_id'] in union)==29300
assert sum(len(r[5].split(';')) for r in windows)==7 and len(union)==5
assert [r[4] for r in results]==['MATCH','MATCH','EXCLUDED','NOT_ASSESSABLE']
def screen(c,d,h,complete=True):
    if not complete:return 'NOT_ASSESSABLE'
    return 'MATCH' if c>=dec('5000') and c>0 and d/c>=dec('.9') and h is not None and 0<h<=86400 else 'NO_MATCH'
assert screen(dec('5000'),dec('4500'),86400)=='MATCH'
assert screen(dec('5000'),dec('4500'),86401)=='NO_MATCH'
assert screen(dec('10000'),dec('8999'),7200)=='NO_MATCH'
assert screen(dec('10000'),dec('9000'),7200)=='MATCH'
assert screen(dec('5000'),dec('4500'),0)=='NO_MATCH'
assert screen(dec('5000'),dec('4500'),3600,False)=='NOT_ASSESSABLE'

print("Fictional specimen arithmetic and boundary assertions passed.")
```
<!-- FIXTURE_CHECK:END -->
