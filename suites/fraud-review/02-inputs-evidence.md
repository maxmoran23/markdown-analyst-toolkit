# Fraud review: inputs and evidence

## Incident, instruction, and payment are different units

One incident may include several instructions, several executed payments, and several recoveries. Preserve those relationships before aggregating. A screenshot of an instruction proves that the message exists; it does not prove payment execution. A complaint establishes that a person reported a concern; it does not resolve authorization, liability, or loss. The review should make these distinctions visible from the first table.

| Input | Minimum fields | Required interpretation |
| --- | --- | --- |
| Incident | case_id, discovered_at, reported_at, alleged_mechanism, reporter_role, urgency_facts | Do not infer a scheme classification beyond the evidence. |
| Instruction | instruction_id, received_at, requested_amount, currency, requested_payee, channel, purported_author | Keep requested and executed amounts separate. |
| Execution | transaction_id, instruction_id, posted_at, amount, currency, status, actual_payee | Ledger status controls the execution claim; pending and rejected states are distinct. |
| Return/recovery | recovery_id, original_transaction_id, posted_at, amount, status, currency | Only confirmed realized returns reduce the defined unreturned measure. |
| Authorization | asserted_authorizer, approved_channel, verification_record, effective_time, evidence_id | Distinguish valid credentials, genuine instruction, and customer authorization. |
| Technical evidence | access_event_id, device_or_session_ref, time, source, extraction_scope | Logs are evidence of system events, not automatic attribution to a person. |
| Claim or complaint | statement_id, statement_time, exact_allegation, supporting_records | Preserve Reported classification and contradictory evidence. |

Additional evidence can include account-change history, beneficiary changes, original message headers, approval logs, vendor master changes, signed amendments, trusted-channel confirmations, and existing incident records. Use only authorized material. Never ask the assistant to obtain credentials, contact a purported vendor, or access a compromised account.

## Amount dictionary

Requested amount is the amount in an instruction or allegation. Executed amount is a confirmed posted payment. Pending amount is unresolved payment status and must not be silently included in executed totals. Confirmed return is realized value explicitly linked to an executed payment. Net unreturned equals confirmed executed amount minus confirmed linked returns for the specified scope. It is a flow measure, not a legal loss measure.

Attempted suspected-fraud amount can include an unexecuted suspicious request, but label it as attempted and state the review basis. Confirmed loss requires a separately supported definition, accounting treatment, and as-of date. Customer reimbursement shifts who bears exposure; it does not by itself recover money from the recipient. Insurance recovery, chargeback, merchant reversal, and interbank return are different mechanisms and must not be double counted.

## Reconciliation

Reconcile raw source items into mutually exclusive terminal buckets. Then reconcile incident count, instruction count, execution count, and return count separately. Match recoveries to original payments using explicit references or a documented linkage analysis. An identical amount and nearby date alone may be insufficient.

For each case verify `confirmed_returns <= executed_amount` unless a documented overreturn or additional credit explains the difference. Do not clip a negative net value to zero to hide an error. Aggregate by currency. Distinguish known totals from complete totals when one case is unresolved. Unknown execution is null, not zero; unknown recovery is null, not an assumption of no recovery.

Keep ordinary transactions in the reviewed population while excluding them from a specifically defined suspected-fraud subtotal. This allows the case count to reconcile without inflating exposure. A payment deemed ordinary for this review can still have a nonzero unreturned amount because ordinary payments are not expected to return. Explain the metric rather than relabeling that amount a loss.

## Authorization evidence hierarchy

Use the actual approved verification process as the criterion when provided in an authorized environment. A known-channel confirmation means a documented contact route established independently before the suspect message; a callback number supplied in the suspect message is not independent. A signature, familiar name, matching email display name, or successful login alone may not resolve whether the instruction was genuine.

Do not assume valid credentials mean authorized intent, or that a customer-approved payment cannot involve deception. Conversely, a new beneficiary or urgent request can be legitimate. The analyst must evaluate instruction origin, approved process, independent verification, and actual execution without treating any single feature as dispositive.

## Preservation and source limits

Keep original messages, header fields where supplied, filenames, timezones, and payment references. Avoid altering original evidence. Capture transformations and redactions. If a screenshot lacks headers, say so; do not invent a spoofing diagnosis. If logs are missing, identify the attribution question that remains open. Do not run attachments, enable macros, or follow an embedded recovery link.

Public-source guidance supports contextual patterns and response considerations. It does not establish a live incident, current legal entitlement, a reporting deadline, or permission to contact another institution. Current obligations depend on jurisdiction, institution type, product, and the authorized process.


## Public-source register

Sources below were retrieved for package preparation on **2026-10-09**. This records access, not a legal-currency certification. Recheck applicability, amendments, jurisdiction, and institution type for a live task. The methods and illustrative thresholds in this suite are authored analytical conventions, not quotations from or mandates attributed to these sources.

| ID | Source and locator | Publication/version | Applicability and boundary |
| --- | --- | --- | --- |
| AUTH-FR-01 | [FinCEN FIN-2019-A005: Updated Advisory on Email Compromise Fraud Schemes](https://www.fincen.gov/system/files/2019-07/Updated%20BEC%20Advisory%20FINAL%20508.pdf) | 2019-07-16; pages 1–3 and operational context | US advisory context for compromised business processes and payment instructions; not case proof or an automatic response rule. |
| AUTH-FR-02 | [FinCEN: Advisory to Financial Institutions on E-mail Compromise Fraud Schemes](https://www.fincen.gov/resources/statutes-regulations/guidance/advisory-financial-institutions-e-mail-compromise-fraud) | 2016-09-06; read with 2019 update | Historical pattern reference; the 2019 advisory updates relevant definitions. |

Record future retrievals separately using source ID, direct URL, publisher, publication date if stated, retrieval timestamp, page or section, exact proposition supported, and status. Guidance cannot establish the facts of a particular case. An accessible page does not establish the correctness of an attached customer assertion.
