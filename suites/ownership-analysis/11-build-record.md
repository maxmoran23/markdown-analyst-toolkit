# Ownership Analysis — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 18,572 | Whitespace-separated tokens, including code |
| Authored method prose | 7,234 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 49,828 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 2 registers / 10 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 176,327 | Sum of files 01–10 |
| Characters | 176,253 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 44,064 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 35,251–58,751 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 176,256–440,640 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `515ac35d65be8716feb11cefd26a12168f51fb887239047e089d39cabd469287` |
| `02-inputs-evidence.md` | `4dc136a7f1654a6c5b8cdbdbd557b5966a265619edc04638c5b79cf8314345d6` |
| `03-analysis-method.md` | `1d87ff744a31606d1e5ddf9175a99b5fbc9031e9b91ac0333dcb0ad8d8d77c4c` |
| `04-decision-rules.md` | `3541692a87e2f227cd19d657aa290efe98271ccf93e7b4261b20acdec2b5214f` |
| `05-output-contract.md` | `7dec5e608a41363706c10ea668dccaa99a5c9bb96a3fe900ed76e9e926d1eeb3` |
| `06-report-template.md` | `017520abc60055cf17474ed0b787d2aa7472611ac09d51010212ee8cf0170b67` |
| `07-workbook-template.md` | `04285a388cb051995047c5978ea7e25ef403d4ade191804ff760fb9db3be483c` |
| `08-dashboard-template.md` | `e3f3f4f9fb39c315b5e6b27f4455df6c95a91c3da581728e1f99183a0f9887f7` |
| `09-quality-review.md` | `48f38535296c86375a66ea45a36773a1a9fc707fedd5d15906e255f1421f8012` |
| `10-worked-example.md` | `f3d0275bb6c6efebae23e489c5f5d96dc2d99aa84dfe9d85345f238f3c1bc8a4` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
