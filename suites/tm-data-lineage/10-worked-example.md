# Transaction Monitoring Data Lineage: complete fictional case and alternate controls

All feeds, accounts and evidence declarations are fictional. Economic event scope is Sep 01, 2026 12:00 AM ET inclusive through Sep 02, 2026 12:00 AM ET exclusive. RUN0 ingestion cutoff is Sep 02, 2026 12:00 AM ET (04:00Z), inclusive. RUN1 cutoff is Sep 02, 2026 8:00 AM ET (12:00Z), inclusive. The later-delivered review package contains fifteen rows and deliberately includes X12, which RUN0 did not yet have. Reproduction therefore distinguishes historical run visibility from the later reviewer's knowledge of a missing event.

LN-E01 comprises SourceRows X01-X15 and the supplied scope/cutoff declarations. LN-E02 declares that X06 and X07 share the same LC/TX05/version-1 economic identity and disagree on amount; neither is authoritative. LN-E03 links X11 to X10 as an exact USD 3000 posted reversal at LE. This authored external-flow example excludes the validated pair while retaining its posting history; another monitoring design might assess reversals separately. LN-E04 confirms X12's event time and later ingestion and the RUN1 receipt. LN-E05 states X14's posted credit amount is unreadable. LN-E06 supplies every FieldMappings transformation and the downstream illustrative daily TM-01 rule: USD credits at least 5000, debit/credit at least .90 and a subsequent debit within 24 elapsed hours; relevant source defects precede numeric classification.

The initial terminal equation is fifteen rows = seven canonical + one duplicate + two conflicting rows + one pending + two reversal-pair rows + one late-deferred + one unparsed. The conflicting rows represent one unresolved economic identity. Initial canonical rows are X01, X02, X04, X05, X08, X13 and X15. The USD canonical credits are 6000 + 5000 = 11000; debits are 5400 + 4500 + 1000 + 3600 = 14500; known gross is 25500. X15 remains EUR 1000 and is not added to USD. Raw USD known credits are 35200 and debits 17500, gross 52700, but this raw control includes duplicates, alternatives, pending and reversal entries and is not canonical economic movement.

RUN1 adds only X12 USD 4000 credit. Canonical rows rise from seven to eight; known USD credits from 11000 to 15000; debits remain 14500; gross rises by 4000 to 29500. EUR remains 1000. LF's credit/debit sequence is 30 minutes: 7:30 PM ET credit and 8:00 PM ET debit on Sep 01. The repaired .90 ratio passes, but USD 4000 credits fail the USD 5000 minimum, so LF changes from NOT_ASSESSABLE to NO_MATCH. LA and LB remain matches. LC conflict and LG unreadable amount remain blocked. LD has no posted activity; LE is a documented reversal-pair exclusion; LH is outside the USD rule with EUR source retained.

## Complete populated source and expected result registers

All rows below belong to the baseline. They are printed in full so the assistant can reproduce the case without importing any repository file. The later alternate controls are independent perturbations and must not be added to these baseline counts or monetary totals.

### SourceRows

Grain: one immutable raw delivered feed record, including later-unavailable and exceptional records.

| raw_row_id | transaction_id | account_id | event_utc | ingest_utc | source_direction | amount_text | currency | source_status | source_version | reversal_of | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X01 | TX01 | LA | 2026-09-01T13:00:00Z | 2026-09-01T13:05:00Z | C | 6000.00 | USD | P | 1 | null | LN-E01 |
| X02 | TX02 | LA | 2026-09-01T14:00:00Z | 2026-09-01T14:05:00Z | D | 5400.00 | USD | P | 1 | null | LN-E01 |
| X03 | TX01 | LA | 2026-09-01T13:00:00Z | 2026-09-01T15:00:00Z | C | 6000.00 | USD | P | 1 | null | LN-E01 |
| X04 | TX03 | LB | 2026-09-01T13:00:00Z | 2026-09-01T13:05:00Z | C | 5000.00 | USD | P | 1 | null | LN-E01 |
| X05 | TX04 | LB | 2026-09-01T14:00:00Z | 2026-09-01T14:05:00Z | D | 4500.00 | USD | P | 1 | null | LN-E01 |
| X06 | TX05 | LC | 2026-09-01T13:00:00Z | 2026-09-01T13:05:00Z | C | 2000.00 | USD | P | 1 | null | LN-E01 |
| X07 | TX05 | LC | 2026-09-01T13:00:00Z | 2026-09-01T13:06:00Z | C | 2200.00 | USD | P | 1 | null | LN-E01;LN-E02 |
| X08 | TX06 | LC | 2026-09-01T14:00:00Z | 2026-09-01T14:05:00Z | D | 1000.00 | USD | P | 1 | null | LN-E01 |
| X09 | TX07 | LD | 2026-09-01T13:00:00Z | 2026-09-01T13:05:00Z | C | 7000.00 | USD | N | 1 | null | LN-E01 |
| X10 | TX08 | LE | 2026-09-01T13:00:00Z | 2026-09-01T13:05:00Z | C | 3000.00 | USD | P | 1 | null | LN-E01 |
| X11 | TX09 | LE | 2026-09-01T14:00:00Z | 2026-09-01T14:05:00Z | D | 3000.00 | USD | R | 1 | TX08 | LN-E01;LN-E03 |
| X12 | TX10 | LF | 2026-09-01T23:30:00Z | 2026-09-02T10:00:00Z | C | 4000.00 | USD | P | 1 | null | LN-E01;LN-E04 |
| X13 | TX11 | LF | 2026-09-02T00:00:00Z | 2026-09-02T00:05:00Z | D | 3600.00 | USD | P | 1 | null | LN-E01 |
| X14 | TX12 | LG | 2026-09-01T13:00:00Z | 2026-09-01T13:05:00Z | C | unreadable | USD | P | 1 | null | LN-E01;LN-E05 |
| X15 | TX13 | LH | 2026-09-01T13:00:00Z | 2026-09-01T13:05:00Z | C | 1000.00 | EUR | P | 1 | null | LN-E01 |

