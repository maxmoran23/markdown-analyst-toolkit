# Transaction Monitoring Review: decision rules and human gates

## Mandatory decision hierarchy

Evaluate scope and evidence availability first, identity and source consistency second, record eligibility third, account/window completeness fourth, numeric predicates fifth, contextual interpretation sixth and authorized human disposition last. This order prevents an attractive numerical pattern from masking an invalid denominator. It also prevents a plausible explanation from silently changing the raw inputs or threshold. Each layer has its own retained state and its own evidence requirement; a later-layer conclusion cannot retroactively satisfy an earlier-layer prerequisite.

| Condition established by evidence | Required analytical branch | Retained record | Prohibited inference |
| --- | --- | --- | --- |
| Relevant amount, identity, direction or time cannot be resolved | NOT_ASSESSABLE for the affected proposition | Original row, known subtotal, missing field and repair dependency | A clean negative or zero activity |
| Exact extraction copy of the same economic identity and payload | DUPLICATE at raw-row layer | Both raw IDs and one canonical target | A second economic transaction |
| Same identity/version with conflicting economic payload | CONFLICT until authoritative resolution | All competing values and their source locators | Latest, largest or average is authoritative |
| Confirmed own transfer under the particular external-flow rule | Limited scenario exclusion | Gross amount, ownership evidence and affected rule | Relationship-wide clearance |
| Complete input and every required numeric predicate true | MATCH at raw-rule layer | Predicate values, window membership and version | Suspicion, illegality or filing authorization |
| Complete input and at least one required predicate false | NO_MATCH for the specified rule | Failed predicate and complete source basis | Absence of other risks or universal clearance |
| Match and transaction-specific ordinary explanation supported | EXPLANATION_SUPPORTED as proposed review state | Original match, document linkage and explanation limits | Deletion of the trigger or automatic closure |
| Match and material purpose evidence absent | OPEN_QUESTION or ESCALATE_FOR_REVIEW proposal | Concern, counterexplanation and discriminating request | Proof of wrongdoing from missingness |
| Criterion or specification approval absent | Exploratory or design-review-only use | Exact authored parameter and unrecorded approval | Operational deployment or policy adoption |
| Corrected source changes a prior result | Versioned rerun and impact comparison | Before/after values, affected keys and correction evidence | Quiet overwrite of the old case |

## Branch cards for nuanced cases

**Unknown ownership.** Do not silently classify unknown ownership as confirmed external or confirmed own. Preserve the source leg and identify the two competing eligibility outcomes. If inclusion or exclusion can change a match, record the affected result as not assessable under the ownership-dependent rule and request the dated ownership bridge. A sensitivity can show both numerical outcomes, but neither becomes the approved base result. If an institution supplies a different explicit unknown-ownership policy, record its version and apply it only within its authorized scope; do not pretend it was part of this specimen.

**Relevant but non-decisive missingness.** A missing narrative may not change a volume ratio, but it can prevent contextual explanation. Report the exact arithmetic as known while leaving purpose unresolved. Conversely, an unknown debit amount changes the numerator and prevents a complete volume calculation. A missing field should block the claims it affects, not every possible observation and not none of them. Explain the dependency in the finding so the reviewer knows what repair will actually improve.

**Boundary incompleteness.** If the extract ends before an anchored interval ends, its observed sums are diagnostic only. Additional credits could reduce the ratio, additional debits could increase it, and either could change the interpretation. Do not assume the unseen interval is inactive. A known match from the visible slice does not necessarily establish a full-window match when the denominator can still grow. Request complete look-forward coverage, or explicitly change the method to a bounded observed slice and rename its result.

**Daylight-saving ambiguity.** Two identical local clock times can represent different instants during a fall-back transition. Preserve the supplied offset or zone rules and compare normalized instants. Without disambiguation, return an uncertain timing branch if the difference matters. During a spring-forward transition, a nonexistent local time is not repaired by subtracting an hour on intuition. Obtain source metadata or record the defect. The rule duration is elapsed hours, not the number of date labels crossed.

**Same-time events.** If a debit and credit share an instant, an ID sort is not economic sequence. The scenario-design rule allows both to contribute to the closed interval totals but requires a strictly later debit for timing. The transaction-monitoring daily screen also requires a strictly subsequent debit. State this explicitly when reviewing a negative. If actual sequencing metadata is supplied, a revised interpretation requires a documented sequencing convention and a repeated acceptance test; do not smuggle it into the original specification.

**Reversal, refund and return.** A reversal may negate an earlier posting under a source-specific convention; a refund may be a new payment with its own purpose; a returned payment may have partial fees or different timing. Equal and opposite amounts are insufficient to decide which mechanism occurred. Require the original link, account, currency, amount and relevant status semantics. Preserve gross posting history even when the declared scenario excludes a validated pair. Partial reversals require a separate residual calculation and cannot be treated as the full-pair specimen.

