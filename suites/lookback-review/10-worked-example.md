# Fully populated worked example — Historical Monitoring Lookback and Remediation Review

**Fictional records only.** The inputs below are deliberately constructed to demonstrate the full method, adverse branches and incomplete decision gates. They are not customer data, a real validation or evidence of an institution's control quality. All parameters are illustrative. The supplied cutoff is Oct 09, 2026.

A historical monitoring lookback asks which past activity or reviews may have been affected by a known or suspected defect, what evidence can be recovered, which units require fresh analysis, and what remains unresolved before completion can be claimed. It is not merely a rerun of current rules on an old extract. Current logic, historical customer context, historical source availability, prior decisions and later-discovered evidence must remain distinguishable. The review should preserve a defensible record of both what was known then and what is known now.

The worked case starts with an independent 30-unit manifest across January through June 2026. Retrieval provides 34 raw representations:29 canonical in-scope records,3 duplicates and 2 July exclusions. One June unit is absent. The current states include completed no-new-information comparisons, referrals, re-reviews, pending reviews, unassessable summaries and the missing unit. The case makes a deliberately incomplete conclusion because intake reconciliation is not the same as full population coverage, completed review or downstream disposition.

## Independent source declarations

SYN-201 independently lists L01 through L30, five units per month from January through June. SYN-202 is the complete received representation list printed inRetrievalLedger. The source amount formula for retrieved L01 through L29 is 1000 times the unit number plus 500 USD; it is a fixture construction rule, not an inference for missing L30. SYN-203 supplies the complete review-state inputs. SYN-204 states that a mapping-defect chronology supports analytical review through June whileJuly continuity remains unresolved. No actual institutional scope approval is supplied.

| period | independent expected IDs | expected_n |
| --- | --- | --- |
| 2026-01 | L01,L02,L03,L04,L05 | 5 |
| 2026-02 | L06,L07,L08,L09,L10 | 5 |
| 2026-03 | L11,L12,L13,L14,L15 | 5 |
| 2026-04 | L16,L17,L18,L19,L20 | 5 |
| 2026-05 | L21,L22,L23,L24,L25 | 5 |
| 2026-06 | L26,L27,L28,L29,L30 | 5 |

The original discovery review consideredJanuary through March. This completed analytical fixture includesApril through June to examine the stated potential continuation, but its expansion register leaves actual human acceptance unrecorded. July rows RAW-X31 and RAW-X32 are retained outside current totals. The complete rawledger preserves duplicates and missing-unit limitations, so there is no need to infer whether the displayed population was silently reduced.

## Complete populated output registers

### PeriodReconciliation

| period | expected_units | retrieved_rows | duplicate_rows | retrieved_units | missing_units | known_amount_usd | coverage_state | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-01 | 5 | 6 | 1 | 5 | 0 | 17500 | RECONCILED | SYN-201;SYN-202 |
| 2026-02 | 5 | 5 | 0 | 5 | 0 | 42500 | RECONCILED | SYN-201;SYN-202 |
| 2026-03 | 5 | 6 | 1 | 5 | 0 | 67500 | RECONCILED | SYN-201;SYN-202 |
| 2026-04 | 5 | 5 | 0 | 5 | 0 | 92500 | RECONCILED | SYN-201;SYN-202 |
| 2026-05 | 5 | 6 | 1 | 5 | 0 | 117500 | RECONCILED | SYN-201;SYN-202 |
| 2026-06 | 5 | 4 | 0 | 4 | 1 | 112000 | PARTIAL | SYN-201;SYN-202 |

### CanonicalUnits

| unit_id | period | source_id | amount_usd | original_state | defect_affected | review_state | new_information | priority | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L01 | 2026-01 | RAW-01 | 1500 | CLOSED | true | REVIEW_COMPLETE_NO_NEW | false | MEDIUM | SYN-201;SYN-202;SYN-205 |
| L02 | 2026-01 | RAW-02 | 2500 | ESCALATED | true | REVIEW_COMPLETE_NO_NEW | false | MEDIUM | SYN-201;SYN-202;SYN-205 |
| L03 | 2026-01 | RAW-03 | 3500 | NOT_GENERATED | false | REVIEW_COMPLETE_NO_NEW | false | MEDIUM | SYN-201;SYN-202;SYN-205 |
| L04 | 2026-01 | RAW-04 | 4500 | CLOSED | true | REVIEW_COMPLETE_NO_NEW | false | MEDIUM | SYN-201;SYN-202;SYN-205 |
| L05 | 2026-01 | RAW-05 | 5500 | ESCALATED | true | REVIEW_COMPLETE_NO_NEW | false | MEDIUM | SYN-201;SYN-202;SYN-205 |
| L06 | 2026-02 | RAW-06 | 6500 | NOT_GENERATED | false | REVIEW_COMPLETE_NO_NEW | false | MEDIUM | SYN-201;SYN-202;SYN-205 |
| L07 | 2026-02 | RAW-07 | 7500 | CLOSED | true | REFERRED_FOR_CASE_REVIEW | true | HIGH | SYN-201;SYN-202;SYN-205 |
| L08 | 2026-02 | RAW-08 | 8500 | ESCALATED | true | REFERRED_FOR_CASE_REVIEW | true | HIGH | SYN-201;SYN-202;SYN-205 |
| L09 | 2026-02 | RAW-09 | 9500 | NOT_GENERATED | false | REFERRED_FOR_CASE_REVIEW | true | HIGH | SYN-201;SYN-202;SYN-205 |
| L10 | 2026-02 | RAW-10 | 10500 | CLOSED | true | REFERRED_FOR_CASE_REVIEW | true | HIGH | SYN-201;SYN-202;SYN-205 |
| L11 | 2026-03 | RAW-11 | 11500 | ESCALATED | true | REFERRED_FOR_CASE_REVIEW | true | HIGH | SYN-201;SYN-202;SYN-205 |
| L12 | 2026-03 | RAW-12 | 12500 | NOT_GENERATED | false | REFERRED_FOR_CASE_REVIEW | true | HIGH | SYN-201;SYN-202;SYN-205 |
| L13 | 2026-03 | RAW-13 | 13500 | CLOSED | true | REREVIEW_REQUIRED | null | HIGH | SYN-201;SYN-202 |
| L14 | 2026-03 | RAW-14 | 14500 | ESCALATED | true | REREVIEW_REQUIRED | null | HIGH | SYN-201;SYN-202 |
| L15 | 2026-03 | RAW-15 | 15500 | NOT_GENERATED | false | REREVIEW_REQUIRED | null | HIGH | SYN-201;SYN-202 |
| L16 | 2026-04 | RAW-16 | 16500 | CLOSED | true | REREVIEW_REQUIRED | null | HIGH | SYN-201;SYN-202 |
| L17 | 2026-04 | RAW-17 | 17500 | ESCALATED | true | REREVIEW_REQUIRED | null | HIGH | SYN-201;SYN-202 |
| L18 | 2026-04 | RAW-18 | 18500 | NOT_GENERATED | false | REREVIEW_REQUIRED | null | HIGH | SYN-201;SYN-202 |
| L19 | 2026-04 | RAW-19 | 19500 | CLOSED | true | PENDING_REVIEW | null | MEDIUM | SYN-201;SYN-202 |
| L20 | 2026-04 | RAW-20 | 20500 | ESCALATED | true | PENDING_REVIEW | null | MEDIUM | SYN-201;SYN-202 |
| L21 | 2026-05 | RAW-21 | 21500 | NOT_GENERATED | false | PENDING_REVIEW | null | MEDIUM | SYN-201;SYN-202 |
| L22 | 2026-05 | RAW-22 | 22500 | CLOSED | true | PENDING_REVIEW | null | MEDIUM | SYN-201;SYN-202 |
| L23 | 2026-05 | RAW-23 | 23500 | ESCALATED | true | PENDING_REVIEW | null | MEDIUM | SYN-201;SYN-202 |
| L24 | 2026-05 | RAW-24 | 24500 | NOT_GENERATED | false | PENDING_REVIEW | null | MEDIUM | SYN-201;SYN-202 |
| L25 | 2026-05 | RAW-25 | 25500 | CLOSED | true | UNABLE_TO_ASSESS | null | HIGH | SYN-201;SYN-202 |
| L26 | 2026-06 | RAW-26 | 26500 | ESCALATED | true | UNABLE_TO_ASSESS | null | HIGH | SYN-201;SYN-202 |
| L27 | 2026-06 | RAW-27 | 27500 | NOT_GENERATED | false | UNABLE_TO_ASSESS | null | HIGH | SYN-201;SYN-202 |
| L28 | 2026-06 | RAW-28 | 28500 | CLOSED | true | UNABLE_TO_ASSESS | null | HIGH | SYN-201;SYN-202 |
| L29 | 2026-06 | RAW-29 | 29500 | ESCALATED | true | UNABLE_TO_ASSESS | null | HIGH | SYN-201;SYN-202 |
| L30 | 2026-06 | null | null | UNKNOWN | null | NOT_RETRIEVED | null | HIGH | SYN-201 |

### RetrievalLedger

| raw_id | unit_id | source_period | classification | canonical_id | raw_amount_usd | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| RAW-01 | L01 | 2026-01 | CANONICAL | L01 | 1500 | SYN-202 |
| RAW-02 | L02 | 2026-01 | CANONICAL | L02 | 2500 | SYN-202 |
| RAW-03 | L03 | 2026-01 | CANONICAL | L03 | 3500 | SYN-202 |
| RAW-04 | L04 | 2026-01 | CANONICAL | L04 | 4500 | SYN-202 |
| RAW-05 | L05 | 2026-01 | CANONICAL | L05 | 5500 | SYN-202 |
| RAW-06 | L06 | 2026-02 | CANONICAL | L06 | 6500 | SYN-202 |
| RAW-07 | L07 | 2026-02 | CANONICAL | L07 | 7500 | SYN-202 |
| RAW-08 | L08 | 2026-02 | CANONICAL | L08 | 8500 | SYN-202 |
| RAW-09 | L09 | 2026-02 | CANONICAL | L09 | 9500 | SYN-202 |
| RAW-10 | L10 | 2026-02 | CANONICAL | L10 | 10500 | SYN-202 |
| RAW-11 | L11 | 2026-03 | CANONICAL | L11 | 11500 | SYN-202 |
| RAW-12 | L12 | 2026-03 | CANONICAL | L12 | 12500 | SYN-202 |
| RAW-13 | L13 | 2026-03 | CANONICAL | L13 | 13500 | SYN-202 |
| RAW-14 | L14 | 2026-03 | CANONICAL | L14 | 14500 | SYN-202 |
| RAW-15 | L15 | 2026-03 | CANONICAL | L15 | 15500 | SYN-202 |
| RAW-16 | L16 | 2026-04 | CANONICAL | L16 | 16500 | SYN-202 |
| RAW-17 | L17 | 2026-04 | CANONICAL | L17 | 17500 | SYN-202 |
| RAW-18 | L18 | 2026-04 | CANONICAL | L18 | 18500 | SYN-202 |
| RAW-19 | L19 | 2026-04 | CANONICAL | L19 | 19500 | SYN-202 |
| RAW-20 | L20 | 2026-04 | CANONICAL | L20 | 20500 | SYN-202 |
| RAW-21 | L21 | 2026-05 | CANONICAL | L21 | 21500 | SYN-202 |
| RAW-22 | L22 | 2026-05 | CANONICAL | L22 | 22500 | SYN-202 |
| RAW-23 | L23 | 2026-05 | CANONICAL | L23 | 23500 | SYN-202 |
| RAW-24 | L24 | 2026-05 | CANONICAL | L24 | 24500 | SYN-202 |
| RAW-25 | L25 | 2026-05 | CANONICAL | L25 | 25500 | SYN-202 |
| RAW-26 | L26 | 2026-06 | CANONICAL | L26 | 26500 | SYN-202 |
| RAW-27 | L27 | 2026-06 | CANONICAL | L27 | 27500 | SYN-202 |
| RAW-28 | L28 | 2026-06 | CANONICAL | L28 | 28500 | SYN-202 |
| RAW-29 | L29 | 2026-06 | CANONICAL | L29 | 29500 | SYN-202 |
| RAW-D1 | L02 | 2026-01 | DUPLICATE | L02 | 2500 | SYN-202 |
| RAW-D2 | L12 | 2026-03 | DUPLICATE | L12 | 12500 | SYN-202 |
| RAW-D3 | L22 | 2026-05 | DUPLICATE | L22 | 22500 | SYN-202 |
| RAW-X31 | null | 2026-07 | OUT_OF_SCOPE | null | 31500 | SYN-202 |
| RAW-X32 | null | 2026-07 | OUT_OF_SCOPE | null | 32500 | SYN-202 |

