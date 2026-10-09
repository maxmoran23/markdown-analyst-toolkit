# Digital Asset Review — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 18,118 | Whitespace-separated tokens, including code |
| Authored method prose | 6,866 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 46,930 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 2 registers / 9 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 173,570 | Sum of files 01–10 |
| Characters | 173,526 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 43,382 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 34,706–57,842 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 173,528–433,820 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `4225bb77885566fd377f20ecfd92daf306cf2628c7c02cb9b1a64f59ee8ab64e` |
| `02-inputs-evidence.md` | `25ab825e259098cf81ec5433c8ff7669e9c8e8e3a9eb60bef173fd6902767fa3` |
| `03-analysis-method.md` | `9af8936fd6beda2a2c26c45f4fb368ab10f743507f662a5ecab3efffe5fad9f4` |
| `04-decision-rules.md` | `f6e37b200b350cd48b8a48b496e4705950390b37fffe63ee0fd66f76804135c6` |
| `05-output-contract.md` | `5f3dc6f76440f676e418189a746da73eb4b6b14e794af8fb423ff314a1a76797` |
| `06-report-template.md` | `2d1c80e2f13ae9848b341fd2950c01847734973d024a1e593dea468bdb9a0226` |
| `07-workbook-template.md` | `ef970139f2fe6d84f320fafdb7f447e8d71d60c6f9c8a8de4d274c481c930ed2` |
| `08-dashboard-template.md` | `e4a6a0386e3a906f62c1df1764188ad3bbbbe100d3810ae4dc2d666d35b8ceaa` |
| `09-quality-review.md` | `7b9f46ee1bcaddb1167c9a6f85dfdd422581ac95c619d076b346370186adb66e` |
| `10-worked-example.md` | `2cbc0948462e7f6dfc7fe1e804a4a3b8ddcd1395b2f1eb00175874e2a587d607` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