### FieldMappings

Grain: one explicit source-to-canonical transformation with its failure branch.

| mapping_id | source_field | target_field | transformation | failure_state | test_locator | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| MAP01 | transaction_id + account_id + source_version | canonical identity | Exact text tuple; currency and amount are compared payload, not identity | CONFLICT if same tuple differs | X06 and X07 | LN-E06 |
| MAP02 | event_utc | event instant | Parse timezone-aware ISO timestamp; normalize UTC without changing instant | UNPARSED_TIME | X12 and X13 are previous ET business date | LN-E06 |
| MAP03 | source_direction | direction | C -> CREDIT; D -> DEBIT; no other mapping | UNMAPPED_DIRECTION | X01 C; X02 D | LN-E06 |
| MAP04 | amount_text | amount | Decimal nonnegative; retain original string; no thousands separator guessing | UNPARSED_AMOUNT | X14 unreadable | LN-E06 |
| MAP05 | source_status | posting_state | P -> POSTED; N -> PENDING; R -> REVERSAL_POSTED | UNMAPPED_STATUS | X09 pending; X11 linked reversal | LN-E06 |
| MAP06 | currency | currency | Preserve uppercase ISO code; no conversion in this case | UNKNOWN_CURRENCY | X15 EUR stays EUR | LN-E06 |
| MAP07 | reversal_of | reversal link | Resolve original same-account transaction and exact amount/currency before paired exclusion | UNRESOLVED_REVERSAL | X11 refers TX08 at LE, USD 3000 | LN-E03;LN-E06 |
| MAP08 | ingest_utc | cutoff eligibility | Include if ingest instant <= run cutoff; apply event scope separately | LATE_DEFERRED | X12 appears only in rerun | LN-E04;LN-E06 |

### LineageLedger

Grain: one raw source row and its initial RUN0 terminal disposition.

| lineage_id | raw_row_id | canonical_id | terminal_state | reason | run_id | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| LIN-X01 | X01 | CL01 | CANONICAL | Unique readable posted leg available by initial cutoff | RUN0 | LN-E01;LN-E06 |
| LIN-X02 | X02 | CL02 | CANONICAL | Unique readable posted leg available by initial cutoff | RUN0 | LN-E01;LN-E06 |
| LIN-X03 | X03 | CL01 | DUPLICATE | Same economic tuple and payload as X01; later extraction metadata only | RUN0 | LN-E01;LN-E06 |
| LIN-X04 | X04 | CL03 | CANONICAL | Unique readable posted leg available by initial cutoff | RUN0 | LN-E01;LN-E06 |
| LIN-X05 | X05 | CL04 | CANONICAL | Unique readable posted leg available by initial cutoff | RUN0 | LN-E01;LN-E06 |
| LIN-X06 | X06 | null | CONFLICT | Same TX05 identity; conflicting amount; neither selected | RUN0 | LN-E01;LN-E06 |
| LIN-X07 | X07 | null | CONFLICT | Same TX05 identity; conflicting amount; neither selected | RUN0 | LN-E01;LN-E02;LN-E06 |
| LIN-X08 | X08 | CL05 | CANONICAL | Unique readable posted leg available by initial cutoff | RUN0 | LN-E01;LN-E06 |
| LIN-X09 | X09 | null | PENDING | Not posted at supplied status; retain outside posted ledger | RUN0 | LN-E01;LN-E06 |
| LIN-X10 | X10 | null | REVERSAL_PAIR | Exact linked original and reversal preserved but netted out of external-flow scenario | RUN0 | LN-E01;LN-E06 |
| LIN-X11 | X11 | null | REVERSAL_PAIR | Exact linked original and reversal preserved but netted out of external-flow scenario | RUN0 | LN-E01;LN-E03;LN-E06 |
| LIN-X12 | X12 | null | LATE_DEFERRED | Event in period, ingestion after initial cutoff; add only in rerun | RUN0 | LN-E01;LN-E04;LN-E06 |
| LIN-X13 | X13 | CL06 | CANONICAL | Unique readable posted leg available by initial cutoff | RUN0 | LN-E01;LN-E06 |
| LIN-X14 | X14 | null | UNPARSED_AMOUNT | Posted amount cannot be recovered; LG blocked | RUN0 | LN-E01;LN-E05;LN-E06 |
| LIN-X15 | X15 | CL07 | CANONICAL | Unique readable posted leg available by initial cutoff | RUN0 | LN-E01;LN-E06 |

### CanonicalOutput

