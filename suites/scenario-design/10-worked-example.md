# Transaction Monitoring Scenario Design: complete fictional case and alternate controls

All records and source declarations are fictional. RULE-SD-01-v1 is an authored design, not an approved institutional rule. The complete source event interval is Sep 01, 2026 12:00 AM ET through Sep 03, 2026 12:00 AM ET exclusive. All events are USD and posted. The thirteen printed events are the complete source frame for six accounts, with one amount unknown. Event-time coverage is complete for every generated 24-hour window; monetary completeness is not complete for O.

SD-E01 consists of all EventLedger rows below and that coverage declaration. SD-E02 confirms historical common ownership for both M events; M is excluded from the external-flow anchor population while remaining in AccountCoverage. SD-E03 states E13 is a posted, in-period debit of unknown amount; no amount estimate is supplied. SD-E04 is the complete authored specification: one closed 24-hour window per eligible external credit; same-account and same-currency membership; USD credit total at least 5000; debit/credit at least .90; at least one debit strictly after the anchor and within the window; relevant missing inputs block assessment; only exact same-account, same-version, same-run event sets can share a proposed delivery group. No account cooldown or behavioral suppression is authorized.

Known credits are J 5000 + K 5000 + L 5000 + M 6000 + N 5000 + O 5000 = USD 31000. Known debits are J 4500 + K 4500 + L 4499.99 + M 5700 + N 4500 = USD 23699.99. Known gross is USD 54699.99 plus E13's unknown amount. Six windows arise from J's two credits and one credit each at K, L, N and O. M produces no external anchor. The six windows contain thirteen memberships over eleven distinct external events; J's E02 and E03 appear in both J windows.

WJ1 has 5000/4500 and .90 at two hours, therefore MATCH. WJ2 has 2000/4500 and 2.25 at one hour but fails the USD 5000 credit minimum. WK1 includes its debit exactly 24 hours after the anchor and matches .90. WL1 has .899998, which fails despite displaying 90.0% at one decimal percent. WN1 has .90 aggregate ratio but no strictly subsequent debit because both events share the same instant. WO1 cannot assess its unknown debit amount. This yields two MATCH, three NO_MATCH and one NOT_ASSESSABLE window. No purpose investigation or human approval is supplied.

## Complete populated source and expected result registers

All rows below belong to the baseline. They are printed in full so the assistant can reproduce the case without importing any repository file. The later alternate controls are independent perturbations and must not be added to these baseline counts or monetary totals.

### EventLedger

Grain: one unique fictional source event within the complete declared 48-hour interval.

| event_id | account_id | event_utc | direction | amount | currency | ownership_state | posting_state | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E01 | J | 2026-09-01T13:00:00Z | CREDIT | 3000 | USD | EXTERNAL | POSTED | SD-E01 |
| E02 | J | 2026-09-01T14:00:00Z | CREDIT | 2000 | USD | EXTERNAL | POSTED | SD-E01 |
| E03 | J | 2026-09-01T15:00:00Z | DEBIT | 4500 | USD | EXTERNAL | POSTED | SD-E01 |
| E04 | K | 2026-09-01T13:00:00Z | CREDIT | 5000 | USD | EXTERNAL | POSTED | SD-E01 |
| E05 | K | 2026-09-02T13:00:00Z | DEBIT | 4500 | USD | EXTERNAL | POSTED | SD-E01 |
| E06 | L | 2026-09-01T13:00:00Z | CREDIT | 5000 | USD | EXTERNAL | POSTED | SD-E01 |
| E07 | L | 2026-09-01T15:00:00Z | DEBIT | 4499.99 | USD | EXTERNAL | POSTED | SD-E01 |
| E08 | M | 2026-09-01T13:00:00Z | CREDIT | 6000 | USD | CONFIRMED_OWN | POSTED | SD-E01;SD-E02 |
| E09 | M | 2026-09-01T14:00:00Z | DEBIT | 5700 | USD | CONFIRMED_OWN | POSTED | SD-E01;SD-E02 |
| E10 | N | 2026-09-01T13:00:00Z | CREDIT | 5000 | USD | EXTERNAL | POSTED | SD-E01 |
| E11 | N | 2026-09-01T13:00:00Z | DEBIT | 4500 | USD | EXTERNAL | POSTED | SD-E01 |
| E12 | O | 2026-09-01T13:00:00Z | CREDIT | 5000 | USD | EXTERNAL | POSTED | SD-E01 |
| E13 | O | 2026-09-01T14:00:00Z | DEBIT | null | USD | EXTERNAL | POSTED | SD-E01;SD-E03 |

