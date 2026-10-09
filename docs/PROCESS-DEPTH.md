# Measured process depth

This record separates authored method content from generated field dictionaries and repeated renderer payloads. Length is a capacity measure; arithmetic, record preservation and independent review are separate checks. A longer attachment does not establish a better conclusion.

The comparison baseline is release 1.1.0 at commit `4a783f41b4dcf1fcff057dfbed4064fe4ebca92a`. Current figures cover release 1.2.0. Counts use whitespace-separated words and UTF-8 bytes.

| Process suite | Authored prose words before | Authored prose words now | Complete authored-file bytes before | Complete authored-file bytes now | Populated domain tables | Domain rows |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [transaction-monitoring](../suites/transaction-monitoring/) | 6,574 | 20,639 | 45,237 | 184,952 | 10 | 61 |
| [scenario-design](../suites/scenario-design/) | New suite | 18,478 | New suite | 157,415 | 8 | 55 |
| [tm-data-lineage](../suites/tm-data-lineage/) | New suite | 20,044 | New suite | 174,724 | 9 | 74 |
| [monitoring-tuning](../suites/monitoring-tuning/) | 6,367 | 22,947 | 43,599 | 174,523 | 8 | 163 |
| [monitoring-validation](../suites/monitoring-validation/) | New suite | 20,155 | New suite | 158,912 | 8 | 76 |
| [lookback-review](../suites/lookback-review/) | New suite | 23,400 | New suite | 199,868 | 10 | 144 |
| [investigations](../suites/investigations/) | 6,491 | 20,450 | 45,368 | 160,977 | 8 | 69 |
| [network-flow-review](../suites/network-flow-review/) | New suite | 20,232 | New suite | 160,735 | 8 | 65 |
| [alert-qa](../suites/alert-qa/) | New suite | 20,607 | New suite | 164,400 | 8 | 84 |

Across these 9 process suites: **186,952 authored prose/table words**, **1,536,506 bytes in the seven complete authored files**, **77 populated domain tables**, and **791 domain rows**.

## Measurement boundaries

- Authored prose means files 01–05, 09 and 10, including Markdown tables but excluding fenced code and the compiled FIELD_CONTRACTS block.
- Complete authored-file bytes include their fixture-check code and compiled dictionary. The corresponding word count deliberately excludes both, so embedded code cannot satisfy the prose-depth gate.
- Files 06–08 contain complete renderers and repeatedly embedded specimens. Their size is included in the full attachment budget, but not the authored-depth comparison.
- Read the per-file table before choosing a session stage. Neither twelve files nor a token estimate establishes platform context capacity.
- The exact fixture check is supplied inside each file 10. The maintainer test executes that delivered block and compares its derived records to the declared case. This verifies the fictional arithmetic under its stated assumptions, not operational effectiveness.
- [Verification](VERIFICATION.md) records checks actually completed; this generated inventory does not claim a test passed.

## Transaction Monitoring Review

| Authored file | Prose/table words | Complete UTF-8 bytes |
| --- | ---: | ---: |
| [01-session-guide.md](../suites/transaction-monitoring/01-session-guide.md) | 1,354 | 9,808 |
| [02-inputs-evidence.md](../suites/transaction-monitoring/02-inputs-evidence.md) | 2,160 | 15,835 |
| [03-analysis-method.md](../suites/transaction-monitoring/03-analysis-method.md) | 2,208 | 15,945 |
| [04-decision-rules.md](../suites/transaction-monitoring/04-decision-rules.md) | 2,695 | 18,285 |
| [05-output-contract.md](../suites/transaction-monitoring/05-output-contract.md) | 5,470 | 72,343 |
| [09-quality-review.md](../suites/transaction-monitoring/09-quality-review.md) | 2,120 | 14,736 |
| [10-worked-example.md](../suites/transaction-monitoring/10-worked-example.md) | 4,632 | 38,000 |

Domain registers: `RawTransactions`, `CanonicalLedger`, `Eligibility`, `AccountFlows`, `WindowDiagnostics`, `ScenarioResults`, `ReviewLedger`, `ControlTotals`, `EvidenceProvenance`, `ProcessQA`.

## Transaction Monitoring Scenario Design

