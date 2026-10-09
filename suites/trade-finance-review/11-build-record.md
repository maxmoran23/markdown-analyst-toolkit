# Trade Finance Review — build record

Version 1.1.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 19,074 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 165,146 | Sum of files 01–10 |
| Characters | 165,042 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 41,261 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 33,009–55,014 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 165,044–412,610 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `2482964dafc6f0cb0f2f5292c38618b752f341ac62ea88ea75f90a0a4c60d334` |
| `02-inputs-evidence.md` | `267f4f160d28b79d9f3439a5a4f16ea2a1c57feefc4bf24ee93a65f1af78d9a7` |
| `03-analysis-method.md` | `e09484d2eb96ac0174a2fef70ebeb33a3cdce32d420f38a3faf8638e25c79790` |
| `04-decision-rules.md` | `c6edd1e793269896aa11c968f1cd68d030c672a20a183f19a926f6d619adcdeb` |
| `05-output-contract.md` | `994bd55c005c57c9ac4a295d908cf5784aa7c28bc282bc29177a3e03519de152` |
| `06-report-template.md` | `527025a197f5333a5bf4c96638405cff557521caf3997503721855511aed4b6d` |
| `07-workbook-template.md` | `d897681511b98c25366cb4dd6cdfb032d0441a2092698e36879a98f3d3674d26` |
| `08-dashboard-template.md` | `1773939039cf9f31830506951ab08724363a08315fc7dc4c163976ed9e600a8c` |
| `09-quality-review.md` | `598d305079e42003947c5db688d05f3381a353ea0a9b0b04a6f3e4b444c81a34` |
| `10-worked-example.md` | `b45133915215dbfdb9c4b59340600404f43a55e1e3c6bd910091d868a11fc0b1` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