### PredicateSpec

Grain: one ordered predicate in RULE-SD-01-v1.

| predicate_id | order | field_or_measure | operator | operand | null_result | purpose | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | 1 | data coverage | EQUAL | COMPLETE | NOT_ASSESSABLE | Reject relevant missing amount, time, identity or uncovered interval | SD-E04 |
| P02 | 2 | posting_state | EQUAL | POSTED | NOT_ASSESSABLE | Pending and rejected legs never enter sums | SD-E04 |
| P03 | 3 | ownership_state | EQUAL | EXTERNAL | NOT_ASSESSABLE | Confirmed own legs excluded; unknown ownership blocks affected window | SD-E04 |
| P04 | 4 | event_utc | INTERVAL | anchor <= t <= anchor + 24 hours | NOT_ASSESSABLE | Credit-anchored closed window uses normalized UTC instants | SD-E04 |
| P05 | 5 | credit_total | GREATER_OR_EQUAL | 5000.00 USD | NOT_ASSESSABLE | Minimum aggregate eligible credits | SD-E04 |
| P06 | 6 | debit_total / credit_total | GREATER_OR_EQUAL | 0.90 | NO_MATCH_IF_ZERO_CREDITS | Exact comparison before display rounding | SD-E04 |
| P07 | 7 | first subsequent debit | STRICTLY_AFTER | anchor instant | NO_MATCH_IF_NONE | Same-time debit without sequence is not subsequent | SD-E04 |
| P08 | 8 | delivery grouping | SAME_ACCOUNT_AND_EVENT_SET | same version; same review run | NO_GROUP_IF_UNKNOWN | Retain raw matches; one delivery group only for exact identical event set | SD-E04 |

### WindowResults

Grain: one account, eligible credit anchor, currency and rule version.

| window_id | account_id | anchor_event_id | start_utc | end_utc | event_ids | credit_total | debit_total | ratio | first_debit_hours | coverage_state | rule_result | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WJ1 | J | E01 | 2026-09-01T13:00:00Z | 2026-09-02T13:00:00Z | E01;E02;E03 | 5000 | 4500 | 0.9 | 2 | COMPLETE | MATCH | SD-E01;SD-E04 |
| WJ2 | J | E02 | 2026-09-01T14:00:00Z | 2026-09-02T14:00:00Z | E02;E03 | 2000 | 4500 | 2.25 | 1 | COMPLETE | NO_MATCH | SD-E01;SD-E04 |
| WK1 | K | E04 | 2026-09-01T13:00:00Z | 2026-09-02T13:00:00Z | E04;E05 | 5000 | 4500 | 0.9 | 24 | COMPLETE | MATCH | SD-E01;SD-E04 |
| WL1 | L | E06 | 2026-09-01T13:00:00Z | 2026-09-02T13:00:00Z | E06;E07 | 5000 | 4499.99 | 0.899998 | 2 | COMPLETE | NO_MATCH | SD-E01;SD-E04 |
| WN1 | N | E10 | 2026-09-01T13:00:00Z | 2026-09-02T13:00:00Z | E10;E11 | 5000 | 4500 | 0.9 | null | COMPLETE | NO_MATCH | SD-E01;SD-E04 |
| WO1 | O | E12 | 2026-09-01T13:00:00Z | 2026-09-02T13:00:00Z | E12;E13 | 5000 | null | null | 1 | AMOUNT_UNKNOWN | NOT_ASSESSABLE | SD-E01;SD-E03;SD-E04 |

