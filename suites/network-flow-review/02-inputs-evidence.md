# Network and Funds Flow Review — inputs and evidence

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

### N01 — Fictional canonical transfer ledger

**Locator:** 10-worked-example.md, Raw edges E01–E24. **Source-description class:** Observed. **Exact populated dependencies:** Nodes [A1, A2, P, Q, R, C, D, E, F]; EconomicEdges [E01, E02, E03, E04, E05, E06, E07, E08, E09, E10, E11, E12, E13, E14, E15, E16, E17, E18, E19, E20, E21, E22, E23, E24]; BalanceChecks [B01, B02, B03]; PatternTests [P01, P02, P03, P04, P05, P06]; AllocationBounds [AL01, AL02, AL03, AL04]; AttributionScenarios [AS01, AS02, AS03, AS04]; DecisionRecord [D02, D03, D04]; ProcessQA [Q01, Q02, Q03, Q04, Q05, Q06, Q07, Q08, Q09].
**Bounded proposition and limit:** The ledger establishes the supplied edges and amounts. Complete external-node activity and ultimate source attribution remain unavailable.

### N02 — Fictional account identity and balances

**Locator:** 10-worked-example.md, A1/A2 ownership and balances. **Source-description class:** Observed. **Exact populated dependencies:** Nodes [A1, A2]; BalanceChecks [B01, B02, B03]; PatternTests [P02, P04]; AllocationBounds [AL01, AL02, AL03, AL04]; AttributionScenarios [AS01, AS02, AS03, AS04]; DecisionRecord [D01, D02]; ProcessQA [Q02, Q04, Q05, Q06, Q08].
**Bounded proposition and limit:** The ownership record supports A1/A2 consolidation and supplied balances only. It does not establish control of any other node.

### N03 — Fictional return references

**Locator:** 10-worked-example.md, E08→E03 and E21→E15. **Source-description class:** Observed. **Exact populated dependencies:** Nodes [C, D]; EconomicEdges [E08, E21]; PatternTests [P05].
**Bounded proposition and limit:** The exact references support only E08→E03 and E21→E15. Opposite direction without this reference is not a linked return.

### N04 — Fictional onward transfer extracts

**Locator:** 10-worked-example.md, E10 and E18. **Source-description class:** Observed. **Exact populated dependencies:** Nodes [E, F]; EconomicEdges [E10, E18]; PatternTests [P03, P06]; DecisionRecord [D03, D04]; ProcessQA [Q07, Q09].
**Bounded proposition and limit:** Two onward extracts support E10/E18. They do not provide complete E/F account histories or establish how those edges were funded.

### N05 — Fictional raw intake manifest

**Locator:** 10-worked-example.md, 28 raw representations. **Source-description class:** Observed. **Exact populated dependencies:** ProcessQA [Q01].
**Bounded proposition and limit:** The manifest explains received-to-canonical counts. A confirmed duplicate or instruction is a representation category, not a new economic edge.

### N06 — Illustrative graph method charter

**Locator:** 10-worked-example.md, Fixture GP-1; source allocation bounds. **Source-description class:** Observed. **Exact populated dependencies:** AllocationBounds [AL01, AL02, AL03, AL04]; AttributionScenarios [AS01, AS02, AS03, AS04]; DecisionRecord [D02, D05]; ProcessQA [Q06, Q08, Q10].
**Bounded proposition and limit:** The charter defines illustrative bounds and attribution conventions. It is an authored method, not observed source tracing or a legal presumption.

### N07 — Customer purpose statement

**Locator:** 10-worked-example.md, Statement G-X01. **Source-description class:** Reported. **Exact populated dependencies:** the common evidence register and narrative.
**Bounded proposition and limit:** The customer statement supplies a reported purpose account. It does not establish identity, actual performance or the source of commingled funds.

### N08 — Fictional period and temporal order

**Locator:** 10-worked-example.md, Hour-index E01 through E24. **Source-description class:** Observed. **Exact populated dependencies:** the common evidence register and narrative.
**Bounded proposition and limit:** The hour index establishes fixture ordering. Real date-only inputs would require intervals and might not support the same temporal path.

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
