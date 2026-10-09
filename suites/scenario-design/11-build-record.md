# Transaction Monitoring Scenario Design — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 42,724 | Whitespace-separated tokens, including code |
| Authored method prose | 18,478 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 157,415 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 8 registers / 55 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 367,601 | Sum of files 01–10 |
| Characters | 367,405 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 91,852 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 73,481–122,469 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 367,408–918,520 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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

Stage order describes the workflow, not a fabricated hourly timeline. A listed acceptance test is not evidence it passed. See [release verification](https://github.com/maxmoran23/markdown-analyst-toolkit/blob/v1.2.0/docs/VERIFICATION.md) for checks actually performed and limits, including lack of testing in an enterprise Copilot tenant.

## Instructional file integrity

| File | SHA-256 |
| --- | --- |
| `01-session-guide.md` | `96e52d35d720924d41093a494bda151614aab9b3ec50c0beb7afb5b6a69fb16e` |
| `02-inputs-evidence.md` | `e50f3f2d39799f3c3fcde56ea8d50dc3783837fcd5450cdb10b9a1e452da7442` |
| `03-analysis-method.md` | `385181f4897e0c39ab223d0b5e9f677430f464566a3d25c58a63e434f5a494d0` |
| `04-decision-rules.md` | `4492d5702534e21c8225c4a34ed9c370ac51ce4c53b39cf1c30d3fea861ceaf5` |
| `05-output-contract.md` | `1f5b6334f0e0e83207764f8f90d718d124e19c8904f64846909669f6a2945a57` |
| `06-report-template.md` | `3c752dcec53425930c19967354c11c3609f3b6a119acec9c5d2698c60c2d75ea` |
| `07-workbook-template.md` | `1b126d2dd9c761b68e76dc32a7a8259f68ac178bce2769448e62200bf6a8a3ff` |
| `08-dashboard-template.md` | `1d34ec05b94dcf3d0642f6c5a1250acfe624f1416734ff29bb2aa7dc551a1fe8` |
| `09-quality-review.md` | `d5c5e42ca8f98aa8bb946e49b7b866e1da749555113b0c20bed4416accf8e21a` |
| `10-worked-example.md` | `d21d29f342401632498cdf158087af9c23fba5eb83d937011f03cf255c831e24` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