### DeliveryDecisions

Grain: one proposed delivery disposition for a retained raw window result.

| delivery_id | window_id | raw_result | delivery_state | group_id | reason | human_approval | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DL-J1 | WJ1 | MATCH | PROPOSED_FOR_REVIEW | G-J1 | No earlier identical match; purpose unreviewed | NOT_RECORDED | SD-E01;SD-E04 |
| DL-J2 | WJ2 | NO_MATCH | NO_DELIVERY | null | Credit total below minimum despite ratio above one | NOT_RECORDED | SD-E01;SD-E04 |
| DL-K1 | WK1 | MATCH | PROPOSED_FOR_REVIEW | G-K1 | Exact 24-hour endpoint included | NOT_RECORDED | SD-E01;SD-E04 |
| DL-L1 | WL1 | NO_MATCH | NO_DELIVERY | null | 4499.99 / 5000 below .90 before rounding | NOT_RECORDED | SD-E01;SD-E04 |
| DL-N1 | WN1 | NO_MATCH | NO_DELIVERY | null | No strictly subsequent debit | NOT_RECORDED | SD-E01;SD-E04 |
| DL-O1 | WO1 | NOT_ASSESSABLE | DATA_REPAIR_QUEUE | null | Debit amount unknown; retain blocked window | NOT_RECORDED | SD-E03;SD-E04 |

### AccountCoverage

Grain: one source account, including accounts that generate no external windows.

| account_id | raw_events | known_credit_total | known_debit_total | external_anchor_count | window_count | coverage_outcome | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| J | 3 | 5000 | 4500 | 2 | 2 | ASSESSED | SD-E01;SD-E04 |
| K | 2 | 5000 | 4500 | 1 | 1 | ASSESSED | SD-E01;SD-E04 |
| L | 2 | 5000 | 4499.99 | 1 | 1 | ASSESSED | SD-E01;SD-E04 |
| M | 2 | 6000 | 5700 | 0 | 0 | CONFIRMED_OWN_EXCLUDED | SD-E01;SD-E02 |
| N | 2 | 5000 | 4500 | 1 | 1 | ASSESSED | SD-E01;SD-E04 |
| O | 2 | 5000 | 0 | 1 | 1 | BLOCKED_UNKNOWN_DEBIT | SD-E01;SD-E03 |

### AcceptanceTests

Grain: one explicit deterministic expectation and its authored synthetic actual result.

| test_id | test_name | expected | actual | result | affected_ids | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| AT01 | All raw events retained | 13 | 13 | PASS | E01-E13 | SD-E01 |
| AT02 | Raw matching windows | WJ1;WK1 | WJ1;WK1 | PASS | WJ1;WK1 | SD-E01;SD-E04 |
| AT03 | Below-ratio boundary | WL1 NO_MATCH at .899998 | WL1 NO_MATCH at .899998 | PASS | WL1 | SD-E01;SD-E04 |
| AT04 | Same-time ordering | WN1 NO_MATCH | WN1 NO_MATCH | PASS | WN1 | SD-E01;SD-E04 |
| AT05 | Missing amount | WO1 NOT_ASSESSABLE | WO1 NOT_ASSESSABLE | PASS | WO1 | SD-E03;SD-E04 |
| AT06 | Independent operational approval | No approval supplied | No approval supplied | NOT_RECORDED | RULE-SD-01-v1 | SD-E04 |
| AT07 | Window memberships versus unique events | 13 memberships;11 unique external events | 13 memberships;11 unique external events | PASS | WJ1;WJ2;WK1;WL1;WN1;WO1 | SD-E01;SD-E04 |

### EvidenceProvenance