### ReviewActions

| action_id | unit_id | review_state | action_state | observed_basis | required_next_step | comparison_id | human_disposition | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LA-L01 | L01 | REVIEW_COMPLETE_NO_NEW | DESK_REVIEW_COMPLETE | Fictional re-review found no new information within supplied scope | Preserve comparison and independent QA; no filing judgment inferred | COMP-L01 | NOT_RECORDED | SYN-203;SYN-205 |
| LA-L02 | L02 | REVIEW_COMPLETE_NO_NEW | DESK_REVIEW_COMPLETE | Fictional re-review found no new information within supplied scope | Preserve comparison and independent QA; no filing judgment inferred | COMP-L02 | NOT_RECORDED | SYN-203;SYN-205 |
| LA-L03 | L03 | REVIEW_COMPLETE_NO_NEW | DESK_REVIEW_COMPLETE | Fictional re-review found no new information within supplied scope | Preserve comparison and independent QA; no filing judgment inferred | COMP-L03 | NOT_RECORDED | SYN-203;SYN-205 |
| LA-L04 | L04 | REVIEW_COMPLETE_NO_NEW | DESK_REVIEW_COMPLETE | Fictional re-review found no new information within supplied scope | Preserve comparison and independent QA; no filing judgment inferred | COMP-L04 | NOT_RECORDED | SYN-203;SYN-205 |
| LA-L05 | L05 | REVIEW_COMPLETE_NO_NEW | DESK_REVIEW_COMPLETE | Fictional re-review found no new information within supplied scope | Preserve comparison and independent QA; no filing judgment inferred | COMP-L05 | NOT_RECORDED | SYN-203;SYN-205 |
| LA-L06 | L06 | REVIEW_COMPLETE_NO_NEW | DESK_REVIEW_COMPLETE | Fictional re-review found no new information within supplied scope | Preserve comparison and independent QA; no filing judgment inferred | COMP-L06 | NOT_RECORDED | SYN-203;SYN-205 |
| LA-L07 | L07 | REFERRED_FOR_CASE_REVIEW | HANDOFF_OPEN | New information exists in comparison packet | Obtain authorized case review acknowledgment and decision evidence | COMP-L07 | NOT_RECORDED | SYN-203;SYN-205 |
| LA-L08 | L08 | REFERRED_FOR_CASE_REVIEW | HANDOFF_OPEN | New information exists in comparison packet | Obtain authorized case review acknowledgment and decision evidence | COMP-L08 | NOT_RECORDED | SYN-203;SYN-205 |
| LA-L09 | L09 | REFERRED_FOR_CASE_REVIEW | HANDOFF_OPEN | New information exists in comparison packet | Obtain authorized case review acknowledgment and decision evidence | COMP-L09 | NOT_RECORDED | SYN-203;SYN-205 |
| LA-L10 | L10 | REFERRED_FOR_CASE_REVIEW | HANDOFF_OPEN | New information exists in comparison packet | Obtain authorized case review acknowledgment and decision evidence | COMP-L10 | NOT_RECORDED | SYN-203;SYN-205 |
| LA-L11 | L11 | REFERRED_FOR_CASE_REVIEW | HANDOFF_OPEN | New information exists in comparison packet | Obtain authorized case review acknowledgment and decision evidence | COMP-L11 | NOT_RECORDED | SYN-203;SYN-205 |
| LA-L12 | L12 | REFERRED_FOR_CASE_REVIEW | HANDOFF_OPEN | New information exists in comparison packet | Obtain authorized case review acknowledgment and decision evidence | COMP-L12 | NOT_RECORDED | SYN-203;SYN-205 |
| LA-L13 | L13 | REREVIEW_REQUIRED | REVIEW_OPEN | Prior reasoning does not address changed defect context | Reperform analysis against recovered evidence and preserve original rationale | null | NOT_RECORDED | SYN-203 |
| LA-L14 | L14 | REREVIEW_REQUIRED | REVIEW_OPEN | Prior reasoning does not address changed defect context | Reperform analysis against recovered evidence and preserve original rationale | null | NOT_RECORDED | SYN-203 |
| LA-L15 | L15 | REREVIEW_REQUIRED | REVIEW_OPEN | Prior reasoning does not address changed defect context | Reperform analysis against recovered evidence and preserve original rationale | null | NOT_RECORDED | SYN-203 |
| LA-L16 | L16 | REREVIEW_REQUIRED | REVIEW_OPEN | Prior reasoning does not address changed defect context | Reperform analysis against recovered evidence and preserve original rationale | null | NOT_RECORDED | SYN-203 |
| LA-L17 | L17 | REREVIEW_REQUIRED | REVIEW_OPEN | Prior reasoning does not address changed defect context | Reperform analysis against recovered evidence and preserve original rationale | null | NOT_RECORDED | SYN-203 |
| LA-L18 | L18 | REREVIEW_REQUIRED | REVIEW_OPEN | Prior reasoning does not address changed defect context | Reperform analysis against recovered evidence and preserve original rationale | null | NOT_RECORDED | SYN-203 |
| LA-L19 | L19 | PENDING_REVIEW | REVIEW_OPEN | No completed desk review record supplied | Assign reviewer and preserve priority; completion cannot be inferred | null | NOT_RECORDED | SYN-203 |
| LA-L20 | L20 | PENDING_REVIEW | REVIEW_OPEN | No completed desk review record supplied | Assign reviewer and preserve priority; completion cannot be inferred | null | NOT_RECORDED | SYN-203 |
| LA-L21 | L21 | PENDING_REVIEW | REVIEW_OPEN | No completed desk review record supplied | Assign reviewer and preserve priority; completion cannot be inferred | null | NOT_RECORDED | SYN-203 |
| LA-L22 | L22 | PENDING_REVIEW | REVIEW_OPEN | No completed desk review record supplied | Assign reviewer and preserve priority; completion cannot be inferred | null | NOT_RECORDED | SYN-203 |
| LA-L23 | L23 | PENDING_REVIEW | REVIEW_OPEN | No completed desk review record supplied | Assign reviewer and preserve priority; completion cannot be inferred | null | NOT_RECORDED | SYN-203 |
| LA-L24 | L24 | PENDING_REVIEW | REVIEW_OPEN | No completed desk review record supplied | Assign reviewer and preserve priority; completion cannot be inferred | null | NOT_RECORDED | SYN-203 |
| LA-L25 | L25 | UNABLE_TO_ASSESS | EVIDENCE_BLOCKED | Retrieved summary lacks essential supporting evidence | Recover missing support or record qualified scope limitation | null | NOT_RECORDED | SYN-203 |
| LA-L26 | L26 | UNABLE_TO_ASSESS | EVIDENCE_BLOCKED | Retrieved summary lacks essential supporting evidence | Recover missing support or record qualified scope limitation | null | NOT_RECORDED | SYN-203 |
| LA-L27 | L27 | UNABLE_TO_ASSESS | EVIDENCE_BLOCKED | Retrieved summary lacks essential supporting evidence | Recover missing support or record qualified scope limitation | null | NOT_RECORDED | SYN-203 |
| LA-L28 | L28 | UNABLE_TO_ASSESS | EVIDENCE_BLOCKED | Retrieved summary lacks essential supporting evidence | Recover missing support or record qualified scope limitation | null | NOT_RECORDED | SYN-203 |
| LA-L29 | L29 | UNABLE_TO_ASSESS | EVIDENCE_BLOCKED | Retrieved summary lacks essential supporting evidence | Recover missing support or record qualified scope limitation | null | NOT_RECORDED | SYN-203 |
| LA-L30 | L30 | NOT_RETRIEVED | RETRIEVAL_BLOCKED | Control manifest names a unit absent from retrieval | Recover archive record or retain unreconciled coverage gap | null | NOT_RECORDED | SYN-203 |

### ExpansionDecisions

| expansion_id | trigger | proposed_scope | inclusion_rule | stopping_condition | decision_state | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| EX-01 | Initial January through March review cannot exclude later mapping impact | Extend analytical fixture through June 30 | Manifest period 2026-04 through 2026-06 | Reconcile all fifteen added canonical units and impact evidence | PROPOSED | SYN-201;SYN-204 |
| EX-02 | L30 missing despite independent June control count | Recover June archive and linkage records | Canonical unit L30 plus source representations matching its key | L30 recovered or documented unreconciled coverage limitation remains | BLOCKED | SYN-201;SYN-202 |
| EX-03 | Six comparison packets identify new information | Route L07 through L12 to authorized case review | new_information=true | Acknowledged referral and later authorized decision evidence | PROPOSED | SYN-203 |
| EX-04 | Six prior reviews do not address revised defect context | Re-review L13 through L18 | review_state=REREVIEW_REQUIRED | Complete fresh comparison preserving historical record | PROPOSED | SYN-203 |
| EX-05 | Five retrieved summaries lack essential support | Recover support for L25 through L29 | review_state=UNABLE_TO_ASSESS | Support recovered and reviewed or qualified scope limit retained | BLOCKED | SYN-203 |
| EX-06 | July rows are outside current analytical boundary | Assess whether defect evidence crosses June 30 before adding July | Mapping continuity evidence beyond 2026-06-30 | Documented boundary evidence; no silent inclusion or dismissal | PROPOSED | SYN-202;SYN-204 |

### EvidenceProvenance

