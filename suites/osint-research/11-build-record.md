# OSINT Research — build record

Version 1.1.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 15,256 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 135,001 | Sum of files 01–10 |
| Characters | 134,884 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 33,721 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 26,977–44,962 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 134,884–337,210 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `40ac517b87131ca509fc97bdb116fb02780239a448ccdb9f46aa1c619a8b3377` |
| `02-inputs-evidence.md` | `7e04b72cc8077d9aa843f811bf02c683439e3d53e12ac3e8631a4ef487e8fdc1` |
| `03-analysis-method.md` | `645133850e5dfd7d03aeb810b8e1e1030463876f2ab520db6ef98c55e059bcee` |
| `04-decision-rules.md` | `3e755b3c6d9bc9fe31ffc6b2f6163aefc07e2f178bd4bd7a681f5b79b99c328c` |
| `05-output-contract.md` | `35c0f304e2ef2dcce1250835a294bb7581404f8e43166cb3982ee74369b77349` |
| `06-report-template.md` | `40c4f04fe938e3493d4ca77939c6e321629655f35158044320085c893557f55c` |
| `07-workbook-template.md` | `7b2d6c65f2ea8b472fe5c3232d7aac88a6ee9ef4bd133f14d5d9b724c7f1e665` |
| `08-dashboard-template.md` | `4d2b1a57dc043ba09e8f02aa99624eb4d4669f86fc05e04fab0275d414b4e442` |
| `09-quality-review.md` | `9bd1940be665fa6dd383e124481124b094085dee2bb2d0bf4e80dc11273ec2f0` |
| `10-worked-example.md` | `14fadea72cad18f057a502f4df92a33ed1f748ae8940c2fbec012fc496d852b9` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
