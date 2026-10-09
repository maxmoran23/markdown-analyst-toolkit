# Typology and red flags: decision rules

## Indicator-state decision table

| First applicable condition | State | Required statement |
| --- | --- | --- |
| Defined indicator is outside the supported product/activity scope | NOT_APPLICABLE | Identify the exclusion and evidence supporting it. |
| Required event, identity, time, amount, or source completeness missing | INDETERMINATE | Name the missing prerequisite and the exact claim blocked. |
| Adequate evidence supports every element of the condition | PRESENT | State the measured value, criterion, and source events. |
| Adequate evidence covers the window and at least one element is false | ABSENT | State the failed element; limit the negative result to this indicator and period. |

Never translate INDETERMINATE to ABSENT for sorting, charts, or a combined score. NOT_APPLICABLE is also not a favorable risk observation: it means the chosen test does not apply. A reviewer can question the test selection or exclusion.

## Illustrative condition register

| ID | Required data | Positive condition | Ordinary explanation | Disconfirming evidence |
| --- | --- | --- | --- | --- |
| RF-01 | Complete external ledger, amounts, ordered times | Credit >= 5,000.00 USD; debit/credit >= 0.90; first subsequent debit <=24h | Supplier settlement, customer treasury activity | Matched purpose and parties; confirmed own transfer exclusion |
| RF-02 | Complete payer identity coverage | >=3 distinct payers in 24h | Collections, marketplace settlement | Only two independent payers; duplicates/aliases resolve to fewer |
| RF-03 | Original posted-event records and times | >=3 related posted payments in 24h | Installment settlement, separate purchases | Repeated descriptions refer to one event; pending/rejected instructions |
| RF-04 | Complete payee identity coverage | >=3 distinct payees in 24h | Payroll or disbursement operations | One payee; duplicate beneficiaries collapse |

These are detection illustrations. Do not replace an applicable current policy with them. None of the four conditions asserts illegality, intent, filing eligibility, or customer treatment. A known missing boundary day prevents a complete 24-hour assessment even if some events are visible.

## Hypothesis-review rules

PATTERN_ONLY means the indicator is observed while its economic explanation remains unresolved. BENIGN_SUPPORTED means a particular ordinary explanation has corroboration. PATTERN_NOT_MET means the selected pattern is absent within adequate scope. INSUFFICIENT_EVIDENCE means the observation cannot distinguish competing explanations. These labels are analytical descriptions and must not be displayed as “cleared,” “fraud,” or “criminal.”

Use HIGH priority for a supported urgent risk or a material coverage problem requiring immediate human attention under the applicable process. Use MEDIUM for a supported pattern without sufficient explanation or a material unresolved referral. Use LOW for bounded negative observations or supported ordinary explanations. Do not mechanically increase priority with the number of indicators. Explain why the fact matters and what further evidence is needed.

## Escalation and action boundary

An assistant may recommend that the authorized reviewer examine the case, obtain approved-source records, consider a parallel fraud or sanctions process, or repair an input defect. It cannot make those processes' final decisions. No indicator authorizes customer contact, transaction interdiction, a filing, an account restriction, or a public allegation. If a supplied fact suggests current harm, flag the urgency for the human operator without attempting external action.

Separate “request proposed” from “request sent” and “evidence requested” from “evidence obtained.” Do not report actions as executed merely because the recommendation sounds operational. A follow-up review begins with the actual new evidence, not an assumption that a recommended inquiry succeeded.

## Bias and scope controls

Use observable behavior and relevant product mechanics. Do not use protected attributes as evidence of suspicious conduct. Avoid unsupported proxies such as name, language, cultural practices, or neighborhood stereotypes. When geography is relevant, specify the actual transaction nexus, authoritative basis, effective date, and scope. A country label without a legal or risk criterion is not a complete rule.

When several sources share one origin, collapse them for corroboration assessment while preserving their individual locators. When two indicators share one factual premise, identify that dependence. The report should be able to state “one underlying pattern supports two observations” without implying independent confirmation.
