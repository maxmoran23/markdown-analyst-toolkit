# Measured attachment budgets

Measurements cover the instructional files, including embedded code. Estimates use
Unicode characters divided by four, rounded up; they are not model-tokenizer counts.
All figures exclude your input data, prior messages, the case checkpoint and generated
output. Reserve space for each. File 11 in every suite supplies a sensitivity range,
resource-estimate limitations and the exact file hashes.

| Suite | Words in 01–10 | Full ten-file token estimate | Analysis stage estimate | Render stage: report / workbook / dashboard |
| --- | --- | --- | --- | --- |
| [adverse-media](../suites/adverse-media/) | 16,771 | 37,680 | 10,316 | 13,410 / 14,684 / 14,237 |
| [control-testing](../suites/control-testing/) | 15,547 | 34,020 | 9,685 | 11,882 / 13,144 / 12,413 |
| [correspondent-banking](../suites/correspondent-banking/) | 17,613 | 39,334 | 11,219 | 13,765 / 15,033 / 14,625 |
| [customer-risk-review](../suites/customer-risk-review/) | 17,766 | 39,324 | 10,699 | 13,713 / 14,988 / 15,018 |
| [data-quality](../suites/data-quality/) | 15,295 | 33,652 | 9,494 | 11,857 / 13,108 / 12,457 |
| [digital-asset-review](../suites/digital-asset-review/) | 15,834 | 35,340 | 9,999 | 12,143 / 13,442 / 12,856 |
| [entity-due-diligence](../suites/entity-due-diligence/) | 15,411 | 35,089 | 9,654 | 12,144 / 13,431 / 12,797 |
| [fraud-review](../suites/fraud-review/) | 16,404 | 36,922 | 10,058 | 12,405 / 13,671 / 13,053 |
| [investigations](../suites/investigations/) | 15,659 | 35,005 | 9,658 | 11,871 / 13,132 / 12,504 |
| [issue-remediation](../suites/issue-remediation/) | 18,448 | 39,504 | 11,305 | 13,124 / 14,382 / 13,801 |
| [jurisdiction-risk](../suites/jurisdiction-risk/) | 16,603 | 37,366 | 10,587 | 13,197 / 14,469 / 13,922 |
| [monitoring-tuning](../suites/monitoring-tuning/) | 15,161 | 33,753 | 9,621 | 11,892 / 13,136 / 12,461 |
| [new-product-risk](../suites/new-product-risk/) | 15,356 | 34,380 | 9,753 | 11,908 / 13,148 / 12,484 |
| [osint-research](../suites/osint-research/) | 15,256 | 33,721 | 9,311 | 11,775 / 13,063 / 12,398 |
| [ownership-analysis](../suites/ownership-analysis/) | 16,288 | 36,021 | 10,419 | 12,185 / 13,467 / 12,856 |
| [regulatory-change](../suites/regulatory-change/) | 15,595 | 35,098 | 9,967 | 12,077 / 13,332 / 12,698 |
| [sampling-assurance](../suites/sampling-assurance/) | 17,614 | 37,839 | 10,961 | 12,883 / 14,153 / 13,511 |
| [sanctions-review](../suites/sanctions-review/) | 15,680 | 35,131 | 9,858 | 12,173 / 13,458 / 12,822 |
| [source-wealth-funds](../suites/source-wealth-funds/) | 18,013 | 39,690 | 11,265 | 13,731 / 15,009 / 14,656 |
| [third-party-risk](../suites/third-party-risk/) | 15,621 | 35,177 | 10,048 | 12,068 / 13,308 / 12,648 |
| [trade-finance-review](../suites/trade-finance-review/) | 19,074 | 41,261 | 12,182 | 14,145 / 15,443 / 14,981 |
| [trade-surveillance](../suites/trade-surveillance/) | 16,735 | 36,839 | 10,607 | 12,161 / 13,436 / 12,863 |
| [transaction-monitoring](../suites/transaction-monitoring/) | 15,540 | 34,474 | 9,584 | 11,641 / 12,916 / 12,261 |
| [typology-red-flags](../suites/typology-red-flags/) | 15,679 | 34,839 | 9,659 | 11,804 / 13,077 / 12,431 |

Across 24 suites, the ten-file sets contain 392,963 whitespace-counted
words and a summed estimate of 871,459 tokens. This is library size, not a
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
