# Analysis method — Historical Monitoring Lookback and Remediation Review

The following is an authored operational method for the supplied analytical task. Its sequence and fixture parameters are toolkit choices, not an assertion that a regulator prescribes these exact steps. Execute each applicable stage and retain a specific reason when a stage is blocked or outside scope. The completed specimen in file 10 shows the full record trail.

## M01: Write the defect hypothesis

Describe the failure mechanism, affected data or logic, timing evidence and plausible impact pathway. Separate established facts from possible exposure. A technical defect can affect population, features, routing or reasoning differently.

**Exact specimen checkpoint.** The fixture describes a mapping defect relevant to January through June. Its exact effect on L30 cannot be assessed because the record is absent.

**Failure or competing explanation.** Do not label every in-scope unit affected merely because it falls in the period; preserve known affected, known unaffected and unassessable impact states.

## M02: Set an evidence-based historical boundary

Choose initial start and end dates from version, source and business evidence. Add a boundary-testing plan for adjacent periods and related populations. Record inclusions, exclusions and unresolved assumptions.

**Exact specimen checkpoint.** The analytical fixture includes all 30 manifest units from January through June. July rows are preserved as exclusions while continuity evidence is requested.

**Failure or competing explanation.** If later evidence shows the same defect in July, propose expansion and reconcile a new denominator; do not quietly add July findings while retaining a 30-unit completion rate.

## M03: Freeze the independent manifest

Retain every expected canonical unit and period count before comparing retrieval. The manifest is a control population, not a list manufactured from successfully received records.

**Exact specimen checkpoint.** Five units per month produce 30 expected units. L30 remains in CanonicalUnits with missing source and amount.

**Failure or competing explanation.** If the original manifest was generated using the same broken mapping, its agreement with retrieval cannot prove completeness; seek a genuinely different control.

## M04: Inventory all received representations

Assign a unique raw ID to each received row and retain source period, representation and amount. Classify it as canonical, duplicate, out of scope or unresolved under the supplied rules.

**Exact specimen checkpoint.** The fixture has 34 raw rows. Twenty-nine are canonical,3 duplicate and 2 out of scope. Every raw row is accounted for exactlyonce.

**Failure or competing explanation.** A raw row with conflicting identity is unresolved, not automatically a duplicate selected to make totals reconcile.

## M05: Resolve duplicates without losing history

Choose canonical identity from stable keys and preserve every alias. Compare fields before collapsing duplicate representations. A second copy with a corrected value may require a version chain rather than deletion.

**Exact specimen checkpoint.** RAW-D1 maps to L02, RAW-D2 to L12 and RAW-D3 to L22. Their amounts match the canonical record in this fixture.

**Failure or competing explanation.** If RAW-D1 changes the amount, flag a source conflict and state which version is authoritative for which cutoff before summing activity.

## M06: Reconcile counts by period

Compare expected units, raw representations, duplicate rows, retrieved canonical units and missing units for each historical slice. An aggregate match can conceal offsetting period defects.

**Exact specimen checkpoint.** January throughMay each retrieve 5/5. June retrieves 4/5. Total 29/30 remains incomplete even though all 34 received rows were classified.

**Failure or competing explanation.** A surplus duplicate inMarch cannot offset a missing canonical unit inJune; distinct-grain counts must never be netted together.

## M07: Reconcile financial amounts at canonical grain

Sum each known canonical unit once in a common currency. Keep missing amounts outside the known sum with an explicit unknown count. State what the amount represents and what it does not.

**Exact specimen checkpoint.** Known activity for L01 through L29 is 449500 USD. L30 isnull. Duplicate amounts 37500 and July amounts 64000 are excluded from that canonical sum.

**Failure or competing explanation.** Do not call 449500 the complete scoped activity amount, a loss, or illicit funds. It is only the known canonical amount in the supplied fixture.

## M08: Preserve original and current states

Keep historical status and rationale intact while assigning a current lookback state. New evidence changes the present review, not what the historical analyst knew. Record comparison evidence and the reasoning for any different recommendation.

**Exact specimen checkpoint.** Original CLOSED, ESCALATED and NOT_GENERATED states remain unchanged. Current review states determine lookback workload separately.

**Failure or competing explanation.** A current referral cannot be backdated into the original decision record. Preserve the chronology and distinguish correction from historical fact.

## M09: Assess defect exposure per unit

Apply the established impact mechanism to each record when the necessary fields exist. Mark inability to assess when evidence is missing. Track uncertainty separately from exposure priority.

**Exact specimen checkpoint.** Twenty of 29 retrieved units have defect_affected=true,9 false. L30 impact isnull. These flags do not determine whether review is complete or whether reporting is required.

**Failure or competing explanation.** Afalse impact flag means the defined defect predicate was not met on available evidence; it does not establish that the unit has no other risk.

## M10: Triage for fresh comparison

Use defect relevance, new information, prior rationale gaps and missing support to assign a review route. Avoid allowing an old closed state to bypass a materially different current question.

