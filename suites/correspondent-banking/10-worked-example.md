# Correspondent Banking — complete fictional example

Every institution, license, agreement, identifier, payment and source below is invented. The correspondent is a generic fictional bank. All four respondent relationships are evaluated through Sep 10, 2026 5:00 PM ET. No onboarding, processing, restriction, exit, information request or filing occurs. All payment amounts are USD.

## Complete relationship inputs

| Profile | Evidence | Complete supplied facts |
| --- | --- | --- |
| CB01 Cedar Basin Bank | SYN-001 | Fictional license and staffed management-office facts dated Aug 31, 2026 are supplied. Agreement permits commercial payments and nested access for NB-01. A policy and a limited operating test cover that service. No broader effectiveness conclusion is supplied. |
| CB02 Delta Reach Bank | SYN-002 | Fictional license and questionnaire dated Aug 31, 2026 are supplied. Services are commercial and remittance payments; the questionnaire declares no nested access. Physical presence, affiliate status and operating-test evidence are not supplied. |
| CB03 Islet Digital Bank | SYN-003 | Fictional profile reports no separate physical presence. A dated legal-entity ownership record and supervisory statement support affiliation with a bank that has physical presence and consolidated supervision of the affiliate. Their legal sufficiency under an applicable exception remains a human question. Agreed service is own treasury payments; no nested access declared. |
| CB04 Orchard Plain Bank | SYN-004 | Fictional license, management-office facts and a scoped operating test are supplied. Agreed service is own treasury payments; no nested access declared. |

These are four supplied profile records, not public facts about actual banks. A supplied testing summary supports only its stated scope. Absence of a document from CB02's packet is an evidence gap, not proof the relevant control or office does not exist.

## Complete initial payment population

SYN-005 contains all ten unique payments below, dated Sep 01–08, 2026. The invented criterion requires originator name, originator identifier, beneficiary name and beneficiary identifier. A value YES means the field is present and usable within this fixture; NO means absent. No amount threshold or legal compliance claim is attached to that convention. All ten payments are supplied as settled; no return or cancellation records are included or implied.

| ID | Respondent | Underlying bank | USD amount | Originator name | Originator identifier | Beneficiary name | Beneficiary identifier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | CB01 | NONE_DECLARED | 100000 | YES | YES | YES | YES |
| P02 | CB01 | NB-01 | 50000 | YES | NO | YES | YES |
| P03 | CB01 | NB-01 | 25000 | YES | YES | YES | YES |
| P04 | CB01 | NONE_DECLARED | 25000 | YES | YES | YES | YES |
| P05 | CB02 | NB-02 | 60000 | YES | NO | YES | YES |
| P06 | CB02 | NB-02 | 40000 | YES | YES | YES | YES |
| P07 | CB02 | NONE_DECLARED | 20000 | YES | YES | YES | NO |
| P08 | CB03 | NONE_DECLARED | 30000 | YES | YES | YES | YES |
| P09 | CB03 | NONE_DECLARED | 70000 | YES | YES | YES | YES |
| P10 | CB04 | NONE_DECLARED | 80000 | YES | YES | YES | YES |

The supplied message-role annotation expressly identifies NB-01 and NB-02 as downstream banks obtaining access through their respondent, not merely beneficiary banks. P01, P04 and P07 are direct customer payments. P08, P09 and P10 are respondent own-treasury payments. No payable-through access is evidenced. No agreement authorizing NB-02 before the payment dates is supplied.

Repair R01, SYN-006: Sep 09, 2026 11:00 AM ET, a linked and verified replacement field supplies P02's originator identifier. It changes no amount, party or payment ID. It is the only repair supplied through cutoff. No repair for P05 or P07 is evidenced.

## Population reconciliation and exact arithmetic

Source records received = 4 profiles + 10 initial payment rows + 1 repair = 15. Processed = 15; ingestion duplicates, exclusions, unparsed, inaccessible received records and deferred records are all zero. Payment records = 10 unique economic payments; R01 is a lifecycle update and does not create an eleventh payment.

CB01 value = 100,000 + 50,000 + 25,000 + 25,000 = USD 200,000.00. CB02 = 60,000 + 40,000 + 20,000 = USD 120,000.00. CB03 = 30,000 + 70,000 = USD 100,000.00. CB04 = USD 80,000.00. Total = 200,000 + 120,000 + 100,000 + 80,000 = USD 500,000.00.

Initial missing-field payments are P02, P05 and P07: count 3/10 = 30.0%; value 50,000 + 60,000 + 20,000 = USD 130,000.00; value rate 130,000/500,000 = 26.0%. After R01, open gaps are P05 and P07: count 2/10 = 20.0%; value USD 80,000.00; value rate 80,000/500,000 = 16.0%. The repair changes the current count rate by 10.0 percentage points, not 10.0 percent relative. Relative count reduction is 1/3 = 33.3%.

