# Customer Risk Review — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 20,050 | Whitespace-separated tokens, including code |
| Authored method prose | 7,538 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 50,414 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 2 registers / 36 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 189,546 | Sum of files 01–10 |
| Characters | 189,463 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 47,366 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 37,893–63,155 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 189,464–473,660 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `c72f3fc72038038dbbeb5e387e7b9edf542040b876b49c0931ed45b4a141bacb` |
| `02-inputs-evidence.md` | `04542f2e24988892c583a5ddaf7984e129a1b50e7c0e3cae53565aec29690238` |
| `03-analysis-method.md` | `579ab4f3f682ed743ba49df948e8709012a6be323dfd701b82b5deb8558f83f8` |
| `04-decision-rules.md` | `f8f6c16a6519be028baea702e6f0eb45ab14ae9367a67d8afbb199c0a4b6ed7e` |
| `05-output-contract.md` | `d71de3ba341df8d00a7f7ec40def603dcb74b85a2c3c500c64e03cffdcc736d9` |
| `06-report-template.md` | `99ea244a8a665851a7ea76258dc34148a3f4de131d8e9e979ba3a8ee2f2ac4b9` |
| `07-workbook-template.md` | `ec46745ed78a533d26b1af4d46cac0913130222ec79a4a94f3d4495e6f156aa7` |
| `08-dashboard-template.md` | `3b9cd997efb5038d6416a75bb7a09e58b51258d10168733beee1a9092a1177e2` |
| `09-quality-review.md` | `2380145b2f244109d593a9c0fd2e0f8fa1582e225e0e9091ef3c8d2b2a8058f5` |
| `10-worked-example.md` | `3119ee53958f5912ada65acf036e40532891d4bd1afa76ee91d53b93ceef28bd` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
