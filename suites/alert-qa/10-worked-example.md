# Alert Adjudication Quality Review — complete worked case

**Fictional training case. All identifiers, parties, amounts, policy criteria, reviewers and outcomes below are synthetic.** The fully populated case demonstrates analytical method and output structure; it is not a completed operational review. All facts needed for its arithmetic are printed below.

## Raw packet selection and review record

This is a deliberately selected twelve-packet calibration set. It is not a probability sample. CP-QA-1 supplies eight authored quality criteria printed below; the criteria are internal illustrative policy for this exercise. Two fictional reviewers R1 and R2 record blind round 1 votes before the consensus shown in Q14. No real person, customer, case or actual institution is represented.

| case_id | topic | complete_packet_facts | later_consensus | adjudication_reason |
| --- | --- | --- | --- | --- |
| C01 | Routine pass-through explanation | Posted debit 1000; invoice 1000; beneficiary and delivery match; counterevidence considered. | ACCEPT | No material reasoning defect on supplied packet. |
| C02 | Omitted contrary invoice | Investigator described no business support; packet includes matched invoice 2000 and delivery for the same payment. | REWORK | Material contrary evidence omitted; outcome must be reconsidered without assuming reversal. |
| C03 | Partial return treated as full reversal | Original debit 11000 and explicitly linked return 2000; narrative says fully reversed. | REWORK | Correct net 9000 and review conclusion dependent on the error. |
| C04 | Unsupported identity merge | Two beneficiaries have similar names but different supplied identifiers; investigator merged them into one subject. | REWORK | Split identities and recompute aggregate before reassessing. |
| C05 | Nonmaterial display defect | Ledger and narrative amounts match; one non-substantive punctuation defect in an evidence title. | ACCEPT | Optional editorial correction; no effect on inference or traceability. |
| C06 | Relevant timeline gap | Two same-period postings 4000 and 3500 omitted from chronology while present in supplied ledger; net effect 500. | REWORK | Restore both gross events and recompute period totals; net 500 does not excuse omission. |
| C07 | Bounded unknown handled correctly | Opening balance missing; investigator declines source attribution, requests balance and gives descriptive flows only. | ACCEPT | Properly bounded analysis; unknown is not itself a quality failure. |
| C08 | Source inaccessible | Case conclusion cites an encrypted document unavailable to either reviewer; no equivalent source supplied. | INSUFFICIENT | Review cannot determine whether the underlying conclusion is supported. |
| C09 | Different defensible wording | Narrative uses unresolved purpose; reviewer prefers insufficient corroboration; both reflect same evidence and scope. | ACCEPT | Style preference alone is not a defect. |
| C10 | Observed pattern overstates intent | Rapid onward transfers are evidenced; conclusion states intent to launder without supporting intent evidence. | REWORK | Remove unsupported intent assertion and reconsider bounded analytical conclusion. |
| C11 | Invented universal documentation rule | Reviewer worksheet treats absent nonfiling memorandum as a universal BSA breach; supplied fixture policy only requires a brief case rationale. | REWORK | Use supplied policy CP-QA-1 and actual case rationale; no universal nonfiling memo requirement. |
| C12 | Unknown historical cutoff | Packet does not identify what evidence was available at original decision date; reviewers see later documents mixed with earlier material. | INSUFFICIENT | Cannot assess original decision under hindsight without an availability chronology. |

### Original blind round 1 votes

| case_id | R1 | R2 |
| --- | --- | --- |
| C01 | ACCEPT | ACCEPT |
| C02 | ACCEPT | REWORK |
| C03 | REWORK | REWORK |
| C04 | REWORK | REWORK |
| C05 | ACCEPT | ACCEPT |
| C06 | REWORK | ACCEPT |
| C07 | ACCEPT | ACCEPT |
| C08 | INSUFFICIENT | INSUFFICIENT |
| C09 | ACCEPT | ACCEPT |
| C10 | REWORK | REWORK |
| C11 | ACCEPT | INSUFFICIENT |
| C12 | INSUFFICIENT | INSUFFICIENT |

### Supplied illustrative criterion cards CP-QA-1

| criterion_id | dimension | rule | class | boundary |
| --- | --- | --- | --- | --- |
| K01 | Population completeness | Include relevant supplied records or a documented scope exclusion. | MATERIAL | Missing relevant rows can change amounts, chronology or explanation. |
| K02 | Calculation accuracy | Reperform stated gross, returns, net and denominator calculations. | MATERIAL | A correct net cannot replace omitted gross events. |
| K03 | Identity substantiation | Merge subjects only with adequate supplied identifier linkage. | MATERIAL | Similar names alone cannot support aggregation. |
| K04 | Contrary evidence | Address material evidence inconsistent with the proposed conclusion. | MATERIAL | Reviewers need not prefer the contrary explanation, but must evaluate it. |
| K05 | Claim strength | Match assertion to evidence class and confidence. | MATERIAL | Observed timing does not establish intent. |
| K06 | Criterion authority | Attribute a defect to applicable supplied policy or relevant law with scope. | MATERIAL | Do not invent a universal nonfiling-document requirement. |
| K07 | Reviewability | Establish source accessibility and decision-time availability. | ASSESSABILITY | Unable to assess is separate from a demonstrated investigator defect. |
| K08 | Presentation clarity | Correct editorial issues that affect comprehension or traceability. | NONMATERIAL | Pure preference with no consequence is not a quality failure. |

Q14 adjudication explicitly records C02, C06 and C11 as REWORK after discussing the criterion/evidence disagreement. It retains C08/C12 as INSUFFICIENT because discussion cannot create missing source access or historical availability. Q16 consists of proposed repairs only; there are no completed repairs or closure approvals.