Nested payments are P02, P03, P05 and P06: count 4/10 = 40.0%; value 50,000 + 25,000 + 60,000 + 40,000 = USD 175,000.00; value share 35.0%. Disclosed NB-01 value is USD 75,000.00. Undeclared-at-time NB-02 value is USD 100,000.00. Only P05 overlaps the open-gap and undeclared-nested sets. Their union is P05, P06 and P07 totaling USD 120,000.00, not the incorrect USD 180,000.00 obtained by adding overlapping subtotals.

## Expected table states and findings

RelationshipReview: CB01 LIMITED_SUPPORT, CB02 FOLLOW_UP, CB03 LEGAL_CLASSIFICATION_REVIEW, CB04 LIMITED_SUPPORT. These are evidence assessments, not approvals. PaymentReview: P02 REPAIRED; P05 and P07 GAP_OPEN; all other payments COMPLETE under the illustrative criterion. Nested state is DISCLOSED for P02/P03, UNDECLARED_OBSERVED for P05/P06 and NOT_INDICATED for the others.

CB-F01 is HIGH severity and HIGH confidence for the observed CB02 agreement/message inconsistency and absent fields. Deliberate concealment is not established. CB-F02 is MEDIUM severity and HIGH confidence for the historical P02 defect and repair. CB-F03 is MEDIUM severity and MODERATE confidence for the need to classify the supplied affiliate facts under applicable law. CB-F04 is LOW severity and HIGH confidence for the bounded ordinary treasury control.

CB02 needs specific follow-up, not a blanket conclusion about remittance businesses. CB03 must not be labeled prohibited solely because separate physical presence is absent; it also must not be called approved merely because an affiliation record exists. CB04 remains in every denominator despite its benign interpretation. All actions are Proposed and human disposition is NOT REVIEWED.

## Negative-control variations

Remove R01: current gap count becomes three and current gap value becomes USD 130,000.00; initial metrics are unchanged. Duplicate P05 with the same immutable ID: received raw rows increase but unique payments and value remain ten and USD 500,000.00 after supported deduplication. Add a later NB-02 authorization: preserve historical undeclared status and separately assess the later period. Reclassify P06 as an ordinary bank-beneficiary payment with actual role evidence: nested value falls by USD 40,000.00, while its payment amount remains in the full population. Record the changed evidence and actual recomputation, not just the expected answer.

## Separate unresolved-role negative case

Run this variant in a copy of the baseline; it does not alter the catalog specimen or its original totals. Replace only the SYN-005 role annotation for P06 with this complete fictional statement: "P06 identifies NB-02 in a bank field, but the supplied extract omits its role code. NB-02 may be an ordinary bank beneficiary or a downstream access user. No other agreement or message evidence resolves the role." All four identity fields remain present, the amount remains USD 40,000.00, and every other baseline input and the P02 repair remain unchanged. Label the replacement SYN-005-U and retain its locator as this paragraph plus the original P06 input row; claim class Observed describes the incomplete extract, not nested use.

Expected replacement PaymentReview row, in the exact 05 column order:

| payment_id | respondent_id | underlying_bank_id | amount | currency | initial_missing | cutoff_missing | nested_state | review_state | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P06 | CB02 | NB-02 | 40000 | USD | NONE | NONE | UNRESOLVED | COMPLETE | SYN-005-U |

Add SYN-005-U to the variant's Evidence register as: id SYN-005-U; title Fictional P06 incomplete role extract; locator 10-worked-example.md, Separate unresolved-role negative case and original P06 row; claim_class Observed. Preserve the original source as superseded for this proposition, and update any variant finding that claimed two confirmed undeclared payments.

Recomputed variant results: ten payments and USD 500,000.00 remain in the full population. Confirmed nested payments are P02, P03 and P05, count 3 and value 50,000 + 25,000 + 60,000 = USD 135,000.00, or 27.0% of total value. P06 is a separate unresolved count of 1 and USD 40,000.00, or 8.0% of total value. Confirmed undeclared-at-time value is now only P05, USD 60,000.00. Six other payments have NOT_INDICATED roles. The state counts reconcile as 3 confirmed nested + 1 unresolved + 6 NOT_INDICATED = 10; the six are P01, P04, P07, P08, P09 and P10. Initial and cutoff missing-field metrics do not change because role uncertainty is a separate test. The human request should seek the missing role evidence; no blanket adverse or favorable disposition follows.
