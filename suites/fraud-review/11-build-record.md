# Fraud Incident Review — build record

Version 1.1.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 16,404 | Whitespace-separated tokens, including code |
| UTF-8 bytes | 147,765 | Sum of files 01–10 |
| Characters | 147,685 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 36,922 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 29,537–49,229 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 147,688–369,220 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `4b340eeac02818a0730da502befe62ff66c11693804e9168dcf2f299a0f9e30e` |
| `02-inputs-evidence.md` | `2e9410cb14435a9f6440ab09e89ceee80663fb4e498f1478c7a46c2dc5045fdb` |
| `03-analysis-method.md` | `119bd26f9c0fb972701130edd7d22d3827312db64c12b4dc5e2544af0b288eba` |
| `04-decision-rules.md` | `6995a5d24eeafdae000c9268b5b701e1c578c3d98a371de5e17ccaf671f6f5cc` |
| `05-output-contract.md` | `aee727bab2d1cf2813a3393d7681679b15fbba863557474a1c8c95a48e2706cb` |
| `06-report-template.md` | `d288a7fb9ae9e52f88b09664b382f3406d0e261e00d9bd4a0bc6cc916ac0bf22` |
| `07-workbook-template.md` | `d7e03cceee878019709cc0ee4cd56b6f8ba334da941b469308082f6c02a99371` |
| `08-dashboard-template.md` | `2bbc67db93f092914ba1ca4b18ed7ae670c3ef74a9c8e81d9fc3d5b3016c1947` |
| `09-quality-review.md` | `7df34200e17cfaf298bb355b0ba01bb52bae84a91027a921ae6f039d9c7acbd9` |
| `10-worked-example.md` | `c1187a77a166d7f7953ee6361b3f8aad1e63a03675beb3576b198d2353642ea5` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