## Fully adjudicated packet-by-packet review

### C01 — Routine pass-through explanation

**Supplied packet facts.** Posted debit 1000; invoice 1000; beneficiary and delivery match; counterevidence considered. These facts are the complete fictional packet for this calibration question. Do not infer additional customer conduct, omitted attachments or an actual filing outcome. The source locator is Q01.

**Original blind assessment.** R1 recorded `ACCEPT` and R2 recorded `ACCEPT`. The pair therefore agrees before discussion. Keep both votes unchanged in ReviewVotes and Calibration; later consensus is `ACCEPT`.

**Adjudicated reasoning.** No material reasoning defect on supplied packet. No demonstrated defect row is assigned on the supplied evidence. That is a scoped result, not a statement that the underlying customer activity is benign or that the case should receive an operational closure.

**Denominator effect.** This packet contributes to the four acceptable cases and the 10 assessable cases. A nonmaterial defect, where present, is counted in the defect ledger without automatically changing the substantive case outcome. Acceptance means the bounded quality rubric is satisfied on this packet, not approval of an underlying filing decision.

### C02 — Omitted contrary invoice

**Supplied packet facts.** Investigator described no business support; packet includes matched invoice 2000 and delivery for the same payment. These facts are the complete fictional packet for this calibration question. Do not infer additional customer conduct, omitted attachments or an actual filing outcome. The source locator is Q02.

**Original blind assessment.** R1 recorded `ACCEPT` and R2 recorded `REWORK`. The pair therefore disagrees before discussion. Keep both votes unchanged in ReviewVotes and Calibration; later consensus is `REWORK`.

**Adjudicated reasoning.** Material contrary evidence omitted; outcome must be reconsidered without assuming reversal. Demonstrated defect membership is D01 under K04 (MATERIAL, MEDIUM). The proposed repair is: Evaluate matched invoice and delivery as counterevidence. The closure test is: Revised rationale addresses both sides and any outcome change.

**Denominator effect.** This packet contributes one unique material-defect case to both the selected-case numerator and assessable-case numerator. It appears once in the case rate even if a later review identifies more than one defect. It remains one of 12 selected cases and one of 10 assessable cases.

### C03 — Partial return treated as full reversal

**Supplied packet facts.** Original debit 11000 and explicitly linked return 2000; narrative says fully reversed. These facts are the complete fictional packet for this calibration question. Do not infer additional customer conduct, omitted attachments or an actual filing outcome. The source locator is Q03.

**Original blind assessment.** R1 recorded `REWORK` and R2 recorded `REWORK`. The pair therefore agrees before discussion. Keep both votes unchanged in ReviewVotes and Calibration; later consensus is `REWORK`.

**Adjudicated reasoning.** Correct net 9000 and review conclusion dependent on the error. Demonstrated defect membership is D02 under K02 (MATERIAL, HIGH). The proposed repair is: Correct gross 11000, return 2000 and net 9000. The closure test is: Recalculate from posted records and inspect affected conclusion.

**Denominator effect.** This packet contributes one unique material-defect case to both the selected-case numerator and assessable-case numerator. It appears once in the case rate even if a later review identifies more than one defect. It remains one of 12 selected cases and one of 10 assessable cases.

### C04 — Unsupported identity merge

**Supplied packet facts.** Two beneficiaries have similar names but different supplied identifiers; investigator merged them into one subject. These facts are the complete fictional packet for this calibration question. Do not infer additional customer conduct, omitted attachments or an actual filing outcome. The source locator is Q04.

**Original blind assessment.** R1 recorded `REWORK` and R2 recorded `REWORK`. The pair therefore agrees before discussion. Keep both votes unchanged in ReviewVotes and Calibration; later consensus is `REWORK`.

**Adjudicated reasoning.** Split identities and recompute aggregate before reassessing. Demonstrated defect membership is D03 under K03 (MATERIAL, HIGH). The proposed repair is: Split unsupported merged subjects. The closure test is: Recompute separate aggregates and verify each identity link.

**Denominator effect.** This packet contributes one unique material-defect case to both the selected-case numerator and assessable-case numerator. It appears once in the case rate even if a later review identifies more than one defect. It remains one of 12 selected cases and one of 10 assessable cases.

### C05 — Nonmaterial display defect

**Supplied packet facts.** Ledger and narrative amounts match; one non-substantive punctuation defect in an evidence title. These facts are the complete fictional packet for this calibration question. Do not infer additional customer conduct, omitted attachments or an actual filing outcome. The source locator is Q05.

**Original blind assessment.** R1 recorded `ACCEPT` and R2 recorded `ACCEPT`. The pair therefore agrees before discussion. Keep both votes unchanged in ReviewVotes and Calibration; later consensus is `ACCEPT`.

**Adjudicated reasoning.** Optional editorial correction; no effect on inference or traceability. Demonstrated defect membership is D04 under K08 (NONMATERIAL, LOW). The proposed repair is: Optionally correct punctuation without altering analytical outcome. The closure test is: Evidence title remains resolvable; no material rework needed.

**Denominator effect.** This packet contributes to the four acceptable cases and the 10 assessable cases. A nonmaterial defect, where present, is counted in the defect ledger without automatically changing the substantive case outcome. Acceptance means the bounded quality rubric is satisfied on this packet, not approval of an underlying filing decision.

### C06 — Relevant timeline gap

**Supplied packet facts.** Two same-period postings 4000 and 3500 omitted from chronology while present in supplied ledger; net effect 500. These facts are the complete fictional packet for this calibration question. Do not infer additional customer conduct, omitted attachments or an actual filing outcome. The source locator is Q06.

