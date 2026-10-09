# Entity Due Diligence — analysis method

## 1. Establish the exact entity and decision

Build an entity spine: legal name, identifier, incorporation jurisdiction, formation date if available, present status, former names, official website association, and relevant group relationships. Record whether each item is independently established, publicly filed, or self-reported. A filed active status does not establish trading activity, financial soundness, or authority to perform a regulated service.

Map the contemplated relationship to the entity expected to contract, perform the service, hold assets, receive payment, and provide recourse. These roles may sit in different subsidiaries. Create separate IDs for each legal person and describe the arrangement in plain language. Do not collapse a brand into one organization simply to simplify a chart.

## 2. Normalize the ownership graph

Represent each direct holding as one edge: owner, owned entity, percentage, share class or interest basis, effective date, source, and uncertainty. Verify that percentages are comparable before summing them. Ordinary equity, voting rights, profit interests, options, and trust powers are not interchangeable. Do not add percentages across incompatible classes without a documented conversion basis.

For each entity and comparable class/date, reconcile disclosed holdings to 100.0%. A positive residual is unresolved ownership unless a documented public-float convention applies. A total above 100.0% usually signals duplication, incompatible dates, or mixed bases; stop the calculation and investigate. Rounding may cause a small residual, but do not label a material gap rounding without evidence. Document the accepted rounding precision.

Identify cycles, cross-holdings, nominees, trusts, partnerships, and intermediate entities before calculating ultimate interests. A simple acyclic ordinary-equity tree can support multiplication along a path and addition across distinct nonoverlapping paths. More complex structures need specialist analysis; do not repeatedly traverse a cycle or assume its residual disappears. Preserve unknown branches instead of redistributing their percentage among known owners.

## 3. Calculate economic interests only under explicit assumptions

For a path of comparable ordinary equity stakes, multiply fractions: 60.0% × 70.0% = 42.0%. If the same ultimate person has another distinct direct 5.0% holding, add it only after confirming no overlap: 42.0% + 5.0% = 47.0%. Record each contributing path so the reviewer can find duplicated edges or a repeated nominee interest.

Call the result an estimated economic interest derived from the supplied ownership schedule. Even exact arithmetic can rely on unverified representations. Do not call a person a legally determined beneficial owner merely because the arithmetic crosses a convenient percentage. Apply relevant legal definitions, control tests, exceptions, and current authority separately. In particular, these proportional calculations must not be reused as an OFAC blocking calculation.

Compute resolved terminal economic ownership as the sum of the known nonoverlapping ultimate interests under the selected basis. It is a completeness metric for the supplied graph, not the probability of identifying all relevant owners. Show unresolved percentage and affected branches. If the graph is cyclic or bases conflict, report the metric NOT ASSESSABLE and explain why.

## 4. Assess control as a separate evidence stream

Review board appointment powers, voting agreements, vetoes, management authority, general-partner roles, trustees, protectors, and nominee arrangements where relevant public evidence exists. Identify what a right allows, who holds it, and its effective period. Do not equate a director, authorized signer, founder, or website spokesperson with ultimate control without evidence of actual rights or responsibilities.

When only economic equity is available, say control is not assessed. Where one person holds a small share but broad appointment rights, describe both facts without forcing them into an ownership percentage. Conversely, dispersed ownership does not prove absence of control. Separate legal interpretation from factual mapping and identify the human expertise required.

## 5. Test the business model against disclosed capacity

Describe products, customers, delivery channels, operating footprint, source of revenue, expected payment flows, and reliance on affiliates or intermediaries. Each statement should have a source and date. Distinguish a business plan from actual operations. Compare publicly available capacity evidence with claimed activity: staffing, licenses, premises, financial statements, service history, or counterparties. Lack of public evidence can be a disclosure limitation, not evidence the business is fictitious.

Normalize financial comparisons to the same entity, reporting period, accounting basis, and currency. Annualizing three months of receipts may be a scenario, but it is not verified annual revenue. Show seasonality and one-off assumptions. If a company reports monthly receipts of $600,000.00 a simple annualized run rate is $7,200,000.00 under a constant-month assumption; do not compare it to audited annual revenue without the qualification.

## 6. Review permissions and adverse information

For any permission claimed to support the proposed activity, capture holder identifier, issuing authority, jurisdiction, service scope, restrictions, effective and expiry dates, and status at cutoff. Test the exact activity and entity. A parent's license might or might not cover an affiliate arrangement; obtain the governing scope evidence instead of assuming either result. A missing license record is an unresolved permission question until jurisdiction and activity requirements are understood.

For adverse information, resolve identity, retrieve the underlying record where possible, identify allegations versus findings, and establish current procedural posture. Record dismissal, settlement without admission, appeal, correction, or ongoing proceeding accurately. Assess relevance to the proposed activity, recency, recurrence, and management involvement. Media volume is not a severity metric, and politically exposed status is not wrongdoing.

## 7. Integrate findings without false precision

Organize findings by identity, ownership/control, business purpose, permissions, adverse information, and evidence sufficiency. State inherent concerns separately from demonstrated controls or mitigating facts. A claimed control receives credit only to the extent there is evidence of its design and operation relevant to the concern. A policy document alone does not show implementation.

Use qualitative priorities with reasons, not an invented universal weighted risk score. If a user supplies an authorized scoring framework, reproduce its definitions, test inputs, show missingness, and distinguish its rating from this pack's evidence confidence. Do not let a low score in one dimension offset a material unresolved permission issue without an explicit governing decision rule.

## 8. Write targeted next steps

Every request should name the question it resolves, exact evidence needed, acceptable public source or authorized excerpt, responsible role, and consequence if unresolved. Prioritize decision-critical gaps over routine completeness. Recommend continued research, specialist interpretation, or a conditional human review as appropriate. Do not prescribe onboarding, offboarding, restrictions, regulatory filings, or public allegations as automatic outcomes.
