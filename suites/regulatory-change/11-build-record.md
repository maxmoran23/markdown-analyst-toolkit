# Regulatory Change and Obligation Mapping — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 17,879 | Whitespace-separated tokens, including code |
| Authored method prose | 6,677 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 46,206 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 2 registers / 11 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 172,641 | Sum of files 01–10 |
| Characters | 172,559 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 43,140 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 34,512–57,520 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 172,560–431,400 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `1800ff724cdea4678c6559af2e9a875d99f01fab92955880801b4c9a648e96e6` |
| `02-inputs-evidence.md` | `645801372266952ed5268a433e6aa7ae36c1677a1ecbca4fa7fedc3890317f76` |
| `03-analysis-method.md` | `a80f88d95e3b63b69c676949efd3639bf95479d3e6eb1bb8b59e465cf5a9482f` |
| `04-decision-rules.md` | `ea8fe5a214a8489c69bf31ad2e4cee5cc97d9fd9bd34de90014118fed5bc1912` |
| `05-output-contract.md` | `5a7dc9af3660fc7966f269e1542b4f3211289c9a5294b6b9a962363a4c35ee4d` |
| `06-report-template.md` | `4a1442cfeca20e42dabbaa8c5b0a3fc73e6b7fe5c4fb8445583b2b626905f56d` |
| `07-workbook-template.md` | `1a1245857411c4aeded3f149ba166d1286e78af041025d1ee27b05bf98ce1d59` |
| `08-dashboard-template.md` | `f565b73479f933cbafb0b583bc64b7ca44c5cf598de7081c1e77a4aacd1edfb2` |
| `09-quality-review.md` | `dc6a30052065069750feedfb6effb3d112e5641ac80f500f119502f40b45e186` |
| `10-worked-example.md` | `26526cfb3c5773b407b0c1ed7f48bb696279b07b92eef464294a2bdf3f31d646` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