Grain: one known unique posted account leg available at RUN0 and surviving declared exclusions.

| canonical_id | raw_row_id | transaction_id | account_id | event_utc | direction | amount | currency | run_id | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CL01 | X01 | TX01 | LA | 2026-09-01T13:00:00Z | CREDIT | 6000.0 | USD | RUN0 | LN-E01 |
| CL02 | X02 | TX02 | LA | 2026-09-01T14:00:00Z | DEBIT | 5400.0 | USD | RUN0 | LN-E01 |
| CL03 | X04 | TX03 | LB | 2026-09-01T13:00:00Z | CREDIT | 5000.0 | USD | RUN0 | LN-E01 |
| CL04 | X05 | TX04 | LB | 2026-09-01T14:00:00Z | DEBIT | 4500.0 | USD | RUN0 | LN-E01 |
| CL05 | X08 | TX06 | LC | 2026-09-01T14:00:00Z | DEBIT | 1000.0 | USD | RUN0 | LN-E01 |
| CL06 | X13 | TX11 | LF | 2026-09-02T00:00:00Z | DEBIT | 3600.0 | USD | RUN0 | LN-E01 |
| CL07 | X15 | TX13 | LH | 2026-09-01T13:00:00Z | CREDIT | 1000.0 | EUR | RUN0 | LN-E01 |

### StageControls

Grain: one pipeline layer, run and currency control population.

| control_id | stage | currency | row_count | known_credit_total | known_debit_total | unknown_amount_count | interpretation | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LC01 | Delivered raw | USD | 14 | 35200 | 17500 | 1 | Raw contains duplicate, conflicting alternatives, pending and reversal; not economic total | LN-E01 |
| LC02 | Delivered raw | EUR | 1 | 1000 | 0 | 0 | Separate currency; not added to USD | LN-E01 |
| LC03 | RUN0 canonical | USD | 6 | 11000 | 14500 | 0 | Known partial posted population; LC conflict, LF late, LG unknown remain blocked | LN-E01;LN-E06 |
| LC04 | RUN0 canonical | EUR | 1 | 1000 | 0 | 0 | Preserved EUR leg; USD scenario exclusion separately disclosed | LN-E01;LN-E06 |
| LC05 | RUN1 canonical | USD | 7 | 15000 | 14500 | 0 | Adds X12 USD 4000 credit; unresolved conflict and parse defect remain | LN-E04;LN-E06 |
| LC06 | RUN1 canonical | EUR | 1 | 1000 | 0 | 0 | EUR unchanged | LN-E01;LN-E06 |

### RunImpact

Grain: one account and currency compared across RUN0 and RUN1.

| impact_id | account_id | currency | run0_credit | run0_debit | run0_state | run1_credit | run1_debit | run1_state | change_reason | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IMP-A | LA | USD | 6000 | 5400 | MATCH | 6000 | 5400 | MATCH | No source change | LN-E01;LN-E06 |
| IMP-B | LB | USD | 5000 | 4500 | MATCH | 5000 | 4500 | MATCH | No source change | LN-E01;LN-E06 |
| IMP-C | LC | USD | 0 | 1000 | NOT_ASSESSABLE | 0 | 1000 | NOT_ASSESSABLE | TX05 conflict unresolved; credit zero means known subtotal only | LN-E02;LN-E06 |
| IMP-D | LD | USD | 0 | 0 | NO_POSTED_ACTIVITY | 0 | 0 | NO_POSTED_ACTIVITY | Pending source retained; no posted leg | LN-E01;LN-E06 |
| IMP-E | LE | USD | 0 | 0 | REVERSAL_PAIR_EXCLUDED | 0 | 0 | REVERSAL_PAIR_EXCLUDED | Original and reversal retained outside illustrative flow totals | LN-E03;LN-E06 |
| IMP-F | LF | USD | 0 | 3600 | NOT_ASSESSABLE | 4000 | 3600 | NO_MATCH | Late credit repaired; ratio .90 but 4000 below illustrative 5000 minimum | LN-E04;LN-E06 |
| IMP-G | LG | USD | 0 | 0 | NOT_ASSESSABLE | 0 | 0 | NOT_ASSESSABLE | Unknown posted credit remains; zeros are known subtotals | LN-E05;LN-E06 |
| IMP-H | LH | EUR | 1000 | 0 | CURRENCY_EXCLUDED | 1000 | 0 | CURRENCY_EXCLUDED | USD-only rule; EUR preserved in lineage | LN-E01;LN-E06 |

### ExceptionRegister

Grain: one specific defect or documented controlled treatment and its repair evidence.

| exception_id | account_id | source_rows | exception_type | affected_claim | required_evidence | repair_state | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EX01 | LC | X06;X07 | CONFLICT | Credit amount and LC rule outcome | Authoritative TX05 version history and amount; do not choose maximum | OPEN | LN-E02 |
| EX02 | LF | X12 | LATE_ARRIVAL | Initial completeness and LF timing | RUN1 ingest receipt and complete lag population | RERUN_REPRODUCED | LN-E04 |
| EX03 | LG | X14 | UNPARSED_AMOUNT | Credit total and LG rule outcome | Corrected signed source extract and source amount control | OPEN | LN-E05 |
| EX04 | LE | X10;X11 | REVERSAL_TREATMENT | Difference between posting gross and illustrative external flow | Exact reversal link, currency and amount, plus stated exclusion convention | DOCUMENTED_ONLY | LN-E03;LN-E06 |

