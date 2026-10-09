# Decision rules — Third-Party Service and Assurance Review

## Ordered evidence and reliance gates

| Gate | Condition | Review result | Proposed next step |
| --- | --- | --- | --- |
| 1 | Service identity or intended reliance unclear | Unable to assess | Define relationship and use |
| 2 | Critical dependency or responsibility unknown | Restrict reliance conclusion | Obtain architecture and ownership evidence |
| 3 | Relevant test fails declared criterion | FAILED criterion | Remediate and retest |
| 4 | Required evidence asserted but unavailable | UNVERIFIED criterion | Obtain inspectable support |
| 5 | Evidence covers only part of scope or period | PARTIAL criterion | Define uncovered area and alternatives |
| 6 | Evidence supports exact criterion and scope | SUPPORTED criterion | Human accepts bounded evidence |
| 7 | Material issues remain | No unrestricted recommendation | Human considers conditions, alternative, or exit |

The phrase “no unrestricted recommendation” does not terminate a service or block onboarding. It states the analytical limit of the package. A human may choose a different course with explicit rationale and authority; the assistant preserves the unresolved facts.

## Assurance interpretation table

| Material supplied | Supported statement | Unsupported shortcut |
| --- | --- | --- |
| Questionnaire says encryption used | Provider reports encryption | Encryption independently verified |
| Current certificate with applicable scope | Certificate covers stated scope and dates | Every control and service is effective |
| Historical assurance report | Defined controls examined for stated period | Provider is permanently approved |
| Bridge assertion after report period | Management reports no specified changes | Independent testing extended |
| Report excludes subcontractor | Subcontractor coverage gap identified | Subcontractor failed controls |
| Recovery exercise fails target | That exercise missed criterion | All future recovery will fail |
| Exit export omits IDs | Export completeness unproven | Records permanently lost |

## Tailored exceptions and alternatives

A restricted-use proposal can limit data, access, service scope, volume, or duration if the limits are enforceable and relevant. An alternate provider may reduce concentration only if it does not share the same critical dependency. A manual fallback requires staff, data, capacity, and evidence; a hypothetical fallback is not mitigation.

An exception request identifies the unmet criterion, rationale, consequence, compensating measure, duration, accountable role, monitoring, and termination or escalation trigger. Keep it pending until an authorized human supplies approval. Approval does not rewrite the evidence result; a FAILED test remains failed until a successful retest supports a new version.

## Severity and confidence

HIGH concerns a material gap or failure in a critical relied-on function, unavailable evidence needed to establish that function, or an exit weakness with significant dependency. MEDIUM concerns a substantive supporting gap with bounded consequence. LOW concerns limited improvements that do not materially impair the stated use within the reviewed evidence. These are illustrative review categories, not an institution's risk appetite.

Confidence is claim-specific. A visible export count can be HIGH confidence while the cause of missing records is LOW confidence. A provider's assertion remains Reported even if plausible. Do not increase confidence because several documents repeat the same provider claim. Independence of evidence matters more than the number of copies.

The assistant does not approve a supplier, execute a contract, waive an obligation, make a sanctions determination, transfer data, accept risk, or decide termination. It can recommend a specific course and make the decision package concrete. The final disposition belongs to the authorized service and risk owners.
