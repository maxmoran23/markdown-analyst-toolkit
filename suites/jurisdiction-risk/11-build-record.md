# Jurisdiction Risk and Exposure Review — build record

Version 1.1.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 16,603 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 149,550 | Sum of files 01–10 |
| Characters | 149,462 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 37,366 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 29,893–49,821 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 149,464–373,660 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `6048bb1088c4033caf6cbdeaf525af873b5e940301077f020940dda2ce2c3b7f` |
| `02-inputs-evidence.md` | `ab566168899bcfe8efc7b11c8b2dd13bfa76a6dfb0f3e02e48e7e870ae0ded34` |
| `03-analysis-method.md` | `26c6468c19ddab2f8f0af67566d62b0f115d075616417d041175822dcaa106dd` |
| `04-decision-rules.md` | `c23afc8ac37583c3cc264bd2b0ee17d20277ee1ac92ad84d9924fbe7104d760a` |
| `05-output-contract.md` | `47c235f52e9f737ac8a0a3eeb92af3bb2976d892d67a54d6cd3ef4e90fc44edf` |
| `06-report-template.md` | `8f4be9a2a2f83b09f4cf7997edb4ad6a86eadf4cfefd9267e2e47acea58a8e95` |
| `07-workbook-template.md` | `0a46442cdb4eeaa1fbed3c21673918fadd414614269174ba32968e21cbef253f` |
| `08-dashboard-template.md` | `f0a60a137a48eceb2fd4ca8938a567e508b4caa5eefbe58c683fbcb0162f47c4` |
| `09-quality-review.md` | `c9f7cc796308cfb906b999d8319deae2be62311b4d8de832fc9344c61e877cc6` |
| `10-worked-example.md` | `45edd4fe719484cedb92ac1d8b75666e54f3c315ab7b3a88ef8da142744eef97` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
