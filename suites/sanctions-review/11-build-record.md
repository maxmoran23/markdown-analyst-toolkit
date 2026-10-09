# Sanctions Review — build record

Version 1.1.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 15,680 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 140,594 | Sum of files 01–10 |
| Characters | 140,523 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 35,131 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 28,105–46,841 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 140,524–351,310 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `091f3c7ef69da6e820238bfd5cf692e7ef0ff2442692e8a5d26a5f1007ea7de7` |
| `02-inputs-evidence.md` | `0c2138c8e2bf523c51598d5ee4dda35fe6c00432c5d2bb63f96ea10b36923e0b` |
| `03-analysis-method.md` | `95431d5ab0d1b7e16840ea5be715f89d52df01016fa66f938a25ff6d06d2c934` |
| `04-decision-rules.md` | `4cca41e65549b95fba5e67f324f7a3913bf9ea0eba0f3d8c425989a91b889399` |
| `05-output-contract.md` | `91bf0f00f0d5a7776c20d9e0982de8107d4621d4210dce22f8ebf9fe3125ee37` |
| `06-report-template.md` | `535643c50a5be068df43c5649748038ad68c13dc66649c34fc36c77961442a05` |
| `07-workbook-template.md` | `38002e549b9912774f8448d8425d419c0699716da4608e705d65a238632045a0` |
| `08-dashboard-template.md` | `564d855f10bdef657e6f32d50a64abddc81a8d42cd40fa7bce58cd15e45d3c5c` |
| `09-quality-review.md` | `bd17d3521bf1961738be1bc561e88fc125ac8474fc12d1c23dc8328629481437` |
| `10-worked-example.md` | `65958a2769f8495fe011919d6436dbbe3d5f637126d19265ab13e230c54e295d` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
