# Correspondent Banking — inputs and evidence

## Intake perimeter

Record the legal entities on both sides, relevant branches, service agreement, account function, review period, currencies and jurisdictional nexus. Distinguish a respondent-bank customer relationship from an isolated payment intermediary role. The same institution can occupy different roles in different flows. A group-level profile may not establish a particular subsidiary's license, control scope or permission to provide nested services.

| Input | Required analytical use | If missing |
| --- | --- | --- |
| Respondent identity and license | Match legal entity, issuer and relevant date | Classification remains incomplete |
| Service agreement | Identify permitted products, nested access and responsibilities | Do not infer contract terms from payment behavior |
| Ownership and supervision | Understand control and any regulated-affiliate claim | Keep legal classification open |
| Physical-presence facts | Apply the relevant definition to documented facts | Unknown does not mean no presence |
| Controls and testing | Distinguish policy statements from operating evidence | Record representation-only support |
| Payment population | Stable IDs, lifecycle, fields, amounts and control totals | Limit rates to available records |
| Requests and repairs | Original message, reply, verified repair and timestamps | No presumed completion from an unanswered request |
| Legal criterion | Jurisdiction, provision, applicability and date | Use illustrative analytic criteria only |

## Public references and status

REF-FATF-CB: [FATF, Guidance on Correspondent Banking Services](https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Guidance-Correspondent-Banking-Services.pdf), October 2016, especially paragraphs 1–4 and 9. Reviewed on 2026-10-09. This is international guidance, not self-executing domestic law. It supports risk-sensitive respondent due diligence and transaction follow-up, and clarifies that FATF does not require systematic due diligence on every respondent customer. It does not remove the correspondent's own applicable duties. Apply current domestic rules and the specific service context.

REF-SHELL: [FFIEC BSA/AML Manual, Prohibition on Correspondent Accounts for Foreign Shell Banks; Records Concerning Owners and Agents](https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/12), reviewed on 2026-10-09. This US examination manual explains the prohibition and regulated-affiliate exception by reference to 31 CFR 1010.605 and 1010.630. Its applicability is US-specific. Lack of physical presence and a qualifying regulated-affiliate relationship are separate factual questions; the manual is not a basis to classify every digital or branch-light bank as prohibited.

The four-field payment criterion in the worked example is an invented testing convention. It is not a complete implementation of FATF Recommendation 16, an international messaging standard or any domestic wire-transfer rule. Before making a legal noncompliance finding, identify the currently applicable provision, institutional role, message type, value threshold if any, effective date and exceptions. Do not assume that a historic guidance document defines every current field requirement.

## Relationship evidence and representations

Give each evidence item a stable ID and exact locator. Preserve issuer, title, relevant date, actual access status, legal entity, service scope, source class and limitations in the full case record. Map these into the common Evidence columns in 07. A respondent questionnaire is a representation until tested against suitable evidence. A signed answer is evidence that the respondent made that statement; it does not prove the control operated effectively.

For ownership and supervision, separate parent affiliation from consolidated supervision and the relevant licensed entity. For physical presence, collect facts relevant to the applicable definition rather than relying on office photographs or a website address. A registered-agent address may differ from the place where management and operations occur. Do not infer either presence or absence from silence in a short public profile.

For controls, distinguish policy design, implementation, operating sample, independent testing and remediation evidence. Note who performed testing and what period and services it covered. A broad positive assessment may exclude the exact nested product under review. A stale report can support historical design without proving present effectiveness. Lack of public detail often means the public-source review cannot resolve the question; it does not establish a control failure.

## Payment evidence and completeness

Retain the original message and each amendment or repair as separate lifecycle versions linked by payment_id. Distinguish rejected, pending, settled, returned and canceled states when available. A corrected message may cure current missing information while the original defect remains relevant to process analysis. Do not count a repair message as a second economic payment or subtract a return without the measure specifically requiring net settlement.

The example uses transaction amounts as review exposure measures, not suspicious proceeds or loss. Keep currency native and preserve the sign convention. Count separate economically distinct payments separately even if their references resemble one another. Deduplicate only with supported identifiers and lifecycle evidence. A shared amount and date are insufficient by themselves.

Nested access means a respondent provides other financial institutions access through its correspondent arrangement. Payable-through functionality raises a different question about access by underlying customers. Document the actual access mechanism and responsibilities; do not infer payable-through access merely because a message names a downstream institution. A funds transfer involving a bank as beneficiary is not automatically nested use.

## Missing evidence and bounded conclusions

Track inaccessible sources, missing attachments and unanswered information requests distinctly. The available public or fictional packet may be inadequate for an operational determination. Preserve that limit without manufacturing customer records, hidden banking ties or supervisory facts. A record of an information request supports that the request was made only when actual issuance is evidenced; a proposed request remains proposed.

Public country context can inform a defined risk question but cannot substitute for relationship evidence. Apply the same identity and source-quality standards to benign and concerning material. Record contrary facts, remedial changes and restrictions already evidenced so the report does not portray an obsolete configuration as current.

## Unresolved payment roles

An identified bank in a payment field is not enough to classify nested use. Preserve the exact role label and any uncertainty about message conversion or extraction. If the record identifies NB-02 but does not establish whether it obtains downstream access or merely receives payment as a beneficiary, retain NB-02 as the identifier and set nested_state UNRESOLVED. If the identity also is absent, use UNKNOWN for underlying_bank_id. These cases remain in full-population payment and value totals; their nesting status is not zero and is not silently excluded.