**Original blind assessment.** R1 recorded `REWORK` and R2 recorded `ACCEPT`. The pair therefore disagrees before discussion. Keep both votes unchanged in ReviewVotes and Calibration; later consensus is `REWORK`.

**Adjudicated reasoning.** Restore both gross events and recompute period totals; net 500 does not excuse omission. Demonstrated defect membership is D05 under K01 (MATERIAL, MEDIUM). The proposed repair is: Restore omitted credit 4000 and debit 3500. The closure test is: Reconcile gross flows, net 500 and chronology.

**Denominator effect.** This packet contributes one unique material-defect case to both the selected-case numerator and assessable-case numerator. It appears once in the case rate even if a later review identifies more than one defect. It remains one of 12 selected cases and one of 10 assessable cases.

### C07 — Bounded unknown handled correctly

**Supplied packet facts.** Opening balance missing; investigator declines source attribution, requests balance and gives descriptive flows only. These facts are the complete fictional packet for this calibration question. Do not infer additional customer conduct, omitted attachments or an actual filing outcome. The source locator is Q07.

**Original blind assessment.** R1 recorded `ACCEPT` and R2 recorded `ACCEPT`. The pair therefore agrees before discussion. Keep both votes unchanged in ReviewVotes and Calibration; later consensus is `ACCEPT`.

**Adjudicated reasoning.** Properly bounded analysis; unknown is not itself a quality failure. No demonstrated defect row is assigned on the supplied evidence. That is a scoped result, not a statement that the underlying customer activity is benign or that the case should receive an operational closure.

**Denominator effect.** This packet contributes to the four acceptable cases and the 10 assessable cases. A nonmaterial defect, where present, is counted in the defect ledger without automatically changing the substantive case outcome. Acceptance means the bounded quality rubric is satisfied on this packet, not approval of an underlying filing decision.

### C08 — Source inaccessible

**Supplied packet facts.** Case conclusion cites an encrypted document unavailable to either reviewer; no equivalent source supplied. These facts are the complete fictional packet for this calibration question. Do not infer additional customer conduct, omitted attachments or an actual filing outcome. The source locator is Q08.

**Original blind assessment.** R1 recorded `INSUFFICIENT` and R2 recorded `INSUFFICIENT`. The pair therefore agrees before discussion. Keep both votes unchanged in ReviewVotes and Calibration; later consensus is `INSUFFICIENT`.

**Adjudicated reasoning.** Review cannot determine whether the underlying conclusion is supported. No demonstrated defect row is assigned on the supplied evidence. That is a scoped result, not a statement that the underlying customer activity is benign or that the case should receive an operational closure.

**Denominator effect.** This packet remains in the 12 selected-case denominator but outside the 10 assessable-case denominator. It contributes to the two unknowns and is not counted as an acceptable case or a demonstrated material-defect case. Any later evidence-driven reassessment must update consensus counts and rates without rewriting original agreement.

### C09 — Different defensible wording

**Supplied packet facts.** Narrative uses unresolved purpose; reviewer prefers insufficient corroboration; both reflect same evidence and scope. These facts are the complete fictional packet for this calibration question. Do not infer additional customer conduct, omitted attachments or an actual filing outcome. The source locator is Q09.

**Original blind assessment.** R1 recorded `ACCEPT` and R2 recorded `ACCEPT`. The pair therefore agrees before discussion. Keep both votes unchanged in ReviewVotes and Calibration; later consensus is `ACCEPT`.

**Adjudicated reasoning.** Style preference alone is not a defect. No demonstrated defect row is assigned on the supplied evidence. That is a scoped result, not a statement that the underlying customer activity is benign or that the case should receive an operational closure.

**Denominator effect.** This packet contributes to the four acceptable cases and the 10 assessable cases. A nonmaterial defect, where present, is counted in the defect ledger without automatically changing the substantive case outcome. Acceptance means the bounded quality rubric is satisfied on this packet, not approval of an underlying filing decision.

### C10 — Observed pattern overstates intent

**Supplied packet facts.** Rapid onward transfers are evidenced; conclusion states intent to launder without supporting intent evidence. These facts are the complete fictional packet for this calibration question. Do not infer additional customer conduct, omitted attachments or an actual filing outcome. The source locator is Q10.

**Original blind assessment.** R1 recorded `REWORK` and R2 recorded `REWORK`. The pair therefore agrees before discussion. Keep both votes unchanged in ReviewVotes and Calibration; later consensus is `REWORK`.

**Adjudicated reasoning.** Remove unsupported intent assertion and reconsider bounded analytical conclusion. Demonstrated defect membership is D06 under K05 (MATERIAL, HIGH). The proposed repair is: Replace unsupported intent assertion with bounded observed pattern. The closure test is: Every remaining proposition matches its evidence class.

**Denominator effect.** This packet contributes one unique material-defect case to both the selected-case numerator and assessable-case numerator. It appears once in the case rate even if a later review identifies more than one defect. It remains one of 12 selected cases and one of 10 assessable cases.

### C11 — Invented universal documentation rule

**Supplied packet facts.** Reviewer worksheet treats absent nonfiling memorandum as a universal BSA breach; supplied fixture policy only requires a brief case rationale. These facts are the complete fictional packet for this calibration question. Do not infer additional customer conduct, omitted attachments or an actual filing outcome. The source locator is Q11.

**Original blind assessment.** R1 recorded `ACCEPT` and R2 recorded `INSUFFICIENT`. The pair therefore disagrees before discussion. Keep both votes unchanged in ReviewVotes and Calibration; later consensus is `REWORK`.

