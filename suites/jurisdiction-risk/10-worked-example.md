# Worked example — Jurisdiction Risk and Exposure Review

## Fictional case and cutoff

This is an invented transfer exposure review as of Sep 30, 2026. J-A, J-B, J-C, and J-D have no real-world counterparts. Their category assignments are fabricated solely to test analytical distinctions. The exercise is not a current list of countries, a sanctions screening result, or a legal conclusion. SYN-001 supplies four context snapshots dated Sep 15, 2026; SYN-002 supplies the complete eight-transfer ledger. All amounts are USD, so no currency conversion is used.

The primary question is beneficiary-jurisdiction concentration by value. The secondary question is the distinct route exposure to J-D. Both use the same eight economic events. The output should identify missing geography and the evidence needed to assess the fictional sector-related scope question. It cannot decide whether any transfer is lawful or any customer should be accepted.

## Full context population — SYN-001

| Jurisdiction | AML-context fixture category | Separate sanctions-scope fixture | Corruption-context fixture | Limitation |
| --- | --- | --- | --- | --- |
| J-A | NONE_IN_FIXTURE | NO_PROGRAM_QUESTION_IN_FIXTURE | Lower fictional concern | No absence-of-risk conclusion |
| J-B | INCREASED_MONITORING_FIXTURE | NO_PROGRAM_QUESTION_IN_FIXTURE | Moderate fictional concern | Category is distinct from sanctions |
| J-C | CALL_FOR_ACTION_FIXTURE | NO_PROGRAM_QUESTION_IN_FIXTURE | Higher fictional concern | Context needs applicable interpretation |
| J-D | NONE_IN_FIXTURE | SCOPE_REVIEW_REQUIRED | Moderate fictional concern | Fictional sector-related rule question unresolved |

NONE_IN_FIXTURE means the invented record supplies no category, not that an actual jurisdiction has no issues. NO_PROGRAM_QUESTION_IN_FIXTURE means no question is posed by this small fixture; it is not a completed sanctions clearance. The word “concern” is an illustrative descriptive category with no calibrated relationship to crime frequency.

## Full transfer population — SYN-002

Every row is included once in the total. There are no reversals, duplicates, fees, exchange differences, or excluded rows in the baseline.

| Transfer | Customer | Beneficiary jurisdiction | Intermediary jurisdiction | USD amount |
| --- | --- | --- | --- | --- |
| T01 | C01 | J-A | J-A | 100000 |
| T02 | C01 | J-B | J-A | 200000 |
| T03 | C02 | J-C | J-D | 150000 |
| T04 | C02 | J-B | J-A | 50000 |
| T05 | C03 | null | J-A | 100000 |
| T06 | C03 | J-D | J-A | 250000 |
| T07 | C04 | J-A | J-A | 50000 |
| T08 | C04 | J-C | J-A | 100000 |

T05's null is a missing beneficiary-country mapping, not a zero-valued payment. Its known intermediary location does not determine its beneficiary location. Four fictional customers appear; each has two transfers. Customer counts cannot replace the eight-transfer denominator in transaction frequency measures.

## Expected primary allocation

Total = 100,000 + 200,000 + 150,000 + 50,000 + 100,000 + 250,000 + 50,000 + 100,000 = $1,000,000.00. Known-destination amount = total minus T05 = $900,000.00. Mapping coverage by value = 900,000/1,000,000 = 90.0%. Mapping coverage by count = 7/8 = 87.5%. Both are correct and must have separate labels.

| Destination | Included IDs | USD value | Value share | Transfer count | Count share |
| --- | --- | --- | --- | --- | --- |
| J-A | T01, T07 | 150000 | 15.0% | 2 | 25.0% |
| J-B | T02, T04 | 250000 | 25.0% | 2 | 25.0% |
| J-C | T03, T08 | 250000 | 25.0% | 2 | 25.0% |
| J-D | T06 | 250000 | 25.0% | 1 | 12.5% |
| UNKNOWN | T05 | 100000 | 10.0% | 1 | 12.5% |

The five monetary buckets reconcile exactly to the total. The unknown bucket is an exposure data gap; it is not a fifth invented jurisdiction. J-D's mapped-only share is 250,000/900,000 = 27.777778%, displayed 27.8%. It may be shown as a separate descriptive statistic, but cannot be substituted for the 25.0% full-population share.

## Expected route and union arithmetic

J-D as intermediary: T03 = $150,000.00, or 15.0% of value. J-D as destination: T06 = $250,000.00, or 25.0%. For this particular fixture those sets do not overlap, so the union is $400,000.00, or 40.0%, across two of eight transfers. The general rule is still unique-ID union, not indiscriminate addition; a transfer with both roles would count once.

J-A as intermediary: T01,T02,T04,T05,T06,T07,T08 = $850,000.00. Its destination set T01,T07 is already inside that intermediary set. J-A any-nexus value therefore stays $850,000.00. Adding destination $150,000.00 would double count T01 and T07. This negative control deliberately tests overlap that J-D's baseline does not contain.

Any-nexus values by jurisdiction are J-A $850,000.00, J-B $250,000.00, J-C $250,000.00, and J-D $400,000.00. Their sum $1,750,000.00 is not the transfer total. It reflects overlapping role connections across a $1,000,000.00 population. A chart that adds those values must label them nonadditive or choose a different presentation.

## Sensitivity and category interpretation

If T05's destination were J-D, its destination amount would increase to $350,000.00 and 35.0%. If T05 belonged elsewhere, J-D remains $250,000.00 and 25.0%. This range describes a missing-data scenario with no assigned probabilities. J-D any-nexus would similarly range from $400,000.00 to $500,000.00 because T05 currently has only J-A as a known intermediary. Keep the observed baseline and hypothetical allocation separate.

J-B and J-C total $500,000.00 by destination, or 50.0%, across four transfers. Their categories are different and must first be reported separately. A combined measure may be called “destination value in the two selected fictional AML-context categories.” It must not be labelled sanctioned value, suspicious value, illicit value, or a 50.0% likelihood of money laundering. J-D's separate scope question is not erased by NONE_IN_FIXTURE in its AML field.

## Expected findings and counterexamples

JR-F01 identifies the $100,000.00 unmapped destination and proposes mapping repair. JR-F02 explains the role-dependent J-D values and overlap controls. JR-F03 identifies an unresolved fictional legal-scope question requiring transaction facts and appropriate authority. Each is a draft analytical finding. No blocking, approval, reporting, restriction, or customer exit occurs.

Change T03 destination to J-D in a separate test: its destination union with T06 becomes $400,000.00, and its any-nexus union is still $400,000.00 because T03 already touches J-D. A naive sum of destination plus intermediary would produce $550,000.00 and fail. Change T05 amount to zero in a test without evidence: reject the change because missing geography does not alter amount. Treat J-B's category as sanctions: reject the category substitution.

Add a reversal of T06 as a new source row in a different scenario: first declare gross activity versus net settlement and link the reversal to its economic event. Do not apply an unstated netting convention to reproduce the baseline total. Change T01 currency while keeping its numeric amount: the single-currency total no longer holds and must be qualified or converted with a supplied rate. These tests verify method boundaries rather than new customer facts.

## Actual-session record

Preserve every raw row, each source snapshot, role selection, inclusion rule, grouping, union membership set, and denominator in the checkpoint. Record actual observed test results separately from these expected answers. An unrun browser or workbook check remains NOT RUN. The example supports reproducibility of this method only; it cannot establish real sanctions coverage, current jurisdiction statuses, or a human disposition.
