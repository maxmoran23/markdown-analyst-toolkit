# Trade Surveillance Review — build record

Version 1.1.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 16,735 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 147,432 | Sum of files 01–10 |
| Characters | 147,356 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 36,839 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 29,472–49,119 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 147,356–368,390 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `31945fef9e5dead1c86f0eddb895b9d934c057cc1493f4b5546d5cb5533517ea` |
| `02-inputs-evidence.md` | `a60cf7e97940d116829619350798442a3fe3d37c780034612bf29ca0578bb20f` |
| `03-analysis-method.md` | `f7963e7c9a1b20f4130c12acbba9999a3a2f5bdf55725c1495722eb40d615b90` |
| `04-decision-rules.md` | `9e29df4668c117f4cbd8df5579bffa045a556e335624c0d4ab73044a3342d3ca` |
| `05-output-contract.md` | `c0963ba5fdde3f604024ad3c1efdc9039a1cc25a869bf2265916672c89dfbb44` |
| `06-report-template.md` | `8133101e802e44c019976e45c368f9c9f6e60abf0ef6de84e9f905ffe20912ae` |
| `07-workbook-template.md` | `95a8b5c5d5a831c72a9290fdfa592ef61f3c5d7f4c8351ea9b89a6a4965b7cea` |
| `08-dashboard-template.md` | `a42fbc281d6ea391e995cd8592e03dc3ce83f8537a5e9fdae05b17378c97b7d4` |
| `09-quality-review.md` | `618a4143babb5c3a57a605f8bde386f647fb47d8f849a7298a0992f40e80ee8e` |
| `10-worked-example.md` | `4627241f1876ea817f7bd0fb00263b85b045a2bc81b8875ef72add191f9e2b74` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
