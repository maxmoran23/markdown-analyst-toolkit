# Correspondent Banking — decision rules

## Relationship gates

| Condition | Analytical treatment | Proposed human next step |
| --- | --- | --- |
| Identity or license uncertain | Incomplete respondent classification | Obtain dated entity-specific evidence |
| Physical presence unknown | Unknown fact, not shell-bank conclusion | Resolve facts under applicable definition |
| No physical presence reported, affiliate support incomplete | Legal classification unresolved | Obtain affiliation and supervision evidence |
| Qualifying affiliate evidence supplied | Potential exception support within applicable framework | Authorized legal classification review |
| Nested role cannot be established | UNRESOLVED access role, distinct from field completeness | Obtain role or agreement evidence; preserve unknown count and value |
| Nested activity matches declared scope | Supported arrangement within packet | Assess controls and current operating evidence |
| Nested activity undeclared at relevant date | Specific scope exception | Clarify role and authorization chronology |
| Message fields repaired by cutoff | Historical defect plus current repair | Assess whether broader process work is warranted |
| Message fields still absent | Open information gap | Targeted request and applicable escalation review |

The table is an analytical convention. It does not authorize opening, closing, restricting or processing an account. A jurisdiction-specific legal prohibition must be assessed under its own conditions and exceptions. A risk-based approach does not override a binding prohibition, and a generalized concern does not create one.

## Shell-bank distinctions

Separate three questions: whether the relevant definition applies, whether the factual elements are established, and whether an exception is supported. UNKNOWN presence is not the same as established absence. A regulated-affiliate exception cannot be inferred solely from ownership by a named group. The evidence must address the legally relevant affiliation and supervision conditions. A human with appropriate authority decides the applicable classification.

The fictional CB03 record deliberately reports no separate physical presence while supplying affiliation and consolidated-supervision evidence. Its outcome is LEGAL_CLASSIFICATION_REVIEW, not automatic prohibition and not unqualified approval. CB02 has unknown presence and incomplete control evidence; it remains FOLLOW_UP. Neither outcome certifies the respondent's legal status or risk acceptability.

Do not use 'shell company', 'shell bank', 'offshore bank' and 'digital bank' interchangeably. A company structure, booking location or delivery channel may raise questions but does not itself satisfy a legal banking definition. State the exact factual question that remains open instead of relying on a loaded label.

## Correspondent responsibilities and limits

Risk-sensitive due diligence on the respondent and targeted follow-up on its activity can require information about particular underlying transactions or customers. That differs from assuming a universal duty to perform full customer due diligence on every respondent customer. The applicable law, account arrangement and detected issue determine the actual inquiry. Document those links when proposing a request so the question is useful and proportionate.

A respondent's role in controlling its customers does not make the correspondent passive. The review should assess its own service scope, monitoring evidence, information gaps and escalation criteria. A questionnaire cannot transfer away a duty. Equally, a lack of visibility into every downstream private record should not be portrayed as proof of prohibited activity when the current question can be resolved through a targeted and lawful request.

## Severity and confidence

HIGH severity is reserved for a consequential unresolved transparency, access or legal-classification issue within the stated decision. MEDIUM covers a material information gap or historical defect with a supported current repair. LOW covers supported ordinary activity or a limited issue without an identified material unresolved gate. These are illustrative priorities; the local human reviewer sets operational urgency.

HIGH confidence applies to direct message fields or explicit reviewed agreement terms within scope. MODERATE may apply to an inferred access pattern with supporting role evidence but unresolved authorization. LOW applies to unsupported allegations or substantial gaps. NOT ASSESSABLE is appropriate where critical role or legal facts are absent. High confidence that a field is missing does not establish high confidence in intentional concealment.

## Alternatives and disposition

For unexpected nested activity, test message-role error, incomplete declaration, later amendment, ordinary bank beneficiary and genuine unauthorized access. For missing fields, test extraction loss, message conversion, source omission and actual message deficiency. For apparent presence gaps, test a branch or group structure and the relevant legal definition. Preserve evidence that supports a benign explanation, with the same standards applied to concerning facts.

An accepted explanation closes only the specific issue it resolves. A repaired payment does not prove every payment is complete. An agreement amendment does not retroactively authorize prior activity unless its actual terms and applicable interpretation support that conclusion. A favorable license record does not prove controls operated effectively.

Recommend a bounded information request where the answer could change the disposition. Keep proposed, issued, answered, validated and closed states distinct in the case record, mapped into the existing action fields in 07. A missing response is not evidence that a request was refused if issuance was never shown. No filing, account restriction or respondent communication is executed by this suite.
