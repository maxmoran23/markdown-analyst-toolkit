# Analysis method — Third-Party Service and Assurance Review

## 1. Define the relationship being assessed

Describe the contracted service, actual use, legal entity, customer population, delivery locations, data handled, access privileges, and critical business process. Separate what the provider promises, what the contract requires, and what evidence shows. A service can be important because of data access even when its monetary spend is small. Conversely, a high spend alone does not establish criticality.

State review type: proposed onboarding, renewal, periodic reassessment, material change, incident response, or exit. For a renewal, compare the current scope and evidence with the last approved version. Changes to subprocessors, hosting, data use, support access, ownership, product configuration, or recovery design can alter reliance even if the commercial name is unchanged.

## 2. Assess inherent dependence and proportionality

Identify the consequence and timing of service failure, unauthorized activity, incorrect output, data loss, unavailable evidence, and exit difficulty. Consider scale, reversibility, substitution, concentration, and the organization's own capability to detect problems. Set review depth based on these characteristics rather than running the same large checklist for every low-impact service.

Use qualitative criticality with a clear reason. A critical review decision service with no immediate alternative warrants closer evidence scrutiny than a non-sensitive optional reference tool. Unknown facts do not automatically imply the worst conceivable outcome, but material uncertainty must prevent an unsupported low-risk conclusion. State what evidence would reduce uncertainty.

## 3. Map dependency and responsibility chains

List primary service, hosting, storage, reference data, support, network, identity, and fallback dependencies relevant to the intended use. Identify which party controls configuration, access, incident detection, remediation, customer notification, records, and termination. For each link record whether it is contractually disclosed, observed in architecture, or only reported by the provider.

A proposed fallback may share the same cloud region, storage provider, identity service, or data supplier as the primary. Test shared dependencies before calling it independent resilience. In the fixture, SV01 and SV05 both rely on SV02 storage. Switching review providers may not restore access when that storage fails. That is a bounded architectural observation, not a claim that the provider will fail.

Fourth-party evidence can be direct, included in an assurance scope, separately reviewed, or unavailable. Do not assume the prime provider's report covers every subcontractor. If a component is excluded, determine what complementary evidence or oversight exists and whether it is adequate for the use. Lack of direct contract can affect the practical ability to obtain evidence or enforce change; identify the route through the primary contract.

## 4. Evaluate assurance scope before reputation

Read the service/system description and period before relying on an opinion or certification badge. Compare the actual service and configuration to the examined scope. Identify locations, products, controls, and subservice organizations included or excluded. A favorable report on a different product is not equivalent evidence for this service.

Inspect relevant exceptions and how management responded. An exception may be isolated or material to the relied-on control; evaluate the specific consequence and period. A clean opinion is not a guarantee of no incidents or no residual risk. A report ending last year is not necessarily “expired”; it establishes a defined historical coverage period and leaves a later interval requiring assessment.

Separate provider controls from customer-side controls required for the arrangement to work. If an assurance report assumes the customer reviews privileged access, that responsibility does not disappear because the provider supplied a report. Obtain the customer's relevant evidence where permitted. Missing user-control evidence may restrict reliance even if provider testing was satisfactory.

## 5. Assess operational and resilience evidence

Compare service performance measures to the actual scope and denominators. Uptime may exclude maintenance, partial degradation, dependent services, or customer-specific failures. A provider's aggregate availability figure may not describe the period or function under review. Preserve the source definition and exclusions before treating a metric as evidence.

For recovery, separate restoration of the service, reconciliation of data, resumption of critical controls, and resolution of pending work. Recovery time is the elapsed time to the defined recovered state. Recovery point or data lag concerns how current the recovered data is under a declared definition. A system available in four hours may still fail the required state if records are incomplete.

Review test design, scenario, environment, dependencies, timing, expected result, actual result, exceptions, and retest. A planned exercise is not a completed exercise. A tabletop can test roles and decisions but may not prove technical recovery. The fixture uses an executed rehearsal with six-hour recovery against a four-hour criterion and twenty-minute lag against fifteen; both deviations remain visible.

## 6. Assess contract support without inventing enforceability

Map critical reliance assumptions to the supplied terms: service scope, performance definitions, incident communication, access and audit rights, subcontracting, data location and use, confidentiality, retention, return and deletion, change notification, termination assistance, and responsibilities. These are review topics to tailor, not universal prescribed clauses.

Distinguish executed terms from draft schedules, sales commitments, and unsigned amendments. A proposed24-hour notification clause is not an operative obligation merely because it appears in a negotiation document. Whether a clause is legally sufficient or enforceable requires the appropriate legal review. The assistant can identify a gap and draft questions, not accept terms or give a binding legal opinion.

If bargaining power limits a desired term, assess the remaining risk, available alternatives, monitoring, and authority needed for an exception. Lack of a preferred clause does not automatically require rejection for every service. Equally, a signed clause does not prove that the operational capability exists. Evaluate the service-specific consequence.

## 7. Test exit and portability

Define what must transfer or remain accessible at exit: records, metadata, audit trail, open cases, configuration, historical outputs, keys, and required retention evidence. Specify export format, completeness, integrity, permissions, and time. A successful download is not a complete exit if important fields or records are missing.

Reconcile expected and returned populations by stable IDs and relevant totals. In the fixture,985 returned of 1000 expected is 98.5%, but fifteen unexplained records prevent a completeness conclusion. Determine whether omissions are valid exclusions, extraction defects, access problems, or retention issues. Do not delete the expected IDs to make the ratio100%.

Assess how work continues during transition and who resolves outstanding obligations. Verify access removal and data disposition against applicable requirements and human-approved instructions. Data deletion is not a default action of this suite. A recovery plan that depends on an unavailable provider to release exports should be challenged as a dependency.

## 8. Form a bounded reliance recommendation

Combine the evidence by service and critical dependency, not by averaging questionnaire answers. A serious unresolved control reliance issue cannot be cancelled by strong marketing materials or many low-impact passing checks. Recommendations can support human consideration, propose a restricted or conditional relationship, recommend more evidence before reliance, or identify a basis for a human decline or exit discussion.

If conditional reliance is proposed, name the residual issue, interim measure, owner, date, monitoring, trigger, and evidence needed to clear it. The measure must address the actual failure mechanism and be feasible at expected scale. Do not call an untested fallback a proven mitigation.

Record what was not assessed, including unknown fourth parties, absent current evidence, inaccessible contract terms, incomplete financial information, and unperformed public-source research. Recommend a review cadence or event trigger proportionate to the service, but do not create schedules or operate the relationship. Acceptance, renewal, termination, and communications remain authorized human actions.
