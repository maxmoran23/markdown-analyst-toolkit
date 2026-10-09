# Typology and Red-Flag Review — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 17,963 | Whitespace-separated tokens, including code |
| Authored method prose | 6,561 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 45,491 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 2 registers / 9 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 171,622 | Sum of files 01–10 |
| Characters | 171,522 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 42,881 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 34,305–57,174 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 171,524–428,810 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `9a02f3cf34a2a4d4c1ff39da958a6f233a413d55b4c82929f5bc5ccfa7f1eac9` |
| `02-inputs-evidence.md` | `3197fffac6ae4e80ab5920154d6c656deece7e4e863ed0fd3138d54bd2b6da36` |
| `03-analysis-method.md` | `19026c7c2cc8f20e86d74c4de0e331d10baf191fe519704f4273e9eb6c9c45d8` |
| `04-decision-rules.md` | `c5158465406093a7adba14f6b3bc7a89d20e6c96a354a69fc862f521821d7b78` |
| `05-output-contract.md` | `539ff1c972e7fbeef97d95327e274913c499e401eb384faf96a72da9d70fc6d3` |
| `06-report-template.md` | `8000caf0560c20b9f3e45044d14fd9c253171b52f580abc26ec758d4ff2b65c7` |
| `07-workbook-template.md` | `34650151b01f985ed9d40ff074ae3859fbe374076aa2e71ef4888b1e4c289cc7` |
| `08-dashboard-template.md` | `3a1a96efb5ca4226002319ec98ae9965311d91dd45a9dd358c02d45b11523174` |
| `09-quality-review.md` | `20ab399003f3dd0425c8616fcdc32b448bc66b8214ac9959cf7d87685ff828d6` |
| `10-worked-example.md` | `4b1dc5d6addcfe7f30a784fb265381f5090f24b87784c05e59f2a443c21d244e` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
