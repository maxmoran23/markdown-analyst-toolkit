# Entity Due Diligence — worked fictional example

## Subject and intake

All facts below are fictional and collectively form SYN-001. No real person, customer, legal entity, license, or register is represented. The subject is Meridian Paperlight Services, internal ID ENTITY-Q, fictional registry number Q-410. The decision is whether a public-source profile is sufficiently complete to support a human assessment of a proposed research-service relationship as of 2026-09-30.

The fictional register extract records ENTITY-Q active. A company disclosure supplies ownership and reports monthly receipts of $600,000.00. A separate group brochure refers to a license held by ENTITY-R. An article alleges a proceeding but provides no order. No control-right documents, complete ultimate ownership records, or independently verified financial statements are supplied.

## Ownership input

| edge_id | owner_id | owned_entity_id | interest_pct | interest_basis | effective_date | source_status | evidence_ids | notes |
| --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| O-01 | PERSON-A | HOLDCO-A | 60.0 | Ordinary economic equity | 2026-09-30 | REPORTED | SYN-001 | Company schedule |
| O-02 | PERSON-B | HOLDCO-A | 40.0 | Ordinary economic equity | 2026-09-30 | REPORTED | SYN-001 | Company schedule |
| O-03 | HOLDCO-A | ENTITY-Q | 70.0 | Ordinary economic equity | 2026-09-30 | REPORTED | SYN-001 | Company schedule |
| O-04 | PERSON-C | ENTITY-Q | 20.0 | Ordinary economic equity | 2026-09-30 | REPORTED | SYN-001 | Direct holder |
| O-05 | UNKNOWN-POOL | ENTITY-Q | 10.0 | Ordinary economic equity | 2026-09-30 | UNKNOWN | SYN-001 | Underlying holders absent |

The exercise assumes comparable ordinary equity, no cycles, no overlapping paths, no preferred interests, and no unrecorded direct holdings. Those assumptions are necessary for the following calculation. They are not conclusions established by the mere appearance of a neat table.

## Reconciliation and arithmetic

HOLDCO-A's supplied direct interests sum to 60.0 + 40.0 = 100.0%. ENTITY-Q's direct interests sum to 70.0 + 20.0 + 10.0 = 100.0%. The latter includes a residual pool whose amount is known but holders are unknown. A 100.0% direct total therefore does not mean full ultimate-owner resolution.

Person A's estimated economic interest in ENTITY-Q is 0.60 × 0.70 = 0.42 = 42.0%. Person B's is 0.40 × 0.70 = 0.28 = 28.0%. Person C has 20.0% directly. Known terminal economic interests total 42.0 + 28.0 + 20.0 = 90.0%. Unresolved terminal interest is 100.0 − 90.0 = 10.0%.

The amount-based resolution metric is 90.0%. It describes the supplied comparable-equity graph. It is not a confidence estimate, a legal beneficial-owner determination, or a statement that 90.0% of diligence is complete. Control rights remain unassessed for the whole structure.

The company reports monthly receipts of $600,000.00. If every month were identical, the annualized run rate would be 600,000 × 12 = $7,200,000.00. Classify this Estimated and explain the constant-month assumption. Do not label it audited annual revenue or use it to infer profitability, solvency, or source of wealth. No operating-cost, seasonality, or accounting-basis evidence was supplied.

## Expected profile assessment

P-01 legal identity is SUPPORTED within the fictional registry scope. P-02 ownership is INCOMPLETE because the residual holders and control rights are absent. P-03 business purpose is REPORTED because the activity and receipts come from a company statement. P-04 permission is UNRESOLVED: ENTITY-R's license does not itself demonstrate ENTITY-Q's authority. P-05 adverse event is NOT ASSESSED beyond the existence of a reported allegation because the underlying order and procedural history are missing.

There are five profile questions. Four lack a fully supported substantive resolution: P-02, P-03, P-04, P-05. The single SUPPORTED status on P-01 is not a 20.0% overall quality score. The questions have different consequences and different evidence requirements. Show each state rather than averaging them.

## Expected findings

F-01: HIGH materiality, HIGH confidence, Observed — 10.0% of the target's comparable economic ownership has no identified underlying holder in the supplied schedule. The confidence concerns the observed disclosure gap. Request the missing holder schedule and separate control-right evidence. Do not characterize the gap as concealment.

F-02: HIGH materiality, MODERATE confidence, Inferred — target-entity permission has not been demonstrated by a license naming ENTITY-R. Request the operative permission and scope rationale for ENTITY-Q's contemplated activity. Possible explanations include group coverage, exempt activity, incorrect brochure wording, or an actual permission gap; none is established by these inputs.

F-03: MEDIUM materiality, HIGH confidence, Observed — the receipts figure is self-reported and the annual figure is only a scenario. Seek comparable financial evidence if capacity is decision-relevant. The annualization arithmetic is exact under the assumption, while the assumption remains unsupported.

The recommendation is ADDITIONAL EVIDENCE REQUIRED for ownership and capacity and SPECIALIST REVIEW REQUIRED if the permission question depends on legal scope. Final relationship disposition remains PENDING. The pack does not infer that the entity should be accepted or rejected.

## Edge cases and reverse tests

If Person A also directly owns 5.0% of ENTITY-Q, do not simply add a sixth row without reconciling the existing 100.0% total. Identify which prior holding changed and its effective date. If 5.0% comes from the unresolved pool at the same cutoff, the new derived interest would be 47.0%, with 5.0% residual remaining. If it is a later acquisition, produce a separate dated graph.

If Person B controls board appointments despite a 28.0% economic interest, record the control fact separately and obtain the governing document. If HOLDCO-A holds preferred shares with different economic rights, the simple multiplication might no longer describe the relevant interest. If a circular holding appears, the acyclic calculation is invalid and must be withheld pending an appropriate method.

If a current permission expressly covers ENTITY-Q and the proposed service, update P-04 with the exact scope and conditions; do not retain the prior gap as an unresolved finding. If the proceeding is shown to involve another legal entity or has a later dismissal, correct P-05 accordingly. All revisions require evidence IDs and an affected-findings ledger.

## Quality boundary

The expected results demonstrate reconciliation and careful labeling on an invented, simple graph. They do not validate entity verification, ownership discovery, regulatory applicability, or the effectiveness of a diligence program. A human reviewer must decide which further evidence is proportionate to the actual intended use and applicable requirements.
