# Regulatory Change and Obligation Mapping — build record

Version 1.0.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 13,975 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 121,944 | Sum of files 01–10 |
| Characters | 121,862 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 30,466 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 24,373–40,621 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 121,864–304,660 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `1800ff724cdea4678c6559af2e9a875d99f01fab92955880801b4c9a648e96e6` |
| `02-inputs-evidence.md` | `645801372266952ed5268a433e6aa7ae36c1677a1ecbca4fa7fedc3890317f76` |
| `03-analysis-method.md` | `a80f88d95e3b63b69c676949efd3639bf95479d3e6eb1bb8b59e465cf5a9482f` |
| `04-decision-rules.md` | `ea8fe5a214a8489c69bf31ad2e4cee5cc97d9fd9bd34de90014118fed5bc1912` |
| `05-output-contract.md` | `5a7dc9af3660fc7966f269e1542b4f3211289c9a5294b6b9a962363a4c35ee4d` |
| `06-report-template.md` | `60324afb7cbb106f8dcac0fb0493e63ac8c05aa49d0c7ddacf83eb9eb51fb7ef` |
| `07-workbook-template.md` | `76803e0964dc29f92527fa7f2f5ee84947f0773f6faa58a31ee7cec394e67f22` |
| `08-dashboard-template.md` | `0296581200d06d02f41ba9ac3e1d22fb85dd73a4b13597b4ca7b0107e2421c86` |
| `09-quality-review.md` | `dc6a30052065069750feedfb6effb3d112e5641ac80f500f119502f40b45e186` |
| `10-worked-example.md` | `26526cfb3c5773b407b0c1ed7f48bb696279b07b92eef464294a2bdf3f31d646` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
