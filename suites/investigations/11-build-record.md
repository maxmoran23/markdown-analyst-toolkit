# Investigation Case Review — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 42,912 | Whitespace-separated tokens, including code |
| Authored method prose | 20,450 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 160,977 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 8 registers / 69 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 371,362 | Sum of files 01–10 |
| Characters | 370,966 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 92,742 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 74,194–123,656 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 370,968–927,420 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `376d5304039d58ccc1d058efa5619532ad122c2068e6ca5a2c4d89581e9bef29` |
| `02-inputs-evidence.md` | `4b2b7c23829576e3243ffe3a65e2c5facf2e59bab73500784d7b1458ff27e299` |
| `03-analysis-method.md` | `011b9aec7e8e5afb0030b301fabb4b987bac7110698e72bc327f16f563c4e934` |
| `04-decision-rules.md` | `0fbbccf408816dd58cbe9d61be27cd5e48a8a0dc416c48d58191f524259a37a2` |
| `05-output-contract.md` | `d49210952454a367fe88dde99681223df5945ab4de9339dac64cbc5c6dea8cbb` |
| `06-report-template.md` | `32afa524384bf72bdbc9e75dffd37bbfc919a2de945baa68c5938152ae4dd6f6` |
| `07-workbook-template.md` | `8b4418c80db42413ae7c745fcffbe4f83fa9f3c608f77a054208f490594b39d6` |
| `08-dashboard-template.md` | `7486c5b860fb58af3700c266bb4683c8265ef11a7bb0c39707fe5765c2f68b26` |
| `09-quality-review.md` | `4c6b50f14f00f4e581c801c2e223f0ab69166af73a15ba1c5bd6b78ae30a9bd3` |
| `10-worked-example.md` | `5b4412629f781edfff59ea7f58ae4e866b0c7f0ed0e2490e54c1f57423661207` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