Grain: one fictional evidence source with its access state and evidential limit.

| evidence_id | source_kind | source_date | availability | locator | supports | limitation |
| --- | --- | --- | --- | --- | --- | --- |
| SD-E01 | Authored fictional case record | 2026-09-03 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, EventLedger E01-E13; coverage declaration | Fictional complete 48-hour event ledger | Supports only the stated fictional proposition; no external subject fact or institutional approval |
| SD-E02 | Authored fictional case record | 2026-09-03 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, M ownership declaration | Fictional common-ownership evidence | Supports only the stated fictional proposition; no external subject fact or institutional approval |
| SD-E03 | Authored fictional case record | 2026-09-03 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, E13 missing amount notice | Fictional extraction exception | Supports only the stated fictional proposition; no external subject fact or institutional approval |
| SD-E04 | Authored fictional case record | 2026-09-03 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, RULE-SD-01-v1 full specification and acceptance convention | Authored illustrative rule specification | Supports only the stated fictional proposition; no external subject fact or institutional approval |

### ProcessQA

Grain: one performed or explicitly unrecorded quality proposition.

| check_id | check | expected | actual | status | reviewer | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| SQ01 | Raw matches | WJ1 and WK1 | WJ1 and WK1 | PASS | Authored specimen arithmetic; independent operational reviewer not supplied | SD-E01;SD-E04 |
| SQ02 | Rounding cannot change decision | .899998 is NO_MATCH | .899998 is NO_MATCH | PASS | Authored specimen arithmetic; independent operational reviewer not supplied | SD-E01;SD-E04 |
| SQ03 | Same-time debit | WN1 NO_MATCH | WN1 NO_MATCH | PASS | Authored specimen arithmetic; independent operational reviewer not supplied | SD-E01;SD-E04 |
| SQ04 | Unknown amount | WO1 remains blocked | WO1 remains blocked | PASS | Authored specimen arithmetic; independent operational reviewer not supplied | SD-E03 |
| SQ05 | Operational approval | Not supplied | Not supplied | NOT RECORDED | Authored specimen arithmetic; independent operational reviewer not supplied | SD-E04 |

## Full finding and action specimen

### SD-F01: Two raw windows meet the authored rule

Severity `MEDIUM`; confidence `HIGH`; claim class `Observed`; evidence `SD-E01;SD-E04`. WJ1 and WK1 satisfy the exact predicates. No subject context or operational review outcome has been supplied. Proposed next step: Preserve both raw matches and request authorized review of the proposed specification. Human disposition is NOT_RECORDED; no external action is represented as executed. The rationale concerns this specific observed condition, not a broader allegation or certification.

### SD-F02: One unknown debit blocks a window

Severity `HIGH`; confidence `HIGH`; claim class `Observed`; evidence `SD-E01;SD-E03`. E13 has unknown amount; WO1 cannot be classified as a clean negative or a numerical match. Proposed next step: Repair E13 and rerun O; retain the original blocked state. Human disposition is NOT_RECORDED; no external action is represented as executed. The rationale concerns this specific observed condition, not a broader allegation or certification.

### SD-F03: Specification tests do not authorize deployment

Severity `MEDIUM`; confidence `HIGH`; claim class `Observed`; evidence `SD-E04`. No institution-specific criteria, independent operating validation or deployment approval is supplied. Proposed next step: Obtain the appropriate human design decision before any operational use. Human disposition is NOT_RECORDED; no external action is represented as executed. The rationale concerns this specific observed condition, not a broader allegation or certification.

## Independently reset alternate controls

For every alternate, record the deciding predicate and compare actual output with the fixed expected result. On divergence, identify the first differing source, mapping, membership, arithmetic or review branch; do not rewrite the expectation to match the first answer. Confirm consistent results across requested artifacts. Each control tests only its stated behavior.

