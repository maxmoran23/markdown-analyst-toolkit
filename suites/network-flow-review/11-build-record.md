# Network and Funds Flow Review — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 41,966 | Whitespace-separated tokens, including code |
| Authored method prose | 20,232 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 160,735 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 8 registers / 65 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 359,824 | Sum of files 01–10 |
| Characters | 359,372 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 89,843 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 71,875–119,791 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 359,372–898,430 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `231923681c56f341d42fcd406df3db4e2e5aca3f2985281d957540219f21044d` |
| `02-inputs-evidence.md` | `fb7972f6e45af96d5b141f78e58e7fbd428db6c1a25aa185c477fb774bfb189f` |
| `03-analysis-method.md` | `179375dd56763c35a566ffb2c83a7ccd380721a3d1334fea910f25eccfb0ddf1` |
| `04-decision-rules.md` | `c51d2eaea188082496ed822f95d70177c58e406e3655410d804710f6d52941cc` |
| `05-output-contract.md` | `3a557ffdaa4ac3296df5dc8f0d6cc1b3ae4716d9d74195b820681d09167b1069` |
| `06-report-template.md` | `9ec398ee111ac0f98fa778d74fe6b0381eb3de0c5920c232b8bfb4f97dc13cd3` |
| `07-workbook-template.md` | `2c625f9b4e6ac97855e6ecfef50508fb47129267f176ddaf58da90a452c2162c` |
| `08-dashboard-template.md` | `07def599fb6d93328c05b090eeb23704f36a661421ecc28affac81d1e8e17a74` |
| `09-quality-review.md` | `b57244bd158b3262749250030de980e997a79feebd78cce10c764bead560fbca` |
| `10-worked-example.md` | `dbaff5ea15bce7953fd57eefb797d3cc46e575ab5aa9ae965a5e7e76bd9e8676` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
