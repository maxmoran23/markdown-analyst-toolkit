# Third-Party Service and Assurance Review — build record

Version 1.1.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 15,621 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 140,760 | Sum of files 01–10 |
| Characters | 140,708 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 35,177 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 28,142–46,903 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 140,708–351,770 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `2d62cb460163ca6079931c7f4062a33febc1f673019eca860e1098106086a0ba` |
| `02-inputs-evidence.md` | `61332edef806b46e4f0d5395238c9edc358f2ac6a50f67ba7b6fa8e3ebafd20d` |
| `03-analysis-method.md` | `a4d2adc6d646e9ac6828bd6a05e49758b3e88f033e6e219b24e2eb1adcb79282` |
| `04-decision-rules.md` | `2a971d76f12dbf4009872aed4d383583b0955247467b7712a055ea977b3678d7` |
| `05-output-contract.md` | `51875af56f22bd16a94a566a4204fb9bf091d163ebab4009e7631f377ccbec52` |
| `06-report-template.md` | `094334c1a59e306aa80d1e2ebb3ae6e7543ef93609cf1423d8d5b9dea5630841` |
| `07-workbook-template.md` | `b03853c875cb9bd4bcc64a8c70e8615c52d3290738438909f63a881a02378840` |
| `08-dashboard-template.md` | `05ddea03ccd31167d379facba9ba6c4880254899673cefc51f6d0e477d058e32` |
| `09-quality-review.md` | `268e338aed0112523aa5a45c78e9a4307a2cfa68e0303d7eabaf235c9ac0c0b0` |
| `10-worked-example.md` | `b840bb35ca4631fcb97117113b101a43035e48d26c442f17da207a9c7f123798` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
