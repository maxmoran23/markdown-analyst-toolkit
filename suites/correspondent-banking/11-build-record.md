# Correspondent Banking — build record

Version 1.1.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 17,613 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 157,382 | Sum of files 01–10 |
| Characters | 157,336 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 39,334 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 31,468–52,446 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 157,336–393,340 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `5c0971ad381f05a1f9db2e4dbd1bf71d93760a0f45f3d4410de09e42a4f37ab8` |
| `02-inputs-evidence.md` | `505609ab33cbcd0c7f35d61c360423833ac5706ba33d8d78c228eea070887d9f` |
| `03-analysis-method.md` | `e54667b3cbc751d7fd4ec4a44031cd0f920b615ab670d71bd8feb27ab318cc71` |
| `04-decision-rules.md` | `614da35ac03a605345da25d10bb0d6e651363468f38c3e13c616ae7ae843c744` |
| `05-output-contract.md` | `c83e08725e14a3c3330156435e36697ac6d0ab3ff04c0acc63576998e0c7ef6d` |
| `06-report-template.md` | `5d5461f5bc9b8d3e281906663d32964ad4f6380c91c2f578e8c4bfddfd5a1f45` |
| `07-workbook-template.md` | `888f6bd8f579661d12e1e144f59f04f366d73883dda8c71f6358eb11c13da0df` |
| `08-dashboard-template.md` | `5a7f09ced49497124ed7907827cd84f0bd671f493b7a39e8cc1702ebdb0354da` |
| `09-quality-review.md` | `649b8af1bd66fc0baffc827914519ddee6a598bfe3e460a8a97488b296825341` |
| `10-worked-example.md` | `404a15c51288a88418ecd385df8f19906892723e314c6cba99de57fb2ee73574` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