### EvidenceProvenance

Grain: one fictional evidence source with its access state and evidential limit.

| evidence_id | source_kind | source_date | availability | locator | supports | limitation |
| --- | --- | --- | --- | --- | --- | --- |
| LN-E01 | Authored fictional case record | 2026-09-02 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, SourceRows X01-X15; source manifest | Fictional delivered feed | Supports only the stated fictional proposition; no external subject fact or institutional approval |
| LN-E02 | Authored fictional case record | 2026-09-02 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, TX05 conflict declaration | Fictional conflict notice | Supports only the stated fictional proposition; no external subject fact or institutional approval |
| LN-E03 | Authored fictional case record | 2026-09-02 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, TX08/TX09 reversal declaration | Fictional exact reversal link | Supports only the stated fictional proposition; no external subject fact or institutional approval |
| LN-E04 | Authored fictional case record | 2026-09-02 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, X12 cutoff declaration and RUN1 receipt | Fictional late-arrival notice | Supports only the stated fictional proposition; no external subject fact or institutional approval |
| LN-E05 | Authored fictional case record | 2026-09-02 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, X14 parse-defect declaration | Fictional unreadable amount | Supports only the stated fictional proposition; no external subject fact or institutional approval |
| LN-E06 | Authored fictional case record | 2026-09-02 | FULL_TEXT_IN_FILE_10 | 10-worked-example.md, FieldMappings, run cutoffs and illustrative TM-01 predicates | Authored transformation and downstream rule | Supports only the stated fictional proposition; no external subject fact or institutional approval |

### ProcessQA

Grain: one performed or explicitly unrecorded quality proposition.

| check_id | check | expected | actual | status | reviewer | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| LQ01 | Initial terminal conservation | 15 = 7 + 1 + 2 + 1 + 2 + 1 + 1 | 15 = 7 + 1 + 2 + 1 + 2 + 1 + 1 | PASS | Authored specimen arithmetic; independent operational reviewer not supplied | LN-E01;LN-E06 |
| LQ02 | RUN1 known USD gross | 29500.00 | 29500.00 | PASS | Authored specimen arithmetic; independent operational reviewer not supplied | LN-E01;LN-E04 |
| LQ03 | Distinct currencies | USD and EUR separate | USD and EUR separate | PASS | Authored specimen arithmetic; independent operational reviewer not supplied | LN-E01 |
| LQ04 | Conflict not selected | X06 and X07 both quarantined | X06 and X07 both quarantined | PASS | Authored specimen arithmetic; independent operational reviewer not supplied | LN-E02 |
| LQ05 | Independent acceptance | Not supplied | Not supplied | NOT RECORDED | Authored specimen arithmetic; independent operational reviewer not supplied | LN-E06 |

## Full finding and action specimen

### LN-F01: Conflicting versions block LC

Severity `HIGH`; confidence `HIGH`; claim class `Observed`; evidence `LN-E01;LN-E02`. X06 and X07 share the TX05 identity but disagree between USD 2000 and USD 2200; neither is selected. LC remains not assessable. Proposed next step: Obtain an authoritative version history, resolve TX05 and rerun every affected window. Human disposition is NOT_RECORDED; no external action is represented as executed. The rationale concerns this specific observed condition, not a broader allegation or certification.

### LN-F02: Known late credit changes LF assessment

Severity `MEDIUM`; confidence `HIGH`; claim class `Observed`; evidence `LN-E01;LN-E04;LN-E06`. RUN1 adds X12 USD 4000 credit. LF changes from not assessable to no match because .90 satisfies the ratio but USD 4000 fails the credit minimum. Proposed next step: Preserve RUN0 and RUN1 and verify the wider lag population before accepting complete coverage. Human disposition is NOT_RECORDED; no external action is represented as executed. The rationale concerns this specific observed condition, not a broader allegation or certification.

### LN-F03: Unreadable posted credit remains unresolved

Severity `HIGH`; confidence `HIGH`; claim class `Observed`; evidence `LN-E01;LN-E05`. X14 amount is unknown; LG contributes no known amount but cannot be treated as a zero-activity negative. Proposed next step: Request corrected source evidence and reconcile the replacement to source totals. Human disposition is NOT_RECORDED; no external action is represented as executed. The rationale concerns this specific observed condition, not a broader allegation or certification.

## Independently reset alternate controls

For every alternate, record the deciding predicate and compare actual output with the fixed expected result. On divergence, identify the first differing source, mapping, membership, arithmetic or review branch; do not rewrite the expectation to match the first answer. Confirm consistent results across requested artifacts. Each control tests only its stated behavior.

For each control, start from a fresh baseline or the expressly stated independent account. Record the exact change, expected branch, protected invariants and actual output. Do not carry one control's changes into the next. The specimen supplies complete expected conclusions only where all necessary inputs are stated; a deliberately underspecified change must remain NOT COMPUTED rather than guessed.

### L01: controlled alternate

**Changed input or criterion:** Move X12 ingestion to exactly RUN0 cutoff 04:00Z.

