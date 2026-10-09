# Transaction Monitoring Review — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 50,262 | Whitespace-separated tokens, including code |
| Authored method prose | 20,639 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 184,952 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 10 registers / 61 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 432,305 | Sum of files 01–10 |
| Characters | 432,037 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 108,010 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 86,408–144,013 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 432,040–1,080,100 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `0a8c505eb90abbc48a3ce57fbc457e1cfed85e5103ae7e71cf9c3a8c848bdb6b` |
| `02-inputs-evidence.md` | `3619b96ce262b955d68eb2bd476b5a22f2a1230179f62a31f12754e9a48bbbd7` |
| `03-analysis-method.md` | `6924ceb513d00505e18ccb72bb62887caed484249dc1cc58d2f66d86e1108117` |
| `04-decision-rules.md` | `3d259790bc3902aba255bf2960ae97d42430f2c7b667a66d8ce0620c21db0815` |
| `05-output-contract.md` | `bb6e5fe2daedc79d28e0ab6ec5dd4841b16f77fedb9bf95e434377f42b35211c` |
| `06-report-template.md` | `8a3705ce6f7b27cdfd4ae78be6a77c0a18065f6d795b67884fcb02acc3fe4ab3` |
| `07-workbook-template.md` | `e486edab10e412a2e444269d2a1db59dd47721493e3dfde0af7b281641fae88c` |
| `08-dashboard-template.md` | `a1e8edabe208b9635f41b2197cd7460d32273a514f3e0d5336a162c6d7a4119e` |
| `09-quality-review.md` | `f23866d516e96700e0065b8601b39d492e3d58b28b529ca74a41f029bd8961aa` |
| `10-worked-example.md` | `c4b1ed384671546c830d69a3830fbeea0328059b6c0e21ddc011aa4e1cc6537e` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