For each control, start from a fresh baseline or the expressly stated independent account. Record the exact change, expected branch, protected invariants and actual output. Do not carry one control's changes into the next. The specimen supplies complete expected conclusions only where all necessary inputs are stated; a deliberately underspecified change must remain NOT COMPUTED rather than guessed.

### S01: controlled alternate

**Changed input or criterion:** Change only E07 debit from 4499.99 to 4500.00.

**Exact expected result:** WL1 ratio becomes .90 and MATCH; total raw matches become 3.

**Other quantities and protected conditions:** Known gross increases by .01 to 54700.00.

**Interpretation tested:** The base near-threshold negative checks exact decimal comparison.

### S02: controlled alternate

**Changed input or criterion:** Move E05 from exactly +24 hours to +24 hours and one second.

**Exact expected result:** E05 leaves WK1 membership; WK1 debit zero, ratio zero and NO_MATCH.

**Other quantities and protected conditions:** Source raw event count and source gross remain unchanged.

**Interpretation tested:** Closed window endpoint governs membership before timing or aggregation.

### S03: controlled alternate

**Changed input or criterion:** Move E05 to one second before its anchor.

**Exact expected result:** E05 is outside WK1; no qualifying subsequent debit; NO_MATCH.

**Other quantities and protected conditions:** K source gross remains 9500 while window gross is 5000.

**Interpretation tested:** Account-period and window totals must remain separate.

### S04: controlled alternate

**Changed input or criterion:** Move E11 one second after E10.

**Exact expected result:** WN1 has .90 ratio and 1/3600 hour subsequent timing; MATCH.

**Other quantities and protected conditions:** Source gross unchanged; raw matches become 3.

**Interpretation tested:** Temporal order changes the outcome without any amount change.

### S05: controlled alternate

**Changed input or criterion:** Add a new N external debit of 1.00 one second after its anchor.

**Exact expected result:** WN1 totals 5000/4501, ratio .9002; subsequent gate satisfied; MATCH.

**Other quantities and protected conditions:** The contemporaneous 4500 remains in totals under this exact specification.

**Interpretation tested:** This deliberately exposes the distinction between aggregate membership and the subsequent-debit predicate.

### S06: controlled alternate

**Changed input or criterion:** Repair E13 as debit 4500 with authoritative source evidence.

**Exact expected result:** WO1 5000/4500, ratio .90, one hour; MATCH.

**Other quantities and protected conditions:** Known gross becomes 59199.99; blocked-window count becomes zero.

**Interpretation tested:** Actual amount repair changes both monetary completeness and match count.

### S07: controlled alternate

**Changed input or criterion:** Repair E13 as debit zero with authoritative source evidence.

**Exact expected result:** WO1 ratio zero; NO_MATCH; zero amount remains an event.

**Other quantities and protected conditions:** Known gross stays 54699.99 while monetary completeness becomes established for this source.

**Interpretation tested:** A zero event differs from a missing amount even when the known subtotal is unchanged.

### S08: controlled alternate

**Changed input or criterion:** Change only P05 threshold from 5000 to 2000 in a labeled alternative version.

**Exact expected result:** WJ2 changes to MATCH; base other complete states remain; raw matches become 3.

**Other quantities and protected conditions:** WO1 still NOT_ASSESSABLE; all memberships unchanged.

**Interpretation tested:** A threshold change creates a new criteria version; it is not a source correction.

### S09: controlled alternate

**Changed input or criterion:** Change only P06 threshold from .90 to .8999 in an alternative version.

**Exact expected result:** WL1 .899998 now passes; raw matches become 3.

**Other quantities and protected conditions:** WN1 still fails ordering; WO1 remains blocked.

**Interpretation tested:** Changing a ratio threshold does not repair other necessary gates.

### S10: controlled alternate

**Changed input or criterion:** Change P07 to allow contemporaneous debits in an alternative specification.

**Exact expected result:** WN1 becomes MATCH at .90; raw matches become 3.

**Other quantities and protected conditions:** Amounts and membership unchanged.

