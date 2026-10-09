# Trade Surveillance Review — build record

Version 1.0.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 15,115 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 128,904 | Sum of files 01–10 |
| Characters | 128,828 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 32,207 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 25,766–42,943 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 128,828–322,070 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `31945fef9e5dead1c86f0eddb895b9d934c057cc1493f4b5546d5cb5533517ea` |
| `02-inputs-evidence.md` | `a60cf7e97940d116829619350798442a3fe3d37c780034612bf29ca0578bb20f` |
| `03-analysis-method.md` | `f7963e7c9a1b20f4130c12acbba9999a3a2f5bdf55725c1495722eb40d615b90` |
| `04-decision-rules.md` | `9e29df4668c117f4cbd8df5579bffa045a556e335624c0d4ab73044a3342d3ca` |
| `05-output-contract.md` | `c0963ba5fdde3f604024ad3c1efdc9039a1cc25a869bf2265916672c89dfbb44` |
| `06-report-template.md` | `0cc3ac606dbec843895bf39188248194e7ab79044e9a55a042456238bbf4600c` |
| `07-workbook-template.md` | `1a29f0b5e31608931aa7178417f0d05745c2ee252dea82f45e02a918324f8c93` |
| `08-dashboard-template.md` | `9011c28cc148bcc3ffe3e99891f2f04351b9b98828b0411cb6831ef4993cb857` |
| `09-quality-review.md` | `618a4143babb5c3a57a605f8bde386f647fb47d8f849a7298a0992f40e80ee8e` |
| `10-worked-example.md` | `4627241f1876ea817f7bd0fb00263b85b045a2bc81b8875ef72add191f9e2b74` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
