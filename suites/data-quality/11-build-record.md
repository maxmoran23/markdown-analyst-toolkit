# Data Quality and Fitness for Use — build record

Version 1.1.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 15,295 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 134,663 | Sum of files 01–10 |
| Characters | 134,605 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 33,652 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 26,921–44,869 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 134,608–336,520 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
| Actual authoring/reasoning/input tokens | Not available | No complete per-suite generation telemetry captured |
| Actual monetary build cost | Not available | No token billing attribution or assumed model price |
| Elapsed effort | Not attributed per suite | Parallel authoring and shared template work overlap |

The build-budget range is intentionally an estimate of resources one might reserve to reproduce the workflow, not a claim about tokens spent on this release. It cannot establish value, model quality or elapsed human labor. The attachment estimate excludes your data, conversation history and generated answer. Reserve room for all three. A file-count limit does not imply the content fits a model's context or was fully attended to.

## Creation sequence

| Stage | Work performed | Evidence available |
| --- | --- | --- |
| 1. Scope | Mapped the specialist task to existing public toolkit methods | Root coverage map and suite README |
| 2. Method | Authored inputs, method, decision rules and exceptions | Files 01–04 |
| 3. Contract | Fixed field names, narrative roles and deliverable layouts | Files 05–08 |
| 4. Case | Added a complete fictional example with expected results and edge cases | File 10 and maintainer catalog |
| 5. Review | Defined falsifiable analytical and delivery checks | File 09; actual release checks are listed in the root verification record |
| 6. Package | Measured files, embedded renderers and created checksummed bundles | This record, release assets and root verification record |

Stage order describes the workflow, not a fabricated hourly timeline. A listed acceptance test is not evidence it passed. See [release verification](https://github.com/maxmoran23/markdown-analyst-toolkit/blob/v1.1.0/docs/VERIFICATION.md) for checks actually performed and limits, including lack of testing in an enterprise Copilot tenant.

## Instructional file integrity

| File | SHA-256 |
| --- | --- |
| `01-session-guide.md` | `7b4fefd568b9ce9aad8e9d96e9efb527fe14f9ca09d5e19f75317d345d8be079` |
| `02-inputs-evidence.md` | `213ca8ccc9ca87acaedc1491cc73aadc0183792981f719c16ca22ce58779f7fd` |
| `03-analysis-method.md` | `a3cc1744b44eceb138c401ac3aeb5ca786bc7c8e90ad357b26f09cbb48ff8ceb` |
| `04-decision-rules.md` | `be0f33bc0ebe1e95294e7206b6ba643917d5ee845146f0d32afca347343090fd` |
| `05-output-contract.md` | `b15ca6c76a08f368b504c03a42aaf8816bb48713a1891a50e88cd6339aaf54e5` |
| `06-report-template.md` | `ecb69d9906b536e0d80ea40d266efbe90eca770d734d077c4ab93538582247f3` |
| `07-workbook-template.md` | `ba78a0af52dbd2d76926379b7280454bc28815c43ce0c725eb9eb3285e55fa5a` |
| `08-dashboard-template.md` | `ba8bafdd19b372895cc71d58f5b84194382ba23a820923455adee953de011eea` |
| `09-quality-review.md` | `fa7d1af92fa9062ad166b1a2dde0283578b84f13ea5934fa76a75871d6fdca86` |
| `10-worked-example.md` | `e14210d4d45b4adbe93f877b0c0efb5ebb271926a86631e962c11f263ad56902` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
