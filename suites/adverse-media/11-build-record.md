# Adverse Media — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 19,055 | Whitespace-separated tokens, including code |
| Authored method prose | 6,971 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 48,882 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 2 registers / 13 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 182,933 | Sum of files 01–10 |
| Characters | 182,886 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 45,722 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 36,578–60,962 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 182,888–457,220 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `fe225db9a992cb6686423db504f619d00181eb7f538689d31c7a8fd533a3fabb` |
| `02-inputs-evidence.md` | `b481b38432947bfae76b3290b019bd86787dfbf086b461ab8dc28510188df35f` |
| `03-analysis-method.md` | `8f9bd8c151aa9ebdb4af61ed3fdf210af2d5b4dd6e95305af50c404d1524f956` |
| `04-decision-rules.md` | `deec37c422ccb1245d799e2de082218b1e19842d4218c6827186e9ccf62c8e71` |
| `05-output-contract.md` | `146585bfb9dcf054b979e519f247342f7c5851adff80073233e0e2090593643d` |
| `06-report-template.md` | `b42633580b336bb823450b8993ac09236ac66850b822ac99c674e368194f0381` |
| `07-workbook-template.md` | `8f815a993d52891011329115e84ce561d34037b3513bd53748474a7a6ac9aa1f` |
| `08-dashboard-template.md` | `136a57709ca59572ec70c0d9f035055135ceaae4b64b9f3180bde5a42b474d57` |
| `09-quality-review.md` | `86748af18c73bb45539a5646406cd5e65d44ea8e3bf4801b987ca3416a264d17` |
| `10-worked-example.md` | `fdbc8163ff3522dbd9f9de652871fce4e3a3d91e8076036d4c5f3263c027aed9` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