**Interpretation tested:** This is a business design change requiring explicit acceptance, not a harmless timestamp formatting change.

### S11: controlled alternate

**Changed input or criterion:** Remove the independent common-ownership confirmation for M.

**Exact expected result:** M ownership-dependent eligibility becomes unresolved; do not silently add or exclude its anchors.

**Other quantities and protected conditions:** M known gross 11700 remains in account coverage.

**Interpretation tested:** Source ownership labels require their dated evidential basis.

### S12: controlled alternate

**Changed input or criterion:** Add an exact duplicate extraction copy of E01 with a distinct raw receipt ID.

**Exact expected result:** Canonical event population and six windows remain unchanged after documented deduplication.

**Other quantities and protected conditions:** Received rows increase by one; source-copy gross is not economic gross.

**Interpretation tested:** The acceptance source contract must preserve raw and canonical layers when duplicates are introduced.

### S13: controlled alternate

**Changed input or criterion:** Add a distinct valid J credit of 3000 at E01 time.

**Exact expected result:** WJ1 credits 8000 and debit 4500 ratio .5625; new anchor also requires its own window.

**Other quantities and protected conditions:** A same-time same-amount payment with new valid identity is retained.

**Interpretation tested:** Window count changes with anchor count; equal payload is not sufficient duplicate evidence.

### S14: controlled alternate

**Changed input or criterion:** Remove the final hour of source coverage for WK1 without replacement evidence.

**Exact expected result:** WK1 becomes BOUNDARY_INCOMPLETE / NOT_ASSESSABLE despite currently visible 5000/4500.

**Other quantities and protected conditions:** Observed sums remain diagnostic only.

**Interpretation tested:** Additional unseen credits or debits can change the complete interval result.

### S15: controlled alternate

**Changed input or criterion:** Set E07 amount to the text unreadable.

**Exact expected result:** WL1 becomes NOT_ASSESSABLE, not the baseline numeric negative.

**Other quantities and protected conditions:** L known debit subtotal zero is partial; source known gross falls by 4499.99.

**Interpretation tested:** The absence of a number cannot be interpreted as a low debit amount.

### S16: controlled alternate

**Changed input or criterion:** Set E02 credit to 1999.99.

**Exact expected result:** WJ1 credits 4999.99 and fails minimum; WJ2 credits 1999.99 also fails.

**Other quantities and protected conditions:** Raw matches fall to 1, WK1 only.

**Interpretation tested:** High ratio alone does not overcome the aggregate credit minimum.

### S17: controlled alternate

**Changed input or criterion:** Add a late-arriving J debit that was unavailable at the original run cutoff.

**Exact expected result:** Retain original raw result and compute a separately identified rerun with the new membership.

**Other quantities and protected conditions:** Do not mutate the original run silently; exact delta depends on supplied amount and time.

**Interpretation tested:** Without those fields the alternate result is NOT COMPUTED, not a guessed match count.

### S18: controlled alternate

**Changed input or criterion:** Run the identical source/specification again with no changed events.

**Exact expected result:** Raw results reproduce exactly; any proposed delivery grouping retains both raw run records.

**Other quantities and protected conditions:** No new economic event or changed amount is created by rerunning.

**Interpretation tested:** Idempotent presentation is separate from deletion of prior analytical evidence.

### S19: controlled alternate

**Changed input or criterion:** Apply an account cooldown that suppresses K because it had an unrelated prior alert.

**Exact expected result:** Reject this treatment as outside P08; retain WK1 proposed review.

**Other quantities and protected conditions:** Base raw match count stays 2.

**Interpretation tested:** The package defines only exact-set grouping, not time-based account suppression.

### S20: controlled alternate

**Changed input or criterion:** Use 5000 credit and 6000 subsequent debit in an independent complete account.

**Exact expected result:** Ratio 1.2; MATCH when all other predicates hold.

