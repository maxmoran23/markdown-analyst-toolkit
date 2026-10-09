# Transaction Monitoring Data Lineage — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 48,094 | Whitespace-separated tokens, including code |
| Authored method prose | 20,044 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 174,724 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 9 registers / 74 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 411,015 | Sum of files 01–10 |
| Characters | 410,795 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 102,699 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 82,159–136,932 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 410,796–1,026,990 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `ba2623a2e6d73e8a8a2501a9c9cdb21caffb3c0bcdc5e2ee4ea10b41a704a3c0` |
| `02-inputs-evidence.md` | `d3e53818b8d5b6dd254a5fd0b8f3b4d15832e039b614c02cf0ad299c79987050` |
| `03-analysis-method.md` | `f23de1e5731a260d6ddc770fc8345b5db35214106adcaffcb5019a4ecfe2bff3` |
| `04-decision-rules.md` | `03b58263b7a17c119dde726f4080c093d86757e127b72fb3094a8b7c517d4384` |
| `05-output-contract.md` | `67c1c517d844b27af8b8e2b1ea925c0a1e84e23f32d7133b078f1cf139e49e83` |
| `06-report-template.md` | `7ebc9eb377bb397f55a26632c4ed196c4e952414a1549ab64068e8f473f8a6b2` |
| `07-workbook-template.md` | `29c9d46617667147d3c26f6ac617e28e948cdce1026b4057da9df2a22c70b6ef` |
| `08-dashboard-template.md` | `ecdb3a8f4899b8dacf3781e8948f047fa5bd4d42d3cfe6ccc4da2020806de91f` |
| `09-quality-review.md` | `41609211beb0dfded7b6c61e82c506e96e92335ad21004363c9f3f063c55a413` |
| `10-worked-example.md` | `81ad582fffc1111e7aa033b80826c7b1d53196b5f55b8e06ab6a0ad30d9e5eb7` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