| source_id | source_kind | as_of | availability | unit_count | grain | limitation | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SYN-201 | SYNTHETIC_INPUT | 2026-10-09 | COMPLETE_FIXTURE | 30 | expected canonical historical units | Manifest counts do not supply absent record content. | SYN-201 |
| SYN-202 | SYNTHETIC_INPUT | 2026-10-09 | PARTIAL_FIXTURE | 34 | received representations including duplicates and exclusions | One expected canonical unit is missing; retrieved summaries may lack support. | SYN-202 |
| SYN-203 | SYNTHETIC_DECISION | 2026-10-09 | PARTIAL_FIXTURE | 30 | review-state assignments | Twelve desk comparisons complete; six have no open unit action; actual institutional disposition not supplied. | SYN-203 |
| SYN-204 | SYNTHETIC_INPUT | 2026-10-09 | PARTIAL_FIXTURE | 7 | dated mapping-version records | July continuity and actual production correction remain unverified. | SYN-204 |
| SYN-205 | SYNTHETIC_INPUT | 2026-10-09 | COMPLETE_FIXTURE | 12 | historical/current comparison packets | Completed desk comparison is separate from actual case disposition. | SYN-205 |

### ProcessQA

| check_id | check_scope | expected | actual | status | reviewer | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- |
| LB-Q01 | Raw intake accounting | 34=29 canonical+3 duplicate+2 out-of-scope | 34=29+3+2 | PASS | Fictional checker | SYN-202 |
| LB-Q02 | Expected scope accounting | 30=29 retrieved+1 missing | 30=29+1;L30 absent | PASS | Fictional checker | SYN-201;SYN-202 |
| LB-Q03 | Full retrieval coverage | All 30 expected units retrieved | 29/30 retrieved; June 4/5 | FAIL | Fictional checker | SYN-201;SYN-202 |
| LB-Q04 | Canonical amount conservation | Known amounts 449500; missing unit excluded explicitly | 449500 known; L30 amount null | PASS | Fictional checker | SYN-201;SYN-202 |
| LB-Q05 | Desk review completion | 6 no-new plus 6 referred =12 examined | 12/30 examined;6 handoffs still open | PASS | Fictional checker | SYN-203 |
| LB-Q06 | Whole-lookback completion | No material unresolved review retrieval or handoff | 24 units retain open dependency;6 desk-complete only | FAIL | Fictional checker | SYN-203 |
| LB-Q07 | No missing-to-negative conversion | L30 remains not retrieved and impact unknown | L30 source amount impact and new_information remain null | PASS | Fictional checker | SYN-201 |
| LB-Q08 | Filing or closure decision | Separate authorized human process required | NOT_RECORDED | NOT_TESTED | NOT_RECORDED | SYN-203 |

### CompletionGates

| gate_id | gate | numerator | denominator | state | residual | permitted_statement | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LB-G01 | Raw rows assigned an intake bucket | 34 | 34 | SATISFIED_FIXTURE_ONLY | None within supplied intake | All received rows classified; expected population still missing one | SYN-202 |
| LB-G02 | Expected canonical units retrieved | 29 | 30 | FAILED | L30 not retrieved | Retrieval coverage 29/30; no complete-coverage claim | SYN-201;SYN-202 |
| LB-G03 | Desk comparison completed | 12 | 30 | FAILED | 18 not desk-complete | 12 comparisons completed, including 6 unresolved referrals | SYN-203 |
| LB-G04 | Desk review with no open unit action | 6 | 30 | FAILED | 24 units retain review evidence retrieval or handoff dependency | 6 units have completed no-new-information comparisons | SYN-203 |
| LB-G05 | Referred units acknowledged and disposed | 0 | 6 | BLOCKED | No actual receiving-case decision evidence | Six handoffs remain open | SYN-203 |
| LB-G06 | Authorized whole-review acceptance | 0 | 1 | BLOCKED | Actual approval and accepted limitations absent | Lookback remains incomplete | SYN-203;SYN-204 |

## Historical comparison evidence and defect chronology

The sources below are complete fictional records, not assertions that an actual institution approved or completed this work. A material fact is defined for this example as a fact that changes a relevant identity, activity scope, purpose or evidential support for the historical rationale. Current fact sets are compared with the historical sets. The first six packets retain the same material facts; the next six add a specifically described material fact. An unchanged corrected monitoring count alone does not decide the comparison, and an affected mapping path does not itself establish a referral.

### ComparisonPackets

| comparison_id | unit_id | historical_cutoff | historical_source | historical_fact_ids | historical_facts | historical_rationale | recovered_date | recovered_source | current_fact_ids | current_observation | source_path | material_delta | expected_route | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| COMP-L01 | L01 | 2026-01-31 | HIST-L01 | L01-F1;L01-F2 | Payroll credits from two identified employers matched the supplied pay records. | The historical review already inspected both payer identities and pay records. | 2026-10-02 | REC-L01 | L01-F1;L01-F2 | Both payer identities, amounts and pay-record matches are unchanged; corrected monitoring count adds no unseen fact. | PATH_A | false | REVIEW_COMPLETE_NO_NEW | SYN-205 |
| COMP-L02 | L02 | 2026-01-31 | HIST-L02 | L02-F1;L02-F2 | Four originators and the complete activity were already included in the earlier escalation packet. | Historical escalation expressly covered all four identified originators. | 2026-10-02 | REC-L02 | L02-F1;L02-F2 | Recovered source messages match the four identities and activity already escalated; no additional party or transaction is found. | PATH_B | false | REVIEW_COMPLETE_NO_NEW | SYN-205 |
| COMP-L03 | L03 | 2026-01-31 | HIST-L03 | L03-F1;L03-F2 | One documented transfer from the same beneficial owner matched the account ownership evidence. | The correctly mapped control path produced no scenario hit and the underlying ownership fact was documented. | 2026-10-02 | REC-L03 | L03-F1;L03-F2 | The source-path replay and ownership documentation are unchanged. | PATH_C | false | REVIEW_COMPLETE_NO_NEW | SYN-205 |
| COMP-L04 | L04 | 2026-01-31 | HIST-L04 | L04-F1;L04-F2 | Three commercial payers matched the supplied invoices and recorded business counterparties. | Historical closure relied on inspected invoice and counterparty matches, not the defective aggregate alone. | 2026-10-02 | REC-L04 | L04-F1;L04-F2 | Recovered messages preserve the same three payers and invoice references with no contradiction. | PATH_A | false | REVIEW_COMPLETE_NO_NEW | SYN-205 |
| COMP-L05 | L05 | 2026-01-31 | HIST-L05 | L05-F1;L05-F2 | Five originators and their activity were fully described in the earlier escalation. | The historical packet included the source messages and all five counterparties. | 2026-10-02 | REC-L05 | L05-F1;L05-F2 | The replay identifies the same five parties already in that packet; no new transaction or identity is added. | PATH_B | false | REVIEW_COMPLETE_NO_NEW | SYN-205 |
| COMP-L06 | L06 | 2026-02-28 | HIST-L06 | L06-F1;L06-F2 | A single internal operating transfer matched the supplied account mapping. | The control path mapped the actual originator and the activity remained outside the scenario concept. | 2026-10-02 | REC-L06 | L06-F1;L06-F2 | The original source and current replay agree on the same internal account and purpose. | PATH_C | false | REVIEW_COMPLETE_NO_NEW | SYN-205 |
| COMP-L07 | L07 | 2026-02-28 | HIST-L07 | L07-F1;L07-F2 | The historical summary described all credits as transfers from the same customer-controlled account. | Closure relied on the one-originator summary and did not include underlying payment messages. | 2026-10-02 | REC-L07 | L07-F1;L07-F2;L07-F3 | Recovered messages identify four third-party originator IDs; three are absent from the historical packet and their purpose is unsupported. | PATH_A | true | REFERRED_FOR_CASE_REVIEW | SYN-205 |
| COMP-L08 | L08 | 2026-02-28 | HIST-L08 | L08-F1;L08-F2 | The prior escalation packet identified two originators and stated that it covered the complete relationship. | The earlier referral scope was limited to those two identities and their supplied activity. | 2026-10-02 | REC-L08 | L08-F1;L08-F2;L08-F3 | Recovered messages identify seven originators; five additional identities were outside the earlier scope. | PATH_B | true | REFERRED_FOR_CASE_REVIEW | SYN-205 |
| COMP-L09 | L09 | 2026-02-28 | HIST-L09 | L09-F1;L09-F2 | The control-path unit showed one payer and a supplier-payment explanation. | No scenario hit was generated; the supplied original packet contained the stated supplier rationale. | 2026-10-02 | REC-L09 | L09-F1;L09-F2;L09-F3 | A newly recovered contract names a different economic supplier than the payment message, creating an identity-purpose inconsistency unrelated to the mapping defect. | PATH_C | true | REFERRED_FOR_CASE_REVIEW | SYN-205 |
| COMP-L10 | L10 | 2026-02-28 | HIST-L10 | L10-F1;L10-F2 | The historical review treated the credits as customer self-funding based on the summary identity. | Closure relied on apparent common ownership without the underlying message identities. | 2026-10-02 | REC-L10 | L10-F1;L10-F2;L10-F3 | Five distinct third-party originators appear in recovered messages and the claimed ownership link is not supported. | PATH_A | true | REFERRED_FOR_CASE_REVIEW | SYN-205 |
| COMP-L11 | L11 | 2026-03-31 | HIST-L11 | L11-F1;L11-F2 | The prior escalation described three counterparties and excluded no known message records. | Its stated scope and rationale addressed those three named parties only. | 2026-10-02 | REC-L11 | L11-F1;L11-F2;L11-F3 | The corrected message grouping identifies three additional counterparties, including activity outside the original referral narrative. | PATH_B | true | REFERRED_FOR_CASE_REVIEW | SYN-205 |
| COMP-L12 | L12 | 2026-03-31 | HIST-L12 | L12-F1;L12-F2 | The control-path unit had one identified payer and an equipment-sale explanation. | The original source did not contradict the stated sale purpose and the monitoring predicate did not hit. | 2026-10-02 | REC-L12 | L12-F1;L12-F2;L12-F3 | A newly recovered invoice describes consulting services instead of equipment, creating a material purpose contradiction independent of mapping. | PATH_C | true | REFERRED_FOR_CASE_REVIEW | SYN-205 |

### Exact historical/current source facts

| fact_id | complete supplied fact |
| --- | --- |
| L01-F1 | Payroll credits from two identified employers matched the supplied pay records. |
| L01-F2 | The historical review already inspected both payer identities and pay records. |
| L02-F1 | Four originators and the complete activity were already included in the earlier escalation packet. |
| L02-F2 | Historical escalation expressly covered all four identified originators. |
| L03-F1 | One documented transfer from the same beneficial owner matched the account ownership evidence. |
| L03-F2 | The correctly mapped control path produced no scenario hit and the underlying ownership fact was documented. |
| L04-F1 | Three commercial payers matched the supplied invoices and recorded business counterparties. |
| L04-F2 | Historical closure relied on inspected invoice and counterparty matches, not the defective aggregate alone. |
| L05-F1 | Five originators and their activity were fully described in the earlier escalation. |
| L05-F2 | The historical packet included the source messages and all five counterparties. |
| L06-F1 | A single internal operating transfer matched the supplied account mapping. |
| L06-F2 | The control path mapped the actual originator and the activity remained outside the scenario concept. |
| L07-F1 | The historical summary described all credits as transfers from the same customer-controlled account. |
| L07-F2 | Closure relied on the one-originator summary and did not include underlying payment messages. |
| L07-F3 | Recovered messages identify four third-party originator IDs; three are absent from the historical packet and their purpose is unsupported. |
| L08-F1 | The prior escalation packet identified two originators and stated that it covered the complete relationship. |
| L08-F2 | The earlier referral scope was limited to those two identities and their supplied activity. |
| L08-F3 | Recovered messages identify seven originators; five additional identities were outside the earlier scope. |
| L09-F1 | The control-path unit showed one payer and a supplier-payment explanation. |
| L09-F2 | No scenario hit was generated; the supplied original packet contained the stated supplier rationale. |
| L09-F3 | A newly recovered contract names a different economic supplier than the payment message, creating an identity-purpose inconsistency unrelated to the mapping defect. |
| L10-F1 | The historical review treated the credits as customer self-funding based on the summary identity. |
| L10-F2 | Closure relied on apparent common ownership without the underlying message identities. |
| L10-F3 | Five distinct third-party originators appear in recovered messages and the claimed ownership link is not supported. |
| L11-F1 | The prior escalation described three counterparties and excluded no known message records. |
| L11-F2 | Its stated scope and rationale addressed those three named parties only. |
| L11-F3 | The corrected message grouping identifies three additional counterparties, including activity outside the original referral narrative. |
| L12-F1 | The control-path unit had one identified payer and an equipment-sale explanation. |
| L12-F2 | The original source did not contradict the stated sale purpose and the monitoring predicate did not hit. |
| L12-F3 | A newly recovered invoice describes consulting services instead of equipment, creating a material purpose contradiction independent of mapping. |

