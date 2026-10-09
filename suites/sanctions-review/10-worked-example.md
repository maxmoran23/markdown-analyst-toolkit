# Sanctions Review — worked fictional example

## Narrow scope and stipulated facts

All identifiers and relationships are fictional. SYN-001 covers the entire fixture. BLOCKED-A and BLOCKED-B are stipulated blocked holders for the exercise only; no actual list entry, person, country, or program is represented. The scope is the simple OFAC ownership illustration described in the public source reference in 02. Identity, current authority applicability, other sanctions nexuses, authorization, and real operational disposition are not demonstrated by this fixture.

As of the fictional snapshot 2026-09-30, the comparable ordinary ownership facts are:

| edge_id | owner_id | owned_entity_id | interest_pct | basis | effective_date | evidence_ids | notes |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| S-01 | BLOCKED-A | ENTITY-A | 60.0 | Ordinary ownership | 2026-09-30 | SYN-001 | Remaining 40.0% stipulated nonblocked |
| S-02 | ENTITY-A | ENTITY-B | 55.0 | Ordinary ownership | 2026-09-30 | SYN-001 | Remaining 45.0% stipulated nonblocked |
| S-03 | BLOCKED-B | ENTITY-C | 20.0 | Ordinary ownership | 2026-09-30 | SYN-001 | Distinct direct holding |
| S-04 | ENTITY-A | ENTITY-C | 30.0 | Ordinary ownership | 2026-09-30 | SYN-001 | Remaining 50.0% stipulated nonblocked |
| S-05 | BLOCKED-A | ENTITY-D | 49.0 | Ordinary ownership | 2026-09-30 | SYN-001 | Remaining 51.0% stipulated nonblocked |

There are no cycles, mixed classes, date conflicts, overlapping direct stakes, or unknown residuals in this base case. These simplifying assumptions matter. A real review cannot simply assume them because the source table omits inconvenient branches.

## Propagation trace and economic counterexample

Pass 0 contains only the two stipulated seeds. Pass 1 adds ENTITY-A because S-01 gives 60.0%. ENTITY-D remains below the ownership condition at 49.0%. Pass 2 adds ENTITY-B at 55.0% through S-02 and ENTITY-C at 20.0% + 30.0% = 50.0% through S-03 and S-04. Pass 3 adds nothing; the worksheet has reached a stable result.

The economic product for BLOCKED-A through ENTITY-A into ENTITY-B would be 0.60 × 0.55 = 0.33, or 33.0%. That number answers a different economic-interest question. Using it to dismiss the scoped ownership condition would produce the wrong worksheet result. For ENTITY-C, count S-03 and S-04 once each; do not add an upstream economic fraction again.

The expected decision rows are ENTITY-A 60.0% THRESHOLD MET; ENTITY-B 55.0% THRESHOLD MET; ENTITY-C 50.0% THRESHOLD MET; ENTITY-D 49.0% THRESHOLD NOT MET ON SUPPLIED FACTS. All rows say other_nexus NOT ASSESSED and review_state HUMAN REVIEW REQUIRED. The fourth row is not an all-sanctions clearance.

## Reconciliation and metrics

Five direct edges are supplied. Four reviewed entities have one scoped result each: 4 = 3 threshold met + 1 threshold not met. This ratio is a fixture description, not a population estimate. Final propagation sources are the two original seeds plus three added entities. Do not count ENTITY-D as a cleared counterparty or infer a permission to transact.

Ownership completeness is stipulated by the notes on remaining holders. If those notes are removed, the below-threshold row cannot retain the same completeness claim. The three threshold-met rows still have sufficient known percentages for the mathematical illustration, but the actual legal and factual analysis remains limited to the supported rule and evidence.

## Expected findings

F-01, HIGH consequence, HIGH confidence, Inferred: three entities meet the scoped ownership condition in the fictional graph. Confidence is in the stipulated arithmetic and rule application, not in real ownership verification. Refer the scoped result and remaining questions to the human reviewer.

F-02, HIGH consequence, HIGH confidence, Observed: all four entities lack an assessed other-nexus and authorization review. A full sanctions disposition is therefore not provided. Obtain the actual parties, activity, jurisdictional facts, operative authorities, and authorization evidence before a real decision.

F-03, MEDIUM consequence, HIGH confidence, Observed: ENTITY-D is below the scoped condition only under the explicit assumption that the remaining holders are nonblocked. Preserve that assumption and do not describe the result as a broad clearance.

## Boundary variants

Variant A: replace ENTITY-D's remaining 51.0% stipulated nonblocked ownership with unknown ownership. Known blocked ownership is 49.0%; possible additional relevant ownership ranges from 0.0% to 51.0%. The evidence does not resolve the threshold, so ownership_result becomes INDETERMINATE. Do not choose the favorable endpoint.

Variant B: add a duplicate copy of S-04 under a new source document. The underlying stake remains 30.0%, not 60.0%. Link the duplicate source to the same edge and retain its provenance. ENTITY-C remains at 50.0%, not 80.0%.

Variant C: change the effective date of S-02 to after the review cutoff. Do not use the future stake in the historical graph. ENTITY-B becomes NOT ASSESSED for the historical snapshot unless a valid prior holding is supplied. Present the later graph separately if requested.

Variant D: add broad appointment powers for BLOCKED-A at ENTITY-D. Record a separate control question under the actual applicable authority; do not turn 49.0% into 50.0% by narrative adjustment. The pack's base illustration does not resolve all control-based restrictions.

Variant E: a later notice claims BLOCKED-A sold its interest. Preserve the notice as Reported, obtain completion and ownership evidence, and keep any previously restricted property's treatment separate. The worksheet cannot authorize release.

## Human decision and limits

The correct output is a review packet with explicit assumptions and pending disposition. No transaction was evaluated, no funds were restricted, no report was filed, and no real entity was screened. The exercise demonstrates why distinct direct stakes and a pass trace matter; it does not prove screening performance, legal completeness, or operational compliance. Refresh primary authority and evidence at the actual decision time.