**Adjudicated reasoning.** Use supplied policy CP-QA-1 and actual case rationale; no universal nonfiling memo requirement. Demonstrated defect membership is D07 under K06 (MATERIAL, MEDIUM). The proposed repair is: Apply CP-QA-1 brief-rationale criterion and remove invented legal premise. The closure test is: Assess actual rationale under supplied policy; no automatic regulatory finding.

**Denominator effect.** This packet contributes one unique material-defect case to both the selected-case numerator and assessable-case numerator. It appears once in the case rate even if a later review identifies more than one defect. It remains one of 12 selected cases and one of 10 assessable cases.

### C12 — Unknown historical cutoff

**Supplied packet facts.** Packet does not identify what evidence was available at original decision date; reviewers see later documents mixed with earlier material. These facts are the complete fictional packet for this calibration question. Do not infer additional customer conduct, omitted attachments or an actual filing outcome. The source locator is Q12.

**Original blind assessment.** R1 recorded `INSUFFICIENT` and R2 recorded `INSUFFICIENT`. The pair therefore agrees before discussion. Keep both votes unchanged in ReviewVotes and Calibration; later consensus is `INSUFFICIENT`.

**Adjudicated reasoning.** Cannot assess original decision under hindsight without an availability chronology. No demonstrated defect row is assigned on the supplied evidence. That is a scoped result, not a statement that the underlying customer activity is benign or that the case should receive an operational closure.

**Denominator effect.** This packet remains in the 12 selected-case denominator but outside the 10 assessable-case denominator. It contributes to the two unknowns and is not counted as an acceptable case or a demonstrated material-defect case. Any later evidence-driven reassessment must update consensus counts and rates without rewriting original agreement.

## Fully populated expected domain outputs

These are the complete expected base-case records. They are not selected examples. Preserve every row when generating the report, workbook and dashboard. The raw facts above and the independent checks below explain the calculations; descriptive decisions additionally require the methods and gates in files 03–04.

### CasePackets

| case_id | case_topic | raw_packet | consensus | rationale | evidence_ids |
| --- | --- | --- | --- | --- | --- |
| C01 | Routine pass-through explanation | Posted debit 1000; invoice 1000; beneficiary and delivery match; counterevidence considered. | ACCEPT | No material reasoning defect on supplied packet. | Q01;Q14;Q15 |
| C02 | Omitted contrary invoice | Investigator described no business support; packet includes matched invoice 2000 and delivery for the same payment. | REWORK | Material contrary evidence omitted; outcome must be reconsidered without assuming reversal. | Q02;Q14;Q15 |
| C03 | Partial return treated as full reversal | Original debit 11000 and explicitly linked return 2000; narrative says fully reversed. | REWORK | Correct net 9000 and review conclusion dependent on the error. | Q03;Q14;Q15 |
| C04 | Unsupported identity merge | Two beneficiaries have similar names but different supplied identifiers; investigator merged them into one subject. | REWORK | Split identities and recompute aggregate before reassessing. | Q04;Q14;Q15 |
| C05 | Nonmaterial display defect | Ledger and narrative amounts match; one non-substantive punctuation defect in an evidence title. | ACCEPT | Optional editorial correction; no effect on inference or traceability. | Q05;Q14;Q15 |
| C06 | Relevant timeline gap | Two same-period postings 4000 and 3500 omitted from chronology while present in supplied ledger; net effect 500. | REWORK | Restore both gross events and recompute period totals; net 500 does not excuse omission. | Q06;Q14;Q15 |
| C07 | Bounded unknown handled correctly | Opening balance missing; investigator declines source attribution, requests balance and gives descriptive flows only. | ACCEPT | Properly bounded analysis; unknown is not itself a quality failure. | Q07;Q14;Q15 |
| C08 | Source inaccessible | Case conclusion cites an encrypted document unavailable to either reviewer; no equivalent source supplied. | INSUFFICIENT | Review cannot determine whether the underlying conclusion is supported. | Q08;Q14;Q15 |
| C09 | Different defensible wording | Narrative uses unresolved purpose; reviewer prefers insufficient corroboration; both reflect same evidence and scope. | ACCEPT | Style preference alone is not a defect. | Q09;Q14;Q15 |
| C10 | Observed pattern overstates intent | Rapid onward transfers are evidenced; conclusion states intent to launder without supporting intent evidence. | REWORK | Remove unsupported intent assertion and reconsider bounded analytical conclusion. | Q10;Q14;Q15 |
| C11 | Invented universal documentation rule | Reviewer worksheet treats absent nonfiling memorandum as a universal BSA breach; supplied fixture policy only requires a brief case rationale. | REWORK | Use supplied policy CP-QA-1 and actual case rationale; no universal nonfiling memo requirement. | Q11;Q14;Q15 |
| C12 | Unknown historical cutoff | Packet does not identify what evidence was available at original decision date; reviewers see later documents mixed with earlier material. | INSUFFICIENT | Cannot assess original decision under hindsight without an availability chronology. | Q12;Q14;Q15 |

### ReviewVotes

