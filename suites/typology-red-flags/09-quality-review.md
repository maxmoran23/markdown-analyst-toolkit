# Typology and red flags: quality review

## Falsifiable tests

| Test | Expected result | What failure reveals |
| --- | --- | --- |
| Population levels | 7 source records, 6 numeric transactions, 5 observations, 4 cases | Mixing documents, transactions, and indicators |
| Indicator state counts | PRESENT 1 + ABSENT 2 + INDETERMINATE 1 + NOT_APPLICABLE 1 = 5 | Hidden unknowns or duplicated observations |
| Event gross amount | E01–E06 sum to 27,500.00 USD | Inclusion of narrative-only amount or double counting |
| A ratio | 9,500 / 10,000 = 0.95 | Wrong direction or duplicated event |
| A payer count | 2 distinct payer identities | Confusion between rows and identities |
| C status | INDETERMINATE with measured_value null | Treating a referral claim as established events |
| B exclusion | Supported ownership record cited; no universal clearance | Overbroad benign inference |
| D negative | One payee, threshold three, complete stated window | Unsupported absence claim |
| Evidence classes | Ledger Observed; referral Reported; concern Inferred | Promotion of allegations to facts |

## Perturbation controls

Change A's second payer ID to its first payer ID: RF-02's count becomes one, not two. Add an exact duplicate copy of E02: canonical payer count and ratio stay unchanged. Add a third distinct genuine payer of 1,000.00 USD: RF-02 becomes PRESENT, while RF-01's ratio becomes 9,500/11,000 = 0.863636... and therefore ABSENT on its ratio criterion. This is a useful adversarial case: one indicator can strengthen while another weakens.

Remove the complete-window assurance for D: RF-04 becomes INDETERMINATE for the full proposed window, even though one visible payee remains observable. Supply C with three original 2,000.00 USD posted payments within 24 hours and distinct transaction IDs: RF-03 becomes PRESENT; it still does not establish intent or a predicate offense. Supply instead three copies of one transaction: it remains one event and the repeated-payment criterion is ABSENT if coverage is complete.

Remove B's ownership register: the limited exclusion is no longer supported. Do not assume the transfers are external or criminal; mark the ownership-dependent assessment INDETERMINATE until facts support an alternative evaluation. This tests whether the assistant preserves uncertainty instead of flipping directly from benign to suspicious.

## Review the strongest claim

Identify the sentence with the largest gap between evidence and conclusion. Ask which premise establishes identity, control, economic purpose, and intent. If a premise is unsupported, narrow the sentence. A transaction path may be observed while its economic purpose is unresolved. A concerning pattern may warrant inquiry without proving wrongdoing.

Review benign explanations with the same skepticism as concerning ones. Check whether an invoice actually matches the payment, whether ownership was effective at the event date, and whether an explanation covers all relevant events or only one. Do not accept a polished narrative because it is reassuring.

## Output and source review

Confirm every indicator criterion has a version and every source has a direct locator. Public guidance is contextual, not the authority for the example's numerical thresholds. Mark references not retrieved during the actual user session. Check that dashboard colors represent states without implying guilt. Unknown states must remain visible after filters, sorting, and export.

Trace one PRESENT, one ABSENT, one INDETERMINATE, and one NOT_APPLICABLE observation from output back to input. Confirm that a missing field remains null in the workbook, text report, and dashboard. Confirm the case count does not change when selecting multiple indicators for one case.

## Signoff

Record analyst, reviewer, timestamp, test IDs, expected/actual values, defects corrected, residual limitations, and release status. An assistant can document self-check results but cannot invent independent review. A reviewer may accept a limited inquiry recommendation while declining a stronger attribution claim. Keep those decisions separate.

Do not claim the indicator library is comprehensive for all products, jurisdictions, or criminal methods. A bounded passed example establishes that the supplied method behaved as specified on that example. It does not measure detection effectiveness, false-positive rates, or operational suitability.