**Exact expected result:** X12 is available because ingest <= cutoff; RUN0 canonical rows become 8.

**Other quantities and protected conditions:** USD credits 15000, debits 14500, gross 29500; LF complete NO_MATCH.

**Interpretation tested:** The cutoff operator is inclusive and distinct from half-open economic scope.

### L02: controlled alternate

**Changed input or criterion:** Move X12 ingestion to 04:00Z plus one second.

**Exact expected result:** X12 remains LATE_DEFERRED at RUN0.

**Other quantities and protected conditions:** RUN0 known USD gross remains 25500; RUN1 remains 29500 if later cutoff unchanged.

**Interpretation tested:** A one-second boundary must not be lost through date-only comparison.

### L03: controlled alternate

**Changed input or criterion:** Resolve authoritative TX05 amount as USD 2000, retaining one canonical version.

**Exact expected result:** RUN1 USD credits 17000, debits 14500, gross 31500; LC becomes NO_MATCH.

**Other quantities and protected conditions:** LC ratio 1000/2000=.5; source conflict history retained.

**Interpretation tested:** Two conflict rows resolve to one economic leg, not two credits.

### L04: controlled alternate

**Changed input or criterion:** Resolve authoritative TX05 amount instead as USD 2200.

**Exact expected result:** RUN1 USD credits 17200, debits 14500, gross 31700; LC NO_MATCH.

**Other quantities and protected conditions:** LC ratio 1000/2200=5/11; both amount and minimum tests fail.

**Interpretation tested:** Do not average 2000 and 2200 into a third invented amount.

### L05: controlled alternate

**Changed input or criterion:** Repair X14 as authoritative posted USD 5000 credit.

**Exact expected result:** RUN1 known USD credits 20000, debits 14500, gross 34500 before TX05 resolution.

**Other quantities and protected conditions:** LG has credit 5000 and no debit; NO_MATCH; LC still blocked.

**Interpretation tested:** Repairing one account does not establish global economic completeness while another conflict remains.

### L06: controlled alternate

**Changed input or criterion:** Repair X14 as authoritative zero credit.

**Exact expected result:** RUN1 known USD gross stays 29500, canonical row count increases to 9.

**Other quantities and protected conditions:** LG no longer amount-blocked; zero credit yields no positive denominator.

**Interpretation tested:** Coverage can improve with no monetary delta.

### L07: controlled alternate

**Changed input or criterion:** Post X09 through a later authoritative source version with amount 7000 unchanged.

**Exact expected result:** Later-run USD credits increase by 7000 and gross by 7000.

**Other quantities and protected conditions:** Retain the original pending version and the new effective/run date.

**Interpretation tested:** A lifecycle update is neither an extraction duplicate nor evidence the earlier status was false.

### L08: controlled alternate

**Changed input or criterion:** Remove X11 reversal link while retaining the debit posting.

**Exact expected result:** The exact-pair exclusion is unsupported; LE requires unresolved reversal treatment.

**Other quantities and protected conditions:** Do not net the equal amounts automatically.

**Interpretation tested:** Equal and opposite values do not independently establish reversal identity.

### L09: controlled alternate

**Changed input or criterion:** Change X11 reversal amount to 2500 with original USD 3000 credit.

**Exact expected result:** The full-pair exclusion fails; partial reversal requires a separately specified residual treatment.

**Other quantities and protected conditions:** Posting signed residual would be +500 USD; gross 5500.

**Interpretation tested:** Do not treat the pair as zero or silently adopt a new netting convention.

### L10: controlled alternate

**Changed input or criterion:** Change X11 currency to EUR while X10 remains USD.

**Exact expected result:** Exact same-currency reversal check fails; preserve currencies and block the pair treatment.

**Other quantities and protected conditions:** No cross-currency netting or invented FX conversion.

**Interpretation tested:** Matching numeric amounts are not matching monetary quantities across currencies.

### L11: controlled alternate

**Changed input or criterion:** Add another exact copy of X02 with new raw ID X16.

**Exact expected result:** Received rows become 16; duplicate count 2; canonical amounts unchanged.

**Other quantities and protected conditions:** RUN0 USD gross 25500 and RUN1 29500 unchanged.

**Interpretation tested:** Copy count and economic count require separate controls.

### L12: controlled alternate

**Changed input or criterion:** Give X03 a new valid transaction identity TX14 instead of TX01.

**Exact expected result:** It becomes another USD 6000 credit rather than duplicate; RUN0 USD credits 17000.

**Other quantities and protected conditions:** LA credits 12000, debit 5400, ratio .45; LA changes to NO_MATCH.

**Interpretation tested:** A distinct valid identity with equal values must not be discarded as a duplicate.

### L13: controlled alternate

**Changed input or criterion:** Change X02 source direction from D to unknown code Z.

**Exact expected result:** Mapping fails; LA amount-dependent assessment becomes NOT_ASSESSABLE.

**Other quantities and protected conditions:** Do not default unknown direction to debit or infer it from transaction purpose.

**Interpretation tested:** The original amount string remains evidence despite failed mapping.

### L14: controlled alternate

**Changed input or criterion:** Change X02 amount string to -5400.00 under the nonnegative mapping.

**Exact expected result:** Amount validation fails; LA becomes NOT_ASSESSABLE.

