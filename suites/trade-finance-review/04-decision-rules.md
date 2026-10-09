# Trade Finance Review — decision rules

## Interpret each test independently

| Test | Supported result | Unresolved result |
| --- | --- | --- |
| Invoice arithmetic | Quantity and price reconcile to amount within stated adjustments | Request corrected arithmetic or missing components |
| Currency normalization | Quote direction, date and purpose are supported | Keep native amounts; no mixed-currency ratio |
| Price comparability | Goods and commercial basis match sufficiently | NOT_ASSESSABLE, not a zero variance |
| Shipment quantity | Distinct consignments reconcile at cutoff | Preserve gap and timing uncertainty |
| Funding allocation | Distinct outstanding advances link to the trade | Do not claim confirmed overlapping finance |
| Legitimate alternative | Specific explanation supported by relevant evidence | Retain hypothesis without accepting or rejecting it as fact |
| Operational disposition | Applicable rule and authorized human decision evidenced | Proposed review only |

These tests do not form a mechanical guilt score. A trade can have correct arithmetic and an unexplained commercial price. It can have a shipment gap explained by an agreed schedule and a separate funding concern. Record each test so a later update changes only the conclusions it actually affects.

## Illustrative thresholds

The price review trigger is absolute comparable-price deviation greater than 50.0%. Exactly 50.0% does not trigger this particular illustration. The financing review trigger is outstanding attributed principal greater than 100.0% of comparable invoice value. Exactly 100.0% does not trigger it. Both thresholds are invented for the exercise, not regulatory limits, market norms or recommendations for production calibration.

A value below a trigger is not a clean bill of health. Non-price evidence, missing goods, inconsistent parties or an applicable legal issue can merit review independently. A value above a trigger does not establish misconduct. Always disclose the source and purpose of the criterion and its sensitivity to alternate assumptions. Do not quietly change the trigger after seeing the case result.

Where the benchmark or denominator is missing, use NOT_ASSESSABLE and preserve the raw values. Never replace a missing benchmark with zero, the invoice price itself or an unsupported industry average. Do not call an unassessable case 'within threshold' merely because no numerical exception was produced.

## Shipment and financing interpretation

PARTIAL_SUPPORTED requires an actual documented schedule or other evidence that explains the remaining obligation at cutoff. A party's unsupported claim that goods will arrive later is Reported, not independently established completion. The supported interpretation should state what is still outstanding. If the scheduled date passes without new evidence, reassess the question under a later cutoff rather than retroactively change the original snapshot.

OVERLAP_REVIEW means the supplied funded amounts and allocations warrant examination of multiple financing or a denominator mismatch. It does not establish deception or fraud. Multiple documents can represent one economic advance, a participation, refinancing, separate collateral, financing of another component or incorrect allocation. Test these explanations with dates and actual funded amounts, not just invoice-number similarity.

An invoice credit note reduces the obligation only when it is effective and linked to the trade. A repayment reduces outstanding principal only when realized and linked to the relevant advance. A recall request, promise to repay or undrawn facility amendment is not a realized principal reduction. Preserve lifecycle distinctions even if the formatted report would be shorter without them.

## Severity, confidence and alternatives

HIGH severity is appropriate for a consequential unresolved funding or documentation discrepancy in the stated decision. MEDIUM covers a material pricing question or a gap requiring clarification with no established illicit conduct. LOW covers supported ordinary or timing explanations within the supplied scope. The fixture uses these priorities illustratively; no universal loss or legal consequence is inferred.

HIGH confidence can apply to exact arithmetic and explicit document terms. It cannot transfer automatically to the explanation of an anomaly. MODERATE reflects partial support or a material interpretive limitation. LOW reflects an attributed assertion without corroboration. NOT ASSESSABLE means the necessary comparator, allocation or source is absent. State both the numerical confidence and the substantive uncertainty when they differ.

For T02 the multiplication and 200.0% comparable-price deviation are HIGH-confidence observations under fictional assumptions. Whether the difference reflects customization, an error or illicit value transfer is unresolved. For T05 the two funded amounts and 125.0% ratio are supported within the fixture; intent and legal characterization are not. A precise ratio cannot supply missing mental-state evidence.

## Actions and human disposition

A proposed clarification should identify the exact trade, missing fact, relevant source and effect of the possible answer. Seek product and cost-basis support for T02; seek allocation, participation, repayment and agreement evidence for T05. Preserve the supported currency and shipment explanations for T03 and T04. Do not send requests, reject documents, cancel facilities, restrict payments or make filings through this analytical suite.

A human reviewer may decide the available explanation is sufficient for a specific operational purpose. Record that decision and its scope without representing it as proof of all underlying facts. If legal applicability or contractual interpretation is decisive, identify the question for the authorized reviewer. No rule in this pack supersedes a governing instrument or grants authority to act.

## Mixed-line and allocation gate

Where one trade contains several goods, preserve separate line-level price and shipment decisions. Do not label the whole trade's shipment complete because one line is complete. If a material line remains unexplained, name that line and its native quantity in the trade rationale. If the shipment cannot be allocated to lines, use null line quantities with NOT_ASSESSABLE and request allocation evidence.

Finance-to-invoice ratios are assessed on the complete economic trade denominator unless the actual financing scope supports a narrower denominator. Do not repeat a full advance across two lines, and do not assume a convenient proportional allocation. A two-line trade with USD 2,000.00 total value and one USD 1,500.00 advance has a 75.0% trade ratio, regardless of the lines' incompatible units. That ratio does not resolve a line's separate shipment discrepancy.
