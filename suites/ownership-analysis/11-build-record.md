# Ownership Analysis — build record

Version 1.1.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 16,288 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 144,158 | Sum of files 01–10 |
| Characters | 144,084 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 36,021 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 28,817–48,028 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 144,084–360,210 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `515ac35d65be8716feb11cefd26a12168f51fb887239047e089d39cabd469287` |
| `02-inputs-evidence.md` | `4dc136a7f1654a6c5b8cdbdbd557b5966a265619edc04638c5b79cf8314345d6` |
| `03-analysis-method.md` | `1d87ff744a31606d1e5ddf9175a99b5fbc9031e9b91ac0333dcb0ad8d8d77c4c` |
| `04-decision-rules.md` | `3541692a87e2f227cd19d657aa290efe98271ccf93e7b4261b20acdec2b5214f` |
| `05-output-contract.md` | `7dec5e608a41363706c10ea668dccaa99a5c9bb96a3fe900ed76e9e926d1eeb3` |
| `06-report-template.md` | `07b7faf7383b62f7f60745a2751470363ce09f0d8f988f21aebcdbe1bcc885a8` |
| `07-workbook-template.md` | `87fec4d11c55001f2a3f4ad76183d514b9794d307472e694663bdff28492cead` |
| `08-dashboard-template.md` | `3cf1413ca18881d19bfb728fb5c17afad0026641ea80844ad2ade36909ac3383` |
| `09-quality-review.md` | `48f38535296c86375a66ea45a36773a1a9fc707fedd5d15906e255f1421f8012` |
| `10-worked-example.md` | `f3d0275bb6c6efebae23e489c5f5d96dc2d99aa84dfe9d85345f238f3c1bc8a4` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
