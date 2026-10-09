# Alert Adjudication Quality Review — inputs and evidence

## Evidence intake rules

Assign a stable source identifier on receipt. Record the supplied filename or source title, exact internal locator, owner or publisher, creation date, date received, data period, format, accessibility and analytical role. A file name is not proof of authenticity. A bank-looking statement, invoice, exported case note or screenshot must be described as the supplied document until its source and integrity are established. Do not invent verification by implying a direct system extraction when only a user attachment exists.

Preserve the original content and a normalized representation separately. Normalization may standardize a date format, decimal separator or identifier spacing; it must not silently resolve an ambiguous sign, currency, timezone or identity. Record the original value, normalized value, rule and reason. For every transformation that changes inclusion or a calculation, retain enough detail to reverse the transformation. Correcting a spelling error in a display label does not authorize merging two counterparties.

Classify each proposition as Observed, Reported, Inferred or Estimated. Observed describes something visible in the supplied record, such as a posted amount or the words on an invoice. Reported describes an account given by a person or source. Inferred describes a conclusion drawn from records under an explicit reasoning rule. Estimated describes a quantity derived under a stated model or incomplete measurement. A supplied customer explanation remains Reported even when its author is identified. Observation of a document does not make every assertion inside it Observed.

Use availability states AVAILABLE, PARTIAL, INACCESSIBLE, REQUESTED and NOT_SUPPLIED. These are different from reliability. A fully readable source can be unreliable for a particular proposition; a highly credible source can be unavailable in the session. Record which field or span is missing in a partial source. If page three of a four-page contract is absent, do not call the entire contract unavailable, but do not infer the absent clause from the other pages.

## Source independence and corroboration

Count independent origins, not documents. A screenshot, PDF export and spreadsheet row copied from the same underlying system are three representations of one origin. They can help detect transcription differences, but they do not provide three independent confirmations. A customer explanation repeated in an investigator’s note remains the customer’s explanation. An external article quoting the same allegation is not independent substantiation merely because it has a different publisher.

For each material proposition, identify what the source can establish and what it cannot. A posted ledger can establish a booked amount within its stated coverage; it may not establish ultimate beneficial receipt or purpose. A contract can establish the terms represented by its text; it may not prove performance. A review vote establishes the reviewer’s recorded assessment; it does not independently establish the truth of the underlying case. The evidence ledger must preserve those limits beside the source reference.

Resolve conflicts by comparing scope, timing, origin and proposition. Do not rank a source solely by document type or apparent formality. A contemporaneous transaction record may be stronger for a posted amount; a later correction may supersede an earlier entry if its linkage is evidenced. Both remain in the record with the reason for the supersession. Where the conflict cannot be resolved, preserve both accounts and explain which conclusions remain insensitive to it.

## Missingness, zeros and negative evidence

A missing transaction is not a zero transaction. A missing explanation is not evidence that there was no explanation. A search with no result is informative only within its stated population, period, fields and query. Record what was searched, where, when and with which identifiers. “No adverse evidence located” requires a bounded search description; “no adverse evidence exists” usually exceeds the supplied coverage.

Use null when a required value is unavailable. Explain its meaning in the row’s status or rationale rather than converting it to zero or an empty favorable sentence. Zero means the calculation was performed on the stated population and produced zero. NOT_APPLICABLE requires a rule showing why the field does not apply. UNKNOWN means the field applies but cannot be resolved. NOT_TESTED means the procedure was not executed. These states must survive workbook export, dashboard filtering and narrative compression.

## Coverage and controlled substitutions

Keep a received-to-analyzed reconciliation. List duplicate representations, instructions that did not execute, rejected items, records outside the period and partial records separately. An exclusion requires an explicit rule and source locator. If one raw record generates several analytical rows, explain the expansion so users do not mistake row count for source count. If multiple raw records collapse to one canonical event, preserve their linkage and the authoritative source choice.

When an input is absent, state whether the analysis can continue descriptively, requires a bounded scenario, or must stop at a decision gate. A scenario must change exactly the stated assumptions and keep its outputs separate from the base case. Do not invent an opening balance, ownership link, policy deadline or adjudication outcome merely to complete a table. If a bounded range is calculable, report its endpoints, assumptions and feasibility checks instead of fabricating a point estimate.