| vote_id | case_id | reviewer_id | vote | round | evidence_ids |
| --- | --- | --- | --- | --- | --- |
| V01 | C01 | R1 | ACCEPT | 1 | Q13;Q01 |
| V02 | C01 | R2 | ACCEPT | 1 | Q13;Q01 |
| V03 | C02 | R1 | ACCEPT | 1 | Q13;Q02 |
| V04 | C02 | R2 | REWORK | 1 | Q13;Q02 |
| V05 | C03 | R1 | REWORK | 1 | Q13;Q03 |
| V06 | C03 | R2 | REWORK | 1 | Q13;Q03 |
| V07 | C04 | R1 | REWORK | 1 | Q13;Q04 |
| V08 | C04 | R2 | REWORK | 1 | Q13;Q04 |
| V09 | C05 | R1 | ACCEPT | 1 | Q13;Q05 |
| V10 | C05 | R2 | ACCEPT | 1 | Q13;Q05 |
| V11 | C06 | R1 | REWORK | 1 | Q13;Q06 |
| V12 | C06 | R2 | ACCEPT | 1 | Q13;Q06 |
| V13 | C07 | R1 | ACCEPT | 1 | Q13;Q07 |
| V14 | C07 | R2 | ACCEPT | 1 | Q13;Q07 |
| V15 | C08 | R1 | INSUFFICIENT | 1 | Q13;Q08 |
| V16 | C08 | R2 | INSUFFICIENT | 1 | Q13;Q08 |
| V17 | C09 | R1 | ACCEPT | 1 | Q13;Q09 |
| V18 | C09 | R2 | ACCEPT | 1 | Q13;Q09 |
| V19 | C10 | R1 | REWORK | 1 | Q13;Q10 |
| V20 | C10 | R2 | REWORK | 1 | Q13;Q10 |
| V21 | C11 | R1 | ACCEPT | 1 | Q13;Q11 |
| V22 | C11 | R2 | INSUFFICIENT | 1 | Q13;Q11 |
| V23 | C12 | R1 | INSUFFICIENT | 1 | Q13;Q12 |
| V24 | C12 | R2 | INSUFFICIENT | 1 | Q13;Q12 |

### QualityCriteria

| criterion_id | criterion | rule | materiality_class | boundary | evidence_ids |
| --- | --- | --- | --- | --- | --- |
| K01 | Population completeness | Include relevant supplied records or a documented scope exclusion. | MATERIAL | Missing relevant rows can change amounts, chronology or explanation. | Q15 |
| K02 | Calculation accuracy | Reperform stated gross, returns, net and denominator calculations. | MATERIAL | A correct net cannot replace omitted gross events. | Q15 |
| K03 | Identity substantiation | Merge subjects only with adequate supplied identifier linkage. | MATERIAL | Similar names alone cannot support aggregation. | Q15 |
| K04 | Contrary evidence | Address material evidence inconsistent with the proposed conclusion. | MATERIAL | Reviewers need not prefer the contrary explanation, but must evaluate it. | Q15 |
| K05 | Claim strength | Match assertion to evidence class and confidence. | MATERIAL | Observed timing does not establish intent. | Q15 |
| K06 | Criterion authority | Attribute a defect to applicable supplied policy or relevant law with scope. | MATERIAL | Do not invent a universal nonfiling-document requirement. | Q15 |
| K07 | Reviewability | Establish source accessibility and decision-time availability. | ASSESSABILITY | Unable to assess is separate from a demonstrated investigator defect. | Q15 |
| K08 | Presentation clarity | Correct editorial issues that affect comprehension or traceability. | NONMATERIAL | Pure preference with no consequence is not a quality failure. | Q15 |

### DefectRegister

| defect_id | case_id | criterion_id | severity | materiality | condition | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| D01 | C02 | K04 | MEDIUM | MATERIAL | Contrary matched invoice and delivery omitted | Q02;Q15 |
| D02 | C03 | K02 | HIGH | MATERIAL | USD11000 minus USD2000 is USD9000, not zero | Q03;Q15 |
| D03 | C04 | K03 | HIGH | MATERIAL | Unsupported subject merge changes aggregation | Q04;Q15 |
| D04 | C05 | K08 | LOW | NONMATERIAL | Punctuation correction does not affect meaning | Q05;Q15 |
| D05 | C06 | K01 | MEDIUM | MATERIAL | Gross 4000 credit and 3500 debit omitted; net 500 | Q06;Q15 |
| D06 | C10 | K05 | HIGH | MATERIAL | Intent claim exceeds evidence of timing | Q10;Q15 |
| D07 | C11 | K06 | MEDIUM | MATERIAL | Universal regulatory documentation premise unsupported | Q11;Q15 |

### Calibration

| case_id | r 1_vote | r 2_vote | agreement | consensus | adjudication_reason | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| C01 | ACCEPT | ACCEPT | true | ACCEPT | No material reasoning defect on supplied packet. | Q13;Q14;Q15;Q01 |
| C02 | ACCEPT | REWORK | false | REWORK | Material contrary evidence omitted; outcome must be reconsidered without assuming reversal. | Q13;Q14;Q15;Q02 |
| C03 | REWORK | REWORK | true | REWORK | Correct net 9000 and review conclusion dependent on the error. | Q13;Q14;Q15;Q03 |
| C04 | REWORK | REWORK | true | REWORK | Split identities and recompute aggregate before reassessing. | Q13;Q14;Q15;Q04 |
| C05 | ACCEPT | ACCEPT | true | ACCEPT | Optional editorial correction; no effect on inference or traceability. | Q13;Q14;Q15;Q05 |
| C06 | REWORK | ACCEPT | false | REWORK | Restore both gross events and recompute period totals; net 500 does not excuse omission. | Q13;Q14;Q15;Q06 |
| C07 | ACCEPT | ACCEPT | true | ACCEPT | Properly bounded analysis; unknown is not itself a quality failure. | Q13;Q14;Q15;Q07 |
| C08 | INSUFFICIENT | INSUFFICIENT | true | INSUFFICIENT | Review cannot determine whether the underlying conclusion is supported. | Q13;Q14;Q15;Q08 |
| C09 | ACCEPT | ACCEPT | true | ACCEPT | Style preference alone is not a defect. | Q13;Q14;Q15;Q09 |
| C10 | REWORK | REWORK | true | REWORK | Remove unsupported intent assertion and reconsider bounded analytical conclusion. | Q13;Q14;Q15;Q10 |
| C11 | ACCEPT | INSUFFICIENT | false | REWORK | Use supplied policy CP-QA-1 and actual case rationale; no universal nonfiling memo requirement. | Q13;Q14;Q15;Q11 |
| C12 | INSUFFICIENT | INSUFFICIENT | true | INSUFFICIENT | Cannot assess original decision under hindsight without an availability chronology. | Q13;Q14;Q15;Q12 |

