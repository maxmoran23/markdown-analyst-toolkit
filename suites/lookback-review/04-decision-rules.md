# Decision rules — Historical Monitoring Lookback and Remediation Review

These rules govern the analytical output. They are deliberately explicit so the assistant cannot fill nuanced decisions with an unstated default. They do not authorize operational changes or replace the applicable human process. Use the exact branch that matches the evidence, keep competing interpretations visible and record the evidence needed to move to another state.

## L-R01: Missing expected unit

**Trigger.** An independently supported expected unit ID has no matching retrieved canonical source after the documented reconciliation and identity checks.

**UNKNOWN branch.** If the expected population or identity match is unverified, retain an unresolved population/identity exception; do not assert complete retrieval or fabricate a specific missing record.

**Required branch.** Retain a canonical placeholder and retrieval exception with the independent control evidence.

**Forbidden substitution.** Do not erase the unit or treat its amount and impact as zero.

**Exact specimen or boundary case.** L30 remains in the denominator with source,amount,impact and new_information null.

## L-R02: Duplicate representation

**Trigger.** Stable source keys and inspected content establish that two received representations refer to the same canonical economic or review unit under the declared identity rule.

**UNKNOWN branch.** If identity is uncertain, retain both representations in an unresolved intake bucket; do not deduplicate, discard an amount or force a canonical match.

**Required branch.** Preserve the raw row and map it to the established canonical key.

**Forbidden substitution.** Do not add its amount again or remove it without lineage.

**Exact specimen or boundary case.** RAW-D1 maps to L02 and adds no canonical activity.

## L-R03: Conflicting duplicate

**Trigger.** Two representations are established as the same canonical unit, but inspected material fields or version evidence conflict.

**UNKNOWN branch.** If duplicate identity or the conflicting value is unverified, retain both sources with the unresolved question; do not select or average a value to make totals reconcile.

**Required branch.** Preserve both versions and request authority and timing evidence.

**Forbidden substitution.** Do not select the smaller value to improve an activity total.

**Exact specimen or boundary case.** A changed RAW-D1 amount requires a conflict record before aggregation.

## L-R04: Out-of-scope record

**Trigger.** The record’s verified attributes fail an explicit inclusion condition in the documented current scope.

**UNKNOWN branch.** If attributes, scope authorization or the boundary predicate are unclear, keep the scope classification unresolved; do not silently exclude the record from the expected population.

**Required branch.** Retain it with a precise exclusion reason and assess boundary implications.

**Forbidden substitution.** Excluded does not mean irrelevant or risk-free.

**Exact specimen or boundary case.** The two July rows do not enter January–June totals but keep the July continuity question open.

## L-R05: Retrieved summary only

**Trigger.** The retrieved record is a summary and inspection shows that essential support required for the current substantive review is absent.

**UNKNOWN branch.** If supporting-material completeness is unknown, mark reviewability unverified and request the inventory; receipt alone cannot establish a completed comparison.

**Required branch.** Mark supporting-evidence availability separately from retrieval.

**Forbidden substitution.** A received summary does not prove that a substantive review can be completed.

**Exact specimen or boundary case.** L25–L29 remain UNABLE_TO_ASSESS despite having source rows.

## L-R06: Historical closed status

**Trigger.** An inspected historical decision source explicitly records CLOSED for that unit at a stated cutoff or decision date.

**UNKNOWN branch.** If the historical status or source is unavailable, record UNKNOWN historical state; do not manufacture a prior closure or treat the current review as already complete.

**Required branch.** Preserve it as an original fact and perform the current question independently.

**Forbidden substitution.** Do not infer that newly discovered facts were considered historically.

**Exact specimen or boundary case.** A closed original unit can now require re-review or referral.

## L-R07: No new information

**Trigger.** A completed, adequately supported comparison preserves the historical source, cutoff, facts and rationale alongside recovered/current evidence and finds no material difference under the stated relevance criterion, with no unresolved contradiction or material evidence gap in that comparison’s scope.

**UNKNOWN branch.** If either evidence set, the comparison, materiality assessment or contradiction resolution is incomplete, retain PENDING_REVIEW, REREVIEW_REQUIRED or UNABLE_TO_ASSESS as supported. Do not infer no new information or mark the desk comparison complete.

**Required branch.** Complete only the defined comparison and record its scope and evidence.

**Forbidden substitution.** Do not imply no suspicious activity, no reporting duty or account clearance.

**Exact specimen or boundary case.** L01–L06 have fictional completed comparisons, not actual institutional signoff.