**Other quantities and protected conditions:** Gross 11000; outflow can include preexisting balance.

**Interpretation tested:** A ratio above one is valid and is not capped or interpreted as impossible.

### S21: controlled alternate

**Changed input or criterion:** Use a complete account with only one 4500 debit.

**Exact expected result:** No eligible credit anchor; account coverage shows no credit anchor, not a fabricated zero-ratio window.

**Other quantities and protected conditions:** Source event retained; zero windows generated.

**Interpretation tested:** The account frame is needed to distinguish valid no-window outcomes from omitted accounts.

### S22: controlled alternate

**Changed input or criterion:** Use an anchor with unknown currency.

**Exact expected result:** Block currency eligibility and affected window interpretation.

**Other quantities and protected conditions:** Do not guess USD from the use of a dollar sign in another source.

**Interpretation tested:** Currency is a necessary field for threshold applicability.

### S23: controlled alternate

**Changed input or criterion:** Present L ratio rounded to one decimal percent as 90.0%.

**Exact expected result:** Keep raw decision NO_MATCH based on .899998.

**Other quantities and protected conditions:** Display and decision layers intentionally differ at this boundary.

**Interpretation tested:** The report must explain this apparent discrepancy so reviewers do not treat it as an error.

### S24: controlled alternate

**Changed input or criterion:** Use the two matching windows as the denominator for a claimed detection recall.

**Exact expected result:** Reject recall: positives outside the designed test set are unknown.

**Other quantities and protected conditions:** Two expected matches validate these cases only.

**Interpretation tested:** Synthetic acceptance accuracy is not production detection performance.

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

RAW_COLUMNS = ['event_id', 'account_id', 'event_utc', 'direction', 'amount', 'currency', 'ownership_state', 'posting_state', 'evidence_ids']
RAW = [['E01', 'J', '2026-09-01T13:00:00Z', 'CREDIT', 3000, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E02', 'J', '2026-09-01T14:00:00Z', 'CREDIT', 2000, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E03', 'J', '2026-09-01T15:00:00Z', 'DEBIT', 4500, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E04', 'K', '2026-09-01T13:00:00Z', 'CREDIT', 5000, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E05', 'K', '2026-09-02T13:00:00Z', 'DEBIT', 4500, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E06', 'L', '2026-09-01T13:00:00Z', 'CREDIT', 5000, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E07', 'L', '2026-09-01T15:00:00Z', 'DEBIT', 4499.99, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E08', 'M', '2026-09-01T13:00:00Z', 'CREDIT', 6000, 'USD', 'CONFIRMED_OWN', 'POSTED', 'SD-E01;SD-E02'], ['E09', 'M', '2026-09-01T14:00:00Z', 'DEBIT', 5700, 'USD', 'CONFIRMED_OWN', 'POSTED', 'SD-E01;SD-E02'], ['E10', 'N', '2026-09-01T13:00:00Z', 'CREDIT', 5000, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E11', 'N', '2026-09-01T13:00:00Z', 'DEBIT', 4500, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E12', 'O', '2026-09-01T13:00:00Z', 'CREDIT', 5000, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01'], ['E13', 'O', '2026-09-01T14:00:00Z', 'DEBIT', None, 'USD', 'EXTERNAL', 'POSTED', 'SD-E01;SD-E03']]

events=[dict(zip(RAW_COLUMNS,row)) for row in RAW]
for r in events:
    if r['amount'] is not None:r['amount']=dec(r['amount'])