| Authored file | Prose/table words | Complete UTF-8 bytes |
| --- | ---: | ---: |
| [01-session-guide.md](../suites/scenario-design/01-session-guide.md) | 1,355 | 9,817 |
| [02-inputs-evidence.md](../suites/scenario-design/02-inputs-evidence.md) | 2,058 | 14,829 |
| [03-analysis-method.md](../suites/scenario-design/03-analysis-method.md) | 2,188 | 15,609 |
| [04-decision-rules.md](../suites/scenario-design/04-decision-rules.md) | 2,647 | 17,815 |
| [05-output-contract.md](../suites/scenario-design/05-output-contract.md) | 4,145 | 53,614 |
| [09-quality-review.md](../suites/scenario-design/09-quality-review.md) | 2,097 | 14,372 |
| [10-worked-example.md](../suites/scenario-design/10-worked-example.md) | 3,988 | 31,359 |

Domain registers: `EventLedger`, `PredicateSpec`, `WindowResults`, `DeliveryDecisions`, `AccountCoverage`, `AcceptanceTests`, `EvidenceProvenance`, `ProcessQA`.

## Transaction Monitoring Data Lineage

| Authored file | Prose/table words | Complete UTF-8 bytes |
| --- | ---: | ---: |
| [01-session-guide.md](../suites/tm-data-lineage/01-session-guide.md) | 1,355 | 9,814 |
| [02-inputs-evidence.md](../suites/tm-data-lineage/02-inputs-evidence.md) | 2,115 | 15,331 |
| [03-analysis-method.md](../suites/tm-data-lineage/03-analysis-method.md) | 2,176 | 15,403 |
| [04-decision-rules.md](../suites/tm-data-lineage/04-decision-rules.md) | 2,645 | 17,945 |
| [05-output-contract.md](../suites/tm-data-lineage/05-output-contract.md) | 4,767 | 61,648 |
| [09-quality-review.md](../suites/tm-data-lineage/09-quality-review.md) | 2,126 | 14,618 |
| [10-worked-example.md](../suites/tm-data-lineage/10-worked-example.md) | 4,860 | 39,965 |

Domain registers: `SourceRows`, `FieldMappings`, `LineageLedger`, `CanonicalOutput`, `StageControls`, `RunImpact`, `ExceptionRegister`, `EvidenceProvenance`, `ProcessQA`.

## Monitoring Scenario and Threshold Review

| Authored file | Prose/table words | Complete UTF-8 bytes |
| --- | ---: | ---: |
| [01-session-guide.md](../suites/monitoring-tuning/01-session-guide.md) | 1,961 | 13,353 |
| [02-inputs-evidence.md](../suites/monitoring-tuning/02-inputs-evidence.md) | 1,842 | 14,031 |
| [03-analysis-method.md](../suites/monitoring-tuning/03-analysis-method.md) | 1,949 | 13,411 |
| [04-decision-rules.md](../suites/monitoring-tuning/04-decision-rules.md) | 1,573 | 10,868 |
| [05-output-contract.md](../suites/monitoring-tuning/05-output-contract.md) | 2,362 | 33,763 |
| [09-quality-review.md](../suites/monitoring-tuning/09-quality-review.md) | 3,132 | 21,781 |
| [10-worked-example.md](../suites/monitoring-tuning/10-worked-example.md) | 10,128 | 67,316 |

Domain registers: `Population`, `Candidates`, `CandidateMetrics`, `AlertRouting`, `BelowThreshold`, `CandidateDecisions`, `EvidenceProvenance`, `ProcessQA`.

## Monitoring System Independent Challenge and Validation

| Authored file | Prose/table words | Complete UTF-8 bytes |
| --- | ---: | ---: |
| [01-session-guide.md](../suites/monitoring-validation/01-session-guide.md) | 1,943 | 13,319 |
| [02-inputs-evidence.md](../suites/monitoring-validation/02-inputs-evidence.md) | 1,725 | 13,304 |
| [03-analysis-method.md](../suites/monitoring-validation/03-analysis-method.md) | 3,302 | 23,148 |
| [04-decision-rules.md](../suites/monitoring-validation/04-decision-rules.md) | 1,564 | 11,273 |
| [05-output-contract.md](../suites/monitoring-validation/05-output-contract.md) | 2,009 | 29,499 |
| [09-quality-review.md](../suites/monitoring-validation/09-quality-review.md) | 2,863 | 20,356 |
| [10-worked-example.md](../suites/monitoring-validation/10-worked-example.md) | 6,749 | 48,013 |

Domain registers: `ComponentInventory`, `ChallengeTests`, `OutcomeUnits`, `OutcomeMetrics`, `IssueRegister`, `EvidenceProvenance`, `ProcessQA`, `ReleaseGates`.

## Historical Monitoring Lookback and Remediation Review

