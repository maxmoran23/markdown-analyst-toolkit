# Sanctions Review — build record

Version 1.0.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 14,060 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 122,066 | Sum of files 01–10 |
| Characters | 121,995 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 30,499 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 24,399–40,665 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 121,996–304,990 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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

Stage order describes the workflow, not a fabricated hourly timeline. A listed acceptance test is not evidence it passed. See [release verification](https://github.com/maxmoran23/markdown-analyst-toolkit/blob/v1.0.0/docs/VERIFICATION.md) for checks actually performed and limits, including lack of testing in an enterprise Copilot tenant.

## Instructional file integrity

| File | SHA-256 |
| --- | --- |
| `01-session-guide.md` | `091f3c7ef69da6e820238bfd5cf692e7ef0ff2442692e8a5d26a5f1007ea7de7` |
| `02-inputs-evidence.md` | `0c2138c8e2bf523c51598d5ee4dda35fe6c00432c5d2bb63f96ea10b36923e0b` |
| `03-analysis-method.md` | `95431d5ab0d1b7e16840ea5be715f89d52df01016fa66f938a25ff6d06d2c934` |
| `04-decision-rules.md` | `4cca41e65549b95fba5e67f324f7a3913bf9ea0eba0f3d8c425989a91b889399` |
| `05-output-contract.md` | `91bf0f00f0d5a7776c20d9e0982de8107d4621d4210dce22f8ebf9fe3125ee37` |
| `06-report-template.md` | `79f677cce0b2ec9bc201c0a1eb304c6eed02b061285a46fac61b1711c236fa8c` |
| `07-workbook-template.md` | `b407a524c9e91dd29815644fb3b8d363f224ad43d5f1bbb45c975e89ef7a7d1a` |
| `08-dashboard-template.md` | `7c192584b145a26f23ae0d8491b55b929e30324e0d43418675f817fa1b6b5ad9` |
| `09-quality-review.md` | `bd17d3521bf1961738be1bc561e88fc125ac8474fc12d1c23dc8328629481437` |
| `10-worked-example.md` | `65958a2769f8495fe011919d6436dbbe3d5f637126d19265ab13e230c54e295d` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
