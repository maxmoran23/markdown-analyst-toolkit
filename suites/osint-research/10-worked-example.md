# OSINT Research — worked fictional example

## Fictional case and question

Every organization, identifier, license, publication, and event below is invented. SYN-001 is this fixture as a whole; D-01 through D-06 are its source-item locators. No web search about these invented names is required or appropriate. REF-PROV supports the provenance method, not the fictional facts.

Question: Can a research note cite four public claims about Aster Quay Research as established facts? Intended cutoff is 2026-09-30. The fictional entity identifier is AQ-104 in Fictional Register North. The intended use is an internal-style generic research exercise, not a real relationship decision. The provisional answer is: one narrow registry-status claim is supported; the other three require qualification or further work.

## Supplied fixture records

| Item | Fictional source and date | Relevant content | Upstream family |
| --- | --- | --- | --- |
| D-01 | Register extract, 2026-09-30 | AQ-104, Aster Quay Research, status active | F-REG |
| D-02 | Company page, published 2026-09-01 | AQ-104 claims current research-services license and 240 employees | F-COMPANY |
| D-03 | License register extract, 2026-09-30 | AQ-104 license L-77 expired 2026-06-30; no renewal in extract | F-LIC |
| D-04 | Trade story, 2026-09-03 | Repeats “240 employees,” expressly citing D-02 | F-COMPANY |
| D-05 | Newsletter, 2026-09-05 | Reprints D-04's staffing statement | F-COMPANY |
| D-06 | Award register, 2026-08-20 | Award granted to Aster Quay Labs, identifier AQ-901 | F-AWARD |

A seventh requested item, the fictional court docket, was not supplied and could not be assessed. It is an access gap in Q-05, not a reviewed source item. The license register is assumed accurate for this exercise only; a real session must assess source scope, legal effect, subsequent changes, and identifier resolution.

## Extraction and identity reasoning

D-01, D-02, and D-03 identify AQ-104. D-04 and D-05 repeat D-02 and add no independent staffing measurement. D-06 identifies AQ-901, so its award cannot be assigned to AQ-104 on name resemblance. Keep the award claim IDENTITY UNRESOLVED unless the question is simply whether the supplied award record names AQ-104; for that narrower proposition the record does not support it. This distinction prevents an analyst from silently changing the question to obtain a cleaner answer.

C-01 states only that the registry recorded AQ-104 as active at the cutoff. It does not establish solvency, business operations, or permission to offer regulated services. C-02 repeats the company's claim of a current license; D-03 contradicts it for the same identifier and cutoff. C-03 is a reported staffing assertion without independent measurement. C-04 is not supported because the award's identifier differs.

## Expected Claims table

| claim_id | proposition | claim_class | status | confidence | support_families | contradiction_ids | evidence_ids | notes |
| --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| C-01 | Entity recorded active at cutoff | Observed | SUPPORTED | HIGH | 1 | | SYN-001 | D-01; register-status scope only |
| C-02 | Entity holds current stated license | Reported | CONTRADICTED | MODERATE | 1 | D-03 | SYN-001 | D-02 supports assertion; D-03 opposes underlying fact |
| C-03 | Entity has 240 employees | Reported | UNRESOLVED | LOW | 1 | | SYN-001 | D-02, D-04, D-05 share origin |
| C-04 | Subject received the award | Reported | IDENTITY UNRESOLVED | NOT ASSESSABLE | 0 | | SYN-001 | D-06 concerns AQ-901 |

## Arithmetic and reconciliation

Six documents were reviewed. D-01 through D-05 are eligible for the target, while D-06 is a different-identifier candidate retained for transparency: 6 = 5 eligible + 1 ineligible. Four original families are represented among all reviewed documents: F-REG, F-COMPANY, F-LIC, F-AWARD. Three families contribute eligible target evidence. For the employee claim specifically, three documents map to one original assertion. Do not report “three independent sources confirm 240.”

Five planned searches are represented in SearchCoverage. Q-01 registry: reviewed 1, eligible 1. Q-02 license: 1 and 1. Q-03 employee statement: 3 and 3. Q-04 award: 1 and 0. Q-05 court: 0 and 0, ACCESS LIMITED. Planned-search completion is 4 / 5 × 100 = 80.0%. This measures completion of the five planned review tasks. It does not mean 80.0% of relevant public information was found.

Claim counts reconcile as 4 = 1 supported + 1 contradicted + 1 unresolved + 1 identity unresolved. Do not average these into a confidence percentage. C-02 has one supporting family because the company's assertion is still evidence of what it reported; the contrary regulator extract is recorded separately and controls the current provisional interpretation of the underlying licensing fact.

## Expected findings and recommendation

F-01, HIGH consequence, MODERATE confidence, Inferred: the current-license claim is inconsistent with the supplied fictional register. Seek the current license record and any renewal or appeal document before treating the claim as established. High consequence reflects the proposed citation's importance, not an accusation of wrongdoing.

F-02, MEDIUM consequence, HIGH confidence, Observed: the three staffing publications have one origin. Attribute the 240 figure to the company or omit it pending independent support. Confidence is high in the observed copy lineage, while confidence in the actual headcount remains low.

F-03, MEDIUM consequence, HIGH confidence, Observed: the award record carries a different identifier. Exclude it from affirmative support for the target and request linkage evidence if the award matters. The award could belong to an affiliate, a former entity, or an unrelated organization; none is established here.

## Counterfactuals and stopping point

If an authenticated renewal effective before the cutoff is supplied, revise C-02 after confirming it belongs to AQ-104 and actually covers the claimed service. If a payroll headcount extract is supplied, examine its date and population before comparing it with 240. If D-06 is linked through a documented legal-name change, reconsider identity using the effective dates. If the court docket remains unavailable, preserve the gap; it neither supports nor contradicts any allegation.

The exercise is complete when the claims, lineage, totals, and limitations agree across outputs. It has not measured real-world OSINT recall, confirmed any real license, or established a real entity's reputation. A human reviewer decides whether the remaining qualified claims are suitable for the intended use.
