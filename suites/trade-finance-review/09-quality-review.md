# Trade Finance Review — quality review

## Record actual checks

The expected results in 10 are a reference, not proof that this session reproduced them. Record each check ID, expected result, actual result, method, relevant evidence and PASS, FAIL, NOT RUN or NOT APPLICABLE in the case record. Map that information into the exact QA fields in 07. Do not mark a check PASS merely because it is listed here. An unavailable capability means NOT RUN for its dependent check.

Separate four propositions: the method was followed, the arithmetic was reproduced, the delivered file was inspected, and the human decision was authorized. Success on one does not establish the others. No fictional case result supports a claim of operational validation, compliance certification, universal platform support or reliable future model performance.

## Population and join checks

- Q-01: Reconcile received source records into mutually exclusive processed, duplicate, excluded, unparsed, inaccessible and deferred states. A processed inventory saying a document is missing does not count as processing that missing document. Record the lack of an upstream control total.
- Q-02: Verify each subject and domain row has a stable identifier. Distinct versions remain distinguishable. Repeated references cannot create duplicate economic events or additional independent sources.
- Q-03: Match each finding and each semicolon-delimited domain evidence ID to Evidence, then locate the exact source statement. Method references never support fictional facts. Orphan joins and citations to unavailable passages block the affected statement.
- Q-04: Compare report, workbook and dashboard populations. Counts, nulls, current states, monetary totals and cutoff must agree. Reconcile filtered views back to the full population and show what is hidden.

## Domain falsification tests

- Q-TF01: Recalculate T03 in native EUR and USD. EUR 1,600.00 × 1.25 USD/EUR = USD 2,000.00. Comparing EUR 8.00 directly with USD 10.00 is invalid; its normalized price variance is zero.
- Q-TF02: Replace the benchmark's grade or delivery basis with a noncomparable one. Set price variance null and price state NOT_ASSESSABLE; do not retain a spurious percentage.
- Q-TF03: Duplicate T05's invoice PDF but preserve its economic invoice identifier. Invoice count and denominator do not increase; the duplicate is an ingestion record.
- Q-TF04: Supply a verified participation record showing F05B is a share of F05A rather than an additional advance. Reconcile unique funded principal before recalculating; do not sum both faces as independent cash advances.
- Q-TF05: Remove T04's split-shipment schedule. The numeric quantity gap remains 40 units but PARTIAL_SUPPORTED is no longer evidenced; use an unresolved shipment state.
- Q-TF06: Move the second T04 shipment date beyond the revised review cutoff without delivery evidence. The packet may support an overdue unresolved shipment question, but not a fabricated delivery or automatic fraud conclusion.
- Q-TF07: Supply a full T05 advance repayment before cutoff. Remove that outstanding principal only after confirming linkage and timing; retain historical funding events separately.
- Q-TF08: Run the separate MX01 mixed-unit fixture in 10. Require two distinct line_id values, two line shipment states and exactly one ShipmentFinance row. Verify USD 2,000.00 invoice total, USD 1,500.00 finance and 75.0% ratio. The 20-unit coupling gap must not be added to a kilogram quantity. An expanded join must not produce USD 3,000.00 funding.
- Q-TF09: Remove a line-specific shipment allocation in the mixed-unit fixture. That line's shipped quantity and gap become null with NOT_ASSESSABLE; trade funding remains USD 1,500.00. Remove a required line valuation instead: trade invoice_usd_total and ratio become null, with known subtotal and missing-line count preserved in review_rationale.

## Interpretation review

Read each conclusion as an adversarial reviewer. Identify the most plausible benign explanation and the precise fact that would weaken or reverse the conclusion. If a contrary source is omitted, restore it and reassess. If identity, currency, time window, economic event or legal scope differs, do not manufacture a contradiction. A higher-severity recommendation must explain consequence and timing rather than rest on emotionally loaded terms.

Verify that Observed applies to the source content actually seen. A party's denial is a Reported denial; its existence may be observed. A regulator announcement may establish that a proceeding was announced while leaving the alleged conduct unresolved. A spreadsheet computation is only as sound as its operands and inclusion rules. Confidence needs a source-specific explanation, not a mechanical upgrade because many rows exist.

Inspect all statements of absence. Replace universal negatives with bounded statements naming searched sources, period, language and access limits. Confirm any claimed completion has a denominator. Do not convert a missing response into an admission, an absent record into a favorable control result, or a zero numerical amount into evidence of no risk. Confirm the final report distinguishes recommended action, recorded human decision and action execution.

## Arithmetic and artifact review

Recalculate principal totals from the raw records independently of the formatted output. Use a second representation, such as an explicit manual sum against a table calculation. Keep full precision and show any rounding tolerance before comparison. Rebuild every affected metric after inserting the negative controls in a copy of the example. Restore the original fixture after testing and preserve actual differences.

Reopen each delivered file using its intended application when available. For a report, inspect heading order, line wraps, full evidence text and page breaks. For a workbook, verify headers, table range, numeric types, null handling, literal source strings, filters and visible currency or percentage units. For HTML, inspect both themes, filter behavior, hidden-row counts and absence of network dependencies. Test a long locator and a source string beginning with a formula marker as literal data. If the current chat cannot perform a check, preserve that limitation instead of claiming visual inspection.

## Release disposition

A material identity, source, arithmetic or scope error blocks the affected recommendation. It need not block clearly separated facts supported by unaffected evidence. Label partial output and identify the blocked statement, its consequence and the smallest resolving evidence. Avoid an undifferentiated 'all clear' based on the number of checks that passed.

The reviewer should record name or authorized role, review date, open issues, accepted limitations, decision and its scope. If no reviewer disposition is supplied, retain NOT REVIEWED in the case record and the draft banner. A proposed deadline is not a legal deadline. A planned information request is not a completed request. Preserve changed decisions with their evidence version so a later reviewer can understand reversals without reconstructing chat history.
