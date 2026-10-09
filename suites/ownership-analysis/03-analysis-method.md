# Ownership Analysis — analysis method

## 1. Freeze the entity, date, and denominator

Create an identity record for every node: legal or synthetic ID, name, entity type, jurisdiction, relevant registry, and evidence. Merge aliases only when the same legal person is supported by identifiers or documented changes. Do not merge two subsidiaries because they share a brand, address, director, or website. Record former names with their effective periods.

Set one effective date for the principal graph. Where holdings changed, build separate snapshots. A later filing may disclose an earlier effective ownership date; record both. Separate completed transfers, pending agreements, options, and contingent rights. A proposed transaction is context and a possible future scenario, not a current edge.

Choose the denominator. Ordinary economic equity may be suitable for a simple example, but voting shares, profit participation, partnership capital, trust interests, and preferred rights can differ. If the question requires several bases, build separate comparable groups and label them clearly. Never total 30.0% voting power and 40.0% economic equity as a 70.0% combined interest.

## 2. Register and reconcile direct edges

Enter each direct holding once, with its source and effective period. Multiple documents supporting the same holding add provenance, not another stake. If a source reports both an intermediate stake and a derived ultimate percentage, enter the direct edge in OwnershipEdges and keep the derived assertion in evidence notes until it can be checked. Mixing direct and derived edges in one summation creates double counting.

For each owned entity, basis, class, and date, calculate disclosed comparable holdings and the residual to 100.0%. A positive residual is unresolved unless evidence explains it. A negative residual signals over-allocation: check duplicates, stale records, multiple classes, inconsistent units, or overlapping nominee disclosures. Do not trim the largest holding to force the total to 100.0%.

Rounding must be explicit. If three disclosed holdings are each one-third rounded to 33.3%, a 0.1 percentage-point residual can be labeled rounding only when the underlying description supports it. If the source simply lists 33.3% three times without explaining completeness, record the residual and the assumption. The tolerance for numerical display is not a tolerance for missing owners.

## 3. Identify terminal and unresolved nodes

Trace intermediate entities upstream until the question's terminal type is reached or evidence ends. A natural person may be terminal for an ultimate-person economic view, but a trust or fund requires its own rights analysis. A public company may be retained as an intermediate node if shareholder information is unavailable; do not call it an ultimate natural person or presume an exemption without applicable authority.

Use UNKNOWN-POOL only for a quantified residual whose holder identities are unknown. Use an unresolved intermediate entity when its direct stake is known but upstream holders are missing. Those are different gaps. A 15.0% unknown direct pool and a known 50.0% intermediate stake with no upstream records affect different branches and may require different source requests.

Do not redistribute unknown stakes pro rata among known owners. That would turn absence of evidence into invented ownership. Report known resolved interest, unresolved interest, and unassessable structures separately. If percentages themselves are missing, an amount-based completeness metric may be impossible even when the number of missing edges is known.

## 4. Enumerate paths and calculate simple economic interests

For an acyclic graph with comparable proportional interests, list every distinct path from each ultimate holder to the target. Multiply fractions along each path. Add the resulting path interests only where the paths represent distinct, nonoverlapping stakes. Preserve the ordered edge IDs so the reviewer can reproduce the calculation without trusting a diagram.

For example, a 60.0% holding in an intermediary with a 50.0% target stake produces 30.0% through that path. A separate 10.0% direct target holding produces a total of 40.0% for that holder. Do not also add the intermediary's entire 50.0% to the ultimate person's economic total. The intermediary's stake and its upstream allocations are different levels of the same interest.

Reconcile terminal interests plus unresolved residuals against the target's compatible ownership total. In a fully resolved simple tree, the terminal sum should equal 100.0% within the documented precision. A correct sum does not prove the graph is correct: two errors can cancel. Inspect source edges and at least one independent path calculation in addition to the grand total.

## 5. Handle cross-holdings, cycles, and overlapping rights

Detect whether a path revisits a node. If it does, the simple path method is not applicable as written. Do not continue traversing indefinitely, discard the repeated edge, or declare the cycle fully resolved. Record the cycle's members, direct stakes, source dates, and why it affects the target.

Some economic cross-holding questions can be modeled with simultaneous equations under restrictive assumptions, but a numerical solution alone does not settle legal ownership, control, treasury-share treatment, or denominator definitions. This manual pack requires specialist review of those assumptions before using an alternative method. If the necessary evidence or expertise is absent, show the direct graph and withhold the unsupported ultimate-interest number.

Nominees, custodians, investment managers, trustees, protectors, beneficiaries, and general partners can hold different legal and economic roles. Do not collapse them into one “owner” without explaining the role. A trustee's legal title and a beneficiary's economic rights may overlap as descriptions of the same property; summing them as separate ownership would be wrong. Retain rights and role records alongside the edge table.

## 6. Assess control independently

Inventory appointment/removal powers, voting arrangements, reserved matters, veto rights, management authority, and actual governance arrangements where public evidence is available. Specify whether a right is unilateral, shared, protective, contingent, or limited to particular matters. A veto over one exceptional action is not automatically general control, and a small equity stake does not exclude important governance rights.

Describe observed or reported rights before drawing a conclusion. “Person C is reported to hold a veto over asset sales” is different from “Person C controls the entity.” The latter needs a governing definition and factual context. If the rights document is absent, classify the assertion as Reported and identify the exact source needed. Do not fill the control column with NO simply because equity is below 50.0%.

## 7. Keep legal tests as separate overlays

The economic graph is factual and mathematical input. For each legal question, identify the jurisdiction, applicable entity/institution scope, authority, definition, threshold if any, exceptions, effective date, and responsible reviewer. Do not create one universal beneficial-ownership threshold. A regulatory collection threshold, a control-person test, a tax definition, and a sanctions ownership rule can use different concepts.

When illustrating sanctions ownership propagation, use a separately labeled scenario with established blocked seeds and the applicable rule. Preserve the direct edges and calculation trace. Never overwrite the economic-interest column with a sanctions percentage. A person can have a 40.0% calculated economic interest while a separately scoped propagation scenario reaches a different downstream result; the labels explain why.

## 8. Quantify completeness without a false assurance score

Report the target's direct disclosed percentage, resolved terminal economic percentage under supported assumptions, unresolved percentage, number of source-supported direct edges, and number of unresolved control questions. These are descriptive measures. Do not combine them into an “ownership certainty score.” A fully filled direct table may still have no ultimate-person resolution.

If a known branch's upstream split is missing, show the entire target-equivalent interest of that branch as unresolved under the proportional method. If its possible holders overlap with known persons, report potential overlap without allocating it. Bounds may be useful if assumptions are explicit, but do not present a lower or upper bound as the true holding. Show which missing document would narrow the interval.

## 9. Write a decision-oriented handoff

State the supported graph, calculations, controlling assumptions, unresolved branches, rights questions, and legal overlays not performed. Each request should name the exact edge, denominator, date, or right to resolve. Prioritize gaps by their ability to change the intended decision. Preserve human disposition as pending until an actual reviewer supplies it.

A diagram is optional and must match the edge table. Label direction, percentages, basis, date, and unknown nodes. Do not place an unexplained “ultimate owner” badge on a node just because it is visually at the top. The report should remain intelligible and reproducible if the diagram is removed.