## Criteria authority and version control

Separate law or regulation, supervisory guidance, supplied institutional policy, supplied procedure, authored analytical method and fictional fixture parameter. Every criterion used to fail a real case must identify its source class and applicable version. A recommendation in public guidance is not automatically an institution’s mandatory field requirement. An internal style preference is not a legal violation. The same source can support a general process principle without establishing a specific quantitative tolerance.

Public-source references in this file were accessed during authoring on Oct 09, 2026. Recheck current applicability before operational use, especially if the case falls under a different jurisdiction, institution type or historical policy. The suite does not provide jurisdiction-specific legal advice or authorize a filing decision. Cite the exact section supporting a regulatory statement; use the authored method label for rules designed for this analytical exercise.

## Exact extraction protocol for mixed attachments

Read the attachment inventory before extracting facts. Give every file a received identifier, even if it is unreadable or later excluded. Record whether the file appears complete, whether page numbers are continuous, whether a worksheet is hidden, whether a screenshot is cropped and whether a message includes its attachments. These observations establish extraction coverage; they do not authenticate the source. If the environment cannot inspect a file component, say which component was not inspected. Never convert an inaccessible page into an empty evidence result.

For a table, preserve its header, units, sign convention, timezone, date range and any footnotes controlling interpretation. A column headed amount may contain debit signs, unsigned amounts with a separate direction flag, or cumulative balances. Determine which before calculating totals. A source may use parentheses for negatives or commas as decimal separators; retain the original string where ambiguity is material. Do not infer transaction currency from a workbook’s default currency formatting. Ask for the source convention or classify the affected values as unresolved.

For a narrative source, extract propositions with exact locators rather than rewriting the entire source into a single confident summary. Capture the speaker or author, what is asserted, the event period described, the source date, whether the statement is firsthand, and any qualification. Preserve conditional language. “May have,” “approximately,” “not confirmed,” “according to” and “subject to” can materially change the claim. A concise paraphrase must keep those limits when they affect a live hypothesis.

For a structured export, inspect whether the identifier is unique within the file, within an account, within a day or globally. A transaction reference reused by several systems may require a compound key. Use the declared grain and crosswalk instead of assuming one column is globally unique. For a case review, a case ID repeated for two reviewers is expected at the vote grain but duplicate at the case-packet grain. The same data can be valid in one table and erroneous in another because the unit of analysis differs.

For an image or scanned page, record transcription uncertainty at the field level. Distinguish unreadable from absent. If a digit could be three or eight, do not choose the value that makes a total reconcile. Retain the uncertainty, identify the possible effect and request a better source if the decision is sensitive to it. If optical character recognition is used, identify that it was used and recheck all material amounts, dates, identifiers and negations against the image when possible.

For a collection of communications, retain the quoted message’s original date and author separately from the forwarding date and forwarder. The forwarding person may add a new claim, but does not become the origin of the quoted claim. A reply that says agreed may refer to only one issue in a long chain; do not treat it as approval of every earlier proposition. If authorization matters, identify the exact decision, scope, authorized role and referenced version rather than inferring broad approval from conversational tone.

## Evidence request design with branching responses

A useful request has a live decision target. State the disputed proposition first, then the minimum records needed to distinguish the surviving explanations. Name the period, counterparties or record identifiers using supplied aliases; avoid open-ended requests for all information where a narrower question is sufficient. Explain internally what a confirming response would establish, what a conflicting response would establish and what a nonresponse would leave unknown. A nonresponse may be operationally relevant under supplied policy, but it is not automatically affirmative evidence of misconduct.

If a response supplies a document, validate its relationship to the requested event. Check identifier, date, amount, parties and purpose. A document can be genuine and irrelevant to the transaction being investigated. If it covers several payments, identify the allocation rather than assigning the full face amount to every payment. If the response supplies only an explanation, retain it as Reported and evaluate its consistency with existing records. Do not promote an explanation to corroborated fact solely because it is detailed or confidently phrased.