### Remediation

| remediation_id | defect_id | repair | closure_test | status | evidence_ids |
| --- | --- | --- | --- | --- | --- |
| M01 | D01 | Evaluate matched invoice and delivery as counterevidence. | Revised rationale addresses both sides and any outcome change. | PROPOSED | Q02;Q16 |
| M02 | D02 | Correct gross 11000, return 2000 and net 9000. | Recalculate from posted records and inspect affected conclusion. | PROPOSED | Q03;Q16 |
| M03 | D03 | Split unsupported merged subjects. | Recompute separate aggregates and verify each identity link. | PROPOSED | Q04;Q16 |
| M04 | D04 | Optionally correct punctuation without altering analytical outcome. | Evidence title remains resolvable; no material rework needed. | PROPOSED | Q05;Q16 |
| M05 | D05 | Restore omitted credit 4000 and debit 3500. | Reconcile gross flows, net 500 and chronology. | PROPOSED | Q06;Q16 |
| M06 | D06 | Replace unsupported intent assertion with bounded observed pattern. | Every remaining proposition matches its evidence class. | PROPOSED | Q10;Q16 |
| M07 | D07 | Apply CP-QA-1 brief-rationale criterion and remove invented legal premise. | Assess actual rationale under supplied policy; no automatic regulatory finding. | PROPOSED | Q11;Q15;Q16 |

### DecisionRecord

| decision_id | question | status | basis | evidence_ids |
| --- | --- | --- | --- | --- |
| D01 | Calibration consensus | RECORDED | 4 ACCEPT,6 REWORK,2 INSUFFICIENT across 12 selected packets | Q14 |
| D02 | Population defect rate | INSUFFICIENT | Deliberate calibration selection does not support population-rate extrapolation | Q15 |
| D03 | Underlying alert or filing dispositions | NOT_RECORDED | Quality consensus does not decide customer conduct or SAR outcome | Q15 |
| D04 | Remediation closure | NOT_RECORDED | Seven proposals exist; no executed repair or closure verification supplied | Q16 |

### ProcessQA

| check_id | check | expected | actual | result | evidence_ids |
| --- | --- | --- | --- | --- | --- |
| Q01 | Packet and vote counts | 12 packets;24 votes | 12 / 24 | PASS | Q13 |
| Q02 | Original agreement | 9 of 12;75.0% | 9 / 12 =75.0% | PASS | Q13 |
| Q03 | Reviewer marginals | R1 6/4/2; R2 5/4/3 | 6/4/2;5/4/3 | PASS | Q13 |
| Q04 | Chance agreement | 52/144 =36.1111% | 52/144 | PASS | Q13 |
| Q05 | Cohen kappa | 14/23 =0.6086956522 | 14/23 | PASS | Q13 |
| Q06 | Consensus denominator | 4/12 ACCEPT;6/12 REWORK;2/12 INSUFFICIENT | 33.3%;50.0%;16.7% | PASS | Q14 |
| Q07 | Material defect cases | 6 of 10 assessable;6 of 12 selected | 60.0% assessable;50.0% selected | PASS | Q14;Q15 |
| Q08 | Defect counts | 7 defects:6 material,1 nonmaterial | 7 / 6 / 1 | PASS | Q14;Q15 |
| Q09 | Unknown treatment | C08/C12 not counted as passes | INSUFFICIENT retained | PASS | Q08;Q12;Q14 |
| Q10 | Closure authority | No executed correction or closure | NOT_RECORDED | NOT RECORDED | Q16 |

## Complete expected report narrative

This is the populated fictional report body, in the exact eight-section order. It gives a complete narrative answer while the domain registers above supply all underlying rows. Adaptation requires new source-based paragraphs, not cosmetic changes to these conclusions.

### Quality decision and open gates

The calibration set contains four acceptable packets, six requiring substantive rework and two unassessable packets. Original reviewer agreement is 75.0% with kappa 0.6087; consensus preserves rather than replaces the original disagreements.

### Scope, supplied criteria and review design

Twelve deliberately selected fictional case packets, two original blind reviewers each, supplied illustrative policy CP-QA-1 and a separate consensus round. No random sample or population estimate.

The supplied rubric separates material reasoning defects, reviewability limitations and nonmaterial presentation issues. Criteria are illustrative internal policy and must not be described as universal legal requirements.

### Material and nonmaterial findings

AQA-F01: Consensus identifies six material-defect cases among twelve deliberately selected packets. This is 50.0% of selected packets or 60.0% of ten assessable packets; it is not a population defect estimate.

AQA-F02: C08 lacks accessible cited evidence; C12 lacks decision-time availability chronology. Neither is counted as an acceptable case or a demonstrated investigator defect.

AQA-F03: Original votes agree on 9/12 cases (75.0%); unweighted Cohen kappa is 14/23, approximately 0.6087. Adjudication later produces consensus without erasing three disagreements.

AQA-F04: C05 has one punctuation defect without effect on calculation, evidence linkage or conclusion. Its consensus status remains ACCEPT under the fixture rubric.

### Case packets and original review votes

C01–C12 are the complete selected packet population. Twenty-four original votes are retained before adjudication. Reviewers agree on C01/C03/C04/C05/C07/C08/C09/C10/C12 and disagree on C02/C06/C11.

