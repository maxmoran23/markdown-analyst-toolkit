# Sampling Design and Assurance Review — build record

Version 1.1.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 17,614 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 151,444 | Sum of files 01–10 |
| Characters | 151,354 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 37,839 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 30,271–50,452 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 151,356–378,390 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `275efe279d62dfa6f10d8fc0de61b4692e9c79e9640d21091e851dea19ffec7c` |
| `02-inputs-evidence.md` | `b25490d054606c315852ff31fa92b8ad4ee7ae97cc56ba3d23ff8961fe032ba1` |
| `03-analysis-method.md` | `144eaa9b003db1a0df2b4015814b18a07b3bfad66369efd18862fda9c40e2995` |
| `04-decision-rules.md` | `0f8a8752ca4919c3f7983970d3d462708905254cd8a3ecf671ce05ba081d9b71` |
| `05-output-contract.md` | `c7ca095024b5456dc98433b3c737c46d18707884af2026ff07a5910db269984f` |
| `06-report-template.md` | `5f2bf06e3dd713f4059ab10c9545ee54b7e44bf1c9ca533bb96e5cbd205dcc91` |
| `07-workbook-template.md` | `3bc91af13720db2ac3e6bf3e8bd9f09acfd6cdd77fe2b66307efdec506b6b033` |
| `08-dashboard-template.md` | `7d06de7d0d7d2f3bf3b24898cea1d123496022c1ff25d8ee3aaf7a839d42f5cc` |
| `09-quality-review.md` | `3b1c4523216103f41233909bf74fe452540ebfdc8663e3f6f0312a6bbf36883d` |
| `10-worked-example.md` | `2b8930a001492f0d25499209e340f8847b093e76e51fec3f3e188cecec4e326f` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