If the response partly resolves the issue, split the result. An amount explanation may resolve a price difference while leaving beneficiary linkage unknown. A readable contract may resolve an accessibility problem while leaving actual performance unproved. A revised quality narrative may remove an unsupported phrase while leaving the underlying omitted transaction unchanged. The request ledger should show the precise satisfied component and the remaining open component instead of forcing a binary complete/incomplete label that hides this distinction.

If a response conflicts with an earlier source, create or update the contradiction record. Preserve the original source and the new account. Determine whether the conflict is a correction, a difference in scope, a difference in timing, a different definition or an unresolved factual inconsistency. Do not accuse the source of deception merely because the accounts differ. The next inquiry should target the difference that matters to the decision. A contradiction can be resolved analytically without deciding intent.

If a response is inaccessible, record the actual technical or access limitation. Do not claim the document lacks support when its contents were not inspected. Use the available source metadata only for the propositions it supports, such as that an attachment was supplied. If the user later provides a readable version, assign a version link and reassess the affected claims. Do not count the two versions as independent sources or duplicate economic events.

## Policy-input checklist and unavailable-policy path

A supplied policy input should identify institution type, jurisdiction, relevant business or product, effective date, policy owner, approval status, applicability, required process, escalation roles, exceptions and historical version if the case is being reviewed retrospectively. A title alone is not enough to determine applicability. If the user supplies an excerpt, record whether omitted surrounding text could contain definitions or exceptions material to the judgment. Do not invent the missing portions.

When policy is absent, the suite still supports factual reconstruction, source comparison, arithmetic, bounded hypotheses and a proposed evidence plan. It does not support asserting that an institution breached an unknown internal deadline, failed an unspecified mandatory form, or should make a particular regulated filing. Label the authored method as an analytical criterion where appropriate, and distinguish recommendations from compliance findings. The absence of policy itself can be a scope limitation rather than a defect attributable to the subject of the review.

When policy changes during the case period, identify which version applies to each reviewed decision. Avoid applying the newest standard retroactively without a basis. Record both the contemporaneous assessment and any current-process improvement recommendation as different conclusions. If the organization chooses a stricter current review standard, state that it is a chosen current standard rather than the historical requirement. This distinction matters in quality review and in interpreting what an investigator reasonably knew at a prior cutoff.

## Complete source-use map for the worked case

The following map identifies the exact supplied origins and where the fixed case uses them. It is a navigation aid for source review, not a substitute for reading the raw facts. A source can support a row while leaving its purpose, ownership or authority unresolved.

### Q01 — Fictional case packet C01

**Locator:** 10-worked-example.md, Raw packet C01. **Source-description class:** Observed. **Exact populated dependencies:** CasePackets [C01]; ReviewVotes [V01, V02]; Calibration [C01]; ProcessQA [Q01].
**Bounded proposition:** Posted debit 1000; invoice 1000; beneficiary and delivery match; counterevidence considered. **Permitted quality conclusion:** No material reasoning defect on supplied packet.

### Q02 — Fictional case packet C02

**Locator:** 10-worked-example.md, Raw packet C02. **Source-description class:** Observed. **Exact populated dependencies:** CasePackets [C02]; ReviewVotes [V03, V04]; DefectRegister [D01]; Calibration [C02]; Remediation [M01]; ProcessQA [Q02].
**Bounded proposition:** Investigator described no business support; packet includes matched invoice 2000 and delivery for the same payment. **Permitted quality conclusion:** Material contrary evidence omitted; outcome must be reconsidered without assuming reversal.

### Q03 — Fictional case packet C03

**Locator:** 10-worked-example.md, Raw packet C03. **Source-description class:** Observed. **Exact populated dependencies:** CasePackets [C03]; ReviewVotes [V05, V06]; DefectRegister [D02]; Calibration [C03]; Remediation [M02]; ProcessQA [Q03].
**Bounded proposition:** Original debit 11000 and explicitly linked return 2000; narrative says fully reversed. **Permitted quality conclusion:** Correct net 9000 and review conclusion dependent on the error.

### Q04 — Fictional case packet C04

