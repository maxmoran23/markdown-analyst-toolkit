# Measured attachment budgets

Measurements cover the instructional files, including embedded code. Estimates use
Unicode characters divided by four, rounded up; they are not model-tokenizer counts.
All figures exclude your input data, prior messages, the case checkpoint and generated
output. Reserve space for each. File 11 in every suite supplies a sensitivity range,
resource-estimate limitations and the exact file hashes.

Authored prose counts cover files 01–05, 09 and 10, including Markdown tables but
excluding fenced code and the compiled field dictionary. Full-set figures include
all content. [Process depth](PROCESS-DEPTH.md) reports the focused before/after
comparison and individual authored-file sizes.

| Suite | Authored prose words | All words in 01–10 | Full ten-file token estimate | Analysis stage estimate | Render stage: report / workbook / dashboard |
| --- | --- | --- | --- | --- | --- |
| [adverse-media](../suites/adverse-media/) | 6,971 | 19,055 | 45,722 | 10,316 | 15,677 / 17,098 / 17,597 |
| [alert-qa](../suites/alert-qa/) | 20,607 | 43,184 | 93,475 | 29,699 | 31,530 / 33,057 / 36,101 |
| [control-testing](../suites/control-testing/) | 6,769 | 17,831 | 42,062 | 9,685 | 14,149 / 15,559 / 15,774 |
| [correspondent-banking](../suites/correspondent-banking/) | 7,758 | 19,897 | 47,377 | 11,219 | 16,032 / 17,448 / 17,985 |
| [customer-risk-review](../suites/customer-risk-review/) | 7,538 | 20,050 | 47,366 | 10,699 | 15,980 / 17,402 / 18,378 |
| [data-quality](../suites/data-quality/) | 6,504 | 17,579 | 41,694 | 9,494 | 14,124 / 15,523 / 15,818 |
| [digital-asset-review](../suites/digital-asset-review/) | 6,866 | 18,118 | 43,382 | 9,999 | 14,410 / 15,856 / 16,216 |
| [entity-due-diligence](../suites/entity-due-diligence/) | 6,477 | 17,695 | 43,132 | 9,654 | 14,411 / 15,846 / 16,157 |
| [fraud-review](../suites/fraud-review/) | 6,739 | 18,688 | 44,964 | 10,058 | 14,672 / 16,086 / 16,414 |
| [investigations](../suites/investigations/) | 20,450 | 42,912 | 92,742 | 29,219 | 32,084 / 33,667 / 36,720 |
| [issue-remediation](../suites/issue-remediation/) | 8,736 | 20,732 | 47,546 | 11,305 | 15,391 / 16,797 / 17,162 |
| [jurisdiction-risk](../suites/jurisdiction-risk/) | 7,335 | 18,887 | 45,408 | 10,587 | 15,464 / 16,884 / 17,283 |
| [lookback-review](../suites/lookback-review/) | 23,400 | 55,067 | 122,238 | 27,561 | 39,317 / 41,037 / 46,772 |
| [monitoring-tuning](../suites/monitoring-tuning/) | 22,947 | 50,310 | 109,185 | 26,779 | 35,832 / 37,455 / 43,914 |
| [monitoring-validation](../suites/monitoring-validation/) | 20,155 | 43,631 | 94,794 | 27,701 | 31,918 / 33,515 / 36,986 |
| [network-flow-review](../suites/network-flow-review/) | 20,232 | 41,966 | 89,843 | 29,002 | 31,310 / 32,894 / 35,863 |
| [new-product-risk](../suites/new-product-risk/) | 6,536 | 17,640 | 42,422 | 9,753 | 14,175 / 15,563 / 15,845 |
| [osint-research](../suites/osint-research/) | 6,401 | 17,540 | 41,764 | 9,311 | 14,042 / 15,477 / 15,758 |
| [ownership-analysis](../suites/ownership-analysis/) | 7,234 | 18,572 | 44,064 | 10,419 | 14,452 / 15,882 / 16,216 |
| [regulatory-change](../suites/regulatory-change/) | 6,677 | 17,879 | 43,140 | 9,967 | 14,344 / 15,747 / 16,059 |
| [sampling-assurance](../suites/sampling-assurance/) | 7,847 | 19,898 | 45,881 | 10,961 | 15,150 / 16,568 / 16,871 |
| [sanctions-review](../suites/sanctions-review/) | 6,589 | 17,964 | 43,173 | 9,858 | 14,440 / 15,872 / 16,183 |
| [scenario-design](../suites/scenario-design/) | 18,478 | 42,724 | 91,852 | 31,467 | 34,985 / 36,591 / 39,196 |
| [source-wealth-funds](../suites/source-wealth-funds/) | 8,032 | 20,297 | 47,732 | 11,265 | 15,998 / 17,423 / 18,016 |
| [third-party-risk](../suites/third-party-risk/) | 6,740 | 17,905 | 43,220 | 10,048 | 14,335 / 15,723 / 16,008 |
| [tm-data-lineage](../suites/tm-data-lineage/) | 20,044 | 48,094 | 102,699 | 33,637 | 38,937 / 40,595 / 43,956 |
| [trade-finance-review](../suites/trade-finance-review/) | 9,138 | 21,358 | 49,303 | 12,182 | 16,412 / 17,858 / 18,341 |
| [trade-surveillance](../suites/trade-surveillance/) | 7,292 | 19,019 | 44,882 | 10,607 | 14,428 / 15,851 / 16,224 |
| [transaction-monitoring](../suites/transaction-monitoring/) | 20,639 | 50,262 | 108,010 | 36,677 | 42,497 / 44,246 / 47,587 |
| [typology-red-flags](../suites/typology-red-flags/) | 6,561 | 17,963 | 42,881 | 9,659 | 14,071 / 15,491 / 15,792 |

Across 30 suites, the ten-file sets contain 812,717 whitespace-counted
words and a summed estimate of 1,841,953 tokens. This is library size, not a
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
