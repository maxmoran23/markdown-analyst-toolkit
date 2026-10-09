# Ownership Analysis — worked fictional example

## Question and stipulated evidence

All names, IDs, holdings, and rights in this case are fictional. SYN-001 is the complete fixture. TARGET is an invented legal entity, and HOLDCO is its intermediate shareholder. PERSON-A, PERSON-B, and PERSON-C are synthetic labels with no real identities. The question is: what ultimate economic interests are supported by the supplied ordinary-equity schedule at 2026-09-30, and what remains unresolved?

The schedule is reported rather than independently verified. It is assumed to describe comparable ordinary economic equity, with no preferred rights, cycles, overlapping nominee interests, or undisclosed direct holdings beyond the explicit unknown pool. A separate company statement says PERSON-C has a veto over certain asset sales; the governing document is not supplied. No jurisdiction-specific legal beneficial-owner conclusion is requested or established.

## Direct ownership inputs

| edge_id | owner_id | owned_entity_id | interest_pct | interest_basis | effective_date | evidence_ids | notes |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| OW-01 | PERSON-A | HOLDCO | 60.0 | Ordinary economic equity | 2026-09-30 | SYN-001 | Reported schedule |
| OW-02 | PERSON-B | HOLDCO | 40.0 | Ordinary economic equity | 2026-09-30 | SYN-001 | Reported schedule |
| OW-03 | HOLDCO | TARGET | 50.0 | Ordinary economic equity | 2026-09-30 | SYN-001 | Intermediate stake |
| OW-04 | PERSON-A | TARGET | 10.0 | Ordinary economic equity | 2026-09-30 | SYN-001 | Separate direct stake |
| OW-05 | PERSON-C | TARGET | 25.0 | Ordinary economic equity | 2026-09-30 | SYN-001 | Separate reported veto right |
| OW-06 | UNKNOWN-POOL | TARGET | 15.0 | Ordinary economic equity | 2026-09-30 | SYN-001 | Holders absent |

## Direct reconciliation

HOLDCO: 60.0 + 40.0 = 100.0%. TARGET: 50.0 + 10.0 + 25.0 + 15.0 = 100.0%. Each total has a coherent entity denominator. Adding all six edge percentages yields 200.0%, which has no useful ownership meaning because the two entities' denominators are different. Do not display that graph-wide sum as a completeness score.

The target's direct table is fully allocated numerically, but OW-06 remains unidentified. A residual row is accounting for a gap, not resolving it. Likewise, HOLDCO's own total could reconcile while its source reliability remains limited. Arithmetic completeness and evidential verification are separate.

## Path calculations

PERSON-A has two distinct target paths. Path OW-01>OW-03: 0.60 × 0.50 = 0.30, or 30.0%. Path OW-04: 10.0% direct. Total: 30.0 + 10.0 = 40.0%. The direct path does not overlap the intermediate path under the stipulated schedule.

PERSON-B has path OW-02>OW-03: 0.40 × 0.50 = 0.20, or 20.0%. PERSON-C has path OW-05: 25.0% direct. Known terminal economic interests total 40.0 + 20.0 + 25.0 = 85.0%. UNKNOWN-POOL remains 15.0%. Combined known plus unresolved interests reconcile to 100.0%.

Do not add HOLDCO's 50.0% as another ultimate interest after allocating it 30.0% to PERSON-A and 20.0% to PERSON-B. Doing so would create a false 150.0% target total. Do not allocate the unknown 15.0% pro rata to the three known persons; the evidence says nothing about its holders.

## Expected ultimate-interest rows

