# Correspondent Banking — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 19,897 | Whitespace-separated tokens, including code |
| Authored method prose | 7,758 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 54,432 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 2 registers / 14 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 189,551 | Sum of files 01–10 |
| Characters | 189,505 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 47,377 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 37,901–63,169 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 189,508–473,770 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `5c0971ad381f05a1f9db2e4dbd1bf71d93760a0f45f3d4410de09e42a4f37ab8` |
| `02-inputs-evidence.md` | `505609ab33cbcd0c7f35d61c360423833ac5706ba33d8d78c228eea070887d9f` |
| `03-analysis-method.md` | `e54667b3cbc751d7fd4ec4a44031cd0f920b615ab670d71bd8feb27ab318cc71` |
| `04-decision-rules.md` | `614da35ac03a605345da25d10bb0d6e651363468f38c3e13c616ae7ae843c744` |
| `05-output-contract.md` | `c83e08725e14a3c3330156435e36697ac6d0ab3ff04c0acc63576998e0c7ef6d` |
| `06-report-template.md` | `a9e312bd6ec8744b2df3469f901a43215a956c98e78cabae56896b197e40cc9b` |
| `07-workbook-template.md` | `8ebbf7f64aff57adb26934a08ddbe50fa67642d8a856b1fab1aef2788701043f` |
| `08-dashboard-template.md` | `1e0b365d1e8b3a85eead00372086f08df2f6f59a9d04889e67ab105cea401a04` |
| `09-quality-review.md` | `649b8af1bd66fc0baffc827914519ddee6a598bfe3e460a8a97488b296825341` |
| `10-worked-example.md` | `404a15c51288a88418ecd385df8f19906892723e314c6cba99de57fb2ee73574` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
