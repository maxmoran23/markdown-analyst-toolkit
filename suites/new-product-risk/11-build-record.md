# New Product Risk and Launch Readiness — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 17,640 | Whitespace-separated tokens, including code |
| Authored method prose | 6,536 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 44,934 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 2 registers / 11 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 169,738 | Sum of files 01–10 |
| Characters | 169,686 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 42,422 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 33,938–56,562 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 169,688–424,220 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `dad56b562747a4305a543fe18147ded96011398d5290426e926042b6d31507cc` |
| `02-inputs-evidence.md` | `744f3187302694ae6b545079db17de112ed7290d0bc88a30548505fafbf97bfb` |
| `03-analysis-method.md` | `b1c3409c5fbb76a099a044ed7f8ee52c88fbf6142ada367b7cb040ef63c81866` |
| `04-decision-rules.md` | `f96b2d29c0f7bec3083adac7ea2f2359c4e2979c38ee1881027ec10bfced9976` |
| `05-output-contract.md` | `e190a2a34ac0b096c6335ff040e2c7616da36b6a74b73139b2c9da33c565960e` |
| `06-report-template.md` | `15e5934caef8b7a8390916b3aa13339b2aed5102b209870d9473c8a2f352e2bf` |
| `07-workbook-template.md` | `95d5b9d872b80ee58aa4747390ba0bd672fee0c5fd2d399d3ef52a877f9e0548` |
| `08-dashboard-template.md` | `42de78483566609f8cf034d7faaf93daa658fd29c789a6b28ea20dc399a617b6` |
| `09-quality-review.md` | `93a7a78c6995c94dd951f9102f1b1e5ccdec2da8a8be81a2d867f2f0231a53d9` |
| `10-worked-example.md` | `0fefa82be0f0f2e65839bc4ffdaaba79ee2854b44c5f9b7d523820e1b2a5e15d` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