**Other quantities and protected conditions:** Do not take absolute value or double-flip the direction.

**Interpretation tested:** A signed-source convention requires explicit redesign and tests.

### L15: controlled alternate

**Changed input or criterion:** Move X13 event exactly to economic period end 04:00Z Sep 02.

**Exact expected result:** X13 is out of the half-open event period despite available ingestion.

**Other quantities and protected conditions:** Initial in-period LF debit known subtotal becomes zero; late credit still tracked separately.

**Interpretation tested:** Event scope and ingestion visibility are independent predicates.

### L16: controlled alternate

**Changed input or criterion:** Remove X15 EUR record from the delivered source without an expected source control.

**Exact expected result:** Accessible rows fall to 14; claim only accessible coverage.

**Other quantities and protected conditions:** Do not assert all currencies reconciled without source expectations.

**Interpretation tested:** A technically clean USD pipeline can still omit an entire currency population.

### L17: controlled alternate

**Changed input or criterion:** Convert EUR 1000 using explicit hypothetical USD-per-EUR 1.20 for a separate valuation exhibit.

**Exact expected result:** Converted value 1200 USD; retain original EUR 1000, rate 1.20 and rate convention.

**Other quantities and protected conditions:** Do not merge the valuation exhibit into the unchanged USD-only rule.

**Interpretation tested:** A valuation assumption is not source transaction currency.

### L18: controlled alternate

**Changed input or criterion:** Hold data fixed and lower downstream credit floor from 5000 to 4000 in a new criterion version.

**Exact expected result:** RUN1 LF becomes MATCH at .90 and .5 hours; original version remains NO_MATCH.

**Other quantities and protected conditions:** Lineage controls and canonical sums unchanged.

**Interpretation tested:** A rule-version delta must not be attributed to data repair.

### L19: controlled alternate

**Changed input or criterion:** Resolve TX05 and X14 as 2000 and 5000 in a labeled compound repair after RUN1.

**Exact expected result:** USD credits 22000, debits 14500, gross 36500; canonical rows 10 including EUR.

**Other quantities and protected conditions:** LC and LG become complete negatives under the original rule; two matches remain.

**Interpretation tested:** Match count can remain stable while completeness and amounts change materially.

### L20: controlled alternate

**Changed input or criterion:** Reprocess RUN1 twice with identical inputs and cutoffs.

**Exact expected result:** Canonical rows remain 8 and USD gross 29500 each time.

**Other quantities and protected conditions:** No extra USD 4000 is added on the second run.

**Interpretation tested:** Rerun identity must prevent appending the same late event twice as economic activity.

### L21: controlled alternate

**Changed input or criterion:** Treat both conflicting TX05 rows as valid credits.

**Exact expected result:** Reject resulting double count 4200 and apparent conflict disappearance.

**Other quantities and protected conditions:** Correct state retains both source rows but no selected canonical TX05 amount.

**Interpretation tested:** A reconciled row count alone would not catch this semantic identity failure.

### L22: controlled alternate

**Changed input or criterion:** Describe raw USD gross 52700 as canonical economic movement.

**Exact expected result:** Reject: raw known credits 35200 plus debits 17500 include non-economic copies and controlled exclusions.

**Other quantities and protected conditions:** Correct RUN0 known canonical USD gross is 25500.

**Interpretation tested:** The layer label is essential to interpreting a monetary control.

### L23: controlled alternate

**Changed input or criterion:** Declare RUN1 fully timely because X12 is repaired.

**Exact expected result:** Reject: only this known late event has been reproduced; broader latency distribution is not supplied.

**Other quantities and protected conditions:** Retain explicit limit on complete late-arrival population.

**Interpretation tested:** One successful rerun is not a feed-wide service-level validation.

### L24: controlled alternate

**Changed input or criterion:** Set a high-severity defect label on LC and infer customer suspicion.

**Exact expected result:** Reject the inference; HIGH concerns coverage impact and HIGH confidence concerns the observed conflict.

**Other quantities and protected conditions:** No customer offense conclusion exists in the source.

**Interpretation tested:** Severity, confidence and substantive suspicion are independent concepts.

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

