# Transaction Monitoring Scenario Design: decision rules and human gates

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

## RULE-SD-01-v1 complete truth table and design decision

The specification is a conjunction of eligibility, coverage, minimum credits, ratio and strict subsequent-debit conditions. A credit anchor creates a candidate window; it does not itself establish a match. All eligible same-account events in the closed interval contribute to the sums, including a contemporaneous debit, while the timing predicate separately requires at least one debit later than the anchor. This deliberate choice is fully specified so a reviewer can accept it, reject it or request a changed version. It must not be left to an assistant or implementation vendor to guess.

| Window | Credit predicate | Ratio predicate | Subsequent predicate | Data gate | Raw result | Exact deciding reason |
| --- | --- | --- | --- | --- | --- | --- |
| WJ1 | 5000 passes | .90 passes | 2 hours passes | Complete | MATCH | All necessary conditions true |
| WJ2 | 2000 fails | 2.25 passes | 1 hour passes | Complete | NO_MATCH | Minimum credit condition false |
| WK1 | 5000 passes | .90 passes | Exactly 24 hours passes | Complete | MATCH | Closed endpoint and inclusive time accepted |
| WL1 | 5000 passes | .899998 fails | 2 hours passes | Complete | NO_MATCH | Ratio false before rounding |
| WN1 | 5000 passes | .90 passes | No strictly later debit | Complete | NO_MATCH | Contemporaneous debit cannot satisfy timing |
| WO1 | 5000 known | Unknown debit prevents ratio | 1 hour observable | Amount incomplete | NOT_ASSESSABLE | Completeness gate takes precedence |

M is intentionally absent from WindowResults because confirmed-own credits do not create external-flow anchors. M remains present in AccountCoverage with two events, USD 6000 credits and USD 5700 debits. If an implementation drops M from every output, it has not merely chosen a shorter table: it has lost the evidence that the account was considered and excluded for a stated reason. Similarly, O must retain its blocked window rather than disappear because an aggregation ignored a null debit.

**Raw match versus proposed delivery.** WJ1 and WK1 each produce a proposed review group. Neither has an existing identical event-set match in the specimen. WJ2 is a nonmatch even though it overlaps WJ1, and its nonmatch is retained separately. No feature of this design authorizes suppressing later K activity because K already matched. If a reviewer wants a cooldown, consolidated customer case or cross-scenario deduplication policy, its identity keys, new-event behavior, expiry, override and testing requirements must be separately specified and approved.

**Identical rerun.** A repeated calculation on unchanged source and criteria must reproduce all six raw outcomes. A presentation system may avoid duplicate display only with an explicit run and event-set link, preserving both execution records. If a new relevant event arrives, the event set has changed and cannot use exact-set grouping to conceal the delta. If a source value changes under the same event identifier, it requires version resolution and recalculation; identical identifiers alone do not establish identical data.

**Design acceptance scope.** The tests establish precise behavior for the printed source, not whether USD 5000, .90 or 24 hours are appropriate for a real risk profile. No adjudicated population, false-negative search, representative historical sample or operational cost study is supplied. The reviewer can determine that the specification is internally reproducible while leaving deployment suitability unresolved. Record these as different decisions. A coherent specification is a prerequisite for a useful review, not evidence of detection effectiveness.

**Required change record.** For any alternative parameter or temporal convention, record old and new specification versions, the exact predicate changed, reason, source population held fixed, raw windows gained and lost, unchanged blocked cases and test results. A change to allow same-time debits, lower the credit floor or round ratios before comparison is substantive even if only one symbol changes in code. The alternate controls in file 10 show the expected consequences and give the reviewer concrete examples to assess.