### Criteria, defects, calibration and remediation

R1 marginals are 6 ACCEPT,4 REWORK,2 INSUFFICIENT; R2 marginals are 5/4/3. Chance agreement is(6×5+4×4+2×3)/144=52/144. Kappa is(9/12-52/144)/(1-52/144)=14/23. No universal adequacy threshold is applied.

Consensus produces 4 ACCEPT,6 REWORK and 2 INSUFFICIENT. Seven demonstrated defects include 6 material and 1 nonmaterial across 7 cases. Six material cases divide by 12 selected packets for 50.0% or 10 assessable packets for 60.0%; the two unknowns are explicit in both presentations.

Seven repairs are proposed with case-specific closure tests. C05 stays ACCEPT because its punctuation defect has no substantive effect. C08/C12 require reviewability inputs, not invented investigator-error findings.

### Evidence and decision-time provenance

Q01–Q12 are the individual packets; Q13 preserves original votes; Q14 records later consensus; Q15 supplies the illustrative criteria; Q16 contains proposed remediation. Original decision-time availability must be established before applying later evidence to a prior adjudication.

### Proposed repairs and closure tests

Correct omitted counterevidence, reversal arithmetic, unsupported identity merging, incomplete chronology, unsupported intent and criterion provenance. Obtain accessible evidence for C08 and a decision-time availability chronology for C12. Keep all repairs proposed until execution and independent verification are supplied.

### Quality checks, limitations and human disposition

All case packets, reviewers, decisions and policy are fictional.

Deliberate calibration selection does not support a population defect estimate or statistical assurance.

Quality consensus does not determine suspicious activity, customer conduct or filing obligations.

C08/C12 cannot be assessed until their reviewability gaps are resolved.

No proposed repair has been executed and no actual authorized closure has been supplied.

Fixture metrics reperform correctly. Human business disposition and remediation closure remain NOT_RECORDED.

### Complete finding statements

**AQA-F01 — Six packets need substantive rework under the fixture rubric.** Severity `HIGH`; confidence `HIGH`; claim class `Observed`. Evidence: Q02, Q03, Q04, Q06, Q10, Q11, Q14, Q15. Consensus identifies six material-defect cases among twelve deliberately selected packets. This is 50.0% of selected packets or 60.0% of ten assessable packets; it is not a population defect estimate. Proposed action: Correct each case-specific defect and reperform its closure test before claiming repair. Actual human decision: NOT_RECORDED.

**AQA-F02 — Two packets remain unassessable.** Severity `MEDIUM`; confidence `HIGH`; claim class `Observed`. Evidence: Q08, Q12, Q14. C08 lacks accessible cited evidence; C12 lacks decision-time availability chronology. Neither is counted as an acceptable case or a demonstrated investigator defect. Proposed action: Obtain the missing reviewability inputs and reassess under the original decision-time frame. Actual human decision: NOT_RECORDED.

**AQA-F03 — Original reviewer agreement is incomplete.** Severity `MEDIUM`; confidence `HIGH`; claim class `Observed`. Evidence: Q13, Q14. Original votes agree on 9/12 cases (75.0%); unweighted Cohen kappa is 14/23, approximately 0.6087. Adjudication later produces consensus without erasing three disagreements. Proposed action: Use C02/C06/C11 for criterion calibration; preserve original votes and track later rounds separately. Actual human decision: NOT_RECORDED.

**AQA-F04 — One nonmaterial editorial defect does not require substantive rework.** Severity `LOW`; confidence `HIGH`; claim class `Observed`. Evidence: Q05, Q14, Q15. C05 has one punctuation defect without effect on calculation, evidence linkage or conclusion. Its consensus status remains ACCEPT under the fixture rubric. Proposed action: Record optional correction without treating style preference as a material quality failure. Actual human decision: NOT_RECORDED.

## Standalone in-session arithmetic and table reproduction

This block uses only the Python standard library and printed fixture inputs. Run it only if an approved Python capability already exists in the current session; no terminal, installation, repository file or network is required. It independently derives the quantitative tables, checks count/amount/denominator invariants and exposes CHECKED_TABLES for exact row comparison. Successful arithmetic does not validate every qualitative judgment or establish real human authorization.

