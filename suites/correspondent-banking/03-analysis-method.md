# Correspondent Banking — analysis method

## 1. Establish role and applicable criteria

Map correspondent, respondent, branch, service and payment roles before assessing a gap. State the question separately for each respondent legal entity. Identify which domestic rules and contractual criteria actually govern the account or activity. A global group questionnaire cannot erase differences between branches or products. Where applicability remains unresolved, describe the facts and the legal question rather than declare compliance or violation.

Create a criterion record containing source, provision or contract section, relevant version, jurisdiction, institutional role, effective period and test logic. Label original analytic thresholds as illustrative. The example tests whether originator name, originator identifier, beneficiary name and beneficiary identifier are present. It makes no assertion that these are sufficient for every applicable payment transparency obligation.

## 2. Review respondent evidence

Match license, ownership, supervision and operating presence to the respondent's exact identity. Separate factual gaps from adverse facts. When assessing a regulated-affiliate claim, determine what evidence supports affiliation and what supports supervision within the relevant definition. Do not accept a logo as a substitute for either. If the legal interpretation is uncertain, refer the identified question to an authorized legal or compliance reviewer.

Assess the respondent's business, products, customer categories, geographies, anticipated activity and control evidence against the service actually provided. Record source limitations: a policy can establish intended design; a scoped test can support only the tested period and population. A self-completed questionnaire plus a management statement is not independent operating evidence merely because there are two documents.

## 3. Map direct and nested access

Create a relationship map from contractual declarations and observed message fields. Identify the downstream institution, the respondent providing access, the service involved and whether the arrangement was declared or authorized at the relevant date. A newly observed bank may be an ordinary beneficiary rather than an underlying user; test its message role and the agreement before labeling it nested.

Compare observed activity with the declared service perimeter. Undeclared-at-time access is an exception requiring clarification, not proof of money laundering. Record plausible alternatives: a reporting omission, a recently added approved service, a bank acting as commercial beneficiary, a message-role mapping error or an actual unauthorized nested arrangement. Seek the specific agreement or role evidence that distinguishes them.

Payable-through arrangements require their own access and responsibility assessment. Do not merge them with all nested flows. Document who can initiate activity, what information the respondent holds, and which responsibilities the applicable framework assigns. This public-method suite cannot infer private contractual rights that are not supplied.

## 4. Reconcile the payment population

Freeze raw payment IDs, amounts, currencies and initial fields. Keep message versions linked to one economic payment. Reconcile raw rows to unique payments, ingestion duplicates, out-of-scope records and unresolved lifecycle cases. A gap in supplied ledger coverage prevents a complete-period exposure claim even if every visible row parses correctly.

For each unique payment, apply the same declared field criterion to initial and cutoff versions. Record the names of missing fields rather than a single opaque fail flag. Count a record missing several fields once in the payment-level gap rate, but preserve field-level details. Blank, unreadable, semantically unusable and not applicable are distinct states. A string of placeholder characters is not necessarily usable identity information.

Repairs require a sourced version, timestamp and linkage to the payment. A response that promises to supply information does not complete the field. A repair arriving after cutoff cannot be inserted into the prior snapshot; issue a later snapshot and explain the change. Initial defect rates remain initial even when all cases are later repaired.

## 5. Calculate transparent measures

Initial missing-payment count = distinct payment IDs with at least one required field absent on receipt. Cutoff missing-payment count = distinct IDs with at least one required field still absent at the cutoff. Each count divided by all eligible payments gives the corresponding count rate. State the denominator and period each time.

Value associated with missing information = sum of native-currency amounts for the missing-payment set. Divide by total eligible value in the same currency for the corresponding value rate. This is a measure of review exposure, not illicit value or a loss estimate. Do not sum currencies or use a count rate as a value rate. If amounts are unknown, show known subtotal and unresolved count.

Nested payment count and value use only records whose actual role supports nested access. Keep disclosed and undeclared-at-time amounts separate. Where a nested classification is unresolved, use the exact UNRESOLVED state in PaymentReview and report its count and native-currency value separately. It remains in the full-population denominator but outside the confirmed nested numerator. NOT_INDICATED requires evidence supporting a non-nested payment role; absence of a role annotation cannot supply that conclusion. Field completeness and nesting status are independent: a COMPLETE four-field record may have an UNRESOLVED access role. A high nested share indicates activity composition; it is not inherently a defect.

The fixture totals USD 500,000.00 across ten unique payments. Three initial missing-field payments total USD 130,000.00: 30.0% by count and 26.0% by value. A documented repair reduces current gaps to two payments and USD 80,000.00: 20.0% and 16.0%. Four nested payments total USD 175,000.00, comprising USD 75,000.00 disclosed and USD 100,000.00 undeclared at the payment dates.

## 6. Connect metrics to relationship findings

Describe why a particular gap matters for the stated service and decision. Two missing fields at one respondent may warrant targeted follow-up, but the packet does not prove deliberate concealment. A repaired item may reveal a repeat process issue if a broader population supports repetition; one example alone does not establish a pattern. Keep questionnaire contradictions, observed message defects and missing public evidence as different finding types.

Evaluate whether the expected control would detect, clarify or prevent the specific issue and whether operation is evidenced. Do not call a mitigation effective merely because a policy exists. Conversely, do not call a control ineffective merely because its testing file was not supplied. State design support, operating support and coverage gap separately.

## 7. Prepare a proportionate human decision

For each respondent propose a question, evidence request, owner role and review trigger. Consider clarifying the access model, resolving missing information, verifying a legal classification, or recording supported ordinary activity. Any restrictions, escalation, filing or termination require the applicable human process; the suite performs none of them.

Avoid blanket de-risking by applying the same evidence gates to each relationship. A respondent serving remittance customers is not automatically deficient. A digital operating model is not itself proof of prohibited shell banking. A physical office is not proof of adequate controls. The decision should follow the exact facts, applicable rules and supported mitigants rather than a sector label.