RAW_COLUMNS = ['raw_row_id', 'transaction_id', 'account_id', 'event_utc', 'ingest_utc', 'source_direction', 'amount_text', 'currency', 'source_status', 'source_version', 'reversal_of', 'evidence_ids']
RAW = [['X01', 'TX01', 'LA', '2026-09-01T13:00:00Z', '2026-09-01T13:05:00Z', 'C', '6000.00', 'USD', 'P', '1', None, 'LN-E01'], ['X02', 'TX02', 'LA', '2026-09-01T14:00:00Z', '2026-09-01T14:05:00Z', 'D', '5400.00', 'USD', 'P', '1', None, 'LN-E01'], ['X03', 'TX01', 'LA', '2026-09-01T13:00:00Z', '2026-09-01T15:00:00Z', 'C', '6000.00', 'USD', 'P', '1', None, 'LN-E01'], ['X04', 'TX03', 'LB', '2026-09-01T13:00:00Z', '2026-09-01T13:05:00Z', 'C', '5000.00', 'USD', 'P', '1', None, 'LN-E01'], ['X05', 'TX04', 'LB', '2026-09-01T14:00:00Z', '2026-09-01T14:05:00Z', 'D', '4500.00', 'USD', 'P', '1', None, 'LN-E01'], ['X06', 'TX05', 'LC', '2026-09-01T13:00:00Z', '2026-09-01T13:05:00Z', 'C', '2000.00', 'USD', 'P', '1', None, 'LN-E01'], ['X07', 'TX05', 'LC', '2026-09-01T13:00:00Z', '2026-09-01T13:06:00Z', 'C', '2200.00', 'USD', 'P', '1', None, 'LN-E01;LN-E02'], ['X08', 'TX06', 'LC', '2026-09-01T14:00:00Z', '2026-09-01T14:05:00Z', 'D', '1000.00', 'USD', 'P', '1', None, 'LN-E01'], ['X09', 'TX07', 'LD', '2026-09-01T13:00:00Z', '2026-09-01T13:05:00Z', 'C', '7000.00', 'USD', 'N', '1', None, 'LN-E01'], ['X10', 'TX08', 'LE', '2026-09-01T13:00:00Z', '2026-09-01T13:05:00Z', 'C', '3000.00', 'USD', 'P', '1', None, 'LN-E01'], ['X11', 'TX09', 'LE', '2026-09-01T14:00:00Z', '2026-09-01T14:05:00Z', 'D', '3000.00', 'USD', 'R', '1', 'TX08', 'LN-E01;LN-E03'], ['X12', 'TX10', 'LF', '2026-09-01T23:30:00Z', '2026-09-02T10:00:00Z', 'C', '4000.00', 'USD', 'P', '1', None, 'LN-E01;LN-E04'], ['X13', 'TX11', 'LF', '2026-09-02T00:00:00Z', '2026-09-02T00:05:00Z', 'D', '3600.00', 'USD', 'P', '1', None, 'LN-E01'], ['X14', 'TX12', 'LG', '2026-09-01T13:00:00Z', '2026-09-01T13:05:00Z', 'C', 'unreadable', 'USD', 'P', '1', None, 'LN-E01;LN-E05'], ['X15', 'TX13', 'LH', '2026-09-01T13:00:00Z', '2026-09-01T13:05:00Z', 'C', '1000.00', 'EUR', 'P', '1', None, 'LN-E01']]

raw=[dict(zip(RAW_COLUMNS,row)) for row in RAW]
for r in raw:
    try:r['amount']=dec(r['amount_text'])
    except Exception:r['amount']=None
    r['direction']={'C':'CREDIT','D':'DEBIT'}[r['source_direction']]
cut0=instant('2026-09-02T04:00:00Z');cut1=instant('2026-09-02T12:00:00Z')
groups=defaultdict(list)
for r in raw:groups[(r['transaction_id'],r['account_id'],r['source_version'])].append(r)
conflict={r['raw_row_id'] for rows in groups.values() if len({(r['amount_text'],r['direction'],r['currency'],r['event_utc'],r['source_status']) for r in rows})>1 for r in rows}
bytx={r['transaction_id']:r for r in raw}
reverse=set()
for r in raw:
    if r['source_status']=='R':
        original=bytx[r['reversal_of']]
        assert original['account_id']==r['account_id'] and original['currency']==r['currency'] and original['amount']==r['amount']
        reverse.update([r['raw_row_id'],original['raw_row_id']])
seen={};states={};canonical=[];cid_by_identity={}
for r in raw:
    identity=(r['transaction_id'],r['account_id'],r['source_version'])
    if r['raw_row_id'] in conflict:state='CONFLICT'
    elif identity in seen:state='DUPLICATE'
    elif r['source_status']=='N':state='PENDING'
    elif r['raw_row_id'] in reverse:state='REVERSAL_PAIR'
    elif instant(r['ingest_utc'])>cut0:state='LATE_DEFERRED'
    elif r['amount'] is None:state='UNPARSED_AMOUNT'
    else:state='CANONICAL'
    states[r['raw_row_id']]=state
    if state=='CANONICAL':
        cid='CL'+str(len(canonical)+1).zfill(2);cid_by_identity[identity]=cid
        canonical.append(dict(r,canonical_id=cid))
    seen[identity]=r
assert Counter(states.values())=={'CANONICAL':7,'DUPLICATE':1,'CONFLICT':2,'PENDING':1,'REVERSAL_PAIR':2,'LATE_DEFERRED':1,'UNPARSED_AMOUNT':1}
reasons={'CANONICAL':'Unique readable posted leg available by initial cutoff','DUPLICATE':'Same economic tuple and payload as X01; later extraction metadata only','CONFLICT':'Same TX05 identity; conflicting amount; neither selected','PENDING':'Not posted at supplied status; retain outside posted ledger','REVERSAL_PAIR':'Exact linked original and reversal preserved but netted out of external-flow scenario','LATE_DEFERRED':'Event in period, ingestion after initial cutoff; add only in rerun','UNPARSED_AMOUNT':'Posted amount cannot be recovered; LG blocked'}
lineage=[]
for r in raw:
    state=states[r['raw_row_id']];identity=(r['transaction_id'],r['account_id'],r['source_version'])
    cid=cid_by_identity.get(identity) if state in ['CANONICAL','DUPLICATE'] else None
    lineage.append(['LIN-'+r['raw_row_id'],r['raw_row_id'],cid,state,reasons[state],'RUN0',r['evidence_ids']+';LN-E06'])
