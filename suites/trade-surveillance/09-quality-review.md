# Trade surveillance: quality review

## Reconstruction checks

| Check | Expected example result | Failure implication |
| --- | --- | --- |
| Raw messages | 12 = 11 processed + 1 exact duplicate | Duplicate event affects flow |
| Accepted orders | Five, O1–O5 | Requests or copies counted as new orders |
| Lifecycle identity | Each new quantity equals filled + cancelled + remaining | Cancel after partial fill overcounted |
| O1 | 1,000 = 200 + 800 + 0; cancellation ratio 0.80 | Full original quantity mistaken for cancelled remainder |
| Unique executions | Three: X-A1, X-A2, X-C1 | Same-owner trade counted twice as market volume |
| Account-side filled quantities | FICT-A 300, FICT-B 0, FICT-C 200 | Unit or leg confusion |
| Unique traded quantities | FICT-A 300, FICT-B 0, FICT-C 100 | Incorrect economic counting |
| TS-01 A | 300 ms gap; MATCH | Timestamp or operator error |
| TS-02 A | One simultaneous buy price level; NO_MATCH | Sequential or opposite-side levels counted |
| TS-01 B | No opposite execution; NO_MATCH | Cancellation alone misclassified |
| TS-03 C | One 100-share same-owner execution; MATCH as a lead | Legal conclusion substituted for evidence |

## Denominator checks

A's cancellation quantity ratio across its orders is 800/1,100 = 72.7272...%, displayed 72.7%. Its order cancellation incidence is 1/2 = 50.0%. O1's own ratio is 80.0%. These measures must not share one undifferentiated “cancellation rate” label.

A's unique execution participation is 300/1,000 = 30.0% for the aligned instrument/window market volume. C's same-owner unique execution is 100 shares, not its 200 account-side shares. Displayed depth share for A at the benchmark instant is 1,000/(1,000+2,000) = 33.3%; relative-to-external size is a different 50.0% measure. Changing the denominator must change the label and method.

## Boundary and adversarial tests

Move O1 cancellation to .700 while O2 remains .200: the 500 ms condition still matches. Move it to .701: 501 ms fails. Remove O2's fill while preserving complete coverage: TS-01 becomes NO_MATCH. Remove the opposite-side feed instead: TS-01 becomes NOT_ASSESSABLE. Reduce O1's cancelled quantity to 799 while increasing filled quantity to 201 so conservation holds: 79.9% fails the ratio condition.

Duplicate M02 under the same source message identity: effective filled quantity remains 200. Change duplicate content without changing identity: create a conflict defect instead of selecting a preferred version. Remove the ownership bridge for C: TS-03 becomes NOT_ASSESSABLE, not automatically false or true. Change C's execution IDs so no matching reference exists: do not infer one trade merely because time, price, and quantity coincide.

Round timestamps to seconds: do not preserve the 300 ms claim. Add clock uncertainty large enough to reverse fill/cancel order: timing-dependent assessment becomes unassessable. Add three sequential buy prices that never overlap: TS-02 remains NO_MATCH for simultaneous layering. Add three simultaneous live levels with full coverage: it becomes a descriptive MATCH, still not a legal conclusion.

## Interpretation review

Challenge any use of intent, manipulation, artificial price, profit, spoofing, layering, or wash trading. Identify the exact proposition and evidence supporting it. A screen's name cannot supply a missing legal element. A price movement around an order is not proof of causation. A sale above a prior midpoint is not net profit. A same-owner match may require controls review without proving intentional wash trading.

Evaluate the ordinary explanation against actual timing and logs. B's price-response rationale is supported context; it does not show that every cancellation by B is legitimate. A's partial fill is relevant counterevidence but not automatic exoneration. Preserve both sides of the analysis.

## Output and signoff

Check exact table headers, units, precision, raw versus displayed values, and reference IDs across artifacts. Ensure dashboard filtering cannot change a full-population denominator without disclosure. Unknown values must be visible as unknown. Do not aggregate instrument quantity into an economic-exposure figure without a conversion basis.

Record actual reviewer, timestamp, checks performed, expected and observed results, corrections, and residual limitations. Label independent review only when it occurred. The example can be READY FOR HUMAN REVIEW with two matched leads and no legal determination. Passing this small designed fixture establishes arithmetic and contract behavior only; it does not validate production surveillance effectiveness.
