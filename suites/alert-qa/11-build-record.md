# Alert Adjudication Quality Review — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 43,184 | Whitespace-separated tokens, including code |
| Authored method prose | 20,607 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 164,400 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 8 registers / 84 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 374,219 | Sum of files 01–10 |
| Characters | 373,898 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 93,475 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 74,780–124,633 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 373,900–934,750 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `f1b3644d7d800dde2960465a8b1e356f83cdc97c6a5cc7cf05bc1abdc081d8b8` |
| `02-inputs-evidence.md` | `14182fb55d7d7d18fe848bd72b7fb7f23b8312c971f62cd0e2ff01ab58d96091` |
| `03-analysis-method.md` | `8adf4a53ea5b8ca8518f60a50476d883f8c28642c0a81f537cdb1a7f0ec98425` |
| `04-decision-rules.md` | `1bf4ea160978b2f5f5c3e4a06f54bf624a5666e8910a91b5a078c6b42ec3787a` |
| `05-output-contract.md` | `82981c67dd0efec3bf7b697c162833233bf472b88f8a728cc8ec0685a6686200` |
| `06-report-template.md` | `8afc602ebd716f2697cf2d18f78d4950c7df2400b89990053beaf9a32d7f5c76` |
| `07-workbook-template.md` | `4fba91f83ca675569593fe8db2a5651330897650cf1dfb019c8caa927afc786b` |
| `08-dashboard-template.md` | `0daf3246836861238ed5091a1109f3779eb0c1d2ae069f52c231fe6f6454c5d1` |
| `09-quality-review.md` | `a4a5d3d598e90acf8631bfe2d536e6b9911a0c17877c3399b7e8dad965a87839` |
| `10-worked-example.md` | `b084eef96d8c9db9c66fd6afdb271ee50b454d9dcea01df8348c0fc32d9a8de8` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