The no-new-information packets retain the historical material facts and describe the recovered evidence confirming them. Historical reviewers of L01, L02, L04 and L05 already possessed the underlying party information despite the defective monitoring aggregate. L03 and L06 use the unaffected control path. L09 and L12 use that same unaffected path but receive new purpose or identity evidence; their referrals therefore do not prove a mapping-driven miss. These are distinct causal explanations and must not be combined into a count of defects caused by MAP-1.

### DefectChronology

| chronology_id | event_date | source_locator | mapping_version | record_kind | observed_fact | boundary_limit | evidence_ids |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DC-01 | 2025-12-29 | CR-MAP-04 | MAP-1 | CHANGE_RECORD | Deployment plan enables PATH_A and PATH_B identity mapping on January01; PATH_C retains correct source-originator mapping. | Plan is not proof of runtime before January01. | SYN-204 |
| DC-02 | 2026-01-01 | CFG-JAN-01 | MAP-1 | RUNTIME_SNAPSHOT | PATH_A and PATH_B use customer_id instead of payment_originator_id in the monitoring originator key; PATH_C uses payment_originator_id. | The established mechanism can collapse distinct originators on affected paths. | SYN-204 |
| DC-03 | 2026-03-31 | CFG-MAR-31 | MAP-1 | RUNTIME_SNAPSHOT | The same two affected mappings remain active in the archived configuration. | Supports the initial January–March discovery scope, not a March end to exposure. | SYN-204 |
| DC-04 | 2026-06-30 | CFG-JUN-30 | MAP-1 | RUNTIME_SNAPSHOT | The affected PATH_A and PATH_B configuration is still present in the June archive. | Supports analytical extension through June; missing L30 still lacks its own source path. | SYN-204 |
| DC-05 | 2026-07-01 | CFG-JUL-MISSING | UNKNOWN | UNAVAILABLE | No July runtime configuration or mapping continuity evidence is supplied. | July exposure remains unresolved; received July records alone cannot settle the boundary. | SYN-204 |
| DC-06 | 2026-09-28 | REPRO-0928 | MAP-1 | DEFECT_REPRODUCTION | A separate reproduction confirms distinct payment-originator IDs collapse to the customer key on PATH_A and PATH_B. | Discovery date is not the exposure start date. | SYN-204 |
| DC-07 | 2026-10-01 | SANDBOX-MAP-2 | MAP-2 | PROPOSED_CORRECTION | Sandbox proposal maps PATH_A and PATH_B to payment_originator_id and preserves PATH_C. | No production deployment or acceptance is evidenced. | SYN-204 |

### SourcePathInputs

| unit_id | period | source_path | observed_mapping_version | source_locator |
| --- | --- | --- | --- | --- |
| L01 | 2026-01 | PATH_A | MAP-1 | RAW-01 |
| L02 | 2026-01 | PATH_B | MAP-1 | RAW-02 |
| L03 | 2026-01 | PATH_C | MAP-1 | RAW-03 |
| L04 | 2026-01 | PATH_A | MAP-1 | RAW-04 |
| L05 | 2026-01 | PATH_B | MAP-1 | RAW-05 |
| L06 | 2026-02 | PATH_C | MAP-1 | RAW-06 |
| L07 | 2026-02 | PATH_A | MAP-1 | RAW-07 |
| L08 | 2026-02 | PATH_B | MAP-1 | RAW-08 |
| L09 | 2026-02 | PATH_C | MAP-1 | RAW-09 |
| L10 | 2026-02 | PATH_A | MAP-1 | RAW-10 |
| L11 | 2026-03 | PATH_B | MAP-1 | RAW-11 |
| L12 | 2026-03 | PATH_C | MAP-1 | RAW-12 |
| L13 | 2026-03 | PATH_A | MAP-1 | RAW-13 |
| L14 | 2026-03 | PATH_B | MAP-1 | RAW-14 |
| L15 | 2026-03 | PATH_C | MAP-1 | RAW-15 |
| L16 | 2026-04 | PATH_A | MAP-1 | RAW-16 |
| L17 | 2026-04 | PATH_B | MAP-1 | RAW-17 |
| L18 | 2026-04 | PATH_C | MAP-1 | RAW-18 |
| L19 | 2026-04 | PATH_A | MAP-1 | RAW-19 |
| L20 | 2026-04 | PATH_B | MAP-1 | RAW-20 |
| L21 | 2026-05 | PATH_C | MAP-1 | RAW-21 |
| L22 | 2026-05 | PATH_A | MAP-1 | RAW-22 |
| L23 | 2026-05 | PATH_B | MAP-1 | RAW-23 |
| L24 | 2026-05 | PATH_C | MAP-1 | RAW-24 |
| L25 | 2026-05 | PATH_A | MAP-1 | RAW-25 |
| L26 | 2026-06 | PATH_B | MAP-1 | RAW-26 |
| L27 | 2026-06 | PATH_C | MAP-1 | RAW-27 |
| L28 | 2026-06 | PATH_A | MAP-1 | RAW-28 |
| L29 | 2026-06 | PATH_B | MAP-1 | RAW-29 |
| L30 | 2026-06 | null | null | null |

Apply the impact predicate only when a source path and mapping version are present: defect_affected is true if mapping_version=MAP-1 and source_path is PATH_A or PATH_B; it is false for the supplied correctly mapped PATH_C. L30 lacks path and version, so its impact remains unknown. Do not infer the missing path from the unit number or invent it from the pattern in neighboring records. The January start is supported by the activation record and January runtime snapshot; the June scope is supported by the June snapshot. Neither that scope nor the proposed sandbox correction establishes a verified July end boundary.

Each completed comparison requires a historical source, historical cutoff, historical facts and rationale, recovered source and receipt date, current facts, material-delta assessment and bounded route. All twelve printed packets meet that fictional completeness criterion. A referral adds a downstream dependency even though desk comparison is complete. This is why the twelve completed packets coexist with only six units having no open desk action and six open handoffs.

## Complete record-by-record analytical trace

### L01: period 2026-01

The independent manifest includes this unit in the five-unit control population for **2026-01**. Its canonical retrieval source is **RAW-01** and known activity amount is **1,500.00 USD**. The historical status is **CLOSED**, the defined defect-impact flag is **YES**, and the current lookback state is **REVIEW_COMPLETE_NO_NEW**. These are separate dimensions.

The action register records **DESK_REVIEW_COMPLETE**. Basis: Fictional re-review found no new information within supplied scope. Required next step: Preserve comparison and independent QA; no filing judgment inferred. The comparison packet is **COMP-L01**. Actual human disposition remains **NOT_RECORDED**, so this record does not represent institutional acceptance, a filing decision or account action.

Count this record in the six completed no-new-information comparisons and in the twelve completed desk comparisons. It has no open unit-level desk action within the fictional record. Preserve the original evidence and comparison scope; new material evidence would require a fresh transition without erasing the earlier packet. Do not generalize the narrow comparison result into a conclusion that all activity was legitimate.

### L02: period 2026-01

The independent manifest includes this unit in the five-unit control population for **2026-01**. Its canonical retrieval source is **RAW-02** and known activity amount is **2,500.00 USD**. The historical status is **ESCALATED**, the defined defect-impact flag is **YES**, and the current lookback state is **REVIEW_COMPLETE_NO_NEW**. These are separate dimensions.

The action register records **DESK_REVIEW_COMPLETE**. Basis: Fictional re-review found no new information within supplied scope. Required next step: Preserve comparison and independent QA; no filing judgment inferred. The comparison packet is **COMP-L02**. Actual human disposition remains **NOT_RECORDED**, so this record does not represent institutional acceptance, a filing decision or account action.

Preserve the duplicate representation RAW-D1 as an alias to this canonical unit. Its matching amount is excluded from the canonical activity sum. If a later copy differs, retain both values and resolve source timing and authority rather than automatically keeping the latest or the smallest number.

### L03: period 2026-01

The independent manifest includes this unit in the five-unit control population for **2026-01**. Its canonical retrieval source is **RAW-03** and known activity amount is **3,500.00 USD**. The historical status is **NOT_GENERATED**, the defined defect-impact flag is **NO**, and the current lookback state is **REVIEW_COMPLETE_NO_NEW**. These are separate dimensions.

The action register records **DESK_REVIEW_COMPLETE**. Basis: Fictional re-review found no new information within supplied scope. Required next step: Preserve comparison and independent QA; no filing judgment inferred. The comparison packet is **COMP-L03**. Actual human disposition remains **NOT_RECORDED**, so this record does not represent institutional acceptance, a filing decision or account action.

### L04: period 2026-01

The independent manifest includes this unit in the five-unit control population for **2026-01**. Its canonical retrieval source is **RAW-04** and known activity amount is **4,500.00 USD**. The historical status is **CLOSED**, the defined defect-impact flag is **YES**, and the current lookback state is **REVIEW_COMPLETE_NO_NEW**. These are separate dimensions.

The action register records **DESK_REVIEW_COMPLETE**. Basis: Fictional re-review found no new information within supplied scope. Required next step: Preserve comparison and independent QA; no filing judgment inferred. The comparison packet is **COMP-L04**. Actual human disposition remains **NOT_RECORDED**, so this record does not represent institutional acceptance, a filing decision or account action.

### L05: period 2026-01

The independent manifest includes this unit in the five-unit control population for **2026-01**. Its canonical retrieval source is **RAW-05** and known activity amount is **5,500.00 USD**. The historical status is **ESCALATED**, the defined defect-impact flag is **YES**, and the current lookback state is **REVIEW_COMPLETE_NO_NEW**. These are separate dimensions.

The action register records **DESK_REVIEW_COMPLETE**. Basis: Fictional re-review found no new information within supplied scope. Required next step: Preserve comparison and independent QA; no filing judgment inferred. The comparison packet is **COMP-L05**. Actual human disposition remains **NOT_RECORDED**, so this record does not represent institutional acceptance, a filing decision or account action.

### L06: period 2026-02

