# OSINT Research — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 17,540 | Whitespace-separated tokens, including code |
| Authored method prose | 6,401 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 44,015 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 2 registers / 9 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 167,170 | Sum of files 01–10 |
| Characters | 167,053 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 41,764 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 33,411–55,685 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 167,056–417,640 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `40ac517b87131ca509fc97bdb116fb02780239a448ccdb9f46aa1c619a8b3377` |
| `02-inputs-evidence.md` | `7e04b72cc8077d9aa843f811bf02c683439e3d53e12ac3e8631a4ef487e8fdc1` |
| `03-analysis-method.md` | `645133850e5dfd7d03aeb810b8e1e1030463876f2ab520db6ef98c55e059bcee` |
| `04-decision-rules.md` | `3e755b3c6d9bc9fe31ffc6b2f6163aefc07e2f178bd4bd7a681f5b79b99c328c` |
| `05-output-contract.md` | `35c0f304e2ef2dcce1250835a294bb7581404f8e43166cb3982ee74369b77349` |
| `06-report-template.md` | `d7f2ddffa8bbaa16394a7d547010e477b502cb7fdb5b32eb5a45588b6db27461` |
| `07-workbook-template.md` | `6399dfc741dd45c600f2dc49f5a8542428eade63ef210a4bad658b4cd4186265` |
| `08-dashboard-template.md` | `2372d64439bf8ad3aa788bc7d29c055a495146090ef2223309675ce6459d55a4` |
| `09-quality-review.md` | `9bd1940be665fa6dd383e124481124b094085dee2bb2d0bf4e80dc11273ec2f0` |
| `10-worked-example.md` | `14fadea72cad18f057a502f4df92a33ed1f748ae8940c2fbec012fc496d852b9` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