**Exact specimen checkpoint.** L01–L06 have complete no-new-information comparisons;L07–L12 require case review;L13–L18 require re-review;L19–L24 are pending;L25–L29 areunable;L30 ismissing.

**Failure or competing explanation.** If a completed unit receives new material evidence, reopen its current lookback state with a new transition; preserve the prior completion packet.

## M11: Perform a historical-versus-current comparison

State the original facts and rationale, the newly recovered evidence, what changed, what remains supported and the resulting proposed route. Distinguish a new allegation from corroborated new activity.

**Exact specimen checkpoint.** Six completed comparisons find no new information within their supplied scope. Six others identify new information and remain in an open referral route.

**Failure or competing explanation.** No-new-information means the comparison found no material difference within the reviewed evidence; it is not an exoneration or a conclusion about all activity.

## M12: Route cases with explicit handoff tracking

Prepare a referral with unit IDs, trigger, new evidence, historical context, unresolved questions and requested decision. Track actual acknowledgment separately from preparation and final disposition separately from acknowledgment.

**Exact specimen checkpoint.** All six L07–L12 referrals remainHANDOFF_OPEN. No actual receiving acknowledgment or decision is supplied.

**Failure or competing explanation.** Do not mark a referral closed because a report was created or a proposed action row names a recipient role.

## M13: Control scope expansion

Define each trigger, proposed additional population, inclusion predicate, needed evidence and stopping condition. Assess adjacent periods, related systems or products only through an explicit scope record.

**Exact specimen checkpoint.** EX-01 addresses April–June; EX-02, missing L30; EX-03, referrals; EX-04, re-reviews; EX-05, missing support; and EX-06, July continuity. All are proposed or blocked.

**Failure or competing explanation.** A new finding outside the original scope requires a visible denominator change and revised plan; it cannot be hidden as a narrative aside.

## M14: Measure progress using distinct completion levels

Report intake accounting, retrieval coverage, completed desk comparisons, units with no open action, downstream referral disposition and whole-review acceptance separately.

**Exact specimen checkpoint.** The fixture has 34/34 raw accounting,29/30 retrieval,12/30 desk comparison,6/30 no-open-action,0/6 referral disposition and 0/1 whole-review approval.

**Failure or competing explanation.** Do not choose the largest percentage as the headline completion rate. State exactly which work layer each numerator represents.

## M15: Define stopping evidence before closing

Completion requires the population accounted for, material review and evidence dependencies resolved or expressly accepted by the authorized process, and required downstream handoffs tracked. The toolkit does not supply an automatic materiality waiver.

**Exact specimen checkpoint.** Twenty-four units retain an open dependency, including six referrals and eighteen other review or evidence gaps. The lookback remains incomplete.

**Failure or competing explanation.** A human may choose a restricted acceptance in a real process, but the record must state the limit and authority; this fixture contains no such acceptance.

## M16: Preserve a defensible completion package

Retain source manifests, raw aliases, canonical records, comparison packets, state histories, calculations, findings, scope changes, open items and actual acceptance evidence. Preserve prior versions and source cutoffs.

**Exact specimen checkpoint.** The case package contains all 30 expected units and all 34 received representations. Missing L30 stays visible rather than disappearing from the final report.

**Failure or competing explanation.** Do not delete source records or prescribe a retention period from this suite; use the applicable supplied requirements and authorized records process.

## Calculation order and invariant handling

The calculation order is defect chronology, independent expected population, raw retrieval inventory, identity resolution, canonical selection, period reconciliation, available-amount total, historical-versus-current comparison, review route, expansion and completion. Do not start with a percentage complete calculated from the successfully retrieved population. That sequence would make unavailable L30 disappear before the denominator is established. The expected population must remain visible at every stage, including missing placeholders that cannot yet support a substantive review.

Three conservation equations have different grains. Raw received rows 34 =canonical representations 29 +duplicate representations 3 +out-of-scope representations 2. Expected in-scope units 30 =retrieved canonical units 29 +missing units 1. Review states 30 =completed no-new-information 6 +referred 6 +re-review 6 +pending 6 +unable 5 +not-retrieved 1. Each equation is necessary but none substitutes for another. Duplicate rows cannot cure missing units, and completed referral preparation cannot cure an unresolved downstream decision.

Amount accounting uses canonical units with known values. The sum of L01 through L29 is 449500 USD. Duplicate representations add 37500 USD and excludedJuly rows add 64000 USD, so the raw received representation sum is 551000 USD. The difference 101500 USD is explained by those two categories; it is not a discrepancy to be allocated to L30. The missing unit’s amount remainsnull. Do not subtract the known canonical total from a representation total and call the residual missing activity.

Desk completion is a narrow state. Twelve comparisons have been performed, but six produced new-information referrals whose receiving decisions are absent. Only six units have no open desk-review action in the fixture. Eighteen units have not completed desk review: six re-review, six pending, five unable and one missing. Adding the six open handoffs produces 24 units with an unresolved dependency. These counts are mutually traceable to the 30-unit ledger and support the conclusion that the lookback remains incomplete.