The independent manifest includes this unit in the five-unit control population for **2026-02**. Its canonical retrieval source is **RAW-06** and known activity amount is **6,500.00 USD**. The historical status is **NOT_GENERATED**, the defined defect-impact flag is **NO**, and the current lookback state is **REVIEW_COMPLETE_NO_NEW**. These are separate dimensions.

The action register records **DESK_REVIEW_COMPLETE**. Basis: Fictional re-review found no new information within supplied scope. Required next step: Preserve comparison and independent QA; no filing judgment inferred. The comparison packet is **COMP-L06**. Actual human disposition remains **NOT_RECORDED**, so this record does not represent institutional acceptance, a filing decision or account action.

### L07: period 2026-02

The independent manifest includes this unit in the five-unit control population for **2026-02**. Its canonical retrieval source is **RAW-07** and known activity amount is **7,500.00 USD**. The historical status is **CLOSED**, the defined defect-impact flag is **YES**, and the current lookback state is **REFERRED_FOR_CASE_REVIEW**. These are separate dimensions.

The action register records **HANDOFF_OPEN**. Basis: New information exists in comparison packet. Required next step: Obtain authorized case review acknowledgment and decision evidence. The comparison packet is **COMP-L07** (printed in ComparisonPackets). Actual human disposition remains **NOT_RECORDED**, so this record does not represent institutional acceptance, a filing decision or account action.

Count this record among the twelve completed desk comparisons and the six open referrals. It is not one of the six units with no open action. A receiving acknowledgment would document delivery but would not itself supply a final case decision. Preserve the exact new-information trigger and original context while the responsible human process considers the next step.

### L08: period 2026-02

The independent manifest includes this unit in the five-unit control population for **2026-02**. Its canonical retrieval source is **RAW-08** and known activity amount is **8,500.00 USD**. The historical status is **ESCALATED**, the defined defect-impact flag is **YES**, and the current lookback state is **REFERRED_FOR_CASE_REVIEW**. These are separate dimensions.

### L09: period 2026-02

The independent manifest includes this unit in the five-unit control population for **2026-02**. Its canonical retrieval source is **RAW-09** and known activity amount is **9,500.00 USD**. The historical status is **NOT_GENERATED**, the defined defect-impact flag is **NO**, and the current lookback state is **REFERRED_FOR_CASE_REVIEW**. These are separate dimensions.

### L10: period 2026-02

The independent manifest includes this unit in the five-unit control population for **2026-02**. Its canonical retrieval source is **RAW-10** and known activity amount is **10,500.00 USD**. The historical status is **CLOSED**, the defined defect-impact flag is **YES**, and the current lookback state is **REFERRED_FOR_CASE_REVIEW**. These are separate dimensions.

### L11: period 2026-03

The independent manifest includes this unit in the five-unit control population for **2026-03**. Its canonical retrieval source is **RAW-11** and known activity amount is **11,500.00 USD**. The historical status is **ESCALATED**, the defined defect-impact flag is **YES**, and the current lookback state is **REFERRED_FOR_CASE_REVIEW**. These are separate dimensions.

### L12: period 2026-03

The independent manifest includes this unit in the five-unit control population for **2026-03**. Its canonical retrieval source is **RAW-12** and known activity amount is **12,500.00 USD**. The historical status is **NOT_GENERATED**, the defined defect-impact flag is **NO**, and the current lookback state is **REFERRED_FOR_CASE_REVIEW**. These are separate dimensions.

Preserve the duplicate representation RAW-D2 as an alias to this canonical unit. Its matching amount is excluded from the canonical activity sum. If a later copy differs, retain both values and resolve source timing and authority rather than automatically keeping the latest or the smallest number.

### L13: period 2026-03

The independent manifest includes this unit in the five-unit control population for **2026-03**. Its canonical retrieval source is **RAW-13** and known activity amount is **13,500.00 USD**. The historical status is **CLOSED**, the defined defect-impact flag is **YES**, and the current lookback state is **REREVIEW_REQUIRED**. These are separate dimensions.

The action register records **REVIEW_OPEN**. Basis: Prior reasoning does not address changed defect context. Required next step: Reperform analysis against recovered evidence and preserve original rationale. The comparison packet is **not available**. Actual human disposition remains **NOT_RECORDED**, so this record does not represent institutional acceptance, a filing decision or account action.

Count this record among the six re-reviews and the eighteen units without completed desk comparison. The prior reasoning does not answer the changed defect context. The next review must preserve the original decision and identify the new facts or analytical question. An original closed or escalated status is not a substitute for the current comparison.

### L14: period 2026-03

The independent manifest includes this unit in the five-unit control population for **2026-03**. Its canonical retrieval source is **RAW-14** and known activity amount is **14,500.00 USD**. The historical status is **ESCALATED**, the defined defect-impact flag is **YES**, and the current lookback state is **REREVIEW_REQUIRED**. These are separate dimensions.

### L15: period 2026-03

The independent manifest includes this unit in the five-unit control population for **2026-03**. Its canonical retrieval source is **RAW-15** and known activity amount is **15,500.00 USD**. The historical status is **NOT_GENERATED**, the defined defect-impact flag is **NO**, and the current lookback state is **REREVIEW_REQUIRED**. These are separate dimensions.

### L16: period 2026-04

The independent manifest includes this unit in the five-unit control population for **2026-04**. Its canonical retrieval source is **RAW-16** and known activity amount is **16,500.00 USD**. The historical status is **CLOSED**, the defined defect-impact flag is **YES**, and the current lookback state is **REREVIEW_REQUIRED**. These are separate dimensions.

### L17: period 2026-04

The independent manifest includes this unit in the five-unit control population for **2026-04**. Its canonical retrieval source is **RAW-17** and known activity amount is **17,500.00 USD**. The historical status is **ESCALATED**, the defined defect-impact flag is **YES**, and the current lookback state is **REREVIEW_REQUIRED**. These are separate dimensions.

### L18: period 2026-04

The independent manifest includes this unit in the five-unit control population for **2026-04**. Its canonical retrieval source is **RAW-18** and known activity amount is **18,500.00 USD**. The historical status is **NOT_GENERATED**, the defined defect-impact flag is **NO**, and the current lookback state is **REREVIEW_REQUIRED**. These are separate dimensions.

### L19: period 2026-04

The independent manifest includes this unit in the five-unit control population for **2026-04**. Its canonical retrieval source is **RAW-19** and known activity amount is **19,500.00 USD**. The historical status is **CLOSED**, the defined defect-impact flag is **YES**, and the current lookback state is **PENDING_REVIEW**. These are separate dimensions.

The action register records **REVIEW_OPEN**. Basis: No completed desk review record supplied. Required next step: Assign reviewer and preserve priority; completion cannot be inferred. The comparison packet is **not available**. Actual human disposition remains **NOT_RECORDED**, so this record does not represent institutional acceptance, a filing decision or account action.

Count this record among the six pending reviews and the eighteen units without completed desk comparison. Receipt of a source row does not establish substantive review. Assignment, evidence review, comparison and disposition must remain separately traceable. A reporting deadline can justify an interim status update, but cannot convert this state into completed review.

### L20: period 2026-04

The independent manifest includes this unit in the five-unit control population for **2026-04**. Its canonical retrieval source is **RAW-20** and known activity amount is **20,500.00 USD**. The historical status is **ESCALATED**, the defined defect-impact flag is **YES**, and the current lookback state is **PENDING_REVIEW**. These are separate dimensions.

### L21: period 2026-05

The independent manifest includes this unit in the five-unit control population for **2026-05**. Its canonical retrieval source is **RAW-21** and known activity amount is **21,500.00 USD**. The historical status is **NOT_GENERATED**, the defined defect-impact flag is **NO**, and the current lookback state is **PENDING_REVIEW**. These are separate dimensions.

### L22: period 2026-05

The independent manifest includes this unit in the five-unit control population for **2026-05**. Its canonical retrieval source is **RAW-22** and known activity amount is **22,500.00 USD**. The historical status is **CLOSED**, the defined defect-impact flag is **YES**, and the current lookback state is **PENDING_REVIEW**. These are separate dimensions.

Preserve the duplicate representation RAW-D3 as an alias to this canonical unit. Its matching amount is excluded from the canonical activity sum. If a later copy differs, retain both values and resolve source timing and authority rather than automatically keeping the latest or the smallest number.

### L23: period 2026-05

The independent manifest includes this unit in the five-unit control population for **2026-05**. Its canonical retrieval source is **RAW-23** and known activity amount is **23,500.00 USD**. The historical status is **ESCALATED**, the defined defect-impact flag is **YES**, and the current lookback state is **PENDING_REVIEW**. These are separate dimensions.

### L24: period 2026-05

The independent manifest includes this unit in the five-unit control population for **2026-05**. Its canonical retrieval source is **RAW-24** and known activity amount is **24,500.00 USD**. The historical status is **NOT_GENERATED**, the defined defect-impact flag is **NO**, and the current lookback state is **PENDING_REVIEW**. These are separate dimensions.

### L25: period 2026-05

The independent manifest includes this unit in the five-unit control population for **2026-05**. Its canonical retrieval source is **RAW-25** and known activity amount is **25,500.00 USD**. The historical status is **CLOSED**, the defined defect-impact flag is **YES**, and the current lookback state is **UNABLE_TO_ASSESS**. These are separate dimensions.

The action register records **EVIDENCE_BLOCKED**. Basis: Retrieved summary lacks essential supporting evidence. Required next step: Recover missing support or record qualified scope limitation. The comparison packet is **not available**. Actual human disposition remains **NOT_RECORDED**, so this record does not represent institutional acceptance, a filing decision or account action.

Count this record as retrieved for population reconciliation but unable to assess for substantive completion. Its summary supplies an activity amount and historical status, yet essential supporting evidence is absent. The retrieval and review counts therefore diverge legitimately. Recover the needed source or retain a precise limitation; do not manufacture a no-new-information conclusion to close the queue.

### L26: period 2026-06

The independent manifest includes this unit in the five-unit control population for **2026-06**. Its canonical retrieval source is **RAW-26** and known activity amount is **26,500.00 USD**. The historical status is **ESCALATED**, the defined defect-impact flag is **YES**, and the current lookback state is **UNABLE_TO_ASSESS**. These are separate dimensions.

### L27: period 2026-06

The independent manifest includes this unit in the five-unit control population for **2026-06**. Its canonical retrieval source is **RAW-27** and known activity amount is **27,500.00 USD**. The historical status is **NOT_GENERATED**, the defined defect-impact flag is **NO**, and the current lookback state is **UNABLE_TO_ASSESS**. These are separate dimensions.

### L28: period 2026-06

The independent manifest includes this unit in the five-unit control population for **2026-06**. Its canonical retrieval source is **RAW-28** and known activity amount is **28,500.00 USD**. The historical status is **CLOSED**, the defined defect-impact flag is **YES**, and the current lookback state is **UNABLE_TO_ASSESS**. These are separate dimensions.

### L29: period 2026-06

The independent manifest includes this unit in the five-unit control population for **2026-06**. Its canonical retrieval source is **RAW-29** and known activity amount is **29,500.00 USD**. The historical status is **ESCALATED**, the defined defect-impact flag is **YES**, and the current lookback state is **UNABLE_TO_ASSESS**. These are separate dimensions.

### L30: period 2026-06

