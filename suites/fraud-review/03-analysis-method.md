# Fraud review: sequential method

## 1. Identify time-sensitive facts without executing actions

Start with whether funds may still be pending or moving, whether access may remain compromised, whether additional instructions are active, and whether an authorized responder is already engaged. Separate established facts from reported urgency. A current unanswered payroll allegation can require urgent human attention even when execution is unknown.

State the immediate decision questions: confirm payment status; confirm authorization evidence; assess possible further exposure; preserve relevant records; route the issue through the approved response process. The assistant prepares this package. It does not hold payments, disable access, recall funds, contact customers, notify law enforcement, or change records.

## 2. Build the incident and payment map

Assign stable case, instruction, payment, and recovery IDs. Link records using actual references, preserving uncertainty where references are incomplete. Keep repeated notifications of one incident from becoming multiple losses. Conversely, do not collapse a series of distinct payments because one complaint describes them together.

Capture request time, approval time, execution time, discovery time, report time, recovery request time if documented, and realized return time. These times answer different questions. A recall request before settlement is not proof the payment was stopped; only a verified status supports nonexecution. A claimed recovery is not realized until the relevant records confirm it.

## 3. Establish payment status

Classify each instruction as not submitted, rejected, cancelled, pending, executed, partially returned, fully returned, or unknown, using supplied system evidence. If status records conflict, preserve the conflict and use UNKNOWN until the authoritative source resolves it. Do not infer execution from an email saying “sent,” or nonexecution from a fraud analyst's intended action.

For partial execution, separate the executed portion and unexecuted remainder. For a batch, keep each child payment and the batch control total. For multiple currencies, preserve original units and convert only with an approved rate basis. Fees may remain after a return; show them separately and do not assume full economic recovery from principal returned.

## 4. Reconcile the monetary measures

Calculate per case: requested, confirmed executed, confirmed linked returns, and net unreturned. Include dates and currency. If execution is unknown, leave both executed and net unreturned null even when the requested amount is known. If execution is known but return evidence is incomplete, do not report a final net figure without disclosing the assumption or bounded range.

Define portfolio subtotals before calculating them. The worked example's known suspected-fraud unreturned amount includes F01 and F02, excludes unresolved F03 from the numeric sum with a visible gap, and excludes ordinary F04 from the fraud subtotal while retaining it in the reviewed population. The resulting 30,000.00 USD is a known subtotal, not complete portfolio exposure.

Do not count customer reimbursement as recovery from the perpetrator. If 5,000.00 USD is reimbursed to a customer while the original funds remain unrecovered, describe the allocation of exposure, not a 5,000.00 USD reduction in external loss. If several systems report the same return, deduplicate it by recovery identity before summing.

Avoid “fraud prevented” or “savings” claims based solely on rejected requests. A 15,000.00 USD unexecuted request establishes no execution within the supplied evidence; the counterfactual loss that would otherwise have occurred is not directly observed. Label the measure confirmed unexecuted request amount.

## 5. Assess the instruction and authorization path

Compare the request with the approved process effective at the time. Identify who purportedly requested it, who approved it, what verification was required, which checks occurred, and what evidence supports those checks. A signed amendment can be genuine or forged; a callback can be independent or routed through an attacker-supplied number. Evaluate the actual record rather than the label.

For a suspected supplier-impersonation case, inspect changes to beneficiary, contact details, timing, message origin, and supporting contract. A documented supplier denial through a preexisting trusted channel is relevant; it does not identify the attacker or resolve all liability questions. If the supplied record is a staff note of a denial, classify the underlying denial as Reported while recognizing the note itself is observable.

For possible account takeover, distinguish a suspicious login, successful authentication, session action, beneficiary change, and payment execution. Shared networks, travel, device replacement, and delegated access may explain anomalies. Do not treat device or IP evidence as direct identity attribution. Request approved-source logs to resolve sequence and authorization where necessary.

For authorized-payment deception, a customer may have intentionally sent money under false pretenses. That differs from proving unauthorized account access. Keep both possibilities open when the evidence supports them. Do not use a single “authorized” field to decide liability or whether a fraud inquiry is justified.

## 6. Test benign and adverse alternatives

A new beneficiary may reflect a genuine supplier account change; verify it against independently established contact details and supporting documents. An urgent request may reflect a legitimate deadline; examine whether it bypassed required controls. An employee complaint may describe a misunderstanding or a genuine unauthorized change; the correct next step is evidence acquisition, not dismissal or automatic confirmation.

For every case state the strongest concerning interpretation, the strongest supported ordinary explanation, and the specific evidence that distinguishes them. In F04, an amended contract plus trusted-channel confirmation supports an ordinary change. In F01, supplier denial and execution support urgent suspected-fraud review. In F03, the absence of logs leaves execution and authorization unresolved; it must not be silently treated as either loss or no loss.

## 7. Evaluate controls without confusing outcome and design

Map each observed event to the control expected to prevent, detect, or respond to it. Distinguish a missing control, an unperformed control, an ineffective performed control, and missing evidence of performance. A loss does not by itself prove every control failed; a prevented request does not prove the entire control environment is effective.

Record the criterion, observed operation, evidence, consequence, and proposed remediation. If a control exception is found, test whether the issue is isolated or may affect a broader population before generalizing. Do not deploy rule changes or tighten thresholds from this small synthetic example. Such changes need a separately approved design, testing, and impact assessment.

## 8. Prepare time-sensitive proposed actions

Write actions for authorized roles, with the exact decision needed and factual basis. Examples include confirming current payment status, preserving records, assessing permitted recall/recovery routes, checking whether related instructions remain active, and coordinating approved fraud, security, and financial-crime review. The assistant does not execute these steps or contact parties.

Keep each action status PROPOSED until an actual authorized decision is documented. Capture owner, urgency reason, intended evidence of completion, and any dependency. Do not invent a due time when policy or facts do not supply one; state “time-sensitive human review” and explain why. A template cannot override applicable legal obligations or internal authority.

## 9. Draft the incident assessment

Lead with the known exposure and immediate uncertainty. Use amounts with qualifiers: known requested, confirmed executed, confirmed returned, known unreturned, and unresolved. Distinguish a suspected mechanism from a proven perpetrator identity. Do not call a customer negligent, assign liability, or recommend reimbursement as an automatic consequence of a score.

Provide a chronology, verification review, financial reconciliation, conflicting evidence, and proposed next steps. Include the source and method for every amount. Mark the current as-of time because payment status and recoveries can change. Preserve the history when updates occur.

## 10. Validate and hand off

Run the reconciliation, null handling, status, duplicate recovery, benign case, and unknown-execution tests. Trace every material statement to its source. Check that dashboard filters cannot hide the unresolved case while still labeling the exposure figure complete. Deliver a bounded package to the human reviewer and record no action as executed without actual confirmation.