CHECKED_TABLES['LineageLedger']=lineage
CHECKED_TABLES['CanonicalOutput']=[[r['canonical_id'],r['raw_row_id'],r['transaction_id'],r['account_id'],r['event_utc'],r['direction'],float(r['amount']),r['currency'],'RUN0',r['evidence_ids']] for r in canonical]
rerun=canonical+[dict(r,canonical_id='CL08') for r in raw if states[r['raw_row_id']]=='LATE_DEFERRED' and instant(r['ingest_utc'])<=cut1]
controls=[]
interpretations=[
'Raw contains duplicate, conflicting alternatives, pending and reversal; not economic total','Separate currency; not added to USD','Known partial posted population; LC conflict, LF late, LG unknown remain blocked','Preserved EUR leg; USD scenario exclusion separately disclosed','Adds X12 USD 4000 credit; unresolved conflict and parse defect remain','EUR unchanged']
for label,rows in [('Delivered raw',raw),('RUN0 canonical',canonical),('RUN1 canonical',rerun)]:
    for currency in ['USD','EUR']:
        subset=[r for r in rows if r['currency']==currency];i=len(controls)
        refs='LN-E01' if label=='Delivered raw' else 'LN-E04;LN-E06' if label=='RUN1 canonical' and currency=='USD' else 'LN-E01;LN-E06'
        controls.append(['LC'+str(i+1).zfill(2),label,currency,len(subset),float(total(subset,'CREDIT')),float(total(subset,'DEBIT')),sum(r['amount'] is None for r in subset),interpretations[i],refs])
CHECKED_TABLES['StageControls']=controls
reasons_impact={'LA':'No source change','LB':'No source change','LC':'TX05 conflict unresolved; credit zero means known subtotal only','LD':'Pending source retained; no posted leg','LE':'Original and reversal retained outside illustrative flow totals','LF':'Late credit repaired; ratio .90 but 4000 below illustrative 5000 minimum','LG':'Unknown posted credit remains; zeros are known subtotals','LH':'USD-only rule; EUR preserved in lineage'}
refs_impact={'LA':'LN-E01;LN-E06','LB':'LN-E01;LN-E06','LC':'LN-E02;LN-E06','LD':'LN-E01;LN-E06','LE':'LN-E03;LN-E06','LF':'LN-E04;LN-E06','LG':'LN-E05;LN-E06','LH':'LN-E01;LN-E06'}
def state_for(account,rows,run):
    source=[r for r in raw if r['account_id']==account]
    if any(states[r['raw_row_id']] in ['CONFLICT','UNPARSED_AMOUNT'] for r in source):return 'NOT_ASSESSABLE'
    if run==0 and any(states[r['raw_row_id']]=='LATE_DEFERRED' for r in source):return 'NOT_ASSESSABLE'
    if all(r['currency']!='USD' for r in source):return 'CURRENCY_EXCLUDED'
    if all(states[r['raw_row_id']]=='PENDING' for r in source):return 'NO_POSTED_ACTIVITY'
    if all(states[r['raw_row_id']]=='REVERSAL_PAIR' for r in source):return 'REVERSAL_PAIR_EXCLUDED'
    c=total(rows,'CREDIT');d=total(rows,'DEBIT')
    credits=[instant(r['event_utc']) for r in rows if r['direction']=='CREDIT']
    later=[instant(r['event_utc']) for r in rows if r['direction']=='DEBIT' and credits and instant(r['event_utc'])>min(credits)]
    h=(min(later)-min(credits)).total_seconds()/3600 if later else None
    return 'MATCH' if c>=5000 and d/c>=dec('.9') and h is not None and h<=24 else 'NO_MATCH'
impact=[]
for account in sorted({r['account_id'] for r in raw}):
    before=[r for r in canonical if r['account_id']==account];after=[r for r in rerun if r['account_id']==account]
    currency=next(r['currency'] for r in raw if r['account_id']==account)
    impact.append(['IMP-'+account[1:],account,currency,float(total(before,'CREDIT')),float(total(before,'DEBIT')),state_for(account,before,0),float(total(after,'CREDIT')),float(total(after,'DEBIT')),state_for(account,after,1),reasons_impact[account],refs_impact[account]])
CHECKED_TABLES['RunImpact']=impact
usd0=[r for r in canonical if r['currency']=='USD'];usd1=[r for r in rerun if r['currency']=='USD']
assert total(usd0,'CREDIT')==11000 and total(usd0,'DEBIT')==14500
assert total(usd1,'CREDIT')==15000 and total(usd1,'DEBIT')==14500
assert total(usd1,'CREDIT')+total(usd1,'DEBIT')==29500
assert len(canonical)==7 and len(rerun)==8
assert impact[5][5]=='NOT_ASSESSABLE' and impact[5][8]=='NO_MATCH'
assert (instant('2026-09-02T00:00:00Z')-instant('2026-09-01T23:30:00Z')).total_seconds()/3600==.5
assert sum(r[8]=='MATCH' for r in impact)==2
assert 15000+2000+5000+14500==36500

print("Fictional specimen arithmetic and boundary assertions passed.")
```
<!-- FIXTURE_CHECK:END -->
