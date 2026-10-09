# Measured attachment budgets

Measurements cover the instructional files, including embedded code. Estimates use
Unicode characters divided by four, rounded up; they are not model-tokenizer counts.
All figures exclude your input data, prior messages, the case checkpoint and generated
output. Reserve space for each. File 11 in every suite supplies a sensitivity range,
resource-estimate limitations and the exact file hashes.

| Suite | Words in 01–10 | Full ten-file token estimate | Analysis stage estimate | Render stage: report / workbook / dashboard |
| --- | --- | --- | --- | --- |
| [control-testing](../suites/control-testing/) | 13,927 | 29,388 | 9,685 | 9,720 / 10,679 / 12,408 |
| [data-quality](../suites/data-quality/) | 13,675 | 29,020 | 9,494 | 9,694 / 10,643 / 12,452 |
| [digital-asset-review](../suites/digital-asset-review/) | 14,214 | 30,708 | 9,999 | 9,981 / 10,977 / 12,851 |
| [entity-due-diligence](../suites/entity-due-diligence/) | 13,791 | 30,457 | 9,654 | 9,981 / 10,966 / 12,792 |
| [fraud-review](../suites/fraud-review/) | 14,784 | 32,290 | 10,058 | 10,243 / 11,206 / 13,048 |
| [investigations](../suites/investigations/) | 14,039 | 30,373 | 9,658 | 9,709 / 10,667 / 12,499 |
| [monitoring-tuning](../suites/monitoring-tuning/) | 13,541 | 29,121 | 9,621 | 9,730 / 10,671 / 12,456 |
| [new-product-risk](../suites/new-product-risk/) | 13,736 | 29,748 | 9,753 | 9,746 / 10,683 / 12,479 |
| [osint-research](../suites/osint-research/) | 13,636 | 29,089 | 9,311 | 9,613 / 10,598 / 12,393 |
| [ownership-analysis](../suites/ownership-analysis/) | 14,668 | 31,389 | 10,419 | 10,022 / 11,003 / 12,851 |
| [regulatory-change](../suites/regulatory-change/) | 13,975 | 30,466 | 9,967 | 9,915 / 10,867 / 12,693 |
| [sanctions-review](../suites/sanctions-review/) | 14,060 | 30,499 | 9,858 | 10,011 / 10,993 / 12,817 |
| [third-party-risk](../suites/third-party-risk/) | 14,001 | 30,545 | 10,048 | 9,905 / 10,843 / 12,643 |
| [trade-surveillance](../suites/trade-surveillance/) | 15,115 | 32,207 | 10,607 | 9,999 / 10,972 / 12,858 |
| [transaction-monitoring](../suites/transaction-monitoring/) | 13,920 | 29,842 | 9,584 | 9,479 / 10,451 / 12,256 |
| [typology-red-flags](../suites/typology-red-flags/) | 14,059 | 30,207 | 9,659 | 9,642 / 10,612 / 12,426 |

Across 16 suites, the ten-file sets contain 225,141 whitespace-counted
words and a summed estimate of 485,349 tokens. This is library size, not a
recommended combined attachment. Shared rules and renderers are repeated deliberately
so each suite works on its own.

Analysis stage includes 01, 02, 03, 04, 05 and 09. Each render stage includes 01, 05,
09 and one renderer, **plus your saved case record**, which is not measured here.
Reattach the method and decision rules if analysis changes. The worked example is
an additional instructional input when testing the suite. See [Start here](START-HERE.md)
for the staged process and preservation requirements.

Build-token budgets in suite READMEs use 4–10× final context as an illustrative
reproduction planning assumption. They do not report actual generation consumption,
billed tokens or monetary cost. No fixed multiplier can establish those values.
