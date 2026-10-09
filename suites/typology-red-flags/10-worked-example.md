# Typology and red flags: complete fictional example

All cases and evidence are invented. Scope is a single complete day, 2026-09-01 12:00 AM ET through 2026-09-02 12:00 AM ET, end exclusive. A, B, and D have complete supplied event coverage for that day. C has only a referral. No actual person, service provider, or jurisdiction is identified.

## All six numeric transaction records

| event_id | case_id | time ET on Sep 01, 2026 | direction | amount USD | payer_id | payee_id | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E01 | A | 9:00 AM ET | CREDIT | 6000.00 | P01 | A | POSTED |
| E02 | A | 10:00 AM ET | CREDIT | 4000.00 | P02 | A | POSTED |
| E03 | A | 11:00 AM ET | DEBIT | 9500.00 | A | P03 | POSTED |
| E04 | B | 9:00 AM ET | CREDIT | 3000.00 | B-OWN-1 | B | POSTED |
| E05 | B | 10:00 AM ET | DEBIT | 3000.00 | B | B-OWN-2 | POSTED |
| E06 | D | 1:00 PM ET | DEBIT | 2000.00 | D | P04 | POSTED |

SYN-001 contains E01–E03 with complete-day coverage and no purpose documents. SYN-002 contains E04–E05 plus a fictional ownership confirmation effective throughout the period: B-OWN-1, B, and B-OWN-2 share the same owner. SYN-004 contains E06 with complete-day coverage and a payment narrative “invoice,” which is a stated purpose rather than independent invoice proof.

## Seventh source record: N01 / SYN-003

A fictional referral states: “Case C made three payments of 2,000.00 USD during one day.” The referral provides no transaction IDs, original ledger, posting status, actual date, or time. Its arithmetic describes a reported 6,000.00 USD, but neither event uniqueness nor execution is corroborated. This amount is excluded from observed monetary totals and retained only as a Reported claim.

Received source records: 7 = 7 processed source records + 0 duplicate + 0 excluded + 0 unparsed + 0 inaccessible + 0 deferred. Of the seven, six are canonical numeric transaction events and one is a narrative referral. Processing the referral does not convert it into three observed events. Five indicator tests are planned across four cases.

## Exact calculations

Observed gross movement = 6,000 + 4,000 + 9,500 + 3,000 + 3,000 + 2,000 = **27,500.00 USD**. This measure adds account credit and debit legs and is not unique funds, loss, or criminal proceeds. The reported 6,000.00 USD for C is not added.

A's credit total = 10,000.00 USD, debit total = 9,500.00 USD, ratio = 9,500/10,000 = **0.95**, elapsed first credit to subsequent debit = **2 hours**. RF-01 is PRESENT. Distinct payers are {P01, P02}; count **2**, below the illustrative threshold three, so RF-02 is ABSENT. Those observations share E01 and E02 and are not independent sources of corroboration.

B's confirmed own transfers are excluded from RF-01; state NOT_APPLICABLE and measured_value null. Do not insert 1.00 in a field intended for eligible external-flow ratio. C's original event count is unknown; RF-03 is INDETERMINATE and measured_value null. D has one distinct payee in the complete window, so RF-04 is ABSENT with measured_value 1.

## Expected IndicatorObservations

| observation_id | case_id | indicator_id | state | measured_value | unit | criterion | evidence_ids | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| O-01 | A | RF-01 | PRESENT | 0.95 | ratio | credit>=5000 USD; ratio>=0.90; elapsed<=24h | SYN-001 | Rapid movement pattern; purpose unresolved |
| O-02 | A | RF-02 | ABSENT | 2 | distinct_payers | at least 3 distinct payers | SYN-001 | Two payers; criterion not met |
| O-03 | B | RF-01 | NOT_APPLICABLE | null | ratio | exclude confirmed own transfers | SYN-002 | Ownership evidence supports limited exclusion |
| O-04 | C | RF-03 | INDETERMINATE | null | posted_events | at least 3 posted events in 24h | SYN-003 | Reported events lack transaction corroboration |
| O-05 | D | RF-04 | ABSENT | 1 | distinct_payees | at least 3 distinct payees in 24h | SYN-004 | One visible payment; complete stated window |

## Expected HypothesisReview

| case_id | concern_hypothesis | benign_hypothesis | support_state | next_evidence | priority | confidence | proposed_outcome |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | Unexplained rapid onward movement | Ordinary consolidated supplier settlement | PATTERN_ONLY | Purpose and counterparty records | MEDIUM | MODERATE | FURTHER_REVIEW |
| B | Concealed onward transfer | Movement between confirmed owned accounts | BENIGN_SUPPORTED | No extra inquiry for RF-01 on supplied facts | LOW | HIGH | DOCUMENT_LIMITED_EXCLUSION |
| C | Repeated related payments | Duplicate descriptions of one event | INSUFFICIENT_EVIDENCE | Original ledger and timestamps | MEDIUM | LOW | OBTAIN_SOURCE |
| D | Distribution across multiple beneficiaries | One ordinary invoice payment | PATTERN_NOT_MET | None for RF-04 within stated scope | LOW | HIGH | RECORD_NEGATIVE |

## Expected findings

RF-F01: MEDIUM severity, MODERATE confidence, Inferred. A presents a rapid-movement pattern while its many-to-one receipt test is negative. An ordinary supplier settlement remains plausible. Obtain purpose and counterparty evidence; do not infer laundering from the ratio alone.

RF-F02: MEDIUM severity, LOW confidence, Reported. C's repetition claim lacks original evidence. Obtain the underlying events and confirm identity, dates, and posting status. Do not count an unverified description as three transactions.

RF-F03: LOW severity, HIGH confidence, Observed. B's ownership evidence supports a limited exclusion; D fails the three-payee condition. Neither finding is a universal clearance of the relationship. Their role here is to demonstrate that the method can preserve valid negative and inapplicable results.

Observation totals are **1 PRESENT + 2 ABSENT + 1 INDETERMINATE + 1 NOT_APPLICABLE = 5**. Cases total **4**. The fraction PRESENT is 1/5 = 20.0% of planned observations, but that metric is only a description of this designed example and must not be presented as risk probability or model performance.

## Opposite and edge outcomes

If A receives an additional genuine 1,000.00 USD from P05, its payer count becomes three and RF-02 turns PRESENT. Its new ratio is 9,500/11,000 = 0.863636... = **86.4% displayed**, so RF-01 turns ABSENT on ratio. This prevents an assumption that all indicators move together.

If C's three descriptions are shown to reference one posted payment, RF-03 is ABSENT after complete coverage is established. If three distinct posted events within 24 hours are supplied, it becomes PRESENT, with purpose still requiring review. If D's extract is incomplete, RF-04 becomes INDETERMINATE for the full day. These changes alter only the affected observations and their dependent findings; retain prior versions and the reason for revision.