external=[r for r in events if r['ownership_state']=='EXTERNAL' and r['posting_state']=='POSTED']
anchors=[r for r in external if r['direction']=='CREDIT']
windows=[];account_seq=Counter()
for anchor in anchors:
    a=anchor['account_id'];account_seq[a]+=1;wid='W'+a+str(account_seq[a])
    start=instant(anchor['event_utc']);end=start+timedelta(hours=24)
    members=[r for r in external if r['account_id']==a and r['currency']==anchor['currency'] and start<=instant(r['event_utc'])<=end]
    c=total(members,'CREDIT');unknown=any(r['amount'] is None for r in members)
    d=None if any(r['direction']=='DEBIT' and r['amount'] is None for r in members) else total(members,'DEBIT')
    ratio=d/c if d is not None and c>0 else None
    subsequent=[instant(r['event_utc']) for r in members if r['direction']=='DEBIT' and instant(r['event_utc'])>start]
    hours=(min(subsequent)-start).total_seconds()/3600 if subsequent else None
    result='NOT_ASSESSABLE' if unknown else 'MATCH' if c>=5000 and ratio is not None and ratio>=dec('.9') and hours is not None and hours<=24 else 'NO_MATCH'
    refs='SD-E01;SD-E03;SD-E04' if unknown else 'SD-E01;SD-E04'
    windows.append([wid,a,anchor['event_id'],utc(start),utc(end),';'.join(r['event_id'] for r in members),float(c),numeric(d),numeric(ratio),hours,'AMOUNT_UNKNOWN' if unknown else 'COMPLETE',result,refs])
CHECKED_TABLES['WindowResults']=windows
coverage=[]
for a in sorted({r['account_id'] for r in events}):
    rows=[r for r in events if r['account_id']==a];ws=[r for r in windows if r[1]==a]
    own=all(r['ownership_state']=='CONFIRMED_OWN' for r in rows);unknown=any(r['amount'] is None for r in rows)
    state='CONFIRMED_OWN_EXCLUDED' if own else 'BLOCKED_UNKNOWN_DEBIT' if unknown else 'ASSESSED'
    refs='SD-E01;SD-E02' if own else 'SD-E01;SD-E03' if unknown else 'SD-E01;SD-E04'
    coverage.append([a,len(rows),float(total(rows,'CREDIT')),float(total(rows,'DEBIT')),len(ws),len(ws),state,refs])
CHECKED_TABLES['AccountCoverage']=coverage
reasons={'WJ1':'No earlier identical match; purpose unreviewed','WJ2':'Credit total below minimum despite ratio above one','WK1':'Exact 24-hour endpoint included','WL1':'4499.99 / 5000 below .90 before rounding','WN1':'No strictly subsequent debit','WO1':'Debit amount unknown; retain blocked window'}
delivery=[]
for w in windows:
    wid,a=w[:2];result=w[11]
    delivery.append(['DL-'+wid[1:],wid,result,'PROPOSED_FOR_REVIEW' if result=='MATCH' else 'DATA_REPAIR_QUEUE' if result=='NOT_ASSESSABLE' else 'NO_DELIVERY','G-'+wid[1:] if result=='MATCH' else None,reasons[wid],'NOT_RECORDED','SD-E03;SD-E04' if result=='NOT_ASSESSABLE' else 'SD-E01;SD-E04'])
CHECKED_TABLES['DeliveryDecisions']=delivery
assert len(events)==13 and len(windows)==6
assert Counter(w[11] for w in windows)=={'MATCH':2,'NO_MATCH':3,'NOT_ASSESSABLE':1}
assert total(events,'CREDIT')==31000 and total(events,'DEBIT')==dec('23699.99')
assert total(events,'CREDIT')+total(events,'DEBIT')==dec('54699.99')
assert sum(len(w[5].split(';')) for w in windows)==13
assert len({x for w in windows for x in w[5].split(';')})==11
assert dec('4499.99')/5000==dec('.899998')<dec('.9')
assert instant('2026-09-02T13:00:00Z')-instant('2026-09-01T13:00:00Z')==timedelta(hours=24)
assert not instant('2026-09-01T13:00:00Z')>instant('2026-09-01T13:00:00Z')
assert dec('4501')/5000==dec('.9002')

print("Fictional specimen arithmetic and boundary assertions passed.")
```
<!-- FIXTURE_CHECK:END -->