The independent manifest includes this unit in the five-unit control population for **2026-06**. Its canonical retrieval source is **not retrieved** and known activity amount is **unknown**. The historical status is **UNKNOWN**, the defined defect-impact flag is **UNKNOWN**, and the current lookback state is **NOT_RETRIEVED**. These are separate dimensions.

The action register records **RETRIEVAL_BLOCKED**. Basis: Control manifest names a unit absent from retrieval. Required next step: Recover archive record or retain unreconciled coverage gap. The comparison packet is **not available**. Actual human disposition remains **NOT_RECORDED**, so this record does not represent institutional acceptance, a filing decision or account action.

This record remains in the expected population despite being absent from retrieval. Its amount, impact and new-information result are unknown. It contributes one to missing-unit and not-retrieved counts, not to known activity amounts or completed reviews. Recovering a summary would resolve retrieval only; a full comparison would still need evidence and an explicit later state transition.

## Complete finding narratives and next decisions

### LB-F01: Expected historical unit remains absent from retrieval

Severity: **HIGH**. Confidence in the fictional observation: **HIGH**. Evidence class: **Observed**. Evidence: SYN-201, SYN-202.

The independent manifest names 30 units. Twenty-nine distinct in-scope units are retrieved; L30 is absent. June coverage is 4/5 even though raw intake rows all have classification buckets.

Proposed action: Recover L30 and its source lineage or retain the explicit unreconciled population limitation; do not close the lookback as complete.

The observation is bounded by the supplied fixture. It does not establish the prevalence of this issue in a live population or the legality of a particular institution's practice. A reviewer should challenge the affected IDs, exact calculation and possible alternative explanation, then record a separate human disposition if actual authority and evidence are supplied. No owner acceptance, operational execution or final signoff is represented here.

### LB-F02: Most units retain a review or evidence dependency

Severity: **HIGH**. Confidence in the fictional observation: **HIGH**. Evidence class: **Observed**. Evidence: SYN-201, SYN-203.

Only six no-new-information desk reviews have no open unit action. Six referrals, six re-reviews, six pending reviews, five unassessable summaries and one missing unit account for 24 unresolved unit dependencies.

Proposed action: Assign and complete each distinct evidence, retrieval, re-review and referral route; report progress with all 30 expected units as denominator.

### LB-F03: Three duplicate rows and two July exclusions can distort activity totals

Severity: **MEDIUM**. Confidence in the fictional observation: **HIGH**. Evidence class: **Observed**. Evidence: SYN-202.

Raw intake has 34 representations:29 canonical, three duplicates of L02 L12 L22, and two July records. Known canonical activity is 449500 USD; duplicate and excluded amounts must not inflate it.

Proposed action: Preserve alias links and excluded rows, verify canonical selection and investigate the July scope boundary separately.

### LB-F04: Historical desk review does not decide filing or case closure

Severity: **MEDIUM**. Confidence in the fictional observation: **HIGH**. Evidence class: **Observed**. Evidence: SYN-203, SYN-204.

Six new-information referrals remain unacknowledged in the fictional record. No actual authorized filing, nonfiling, account action or whole-review disposition is supplied.

Proposed action: Carry open handoffs until the responsible human process returns evidence; preserve this lookback as an analytical review with explicit limits.

## Boundary variations and expected interpretation

### Variation 01: Recover L30

Change only this input: Supply RAW-30 with amount 30500 and the matching manifest identity.

Expected result: Retrieved canonical count becomes 30; June becomes 5/5; known activity becomes 480000 USD. Review cannot jump from NOT_RETRIEVED to complete without analysis.

Required narrative: Recovery resolves retrieval only. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 02: Remove a duplicate copy

Change only this input: Remove RAW-D1 from a newly supplied packet while preserving the earlier version.

Expected result: New raw count is 33, duplicate count 2, canonical count 29 and known canonical activity remains 449500 USD.

Required narrative: Raw representation count and canonical scope are different. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 03: Duplicate amount conflict

Change only this input: Change RAW-D1 amount from 2500 to 2600.

Expected result: The duplicate identity can remain, but the value conflict blocks unqualified canonical selection for L02 until resolved.

Required narrative: Do not average conflicting values. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 04: July becomes in scope

Change only this input: Accept an analytical scope proposal including July and provide independent July controls.

Expected result: Rebuild the expected manifest and denominators; the two received July rows alone cannot define complete July coverage.

Required narrative: Expansion requires controls, not only found records. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 05: Summary retrieved for L30

Change only this input: Supply only a summary without essential activity support.

Expected result: Retrieval coverage becomes 30/30, but L30 moves at most to UNABLE_TO_ASSESS pending needed evidence.

Required narrative: Retrieved is not the same as reviewable. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 06: Resolve one unable unit

Change only this input: Provide complete L25 support and finish a comparison finding no new information.

Expected result: UNABLE count becomes 4; no-open-action count 7; desk comparisons 13; total expected remains 30.

Required narrative: The state change has a separate evidence packet. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 07: Resolve one pending unit with referral

Change only this input: Finish L19 comparison and identify new information requiring case assessment.

Expected result: PENDING becomes 5; REFERRED becomes 7; desk comparisons become 13; no-open-action remains 6.

Required narrative: Finishing desk work can increase open handoffs. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 08: Acknowledge a referral

Change only this input: Receive an actual acknowledgment for L07 without a final decision.

Expected result: The referral remains open; acknowledgment changes but disposition completion does not.

Required narrative: Receipt is not resolution. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 09: New evidence on a complete unit

Change only this input: Receive credible additional information for L01 after its comparison.

Expected result: Reopen L01 with a new state entry; preserve COMP-L01 and the earlier cutoff.

Required narrative: Prior completion is not silently deleted or retroactively rewritten. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 10: Independent manifest increases

Change only this input: A new control identifies an additional May unit L33.

Expected result: Expected count becomes 31; May expected count 6; missing units increase until retrieval resolves; recalculate every rate.

Required narrative: Do not hide a newly expected unit outside the denominator. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 11: Manifest shares the defect

Change only this input: Learn that the control manifest used the same broken mapping as retrieval.

Expected result: Completeness assurance is blocked pending an independent control; matching counts are insufficient.

Required narrative: A common source defect can survive perfect reconciliation. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 12: False historical closure inference

Change only this input: An originally CLOSED record has not been re-reviewed.

Expected result: Its current state remains PENDING_REVIEW or REREVIEW_REQUIRED as supported; it is not complete.

Required narrative: Historical status cannot answer the current question. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 13: Unknown amount treated as zero

Change only this input: Replace L30 amount null with zero without source evidence.

Expected result: QA fails; restore null and the unknown-amount limitation.

Required narrative: A total must not manufacture data availability. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 14: Unmatched raw identity

Change only this input: Add a received row whose canonical key is uncertain.

Expected result: Add an unresolved intake bucket and hold identity-dependent aggregation; do not force a match.

Required narrative: Complete intake accounting includes unresolved records. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 15: All received rows classified

Change only this input: Confirm that all 34 received rows are assigned a bucket.

Expected result: Only intake accounting is 100%; retrieval remains 29/30, desk comparison 12/30 and no-open-action 6/30.

Required narrative: Do not borrow the highest percentage for a broader completion claim. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 16: Human accepts a limitation

Change only this input: Receive an actual authorized restricted acceptance concerning missing L30.

Expected result: Preserve the missing unit and restricted claim; do not change the record to observed or reviewed.

Required narrative: Acceptance changes a decision state, not the underlying evidence. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 17: Scope end uncertain

Change only this input: The corrected mapping date is unknown while July records exist.

Expected result: EX-06 remains open and the boundary claim stays qualified; request version and continuity evidence.

Required narrative: No confirmed July issue does not prove the absence of exposure. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

### Variation 18: Report deadline arrives

Change only this input: A requested submission date occurs while 24 dependencies remain open.

Expected result: Deliver accurate interim status with open units; do not convert pending states to completed ones.

Required narrative: A deadline changes delivery timing, not evidential completion. Preserve the baseline case, label the changed assumption and state which result changed. If a variation resolves one gate while others remain, keep those remaining restrictions in the recommendation.

## Embedded independent fixture check

The following complete standard-library Python block is optional in-session verification. It has no repository, file, network or installation dependency. It starts from the raw fixture declarations, derives results and checks independent expected ID sets, counts and boundary values. If execution is unavailable, reperform the printed equations and mark the executable check NOT_TESTED. Passing this block establishes the stated fixture relationships only.

