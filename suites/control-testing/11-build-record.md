# Control Testing and Evidence Review — build record

Version 1.0.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 13,927 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 117,603 | Sum of files 01–10 |
| Characters | 117,549 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 29,388 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 23,510–39,183 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 117,552–293,880 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `66458832434b2eb0c25858c6193662302186bbef41c236ec6b206fcf6a4232d3` |
| `02-inputs-evidence.md` | `2a580f7d440a69fdd9d6bfe1230b18f530cd6bfaa2c3f37b84a0ef0d7dd8fffc` |
| `03-analysis-method.md` | `ad628cc92a90386e64acaeca1db5110bd7566f6491dd6373e9a16dcdf2e51b51` |
| `04-decision-rules.md` | `61ced018ffd087fc3485d17c9d158453003c5a04947d3e5cda02e0636ea8e673` |
| `05-output-contract.md` | `6427a7f9ce6b792b1934f0ef3d1a78f6a6eaa460695707e5f266877630b20068` |
| `06-report-template.md` | `8f4fd456d75167a7bca71aac67d540940212d815eb764471516dff8e2cadeaf1` |
| `07-workbook-template.md` | `7c44a05012c9c6eee4bb7c950ce4971646c1cfaa6c3c14e8c07fea8eebc85c51` |
| `08-dashboard-template.md` | `454f1f1f7030629d56c6bc21913de1f63210a2a21726427b58b8efc5b5e90921` |
| `09-quality-review.md` | `b4e8547cb12880f58751f99c382f260e323164d79e0f3b50d23856b81b981ff7` |
| `10-worked-example.md` | `b4c4cb69e6db42101d4dc2670f11493c0cb1745f1b39183940d9b1f2b70123f7` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