## L-R08: New information

**Trigger.** The historical/current comparison identifies a concrete newly available material fact or contradiction, with source and availability date, that changes the prior identity, scope, purpose or evidential basis under the stated criterion.

**UNKNOWN branch.** If an allegation or possible difference is unverified, retain a pending evidence-assessment route and its exact question; do not assert confirmed new information or make a filing decision.

**Required branch.** Route for authorized case assessment with exact change evidence.

**Forbidden substitution.** Do not automatically decide filing or closure.

**Exact specimen or boundary case.** L07–L12 stay open until a receiving process returns evidence.

## L-R09: Unassessable impact

**Trigger.** A field or source necessary to apply the documented defect-impact predicate is absent, contradictory or otherwise unresolvable at the cutoff.

**UNKNOWN branch.** If the sufficiency of impact evidence has not been checked, retain impact UNKNOWN until the predicate inputs are verified; do not assign affected or unaffected by default.

**Required branch.** Preserve unknown impact and request the source needed to decide it.

**Forbidden substitution.** Do not classify every missing record as either affected or unaffected by default.

**Exact specimen or boundary case.** L30 defect_affected is null rather than false.

## L-R10: Scope expansion

**Trigger.** Specific inspected defect, chronology or population evidence indicates that the current boundary may omit relevant units or that a defined additional review is needed.

**UNKNOWN branch.** If continuity or relevance is uncertain, record a bounded scope question and requested evidence; do not silently expand or declare the existing boundary complete.

**Required branch.** Create a versioned proposal with trigger, predicate and new denominator.

**Forbidden substitution.** Do not silently mix expanded units into an old completion rate.

**Exact specimen or boundary case.** Adding July would require its own independent manifest and new scope totals.

## L-R11: Completion claim

**Trigger.** A completion statement is being prepared for a specifically named work layer, and its numerator, complete denominator and remaining dependencies can be traced to inspected records.

**UNKNOWN branch.** If those controls or statuses are unverified, state that completion is not assessable for that layer and preserve the gaps; do not substitute a different layer’s favorable percentage.

**Required branch.** Name the level and denominator, then all remaining material dependencies.

**Forbidden substitution.** Received-row accounting cannot substitute for complete historical review.

**Exact specimen or boundary case.** 34/34 classified rows coexists with 29/30 retrieved units and 6/30 no-open-action units.

## L-R12: Accepted limitation

**Trigger.** An actual acceptance record identifies the authorized decision maker or role, accepted limitation, affected scope/version, conditions and decision date, and its authority is supported by the supplied governance.

**UNKNOWN branch.** If the acceptance record, authority or scope is missing, retain the limitation as unresolved or proposed for acceptance. Do not record risk acceptance, restricted approval or closure from silence.

**Required branch.** Record actual authorized acceptance and the precise restricted claim.

**Forbidden substitution.** The assistant cannot turn an unresolved gap into risk accepted.

**Exact specimen or boundary case.** No accepted limitation is supplied for missing L30 or the six open referrals.

## Severity and confidence rubric for this specimen

| dimension | decision rule | limit |
| --- | --- | --- |
| HIGH severity | A reproduced loss of intended review, material population gap, silent unknown conversion or major evidence limitation that restricts the central conclusion | Illustrative prioritization; not a statutory rating |
| MEDIUM severity | A material process, lineage or governance weakness requiring correction or human decision, with the immediate effect bounded by the supplied evidence | Do not downgrade merely because the cause is easy to fix |
| LOW severity | A nonmaterial presentation or documentation issue that does not change the population, result or decision | Escalate if it hides a material fact |
| HIGH confidence | Directly inspected evidence or independently reproduced fixture result supports the observation | Does not extend confidence to live effectiveness |
| MODERATE confidence | Partial evidence supports the observation but a credible alternative remains | Name the unresolved alternative |
| LOW confidence | Limited or conflicting material permits only a tentative inference | Do not convert it to an observed finding |
| NOT ASSESSABLE | Necessary evidence is absent and no supported judgment is possible | Maintain the missing-data state rather than inventing a score |

## State-transition record requirements

Every transition must retain prior state, proposed next state, triggering evidence, reason, responsible role and actual disposition when supplied. A state changes because evidence or authorization changed, not because a deadline or dashboard target was reached. Preserve the original transition in the history even when later corrected. A rejected proposal remains visible with its rationale; a reopened item retains the earlier closure basis and the new information that defeated it. The fixture uses completed fictional calculations but leaves actual institutional approvals unrecorded.