**Locator:** 10-worked-example.md, Raw packet C04. **Source-description class:** Observed. **Exact populated dependencies:** CasePackets [C04]; ReviewVotes [V07, V08]; DefectRegister [D03]; Calibration [C04]; Remediation [M03]; ProcessQA [Q04].
**Bounded proposition:** Two beneficiaries have similar names but different supplied identifiers; investigator merged them into one subject. **Permitted quality conclusion:** Split identities and recompute aggregate before reassessing.

### Q05 — Fictional case packet C05

**Locator:** 10-worked-example.md, Raw packet C05. **Source-description class:** Observed. **Exact populated dependencies:** CasePackets [C05]; ReviewVotes [V09, V10]; DefectRegister [D04]; Calibration [C05]; Remediation [M04]; ProcessQA [Q05].
**Bounded proposition:** Ledger and narrative amounts match; one non-substantive punctuation defect in an evidence title. **Permitted quality conclusion:** Optional editorial correction; no effect on inference or traceability.

### Q06 — Fictional case packet C06

**Locator:** 10-worked-example.md, Raw packet C06. **Source-description class:** Observed. **Exact populated dependencies:** CasePackets [C06]; ReviewVotes [V11, V12]; DefectRegister [D05]; Calibration [C06]; Remediation [M05]; ProcessQA [Q06].
**Bounded proposition:** Two same-period postings 4000 and 3500 omitted from chronology while present in supplied ledger; net effect 500. **Permitted quality conclusion:** Restore both gross events and recompute period totals; net 500 does not excuse omission.

### Q07 — Fictional case packet C07

**Locator:** 10-worked-example.md, Raw packet C07. **Source-description class:** Observed. **Exact populated dependencies:** CasePackets [C07]; ReviewVotes [V13, V14]; Calibration [C07]; ProcessQA [Q07].
**Bounded proposition:** Opening balance missing; investigator declines source attribution, requests balance and gives descriptive flows only. **Permitted quality conclusion:** Properly bounded analysis; unknown is not itself a quality failure.

### Q08 — Fictional case packet C08

**Locator:** 10-worked-example.md, Raw packet C08. **Source-description class:** Observed. **Exact populated dependencies:** CasePackets [C08]; ReviewVotes [V15, V16]; Calibration [C08]; ProcessQA [Q08, Q09].
**Bounded proposition:** Case conclusion cites an encrypted document unavailable to either reviewer; no equivalent source supplied. **Permitted quality conclusion:** Review cannot determine whether the underlying conclusion is supported.

### Q09 — Fictional case packet C09

**Locator:** 10-worked-example.md, Raw packet C09. **Source-description class:** Observed. **Exact populated dependencies:** CasePackets [C09]; ReviewVotes [V17, V18]; Calibration [C09]; ProcessQA [Q09].
**Bounded proposition:** Narrative uses unresolved purpose; reviewer prefers insufficient corroboration; both reflect same evidence and scope. **Permitted quality conclusion:** Style preference alone is not a defect.

### Q10 — Fictional case packet C10

**Locator:** 10-worked-example.md, Raw packet C10. **Source-description class:** Observed. **Exact populated dependencies:** CasePackets [C10]; ReviewVotes [V19, V20]; DefectRegister [D06]; Calibration [C10]; Remediation [M06]; ProcessQA [Q10].
**Bounded proposition:** Rapid onward transfers are evidenced; conclusion states intent to launder without supporting intent evidence. **Permitted quality conclusion:** Remove unsupported intent assertion and reconsider bounded analytical conclusion.

### Q11 — Fictional case packet C11

**Locator:** 10-worked-example.md, Raw packet C11. **Source-description class:** Observed. **Exact populated dependencies:** CasePackets [C11]; ReviewVotes [V21, V22]; DefectRegister [D07]; Calibration [C11]; Remediation [M07].
**Bounded proposition:** Reviewer worksheet treats absent nonfiling memorandum as a universal BSA breach; supplied fixture policy only requires a brief case rationale. **Permitted quality conclusion:** Use supplied policy CP-QA-1 and actual case rationale; no universal nonfiling memo requirement.

### Q12 — Fictional case packet C12