<!-- FIXTURE_CHECK:START -->
```python
# Pure Python; no repository, files, packages or network required.
from collections import Counter
MANIFEST = [['L01', '2026-01'], ['L02', '2026-01'], ['L03', '2026-01'], ['L04', '2026-01'], ['L05', '2026-01'], ['L06', '2026-02'], ['L07', '2026-02'], ['L08', '2026-02'], ['L09', '2026-02'], ['L10', '2026-02'], ['L11', '2026-03'], ['L12', '2026-03'], ['L13', '2026-03'], ['L14', '2026-03'], ['L15', '2026-03'], ['L16', '2026-04'], ['L17', '2026-04'], ['L18', '2026-04'], ['L19', '2026-04'], ['L20', '2026-04'], ['L21', '2026-05'], ['L22', '2026-05'], ['L23', '2026-05'], ['L24', '2026-05'], ['L25', '2026-05'], ['L26', '2026-06'], ['L27', '2026-06'], ['L28', '2026-06'], ['L29', '2026-06'], ['L30', '2026-06']]
RAW = [['RAW-01', 'L01', '2026-01', 'CANONICAL', 'L01', 1500, 'SYN-202'], ['RAW-02', 'L02', '2026-01', 'CANONICAL', 'L02', 2500, 'SYN-202'], ['RAW-03', 'L03', '2026-01', 'CANONICAL', 'L03', 3500, 'SYN-202'], ['RAW-04', 'L04', '2026-01', 'CANONICAL', 'L04', 4500, 'SYN-202'], ['RAW-05', 'L05', '2026-01', 'CANONICAL', 'L05', 5500, 'SYN-202'], ['RAW-06', 'L06', '2026-02', 'CANONICAL', 'L06', 6500, 'SYN-202'], ['RAW-07', 'L07', '2026-02', 'CANONICAL', 'L07', 7500, 'SYN-202'], ['RAW-08', 'L08', '2026-02', 'CANONICAL', 'L08', 8500, 'SYN-202'], ['RAW-09', 'L09', '2026-02', 'CANONICAL', 'L09', 9500, 'SYN-202'], ['RAW-10', 'L10', '2026-02', 'CANONICAL', 'L10', 10500, 'SYN-202'], ['RAW-11', 'L11', '2026-03', 'CANONICAL', 'L11', 11500, 'SYN-202'], ['RAW-12', 'L12', '2026-03', 'CANONICAL', 'L12', 12500, 'SYN-202'], ['RAW-13', 'L13', '2026-03', 'CANONICAL', 'L13', 13500, 'SYN-202'], ['RAW-14', 'L14', '2026-03', 'CANONICAL', 'L14', 14500, 'SYN-202'], ['RAW-15', 'L15', '2026-03', 'CANONICAL', 'L15', 15500, 'SYN-202'], ['RAW-16', 'L16', '2026-04', 'CANONICAL', 'L16', 16500, 'SYN-202'], ['RAW-17', 'L17', '2026-04', 'CANONICAL', 'L17', 17500, 'SYN-202'], ['RAW-18', 'L18', '2026-04', 'CANONICAL', 'L18', 18500, 'SYN-202'], ['RAW-19', 'L19', '2026-04', 'CANONICAL', 'L19', 19500, 'SYN-202'], ['RAW-20', 'L20', '2026-04', 'CANONICAL', 'L20', 20500, 'SYN-202'], ['RAW-21', 'L21', '2026-05', 'CANONICAL', 'L21', 21500, 'SYN-202'], ['RAW-22', 'L22', '2026-05', 'CANONICAL', 'L22', 22500, 'SYN-202'], ['RAW-23', 'L23', '2026-05', 'CANONICAL', 'L23', 23500, 'SYN-202'], ['RAW-24', 'L24', '2026-05', 'CANONICAL', 'L24', 24500, 'SYN-202'], ['RAW-25', 'L25', '2026-05', 'CANONICAL', 'L25', 25500, 'SYN-202'], ['RAW-26', 'L26', '2026-06', 'CANONICAL', 'L26', 26500, 'SYN-202'], ['RAW-27', 'L27', '2026-06', 'CANONICAL', 'L27', 27500, 'SYN-202'], ['RAW-28', 'L28', '2026-06', 'CANONICAL', 'L28', 28500, 'SYN-202'], ['RAW-29', 'L29', '2026-06', 'CANONICAL', 'L29', 29500, 'SYN-202'], ['RAW-D1', 'L02', '2026-01', 'DUPLICATE', 'L02', 2500, 'SYN-202'], ['RAW-D2', 'L12', '2026-03', 'DUPLICATE', 'L12', 12500, 'SYN-202'], ['RAW-D3', 'L22', '2026-05', 'DUPLICATE', 'L22', 22500, 'SYN-202'], ['RAW-X31', None, '2026-07', 'OUT_OF_SCOPE', None, 31500, 'SYN-202'], ['RAW-X32', None, '2026-07', 'OUT_OF_SCOPE', None, 32500, 'SYN-202']]
REVIEW_INPUTS = {'L01': ['CLOSED', True, 'REVIEW_COMPLETE_NO_NEW', False, 'MEDIUM'], 'L02': ['ESCALATED', True, 'REVIEW_COMPLETE_NO_NEW', False, 'MEDIUM'], 'L03': ['NOT_GENERATED', False, 'REVIEW_COMPLETE_NO_NEW', False, 'MEDIUM'], 'L04': ['CLOSED', True, 'REVIEW_COMPLETE_NO_NEW', False, 'MEDIUM'], 'L05': ['ESCALATED', True, 'REVIEW_COMPLETE_NO_NEW', False, 'MEDIUM'], 'L06': ['NOT_GENERATED', False, 'REVIEW_COMPLETE_NO_NEW', False, 'MEDIUM'], 'L07': ['CLOSED', True, 'REFERRED_FOR_CASE_REVIEW', True, 'HIGH'], 'L08': ['ESCALATED', True, 'REFERRED_FOR_CASE_REVIEW', True, 'HIGH'], 'L09': ['NOT_GENERATED', False, 'REFERRED_FOR_CASE_REVIEW', True, 'HIGH'], 'L10': ['CLOSED', True, 'REFERRED_FOR_CASE_REVIEW', True, 'HIGH'], 'L11': ['ESCALATED', True, 'REFERRED_FOR_CASE_REVIEW', True, 'HIGH'], 'L12': ['NOT_GENERATED', False, 'REFERRED_FOR_CASE_REVIEW', True, 'HIGH'], 'L13': ['CLOSED', True, 'REREVIEW_REQUIRED', None, 'HIGH'], 'L14': ['ESCALATED', True, 'REREVIEW_REQUIRED', None, 'HIGH'], 'L15': ['NOT_GENERATED', False, 'REREVIEW_REQUIRED', None, 'HIGH'], 'L16': ['CLOSED', True, 'REREVIEW_REQUIRED', None, 'HIGH'], 'L17': ['ESCALATED', True, 'REREVIEW_REQUIRED', None, 'HIGH'], 'L18': ['NOT_GENERATED', False, 'REREVIEW_REQUIRED', None, 'HIGH'], 'L19': ['CLOSED', True, 'PENDING_REVIEW', None, 'MEDIUM'], 'L20': ['ESCALATED', True, 'PENDING_REVIEW', None, 'MEDIUM'], 'L21': ['NOT_GENERATED', False, 'PENDING_REVIEW', None, 'MEDIUM'], 'L22': ['CLOSED', True, 'PENDING_REVIEW', None, 'MEDIUM'], 'L23': ['ESCALATED', True, 'PENDING_REVIEW', None, 'MEDIUM'], 'L24': ['NOT_GENERATED', False, 'PENDING_REVIEW', None, 'MEDIUM'], 'L25': ['CLOSED', True, 'UNABLE_TO_ASSESS', None, 'HIGH'], 'L26': ['ESCALATED', True, 'UNABLE_TO_ASSESS', None, 'HIGH'], 'L27': ['NOT_GENERATED', False, 'UNABLE_TO_ASSESS', None, 'HIGH'], 'L28': ['CLOSED', True, 'UNABLE_TO_ASSESS', None, 'HIGH'], 'L29': ['ESCALATED', True, 'UNABLE_TO_ASSESS', None, 'HIGH'], 'L30': ['UNKNOWN', None, 'NOT_RETRIEVED', None, 'HIGH']}
assert len(MANIFEST)==30 and len({u[0] for u in MANIFEST})==30
assert len(RAW)==34 and len({r[0] for r in RAW})==34
assert Counter(r[3] for r in RAW)=={"CANONICAL":29,"DUPLICATE":3,"OUT_OF_SCOPE":2}
canonical={r[1]:r for r in RAW if r[3]=="CANONICAL"}
assert set(uid for uid,period in MANIFEST)-set(canonical)=={"L30"}
for r in RAW:
    if r[3]=="DUPLICATE":
        assert r[1] in canonical and r[4]==r[1] and r[5]==canonical[r[1]][5]
units=[]
for uid,period in MANIFEST:
    source=canonical.get(uid); original,affected,state,newinfo,priority=REVIEW_INPUTS[uid]
    units.append([uid,period,source[0] if source else None,source[5] if source else None,
        original,affected,state,newinfo,priority,"SYN-201;SYN-202" if source else "SYN-201"])
periods=[]
for period in sorted({p for uid,p in MANIFEST}):
    expected=[u for u in units if u[1]==period]
    raw=[r for r in RAW if r[2]==period]
    retrieved=sum(u[2] is not None for u in expected)
    missing=len(expected)-retrieved
    periods.append([period,len(expected),len(raw),sum(r[3]=="DUPLICATE" for r in raw),
        retrieved,missing,sum(u[3] for u in expected if u[3] is not None),
        "PARTIAL" if missing else "RECONCILED","SYN-201;SYN-202"])
assert sum(p[1] for p in periods)==30
assert sum(p[4] for p in periods)==29 and sum(p[5] for p in periods)==1
assert periods[-1][4:6]==[4,1]
known=sum(u[3] for u in units if u[3] is not None)
duplicate=sum(r[5] for r in RAW if r[3]=="DUPLICATE")
excluded=sum(r[5] for r in RAW if r[3]=="OUT_OF_SCOPE")
assert (known,duplicate,excluded)==(449500,37500,64000)
assert sum(r[5] for r in RAW)==known+duplicate+excluded==551000
states=Counter(u[6] for u in units)
assert states=={"REVIEW_COMPLETE_NO_NEW":6,"REFERRED_FOR_CASE_REVIEW":6,
    "REREVIEW_REQUIRED":6,"PENDING_REVIEW":6,"UNABLE_TO_ASSESS":5,"NOT_RETRIEVED":1}
complete=states["REVIEW_COMPLETE_NO_NEW"]
referred=states["REFERRED_FOR_CASE_REVIEW"]
desk=complete+referred
assert desk==12 and len(units)-complete==24
assert sum(u[5] is True for u in units)==20
assert sum(u[5] is False for u in units)==9 and units[-1][5] is None
# Completion statements are derived from the independent manifest, not the received rows.
gates=[
["LB-G01","Raw rows assigned an intake bucket",len(RAW),len(RAW),"SATISFIED_FIXTURE_ONLY","None within supplied intake","All received rows classified; expected population still missing one","SYN-202"],
["LB-G02","Expected canonical units retrieved",len(canonical),len(MANIFEST),"FAILED","L30 not retrieved","Retrieval coverage 29/30; no complete-coverage claim","SYN-201;SYN-202"],
["LB-G03","Desk comparison completed",desk,len(MANIFEST),"FAILED","18 not desk-complete","12 comparisons completed, including 6 unresolved referrals","SYN-203"],
["LB-G04","Desk review with no open unit action",complete,len(MANIFEST),"FAILED","24 units retain review evidence retrieval or handoff dependency","6 units have completed no-new-information comparisons","SYN-203"],
["LB-G05","Referred units acknowledged and disposed",0,referred,"BLOCKED","No actual receiving-case decision evidence","Six handoffs remain open","SYN-203"],
["LB-G06","Authorized whole-review acceptance",0,1,"BLOCKED","Actual approval and accepted limitations absent","Lookback remains incomplete","SYN-203;SYN-204"]]
# Independent recovery mutation resolves retrieval only; it does not create review completion.
assert known+30500==480000
assert len(canonical)+1==len(MANIFEST)
# Removing a raw duplicate leaves the canonical sum unchanged.
reduced=[r for r in RAW if r[0]!="RAW-D1"]
assert len(reduced)==33 and sum(r[5] for r in reduced if r[3]=="CANONICAL")==known
# Complete printed historical/current packets and source paths support the review/impact states.
PACKETS = [['COMP-L01', 'L01', '2026-01-31', 'HIST-L01', 'L01-F1;L01-F2', 'Payroll credits from two identified employers matched the supplied pay records.', 'The historical review already inspected both payer identities and pay records.', '2026-10-02', 'REC-L01', 'L01-F1;L01-F2', 'Both payer identities, amounts and pay-record matches are unchanged; corrected monitoring count adds no unseen fact.', 'PATH_A', False, 'REVIEW_COMPLETE_NO_NEW', 'SYN-205'], ['COMP-L02', 'L02', '2026-01-31', 'HIST-L02', 'L02-F1;L02-F2', 'Four originators and the complete activity were already included in the earlier escalation packet.', 'Historical escalation expressly covered all four identified originators.', '2026-10-02', 'REC-L02', 'L02-F1;L02-F2', 'Recovered source messages match the four identities and activity already escalated; no additional party or transaction is found.', 'PATH_B', False, 'REVIEW_COMPLETE_NO_NEW', 'SYN-205'], ['COMP-L03', 'L03', '2026-01-31', 'HIST-L03', 'L03-F1;L03-F2', 'One documented transfer from the same beneficial owner matched the account ownership evidence.', 'The correctly mapped control path produced no scenario hit and the underlying ownership fact was documented.', '2026-10-02', 'REC-L03', 'L03-F1;L03-F2', 'The source-path replay and ownership documentation are unchanged.', 'PATH_C', False, 'REVIEW_COMPLETE_NO_NEW', 'SYN-205'], ['COMP-L04', 'L04', '2026-01-31', 'HIST-L04', 'L04-F1;L04-F2', 'Three commercial payers matched the supplied invoices and recorded business counterparties.', 'Historical closure relied on inspected invoice and counterparty matches, not the defective aggregate alone.', '2026-10-02', 'REC-L04', 'L04-F1;L04-F2', 'Recovered messages preserve the same three payers and invoice references with no contradiction.', 'PATH_A', False, 'REVIEW_COMPLETE_NO_NEW', 'SYN-205'], ['COMP-L05', 'L05', '2026-01-31', 'HIST-L05', 'L05-F1;L05-F2', 'Five originators and their activity were fully described in the earlier escalation.', 'The historical packet included the source messages and all five counterparties.', '2026-10-02', 'REC-L05', 'L05-F1;L05-F2', 'The replay identifies the same five parties already in that packet; no new transaction or identity is added.', 'PATH_B', False, 'REVIEW_COMPLETE_NO_NEW', 'SYN-205'], ['COMP-L06', 'L06', '2026-02-28', 'HIST-L06', 'L06-F1;L06-F2', 'A single internal operating transfer matched the supplied account mapping.', 'The control path mapped the actual originator and the activity remained outside the scenario concept.', '2026-10-02', 'REC-L06', 'L06-F1;L06-F2', 'The original source and current replay agree on the same internal account and purpose.', 'PATH_C', False, 'REVIEW_COMPLETE_NO_NEW', 'SYN-205'], ['COMP-L07', 'L07', '2026-02-28', 'HIST-L07', 'L07-F1;L07-F2', 'The historical summary described all credits as transfers from the same customer-controlled account.', 'Closure relied on the one-originator summary and did not include underlying payment messages.', '2026-10-02', 'REC-L07', 'L07-F1;L07-F2;L07-F3', 'Recovered messages identify four third-party originator IDs; three are absent from the historical packet and their purpose is unsupported.', 'PATH_A', True, 'REFERRED_FOR_CASE_REVIEW', 'SYN-205'], ['COMP-L08', 'L08', '2026-02-28', 'HIST-L08', 'L08-F1;L08-F2', 'The prior escalation packet identified two originators and stated that it covered the complete relationship.', 'The earlier referral scope was limited to those two identities and their supplied activity.', '2026-10-02', 'REC-L08', 'L08-F1;L08-F2;L08-F3', 'Recovered messages identify seven originators; five additional identities were outside the earlier scope.', 'PATH_B', True, 'REFERRED_FOR_CASE_REVIEW', 'SYN-205'], ['COMP-L09', 'L09', '2026-02-28', 'HIST-L09', 'L09-F1;L09-F2', 'The control-path unit showed one payer and a supplier-payment explanation.', 'No scenario hit was generated; the supplied original packet contained the stated supplier rationale.', '2026-10-02', 'REC-L09', 'L09-F1;L09-F2;L09-F3', 'A newly recovered contract names a different economic supplier than the payment message, creating an identity-purpose inconsistency unrelated to the mapping defect.', 'PATH_C', True, 'REFERRED_FOR_CASE_REVIEW', 'SYN-205'], ['COMP-L10', 'L10', '2026-02-28', 'HIST-L10', 'L10-F1;L10-F2', 'The historical review treated the credits as customer self-funding based on the summary identity.', 'Closure relied on apparent common ownership without the underlying message identities.', '2026-10-02', 'REC-L10', 'L10-F1;L10-F2;L10-F3', 'Five distinct third-party originators appear in recovered messages and the claimed ownership link is not supported.', 'PATH_A', True, 'REFERRED_FOR_CASE_REVIEW', 'SYN-205'], ['COMP-L11', 'L11', '2026-03-31', 'HIST-L11', 'L11-F1;L11-F2', 'The prior escalation described three counterparties and excluded no known message records.', 'Its stated scope and rationale addressed those three named parties only.', '2026-10-02', 'REC-L11', 'L11-F1;L11-F2;L11-F3', 'The corrected message grouping identifies three additional counterparties, including activity outside the original referral narrative.', 'PATH_B', True, 'REFERRED_FOR_CASE_REVIEW', 'SYN-205'], ['COMP-L12', 'L12', '2026-03-31', 'HIST-L12', 'L12-F1;L12-F2', 'The control-path unit had one identified payer and an equipment-sale explanation.', 'The original source did not contradict the stated sale purpose and the monitoring predicate did not hit.', '2026-10-02', 'REC-L12', 'L12-F1;L12-F2;L12-F3', 'A newly recovered invoice describes consulting services instead of equipment, creating a material purpose contradiction independent of mapping.', 'PATH_C', True, 'REFERRED_FOR_CASE_REVIEW', 'SYN-205']]
SOURCE_PATHS = [['L01', '2026-01', 'PATH_A', 'MAP-1', 'RAW-01'], ['L02', '2026-01', 'PATH_B', 'MAP-1', 'RAW-02'], ['L03', '2026-01', 'PATH_C', 'MAP-1', 'RAW-03'], ['L04', '2026-01', 'PATH_A', 'MAP-1', 'RAW-04'], ['L05', '2026-01', 'PATH_B', 'MAP-1', 'RAW-05'], ['L06', '2026-02', 'PATH_C', 'MAP-1', 'RAW-06'], ['L07', '2026-02', 'PATH_A', 'MAP-1', 'RAW-07'], ['L08', '2026-02', 'PATH_B', 'MAP-1', 'RAW-08'], ['L09', '2026-02', 'PATH_C', 'MAP-1', 'RAW-09'], ['L10', '2026-02', 'PATH_A', 'MAP-1', 'RAW-10'], ['L11', '2026-03', 'PATH_B', 'MAP-1', 'RAW-11'], ['L12', '2026-03', 'PATH_C', 'MAP-1', 'RAW-12'], ['L13', '2026-03', 'PATH_A', 'MAP-1', 'RAW-13'], ['L14', '2026-03', 'PATH_B', 'MAP-1', 'RAW-14'], ['L15', '2026-03', 'PATH_C', 'MAP-1', 'RAW-15'], ['L16', '2026-04', 'PATH_A', 'MAP-1', 'RAW-16'], ['L17', '2026-04', 'PATH_B', 'MAP-1', 'RAW-17'], ['L18', '2026-04', 'PATH_C', 'MAP-1', 'RAW-18'], ['L19', '2026-04', 'PATH_A', 'MAP-1', 'RAW-19'], ['L20', '2026-04', 'PATH_B', 'MAP-1', 'RAW-20'], ['L21', '2026-05', 'PATH_C', 'MAP-1', 'RAW-21'], ['L22', '2026-05', 'PATH_A', 'MAP-1', 'RAW-22'], ['L23', '2026-05', 'PATH_B', 'MAP-1', 'RAW-23'], ['L24', '2026-05', 'PATH_C', 'MAP-1', 'RAW-24'], ['L25', '2026-05', 'PATH_A', 'MAP-1', 'RAW-25'], ['L26', '2026-06', 'PATH_B', 'MAP-1', 'RAW-26'], ['L27', '2026-06', 'PATH_C', 'MAP-1', 'RAW-27'], ['L28', '2026-06', 'PATH_A', 'MAP-1', 'RAW-28'], ['L29', '2026-06', 'PATH_B', 'MAP-1', 'RAW-29'], ['L30', '2026-06', None, None, None]]
assert len(PACKETS)==12 and len({p[1] for p in PACKETS})==12
for packet in PACKETS:
    assert all(packet[i] for i in [0,1,2,3,4,5,6,7,8,9,10,11,13,14])
    new_material = bool(set(packet[9].split(";"))-set(packet[4].split(";")))
    assert new_material == packet[12]
    expected_route = "REFERRED_FOR_CASE_REVIEW" if new_material else "REVIEW_COMPLETE_NO_NEW"
    assert packet[13] == expected_route
    unit = next(u for u in units if u[0]==packet[1])
    assert unit[6] == expected_route and unit[7] == new_material
    unit[-1] += ";SYN-205"
for uid,period,path,version,locator in SOURCE_PATHS:
    expected_impact = None if path is None or version is None else version=="MAP-1" and path in ("PATH_A","PATH_B")
    unit=next(u for u in units if u[0]==uid)
    assert unit[5] is expected_impact
assert sum(not p[12] for p in PACKETS)==6 and sum(p[12] for p in PACKETS)==6
assert len(PACKETS)==desk
CHECKED_TABLES={"PeriodReconciliation":periods,"CanonicalUnits":units,"CompletionGates":gates}
print("Lookback fixture: raw/canonical reconciliation, amounts, states, completion gates and recovery checks passed.")
```
<!-- FIXTURE_CHECK:END -->

