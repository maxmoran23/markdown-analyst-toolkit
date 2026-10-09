# Entity Due Diligence — build record

Version 1.1.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 15,411 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 140,412 | Sum of files 01–10 |
| Characters | 140,356 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 35,089 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 28,072–46,786 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 140,356–350,890 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `2a9a12366a3ec4a1152a4f97c9853bd351d2a6a9eaf3fac51cfd8821bde35d53` |
| `02-inputs-evidence.md` | `a8f21aa47e78c9baa9c156e3c03d9f4b638781434b56fad2b1db1f40acb24dbd` |
| `03-analysis-method.md` | `aa1b21686dfccdc795d98309ff7739c459ef1fe23c56b6c1ae672b83deae3aa8` |
| `04-decision-rules.md` | `081404c4a0690478709a57083a007c5c44026d2834f100b250ca2c54a6270dbc` |
| `05-output-contract.md` | `c042bfb8c18bdcfb50e055235f247e4bb96f5b932f8a48c8c05112eb46742601` |
| `06-report-template.md` | `848a3b6974b7f7c093e798bd31fa34f5e3ea30877576d9517481611b441f2759` |
| `07-workbook-template.md` | `06a99036646d49ac9dcfd65a42930be1a84a201f2c27dbdb14323663c2c67923` |
| `08-dashboard-template.md` | `919831544e8b85fea9282bb204342f0c339ae0f2e3e1a40a1828a2ef2554693e` |
| `09-quality-review.md` | `43b36717ebb57fa949d7e0377290c21fa92e741a335253f8717e230d055b6adf` |
| `10-worked-example.md` | `8b1df959ad2ab40e5e8945d629818a91d774feec7506c99331644507be0121ff` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
