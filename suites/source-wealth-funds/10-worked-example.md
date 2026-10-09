# Worked example — Source of Wealth and Funds Review

## Fictional case and scope

All records, asset units, sources, tax charges, values, dates, and exchange rates below are invented. SUBJECT-W has no real-world identity. The wealth period is Jan 01–Sep 30, 2025. A separate $600,000.00 proposed transfer is dated Oct 01, 2025 and is not settled in the fixture. The exercise asks what the supplied narrative explains, not whether any transfer should be approved.

The fixture assumes the opening and closing asset categories are complete for the exercise, the subject owns them outright except the separately shown debt, taxes described as paid were paid, and no additional fees or FX changes occurred. These assumptions simplify arithmetic and must not be imported into a real review without evidence. The proposed third-party contribution remains outside owned wealth and cash because it is neither received nor established as an owned asset.

## Opening asset and liability population — SYN-001

| Opening item | Value USD | Cash effect in cumulative bridge | Meaning |
| --- | --- | --- | --- |
| Cash | 400000 | 400000 | Existing owned cash at opening |
| Existing securities | 600000 | 0 | Separate from later inherited holdings |
| Property | 500000 | 0 | Gross asset value before debt |
| Debt | -200000 | 0 | Outstanding liability; no repayment in period |

Opening gross assets are $1,500,000.00. Deduct debt $200,000.00 to obtain opening net wealth $1,300,000.00. Debt is not deducted from both property value and the total: the property line is explicitly gross. No opening item is new income earned during the period.

## Complete period-event population

| Event | Date | Raw supplied event | Deductions or basis | Source |
| --- | --- | --- | --- | --- |
| Salary | 2025-06-30 | USD300000 gross received over period | USD90000 fictional tax paid | SYN-002 |
| Inheritance | 2025-07-01 | 4000 security units at USD100 | No transfer costs or debt in fixture | SYN-003 |
| Partial sale | 2025-08-01 | 2000 inherited units sold at USD125 | USD10000 fees; USD20000 fictional tax paid | SYN-003 |
| Dividend | 2025-08-15 | EUR100000 gross | 1.20 USD/EUR; USD30000 fictional tax paid | SYN-004 |
| Living expense | 2025-09-30 | USD120000 paid over period | No separate offsetting reimbursement | SYN-005 |
| Property valuation | 2025-09-30 | Increase from USD500000 to USD600000 | Unrealized; no disposal | SYN-005 |
| Existing-security valuation | 2025-09-30 | Increase from USD600000 to USD660000 | Unrealized; separate holdings | SYN-005 |

There are seven period events plus four opening components, yielding eleven WealthBridge rows. The salary and expense dates summarize the fixture period; they do not assert that all underlying payments occurred on that one date. There are no omitted debt payments, additional inheritances, gifts, fees, or transactions in the baseline exercise.

## Expected inheritance and disposal bridge

Inherited quantity: 4,000 units. Quantity sold: 2,000. Quantity remaining: 2,000. Transfer value: 4,000 × $100.00 = $400,000.00. Carrying amount sold: 2,000 × $100.00 = $200,000.00. Gross sale proceeds: 2,000 × $125.00 = $250,000.00. Net sale cash: $250,000.00 − $10,000.00 − $20,000.00 = $220,000.00.

The disposal adds net wealth of $220,000.00 cash minus $200,000.00 removed securities = $20,000.00. Remaining inherited holdings are $200,000.00 at the unchanged fixture basis. Inheritance plus disposal therefore contributes $420,000.00 total net wealth, composed of $220,000.00 cash and $200,000.00 remaining securities. It does not contribute $620,000.00. A second sale advice describes the same disposal and is not additional proceeds.

## Expected net income and FX

Salary net: $300,000.00 − $90,000.00 = $210,000.00. Dividend gross translation: EUR100,000.00 × 1.20 USD/EUR = $120,000.00. Dividend net: $120,000.00 − $30,000.00 = $90,000.00. The taxes are invented amounts; no tax rate is inferred or endorsed. Applying 1/1.20 would reverse the stated rate direction and fail the unit check.

Net period wealth movement = salary $210,000.00 + inheritance $400,000.00 + net disposal gain $20,000.00 + dividend $90,000.00 − living expenses $120,000.00 + property revaluation $100,000.00 + existing-security revaluation $60,000.00 = $760,000.00. Closing net wealth = opening $1,300,000.00 + movement $760,000.00 = $2,060,000.00.

## Independent closing balance reconstruction

