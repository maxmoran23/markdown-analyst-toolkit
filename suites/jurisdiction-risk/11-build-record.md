# Jurisdiction Risk and Exposure Review — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 18,887 | Whitespace-separated tokens, including code |
| Authored method prose | 7,335 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 50,137 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 2 registers / 12 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 181,719 | Sum of files 01–10 |
| Characters | 181,631 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 45,408 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 36,327–60,544 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 181,632–454,080 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `6048bb1088c4033caf6cbdeaf525af873b5e940301077f020940dda2ce2c3b7f` |
| `02-inputs-evidence.md` | `ab566168899bcfe8efc7b11c8b2dd13bfa76a6dfb0f3e02e48e7e870ae0ded34` |
| `03-analysis-method.md` | `26c6468c19ddab2f8f0af67566d62b0f115d075616417d041175822dcaa106dd` |
| `04-decision-rules.md` | `c23afc8ac37583c3cc264bd2b0ee17d20277ee1ac92ad84d9924fbe7104d760a` |
| `05-output-contract.md` | `47c235f52e9f737ac8a0a3eeb92af3bb2976d892d67a54d6cd3ef4e90fc44edf` |
| `06-report-template.md` | `c73c97786911ff11303f8e694ebd9e6a53ade6d3c1f0637ebf7d0bf6dfc48066` |
| `07-workbook-template.md` | `e3216dde68bb34f92df2688bb1f100bb2dc84353c9b9be726d98bee029ce08f1` |
| `08-dashboard-template.md` | `906df4c7144c53a730a4fed93ecc1cd85169212297c1fd715c36529e3837187c` |
| `09-quality-review.md` | `c9f7cc796308cfb906b999d8319deae2be62311b4d8de832fc9344c61e877cc6` |
| `10-worked-example.md` | `45edd4fe719484cedb92ac1d8b75666e54f3c315ab7b3a88ef8da142744eef97` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
