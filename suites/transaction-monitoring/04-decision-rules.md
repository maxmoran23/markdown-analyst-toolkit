# Transaction monitoring: rules and escalation

## Deterministic rule states

Evaluate the rows below in order. A blocking data defect takes precedence over a numerical match when it can change the account-window result. A confirmed scenario exclusion applies only to the relevant records, not automatically to the account's other activity.

| Rule | Exact condition | Result | Required treatment |
| --- | --- | --- | --- |
| TM-DQ | Required amount, direction, time, identity, or scope unresolved | NOT_ASSESSABLE | Preserve partial totals; request source correction and recompute. |
| TM-EX | All otherwise relevant activity is confirmed own-account transfer | EXCLUDED | Record ownership evidence; retain gross movement. |
| TM-DEN | No eligible credit; data otherwise complete | NO_MATCH with ratio null | Do not divide by zero or imply absence of other risks. |
| TM-01 | Eligible credit total >= 5,000.00 USD; debit/credit >= 0.90; first subsequent debit <= 24 hours | MATCH | Contextual review required. |
| TM-NEG | Complete eligible data and any TM-01 criterion false | NO_MATCH | Record failed criterion and negative-control comparison. |

A numerical hit remains a hit after an explanation. Do not edit threshold values to justify a preferred disposition. If an account has both known own transfers and third-party payments, exclude only the supported own legs and evaluate the remainder. If ownership is unknown, mark it unknown and evaluate sensitivity rather than assume the favorable exclusion.

## Review states are separate from rule states

| Evidence pattern | Proposed review outcome | Benign explanation to test | Escalation route |
| --- | --- | --- | --- |
| Match; payment purpose unsupported; profiles inconsistent with observed pattern | ESCALATE_FOR_REVIEW | Timing of settlement, genuine purchases, documented treasury arrangements | Authorized monitoring reviewer |
| Match; independently matched ordinary-business documentation | EXPLANATION_SUPPORTED | Confirm document covers the actual parties, amount, and event | Human disposition with retained trigger |
| Relevant missing amount or incomplete lookback | DATA_REPAIR_REQUIRED | Extract defect or delayed ingestion | Data owner and monitoring reviewer |
| Own transfer with reliable identity linkage | OWN_TRANSFER_CONFIRMED | Internal liquidity movement | Reviewer confirms limited exclusion |
| Complete data; criterion not met | NO_MATCH_RECORDED | Other scenarios may still be relevant | Normal review process; no automatic clearance |

Severity expresses impact of the identified condition. HIGH covers a material coverage defect that can hide activity or an urgent review need supported by the facts. MEDIUM covers unexplained scenario matches requiring further evidence. LOW covers a supported explanation or bounded documentation issue. These are analytical priorities, not regulatory materiality definitions. If actual urgency falls outside the template's scale, state the urgent fact in words and route to the designated human immediately within approved procedures; the assistant does not contact anyone.

Confidence is HIGH when the specific claim is directly supported and reconciled; MODERATE when important context is unresolved; LOW when evidence is indirect or contradictory; NOT ASSESSABLE when the proposition cannot be evaluated. High confidence that a data defect exists says nothing about whether a customer is suspicious.

## Decisions reserved for humans

No match, score, ratio, or severity label authorizes a SAR, a hold, account closure, rule deployment, threshold suppression, customer contact, or a change to a customer risk rating. Do not embed a filing conclusion in a spreadsheet formula. Provide the reviewer with criterion provenance, supporting facts, alternative explanations, missing facts, timing concerns, and the proposed next step.

If local policy is supplied in an approved environment, identify its version and effective date, map each action to the exact provision, and record conflicts with this illustrative method. Apply the controlling policy only within the user's authority and applicable restrictions. Never treat a policy screenshot as proof that the current version has been verified.

## Threshold sensitivity and fairness

Changing a threshold may redistribute review effort across products and customer groups. Evaluate activity mechanics and measurable risk drivers; do not use protected traits or name-based geography guesses. Show affected populations and data availability before comparing alert rates. Do not label a group inherently suspicious because it has more alerts. A rule's alert burden may reflect a mismatched baseline or poor data.

For a counterfactual test, change only one parameter at a time while holding the reconciled population fixed. Record matches gained and lost, including explained and unreviewed matches. Keep exclusions and incomplete cases in the denominator disclosure. A clean negative control must stay negative for the reason designed, not because a missing value silently became zero.
