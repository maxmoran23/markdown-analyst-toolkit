# Investigation Case Review — build record

Version 1.1.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 15,659 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 140,088 | Sum of files 01–10 |
| Characters | 140,020 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 35,005 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 28,004–46,674 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 140,020–350,050 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `f3e920aadbc09053f4c1d82e88f69e66068008cffd7d76bb920c1343398287c9` |
| `02-inputs-evidence.md` | `7cf804e46ac79ceab36bddf93cef84f1ab2d9d6679380256daeb8327ad76fece` |
| `03-analysis-method.md` | `dc119d5315b88fb291b822ca5619d8dda735e2f27ead87b8fd53d425738f9188` |
| `04-decision-rules.md` | `5871fd8b468e5e822e788902b6a49887edd9eaa33442a40970703eab65267919` |
| `05-output-contract.md` | `5806a2f05c39b95263c0b2276c0abbe481fb699ef7b354d58d1a13ba185f4693` |
| `06-report-template.md` | `834299ebe0c318db51a0243bbb919856ae6e69a53d18ee104963be19a08b2bd4` |
| `07-workbook-template.md` | `052682a5c7eee6a749e0530a3d11837e7f0b06ee490fb95cfbfe1c7007513ac9` |
| `08-dashboard-template.md` | `07f7b45aa41b921df82f26a26179e7e54bda564f90cf8bace4ea8fcb2a17e27a` |
| `09-quality-review.md` | `c9cb24c72f59191c7d177ede8b12c80ef75e41a1e7de1ebdb65cffed2836cb45` |
| `10-worked-example.md` | `7fc528f601146bb70e93ed96050a2f6153bac1c8169b6ee6b00aff5ad29f0c02` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