<!-- FIXTURE_CHECK:START -->
```python
from collections import Counter
from fractions import Fraction
CASES = [('C01', 'Routine pass-through explanation', 'Posted debit 1000; invoice 1000; beneficiary and delivery match; counterevidence considered.', 'ACCEPT', 'No material reasoning defect on supplied packet.'), ('C02', 'Omitted contrary invoice', 'Investigator described no business support; packet includes matched invoice 2000 and delivery for the same payment.', 'REWORK', 'Material contrary evidence omitted; outcome must be reconsidered without assuming reversal.'), ('C03', 'Partial return treated as full reversal', 'Original debit 11000 and explicitly linked return 2000; narrative says fully reversed.', 'REWORK', 'Correct net 9000 and review conclusion dependent on the error.'), ('C04', 'Unsupported identity merge', 'Two beneficiaries have similar names but different supplied identifiers; investigator merged them into one subject.', 'REWORK', 'Split identities and recompute aggregate before reassessing.'), ('C05', 'Nonmaterial display defect', 'Ledger and narrative amounts match; one non-substantive punctuation defect in an evidence title.', 'ACCEPT', 'Optional editorial correction; no effect on inference or traceability.'), ('C06', 'Relevant timeline gap', 'Two same-period postings 4000 and 3500 omitted from chronology while present in supplied ledger; net effect 500.', 'REWORK', 'Restore both gross events and recompute period totals; net 500 does not excuse omission.'), ('C07', 'Bounded unknown handled correctly', 'Opening balance missing; investigator declines source attribution, requests balance and gives descriptive flows only.', 'ACCEPT', 'Properly bounded analysis; unknown is not itself a quality failure.'), ('C08', 'Source inaccessible', 'Case conclusion cites an encrypted document unavailable to either reviewer; no equivalent source supplied.', 'INSUFFICIENT', 'Review cannot determine whether the underlying conclusion is supported.'), ('C09', 'Different defensible wording', 'Narrative uses unresolved purpose; reviewer prefers insufficient corroboration; both reflect same evidence and scope.', 'ACCEPT', 'Style preference alone is not a defect.'), ('C10', 'Observed pattern overstates intent', 'Rapid onward transfers are evidenced; conclusion states intent to launder without supporting intent evidence.', 'REWORK', 'Remove unsupported intent assertion and reconsider bounded analytical conclusion.'), ('C11', 'Invented universal documentation rule', 'Reviewer worksheet treats absent nonfiling memorandum as a universal BSA breach; supplied fixture policy only requires a brief case rationale.', 'REWORK', 'Use supplied policy CP-QA-1 and actual case rationale; no universal nonfiling memo requirement.'), ('C12', 'Unknown historical cutoff', 'Packet does not identify what evidence was available at original decision date; reviewers see later documents mixed with earlier material.', 'INSUFFICIENT', 'Cannot assess original decision under hindsight without an availability chronology.')]
R1 = ['ACCEPT', 'ACCEPT', 'REWORK', 'REWORK', 'ACCEPT', 'REWORK', 'ACCEPT', 'INSUFFICIENT', 'ACCEPT', 'REWORK', 'ACCEPT', 'INSUFFICIENT']
R2 = ['ACCEPT', 'REWORK', 'REWORK', 'REWORK', 'ACCEPT', 'ACCEPT', 'ACCEPT', 'INSUFFICIENT', 'ACCEPT', 'REWORK', 'INSUFFICIENT', 'INSUFFICIENT']
DEFECTS = [('D01', 'C02', 'K04', 'MEDIUM', 'MATERIAL', 'Contrary matched invoice and delivery omitted', 'Q02;Q15'), ('D02', 'C03', 'K02', 'HIGH', 'MATERIAL', 'USD11000 minus USD2000 is USD9000, not zero', 'Q03;Q15'), ('D03', 'C04', 'K03', 'HIGH', 'MATERIAL', 'Unsupported subject merge changes aggregation', 'Q04;Q15'), ('D04', 'C05', 'K08', 'LOW', 'NONMATERIAL', 'Punctuation correction does not affect meaning', 'Q05;Q15'), ('D05', 'C06', 'K01', 'MEDIUM', 'MATERIAL', 'Gross4000 credit and3500 debit omitted; net500', 'Q06;Q15'), ('D06', 'C10', 'K05', 'HIGH', 'MATERIAL', 'Intent claim exceeds evidence of timing', 'Q10;Q15'), ('D07', 'C11', 'K06', 'MEDIUM', 'MATERIAL', 'Universal regulatory documentation premise unsupported', 'Q11;Q15')]
assert len(CASES)==len(R1)==len(R2)==12
votes=[]; calibration=[]
for i,case in enumerate(CASES):
    cid,topic,raw,consensus,reason=case
    for j,rating in enumerate((R1[i],R2[i])):
        votes.append([f'V{i*2+j+1:02}',cid,f'R{j+1}',rating,1,'Q13;Q'+f'{i+1:02}'])
    calibration.append([cid,R1[i],R2[i],R1[i]==R2[i],consensus,reason,'Q13;Q14;Q15;Q'+f'{i+1:02}'])
a,b=Counter(R1),Counter(R2); n=len(CASES)
agreement=sum(x==y for x,y in zip(R1,R2))
po=Fraction(agreement,n)
pe=sum((Fraction(a[c]*b[c],n*n) for c in ('ACCEPT','REWORK','INSUFFICIENT')),Fraction(0))
kappa=(po-pe)/(1-pe) if pe!=1 else None
assert (agreement,po,pe,kappa)==(9,Fraction(3,4),Fraction(13,36),Fraction(14,23))
assert [a[x] for x in ('ACCEPT','REWORK','INSUFFICIENT')]==[6,4,2]
assert [b[x] for x in ('ACCEPT','REWORK','INSUFFICIENT')]==[5,4,3]
consensus=Counter(c[3] for c in CASES)
assert [consensus[x] for x in ('ACCEPT','REWORK','INSUFFICIENT')]==[4,6,2]
material={d[1] for d in DEFECTS if d[4]=='MATERIAL'}
assert len(DEFECTS)==7 and len(material)==6
assert Fraction(len(material),n)==Fraction(1,2)
assert Fraction(len(material),n-consensus['INSUFFICIENT'])==Fraction(3,5)
assert 11000-2000==9000 and 4000-3500==500
# Add a second material defect on an existing case: defect count changes, case rate does not.
more=DEFECTS+[('D08','C03','K05','HIGH','MATERIAL','Additional demonstrated issue','Q03;Q15')]
assert len(more)==8 and len({d[1] for d in more if d[4]=='MATERIAL'})==6
# Uniform single-category ratings yield undefined kappa, not one.
uniform_pe=Fraction(12*12,12*12)
assert uniform_pe==1
assert sum(x==y for x,y in zip(R1[:-1],R2[:-1]))==8
CHECKED_TABLES={'ReviewVotes':votes,'Calibration':calibration}
print('PASS: packets12; votes24; agreement9/12; Pe52/144; kappa14/23; consensus4/6/2; material6/10 assessable')
```
<!-- FIXTURE_CHECK:END -->