| Authored file | Prose/table words | Complete UTF-8 bytes |
| --- | ---: | ---: |
| [01-session-guide.md](../suites/lookback-review/01-session-guide.md) | 1,923 | 13,160 |
| [02-inputs-evidence.md](../suites/lookback-review/02-inputs-evidence.md) | 1,775 | 13,740 |
| [03-analysis-method.md](../suites/lookback-review/03-analysis-method.md) | 1,723 | 12,458 |
| [04-decision-rules.md](../suites/lookback-review/04-decision-rules.md) | 1,526 | 10,999 |
| [05-output-contract.md](../suites/lookback-review/05-output-contract.md) | 2,425 | 38,749 |
| [09-quality-review.md](../suites/lookback-review/09-quality-review.md) | 2,999 | 21,272 |
| [10-worked-example.md](../suites/lookback-review/10-worked-example.md) | 11,029 | 89,490 |

Domain registers: `PeriodReconciliation`, `CanonicalUnits`, `RetrievalLedger`, `ReviewActions`, `ExpansionDecisions`, `EvidenceProvenance`, `ProcessQA`, `CompletionGates`, `ComparisonPackets`, `DefectChronology`.

## Investigation Case Review

| Authored file | Prose/table words | Complete UTF-8 bytes |
| --- | ---: | ---: |
| [01-session-guide.md](../suites/investigations/01-session-guide.md) | 1,791 | 12,625 |
| [02-inputs-evidence.md](../suites/investigations/02-inputs-evidence.md) | 3,029 | 22,282 |
| [03-analysis-method.md](../suites/investigations/03-analysis-method.md) | 2,572 | 18,459 |
| [04-decision-rules.md](../suites/investigations/04-decision-rules.md) | 1,384 | 9,743 |
| [05-output-contract.md](../suites/investigations/05-output-contract.md) | 2,035 | 30,384 |
| [09-quality-review.md](../suites/investigations/09-quality-review.md) | 3,410 | 23,624 |
| [10-worked-example.md](../suites/investigations/10-worked-example.md) | 6,229 | 43,860 |

Domain registers: `CaseTimeline`, `AccountBalances`, `ClaimTests`, `Contradictions`, `EvidenceRequests`, `EvidenceProvenance`, `DecisionRecord`, `ProcessQA`.

## Network and Funds Flow Review

| Authored file | Prose/table words | Complete UTF-8 bytes |
| --- | ---: | ---: |
| [01-session-guide.md](../suites/network-flow-review/01-session-guide.md) | 1,788 | 12,643 |
| [02-inputs-evidence.md](../suites/network-flow-review/02-inputs-evidence.md) | 2,935 | 21,056 |
| [03-analysis-method.md](../suites/network-flow-review/03-analysis-method.md) | 2,566 | 18,314 |
| [04-decision-rules.md](../suites/network-flow-review/04-decision-rules.md) | 1,381 | 9,679 |
| [05-output-contract.md](../suites/network-flow-review/05-output-contract.md) | 2,036 | 31,209 |
| [09-quality-review.md](../suites/network-flow-review/09-quality-review.md) | 3,359 | 23,355 |
| [10-worked-example.md](../suites/network-flow-review/10-worked-example.md) | 6,167 | 44,479 |

Domain registers: `Nodes`, `EconomicEdges`, `BalanceChecks`, `PatternTests`, `AllocationBounds`, `AttributionScenarios`, `DecisionRecord`, `ProcessQA`.

## Alert Adjudication Quality Review

| Authored file | Prose/table words | Complete UTF-8 bytes |
| --- | ---: | ---: |
| [01-session-guide.md](../suites/alert-qa/01-session-guide.md) | 1,782 | 12,627 |
| [02-inputs-evidence.md](../suites/alert-qa/02-inputs-evidence.md) | 3,444 | 25,486 |
| [03-analysis-method.md](../suites/alert-qa/03-analysis-method.md) | 2,722 | 19,584 |
| [04-decision-rules.md](../suites/alert-qa/04-decision-rules.md) | 1,315 | 9,528 |
| [05-output-contract.md](../suites/alert-qa/05-output-contract.md) | 1,984 | 28,962 |
| [09-quality-review.md](../suites/alert-qa/09-quality-review.md) | 3,277 | 22,849 |
| [10-worked-example.md](../suites/alert-qa/10-worked-example.md) | 6,083 | 45,364 |

Domain registers: `CasePackets`, `ReviewVotes`, `QualityCriteria`, `DefectRegister`, `Calibration`, `Remediation`, `DecisionRecord`, `ProcessQA`.