**Negative or signed source amount.** These contracts use nonnegative magnitude and separate direction. A negative magnitude violates that contract. Do not take its absolute value or flip direction automatically because either repair may hide a double-sign mapping defect. If an approved source uses signed values, establish a new explicit mapping and test positive, negative, zero and incompatible status combinations before calculating. The source convention controls interpretation, not the assistant's preference for a neat table.

**Late data and revised history.** Preserve both event time and information availability. An earlier run can have a defensible partial conclusion that changes after a late record. Record what was known at each cutoff and whether the initial incompleteness was known to the reviewer. Do not retrospectively claim the original system detected an event it had not yet ingested. A repaired run does not prove the rest of the feed is timely; it proves the declared late record was handled as specified.

**Multiple currencies.** Currency exclusion belongs to the specific scenario, not the raw population. Keep non-base-currency source rows and controls. If conversion becomes necessary, freeze the rate convention before comparing thresholds and preserve original amounts. An absent rate blocks the converted proposition but not original-currency reconciliation. A USD-only rule result cannot be presented as full multi-currency monitoring coverage. Avoid combining token quantities, fiat amounts and market valuations into one unexplained total.

**Overlapping windows and scenarios.** Preserve every raw match and its membership set. Grouping for presentation or proposed delivery is a separate decision. A transaction in three windows remains one economic leg. A customer with two matching accounts remains two account-window observations and one customer only if identity linkage is established. A cooldown or suppression policy that hides later activity requires an explicit approved design; the examples authorize no such operational policy.

**Plausible ordinary explanation.** Match the explanation to the actual payment, parties, dates and amount. A genuine commercial invoice can support one payment while leaving an unusual counterparty role or another payment unresolved. Distinguish reported explanation, documented support and independent corroboration. Preserve evidence that conflicts with the explanation. If the supporting record is removed in a sensitivity test, the numeric result stays fixed while the review state changes; this separation is a mandatory control.

**High confidence in a defect.** A source row can plainly contain unreadable text or conflicting values. HIGH confidence is appropriate for the existence of that defect when directly observed. It does not mean high confidence that the account is suspicious. Severity can be HIGH because coverage is materially impaired. Phrase the finding around the impaired proposition and repair need rather than attaching a risk accusation to the customer.

**Authorization missing.** Leave human decisions NOT_RECORDED and action states Proposed. Do not assign a real owner, due date or approval date without supplied evidence. A public method can recommend what information to bring to a reviewer; it cannot decide the applicable institutional workflow, legal deadline or filing obligation. If an actual controlling policy is supplied in an approved environment, cite its exact version and provision and distinguish its requirements from this authored illustrative method.

## Severity, confidence and claim-class rules

| Dimension | Permitted value | Required rationale |
| --- | --- | --- |
| Severity | HIGH | Material coverage failure or supported urgent analytical need; name the affected scope and consequence |
| Severity | MEDIUM | Unresolved design or contextual condition needing further evidence or human review |
| Severity | LOW | Bounded documented explanation or limited issue without the broader consequence implied by higher labels |
| Confidence | HIGH | The specific claim is directly evidenced or independently reproduced from complete relevant rows |
| Confidence | MODERATE | The calculation is sound but material contextual premises remain uncertain |
| Confidence | LOW | The proposition depends on indirect, weak or contradictory evidence |
| Confidence | NOT ASSESSABLE | Evidence cannot support evaluation of the proposition |
| Claim class | Observed | Directly supplied record or reproducible calculation within its explicit limitations |
| Claim class | Reported | Assertion attributed to a source without converting it into independently established fact |
| Claim class | Inferred | Interpretation with stated premises, alternatives and a condition that could change it |
| Claim class | Estimated | Approximation with method, assumptions and uncertainty, never inserted as a known posting |

A confidence label is not a numerical probability. A severity label is not regulatory materiality. Do not translate these labels into a filing rule or an automatic customer score. If a genuinely urgent fact is supplied, describe the fact and the designated human route within the approved process; the assistant still does not contact a third party or execute a restriction. The fictional examples contain no actual urgency, customer or external action.

## Required finding and review text patterns

For a calculation write: “Under [specification version], [record/window IDs] have [numerator and denominator with units], producing [unrounded value]; [predicate] is [true/false/unknown]. The observation covers [scope] and excludes [explicit records].” This wording makes the arithmetic inspectable without turning it into a behavioral accusation.

For a contextual inference write: “The observed pattern is consistent with [bounded hypothesis]. [Specific supplied evidence] supports [premise]. [Counterevidence or ordinary mechanism] limits that interpretation. [Named missing record] would distinguish these alternatives. Proposed next step: [human review or evidence request]. Human disposition: [actual recorded state].” Do not fill this structure with generic phrases that could apply to any customer; use the actual IDs, amounts and documents.