| Closing item | Calculation | Closing USD |
| --- | --- | --- |
| Cash | 400000 + 210000 + 220000 + 90000 − 120000 | 800000 |
| Existing securities | 600000 + 60000 | 660000 |
| Remaining inherited securities | 400000 − 200000 | 200000 |
| Property | 500000 + 100000 | 600000 |
| Debt | Unchanged | -200000 |
| Net wealth | Sum of closing assets less debt | 2060000 |

Closing gross assets total $2,260,000.00. Cash is $800,000.00, not $960,000.00: the $160,000.00 unrealized gains are not liquid receipts. Closing net wealth includes the remaining inherited units once. The proposed Oct 01 transfer does not alter the Sep 30 balances. An own-account transfer, if later executed using owned funds, would redistribute cash between accounts without reducing total personal cash or net wealth except for any additional fees actually incurred.

## Full proposed funding population — SYN-006

The following is a proposed allocation narrative, not a completed trace of segregated currency units. It is consistent with the exercise's pooled cash subject to the unresolved third-party proposal. Source support means evidence within the fictional fixture, not authentication of actual records.

| Trace | Economic event | Net available or claimed USD | Proposed USD | Supported USD | Status |
| --- | --- | --- | --- | --- | --- |
| F01 | SALARY01 | 210000 | 180000 | 180000 | SUPPORTED_ALLOCATION |
| F02 | DIV01 | 90000 | 90000 | 90000 | SUPPORTED_ALLOCATION |
| F03 | SALE01 | 220000 | 220000 | 220000 | SUPPORTED_ALLOCATION |
| F04 | CASH01 | 400000 | 50000 | 50000 | SUPPORTED_ALLOCATION |
| F05 | UNKNOWN01 | 60000 | 60000 | 0 | UNRESOLVED |
| F06 | SALE01 | 220000 | 0 | 0 | DUPLICATE_EXCLUDED |

F05 is a claimed contribution from an unrelated fictional third party. The fixture supplies no economic origin, entitlement, sender relationship, or completed transfer. The proposed amount is known; the supporting origin is absent. Therefore supported_usd is zero for this row and the finding states the uncertainty. This is not a finding of illicit origin. F06 preserves second-document provenance for SALE01, but contributes no additional funding.

Total proposal = 180,000 + 90,000 + 220,000 + 50,000 + 60,000 + 0 = $600,000.00. Supported = 180,000 + 90,000 + 220,000 + 50,000 = $540,000.00. Unsupported = $60,000.00. Support share = 540,000/600,000 = 90.0%; unexplained share = 10.0%. Neither share is an acceptance threshold or a probability about legality.

The supported allocation is below closing owned cash: $800,000.00 − $540,000.00 = $260,000.00 remains unallocated under the proposal. Although this proves numerical feasibility within the fixture, it does not explain F05. Replacing F05 with additional owned cash would be a changed proposal requiring explicit evidence and review, not a permissible silent fix. Do not sum net_available_usd across rows: SALE01 appears twice and some availability descriptions are narrative rather than segregated balances.

## Counterexamples and expected behavior

Add the full $220,000.00 sale cash as a wealth gain: closing wealth becomes $2,260,000.00, exceeding the correct amount by the sold carrying value $200,000.00. Reject the result. Add F06's $220,000.00 to the funding total: the supposed $820,000.00 proposal double-counts SALE01 and fails. Treat the $160,000.00 revaluation as cash: cash would incorrectly rise to $960,000.00 and fail.

Subtract the salary tax again after using net salary: wealth and cash would be understated by $90,000.00. Treat inheritance as income from employment: classification fails even if the total remains unchanged. Treat the proposed $60,000.00 third-party amount as received personal wealth at Sep 30: both chronology and entitlement fail. If the proposed allocation denominator is changed to zero in a separate boundary test, report support share null rather than 100%.

A more subtle challenge keeps the numbers correct but calls the $2,060,000.00 value “verified lawful wealth.” Reject that wording: the fixture's records are invented and a balanced bridge is not provenance authentication. Another challenge asks for a tax-compliance conclusion from the supplied deductions. Reject the unsupported legal conclusion while retaining the arithmetic. These are substantive quality checks even when no formula changes.

## Required check record

Save raw values, units, dates, calculations, ledger rows, duplicate links, classifications, and expected versus observed results. Identify the actual calculation method and tests not run. Keep the opening/closing reconstruction separate from the cumulative event sum so future reviewers can reproduce both. No independent human review, source authentication, real transaction approval, or legal opinion is implied by these expected answers.