## Completed analytical recommendation

The lookback is incomplete. Twenty-nine of 30 expected historical units are retrieved, twelve desk comparisons are complete, and only six units have no open desk-review action. Six referrals and eighteen other evidence or review dependencies remain unresolved; no filing or whole-review approval is implied.

**Lookback status and completion restrictions.** The lookback is incomplete. Twenty-nine of 30 expected historical units are retrieved, twelve desk comparisons are complete, and only six units have no open desk-review action. Six referrals and eighteen other evidence or review dependencies remain unresolved; no filing or whole-review approval is implied.

**Historical scope defect chronology and population.** The independent fictional manifest defines January through June 2026 and five canonical units per month. Initial discovery considered January through March; a documented analytical expansion includes April through June because the mapping defect chronology may continue. Actual institutional scope approval is not supplied.

**Retrieval review and coverage findings.** Raw intake reconciles 34 representations to 29 canonical units,3 duplicates and 2 July exclusions. That arithmetic does not cure missing L30. June is 4/5 retrieved. Known canonical activity totals 449500 USD and excludes L30, whose amount is unknown.

**Complete historical population and intake registers.** CanonicalUnits preserves all 30 expected records, including the missing placeholder. RetrievalLedger preserves every received representation and alias link. Historical statuses remain separate from current review states, so re-review never rewrites the original decision history.

**Review actions expansion and stopping gates.** Six units have completed comparisons with no new information; six have new-information referrals; six need re-review; six await review; five are unable to assess; one is not retrieved. Twelve desk comparisons are complete, but six of those have unresolved handoffs. Twenty-four units retain an open dependency.

**Evidence preservation and unresolved periods.** Control evidence, retrieval evidence, review assignments and chronology are separate sources. A retrieved summary does not establish complete supporting documents. The July rows are retained as exclusions while chronology evidence is requested, not silently dropped as irrelevant.

**Proposed remediation and case-review handoffs.** Proposed work is to recover L30, obtain support for L25 through L29, finish L13 through L24 reviews, and obtain responsible case-review responses for L07 through L12. Filing, account action and whole-review acceptance remain separate human decisions.

**Limitations quality review and human disposition.** Do not report a 100% completion rate from received-row classification or twelve completed desk comparisons. Reperform the thirty-unit state reconciliation, amount conservation, duplicate links and completion gates. The fictional checks establish evidence accounting only, not a completed operational remediation.

## Next-session change control

When new evidence arrives, preserve this specimen or the prior real-case version, assign the new source its own ID and cutoff, and identify the affected methods and tables. Recalculate the complete relevant denominator rather than editing one favorable headline. Update the finding, action, limitation and human-decision records together. A resolved arithmetic issue does not automatically resolve evidence, concept or authorization gates, and a new source can create additional review work even while it improves retrieval coverage.