For a data defect write: “[Source rows] contain [exact defect]. This prevents [specific calculation or completeness claim] for [affected scope]. Known subtotal [value] remains available but is partial. Request [specific correction and controls], then rerun [dependency set].” For an explained match write: “The raw match remains. [Document and linkage] supports [specific transaction purpose] within [limit]. The proposed explanation awaits [recorded human decision state].” These patterns preserve the separation between source facts, interpretation and authority.

## Acceptance and release decision

A package may be READY_FOR_HUMAN_REVIEW when its known calculations reconcile, required tables are complete, exceptions are visible and the unresolved human gate is explicit. It must remain DRAFT when known arithmetic, row linkage, schema or contradictory output errors remain. The existence of unresolved source data can be compatible with a useful bounded review package, but never with a claim that the affected population was fully assessed. Record the precise residual condition in the report, workbook, dashboard and handoff rather than burying it in a generic disclaimer.

## TM-01 exact account decision and evidence-routing matrix

The daily screen is authored as an account/currency measure over the fixed observed period. Credits and debits are aggregate eligible daily amounts, while timing uses the first eligible credit and its first strictly subsequent eligible debit. This is intentionally a coarse temporal co-occurrence screen. It does not establish that every debit followed every credit or that the identified credits funded the debits. An analyst must not silently substitute credit-anchored rolling mathematics, FIFO allocation, proportional allocation or balance tracing to make the interpretation stronger.

| Account | Completeness gate | Ownership gate | Amount and ratio branch | Timing branch | Raw result | Contextual proposal |
| --- | --- | --- | --- | --- | --- | --- |
| A | Readable daily rows | External as supplied | 10000 >= 5000 and .95 >= .90 | First subsequent debit at 2 hours | MATCH | Request T03 purpose and P03 role; further human review |
| B | Readable daily rows | External as supplied | 5000 >= 5000 and .96 >= .90 | First subsequent debit at 3 hours | MATCH | Preserve invoice-supported explanation for T05 only |
| C | Readable daily rows | Every supplied leg confirmed own | Eligible credits and debits zero; ratio null | No eligible ordered pair | EXCLUDED | Retain ownership evidence and limited scenario exclusion |
| D | T09 amount unreadable | Known T08 externally eligible | Known debit 1000 is partial; complete amount unavailable | No complete eligible sequence conclusion | NOT_ASSESSABLE | Correct T09 and rerun D with source controls |

**A evidence request.** The discriminating record is a contemporaneous invoice or contract for T03, linked by payment reference, amount and counterparty role. An undated generic statement that the account pays suppliers is already represented by the profile and does not resolve the USD 9500 event. If the question changes from pattern review to tracing, request opening balances and complete interleaved activity first. Without them, do not describe the two-hour sequence as proven movement of the same funds.

**B explanation acceptance.** Verify INV-B-01 names P05 and USD 4800 and that the payment reference independently matches T05. The supplied case already includes those fictional facts, so EXPLANATION_SUPPORTED is a justified proposed review outcome. No fact supplied establishes a genuine real-world document or a complete customer review. Preserve the original match and note that a human still has to decide whether the documented explanation is sufficient for the authorized scope.

**C exclusion acceptance.** Confirm that ownership evidence is effective during the observed period and covers both C-OWN-1 and C-OWN-2. If either link is unavailable, withdraw the confirmed classification for that leg and recalculate sensitivity. Do not remove C from the source population or its USD 6000 gross movement. The exclusion concerns an external-flow hypothesis; internal-transfer velocity or other scenarios could have different coverage rules.

**D repair acceptance.** A replacement amount must identify T09, explain the extraction correction and reconcile to source controls. Preserve the old unreadable row and a correction event rather than editing history without a record. Recalculate D's canonical count, debit subtotal, ratio branch, raw outcome, review recommendation and affected portfolio known totals. If T09 is verified at zero, the count and completeness still change even though the known gross amount does not. If the source correction also changes direction or date, repeat the corresponding eligibility and timing checks.

## Diagnostic-window decision restriction

WindowDiagnostics is included to teach and retain rolling-window membership; it does not change TM-01's daily result. All three diagnostic intervals end after the extract boundary. Their ratios .95, 2.375 and .96 are known-slice ratios only. The second A interval has USD 4000 visible credits and USD 9500 debits, a 237.5% ratio, but this is neither an error nor a basis for stronger concern without complete coverage and balances. Use the diagnostic to request the missing interval and demonstrate overlap. Do not issue an additional raw MATCH from this incomplete register.

The base package therefore supports a precise limited conclusion: two daily raw matches, one supplied transaction-level ordinary explanation, one unexplained purpose requiring human review, one confirmed-own scenario exclusion and one amount-blocked account. These are review dimensions, not five mutually exclusive source transactions. Keep all four account rows visible when presenting coverage.
