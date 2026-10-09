# Investigation review: inputs and evidence

## Case boundary and evidence dictionary

Define the referral question, subject scope, product scope, review dates, and decision-maker. Record how the case began: alert, complaint, referral, periodic review, or external information. The trigger is a lead, not a conclusion. Do not broaden the subject population because names look similar or because a source mentions an unrelated person.

| Input | Minimum fields | Interpretation requirement |
| --- | --- | --- |
| Referral | case_id, received_at, originating_role, alleged_condition, source_locator | Preserve allegation wording and the distinction between author and source. |
| Transaction record | transaction_id, account_id, event_time, posting_time, direction, amount, currency, status, related_transaction_id | One posting leg; link returns without deleting original events. |
| Entity record | entity_id, aliases, relationship_type, basis, effective_date | Distinguish identity, ownership, control, and commercial relationship. |
| Document | evidence_id, title, issuer, document_date, received_at, locator, version, completeness | Record what is visible and what is missing. Document appearance is not authenticity. |
| Statement | speaker_role, statement_time, claim, direct_or_hearsay, corroboration | A statement remains Reported until the proposition is independently supported. |
| Inquiry record | question_id, requested_item, request_status, response_status, relevance | A proposed request is not an executed request. |
| Chronology | event_id, event_time, event_type, evidence_id, claim_class | Use event time; preserve discovery time separately if material. |

The complete case file may include profiles, statements, payments, invoices, contracts, delivery evidence, account activity, public records, and previous reviews. Receive only authorized material. Do not invent access to communications, identity services, law-enforcement records, or internal systems. If privileged or restricted material is present, follow the approved handling rules; this public suite does not create access authority.

## Population reconciliation

Maintain a source-item inventory separate from events and transactions. One invoice can support a document event without being a payment. One statement can describe several alleged events without proving their existence. One payment can have several document copies. Reconcile received source items into processed, duplicates, scope exclusions, unparsed, inaccessible, and deferred.

Inaccessible means a referenced or supplied item cannot actually be inspected. It remains in the inventory and in limitations. Do not claim a contract supports a payment merely because its filename appears in a folder. A duplicate should point to the retained item and state how identity was confirmed. If two versions differ, preserve both and resolve version authority rather than call the inconvenient copy a duplicate.

## Provenance and custody

For every item record who supplied it, when it was obtained, original locator, source type, version, transformations, and availability. If the approved environment permits a file hash, record it as an integrity aid; do not treat a matching hash as proof of truth or authorship. For a pasted excerpt, preserve page and paragraph boundaries and note omissions. For OCR, retain original image and extraction uncertainty where policy permits.

Classify each proposition at the level it deserves. Observed: a ledger displays a posted debit. Reported: a customer says the debit purchased equipment. Inferred: the sequence is consistent with rapid onward movement. Estimated: a modeled quantity based on incomplete observations. The invoice's visible face amount can be Observed while its genuineness and underlying delivery remain unverified.

## Time and identity reconciliation

Keep event time, posting time, document date, receipt time, and analyst discovery time distinct. A later-discovered old invoice belongs in the historical chronology by document date, with a separate receipt note. Do not imply the investigator knew it earlier. If time is approximate, use a bounded interval and do not create a precise ordering within that interval.

Normalize names only for search and comparison; retain original text. Build identity bridges from stable identifiers or corroborating records. A supplier trading name might differ from its legal beneficiary, but that explanation requires evidence. A name mismatch is a discrepancy to investigate, not proof of fraud. Record negative and ambiguous matching results.

## Amount reconciliation

Use separate measures for gross debits, gross credits, returns, net unreversed value, alleged loss, and confirmed loss. These amounts answer different questions. A supplier invoice is a document amount, not a ledger flow. A return requires a link to the original payment before it reduces net unreversed value. If the link is only inferred, show gross amounts and the uncertainty separately.

Do not mix currencies without a recorded rate and conversion basis. Preserve fees and taxes as separate components when explaining an invoice/payment difference. Do not manufacture a tax or fee explanation to make two amounts agree. The difference itself is an observed discrepancy; its cause is a hypothesis.


## Public-source register

Sources below were retrieved for package preparation on **2026-10-09**. This records access, not a legal-currency certification. Recheck applicability, amendments, jurisdiction, and institution type for a live task. The methods and illustrative thresholds in this suite are authored analytical conventions, not quotations from or mandates attributed to these sources.

| ID | Source and locator | Publication/version | Applicability and boundary |
| --- | --- | --- | --- |
| AUTH-INV-01 | [FFIEC Appendix L: SAR Quality Guidance](https://bsaaml.ffiec.gov/manual/Appendices/13) | Online manual; section publication date not stated | Context for clear chronology and description; this suite prepares a case review and does not file a SAR. |
| AUTH-INV-02 | [FFIEC: Suspicious Activity Reporting](https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04) | Online manual; section publication date not stated | Human decision-process context; no case-specific filing threshold is supplied here. |

Record future retrievals separately using source ID, direct URL, publisher, publication date if stated, retrieval timestamp, page or section, exact proposition supported, and status. Guidance cannot establish the facts of a particular case. An accessible page does not establish the correctness of an attached customer assertion.