| ultimate_id | target_id | economic_interest_pct | path_ids | resolution_state | control_state | claim_class | evidence_ids | notes |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- |
| PERSON-A | TARGET | 40.0 | OW-01>OW-03;OW-04 | RESOLVED ON SUPPLIED GRAPH | NOT ASSESSED | Estimated | SYN-001 | 60.0% × 50.0% + 10.0% |
| PERSON-B | TARGET | 20.0 | OW-02>OW-03 | RESOLVED ON SUPPLIED GRAPH | NOT ASSESSED | Estimated | SYN-001 | 40.0% × 50.0% |
| PERSON-C | TARGET | 25.0 | OW-05 | RESOLVED ON SUPPLIED GRAPH | REPORTED RIGHTS | Reported | SYN-001 | Veto instrument absent |
| UNKNOWN-POOL | TARGET | 15.0 | OW-06 | UNRESOLVED | NOT ASSESSED | Reported | SYN-001 | Holder identities absent |

The result for PERSON-C is a reported direct stake. The calculated layered totals for PERSON-A and PERSON-B are Estimated because they derive from reported inputs and structural assumptions. The arithmetic can be independently reproduced without converting the reported inputs into verified facts.

## Separate sanctions-method counterexample

For this subsection only, hypothetically stipulate PERSON-A as an established blocked seed under the cited OFAC ownership framework. HOLDCO then enters the propagation set through its 60.0% stake. For TARGET, distinct direct stakes from that set are HOLDCO's 50.0% plus PERSON-A's 10.0%, totaling 60.0%. This differs from PERSON-A's 40.0% economic interest. It is a separate rule illustration, not a change to UltimateInterests or a real sanctions determination.

Do not add the 30.0% economic path again to the 60.0% direct-stake total. Do not apply this hypothetical result to other jurisdictions. Other nexus, control, authorization, property history, identity, and current legal applicability remain outside the illustration. No real person is designated or screened by the example.

## Expected findings and next steps

F-01, HIGH materiality, HIGH confidence, Observed: 15.0% of the target's economic interest remains assigned to unidentified holders in the supplied graph. Obtain the missing holder schedule and its effective date. Confidence is in the observed gap, not in any hypothesis about who holds it.

F-02, MEDIUM materiality, HIGH confidence, Estimated: known terminal economic interests total 85.0% under the simple proportional assumptions. Preserve the path register and source status. The result does not establish legal beneficial-owner status or control.

F-03, MEDIUM materiality, LOW confidence, Reported: PERSON-C reportedly has a veto right, but its scope and governing document are absent. Obtain the rights instrument and relevant governance context. Do not conclude control from the word “veto” alone.

The decision recommendation is to use the calculated graph as a qualified research view and request evidence for the unknown branch and reported right before a consequential interpretation. Final disposition remains PENDING. No relationship action or regulatory determination follows automatically.

## Dated update and edge cases

If a completed 2026-10-01 transfer moves 5.0% from UNKNOWN-POOL to PERSON-C, create a new snapshot. At that later date, PERSON-C becomes 30.0%, unresolved becomes 10.0%, and known terminal interests become 90.0%. Do not rewrite the 2026-09-30 results. If only an intention to transfer is announced, retain the original graph and label the change a future scenario.

If HOLDCO's upstream split becomes unavailable, PERSON-A still has 10.0% directly and PERSON-C 25.0% directly. The 50.0% HOLDCO branch and 15.0% unknown pool become unresolved, totaling 65.0%; known terminal interests become 35.0%. Do not retain the old 30.0% and 20.0% derived allocations without their inputs.

If a new record says PERSON-A owns 70.0% of HOLDCO while PERSON-B remains 40.0% at the same date and basis, the 110.0% total fails reconciliation. Do not average PERSON-A's old and new figures to 65.0% or reduce PERSON-B to 30.0% without evidence. Preserve both source claims and resolve the conflict.

If TARGET also owns part of HOLDCO, the simple acyclic calculation no longer applies. Show the circular edge and refer the economic and legal treatment for specialist review. If PERSON-C's 25.0% is actually voting power rather than economic equity, separate the basis and mark the economic target total incomplete until comparable data are available.

## What this example demonstrates

The fixture demonstrates dated graph discipline, direct-versus-derived separation, exact path arithmetic, missing-branch treatment, and distinct legal overlays. It does not discover real owners, verify a share register, establish a universal threshold, or validate the assistant's performance on complex real structures. A human reviewer must decide what further evidence and interpretation are needed for the actual purpose.