**Locator:** 10-worked-example.md, Raw packet C12. **Source-description class:** Observed. **Exact populated dependencies:** CasePackets [C12]; ReviewVotes [V23, V24]; Calibration [C12]; ProcessQA [Q09].
**Bounded proposition:** Packet does not identify what evidence was available at original decision date; reviewers see later documents mixed with earlier material. **Permitted quality conclusion:** Cannot assess original decision under hindsight without an availability chronology.

### Q13 — Fictional review votes

**Locator:** 10-worked-example.md, Raw votes R1/R2 across C01–C12. **Source-description class:** Observed. **Exact populated dependencies:** ReviewVotes [V01, V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24]; Calibration [C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12]; ProcessQA [Q01, Q02, Q03, Q04, Q05].
**Bounded proposition and limit:** Original votes precede adjudication. They support agreement calculations, not truth of the underlying case conclusion.

### Q14 — Fictional adjudication minutes

**Locator:** 10-worked-example.md, Consensus C01–C12. **Source-description class:** Observed. **Exact populated dependencies:** CasePackets [C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12]; Calibration [C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12]; DecisionRecord [D01]; ProcessQA [Q06, Q07, Q08, Q09].
**Bounded proposition and limit:** Consensus is later quality adjudication under CP-QA-1. It does not replace original ratings or provide a customer/filing disposition.

### Q15 — Illustrative quality policy CP-QA-1

**Locator:** 10-worked-example.md, Eight criterion cards. **Source-description class:** Observed. **Exact populated dependencies:** CasePackets [C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12]; QualityCriteria [K01, K02, K03, K04, K05, K06, K07, K08]; DefectRegister [D01, D02, D03, D04, D05, D06, D07]; Calibration [C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12]; Remediation [M07]; DecisionRecord [D02, D03]; ProcessQA [Q07, Q08].
**Bounded proposition and limit:** The eight rules are supplied illustrative policy. Do not characterize every rule as a universal legal requirement.

### Q16 — Fictional remediation proposals

**Locator:** 10-worked-example.md, Remediation D01–D07. **Source-description class:** Observed. **Exact populated dependencies:** Remediation [M01, M02, M03, M04, M05, M06, M07]; DecisionRecord [D04]; ProcessQA [Q10].
**Bounded proposition and limit:** Every repair is proposed. No executed correction, independent retest or actual human closure is evidenced.

## Primary authority register and applicability

### A01: FFIEC, Suspicious Activity Reporting overview

[FFIEC, Suspicious Activity Reporting overview](https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04). Accessed Oct 09, 2026. Public supervisory method context for identification, research and decision responsibilities. It does not make the illustrative fixture thresholds binding or establish a fictional subject’s conduct.

### A02: FFIEC, Suspicious Activity Reporting examination procedures

[FFIEC, Suspicious Activity Reporting examination procedures](https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04_ep). Accessed Oct 09, 2026. Public examination context for reviewing policies and execution. This suite’s internal quality rubric is authored methodology, not a claim that every rubric field is mandated.

### A03: FinCEN, October 9, 2025 SAR FAQs

[FinCEN, October 9, 2025 SAR FAQs](https://www.fincen.gov/system/files/2025-10/SAR-FAQs-October-2025.pdf). Accessed Oct 09, 2026. Question 4 clarifies that the BSA and implementing regulations do not require or expect documentation of a decision not to file. Where an institution chooses documentation, the appropriate level depends on its risk-based policies and circumstances. The case ledgers here are an analytical design; any operational requirement must identify supplied policy.

### A04: FATF, Operational Issues: Financial Investigations Guidance

[FATF, Operational Issues: Financial Investigations Guidance](https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Operational%20Issues_Financial%20 investigations%20Guidance.pdf). Accessed Oct 09, 2026. Public financial investigation context. The document concerns countries and competent authorities; it does not confer investigative powers on an analyst or authorize access, contact, surveillance or external disclosure.

These references supply limited public context. The extensive extraction, table, calculation, scenario and release rules in this suite are authored analytical methods. They are not paraphrases of a single authority and must not be presented as binding legal obligations merely because a public source is cited nearby. The worked case does not use public sources as evidence about its fictional subjects.
