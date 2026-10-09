# Typology and red flags: inputs and evidence

## Two linked units

An event is a source occurrence; an observation is an evaluation of one indicator for one case and window. A case can have several observations, and an event can support more than one observation. Maintain both levels so three related flags do not become three transactions. A typology is an explanatory pattern; an indicator is a testable feature; a finding is a supported analytical statement; a disposition is a human decision. Use these terms consistently.

| Input | Minimum fields | Required meaning |
| --- | --- | --- |
| Event ledger | event_id, case_id, timestamp, direction, amount, currency, payer_id, payee_id, status, source_id | One unique event; preserve raw locator and precision. |
| Entity bridge | case_id, entity_id, relationship_type, evidence_id, valid_from, valid_to | Identity and ownership claims need evidence; similar names are not a sufficient bridge. |
| Referral text | referral_id, author_role, received_at, exact_claim, basis, source_locator | The text is evidence that the claim was made, not necessarily evidence the described event occurred. |
| Indicator register | indicator_id, version, scope, prerequisites, positive_condition, exclusions, counterexplanations | Each indicator must be executable as an explicit question. |
| Public context | source_id, issuer, direct_url, publication_date, accessed_at, relevant_section | Guidance supplies context and definitions, not case facts or automatic decision thresholds. |
| Observation | observation_id, case_id, indicator_id, state, supporting_events, conflicting_events | Keep ABSENT, INDETERMINATE, and NOT_APPLICABLE distinct. |

Record product, channel, declared business purpose, source of funds, payment mechanics, and geography when supplied. Do not manufacture attributes from names, accents, language, nationality, or an address fragment. Distinguish the location of a service provider from the location of its user and from the location of the underlying activity.

## State definitions

PRESENT means the stated indicator condition is supported by the required evidence. ABSENT means adequate evidence covers the stated scope and the condition is not met. INDETERMINATE means a necessary fact is missing, ambiguous, conflicting, or too weak. NOT_APPLICABLE means the indicator's defined scope excludes the case on a supported basis. These states describe one indicator; none is a universal customer risk classification.

A confidence label qualifies the claim being made. High confidence in a posted amount does not imply high confidence in a laundering hypothesis. Low confidence in a referral does not erase the possibility of material harm. Keep evidence strength, indicator state, severity, and review priority as separate fields.

## Reconcile each population independently

First reconcile source items: received equals processed plus duplicate plus excluded plus unparsed plus inaccessible plus deferred. Then reconcile distinct canonical events, with amounts by currency and direction. Finally reconcile planned indicator-case tests: evaluated PRESENT + ABSENT + INDETERMINATE + NOT_APPLICABLE equals the complete test plan. A source document can contain multiple events; an event can support several observations. Never compare these counts as if they were the same denominator.

Freeze the indicator test plan before interpreting results. Add later indicators with an explicit version and reason. Otherwise a search for more flags can inflate the apparent severity of a case without any new facts. Include relevant negative tests, especially where an intuitive concern has an ordinary explanation.

## Evidence handling and classification

Observed includes directly supplied ledger entries and reproducible arithmetic. Reported includes a customer explanation, referral allegation, media statement, or vendor label not independently established. Inferred covers conclusions about a possible pattern or relationship drawn from observations. Estimated covers modeled quantities and must disclose assumptions. A blockchain address label from a commercial source is Reported attribution unless independently corroborated, even if transfers are publicly observable.

For screenshots, capture the visible boundaries, date, missing fields, and whether the underlying document was obtained. A cropped screenshot may omit reversals or context. For transaction narratives, preserve raw wording and normalized categories. Do not let a phrase such as “loan repayment” become proof of a loan without a matching instrument or other appropriate support.

## Public context is not case proof

A red-flag library can be broader than the institution's actual exposure. Map each indicator to its product and data prerequisites. Self-hosted wallets, privacy features, international payments, cash-intensive businesses, and rapid settlement can all have legitimate uses; the analyst must evaluate the actual pattern and context. Do not turn an exposure category into an allegation. When a rule depends on a current official designation or restriction, retrieve the applicable primary instrument and effective date or mark that branch unassessed.


## Public-source register

Sources below were retrieved for package preparation on **2026-10-09**. This records access, not a legal-currency certification. Recheck applicability, amendments, jurisdiction, and institution type for a live task. The methods and illustrative thresholds in this suite are authored analytical conventions, not quotations from or mandates attributed to these sources.

| ID | Source and locator | Publication/version | Applicability and boundary |
| --- | --- | --- | --- |
| AUTH-RF-01 | [FFIEC Appendix F: Money Laundering and Terrorist Financing Red Flags](https://bsaaml.ffiec.gov/manual/Appendices/07) | Online manual; section publication date not stated | Context for indicators that warrant evaluation; not a deterministic proof standard. |
| AUTH-RF-02 | [FATF: Virtual Assets Red Flag Indicators](https://www.fatf-gafi.org/en/publications/Methodsandtrends/Virtual-assets-red-flag-indicators.html) | 2020-09-14 | Virtual-asset typology context; the public report does not make every listed feature inherently illicit. |

Record future retrievals separately using source ID, direct URL, publisher, publication date if stated, retrieval timestamp, page or section, exact proposition supported, and status. Guidance cannot establish the facts of a particular case. An accessible page does not establish the correctness of an attached customer assertion.
