# Typology and red flags: analytical method

## 1. Convert the question into testable propositions

Start with the observed condition, not a crime label. “Three payments reached one recipient” is testable; “the recipient is laundering money” combines several unproven propositions. Decompose a proposed concern into event existence, identity relationship, temporal pattern, economic explanation, and possible intent. Identify the evidence needed for each proposition and leave unsupported links open.

Select only indicators relevant to the product, channel, period, and accessible data. Write the selection basis before counting results. Include a negative or benign comparison for each selected family. A typology library is a search aid, not a menu from which to choose enough flags to justify a conclusion already reached.

## 2. Construct the evidence map

Create one canonical event per source transaction and keep a separate mapping from events to observations. Normalize timestamps, direction, amount units, status, and identifiers. Resolve duplicates using actual transaction identity; do not collapse different payments with the same amount. Keep reversal and correction links. Establish whether statements are complete for the chosen window, including zero-activity periods.

Create separate edges for ownership, control, transaction, employment, address sharing, and reported association. Do not equate these relationships. Two entities sharing an address may use a service provider; two wallets transacting may be counterparties rather than jointly controlled. Preserve the source and strength of each edge. A path through two uncertain links is not stronger than its premises.

For each observation, record supporting events, contradictory events, missing prerequisites, and a proposed benign explanation. An evidence map should make it possible to remove a source and see which conclusions fail. Multiple news stories repeating the same allegation are one origin, not independent corroboration.

## 3. Apply the illustrative register

RF-01 rapid movement: evaluate eligible external credits of at least $5,000.00, an outward/inward ratio at least 0.90, and a subsequent outward event within 24 hours of the first eligible credit. Exclude confirmed same-owner transfers. Require complete relevant amounts and ordered timestamps. This detects temporal co-occurrence, not exact tracing.

RF-02 many-to-one receipts: count distinct independently identified payer IDs to one case in 24 hours; PRESENT at three or more. Count identities, not rows, and document aggregation across aliases. Two payments from one payer produce one payer. Unknown identity cannot be counted as a new distinct party by default. A processor may aggregate many underlying payers; record what the supplied data can actually distinguish.

RF-03 repeated related payments: require at least three distinct posted payment events for one case within 24 hours. The indicator is intentionally descriptive; it makes no reference to a reporting threshold or an intent to evade it. An uncorroborated narrative reporting three payments is INDETERMINATE. Returned or duplicated instructions are not three executed events.

RF-04 one-to-many distribution: count distinct payee IDs receiving posted debits from one case within 24 hours; PRESENT at three or more. Document whether payees are separate legal entities, separate accounts, or unresolved labels. A payroll batch or marketplace settlement can satisfy the condition while having an ordinary business explanation.

The four thresholds are authored controls for this example. They are neither universal suspicious-activity criteria nor deployment recommendations. In a live review, use approved indicator definitions and preserve any differences from this version.

## 4. Compute measures without manufacturing certainty

For a ratio, record numerator, denominator, currency, included events, and exclusions. A zero or unknown denominator produces null. For distinct counts, retain the underlying identity list. For elapsed time, retain both event IDs and timestamps. For network paths, list each edge and its basis. Do not hide identity assumptions in a count or causal assumptions in a chart arrow.

A high ratio can be explained by normal settlement. A high count can be explained by payroll. A large payment can be explained by a documented asset sale. The question is whether the complete pattern and supplied context support a concern after these alternatives are tested. Arithmetic should be exact even when economic interpretation remains uncertain.

Avoid assigning points simply because several indicators co-occur. RF-01 and RF-02 may be supported by the same three events and may not be independent. A weighted total requires a justified scale, correlation treatment, calibration, and stated interpretation. Without those, show a transparent matrix of observations and use reasoned human prioritization.

## 5. Compare competing explanations

For each case write at least one concerning hypothesis and one plausible benign hypothesis grounded in the facts. Do not invent a remote benign story simply to create balance, and do not omit a strong benign explanation because it weakens a favored conclusion. State what each hypothesis predicts and which available facts agree or disagree.

For A, rapid onward movement predicts receipts followed by a debit but says little about purpose. Ordinary supplier consolidation predicts a real supplier relationship, invoice or contract, timing consistent with settlement, and a matched payment reference. The supplied ledger supports timing but cannot distinguish purpose. The next inquiry should seek the discriminating records rather than repeat a broad request for “more KYC.”

For B, confirmed common ownership predicts movement within the same customer's holdings. That evidence supports a limited exclusion from RF-01. It does not prove the source of funds or eliminate every other possible indicator. For C, repeated narrative descriptions may reflect three events or three descriptions of one event. Only the original ledger can resolve uniqueness. For D, one payee cannot satisfy a three-payee condition within the complete supplied window.

## 6. Address common interpretation traps

Do not call repeated below-threshold payments structuring without evaluating the applicable reporting requirement, aggregation rules, surrounding circumstances, and evidence relevant to intent. A decimal pattern or amount near a threshold is a lead for review, not proof of evasion. Do not publish operational threshold avoidance guidance or imply that payments below a number are safe.

Do not infer criminality from privacy-preserving technology alone. Separate technology use, observable flows, counterparty attribution, and prohibited conduct. Do not equate geographic exposure with nationality or residency. Do not infer beneficial ownership from transaction adjacency. Do not treat absence of adverse media as proof of legitimacy, especially when name coverage is weak or sources are inaccessible.

Do not treat an alert closure in another system as independent proof unless the reviewed population, rationale, evidence, and date are known. A previously explained pattern can change; a previously unexplained pattern may later receive corroboration. Keep versioned observations and the basis for changes.

## 7. Build a proportionate inquiry plan

Prioritize the questions that can change the decision. For each gap, name the required source, likely custodian, expected fields, urgency basis, and consequence of nonavailability. Avoid broad requests for sensitive information when a narrower evidence item would answer the question. Preserve the current conclusion if a requested record does not arrive; do not infer guilt from delay alone.

Present indicator counts separately from case priorities. A case with one well-supported urgent concern may merit greater attention than a case with five weak correlated flags. Record severity and confidence independently, and explain how missing data affects each. The report should let a reviewer accept a limited result, request further inquiry, or challenge the rule itself.

## 8. Test the interpretation before release

Try to make the conclusion fail. Remove duplicate sources, reverse an uncertain identity link, add the strongest supported ordinary explanation, and reduce the lookback to the actually observed period. State which finding remains and which must weaken. Run the synthetic example and boundary tests before presenting a generalized methodology as complete.

The end product is an evidence-based inquiry recommendation. It cannot establish a predicate offense, identify a person as criminal, authorize a filing, or decide account treatment. Those decisions remain with the approved human process and applicable legal standards.
